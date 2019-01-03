.. Setup

Setup
=====

Preconditions
-------------

General EaaSI infrastructure layout (tbd).

- A EaaSI gateway machine
  - ssh shell access
  - sudo capabilities, make sure you do not need a password to use sudo
  - at least 10 Gb free disk space for the EaaSI installation

Prepare for setup
-----------------

- Checkout `eaas-ansible <https://gitlab.com/openslx/eaas-ansible>`_
- Build the deployment docker (optional):

  - run ``docker build -t eaas/eaasi-deploy .`` (you may need to prepend ``sudo`` depending on your installation

- Setup the ssh-keys for deployment:

  - go inside ``eaas-ansible/example``
  - run ``docker-compose -f setup-docker.yaml pull`` (only if you haven't build the docker youself (see above)
  - run ``docker-compose -f setup-docker.yaml up``:

    - you should have a ``ssh`` directory in your working directory

  - copy the keys to your remote server, run ``ssh-copy-id -i ssh/id_rsa user@host``. the username should match the remote user with sudo capabilities.

Configure the EaaSI Gateway
---------------------------
A minimal ``gateway.yaml`` file should look like:

.. literalinclude:: examples/gateway.yaml.template
	:language: yaml

A minimal ``hosts`` should look like:

.. literalinclude:: examples/hosts.template


- run ``docker-compose -f deploy-eaasi.yaml up``




