# State Channels

State channels allow entities to communicate with each other with the goal of
collectively computing some function `f`.
This `f` can be as simple as "send 0.1 coins every minute" or it could represent
a decentralised exchange. These functions are, in our case, represented by smart
contracts and just like any legal contract, we need an arbiter in case one party
tries to act maliciously. This arbiter is the blockchain.

- trustless
- off chain vs on chain
- same guarantees as blockchain

Before describing the protocols involved, we are going to introduce some high
level issues, that shaped our state channel design.

## Terms

We try to follow the naming conventions used by the lightning network, wherever
it makes sense, in hope to be able to make it easier for others to adopt,
although we try to enforce a `who - what - how` rule for naming, e.g.
`channel_close_solo` as opposed to `solo_close_channel` or `channel_solo_close`.

- ***node***: client connected to the blockchain, that can be addressed via an
  IP address and port
- ***peer***: participant in a channel
- ***channel***: an off-chain method for two peers to exchange state updates,
  each node can have multiple channels and a pair of nodes can also have
  multiple channels between each other, which should be multiplexed over one
  connection


## Notation

All objects on the blockchain have a type and are uniquely addressable. We will
denote this by `Type(Id)`, e.g. `Account(A)` is the account at address `A`. If
we then want to get the balance of that account we use `Account(A).balance`.


## Goals

- generic solution that supports all smart contracts
	- even better if one state channel is generic, s.t. it can be instantiated and
	  then be used for many different contracts
- transitivity of channels, i.e. an application works for the
  A <-> B case should also work in the A <-B-> C (A to C via B) case
- upgradeable without having to close/re-open the channel
- the previous should enable state channels to be long lived
	- this is at odds with privacy
- on chain operations should be kept to a minimum
- participants state should also be kept to a minimum, i.e. O(log n) or better
  constant multiplier
- trust-less to a degree with blockchain as the arbiter
- any party involved can close a channel, but it should be discouraged

Generally, an ideal state channel design should be a strict improvement over
handling interactions on chain. The dimensions we are going to use to measure
improvements are as follows:

- Privacy
- Security
- Speed
- Cost


### Privacy

On-chain interactions offer little to no privacy, since we currently make no
efforts to hide interacting parties or the nature of their interactions.

Basic State channels reveal that two parties establish a channel and
the amount of coins they commit to the channel, which is not an improvement.
In the case that neither party tries to cheat, the exact nature of their
interactions stays unrevealed, since a mutual closing of a channel does not
require publishing of any state.

With that in mind, state channels offer a slight improvement in privacy.


### Security

State channels offer almost the same security guarantees as normal on-chain
transactions.

- ***Liveness***: both peers can independently initiate closing of a channel and
  that operation is then processed by the blockchain with the usual assumptions
  of liveness.
- ***Trust-less***: since operations need to be signed by both peers and they
  sign operations based on their view of the state, both parties will only
  sign operations they agree on and don't need to trust the other peer.

Thus security is on par.


### Speed

Opening a state channel involves an on-chain transaction, thus incurs a normal
on-chain latency. Once a channel is established, operations are executed as fast
as both peers can exchange and process them, which should be a major improvement
over on-chain interactions.


### Cost

State channels require at least two on-chain transactions: to open and to close
them. Once a channel is established, no further on-chain transactions are needed
unless a peer wants to withdraw or deposit funds. Even for one off transaction,
it still might be worth opening a channel if one already has other open channels
and thus might stand to gain fees by relaying messages.


## Channel types

The most generic kind of channel would be one that lets peers instantiate any
arbitrary smart contract within the channel and does not restrict the number of
peers that can participate in such a channel.

Our construction will try to meet the former property, allowing any number of
arbitrary smart contracts to be executed in the channel, but restrict the latter
to two peers per channel. This restriction is mostly to keep the channel
construction simple. It is certainly possible to have more than two participants
per channel, requiring all of them to sign off every update, but it would incur
a big overhead and lead to an increased likelihood of a channel getting stuck,
whenever a peer stops responding. There are methods to avoid the liveness issue
but at that point it becomes unclear if we are still operating a state channel
or already dealing with a side-chain.

With that in mind, the two peers in a channel will most likely not have the
same roles but instead end up in a client-server arrangement for the majority of
channels, where a client is using a service offered by the server, which is
highly available and probably also some well known entity, mirroring the status
quo of the current web.
A popular example would be an exchange, where users connect to an exchange via
state channels. This process can be trustless, since exchanges can not
lose funds, that haven't been signed over to them


## Topology

It is still very much unclear, what topology of a widely used channel network
would look like. It seems that a hub - spoke model would be the most probable.
This model is more likely than a decentralised one because the majority of
users would not be able to offer reliable services, longer paths through the
network would lock up significantly more funds and ostensibly also incur higher
forwarding fee.

In the hub and spoke model, we would have a number of big hubs, which would be
involved in most routes through the network. These hubs would be tightly
connected and offer highly available and short paths for most users. In turn,
this would lead to a loss of privacy and making the network more fragile, since
the disappearance of one of these hubs would have a big impact on its overall
connectedness.


## Incentives

Operating a channel takes at least two on-chain operations and therefore a
base amount of fees is required. This fact could be abused by a malicious
peer. Since closing a channel incurs a fee, (s)he could open a channel with
someone and subsequently refuse to cooperate, to unlock the coins the
other party will require the other party to close the channel and pay
transaction fees.

Once a channel has been opened, all operations happening within have to be
signed off by all participants. This creates a free option for whoever is
signing off an update last. This problem is remedied by the ability to enforce
progress on chain, that is taking the state from the channel and have miners
execute the contract call, that other party wasn't willing to sign off.

With that in mind, it is advised for users to be cautious with whom they open
channels.

On the other hand, attributing every failure in a channel to malice would also
be detrimental and cause both a loss of trust in the system and users to spend
more on fees than they should.


## Artefacts

What should be an outcome of a state? The simplest product would make a change
in on-chain balances of participants. It could be also desirable to use state
channels as a poor man's MPC and have an on-chain contract with a non-empty
state as the result. It will require a compact proof, that the given smart
contract actually produced the state provided by the participants.


## Fees

If we consider state channels to be long lived objects, then problems can arise
around the fees handling, that need to be paid for on chain transactions.

Given that all parties need to sign off everything, a malicious party could
potentially black mail a peer under some circumstances.
If fees come from the channel balance, then one might end up in situations,
where the channel balance is lower than the fee required by miners to pick up
the transaction. The upshot here is, that the black mailed peer would lose less
coins than the cost of an on chain transaction, which should not be a lot.
If the fee instead comes from the account sending the transaction, then that
account might end up without enough coins and thus possibly end up with
insufficient funds to close the channel. This could potentially be worse since
the channel might hold significant funds.

Under these circumstances it seems deducting fees directly from the channel
balance as part of its closing seems like the most sensible approach.

To avoid this situation, a peer should consider halting any interactions if
on-chain fees reach a point, where the fees required to close a channel in a
timely manner approach the balance of the channel.


## Protocol

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


### Communication

Communication between participants of a channel is peer to peer and SHOULD
happen via a reliable and ordered protocol, e.g. TCP. Peers should expect to be
running their own node, to receive transactions relevant to the channels they
are involved in. Although outsourcing that job to a third party, while still
being trustless, might be possible in the future.

Participating in a state channel requires two nodes to be able to communicate
with each other. Throughout this document we are going to assume that this
happens via TCP/IP. The process of discovering the `IP_ADDR:PORT` pair of a
remote node is not covered in this document and assumed to happen out of band,
unless both of them are already part of a state channel network, where nodes
can announce their identities `(IP_ADDR, PORT, ID)`.

Messages will be sent both on- and off-chain.

Off-chain communication MUST be encrypted. To satisfy this, we use the same
transport protocol used for sync, which offers encryption and authentication and
is based on the Noise protocol.

Each pair of nodes SHOULD have at most one open connection. Channels can be
multiplexed easily, given that each channel has a unique id, so re-using
connections does not pose any problems.


### Overview

The following diagram should give an overview of the off-chain state machine.
The starting point for any channel is the `closed` state.

```
+---+ channel_open                                                         +---+
|   | -------------> +-------------+                 error                 |   |
|   |                | initialized | ------------------------------------> |   |
|   | <------------- +-------------+                                       |   |
|   |   [timeout]/          | channel_accept                               |   |
|   |   [disconnect]        v                                              |   |
|   |                +-------------+                 error                 |   |
|   | <------------- |  accepted   | ------------------------------------> |   |
| c |   [timeout]/   +-------------+                                       | e |
| l |   [disconnect]        | funding_created                              | r |
| o |                       v                                              | r |
| s |                +-------------+                 error                 | o |
| e | <------------- | half_signed | ------------------------------------> | r |
| d |   [timeout]/   +-------------+                                       |   |
|   |   [disconnect]        | funding_signed                               |   |
|   |                       v                                              |   |
|   |                +-------------+  [disconnect]                         |   |
|   | <------------- |   signed    | -------------+  error                 |   |
|   |   [timeout]    +-------------+ -------------|----------------------> |   |
|   |                       |    |  shutdown      |                        |   |
|   |        funding_locked |    +------------+   |                        |   |
|   |                       |                 |   |                        |   |
|   |                       |                 |   v                        |   |
|   |                       v        [disconnect] +--------------+  error  |   |
|   |                +-------------+ ---------|-> | disconnected | ------> |   |
|   | <------------- |    open     |          |   +--------------+         |   |
|   |   [timeout]    +-------------+ <--------|------------+               |   |
|   |                 ^ |      |       channel_reestablish                 |   |
|   |       update_*/ | |      |              |                            |   |
|   |       ping/pong +-+      | shutdown     v                            |   |
|   |                          |    +-------------+ [disconnect]           |   |
|   |                          +--> |   closing   | ------------+          |   |
|   |                               +-------------+             |          |   |
|   |                                |  ^                       |          |   |
|   |                                |  | channel_reestablish   |          |   |
|   | <------------------------------+  |                       v          |   |
|   |       closing_signed              |         +--------------+  error  |   |
|   |                                   +-------- | disconnected | ------> |   |
+---+                                             +--------------+         +---+
  ^                                                                          |
  |                                                                          |
  +--------------------------------------------------------------------------+
```

***Note***: Terms in square brackets `[]` are not explicit messages defined by
the protocol but part of the underlying transport protocol.


On-chain

```
+---+           channel_create
|   | --------------------------------> +--------------+
|   |                                   |     open     |
|   | <-------------------------------- +--------------+
|   |         channel_close_mutual             |    ^ |   channel_withdraw/
|   |                                          |    | | channel_snapshot_solo/
|   |                       channel_close_solo |    | |   channel_deposit/
|   |                                          |    | | channel_force_progress
|   |                                          |    | |
| c |                                          |    | |
| l | channel_close_mutual                     |    +-+
| o | <------------------- +--------------+    |
| s |                      |    closing   |    |
| e | <------------------- +--------------+    |
| d |    channel_settle      |          ^      |
|   |                        |          |      |
|   |         channel_slash/ |   [lock_timeout]|
|   |  channel_force_progress|          |      |
|   |                        |          |      |
|   |                        v          |      |
|   | channel_close_mutual +--------------+    |
|   | <------------------- |    locked    | <--+
|   |                      +--------------+
+---+                       | ^
                            | |
                      channel_slash/
                  channel_force_progress
                            | |
                            +-+
```

***Note***: `[lock_timeout]` is not an explicit message of the protocol but the
expiration of a timer.

### Contract execution

Off-chain contract life cycle closely represents the on-chain one. A contract
is created via a co-signed off-chain transaction. Once this is done, the new
contract can be called by both channel participants. Each contract has its own
state and balance, which can be modified by contract calls.
Contract calls are purged on every round. If the last round contained a call,
it would be part of the calls tree, and otherwise the tree will be empty.
Different client implementations can keep old calls in order for participants
to be able to inspect their return values but this is not part of the protocol.
Participants can remove an off-chain contracts from a channel's state tree and
redistribute its balance amongst them.

Each participant of a state channels keeps a state tree representing the
internal channel's state. This tree consists of accounts, contracts and
contract calls. Although this tree is internal to the channel, during dispute
resolution, part of it is posted on-chain in order to use the blockchain as an
arbiter. Despite the contract being internal in most cases, it is not in all
cases. The privacy could be further improved.

Contract call execution relies on both participants agreeing on a state update.
At any point a participant can be missing or refusing to cooperate to a valid
off-chain contract call. We call this a dispute and it can be resolved using
forcing of progress on-chain. This requires the forcing party to provide enough
information for the contract's execution. The result of a successful force
progress is a new channel off-chain state. This way we keep contracts in
channels trustless.

## Node configuration

æternity nodes are prepared to service state channels via a JSON-RPC API over WebSocket.

The following configuration values control the support for state channels:

* `websocket.port` - The listen port for the state channels API. No default, meaning that the WebSocket API is unavailable by default.
* `websocket.listen_address` - The listen address for the WebSocket API. Default: `127.0.0.1`, meaning that only local connections are allowed.
* `websocket.acceptors` - The number of concurrent socket acceptors (default: `10`). This is mainly an optimization, since the node can service requests at good speed even with one acceptor.
* `channels.max_count` - The maximum number of concurrently active state channel clients served by the node (default: `1000`). The limit checking will currently not be applied to channels being reestablished, as the node has already agreed to service them.

## Light node requirements


## Future Work


## References

[1]: Lightning Network RFC: https://github.com/lightningnetwork/lightning-rfc

[2]: Miller, Andrew, et al. "Sprites and State Channels: Payment Networks that Go Faster than Lightning."

[3]: Malavolta, Giulio, et al. "Concurrency and privacy with payment-channel networks." Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security. ACM, 2017.

[4]: Dziembowski, Stefan, et al. PERUN: Virtual Payment Channels over Cryptographic Currencies⋆. IACR Cryptology ePrint Archive, 2017: 635, 2017.

[5]: Roos, Stefanie, et al. "Settling Payments Fast and Private: Efficient Decentralized Routing for Path-Based Transactions." arXiv preprint arXiv:1709.05748 (2017).

[6]: Tremback, Jehan, and Zack Hess. "Universal payment channels." (2015).
