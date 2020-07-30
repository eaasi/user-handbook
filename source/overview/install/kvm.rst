.. Notes about KVM supports

.. _enable-kvm:

KVM Support
==============

KVM (Kernel-based Virtual Machine) is a virtualization module for Linux operating systems. KVM provides `hardware-assisted virtualization <https://en.wikipedia.org/wiki/Hardware-assisted_virtualization>`_ for compatible guest operating systems, greatly improving their performance.

If the operating systems are compatible (generally, x86-64 operating systems like Windows XP or newer, Intel x86 versions of MacOS, comparable Linux systems, etc), enabling KVM virtualization on an EaaSI environment will have a significant effect on how quickly/efficiently it runs. If KVM support is not possible or properly configured, EaaSI must fully emulate all of the guest system's hardware, which will greatly and inefficiently consume resources on the host server (at a certain point, making it largely impossible to improve the Environment's performance by assigning computing resources solely through the emulator configuration).

Besides the compatibility of the guest operating system, the ``Enable KVM`` option for Environments can be complicated by the EaaSI deployment. If the EaaSI platform has been deployed to a VM (as with most/all cloud computing providers), the VM's host machine **must** be configured to allow "nested KVM"/"nested virtualization". Otherwise, EaaSI will not actually be able to provide hardware-assisted virtualization for Environments, even if ``Enable KVM`` is selected and otherwise compatible.

If the ``Enable KVM`` option is selected for an Environment, but nested virtualization is not allowed or enabled on the EaaSI host, EaaSI will not display any error messages - it will just silently run the Environment and its selected hardware in full emulation, potentially reducing performance/speed in the browser greatly.

KVM or nested KVM support is thus not strictly necessary for a minimal deployment or testing EaaSI, but highly recommended for production deployments, or if EaaSI users intend to run contemporary, resource-heavy operating system Environments.
