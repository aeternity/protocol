[back](./README.md)
# Channels - intended usage

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
  | ttl | integer | minimum block height to include the `channel_create_tx` | No | No | Yes |
  | host | string | host of the `responder`'s node| Yes if `role=initiator` | No | No | No |
  | port | integer | the port of the `responder`s node| Yes if `role=initiator` | No | No | No |
  | role | string | the role of the client - either `initiator` or `responder` | Yes | Yes | No |
  | minimum_depth | integer | the minimum amount of blocks to be mined | No | No | No |

  `responder`'s port and host pair must be reachable from `initiator` network
  so unless participants are part of a LAN, they should be exposed to the
  internet as described [here](../../node/api/README.md).
  
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
  | timeout_funding_sign | the time frame the other client has to sign an off-chain update after our client had initiated and signed it. This applies only for double signed on-chain intended updates: channel create transaction, deposit, withdrawal and etc. | 120000 |
  | timeout_funding_lock | the time frame the other client has to confirm an on-chain transaction reaching maturity (passing minimum depth) after the local node has detected this. This applies only for double signed on-chain intended updates: channel create transaction, deposit, withdrawal and etc. | 360000 |
  | timeout_sign | the time frame the client has to return a signed off-chain update or to decline it. This applies for all off-chain updates | 500000 |
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

### Create transaction signing
The `channel_create_tx` is sent subsequently to both parties and they co-sign
it. Then it is posted to the chain.

#### Initiator signs the tx
The initiator receives a message containing the unsigned transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGG0jrV+AAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwPdeleQ",
      "updates": []
    }
  },
  "version": 1
}
```

Initiator is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEDYguuJ4B7hjxr7SV9LCY3510i/qA9fTF8zJfhGlDsFFmgg1rIJFA07EZyL2/Ynu2j4JJg0lARjMFdxJNyWmhcJuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYbSOtX4ADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/A0KV9Qc="
  }
}
```

Please note that the these are just example transactions and you're to have
different values for those.

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

#### Responder signs the tx
After being informed for the initiator's signing the responder receives a message containing the unsigned transaction to be signed as well
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGG0jrV+AAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwPdeleQ",
      "updates": []
    }
  },
  "version": 1
}
```

Note that this is the same transaction and same updates list. Responder is to
decode the transaction, inspect its contents, sign it, encode it and then post
it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEAo6XIvpjlHU6CjJDz7xB0PJrvYhPjv2dwQWLsGc87fMzITg38TngTaF4XeDxoJiKu/9qPDEHkMgOfZx0QXqHoAuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYbSOtX4ADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/A5iL7Fc="
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

#### Signed channel_create_tx
The responder reports to its client that it received the signing reply, and now has a co-signed
`channel_create_tx`. It relies on the initiator to push the co-signed transaction to the mempool:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAe3emwy3TOhBG+P4PHO6neJqCrrTNAGmDAgn5OnrBEnolO1bbptEtvhGO7YiQhhwv9PrMN6yoJo8sIpkvXl/XBbhAzw/GMFHUWeIRF/LbSk9KFDCVC/bELXyniyW8ywF2Lj+EcFP99dU2vmA9Ny2uLmCONnCmkjKfsm0sotP501R0DLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwiMpqfr",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

The initiator reports to its client that it received the co-signed `channel_create_tx` from the responder:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAKOlyL6Y5R1OgoyQ8+8QdDya72IT479ncEFi7BnPO3zMyE4N/E54E2heF3g8aCYirv/ajwxB5DIDn2cdEF6h6ALhA2ILrieAe4Y8a+0lfSwmN+ddIv6gPX0xfMyX4RpQ7BRZoINayCRQNOxGci9v2J7to+CSYNJQEYzBXcSTclpoXCbiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGG0jrV+AAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwMXN1eS",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### Transaction in mempool
At this point both parties had received the co-signed the `channel_create_tx` transaction. The transaction is posted by the state
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
After both parties have confirmed that the funding is signed - they can proceed
with sending the messages for off-chain updates. The inital state is the one
described in the create transaction.

#### Open confirmation
After both parties have co-signed the state update both of them will receive a info for the channel open:
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

## Channel off-chain update
After the channel has been opened and before it has been closed there is a
channel state that is updated when needed. The updates are off-chain and
broadcasted only between parties in the channel. The state is a full state
tree that holds all the latest accounts, contracts and contract calls.
A state is considered to be valid only if both parties have agreed upon it.
Agreement it proven with signing a message that contains the channel id, round
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

##### Starter signs updated state
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
The starter is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+JALAfhCuEAlFbT+jdksxgDVCgl6e09iLPuKXqkPMa1J7G1YRjOxM+iP0EVsLQapxoeA7ItZXME4tX8gJkvzLfNguxDww4QFuEj4RjkCoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgKg1Sp3gZM4VpxGwtqvRWpM1IetpBe+bJCsv8wGpfT3QuG6IwaQ"
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
      "tx": "tx_+EY5AqEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02ICoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhVgB6xw==",
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

Note that this is the same transaction as the one that the starter had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+JALAfhCuEDDzPKbgRe4N4Av4H0OPDh0mnVHWcAYA9efuP/flWLzDPCd4jlX60ClzddeyEx/EdpjSwFaZt17gSd2yi7D1CQFuEj4RjkCoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgKg1Sp3gZM4VpxGwtqvRWpM1IetpBe+bJCsv8wGpfT3QuHoo3H0"
  }
}
```

#### Finish update
After both the parties have signed the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
co-signed off-chain update so the participants can persist it locally.
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+NILAfiEuEAlFbT+jdksxgDVCgl6e09iLPuKXqkPMa1J7G1YRjOxM+iP0EVsLQapxoeA7ItZXME4tX8gJkvzLfNguxDww4QFuEDDzPKbgRe4N4Av4H0OPDh0mnVHWcAYA9efuP/flWLzDPCd4jlX60ClzddeyEx/EdpjSwFaZt17gSd2yi7D1CQFuEj4RjkCoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgKg1Sp3gZM4VpxGwtqvRWpM1IetpBe+bJCsv8wGpfT3QuFZh9R7"
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
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
    "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
    "deposit": 10,
    "vm_version": 3
  }
}
```
##### Owner signs updated state
The owner receives a message containing the updated channel state as an
off-chain transaction

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+QTXOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FBvkEjrkEi/kEiIICPQGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkD+PkD9UYCoP7pKBTItkQVCAzR2d6TDMx0qz7P7ipMDv7xH+3EZ4ra+QL7+QEqoGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFhG1haW64wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7jMYgAAZGIAAISRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAADAV1CAUX9o8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxRRiAACvV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUVlQgJFQUICQUJBWW1BQgpFQUGIAAIxWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoIz9yhHp4TfRRUoSVD3n476Oqo+7A33pu5LuX8v9hxOA+DIQvQ==",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
          "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
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

The owner is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+QUjCwH4QrhAA4QgOat3r4SK+K2SoTOG39wiNGI4/p9XTAmTIsD9UbG8p6afMIiPgu1OP5aLVUZKsQENeMtntzxryu8ao7lQBrkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb5BI65BIv5BIiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCM/coR6eE30UVKElQ95+O+jqqPuwN96buS7l/L/YcTgJuFGps="
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
      "tx": "tx_+QTXOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FBvkEjrkEi/kEiIICPQGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkD+PkD9UYCoP7pKBTItkQVCAzR2d6TDMx0qz7P7ipMDv7xH+3EZ4ra+QL7+QEqoGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFhG1haW64wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7jMYgAAZGIAAISRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAADAV1CAUX9o8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxRRiAACvV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUVlQgJFQUICQUJBWW1BQgpFQUGIAAIxWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoIz9yhHp4TfRRUoSVD3n476Oqo+7A33pu5LuX8v9hxOA+DIQvQ==",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
          "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
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
Note that this is the same transaction as the one that the owner had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+QUjCwH4QrhAn97VoFwTvEdI1xGr/dFXXbZNNCjn66b4u04bGV5+xWMsOsLRXlJKyuoDpskzy17LfCF1mxfHS/GsYGN4odkBDrkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb5BI65BIv5BIiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCM/coR6eE30UVKElQ95+O+jqqPuwN96buS7l/L/YcTgPTCWa8="
  }
}
```
#### Finish update
After both the parties have signed the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
co-signed off-chain update so the participants can persist it locally.
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "state": "tx_+QVlCwH4hLhAA4QgOat3r4SK+K2SoTOG39wiNGI4/p9XTAmTIsD9UbG8p6afMIiPgu1OP5aLVUZKsQENeMtntzxryu8ao7lQBrhAn97VoFwTvEdI1xGr/dFXXbZNNCjn66b4u04bGV5+xWMsOsLRXlJKyuoDpskzy17LfCF1mxfHS/GsYGN4odkBDrkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb5BI65BIv5BIiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCM/coR6eE30UVKElQ95+O+jqqPuwN96buS7l/L/YcTgNbQi/k="
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
  | contract | string | address of the contract to call |
  | abi_version | integer | version of the ABI |
  | amount | integer | amount the caller of the contract commits to it |
  | call_data | string | ABI encoded compiled AEVM call data for the code |

That would call a contract with the poster being the `caller` of it. Poster
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
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  }
}
```

##### Caller signs updated state
The caller receives a message containing the updated channel state as an
off-chain transaction

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQXMSDYKchQbN/BdXL3PgW4GBwYGgLkzPIGiw15gFwyhlgEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKBmNmU3LwTMKrAhSxwIUR59mTgDbVqjhQNnALqIc1ncQ5mkxak=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
          "call_stack": [],
          "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
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

The caller is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+QFqCwH4QrhAsiGALSOnzLx95Bk8unNXuxeRKqRRxisVaIKMajNFLhSkieah4h96xwIu0FpsRjFgblzGjHOZSQlsAH/iUvpoCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgZjZlNy8EzCqwIUscCFEefZk4A21ao4UDZwC6iHNZ3EPscgv1"
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
      "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQXMSDYKchQbN/BdXL3PgW4GBwYGgLkzPIGiw15gFwyhlgEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKBmNmU3LwTMKrAhSxwIUR59mTgDbVqjhQNnALqIc1ncQ5mkxak=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
          "call_stack": [],
          "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
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
Note that this is the same transaction as the one that the caller had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+QFqCwH4QrhAFTUbMymALIdq1DFUQLov+rItP4g6pIc5IVxUoT5Gt3XlXI+zYYyeFC2aoAv+BMghSuF3bR77a9ZqsabtfLH1B7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgZjZlNy8EzCqwIUscCFEefZk4A21ao4UDZwC6iHNZ3ENFKkBe"
  }
}
```
#### Finish update
After both the parties have signed the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
co-signed off-chain update so the participants can persist it locally.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "state": "tx_+QGsCwH4hLhAFTUbMymALIdq1DFUQLov+rItP4g6pIc5IVxUoT5Gt3XlXI+zYYyeFC2aoAv+BMghSuF3bR77a9ZqsabtfLH1B7hAsiGALSOnzLx95Bk8unNXuxeRKqRRxisVaIKMajNFLhSkieah4h96xwIu0FpsRjFgblzGjHOZSQlsAH/iUvpoCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgZjZlNy8EzCqwIUscCFEefZk4A21ao4UDZwC6iHNZ3EMR8cBv"
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
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": 8
  }
}
```
The `contract_address` is the address of the contract that had been called, the `round` is the round of the update and
`caller_address` is the address of the caller.

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
current mutually signed state and then terminates. The `'reestablish'` request
is very similar to a [Channel open](#channel-open) request, but also requires
the channel id and the latest mutually signed state.

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
      "state": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
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
localhost:3014/channel?existing_channel_id=ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAP%2BEiPpXFO80MdqGnw6GkaAYpOHCvcP%2FKBKJZ5IIicYBItA9s95zZA%2BRX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV%2FmHihVXzgLyaRaI%2FSVw2KS%2Bz471bAriD%2BIEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe%2BrdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D%2F5sB8yCR8WumWh0WxWvwdz6zEk&port=12341&protocol=json-rpc&role=initiator
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

followed by an update report with the latest mutually-signed state:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
    }
  },
  "version": 1
}
```

## Channel mutual close
At any moment after the channel is opened, a closing procedure can be
triggered. This can be done by either of the parties. The process is similar to
the [off-chain updates](#channel-off-chain-update). The most notable change is the
special transaction co-signed by both parties. It is called
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

### Starter signing
Then the starter receives a `channel_close_mutual_tx` to sign:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "tx": "tx_+F01AaEGXfP3k2aiLfV2X4HR75EK/1UzKSNqQqHHe0CN8/jQc6GhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmhjaR1q+//4YbSOtX4AEAhhIwnOVAAAWwHvpF",
      "updates": []
    }
  },
  "version": 1
}
```
Starter is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_+KcLAfhCuEC1uzCpbr9f7MYnkb5u/iL9okyhJTcRMGlTIqgMsari9Kdomn+Z+P3FmcAw1ma4GENBPYF/hl/X9EJi1fktkKAOuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAABc176hQ="
  }
}
```
### Acknowledger signing
Then the acknowledger receives a `channel_close_mutual_tx` to sign:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "tx": "tx_+F01AaEGXfP3k2aiLfV2X4HR75EK/1UzKSNqQqHHe0CN8/jQc6GhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmhjaR1q+//4YbSOtX4AEAhhIwnOVAAAWwHvpF",
      "updates": []
    }
  },
  "version": 1
}
```
Note that this is the same transaction. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_+KcLAfhCuEA2hK6nlhTF+hVjLYYoh09xVn5M4BrSwB3dXyjteMotYj8/+WpdbJwvO1KBUsg2p2zedlZnnVfR5g7O4m1q9OkOuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAABY9XDr0="
  }
}
```

#### Signed `channel_close_mutual_tx`
Both participants receive the co-signed `channel_close_mutual_tx`:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEA2hK6nlhTF+hVjLYYoh09xVn5M4BrSwB3dXyjteMotYj8/+WpdbJwvO1KBUsg2p2zedlZnnVfR5g7O4m1q9OkOuEC1uzCpbr9f7MYnkb5u/iL9okyhJTcRMGlTIqgMsari9Kdomn+Z+P3FmcAw1ma4GENBPYF/hl/X9EJi1fktkKAOuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAABVYF49s=",
      "type": "channel_close_mutual_tx"
    }
  },
  "version": 1
}
```
Using its hash, participants can track its progress on the chain: entering the mempool, block inclusion and a number of confirmations.

### Channel closing
After both parties have received the co-signed `channel_close_mutual_tx`
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
After calculating the hash of the co-signed `channel_close_mutual_tx` parties can track
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

The `channel_close_solo` transaction only needs a single signature, and is described in more detail in [this section](#channel-solo-close).

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

### Requester signing
Then the requester receives a `channel_close_solo_tx` to sign:
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

Requester is to decode the transaction, inspect its contents, sign it, encode it
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

As the channel fsm receives the signed solo close transaction, verifies it
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

#### Requester signing
Then the requester receives a `channel_settle_tx` to sign:
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

The requester is to decode the transaction, inspect its contents, sign it,
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
As the channel fsm receives the signed settle transaction, verifies it
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
state is reverted to the last mutually signed one. Both participant receive a
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
difference is the transaction has been co-signed: it is `channel_deposit_tx` and
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

##### Depositor signs updated state
The depositor receives a message containing the updated channel state as a
`channel_deposit_tx` transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HIzAaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoIGnTOuUnVM9QThcVqCCAFeJ51D7a6A4ldyhd3nuKg7lAglKqnZP",
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
The depositor is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "tx": "tx_+LwLAfhCuEBpdn6/h5FeyYL9/JMO3XqEDdmaxrtsqamG4XJJAUNoQI0DtzQVkGHWC4lia9rcsNa9vdBj0a5o8S7fGE3I8Z0FuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCYBI8r0="
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
transaction for confirmation:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HIzAaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoIGnTOuUnVM9QThcVqCCAFeJ51D7a6A4ldyhd3nuKg7lAglKqnZP",
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
Note that this is the same transaction as the one that the depositor had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEBa3V9ZXezm+ya0GQGg7RBpS6DbYhiE10oRgSuHpn0JFsdcUz0f2Ldsi1I62JxkLmDAqhxIgYUeya0PP1M4PXsOuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCXv07Q4="
  }
}
```

#### Finish deposit
After both parties had signed the deposit transaction, the transaction is posted on-chain and
both parties receive it:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBa3V9ZXezm+ya0GQGg7RBpS6DbYhiE10oRgSuHpn0JFsdcUz0f2Ldsi1I62JxkLmDAqhxIgYUeya0PP1M4PXsOuEBpdn6/h5FeyYL9/JMO3XqEDdmaxrtsqamG4XJJAUNoQI0DtzQVkGHWC4lia9rcsNa9vdBj0a5o8S7fGE3I8Z0FuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCZiFbkw=",
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
difference is that the transaction has been co-signed: it is `channel_withdraw_tx` and
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

##### Withdrawer signs updated state
The withdrawer receives a message containing the updated channel state as a
`channel_withdraw_tx` transaction
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoEUfp6Gv3gLYNHIy08ITGVY9Xv7I69D5Yu0FUzyRePtuBAqOT2uR",
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
The withdrawer is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_+LwLAfhCuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECi9pymI="
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
Then the acknowledger receives a new message containing the withdraw
transaction for confirmation:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoEUfp6Gv3gLYNHIy08ITGVY9Xv7I69D5Yu0FUzyRePtuBAqOT2uR",
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
Note that this is the same transaction as the one that the withdrawer has already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECjOLPuM="
  }
}
```

#### Finish withdrawal
After both the parties had signed the withdraw transaction, the transaction is posted on-chain and
both parties receive it:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24EChZDmcY=",
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
      "poi": "pi_+QjLPAH5Aar5AaegUHXVJYllXPYCKsNzFPm556q8IgudzPRI4O/BDFpobNP5AYP4lKBQddUliWVc9gIqw3MU+bnnqrwiC53M9Ejg78EMWmhs0/hxgICAgICAoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJgICAgKCQ1bLD69k9BcQwVvuyoPXBJe++idIJ/lwoO4qPYlt0YaCmyjgxBha42v7WL6pOfqG1Ttf6NYVnqZHqR+T0JmGLxYCAgID4T6CQ1bLD69k9BcQwVvuyoPXBJe++idIJ/lwoO4qPYlt0Ye2gMbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aLygoBAIY/qiUiX/X4SaCmyjgxBha42v7WL6pOfqG1Ttf6NYVnqZHqR+T0JmGLxeegPEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZaFxAoBAAr4T6DtAhY8YmyH3XobvMIBmlR5pFC4ZVqbCNHwlrFAoQ8jCe2gNxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAHj4qAjoqXI5ZEb6//BQUWWVlPkHd4lWRhzVFmXY/6F2X4ZBMDA+Qby+QbvoCP+J+CKG9HLoyiF11XYCmZ637Cc43DhBKz5ZV3DDp7r+QbL+IagCHQOBl3W9IhcdkmZJCJrKJ+h0G8+ZeIKUZ3W5p9/Nez4YyC4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////hmoCP+J+CKG9HLoyiF11XYCmZ637Cc43DhBKz5ZV3DDp7r+EOhAMxINgpyFBs38F1cvc+BbgYHBgaAuTM8gaLDXmAXDKGWoFfuIRzcN3UiqZeS8ooxO7bH4x9PphQ5GgpJtO3WWhJu+ESgJ6ky/mLaY+D64bXs7TR5BIRxO0hOakcKlSHrfu7sP7/iEKA1jHy+JkYGJXeg4QZT9QYTyIjuaukMdPKoxXeDh8vbz/hToDWMfL4mRgYld6DhBlP1BhPIiO5q6Qx08qjFd4OHy9vP8aCFlE6Nir08G/FQ+dPMIRjPZKt+jIKfH4aEhiH2DCC/C4CAgICAgICAgICAgICAgAD4RKA/cNKMPbnMACszBp/R0S52OAbwRhxnBpoCOSMcfJ92pOIgoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QSBoFfuIRzcN3UiqZeS8ooxO7bH4x9PphQ5GgpJtO3WWhJu+QRdgKAnqTL+Ytpj4PrhteztNHkEhHE7SE5qRwqVIet+7uw/v4CAgICAgICAgICAgICAuQQq+QQnKAGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkD+PkD9UYCoP7pKBTItkQVCAzR2d6TDMx0qz7P7ipMDv7xH+3EZ4ra+QL7+QEqoGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFhG1haW64wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7jMYgAAZGIAAISRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAADAV1CAUX9o8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxRRiAACvV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUVlQgJFQUICQUJBWW1BQgpFQUGIAAIxWhTIuMS4wgAHACvh0oIWUTo2KvTwb8VD508whGM9kq36Mgp8fhoSGIfYMIL8L+FGgP3DSjD25zAArMwaf0dEudjgG8EYcZwaaAjkjHHyfdqSgCHQOBl3W9IhcdkmZJCJrKJ+h0G8+ZeIKUZ3W5p9/NeyAgICAgICAgICAgICAgIDAwC95Gqk="
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
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  }
}
```

The `payload` is an mirror image of the [call contract
update](#trigger-a-contract-call-update), the only difference being that the
dry-run does not impact the state and it does not need signing. The call is
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
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 10
  }
}
```
The combination of a `caller`, `contract` and a `round` of execution determines the
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

If it is a `channel_offchain` transaction - it must be co-signed by both
participants. It also contains a `channel_id`, `round` and `state_hash`.
The `channel_id` in combination with the correct singatures verifies that
this off-chain transaction indeed is part of the channel off-chain state. The
`round` represents the height of the channel's state at the time the
transaction was co-signed by the parties. The higher the round, the newer the
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
