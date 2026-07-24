.. Resource Details pages

.. _details:

Resource Detail Pages
======================

:term:`Resource` Detail pages provide some additional descriptive information for EAASI resources. Depending on permissions, users may also be able to edit the resource's configuration settings for Emulation Access sessions.


.. _environment_details:

Environment Details
---------------------

The Details page for :term:`Environment` resources is divided into two tabs: Metadata and History.

Metadata
*********

In "Review Mode", users can view current descriptive metadata and configured emulator settings. Click on "Edit Mode" to edit and save changes to compatible fields in Private Environments.

.. warning::
  Resources marked "Saved Locally" **are not editable**. Once published, neither the descriptive metadata nor emulator configuration settings for Environments can be altered. Editing **any** fields on a "Saved Locally" Environment will create a new, derivative, Private Environment. Take care to edit Resource Names or other fields for clarity.

**Resource Name**: This is an arbitrary, free text field for users to identify the resource.

.. image:: ../images/environment_name_desc.png

**Configured Drives**: Storage drives must be added and configured properly for Environments in order to allow mounting Software and Content resources in emulation. Drive configuration requires a Media Type (CD-ROM/ISO, Floppy, or Disk) corresponding to the three available :ref:`Media Types <media_types>` for Software and Content resources). Depending on the underlying emulator, additional storage interface and bus/address numbers must be specified to function properly. (editable)

By default, PC-based EAASI Environments should have at least: a Disk drive (for the Environment's system drive/operating system), a CDROM drive (for mounting ISO and Files type resources), and a Floppy drive (for mounting Floppy type resources). Adding additional Configured Drives, particularly with Macintosh or other non-PC hardware, may allow for Software and Content resources with multiple CD-ROM or Floppy type objects to be properly mounted.

.. warning::
  There can be severe limitations to the Configured Drive feature depending on the underlying emulator and the Environment's operating system.

.. image:: ../images/configured_drives.png

**Emulator**: This section indicates the underlying emulator and :term:`Hardware Configuration` used to run this Environment in emulation. Advanced users can use this section to switch the emulator version used to run the Environment (e.g. QEMU 2.12 or QEMU 3.1) and, if necessary, tweak the emulated machine's hardware. Consult each emulator's own documentation to correctly pass Configuration settings to the emulator.

.. image:: ../images/emulator_details.png

**Environment Options**: Enables (or disables) various options for running the Environment in the Emulation Access Interface.

"Environment can Print" enables the "Download Print Jobs" feature. If an emulated operating system is configured with a PostScript-enabled virtual printer, print jobs sent to that printer within the emulation session will be intercepted by the EAASI client and offered to the user to download as a PDF. This is currently the only method of extracting data/files from within EAASI Environments and :ref:`only available in QEMU-based Environments <print-jobs-qemu-limitation>`.

"Relative Mouse (Pointerlock)" enables a running Environment to capture the user's mouse input.

"Requires clean shutdown" forces the user to perform a full ACPI shutdown of the Environment's operating system in emulation before allowing the user to use the Save Environment feature.

"Internet Enabled" controls whether or not the Environment can theoretically access the live internet while running (if the Environment's guest system is configured correctly).

.. note::
  "Requires clean shutdown" is recommended for most Environments from approximately 1998 and later (e.g. Windows 98 and up) to make sure emulation sessions save cleanly as a new Environment or revision without operating system errors. It should **not** be enabled for Environments and operating systems prior to this. See `Advanced Configuration and Power Interface <https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface>`_.

.. warning::
  For "Environment can print" and "Enable Internet access" features to work correctly, the Environment's operating system must have been properly configured with a functional PostScript printer drive (for "Environment can print") or an installed TCP/IP networking stack ("Enable Internet access").

.. image:: ../images/ui_options.png


History
*********

The History tab displays prior revisions of the Environment, if any. Revisions are displayed and sorted according to the "Description" field for that revision.

.. note::
  The EAASI team recommends using the "Description" field in a similar manner to git commit messages, providing a brief but descriptive message to other users regarding the configuration or metadata change to create that revision.

The user can choose to "Fork" any previous revision. Forking will create a new, Private Environment resource based on that revision. This essentially allows users to revert Environment revisions.

.. image:: ../images/resource_history.png

Software Details
--------------------

.. warning::
  Software metadata is **not** editable after import.

Software resource details are ONLY available in "Review Mode." Users can view current properties of Software resources and some details of the object, including attached files and their Media Type, but not edit any of these properties.

.. note::
  "Allowed Number of Instances" is set by default to "unlimited", allowing an unlimited number of concurrent emulation sessions.

.. note::
  "Is Operating System" is a legacy descriptive metadata field with no effect on EAASI functionality, and can be ignored. It will always display "FALSE" regardless of whether the imported Software object actually is an operating system installer or not.

.. image:: ../images/software_properties.png

Content Details
-------------------

.. warning::
  Content metadata is **not** editable after import.

The EAASI system currently gathers very little metadata or description about Content resources, except for its name/label. Therefore there are no Details pages for Content resources.