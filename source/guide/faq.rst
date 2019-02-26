.. FAQ

FAQ
***

**Q: Are EaaSI and EaaS the same thing?**

A: Not exactly!

Emulation-as-a-Service (EaaS) is an open source software stack, originally developed by the `bwFLA <http://eaas.uni-freiburg.de/>`_ project at the University of Freiburg, now maintained by OpenSLX. It allows for emulated computing environments to be assembled, configured and accessed via a modern web browser.

EaaSI is shorthand for the Scaling Emulation and Software Preservation Infrastructure program of work. It refers to our series of projects collectively aiming to expand preservation, access and use of legacy software and digital objects via emulation and a shared network of resources, services and labor. That *includes* a custom EaaSI "flavor" of EaaS that suits the needs of our distributed network, but also includes documentation, front-end access services, improving metadata schema for cataloging software, community outreach and more.

**Q: (How) is this legal?**

A: EaaSI adheres to principles of fair use for academic and cultural institutions as recommended by the SPN-affiliate project `Code of Best Practices for Fair Use in Software Preservation <https://www.softwarepreservationnetwork.org/bp-fair-use/>`_. Our network's members have countless files in digital collections that are inaccessible without appropriate software - by sharing our acquired *software* collections (with measures for network authentication and object control baked in to our platform), we can offer long-term access to these files for scholarly research and discovery in cases where current commercial options no longer functionally or contextually support them.

We also rely on the provisions of the 2018 DMCA exemption for software preservation in cases where legacy software DRM might otherwise prevent us from exercising our fair use. Please see the `Preservationist's Guide to the DMCA Exemption for Software Preservation <http://softwarepn.webmasters21.com/wp-content/uploads/2019/01/2018-12_DMCAchecklist_updated_12132018.pdf>`_ for more details and guidance.

These guidelines are dependent on United States copyright law - EaaSI network :term:`node hosts <node>` are therefore currently limited to US-based institutions.

**Q: Can EaaSI emulate (Amiga, Mac OS, Commodore, DOS, Atari...)?**

A: EaaSI is a platform that allows for configuring, sharing and accessing emulated environments - but the emulation itself relies on a number of underlying open source :ref:`emulation projects <emulators>`. Whatever legacy systems those programs are compatible with, EaaSI should be as well!

Emulators are containerized by the EaaSI development team to allow for easily popping in new emulators, or multiple versions of the same emulator, into an installation to expand and optimize its legacy hardware and software compatibility.

**Q: How long should an environment take to boot (on average)?**

A: That will depend on a few factors, mainly:

  1. Is the environment locally stored/cached, or remote (hosted by another node)?
  2. What computing resources (CPU, RAM) have been assigned to that environment's :term:`hardware configuration`?

The former will have the most noticeable results: the emulation session will load and boot much faster if the base environment's disk image is already in storage connected to the local :term:`image archive`.
[gif of Win98 booting locally, ~10-15 seconds?]

Otherwise, the base image must first be fetched over HTTP from the remote node's storage, which will slow loading (variably, depending on network bandwidth, data rates, the size of the image, etc.)
[gif of Win98 booting remotely, ~30 seconds or more]

After being run once, a remote environment will load faster on subsequent boots as long as that environment image remains in the local cache, but caches will be cleared periodically and possibly unpredictably, so this is not a recommended strategy for optimization.

From there, a legacy operating system's boot time might be improved marginally by assigning that environment more RAM or processor power in the emulated hardware configuration. EaaSI staff have striven to create base environments that accurately reflect contemporary hardware for the target operating system, but there is obviously much wiggle room within those lines. If employing this strategy to optimize environments, keep legacy system requirements and compatibility in mind to avoid unexpected software behavior.


**Q: How do I get a direct link to an environment for sharing?**
