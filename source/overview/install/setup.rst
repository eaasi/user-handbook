.. Setup

.. _setup:

Setup and Deployment
=====================

Production deployment uses Ansible for setting up and configuring a server for EaaSI deployment.

.. _eaasi-installer: https://gitlab.com/eaasi/eaasi-installer
.. _eaasi-ansible: https://gitlab.com/eaasi/eaasi-ansible


System Requirements
---------------------

Hardware Requirements
^^^^^^^^^^^^^^^^^^^^^^

- A VM or physical machine for the EaaSI gateway (*target* machine).

- Minimal/testing:

  - 8-core AMD64 CPU
  - 16 GB RAM
  - 10 GB free disk space for the EaaSI system
  - an additional 100+ GB disk space for resources (Environments, Software, Content), mounted to local file system

- Recommended:

  - 12-core AMD64 CPU
  - 24 GB RAM
  - 10 GB free disk space for the EaaSI system
  - an additional 300+ GB disk space for resources
  - For VM deployments, support for "Nested KVM"/nested virtualization on the host machine (see :ref:`enable-kvm`)
  
    - If deploying in the cloud, Azure and GCloud VMs should offer this feature out-of-the-box (GCloud users must acknolwedge that the feature is still technically in "beta" first).
    - AWS currently only offers nested virtualization support on its "bare metal" options.
  
- A *controller* machine to run the installation scripts. Typical desktop/laptop hardware is plenty. See below for software requirements.

 
Software Requirements
^^^^^^^^^^^^^^^^^^^^^^^

- A supported Linux operating system should be installed on the *target* machine:

  - Ubuntu 16.04
  - Ubuntu 18.04
  - CentOS 7
  
- A ``python`` interpreter on the *target* machine (this should usually be handled automatically on the supported Linux distributions listed above)

- `Docker <https://docs.docker.com/get-docker/>`_ must be installed on the *controller* machine. (Installation of Docker and Docker-Compose on the *target* machine will be automatically handled by the installer, if they are not already present). Please consult Docker's official documentation to install Docker and Docker Compose on the controller machine before proceeding to installation.


Target Machine Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- SSH access to the *target* machine with ``sudo`` or root capabilities. Please make sure the target machine user does not need a password to use sudo.

- EaaSI (as of v2020.03) requires access from the *target* machine to a SMTP mail server, to handle delivery of user passwords. Either a third-party service (MailGun, SendGrid, AWS, Gmail) or a local option (e.g. a university's mailing system) should work. Please contact your appropriate IT representative if necessary to obtain the ``mailer`` variables listed in :ref:`configuring-eaasi-installer`.

- Certain emulators, such as SheepShaver, require mapping to low memory addresses, which may be disabled by SELinux. If SELinux is enabled, allow mapping low memory addresses by running ``sudo setsebool -P mmap_low_allowed 1`` on the *target* machine.

- Make sure that the Docker user has write permission to shared folders.

- The Docker user must have read/write permissions to ``/dev/kvm`` for :ref:`KVM <enable-kvm>`/nested virtualization support for Environments to work properly.

- In order to interact and exchange resources with the EaaSI Network, the *target* machine must be configured at a publicly addressable IP and able to accept HTTP requests.

- EaaSI specifically retrieves resources from the EaaSI Network via HTTPS, so the machine must also be set up with a valid SSL certificate.


Assumptions
^^^^^^^^^^^

The current version of the EaaSI installer makes the following assumptions:

- The `eaasi-installer`_ depends on the `eaasi-ansible`_ repository, which is meant to be used as
  an EaaSI-specific Ansible library containing a collection of Ansible roles, Docker images and
  shell-scripts for deploying and configuring Emulation-as-a-Service servers. The installer
  repository should be viewed as an example for custom deployments. Over time both repositories
  will be extended and updated to support more deployment setups, based on feedback from users.

- The target machine will act as an all-in-one installation. This means the UI and several EaaS
  components will be installed and configured to run from that single machine.

  .. note::

     `eaasi-ansible`_ technically supports distributed deployment, consisting of a single gateway
     machine and multiple worker machines running emulation sessions. However, this is not yet
     fully documented and therefore not available in the current installer version.


Installation Procedure
-----------------------

The installation procedure consists of the following steps:

#. Setting up a controller-machine for running the Ansible-based installer. To minimize platform and
   version differences of required tools, multiple pre-configured Docker-containers will be built during
   this step. All tools will be run inside those containers to make the installation procedure more
   OS agnostic and reproducible. For more details, see :ref:`preparing-controller-machine`.

#. Configuring the installer by specifying the installation target machines and setting options for a
   customized EaaSI-deployment. For more details, see :ref:`configuring-eaasi-installer`.

#. Deploying EaaSI server (see :ref:`running-eaasi-installer`). Here, an Ansible playbook (with custom
   options from previous step) will be executed. The deployment process is basically composed of the
   following actions:

   - Preparing target machine, optionally installing Python, Docker and Docker-Compose
   - Downloading pre-built EaaS components from our CI-system
   - Downloading pre-built docker-image containing EaaS runtime
   - Generating deployment-specific EaaS configuration files
   - Starting EaaS container with generated configuration and downloaded components


.. _preparing-controller-machine:

Preparing Controller-Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, an Ansible controller-machine must be prepared. This controller-machine will coordinate the EaaSI
installation process and should preferably use a Linux operating system, but MacOS should also work.
To prepare the controller-machine execute the following steps:

- Clone the `eaasi-installer`_ repository into an empty directory. Make sure you have cloned the recommended branch for the current EaaSI release, e.g.:

  .. code-block:: sh

    $ git clone -b eaasi-release-2020.03 https://gitlab.com/eaasi/eaasi-installer

- Change into this directory and run:

  .. code-block:: sh

    $ ./scripts/prepare.sh

  This script will prepare the repository, build Docker images required for running the installer and generate
  an SSH key-pair for accessing the target machine. During that process you may be asked for ``sudo`` password,
  depending on your Docker installation.

- Copy the generated SSH public key to the installation target machine:

  .. code-block:: sh

    $ ssh-copy-id -i ./artifacts/ssh/admin.key user@hostname

  The username should match the remote user with sudo capabilities.

  .. note::

     If you want to use your own exisiting SSH key, then simply copy the public and private key-pair into the
     directory ``./artifacts/ssh`` and rename those keys to ``admin.key`` and ``admin.key.pub``. Please note,
     that symbolic links won't work, because Ansible will be executed in a docker-container, where host's
     symbolic links are not valid!


.. _configuring-eaasi-installer:

Configuring EaaSI-Installer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The target machines to install EaaSI on should be defined in a file ``./artifacts/config/hosts.yaml``.
You can use the provided template file for a basic configuration:

.. code-block:: sh

   $ cp ./config/hosts.yaml.template ./artifacts/config/hosts.yaml

Edit this file with a text editor to match your machine, for example:

.. literalinclude:: examples/hosts.yaml.template
   :language: yaml

Next the EaaSI deployment must be configured in a file ``./artifacts/config/eaasi.yaml``.
As a starting point, you can use the provided template file:

.. code-block:: sh

   $ cp ./config/eaasi.yaml.template ./artifacts/config/eaasi.yaml

Edit this file with a text editor. An example configuration can look as follows:

.. literalinclude:: examples/eaasi.yaml.template
   :language: yaml

All available configuration options are grouped into 4 sections: ``host``, ``docker``, ``eaas`` , ``portal``.

.. include:: installer-config.rst


.. _running-eaasi-installer:

Running EaaSI-Installer
^^^^^^^^^^^^^^^^^^^^^^^

When everything is configured, the installation process can be started by running:

.. code-block:: sh

   $ ./scripts/deploy.sh

It will take a while depending on your internet connection and target machine. When the installation process
is finished, you should be able to access EaaSI with a browser at the URL ``http://<hostname>`` (or ``https://<hostname>`` if SSL was properly enabled and configured)
The ``<hostname>`` should match the address of the target machine you specified in the ``hosts.yaml`` file.
When asked for login credentials, use the email you configured for the ``intial_user`` and the password ``eaasidemo1``.

.. warning::
  Again, we strongly recommend the initial user immediately reset their password upon successful login. This will also act as a test of the selected SMTP mailer configuration.
  

.. _updating-eaasi:

Updating EaaSI
---------------

To update a previously-existing EaaSI installation, first update the `eaasi-installer`_ by running its ``git-pull.sh``
script to match the most up-to-date release provided by the EaaSI team:

.. code-block:: sh

  $ ./git-pull.sh && ./git-pull.sh origin eaasi-release-2020.03

.. note::
  Running the ``git-pull.sh`` script twice, first without arguments, ensures that the script itself is up-to-date first, before fetching the current release branch.

The EaaSI configuration located in ``artifacts/config/eaasi.yaml`` must then be updated with the relevant git branch or tag on
certain lines as well, for the ``docker``, ``eaas`` and ``portal`` modules. For the most up-to-date release recommended by EaaSI staff, please use:

  - docker.image: ``eaas/eaas-appserver:eaasi-release-2019.11``
  - eaas.git_branch: ``eaasi-release-2019.11``
  - portal.git_branch: ``eaasi-release-2020.03``

Following these configuration changes, to update the various EaaSI components, run:

.. code-block:: sh

   $ ./scripts/update.sh [<component>...]

where ``<component>`` can be one of the following:

- ``ear``: to update EaaSI's server binary to the latest version
- ``docker-image``: to update runtime docker-image to the latest version
- ``ui``: to update the PortalMedia UI elements to the latest version  

Multiple components can be specified as a space-separated list. If called without any ``<component>``
arguments, then all components will be updated by default.

Updates are run selectively in this way due to the way Ansible works: most actions executed during the installation are
idempotent and can be repeated multiple times resulting in the same deployment state. This also means certain
operations (like downloading files) are skipped, if those files are already present on the target machine. Ansible
must be forced to omit the idempotency requirement for certain operations, to be able to update EaaSI's UI,
server binary and runtime docker-image.

Deployment Troubleshooting
----------------------------

If you encounter errors in deploying or updating to EaaSI release 2020.03-beta, the EaaSI team has created a :ref:`Deployment FAQ/troubleshooting <deploy_faq>` page with possible pitfalls and work-arounds encountered by the development team during testing. This may be of use when working in non-standard network environments in particular.

Please :ref:`file a ticket <bugs>` if continuing to encounter issues/errors during deployment or updating of your EaaSI node.


Browser Compatibility
----------------------

The EaaSI team recommends attempting to access the EaaSI UI using:

- Firefox (v. 65+, possibly a few older versions too)
- Chrome

All other current browsers - such as Safari or older (non-Chrome-based) versions of Microsoft Edge will work to some degree but are not well tested.

.. note:: Some browser extensions also may interfere with EaaSI functionality, including ad-blockers, popup-blockers or similar. If encountering unexpected behavior, please try disabling all browser extensions first.
