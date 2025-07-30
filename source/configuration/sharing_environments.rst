.. Sharing Environments

Sharing Environments
=====================

.. note::

    The following guidance is unique to `v2021-10` of EAASI. It reflects the technical capabilities and limitations of the platform's grant-funded, exploratory period and does not reflect how the EAASI team imagines Environment and resource sharing to function moving foward in the re-architected, "Next-Gen" EAASI platform. For more details on the team's future vision for user account management and access control, please check out the :ref:`roadmap` or join the discussion on the `User Forum <https://forum.eaasi.cloud/c/eaasi-alliance-discussion/roadmap-governance/23>`_!

Due to limitations in the underlying architecture, the options for having multiple users interact with the same Environment in v2021.10 of EAASI - whether at the same time, or distributed - are few.

This page attempts to lay out some historical context behind this limited functionality - if you would like to skip straight to the team's functional recommendations for "sharing" resources in v2021.10, click to that :ref:`section below<recommendations>`.

Development History
*********************

The earliest, grant-funded iterations of the EAASI platform (itself building off the bwFLA/Emulation-as-a-Service application originally developed in the early 2010s) were "single-user:" access to an EAASI installation and its resources could be placed behind a password, but once an individual with these credentials logged in, the system would make no distinction between which users could import, edit, or access which resources.

During the grant-funded phase, the EAASI team developed the stack to allow for "multi-user" installations: multiple user accounts, each with their own unique credentials, could now be created, each with the ability to import, edit and access their own private pool of resources. These user accounts could also be sorted into arbitrary groups of user accounts, referred to in EAASI as "Organizations" - but, in an attempt to iterate the technical challenges faced by "multi-user" installations, there was no mechanism implemented to associate resource ownership or access with multiple user accounts, let alone an entire Organization.

("Multi-user" account ownership was also implemented in a staggered fashion across resources, first with Content and Software objects, then with Environments, leaving permissions and multi-user access control for stand-alone Computer Image resources lagging.)

In other words, as of v2021.10, **there remains no method to share any EAASI resource - Environment, Software, Content, or Computer Image - from one user account to another user account**. You can neither share a resource to another, single user account (whether or not that account is also a member of your Organization), nor can you share a resource specifically to all accounts in your Organization.

At the same time as the team was developing "multi-user" installations, the EAASI grants also made a significant assumption about data and resource sharing *between real-world institutions*: in 2018, the primary assumption was that each real-world institution would run its own EAASI server, and many of these EAASI servers would eventually be part of a coordinated, decentralized *network* of EAASI servers making their Software and Environment resources available to each other, for the purposes of reducing redundant legacy software collection and configuration efforts. 

The mechanism for marking an Environment or Software resource available for other EAASI servers to copy and re-use was referred to as "Publishing" the resource. Each EAASI server in the network would be referred to as a "node". This terminology will still be encountered by an EAASI user in the v2021.10 interface.

Because "Publishing" was designed for sharing resources between *servers* - not between *users* - the "Publishing" functionality intersected with the simulatenous "multi-user" installation development in potentially counter-intuitive ways. In v2021.10 - which is the last version of EAASI in which the "Publishing" functionality will be present - "Publishing" an Environment resource has the effect of not only making it available to other servers, but to **all user accounts within the same EAASI server - regardless of their Organization**.

"Publishing" an Environment also has the effect of completely freezing it - since a Public Environment had to be persistently available to other EAASI servers, you could not edit its metadata (e.g. change emulator settings, re-name the Environment) or adjust the guest system at all (install additional software, re-configure an operating system, etc.) without generating a new, :term:`derivative` Environment resource. This new Environment becomes automatically private to the user account account that created it. 

Over the six-year course of the Mellon- and Sloan-foundation-funded "Scaling Emulation-as-a-Service Infrastructure" grants, expectations for EAASI platform use and development shifted significantly away from a decentralized network of servers and the "Publishing" design. The desire to pursue fine-grained access control (the ability to share and set limits on the particular uses of Environments between specific user accounts and to/within Organizations) plus a need to bring down infrastructure costs with cloud-native services and storage, collided with the underlying architecture, and the "Publishing" functions in particular.

"Next-Gen" EAASI will aim to address these concerns and remove "Publishing" in favor of a more flexible sharing model that will be more familiar to users from other major file- and resource-management cloud systems. In the meantime, the following are a few recommendations for sharing Environment resources within the legacy v2021.10 "Publishing" framework, but in a way that should hopefully smooth the eventual transition to working with "Next-Gen" EAASI.

Recommendations
****************

The EAASI team can not categorically state that any sharing approach is appropriate across all possible access and use scenarios for the platform. Our aim is to describe the technical possibilites, limitations and repercussions of certain actions in the platform, and allow users and the Research Alliance community of practice to determine the paths forward for their holdings and EAASI resources from there.

Because Environments **can not be shared between user accounts without "Publishing" them - thereby making them available to ALL user accounts within ALL Organizations in the EAASI server** - the EAASI team recommends creating and using **only one Admin-level user account per Organization**.

Assuming that Organizations map to a real-world instutition or organization, and that there are potentially many individual users per real-world institution, this means sharing account credentials - a single username and password - between multiple individuals, outside of EAASI.

**Advantages:**

- all users within a real-world instutition (i.e. EAASI Research Alliance member) can access that institution's software holdings, Content Environments, etc.
- avoids redundant configuration effort and storage of operating system installation media and/or other Software and Content resources that would otherwise be necessary to repeat across every assigned user account
- avoids the copyright and/or collection permissions assessment that would otherwise likely be necessary by "Publishing" an Environment in order to make it available to another user account within the Organization (but that would also make the Environment accessible to all other Organization's accounts as well)
- multiple users can log in to the same account at the same time and **run** Environments - even the same Environment - without repercussions in the EAASI app

**Drawbacks:**

- security concerns of sharing credentials, including passwords
- multiple individuals logged in to the same account and performing certain actions at the same time could result in unpredictable user experience, particularly with features that rely on per-account configuration like Bookmarks and the Emulation Project page; or worse, attempting to edit the same Environment resource at the same time, which could result in duplicate Environments, corrupted Environments, or other unpredictable behavior
- the design of the EAASI web interface assumes multiple user accounts per-Organization, resulting in conflicting UX between these recommendations and functions that the platform itself describes or encourages
- the potential need to provide extra guidance to patrons or other infrequent EAASI users to view and interact with exactly the Environment and Content they are looking for, among a pool of resources that are otherwise irrelevant to them


The only alternatives for "sharing" an Environment (including Content Environments) between user accounts are:

1. Selecting the relevant Environment and using the "Publish to Network" option in the Actions menu - making the Environment visible and runnable by all user accounts across all Organizations in the deployment.
2. Logging in to the second user account ahead of time, re-create the relevant Environment (including its entire configuration chain, starting from any of the available :ref:`template environments`) in the second user account, log out and back in to the first, Admin-level user account, use the User Management options on the Manage Node page to reset the password on the second user account, then provide the generated temporary password for the second user account to the desired individual user, outside of EAASI. (Note that this approach is not even so much "sharing" an Environment as it is a separate Environment resource that duplicates the configuration effort of the target Environment)

If you have further questions about sharing or having multiple users access EAASI resources, please start a thread in the `Forum <https://forum.eaasi.cloud/c/support/6>`_!