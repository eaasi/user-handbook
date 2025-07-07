.. EAASI Glossary

Glossary
**********

.. glossary::

  Admin
      Admin users have the highest level of permissions in EAASI. They are responsible for user account management in their :term:`organization` and have a higher level of control over :term:`resources<resource>`. Admins
      also retain all the permissions/actions of :term:`Configuration Users<configuration user>`
      as well.

  Base
      A base is an :term:`environment` as initially created in EAASI. “Base” essentially refers to a
      starting point for configuration and can thus be highly contextual to a workflow. Base environments will generally take up the most storage space in an instance.

  Configuration User
      Configuration users have the lowest set of permissions in EAASI. They are able to configure or edit metadata for
      existing :term:`resources<resource>` and run environments, but can not interact access user account management features.

  Content
      Content are items from a digital collection; that is, digital information or works from institutional collections intended
      for representation (via :term:`software`) and interpretation by users (in an :term:`environment`). Within EAASI, the line between Software and Content (which may also be a piece of “software” in the general sense) is largely contextual and workflow related - a file or file-set is “Software” if it is intended to be used as a tool to accurately render and interact with software-dependent Content. A file or file-set is Content if it is the intended target of rendering. (It is assumed that Content may be subject to further access restrictions depending on digital collection practice at each :ref:`organization`.)

  Content Environment
      A "Content Environment" is a :term:`derivative` environment in which :term:`content` has been imported, saved, and/or
      installed into an existing environment. The intended use of a Content Environment is to provide access to digital/collection
      objects as they would have been rendered in their original (or a representative) computing environment. Content Environments are
      marked with the 'Content' label in the EAASI interface.

  Derivative
      Any configuration performed and saved on a :term:`base` environment in EAASI is captured and referred to
      as a derivative environment. Derivatives are stored as delta/diff files from the original base to conserve storage. Derivatives allow
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

  Organization
      Since v2021.10, user accounts in an EAASI server can be arranged into arbitrary groups referred to as "organizations". :term:`Admin`-level users can only see and control other user accounts within their Organization.

  Resource
      A resource refers broadly to a usable entity in EAASI: an :term:`environment`, :term:`software`, or :term:`content`.
      It is the combination of an :term:`object` and any metadata necessary to render that object.

  Software
      Software refers to application and system software, including operating systems, commercial and open source
      software applications, device drivers, etc.
