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
