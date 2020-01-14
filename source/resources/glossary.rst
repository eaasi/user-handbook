.. EaaSI Glossary

EaaSI Glossary
**************

.. glossary::

  Node
      A node is an institutional member of the EaaSI network. Each node administers an instance of the EaaS stack;
      it controls which of its uploaded resources are synced to the rest of the EaaSI network and which remain accessible 
      only within the node’s instance. One institution may host multiple nodes within the EaaSI network; 
      for example if they are a lead infrastructure provider in a consortium, they may providing hosting for 
      distinct nodes for their consortium members.

  Source
      If a node contributes any resources to the EaaSI network, it is also considered the source for that particular
      resource.

  User
      A user is an operator of the EaaS software.

  Admin
      Admins are a user or a set of users within each node responsible for maintaining the node’s EaaS instance. Admins
      install, update, and configure the EaaS software stack, including all necessary aspects of linking storage
      services, setting local authentication and permissions, syncing the node’s instance with the EaaSI network, etc.

  Configuration User
      Configuration users are a user or set of users within each node with power to edit and modify content within
      their EaaS instance. Configuration users might, for example, upload software, configure new base environments, or
      enter descriptive and technical metadata for objects.

--------------------------------------------------------------------------------------------------

.. glossary::

  Resources
    A resource refers broadly to any usable element within the EaaS system, such as environments, software, and objects
    (e.g., file sets, data, disk images of storage media, etc.). It is the combination of metadata and files necessary
    to manifest the resource within the system as either a record or an operational element of a computing environment.


  Files
      Files in the system manifest as environments, software, or objects in emulation environments (e.g., environment
      disk images, installation media, file sets, etc.); or, potentially, metadata and unstructured documentation (e.g.
      photographs used to represent a resource visually, admin logs)


  Environments
      Environments are emulated computing systems within EaaS - i.e., a combination of emulated hardware and software
      components. Every environment contains at least two essential pieces: a Hardware Configuration and an Operating
      System.


  Hardware Configuration
      An environment’s Hardware Configuration refers to the emulator configuration settings that replicate the hardware
      of a physical computer system. Within EaaS, these configurations are provided as templates.

  Operating System
      In the context of an EaaS environment, an Operating System refers to installed and configured operating system
      software. Operating systems may also be available as installable software in the system, independent of an
      environment.

  Base
      A Base Environment refers to an emulated computing environment (hardware configuration + operating system) as
      initially imported into or created within EaaS. “Base” essentially refers to a starting point for configuration
      and can thus be highly contextual to a workflow: e.g., an imported disk image taken of a collection donor’s
      personal computer; a blank disk image created by EaaS on to which Windows 95 is installed via the EaaS software
      library; an OS configured with fundamental drivers (audio card, graphics card) and a fun new desktop background.
      Base environments will take up the most storage space in an instance, since they require full disk images.

  Derivative
      Any further configuration performed and saved on a base environment from inside EaaS is captured and referred to
      as a derivative environment. Derivatives are stored as delta/diff files from the original base to conserve storage
      but they can always be programmatically combined to re-form a single coherent disk image.
      Derivative environments can take several possible explicit forms in the UI:

  Software Environment
        A Software Environment is a derivative environment in which software has been imported, installed, configured
        and saved into a base environment from the available library of installable software. The intended use of a
        Software Environment is to expand the rendering/interaction capabilities of a base environment with software
        that is compatible with but, for whatever reason, was not initially available within a base environment.
        Software Environments can be derived from another Software Environment.

  Object Environment
        An Object Environment is a derivative environment in which a digital object (file, set of files, disk image,
        etc.) has been imported, saved, and/or installed into a Base Environment or Software Environment from the
        node’s available Object Archive. The intended use of an Object Environment is to provide access to the digital
        object as it would have been rendered/interacted with in its original (or a representative) computing
        environment.

  Software
      May also be referred to as a "Software Object". Software refers to application and system software, including
      operating systems, commercial and open source software applications, device drivers, etc.

  Objects
      May also be referred to as a "Digital Object". Objects are items in a digital collection; that is, information or
      works from institutional collections intended for representation (by Software) and interpretation by users within
      an emulated Environment. Within EaaS, the line between Software and Object (which may also be a piece of
      “software” in the general sense) is largely contextual and workflow related: a file or file-set is “Software” if
      it is intended to be used to accurately render and interact with Object(s) originally created with that (or
      otherwise compatible) Software. A file or file-set is an Object if it is the thing intended to be provided for
      interaction using Software in an Environment.

----------------------------------------------------------------------------------------------------------------

.. glossary::

  EaaS Components
      Components refer to individual modules of the EaaS software stack - as each System Role plays a part in the EaaS
      user ecosystem, each component performs a particular task within the EaaS stack.

  Front-End
      The front-end provides a user interface for accessing an EaaS instance and its contents (environments, software,
      objects) via HTTP (RESTful API) requests. This module may be implemented as part of a third-party system (e.g. as
      part of a library catalog).
      The front-end will be initially deployed to the EaaSI network as a demo admin UI.

  Gateway
      The Gateway module acts as the end-point for the EaaS REST API. It takes HTTP requests from the user, matches
      them with metadata from the database and uses that information to request/initialize emulation environments from
      the Emulation Component.

  Emulation Component
      The Emulation Component (or EmuComp) module hosts and allocates CPU resources to create and serve emulation
      sessions (including requesting and assembling any necessary resources from the Image, Software, and Object
      Archives). It delivers the emulator session back to the end-user’s browser. The EmuComp’s requirements/resources
      will need to scale depending on the number of simultaneous emulation sessions potentially allowed.

  Image Archive
      The Image Archive module provides the EmuComp with access to virtual disk images - it is responsible for
      connecting Environments to the EaaS instance. The Image Archive component can simply act as a connector to
      third-party storage (if the images are stored/hosted elsewhere) or can serve as a simple file-based archive,
      hosting the images themselves locally.

  Software Archive
      The Software Archive component provides the EmuComp with access to a library of installable software- it is the
      basis for connecting Software to the EaaS instance. The Software Archive component can simply act as a connector
      to third-party storage or serve as a file-based archive, hosting the software locally.

  Object Archive
      The Object Archive module provides the EmuComp with access to a digital object collection - it is the basis for
      connecting Objects to the EaaS instance. The Object Archive module can simply act as a connector to third-party
      storage or serve as a file-based archive, hosting the objects themselves locally.

  Database
      The EaaS database hosts all software, hardware configuration, and object repository metadata necessary for EaaS
      to coordinate requests and retrieval of emulation resources between the various EaaS components, and between
      instances of the EaaSI network. The database is currently a locally-stored MySQL database; updates and syncing of
      local databases with the EaaSI network should be performed by Admins only at direction of the EaaSI development
      team.
