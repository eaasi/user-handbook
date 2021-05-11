.. FAQ

FAQ
***

.. contents:: Table of Contents
  :depth: 3

EaaSI Program of Work
=======================

Are EaaSI and EaaS the same thing?
---------------------------------------

Not exactly!

Emulation-as-a-Service (EaaS) is an open source software stack, originally developed by the `bwFLA <http://eaas.uni-freiburg.de/>`_ project at the University of Freiburg, now maintained by OpenSLX. It allows for emulated computing environments to be assembled, configured and accessed via a modern web browser.

EaaSI is shorthand for the Scaling Emulation and Software Preservation Infrastructure program of work. The EaaSI project has two key components:

| 1. The **core EaaSI platform** builds on EaaS while adding or expanding on certain pieces of functionality. For instance, the EaaSI program of work sponsored the development and addition of OAI-PMH resource exchange between separate installations of EaaS. It also designed and implemented a new EaaSI Client, updating the EaaS user interface for a more intuitive experience. Further development in this area might include but is not limited to: the Universal Virtual Interactor (an API for automated search and interaction with EaaSI resources), a Virtual Reading Room service (additions to the EaaSI Client allowing for more granular user management, permissions and patron access).
|
| 2. The **EaaSI Network** is a community collaboration. It greatly simplifies engagement with emulation as it avoids each organization having to acquire, install, configure and document legacy software and instead gives them access to working versions via a simple replication process. Members of the EaaSI Network also have priority access to end-user and technical support, as well as training opportunities facilitated by the EaaSI team. The EaaSI team members at Yale are seeding the Network with a large number of software titles pre-configured in working emulated|environments, while other nodes (participating organizations) investigate software titles in their |own domains of collection. EaaSI Network members also have priority for feedback and guidance on |the future direction of the EaaSI program of work.

|

(How) is this legal?
---------------------

EaaSI adheres to principles of fair use in United States copyright law, as recommended for academic, cultural, and non-profit institutions by the SPN-affiliate project `Code of Best Practices for Fair Use in Software Preservation <https://www.softwarepreservationnetwork.org/bp-fair-use/>`_.
Our Network's members have countless files in digital collections that are inaccessible without appropriate software - by sharing our acquired *software* collections (with measures for network authentication and object control baked in to our platform), we can offer long-term access to these files for scholarly research and discovery in cases where current commercial options no longer functionally or contextually support them.

We also rely on the provisions of the 2018 DMCA exemption for software preservation in cases where legacy software DRM might otherwise prevent us from exercising right to fair use. Please see the
`Preservationist's Guide to the DMCA Exemption for Software Preservation <http://softwarepn.webmasters21.com/wp-content/uploads/2019/01/2018-12_DMCAchecklist_updated_12132018.pdf>`_
for more details and guidance.

These guidelines are dependent on United States copyright law - EaaSI Network :term:`node hosts <node>` are therefore currently limited to US-based servers. We are actively exploring possibilities for international partnership, including cross-compatibility between U.S. fair use and "fair dealing" in Commonwealth nations, and assisting the creation of localized EaaSI networks elsewhere in the world.

|

How can I get involved with EaaSI?
-----------------------------------

There are lots of options, depending on your level of capacity and interest!

|   - Join the `EaaSI Community Forum <https://forum.eaasi.cloud>`_! The Forum is open to all interested in software preservation as well as using emulation for preservation purposes.
|
|   - Join the `Software Preservation Network <https://www.softwarepreservationnetwork.org>`_! If you are interested in joining an active and healthy community of practice that is focused on software preservation and emulation.
|
|   - Encourage local and regional colleagues to play in the `EaaSI Open Source Sandbox <https://eaasi-sandbox.softwarepreservationnetwork.org/eaasi/#/portal/welcome>`_! The sandbox is currently limited to open source software and does not have the updated EaaSI Client, but it does give everyone a chance to interact with emulated environments and helps users understand the opportunities offered by EaaSI.
|
|   - :ref:`container_setup`, with our self-contained demo EaaSI Docker deployments. (See :ref:`demo_client` for using the "Try EaaSI" interface)
|
|   - Check out the `EaaSI project site <https://www.softwarepreservationnetwork.org/projects/emulation-as-a-service-infrastructure/>`_! Our site is home to Capacity-Building Templates, Presentations, Training Modules, Roundtable discussion recordings, and more, all designed to educate and engage digital preservation practictioners in the problems EaaSI is trying to address.
|
|   - Request a demo or presentation! If you are a member or representative of a professional community or association that you think would be interested in EaaSI - we are happy to join periodic or ad hoc community calls to provide technical overviews, share demos, and answer questions as capacity allows. (Please email eaasi@yale.edu for details)
|
|   - Partner with SPN on an international grant project on the legal framework for sharing software and emulation environments across borders. SPN is currently seeking collaborators for a grant project that will determine the legal basis for an international EaaSI network. This project will explore the terms of existing international treaties, as well as compare legal tools available in three distinct intellectual property regimes. Please let `Jessica Meyerson <mailto:jessica@educopia.org>`_ know if you are interested in collaborating.

|

Technical Concerns
===================

Can EaaSI emulate (Amiga, Mac OS, Commodore, DOS, Atari...)?
---------------------------------------------------------------

EaaSI is a platform that allows for configuring, sharing and accessing emulated environments - but the emulation
itself relies on a number of underlying open source :ref:`emulation projects <emulators>`. In theory, any Linux-compatible open-source emulator can be incorporated into EaaSI, along with the hardware it is meant to recreate.

However, to be incorporated into EaaSI, emulators must be configured and containerized in a particular configuration to communicate with the EaaS framework. If you are interested in emulating a particular hardware system or incorporating a specific emulator not mentioned in this Handbook, please contact the EaaSI team for guidance.

|

How long should an environment take to boot (on average)?
----------------------------------------------------------

That will depend greatly on a few factors, mainly:

  #. Has the environment already been run recently on the same node? (is it cached)
  #. What computing resources (CPU, RAM) have been assigned to that environment's :term:`hardware configuration`?
  #. The size of the environment's base disk image(s)
  #. The strength/bandwidth of your network connection

The emulation session will load and boot much faster if the environment's disk image has already been cached on the Emulation Component from storage. So an environment that is being run for the first time in days (weeks, etc.) may load slower than subsequent, immediate attempts to run.

From there, a legacy operating system's boot time might be improved by assigning more computing resources to the emulated Environment. EaaSI staff have striven to create emulated hardware configurations that accurately reflect contemporary real-life hardware for the target operating systems, but there is obviously much wiggle room within those lines. Assigning more RAM or CPU cores, or enabling KVM (on :ref:`compatible <enable-kvm>` Environments) in the emulator configuration may improve response time. Be careful with this strategy though - keep legacy system requirements and compatibility in mind to avoid unexpected behavior.

Generally speaking, environments based on older operating systems will load faster than more recent systems, since the average size of operating systems, applications, and user data/files have grown along with the capacity of storage media. The bigger the operating system, to longer it will take to cache the Environment from storage to the EmuComp.

Finally, the emulator's video output is streamed from the EmuComp server to your web browser over HTTP. As with any streaming media service, the performance may be affected by the strength of your network connection, affecting the user's perceived loading and response times (e.g. booting screens may *appear* to take longer as the monitor output is streamed from the EmuComp to your browser, or mouse and keyboard input may lag). A stable, wired internet connection should be preferred if available.

|

Your legacy software environments can connect to the live internet...are there malware or security concerns?
------------------------------------------

Sure, but no more so than on any other modern computing system.

There are a few layers of this question: first, the possibility of encountering legacy malware that target our historical operating systems somewhere still hosted on the live web. Since updates to internet protocols and web security (e.g. HTTPS, changes to JavaScript) have made the vast majority of the live web incompatible with legacy browsers in the first place, this is not likely. But employ the same kind of healthy and skeptical browsing habits that you bring to the modern web on your own computer and you'll be fine.

Also keep in mind the layers involved in emulated systems and in EaaSI specifically: emulation sessions are written and stored as changes from a base disk image, so until an EaaSI user intentionally clicks "Save Environment", the results of a session are not saved *at all*. If you somehow managed to unintentionally download `Festering Hate <https://en.wikipedia.org/wiki/Festering_Hate>`_, just leave the emulation session immediately and the virus' data, along with any changes to your system during that session, will be discarded.

Even if you do somehow save an infected environment, the damage should be isolated to that environment/image. To have any effect outside the emulated environment, the malware would have to bridge out of the "guest" operating system to the "host" system running the EaaSI platform - a fully up-to-date, modern, secure OS, managed by your node's system administrators. Legacy malware just wasn't written to behave or be effective this way. And in any case, our emulated environments (and the EaaSI platform itself) are further deployed on host systems via Docker containers, which provides even another layer of network isolation between any emulated environment and your local network.

The most likely concern would be modern malware and vulnerabilities that are specifically designed to target emulation and virtualization platforms. Again, most legacy web browsers likely couldn't even access the sites where these vulnerabilities are exploited. But this is also another part of the motivation in containerizing many of the modules and emulators underlying EaaSI: to allow them to be easily updated to account for security updates. The EaaS development team regularly updates components to account for secure releases.

In other words, just as you should regularly update your own operating system and applications, EaaSI will too!

|

Can I take screenshots or video of Software or Content running in emulation?
--------------------------------------------

EaaSI's Emulation Access interface has a built-in feature for taking screenshots of the currently-running emulation. Video is not available out-of-the-box at this time.

|

What is the difference between saving a "New Environment" or a "Revision" from an existing Environment?
----------------------------------------------

The choice affects how the resource is presented to users in the EaaSI Client. 

Choosing a "new environment" creates an entirely new resource card anywhere resources are visible in the Client (the Explore Resources or My Resources pages, for example). The original Environment will *also* still have an entry. The new Environment will be Private by default.

Choosing "revision" does not create a new resource card - instead it updates and overrides the current resource card.

(**This is only true** if the original Environment was a **Private** resource, not published to the EaaSI Network. If the original Environment was a Public + Saved Locally Environment, selecting "revision" will have **the same** effect as "new environment", and a new resource card will be created for the revision.)

In both cases, Emulation-as-a-Service creates a derivative QCOW disk image file to represent and save the changes to the original Environment, whether the changes are *presented* as a new Environment or as a revision. So revisions can still be easily reverted by consulting the History tab on the Environment's details page and creating a fork at the point of the original Environment.
