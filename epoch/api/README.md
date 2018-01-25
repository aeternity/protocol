# Æternity epoch node API

This document:
* Provides an overview of the API exposed by the epoch node;
* Defines the WebSocket API of the epoch node;
* Describes the intented usage of the user API of the epoch node.

## Overview

The epoch node API consists of the following endpoints:
* External HTTP API;
  * It consists of the peer-to-peer network API and of part of the user API;
  * It is defined via Swagger schema;
  * It is meant to be exposed on the Internet;
  * Its TCP port is configurable.
* Internal HTTP API;
  * It consists of part of the user API;
  * It is defined via Swagger schema;
  * It is **not** meant to be exposed on the Internet;
  * Its TCP port is configurable.
* Internal WebSocket API.
  * It consists of part of the user API;
  * It is defined in the rest of this document;
  * It is **not** meant to be exposed on the Internet;
  * Its TCP port is configurable.

The epoch node uses the plain HTTP protocol for its API endpoints during the testnet phase while it will use the HTTPS protocol in mainnet.

## WebSocket API definition

### Connection
The epoch node supports an endpoint with a configurable port where the
websocket's clients connect. It is located on `/websocket`.

The node could serve multiple websocket clients. Their number is configured in
the epoch.yaml. When all websocket connections are consumed - any new incoming
connections will be queued. The queue has a maximum size and when it is
reached - any new incoming connections will be rejected with an error code 400.
This is to prevent the node of being overloaded with websocket connections.

### Subscription to events
Websocket clients will receive updates to events they've subscribed to. A
client can subscribe to certain events on connecting and to others - on the
fly.

An example for the former can be [mining a block](./chain_ws_api.md#block-mined) event. On connection a client can pass a list of services to pass with a query parameter `subscribe_to`. If it is not passed - the client is subscribed to all events:

* [mining a block](./chain_ws_api.md#block-mined) - keyword: `block_created`

All events to be subscribed to are to be comma separated. Keyword `all` has
the same effect as not passing the parameter at all. Examples:
```
/websocket?subscribe_to=all
/websocket?subscribe_to=block_created
/websocket?subscribe_to=event1,event2
```

Example for specific events to be subscribed on the fly are the Oracle ones as
described [here](./oracle_ws_api.md#register-for-post-query-events)

### General Request/Response types
A request has the format:

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| target | string | what component to target | Yes |
| action | string | what is the action | Yes |
| payload | object | data for action | Yes |

A response (and an event) has the format:

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| origin | string | what component did the action | Yes |
| action | string | what was the action | Yes |
| payload | object | data from the action | Yes |

### List of WS APIs
* [Oracle WS API](./oracle_ws_api.md)
* [Chain WS API](./chain_ws_api.md)

## User API - intended usage

* [Account management user API usage](./account_api_usage.md)
* [Spending tokens using user API](./spend_api_usage.md)
* [Oracle user API usage](./oracle_api_usage.md)
