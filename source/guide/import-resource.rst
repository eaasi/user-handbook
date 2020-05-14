.. Import Resource

.. _add_resources:

.. note::
  Resources imported by nodes previous to the 2020.03-beta release *should* persist without additional
  migration steps. Please file a bug report or contact the EaaSI team if encountering missing resources.

Import Resources
*******************

.. image:: ../images/visual_designs5.jpg

To import a new Content, Software, or Environment Resource, navigate to the "Import Resource" page using the sidebar
navigation menu.

.. image:: ../images/import_resource_overview.png

From there, please follow the corresponding instructions and guidelines below depending on whether you wish to import :term:`Content`,
:term:`Software`, or a stand-alone :term:`Environment`.

.. _import_content:

Importing Content
===================

To begin, select the "Import Content" button on the Import Resource page.

First, you will need to name your Content resource. This should be something short and descriptive; spaces, periods, hyphens
and underscores are OK, but please avoid using other special characters. Then proceed by clicking "Continue".

.. image:: ../images/about_this_content.png

You have three options for attaching and uploading files to be included in an import:

.. image:: ../images/attach_files.png

1. **URL**: Provide a direct download URL from publicly available cloud/web storage (HTTP addresses only)
2. **My Computer**: Will pull up a file browser for you to manually select the file(s) from your computer that make up your desired Content.
3. **Drag Files**: You may drag-and-drop the file(s) from your desktop to make up your desired Content.

Once at least one file is selected, the UI will allow you to "Add More Files" to create a multi-file resource:

.. image:: ../images/add_more_files.png

You may add as many files as desired.

.. _media_types:

There are four Physical Formats available to describe the file(s) being uploaded. The Physical Format will be used by EaaS to
communicate to emulators where/how to mount an object into an environment (i.e. relevant file system and/or virtual
drive).

.. image:: ../images/visual_designs4.jpg


- *ISO* - Mounts the object in an environment's virtual optical/CD-ROM drive. Should accept any file extension.

- *Floppy* - Mounts the object in an environment's virtual floppy drive. Should accept any file extension.

- *Disk* - Attempts to mount the object as a hard drive (success may thus be highly variable depending on an environment's configured hardware, the operating system's compatibility with the image's file system, etc.). Should accept most if not all hard disk image formats (IMG, DMG, DD/raw, QCOW, VDI, VMDK, E01/EWF, etc.)

- *Files* - This option will accept any set of files (i.e. intended for files that are not packaged in a disk image). To allow the arbitrary file set to be mounted in the broadest possible range of operating systems, imported file sets are currently packaged by EaaSI into an ISO file on the back-end; Files objects should thus mount in an environment's virtual CD-ROM/optical drive.


For "ISO", "Floppy", and "Disk" type resources, the files that make up the Content **must** be of the same Physical Format to mount and switch between files/disks
properly in emulation. Mixed-format resources are currently not supported.

.. warning::
  For example, An operating system installer might contain a boot floppy and then multiple CD-ROMs. The floppy image
  and the CD-ROM images must be considered and imported as different resources, but the CD-ROM images should likely be
  imported together as a single resource.

Once all desired files have been selected, click "Finish Import" at the top of the page:

.. image:: ../images/finish_import.png

Please **do not** navigate away fromm the import page until the upload is completed (i.e. the EaaSI logo stops spinning)

On successful import, the new Content resource will be available in the :ref:`explore` menu.


.. _import_software:

Importing Software
======================

The steps for importing Software resources are extremely similar to those for :ref:`import_content` above, with a few added options
for additional metadata.

To start import of a Software resource, select "Import Software" on the Import Resources page, then select "Fast Import".

.. image:: ../images/fast_import.png

.. warning::
  "Detailed Import" is a proposed future feature that takes advantage of the full EaaSI metadata model for describing software.
  It is non-functional in the 2020.03-beta release, but can give nodes an idea of the type of information they may want to start
  capturing about their software collections. The EaaSI team is considering enforcing detailed description of Software resources
  that are published to the Network in order to reduce redundant/duplicate resources.
  
From there, you must at a minimum assign a name to the Software Resource:

.. image:: ../images/about_software.png

All notes above regarding Physical Formats and selecting files to create a Content resource apply to Software as well.

(Again, mixed-format Software types are currently not compatible with EaaSI)

When you have selected Finish Import.


.. _import_base:

Importing an Environment
===========================

To import a new Environment resource (i.e. a disk image that already contains a bootable operating system), 
select "Import Environment" on the "Import Resources" menu.

.. image:: images/create_base_environment.png

Choose the most appropriate system for the environment from the available dropdown menu. These options are provided
:term:`Hardware Configurations <Hardware Configuration>` that will determine the emulator program and settings EaaSI
uses for this environment (the displayed "System Properties" will change accordingly).

.. image:: images/generic_pc_system.png

Under the "Disk" section, copy the HTTP link to the base image file (accepted disk image types are raw/dd, VDI, E01/EWF
and QCOW2; VHD and VDMK are also accepted but will be converted to QCOW2). If importing from a cloud storage service,
this *must* be a direct link; consult your service's sharing settings.

.. note::
  If importing an EWF image, this must be contained in a single E01 file. Multi-file forensic images are not supported.

If the Base Environment is running a KVM-compatible operating system (e.g. Windows XP), you can enable virtualization
here.

If a specific ROM file is needed to run the environment (e.g. for Apple/Mac operating systems), contact the EaaSI team
for instructions.

The "Native Config" field will specify the actual flags/options passed to the underlying emulator according to the
selected Hardware Configuration template. You can edit the Hardware Configuration here accordingly (consult each
:ref:`emulator's <emulators>`) documentation for available options.

.. image:: images/native_config.png

Click "Start" to begin the import process. The base image will first be cached into EaaSI's temporary storage. Once the
base image has been cached, an emulation session will load to allow the user to preview the new environment before
saving. The length of the import process will depend on the size of the base image, data rate and bandwidth of the
local network, etc.

When the user is satisfied with the new environment's operation, shut down the emulated operating system and select
"Save Environment" from the Action Menu. When the new base has been named, described and saved, it will be available in
the *Private* sub-section of the Base Environments overview.


Importing Emulators
====================

Please see :ref:`managing_emulators` for more detailed instructions on managing and importing new emulators into an EaaSI
node.
