[back](./README.md)
# Mining - intended usage

## Introduction

In order to get a reward and transaction fees, the epoch node needs to mine
a key block. With increased difficulty, the probability of mining a key block
is lower. Therefore, the miners can form mining pools where they share the
processing power over the network so they can mine key blocks more often. They
split the reward according to the amount of work they contribute to mine a
block. The mining pool is formed of a mining pool manager that manages the
pool (and gets a fee for that) and the miners.

The epoch node provides very basic API that allows to retrieve a pending key
block and submit a mined key block.

The way to interact with the epoch node is to use HTTP API.

The following assumes that the node exposes at address 127.0.0.1 the following
ports:
* User API external HTTP endpoint: 3013
* User API internal HTTP endpoint: 3113

## Epoch node modes

### Pool manager

The epoch node can be configured (using `autostart: false`) not to mine key
blocks. Even though the node does not mine the key blocks, it still produces
the key block candidates that do not have `nonce` and `pow` set. These key
block candidates can be retrieved using the
[/key-blocks/pending endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/GetPendingKeyBlock):

```
curl http://127.0.0.1:3013/v2/key-blocks/pending

{"beneficiary":"ak_25MZX3BXYP32YDPGWsJqYZ6CgWnqD93VdpCYaTk6KsThEbeFJX","hash":"kh_2fsLicTxjJfy4T2ky1gD4byNaSKXyFAZhbUMuZHx3T1xgu5nN","height":6402,"miner":"ak_BpwWtzwJpfGe6AmusjQ9a5aqKF784nXkB2apoHPmNmrJTnPdn","prev_hash":"kh_kb3PaxWQmnE2Nz3CU9GKmX1ZKq2yxEc4YcKL1AT9TSTmrB6YM","prev_key_hash":"kh_kb3PaxWQmnE2Nz3CU9GKmX1ZKq2yxEc4YcKL1AT9TSTmrB6YM","state_hash":"bs_h1XLV6ALUWDP2q7B3B8vxzwgVPncsytAyKH5S8SC8EuFeZYBw","target":537156549,"time":1538656736062,"version":23}
```

The pool manager node can accept the key blocks mined elsewhere using the
[/key-blocks endpoint](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostKeyBlock):

```
curl -X POST -H "Content-Type: application/json" http://localhost:3113/v2/key-blocks -d'{"beneficiary":"ak_25MZX3BXYP32YDPGWsJqYZ6CgWnqD93VdpCYaTk6KsThEbeFJX","hash":"kh_2K6enJiddfPvZTPJ9m5WgbFAc4y1Gtm4tx6C4ZbKtkUh3QqAJ6","height":6402,"miner":"ak_BpwWtzwJpfGe6AmusjQ9a5aqKF784nXkB2apoHPmNmrJTnPdn","nonce":2461944701583915239,"pow":[515,592,722,2277,5240,5312,6595,6839,7029,7395,7526,7887,8923,9132,12424,13618,14312,14628,15103,15328,16004,16739,16820,17997,18693,19146,19817,20099,21378,22029,22254,23161,24974,25504,25946,26563,28831,29300,29425,30198,31005,31202],"prev_hash":"kh_kb3PaxWQmnE2Nz3CU9GKmX1ZKq2yxEc4YcKL1AT9TSTmrB6YM","prev_key_hash":"kh_kb3PaxWQmnE2Nz3CU9GKmX1ZKq2yxEc4YcKL1AT9TSTmrB6YM","state_hash":"bs_h1XLV6ALUWDP2q7B3B8vxzwgVPncsytAyKH5S8SC8EuFeZYBw","target":537156549,"time":1538656736062,"version":23}'
```

NOTE: The pool manager does not track the key block candidates created in the
past. It is not implemented.

NOTE: The pool manager's job is to also distribute rewards to the miners
according to how much processing power they provide to the pool. It is not
implemented.

### Miner

Miners are supposed to get a pending key block over the HTTP API. When they
find a solution (`nonce` and `pow`) they send it back to the pool manager
using the HTTP API.

NOTE: The miners join mining pools as they get rewards for finding incomplete
solutions as well. This way the pool manager can also track how much
processing power they provide to the pool and what their share is. It is not
implemented.

## TODO

Implement Stratum protocol for mining pools.

