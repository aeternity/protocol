# Oracles - intended usage

The most general way to interact with Oracles is to use the HTTP API. In this
document the API is put to use, showing the complete life cycle of an Oracle.

To show the intended usage of oracles we walk through basically the [Oracle
life cycle](../../oracles/oracle_life_cycle.md) For simplicity, we only work with a single
node in this example. It should be straightforward
to split the example into one node running the oracle and other nodes querying
that oracle.

The following assumes that the node exposes at address `localhost/127.0.0.1` the following ports:

* User API external HTTP endpoint: 3013
* User API internal HTTP endpoint: 3113

## Oracle management flow

In order to work through the example we need the (Base58Check-encoded)
public key of the account with positive balance. For simplicity, we will use
beneficiary account. It is easily retrieved from the running node:

```
curl http://127.0.0.1:3113/v2/debug/accounts/beneficiary

{"pub_key":"ak_jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdF"}
```

We need to wait for the first block to be mined by the node (or else our
transactions will be rejected with _"Insufficient balance"_).

### Register

Once the account has a positive balance we can register an oracle:

* prepare oracle register transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the æternity node provides
[/debug/oracles/register endpoint](https://api-docs.aeternity.io#/internal/PostOracleRegister):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/oracles/oracle -d '{"account_id:"ak_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov", "query_format":"the query spec", "response_format":"the response spec", "query_fee":4, "oracle_ttl":{"type":"delta", "value":50}, "fee":2, "ttl":1234}'
{"tx":"..."}
```
**NOTE:** the *transaction fee* is depending on the _TTL_. An oracle register
transaction costs at least 1 (as all other transactions), plus 1 per 1000 blocks of life time. (I.e. a TTL of
50 blocks --> 2, and a TTL of 4500 blocks --> 6)
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)

This means that we have created the transaction to create the oracle, once the
next block is mined this transaction will be included. We can verify that the
oracle is created:
```
curl http://localhost:3013/v2/oracles/ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov

{"expires":51,"id":"ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","query_fee":4,"query_format":"the query spec","response_format":"the response spec"}
```

### Extend

Now, when the oracle exists, we can extend the TTL:

* prepare oracle extend transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the æternity node provides
[/debug/oracles/extend endpoint](https://api-docs.aeternity.io#/internal/PostOracleExtend):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/oracles/extend -d '{"oracle_id":"ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov", "fee":5, "oracle_ttl":{"type":"delta", "value":100}}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)

Again, we can check that the TTL was extended:
```
curl http://localhost:3013/v2/oracles/ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov

{"expires":151,"id":"ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","query_fee":4,"query_format":"the query spec","response_format":"the response spec"}
```

### Query

We can post a query to the existing oracle:

* prepare oracle query transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the æternity node provides
[/debug/oracles/query endpoint](https://api-docs.aeternity.io#/internal/PostOracleQuery):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/oracles/query -d '{"oracle_id":"ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov", "query_fee":4, "query_ttl":{"type":"delta", "value":10}, "response_ttl":{"type":"delta", "value":10}, "fee":2, "ttl":15, "query":"How are you?"}'
{"tx":"..."}
```
**NOTE** Similarly to the oracle registration transaction, the _transaction fee_ field depends
on the query _TTL_. The base query transaction fee is 1 (as all other transactions),
and the TTL accounts for 1 per 1000 blocks (just a preliminary value to test the concept). I.e. the minimum fee field for our test transaction is 2.
We specify query fee 4 - that is the minimum considering that the oracle was registered with query fee 4.
Therefore the cost of the transaction is 6.
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)

We can check the active oracle queries:
```
curl http://localhost:3013/v2/oracles/ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov/queries

{"oracle_queries":[{"expires":13,"fee":4,"oracle_id":"ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","query":"ov_9wnkKJ3Qf2trdpq9EQbWQC","query_id":"oq_2f9NqPf39Hin4FZoYCyL66zcyZEQJ3L2K7ZGQFbTR3PdT3u2m","response":"or_3QJmnh","response_ttl":{"type":"delta","value":10},"sender_id":"ak_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","sender_nonce":3}]}
```

**NOTE** the query and response values are Base58Check-encoded.

### Respond

We should note that in the response for the query request above we got the
*query_id* which we use to respond to the query:

* prepare oracle respond transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the æternity node provides
[/debug/oracles/respond endpoint](https://api-docs.aeternity.io#/internal/PostOracleRespond):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/oracles/respond -d '{"query_id":"oq_2f9NqPf39Hin4FZoYCyL66zcyZEQJ3L2K7ZGQFbTR3PdT3u2m", "response_ttl":{"type":"delta", "value":10}, ""fee":2, "ttl":1234, "response":"I am fine, thanks!"}'
{"tx":"..."}
```
**NOTE** The _transaction fee_ depends on the response _TTL_ (as set in the query). The base
response transaction fee is 1 (as all other transactions) and the TTL accounts for 1 per 1000 blocks
I.e. the cost for our test transaction is 2.
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)

If we then wait for another block to be mined (and the response transaction to
be added to the chain), we see that there is a response for the query:
```
curl http://localhost:3013/v2/oracles/ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov/queries

{"oracle_queries":[{"expires":14,"fee":4,"oracle_id":"ok_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","query":"ov_9wnkKJ3Qf2trdpq9EQbWQC","query_id":"oq_2f9NqPf39Hin4FZoYCyL66zcyZEQJ3L2K7ZGQFbTR3PdT3u2m","response":"or_Lr9RvdW8vZR8wq14ic7yUyC2vzi4nT","response_ttl":{"type":"delta","value":10},"sender_id":"ak_EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","sender_nonce":3}]}
```

**NOTE** the query and response values are Base58Check-encoded.

This conclude the walk through of the oracle life cycle example, which also
exercise the HTTP API for Oracles fully.

### Alternative usage

TODO: WS API in the middleware.
