.. Demo

.. _container_setup:

Try EaaSI
-----------

.. note::

   Trying EaaSI requires installation of Docker Engine and Docker Compose. On macOS and Windows, both will be handled automatically by installing Docker Desktop. On Linux, it may be necessary to install both packages/tools separately. Please consult the `Get Docker <https://docs.docker.com/get-docker/>`_ instructions for your operating system and make sure you have both packages before proceeding.
   
The development team at OpenSLX has packaged custom Docker images of an example EaaSI release
to simplify running EaaSI on a single machine (out of a single directory) for purposes of testing and demonstration. The
following instructions are optimized for MacOS and Linux but can be adapted for Windows as well (see
below).

.. note::
  EaaSI demo Docker deployments use the "Legacy UI" interface. Use the :ref:`legacy_ui` section of this Handbook
  for instructions for using your portable EaaSI Docker deployment!

**1.** Download and unpack ``EaaSI_Demo_v1_Lite.tar.gz`` from https://s3.wasabisys.com/EaaSIDemonstrators/EaaSI_Demo_v1_Lite.tar.gz.

  Checksum (SHA256): [7cbad886168e7d59956720c70a4047cf63e372169e54c5324bdf5bf622c67e7b]

  This file is approximately 2.6 GB (~8 GB unzipped) and contains the filesystem, server deployment
  and Docker layers necessary to run EaaSI within a single directory.
  
**2.** Using terminal of choice, change directories into the extracted, top-level ``EaaSI_Demo_Lite`` folder::
  
  $ cd EaaSI_Demo_Lite
  
**3.** Load the two required Docker images (enter sudo/admin credentials when prompted)::

  $ sudo docker load -i docker/eaas-proxy.tar
  $ sudo docker load -i docker/eaas-rootfs.tar
  
**4.** Run ``docker-compose`` to create and run containers from the loaded images, using the
configuration in the provided ``docker-compose.yaml`` file::

  $ sudo docker-compose up
  
**5.** After a minute, your test EaaSI instance should be available by directing any common browser
(Firefox and Chrome recommended) to ``localhost:8080/admin``. (Look for a terminal message:
``root: Successfully deployed "eaas-server.ear"``)

**6.** Log in to the EaaSI Demo admin interface with the credentials:

  - User: ``eaasi``  
  - Password: ``demo``

**7.** At this point, you have a functional test instance of EaaSI and can consult the rest of this
User Handbook to add :ref:`emulators <managing_emulators_dev>`, :ref:`upload software <adding_software_dev>` 
and :ref:`create environments <import_base_dev>`! The provided demo includes a few open source operating
system environments to get you started.

**8.** To gracefully shut down the EaaSI Docker container, open a second terminal window and run::
  
  $ sudo docker-compose down
  
in the ``EaaSI_Demo_Lite`` directory.

.. note::
  
  **For Windows users**: The EaaSI team has sometimes encountered minor issues with Docker for Windows. 
  You *must* share the drive containing the "EaaSI_Demo" directory with Docker in Docker Desktop -> Settings -> Shared Drives, 
  using an admin account's credentials. There may be issues at this point if you are logged in to Windows 
  with Microsoft account or domain authentication, where drive sharing does not work even if that domain user has admin privilieges. 
  See: https://github.com/docker/for-win/issues/3174. If there are problems authenticating with a domain user,
  try setting up a local admin account and using those credentials to share the drive with Docker. 
  
  Once the C: (or other relevant drive address) has been properly shared with Docker, all the Docker commands described 
  above can be run in a PowerShell or Command Prompt terminal with raised (admin) privileges, simply excluding "sudo" from the commands.
