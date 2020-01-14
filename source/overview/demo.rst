.. Demo

.. _container_setup:

Try EaaSI
-----------

.. note::

   This method requires installation of Docker.
   Consult the `Docker Engine - Community <https://docs.docker.com/install/>`_ installation instructions
   for your operating system before proceeding.
   
The development team at OpenSLX has packaged custom Docker images of an example EaaSI release
to simplify deploying EaaSI on to a single desktop for purposes of testing and demonstration. The
following instructions are optimized for MacOS and Linux but can be adapted for Windows as well (see
below).

**1.** Download and unpack ``EaaSI_Demo.tar.gz`` from [Wasabi link].

  Checksum (SHA256): []

  This file is approximately 1.6 GB (3.4 GB unzipped) and contains the filesystem, server deployment
  and Docker images necessary to run EaaSI within a single directory.
  
**2.** Using terminal of choice, change directories into the extracted ``EaaSI_Demo`` folder::
  
  $ cd EaaSI_Demo
  
**3.** Load the two required Docker images (enter sudo/admin credentials when prompted)::

  $ sudo docker load -i docker/eaas-proxy.tar
  $ sudo docker load -i docker/eaas-custom.tar
  
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
User Handbook to add :ref:`emulators <managing_emulators>`, :ref:`upload software <adding_software>` 
and :ref:`create environments <import_base>`! But we recommend using the `EaaSI Open Source Sandbox 
<https://eaasi-sandbox.softwarepreservationnetwork.org/eaasi/#/portal/welcome>`_ to get started with 
some already-made environments.

Click on "OAI-PMH" in the navigation sidebar. In the "Metadata Harvesting" menu, click on the "Add OAI-PMH
Endpoint" button.

.. image:: /guide/images/add_endpoint.png

Under ``Hostname``, enter: ``http://[sandbox_endpoint_URL]``. (You may name the endpoint however you
wish, e.g. "EaaSI Sandbox")

Click "Add". Your EaaSI Sandbox entry should now be available in the Metadata Harvesting menu.

Click "Synchronize Full" to fetch information about all of the environments available in the Open
Source Sandbox. (This may take a minute or two!)

Once the synchronization is complete, use the sidebar to navigate to "Environments", then under
"Virtual machines" click on the "Remote" tab. You should see a list of the same environments available
on the online Sandbox!

Use the dropdown menus to view the Details pages of the various environments and choose which you
would like to run and use locally. When you have chosen an environment, click "Replicate" in the top
right corner of any environment Details page to download it into your EaaSI installation. (Download/
replication time will vary depending on the size of the environment, the quality of your internet
connection, and current traffic on the Open Source Sandbox)

As part of the replication process, EaaSI will automatically fetch and download the necessary emulator
for running that environment. This has the added benefit of making that emulator and its templates
available for you to create and import new environments as well!
