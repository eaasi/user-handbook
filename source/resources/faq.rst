.. FAQ

FAQ
***

EaaSI Program of Work
======================

**Q: Are EaaSI and EaaS the same thing?**

A: Not exactly!

Emulation-as-a-Service (EaaS) is an open source software stack, originally developed by the `bwFLA <http://eaas.uni-freiburg.de/>`_
project at the University of Freiburg, now maintained by OpenSLX. It allows for emulated computing environments to be
assembled, configured and accessed via a modern web browser.

EaaSI is shorthand for the Scaling Emulation and Software Preservation Infrastructure program of work. The EaaSI project has two key components:

  1. The **core EaaSI software** provides an improved EaaS interface with an updated User Interface, extensive metadata capture, search, and browse features and workflows, user and content access management features and workflows, Virtual Reading Room features and workflows, and the Universal Virtual Interactor (UVI) algorithms and workflows. While compared to previous options, the EaaSI software provides much improved emulator administration, management and access interface, it is fairly complicated software to install, configure, and run in a large scale production capacity.  Most significantly, acquiring, installing, configuring and documenting legacy software is also a huge challenge, as it can take detailed knowledge of hardware settings and software configurations to make it all work seamlessly. For these reasons a core outcome of the EaaSI Program of work has been the creation of the EaaSI Network.

  2. The **EaaSI Network** greatly simplifies engagement with emulation as it avoids each organization having to acquire, install, configure and document legacy software and instead gives them access to working versions via a simple replication process. Members of the EaaSI Network also have access to end-user and technical support for configuring and running the EaaSI software as well as training opportunities facilitated by the EaaSI team. The EaaSI team members at Yale are seeding the network with a large number of software titles pre-configured in working emulated environments and other nodes (EaaSI installation hosts) are populating the network with software titles from domains related to their collecting focus.

**Q: (How) is this legal?**

A: EaaSI adheres to principles of fair use for academic, cultural, and non-profit institutions as recommended by the SPN-affiliate
project `Code of Best Practices for Fair Use in Software Preservation <https://www.softwarepreservationnetwork.org/bp-fair-use/>`_.
Our network's members have countless files in digital collections that are inaccessible without appropriate software -
by sharing our acquired *software* collections (with measures for network authentication and object control baked in to
our platform), we can offer long-term access to these files for scholarly research and discovery in cases where current
commercial options no longer functionally or contextually support them.

We also rely on the provisions of the 2018 DMCA exemption for software preservation in cases where legacy software DRM
might otherwise prevent us from exercising right to fair use. Please see the
`Preservationist's Guide to the DMCA Exemption for Software Preservation <http://softwarepn.webmasters21.com/wp-content/uploads/2019/01/2018-12_DMCAchecklist_updated_12132018.pdf>`_
for more details and guidance.

These guidelines are dependent on United States copyright law - EaaSI network :term:`node hosts <node>` are therefore
currently limited to US-based institutions. Along with our SPN colleagues, we are actively exploring possibilities for
international partnership, including cross-compatibility between U.S. fair use and "fair dealing" in Commonwealth nations; creating localized EaaSI networks in other nations; how US-hosted storage might affect the legal framework of the Network, etc.

**Q: Can EaaSI emulate (Amiga, Mac OS, Commodore, DOS, Atari...)?**

A: EaaSI is a platform that allows for configuring, sharing and accessing emulated environments - but the emulation
itself relies on a number of underlying open source :ref:`emulation projects <emulators>`. Whatever legacy systems
those programs are compatible with, EaaSI should be as well!

Emulators are containerized by the EaaSI development team to allow for easily popping in new emulators, or multiple
versions of the same emulator, into an installation to expand and optimize its legacy hardware and software
compatibility.

**Q: How can I get involved with EaaSI?**

A: There are lots of options, depending on your level of capacity and interest!

- Join the `EaaSI Community Forum <https://forum.eaasi.cloud>`_! The Forum is open to all interested in software preservation as well as using emulation for preservation purposes. Using the Forum you can track EaaSI project announcements, ask questions of existing users, and join or start community discussions around emulation projects and legacy software.

- Join the `Software Preservation Network <https://www.softwarepreservationnetwork.org>`_! If you are interested in joining an active and healthy community of practice that is focused on software preservation and emulation, and/or, if you are interested in testing the **EaaSI beta hosted service in 2021** (rather than hosting your own node or standing up your own infrastructure), join the Software Preservation Network. Please reach out to us at `eaasi@yale.edu <mailto:eaasi@yale.edu>`_ to learn more.  

- Encourage local and regional colleagues to play in the `EaaSI Open Source Sandbox <https://eaasi-sandbox.softwarepreservationnetwork.org/eaasi/#/portal/welcome>`_! The sandbox is currently limited to open source software and does not have the updated administrative interface, but it does give everyone a chance to interact with emulated environments and helps users understand the core functionality of EaaSI.

- Try out the :ref:`demo <container_setup>` EaaSI alpha installation. While we can’t provide end-user support for this right now, there is documentation in this Handbook and we’re working on additional community-driven support options.

- The `EaaSI project site <https://www.softwarepreservationnetwork.org/projects/emulation-as-a-service-infrastructure/>`_ is home to Capacity-Building Templates, Presentations, and more. After playing in the sandbox, or trying the demo installation, encourage practitioners within local/regional organizations to walk through these capacity building exercises (e.g. assessing emulation needs in your collections) with key organizational partners, compare notes, convene a conversation. We are building a body of data resulting from these capacity-building exercises that spans organizational types, geographies, and sizes. This data is synthesized on a rolling basis in order to have up-to-date information about where the software preservation and emulation community writ large should dedicate its energy and attention. These exercises are usually meant to be completed in pairs, or completed on behalf of a single organization or single unit/department and then compared with colleagues in other organizations or other units/departments.

- We have Environment Creation Office Hours every other week where network participants can show up and work alongside one another in the configuration of base environments. Joining information is available in the `Forum <https://forum.eaasi.cloud/t/environment-creation-office-hours-zoom-info/57>`_!

- If you are a member or representative of a professional community or association that you think would be interested in EaaSI - while we cannot provide end-user support to those outside the Network at this time, we are happy to join periodic or ad hoc community calls to provide technical overviews, share demos, and answer questions.

- Partner with SPN on an international grant project on the legal framework for sharing software and emulation environments across borders. As described above, the EaaSI network is currently limited to countries with an equivalent of “fair use” (US) or “fair dealing” (Canada). SPN is driving the law and policy agenda to expand lawful preservation and reuse of software and is currently seeking collaborators for a grant project that will determine the legal basis for an international EaaSI network. This project will explore the terms of existing international treaties, as well as, compare legal tools available in three distinct intellectual property regimes. Please let `Jessica Meyerson <mailto:jessica@educopia.org>`_ know if you are interested in collaborating.


Technical Concerns
===================

**Q: How long should an environment take to boot (on average)?**

A: That will depend on a few factors, mainly:

  1. Is the environment locally stored/cached, or remote (hosted by another node)?
  2. What computing resources (CPU, RAM) have been assigned to that environment's :term:`hardware configuration`?
  3. The size of the environment's base disk image(s)
  4. The strength/bandwidth of your network connection

The emulation session will load and boot much faster if the environment's disk image is already in 
storage connected to the local :term:`image archive` and cached on the Emulation Component (i.e. the configured server in the EaaSI stack that actually performs the emulation). So an environment that is being run for the first time in days (weeks, etc.) may load slower than subsequent, immediate attempts to run.

From there, a legacy operating system's boot time might be improved marginally by assigning that environment more RAM
or processor power in the emulated hardware configuration. EaaSI staff have striven to create base environments that
accurately reflect contemporary hardware for the target operating system, but there is obviously much wiggle room
within those lines. If employing this strategy to optimize environments, keep legacy system requirements and
compatibility in mind to avoid unexpected software behavior.

Generally speaking, environments based on older operating systems will load faster than more recent systems,
since the average size of operating systems, applications, and user data/files have grown along with the capacity of
storage media. Particularly when dealing with newer operating systems, EaaSI staff recommend setting up
staying as conservative as possible when setting up base environments (e.g. selecting "minimal" install options) to
minimize the amount of data that needs to get moved around the Network or streamed to client browsers and speed up
response time.


**Q: Your legacy software environments can connect to the live internet...are there malware or security concerns?**

A: Sure, but no more so than on any other modern computing system.

There are a few layers of this question: first, the possibility of encountering legacy malware that target our
historical operating systems somewhere still hosted on the live web. Since updates to internet protocols and web
security (e.g. HTTPS, changes to JavaScript) have made the vast majority of the live web incompatible with legacy
browsers in the first place, it's not exactly likely. But employ the same kind of healthy and skeptical browsing
habits that you bring to the modern web on your own computer and you'll be fine.

Also keep in mind the layers involved in emulated systems and in EaaSI specifically: emulation sessions are written and
stored as changes from a base image, so until an EaaSI user intentionally clicks "Save Environment", the results of a
session are not saved *at all*. Somehow manage to download `Festering Hate <https://en.wikipedia.org/wiki/Festering_Hate>`_?
Leave the session immediately and the virus' data, along with any changes to your system during that session, will be
discarded.

Even if you do somehow save an infected environment, the damage should be isolated to that environment/image. To have
any effect outside the emulated environment, the malware would have to bridge out of the "guest" operating system to
the "host" system running the EaaSI platform - a fully up-to-date, modern, secure OS, managed by our node system
administrators. Legacy malware just wasn't written to behave or be effective this way. And in any case, our emulated environments
(and the EaaSI platform itself) are further deployed on host systems via Docker containers, which provides even another layer of network protection
between any emulated environment and your host network.

The more likely concern would be modern malware and vulnerabilities that are specifically designed to target emulation
and virtualization platforms. Again, most legacy web browsers likely couldn't even access the places where these
vulnerabilities are exploited. But this is also one part of our motivation in containerizing the emulators underlying
EaaSI: to allow them to be easily updated to account for security updates from these projects. The EaaS development
team will regularly Docker-ize new releases of QEMU and others to ease and encourage this process.

In other words, just as you should regularly update your modern operating system and applications, EaaSI will too!
