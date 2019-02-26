.. Navigating the interface

.. _navigation:

Navigating the EaaSI Interface
******************************

These guidelines and screenshots refer to the EaaSI demo administration interface, as provided for the beta release starting in March 2019. Front-end development will continue throughout the course of the EaaSI project and instructions may be periodically updated and versioned accordingly.

Logging In
==========

Landing Page
============

The demo Admin UI landing page features live statistics regarding the health of the local EaaSI node and the network as a whole (i.e. CPU and memory usage). These may assist Admin users and systems administrators with troubleshooting.

[screenshot]

The EaaSI navigation sidebar allows users to investigate and interact with EaaSI's three primary types of :term:`resources` - Environments_, Software_ and Objects_.

[screenshot]

The sidebar can also be used to access pages for :ref:`importing resources <add_resources>` and :ref:`adminstrative settings <administration>`.

[screenshot]



Environments
============

Overview page
-------------

Environments are sorted into tabs and sub-sections depending on:

  1. Derivative status (i.e. if it is a Base, Software or Object Environment)
  2. Published status (its visibility to other users in the network)

The "Base Environments" tab contains both :term:`Base` and :term:`Software Environments <Software Environment>`. Base Environments have typically been marked as a "Base" in their name. The notation "V#" has been used internally by EaaSI staff to mark "version" number for base environments - e.g. "V1" for the first attempt at importing a base image, "V2" for the second attempt at importing a base image of the same system, etc.

Software Environments can typically be identified by a name that connotes its original base environment and the name of the Software added (e.g. Windows98 + Office97).

The "Base Environments" tab is further broken down into three sub-sections: *Private*, *Public* and *Remote*.

  - *Private* environments are visible only to the currently logged-in user (see `Logging In`_). Other users, even those logged in to the same node, will not be able to see private environments. They are stored locally at the node.

  - *Public* environments are visible to all users on the node. They are also visible and available for replication by users at other nodes (via their *Remote* tab)

  - *Remote* environments are all public environments from other nodes on the network. These environments are not stored locally but are available for replication to local storage (at which point they would move to the *Public* sub-section)

The "Object Environments" tab contains only derivative :term:`Object Environments <Object Environment>`. The environments displayed here should **always** be unique to the node; no node should be able to see or interact with other nodes' Object Environments.




Viewing/editing records
-----------------------

Software
========

Overview page
-------------
Viewing/editing records
-----------------------

Objects
=======

Overview page
-------------
Viewing/editing page
--------------------

Action Menu
===========
