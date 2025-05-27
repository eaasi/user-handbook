.. FAQ

FAQ
***

.. contents:: Table of Contents
  :depth: 3

Technical Concerns
===================

Can EAASI emulate (Amiga, Mac OS, Commodore, DOS, Atari...)?
---------------------------------------------------------------

EAASI is a platform that allows for configuring, sharing and accessing emulated environments - but the emulation
itself relies on a number of underlying open source :ref:`emulation projects <emulators>`. In theory, any Linux-compatible open-source emulator can be incorporated into EAASI, along with the hardware it is meant to recreate.

However, to be incorporated into EAASI, emulators must be configured and containerized in a particular configuration to communicate with the EaaS framework. We are currently limited to:

- 8-bit Commodore series machines (PET, VIC, Commodore 64, etc.), via VICE
- late Motorola 68k-series Macintoshes, via BasiliskII
- PowerPC-series Macs, via SheepShaver or QEMU
- x86 Intel systems, via QEMU

|

How long should an environment take to boot (on average)?
----------------------------------------------------------

That will depend greatly on a few factors, mainly:

  #. What computing resources (CPU, RAM) have been assigned to that environment's :term:`hardware configuration`?
  #. The size of the environment's base disk image(s)
  #. The strength/bandwidth of your network connection

A legacy operating system's boot time might be improved by assigning more computing resources to the emulated Environment. EAASI staff have striven to create emulated hardware configurations that accurately reflect contemporary real-life hardware for the target operating systems, but there is obviously much wiggle room within those lines. Assigning more RAM or CPU cores, or enabling KVM (on :ref:`compatible <enable-kvm>` Environments) in the emulator configuration may improve response time. Be careful with this strategy though - keep legacy system requirements and compatibility in mind to avoid unexpected behavior.

Generally speaking, environments based on older operating systems will load faster than more recent systems, since the average size of operating systems, applications, and user data/files have grown along with the capacity of storage media. The bigger the operating system, to longer it will take to cache the Environment from storage to the EmuComp.

Finally, the emulator's video output is streamed from the EmuComp server to your web browser over HTTP. As with any streaming media service, the performance may be affected by the strength of your network connection, affecting the user's perceived loading and response times (e.g. booting screens may *appear* to take longer as the monitor output is streamed from the EmuComp to your browser, or mouse and keyboard input may lag). A stable, wired internet connection should be preferred if available.

|

Your legacy software environments can connect to the live internet...are there malware or security concerns?
-----------------------------------------------------------------------------------------------------------------------

Sure, but no more so than on any other modern computing system.

There are a few layers of this question: first, the possibility of encountering legacy malware that target our historical operating systems somewhere still hosted on the live web. Since updates to internet protocols and web security (e.g. HTTPS, changes to JavaScript) have made the vast majority of the live web incompatible with legacy browsers in the first place, this is not likely. But employ the same kind of healthy and skeptical browsing habits that you bring to the modern web on your own computer and you'll be fine.

Also keep in mind the layers involved in emulated systems and in EAASI specifically: emulation sessions are written and stored as changes from a base disk image, so until an EAASI user intentionally clicks "Save Environment", the results of a session are not saved *at all*. If you somehow managed to unintentionally download `Festering Hate <https://en.wikipedia.org/wiki/Festering_Hate>`_, just leave the emulation session immediately and the virus' data, along with any changes to your system during that session, will be discarded.

Even if you do somehow save an infected environment, the damage should be isolated to that environment/image. To have any effect outside the emulated environment, the malware would have to bridge out of the "guest" operating system to the "host" system running the EAASI platform - a fully up-to-date, modern, secure OS, managed by your server's system administrators. Legacy malware just wasn't written to behave or be effective this way. And in any case, our emulated environments (and the EAASI platform itself) are further deployed on host systems via Docker containers, which provides even another layer of network isolation between any emulated environment and your local network.

The most likely concern would be modern malware and vulnerabilities that are specifically designed to target emulation and virtualization platforms. Again, most legacy web browsers likely couldn't even access the sites where these vulnerabilities are exploited. But this is also another part of the motivation in containerizing many of the modules and emulators underlying EAASI: to allow them to be easily updated to account for security updates. The EaaS development team regularly updates components to account for secure releases.

In other words, just as you should regularly update your own operating system and applications, EAASI will too!

|

Can I take screenshots or video of Software or Content running in emulation?
-----------------------------------------------------------------------------

EAASI's Emulation Access interface has a built-in feature for taking screenshots of the currently-running emulation. Video is not available out-of-the-box at this time.

|

What is the difference between saving a "New Environment" or a "Revision" from an existing Environment?
----------------------------------------------------------------------------------------------------------

The choice affects how the resource is presented to users in the EAASI Teleport web app. 

Choosing a "new environment" creates an entirely new resource card anywhere resources are visible in Teleport (the Explore Resources or My Resources pages, for example). The original Environment will *also* still have an entry. The new Environment will be Private by default.

Choosing "revision" does not create a new resource card - instead it updates and overrides the current resource card.

In both cases, Emulation-as-a-Service creates a :term:`derivative` disk image file to represent and save the changes to the original Environment, whether the changes are *presented* as a new Environment or as a revision. Revisions can still be easily reverted by consulting the History tab on the Environment's details page and creating a fork at the point of the original Environment.
