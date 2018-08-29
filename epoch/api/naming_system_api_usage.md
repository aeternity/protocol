[back](./README.md)
# Naming System - intended usage

## Introduction

The way to interact with Naming System is to use HTTP API.
To read about possible states and life cycle of a name please see [the doc](/AENS.md).

The following assumes that the node exposes at address 127.0.0.1 the following ports:
* User API external HTTP endpoint: 3013
* User API internal HTTP endpoint: 3113

## Name management flow

Check the public key of the node first (used as account key in later API calls):
```
curl http://127.0.0.1:3113/v2/debug/accounts/node
{"pub_key":"ak$scLu3oJbhsdCJkDjfJ6BUPJ4M9ZZJe57CQ56deSbEXhaTSf"}
```

### Verify availability

Verify that the name that your going to claim is not taken.
For the purpose of this example let's consider `foobar.aet` name:
```
curl http://localhost:3013/v2/name\?name\=foobar.aet
{"reason":"Name not found"}
```

### Preclaim

In order to claim a name you need to submit a preclaim transaction first, containing commitment hash.

You need to pick a random salt value, to make commitment hash unique.
Commitment hash is calculated based on [the formula](/AENS.md#pre-claim).
For the purpose of this example name `foobar.aet` with salt 123 is considered.
In order to obtain commitment hash use the following API:
```
curl http://localhost:3013/v2/commitment-hash\?name\=foobar.aet\&salt\=123
{"commitment":"cm$cwe2wGMbiNkXadsw1vzDDCKgi1TunyWgpz3s9fGPE25gJJnHK"}
```

To preclaim a name, send name preclaim transaction with commitment hash in the payload:
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/name-preclaim-tx -d '{"commitment": "cm$cwe2wGMbiNkXadsw1vzDDCKgi1TunyWgpz3s9fGPE25gJJnHK", "fee": 1, "ttl":1234}'
{"commitment":"cm$cwe2wGMbiNkXadsw1vzDDCKgi1TunyWgpz3s9fGPE25gJJnHK"}
```

Mind that preclaim and claim transactions will not be accepted in the same block,
so please check that at least one block is mined before submitting claim transaction.
To check the height of the blockchain use the following call:
```
curl http://localhost:3013/v2/top
{"hash":"bh$8CBh7DAfnsbgZf8Btd541jm1Smhd6177CBv7UgK8vcAgxfH8m","height":17,"nonce":10943666989495949657,"pow":[1042489,1586082,7185269,17390250,22010949,23823133,26084833,26496880,26982374,27985078,29155969,30765562,34280527,36576404,40341757,42010247,48864118,53081230,53085626,58374655,58640182,60230517,63786551,65401252,78883695,80142167,85509843,87676973,91934825,92005073,94576137,100347674,103149860,106024683,109781247,113905034,121009561,124198978,126781361,129629191,131266393,131659086],"prev_hash":"bh$2fDH24kVtC4UuEheXMeSZhqMUoaDyo495iotrCVYv1ES8wH38K","state_hash":"bs$2jVx7kz9Uvp55etQsoJTmKwy2pMAHC2tn5dUt5W2gq99k7UKWp","target":539923902,"time":1517504077312,"txs_hash":"bx$2RLzQbRE1frHPYnPi8peZgBzeUGccV4NtWhDf6tGnn6p3wMSZv","version":5}
```

### Claim

When a name is preclaimed, you are in a position to claim it.
You must use the name with the same salt as used in commitment hash computation:
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/name-claim-tx -d '{"name": "foobar.aet", "name_salt": 123, "fee": 1, "ttl":1234}'
{"name_hash":"nm$sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC"}
```

After claiming the name (and claim transaction being accepted) you may verify name presence:
```
curl http://localhost:3013/v2/name\?name\=foobar.aet
{"name":"foobar.aet","name_hash":"nm$sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC","name_ttl":50018,"pointers":"[]"}
```

Note that the name is claimed for the max period (50000 blocks) and relative to the current height of chain.
### Update

In order to make better use of claimed name you need to specify where it should point to.
To do so, specify pointers, which translates to different blockchain entities.
In the initial version two pointers are available:
* `account_pubkey`
* `oracle_pubkey`

```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/name-update-tx -d '{"name_hash": "nm$sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC", "name_ttl": 10000, "client_ttl": 50, "pointers": "{\"account_pubkey\":\"ak$3scLu3oJbhsdCJkDjfJ6BUPJ4M9ZZJe57CQ56deSbEXhaTSfG3Wf3i2GYZV6APX7RDDVk4Weewb7oLePte3H3QdBw4rMZw\"}", "fee": 1, "ttl":1234}'
{"name_hash":"nm$sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC"}

curl http://localhost:3013/v2/name\?name\=foobar.aet
{"name":"foobar.aet","name_ttl":10023,"pointers":"{\"account_pubkey\":\"ak$scLu3oJbhsdCJkDjfJ6BUPJ4M9ZZJe57CQ56deSbEXhaTSf\"}"}
```
Note that `name_ttl` is relative to the current height of the chain. Here we shortened the claim.
### Spend to name

Now you may use account and oracle pointers interchangeably with their addresses.
In order to utilize account pubkey pointer, put a name instead of an account key, e.g. in spend transaction put it in `recipient_pubkey` field:
```
curl -X POST -H "Content-Type: application/json" -d '{"recipient_pubkey":"foobar.aet", "amount":2, "fee":1, "ttl":1234}' http://127.0.0.1:3113/v2/spend-tx
{}
```

### Transfer ownership

In order to transfer a name to another user send name transfer transaction:
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/name-transfer-tx -d '{"name_hash": "nm$sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC", "recipient_pubkey": "ak$3scLu3oJbhsdCJkDjfJ6BUPJ4M9ZZJe57CQ56deSbEXhaTSfG3Wf3i2GYZV6APX7RDDVk4Weewb7oLePte3H3QdBw4rMZw", "fee": 1, "ttl":1234}'
{"name_hash":"nm$sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC"}
```

### Revoke

In order to revoke a name send name revoke transaction:
```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/name-revoke-tx -d '{"name_hash": "nm$sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC", "fee": 1, "ttl":1234}'
{"name_hash":"nm$sEWkhrhGMAve7dhfNgXbjUVqSGD1HoZLgBnNAjRjWe5wm8iCC"}
```
