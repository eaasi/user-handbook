.. EaaSI Glossary

Glossary
**********

.. glossary::

  Admin
      Admin users have the highest level of permissions in EaaSI. They are responsible for :term:`node` management
      and can perform all administrative tasks, including importing emulators, syncing :term:`resources<resource>` to
      the :term:`network`, adding new network :term:`endpoints<endpoint>`, monitoring running tasks, etc. Admins
      also retain all the permissions/actions of :term:`Managers<manager>` and :term:`Configuration Users<configuration user>`
      as well.
      
  Base
      A base is an :term:`environment` as initially either imported or created in EaaSI. “Base” essentially refers to a 
      starting point for configuration and can thus be highly contextual to a workflow: e.g., an imported disk image taken of a collection donor’s
      personal computer; a Windows 95 environment created from scratch using the Emulation Project menu; an Ubuntu environment
      synced from the `EaaSI Open Source Sandbox <https://eaasi-sandbox.softwarepreservationnetwork.org/eaasi/#/portal/welcome>`_.
      Base environments will take up the most storage space in an instance, since they require full disk images.
      
  Configuration User
      Configuration users have the lowest set of permissions in EaaSI. They are able to configure or edit metadata for
      existing :term:`resources<resource>` and run environments, but can not import any new resources or access the
      Manage Node menu.
        
  Content
      Content are items from a digital collection; that is, digital information or works from institutional collections intended 
      for representation (via :term:`software`) and interpretation by users (in an :term:`environment`). Within EaaSI, the line between Software and Content 
      (which may also be a piece of “software” in the general sense) is largely contextual and workflow related: a file or file-set is “Software” if
      it is intended to be used as a tool to accurately render and interact with software-dependent Content. A file or file-set is Content if it is 
      the intended target of rendering. (It is assumed that Content may be subject to further access restrictions depending on digital collection
      practice at each :term:`node host`)
      
  Content Environment
      A "Content Environment" is a :term:`derivative` environment in which :term:`content` has been imported, saved, and/or 
      installed into an existing environment. The intended use of a Content Environment is to provide access to digital/collection 
      objects as they would have been rendered in their original (or a representative) computing environment. Content environments are 
      marked with the 'Content' label in the EaaSI interface and can not be published to the :term:`EaaSI Network`. 
      
  Derivative
      Any configuration performed and saved on a :term:`base` environment in EaaSI is captured and referred to
      as a derivative environment. Derivatives are stored as delta/diff files from the original base to conserve storage
      (but it is possible to programmatically combine them to re-form a single coherent disk image). Derivatives allow
      EaaSI users to build off previous work without starting from scratch every time a new environment is needed. The
      derivative chain of any given environment can be traced via its Details page.
      
  EaaSI Network
      The EaaSI Network is the community of :term:`node hosts<node host>` using the EaaSI platform to share collections of :term:`environments<environment>`
      and :term:`software`. The Network is controlled through exclusive access to node :term:`endpoints<endpoint>`; you
      can run/use an EaaSI :term:`node` without being a member of the Network. (But if you would like details about joining the Network,
      contact us at eaasi@yale.edu!)
      
  Endpoint
      An endpoint allows for synchronization of :term:`environments<environment>` between two EaaSI :term:`nodes<node>`. 
      They are a URL configured during node installation to allow for exchange of metadata and files via :ref:`OAI-PMH <oai-pmh>`.
       
  Environment
      Environments are emulated computing systems - i.e., a combination of emulated hardware and software
      components. The goal of EaaSI is to make it simple to create and run environments in a browser. Every environment must have 
      at least two pieces: a :term:`hardware configuration` and bootable software (i.e. an :term:`operating system`).
            
  Hardware Configuration
      An :term:`environment’s<environment>` hardware configuration refers to the emulator configuration settings that replicate the hardware
      of a physical computer system. Within EaaSI, these configurations are provided as templates.
      
  Image
      A bootable disk image imported to create a new :term:`Base`. EaaSI users are encouraged to create new Base Environments from :term:`software` resources within the platform using the :ref:`emulation-project`menu. However, importing Images allows users to make use of bootable computing environments originally created *outside* the EaaSI platform: e.g. a virtual machine from VirtualBox or VMWare, or a physical hard drive extracted from a running computer and imaged.
      
  Manager
      Managers have the middle level of permissions in EaaSI. They are able to manage other users (at the same permission
      level or lower) and :term:`resources<resource>` (e.g. import :term:`software` or :term:`content`, publish or replicate :term:`environments
      <environment>`), but can not access :term:`Admin` settings for node management. Managers also retain
      all permissions/actions of :term:`Configuration Users<configuration user>`.
            
  Node
      A node is one installation/instance of the EaaSI platform. By default, all imported or created :term:`resources<resource>` stay
      within their node, but :term:`environments<environment>` can be published and synced to other nodes in the :term:`EaaSI Network`.
      
  Node Host
      Node hosts are an institutional or organizational member of the EaaSI Network. Each host administers at least one :term:`node`;
      it controls which of that node's :term:`resources<resource>` are synced to the rest of the EaaSI Network and which remain accessible 
      only within the node. One node host could potentially run multiple nodes within the EaaSI Network; for example if they are 
      a lead infrastructure provider in a consortium, they may provide hosting for distinct nodes for their consortial members.
      
  Object 
      An object is any collection of files that represent the materials used to transmit, install, and/or operate :term:`software` or :term:`content` 
      in EaaSI. (For example, disk images of an installation CD or an archive file packaging software components together)
  
  Operating System
      :term:`Software` may be labelled an Operating System if it contains bootable or installable system software (i.e. that Software
      can run or install a stand-alone :term:`environment`).
      
  Resource
      A resource refers broadly to either an :term:`environment`, :term:`software` object, or :term:`content` object.
      It is the combination of metadata and files necessary to render an environment or :term:`object` in the system.

  Software
      Software refers to application and system software, including operating systems, commercial and open source 
      software applications, device drivers, etc.
  
  Source
      If a :term:`node` contributes any :term:`resources<resource>` to the EaaSI Network, it is also considered that resource's source.
