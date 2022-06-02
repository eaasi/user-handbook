.. Setup

.. _setup:

Setup and Deployment
=====================

Production deployment uses Ansible for setting up and configuring a server for EaaSI deployment.

.. _eaasi-installer: https://gitlab.com/eaasi/eaasi-installer
.. _eaasi-ansible: https://gitlab.com/eaasi/eaasi-ansible
.. _eaas-orgctl: https://gitlab.com/eaasi/eaas-orgctl


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

  - Ubuntu 18.04
  - Ubuntu 20.04
  - CentOS/RHEL 7

- A ``python`` interpreter on the *target* machine (this should usually be handled automatically on the supported Linux distributions listed above)

- `Docker <https://docs.docker.com/get-docker/>`_ must be installed on the *controller* machine. (Installation of Docker and Docker-Compose on the *target* machine will be automatically handled by the installer, if they are not already present). Please consult Docker's official documentation to install Docker and Docker Compose on the controller machine before proceeding to installation.


Target Machine Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- SSH access to the *target* machine with ``sudo`` or root capabilities. Please make sure the target machine user does not need a password to use sudo.

- Certain emulators, such as SheepShaver, require mapping to low memory addresses, which may be disabled by SELinux. If SELinux is enabled, allow mapping low memory addresses by running ``sudo setsebool -P mmap_low_allowed 1`` on the *target* machine.

- Make sure that the Docker user has write permission to shared folders.

- The Docker user must have read/write permissions to ``/dev/kvm`` for :ref:`KVM <enable-kvm>`/nested virtualization support for Environments to work properly.

- In order to interact and exchange resources with the EaaSI Network, the *target* machine must be configured at a publicly addressable IP and able to accept HTTP requests.

- EaaSI specifically retrieves resources from the EaaSI Network via HTTPS, so the machine must also be set up with a valid SSL certificate.



Installation Procedure
-----------------------

The installation procedure consists of the following steps:

#. Setting up a controller-machine for running the Ansible-based installer. To minimize platform and
   version differences of required tools, multiple pre-configured Docker-containers will be built during
   this step. All tools will be run inside those containers to make the installation procedure more
   OS agnostic and reproducible. For more details, see :ref:`preparing-controller-machine`.

#. Configuring the installer by specifying the installation target machine and setting options for your EaaSI deployment. For more details, see :ref:`configuring-eaasi-installer`.

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

- Clone the `eaasi-installer`_ repository into an empty directory:

  .. code-block:: sh

    $ git clone https://gitlab.com/eaasi/eaasi-installer

- Change into the ``eaasi-installer`` directory and check out the currently recommended release tag for the installer using the provided ``git-pull.sh`` script:

  .. code-block:: sh

    $ ./git-pull.sh origin v2021.10

- Then run:

  .. code-block:: sh

    $ ./scripts/prepare.sh

|  This script will prepare the repository, build Docker images required for running the installer and generate
|  an SSH key-pair for accessing the target machine. During that process you may be asked for your ``sudo`` password,
|  depending on your Docker installation.

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

Edit the ``hosts.yaml`` template to match the details of your target machine:

.. literalinclude:: examples/hosts.yaml.template
   :language: yaml

Next the EaaSI deployment must be configured in a file ``./artifacts/config/eaasi.yaml``.
As a starting point, you can use the provided template file:

.. code-block:: sh

   $ cp ./config/eaasi.yaml.template ./artifacts/config/eaasi.yaml

Edit this file with a text editor. An example configuration can look as follows:

.. literalinclude:: examples/eaasi.yaml.template
   :language: yaml

There are only two **required** (or recommended) edits that must be made before deployment: first is to set an ``admin_password`` for
the initial "superadmin" user (this is assumed to be the same person/user running the deployment; they
will have the option to set up and add additional users, including additional Admins, in the EaaSI UI
once deployed).

The second is to set a functional SSL configuration (disabling SSL may work but will likely cause unpredictable
behavior in the UI and is unsupported by the EaaSI team).

A *full-chain* certificate and public key (e.g. both `.crt` and `.key` components) must be provided for
the domain specified in `hosts.yaml`. Since the installer runs in a Docker container, the
certificate files must be placed or copied in the ``./artifacts`` directory before deployment
to be properly installed.

.. note::
  The EaaSI Installer has a number of advanced configuration options that are selected by default to optimize
  for support and compatibility between your installation and existing nodes in the EaaSI Network. Changing these options is not
  recommended or supported unless specifically directed by the EaaSI team.


.. _running-eaasi-installer:

Running EaaSI-Installer
^^^^^^^^^^^^^^^^^^^^^^^

When everything is configured, the installation process can be started by running:

.. code-block:: sh

   $ ./scripts/deploy.sh

It will take a while depending on your internet connection and target machine. When the installation process
is finished, you should be able to access the EaaSI login page with a browser at the URL ``https://<hostname>``.
The ``<hostname>`` should match the address of the target machine you specified in the ``hosts.yaml`` file.


.. _setting-up-orgctl:

Set up "Organization" using eaas-orgctl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the EaaSI platform is deployed, the superadmin must use the `eaas-orgctl`_ script to
create at least one "organization" for their EaaSI installation.

"Organizations" can be used to create arbitrary groups of users and resources within a single
EaaSI installation (in other words, to make a single EaaSI deployment serve as the back-end for multiple
"nodes"). The following instructions will assume a single-organization deployment (the simplest and currently recommended
configuration; you can consult the README on the `eaas-orgctl`_ repository for additional information on managing multiple
orgs)

Clone the `eaas-orgctl`_ script into an empty directory (outside/separate from your `eaasi-installer`_):

.. code-block:: sh

  $ git clone https://gitlab.com/eaasi/eaas-orgctl

Change into the new directory and use the script's built-in "template" feature to generate a JSON configuration file for your organization:

.. code-block:: sh

  $ ./eaas-orgctl template > <org-name>.json

Open and edit the empty JSON template with the desired values for your organization name and to specify an initial Admin-level user
for the node. An example configuration would look as follows:

.. literalinclude:: examples/org-xyz.json
  :language: json

.. warning::
  The EaaSI "superadmin" and the initial Admin-level user will be separate accounts with different credentials. The superadmin
  has access and control to the EaaSI server in order to run these deployment, upgrade, and organization control instructions. The initial Admin
  user simply refers to a first user with :ref:`Admin-level <user_admin>` power in the EaaSI UI, e.g. to import and replicate resources, create further users, etc.
  Please keep this in mind that the superadmin and initial Admin user may be the same or different individuals.

Once the organization configuration JSON is ready, use the ``<hostname>`` URL and superadmin credentials from the previous deployment step to create the organization:

.. code-block:: sh

  $ ./eaas-orgctl -e 'https://<hostname>' -u 'superadmin' create <org-name>.json

You will be prompted to enter the superadmin account password (previously set as ``admin_password`` in your ``eaasi.yaml``).

The ``eaas-orgctl`` script will create the organization and generate a random, temporary password for the initial Admin user
specified in the ``<org-name>.json``.

Provide the initial Admin username and temporary password to the desired initial EaaSI user, or use it yourself to log in to the
EaaSI UI at ``https://<hostname>``. On first login, this initial Admin user will be prompted to set a new, permanent password.

You are now ready to use EaaSI!

.. _managing-eaasi:

Managing EaaSI
---------------

A full EaaSI deployment incorporates a number of Docker containers related to the Emulation-as-a-Service (EaaS) back-end and the EaaSI UI. These containers are best managed in tandem via ``systemctl`` rather than individually. For example:

.. code-block:: sh

  $ sudo systemctl stop eaas     # to stop EaaSI
  $ sudo systemctl start eaas    # to start EaaSI
  $ sudo systemctl restart eaas  # to restart EaaSI

.. _removing-eaasi:

Removing EaaSI
---------------

If errors are encountered during Ansible deployment, it may become necessary or advisable during troubleshooting to wipe an incomplete installation before re-attempting the deploy script. Alternatively, sysadmins may want to remove EaaSI to reclaim or clean a machine after testing/demo.

To remove an EaaSI installation cleanly from your server, please execute the following steps in order:

.. code-block:: sh

  $ sudo systemctl stop eaas                            # stop EaaSI from running
  $ sudo rm -rf /eaasi                                  # delete the EaaSI installation directory (as specified in your eaasi.yaml configuration)
  $ sudo systemctl rm /etc/systemd/system/eaas.service  # delete the EaaSI service

.. _updating-eaasi:

Updating EaaSI
---------------

.. warning::
  Unpredictable behavior can always happen during an upgrade or migration process and EaaSI sysadmins should always prepare a complete server backup before performing any update or migration with the eaasi-installer.

To update a previously-existing EaaSI installation, first update the `eaasi-installer`_ by running its ``git-pull.sh``
script to match the most up-to-date release provided by the EaaSI team:

.. code-block:: sh

  $ ./git-pull.sh && ./git-pull.sh origin v2021.10

.. note::
  Running the ``git-pull.sh`` script twice, first without arguments, ensures that the script itself is up-to-date first, before fetching the current release branch.

The EaaSI configuration located in ``artifacts/config/eaasi.yaml`` must then be updated with the relevant git branch or tag on
certain lines as well, for the ``docker``, ``eaas`` and ``eaasi_ui`` and ``demo_ui`` modules. For the most up-to-date release recommended by EaaSI staff, please use the following (as seen in the provided ``eaasi.yaml.template``):

  - docker.image: ``eaas/eaas-appserver:v2021.10-eaasi``
  - eaas.git_branch: ``v2021.10-eaasi``
  - eaasi_ui.git_branch: ``v2021.10``
  - demo_ui.git_brach: ``v2021.10-eaasi``

Following these configuration changes, to update the various EaaSI components, run:

.. code-block:: sh

   $ ./scripts/update.sh [<component>...]

where ``<component>`` can be one of the following:

- ``ear``: to update EaaSI's server binary to the latest version
- ``docker-image``: to update runtime docker-image to the latest version
- ``eaasi_ui``: to update the EaaSI UI elements to the latest version
- ``demo_ui``: to update the Demo UI elements to the latest version

Multiple components can be specified as a space-separated list. If called without any ``<component>``
arguments, then all components will be updated by default.

.. _migration:

Migrating from 2020.03 to 2021.10
-----------------------------------

.. note::
  If you are not or have never used the 2020.03 release of the EaaSI UI to create resources, you can ignore this section when installing or upgrading EaaSI. The eaasi-installer will automatically detect and skip over migration steps if they are unnecessary.

.. warning::
  Unpredictable behavior can always happen during an upgrade or migration process and EaaSI sysadmins should always prepare a complete server backup before performing any update or migration with the eaasi-installer.

As of ``v2021.10`` eaasi-installer contains a number of migrations intended to address major structural changes in the storage and exchange of resource metadata between the 2020.03 release of the EaaSI UI and later tagged releases (starting with 2021.10).

These migrations should not actively alter or affect any resource metadata created by the 2020.03 EaaSI UI release; all Environments, Software, and Content imported or created in a previous release will still be present on migration, and associated with the original user who created them. Network status (Public/Saved to Node/Private) should also remain unchanged. The migrations are merely intended to optimize system performance by moving data previously stored only in the EaaSI client's front-end PostgreSQL database to the Emulation-as-a-Service back-end, and remove redundant storage of some metadata on both front- and back-end.

The necessary migration steps are defined in the provided ``eaasi.yaml.template`` and should be left as-is. The migration will be performed automatically when running the ``update.sh`` script as specified above in :ref:`updating-eaasi`.

However, migrating from the 2020.03 to 2021.10 EaaSI UI release requires migrating *user* metadata from the Postgres database to Emulation-as-a-Service's new integrated Keycloak module for user management and authentication. Unfortunately, user passwords in Postgres are hashed and can not be migrated directly. In order to migrate existing users from the 2020.03 EaaSI UI release, new, equivalent accounts must be created in Keycloak and all passwords reset.

When the eaasi-installer has successfully completed migrating from a 2020.03 installation, it will automatically generate a file titled ``keycloak-users.csv`` under ``/[eaas-home-dir]/eaasi-ui/migrations/exports`` on the target server. This CSV contains a list of all the newly-created Keycloak users (maintaining user name and email account information from the 2020.03 release) with a corresponding, temporary password. The sysadmin who runs the update and migration must provide the corresponding temporary password to each user for them to use on initial login attempt in the updated EaaSI node. The user will then be prompted to set their own, permanent password for their account, now managed by Keycloak. (See :ref:`logging_in`)


Browser Compatibility
----------------------

The EaaSI team recommends attempting to access the EaaSI UI using:

- Firefox (v. 65+)
- Chrome/Chromium
- Microsoft Edge (v. 79+)

Other browsers - including Safari or older (non-Chrome-based) versions of Microsoft Edge may work to some degree but are not well tested.

.. note:: Some browser extensions also may interfere with EaaSI functionality, including ad-blockers, popup-blockers or similar. If encountering unexpected behavior, please try disabling all browser extensions first.
