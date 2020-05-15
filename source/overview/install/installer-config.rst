.. config-value:: host

   Configuration options for the installation target machine.

   .. config-value:: build_dir

      :type: string

      An intermediate directory to use during installation.

   .. config-value:: eaas_home

      :type: string

      Target directory to install EaaS into.

   .. config-value:: eaas_tmp

      :type: string
      :default: ``/tmp``

      Directory to store runtime data. (optional)

   .. config-value:: ssh_port

      :type: int

      Optional, custom SSH port to use during installation.


.. config-value:: docker

   Configuration options for the EaaS container.

   .. config-value:: image

      :type: string

      Docker image to pull during installation.

   .. config-value:: network_name
   
      :type: string
      :default: ``eaasi``
      
      Name the Docker network created and used for all communication between EaaSI containers. Can be any arbitrary name.
      
   .. config-value:: port
   
      :type: int
      
      Optional, custom Docker port to use during installation.

   .. config-value:: ssl

      Optional configuration options for SSL support.

      .. config-value:: enabled

         :type: boolean
         :default: ``false``

         If ``true``, then the SSL support will be enabled.

      .. config-value:: certificate

         :type: string

         A path to a *full-chain* certificate to use for EaaS service.

         .. note::

            Since the installer runs in a Docker container, the certificate file must
            be located somewhere under ``./artifacts`` on the controller-machine to be
            available during the installation process.

      .. config-value:: private_key

         :type: string

         A path to certificate's private key. Similar file location restrictions apply,
         see `certificate's note <#config-value-certificate>`_ for more information.

   .. config-value:: image_archive_volume

      :type: string
      :default: ``./image-archive``

      Optional path to the image archive directory. This path must be writable.
      If it does not exist, it will be created.

   .. config-value:: import_volume

      :type: string
      :default: ``./import``

      Optional path to the images import directory.

.. config-value:: eaas

   Configuration options for the EaaS service.

   .. config-value:: git_branch

      :type: string

      Name of the Git branch to install EaaS from.

   .. config-value:: enable_oaipmh_provider

      :type: boolean

      Flag to enable export of EaaS environments through an OAI-PMH provider.
      
   .. config-value:: db_upgrade
   
      :type: boolean
      :default: true
      
      Performs a one-time migration of legacy EaaS UI database to new Portal database, if necessary. Action is idempotent (will check itself so that it only executes once), so can always be left to ``true``
      
.. config-value:: portal

  Configuration options for the PortalMedia EaaSI User Interface.
     
  .. config-value:: git_branch
     
     :type: string
     
      Git branch name to install EaaSI UI from.
      
  .. config-value:: db_update

      :type: boolean
      :default: false
         
      This will remove all current data, if any from the eaasi-database, and perform a clean seed. This optional variable is hidden and defaults to ``false`` to prevent accidental deletion of production data. **Only set this variable to ``true`` if it is necessary or helpful to perform a clean install or update of your node!!!**
      
  .. config-value:: auth
    
  .. config-value:: mailer
  
    SMTP server configuration - required for creating new user accounts (new users will receive an email
    with their auto-generated password when added by the initial Admin user)
    
    .. config-value:: port
    
      :type: int
      :default: 587
      
      Port for communication with SMTP server (generally either 587 or 465 for SSL-secured connections)
    
    .. config-value:: host
    
      :type: string
      
      Host domain or IP address for SMTP mailer.
      
    .. config-value:: user
    
      :type: string
      
      Admin username for SMTP mailer.
      
    .. config-value:: password
    
      :type: string
      
      Admin password for SMTP mailer.
      
    .. config-value:: sender
    
      :type: string
      
      Sender email address for communications from your SMTP mailer (EaaSI users will receive their 
      passwords from this address)
      
  .. config-value:: organization
  
    .. config-value:: name
    
      :type: string
      
      Organization name for your node (for display in the UI)
      
  .. config-value:: initial_user
  
    Configure credentials for initial Admin user in the UI. This user can/must then assign further
    users using the Manage Node menu.
  
    .. config-value:: email
    
      :type: string
      
      The login password for the initial user is hard-coded to **"eaasidemo1"**. It is strongly recommended that this initial user reset their password (which will generate a random, more secure password). Reset passwords for the initial user will be sent to this address.
      
    .. config-value:: username
    
      :type: string
      
      Assign a username to the initial Admin user.
      
    .. config-value:: first_name
    
      :type: string
      
      Assign first name for the initial Admin user.
      
    .. config-value:: last_name
    
      :type: string
      
      Assign last name for the initial Admin user.
