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

(***TODO***: needs some more work/clarification)

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
	- [Messages](#messages)
	- [Establishing channel off-chain](#establishing-channel-off-chain)
	- [Establishing channel on-chain](#establishing-channel-on-chain)
- [Contract execution in channels](#contract-execution)
- [Light node requirements](#light-node-requirements)
- [Examples](#examples)
- [Open Questions](#open)

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

In most cases a client/server architecture will most likely be mode of choice,
where a client is using a service offered by the server, which is highly
available and probably also some well known entity.
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
most likely one. This model seems more likely than a decentralised one because
the majority of users would not be able to offer reliable services, longer paths
through the network would lock up significantly more funds and most likely also
incur a higher forwarding fee.

In the hub and spoke model would have a number of big hubs, which would be
involved in most routes through the network. These hubs would be tightly
connected and offer highly available and short paths for most users at the price 
of a loss of privacy.

## Incentives

Operating a channel takes at least two on-chain operations and therefore has a base amount of fees is required and this fact could be abused by a malicious
peer.
If the on-chain balance of an honest peer is less than

To discourage malicious behaviour, a successful slashing of a channel closing,
forfeits the malicious party's funds to the slasher.

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
|   |                       |    +------------+   |                        |   |
|   |                       | funding_locked  |   |                        |   |
|   |                       |                 |   v                        |   |
|   |                       v        [disconnect] +--------------+  error  |   |
|   |                +-------------+ ---------|-> | disconnected | ------> |   |
|   | <------------- |    open     |          |   +--------------+         |   |
|   |   [timeout]    +-------------+ <--------|------------+               |   |
|   |                 ^ |  ^ | |       channel_reestablish                 |   |
|   |        update_* | |  | | |              |                            |   |
|   |                 +-+  +-+ | shutdown     v                            |   |
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


### Messages

#### Off-chain

- [Establishment](#establishing-channel-off-chain)
	- [`channel_open`](#channel_open)
	- [`channel_accept`](#channel_accept)
	- [`funding_created`](#funding_created)
	- [`funding_signed`](#funding_signed)
	- [`funding_locked`](#funding_locked)
	- [`channel_reestablish`](#channel_reestablish)
- Updates
	- [`update_init_contract`](#update_init_contract)
	- [`update_exec_func`](#update_exec_fun)
	- [`update_exec_result`](#update_exec_result)
	- [`update_deposit`](#update_deposit)
	- [`update_withdrawal`](#update_withdrawal)
- Closing
	- [`shutdown`](#shutdown)


#### On-chain

- [Establishment](#establishing-channel-on-chain)
	- [`channel_create`](#channel_create)
- [Updates](#updating-channel-on-chain)
	- [`channel_deposit`](#channel_deposit)
	- [`channel_withdraw`](#channel_withdraw)
- [Closing](#closing-channel-on-chain)
	- [`channel_close_mutual`](#channel_close_mutual)
	- [`channel_close_solo`](#channel_close_solo)
	- [`channel_slash`](#channel_slash)
	- [`channel_settle`](#channel_settlement)


### Establishing channel off-chain

```
A (initiator)          B
|                      |
|---  channel_open  -->|
|<-- channel_accept ---|
|                      |
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

Opening a channel is initiated with this message and communicates the initiators
intent to the potential future peer.

The `channel_open` message should provide the accepting peer all the information
it needs to assemble the [`channel_create`](`channel_create`) transaction in
order to sign it.


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
| responder_amount     | 8  |
 ---------------------- ----
| channel_reserve      | 8  |
 ---------------------- ----
| initiator_pubkey     | 32 |
 ---------------------- ----
```

- `chain_hash`: transaction hash of the chain you want to use, e.g. hash of the
  genesis
- `temporary_channel_id`: randomly chosen id unique between the involved peers
- `lock_period`: time in blocks until a channel closing is to be accepted if not
  mutual or in general for peers to wait for new messages.
- `push_amount`: initial deposit in favour of the responder by the initiator
- `initiator_amount`: amount the initiator is willing to commit
- `responder_amount`: amount the initiator wants the responder to commit
- `channel_reserve`: the minimum amount both peers need to maintain, s.t. both
  have to lose something in case they act maliciously
- `initiator_pubkey`: the account that the initiator wants to use to open the
  channel

(***TODO***: what's the appropriate size for the amounts. Do we want to
discourage channels from holding big amounts?)

In the future state channels might exist across different chains, at which point
specifying a `chain_hash` will become meaningful.

The `lock_period` can be freely chosen. Setting it too high might lock up funds
for too long in the case of non-cooperation and setting it too low could leave
a peer without enough time to react to a malicious peer trying to unilaterally
close a channel.

Having the ability to include a `push_amount`, which credits funds to the other
peer, simplifies the common case of wanting to open a channel and pay someone
immediately. An exchange might want to send you funds via this mechanism, since
it only requires only one on-chain transaction and has the side effect of also
opening a channel.


##### Requirements

*Initiator*:

- `chain_hash` MUST identify the chain to be used
- `temporary_channel_id` MUST be unique between the involved peers
- `lock_period` SHOULD be sufficient time to safely publish transactions to the
  blockchain to stop a cheater
- `push_amount` MUST be less or equal to `initiator_amount`
- `initiator_pubkey` MUST be a valid ed25519 pubkey

*Responder* MUST abort if:

- `chain_hash` is unrecognised
- `initiator_pubkey` not a valid ed25519 pubkey
- `temporary_channel_id` is not unique between the peers

*Responder* SHOULD abort if:

- `initiator_pubkey` does not have sufficient balance to cover
  `initiator_amount`

*Responder* MAY abort if:

- `lock_period` is too small
- `push_amount` is too small
- `channel_reserve` is too large
- `responder_amount` is too large
- `initiator_amount` is too small


#### `channel_accept`

This message is sent by the `responding` peer. It is used to convey the
conditions under which they are willing to accept the terms proposed by the
initiating peer.

```
  name                  size (bytes)
 ---------------------- ----
| chain_hash           | 32 |
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| minimum_depth        | 4  |
 ---------------------- ----
| initiator_amount     | 8  |
 ---------------------- ----
| responder_amount     | 8  |
 ---------------------- ----
| channel_reserve      | 8  |
 ---------------------- ----
| initiator_pubkey     | 32 |
 ---------------------- ----
```

- `chain_hash`: transaction hash of the chain you want to use
- `temporary_channel_id`: randomly chosen id unique between the involved peers,
- `minimum_depth`: number of blocks until an opening transaction should be
  considered final. The `minimum_depth` is set by the responding peer, since
  they will typically be the one providing a service.
- `initiator_amount`: amount the initiator is willing to commit
- `responder_amount`: amount the initiator wants the responder to commit
- `channel_reserve`: the minimum amount both peers need to maintain. This makes
  sure that both have to lose something in case they act maliciously
- `responder_pubkey`: the account that the initiator wants to use to open the
  channel
  
(***TODO***: This could be interactive, i.e. if the responding peer sends
different amounts, then that might communicate that it wants these instead.)

##### Requirements

*Responder*:

- `chain_hash` MUST identify the chain to be used
- `temporary_channel_id` MUST be unique between the involved peers
- `lock_period` SHOULD be sufficient time to safely publish transactions to the
  blockchain to stop a cheater
- `responder_pubkey` MUST be a valid ed25519 pubkey

#### `funding_created`

Both peers need to sign

#### `funding_signed`

#### `funding_locked`

Opening a channel requires an on-chain transaction. This transaction needs to be
included in a block and, since we only have probabilistic finality, be
sufficiently confirmed, s.t. the probability of a chain re-organisation is
negligible.

This message is exchanged by both peers to signal to each other that the above
condition has been met from their point of view and only after both of them
agree on this, can the channel be considered to be opened.

##### Requirements

A node SHOULD NOT send the `funding_locked` message unless the `channel_create`
transaction has `minimum_depth` confirmations.

### Initialise contract

#### `update_init_contract`


### State update

State updates require consent of both peers.

Each update MUST have a strictly increasing sequence number, which SHOULD start
at `0` on channel initialisation.

Parameters:

- `channel_id`:
- `lock_period`: timeout in blocks


#### `update_exec_func`



#### `update_exec_result`

### Deposit

Depositing funds into a channel should increase the longevity of channels, since
it makes balancing them easier but seeing as this incurs an on-chain transaction
we'd still like to avoid it, if possible.


#### `update_deposit`

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| amount               | 8  |
 ---------------------- ----
| data                 |    |
 ---------------------- ----
```


### Withdrawal

#### `update_withdrawal`

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| from                 | 32 |
 ---------------------- ----
| to                   | 32 |
 ---------------------- ----
| amount               | 2  |
 ---------------------- ----
| fee                  |    |
 ---------------------- ----
```

### Errors

Explicitly communicating errors should make debugging easier. In order to avoid
complex error handling, which tends to be prone to mistakes, once a channel
returns an error, it MUST be considered unusable. As such, errors SHOULD be
reserved for unrecoverable failures only.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 |    |
 ---------------------- ----
```

- `channel_id`
- `length`: length of data field
- (optional) `data`: relevant information


### Channel closing

A channel can be closed under three circumstances:

1. Both peers agree to the close and sign the closing transaction together,
   which then gets broadcast to the blockchain.
2. One peer wants to close the channel or the channel gets closed due to an
   error. In this case either side can publish the latest state signed by both
   peers and claim their balance after the negotiated timeout.
3. A malicious peer tries to publish an outdated state, which it prefers over a
   later state. In this case the honest peer can publish a state signed by both
   with a higher nonce and thereby prove that the other one is trying to cheat.

In the case that peers decide to close the channel, funds are accessible
immediately, otherwise they have to wait at least `lock_period` blocks.

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

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
```


The `shutdown` message initiates the closing of a channel and can be sent by
either party. After a peer sends the `shutdown` message, it MUST NOT propose any
more update messages.


##### Requirements

A shutdown cannot be initiated before the on-chain channel opening is not signed.

The initiator MUST NOT send a `shutdown` before a `funding_created` and the responder MUST NOT send a `shutdown` before a `funding_signed` has been sent.
Prior to the respective points peers can still safely abort the procedure
without having committed to anything.


### Establishing channel on-chain

All of the on-chain operations could be submitted by any peer but we assume that
the initiating peer pays for the setup of the channel. Therefore the `initiator`
MUST pay the standard transaction fees.

(***TODO***: should fees be directly be deducted from channel balance?)
(***TODO***: should a third party be able to open a channel for others?)


#### `channel_create`

The `channel_create` transaction is used to register a channel on chain and its
inclusion on chain causes the specified amounts to be locked up.

e.g.

```
Account(initiator).balance := Account(initiator).balance - initiator_amount
Account(responder).balance := Account(responder).balance - responder_amount

Channel(cid).amount := initiator_amount + responder_amount
```

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| initiator            | 32 |
 ---------------------- ----
| responder            | 32 |
 ---------------------- ----
| initiator_amount     | 32 |
 ---------------------- ----
| responder_amount     | 32 |
 ---------------------- ----
| lock_period          | 2  |
 ---------------------- ----
| fee                  |    |
 ---------------------- ----
| nonce                |    |
 ---------------------- ----
```

- `initiator`: public key/address of the initiating peer
- `responder`: public key/address of the responding peer
- `initiator_amount`: unsigned
- `responder_amount`:
- `lock_period`
- `fee`
- `nonce`

The `fee` and `nonce` refer to the `initiator` account, i.e. the `fee` MUST be taken from their balance and the `nonce` of their account MUST be incremented.


##### Requirements

`Account(initiator).balance >= initiator_amount + fee`

### Updating channel on-chain

An update to an open channel requires the signatures of all participants.

Both `channel_deposit` and `channel_withdraw` MUST be signed by all involved
parties, since changing channel balances might change the dynamics of code
running in a channel.


#### `channel_deposit`

Depositing funds into a channel after creation should allow channels to be more
long lived due to the increased ease of balancing out channels. The amount of
coins sent along with this transaction will get locked up just like the initial
deposit.

While it could be desirable to allow anyone to deposit into a channel, we are
going to restrict deposits to the peers of a channel. That means, the `from`
field MUST be an address of one of the participants of the targeted channel and
the standard transaction fee MUST be paid by the `from` account.

This operation is not mandatory for normal channel operations.

- `channel_id`:
- `from`: sender of the deposit
- `amount`: amount of coins deposited
- `to`: the peer which should receive the deposit
- `nonce`: the transaction number of the submitting account


#### `channel_withdraw`

Channels should generally not be used to hold significant amounts of coins but
being able to withdraw locked coins might still be of some use.

The `from` account MUST be a participant in the target channel. The `amount`
MUST be less or equal than the sum of all participants balances, i.e. channels
cannot create coins out of thin air.

- `channel_id`:
- `amount`:
- `from`:
- `to`:
- `nonce`

To give an example, suppose `A` initially deposited `10` coins and `B` deposited `5` coins. Now `B` issues a `channel_withdraw` transaction, which MUST be signed
by both `A` and `B`, with `amount: 6`. Given that both peers agreed to this
value, the updated channel state would now have a balance of `9` and record.


### Closing channel on-chain

#### `channel_close_mutual`

- `channel_id`:
- `amount`: signed
- `fee`
- `nonce`

`amount` is the change in balance for both peers, e.g. if the initiator sent 2
coins, then the amount should be `2`, and the final balances for both peers are
then:

`initiator_final = initiator_start + amount - fee/2`
`responder_final = responder_start - amount - fee/2`


##### Requirements

This transaction MUST have valid signatures of all involved parties.

#### `channel_close_solo`

In order to close a channel unilaterally, a user has to send a
`channel_close_solo` transaction. This is only necessary if one peer stops
responding but can also be used by an malicious peer trying to close a channel
with a state that hasn't been agreed on by all participants.

With the inclusion of this transaction on chain, the timer, during which
disputes in the form of `channel_slash` will be considered, is started.

- `channel_id`:
- `from`
- `nonce`
- `fee`

#### `channel_slash`

If a malicious party sent a `channel_close_solo` with an outdated state, the
honest party has the opportunity to issue a `channel_slash` transaction. This
transaction needs to include a state signed by all peers with a higher sequence
number and if successful, causes the malicious party to forfeit its channel balance.

- `channel_id`:

#### `channel_settle`

The settlement transaction is the last one in the lifecycle of a channel, after
all possible disputes are resolved. This transaction then redistributes the
locked funds.

The `channel_settle` MUST only be included in a block if:

- a `channel_close_solo` transaction was published and has expired, i.e.
`blockheight(top) - blockheight(channel_close_solo_tx) >= lock_period`
- there are no outstanding `channel_slash` transactions, which means that
  either none were published or the most recent one expired

- `channel_id`:

### Channel state tree

Each block MUST commit to a Patricia Merkle tree of open channels, where the
`channel_id` specifies the path.
At a leaf, nodes store information pertaining to the current state of the given
channel.

- `channel_id`
- `chain_hash`
- `initiator_pubkey`
- `responder_pubkey`
- `initiator_amount`
- `responder_amount`
- `lock_period`


### Local state

Peers need to store local state in order to be able to keep track of state
channel operations.

- `chain_hash`
- `initiator_pubkey`
- `responder_pubkey`
- `initiator_amount`
- `responder_amount`
- `channel_active`
- `sequence_number`
- `closed`

## Contracts

### Contract execution

Execution of a contract inside a state channel requires peers to be able to
initialise a virtual machine to run their smart contracts in.

When operating in co-signing mode, contracts might need to be written in a way
to avoid the free option problem.


### Initialisation



## Light node requirements

## Examples


## References

[1]: Lightning Network RFC: https://github.com/lightningnetwork/lightning-rfc

[2]:

[3]: Miller, Andrew, et al. "Sprites and State Channels: Payment Networks that Go Faster than Lightning."

[4]: Malavolta, Giulio, et al. "Concurrency and privacy with payment-channel networks." Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security. ACM, 2017.

[5]: Dziembowski, Stefan, et al. PERUN: Virtual Payment Channels over Cryptographic Currencies⋆. IACR Cryptology ePrint Archive, 2017: 635, 2017.

[6]: Roos, Stefanie, et al. "Settling Payments Fast and Private: Efficient Decentralized Routing for Path-Based Transactions." arXiv preprint arXiv:1709.05748 (2017).

[7]: Tremback, Jehan, and Zack Hess. "Universal payment channels." (2015).
