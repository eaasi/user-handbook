.. Resource Details pages

.. _details:

Resource Detail Pages
======================

:term:`Resource` Detail pages provide some additional descriptive information for EaaSI resources. Depending on permissions and the resource's Network status, users may be also be able to edit teh resource's configuration settings for Emulation Access sessions.


Environment Details
---------------------

The Details page for :term:`Environment` resources is divided into two tabs: Metadata and History.

Metadata
*********

In "Review Mode", users can view current descriptive metadata and configured emulator settings. Click on "Edit Mode" to edit and save changes to compatible fields in Private Environments.

.. warning::
  At this time, not all fields on Environment Detail pages are editable. Various fields' status will be marked below.
  
.. warning::
  Resources marked "Public" **are not editable**. Once published to the EaaSI Network, neither their descriptive metadata nor emulator configuration settings can be altered. Editing **any** fields on a Public/Saved Locally Environment will create a new, derivative, Private Environment. Take care to change Resource Names or other fields to indicate new Environments created from changing settings on the Details page.

.. note::
  All resources are assigned a unique identifier (UUID) by the EaaS back-end on creation. UUIDs are not viewable in the EaaSI interface or editable.
  
**Resource Name and Description**: these are arbitrary, free text fields for users to identify the resource (editable)

.. image:: ../images/environment_name_desc.png
  
**Operating System**: These details are intended to reflect relevant details for discovery from the Environment's operating system. This section is currently **not functional** and should not be considered accurate. It is included to indicate the roadmap for future development on the EaaSI metadata model. (not editable)

.. image:: ../images/os_details.png

**Configured Machine**: TBD (not editable)

**Emulator**: This section indicates the underlying emulator and :term:`Hardware Configuration` used to run this Environment in emulation. Advanced users can use this section to switch the emulator version used to run the Environment (e.g. QEMU 2.12 or QEMU 3.1) and, if necessary, tweak the emulated machine's hardware. Consult each emulator's own documentation to correctly pass Configuration settings to the emulator. (editable)

.. image:: ../images/emulator_details.png

**Configured Drives**: Storage drives must be added and configured properly for Environments in order to allow mounting Software and Content resources in emulation. Drive configuration requires a Media Type (CD-ROM/ISO, Floppy, or Disk) corresponding to the three available :ref:`Media Types <media_types>` for Software and Content resources). Depending on the underlying emulator, additional storage interface and bus/address numbers must be specified to function properly. (editable)

By default, every EaaSI Environment created will have at least: a Disk drive (for the Environment's system drive/operating system), a CDROM drive (for mounting ISO and Files type resources), and a Floppy drive (for mounting Floppy type resources). Adding additional Configured Drives can allow for mounting Disk type objects, or possibly multiple CD-ROM or Floppy type objects within a Software or Content resource at once.

.. warning::
  There can be severe limitations to the Configured Drive feature depending on the underlying emulator and the Environment's operating system. Please raise specific examples/concerns in the `Support Center <https://forum.eaasi.cloud/c/support-center/6>`_ in the EaaSI Community Forum for help and guidance if needed.
  
.. image:: ../images/configured_drives.png

**UI Options**: Enables (or disables) various options for running the Environment in the Emulation Access Interface. "Environment can Print" enables the "Download Print Jobs" feature. "Relative Mouse (Pointerlock)" enables a running Environment to capture the user's mouse input. "WebRTC Audio (Beta)" enables an improved method for streaming audio from the emulation session to the user's browser. "Requires clean shutdown" forces the user to perform a full ACPI shutdown of the Environment's operating system in emulation before allowing the user to use the Save Environment feature. (editable)

.. note::
  WebRTC Audio is now out of beta and considered a recommended configuration setting for most Environments.
  
.. note::
  "Requires clean shutdown" is recommended for most Environments from approximately 1998 and later (e.g. Windows 98 and up) to make sure emulation sessions save cleanly as a new Environment or revision without operating system errors. It should **not** be enabled for Environments and operating systems prior to this. See `Advanced Configuration and Power Interface <https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface>`_. 
  
.. image:: ../images/ui_options.png

**Networking**: Using this option, users can change whether or not the Environment can access the live internet while running in the Emulation Access interface (editable)

.. warning::
  For "Environment can  print" and "Enable Internet access" features to work correctly, the Environment's operating system must have been properly configured with a functional PostScript printer drive (for "Environment can print") or an installed TCP/IP networking stack ("Enable Internet access"). Please consult the `Software Help <https://forum.eaasi.cloud/c/software-help/10>`_ section of the EaaSI Community Forum if needing assistance in this area for the Environment or legacy operating system of your choice.
  
  
History
*********

The History tab displays prior revisions of the Environment, if any. Revisions are displayed and sorted according to the "Description" field for that revision.

.. note::
  The EaaSI team recommends using the "Description" field in a similar manner to git commit messages, providing a brief but descriptive message to other users regarding the configuration or metadata change to create that revision.
  
The user can choose to "Fork" any previous revision. Forking will create a new, Private Environment resource based on that revision. This essentially allows node users to revert Environment revisions.

.. image:: ../images/resource_history.png

Software Details
--------------------

In "Review Mode", users can view current properties of Software resources and some details of the object, including attached files and their Media Type. In "Edit Mode", **only** "Software Properties" are editable.

**Software Properties**: These are editable settings that control to some degree how and when users can interact with the Software resource in emulation. "License Information" is a free-text field and a recommended place to stash license key or registration information that a user may need to correctly run or install the software. "Allowed Number of Instances" controls how many concurrent emulation sessions can be run using this resource. "This is an Operating System" allows the Software resource to appear in the Emulation Project menu as an option to create a new Environment from scratch.

.. note::
  "Allowed Number of Instances" is set by default to "-1", allowing an unlimited number of concurrent emulation sessions. If editing, set to the desired positive integer.
  
.. note::
  "QID" and "Rendering Capabilites" fields allow for automatic file characterization to pair imported Content resources with Software that may be capable of rendering it via the 'Detect Environments' button. Expanded functionality of this feature (direct connection to Wikidata, auto-rendering based on the `Universal Virtual Interactor <https://ipres2019.org/static/pdf/iPres2019_paper_128.pdf>`_) is planned.
  
.. image:: ../images/software_properties.png

Content Details
-------------------

.. warning::
  Content metadata is **not** editable after import.
  
The EaaSI system currently gathers very little metadata or description about Content resources. From the Content resource Details page, users can attempt to auto-detect compatible Environments with the "Detect Environments" feature or Add the Content to their Emulation Project.

.. image:: ../images/content_details.png
