[back](./README.md)
# Channels - intended usage (JSON-RPC version)

## Introduction
The Aeternity node publishes a [JSON-RPC API](https://www.jsonrpc.org/specification)
for managing state channels over WebSocket connections. This API is intended to
replace the 'legacy' protocol.

The 'legacy' protocol is still supported, and should be considered better tested
at this time.

### Differences between JSON-RPC and 'legacy'

The structure of the `legacy` protocol can be found in [README.md](./README.md).

The JSON-RPC protocol supports both synchronous RPC and asynchronous notifications.
An RPC is indicated by the inclusion of an `'id'` parameter. The Aeternity API
can be used both synchronously and asynchronously.

Whereas the legacy protocol is entirely asynchronous, and uses the elements
`'action'`, `'tag'` and `'payload'`, the JSON-RPC API uses a corresponding
`'method`' element on the form `'channels.<Action>.<Tag>'`. If used
asynchronously, the reply will have `'method': 'channels.<Action>.<Tag>.reply'`.

Implementation support exists for batch processing, however this is not yet tested.

### Examples

Detailed message transcripts from test suites can be found [for JSON-RPC](./examples/aehttp_integration_SUITE/json-rpc/) and [for legacy](./examples/aehttp_integration_SUITE/legacy/).

#### Example, legacy:

```javascript
{'action': 'update',
 'tag': 'new',
 'payload': {
    'from': 'ak_3YGRJv1QMgNbeDzvqX7qJrZWJDaHGmrHYHifxSbhSEgn6anuNYCNPrzsB911xTbZ35bvJYWLyYjrQaQKfvja9gkpvYMfEZ',
    'to': 'ak_3gVuduh7vR9G7Hq3TpFaA7q9oQkMZZF2VsUxDYZabNeKC1uaqtjpKSth7wPn9dxnUzsHoT2fa6GPUzepbDXMHyC2F3HupT',
    'amount': 2
    }
 }
```

#### Equivalent JSON-RPC:

```javascript
{'jsonrpc': '2.0',
 'method': 'channels.update.new',
 'params': {
    'from': 'ak_3YGRJv1QMgNbeDzvqX7qJrZWJDaHGmrHYHifxSbhSEgn6anuNYCNPrzsB911xTbZ35bvJYWLyYjrQaQKfvja9gkpvYMfEZ',
    'to': 'ak_3gVuduh7vR9G7Hq3TpFaA7q9oQkMZZF2VsUxDYZabNeKC1uaqtjpKSth7wPn9dxnUzsHoT2fa6GPUzepbDXMHyC2F3HupT',
    'amount': 2
    }
 }
```

#### Example, synchronous RPC:
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

#### Example, asynchronous request-reply interaction:
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

### Error objects
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
 
 #### Example, error object:
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
