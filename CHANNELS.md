# State Channels

State channels allow entities to communicate with eachother with
the goal of collectively computing some function `f`.
This `f` can be as simple as "send 0.1 coins every minute" or it
could represent a decentralized exchange. These functions are, in
our case, represented by smart contracts and just like any legal
contract, we need an arbiter in case on party tries to act maliciously.
This arbiter is the blockchain.

- trustless
- off chain vs on chain
- same guarantuess as blockchain

(***TODO***: needs some more work/clarification)

## Goals

- generic solution that supports many (all?) smart contracts
	- even better if one state channel is generic, s.t. it can be
	  instantiated and then be used for many different contracts
- composability of channels, i.e. an application works for the
  A <-> B case should also work in the A <-B-> C (A to C via B) case
- upgradeable without having to close/re-open the channel
- the previous should enable state channels to be long lived
	- this is at odds with privacy
- on chain operations should be kept to a minimum
- participants state should also be kept to a minimum, i.e. O(log n)
  or better constant
- trustless to a degree with blockchain as the arbiter
- any party involved can close a channel, but it should be discouraged
- (?)

Generally, an ideal state channel design should be a strict improvement
over handling interactions on chain. The dimensions we are going to use
to measure improvements are as follows:

- Privacy
- Security
- Speed
- Cost

### Privacy

On-chain interactions offer little to no privacy, since we currently make
efforts to hide interacting parties or the nature of their interactions.

State channels, at the least, reveal that two parties establish a channel
and the amount of coins they commit to the channel, which is no improvement.
In the case that neither party tries to cheat, the exact nature of their
interactions stays revealed, since a mutual closing of a channel does not
require publishing of any state.

With that in mind, state channels offer a slight improvement in privacy.

### Security

State channels offer almost the same security guarantuees as normal on-chain
transactions.

- ***Liveness***: both peers can independently initiate closing of a channel and
  that operation is then processed by the blockchain with the usual assumptions
  of liveness
- ***Trustless***: since operations need to be signed by both peers and they
  sign operations based on their view of the state, both parties will only
  sign operations they agree on and don't need to trust the other peer.

(***TODO***: Should this include basic assumption of the underlying arbiter/
blockchain assumptions?)

Thus security is on par.

### Speed

Opening a state channel incurs the normal on-chain latency but after the
channel has been established, operations can be executed as fast as both
peers can process them, which should be a major improvement over on-chain
interactions.

### Cost

A state channel requires funding by at least one peer

## Terms

We try to follow the naming conventions used by the lightning network,
wherever it makes sense, in hope to be able to make it easier for others
to adapt, although we try to enforce a `who - what - how` rule for naming,
e.g. `channel_close_solo` as opposed to `solo_close_channel` or
`channel_solo_close`.

- ***node***: client connected to the blockchain, that can be addressed
- ***peer***: participant in a channel
- ***channel***: an off-chain method for two peers to exchange state
  updates, each node can have multiple channels and a pair of nodes can
  also have multiple channels between eachother, which should be multiplexed
  over one connection

## High level overview

Participating in a state channel requires two nodes to be able to
communicate with each other. Throughout this document we are going to
assume that this happens via TCP/IP.
The process of discovering the `IP_ADDR:PORT` pair of a remote node
is not covered and assumed to happen out of band, unless both of them
are already part of the state channel network, where nodes can announce
their identities `(IP, PORT, ID)`.

To open a channel, two nodes first establish a connection. If they
already have other open channels, opening a new one

## Unidirectional channels

In a typical client/server architectures, it is the server, who gets
to decide what a valid state is and what isn't. This simplification
is sufficient in many cases. To give one example, consider the case
of a data feed. In this scenario the requester sends a micropayment
for each request made to the provider. The most a requester could lose
in this case is one micropayment. (***TODO***: ZKCP)

Here only the requester has an incentive to cheat and publish an outdated
state, which would assign them more money than they actually have.
A cheater is easy to detect for a supplier. Whenever the requester closes
the channel unilaterally with an outdated state, the supplier can, during
the lock period, publish a more recent state signed by the requester
at which point the requester loses all funds in the channel to the
supplier.

## Bidirectional channels

If both peers are equal then, they each have to sign off all state
updates and both might have incentives to


## Topology





## Protocol

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## Communication

Communication between participants of a channel is peer to peer and
should happen via a reliable and ordered protocol, e.g. TCP. Peers
should expect to be running their own node.

Messages will be both on- and off-chain, with the former exclusive
to opening and closing of channels and the latter used for the rest.

Communication should be encrypted (***TODO: this will probably be the
same scheme used by nodes for normal operation***) and use a binary
data format (***TODO: this will probably be the same data format
used by nodes for normal operation***).

Each pair of nodes should have at most one open connection over which
channels can be multiplexed, given that each channel has a unique id.

### Overview

The following diagram should give an overview of the off-chain state
machine. The starting point for any channel is the `closed` state.

```
+---+ channel_open                                                          +---+
|   | --------------> +-------------+                 error                 |   |
|   |                 | initialized | ------------------------------------> |   |
|   | <-------------- +-------------+                                       |   |
|   |    [timeout]/          | channel_accept                               |   |
|   |    [disconnect]        v                                              |   |
|   |                 +-------------+                 error                 |   |
|   | <-------------- |  accepted   | ------------------------------------> |   |
| c |    [timeout]/   +-------------+                                       | e |
| l |    [disconnect]        | funding_created                              | r |
| o |                        v                                              | r |
| s |                 +-------------+                 error                 | o |
| e | <-------------- | half_signed | ------------------------------------> | r |
| d |    [timeout]/   +-------------+                                       |   |
|   |    [disconnect]        | funding_signed                               |   |
|   |                        v                                              |   |
|   |                 +-------------+  [disconnect]                         |   |
|   | <-------------- |   signed    | -------------+  error                 |   |
|   |    [timeout]    +-------------+ -------------|----------------------> |   |
|   |                        |                     |                        |   |
|   |                        | funding_locked      |                        |   |
|   |                        |                     v                        |   |
|   |                        v        [disconnect] +--------------+  error  |   |
|   |                 +-------------+ -----------> | disconnected | ------> |   |
|   | <-------------- |    open     |              +--------------+         |   |
|   |    [timeout]    +-------------+ <---------------------+               |   |
|   |                  ^ |  ^ | |       channel_reestablish                 |   |
|   |         update_* | |  | | |                                           |   |
|   |                  +-+  +-+ | shutdown                                  |   |
|   |                           |    +-------------+ [disconnect]           |   |
|   |                           +--> |   closing   | ------------+          |   |
|   |                                +-------------+             |          |   |
|   |                                 |  ^                       |          |   |
|   |                                 |  | channel_reestablish   |          |   |
|   | <-------------------------------+  |                       v          |   |
|   |        closing_signed              |         +--------------+  error  |   |
|   |                                    +-------- | disconnected | ------> |   |
+---+                                              +--------------+         +---+
  ^                                                                           |
  |                                                                           |
  +---------------------------------------------------------------------------+
```

***Note***: Terms in square brackets `[]` are not explicit messages
defined by the protocol.



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
               |           | channel_close_solo
               |           v
               |   +--------------+
               +-- |    closing   | ----+
                   +--------------+     | channel_slash
                                 ^      |
                                 +------+
```

### Messages

#### Off-chain

- [Establishment](establishing-channel-off-chain)
	- [`channel_open`](#channel_open)
	- [`channel_accept`](#channel_accept)
	- [`funding_created`](#funding_created)
	- [`funding_signed`](#funding_signed)
	- [`funding_locked`](#funding_locked)
	- [`channel_reestablish`](#channel_reestablish)
- Updates
	- [`update_deposit`](#update_deposit)
	- [`update_withdrawal`](#update_withdrawal)
- Closing
	- [`funding_locked`](#funding_locked)
	- [`shutdown`](#shutdown)

(***TODO***: add HTLCs)

##### On-chain

- [Establishment](establishing-channel-on-chain)
	- [`channel_create`](#channel_create)
- Updates
	- [`channel_deposit`](#channel_deposit)
	- [`channel_withdraw`](#channel_withdraw)
- Closing
	- [`channel_close_mutual`](#channel_close_mutual)
	- [`channel_close_solo`](#channel_close_solo)
	- [`channel_slash`](#channel_slash)
	- [`channel_settlement`](#channel_settlement)

### Establishing channel off-chain

```
A (initiator)          B
|                      |
|---  channel_open  -->|
|<-- channel_accept ---|
|
|-- funding_created -->|
|<- funding_signed  ---|
|                      |
|--- funding_locked -->|
|<-- funding_locked ---|
|                      |
```

In order to establish a channel both peers need to agree on the initial
conditions, e.g. funding amounts, minimum reserve and lock time.

By default the initiator of the channel will pay the fee for the opening
transaction.

#### `channel_open`

Opening a channel is initiated with this message and communicates the
initiators intent to the possible future peer.

The `channel_open` message should provide the accepting peer all the
information it needs to assemble the [`channel_create`](`channel_create`)
transaction in order to sign it.


```
  name                  size (bytes)
 ---------------------- ----
| chain_hash           | 32 |
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| lock_period          | 2  |
 ---------------------- ----
| push_amount          | 8  |
 ---------------------- ----
| initiator_amount     | 8  |
 ---------------------- ----
| participant_amount   | 8  |
 ---------------------- ----
| channel_reserve      | 8  |
 ---------------------- ----
| initiator_pubkey     | 32 |
 ---------------------- ----
```

- `chain_hash`: transaction hash of the chain you want to use
- `temporary_channel_id`:
- `lock_period`: time in blocks until a channel closing is to be accepted
  if not mutual
- `push_amount`: initial deposit in favour of the participant by the initiator
- `initiator_amount`: amount the initiator is willing to commit
- `participant_amount`: amount the initiator wants the provider to commit
- `channel_reserve`: the minimum amount both peers need to maintain, s.t.
  both have to lose something in case they act maliciously
- `initiator_pubkey`:

(***TODO***: what's the appropriate size for the amounts. Do we want to
discourage channels from holding big amounts?)

(***TODO***: participant? receiver? Naming is hard.)

At some point state channels might exist accross different chains, at which
point specifying a `chain_hash` will become mandatory.

Having the ability to include a `push_amount`, which credits funds to the other
peer, simplifies the common case of wanting to open a channel an pay someone
immediately. An exchange might want to send you funds via this mechanism, since
it only requires only one on-chain transaction and has the side effect of also
opening a channel.


##### Requirements

Initiator:

- `chain_hash` MUST identify the chain to be used
- `temporary_channel_id` MUST be unique for the connecting peer
- `initiator_pubkey` MUST be a valid ed25519 pubkey
- `lock_period` SHOULD be sufficient time to safely publish transactions
  to the blockchain to stop a cheater

Participant MUST abort if:

- `initiator_pubkey` not a valid ed25519 pubkey
- `temporary_channel_id` is not unique between the peers

Participant MAY abort if:

- `lock_period` is too small
- `push_amount` is too small
- `channel_reserve` is too large
- `participant_amount` is too large
- `initiator_amount` is too small



#### `channel_accept`

```
  name                  size (bytes)
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| chain_hash           | 32 |
 ---------------------- ----
| minimum_depth        | 4  |
 ---------------------- ----
| initiator_amount     | 8  |
 ---------------------- ----
| participant_amount   | 8  |
 ---------------------- ----
| channel_reserve      | 8  |
 ---------------------- ----
| initiator_pubkey     | 32 |
 ---------------------- ----
```

- `minimum_depth`: number of blocks until an opening transaction should be
  considered final. The `minimum_depth` is set by the receiving peer, since
  they will typically be the one providing a service.


### State update

State updates require consent of both peers.

Each update has a strictly increasing sequence number, which should start at
`0` on channel initialization.

Parameters:

- `channel_id`:
- `lock_period`: timeout in blocks


### Deposit

Depositing funds into a channel should increase the longevity of channels,
which is one of the goals we set out to reach.


### Withdrawal



### Errors

Explicitly communicating errors should make debugging easier. In order to
avoid complex error handling, which tends to be prone to mistakes, once a
channel returns an error, it must be considered unusable. As such, errors
should be reserved for unrecoverable failures only.

- `channel_id`
- `length`: length of data field
- (optional) `data`: relevant information


### Channel closing

A channel can be closed in three different ways:

1. Both peers agree to the close and sign the closing transaction
   together, which then gets broadcast to the blockchain.
2. One peer wants to close the channel or the channel gets closed
   due to an error. In this case either side can publish the latest
   state signed by both peers and claim their balance after the
   negotiated timeout
3. A malicious peer tries to publish an outdated state, which it
   prefers over a later state. In this case the honest peer can
   punlish a state signed by both with a higher nonce and thereby
   proof that the other is trying to cheat.


```
A                      B
|                      |
|----   shutdown   --->|
|<---   shutdown   ----|
|          .           |
|          .           |
|  resolve pending op  |
|          .           |
|          .           |
|          .           |
|<-- signed_closing ---|
|--- signed_closing -->|
|                      |
```


#### `shutdown`

The `shutdown` message initiates the closing of a channel and can
be sent by either party.
Afer a peer sends the `shutdown` message, it MUST NOT propose any
more `channel_update`

In the case that both peers decide to close the channel, funds are
accessible immediatly.

### Establishing channel on-chain

#### `channel_create`

- `initiator`: public key
- `participant`: public key
- `initiator_amount`:
- `participant_amount`:

#### `channel_deposit`

- `channel_id`:
- `amount`:
- `to`:

#### `channel_withdraw`

- `channel_id`:
- `amount`:
- `from`:
- `to`:

#### `channel_close_mutual`

- `channel_id`:
- `amount`: signed

`amount` is the change in balance for both peers, e.g. if
the initiator sent 2 coins, then the amount should be `2`,
and the final balances for both peers are then:

`initiator_final = initiator_start - amount`
`receiver_final = receiver_start + amount`

If the initiator sent `-2` coins, i.e. received them, their
final balance would be increased by that amount.

#### `channel_close_solo`

- `channel_id`:

#### `channel_slash`

- `channel_id`:

#### `channel_settlement_force`

- `channel_id`:

### Channel state tree

Each block commits to a merkle tree of open channels.

### Local

## Open

- privacy at odds with long livedness if outsiders can tell
  with whom an entity is opening a state channel with, although
  remedied a bit if they are generic

- What happens if both parties lose their state


## References

[1]: Lightning Network RFC: https://github.com/lightningnetwork/lightning-rfc

[2]:

[3]: Miller, Andrew, et al. "Sprites and State Channels: Payment Networks that Go Faster than Lightning."

[4]: Malavolta, Giulio, et al. "Concurrency and privacy with payment-channel networks." Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security. ACM, 2017.

[5]: Dziembowski, Stefan, et al. PERUN: Virtual Payment Channels over Cryptographic Currencies⋆. IACR Cryptology ePrint Archive, 2017: 635, 2017.

[6]: Roos, Stefanie, et al. "Settling Payments Fast and Private: Efficient Decentralized Routing for Path-Based Transactions." arXiv preprint arXiv:1709.05748 (2017).

[7]: Tremback, Jehan, and Zack Hess. "Universal payment channels." (2015).


