.. Technical architecture

System Architecture
*******************

Emulation-as-a-Service uses configuration templates (stored in XML) to assemble emulated hardware and data
as specified by the user.

The effect is to create in-browser virtual computing :term:`environments <environment>` that mimic the behavior of a physical machine.

When an EaaSI user runs an environment, the configuration file directs the platform to the appropriate emulator
for that system, the hardware settings for that emulator, a disk image containing a bootable operating system, and, if
desired, additional content (e.g. software installation media imaged from a CD-ROM or floppy disk) to mount in the
environment.

.. image:: ../images/visual_designs1.jpg

.. image:: ../images/visual_designs2.jpg

.. image:: ../images/visual_designs3.jpg


Node Components
===============

Emulation-as-a-Service is a server software stack composed of a number of modules working together to accomplish 
the task of emulator assembly and configuration. These modules can be deployed together or configured across multiple 
physical/virtual machines, depending on resources available. EaaSI installations (a :term:`node`) contain additional components to allow for 
sharing :term:`resources <resource>` and metadata across the EaaSI Network, but core functionality is accomplished with the following components.


Client
----------

An EaaSI client/front-end provides an interface to use the EaaS API through RESTful HTTP requests. This Handbook is primarily concerned with the EaaSI administrative interface designed by PortalMedia that allows for importing, saving, and documenting legacy software and content in emulated computing environments.

(The "Legacy UI" used for EaaS dev work can, as of v2020.03 release, remain accessible at the same time as the EaaSI administrative interface if so desired and configured. See :ref:`setup`)

Sharing and accessing those environments (e.g. as a patron or scholar), integrating with existing access services, or interacting
with EaaSI Network metadata in alternative routes and modules, will all be the subject of future front-end development.

.. image:: ../images/eaasi-client_summary.png


Gateway
--------

The EaaS Gateway acts as the API end-point and manages all emulation-related resources (it tracks emulation sessions,
calculates necessary compute resources, and finds all disk images/software/metadata as requested from the front-end).


Emulation Component (EmuComp)
------------------------------

The Emulation Component module actually allocates local CPU resources to serve emulation sessions. Its hardware must be
optimized to allow for potentially running multiple emulation sessions.


Image Archive (Connector)
-------------------------

The Image Archive connector/facade provides access to the underlying disk images that form :term:`environments <environment>` (and
their metadata). This module can act as a simple archive for locally-stored images, or (ideally) connect to a
third-party storage system (e.g. AWS, Wasabi, other cloud or networked storage), depending on where each EaaSI node intends to store its resources.


Object Archive (Connector)
--------------------------

Likewise, the Object Archive module provides access to :term:`content` and :term:`software` objects (floppy, CD-ROM, and hard
disk images, file sets, etc.); this module can also act as a simple archive for locally-stored data or (ideally)
connect to a third-party storage system, depending on the node setup.


.. image:: ../images/EaaS_Model.png


.. _oai-pmh:

OAI-PMH Synchronization
=======================

The EaaSI network makes use of the `Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) <https://www.openarchives.org/pmh/>`_
to request, share and synchronize metadata between nodes.

In addition to the node components listed above, each EaaSI installation contains an OAI-PMH harvester and a data provider. 
The harvester requests metadata (in EaaSI's case, Base and Software Environment records) from the data providers 
at other nodes; the data providers query the node's local records and return this metadata back to the original harvester.

.. image:: ../images/oai-pmh.png
  :align: center

Using the provided metadata, the harvester can also then find and replicate necessary files (disk images) from the
other nodes on :ref:`request <replication>`.

.. _derivation:

Environment Derivation
======================

EaaS makes use of a snapshot-based file format (`qcow <https://en.wikipedia.org/wiki/Qcow>`_) to avoid redundant copying and 
storage of full disk images. Any revisions or changes to an environment are isolated and saved in a new qcow file that is linked
but separate from the environment's original disk image. The saved derivative environments are then recreated programmatically from the 
original base and full chain of changes at the point that the user requests to run or replicate the environment.


.. image:: ../images/Derivatives-example.jpg
