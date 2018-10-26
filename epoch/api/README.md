# Æternity epoch node API

This document:
* Provides an overview of the API exposed by the epoch node;
* Defines the Channels WebSocket API of the epoch node;
* Describes the intended usage of the user API of the epoch node.

## Overview

The epoch node exposes the following APIs:
* Peer-to-peer network API. It consists of one TCP endpoint:
  * It is encrypted and authenticated using the Noise protocol;
  * The schema of its payload is [defined](/sync/);
  * It is meant to be exposed on the Internet;
  * Its TCP port is configurable.
  * Its static Noise key pair is configurable.
* User API. It consists of the following TCP endpoints:
  * External HTTP endpoint;
    * It is defined via Swagger schema;
    * It is meant to be exposed on the Internet;
    * Its TCP port is configurable.
  * Internal HTTP endpoint;
    * It is defined via Swagger schema;
    * It is **not** meant to be exposed on the Internet;
    * Its TCP port is configurable.
  * Internal Channels WebSocket endpoint.
    * It is defined in the rest of this document;
    * It is not meant to be exposed on the Internet;
    * Its TCP port is configurable.
  * Range of external Channels noise endpoints. It consists of as many TCP
    endpoints as needed.
    * They are used for connecting as a `responder` role in channel
      communication;
    * It is up to the node operator to define the range to be used; Their
      configuration is not part of `epoch`;
    * They are encrypted and authenticated using the Noise protocol using
      dynamic keys;
    * The schema of its payload is [defined](/channels/OFF-CHAIN.md#messages);
    * They are meant to be exposed on the Internet;

## Channels WebSocket API definition

**NOTE:** A description of the newer JSON-RPC-based protocol [can be found here](./channel_ws_api_json-rpc.md)

### Description
Channels provide means for off-chain transactions with functionality of on-chain dispute resolution.
Channels require persisted connections to Aeternity nodes. Each participant in
a channel uses one's own trusted node. For persistence of this connection, WebSockets
are used.
Channels have on-chain state that persists who the participants are and the
total amout of tokens put into the channel.
Each channel also has an off-chain state representing the latest distribution of the balance of the
channel. It can be updated - each new state is co-signed by both parties and only then it becomes the latest valid state of the
channel. At any point in time channel can be closed either unilaterally or
through mutual agreement.

### Connection
The epoch node supports an endpoint with a configurable port where the
WebSocket's clients connect. It is located on `/channel`.

The node could serve multiple channel WebSocket clients. Their number is configured in
the `epoch.yaml`. When all WebSocket connections are consumed - any new incoming
connections will be queued. The queue has a maximum size and when it is
reached, any new incoming connections will be rejected with an error code 400.
This is to prevent the node of being overloaded with WebSocket connections.

### General message types
All messages have the format:

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| action | string | what is the action | Yes |
| tag | string | additional info for the action | No |
| payload | object | data for action | Yes |

## User API - intended usage

* [Account management user API usage](./account_api_usage.md)
* [Spending tokens using user API](./spend_api_usage.md)
* [Oracle user API usage](./oracle_api_usage.md)
* [Naming system API usage](./naming_system_api_usage.md)
* [Contract API usage](./contract_api_usage.md)
* [Channels API usage](./channels_api_usage.md)
* [Mining API usage](./mining_api_usage.md)
