.. Exploring Resources

.. _explore:

Explore Resources
====================

The "Explore Resources" page is the EAASI platform's main portal for discovering resources available to the current user account.

Each resource card has visual tags to quickly display relevant information like the Resource Type (Environment, Software, Content or Image).

.. image:: ../images/explore_resources.png
  :width: 1000
  :align: center

The Explore Resources page will display the first 10 resources within each resource category - Environments (which includes both Base and Content Environments), Software and Content. If there are more than 10 resources available in any given category, users can use the "Refine Your Results" sidebar to more narrowly browse, or use the search bar at the top of the screen to find a particular resource.

.. note::
  The "Search resources" bar currently only performs a free-text search based on resource names. Advanced search based on particular metadata fields (Description, Operating System, etc.) is under development.
  
Any resource on the Explore Resources page can be bookmarked by the logged-in user by clicking the bookmark icon at the top right corner of the resource card:

.. image:: ../images/bookmark.png

A bookmarked resource will then be visible on the :ref:`my_resources` page for quick reference/use later.

Environment Results
----------------------

.. image:: ../images/refine_results_envs.png

.. _network_status:

Environment resources can be refined by "Network Status."

.. warning::
  .. warning::
  "Network Status" refers to an outdated and no-longer-applicable model of sharing Environments between EAASI servers that was explored during the platform's grant-funded cycle. This language will be replaced entirely in "Next-Gen EAASI," but due to complexities in the legacy code, could not be replaced in `v2021-10`.

* **Saved Locally** (Published and visible to ALL user accounts, regardless of their Organization; please note that any Environments tagged "Saved Locally" will *also* be tagged "Public", for the same legacy reasons explained in the warning above)

* **Private** (only available to the currently-logged-in user account)

By default, any new Environments, (including any :term:`derivatives` or revisions of Environments that are Saved Locally) are "Private".

Software Results
------------------

.. image:: ../images/refine_results_software.png

Software resource results can only be minimally sorted and refined until further development of the EAASI metadata application profile.
  
  
Content Results
-----------------

.. image:: ../images/content_results.png

Content results can only be minimally sorted and refined until further development of the EAASI metadata application profile.


Image Results
--------------

Due to technical limitations within the v2021.10 codebase (see :ref:`import_image`), all EAASI accounts will see a small handful of :term:`Computer Image` resources listed as available to them on the Explore Resources page of the EAASI Research Alliance's hosted deployment. These are all essentially blank disk images ("Blank 1GB". "Blank 10GB", etc.) and are functionally useless - users can not add them to their Emulation Project or view any metadata about them. Please ignore these resource results.

.. _actions:

Actions Menu
-------------

Clicking on the top left corner of any resource card will activate a slide menu containing contextual "Actions" for that resource:

.. image:: ../images/slide_ui.gif

* **"View Details"** will take the user to that resource's Details page (same as clicking on the resource name/title)
* **"Run in Emulator"** opens an Emulation Access session using that Environment
* **"Bookmark This Resource"** adds the resource to bookmarks on the :ref:`my_resources` page (same action as clicking the bookmark icon)
* **"Add to Emulation Project"** adds the resource to the user's current :ref:`emulation-project`
* **"Add Software"** allows the user to select a Software resource from a dropdown menu, then opens that Environment in the Emulation Access interface with the Software resource attached
* **"Publish to Network"** (Private Environment resources only) makes an Environment available for users all other user accounts - the Environment tag will change from "Private" to "Saved Locally" - see :ref:`warning<publish_warning>` below
* **"Delete"** (Private Environment, Software and Content resources only) removes the selected resource

.. _publish_warning::

.. warning::
  Please **DO NOT** use the "Publish to Network" button without consulting with the EAASI team and/or the rest of the EAASI Research Alliance via the `User Forum <https://forum.eaasi.cloud/c/eaasi-alliance-discussion/8/none>`_ first.

  v2021.10 of EAASI and its sharing features - including "Publishing" - were designed EAASI's experimental grant-funded cycle, and likely have larger-than-intended repercussions for who can then access and use your Environment and its data. Unfortunately, technical limitations and complexities in the code also meant we could not remove this function altogether before deployment.

  Unless you are extremely confident that you want your Environment to be available to all other instutitions and user accounts in the EAASI Research Alliance, **do not** select "Publish to Network".