[back](./README.md)
# Channels - intended usage

## Important

AE State Channels are missing key parts of their integration with Generalized
Accounts.

With introduction of GAs, all on-chain state channel transactions
are to be signed using the on-chain account's authentication method and
off-chain transactions are to be signed using the accounts' authentication
method at channel creation time. You can read more about it
[here](../../channels/authentication.md).

## Introduction
You interact with an Aeternity node both through HTTP requests and WebSocket
connections.
To learn more about channels and their life cycle see [the doc](/channels/README.md).

In each channel there are two WebSocket client parties. For each channel, a new WebSocket connection is opened. Once the channel is opened - participants are
equal in every regard. They have different roles while opening and we have
names for them - `initiator` and `responder`. For short we will call them _the
parties_.

There are two basic types of interaction: persisted connection events and HTTP API calls.

### WebSocket life cycle
These are used for the scenario when all parties behave correctly and as
expected. The flow is the following:

1. [Channel open](#channel-open)
  * [Client reconnect](#client-reconnect)
2. [Channel off-chain update](#channel-off-chain-update)
  * [Transfer](#transfer)
  * [Create a contract](#create-a-contract)
  * [Call a contract](#call-a-contract)
3. [Optionally leave/reestablish](#leave-reestablish)
4. [Channel mutual close](#channel-mutual-close)
  * [Channel solo close](#channel-solo-close)
  * [Channel settle](#channel-settle)

There are a some WebSocket events that can occur while the connection is open
but are not necessarily part of the channel's life cycle.

* [Open error](#open-error)

* [Timeout error](#timeout-error)

* [Update error](#update-error)

* [Update conflict](#update-conflict)

* [Generic messages](#generic-messages)

* [Deposit](#deposit-events)

* [Withdrawal](#withdraw-events)

* [Getting state](#getting-state)

  * [Balances](#get-balances)

  * [Proof of inclusion](#get-proof-of-inclusion)

  * [Dry-run a contract](#dry-run-a-contract)

  * [Contract call](#get-contract-calls)

* [Cleaning local contract calls](#pruning-contract-calls)

* [Connection keep alive](#connection-keep-alive)

Only steps 1 and 4 require chain interactions, step 2 and 3 are off-chain.

### HTTP requests
There are two types of HTTP requests:
* Total amount-modifying ones - [deposit](#deposit-transaction) and [withdrawal](#withdraw-transaction)
* [Channel-closing ones](#solo-closing-sequence) - [solo close](#solo-close-on-chain-transaction), [slash](#slash-on-chain-transaction) and [settle](#settle-on-chain-transaction)

## Channel open
In order to use a channel, it must be opened. Both parties negotiate parameters for the channel - for example the amounts to participate. Some of those are relevant to the chain and end up in a`channel_create_tx` that is posted on the chain. Once a certain amount of blocks have been mined on top of the one that included it, the channel is considered to be opened.

### Websocket protocol

The channel websocket api currently supports one protocol: [`json-rpc`](https://www.jsonrpc.org/specification). `legacy` protocol was removed. Choosen protocol has to be specified with the `protocol` option.

In the examples below, the `json-rpc` protocol is used.

Detailed message transcripts from test suites can also be found [here](./examples/channels/json-rpc/).

### Channel parameters
Each channel has a set of parameters that is required for opening a
connection. Most of those are part of the `channel_create_tx` which is included
in the chain, and the others are metadata used for the connection itself. We
will describe them in two separate groups: one for the channel establishing
and another for optional timeouts.

  | Name | Type | Description | Required for open | Required/Used in reestablish | Part of the `channel_create_tx` |
  | ---- | ---- | ----------- | ----------------- | ---------------------------- | ------------------------------- |
  | initiator_id | string | initiator's public key | Yes | No | Yes |
  | responder_id | string | responder's public key | Yes | No | Yes |
  | lock_period | integer | amount of blocks for disputing a solo close | Yes | No | Yes |
  | push_amount | integer | initial deposit in favour of the responder by the initiator | Yes | No | No |
  | initiator_amount | integer | amount of tokens the initiator has committed to the channel | Yes | No | Yes |
  | responder_amount | integer | amount of tokens the responder has committed to the channel | Yes | No | Yes |
  | channel_reserve | integer | the minimum amount both peers need to maintain | Yes | No | Yes |
  | ttl | integer | maximum height of a block to include the `channel_create_tx` | No | No | Yes |
  | host | string | host of the `responder`'s node| Yes if `role=initiator` | No | No | No |
  | port | integer | the port of the `responder`s node| Yes if `role=initiator` | No | No | No |
  | role | string | the role of the client - either `initiator` or `responder` | Yes | Yes | No |
  | minimum_depth | integer | the minimum amount of blocks to be mined | No | No | No |

  `responder`'s port and host pair must be reachable from `initiator` network
  so unless participants are part of a LAN, they should be exposed to the
  internet as described [here](../../node/api/README.md). It is possible to use the
  same port number for different responder pubkeys and multiple simultaneous
  responders. If the `responder` sets `initiator_id` to `"any"`, the responder will
  accept a connection request from any initiator, and fetch the proper `initiator_id`
  from the `channel_open` message.
  
  Once established, the channel follows a [predefined set of state
  transitions](/channels/README.md#overview). The implementation protects the
  client from edge cases when transitions take too long or never happen using
  a set of different timers - if the event doesn't occur in the specified time
  frame then the off-chain protocol is considered to be violated and the
  WebSocket connection is killed. Those are optionally configurable alongside
  with the channel establish settings. Keep in mind that those are only local
  values for the specific participant, protecting one's own interest. The two
  participants can have different timeout settings and still doing updates, as
  long as no timer fires.

  All timeout values are integers and represent the waiting time in
  milliseconds.

  | Name | Description | Default value |
  | ---- | ----------- | ------------- |
  | timeout_idle | the time waiting for a new event to be initiated | 600000 |
  | timeout_funding_create | the time waiting for the `initiator` to produce the create channel transaction after the `noise` session had been established | 120000 |
  | timeout_funding_sign | the time frame the other client has to authenticate an off-chain update after our client had initiated and authenticated it. This applies only for mutual authentication of on-chain intended updates: channel create transaction, deposit, withdrawal and etc. | 120000 |
  | timeout_funding_lock | the time frame the other client has to confirm an on-chain transaction reaching maturity (passing minimum depth) after the local node has detected this. This applies only for mutually authenticated on-chain intended updates: channel create transaction, deposit, withdrawal and etc. | 360000 |
  | timeout_sign | the time frame the client has to return an authenticated off-chain update or to decline it. This applies for all off-chain updates | 500000 |
  | timeout_accept | the time frame the other client has to react to an event. This applies for all off-chain updates that are not meant to land on-chain, as well as some special cases: opening a `noise` connection, mutual closing acknowledgement and reestablishing an existing channel | 120000 |
  | timeout_initialized | the time frame the responder has to accept an incoming noise session. Applicable only for initiator | timeout_accept's value |
  | timeout_awaiting_open | the time frame the initiator has to start an outgoing noise session to the responder's node. Applicable only for responder | timeout_idle's value |

  In the following examples we will be using the following parameters:

  | Name | Value |
  | ---- | ----- |
  | initiator_id | ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm |
  | responder_id | ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC |
  | lock_period | 10 |
  | push_amount | 1 |
  | initiator_amount | 70000000000000 |
  | responder_amount | 40000000000000 |
  | channel_reserve | 2 |
  | ttl | 1000 |

  The `initiator` will be connecting to the `responder` on localhost:12340
  We will be using the tool [wscat](https://github.com/websockets/wscat)
  We assume the channel's WebSocket listener is set on port 3014 (default one)

### Responder WebSocket open
Using the set of prenegotiated parameters the responder connects
```
$ wscat --connect 'localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder'

connected (press CTRL+C to quit)
```

Note the `role=responder` as it is specific. Note also that the `host` is missing - it is not required for the responder.
The `port` being specified is the one the `responder`'s node will start
listening for the `initiator`'s connection. If the `responder`'s node is
behind a firewall or some port forwarding is done - this should be done before
the initiator starts connecting as it will fail.

At this point the `responder` is listening on address `0.0.0.0` for the `initiator`'s
connection on the specified port - `12340`.

### Initiator WebSocket open
Using the set of prenegotiated parameters the initiator connects
```
$ wscat --connect 'localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator'

connected (press CTRL+C to quit)
```

Note the `role=initiator` as it is specific. Note also the `host` and `port`
values being provided by the `responder`.

### Connection opened messages
Parties' WebSocket clients receive messages for the opening of the TCP
connection.

#### Initiator connection opened message
The initiator receives the following message

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### Responder connection opened message
The responder receives the following message
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

### Create transaction authentication
The `channel_create_tx` is sent subsequently to both parties and they mutually
authenticate it. Then it is posted to the chain.

#### Initiator authenticates the tx
The initiator receives a message containing the unauthenticated transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IEyAaEB...",
      "updates": []
    }
  },
  "version": 1
}
```

Initiator is to decode the transaction, inspect its contents, authenticate it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCu..."
  }
}
```

#### Responder is informed
The responder receives the following message
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### Responder authenticates the tx
After being informed for the initiator's authentication, the responder receives a message containing the solo-authenticated transaction to be co-authenticated by her as well
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCu...",
      "updates": []
    }
  },
  "version": 1
}
```

Note that this is the same transaction that the initiator already
authenticated and same updates list. Responder is to decode the transaction,
inspect its contents, to co-authenticate it, encode it and then to post
it back via a WebSocket message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCP4...",
  }
}
```

#### Initiator is informed
The initiator receives the following message
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "funding_signed"
    }
  },
  "version": 1
}
```

#### Authenticated channel_create_tx
The responder FSM reports to its client that it received the authentication
reply, and now has a co-authenticated `channel_create_tx`. It relies on the
initiator to push the co-authenticed transaction to the mempool:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+MsLAfhCP4...",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

The initiator FSM reports to its client that it received the co-authenticated
`channel_create_tx` from the responder:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+MsLAfhCP4...",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### Transaction in mempool
At this point both parties had received the mutually authenticated the `channel_create_tx` transaction. The transaction is posted by the state
channel's software to the node and goes to the mempool. Having calculated its hash, one can validate it using the external HTTP API:
```
$ curl 'http://localhost:3013/v2/transactions/th_hNyHzj4dSzyBqReAMR36GGz1mhuXxQFuES3AnPkXkuY2w6dZb'
```
if the `block_hash` is `none` - then the transaction is still in the mempool.

#### Transaction detected on-chain
Once the transaction is picked up by a miner and included in a block, the fsms will detect it and report
a `channel_changed` event in an `on_chain_tx` report:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKOlyL6Y5R1OgoyQ8+8QdDya72IT479ncEFi7BnPO3zMyE4N/E54E2heF3g8aCYirv/ajwxB5DIDn2cdEF6h6ALhA2ILrieAe4Y8a+0lfSwmN+ddIv6gPX0xfMyX4RpQ7BRZoINayCRQNOxGci9v2J7to+CSYNJQEYzBXcSTclpoXCbiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGG0jrV+AAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwMXN1eS",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

### Mininum-depth confirmation
A block height timer is started and it ends after `minimum_depth + 1` confirmations. Default value for
it is 4, so 5 blocks need to be mined. As a result, each party will receive
two kinds of confirmation.

An update from one's own node that the block height needed is reached:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

An update from one's own node that the other party had confirmed that the block
height needed is reached:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

### Initial state
After both parties have confirmed that the funding is authenticated - they can proceed
with sending the messages for off-chain updates. The inital state is the one
described in the create transaction.

#### Open confirmation
After both parties have mutually authenticated the state update both of them will receive a info for the channel open:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

From this point on, the channel is considered to be opened.

#### State changed
Each time the fsm returns to the `open` state, it will check whether the channel off-chain state has
changed. If so, it issues a `channels.update` report. When the channel is first opened, this report will
present the initial off-chain state:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QENCwH4hLhAKOlyL6Y5R1OgoyQ8+8QdDya72IT479ncEFi7BnPO3zMyE4N/E54E2heF3g8aCYirv/ajwxB5DIDn2cdEF6h6ALhA2ILrieAe4Y8a+0lfSwmN+ddIv6gPX0xfMyX4RpQ7BRZoINayCRQNOxGci9v2J7to+CSYNJQEYzBXcSTclpoXCbiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGG0jrV+AAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwMXN1eS"
    }
  },
  "version": 1
}
```

### Client reconnect
Once the `channel_create_tx` has been signed, the client Websocket connection may close
without causing the FSM to terminate. The client may reconnect by signing a special
`channel_client_reconnect_tx` transaction, partly to identify the right FSM instance
to connect to, and partly to prove identity. The transaction has the following structure:

 | Name | Type | Description |
 | ---- | ---- | ----------- |
 | channel id | string | ID of the channel |
 | role | string | Role of the instance (initiator or responder) |
 | pub key | string | Public key of the client |

Information about serialization can be found [here](../../serializations.md#channel-client-reconnect-transaction).

After signing the reconnect transaction, the client connects using the parameters `protocol`
and `reconnect_tx` as illustrated below. Note that the `reconnect_tx` parameter uses a
serialized transaction.

```
$ wscat --connect 'localhost:3014/channel?protocol=json-rpc&reconnect_tx=tx_%2BJwLAfhCuEBcOkx9CFjb8i7AsTT5%2BIkuSxG5SKKrSLweRz%2BeIThEXNIq42AQjKyBQGDkT6QEyxbQH5XSSaaojvt%2B2BYJu2wNuFT4UoICPwGhBrBnp1GFwypFOxF3uxx9KK6ZNyKMgeZJFKRgUhZ4U1WfiWluaXRpYXRvcqEBQrhkAQ8qujZTeNSsuZiVkaLuejuljb%2BPfdvSsAm2SNIJAuU9'

connected (press CTRL+C to quit)
```

While the client is disconnected, the corresponding FSM will reject any protocol request that
requires signing. An attempt to reconnect to an FSM that already has a client connected will
be rejected.

## Channel off-chain update
After the channel has been opened and before it has been closed there is a
channel state that is updated when needed. The updates are off-chain and
broadcasted only between parties in the channel. The state is a full state
tree that holds all the latest accounts, contracts and contract calls.
A state is considered to be valid only if both parties have agreed upon it.
Agreement it proven with authenticating a message that contains the channel id, round
and root of the state tree (state_hash). States are ordered by their round - the greater the round,
the newer the state. The latest channel state is the last valid state, having
the greatest round. At any time the latest state can be used for unilaterally closing the channel.

### Channel state
There are a couple of different types that could define the channel state.
Those are deposit, withdrawal and off-chain transactions. They all containt at
least the following data:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel|
  | state_hash | string | root of the state tree |
  | round | integer | current round |

You can find further information for them as it follows:

* [deposit transaction](../../serializations.md#channel-deposit-transaction)
* [withdrawal transaction](../../serializations.md#channel-withdraw-transaction)
* [off-chain transaction](../../serializations.md#channel-off-chain-transaction)

Each subsequent state has a `round` increased with 1

Since both participants are peers, they can both trigger new updates to the
state.
Since one of them starts the update and the other acknowledges is below we are
going to use `starter` and `acknowledger`. Both the initiator and the
responder can take either of the roles.

### Transfer
The transfer update is moving tokens from one channel account to another. The update is a change to be applied on top of the latest state. It has the
following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | from | string | sender's public key |
  | to | string | receiver's public key |
  | amount | integer | the amount given |

Sender and receiver are the channel parties. Both the initiator and responder
can take those roles. Any public key outside of the channel is considered invalid.

#### Start transfer update

##### Check balances
To check the outcome of the following sequence, we can first check the balances of the channel:
```javascript
{
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  }
}
```

The fsm responds:

```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

##### Trigger a transfer update
The starter sends a message containing the desired change
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  }
}
```

The `starter` might take the role of `from` or `to` so the `starter` can
trigger sending or request for tokens.

##### Starter authenticates updated state
The starter receives a message containing the updated channel state as an
off-chain transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+EY5AqEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02ICoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhVgB6xw==",
      "signed_tx": "tx_+JU5AaEGrAT...",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainTransfer",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
        }
      ]
    }
  },
  "version": 1
}
```
The starter is to decode the transaction, inspect its contents, authenticates it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+N8LAfhCu...",
  }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```
Then the acknowledger receives a new message containing the updated channel state as an
off-chain transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "signed_tx": "tx_+N8LAfhCu...",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainTransfer",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
        }
      ]
    }
  },
  "version": 1
}
```

Note that this is the same solo-authenticated transaction. The acknowledger is
to decode the transaction, inspect its contents, authenticate it, encode it and
then post it back via a WebSocket message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+N8LAfhC..."
  }
}
```

#### Finish update
After both the parties have authenticated the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
mutually authenticated off-chain update so the participants can persist it locally.
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+N8LAfhC..."
    }
  },
  "version": 1
}
```

##### Check the result of the update

Since we checked balances before the update, we can do so again to verify the result:

```javascript
{
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  }
}
```

The fsm responds:

```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999998
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

After that a new state updated can be triggered.

### Create a contract
The create contract update is creating a contract inside the channel's internal state tree. The update is a change to be applied on top of the latest state. It has the
following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | vm_version | integer | version of the AEVM |
  | abi_version | integer | version of the ABI |
  | deposit | integer | initial amount the owner of the contract commits to it |
  | code | string | api encoded compiled AEVM byte code |
  | call_data | string | api encoded compiled AEVM call data for the code |

That would create a contract with the poster being the `owner` of it. Poster
commits initially a `deposit` amount of tokens to the new contract.

#### Start create contract update
##### Trigger a create contract update
The owner sends a message containing the desired change
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAA...",
    "code": "cb_+QP1RgKg/ukoF...",
    "deposit": 10,
    "vm_version": 3
  }
}
```
##### Owner authenticates updated state
The owner receives a message containing the updated channel state as an
off-chain transaction

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+QTXOQGhB...",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAA...",
          "code": "cb_+QP1RgKg/ukoF...",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "vm_version": 3
        }
      ]
    }
  },
  "version": 1
}
```

The owner is to decode the transaction, inspect its contents, authenticate it, encode
it and then post it back via a WebSocket message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QUjCw..."
  }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```
Then the acknowledger receives a new message containing the updated channel state as an
off-chain transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+QUjCw..."
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAA...",
          "code": "cb_+QP1RgKg/ukoF...",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "vm_version": 3
        }
      ]
    }
  },
  "version": 1
}
```
Note that this is the same solo-authenticated transaction. The acknowledger
is to decode the transaction, inspect its contents, authenticate it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QUjCwH4QrhA..."
  }
}
```
#### Finish update
After both the parties have authenticated the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
mutually authenticated off-chain update so the participants can persist it locally.
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "state": "tx_+QUjCwH4QrhA..."
    }
  },
  "version": 1
}
```
After that a new state updated can be triggered.

#### Contract address computation
The created contract is part of the state tree. It has its own balance and its
place in the contracts subtree of the channel's state tree. In order to
inspect its balance or call the contract one needs its address.

Computation of this address is done exactly as it is in on-chain contracts -
it is a hashed version of the channel's owner pubkey and the nonce. Only
difference is that nonce is not computated in channels and the update round is
used instead.

### Call a contract
The call contract update is calling a preexisting contract inside the channel's internal state tree. The update is a change to be applied on top of the latest state. It has the
following structure.

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | contract_id | string | address of the contract to call |
  | abi_version | integer | version of the ABI |
  | amount | integer | amount the caller of the contract commits to it |
  | call_data | string | ABI encoded compiled AEVM call data for the code |

That would call a contract with the poster being the `caller_id` of it. Poster
commits an `amount` amount of tokens to the contract.

The call would also create a `call` object inside the channel state tree. It contains the result of the contract call.

#### Start call a contract update
##### Trigger a contract call update
The caller sends a message containing the desired change
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAA...",
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  }
}
```

##### Caller authenticates updated state
The caller receives a message containing the updated channel state as an
off-chain transaction

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+QEeOQGhBoKHx...",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAA...",
          "call_stack": [],
          "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
        }
      ]
    }
  },
  "version": 1
}
```

The caller is to decode the transaction, inspect its contents, authenticate it, encode
it and then post it back via a WebSocket message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QFqCwH4..."
  }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```
Then the acknowledger receives a new message containing the updated channel state as an
off-chain transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+QFqCwH4..."
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAA...",
          "call_stack": [],
          "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
        }
      ]
    }
  },
  "version": 1
}
```
Note that this is the same solo-authenticated transaction. The acknowledger is
to decode the transaction, inspect its contents, authenticate it, encode it and
then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QFqCwH4Q..."
  }
}
```
#### Finish update
After both the parties have authenticated the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
mutually authenticated off-chain update so the participants can persist it locally.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "state": "tx_+QFqCwH4Q..."
    }
  },
  "version": 1
}
```

#### Getting a call result
All calls are stored in the channel state tree. In order to extract one out of
there and inspect it, one shall send a WebSocket event
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": 8
  }
}
```
The `contract_id` is the address of the contract that had been called, the `round` is the round of the update and
`caller_id` is the address of the caller.

Then the call is returned through an incoming message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "caller_nonce": 8,
      "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
      "gas_price": 1,
      "gas_used": 192,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
    }
  },
  "version": 1
}
```

It is worth mentioning that since this is an off-chain transaction the gas price specified is not consumed.
That amount of gas represents the amount of computations. It could be used for
aproximation for the gas needed for executing a contract on-chain if a similar amount of
computations are required. Computation heavy contracts might be just too
expensive to be force progressed on-chain, so please use with caution.

## <a name="leave-reestablish"></a>Optionally leave/reestablish
It is possible to leave a channel and then later reestablish the channel
off-chain state and continue operation. Leaving the channel can either be
done by simply disconnecting, or by sending a `'leave'` request. When receving
a leave request, the channel fsm passes it on to the peer fsm, reports the
current mutually authenticated state and then terminates. The `'reestablish'` request
is very similar to a [Channel open](#channel-open) request, but also requires
the channel id and the latest mutually authenticated state.

The full state, including state trees, is cached internally by the Aeternity
node, and upon reestablish, it is verified that the encoded state provided
by the client corresponds to the latest full state retrieved from the cache.

### Leave request
Example:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

The fsm responds with the following type of report:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLh..."
    }
  },
  "version": 1
}
```

### Reestablish
Open the channel in the same way as in the
[Initiator WebSocket open](#initiator-websocket-open) example,
adding the parameters `existing_channel_id` and `offchain_tx` with values
matching the ones provided in the `leave` report above. Some parameters (related to open transaction) are not required and ignored. See [Channel parameters](#channel-parameters):

```
$ wscat --connect
localhost:3014/channel?existing_channel_id=ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR&host=localhost&offchain_tx=tx_%2BQENCwH4h...&port=12341&protocol=json-rpc&role=initiator
```

The channel fsm responds with the following event reports if all goes well:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_reestablished"
    }
  },
  "version": 1
}
```

then the standard report indicating that the channel is open:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

followed by an update report with the latest mutually authenticated state:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4..."
    }
  },
  "version": 1
}
```

## Channel mutual close
At any moment after the channel is opened, a closing procedure can be
triggered. This can be done by either of the parties. The process is similar to
the [off-chain updates](#channel-off-chain-update). The most notable change is the
special transaction mutually authenticated. It is called
`channel_close_mutual_tx`. After gathering singatures it will end up on the
chain and has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel|
  | from | string | initiator's public key |
  | initiator_amount_final | integer | final amount of tokens to be awarded by the initiator |
  | responder_amount_final | integer | final amount of tokens to be awarded by the responder |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | nonce | integer | initiator's nonce |

Since any of the participants can initiate a closing, we will use `starter`
for the peer that triggers the process and `acknowledger` for the other one.

### Initiate mutual close
The starter sends the following message and triggers the closing procedure:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

### Starter authenticating
Then the starter receives a `channel_close_mutual_tx` to authenticate:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "signed_tx": "tx_+F01AaEGXfP...",
      "updates": []
    }
  },
  "version": 1
}
```
Starter is to decode the transaction, inspect its contents, authenticate it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhC..."
  }
}
```
### Acknowledger authenticating
Then the acknowledger receives a `channel_close_mutual_tx` to authenticate:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "signed_tx": "tx_+KcLAfhC..."
      "updates": []
    }
  },
  "version": 1
}
```
Note that this is the same solo-authenticed transaction. The acknowledger is
to decode the transaction, inspect its contents, authenticate it, encode it and
then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+KcLAfhCuE..."
  }
}
```

#### Authenticated channel_close_mutual_tx

Both participants receive the mutually authenticated `channel_close_mutual_tx`:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "info": "close_mutual",
      "signed_tx": "tx_+KcLAfhCuE...",
      "type": "channel_close_mutual_tx"
    }
  },
  "version": 1
}
```

Using its hash, participants can track its progress on the chain: entering the mempool, block inclusion and a number of confirmations.

### Channel closing
After both parties have received the mutually authenticated `channel_close_mutual_tx`
transaction, it is posted on the chain and the microservice handling the
off-chain requests dies. Parties receive the following infos:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "event": "close_mutual"
    }
  },
  "version": 1
}
```

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

Then the WebSocket connection is closed.

### Tracking the progress of the onchain transaction
After calculating the hash of the mutually authenticated `channel_close_mutual_tx` parties can track
its progress as they would do with any on-chain transaction
```
curl 'http://127.0.0.1:3013/v2/transactions/th_2qkN973cNJiejXVJoXkXbttf1iKetWJCSY1W5VUBh3pnRS1kCC'
```
if the `block_hash` is `none` - then the transaction is still in the mempool.

## Channel solo close
It is possible to close the channel unilaterally, e.g. if the other party has
disconnected and is expected never to return. The channel fsm can be asked
to generate a `channel_close_solo` transaction and post it on-chain. The
resulting transaction will include the latest mutually signed offchain state,
or the empty string, indicating that the latest state is what's on the chain.

The `channel_close_solo` transaction only needs a single authentication, and
is described in more detail in [this section](#channel-solo-close).

The channel fsm does not support picking an earlier state to close with, as
this is a form of cheating.

Since any of the participants can initiate a solo-closing, we will use
`requester` for the peer that triggers the process. The other peer is not
necessarily involved at all, but will be informed if it is actually connected.
For this description, we simply call it `other`.

### Initiate solo close
The requester sends the following message and triggers the closing procedure:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

### Requester authentication
Then the requester receives a `channel_close_solo_tx` to authenticate:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+QGfNgGhBnHSbcHwBwtR5QRwS0O1mI1Gw/8pkaOwcHQap09BPoMFoQGxtXe80yfL
OeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoC5AUz5AUk8AfkBP/kBPKAeoRWJfw9r7+McQQHdwLN6tS/a
qbQUwm8iJYXMIOcncfkBGPh0oB6hFYl/D2vv4xxBAd3As3q1L9qptBTCbyIlhcwg5ydx+FGAgICAgICg7QIWPGJsh916G7zCAZpUeaRQuGVamwjR8JaxQKEPIwmAgICAoEJmfgNwrMeYsFATTDpQ+Y9abOcHR6KUvw5o9LdShJsUgICAgID4T6BCZn4DcKzHmLBQE0w6UPmPWmznB0eilL8OaPS3UoSbFO2gMbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aLygoBAIY/qiUiX//4T6DtAhY8YmyH3XobvMIBmlR5pFC4ZVqbCNHwlrFAoQ8jCe2gNxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAHAwMDAwACGG0jrV+AACPykTFA=",
      "updates": []
    }
  },
  "version": 1
}
```

Requester is to decode the transaction, inspect its contents, authenticate it, encode it
and then post it back via a WebSocket message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "tx": "tx_+QHrCwH4QrhACuHMgbcTg1inUPAUSmhXfODKWI2CFchqpav9VDaBlw+xng9Ld0eLPgysTvks47iVHn4d/11VlkEi6iLRBDkIBLkBovkBnzYBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aAuQFM+QFJPAH5AT/5ATygHqEViX8Pa+/jHEEB3cCzerUv2qm0FMJvIiWFzCDnJ3H5ARj4dKAeoRWJfw9r7+McQQHdwLN6tS/aqbQUwm8iJYXMIOcncfhRgICAgICAoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJgICAgKBCZn4DcKzHmLBQE0w6UPmPWmznB0eilL8OaPS3UoSbFICAgICA+E+gQmZ+A3Csx5iwUBNMOlD5j1ps5wdHopS/Dmj0t1KEmxTtoDG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmi8oKAQCGP6olIl//+E+g7QIWPGJsh916G7zCAZpUeaRQuGVamwjR8JaxQKEPIwntoDccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6Ei8oKAQCGJGE5yoABwMDAwMAAhhtI61fgAAiybuMt"
  }
}
```

As the channel fsm receives the authenticated solo close transaction, verifies it
and posts it to the chain, it should eventually detect the transaction appearing
on the chain, and inform its client with the following WebSocket message.
The other peer will receive the same message if it is online:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhACuHMgbcTg1inUPAUSmhXfODKWI2CFchqpav9VDaBlw+xng9Ld0eLPgysTvks47iVHn4d/11VlkEi6iLRBDkIBLkBovkBnzYBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aAuQFM+QFJPAH5AT/5ATygHqEViX8Pa+/jHEEB3cCzerUv2qm0FMJvIiWFzCDnJ3H5ARj4dKAeoRWJfw9r7+McQQHdwLN6tS/aqbQUwm8iJYXMIOcncfhRgICAgICAoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJgICAgKBCZn4DcKzHmLBQE0w6UPmPWmznB0eilL8OaPS3UoSbFICAgICA+E+gQmZ+A3Csx5iwUBNMOlD5j1ps5wdHopS/Dmj0t1KEmxTtoDG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmi8oKAQCGP6olIl//+E+g7QIWPGJsh916G7zCAZpUeaRQuGVamwjR8JaxQKEPIwntoDccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6Ei8oKAQCGJGE5yoABwMDAwMAAhhtI61fgAAiybuMt",
      "type": "channel_close_solo_tx"
    }
  },
  "version": 1
}
```

As the channel object status also changes to `closing`, the peer(s) will
receive another information message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

## Channel settle
Once a 'dispute' process has been initiated with a `channel_close_tx`, and
once the lock period has expired, it is possible to finally close the channel
with a `channel_settle_tx` transaction. The channel fsm can assist if asked
with the following WebSocket request:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### Requester authenticating
Then the requester receives a `channel_settle_tx` to authenticate:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+F04AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6Ehj+qJSJf/4YkYTnKgAEAhhtI61fgAAIwYkCX",
      "updates": []
    }
  },
  "version": 1
}
```

The requester is to decode the transaction, inspect its contents, authenticate it,
encode it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "tx": "tx_+KcLAfhCuEBdI4Uesh3hYjGQ2BAo0FzD1YPyZlzhy8HyNgf7OzrQdVM44oWQX0yFtmk31HaSLuIJGNDv3hEgdLwe0iZz3LEEuF/4XTgBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGP6olIl//hiRhOcqAAQCGG0jrV+AAAgurGvs="
  }
}
```
As the channel fsm receives the authenticated settle transaction, verifies it
and posts it to the chain, it should eventually detect the transaction appearing
on the chain, and inform its client with the following WebSocket message.
The other peer will receive the same message if it is online:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBdI4Uesh3hYjGQ2BAo0FzD1YPyZlzhy8HyNgf7OzrQdVM44oWQX0yFtmk31HaSLuIJGNDv3hEgdLwe0iZz3LEEuF/4XTgBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGP6olIl//hiRhOcqAAQCGG0jrV+AAAgurGvs=",
      "type": "channel_settle_tx"
    }
  },
  "version": 1
}
```

Once the fsm has confirmed the transaction to be safely on-chain, the following
information message is sent to the connected peers, signaling that the channel
is finally closed, and the channel object removed:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "closed_confirmed"
    }
  },
  "version": 1
}
```

### Other WebSocket events
#### Open error

At channel's WebSocket connection is opened according to initial parameters.
If correct, everything proceeds as planned. If there are some issues with
them, the user receives an error describing the issue and the WebSocket
connection is closed.

##### Missing participant

If a user tries opening a WebSocket and either of the participants is not
present on-chain, the message received is:

```javascript
{
   "channel_id":null,
   "error":{
      "code":3,
      "data":[
         {
            "code":1011,
            "message":"Participant not found"
         }
      ],
      "message":"Rejected",
      "request":{
      }
   },
   "id":null,
   "jsonrpc":"2.0",
   "version":1
}
```

Note that since it is the `initiator` that pays the `channel_create`
transaction fee, it is a must that the `initiator` is present on-chain.
Although this is not the case with the `responder`, having too litle coins in
their on-chain balance is a risk both parties must clearly understand: this
could make it impossible for them to make a dispute. A missing `responder` is
still rejected in the WebSocket connection to protect them from doing this
error involuntary.

##### Integer value is too low

If a user tries opening a WebSocket and any of the integer values is too low
the message received is:

```javascript
{
   "channel_id":null,
   "error":{
      "code":3,
      "data":[
         {
            "code":105,
            "message":"Value too low"
         }
      ],
      "message":"Rejected",
      "request":{
      }
   },
   "id":null,
   "jsonrpc":"2.0",
   "version":1
}
```

Examples for this would be either opening amount being below the threshold
defined by `channel_reserve`, or any of `channel_reserve`, `push_amount` or
`lock_period` being a negative number.

#### Timeout error

In order to prevent zombie states of the state channel which run indefinitely
the protocol defines a set of timeouts for each participant a set of timeouts
defined by each specific participant [at WebSocket connection opening
time](#channel-parameters). A triggered timeout is a violation of the
off-chain protocol and the non-responsive participant is considered to be
missing. In this case the connection is interrupted and the client is expected
either to try reaching for the other party and reconnecting or going through
the solo closing sequence.

The client receives the following message indicating the timeout:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_...",
    "data": {
      "event": "timeout"
    }
  },
  "version": 1
}
```

Subsequently the client receives the following message indicating the closing of
the WebSocket connection:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_...",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```



#### Update error

Updates are not always successful, for example one participant tries to spend
more tokens that one currently has in the channel's balance. This diverges
from the update flow [described above](#channel-off-chain-update).

Example message for when the `from` does not have enough tokens to spend
```javascript
{
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000000000000000,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

The structure is having a `reason` and `request` holding the request being
sent. Possible error reasons are:

* `Insufficient balance` - when `from` does not have enough tokens in the
  channel. Keep in mind that there is a minimal amount of `channel_reserve`
  tokens to be kept by both parties.

* `Negative amount` - the `udpate` event contained a negative amount

* `Invalid pubkeys` - at least one of the addresses in the `update` event is
  not present in the channel.

#### Update conflict

Since updates can be triggered by either party, it is possible both
participants to start an `update` almost simultaneously. If a new `update` is
started by a participant while the other participant has started an `update` of
ones' own - a conflict occurs. Then both `update`-s are invalidated and the
state is reverted to the last mutually authenticated one. Both participant receive a
message containing a reference to the correct state.
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
      "round": 5
    }
  },
  "version": 1
}
```

#### Generic messages

There is the functionality to send participants messages containing
information. In the scope of this - we are going to be calling those a `sender`
and a `receiver`. These roles can be taken by any of the participants, anytime.

The `sender` pushes a message with the following structure:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "hejsan",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  }
}
```

Then the `receiver` gets an event containing the info being sent and some
details:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "message": {
        "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "info": "hejsan",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    }
  },
  "version": 1
}
```

#### Total balance update events

After the channel has been opened it has a total balance of tokens committed to
it. This balance is persisted as part of the on-chain channel state. Upon
closing a channel on-chain, the closing balances of the participants are
checked against this balance. Under no circumstances can the sum of the closing balances
be greater than the total balance on-chain.

Participants are able to modify the total balance: the following two functionalities are available:

* deposit - when a participant wants to commit more tokens from his on-chain
  balance to the channel total balance
* withdrawal - when a participant wants to transfer tokens out of the channel
  on-chain balance to one's personal account

### Deposit events

After the channel had been opened any of the participants can initiate a
deposit. The process closely resembles the [update](#update). The most notable
difference is the transaction has been mutually authenticated: it is `channel_deposit_tx` and
after the procedure is finished, it is posted on-chain.

Since both the initiator and responder can deposit tokens, in the scope of this description we
will call the participant that commits tokens to the channel a depositor and
the other party - acknowledger. Note that any public key outside of the channel participants
is considered invalid for the depositor role.

#### Deposit transaction
The `channel_deposit_tx` is a change to be applied on top of the latest channel state. It also is
posted on-chain and is included in a block. It has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel|
  | from | string | depositor's public key |
  | amount | integer | the amount committed to the channel |
  | ttl | integer | minimum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | state_hash | string | the root of the internal channel state hash after the deposit |
  | round | integer | the next channel round |
  | nonce | integer | depositor's nonce |

#### Start deposit

Any of the participants can initiate a deposit. Only requirements are:
* Channel is already opened
* No off-chain update/deposit/withdrawal is currently being performed
* Channel is not being closed or in a solo closing state
* The deposit must be equal to or greater than zero, and cannot exceed the
  available balance on the depositor's account

##### Trigger a deposit

The depositor sends a WebSocket message containing the desired change
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

##### Depositor authenticates updated state
The depositor receives a message containing the updated channel state as a
`channel_deposit_tx` transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+HIzAaE...",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainDeposit"
        }
      ]
    }
  },
  "version": 1
}
```
The depositor is to decode the transaction, inspect its contents,
solo-authenticate it, encode it and then post it back via a WebSocket
message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAf..."
  }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```
Then the acknowledger receives a new message containing the deposit
solo-authenticated transaction for confirmation:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+LwLAf..."
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainDeposit"
        }
      ]
    }
  },
  "version": 1
}
```
Note that this is the same transaction as the one that the depositor had
already authenticated. The acknowledger is to decode the transaction, inspect
its contents, authenticate it, encode it and then post it back via a WebSocket
message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+LwLAfhCu..."
  }
}
```

#### Finish deposit
After both parties had authenticated the deposit transaction, the transaction is posted on-chain and
both parties receive it:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+LwLAfhCu...",
      "type": "channel_deposit_tx"
    }
  },
  "version": 1
}
```
They are both to compute the transaction hash. Using it,
participants can track its progress on the chain: entering the mempool, block
inclusion and a number of confirmations.

After the `minimum_depth` block confirmations each participant is informed
for the deposit progress on-chain by one's own node:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "own_deposit_locked"
    }
  },
  "version": 1
}
```
An update from one's own node that the other party had confirmed that the block
height needed is reached:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "deposit_locked"
    }
  },
  "version": 1
}
```
With this the deposit sequence is complete and the channel can continue with
other updates. Note that the deposit transaction's `round` and `state_hash`
are the ones considered latest from the channel's perspective. For example the
next correct off-chain update/deposit/withdrawal shall have a deposit
transaction's `round` plus one.

### Withdraw events

After the channel had been opened any of the participants can initiate a
withdrawal. The process closely resembles the [update](#update). The most notable
difference is that the transaction has been mutually authenticated: it is `channel_withdraw_tx` and
after the procedure is finished - it is being posted on-chain.

Since both the initiator and responder can withdraw tokens, in the scope of this description we
will call the participant that commits tokens to the channel a withdrawer and
the other party - an acknowledger. Note that any public key outside of the channel participants
is considered invalid for the withdrawer role.

#### Withdraw transaction
The `channel_withdraw_tx` is a change to be applied on top of the latest channel state. It also is
posted on-chain and is included in a block. It has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel|
  | to | string | withdrawer's public key |
  | amount | integer | the amount taken out from the channel |
  | ttl | integer | minimum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | state_hash | string | the root of the internal channel state hash after the withdraw |
  | round | integer | the next channel round |
  | nonce | integer | withdrawer's nonce |

#### Start withdraw

Any of the participants can initiate a withdrawal. The only requirements are:
* Channel is already opened
* No off-chain update/deposit/withdrawal is currently being performed
* Channel is not being closed or in a solo closing state
* The withdrawal amount must be equal to or greater than zero, and cannot
  exceed the available balance on the channel (minus the `channel_reserve`)

##### Trigger a withdrawal

The withdrawer sends a WebSocket message containing the desired change
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

##### Withdrawer authenticates updated state
The withdrawer receives a message containing the updated channel state as a
`channel_withdraw_tx` transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+HI0AaE...",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```
The withdrawer is to decode the transaction, inspect its contents,
authenticate it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAf..."
  }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```
Then the acknowledger receives a new message containing the already
solo-authenticated withdraw transaction for confirmation:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+LwLAf..."
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```
Note that this is the same transaction as the one that the withdrawer has
already authenticated. The acknowledger is to decode the transaction, inspect
its contents, authenticate it, encode it and then post it back via a WebSocket
message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+LwLAfhC..."
  }
}
```

#### Finish withdrawal
After both the parties had authenticated the withdraw transaction, the transaction is posted on-chain and
both parties receive it:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+LwLAfhC...",
      "type": "channel_withdraw_tx"
    }
  },
  "version": 1
}
```
They are both to compute the transaction hash. Using it,
participants can track its progress on the chain: entering the mempool, block
inclusion and a number of confirmations.

After the `minimum_depth` block confirmations each participant is informed
for the withdraw progress on-chain by one's own node:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "own_withdraw_locked"
    }
  },
  "version": 1
}
```
An update from one's own node that the other party had confirmed that the block
height needed is reached:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```
With this the withdrawal sequence is complete and the channel can continue with
other updates. Note that the withdraw transaction's `round` and `state_hash`
are the ones considered latest from the channel's perspective. For example the
next correct off-chain update/deposit/withdrawal shall have a withdraw
transaction's `round` plus one.

### Getting state
At any moment in time any participant can ask one's own FSM for various views of
the latest channel state. This is to help wallet apps but they shall not trust
FSM and compute state locally.

#### Get balances
In order to get the balances as those are part from the channel's state tree, a
participant sends a WebSocket message
```javascript
{
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  }
}
```

The `accounts` section of the payload contains a list of addresses to fetch
balances of. Those can be either account balances or a contract ones, encoded
as an account addresses.

A response of this call looks like
```javascript
{
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999969
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

If a certain account address had not being found in the state tree - it is simply
skipped in the response.

#### Get proof of inclusion
In order to build and use different services, one might need to provide a third party
a minimal view of the internal channel's state.

In order to fetch a proof of inclusion from the latest modified state tree,
a participant sends a WebSocket message
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ],
    "contracts": [
      "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
    ]
  }
}
```

The `accounts` section of the payload contains a list of addresses to include in the
proof of inclusion. Almost the same goes with the contract addesses listed in `contracts` section:
the only difference being that contract's accounts will be automatically be added
to proof of inclusion as well as their state.

A response of this call looks like
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "poi": "pi_+QjLPAH5A..."
    }
  },
  "version": 1
}
```

If a certain address of an account or a contract is not found in the state tree -
the response is an error.

#### Dry-run a contract
In order to get the result of a potential contract call, one might need to
dry-run a contract call. It takes the exact same arguments as a call would and
returns the `call` object.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAA...",
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  }
}
```

The `payload` is an mirror image of the [call contract
update](#trigger-a-contract-call-update), the only difference being that the
dry-run does not impact the state and it does not need authentication. The call is
executed in the channel's state but it does not impact the state whatsoever.
It uses as an environment the latest channel's state and the current top of
the blockchain as seen by the node.

A response to this call looks like
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "caller_nonce": 11,
      "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
      "gas_price": 1,
      "gas_used": 220,
      "height": 11,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### Get contract calls
Each participant persists contract call results locally. It is not required of
both participants to share the same list of contract calls as this does not
impact consensus between them. Any participant can prune his local set of
calls in order to free some memory. In order to inspect the result value of a
contract call, a participant sends a WebSocket message
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 10
  }
}
```
The combination of a `caller_id`, `contract_id` and a `round` of execution determines the
contract call. Providing an incorrect set of those results in an error response.

A non-error response of this call looks like this

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "caller_nonce": 10,
      "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
      "gas_price": 1,
      "gas_used": 220,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

It is worth mentioning that the gas is not consumed, because this is an off-chain contract call.
It would be consumed if it were a on-chain one. This could happen if a call with a
similar computation amount is to be forced on-chain.

#### Pruning contract calls

Contract calls are kept locally in order for the participant to be able to
look them up. They consume memory and in order for the participant to free it -
one can prune all messages. This cleans up all locally stored contract calls
and those will no longer be available for fetching and inspection.

In order to prune local calls, a participant sends the following WebSocket
message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

Once calls are pruned, the same participant receives the following message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

### Solo closing sequence
At any moment in time after the channel had been opened any participant can
initiate a solo closing. The mutual closing takes just one block
inclusion for the effects to take place. The solo closing sequence requires a
couple of blocks and at least 2 transaction fees to be paid. This makes the
solo closing sequence both slower and more expensive. It is intended to be
used when the other party is trying to cheat or is not responding for a while.
This is called a dispute and it is taken to the chain to resolve it. Dispute
resolution has the following steps:

1. single `channel_solo_close` transaction
2. zero or a couple of `channel_slash` transactions
3. single `channel_settle` transaction

The second step is not required and a `channel_solo_close` could be followed
either by zero, one or more `channel_slash` transactions, each subsequent one
presenting a newer state and overwriting the previous one. Those are settled by
a `channel_settle` transaction that finally closes the channel. Let's discuss
those in detail.

#### Payload and proof of inclusion
The idea behind `channel_solo_close` and `channel_settle` is for parties to
provide, on-chain, the latest channel internal state so that the channel can be closed.
First comes the `channel_solo_close` that provides some off-chain state. Then a
`channel_slash` can be posted but it is checked that it has a newer state than the
`channel_solo_close` one. Then parties can post more `channel_slash` transactions
but those are always checked to be containing a newer channel state than the last
received on-chain. If one party tries to cheat by posting some old state - the other
party can present to the chain a newer channel state and this overwrites the previous
posted one. Thus the comparison on channel states is important. This is done
by comparing rounds.

Both `channel_solo_close` and `channel_slash` contain a `payload` field. This
is either a binary containing a `channel_offchain` transaction or an empty
binary.

If it is a `channel_offchain` transaction - it must be mutually authenticated.
It also contains a `channel_id`, `round` and `state_hash`.
The `channel_id` in combination with the correct singatures verifies that
this off-chain transaction indeed is part of the channel off-chain state. The
`round` represents the height of the channel's state at the time the
transaction was mutually authenticated. The higher the round, the newer the
transaction is. This `round` must be greater than the last on-chain one for that channel.
The `state_hash` is the internal channel state tree root hash
at that `round` height.

If the transaction's `payload` is empty - then the latest on-chain state for
this channel is used. Both `channel_deposit` and `channel_withdraw`
transactions contain a `round` and a `state_hash` and the latest received one
overwrites the previous one. If there had been none of those, then the
`channel_create` transaction is used: it has a `state_hash` and an implicit
`round = 1`.

Either by having a value in the `payload` or not having one, the
`channel_solo_close` and `channel_slash` provide a channel's `round` and a `state_hash`.
In order to determine the order of the channel's states received - we compare
the `rounds` and keep the state with the greatest `round`, considered to be
the _newest_ and _latest_ state. They also provide the `state_hash` the
channel's state tree had at this `round`.

Both `channel_solo_close` and `channel_slash` contain a `poi` field. This is
the proof of inclusion for participants' balances in the channel state: all
the insignificant data in the channel's MPT (Matricia Perkel Tree) is replaced
by corresponding hashes.
The root hash of the PoI must be equal to the `state_hash` provided by the `payload`.
This guarantees that the PoI indeed is a proof of inclusion for tree at this height.

#### Solo close on-chain transaction
The `channel_close_solo` transaction is the one that triggers the solo closing
sequence. After it is included on-chain channel enters a _closing_ state and
any subsequent withdrawal or deposits are considered invalid. Preconditions for
the `channel_close_solo` to be valid are:

* channel is opened on-chain
* channel is not in a _closing_ state but not yet closed - no `channel_close_solo` has been
  included in a block yet

Any participant in the channel can post a `channel_close_solo` transaction. In
the scope of this description we will call the one that posts the transaction
_solo closer_.
The transaction has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel to close |
  | from | string | solo closer's public key |
  | payload | binary | closing payload |
  | poi | binary | closing proof of inclusion |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | nonce | integer | solo closer's nonce |

`payload` and `poi` are validated as [described above](#payload-and-proof-of-inclusion)

#### Slash on-chain transaction
After the channel is already in a _closing_ state, both participants can provide
a newer state via the `channel_slash` transaction. Preconditions for
the `channel_slash` to be valid are:

* channel is opened on-chain
* channel is still in a _closing_ state - no `channel_settle` has been
  included in a block yet

Any participant in the channel can post a `channel_slash` transaction. In
the scope of this description we will call the one that posts the transaction
_slasher_.
The transaction has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel to slash |
  | from | string | slasher's public key |
  | payload | binary | slashing payload |
  | poi | binary | slashing proof of inclusion |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | nonce | integer | slasher's nonce |

`payload` and `poi` are validated as [described above](#payload-and-proof-of-inclusion)

#### Settle on-chain transaction
After the `channel_close_solo` and all the `channel_slash` transactions,
it is time to finally close the channel. One of the participants posts a
`channel_settle` transaction that enforces closing of the channel. This
happens according to the latest channel state that was sent on-chain. The
`channel_settle` just finalizes the channel closing with the last received
state, redistributes tokens to participants and closes the channel. No further
disputes are possible after that.


In order to give parties time to slash a closing channel and update its state
with a newer one, there is a timeframe only after which the `channel_settle`
can be posted. This is measured in blocks mined on top of the last received
transaction for that channel (either `channel_close_solo` or `channel_slash`).
The amount itself is prenegotiated before opening the channel and is part of
the `channel_create` transaction - it is the value of `lock_period`. Under no
condition a `channel_settle` can be included in a block before passing the
`lock_period` amount of blocks on top of the last `channel_close_solo` or
`channel_slash` transaction. Every next included `channel_slash` restarts the
timer. It is worth noting that since those transactions must include a `payload`
newer than the prevous on-chain one - this timer can not be postponed
indefinitely. Preconditions for the `channel_settle` to be valid are:

* channel is opened on-chain
* channel is still in a _closing_ state - no other `channel_settle` has been
  included in a block yet
* at least `lock_period` blocks has been mined on top of the last
  `channel_close_solo` or `channel_slash`

Any participant in the channel can post a `channel_settle` transaction. In
the scope of this description we will call the one that posts the transaction
_settler_.
The transaction has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel to settle |
  | from | string | settler's public key |
  | initiator_amount_final | integer | initiator final amount |
  | responder_amount_final | integer | responder final amount |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | nonce | integer | settler's nonce |

The amounts are the exact amounts stored in the channel object on-chain.

#### Connection keep alive

WebSocket connection handlers are to identify abrupt network disconnects.
Thus the WebSocket protocol defines special control frames to be used: sending
`ping` and `pong`. Clients that are run in a browser have no access nor do
they have any control over those frames. They are to be handled by browsers
and this could introduce some undesired incompatibilities.

In order to provide best user experience, we've kept the functionality of the
node to respond with a `pong` control frame to every `ping` received as well
as enhanced the State Channel's WebSocket API with the option of sending data
frames that act like the corresponding control frames. Depending on the
environment to be run, the client can use either approach.

If no frames have been received for 1 minute, the node will consider the
connection to the client to be lost.

A data frame `ping` message has the following structure:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

If the connection is still open, the node will respond to the same participant
with the following message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```
Where `channel_id` has the correct value of the channel's ID.

