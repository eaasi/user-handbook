.. Emulators

.. _emulators:

Emulators
==========

Emulation-as-a-Service relies on several open source projects to actually perform emulation and virtualization. These emulators have been containerized into Docker images by the EaaS development team to allow for easily swapping in new emulators (or different versions of an emulator) to an EAASI installation.

Due to changes in the EaaS framework and ongoing development on the EAASI Client, not all of OpenSLX's emulator images are compatible with every EAASI release. Please consult the following compatibility matrices for matching your EAASI deployment with appropriate or recommended emulator images that are known to function.

Please see :ref:`managing_emulators` for detailed instructions to actually import or manage emulator images in the EAASI Client.

Compatibility
---------------

.. list-table:: PC (x86) and some PPCs
  :header-rows: 1

  * - EAASI Build
    - `QEMU <https://hub.docker.com/r/eaas/qemu-eaas/tags/?page=1&ordering=last_updated>`_
  * - 2021.10
    - v3-0 (recommended), v2-12

.. list-table:: Apple
  :header-rows: 1

  * - EAASI Build
    - `SheepShaver <https://gitlab.com/emulation-as-a-service/emulators/macemu-eaas-sheepshaver/container_registry/347346>`_
    - `Basilisk II <https://gitlab.com/emulation-as-a-service/emulators/macemu-eaas-basilisk2/container_registry/347345>`_
  * - 2021.10
    - git-587d8376f07f94ffb594bb705e3a781b46b22d47
    - git-63b01290ef6ad143100e571b5d2f1a84ad8b870a

.. list-table:: Other
  :header-rows: 1

  * - EAASI Build
    - `VICE <https://gitlab.com/emulation-as-a-service/emulators/vice-eaas/container_registry/426946>`_
    - `Contralto <https://gitlab.com/emulation-as-a-service/emulators/contralto-eaas/container_registry/360670>`_
    - `Visual Boy Advance <https://gitlab.com/emulation-as-a-service/emulators/visualboyadvance-eaas>`_
  * - 2021.10
    - latest
    - latest
    - latest

Links to Source Projects
--------------------------

- `QEMU <https://www.qemu.org/>`_ (x86 PC emulation/virtualization, PowerPC 9.1-10.x Mac OS emulation)
- `SheepShaver <https://sheepshaver.cebix.net/>`_ (PowerPC Mac OS 8.x-9.0 emulation)
- `Basilisk II <https://basilisk.cebix.net/>`_ (late 68k series Mac emulation)
- `VICE (Versatile Commodore Emulator) <http://vice-emu.sourceforge.net/>`_ (Commodore series emulation)
- `ContrAlto <https://github.com/livingcomputermuseum/ContrAlto>`_ (Xerox Alto emulation)
- `Visual Game Boy Advance <https://visualboyadvance.org/>`_ (Nintendo Game Boy Advance emulation)