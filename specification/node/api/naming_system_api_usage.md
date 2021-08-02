# Naming System - intended usage

## Introduction

The way to interact with Naming System is to use HTTP API.
To read about possible states and life cycle of a name please see [the doc](/AENS.md).

The following assumes that the node exposes at address 127.0.0.1 the following ports:
* User API external HTTP endpoint: 3013
* User API internal HTTP endpoint: 3113

## Name management flow

In order to work through the example we need the (Base58Check-encoded)
public-private key pair of the account with positive balance.

### Verify availability

Verify that the name that your going to claim is not taken using the [/names/{name} endpoint](https://api-docs.aeternity.io#/external/GetNameEntryByName).
For the purpose of this example let's consider `foobar.test` name:
```
curl http://localhost:3013/v2/names/foobar.test
{"reason":"Name not found"}
```

### Preclaim

In order to claim a name you need to submit a preclaim transaction first, containing commitment hash.

You need to pick a random salt value, to make commitment hash unique.
Commitment hash is calculated based on [the formula](/AENS.md#pre-claim).
For the purpose of this example name `foobar.test` with salt 123 is considered.
In order to obtain commitment hash use the [/debug/names/commitment-id endpoint](https://api-docs.aeternity.io#/internal/GetCommitmentId):
```
curl http://localhost:3113/v2/debug/names/commitment-id\?name\=foobar.test\&salt\=123
{"commitment_id":"cm_2ijL6NFZ11RsBVWwFB69oZYp6gFV9JSB71xccbnqrPisEiMrji"}
```

To preclaim a name:
* prepare name preclaim transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the aeternity node provides
[/debug/names/preclaim endpoint](https://api-docs.aeternity.io#/internal/PostNamePreclaim):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/preclaim -d '{"commitment_id":"cm_2ijL6NFZ11RsBVWwFB69oZYp6gFV9JSB71xccbnqrPisEiMrji", "fee": 1, "ttl":1234, "account_id":"ak_tjnw1KcmnwfqXvhtGa9GRjanbHM3t6PmEWEWtNMM3ouvNKRu5"}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)

Mind that preclaim and claim transactions will not be accepted in the same generation,
so please check that at least one key block is mined before submitting claim transaction.
To check the height of the blockchain use the [/generations/current endpoint](https://api-docs.aeternity.io#/external/GetCurrentGeneration).

### Claim

When a name is preclaimed, you are in a position to claim it:
* prepare name claim transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the aeternity node provides
[/debug/names/claim endpoint](https://api-docs.aeternity.io#/internal/PostNameClaim).
You must use the name with the same salt as used in commitment hash computation.
Note that the name should be API encoded in the same way as a name hash.
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/claim -d '{"name": ""nm_3sDdKewfAc1ektVJpwuTD", "name_salt": 123, "fee": 1, "ttl":1234, "account_id":"ak_tjnw1KcmnwfqXvhtGa9GRjanbHM3t6PmEWEWtNMM3ouvNKRu5"}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)

After claiming the name (and claim transaction being accepted) you may verify name presence using the [/names/{name} endpoint](https://api-docs.aeternity.io#/external/GetNameEntryByName).

Note that the name is claimed for the max period (50000 blocks) and relative to the current height of chain.

### Update

In order to make better use of claimed name you need to specify where it should point to.
To do so, specify pointers, which translates to different blockchain entities.
In the initial version the following well-known pointer keys are available:
* `account_pubkey`

In order to update pointers:
* prepare name update transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the aeternity node provides
[/debug/names/update endpoint](https://api-docs.aeternity.io#/internal/PostNameUpdate):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/update -d '{"name_id": "nm_2S4U3A6LGh2LASvbA1RgA6WVq9FDBCfEZK6FN5uL65MPVhiVGL", "name_ttl": 10000, "client_ttl": 50, "pointers":[{"key":"account_pubkey", "id":"ak_3scLu3oJbhsdCJkDjfJ6BUPJ4M9ZZJe57CQ56deSbEXhaTSfG3Wf3i2GYZV6APX7RDDVk4Weewb7oLePte3H3QdBw4rMZw"}], "fee": 1, "ttl":1234, "account_id":"ak_tjnw1KcmnwfqXvhtGa9GRjanbHM3t6PmEWEWtNMM3ouvNKRu5"}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)

Note that `name_ttl` is relative to the current height of the chain. Here we shortened the claim.

### Spend to name

Now you may use account and oracle pointers interchangeably with their addresses.
In order to utilize account pubkey pointer, put a name instead of an account key, e.g. in spend transaction put it in `recipient_id` field:
```
curl -X POST -H "Content-Type: application/json" -d '{"sender_id":"...", "recipient_id":"foobar.test", "amount":2, "fee":1, "ttl":1234}' http://127.0.0.1:3113/v2/debug/transactions/spend
```

### Transfer ownership

In order to transfer a name to another user:
* prepare name transfer transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the aeternity node provides
[/debug/names/transfer endpoint](https://api-docs.aeternity.io#/internal/PostNameTransfer):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/transfer -d '{name_id": "nm_2S4U3A6LGh2LASvbA1RgA6WVq9FDBCfEZK6FN5uL65MPVhiVGL", "recipient_id": "ak_3scLu3oJbhsdCJkDjfJ6BUPJ4M9ZZJe57CQ56deSbEXhaTSfG3Wf3i2GYZV6APX7RDDVk4Weewb7oLePte3H3QdBw4rMZw", "account_id":"ak_tjnw1KcmnwfqXvhtGa9GRjanbHM3t6PmEWEWtNMM3ouvNKRu5", "fee": 1, "ttl":1234}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)

### Revoke

In order to revoke a name:
* prepare name revoke transaction as per [specification](../../serializations.md).
In order to ease the initial integration, the aeternity node provides
[/debug/names/revoke endpoint](https://api-docs.aeternity.io#/internal/PostNameRevoke):
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/debug/names/revoke -d '{"name_id": "nm_2S4U3A6LGh2LASvbA1RgA6WVq9FDBCfEZK6FN5uL65MPVhiVGL", "fee": 1, "ttl":1234, "account_id":"ak_tjnw1KcmnwfqXvhtGa9GRjanbHM3t6PmEWEWtNMM3ouvNKRu5"}'
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction using the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)
