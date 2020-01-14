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

      Directory to store runtime data.

   .. config-value:: ssh_port

      :type: int
      :default: 22

      Custom SSH port to use during installation.


.. config-value:: docker

   Configuration options for the EaaS container.

   .. config-value:: image

      :type: string

      Docker image to pull during installation.

   .. config-value:: port

      :type: int

      Public network port for the EaaS service.

   .. config-value:: ssl

      Configuration options for SSL support.

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
         see `sectificate's note <#config-value-certificate>`_ for more information.

   .. config-value:: image_archive_volume

      :type: string
      :default: ``./image-archive``

      Optional path to the image archive directory. This path must be writable.
      If it does not exist, it will be created.

   .. config-value:: import_volume

      :type: string
      :default: ``./import``

      Optional path to the images import directory.


.. config-value:: ui

   Configuration options for the EaaS user-interface.

   .. config-value:: git_branch

      :type: string

      Name of the Git branch to install UI from.

   .. config-value:: http_auth

      HTTP Basic-Auth options.

      .. config-value:: user

         :type: string

         User name to use for login.

      .. config-value:: password

         :type: string

         Password to use for login.


.. config-value:: eaas

   Configuration options for the EaaS service.

   .. config-value:: git_branch

      :type: string

      Name of the Git branch to install EaaS from.

   .. config-value:: enable_oaipmh_provider

      :type: boolean

      Flag to enable export of EaaS environments through an OAI-PMH provider.
