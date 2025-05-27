.. EAASI Glossary

Glossary
**********

.. glossary::

  Access User
      lorem ipsum

  Base
      A base is an :term:`environment` as initially either imported or created in EAASI. “Base” essentially refers to a
      starting point for configuration and can thus be highly contextual to a workflow: e.g., an imported disk image taken of a collection donor’s
      personal computer; a Windows 95 environment created from scratch using the Emulation Project menu, etc., etc. Base environments will generally take up the most storage space in an instance.

  Computer Image
      lorem ipsum

  Configuration User
      Configuration users have the lowest set of permissions in EAASI. They are able to configure or edit metadata for
      existing :term:`resources<resource>` and run environments, but can not interact directly with a network (saving or publishing Environments) or access administrative features in the Manage Node menu.

  Content
      Content are items from a digital collection; that is, digital information or works from institutional collections intended
      for representation (via :term:`software`) and interpretation by users (in an :term:`environment`). Within EAASI, the line between Software and Content (which may also be a piece of “software” in the general sense) is largely contextual and workflow related - a file or file-set is “Software” if it is intended to be used as a tool to accurately render and interact with software-dependent Content. A file or file-set is Content if it is the intended target of rendering. (It is assumed that Content may be subject to further access restrictions depending on digital collection practice at each :term:`node host`)

  Content Environment
      A "Content Environment" is a :term:`derivative` environment in which :term:`content` has been imported, saved, and/or
      installed into an existing environment. The intended use of a Content Environment is to provide access to digital/collection
      objects as they would have been rendered in their original (or a representative) computing environment.

  Deployment
      lorem ipsum

  Deployment Admin
      lorem ipsum

  Derivative
      Any configuration performed and saved on a :term:`base` environment in EAASI is captured and referred to
      as a derivative environment. Derivatives are stored as delta/diff files from the original base to conserve storage
      (but it is possible to programmatically combine them to re-form a single coherent disk image). Derivatives allow
      EAASI users to build off previous work without starting from scratch every time a new environment is needed. The
      derivative chain of any given environment can be traced via its Details page.

  Environment
      Environments are emulated computing systems - i.e., a combination of emulated hardware and software
      components. The goal of EAASI is to make it simple to create and run environments in a browser. Every environment must have
      at least two pieces: a :term:`hardware configuration` and bootable software (i.e. an :term:`operating system`).

  Hardware Configuration
      An :term:`environment’s<environment>` hardware configuration refers to the emulator configuration settings that replicate the hardware
      of a physical computer system. Within EAASI, these configurations are provided as templates.

  Object
      The collection of files that represent the materials used to transmit, install, and/or operate :term:`software` or :term:`content`
      in EAASI. This could be the disk image(s) of an installation CD or an archive file packaging software components together.

  Operating System
      :term:`Software` may be labelled an Operating System if it contains bootable or installable system software (i.e. that Software
      can run or install a stand-alone :term:`environment`).

  Organization
      An EAASI :term:`deployment` can be arranged into arbitrary groups referred to as Organizations ("Orgs"). :term:`Organization Admin`-level users can only see and control other user accounts within their Organizations as configured by the :term:`Deployment Admin`. In the context of the EAASI Research Alliance, Organizations usually map to a real-world institutional member of the Alliance.

  Organization Admin
      Organization ("Org") Admins are responsible for user management in their :term:`organization`. Organization Admins also retain all the permissions/actions of :term:`Configuration Users<configuration user>` when it comes to creating and managing resources belonging to their own account.

  Research Alliance
      lorem ipsum

  Resource
      A resource refers broadly to a usable entity in EAASI: an :term:`environment`, :term:`software`, :term:`content`, or :term:`computer image`.

  Software
      Software refers to application and system software, including operating systems, commercial and open source
      software applications, device drivers, etc.

  System Admin
      Lorem ipsum

  Teleport
      lorem ipsum