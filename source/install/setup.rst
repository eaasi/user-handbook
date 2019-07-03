.. Setup

Setup and Deployment
=====================

There are currently two supported methods for deployment of EaaSI: via an automated Ansible installer, or via manual
deployment of a pre-configured Docker container. Please consult the appropriate documentation depending on your
preferred method.


Ansible Deployment
------------------

This method uses Ansible for setting up and configuring a server for EaaSI deployment.

.. _eaasi-installer: https://gitlab.com/eaasi/eaasi-installer
.. _eaasi-ansible: https://gitlab.com/eaasi/eaasi-ansible


Preconditions
^^^^^^^^^^^^^^

- A VM or physical machine for the EaaSI gateway (installation target). The gateway machine can act as
  an all-in-one installation, ie include UI, emulator runtime and various archive implementations.
- A supported Linux operating system should be installed on the target machine. Currently Ubuntu 16.04,
  Ubuntu 18.04 and CentOS 7 distributions are supported.
- SSH access to this machine with ``sudo`` or root capabilities. Please make sure you do not need
  a password to use sudo.
- At least 10 GB of free disk space for a minimal EaaSI installation. Additional disk space is required
  to run emulators and store disk images.
- The installer requires a ``python`` interpreter to be installed on the target machine. This will be
  handled automatically on supported Linux distributions.

.. note::

   This method requires manual installation of Docker only on the controller-machine, see
   :ref:`Dependencies <docker_install_section>` for more information. Installation of Docker and
   Docker-Compose on target machines will be handled automatically by the installer, if they are
   not pre-installed there.


Assumptions
^^^^^^^^^^^

Current version of the installer makes the following assumptions:

- The `eaasi-installer`_ depends on the `eaasi-ansible`_ repository, which is meant to be used as
  an EaaSI-specific Ansible library containing a collection of Ansible roles, Docker images and
  shell-scripts for deploying and configuring Emulation-as-a-Service servers. The installer
  repository should be viewed as an example for custom deployments. Over time both repositories
  will be extended and updated to support more deployment setups, based on feedback from users.

- The target machine will act as an all-in-one installation. This means the UI and several EaaS
  components will be installed and configured to run from that single machine.

  .. note::

     `eaasi-ansible`_ already supports distributed deployment, consisting of a single gateway
     machine and multiple worker machines running emulation sessions. However, this is not yet
     fully documented and therefore not available in the current installer version.


Installation Procedure
^^^^^^^^^^^^^^^^^^^^^^

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

- Clone the `eaasi-installer`_ repository into an empty directory
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

All available configuration options are grouped into 4 sections: ``host``, ``docker``, ``ui`` and ``eaas``.

.. include:: installer-config.rst


.. _running-eaasi-installer:

Running EaaSI-Installer
^^^^^^^^^^^^^^^^^^^^^^^

When everything is configured, the installation process can be started by running:

.. code-block:: sh

   $ ./scripts/deploy.sh

It will take a while depending on your internet connection and target machine. When the installation process
is finished, you should be able to access the EaaSI-UI with a browser under the URL ``http://<hostname>``.
The ``<hostname>`` should match the address of the target machine you specified in the ``hosts.yaml`` file.
When asked for login credentials, the ``ui.http_auth.user`` and ``ui.http_auth.password`` you specified in
the ``eaasi.yaml`` file should be used.


.. _updating-eaasi:

Updating EaaSI
^^^^^^^^^^^^^^

To update a previously-existing EaaSI installation, first update the `eaasi-installer`_ by running its ``git-pull.sh``
script to match the new/updated tagged release provided by the EaaSI team, for example:

.. code-block:: sh

  $ git-pull.sh origin eaasi-release-072019

Where ``eaasi-release-072019`` should be replaced by the relevant tag provided.

The EaaSI configuration located in ``artifacts/config/eaasi.yaml`` must then be updated with the relevant tag on
certain lines as well; for example:

  - docker.image: "eaas/eaas-appserver:eaasi-release-072019"
  - eaas.git_branch: "eaasi-release-072019"
  - ui.git_branch: "eaasi-release-072019"

Following these configuration changes, to update the various EaaSI components, run:

.. code-block:: sh

   $ ./scripts/update.sh [<component>...]

where ``<component>`` can be one of the following:

- ``ui``: to update EaaSI's UI to the latest version
- ``ear``: to update EaaSI's server binary to the latest version
- ``docker-image``: to update runtime docker-image to the latest version

Multiple components can be specified as a space-separated list. If called without any ``<component>``
arguments, then all components will be updated by default.

Updates are run selectively in this way due to the way Ansible works: most actions executed during the installation are
idempotent and can be repeated multiple times resulting in the same deployment state. This also means, that certain
operations (like downloading files) are skipped, if those files are already present on the target machine. Ansible
must be forced to omit the idempotency requirement for certain operations, to be able to update EaaSI's UI,
server binary and runtime docker-image.


.. _container_setup:

Container Deployment
---------------------

.. note::

   This method requires installation of Docker before deployment.
   See :ref:`Dependencies <docker_install_section>` for more information.
