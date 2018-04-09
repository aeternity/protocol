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


## Table of Contents

- [Goals](#goals)
	- [Privacy](#privacy)
	- [Security](#security)
	- [Speed](#speed)
	- [Cost](#cost)
- [Terms](#terms)
- [High level overview](#high-level-overview)
- [Channel types](#channel-types)
- [Topology](#topology)
- [Incentives](#incentives)
- [Channel types](#channel-types)
- [Artefacts](#artefacts)
- [Protocol](#protocol)
- [Communication](#communication)
	- [Overview](#overview)
- Messages
	- [Off-chain](./OFF-CHAIN)
	- [On-chain](./ON-CHAIN)
- [Contract execution in channels](#contract-execution)
- [Light node requirements](#light-node-requirements)
- [Examples](#examples)
- [Future work](#future-work)
- [References](#references)


## Goals


- generic solution that supports many (all?) smart contracts
	- even better if one state channel is generic, s.t. it can be instantiated and
	  then be used for many different contracts
- composability of channels, i.e. an application works for the
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

On-chain interactions offer little to no privacy, since we currently make
efforts to hide interacting parties or the nature of their interactions.

State channels, at the least, reveal that two parties establish a channel and
the amount of coins they commit to the channel, which is no improvement.
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

Opening a state channel incurs the normal on-chain latency but after the channel
has been established, operations can be executed as fast as both peers can
process them, which should be a major improvement over on-chain interactions.


### Cost

Using state channels requires at least two on-chain transactions, for opening
and closing them. Once a channel is established, no further on-chain
transactions are needed unless a peer wants to withdraw or deposit funds. Even
in the case of an one off transaction, it still might be worth opening a channel
if one already has other open channels and thus might stand to gain fees by
relaying messages.


## Terms

We try to follow the naming conventions used by the lightning network, wherever
it makes sense, in hope to be able to make it easier for others to adapt,
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
we then want to get the balance of that account we use `Account(A).balance`


## Channel types

The most generic kind of channel would be one that lets peers instantiate any
arbitrary smart contract within the channel and does not restrict the number of
peers that can participate in such a channel.

A client-server setup will most likely be mode of choice for the majority of
channels, where a client is using a service offered by the server, which is
highly available and probably also some well known entity.
To give one example, consider the case of a data feed. In this scenario the
initiator sends a micropayment for each request made to the provider. The most
an initiator could lose in this case is one micropayment. (***TODO***: ZKCP)

Here only the initiator has an incentive to cheat and publish an outdated state,
which would assign them more money than they actually have.
A cheater is easy to detect for a supplier. Whenever the initiator closes the
channel unilaterally with an outdated state, the supplier can, during the lock
period, publish a more recent state signed by the initiator at which point the
initiator loses all funds in the channel to the supplier.


## Topology

It is still very much unclear, what the topology of a widely used channel
network would look like but it seems that a hub and spoke model would be the
most probable. This model seems more likely than a decentralised one because the 
majority of users would not be able to offer reliable services, longer paths
through the network would lock up significantly more funds and ostensibly also
incur a higher forwarding fee.

In the hub and spoke model, we would have a number of big hubs, which would be
involved in most routes through the network. These hubs would be tightly
connected and offer highly available and short paths for most users. In turn, this would lead to a loss of privacy and making the network more fragile, since
the disappearance of one of these hubs would have a big impact.


## Incentives

Operating a channel should be considered collaborative game with incentive for cooperation

Operating a channel takes at least two on-chain operations and therefore has a base amount of fees is required and this fact could be abused by a malicious
peer.

To discourage malicious behaviour, a successful slashing of a channel closing,
forfeits the malicious party's funds to the slasher.

If a malicious peer doesn't want to risk loosing all its channel balance, it
still has other options to disrupt or annoy others. Since closing a channel
incurs a fee, they could open a channel with someone and subsequently refuse to
cooperate, locking up coins and making the other party pay the fees required to
close the channel again.

With that in mind, it is advised for users to be cautious with whom they open
channels if they want to avoid the above issues.

On the other hand, attributing every failure in a channel to malice would also
be detrimental and cause both a loss of trust in the system and cause users to
spend more on fees than they should.


## Artefacts

What should the outcome of a state channel be? The simplest answer would be a
change in on-chain balances of participants but it could also be desirable to
use state channels as a poor man's MPC and have a contract with a non-empty
state as the result on chain.


## Fees

If we consider state channels to be long lived objects, then problems can arise
around the handling of fees, that need to be paid for on chain transactions.

Given that all parties need to sign of everything, a malicious party could
potentially black mail a peer under some circumstances.
If fees come from the channel balance, then one might end up in situations,
where the channel balance is lower than the fee required for miners to pick up
the transaction. The upshot here is, that the black mailed peer would lose less
coins than the cost of an on chain transaction, which should not be a lot.
If the fee instead comes from the account sending the transaction, then that
account might end up without enough coins and thus possibly end up with
insufficient funds to close the channel. This could potentially be worse since
the channel might hold significant funds.

Under these circumstances it seems deducting fees directly from the channel balance as part of its closing seems like the most sensible approach.

To avoid this situation, a peer should consider halting any interactions if on-chain fees reach a point, where the fees required to close a channel in a timely
manner approach the balance of the channel.


## High level overview

Participating in a state channel requires two nodes to be able to communicate
with each other. Throughout this document we are going to assume that this
happens via TCP/IP.
The process of discovering the `IP_ADDR:PORT` pair of a remote node is not
covered in this document and assumed to happen out of band, unless both of them are already part of the state channel network, where nodes can announce their identities `(IP_ADDR, PORT, ID)`.

To open a channel, two nodes first establish a connection. If they already have
an open channel, then creating a new one can be done via the same connection,
using a new `temporary_channel_id` and multiplexing the messages.


## Protocol

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


## Communication

Communication between participants of a channel is peer to peer and SHOULD
happen via a reliable and ordered protocol, e.g. TCP. Peers should expect to be
running their own node, in order to be able to catch transactions relevant to
the channels they are involved in, although outsourcing that job to a third party, while still being trustless, might be possible in the future.

Messages will be both on- and off-chain.

Off-chain communication MUST be encrypted. To satisfy this, we use the same
transport protocol used for sync, which offers encryption and authentication.
Please refer to the [sync document](./SYNC.md) for details.

Each pair of nodes SHOULD have at most one open connection. Channels can be
multiplexed easily, given that each channel has a unique id, so re-using
connection does not pose any problems.


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
|   |                       |             |   |                        |   |
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
                   +--------------+
               +-> |    closed    | <----+
               |   +--------------+      |
               |      | channel_create   |
               |      v                  | channel_close_mutual
               |   +--------------+      |
channel_settle |   |     open     | -----+
               |   +--------------+
               |    ^ |    |
               |    | | channel_withdraw/
               |    | | channel_deposit
               |    +-+    |
               |           | channel_close_solo
               |           v
               |   +--------------+
               +-- |    closing   | ----+
                   +--------------+     | channel_slash
                                 ^      |
                                 +------+
```


## Light node requirements


## Future Work


## References

[1]: Lightning Network RFC: https://github.com/lightningnetwork/lightning-rfc

[2]:

[3]: Miller, Andrew, et al. "Sprites and State Channels: Payment Networks that Go Faster than Lightning."

[4]: Malavolta, Giulio, et al. "Concurrency and privacy with payment-channel networks." Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security. ACM, 2017.

[5]: Dziembowski, Stefan, et al. PERUN: Virtual Payment Channels over Cryptographic Currencies⋆. IACR Cryptology ePrint Archive, 2017: 635, 2017.

[6]: Roos, Stefanie, et al. "Settling Payments Fast and Private: Efficient Decentralized Routing for Path-Based Transactions." arXiv preprint arXiv:1709.05748 (2017).

[7]: Tremback, Jehan, and Zack Hess. "Universal payment channels." (2015).
