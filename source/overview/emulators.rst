.. Emulators

.. _emulators:

Emulators
=========

Emulation-as-a-Service relies on several open source projects to actually perform emulation and virtualization. These emulators have been containerized into Docker images by the EaaS development team to allow for easily swapping in new emulators (or different versions of an emulator) to an EaaSI installation.

Due to changes in the EaaS framework and ongoing development on the EaaSI Client, not all of OpenSLX's emulator images are compatible with every EaaSI release. Please consult the following compatibility matrices for matching your EaaSI deployment with appropriate or recommended emulator images that are known to function.

Please see :ref:`managing_emulators` for detailed instructions to actually import or manage emulator images in the EaaSI Client.

Compatibility
---------------

.. list-table:: PC (x86) and some PPCs
  :header-rows: 1

  * - EaaSI Build
    - `QEMU <https://hub.docker.com/r/eaas/qemu-eaas/tags/?page=1&ordering=last_updated>`_
    - `PCem <https://gitlab.com/emulation-as-a-service/emulators/pcem/container_registry/739754>`_
  * - :ref:`”Try EaaSI” Dockers <container_setup>`
    - v3-0 (recommended), v2-12
    - n/a
  * - 2019.11 and prior
    - v3-0 (recommended), v2-12, v2-5deb (some legacy installs)
    - n/a
  * - 2020.03
    - v3-0 (recommended), v2-12
    - n/a
  * - 2021.10
    - v3-0 (recommended), v2-12
    - n/a

.. list-table:: Apple
  :header-rows: 1

  * - EaaSI Build
    - `SheepShaver <https://gitlab.com/emulation-as-a-service/emulators/macemu-eaas-sheepshaver/container_registry/347346>`_
    - `Basilisk II <https://gitlab.com/emulation-as-a-service/emulators/macemu-eaas-basilisk2/container_registry/347345>`_
    - Mini vMac
  * - :ref:`”Try EaaSI” Dockers <container_setup>`
    - git-587d8376f07f94ffb594bb705e3a781b46b22d47
    - git-63b01290ef6ad143100e571b5d2f1a84ad8b870a
    - n/a
  * - 2019.11 and prior
    - git-587d8376f07f94ffb594bb705e3a781b46b22d47
    - git-63b01290ef6ad143100e571b5d2f1a84ad8b870a
    - n/a
  * - 2020.03
    - git-587d8376f07f94ffb594bb705e3a781b46b22d47
    - git-63b01290ef6ad143100e571b5d2f1a84ad8b870a
    - n/a
  * - 2021.10
    - git-587d8376f07f94ffb594bb705e3a781b46b22d47
    - git-63b01290ef6ad143100e571b5d2f1a84ad8b870a
    - n/a

.. list-table:: Other
  :header-rows: 1

  * - EaaSI Build
    - `VICE <https://gitlab.com/emulation-as-a-service/emulators/vice-eaas/container_registry/426946>`_
    - `FS-UAE <https://gitlab.com/emulation-as-a-service/emulators/fs-uae-eaas/container_registry/367681>`_
    - `Contralto <https://gitlab.com/emulation-as-a-service/emulators/contralto-eaas/container_registry/360670>`_
  * - :ref:`”Try EaaSI” Dockers <container_setup>`
    - latest
    - n/a
    - latest
  * - 2019.11 and prior
    - latest
    - n/a
    - latest
  * - 2020.03
    - latest
    - n/a
    - latest
  * - 2021.10
    - latest
    - n/a
    - latest

Links to Source Projects
--------------------------

- `QEMU <https://www.qemu.org/>`_ (x86 PC emulation/virtualization, PowerPC 9.1-10.x Mac OS emulation)
- `PCem <https://www.pcem-emulator.co.uk/>`_ (x86 PC emulation)
- `SheepShaver <https://sheepshaver.cebix.net/>`_ (PowerPC Mac OS 8.x-9.0 emulation)
- `Basilisk II <https://basilisk.cebix.net/>`_ (late 68k series Mac emulation)
- `Mini vMac <https://www.gryphel.com/c/minivmac/>`_ (late 68k series Mac emulation)
- `VICE (Versatile Commodore Emulator) <http://vice-emu.sourceforge.net/>`_ (Commodore series emulation)
- `FS-UAE <https://fs-uae.net/>`_ (Amiga series emulation)
- `ContrAlto <https://github.com/livingcomputermuseum/ContrAlto>`_ (Xerox Alto emulation)
