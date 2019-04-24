.. Technical Requirements

System Requirements
=====================

Operating System
-----------------

The EaaSI platform can be deployed on a typical in-support Linux server distribution.

Ubuntu 16.04, 18.04 and RHEL/CentOS 7 are supported and recommended by the development team.

Hardware
----------

EaaSI can be installed on a single machine, or its components can be spread across a distributed infrastructure.

For simplicity in the initial "beta" release and testing of the network, EaaSI staff envisions and recommends
installing the system on to a single machine.

**Minimum/testing specifications:**

- 8-core CPU
- 16 GB RAM
- 10 GB disk space for application data/EaaSI system itself
- 100+ GB disk space for system resources (software, environments, digital objects), mounted to local file system

**Recommended for production:**

- 12-core CPU
- 24 GB RAM
- 10 GB disk space for application data/EaaSI system
- 300+ GB disk space for system resources

The amount of storage disk space needed is highly subjective to individual workflows, and will depend on how much remote
material you intend to contribute to or fetch from the EaaSI network. Keeping remote resources from the network locally
cached will greatly improve processing time and performance, but also requires more local storage. Likewise, publishing
resources to the network requires them to be stored on a machine with a publicly accessible IP, which may affect
storage options and strategy.

Roadmaps are in place for configuring EaaSI with full S3 object storage support, which will hopefully alleviate concern
for adjusting and expanding storage space more variably.

The minimum/testing guidelines recommend 100+ GB to ensure satisfactory performance during evaluation. Monitoring
storage use closely during the beta is highly recommended to help plan more specific storage needs in future/production
releases.

Network Accessibility
^^^^^^^^^^^^^^^^^^^^^^^
The EaaSI machine must be configured at a publicly addressable IP and able to accept HTTP requests in order for other
nodes in the network to fetch and contribute resources.

EaaSI specifically retrieves resources via HTTPS, so the machine must also be set up with a valid SSL certificate.


Virtual Machines
^^^^^^^^^^^^^^^^^^
EaaSI infrastructure can easily be deployed via VM rather than physical machines.

To allow for installation and deployment via VM, make sure that CPU flags for nested virtualization are set on the host.


Browser Compatibility
-----------------------
The EaaSI UI heavily depends on a current JavaScript implementation in the browser. Currently supported

- Firefox (v. 65+, probably a few older versions too)
- Chrome

All other current browsers (e.g. Safari, MS Edge) will work to some degree but are not well tested. There are known
issues esp. regarding audio support.

.. note:: Some browser extensions may interfere with EaaSI functionality, such as ad-blocker, popup-blocker or similar.

Software Dependencies
---------------------

.. _docker_install_section:

Docker
^^^^^^^^^^^^^^
Please follow the official instructions to install Docker on your EaaSI machine before proceeding to setup and
deployment:

- `Docker for Windows <https://docs.docker.com/docker-for-windows/install/>`_
- `Docker for Mac OS <https://docs.docker.com/docker-for-mac/install/>`_
- `Docker for Linux (Desktop & Server) <https://docs.docker.com/engine/installation/#cloud>`_



Docker Compose
^^^^^^^^^^^^^^^^^^^^^^
Docker compose is automatically installed for most Windows and Mac users. Linux users should follow `these instructions
<https://docs.docker.com/compose/install/>`_.


Host Configuration
^^^^^^^^^^^^^^^^^^^^
Certain additional steps are required to enable all EaaSI features. Core functionality will still be available without
these modifications.

In the host environment (whether that is a physical machine or VM), please check the following permissions:

- **KVM support**: make sure that the Docker user has read/write permissions to ``/dev/kvm``.
- **SELinux**: if SELinux is enabled, make sure to allow mapping low memory addresses
  (required for certain emulators, such as Sheepshaver) by running ``sudo setsebool -P mmap_low_allowed 1``
- **Writable Shared Folders**: make sure the the Docker user has write permission to shared folders.
