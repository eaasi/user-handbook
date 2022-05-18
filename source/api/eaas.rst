.. Emulation-as-a-Service API

.. _eaasi-api:

EaaSI API
===========

Emulation-as-a-Service exposes a number of RESTful API endpoints users can employ with an API client (including ``curl`` or any other HTTP request tooling) to get information and interact with the resources present in an EaaSI node.

The EaaS/EaaSI API can be useful to:

  - query and gather metadata
  - interact with the experimental "UVI"; see :ref:`uvi`
  - control and perform resource exchange between EaaSI nodes via OAI-PMH (it is recommended to interact with OAI-PMH endpoints via the EaaSI UI's built-in functionality, see :ref:`oaipmh` and :ref:`oai-pmh_management`)

Authentication and Access Tokens
----------------------------------

EaaS's public API can return information about Environments and Software present in a specified EaaSI node. Users with an account in that node can query the API based on their unique user context (for example, to receive metadata about Private Environments or imported Software resources) by obtaining an access token from EaaSI's `Keycloak <https://www.keycloak.org/>`_ authentication module.

.. note::

  If no access token/user context is provided, GET requests to the public API may still return metadata on a node's published/public resources (Public Environments)

Users with an EaaSI account can acquire an access token from their node by sending a POST request to ``https://[eaasi.domain]/auth/realms/master/protocol/openid-connect/token``, for example:

.. code-block:: sh

    $ curl --request POST \
    --url https://[eaasi.domain]/auth/realms/master/protocol/openid-connect/token \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data client_id=eaas \
    --data grant_type=password \
    --data username=[user] \
    --data password=[password]

Being sure to replace all information in ``[]`` with the appropriate values/credentials. Tokens are valid for an hour by default, after which they must be regenerated or refreshed.

A valid request should receive an `OAuth 2.0 access token response <https://www.oauth.com/oauth2-servers/access-tokens/access-token-response/>`_. The received ``access_token`` property value can then be provided in the header of subsequent requests to the EaaS API, for example:

.. code-block:: sh

  curl --request GET \
  --url 'https://[eaasi.domain]/emil/environment-repository/environments' \
  --header 'Authorization: Bearer [access_token]' \
  --header 'accept: application/json'

Public API
------------

**All public EaaS API endpoints are located under the base URL:** ``https://[eaasi.domain]/emil``

.. http:get:: /environment-repository/environments

  Retrieves a list of all available Environments in the node

  :reqheader Accept: Should define response content type as `application/json`
  :reqheader Authorization: optional OAuth token to authenticate (necessary to retrieve Private Environments)
  :query boolean detailed: If set to "true", can be used to display *all* metadata associated with each Environment rather than an overview ("false" by default)
  :query boolean localOnly: If set to "false", returns metadata associated with Public Environments visible but **not** Saved Locally to the node ("true" by default)
  :status 200: An array of Environments
  :>json string envId: Unique ID (UUID) for an Environment resource
  :>json string title: Human-readable name for an Environment resource
  :>json string archive: Indicates the Environment's storage archive, one of three options depending on its Network Status (returns "remote" for Public, "public" for Saved Locally, "default" for Private)
  :>json string owner: Indicates user account that owns the Environment resource (either returns "shared" for Public or Saved Locally, or a UUID for provided user account's Private Environments)
  :>json string objectId: If Environment is a :term:`Content Environment`, returns the UUID of the associated :term:`Content` object
  :>json string objectArchive: If Environment is a :term:`Content Environment`, returns the UUID of the user archive associated with that :term:`Content` (should be the same as ``owner`` UUID)
  :>json string envType: Returns "object" if Environment is a :term:`Content Environment`, returns "base" for all others
  :>json string timestamp: ISO 8601 full-time timestamp for when the Environment was created
  :>json string description: The most recent description of the Environment from its History (displayed during running Emulation Access sessions)
  :>json boolean linuxRuntime: Indicates if the Environment is a Linux runtime appropriate for importing and running containers (an EaaS feature not yet implemented in EaaSI nodes)
  :>json boolean networkEnabled: Indicates if the Environment is capable of networking with the live internet or other Environments (the latter is an EaaS feature not yet implemented in EaaSI nodes)
  :>json boolean internetEnabled: Indicates if the Environment is allowed to connect to the live internet (can only be "true" if ``networkEnabled`` is also "true")
  :>json boolean serviceContainer: Indicates if the Environment represents a container service (an EaaS feature not yet implemented in EaaSI nodes)

  **Example response**:

  .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
        "envId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "title": "Windows 98 + Borland Quattro Pro 5.0",
        "archive": "default",
        "owner": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "envType": "base",
        "timestamp": "2022-04-27T17:45:45.922581Z",
        "description": "installed to C: drive",
        "linuxRuntime": false,
        "networkEnabled": true,
        "internetEnabled": true,
        "serviceContainer": false
        },
        {
        "envId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "title": "The Would-Be Gentleman",
        "archive": "default",
        "owner": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "objectId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "objectArchive": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "envType": "object",
        "timestamp": "2022-03-17T15:18:56.917042Z",
        "description": "unstuffed floppy image and copied contents to MacintoshHD",
        "linuxRuntime": false,
        "networkEnabled": false,
        "internetEnabled": false,
        "serviceContainer": false
        }
      ]

.. http:get:: /software-repository/descriptions

  Retrieves a lightweight list of Software resources

  :reqheader Accept: Should define response content type as `application/json`
  :reqheader Authorization: OAuth token to authenticate (necessary to retrieve Private Software resources)
  :status 200: An array of Software
  :>json string id: Unique ID (UUID) for this Software resource
  :>json string label: Human-readable name for a Software resource
  :>json boolean isPublic: Indicates if the Software resource has been published (publishing Software resources has not yet been properly implemented in EaaSI; this value should be "false")
  :>json string archiveId: Name for the storage archive where the Content object is kept; should be "zero conf" for all private Software resources
  :>json boolean isOperatingSystem: Indicates if the Software resource has been identified as an operating system installer during resource import (available via Demo UI but not yet re-incorporated into EaaSI UI import process; should be "false" but certain legacy objects may display "true")

  **Example response**:

  .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "label": "Microsoft Money 95",
        "isPublic": false,
        "archiveId": "zero conf",
        "isOperatingSystem": false
        },
        {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "label": "Advanced_DB_Master_3.0",
        "isPublic": false,
        "archiveId": "zero conf",
        "isOperatingSystem": false
        }
      ]

.. http:get:: /software-repository/packages

  Retrieves a more detailed array of Software objects, including associated file formats

  :reqheader Accept: Should define response content type as `application/json`
  :reqheader Authorization: OAuth token to authenticate (necessary to retrieve Private Software resources)
  :status 200: An array of Software
  :>json string id: Unique ID (UUID) for this Software resource
  :>json string objectId: Unique ID (UUID) for this Software object (should be same as ``id``)
  :>json string label: Human-readable name for a Software resource
  :>json string licenseInformation: Open field for defining any relevant software license information
  :>json integer allowedInstances: Defines how many *concurrent* emulation sessions may be run with this Software object mounted (default is "-1", indicating *unlimited* sessions)
  :>json array nativeFMTs: An array of file format PUIDs that have been manually assigned with this Software object as formats that can be natively rendered in Environments associated with this Software resource (see :ref:`uvi`)
  :>json array importFMTs: An array of file format PUIDs that have been manually assigned with this Software object as formats that can specifically be *imported* in Environments associated with this Software resource (primarily experimental, for investigating automated migration)
  :>json array exportFMTs: An array of file format PUIDs that have been manually assigned with this Software object as formats that can specifically be *exported* from Environments associated with this Software resource (primarily experimental, for investigating automated migration)
  :>json string archiveId: Name for the storage archive where the Content object is kept; should be "zero conf" for all private Software resources
  :>json boolean isPublic: Indicates if the Software resource has been published (publishing Software resources has not yet been properly implemented in EaaSI; this value should be "false")
  :>json boolean isOperatingSystem: Indicates if the Software resource has been identified as an operating system installer during resource import (available via Demo UI but not yet re-incorporated into EaaSI UI import process; should be "false" but certain legacy objects may display "true")

  **Example response**:

  .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "objectId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "label": "Microsoft Money 95",
        "licenseInformation": "Proprietary commercial",
        "allowedInstances": 1,
        "nativeFMTs": ["fmt/38", "fmt/138", "fmt/57"],
        "importFMTs": ["x-fmt/18", " x-fmt/13"],
        "exportFMTs": ["x-fmt/18", "fmt/15"],
        "archiveId": "zero conf",
        "isPublic": false,
        "isOperatingSystem": false
        },
        {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "objectId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "label": "Advanced_DB_Master_3.0",
        "licenseInformation": "License key: xxx-xxxxx",
        "allowedInstances": -1,
        "nativeFMTs": ["fmt/38", "fmt/138", "fmt/57"],
        "importFMTs": ["x-fmt/18", " x-fmt/13"],
        "exportFMTs": ["x-fmt/18", "fmt/15"],
        "archiveId": "zero conf",
        "isPublic": false,
        "isOperatingSystem": false
        }
      ]
