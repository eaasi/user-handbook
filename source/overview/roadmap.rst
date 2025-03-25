.. Development Roadmap

.. _roadmap:

EAASI Product Roadmap
======================

The annual EAASI Product Roadmap is a high-level summary of both development and maintenance work that has been prioritized for the current calendar year (2024). Work is identified and prioritized for the roadmap according to stakeholder needs. This roadmap is updated quarterly.


New Release and/or Feature Development
---------------------------------------

- Mint new release of EAASI in first half of 2024, which will include the following:

    - Emulation Project "Advanced Workflow" (allowing dynamic object to drive assignment and construction of Environments using imported Images)
    - Map all resource permissions in S3-compatible storage to Keycloak user management module
    - Updated resource type icons and labels for consistency
    - Bug fixes
    - Stability and dependency updates

- Investigate the following functionality for the subsequent release of EAASI:

    - Related to managing user accounts:
  
        - Ability to reset account password by email
        - Ability to log in to EAASI using the single sign-on system of one's institution
        - Ability to designate "Access Users" and "Node Administrators"

    - Related to creating and managing emulation environments:

        - Ability to batch import objects and software into EAASI via API
        - Ability to delete an object, content environment, or base environment that has been shared to multiple users
        - Ability to add a new emulator to be used with EAASI

    - Related to discovering emulation environments:

        - Ability to narrow search results to locate resources by era or system requirements

    - Related to sharing emulation environments:

        - Ability to share an environment to other members of one's Organization
        - Ability to share an environment or resource with another specific user
        - Ability to restrict access to an environment for a user by IP 
        - Ability to limit the length of time that a user can access an environment


Essential Maintenance
----------------------

- Upgrade Yale's local, production installation of EAASI to the newest release, migrate data to support Yale's continued participation in EAASI networks
- Update storage and permissions approach for objects, software, images, and environments - required to achieve the new release and/or feature development above
- Update metadata approach for objects, software, and environments - required to achieve the new release and/or feature development above
- Update emulator handling to enable abstraction and extensibility - required to achieve the new release and/or feature development above
- Update essential dependencies that make it easier to install and maintain EAASI