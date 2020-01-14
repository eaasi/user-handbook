.. Emulators 

.. _emulators:

Emulators
=========
EaaS relies on several open source projects to actually perform emulation and virtualization.
These emulators have been containerized into Docker images by the EaaS development team to allow for easily swapping in
new emulators (or different versions of an emulator) to an EaaSI installation.

Default EaaSI deployments will come only with QEMU (v3.1) installed, but emulation capability can be quickly expanded
by replicating environments from other nodes and/or using the Emulator menu in the demo interface. Please see
:ref:`managing_emulators` for more details.

The full list of compatible and pre-Dockerized emulators prepared by the EaaS team is located and will be updated on
their `public GitLab repository <https://gitlab.com/emulation-as-a-service/emulators>`_, but immediately available for
the EaaSI network are:

- `Basilisk II <https://basilisk.cebix.net/>`_
    68k series Mac emulation

- `BeebEm <http://www.mkw.me.uk/beebem/>`_
    BBC Micro and Master 128 emulation

- `ContrAlto <https://github.com/livingcomputermuseum/ContrAlto>`_
    Xerox Alto emulation

- `FS-UAE <https://fs-uae.net/>`_
    Amiga series emulation

- `Hatari <https://hatari.tuxfamily.org/>`_
    Atari ST/STE/TT/Falcon series emulation

- `KEGS <http://kegs.sourceforge.net/>`_
    Apple IIgs emulation

- `Linapple-pie <https://github.com/dabonetn/linapple-pie/>`_
    Apple II emulation

- `Mini vMac <https://www.gryphel.com/c/minivmac/>`_
    68k series Mac emulation

- `PCE <http://www.hampa.ch/pce/about.html>`_
    Various microcomputer emulators, including Atari ST, IBM PC5150, and classic Macintosh models
    
- `Previous <https://sourceforge.net/projects/previous/>`_
    NeXT hardware emulation (NeXT Cube, NeXT Station)

- `QEMU <https://www.qemu.org/>`_
    x86 PC emulation/virtualization, PowerPC 9.1-10.x Mac OS emulation

- `SheepShaver <https://sheepshaver.cebix.net/>`_
    PowerPC Mac OS 8.x-9.0 emulation

- `VICE (Versatile Commodore Emulator) <http://vice-emu.sourceforge.net/>`_
    Commodore series emulation
