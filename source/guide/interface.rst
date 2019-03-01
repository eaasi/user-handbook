.. Navigating the interface

.. _navigation:

Navigating the EaaSI Interface
******************************

These guidelines and screenshots refer to the EaaSI demo administration interface, as provided for the beta release starting in March 2019. Front-end development will continue throughout the course of the EaaSI project and instructions may be periodically updated and versioned accordingly.

Logging In
==========

To log in to the EaaSI beta interface, navigate to the URL and provide the login credentials provided by your node's system administrators.

.. image:: images/Login.png


Landing Page
============

The demo Admin UI landing page features live statistics regarding the health of the local EaaSI node and the network as a whole (i.e. CPU and memory usage). These may assist Admin users and systems administrators with troubleshooting.

.. image:: images/dashboard.png

The EaaSI navigation sidebar allows users to investigate and interact with EaaSI's three primary types of :term:`resources` : Environments_, Software_ and Objects_.

.. image:: images/resources_navigation.png

The sidebar can also be used to access various pages for :ref:`importing resources <add_resources>` and :ref:`adminstrative settings <administration>`.

.. image:: images/settings_navigation.png


Environments
============

Overview page
-------------

Environments are sorted into tabs and sub-sections depending on:

  1. Derivative status (i.e. if it is a Base, Software or Object Environment)
  2. Published status (its visibility to other users in the network)

.. image:: images/environments_overview.png

The "Base Environments" tab contains both :term:`Base` and :term:`Software Environments <Software Environment>`. Base Environments have typically been marked as a "Base" in their name. The notation "V#" has been used internally by EaaSI staff to mark "version" number for base environments - e.g. "V1" for the first attempt at importing a base image, "V2" for the second attempt at importing a base image of the same system, etc.

Software Environments can typically be identified by a name that connotes its original base environment and the name of the Software added (e.g. "Windows 98 SE + Microsoft Office 97").

The "Base Environments" tab is further broken down into three sub-sections: *Private*, *Public* and *Remote*.

  - *Private* environments are visible only to the currently logged-in node user (see `Logging In`_). They are stored locally at the node.
  - *Public* environments are visible and available for replication to all users on the network. They are stored locally at the source node. (Users at other nodes will see your *Public* environments in their *Remote* sub-section)
  - *Remote* environments are all :ref:`published <publishing>` environments from other nodes on the network. These environments are not stored locally but are available for replication to local storage (at which point they will move to the *Public* sub-section)

The "Object Environments" tab contains only derivative :term:`Object Environments <Object Environment>`. The environments displayed here should **always** be unique to the node; no node should be able to see or interact with other nodes' Object Environments.

.. image:: images/object_environments_overview.png

For each tab and sub-section, the environments display table shows:

  - *Name*: a descriptive human-readable name for the environment
  - *ID*: a unique UUID assigned to the environment to allow for sharing and consistency across the network
  - *Owner*: will indicate ownership status of the environment within one node when multi-user login functionality is added to the platform; for now, all environments should list "shared"
  - *Actions*: dropdown menu allowing for user and administrative actions related to that environment


Running environments
---------------------
To run a selected environment in emulation, choose the "Run Environment" option from the Actions dropdown menu.

.. image:: images/run_environment.png

Your emulation session should load immediately.

.. image:: images/running_environment.png

Clicking on the emulation window will capture your mouse and keyboard input to the emulated system. If Pointerlock is enabled, press "Esc" at any point during the session to free your mouse to interact with your host system.

During the session, the EaaSI Action Menu will appear below the navigation sidebar:

.. image:: images/actions_menu.png
  :align: center

- *Download Print Jobs*: This button will appear contextually depending on whether "Environment can print" has been selected in the environment record (see `Viewing and editing environment records`_). If enabled, PostScript print jobs from the emulated system should be converted and available here as downloadable PDFs.
- *Save Environment*: Saves the current emulation session state as a new revision or derivative environment; changes are :ref:`isolated <derivation>` from the base image that began the session. The guest operating system must be shut down before the environment changes can be saved (see `Creating new environments`_)
- *Send Ctrl-Alt-Del*: Shortcut for sending the `"Ctrl+Alt+Delete" <https://en.wikipedia.org/wiki/Control-Alt-Delete>`_ keyboard input to the emulated operating system
- *Send Esc*: Sends the "Esc" keyboard input to the emulated operating system
- *Restart Session*: Reloads the emulation session; any changes made to the environment during the current session will be discarded
- *Stop*: Shuts down the emulation program and quits emulation session altogether; any changes made to the environment during the session will be discarded

An emulation session can be ended in several ways: using the "Stop" button from the Action Menu, shutting down the emulated operating system, or simply navigating away from the page in your browser. In all scenarios, the changes to the environment are not saved and running the environment again will return the emulation session to its original state.


Viewing and editing environment records
-----------------------

To view and edit a selected environment's metadata, choose the "Details" option from the Actions dropdown menu in the environment overview.

.. image:: images/details_action.png

An environment record will initially only display a few descriptive fields. Click the 'Advanced Options' button to reveal the full environment record:

.. image:: images/environment_record.png

- *Environment Settings* determine the :term:`Hardware Configuration`; users can see which emulator (and version) have been selected the run the environment, as well as specific configuration options/arguments passed to the emulation application.

  .. note:: Only "Environment can print", "Relative Mouse (Pointerlock)", and "Enable Internet access" are fully supported emulation features as of the beta. All other check-box options should be considered experimental.

- *Configured Software* lists any Software Objects that were loaded and saved into this environment.
- *Revision History* describes the history of the environment in EaaSI, including any revisions made to this environment *and* the environment(s) it was derived from, if applicable.

To edit settings and descriptive metadata, click the "Edit" button at the top right corner of the page to open the record in editable mode.

.. image:: images/edit_environment_record.png
  :align: center

.. note:: Enabling "Relative Mouse (Pointerlock)" is highly recommended for most if not all environments. It usually allows more accurate mouse movement and input to the emulated system.

After making any changes to an environment record, be sure to click "Save" at the bottom of the page to save your edits.

.. image:: images/save.png


Creating new environments
--------------------------

Adding new environments to the overview will depend on the type of environment being created. See:

  - :ref:`import_base`
  - `Creating a Software Environment`_
  - `Creating an Object Environment`_



Software
========

Overview page
-------------

The Software overview page allows for browsing and adding Software Objects within the node.

.. image:: images/software_overview.png

- *ID* and *Label* fields are currently the same descriptive value. Updates forthcoming.
- *Operating System* indicates whether the Software Object has been marked as containing a bootable OS (e.g. is an operating system installation disc)

Viewing/editing records
-----------------------

Click the "Edit" button next to a selected Software Object to view its metadata and details.

.. image:: images/software_details.png

Software metadata input is currently minimal. Free text fields allow for input of license information and `WikiData QIDs <https://www.wikidata.org/>`_ if desired or convenient for reference.


Adding Software
----------------


Creating a Software Environment
-------------------------------

Objects
=======

Overview page
-------------
Viewing/editing page
--------------------
Creating an Object Environment
------------------------------
