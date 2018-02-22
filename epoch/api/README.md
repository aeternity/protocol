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
client can subscribe (and unsubscribe) to events on the fly. Subscribe is
described in [Chain WS API - Subscribe](./chain_ws_api.md#subscribe) and an
example usage for oracles can be seen in [Oracle user API usage](./oracle_api_usage.md).

### General Request/Response/Event types
A request has the format:

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| target | string | what component to target | Yes |
| action | string | what is the action | Yes |
| tag | string | tag to be included in response | No |
| payload | object | data for action | Yes |

A response has the format:

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| origin | string | what component did the action | Yes |
| action | string | what was the action | Yes |
| tag | string | tag from request (or `untagged`) | Yes |
| payload | object | data from the action | Yes |

An event has the same type as a response, except for not having a tag:

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
* [Naming system API usage](./naming_system_api_usage.md)
* [Contract API usage](./contract_api_usage.md)
