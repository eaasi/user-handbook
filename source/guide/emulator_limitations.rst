.. Features limited because of underlying emulators

.. _emulator_limitations:

Emulator Limitations
======================

While Emulation-as-a-Service and the EaaSI platform provide a centralized, single interface for interacting with a number of different underlying :ref:`emulators`, variations between these different applications make it difficult if not impossible to have all EaaSI features work in the same way for all Environments.

This page details some of these limitations, along with recommended work-arounds, to help manage user expectations.

Multi-file Content and Software resources and "Change Media" in Apple Environments
-----------------------------------------------------------------------------------

**Relevant emulators**: Basilisk II, SheepShaver

**Affected Environments**: approximately Apple Mac OS 7.x through OS 9.0.4 (late M68K and PowerPC Macs)

**Problem**: Basilisk and SheepShaver do not support live-swapping mounted disk images during a running emulation session. All desired disk images for a session must be selected and mounted before or between running the emulation. Thus, the "Change Media" feature **will not function** as expected when running Basilisk or SheepShaver-based Environments in EaaSI - users can not "eject" and "insert" disk images in multi-file Floppy or ISO type Content and Software resources, the way they would with physical hardware (or with emulators that support live-swapping, such as QEMU, LinApple, VICE, etc.)

**Recommended work-around**: EaaSI users can edit the number of disk images that can be mounted at any one time into a Basilisk or SheepShaver-based Environment by adjusting the Environment's Configured Drives on its Details page. Adding additional Floppy or CDROM drives to match or exceed the number of disk images in a multi-Floppy or ISO-type resource should allow the entire resource to be mounted into the Environment at the same time when run.

Because of hardware limitations (Basilisk and SheepShaver emulate a particular SCSI bus), this method will only work for up to a maximum of 8 drives (including, if relevant, the main/system disk contining the operating system).

Alternatively, break a multi-file Content or Software resource into multiple or individual resources during import. (e.g. treat each individual Floppy or ISO-type disk image as its own separate resource, then mount and save in a series of Environment revisions until the complete desired set is available for interaction)


Floppy Objects (Content or Software) of Mixed Size in QEMU
------------------------------------------------------------

**Relevant emulators**: QEMU

**Affected Environments**: MS-DOS, Windows, and most Linux environments (x86 PCs)

**Problem**: QEMU can switch between Floppy-type objects during a running emulation session, but they must all be of the same size. For instance, if a user uploads a Floppy-type Content object mixing disk images from 5.25" and 3.5" floppies - respectively 1.2 MB and 1.44 MB - the user will **not** be able to swap between them using the Change Media feature in a running QEMU-based Environment. Whichever file was ranked/prioritized first in the Software or Content import will determine the capacity of the emulated floppy drive when that resource is mounted.

**Recommended work-around**: If looking to import a mixed-size floppy set into EaaSI as a Content or Software resource, separate disk images of the same size into separate resources. Copy and save one of the resources into a QEMU-based Environment, then mount the second resource interact with the full set.

Alternatively, if it is possible or acceptable: manipulate the size of a disk image prior to import into EaaSI (e.g. padding a smaller disk image to match the size of a larger one) using a disk image manipulation program such as `WinImage <https://winimage.com/>`_, `qemu-img <https://linux.die.net/man/1/qemu-img>`_ (built-in QEMU utility), or similar.
