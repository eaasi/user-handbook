.. Exploring Resources

.. _explore:

Explore Resources
====================

The "Explore Resources" page is the EaaSI platform's main portal for discovery. From this overview, users can find resources saved in their node or available across the EaaSI Network.

Each resource card has visual tags to quickly display relevant information like the Resource Type (Environment, Software, or Content) and Network status (Private, Saved, Remote).

.. image:: ../images/explore_resources.png

The Explore Resources page will display the first 10 resources within each resource category - Environments (which includes both Base and Content Environments), Software and Content. If there are more than 10 resources available in any given category, users can use the "Refine Your Results" sidebar to more narrowly browse, or use the search bar at the top of the screen to find a particular resource.

.. note::
  The "Search resources" bar currently only performs a free-text search based on resource names. Advanced search based on particular metadata fields (Description, Operating System, etc.) is under development with the implementation of the EaaSI metadata application profile.
  
Any resource on the Explore Resources page can be bookmarked by the logged-in user by clicking the bookmark icon at the top right corner of the resource card:

.. image:: ../images/bookmark.png

A bookmarked resource will then be visible on the :ref:`my_resources` page for quick reference/use later.

Environment Results
----------------------

.. image:: ../images/refine_results_envs.png

Environment resources can be refined by Network Status, i.e. whether that Environment is:

* **Remote** (available at a synced node in the Network but must be replicated to the local node
  before it can be used)
  
* **Public** (published to the Network and already replicated and available in the user's local node)

* **Private** (only available to users in the local node, not available to the Network)

By default, any new Environments, (including derivatives or revisions of Saved Environments) are "Private". To publish a Private environment to the Network, see :ref:`publishing`.

Environment resource cards also contain two additional tags: "Base" and "Content".

* **Content** indicates that the Environment is a Content Environment, meaning it has been
  associated with a particular Content resource. Content resources are exclusively available to the local node, and Content Environment *can not* be published to the Network. They will always be "Private".
* **Base** indicates any Environment that is not associated with Content. It can be further configured, associated with Software and/or Content resources, or published to the Network to benefit users at other nodes.


Software Results
------------------

.. image:: ../images/refine_results_software.png

Software resource results can only be minimally sorted and refined until implementation of the EaaSI metadata application profile.

.. note::
  In the screenshot above, the "Source Location" field refers to an experimental implementation of sharing Software resources between nodes in the EaaSI Network (mimicking the publishing functionality available with Environments). This feature is not functional in EaaSI v2020.03 and can be ignored by users.
  
  
Content Results
-----------------

.. image:: ../images/content_results.png

Content results can only be minimally sorted and refined until implementation of the EaaSI metadata application profile.


Slide Menu
-------------

Clicking on the top left corner of any resource card will activate a Slide Menu containing contextual "Actions" for that resource:

.. image:: ../images/slide_ui.gif

* **"View Details"** will take the user to that resource's Details page (same as clicking on the resource name/title)
* **"Run in Emulator"** (Private and Saved Environment resources only) opens an Environment in the Emulation Access interface
* **"Bookmark This Resource"** adds the resource to bookmarks on the :ref:`my_resources` page (same action as clicking the bookmark icon)
* **"Add to Emulation Project"** adds the resource to the user's current :ref:`emulation-project`
* **"Add Software"** (Private and Saved Environment resources only) allows the user to select a Software resource from a dropdown menu, then opens that Environment in the Emulation Access interface with the Software resource attached
* **"Save to My Node"** (Remote Environment resources only) copies an Environment published from another node in the Network to the user's node - the Environment tag will change from Remote to Public
* **"Publish to Network"** (Private Environment resources only) makes an Environment available for users at other nodes to save to their node - the Environment tag will change from Private to Public + Saved Locally
* **"Delete"** (Private Environment and Content resources only) removes the selected resource from the node

The Slide Menu will also display any currently running background processes in the node (e.g. importing emulators, Saving resources to the node, etc.)
