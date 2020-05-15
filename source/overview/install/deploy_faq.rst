.. Deployment FAQ

.. _deploy_faq:

Deployment Troubleshooting
============================

The target instance SSH port is not default (22)
-------------------------------------------------

Add the variable ``ansible_port: <YOUR_SSH_PORT>`` to the ``./artifacts/config/hosts.yaml`` file, under ``eaas_gateway:``.


The installer is failing to connect to the target instance (usually when connecting over VPN)
-----------------------------------------------------------------------------------------------

Try adding ``--net=host`` to a Docker run script in the ``./scripts/ansible-runner.sh`` file.

.. code-block:: sh

  ansible-runner.sh

  ...

  exec ${sudocmd} docker run --rm --tty --interactive --name eaas-ansible \
      --volume "${repodir}:${workdir}" \
      --net=host
      --workdir "${workdir}" \
      eaas/ansible \
      "$@"

If by adding the above error occurs again, the Docker network may be clashing with your VPN network. Consider restarting the Docker service on the target machine and run the installer again.


The target instance is private and needs to expose public fqdn, instead of a private one
------------------------------------------------------------------------------------------

In the ``./artifacts/config.eaasi.yaml`` add ``frontend_protocol``, ``public_port`` and ``public_fqdn`` properties:

.. code-block:: yml
  
    eaas:
      ...
      frontend_protocol: <PROTOCOL>
      public_port: <PORT>
      public_fqdn: <PUBLIC_FQDN>


- run the installer and wait until it successfully finishes

- ssh to the target machine, and navigate to the ``eaas_home`` directory.

- Remove ``external_links:`` block from ``docker-compose.yaml`` file

.. code-block:: yml
  
  eaas:
      ...
      external_links: <- go ahead and remove it
      eaasi-nginx:<PUBLIC_FQDN> <- go ahead and remove it


- add a bind-mount to ``docker-compose.yaml``

.. code-block:: yml
  eaas:
    ...
    volumes:
    - that-script.sh:/etc/service/eaas/run

- create a script ``that-script.sh`` containing:

.. code-block:: sh

  #!/bin/bash
  if [ ! -d "/home/bwfla/log" ]; then
    /sbin/setuser bwfla mkdir -p /home/bwfla/log
  fi
  if [ -z "$EAAS_PROXYPORT" ]; then
      EAAS_PROXYPORT=443
  fi
  SSL_DEFINES="-Deaas.urischeme=https -Deaas.proxyport=$EAAS_PROXYPORT"
  # NOTE: JBOSS server should be started in background, or else
  #       standlone.sh will not be able to shutdown it cleanly!
  export LAUNCH_JBOSS_IN_BACKGROUND='true'
  if [ "$RUN_AS_ROOT" == "true" ]; then
  	exec /home/bwfla/bw-fla-server/bin/standalone.sh $SSL_DEFINES -b=0.0.0.0 
  else
  	chown -R bwfla /home/bwfla/bw-fla-server/standalone/log 
  	exec /sbin/setuser bwfla /home/bwfla/bw-fla-server/bin/standalone.sh $SSL_DEFINES -b=0.0.0.0
  fi

- make the script executable

- on the target instance, navigate to ``eaas_home/config/eaas-config.d/02-clustermgr.yaml`` and modify ``node_addresses`` with your public port:

.. code-block:: yml

      ...
      node_addresses:
      - <PUBLIC_FQDN>:<PUBLIC_PORT>

- restart ``eaas`` docker container
