[back](./oracles.md)
# Oracles - intended usage

To show the intended usage of oracles we walk through basically the [Oracle
life cycle](./oracle_life_cycle.md) For simplicity, we only work with a single
node (`localhost/127.0.0.1`) in this example. It should be straightforward
to split the example into one node running the oracle and other nodes querying
that oracle. In the default node configuration the websocket interface is at
*port 3014* - i.e. connecting to `ws://127.0.0.1:3114/websocket` opens a
websocket connection.

In order to work through the example we also need the (Base58Check-encoded)
public key of the node. This is easily retrieved from the running node:
```
~/epoch/node: curl http://127.0.0.1:3113/v1/account/pub-key
{"pub_key":"ak$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}
```

On a freshly started node, connect a websocket. (Here we use
[WSCat](https://github.com/websockets/wscat) for the websocket connection.)
Upon connection the client automatically subscribes to the _mined_block_-event,
i.e. everytime the node mines a new block an event is pushed to the client. We
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

The register transaction uses the same format for the payload as the HTTP API
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
with the given id receives a query. Of course we want to test this, so let us
post a query...
```
...
> {"target":"oracle", "action":"query", "payload":{"type":"OracleQueryTxObject", "vsn":1, "oracle_pubkey":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf", "query_fee":4, "query_ttl":{"type":"delta", "value":10}, "response_ttl":{"type":"delta", "value":10}, "fee":7, "query":"How are you?"}}
< {"action":"query","origin":"oracle","payload":{"result":"ok","query_id":"oq$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}}
```

Again we use exactly the same format for the payload as the HTTP API. And also,
similar to the oracle registration transaction, the _transaction fee_ depends
on the _TTL_ **and** the oracle query fee. The base query transaction fee is 2,
we set the oracle query fee to 4 when registering, and the TTL accounts for 1
per 1000 blocks (just a preliminary value to test the concept). I.e. the cost
for our test transaction is 7.

Not much will happen until the node mines another block (and the query
transaction gets included in the blockchain), but once that happens we should
receive an event on the websocket:
```
...
< {"action":"mined_block","origin":"miner","payload":{"height":4,"hash":"bh$K6oGLV2cHMMpmKjr7bKAByqCxVRwhNUUh5nACagXknARLUbJ3"}}
< {"action":"new_oracle_query","origin":"node","payload":{"sender":"ak$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf","query":"How are you?","query_id":"oq$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}}
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
oracle answers the query with the given id. Of course we want to test this as
well, so let us post a response to the query.

```
...
> {"target":"oracle", "action":"response", "payload":{"type":"OracleResponseTxObject", "vsn":1, "query_id":"oq$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr", "fee":3, "response":"I am fine, thanks!"}}
< {"action":"response","origin":"oracle","payload":{"result":"ok","query_id":"oq$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr"}}
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
< {"action":"new_oracle_response","origin":"node","payload":{"query_id":"oq$4RZoMEkm8QuuhJiiq53dd5pE4VstCthYRjBHgUKdhAhe7rLEr","response":"I am fine, thanks!"}}
```

This conclude the walk through of the oracle life cycle example, which also
exercise the websocket API for Oracles fully.

### Alternative usage

Of course the oracle transactions can just as well be supplied through the HTTP
API. Registering for update events has to be done through WebSockets.
