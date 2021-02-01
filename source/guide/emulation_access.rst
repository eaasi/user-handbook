.. Emulation Access interface

.. _emulation_access:

Emulation Access Interface
=============================

The Emulation Access screen allows the user to interact with a running emulation Environment. The user will be led to this screen when:

  1. They select the "Run in Emulator" or "Add Software" actions for any given Environment resource
  2. They complete the Import Image workflow
  3. They complete an Emulator Project workflow
  
.. image:: ../images/emulation_access.png

The features offered on this page may vary depending on how the Environment has been configured.

  - *Download Print Jobs*: Only available if "Environment can Print" has been enabled for the running Environment, and the Environment contains an installed and configured PostScript driver. If so, print jobs to PostScript in the running Environment will be intercepted by the EaaSI interface and this button will become selectable. The printed document will be offered to the EaaSI user as a downloadable PDF.
  
  - *Change Resource Media*: If the Environment contains a mounted Software or Content resource with more than one disk, the user may click on this button to alternate mounting them in the Environment. (In other words, the user may use this menu to mimic the behavior of ejecting and inserting multiple CD-ROMs, floppy disks, or other removable media into a physical machine)
  
  - *Save Screen Image*: Takes a screenshot of the Environment screen. The user's browser will offer the screenshot for download.
  
  - *Esc*: Sends an "Esc" keyboard input to the Environment. "Esc" key presses on the user's keyboard usually do not/will not pass to an EaaSI environment. Clicking this button allows the user to press the "Esc" key in the Environment if/when emulated software requires.
  
  - *Ctrl/Alt/Del*: Likewise, pressing this button will send a "Ctrl + Alt + Delete" keyboard command to the emulated Environment, which may be useful for troubleshooting or rebooting an emulated operating system. Pressing this keyboard combination on the user's keyboard will likely be intercepted by the host system, and is not recommended if an Environment is displaying issues.
  
The three buttons at the top of the screen allow the EaaSI user to stop or leave the Emulation Access interface in various ways:

  - *Save Environment* will open a new modal screen. The EaaSI user can save any changes or edits they made to the Environment during the currently-running Emulation Access session as a new Environment (Private by default) or as a revision (overwriting the originally selected Environment; only available if the originally selected Environment was Private when run).
  
  - *Restart Emulation* will perform a hard restart of the Emulation Access session. Any changes or edits made by the user to the Environment during the currently-running session will be discarded.
  
  - *Exit Emulation* will stop the currently-running Emulation Access session and return the user to whatever menu was used to launch the session. Any changes or edits made by the user to the Environment during the currently-running session will be discarded.
  
.. note::
  If the Environment was configured with the "Relative Mouse (Pointerlock)" option, clicking on the Environment's screen will capture the user's mouse. Press the "Esc" key on your host keyboard to free your mouse and interact with your browser and host system again.

.. note::
  The metadata options ("Saved Metadata" and "Configure New") on the left side of the Emulation Access interface are placeholders and until noted otherwise, non-functional. Advanced options for describing Environments and Software *while* they are running in emulation is under development.
  
