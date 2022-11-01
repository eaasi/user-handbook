.. Notes about importing complex file sets

.. _import_file_sets:

Importing File Hierarchies
============================

Currently, :ref:`importing <import_content>` arbitrary sets of files into EaaSI as a "Files"-type object (whether Software or Content) is only supported if the file set is "flat"; that is, it is not possible to select a *directory* as part of the file set, only a series of individual files.

This is unideal for either:

1. Extremely large file sets where manual or drag-and-drop file selection would be cumbersome
2. File sets with nested directories where it is essential to preserve the directory structure/file hierarchy for proper function or interaction in an emulated Environment.

As a work-around, the EaaSI team currently recommends packaging such complex file/directory sets locally as an ISO disk image and then importing to EaaSI as an "ISO"-type Software or Content object.

The EaaSI platform uses the Linux tool `mkisofs <https://linux.die.net/man/8/mkisofs>`_ to package and mount flat "Files"-type objects in emulation. For maximum compatibility across emulated guests, the EaaSI team recommends doing the same, using the following command:

  .. code-block:: sh

    $ mkisofs -J -r -hfs -o [output_filename.iso] [/path/to/target/directory]`

Where:

    - ``-J``: generates Joliet directory records in addition to ISO9660 file names (primarily useful for using in Windows 9x/NT systems)
    - ``-r``: generates Rock Ridge file ownership permissions on the ISO9660 file system (clears ownership information from your system that may/will conflict with user information in emulated Environments)
    - ``-hfs``: generates a hybrid ISO9660/HFS CD system (required to properly mount in classic Mac OS systems)
    - ``-o [output_filename.iso]``: the specified name for your output/new ISO disk image
    - ``/path/to/target/directory``: the file path to the directory (including any nested files and sub-directories) that you would like package and upload as an EaaSI object

``mkisofs`` can be installed on macOS by installing the ``cdrtools`` package via `Homebrew <https://brew.sh>`_; on Windows the EaaSI team recommends either installing ``mkisofs`` via the `Windows Subsystem for Linux <https://learn.microsoft.com/en-us/windows/wsl/about>`_ or using the `xorriso-for-windows <https://github.com/PeyTy/xorriso-exe-for-windows>`_ tool, which maintains cross-compatibility with ``mkisofs`` syntax.