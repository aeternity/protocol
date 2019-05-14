# Æternity node API

This document:
* Provides an overview of the API exposed by the Aeternity node;
* Defines the Channels WebSocket API of the Aeternity node;
* Describes the intended usage of the user API of the Aeternity node.

## Overview

The Aeternity node exposes the following APIs:
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
      configuration is not part of the Aeternity node;
    * They are encrypted and authenticated using the Noise protocol using
      dynamic keys;
    * The schema of its payload is [defined](/channels/OFF-CHAIN.md#messages);
    * They are meant to be exposed on the Internet;

## Channels WebSocket API definition

The Aeternity node publishes a [JSON-RPC API](https://www.jsonrpc.org/specification)
for managing state channels over WebSocket connections. The 'legacy' protocol was removed.

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

The Aeternity node supports an endpoint with a configurable port where the
WebSocket's clients connect. It is located on `/channel`.

The node could serve multiple channel WebSocket clients. Their number is configured in
the `epoch.yaml`. When all WebSocket connections are consumed - any new incoming
connections will be queued. The queue has a maximum size and when it is
reached, any new incoming connections will be rejected with an error code 400.
This is to prevent the node of being overloaded with WebSocket connections.

### Messages overview

The JSON-RPC protocol supports both synchronous RPC and asynchronous notifications.
An RPC is indicated by the inclusion of an `'id'` parameter. The Aeternity API
can be used both synchronously and asynchronously. When an asynchronous method is called, the reply will have `'method': '<RequestMethod>.reply'`.

Implementation support exists for batch processing, however this is not yet tested.

### Examples

#### Example, synchronous RPC

```javascript
{
  "jsonrpc": "2.0",
  "id": -576460752303423475,
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
    ]
  }
}
```

**Reply:**
```javascript
{
  "jsonrpc": "2.0",
  "id": -576460752303423475,
  "result": [
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 699
    },
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 401
    }
  ]
}
```

#### Example, asynchronous request-reply interaction

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
    "contract": "ct_28pwhjFEVfuirjPzJDRTE4o4ybjKw7vjMymRdhhVrDEVTuXAtq",
    "round": 8
  }
}
```

**Reply:**
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "undefined",
    "data": {
      "caller_id": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "caller_nonce": 8,
      "contract_id": "ct_28pwhjFEVfuirjPzJDRTE4o4ybjKw7vjMymRdhhVrDEVTuXAtq",
      "gas_price": 1,
      "gas_used": 387,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_11111111111111111111111111111115rHyByZ"
    }
  }
}
```

Note that when the node sends an asynchronous notification, the `'params'` element
contains the `'channel_id'` and a `'data'` element. The latter contains the
same information as the `'result'` element in an RPC reply, and the `'payload'`
element in the `legacy` protocol (except that if the `'channel_id'` was
present in the payload, it is removed from `'data'` and only passed as an
element of `'params'`.)

#### Error objects

If an error occurs, a JSON-RPC error object is returned. It has the following form:

```javascript
{'jsonrpc': '2.0',
 'id': null,
 'error' : {
   'code': <ErrorCode>,
   'message': <ErrorMessage>,
   'data': [ ... ],
   'request': { ... }
  }
 }
 ```

The codes and error messages include those specified in the [JSON-RPC 2.0
 Specification](https://www.jsonrpc.org/specification#error_object) [1], some used (or proposed) [by Ethereum](https://github.com/ethereum/wiki/wiki/JSON-RPC-Error-Codes-Improvement-Proposal) [2], and some Aeternity-specific [3].

 | Code   | Message            | Origin |
 | ------ | ------------------ | ------ |
 | -32700 | Parse error        | [1]    |
 | -32000 | Invalid request    | [1]    |
 | -32601 | Method not found   | [1]    |
 | -32602 | Invalid params     | [1]    |
 | -32603 | Internal error     | [1]    |
 |      1 | Unauthorized       | [2]    |
 |      2 | Action not allowed | [2]    |
 |      3 | Rejected           | [2]    |

The `'data'` element may contain more detailed information inside `'data'`:

 | Code   | Message                   | Parent Code | Origin |
 | ------ | ------------------------- | ----------- | ------ |
 | 100    | X doesn't exist           |  3          |  [2]   |
 | 101    | Requires coin             |  3          |  [2]   |
 | 102    | Gas too low               |  3          |  [2]   |
 | 103    | Gas limit exceeded        |  3          |  [2]   |
 | 104    | Rejected                  |  3          |  [2]   |
 | 105    | Value too low             |  3          |  [2]   |
 | 106    | Timeout                   |  3          |  [2]   |
 | 107    | Conflict                  |  3          |  [2]   |
 | 1001   | Insufficient balance      |  3          |  [3]   |
 | 1002   | Negative amount           |  3          |  [3]   |
 | 1003   | Invalid pubkeys           |  3          |  [3]   |
 | 1004   | Call not found            |  3          |  [3]   |
 | 1005   | Broken encoding: accounts |  3          |  [3]   |
 | 1006   | Broken encoding: contracts|  3          |  [3]   |
 | 1007   | Contract init failed      |  3          |  [3]   |
 | 1008   | Not a number              |  3          |  [3]   |

#### Example, error object
 ```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
        "contract": "ct_28pwhjFEVfuirjPzJDRTE4o4ybjKw7vjMymRdhhVrDEVTuXAtq",
        "round": 8
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```
Detailed message transcripts from test suites can be found [here](./examples/channels/json-rpc/).

## User API - intended usage

* [Encoding scheme for API identifiers](./api_encoding.md)
* [Account management user API usage](./account_api_usage.md)
* [Spending tokens using user API](./spend_api_usage.md)
* [Oracle user API usage](./oracle_api_usage.md)
* [Naming system API usage](./naming_system_api_usage.md)
* [Contract API usage](./contract_api_usage.md)
* [Channels API usage](./channels_api_usage.md)
* [Mining API usage](./mining_api_usage.md)
