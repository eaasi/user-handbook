.. Exploring Resources

.. _explore:

Explore Resources
====================

The "Explore Resources" page is the EAASI platform's main portal for discovery. From this overview, users can find resources saved in their node or available across the EAASI Network.

Each resource card has visual tags to quickly display relevant information like the Resource Type (Environment, Software, or Content) and Network status (Public, Public + Saved Locally, Private).

.. image:: ../images/explore_resources.png
  :width: 1000
  :align: center

The Explore Resources page will display the first 10 resources within each resource category - Environments (which includes both Base and Content Environments), Software and Content. If there are more than 10 resources available in any given category, users can use the "Refine Your Results" sidebar to more narrowly browse, or use the search bar at the top of the screen to find a particular resource.

.. note::
  The "Search resources" bar currently only performs a free-text search based on resource names. Advanced search based on particular metadata fields (Description, Operating System, etc.) is under development with the implementation of the EAASI metadata application profile.
  
Any resource on the Explore Resources page can be bookmarked by the logged-in user by clicking the bookmark icon at the top right corner of the resource card:

.. image:: ../images/bookmark.png

A bookmarked resource will then be visible on the :ref:`my_resources` page for quick reference/use later.

Environment Results
----------------------

.. image:: ../images/refine_results_envs.png

Environment resources can be refined by Network Status, i.e. whether that Environment is:

* **Public** (published at a synced node in the Network but must be saved to the local node
  before it can be used)
  
* **Saved Locally** (published to the Network and already saved and available in the user's local node)

* **Private** (only available to users in the local node, not visible to the Network)

By default, any new Environments, (including derivatives or revisions of Environments that are Saved Locally) are "Private". To publish a Private environment to the Network, see :ref:`publishing`.


Software Results
------------------

.. image:: ../images/refine_results_software.png

Software resource results can only be minimally sorted and refined until implementation of the EAASI metadata application profile.

.. note::
  In the screenshot above, the "Source Location" field refers to an experimental implementation of sharing Software resources between nodes in the EAASI Network (mimicking the publishing functionality available with Environments). This feature is not functional in EAASI v2020.03 and can be ignored by users.
  
  
Content Results
-----------------

.. image:: ../images/content_results.png

Content results can only be minimally sorted and refined until implementation of the EAASI metadata application profile.


.. _actions:

Actions Menu
-------------

Clicking on the top left corner of any resource card will activate a slide menu containing contextual "Actions" for that resource:

.. image:: ../images/slide_ui.gif

* **"View Details"** will take the user to that resource's Details page (same as clicking on the resource name/title)
* **"Run in Emulator"** (Private and Saved Locally Environment resources only) opens an Emulation Access session using that Environment
* **"Bookmark This Resource"** adds the resource to bookmarks on the :ref:`my_resources` page (same action as clicking the bookmark icon)
* **"Add to Emulation Project"** adds the resource to the user's current :ref:`emulation-project`
* **"Add Software"** (Private and Saved Locally Environment resources only) allows the user to select a Software resource from a dropdown menu, then opens that Environment in the Emulation Access interface with the Software resource attached
* **"Save to My Node"** (Public Environment resources only) copies an Environment published from another node in the Network to the user's node - the Environment tag will change from Remote to Public
* **"Publish to Network"** (Private Environment resources only) makes an Environment available for users at other nodes to save to their node - the Environment tag will change from Private to Public + Saved Locally
* **"Delete"** (Private Environment and Content resources only) removes the selected resource from the node

The Actions Menu will also display any of the user's currently running background processes (e.g. saving Environments to the node)
