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

The channel websocket api currently supports two protocols: [`json-rpc`](https://www.jsonrpc.org/specification) and `legacy`. Which protocol to use can be specified with the `protocol` option.
 If omitted, `legacy` is chosen by default, although this default is likely to change in the future.

 In the examples below, the `legacy` protocol is used. For a description on how to translate into the `json-rpc` format, see [channel_ws_api_json-rpc.md](channel_ws_api_json-rpc.md).

Detailed message transcripts from test suites can also be found [for JSON-RPC](./examples/aehttp_integration_SUITE/json-rpc/) and [for `legacy`](./examples/aehttp_integration_SUITE/legacy/)

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
```
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
```
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
```
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwhG8eVK",
      "updates": []
    }
  },
  "version": 1
}
```
Initiator is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEB7d6bDLdM6EEb4/g8c7qd4moKutM0AaYMCCfk6esESeiU7Vtum0S2+EY7tiJCGHC/0+sw3rKgmjywimS9eX9cFuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/COnyKTM="
  }
}
```

Please note that the these are just example transactions and you're to have
different values for those.

#### Responder is informed
The responder receives the following message
```
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
```
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwhG8eVK",
      "updates": []
    }
  },
  "version": 1
}
```
Note that this is the same transaction and same updates list. Responder is to
decode the transaction, inspect its contents, sign it, encode it and then post
it back via a WebSocket message:
```
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEDPD8YwUdRZ4hEX8ttKT0oUMJUL9sQtfKeLJbzLAXYuP4RwU/311Ta+YD03La4uYI42cKaSMp+ybSyi0/nTVHQMuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/CIFZNcM="
  }
}
```
#### Initiator is informed
The initiator receives the following message
```
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
Both participants receive the co-signed `channel_create_tx`:
```
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAe3emwy3TOhBG+P4PHO6neJqCrrTNAGmDAgn5OnrBEnolO1bbptEtvhGO7YiQhhwv9PrMN6yoJo8sIpkvXl/XBbhAzw/GMFHUWeIRF/LbSk9KFDCVC/bELXyniyW8ywF2Lj+EcFP99dU2vmA9Ny2uLmCONnCmkjKfsm0sotP501R0DLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwiMpqfr"
    }
  },
  "version": 1
}
```
Using its hash, participants can track its progress on the chain: entering the mempool, block inclusion and a number of confirmations.

#### Transaction in mempool
At this point both parties had received the co-signed the `channel_create_tx` transaction. The transaction is posted by the state
channel's software to the node and goes to the mempool. Having calculated its hash, one can validate it using the external HTTP API:
```
$ curl 'http://localhost:3013/v2/transactions/th_hNyHzj4dSzyBqReAMR36GGz1mhuXxQFuES3AnPkXkuY2w6dZb'
```
if the `block_hash` is `none` - then the transaction is still in the mempool.

### Block inclusion
When the transaction is included in a block - this is the first confirmation. A block height timer is
started and it ends after `minimum_depth + 1` confirmations. Default value for
it is 4, so 5 blocks need to be mined. As a result, each party will receive
two kinds of confirmation.

An update from one's own node that the block height needed is reached:
```
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```
An update from one's own node that the other party had confirmed that the block
height needed is reached:
```
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
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
```
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

From this point on, the channel is considered to be opened.

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
##### Trigger a transfer update
The starter sends a message containing the desired change
```
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
```
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4Zxbb8Q=",
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
```
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEAFOva8xKyh9tzeIps9Tum89u4xTvbT0yokbLnu78KnIK6wZRZiYlwrBujUEQg0t3Tud9BXDn5oKwnkdJizmA0GuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090Lh+pkf9A=="
  }
}
```
#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```
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
```
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4Zxbb8Q=",
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
```
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAGx0qykrlj5/DVq6RJ2AsMe6uiCL4TX8Emv1sC3TL2IdDp9S3jrzRQnIe6gWtM/9kR++JRGwVL+gs+O7SjCKYIuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhNHGU2A=="
  }
}
```
#### Finish update
After both the parties have signed the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
co-signed off-chain update so the participants can persist it locally.
```
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhABTr2vMSsofbc3iKbPU7pvPbuMU7209MqJGy57u/CpyCusGUWYmJcKwbo1BEINLd07nfQVw5+aCsJ5HSYs5gNBrhABsdKspK5Y+fw1aukSdgLDHurogi+E1/BJr9bAt0y9iHQ6fUt4680UJyHuoFrTP/ZEfviURsFS/oLPju0owimCLiX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4ffJBsU="
    }
  },
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
```
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

```
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

```
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
```
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
```
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
```
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
```
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
```
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  }
}
```

##### Caller signs updated state
The caller receives a message containing the updated channel state as an
off-chain transaction

```
{'action': 'sign',
 'tag': 'update',
 'payload' {
    'tx': 'tx_Sweh544j3PL6BzGK8Sk6dqW9ywspMup8J8ETuajNnTGkx3vTbwCS8K8LWAPNSBrkDUWEQCxDR2Kyvuv2v19YtsiNxcetmwWwEjYicTaZ1nZ84PvVs5WoP4LgSgur5yaiDwvoY4xkk5dGjfiXGYWE7udn8HwbZdHUQPXWtJdeGhcApf31SPYWUkW3hWk8sKZeHKU6f9aLQgiSsP2MNoqzfiTL1xppK4NPrS6gje7iVGdz8zBbQ1TRXcTsN7pecY8fSPMwKhEtH88jRbmXouYxatBUvYLy4vRiQJBcsZaCXhHKezoXqggPsPDUjfaM1P1FMrC3GxWS3CHotuR588TuvaUwPBVjwwoMYL1MJcTYLvejnDktsisFtfhH811h7R7pazQuhqbmMSWhRkYMLfXXwTXs32q334CMEZpz1UpWWA1DRJMBUVWmE7FmPedZDaqobUbNe2CKPk8oMG9apvdrrxE6cQRGupVyjXNor'}
}
```

The caller is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:

```
{'action': 'update',
 'payload': {
    'tx': 'tx_C4TACwXiGbsZf6sCqqEkZU7ngzvoDdqPHQMfNVGZUMQhsT9Nj64j3DbGYE6nB8V7R56zmfY8zuGCjAWgZecsby4RCwDtm5nE57DcX3srHgrzt4NS1mFUq9Vuan57SXT8n4xA5BFjz8WvKEqFptsHqzRhv6veY5o9cmTi4ea1t21BaCdfZiVg6mkf4pvrAzsNtnQ149BxuCLqLJJdaJXVWzJthDXBHLcHmDRTvqYRpnH8gD2veHizbJqnvApeVGwMJ9m5rZc3Tw3EDcZnsiFzKXBiZ1FMMBqZtiNzCCRhhn7uANkJiSi8e8iHcBJLyFRPzSgU6KTVNVGcc2CZVh2RQcMoJXWecdHHeMiCnGaX2MiT2EyjEox9a7kZBkTAAnoeri5F2GhGvdK98a275PjaCrA16xizH2DnvRdw92HFA2PgjQmHE3SgxB7MMhTAkaR3LcqmR5KfwLqikneU9DNM5PQzvYTh1J7rupP9AHXUhhFpGQXYcakXQfmEt2D3D4E3zBGDWqJRfVG8xmxYftzefkx5X5CpeWnCyiCepnUSbNyHFxZS4vyzvhZnTHmWVZksyY68MJAMmERk9'
    }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```
{'action': 'info',
 'payload': {'event': 'update'}
 }
```
Then the acknowledger receives a new message containing the updated channel state as an
off-chain transaction
```
{'action': 'sign',
 'tag': 'update_ack',
 'payload' {
    'tx': 'tx_Sweh544j3PL6BzGK8Sk6dqW9ywspMup8J8ETuajNnTGkx3vTbwCS8K8LWAPNSBrkDUWEQCxDR2Kyvuv2v19YtsiNxcetmwWwEjYicTaZ1nZ84PvVs5WoP4LgSgur5yaiDwvoY4xkk5dGjfiXGYWE7udn8HwbZdHUQPXWtJdeGhcApf31SPYWUkW3hWk8sKZeHKU6f9aLQgiSsP2MNoqzfiTL1xppK4NPrS6gje7iVGdz8zBbQ1TRXcTsN7pecY8fSPMwKhEtH88jRbmXouYxatBUvYLy4vRiQJBcsZaCXhHKezoXqggPsPDUjfaM1P1FMrC3GxWS3CHotuR588TuvaUwPBVjwwoMYL1MJcTYLvejnDktsisFtfhH811h7R7pazQuhqbmMSWhRkYMLfXXwTXs32q334CMEZpz1UpWWA1DRJMBUVWmE7FmPedZDaqobUbNe2CKPk8oMG9apvdrrxE6cQRGupVyjXNor'
    }
}
```
Note that this is the same transaction as the one that the caller had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'update_ack',
 'payload': {
    'tx': 'tx_C4TACwXiGbsZg1Z9ChAEuaVJge62Uax5riSw4Tpp763SKTwLLGjhqPDUqjb9swx5X2G6XnpQk72v1yhFSLZvPtUv4JgoimKLqhAVUSoHB3btwEUTdgb3kVbaS6WLiaF86cqBZiDwbiL3GpThgZK7VhYedXFZK6PdK2RjywURhC9s8PNwP19Zetj19VkL4MYn1Z5tkoEh387dMfh9Mfh9jPf7gaBJjvwxNLuMjqHQXwSKPEpR8jYBF4cuzwaZzWeUSPKMxp44wDWQqqG8MTMwR1i8JbZjbAFtuj49TJWMw6xrvXski8XieHLHXrx5y4873CgD1FhRQT374Yvb5mYBTMtsYc8ttUCPiwi7AQteey7h1iRJgGc5bcd2omdGG8BmQZETfLaqwqXWN7mXXxPGfJQUaknHdocTum9FNyncYiAt6Y7znFJ1rZT2UkHvKwbvtJvhftWBJPrbExfeFMypn9DoW4SoaQ7RjBcmz5PWdt79BjRXhZpM7qbjvGF9i1f2cXiQFeKcj9FxXdzttN28kdtDvpYWdBbWcSMaWAYy7EBnMRHrGo2XdcDeJeGQdGnSBKaMHdN5LVhKF'
  }
}
```
#### Finish update
After both the parties have signed the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
co-signed off-chain update so the participants can persist it locally.

```
{'action': 'update',
 'channel_id: 'ch_RnmrHrmv7m37fMS9RfWAGZMhtDbYnqJk4n7G9X9bTyepzwm5t',
 'payload': {
    'state': 'tx_L1mTJpyV97nWgMAFmrqcwECSThovgaU9qv5DYeqn3YQgzjCShS96n6u2rACsXyXAJyRrqGNTv2ytC1LgmH8zSuD6SkDTEiT2eCGuCsM1xXyZGooq14nu8naSZ3rhJEwBoZLTn3Tt86W3eUc1rPs2HaFwtxwsFhFu4dXHJTjmaVjigG8Juhvq1oQytscRCPVt9sjijr8h1mCCj73yhnsvwwJuMLi9WgspqwJfHHRVc8RWPtvKg6hbUKxn4cEP2M1rpXhVEUhCAkgKVfm58m4xvnuCNhvJhi37cGeSMSJkdrs64111jnQY2nwpiiS5dRW8c3VcHt1Zm8Sg1fyQgdmgbr3Rwbez1L6hCndppgX1DA2UniQB1y7eqC8nYMe4DUmXxnjcFxCQyaiTCBGavjcZiQUThHzwoACJ1yf4fr1HXZ2BzsgeSsuE2AuvphAvtiPSDmRUiFwxt1KGg3YRBxsSqs2Ums7D6QDoju11VH3k8ERcb9Hj6uJmHFC2yGu48jKHPB8bUCm1qDBZqEiDBVTQo6E1AiSLtvJmLoRd1gyUZ4pvCPPmGPQJ4Qsb16xH6q4YnJVMVQb7TWSs5PorsdqV1XPKg8rZSwSZJGZ1gT7fkf75ocXt986k3PMNCa98cDQmwbqFuqYYC4iMixj6k2txsFYUCyxrucHidNC8MFC'}
 }
```

#### Getting a call result
All calls are stored in the channel state tree. In order to extract one out of
there and inspect it, one shall send a WebSocket event
```
{'action': 'get',
 'tag': 'contract_call',
 'payload': {
    'contract_address': 'ct_9sRA9AVE4BYTAkh5RNfJYmwQe1NZ4MErasQLXZkFWG43TPBqa',
    'caller_address': 'ak_2YeNqB4jQ1DG7QvUKgCkKeZAiXb2rnzkEoLTS8XeKF8Smgit2e',
    'round': 8
    }
}
```
The `contract_address` is the address of the contract that had been called, the `round` is the round of the update and
`caller_address` is the address of the caller.

Then the call is returned through an incoming message:
```
{'action': 'get',
 'tag': 'contract_call',
 'payload': {
      'contract_address': 'ct_9sRA9AVE4BYTAkh5RNfJYmwQe1NZ4MErasQLXZkFWG43TPBqa',
      'caller_address': 'ak_2YeNqB4jQ1DG7QvUKgCkKeZAiXb2rnzkEoLTS8XeKF8Smgit2e',
      'caller_nonce': 8,
      'gas_price': 0,
      'gas_used': 524,
      'height': 8,
      'return_type': 'ok',
      'return_value': 'cb_11111111111111111111111111111115rHyByZ'
    }
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
{'action': 'leave'}
```

The fsm responds with the following type of report:
```javascript
{'action': 'leave',
 'channel_id': 'ch_FhYNM5KorNAcRwexe1CE3jH5DZd7FBD2g9XhBDHGEouDqVRCR',
 'payload':
    {'state': 'tx_6jPYBUFTkcmQ7A3JYkUsYMChMHNqe3TMEhDZaSat7P1sbP4XXQP9QmaFfaAftUDjws3GhdKaBGyJRMBhHKyk2irBZsymgUVuxfQXR63ojEjg7C583D6cNKLSZtybZr9Cw6mmCkSDRVu41WbF1jKEkAkXbXznANm3AyJ1BLqNVB7qiAyFSVeq5qVcvHL4Z1y2DAhcLLw6YGSqFyuyg8pKVQRhL2LuePa9mdtoYZyY5VhvgShLz2oY8R3taBL8RrnnTvcwECvQu51yPKyM2pryoHaQbED5Zn7hdegZy6KN9wfpLXedtNB9ssmMvz5jHcK12vmtfeUMzRrySqtmBDGfiqwFZrYZ5A7xz1uqi'
    }
}
```

### Reestablish
Open the channel in the same way as in the
[Initiator WebSocket open](#initiator-websocket-open) example,
adding the parameters `existing_channel_id` and `offchain_tx` with values
matching the ones provided in the `leave` report above. Some parameters (related to open transaction) are not required and ignored. See [Channel parameters](#channel-parameters):

```
$ wscat --connect
'localhost:3014/channel?initiator=ak_...&role=initiator&existing_channel_id=ch_FhYNM5KorNAcRwexe1CE3jH5DZd7FBD2g9XhBDHGEouDqVRCR&offchain_tx=tx_6jPYBUFTkcmQ7A3JYkUsYMChMHNqe3TMEhDZaSat7P1sbP4XXQP9QmaFfaAftUDjws3GhdKaBGyJRMBhHKyk2irBZsymgUVuxfQXR63ojEjg7C583D6cNKLSZtybZr9Cw6mmCkSDRVu41WbF1jKEkAkXbXznANm3AyJ1BLqNVB7qiAyFSVeq5qVcvHL4Z1y2DAhcLLw6YGSqFyuyg8pKVQRhL2LuePa9mdtoYZyY5VhvgShLz2oY8R3taBL8RrnnTvcwECvQu51yPKyM2pryoHaQbED5Zn7hdegZy6KN9wfpLXedtNB9ssmMvz5jHcK12vmtfeUMzRrySqtmBDGfiqwFZrYZ5A7xz1uqi
```

The channel fsm responds with the following event reports if all goes well:
```javascript
{'action': 'info',
 'payload': {'event': 'channel_reestablished'}
}
```

then the standard report indicating that the channel is open:
```javascript
{'action': 'info',
 'channel_id': 'ch_FhYNM5KorNAcRwexe1CE3jH5DZd7FBD2g9XhBDHGEouDqVRCR',
 'payload': {'event': 'open'}
}
```

followed by an update report with the latest mutually-signed state:
```javascript
{'action': 'update',
 'channel_id': 'ch_FhYNM5KorNAcRwexe1CE3jH5DZd7FBD2g9XhBDHGEouDqVRCR',
 'payload':
   {'state': 'tx_6jPYBUFTkcmQ7A3JYkUsYMChMHNqe3TMEhDZaSat7P1sbP4XXQP9QmaFfaAftUDjws3GhdKaBGyJRMBhHKyk2irBZsymgUVuxfQXR63ojEjg7C583D6cNKLSZtybZr9Cw6mmCkSDRVu41WbF1jKEkAkXbXznANm3AyJ1BLqNVB7qiAyFSVeq5qVcvHL4Z1y2DAhcLLw6YGSqFyuyg8pKVQRhL2LuePa9mdtoYZyY5VhvgShLz2oY8R3taBL8RrnnTvcwECvQu51yPKyM2pryoHaQbED5Zn7hdegZy6KN9wfpLXedtNB9ssmMvz5jHcK12vmtfeUMzRrySqtmBDGfiqwFZrYZ5A7xz1uqi'
   }
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
```
{'action': 'shutdown'}
```

### Starter signing
Then the starter receives a `channel_close_mutual_tx` to sign:
```
{'action': 'sign',
 'tag': 'shutdown_sign',
 'payload': {
    'tx': 'tx_SUBGDUaJgWhDYs73EPSiX42Xd3PSmHAhRmwd1th9ibGipCVVbsdS96roQZEH4MF'
    }
}
```
Starter is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'shutdown_sign',
 'payload': {
    'tx': 'tx_8oWtHcfnWDSQV6Wdehp1MdXYhcbV29a7tWe3LWDqU5RwKvMhzPQLiSJKaYhtw4NLaBN1m3pmEtsVjoygkohXi9i8e3vpYgenphdKJmYLrFqjouxmyC5yKbsQUY8m9i4EzcMNuHmrLwrXrrPhKC1qY25Pxb6u74VEVuk'
    }
}
```
### Acknowledger signing
Then the acknowledger receives a `channel_close_mutual_tx` to sign:
```
{'action': 'sign',
 'tag': 'shutdown_sign_ack',
 'payload': {
    'tx': 'tx_SUBGDUaJgWhDYs73EPSiX42Xd3PSmHAhRmwd1th9ibGipCVVbsdS96roQZEH4MF'
    }
}
```
Note that this is the same transaction. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'shutdown_sign_ack',
 'payload': {
    'tx': 'tx_8oWtHcfnWDSYu4SfLLLHqYqM5JXiCZd6De7fLQZesMHrArZeWzP7893EVpBpUR56tKUeJXJ3YUTuqB8a4efiHaw6ai3GKwoeu3ZyzfGPUfb5EMG6viv2dM8mhtKqaG7fkEAWuswbmFN4bDjXANbAK2sMU36yfBc9p1h'
    }
}
```

#### Signed channel_close_mutual_tx
Both participants receive the co-signed `channel_close_mutual_tx`:
```
{'action': 'on_chain_tx',
 'payload': {'tx': 'tx_ERkuTBJfEHtrmDkFz7BaigSKsnqmsCc8MorKFUwAW5VmpSoatcN3Njy2Vda8asojeshjb7SoXsqevaDLzXj78GSPwTTfYJmJtwrewTwK3LSFBe5BEYMA8rxNAWSahW1ecp1wbkBgpdiUQn1Q1UFLcYVpWYGpTWFH5DXn69iz6kFWX8sa7c5PSTaLenjVZEkbV9pEgKHKbjfovvd15Jc821y3zhQvtfhcYKS89r7gnhi81LWsjnSghmjANgjiC'
            }
}
```
Using its hash, participants can track its progress on the chain: entering the mempool, block inclusion and a number of confirmations.

### Channel closing
After both parties have received the co-signed `channel_close_mutual_tx` transaction, it is posted on the chain and the microservice handling the off-chain
requests dies. Parties receive the following info:
```
{'action': 'info',
 'payload': {'event': 'died'}
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

### Other WebSocket events
#### Update error
Updates are not always successful, for example one participant tries to spend
more tokens that one currently has in the channel's balance. This diverges
from the update flow [described above](#channel-off-chain-update).

Example message for when the `from` does not have enough tokens to spend
```
{'action': 'error',
 'payload': {'reason': 'insufficient_balance',
             'request': {'action': 'update',
                         'payload': {'amount': 10000,
                                     'from': 'ak_8wWs1j2vhgjexQmKfgEBrG8ysAucRJdb3jsag3PJKjEeXswb7',
                                     'to': 'ak_bmtGbfP3SdPoJNZCQGjjzbKRje15J9CEcWYaL1gZyv2qEyiMe'
                                     },
                          'tag': 'new'
                          }
              }
}
```

The structure is having a `reason` and `request` holding the request being
sent. Possible error reasons are:

* `insufficient_balance` - when `from` does not have enough tokens in the
  channel. Keep in mind that there is a minimal amount of `channel_reserve`
  tokens to be kept by both parties.

* `negative_amount` - the `udpate` event contained a negative amount

* `invalid_pubkeys` - at least one of the addresses in the `update` event is
  not present in the channel.

#### Update conflict

Since updates can be triggered by either party, it is possible both
participants to start an `update` almost simultaneously. If a new `update` is
started by a participant while the other participant has started an `update` of
ones' own - a conflict occurs. Then both `update`-s are invalidated and the
state is reverted to the last mutually signed one. Both participant receive a
message containing a reference to the correct state.
```
{'action': 'conflict',
 'payload': {'channel_id': 'ch_WmpDbaiCs5roqRCL5KEKbpsDNJSbcbiUvt2cs1qyj4sM9HA3b',
             'round': 42
             }
}
```

#### Generic messages

There is the functionality to send participants messages containing
information. In the scope of this - we are going to be calling those a `sender`
and a `receiver`. These roles can be taken by any of the participants, anytime.

The `sender` pushes a message with the following structure:

```
{'action': 'message',
 'payload': {'info': 'hejsan',
             'to': 'ak_bmtGbfP3SdPoJNZCQGjjzbKRje15J9CEcWYaL1gZyv2qEyiMe'
             }
}
```

Then the `receiver` gets an event containing the info being sent and some
details:

```
{'action': 'message',
 'payload': {'message': {'channel_id': 'ch_6SgSc7a14dGbwMNCsjjQZCYVreVLKkFwBzJEZ58ZSZnV9FiQ1',
                         'from': 'ak_8wWs1j2vhgjexQmKfgEBrG8ysAucRJdb3jsag3PJKjEeXswb7',
                         'to': 'ak_bmtGbfP3SdPoJNZCQGjjzbKRje15J9CEcWYaL1gZyv2qEyiMe',
                         'info': 'hejsan'
                         }
            }
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
```
{'action': 'deposit',
 'payload': {
    'amount': 2
    }
 }
```

##### Depositor signs updated state
The depositor receives a message containing the updated channel state as a
`channel_deposit_tx` transaction
```
{'action': 'sign',
 'tag': 'deposit_tx',
 'payload' {
    'tx': 'tx_2C9es4FjJF3MtD1M3Np7tUzgCk8AE3ARVJe94Sxmh63feCNt2CekXvjLhBPS2i8pQ8JKGQfgzMQnvfntEdYmMYo7D1UP59UUQ31Bss5G1gz8sPhzmrx1cXCawF9eB27gjYVhTnaLXwUEqdJfHqfATuwLqJtc1p'}
}
```
The depositor is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'deposit_tx',
 'payload': {
    'tx': 'tx_i2WsEQsiC5XsnyKgLeXGW6b9ys87yoQzNB65csymQbK9AsuWApenk9ViHpzxb2oJwUCGiqzA1Cc1D6pJAjkLcQ6w3m8Bhvt41HSqtpSpEd1MciHMcFg1xsZG9CsPu1NUBey9EupgXFJtZ4caNMXcV4evV7ocBjzdBcJo5CUMQgapQZ8ajgUrPgfqQTb3Gq8FFCuHHaHytA7fTNik4KAAvyHiEDutXf1VJxXG2oYkpoNTQGuriV3g4Hxrms3r7LD8ko91'
    }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```
{'action': 'info',
 'payload': {'event': 'deposit_created'}
 }
```
Then the acknowledger receives a new message containing the deposit
transaction for confirmation:
```
{'action': 'sign',
 'tag': 'deposit_ack',
 'payload' {
    'tx': 'tx_2C9es4FjJF3MtD1M3Np7tUzgCk8AE3ARVJe94Sxmh63feCNt2CekXvjLhBPS2i8pQ8JKGQfgzMQnvfntEdYmMYo7D1UP59UUQ31Bss5G1gz8sPhzmrx1cXCawF9eB27gjYVhTnaLXwUEqdJfHqfATuwLqJtc1p'
    }
}
```
Note that this is the same transaction as the one that the depositor had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'deposit_ack',
 'payload': {
    'tx': 'tx_2WsEQsiC5Xso1aHppqY8EwniUa9demV2SAdrNckji4H5ZRDnakiMPAWRv4SSksecqXBCriNTTFg6c3dXK9TzmRV7DoqkKH68Vh7XbVGS7g9CQfaj46S8wgsFBdJtoBMnHV3xbbzSz36cMAAN3eosKaA74TMkgXWgrDCD619RnmskuyvArGbgy6fMFqSniG1s9a3WoTMLoFyw6ucpxgS523Dk3SQEbPAxznbL9KsBEjsCroe4HBVZZG5bX3LU8ZX9PUy'
  }
}
```

#### Finish deposit
After both parties had signed the deposit transaction, the transaction is posted on-chain and
both parties receive it:
```
{'action': 'on_chain_tx',
 'payload': {'tx': 'tx_3cDMp6242sBycND2FPT2jcDWFceRgA7zL3ckU8VzLQdvf2Uqjx5CKkjMXbYrmYjMnLnDihVTrF2fCLqNG93BTAsCNWT6QiJwdmXrTXLQ2d2d7rAc5bYepTC2w3LyrZ37jhx3dN7ATusjXtSu6jw9N8exaPxnjKD3twye5B6bdqbZEHKXXtqStUmaTmUDofEWtGaUCxTWKCboMH7T2mxEjzxgpaH2fbHRxA3GmxaTaKWoTfbnvqragH9QVo6QxiCRAGNUEkbRbPw8m1qPUKjVFWWQSZ9VcCdXte3DitS3anXv7jtTKAA7uuj5pbdG4qi64dDLTd52sSQP6JZpzMxa6oyJTDo5s'
            }
}
```
They are both to compute the transaction hash. Using it,
participants can track its progress on the chain: entering the mempool, block
inclusion and a number of confirmations.

After the `minimum_depth` block confirmations each participant is informed
for the deposit progress on-chain by one's own node:
```
{'action': 'info',
 'payload': {'event': 'own_deposit_locked'}
 }
```
An update from one's own node that the other party had confirmed that the block
height needed is reached:
```
{'action': 'info',
 'payload': {'event': 'deposit_locked'}
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
```
{'action': 'withdraw',
 'payload': {
    'amount': 2
    }
 }
```

##### Withdrawer signs updated state
The withdrawer receives a message containing the updated channel state as a
`channel_withdraw_tx` transaction
```
{'action': 'sign',
 'tag': 'withdraw_tx',
 'payload' {
    'tx': 'tx_2C9estKT2f86WwC7LCa18cDTTmMCrXM7N2AcrXKmgnTo9DNchXjNmewbgNX2YW4RYk8iHkVRnPpeYLRgh6xH96mHNxCMW4aUL2hgTe6iqdrKyM5eqMbCN9YgTdDvUzDyASJwoicxXb7UeDF5kFWvsEMxXBKGX2'}
}
```
The withdrawer is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'withdraw_tx',
 'payload': {
    'tx': 'tx_2WsEQsiC5Xsn85g88TmLYonFu2r8HT53jQPJ7f6Ai9uvnZGwnExRyJ51nHS2mU4g2FUTf2PHUsgs22X5Nwg1E1Zy8ofuoJAttqhXpySyYJhCwdWXYKF6bapSXCLwQoKJ9bWLYYZqudsiPfwv43ekzgJHtaWozzFjrEq835B7Xbd8LSd4znVh2FRWfAPW1Zvsm6nKjN2NfEPndwbps7zgqvbQYeKngwFk952CLtDEpGfXXiS5pUp5ExYTwsxGE4E6LKV'
    }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```
{'action': 'info',
 'payload': {'event': 'withdraw_created'}
 }
```
Then the acknowledger receives a new message containing the withdraw
transaction for confirmation:
```
{'action': 'sign',
 'tag': 'withdraw_ack',
 'payload' {
    'tx': 'tx_2C9estKT2f86WwC7LCa18cDTTmMCrXM7N2AcrXKmgnTo9DNchXjNmewbgNX2YW4RYk8iHkVRnPpeYLRgh6xH96mHNxCMW4aUL2hgTe6iqdrKyM5eqMbCN9YgTdDvUzDyASJwoicxXb7UeDF5kFWvsEMxXBKGX2'}
    }
}
```
Note that this is the same transaction as the one that the withdrawer has already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'withdraw_ack',
 'payload': {
    'tx': 'tx_2WsEQsiC5XsmkQF6BS1aUhB55XkktxRJi2ZWbpCbGVHgQNPQzUeaEJk57RrhWBagGqNUyUA9YY6PrZhTiXcYs6dK1BxASu8EummTYvfpTjfnA8hU21pw6Ms9fWbJbhBbLNai4hLGPEJZ12r1UHqxLTnq6nJ69vw6szeisRzVJ3XYNpvGgSR5dVyW7Yd2VvtW5CGEMCXCHVYquD8gt6RMBDDr1Q6LeLUTomBpgFGQknjKv56tLtZ2FHkWWa9mU22jXMS'
  }
}
```

#### Finish withdrawal
After both the parties had signed the withdraw transaction, the transaction is posted on-chain and
both parties receive it:
```
{'action': 'on_chain_tx',
 'payload': {'tx': 'tx_3cDMp6242sByJUzkqj5qREcZdMg99K3hYXtj8LTJrYvFEcd2FUa4CNfUzhnUQDkzaeeexK1ejuYPMJDD5bwjuGibBYLE1AYPPncdzwe9dHhATA2ftRgouyUxztZoQKQ1jNCDUpgkWcYPiBBRfSUJhoGGLzTfMHrfU5UiiMkcCkv6CmSWEm8JsiGAciJFJzzsRQyCJTZ6a6JM7ztBikcs9sQsG6crEdfnMwjG3zEowFT4wpaYZAxH849Y7m3c3pQkkABtcAkXznZEmtS89H9GWaecxKWkaAipz6WvCKAu33haGb4SM3apigLUYZc6xa2KyTJ8CutCKYWP8Jacua6z8B4hg4qM4'
            }
}
```
They are both to compute the transaction hash. Using it,
participants can track its progress on the chain: entering the mempool, block
inclusion and a number of confirmations.

After the `minimum_depth` block confirmations each participant is informed
for the withdraw progress on-chain by one's own node:
```
{'action': 'info',
 'payload': {'event': 'own_withdraw_locked'}
 }
```
An update from one's own node that the other party had confirmed that the block
height needed is reached:
```
{'action': 'info',
 'payload': {'event': 'withdraw_locked'}
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
```
{'action': 'get',
 'tag': 'balances'
 'payload': {
    'accounts': ['ak_Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
                 'ak_V6an1xhec1xVaAhLuak7QoEbi6t7w5hEtYWp9bMKaJ19i6A9E']
  }
}
```

The `accounts` section of the payload contains a list of addresses to fetch
balances of. Those can be either account balances or a contract ones, encoded
as an account addresses.

A response of this call looks like
```
{'action': 'get',
 'tag': 'balances'
 'payload': [
    {'account': 'ak_Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
     'balance': 700},
    {'account': 'ak_V6an1xhec1xVaAhLuak7QoEbi6t7w5hEtYWp9bMKaJ19i6A9E',
     'balance': 400}
  ]
}
```

If a certain account address had not being found in the state tree - it is simply
skipped in the response.

#### Get proof of inclusion
In order to build and use different services, one might need to provide a third party
a minimal view of the internal channel's state.

In order to fetch a proof of inclusion from the latest modified state tree,
a participant sends a WebSocket message
```
{'action': 'get',
 'tag': 'poi'
 'payload': {
    'accounts': ['ak_Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
                 'ak_V6an1xhec1xVaAhLuak7QoEbi6t7w5hEtYWp9bMKaJ19i6A9E'],
    'contracts': ['ct_2dCUAWYZdrWfACz3a2faJeKVTVrfDYxCQHCqAt5zM15f3u2UfA']
  }
}
```

The `accounts` section of the payload contains a list of addresses to include in the
proof of inclusion. Almost the same goes with the contract addesses listed in `contracts` section:
the only difference being that contract's accounts will be automatically be added
to proof of inclusion as well as their state.

A response of this call looks like
```
{'action': 'get',
 'tag': 'balances'
 'payload': {
    'poi': 'pi_g1JxqVQDQdvjvekeM8hEnVeMFUgfF7YYNjjtrvir7q5tAKq2hFVdtvQo7q4p5Aix1S5XNvKabjEwQVvYVezmnq9VWYoJcmctc5mAu6xVj7KgDk3aG5E7topuuLPXEyGP6hAzRPbr2KzQrQ7KZvTdH15bY1WW7D7XGBRmuiDgYiDj8MAVVjqRFnBS5C6GgevgCkUpKX2tyQL7Y3svSNwDiGxV1b3G6xMbhDeStzgtZ9SrsCaLArP1g9wCDJkChEDXneCmMcvEv2acGwsmXHPfT1uy8oSTVny8tbivnnET7XVdjPJZWuvFbwGAmywa4fRF7wkzn4FQjasLo24DRS5fGYg7Z3uwnFbt4U8sn6yg4FvUBUweW28qMjFRAqVJPH6JKU6o8kZjgRjXsC2L7fbhRkYboecoft11FkFuFXdPjsCj3XGXWtTTAXihPooyTpbjp9yszXZqVxLZ7ms7zc6qtPS8Arq8yTf7UmManvhpYKreDMUqPLtkbUTy32LmeRGBUdhhCzUSg49EHtRo5ti8SCrARQt11ScBJnytnok4o3WvmNVq7SRcWPQgH3ABa8g9csirhcZcrx4f2LQoJwQ2VRnkZUUuxDPNEGRwprVWeCU7KfB3CU86z1eHDQWLnodaxLLJnM1fvpdbrjknRcTSTUjPR7rHcsWVmtkNTVqajCZJKUZN2izAAq5qnQUZwkgFLokynCkMGnkV4woi8j4YKusqXUGZ9w5iFfFsSRjw7brqEBySpQa3QayBBmqKu5CF3pTvikRyGhigCDhmyB3QUQ9SQNr2e4r91hoJmfLXN9o1mkW5ndCuVkKoJjSqiscshpZnvUWVKhQZoHEacdZM5z6U42DfqEVDUR6ptokdNpkJtQtuKo1YD1SyhXgvoHh2d2QCpR29wgRkUKswEDru4sFMRaaxk4uL2MpJg3XaAFhxv6WeKeELCGuYRn9yFnhT9pntUkoFWSghcBkk73uN8sYGo9EkDFkV59Gyrra2hm8Dj7iSUUMqJSMApssN8dWzL9HhC5Hb12mFy8ZzAw1jdYmEYXSmjP859A8cKdP6StwwjuhLacfqv7BkFsQX6Rg4w3ykjRPF2Aj2cf4rTMsNnU4bKFmGYc5RPctTx5pj6PchPyX8GgXMf7EfedQNv7rtT8pCLZ199MRCnPy1X3HURAb8PE9Mj8aZz21N8FDU3nT2XraYKE4DBfnwPnqTV6YNcUVk7AYbJ42BZ2AhTwtZzDovZ3FhK6RvjvUtU4MBPcbYFnidFeqNHq3uM1UeWyaHZJwRoQiptojxCPaDLr7gfNb4jUYRihbbczgNgWwbBsahC75rJWUn7C3dSzJYBY5BbRtgAUivU7tQAhE1SCZ79RDsHwo9Md6iFdX1W1YRB3U9b4gi2NN3HfH4dnA7ediYgB1r9eNGh8mw8SYXSruHFLV59LkSRyR9rFeTCUSTt418fNZAftdbqWhd1UceLZhB3QsdKA8UmSKZcjx1q8ZF83m5zDDgJnkkpiqoHRpZ5pzogPWR8HiJpaDUySD1D8yGgMuGbfsxLhrBm9oDqB1QDqKEWgtsBgu5ZYNob7DqY9cwmsfKnssuNofMG3MqpsYe28ZwEAGfVi1wm87QkSNqyCHYUa3yQ7woeR4ZvQwWJPF3GcXKpBhjVuJusE'
  }
}
```

If a certain address of an account or a contract is not found in the state tree -
the response is an error.

#### Dry-run a contract
In order to get the result of a potential contract call, one might need to
dry-run a contract call. It takes the exact same arguments as a call would and
returns the `call` object.

```
{'action': 'dry_run',
 'tag': 'call_contract',
 'payload' :{
      'contract': 'ct_9sRA9AVE4BYTAkh5RNfJYmwQe1NZ4MErasQLXZkFWG43TPBqa',
      'abi_version': 1,
      'amount': 0,
      'call_data': 'cb_1111111111111111111111111111111yC4CoPDhKfwheTUFxWaEmAud5DzXdDtnFd3Pdr7SkLrw9ze6ZF21i8tR8VyUz4zLwTwBhFi3dCvp4fSTk38mdQ2ov8GPqznR3G83irbxNjrHkfS9nQDcRnFEZ17EfeXqBgB5Q6k6H3JLjPns3ZGECU3rf9gzbbFmwxJbMFsjK2vhxRBmpXoaq4RUqAEu5KZ8xfuCHG17vJn33UmvtayzkJvYTUYQcprT2'
    },
}
```

The `payload` is an mirror image of the [call contract
update](#trigger-a-contract-call-update), the only difference being that the
dry-run does not impact the state and it does not need signing. The call is
executed in the channel's state but it does not impact the state whatsoever.
It uses as an environment the latest channel's state and the current top of
the blockchain as seen by the node.

A response to this call looks like
```
{'action': 'dry_run',
 'tag': 'call_contract'
 'payload': {
    'channel_id': 'ch_t6X88VVTiXwRzdpW1UMkgqihsoJu7aTswUaw5grrqUd3NWg1m',
    'data': {
        'caller_id': 'ak_2PYxWHAsK2jYaca2EQBiJwZrgxJf6AzebE96ZVe2NwGtjaCdvs',
        'caller_nonce': 8,
        'contract_id': 'ct_2GPzqsJ7quu1xqnYBedwvn7SQ3DEaQf1BKNyf5ZpAB7yZ4uWAk',
        'gas_price': 1,
        'gas_used': 192,
        'height': 8,
        'log': [],
        'return_type': 'ok',
        'return_value': 'cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY'
        }
  }
}
```

#### Get contract calls
Each participant persists contract call results locally. It is not required of
both participants to share the same list of contract calls as this does not
impact consensus between them. Any participant can prune his local set of
calls in order to free some memory. In order to inspect the result value of a
contract call, a participant sends a WebSocket message
```
{'action': 'get',
 'tag': 'contract_call',
 'payload': {'caller': 'ak_Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
             'contract': 'ct_2qSaJ7pe3MTdPpzS69ZdtQsVTPSoj7yyYL2KJLxKQoAAHJQdjq',
             'round': 11
  }
}
```
The combination of a `caller`, `contract` and a `round` of execution determines the
contract call. Providing an incorrect set of those results in an error response.

A non-error response of this call looks like this

```
{'action': 'get',
 'tag': 'contract_call',
 'payload': {
    'caller_address': 'ak_Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
    'caller_nonce': 11,
    'contract_address': 'ct_2qSaJ7pe3MTdPpzS69ZdtQsVTPSoj7yyYL2KJLxKQoAAHJQdjq',
    'gas_price': 0,
    'gas_used': 561,
    'height': 11,
    'return_type': 'ok',
    'return_value': 'cb_11111111111111111111111111111113Un1fbh'
  }
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

```
{'action': 'clean_contract_calls'}
```

Once calls are pruned, the same participant receives the following message:
```
{'action': 'calls_pruned'}
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
