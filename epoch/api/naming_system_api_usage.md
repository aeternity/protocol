[back](./README.md)
# Naming System - intended usage

## Introduction

The way to interact with Naming System is to use HTTP API.
To read about possible states and life cycle of a name please see [the doc](/AENS.md).

The following assumes that the node exposes at address 127.0.0.1 the following ports:
* User API external HTTP endpoint: 3013
* User API internal HTTP endpoint: 3113

## Name management flow

In order to work through the example we need the (Base58Check-encoded)
public key of the account with positive balance. For simplicity, we will use
beneficiary account. It is easily retrieved from the running node:

```
curl http://127.0.0.1:3113/v2/debug/accounts/beneficiary

{"pub_key":"ak_jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdF"}
```

We need to wait for the first block to be mined by the node (or else our
transactions will be rejected with _"Insufficient balance"_).

### Verify availability

Verify that the name that your going to claim is not taken using the [/names/{name} endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/GetNameEntryByName).
For the purpose of this example let's consider `foobar.aet` name:
```
curl http://localhost:3013/v2/names/foobar.aet
{"reason":"Name not found"}
```

### Preclaim

In order to claim a name you need to submit a preclaim transaction first, containing commitment hash.

You need to pick a random salt value, to make commitment hash unique.
Commitment hash is calculated based on [the formula](/AENS.md#pre-claim).
For the purpose of this example name `foobar.aet` with salt 123 is considered.
In order to obtain commitment hash use the [/debug/names/commitment-id endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/GetCommitmentId):
```
curl http://localhost:3013/v2/debug/names/commitment-id\?name\=foobar.aet\&salt\=123
{"commitment_id":"cm_cwe2wGMbiNkXadsw1vzDDCKgi1TunyWgpz3s9fGPE25gJJnHK"}
```

To preclaim a name:
* prepare name preclaim transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the epoch node provides
[/debug/names/preclaim endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostNamePreclaim):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/preclaim -d '{"commitment_id":"cm_cwe2wGMbiNkXadsw1vzDDCKgi1TunyWgpz3s9fGPE25gJJnHK", "fee": 1, "ttl":1234}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostTransaction)

Mind that preclaim and claim transactions will not be accepted in the same block,
so please check that at least one block is mined before submitting claim transaction.
To check the height of the blockchain use the [/generations/current endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/GetCurrentGeneration).

### Claim

When a name is preclaimed, you are in a position to claim it:
* prepare name claim transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the epoch node provides
[/debug/names/claim endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostNameClaim).
You must use the name with the same salt as used in commitment hash computation:
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/claim -d '{"name": "foobar.aet", "name_salt": 123, "fee": 1, "ttl":1234}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostTransaction)

After claiming the name (and claim transaction being accepted) you may verify name presence using the [/names/{name} endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/GetNameEntryByName).

Note that the name is claimed for the max period (50000 blocks) and relative to the current height of chain.

### Update

In order to make better use of claimed name you need to specify where it should point to.
To do so, specify pointers, which translates to different blockchain entities.
In the initial version two pointers are available:
* `account_id`
* `oracle_id`

In order to update pointers:
* prepare name update transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the epoch node provides
[/debug/names/update endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostNameUpdate):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/update -d '{"name_id": "...", "name_ttl": 10000, "client_ttl": 50, "pointers":[{"key":"account_pubkey", "id":"ak_3scLu3oJbhsdCJkDjfJ6BUPJ4M9ZZJe57CQ56deSbEXhaTSfG3Wf3i2GYZV6APX7RDDVk4Weewb7oLePte3H3QdBw4rMZw"}], "fee": 1, "ttl":1234}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostTransaction)

Note that `name_ttl` is relative to the current height of the chain. Here we shortened the claim.

### Spend to name

Now you may use account and oracle pointers interchangeably with their addresses.
In order to utilize account pubkey pointer, put a name instead of an account key, e.g. in spend transaction put it in `recipient_id` field:
```
curl -X POST -H "Content-Type: application/json" -d '{"sender_id":"...", "recipient_id":"foobar.aet", "amount":2, "fee":1, "ttl":1234}' http://127.0.0.1:3113/v2/debug/transactions/spend
```

### Transfer ownership

In order to transfer a name to another user:
* prepare name transfer transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the epoch node provides
[/debug/names/transfer endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostNameTransfer):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/transfer -d '{name_id": "nm_sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC", "recipient_id": "ak_3scLu3oJbhsdCJkDjfJ6BUPJ4M9ZZJe57CQ56deSbEXhaTSfG3Wf3i2GYZV6APX7RDDVk4Weewb7oLePte3H3QdBw4rMZw", "account_id":"ak_3scLu3oJbhsdCJkDjfJ6BUPJ4M9ZZJe57CQ56deSbEXhaTSfG3Wf3i2GYZV6APX7RDDVk4Weewb7oLePte3H3Qd",  "fee": 1, "ttl":1234}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostTransaction)

### Revoke

In order to revoke a name:
* prepare name revoke transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the epoch node provides
[/debug/names/revoke endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostNameRevoke):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/revoke -d '{"name_id": "nm_sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC", "fee": 1, "ttl":1234}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostTransaction)
