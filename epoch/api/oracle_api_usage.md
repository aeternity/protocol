[back](./README.md)
# Oracles - intended usage

The most general way to interact with Oracles is to use the HTTP API. In this
document the API is put to use, showing the complete life cycle of an Oracle.

To show the intended usage of oracles we walk through basically the [Oracle
life cycle](/oracles/oracle_life_cycle.md) For simplicity, we only work with a single
node in this example. It should be straightforward
to split the example into one node running the oracle and other nodes querying
that oracle.

The following assumes that the node exposes at address `localhost/127.0.0.1` the following ports:
* User API external HTTP endpoint: 3013
* User API internal HTTP endpoint: 3113

## Oracle management flow

In order to work through the example we also need the (Base58Check-encoded)
public key of the node. This is easily retrieved from the running node:
```
curl http://127.0.0.1:3113/v2/debug/accounts/node

{"pub_key":"ak$jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdF"}
```

We need to wait for the first block to be mined by the node (or else our
transactions will be rejected with _"Insufficient balance"_).

### Register

Once the account has a positive balance we can post an _"Oracle register transaction"_:
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/oracle-register-tx -d '{"type":"OracleRegisterTxObject", "vsn":1, "account":"ak$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov", "query_format":"the query spec", "response_format":"the response spec", "query_fee":4, "oracle_ttl":{"type":"delta", "value":50}, "fee":5, "ttl":1234}'

{"oracle_id":"ok$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","tx_hash":"th$2sDoWh1qe7PJ3nRJeqY4kaX7rjgWAaUVpET3EEGJvuPk3oaKNR"}
```

**NOTE:** the *transaction fee* is depending on the _TTL_. An oracle register
transaction costs 4, and then 1 per 1000 blocks of life time. (I.e. a TTL of
50 blocks --> 5, and a TTL of 4500 blocks --> 9)

This means that we have created the transaction to create the oracle, once the
next block is mined this transaction will be included. We can verify that the
oracle is created:
```
http://localhost:3013/v2/oracles/ok%24EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov

{"expires":51,"id":"ok$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","query_fee":4,"query_format":"the query spec","response_format":"the response spec"}
```

### Extend

Now, when the oracle exists, we can extend the TTL by posting an _"Oracle extend
transaction"_:
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/oracle-extend-tx -d '{"type":"OracleExtendTxObject", "vsn":1, "oracle":"ok$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov", "fee":5, "oracle_ttl":{"type":"delta", "value":100}}'

{"oracle_id":"ok$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","tx_hash":"th$ACd8e5kcPrqQKg3pyEGTq7tBtdgLZ4MHd7MuPisUxHGjFgWRj"}
```

Again, we can check that the TTL was extended:
```
curl http://localhost:3013/v2/oracles/ok%24EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov

{"expires":151,"id":"ok$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","query_fee":4,"query_format":"the query spec","response_format":"the response spec"}
```

### Query

We can post a query to the existing oracle using an _"Oracle query transaction"_:
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/oracle-query-tx -d '{"type":"OracleQueryTxObject", "vsn":1, "oracle_pubkey":"ok$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov", "query_fee":4, "query_ttl":{"type":"delta", "value":10}, "response_ttl":{"type":"delta", "value":10}, "fee":7, "ttl":15, "query":"How are you?"}'

{"query_id":"oq$2f9NqPf39Hin4FZoYCyL66zcyZEQJ3L2K7ZGQFbTR3PdT3u2m","tx_hash":"th$2rJbVzsNSB6NGYccpCDrTn1EyLkQCCyYwYhUphCkTbWLNmg795"}
```

Similarly to the oracle registration transaction, the _transaction fee_ depends
on the _TTL_ **and** the oracle query fee. The base query transaction fee is 2,
we set the oracle query fee to 4 when registering, and the TTL accounts for 1
per 1000 blocks (just a preliminary value to test the concept). I.e. the cost
for our test transaction is 7.

We can check the active oracle queries:
```
curl http://localhost:3013/v2/oracles/ok%24EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov/queries

{"oracle_queries":[{"expires":13,"fee":4,"oracle_id":"ok$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","query":"ov$9wnkKJ3Qf2trdpq9EQbWQC","query_id":"oq$2f9NqPf39Hin4FZoYCyL66zcyZEQJ3L2K7ZGQFbTR3PdT3u2m","response":"or$3QJmnh","response_ttl":{"type":"delta","value":10},"sender":"ak$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","sender_nonce":3}]}
```

**NOTE** the query value is Base58Check-encoded.

### Response

We should note that in the response for the query request above we got the
*query_id* which we use to respond to the query using an _"Oracle response
transaction"_:

```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/oracle-response-tx -d '{"type":"OracleResponseTxObject", "vsn":1, "query_id":"oq$2f9NqPf39Hin4FZoYCyL66zcyZEQJ3L2K7ZGQFbTR3PdT3u2m", "fee":3, "ttl":1234, "response":"I am fine, thanks!"}'

{"query_id":"oq$2f9NqPf39Hin4FZoYCyL66zcyZEQJ3L2K7ZGQFbTR3PdT3u2m","tx_hash":"th$HjWH76qbDNCb3eGPmwtRSM5wJcyjcSSy2LMFwe4zoCL2VLcDc"}
```

The _transaction fee_ depends on the _TTL_ (as set in the query). The base
response transaction fee is 2 and the TTL accounts for 1 per 1000 blocks
I.e. the cost for our test transaction is 3.

If we then wait for another block to be mined (and the response transaction to
be added to the chain), we see that there is a response for the query:
```
curl http://localhost:3013/v2/oracles/ok%24EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov/queries

{"oracle_queries":[{"expires":14,"fee":4,"oracle_id":"ok$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","query":"ov$9wnkKJ3Qf2trdpq9EQbWQC","query_id":"oq$2f9NqPf39Hin4FZoYCyL66zcyZEQJ3L2K7ZGQFbTR3PdT3u2m","response":"or$Lr9RvdW8vZR8wq14ic7yUyC2vzi4nT","response_ttl":{"type":"delta","value":10},"sender":"ak$EmJyR97vW4jzdcCPCvgjUa8RUmo45E1KnExBum38yz48Frwov","sender_nonce":3}]}
```

**NOTE** the response value is Base58Check-encoded.

This conclude the walk through of the oracle life cycle example, which also
exercise the HTTP API for Oracles fully.

### Alternative usage

TODO: WS API in the middleware.
