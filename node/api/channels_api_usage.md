[back](./README.md)
# Channels - intended usage

## Important

With introduction of GAs, all on-chain state channel transactions
are to be signed using the on-chain account's authentication method and
off-chain transactions are to be signed using the accounts' authentication
method at channel creation time. You can read more about it
[here](../../channels/authentication.md).

## Introduction
You interact with an Aeternity node both through HTTP requests and WebSocket
connections.
To learn more about channels and their life cycle see [the doc](/channels/README.md).

In each channel there are two WebSocket client parties. For each channel, a
new WebSocket connection is opened. Once the channel is opened - participants
are equal in every regard. They have different roles while opening and we have
names for them - `initiator` and `responder`. For short we will call them _the
parties_.

There are two basic types of interaction: persisted connection events and HTTP
API calls.

Although no off-chain transactions consume gas or require any fees, all
on-chain transactions come with a fee. The value of the fee can be set by the
client that initiates the action, ex. a deposit. The FSM could also calculate
it for the client: it will multiply the minimum gas required for the
transaction by the gas price. The gas price could optionally be specified by
the client. If not - the node's setting for `min_miner_gas_price` is used instead.
Note that relying on the `min_miner_gas_price` could result in the fee being
either too low or too high according to dynamically changing miner
expectations for the gas price.  If both a `fee` and a `gas_price` are
provided, then the FSM computes the fee for the client according to the gas
requirements and `gas_price`. The actual fee being used for the transaction is
the larger value between the computed fee using provided `gas_price`and the
provided `fee`.

All on-chain transactions require a replay-attack protection. This could be
either embedded in the transaction itself or implemented in a smart contract
in the case of a Generalized Account. In the latter case the `nonce` in the
transaction is always `0`. In the case of a basic account, though, there must
be a valid `nonce` or the on-chain transaction will not be included in the
blockchain. In all APIs that produce on-chain transaction, there is an
optional parameter `nonce` for the client to specify the value to be used. If
this is not provided, the FSM will do its best defining what that value should
be. It checks all pending transactions for that account, takes the highest
nonce from them and uses it to base the next nonce. If there are no pending
transactions, the account's nonce is used instead. Note that relying on
pending transactions could significantly slow down the channel transaction
inclusion or even render it invalid.

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
  * [Channel slash](#channel-slash)
  * [Channel settle](#channel-settle)
5. [Optionally snapshot](#channel-snapshot)
6. [Optionally force progress](#force-progress)

There are a some WebSocket events that can occur while the connection is open
but are not necessarily part of the channel's life cycle.

* [Open error](#open-error)

* [Timeout error](#timeout-error)

* [Update error](#update-error)

* [Update conflict](#update-conflict)

* [Abort update](#abort-update)

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

### On-chain requests
There are two types of requests:
* Total amount-modifying ones - [deposit](#deposit-transaction) and [withdrawal](#withdraw-transaction)
* [Channel-closing ones](#solo-closing-sequence) - [solo close](#solo-close-on-chain-transaction), [slash](#slash-on-chain-transaction) and [settle](#settle-on-chain-transaction)

### Pinned environment

While on-chain consensus is reached between miners, in off-chain world we
don't have those. State channels are two-party systems that are closer to
proof-of-stake solutions where both participants have equal
stake in the channel, no matter their balances. The channel can make another
step forward only if both parties agree upon the new state or it is produced
via a force progress transaction on-chain that had been based upon a previous
mutually agreed state. This makes channels both trustless and egalitarian.

This trustless model is based upon both participants executing off-chain
updates locally and reaching the same results. This is how consensus is
reached between them. Since off-chain smart contracts can read on-chain
objects like accounts, names, contracts and oracles requests and responses,
the results of their execution rely heavily on the chain environment they are
based on.

Participants are expected to use their own nodes to support their channels.
At the moment using a service hosted by a third party is trustful, thus
potentially undesirable. This leads to both participant's nodes being peers in
a system with an eventual consistency - due to network constraints and forks
both participants can have a different view of the chain.

The combination of participants having different views on the chain and the
off-chain consensus being dependent on it could lead to a fragile system with
a lot of mismatching state hashes of off-chain updates. In order to improve
this there is an optional functionality of setting `block_hash` that defines
the on-chain environment that the update is to be executed in. We call this
shared view of the chain _a pinnned environment_. When a participant wants to
start a new round of updates, one can optionally specify a pinned environment
to execute in. This is how the participant communicates to the other party
what one considers to be a block hash that is safe enough to base an off-chain
update upon. The other party might decide if the block hash is too old or too
new depending on their local view of the chain. If the specified pinned
environment does not meet the expectations, the whole update is rejected as
invalid.

An update might not be pinned to any environment. In that case a placeholder
value for the blockhash is provided:
`"kh_11111111111111111111111111111111273Yts"` or
`"mh_11111111111111111111111111111111273Yts"`. In this case both participants
use whatever they see to be the latest top block.

The `block_hash` is an optional argument to all mutual offchain transactions. If it is
not explicitly provided by the requester, a suitable value is picked for the
client by their FSM.

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
will describe these in groups which indicate their relation to each other.

#### Channel establishing parameters

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
  | fee | integer | the fee to be used for the channel open transaction | No | No | Yes |
  | gas_price | integer | the gas_price to be used for the fee computation of the channel open transaction | No | No | Yes |

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

#### Channel timeout values

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

#### Channel block hash delta values

  A client can specify what is considered by them to be a valid block hash.
  Those are defined as deltas according to the latest chain top as seen from
  the participant's node. A delta of `0` is the latest top, a delta of `1` is
  the previous generation, etc. Each participant can set a delta which defines
  a range of accepted heights according to the current top. If the other
  participant makes an off-chain update based on a hash which refers to a
  block belonging to a generation outside of this range - it will be rejected
  as it would be considered unsafe.

  Additionally to the delta range check for incoming updates, the FSM also can
  pick a correct block hash for the client. This happens when the client
  starts a new update round and a block hash is not specified by the client.
  Then the FSM checks what is the newest allowed block hash according to the
  range. An additional pick offset can be provided for even greater fork
  safety.

  | Name | Description | Default value |
  | ---- | ----------- | ------------- |
  | bh_delta_not_newer_than | height delta to be allowed as the newest possible relative to local top | 0 |
  | bh_delta_not_older_than | height delta to be allowed as the oldest possible relative to local top | 10 |
  | bh_delta_pick | the offset according to `bh_delta_not_newer_than` to use when picking a block hash for the client | 0 |

  Restrictions on them are that:
  * `bh_delta_not_newer_than >= 0`
  * `bh_delta_not_newer_than + bh_delta_pick >= bh_delta_not_older_than`
  * if one is set, the other one must also be set

  If any of the checks fails, the defaults are used instead.

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

### Initial connection indication

Each client receives an `fsm_up` event indicating that a connection has been
established. Each fsm reveals a unique token which is needed for authentication
if the client needs to reconnect later. Note that the tokens are unique to each
respective client.


```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_14XZqoUZUc9U6RUbvN2iWd+dd5H9xIWYDUyjk6L3NE2MZV2P"
    }
  },
  "version": 1
}
```

Note that the channel ID has not yet been created.


### Connection opened messages
Parties' WebSocket clients receive messages for the opening of the TCP
connection.

#### Responder connection opened message
The responder receives the following message, indicating that the protocol
message `channel_open` has been received by the responder FSM.

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

#### Initiator connection opened message
The initiator receives the following message indicating that the
responder FSM replied with a valid `channel_accept` message.

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


### Create transaction authentication
The `channel_create_tx` is sent subsequently to both parties and they mutually
authenticate it. Then it is posted to the chain.

#### Initiator authenticates the tx
The initiator receives a message containing the unauthenticated transaction.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g...",
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
  "id": -576460752303423488,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCu..."
  }
}
```

#### Responder is informed
The responder receives the following message indicating that a valid
`funding_created` protocol message has been received.
The on-chain `channel_id` and `fsm_id` are included, and the client
can use them to reconnect, once it has responded to the signing request.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
    "data": {
      "fsm_id": "ba_M4vTq7zj3l7rRWj56Lyl60P4v6HYM7pbq1OEMXRAIkHrCXJQ",
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### Responder authenticates the tx
After being informed for the initiator's authentication, the responder receives a
message containing the solo-authenticated transaction to be co-authenticated by her
as well.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
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
  "id": -576460752303423487,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4h..."
  }
}
```

#### Initiator is informed
The initiator receives the following message, indicating that the FSM
has received a co-signed `create_tx` object. Since this is the first
report to the initiator where the on-chain channel ID is guaranteed to
be known, the `fsm_id` is also included for convenience.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_14XZqoUZUc9U6RUbvN2iWd+dd5H9xIWYDUyjk6L3NE2MZV2P"
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
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4h...",
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
Once the transaction is picked up by a miner and included in a block, the FSMs will detect it and report
a `channel_changed` event in an `on_chain_tx` report:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4h...",
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
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
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
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
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
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

From this point on, the channel is considered to be opened.

#### State changed
Each time the FSM returns to the `open` state, it will check whether the channel off-chain state has
changed. If so, it issues a `channels.update` report. When the channel is first opened, this report will
present the initial off-chain state:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
    "data": {
      "state": "tx_+QENCwH4h..."
    }
  },
  "version": 1
}
```

### Client reconnect
Once the `channel_create_tx` has been signed, the client Websocket connection may close
without causing the FSM to terminate. The client can reconnect using the
[`reestablish`](#reestablish) method described below.

The node will try to locate the FSM using these parameters and reconnect.
The FSM will check the `fsm_id` token for authentication. If the FSM is not
running, a full reestablish is attempted.

Although it is possible to disconnect and reconnect once the signing request has been
answered, the initiator FSM is not guaranteed to know the channel ID at the time of
sending the initial signing request. If the initiator is a Generalized Account, the
channel ID depends in part on the initiator authentication. The initiator client
could derive the channel ID from its authenticated `channel_create_tx`, but
otherwise, it will be informed of the channel ID and (again) the FSM ID in the
later `funding_signed` message, once the responder client has also authenticated
the `channel_create_tx`. The responder receives the channel and FSM IDs in the
`funding_created` report, and can use them to reconnect after signing the
`channel_create_tx`.

The initiator opens a new WebSocket connection, passing the existing channel and FSM IDs.

```
$ wscat 'localhost:3014/channel?existing_channel_id=ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL&existing_fsm_id=ba_14XZqoUZUc9U6RUbvN2iWd%2Bdd5H9xIWYDUyjk6L3NE2MZV2P&host=localhost&port=13179&protocol=json-rpc&role=initiator'

connected (press CTRL+C to quit)
```

In response to a reconnect/reestablish, the client will always receive an `fsm_up`
indication with a new `fsm_id` needed for the next reconnect/reestablish.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_KrnFPd2vqBEFeYupgCxXLWMqtDFwzSCyar9v7U6YHdNC7QzcL",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_h2NTyK/L2OAXhJnl/sodLTWmZ3g262T4lFTPTwlz84JZswRW"
    }
  },
  "version": 1
}
```


While the client is disconnected, the corresponding FSM will reject any
protocol request that requires signing. An attempt to reconnect to an FSM that
already has a client connected will be rejected. Note, however, that if e.g.
an update request already includes the authentication of the disconnected
client, the operation is allowed, and the responding FSM proceeds as if it had
issued an authentication request and received a successful reply.

#### Example

Assuming that the channel has been set up, and the `initiator` and `responder` both have
received corresponding `channels.update` messages:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "state": "tx_+QENCwH4h..."
    }
  },
  "version": 1
}
```

If the `initiator` client now disconnects, its FSM will keep running.

If the `responder` now initiates an update request, the `initiator` FSM
will respond with a `conflict` error.

```
#### responder ---> node
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
    "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
  }
}

#### responder <--- node
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvFUHNvTaJmM0h7WZRyILi7R5xEube4cPidh39qA4rZ3AqA1OxWEaCmQrMsRAz/aOqULrCfnjvXy3CsSqurneRAweq1oQ2o=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
          "op": "OffChainTransfer",
          "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
        }
      ]
    }
  },
  "version": 1
}

#### responder ---> node
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC9qolUALwHM2t73ZWgLujcu2EPv3IWOBll9bmMb0WIJcCqHnz/ZBf3VHxlPWb/VWCY9wp/Z4MOoqqtiLwpApEGuEj4RjkCoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2dwKgNTsVhGgpkKzLEQM/2jqlC6wn54718twrEqrq53kQMHpotH/U"
  }
}

#### responder <--- node
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
      "round": 1
    }
  },
  "version": 1
}
```

If, on the other hand, the `responder` FSM manages to get `initiator` to
co-authenticate the initial request (e.g. optically by exchanging QR codes),
the `initiator` FSM will detect the existence of its client's authentication,
and will acknowledge the request.

```
#### responder ---> node
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
    "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
  }
}

#### responder <--- node
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvFUHNvTaJmM0h7WZRyILi7R5xEube4cPidh39qA4rZ3AqA1OxWEaCmQrMsRAz/aOqULrCfnjvXy3CsSqurneRAweq1oQ2o=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
          "op": "OffChainTransfer",
          "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
        }
      ]
    }
  },
  "version": 1
}

#### responder ---> node
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB2kYkTBh9xELqllJZzHMFcj9oysyo4t6sBbxWI1tm2LZmkh9liZbwHyzNADWjj9FywzWpVceUfiVWhXfwHXFIFuEC9qolUALwHM2t73ZWgLujcu2EPv3IWOBll9bmMb0WIJcCqHnz/ZBf3VHxlPWb/VWCY9wp/Z4MOoqqtiLwpApEGuEj4RjkCoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2dwKgNTsVhGgpkKzLEQM/2jqlC6wn54718twrEqrq53kQMHqW0FMw"
  }
}

#### responder <--- node
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "state": "tx_+NILAfiEuEB2kYkTBh9xELqllJZzHMFcj9oysyo4t6sBbxWI1tm2LZmkh9liZbwHyzNADWjj9FywzWpVceUfiVWhXfwHXFIFuEC9qolUALwHM2t73ZWgLujcu2EPv3IWOBll9bmMb0WIJcCqHnz/ZBf3VHxlPWb/VWCY9wp/Z4MOoqqtiLwpApEGuEj4RjkCoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2dwKgNTsVhGgpkKzLEQM/2jqlC6wn54718twrEqrq53kQMHqW0FMw"
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

### Meta-information
Update requests that modify the off-chain state can be optionally annotated with
`meta` information objects. The parameter `"meta": [ string() ]` may be added, and each
meta information object can be an arbitrary string. Operations that support this are
transfer (`update.new`), `deposit`, `withdrawal`, `new_contract` and `call_contract`.
Meta information does not get included in on-chain transactions, nor does it affect the
state hash. It can be used to convey useful application-level information to the other
party in the channel.

Example:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
    "meta": [
      "meta 1"
    ],
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

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

The FSM responds:

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
      "signed_tx": "tx_+EY5AqEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02ICoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhVgB6xw==",
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

The FSM responds:

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
a leave request, the channel FSM passes it on to the peer FSM, reports the
current mutually authenticated state and then terminates. The `'reestablish'` request
is very similar to a [Channel open](#channel-open) request, but also requires
the channel id and the latest mutually authenticated state. For authentication,
a unique token called an `fsm_id` also needs to be provided
See [initial connection indication](#initial-connection-indication) on how the
`fsm_id` is communicated.

The full state, including state trees, is cached in encrypted form internally
by the Aeternity node, and upon reestablish, it is verified that the encoded
state provided by the client corresponds to the latest full state retrieved from
the cache.

### Leave request
Example:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

The FSM responds with the following type of report:
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
Open the channel in a similar way as in the
[Initiator WebSocket open](#initiator-websocket-open) example,
providing the parameters `existing_channel_id` and `fsm_id` with values matching
the ones provided in previous signing requests and reports (note that the latest
unique `fsm_id` must be used.)

```
$ wscat --connect localhost:3014/channel?existing_channel_id=ch_qbM3mAio9VyqU3GLhjWmdcg3H5gbrTJhaMYCokik7CbeHghWS&existing_fsm_id=ba_RtzmxPbVqyDrXjPcY3OP%2FU2YdlpWonF%2BcVIEYEH01%2BFQ1AI7&port=13180&protocol=json-rpc&role=responder
```

The channel FSM responds with the following event reports if all goes well:

An `fsm_up` event indicating that the FSM is running, and a new `fsm_id`
has been created:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_qbM3mAio9VyqU3GLhjWmdcg3H5gbrTJhaMYCokik7CbeHghWS",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_gvH8dUxre/htCqdWWxJS6YkBBx4l5Q41noArQf35tCDsB7ZO"
    }
  },
  "version": 1
}
```

A report indicating that the `reestablish` handshake succeeded:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_qbM3mAio9VyqU3GLhjWmdcg3H5gbrTJhaMYCokik7CbeHghWS",
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
    "channel_id": "ch_qbM3mAio9VyqU3GLhjWmdcg3H5gbrTJhaMYCokik7CbeHghWS",
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
    "channel_id": "ch_qbM3mAio9VyqU3GLhjWmdcg3H5gbrTJhaMYCokik7CbeHghWS",
    "data": {
      "state": "tx_+QENCwH4hLhAGi4f1QWVwvBlk2kk+CN3ELiNe6Own36tLwarvqpo2brJlkYdX0gj1VB4B/eqFcYfDWSo1AMsJ0oKQy3AWt/QCrhAPuqasfg0X10mndNxgG75y2QxUm//mYT13c1vp5aSJYX4+xTYfBV8SxZD36M9rNBx1/9/CAfUL4YYdg3GX5JmAbiD+IEyAaEBE7TIKkriBfmYFubsoRmC9dCOrNzIF2Uou0YIXPBsLoGGP6olImAAoQEJFbpig3RT+UOpwl8CyzLXDoK0biVPpJ6fhnl+trcT3IYkYTnKgAACCgCGEAZ510gAwKB9oftkV6lyU0PDMM7T0DutPgGd6CZ2st1XJiEM6z01rhXYqWnL"
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
  | gas_price | integer | the gas_price to be used for the fee computation |
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
      "tx": "tx_+KcLAfhCuE...",
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
disconnected and is expected never to return. The channel FSM can be asked
to generate a `channel_close_solo_tx` transaction and post it on-chain. The
resulting transaction will include the latest mutually signed offchain state,
or the empty string, indicating that the latest state is what's on the chain.

The `channel_close_solo_tx` transaction only needs a single authentication, and
is described in more detail in [this section](#channel-solo-close).

The channel FSM does not support picking an earlier state to close with, as
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
      "signed_tx": "tx_+QGfNgGhBnHSbcHwBwtR5QRwS0O1mI1Gw/8pkaOwcHQap09BPoMFoQGxtXe80yfL
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
    "signed_tx": "tx_+QHrCwH4QrhACuHMgbcTg1inUPAUSmhXfODKWI2CFchqpav9VDaBlw+xng9Ld0eLPgysTvks47iVHn4d/11VlkEi6iLRBDkIBLkBovkBnzYBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aAuQFM+QFJPAH5AT/5ATygHqEViX8Pa+/jHEEB3cCzerUv2qm0FMJvIiWFzCDnJ3H5ARj4dKAeoRWJfw9r7+McQQHdwLN6tS/aqbQUwm8iJYXMIOcncfhRgICAgICAoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJgICAgKBCZn4DcKzHmLBQE0w6UPmPWmznB0eilL8OaPS3UoSbFICAgICA+E+gQmZ+A3Csx5iwUBNMOlD5j1ps5wdHopS/Dmj0t1KEmxTtoDG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmi8oKAQCGP6olIl//+E+g7QIWPGJsh916G7zCAZpUeaRQuGVamwjR8JaxQKEPIwntoDccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6Ei8oKAQCGJGE5yoABwMDAwMAAhhtI61fgAAiybuMt"
  }
}
```

As the channel FSM receives the authenticated solo close transaction, verifies it
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

## Channel slash

If a `channel_close_solo_tx` passes on-chain checks, it is valid to the best
of the miner's knowledge. The channel is to be closed and the final balances
participants receive from its closure are according to whatever state had
been provided last on-chain.

The state given by the `channel_solo_close_tx` can be progressed using a channel force progress
transaction. Each new `channel_force_progress_tx` transaction will result in a
new channel state that is produced on-chain. It will have a new `state_hash`
and an incremented `round`.

On the other hand the `channel_close_solo_tx` could have been both valid and
malicious at the same time: it could have passed all on-chain checks but yet
it might not have been the very last channel state. If any participant tries
to close the channel unilaterally using a `channel_close_solo_tx` based upon
an earlier (i.e. not the latest) channel state, we would consider that a violation of the
off-chain protocol. In that case the other participant can defend themselves
from being cheated by simply providing a co-authenticated off-chain state with
a higher round. This is done via the `channel_slash_tx` transaction.

Since a co-authenticated off-chain state has a higher priority than an
unilaterally on-chain produced one via a `channel_force_progress_tx` transaction, 
a `channel_slash_tx` transaction can invalidate a whole chain of
`channel_force_progress_tx` transactions if the first one of them had been based
on a channel state that is older than the one provided by the `channel_slash_tx`
transaction. This way if one party produces a long chain of force-progressed
states based on a not-the-last state, the other can replace them all providing
a single `channel_slash_tx` transaction.

For completeness it is worth mentioning that the second party can be malicious
as well, not providing the very last state in their `channel_slash_tx`
transaction. In that case the closing party could protect themselves with yet
another `channel_slash_tx` transaction that slashes the slash that is now
on-chain as well as all force-progressed states based upon it. Having this
mechanics at place aims at incentivizing both parties to behave well as all
cheating attempts will cost them on-chain fees.

If the other party tries closing the channel with a `channel_close_solo_tx`
that is not based on the latest off-chain state, our FSM informs us about it
(note the `"info": "can_slash"` bit):

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuECR/+7ZaF0OqeiRuRVkjsd2aEynOBmBk+tFETlA5H/jNIVB2A1RbKDe8yHGBWpUbWZzLnPXK+pl1Wkml094WxUAuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcDKgN0",
      "type": "channel_close_solo_tx"
    }
  },
  "version": 1
}
```

As well as this message, the client receives a message that informs them that
the channel has now entered a closing state:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": 
      "event": "closing"
    }
  },
  "version": 1
}
```

#### Slasher initiates slash

The party that had been prompted to slash is to inspect the closing transaction and
decide if it wants to slash. There is the scenario when one would pay more
in on-chain fees compared to what is to be lost if one allows the channel
being closed with some older state. If one decides to slash, one simply sends:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### Slasher authenticating

Then the slasher receives a `channel_slash_tx` to authenticate:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBh+EzGQSDhTgg+o7QcjF6i97RFCMtDrF7COb0FktaFyToQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79LjU+NILAfiEuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuECR/+7ZaF0OqeiRuRVkjsd2aEynOBmBk+tFETlA5H/jNIVB2A1RbKDe8yHGBWpUbWZzLnPXK+pl1Wkml094WxUAuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe5AUz5AUk8AfkBP/kBPKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPkBGPhPoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdG7aAxNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAvh0oGvmwqokQbLZzors5iPcHRBIz1gqqnXYLC7QVygETXaI+FGAgICAgICAgICAgICgbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnGgSpVcv8aLrenfv730hbUAfsRv/8X/Qb24JV73MWUG90aAgID4T6BtgmNs3qIz02SUPW5KbqyjHeKIi0Exdem+rWnYxfJGce2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/7AwMDAwACGGR7ISegAEhFhZsM=",
      "updates">> => []
    }
  },
  "version": 1
}
```

The slasher is to decode the transaction, inspect its contents, authenticate
it, encode it and then post it back via a WebSocket message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAsEn+SKhPLOh7mmKoHpj4+OQZaHnVatjP8PUnwci+Xn5RzA4mR36at5rK/5j5l1FZGieSga4SOTHX1SY4o9huAbkCd/kCdDcBoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhck6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAQjTRxcbv0fsqW7TgoewawPqBawGGB84WU0fAZkzoDtsmCne5V8FO/sZX7w9zLvXRHladU9Wlbh/FD5P+8FPVDLhAkf/u2WhdDqnokbkVZI7HdmhMpzgZgZPrRRE5QOR/4zSFQdgNUWyg3vMhxgVqVG1mcy5z1yvqZdVpJpdPeFsVALhI+EY5AqEGH4TMZBIOFOCD6jtByMXqL3tEUIy0OsXsI5vQWS1oXJMCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhhkeyEnoABJ3oirv\"
  }
}
```

The FSM is to check the contents and the authentication of the transaction and
then post it on-chain from behalf of the slasher. Once the transaction is
included on-chain, the participant will receive a message informing them:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAsEn+SKhPLOh7mmKoHpj4+OQZaHnVatjP8PUnwci+Xn5RzA4mR36at5rK/5j5l1FZGieSga4SOTHX1SY4o9huAbkCd/kCdDcBoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhck6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAQjTRxcbv0fsqW7TgoewawPqBawGGB84WU0fAZkzoDtsmCne5V8FO/sZX7w9zLvXRHladU9Wlbh/FD5P+8FPVDLhAkf/u2WhdDqnokbkVZI7HdmhMpzgZgZPrRRE5QOR/4zSFQdgNUWyg3vMhxgVqVG1mcy5z1yvqZdVpJpdPeFsVALhI+EY5AqEGH4TMZBIOFOCD6jtByMXqL3tEUIy0OsXsI5vQWS1oXJMCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhhkeyEnoABJ3oirv",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

## Channel settle

Once a 'dispute' process has been initiated with a `channel_close_solo_tx`, and
once the lock period has expired, it is possible to finally close the channel
with a `channel_settle_tx` transaction. The channel FSM can assist if asked
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
      "signed_tx": "tx_+F04AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6Ehj+qJSJf/4YkYTnKgAEAhhtI61fgAAIwYkCX",
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
    "signed_tx": "tx_+KcLAfhCuEBdI4Uesh3hYjGQ2BAo0FzD1YPyZlzhy8HyNgf7OzrQdVM44oWQX0yFtmk31HaSLuIJGNDv3hEgdLwe0iZz3LEEuF/4XTgBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGP6olIl//hiRhOcqAAQCGG0jrV+AAAgurGvs="
  }
}
```
As the channel FSM receives the authenticated settle transaction, verifies it
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

Once the FSM has confirmed the transaction to be safely on-chain, the following
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

Note that since it is the `initiator` that pays the `channel_create_tx`
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

Newly requested updates are not always successful. For example one participant
tries to spend more tokens that one currently has in the channel's balance.
Another would be a participant initiating an update while the other
participant had already proposed a different one. This diverges from the
update flow [described above](#channel-off-chain-update).

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

* `Contract init failed` - when the update introduces a new contract to the
  off-chain state trees and the init function fails

* `Not a number` - when an argument that is expected to be a number is not a
  number but rather some other data type, ex. a string

* `Broken encoding: account pubkey` or `Broken encoding: contract pubkey` when
  the update contains a broken encoding of an account or contract pubkey

* `Broken encoding: contract bytearray` - when the provided bytearray has a
  broken encoding

* `Conflict` - when the other participant had already proposed a new update
  and instead of authenticating it or rejecting it, our client initiates
  another update. It fails with this error and then the [update
  conflict](#update-conflict) messages are sent to both participants.

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

#### Abort update

The update flow relies on participants reaching agreement according to
updates. The process of getting there is not changing the channel state and
thus is not part of the off-chain protocol. If needed, clients are expected to
use [generic messages](#generic_messages) to reach consensus around what the
next update shall be.

Even if a proper protocol is in place for reaching an agreement, there might
be a need for aborting an update explicitly. This is only possible while the
FSM is waiting for an authentication by this particular client. Once an update
is authenticated by a client, that client can no longer abort it.

The FSM produces two types of transactions according to how many
authentications are required for them:
* solo authenticated transactions:
  * `channel_close_solo_tx`
  * `channel_slash_tx`
  * `channel_settle_tx`
  * `channel_snapshot_tx`
  * `channel_force_progress_tx`
* mutually authenticated transactions - all the rest

When a client is prompted to authenticate an update, it is expected to either
agree to it with an authentication or to abort it. Depending on the source of
the update, the other FSM might receive a message or not. If it was this
client that triggered the pending update - the other FSM is not aware of it
yet.  In this case no message is sent to the other FSM.  If the other party
started the update and has already authenticated it, our client can still
either authenticate or abort it. If aborted - the FSM will inform the other
party that the update was rejected, sending an abort conflict message.

If the update is aborted, the FSM returns to the last co-authenticated
state and enters an `open` state, waiting for a new update to be initiated.
Since there is no previous stable state before the channel initial
transaction, the `channel_create_tx` can not be aborted. It is the initiator
that produces it so if the responder had different expectations for it, it is
better to close the connection instead. Then it can be reopened with
a different set of opening arguments.

The request for aborting an update is the same, no matter whether or not the pending
update was triggered by the other party.

When there is a pending udpate, waiting for the client to approve, one can
also abort it using the same method one would use for providing the
authenticated transaction. The difference is that one provides an error code
instead.

```javascript
{
   "jsonrpc":"2.0",
   "method":<signing method>,
   "params":{
      "error":147
   }
}
```

The response the client receives in that case is:

```javascript
{ 
   "jsonrpc":"2.0",
   "method":"channels.info",
   "params":{ 
      "channel_id":"ch_95Ya...",
      "data":{ 
         "event":"aborted_update"
      }
   },
   "version":1
}
```

If the client tries sending a abort message when it is not applicable, it
will receive an error response instead:

```javascript
{
   "channel_id":"ch_95Ya...",
   "error":{
      "code":3,
      "data":[
         {
            "code":1018,
            "message":"Not allowed at current channel state"
         }
      ],
      "message":"Rejected",
      "request":{
         "jsonrpc":"2.0",
         "method":"channels.update",
            "params":{
                "error":147
            }
      }
   },
   "id":null,
   "jsonrpc":"2.0",
   "version":1
}
```

If the other party had triggered the aborted update, it is informed with
receiving the following message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id":"ch_95Ya...",
    "data": {
      "channel_id":"ch_95Ya...",
      "error_code": 147,
      "error_msg": "user-defined",
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
  | gas_price | integer | the gas_price to be used for the fee computation |
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
  | gas_price | integer | the gas_price to be used for the fee computation |
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

### Bypassing minimum-depth wait
In some cases, it can be desirable to get started using the channel directly after
having posted a `create_tx`, `deposit_tx` or `withdraw_tx` transaction, rather
than remaining blocked, waiting for the prescribed number of keyblocks. A way to
do this is for the client to call the `channels.assume_minimum_depth` method,
once the `on_chain_tx` event has been received. This will instruct the FSM to proceed
_as if_ the minimum-depth confirmation has already arrived. When the actual confirmation
arrives, it will be reported in a separate message.

#### Example

After opening a channel and producing a co-authenticated `channel_create_tx`,
the client waits for a `channel_changed` info report, signifying that the tx
has appeared on-chain. Normally, this would be followed by the clients waiting
for a desired number of keyblocks.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAAT1wO6X1XimqSjJgXD2tALoWktcOgWBXvAOPDo5Ul2rBfWPOPkC99JQAO7b8KwPSr7ZMOEilhptPNEWYVqLdBLhAxw3skqCjhCvxm4jwDYZRZ8M/f2QDOuj16uaTYJn9Qx1yvqflv8NcN2Ar++LbxXd2U5QCQnzxRIB1TsNDSG5aCbiE+IIyAqEBwTH0kjbcqZ+kfS4/13ElgHQNj5dEpvgNJ435icc0A0aGP6olImAAoQETPZyIkZzGtspz/mXN+8wG21WBqvpLmWG2islKR7Wj/4YkYTnKgAACCgCGEAsh7xAAwMCgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBOeX7Rg==",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```
If a client decides that it doesn't want to wait for final confirmation, it can call
the `channels.assume_minimum_depth` method:

```javascript
{
  "id": -576460752303421693,
  "jsonrpc": "2.0",
  "method": "channels.assume_minimum_depth",
  "params": {
    "tx_hash": "th_2ERU4LEe8Bn8x1iuw9vSh7iHys9t8zwt3Nq2oz5GQj9pAu9pur"
  }
}
```

This will cause the FSM to proceed as if it had received a minimum_depth event,
and send an `own_funding_locked` report.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

Note that since each client independently waits for minimum depth, the channel
activity can proceed only as soon as both clients have either received minimum
depth confirmation, or selected to defer it.

Once the minimum depth event arrives, the FSM will issue a special info report,
annotated with a notice stating that minimum depth was already assumed.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "minimum_depth_achieved",
      "notice": "already_assumed",
      "tx_hash": "th_2ERU4LEe8Bn8x1iuw9vSh7iHys9t8zwt3Nq2oz5GQj9pAu9pur",
      "tx_type": "channel_create_tx"
    }
  },
  "version": 1
}
```

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
dry-run a contract call. It takes the exact same arguments as a call would (including
optional `meta` objects) and returns the `call` object.

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

1. single `channel_solo_close_tx` transaction
2. zero or a couple of `channel_slash_tx` transactions
3. single `channel_settle_tx` transaction

The second step is not required and a `channel_solo_close` could be followed
either by zero, one or more `channel_slash` transactions, each subsequent one
presenting a newer state and overwriting the previous one. Those are settled by
a `channel_settle` transaction that finally closes the channel. Let's discuss
those in detail.

#### Payload and proof of inclusion
The idea behind `channel_solo_close_tx` `channel_slash_tx` and
`channel_settle` is for parties to provide, on-chain, the latest channel
internal state so that the channel can be closed.
First comes the `channel_solo_close_tx` that provides some off-chain state.
Then a `channel_slash_tx` can be posted, but it is checked that it has a newer
state than the `channel_solo_close_tx` one. Then parties can post more
`channel_slash_tx` transactions, but those are always checked to be containing
a newer channel state than the last received on-chain. If one party tries to
cheat by posting some old state - the other party can present to the chain a
newer channel state and this overwrites the previous posted one. Thus the
comparison on channel states is important. This is done by comparing rounds.

Both `channel_solo_close_tx` and `channel_slash_tx` contain a `payload`
field. This is either a binary containing a `channel_offchain` transaction or an
empty binary.

If it is a `channel_offchain_tx` transaction, it must be mutually authenticated.
It also contains a `channel_id`, `round` and `state_hash`.
The `channel_id` in combination with the correct singatures verifies that this
off-chain transaction indeed is part of the channel off-chain state. The `round`
represents the height of the channel's state at the time when the transaction was
mutually authenticated. The higher the round, the newer the transaction is. This
`round` must be greater than the last on-chain one for that channel.
The `state_hash` is the internal channel state tree root hash at that `round`
height.

If the transaction's `payload` is empty - then the latest on-chain state for
this channel is used. Both `channel_deposit_tx` and `channel_withdraw_tx`
transactions contain a `round` and a `state_hash` and the latest received one
overwrites the previous one. If there had been none of those, then the
`channel_create` transaction is used: it has a `state_hash` and an implicit
`round = 1`.

Either by having a value in the `payload` or not having one, the
`channel_solo_close` and `channel_slash` provide a channel's `round` and a
`state_hash`. In order to determine the order of the channel's states received,
we compare the `rounds` and keep the state with the greatest `round`, considered
to be the _newest_ and _latest_ state. They also provide the `state_hash` that
the channel's state tree had at this `round`.

Both `channel_solo_close_tx` and `channel_slash_tx` contain a `poi` field.
This is the proof of inclusion for participants' balances in the channel state:
all the insignificant data in the channel's MPT (Merkle Patricia Tree) is replaced
by corresponding hashes.
The root hash of the PoI must be equal to the `state_hash` provided by the `payload`.
This guarantees that the PoI indeed is a proof of inclusion for tree at this height.

#### Solo close on-chain transaction
The `channel_close_solo_tx` transaction is the one that triggers the solo
closing sequence. After it is included on-chain channel enters a _closing_ state
and any subsequent withdrawal or deposits are considered invalid. Preconditions
for the `channel_close_solo_tx` to be valid are:

* channel is opened on-chain
* channel is not in a _closing_ state but not yet closed - no
  `channel_close_solo_tx` has been included in a block yet

Any participant in the channel can post a `channel_close_solo_tx` transaction.
In the scope of this description we will call the one that posts the transaction
_solo closer_. The transaction has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel to close |
  | from | string | solo closer's public key |
  | payload | binary | closing payload |
  | poi | binary | closing proof of inclusion |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | gas_price | integer | the gas_price to be used for the fee computation |
  | nonce | integer | solo closer's nonce |

`payload` and `poi` are validated as [described above](#payload-and-proof-of-inclusion)

#### Slash on-chain transaction
After the channel is already in a _closing_ state, both participants can provide
a newer state via the `channel_slash_tx` transaction. Preconditions for
the `channel_slash_tx` to be valid are:

* channel is opened on-chain
* channel is still in a _closing_ state - no `channel_settle_tx` has been
  included in a block yet

Any participant in the channel can post a `channel_slash_tx` transaction. In
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
  | gas_price | integer | the gas_price to be used for the fee computation |
  | nonce | integer | slasher's nonce |

`payload` and `poi` are validated as [described above](#payload-and-proof-of-inclusion)

#### Settle on-chain transaction
After the `channel_close_solo_tx` and all the `channel_slash_tx` transactions,
it is time to finally close the channel. One of the participants posts a
`channel_settle_tx` transaction that enforces closing of the channel. This
happens according to the latest channel state that was sent on-chain. The
`channel_settle_tx` just finalizes the channel closing with the last received
state, redistributes tokens to participants and closes the channel. No further
disputes are possible after that.


In order to give parties time to slash a closing channel and update its state
with a newer one, there is a timeframe only after which the `channel_settle_tx`
can be posted. This is measured in blocks mined on top of the last received
transaction for that channel (either `channel_close_solo_tx` or
`channel_slash_tx`). The amount itself is prenegotiated before opening the
channel and is part of the `channel_create_tx` transaction - it is the value of
`lock_period`. Under no condition can a `channel_settle_tx` be included in a
block before passing the `lock_period` amount of blocks on top of the last
`channel_close_solo_tx` or `channel_slash_tx` transaction. Every next included
`channel_slash_tx` restarts the timer. It is worth noting that since those
transactions must include a `payload` newer than the prevous on-chain one - this
timer can not be postponed indefinitely. Preconditions for the
`channel_settle_tx` to be valid are:

* channel is opened on-chain
* channel is still in a _closing_ state - no other `channel_settle_tx` has been
  included in a block yet
* at least `lock_period` blocks has been mined on top of the last
  `channel_close_solo_tx` or `channel_slash_tx`

Any participant in the channel can post a `channel_settle_tx` transaction. In
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
  | gas_price | integer | the gas_price to be used for the fee computation |
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

## Channel snapshot

Every once and a while a participant might feel the urge to post the latest
channel off-chain state on-chain. That would protect them from malicious
actions from the other party, namely unilaterally closing the channel with an
older state. Another use case would be disputing an on-chain
`channel_force_progress_tx` that is based on an older state. This can be
prevented by posting a `channel_snapshot_solo_tx` transaction on-chain
containing the latest co-authenticated off-chain state - this guarantees that
an older state can not make it on-chain or, in the case of forced progress,
it will be replaced.

It is worth mentioning that if the latest off-chain state is already present
on-chain, the snapshot transaction would not provide any new information
on-chain, so it would fail to be included in the blockchain.

If the channel is not yet closing and a malicious `channel_force_progress_tx`
transaction is included on-chain, the client gets notified. The malicious
forced progress transaction would be one based upon an off-chain state
older than the latest one.
The report declares that a snapshot could dispute the malicious on-chain transaction.
dispute the malicious on-chain transaction.

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "can_snapshot",
      "tx": "tx_+NILAf....",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

#### Snapshotter inittiates a snapshot solo 

If the channel is in an `open` state, any participant can initiate a solo
snapshot transaction by:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```
#### Snapshotter authenticates the snapshot solo 

After the `channel_snapshot_solo_tx` has been requested, the FSM prompts the
client to sign it with:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROELjU+NILAfiEuEAgCeNiiWzLM/cnnqBUv7vRXbaq1oaWD8Ef51YSkRYbPItrwgWidg6w7Q8Ood5kz83sYM26CgwKz4I/AuHusZgKuEDr+hWc0jwrJfeW9ZIojnua4h/tuWLQsr4j2Le5i3spTHVXjba1IClTiqeIZS/3NpnReUsDv1/POzEj1oBZRaEFuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4AhhMG0SswAAH0oWnV",
      "updates": []
    }
  },
  "version": 1
}
```

The snapshotter is to decode the transaction, inspect its contents,
authenticate it, encode it and then post it back via a WebSocket message:
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAV/hWnb8Sh/IknFVUSLYJSQu8v9+SIqilR/Hd/jqKGxCq2OOostDw/DtGNBeqkqeftz2OT4g9EjTR1fyWINwEDLkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAIAnjYolsyzP3J56gVL+70V22qtaGlg/BH+dWEpEWGzyLa8IFonYOsO0PDqHeZM/N7GDNugoMCs+CPwLh7rGYCrhA6/oVnNI8KyX3lvWSKI57muIf7bli0LK+I9i3uYt7KUx1V422tSApU4qniGUv9zaZ0XlLA79fzzsxI9aAWUWhBbhI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4FoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAABqvLutg==\"
  }
}
```

The FSM is to check the transaction and its authentication and then post it
from snapshotters's behalf on-chain. Once it detects it being included
on-chain, it would report it:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAV/hWnb8Sh/IknFVUSLYJSQu8v9+SIqilR/Hd/jqKGxCq2OOostDw/DtGNBeqkqeftz2OT4g9EjTR1fyWINwEDLkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAIAnjYolsyzP3J56gVL+70V22qtaGlg/BH+dWEpEWGzyLa8IFonYOsO0PDqHeZM/N7GDNugoMCs+CPwLh7rGYCrhA6/oVnNI8KyX3lvWSKI57muIf7bli0LK+I9i3uYt7KUx1V422tSApU4qniGUv9zaZ0XlLA79fzzsxI9aAWUWhBbhI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4FoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAABqvLutg==",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

The other participant's FSM will also notify its client that it had seen a new
transaction changing the channel on-chain being included in a microblock.

An interesting edge case would be one participant sending a snapshot with a
round greater than the last seen on-chain but yet not the latest one. This is
not cheating but if the other participant considers this to imply any risk to
them, one could send a `channel_snapshot_solo_tx` as well. The one with the higher
`round` will replace the other and all force-progressed states that had been
based on the older state.

## Force progress

The biggest strength of State Channels lies in having fast and cheap off-chain
contract execution. This imposes a risk, though: if the other party suddenly
becomes non-cooperative or simply missing, a new off-chain state can not be
produced. This is where the `channel_force_progress_tx` transaction comes in.
It allows any of the participants to unilaterally execute an off-chain contract
on-chain. This produces the next State Channel off-chain state on-chain.

A channel force progress transaction is based on the latest co-authenticated
state. It provides off-chain state trees on-chain. They contain the contract
to be executed and all the context needed for the execution itself. This
breaks the assumption of off-chain privacy. If successful, the
`channel_force_progress_tx` transaction produces on-chain the next off-chain
state. That's why it also contains the next `round` and the next `state_hash`.
The latter is the result of applying the off-chain contract call to the
off-chain state trees.

A force progress transaction can be used while the channel is being closed or
while it is still open. The assumption is that if one participant refuses to cooperate,
if the other produces the next forced progress state on-chain, there is no
going back. From then on they could continue either cooperating or they could
close the channel. In both cases, they use the on-chain produced off-chain
state.

The `channel_force_progress_tx` transaction could be a challenge to get right.
The FSM handles this for the client and from a client's perspective it looks
like the off-chain contract call. The only difference is that with
`channel_force_progress_tx` the `gas_price` is mandatory. It is used
both in the contract call execution and the transaction's `fee` computation.

#### Forcer inittiates a forced progress

Any participant can initiate a forced progress by:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version":1,
    "amount":10,
    "call_data":"cb_AAAAA...",
    "contract_id":"ct_5XjcY...",
    "gas_price":1000000000
  }
}
```
Except of the `gas_price`, all other `params` correspond to those in a
`call_contract` off-chain update. The reasoning is quite trivial: if the other
participant refuses a valid off-chain contract call, the other participant can
use the very same arguments, add an actual `gas_price` and produce the
`channel_force_progress_tx`.

#### Forcer authenticates the force progress transaction

After the `channel_force_progress_tx` has been requested, the FSM prompts the
client to sign it with:

```javascript
{ 
   "jsonrpc":"2.0",
   "method":"channels.sign.force_progress_tx",
   "params":{ 
      "channel_id":"ch_2FdiLKkRUdPw4oTRbB6i3M6pquogzWLABQjU373hizDbnD8gGC",
      "data":{ 
         "signed_tx":"tx_+Qi9CwHAuQ....",
         "updates":[ 
            { 
               "abi_version":1,
               "amount":10,
               "call_data":"cb_AAAAAAA...",
               "call_stack":[ 

               ],
               "caller_id":"ak_Vu1cG...",
               "contract_id":"ct_55C...",
               "gas":1000000,
               "gas_price":1000000000,
               "op":"OffChainCallContract"
            }
         ]
      }
   },
   "version":1
}
```

Note that the `updates` that comes with the `channel_force_progress_tx` is the
same as it would be if it were an off-chain `call_contract`.

The forcer is to decode the transaction, inspect its contents, authenticate
it, encode it and then post it back via a WebSocket message:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhA..."
  }
}
```

The FSM is to check the transaction and its authentication and then post it
on the forcer's behalf on-chain. Once it detects it being included
on-chain, it reports it:

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2eiGsAvt...",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA...",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

The other participant's FSM will also notify its client that it has seen a new
transaction in a microblock, changing the channel on-chain.

An interesting edge case would be one participant producing a force progress based on
a state that was valid at some point of time but is not the latest one. This is
considered to be a cheating attempt. The cheating party can try outgrowing the
off-chain state with a couple of `channel_force_progress_tx` transactions at
the end producing on-chain a `round` that is greater than the last one
produced off-chain. If the other participant provides a transaction that was
based on a yet newer off-chain state than the one the chain of forced
progressed transactions was based on, the latter are discared althogether.
With unilaterally forced progress it is not the latest `round` that matters
but rather the latest co-authenticated one they were all based upon.
