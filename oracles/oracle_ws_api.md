[back](./oracles.md)
# Oracle WebSocket API

The preferred way to interact with oracles from outside the block chain is
through a WebSocket. It is possible to do five different actions:
 * [Register an Oracle](register-an-oracle)
 * [Post a query for an Oracle](post-a-query-for-an-oracle)
 * [Answer an Oracle query](answer-an-oracle-query)
 * [Register for post query events](register-for-post-query-events) (for a particular Oracle)
 * [Register for query response events](register-for-query-response-events) (for a particular Oracle query)

## General Request/Response types
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

## [Register an Oracle]
### Request
 * **target:** `oracle`
 * **action:** `register`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | `OracleRegisterTxObject` | | Yes |
  | vsn | number | | No |
  | query_format | string |  | Yes |
  | response_format | string |  | Yes |
  | query_fee | number |  | Yes |
  | ttl | object - [TTL](#ttl) |  | Yes |
  | fee | number |  | Yes |

### Response
 * **origin:** `oracle`
 * **action:** `register`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | result | string | `ok` or error reason | Yes |
  | oracle_id | string | Hash for created oracle | Yes on success |

### Example
```
Request:
  {"target":"oracle",
   "action":"register",
   "payload":{"type":"OracleRegisterTxObject",
              "vsn":1,
              "query_format":"the query spec",
              "response_format":"the response spec",
              "query_fee":4,
              "ttl":{"type":"delta", "value":50},
              "fee":5}
  }

Response:
  {"action":"register",
   "origin":"oracle",
   "payload":{"result":"ok",
              "oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}
  }
```

## Post a query for an Oracle
### Request
 * **target:** `oracle`
 * **action:** `query`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | `OracleQueryTxObject` | | Yes |
  | vsn | number | | No |
  | oracle_pubkey | string |  | Yes |
  | query | string |  | Yes |
  | query_fee | number |  | Yes |
  | query_ttl | object - [TTL](#ttl) |  | Yes |
  | response_ttl | object - [RelativeTTL](#relativettl) |  | Yes |
  | fee | number |  | Yes |

### Response
 * **origin:** `oracle`
 * **action:** `query`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | result | string | `ok` or error reason | Yes |
  | query_id | string | Hash for created query | Yes on success |

### Example
```
Request:
  {"target":"oracle",
   "action":"query",
   "payload":{"type":"OracleQueryTxObject",
              "vsn":1,
              "oracle_pubkey":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf",
              "query_fee":4,
              "query_ttl":{"type":"delta", "value":10},
              "response_ttl":{"type":"delta", "value":10},
              "fee":7,
              "query":"How are you?"
              }
  }

Response:
  {"action":"query",
   "origin":"oracle",
   "payload":{"result":"ok",
              "query_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}
  }
```

### Answer an Oracle query
### Request
 * **target:** `oracle`
 * **action:** `response`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | `OracleResponseTxObject` | | Yes |
  | vsn | number | | No |
  | interaction_id | string |  | No |
  | response | string |  | No |
  | fee | long |  | No |

### Response
 * **origin:** `oracle`
 * **action:** `response`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | result | string | `ok` or error reason | Yes |
  | query_id | string | Hash for the answered query | Yes on success |

### Example
```
Request:
  {"target":"oracle",
   "action":"response",
   "payload":{"type":"OracleResponseTxObject",
              "vsn":1,
              "interaction_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr",
              "fee":4,
              "response":"I am fine, thanks!"}
  }

Response:
  {"origin":"oracle",
   "action":"response",
   "payload":{"result":"ok",
              "query_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}
  }
```

### Register for post query events
### Request
 * **target:** `oracle`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | `query` | | Yes |
  | oracle_id | string | | Yes |

### Response
 * **origin:** `oracle`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | result | string | `ok` or error reason | Yes |
  | subscribed_to | object - query subscribe payload | | Yes on success |

### Event
 * **origin:** `node`
 * **action:** `new_oracle_query`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | sender | string | hash of query sender | Yes |
  | query | string | | Yes |
  | query_id | string | hash that identifies the query | Yes |

### Example
```
Request:
  {"target":"oracle",
   "action":"subscribe",
   "payload":{"type":"query",
              "oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}
  }

Response:
  {"origin":"oracle",
   "action":"subscribe",
   "payload":{"result":"ok",
              "subscribed_to":{"type":"query",
                               "oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}}
  }

Event:
  {"origin":"node",
   "action":"new_oracle_query",
   "payload":{"sender":"ak$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf",
              "query":"How are you?",
              "interaction_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}
  }
```

### Register for query response events
### Request
 * **target:** `oracle`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | `response` | | Yes |
  | interaction_id | string | | Yes |

### Response
 * **origin:** `oracle`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | result | string | `ok` or error reason | Yes |
  | subscribed_to | object - response subscribe payload | | Yes on success |

### Event
 * **origin:** `node`
 * **action:** `new_oracle_response`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | interaction_id | string | hash that identifies the query | Yes |
  | query | string | | Yes |

### Example
```
Request:
  {"target":"oracle",
   "action":"subscribe",
   "payload":{"type":"response",
              "interaction_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}
  }

Response:
  {"origin":"oracle",
   "action":"subscribe",
   "payload":{"result":"ok",
              "subscribed_to":{"type":"response",
                               "interaction_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}}
  }

Event:
  {"origin":"node",
   "action":"new_oracle_response",
   "payload":{"response":"I am fine, thanks!",
              "interaction_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}
  }
```

## Additional types
### TTL

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| type | string | `block` or `delta` | Yes |
| value | number |  | Yes |

### RelativeTTL

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| type | `delta` |  | Yes |
| value | number |  | Yes |


**Current limitation:** Since there is currently no interface for offline signing
(all signing is done by a node - and that node is associated with exactly one
account) it is somewhat limited what you can do with oracles. I.e. in practice
you need a node per account - obviously this is a limitation we should try to
lift as soon as possible.

## Detailed example - Oracle life cycle

For simplicity, we only work with a single node (`localhost/127.0.0.1`) in this
example, but it should be straightforward to split the example into one node
running the oracle and other nodes querying that oracle. In the default node
configuration the websocket interface is at *port 3014* - i.e. connecting to
`ws://127.0.0.1:3114/websocket` open a websocket connection.

In order to work through the example we also need the (Base58Check-encoded)
public key of the node. This is easily retrieved from the running node:
```
~/epoch/node: curl http://127.0.0.1:3113/v1/account/pub-key
{"pub_key":"ak$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}
```

On a freshly started node, connect a websocket. (Here we use
[WSCat](https://github.com/websockets/wscat) for the websocket connection.)
Upon connection the client automatically subscribe to the _mined_block_-event,
i.e. everytime the node mine a new block an event is pushed to the client. We
need to wait for the first block to be mined by the node (or else our
transactions will be rejected with _"Insufficient balance"_).

```
~/epoch/node: wscat -c ws://127.0.0.1:3114/websocket
connected (press CTRL+C to quit)
< {"action":"mined_block","origin":"miner","payload":{"height":1,"hash":"bh$jXjgHkcuXnTY4PtMpctcwFT2jf4fZ1jGdeax1geWoW64hSXpY"}}
```

Once the account has a positive balance we can post an _"Oracle register transaction"_:
```
...
> {"target":"oracle", "action":"register", "payload":{"type":"OracleRegisterTxObject", "vsn":1, "account":"ak$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf", "query_format":"the query spec", "response_format":"the response spec", "query_fee":4, "ttl":{"type":"delta", "value":50}, "fee":5}}
< {"action":"register","origin":"oracle","payload":{"result":"ok","oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}}
```

The register transaction use the same format for the payload as the HTTP API
(<link to Swagger API description>). **NOTE:** the *transaction fee* is
depending on the _TTL_. An oracle register transaction costs 4, and then 1 per
1000 blocks of life time. (I.e. a TTL of 50 blocks --> 5, and a TTL of 4500
blocks --> 9)

This means that we have created the transaction to create the oracle, once the
next block is mined this transaction will be included. Now, when the oracle
exists we can register for getting events whenever a query is posted to this
Oracle:
```
...
< {"action":"mined_block","origin":"miner","payload":{"height":2,"hash":"bh$2UuiuAHW8bmRkcoMqP2Mcj5ZrxvGzjhQRhictByxf4AhcyF4q"}}
> {"target":"oracle","action":"subscribe", "payload":{"type":"query","oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}}
< {"action":"subscribe","origin":"oracle","payload":{"result":"ok","subscribed_to":{"oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf","type":"query"}}}
```

We subscribe for `"type":"query"`, i.e. we want to get notified when the oracle
with the given id receive a query. Of course we want to test this, so let us
post a query...
```
...
> {"target":"oracle", "action":"query", "payload":{"type":"OracleQueryTxObject", "vsn":1, "oracle_pubkey":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf", "query_fee":4, "query_ttl":{"type":"delta", "value":10}, "response_ttl":{"type":"delta", "value":10}, "fee":7, "query":"How are you?"}}
< {"action":"query","origin":"oracle","payload":{"result":"ok","query_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}}
```

Again we use exactly the same format for the payload as the HTTP API. And also,
similar to the oracle registration transaction, the _transaction fee_ depends
on the _TTL_ **and** the oracle query fee. The base query transaction fee is 2,
we set the oracle query fee to 4 when registering, and the TTL accounts for 1
per 1000 blocks (just a preliminary value to test the concept). I.e. the cost
for our test transaction is 7.

Not much will happen until the node mine another block (and the query
transaction gets included in the blockchain), but once that happens we should
receive an event on the websocket:
```
...
< {"action":"mined_block","origin":"miner","payload":{"height":4,"hash":"bh$K6oGLV2cHMMpmKjr7bKAByqCxVRwhNUUh5nACagXknARLUbJ3"}}
< {"action":"new_oracle_query","origin":"node","payload":{"sender":"ak$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf","query":"How are you?","interaction_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}}
```

We should note that in the response for the query request above we got the
*query_id*, this can be used (by Bob in the oracle life cycle example) to
subscribe to an event when the query gets answered. (We also got it in the
*new_oracle_query* event, but that event would normally be received by Alice
rather than Bob...)

```
...
> {"target":"oracle","action":"subscribe", "payload":{"type":"query","oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}}
< {"action":"subscribe","origin":"oracle","payload":{"result":"ok","subscribed_to":{"oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf","type":"query"}}}
```

We subscribe for `"type":"response"`, i.e. we want to get notified when the
oracle answer the query with the given id. Of course we want to test this as
well, so let us post a response to the query.

```
...
> {"target":"oracle", "action":"response", "payload":{"type":"OracleResponseTxObject", "vsn":1, "interaction_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr", "fee":3, "response":"I am fine, thanks!"}}
< {"action":"response","origin":"oracle","payload":{"result":"ok","query_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}}
```

Also here we use exactly the same format for the payload as the HTTP API. The
_transaction fee_ depends on the _TTL_ (as set in the query). The base response
transaction fee is 2 and the TTL accounts for 1 per 1000 blocks I.e. the cost
for our test transaction is 3.

If we then wait for another block to be mined (and the response transaction to
be added to the chain), we see that we receive an event reflecting the query
response:
```
...
< {"action":"mined_block","origin":"miner","payload":{"height":6,"hash":"bh$i9P6dgcihe47Kwm6ZvTDb84HPGWr147KPviatJ5QXntHrBY1m"}}
< {"action":"new_oracle_response","origin":"node","payload":{"interaction_id":"oi$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr","response":"I am fine, thanks!"}}
```

This conclude the walk through of the oracle life cycle example, which also
exercise the websocket API for Oracles fully.

### Alternative usage

Of course the oracle transactions can just as well be supplied through the HTTP
API. Registering for update events has to be done through WebSockets.
