.. FAQ

FAQ
***

**Q: Are EaaSI and EaaS the same thing?**

A: Not exactly!

Emulation-as-a-Service (EaaS) is an open source software stack, originally developed by the `bwFLA <http://eaas.uni-freiburg.de/>`_ project at the University of Freiburg, now maintained by OpenSLX. It allows for emulated computing environments to be assembled, configured and accessed via a modern web browser.

EaaSI is shorthand for the Scaling Emulation and Software Preservation Infrastructure program of work. It refers to our series of projects collectively aiming to expand preservation, access and use of legacy software and digital objects via emulation and a shared network of resources, services and labor. That *includes* a custom EaaSI "flavor" of EaaS that suits the needs of our distributed network, but also includes documentation, front-end access services, improving metadata schema for cataloging software, community outreach and more.

**Q: (How) is this legal?**

A: EaaSI adheres to principles of fair use for academic and cultural institutions as recommended by the SPN-affiliate project `Code of Best Practices for Fair Use in Software Preservation <https://www.softwarepreservationnetwork.org/bp-fair-use/>`_. Our network's members have countless files in digital collections that are inaccessible without appropriate software - by sharing our acquired *software* collections (with measures for network authentication and object control baked in to our platform), we can offer long-term access to these files for scholarly research and discovery in cases where current commercial options no longer functionally or contextually support them.

We also rely on the provisions of the 2018 DMCA exemption for software preservation in cases where legacy software DRM might otherwise prevent us from exercising right to fair use. Please see the `Preservationist's Guide to the DMCA Exemption for Software Preservation <http://softwarepn.webmasters21.com/wp-content/uploads/2019/01/2018-12_DMCAchecklist_updated_12132018.pdf>`_ for more details and guidance.

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


**Q: Your legacy software environments can connect to the live internet...are there malware or security concerns?**

A: Sure, but no more so than on any other modern computing system.

There are a few layers of this question: first, the possibility of encountering legacy malware that target our historical operating systems somewhere still hosted on the live web. Since updates to internet protocols and web security (e.g. HTTPS, changes to JavaScript) have made the vast majority of the live web incompatible with legacy browsers in the first place, it's not exactly likely. But employ the same kind of healthy and skeptical browsing habits that you bring to the modern web on your own computer and you'll be fine.

Also keep in mind the layers involved in emulated systems and in EaaSI specifically: emulation sessions are written and stored as changes from a base image, so until an EaaSI user intentionally clicks "Save Environment", the results of a session are not saved *at all*. Somehow manage to download `Festering Hate <https://en.wikipedia.org/wiki/Festering_Hate>`_? Leave the session immediately and the virus' data, along with any changes to your system during that session, will be discarded.

Even if you do somehow save an infected environment, the damage should be isolated to that environment/image. To have any effect outside the emulated environment, the malware would have to bridge out of the "guest" operating system to the "host" system running the EaaSI platform - a fully up-to-date, modern, secure OS, managed by our node system administrators. Legacy malware just wasn't written to behave or be effective this way. And in any case, EaaSI is further deployed on host systems via Docker containers, which provides even another layer of network protection between any emulated environment and your host network.

The more likely concern would be modern malware and vulnerabilities that are specifically designed to target emulation and virtualization platforms. Again, most legacy web browsers likely couldn't even access the places where these vulnerabilities are exploited. But this is also one part of our motivation in containerizing the emulators underlying EaaSI: to allow them to be easily updated to account for security updates from these projects. The EaaS development team will regularly Docker-ize new releases of QEMU and others to ease and encourage this process.

In other words, just as you should regularly update your modern operating system and applications, EaaSI will too!


**Q: How do I get a direct link to an environment for sharing?**
