# Off-chain

Each party keeps a state tree specific for the channel. It consists of all the
channel data: accounts, contracts and etc. and has the same structure as the
on-chain state tree. Off-chain transactions update this channel auxiliary tree.
It is a responsibility of the parties to keep this locally. Solo closing
transactions provide a proof of inclusion for it instead of
posting the whole tree.
Each off-chain update consists of updates being applied on top of channel state
tree and an integer value `round` representing when it happened. Since `round`
must always be bumped, provided two off-chain transactions we can reason which
was performed earlier than the other.


## Messages

- [Control messages](#control-messages)
  + [`error`](#error)
  + [`ping`/`pong`](#pingpong)
- [Establishing channel off-chain](#establishing-channel-off-chain)
  + [`channel_open`](#channel_open)
  + [`channel_accept`](#channel_accept)
  + [`funding_created`](#funding_created)
  + [`funding_signed`](#funding_signed)
  + [`funding_locked`](#funding_locked)
  + [`channel_reestablish`](#channel_reestablish)
  + [`channel_reestablish_ack`](#channel_reestablish_ack)
- [Updates](#state-update)
  + [`update`](#update)
  + [`update_ack`](#update_ack)
  + [`update_error`](#update_error)
  + [`deposit_created`](#deposit_created)
  + [`deposit_signed`](#deposit_signed)
  + [`deposit_locked`](#deposit_locked)
  + [`deposit_error`](#deposit_error)
  + [`withdraw_created`](#withdraw_created)
  + [`withdraw_signed`](#withdraw_signed)
  + [`withdraw_locked`](#withdraw_locked)
  + [`withdraw_error`](#withdraw_error)
- [Other interaction](#other-interaction)
  + [`inband_msg`](#inband_msg)
- [Closing](#channel-closing)
  + [`leave`](#leave)
  + [`leave_ack`](#leave_ack)
  + [`shutdown`](#shutdown)
  + [`shutdown_ack`](#shutdown_ack)
- [Contracts](#contracts)
  + [On-chain enforcement](#on-chain-enforcement)
  + [Lifecycle](#contracts-lifecycle)
  + [Referring on-chain objects](#contracts-referring-on-chain-data)
  + [Gas consumption](#gas-consumption)


## Overview

The protocol parties use to run smart contracts is a two phase commit protocol,
where one party proposes a change, gets it signed off by the others and then
commits the update locally. These checks are necessary to avoid parties getting
confused if updates are being proposed simultaneously.
On a higher level, to keep off-chain and on-chain state in sync, parties should
refuse to sign updates for either without also getting a signature for the
other, e.g. don't sign an on chain `channel_deposit` transaction without also
updating the state in channel as well.

With the consistency of state updates being secured between parties, it is
essential that parties make absolutely sure to not lose their local state, since
it could potentially lead to them not being able to slash outdated states
published on-chain.


## Control messages

### Framing

Each message is identified by a 1-byte message code. The size of the following
message is defined by the type – see the description of each individual
message type.

```
  name                  size (bytes)
 ---------------------- ----
| msg_type             | 1  |
 ---------------------- ----
| message              | .. |
 ---------------------- ----
```

The following message codes are defined:
```
  type              code
-------------------------
| channel_open     | 1  |
| channel_accept   | 2  |
| channel_reestabl | 3  |
| channel_reest_ack| 4
| funding_created  | 5  |
| funding_signed   | 6  |
| funding_locked   | 7  |
| update           | 8  |
| update_ack       | 9  |
| update_error     | 10 |
| deposit_created  | 11 |
| deposit_signed   | 12 |
| deposit_locked   | 13 |
| deposit_error    | 14 |
| withdraw_created | 15 |
| withdraw_signed  | 16 |
| withdraw_locked  | 17 |
| withdraw_error   | 18 |
| leave            | 94 |
| leave_ack        | 95 |
| inband_message   | 96 |
| error            | 97 |
| shutdown         | 98 |
| shutdown_ack     | 99 |
-------------------------
```

### `error`

Message code: 97

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

- `channel_id`: the temporary or final channel id
- `length`: length of data field
- (optional) `data`: relevant information


### `ping`/`pong`


## Establishing channel off-chain

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

In order to establish a channel both parties need to agree on the initial
conditions, e.g. funding amounts, minimum reserve and lock time.

By default the initiator of the channel will pay the fee for the opening
transaction.


### `channel_open`

Message code: 1

This message initiates the opening of a channel and communicates the initiators'
intent to a potential future party.

The `channel_open` message should provide the accepting party all the information
it needs to assess whether or not it should accept the channel.


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
- `temporary_channel_id`: randomly chosen id unique between the involved parties
- `lock_period`: time in blocks until a channel closing is to be accepted if not
  mutual or in general for parties to wait for new messages.
- `push_amount`: initial deposit in favour of the responder by the initiator
- `initiator_amount`: amount the initiator is willing to commit
- `responder_amount`: amount the initiator wants the responder to commit
- `channel_reserve`: the minimum amount both parties need to maintain, amount of
  coins a party is to lose in case of acting maliciously
- `initiator_pubkey`: the account that the initiator wants to use to open the
  channel


(***TODO***: what's the appropriate size for the amounts. Do we want to
discourage channels from holding big amounts?)

(***TODO***: should the initiator send along fee and nonce as well so that the
responder can assemble the `channel_create` themselves?)

In the future state channels might exist across different chains, at which point
specifying a `chain_hash` will become meaningful.

The `lock_period` can be chosen freely. Setting it too high might lock up funds
for too long in the case of non-cooperation and setting it too low could leave
a party without enough time to react to a malicious party trying to unilaterally
close a channel.

Having the ability to include a `push_amount`, which credits funds to the other
party, simplifies the common case of wanting to open a channel and pay someone
immediately. An exchange might want to send you funds via this mechanism, since
it requires only one on-chain transaction and has the side effect of also
opening a channel.
If `push_amount > 0` then the initiator should send along a signed update,
assigning that amount to the responder, before sending the `funding_created`
message.

A `channel_reserve` ensures that parties have something to lose in the case that
they start acting maliciously. Enforcement of this rule must be done by the
clients, which in practice means they should not sign any updates that end up
violating this invariant.


#### Requirements

*Initiator*:

- `chain_hash` MUST identify the chain to be used
- `temporary_channel_id` MUST be unique between the involved parties
- `lock_period` SHOULD be sufficient time to safely publish transactions to the
  blockchain to stop a cheater
- `push_amount` MUST be less or equal to `initiator_amount`
- `initiator_pubkey` MUST be a valid ed25519 pubkey

*Responder* MUST abort if:

- `chain_hash` is unrecognised
- `initiator_pubkey` not a valid ed25519 pubkey
- `temporary_channel_id` is not unique between the parties

*Responder* SHOULD abort if:

- `initiator_pubkey` does not have sufficient balance to cover
  `initiator_amount`

*Responder* MAY abort if:

- `lock_period` is too small
- `push_amount` is too small
- `channel_reserve` is too large or small
- `responder_amount` is too large
- `initiator_amount` is too small


### `channel_accept`

Message code: 2

This message is sent by the `responding` party. It is used to convey the
conditions under which they are willing to accept the terms proposed by the
initiating party.

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
| responder_pubkey     | 32 |
 ---------------------- ----
```

- `chain_hash`: transaction hash of the chain you want to use
- `temporary_channel_id`: randomly chosen id unique between the involved parties,
- `minimum_depth`: number of blocks until an opening transaction should be
  considered final. The `minimum_depth` is set by the responding party, since
  they will typically be the one providing a service.
- `initiator_amount`: amount the initiator is willing to commit
- `responder_amount`: amount the initiator wants the responder to commit
- `channel_reserve`: the minimum amount both parties need to maintain. This makes
  sure that both have to lose something in case they act maliciously
- `responder_pubkey`: the account that the initiator wants to use to open the
  channel

(***TODO***: This could be interactive, i.e. if the responding party sends
different amounts, then that might communicate that it wants these instead.)

#### Requirements

*Responder*:

- `chain_hash` MUST identify the chain to be used
- `temporary_channel_id` MUST be unique between the involved parties
- `lock_period` SHOULD be sufficient time to safely publish transactions to the
  blockchain to stop a cheater
- `responder_pubkey` MUST be a valid ed25519 pubkey

### `channel_reestablish`

Message code: 3

It is possible to resume a channel which has been terminated either due
to client failure or by the participants mutually agreeing to leave.

```
  name                  size (bytes)
 ---------------------- ----
| chain_hash           | 32 |
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

The payload (`data`) must be the latest mutually signed offchain state, and
the clients must verify that they have the corresponding state trees to match
the state (otherwise, it will not be possible to use the channel later on.)

In the `epoch` implementation, the state trees are cached inside the node.
Note that if the node restarts, cached data is not likely to survive (it is
not persisted on each update for performance reasons.) The `epoch` channel
fsm automatically recovers the state trees and verifies that the provided
state is in fact the last mutually signed state.

#### Requirements

*Responder*:

- MUST abort if the `chain_id` doesn't match the current chain.
- MUST abort if the payload does not correspond to the last known mutually
  signed state.
- MUST abort if it doesn't have a corresponding state tree (is able to verify
  proof-of-inclusion) for the provided state.

### `channel_reestablish_ack`

Message code: 4

```
  name                  size (bytes)
 ---------------------- ----
| chain_hash           | 32 |
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

This is a response message to `channel_reestablish`, expected to contain
identical information.

#### Requirements

*Initiator*:

- MUST abort if contents do not match exactly, those of the preceding
  `channel_reestablish`
- MUST abort if the `chain_id` doesn't match the current chain.
- MUST abort if the payload does not correspond to the last known mutually
  signed state.
- MUST abort if it doesn't have a corresponding state tree (is able to verify
  proof-of-inclusion) for the provided state.


### `funding_created`

Message code: 5

In order to open a channel on chain, parties need to cooperate and co-sign the
`channel_create` transaction. The `funding_created` message is used by the
initiator to send an initial state - a `channel_create_tx` object, signed
by the Initiator.

```
  name                  size (bytes)
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```


#### Requirements

*Responder*:

- MUST abort if the size of the payload does not match `length`
- MUST abort if the `data` cannot be deserialized into a valid
  `channel_create_tx` object
- MUST abort if the signature is invalid for the provided transaction data
- SHOULD abort if the `round` of the state is not equal to `1`


### `funding_signed`

Message code: 6

If the responder was able to validate the initiator's signature sent in the
`funding_created` message, then it should add its own signature to the state
object. The co-signed object will become the initial off-chain state of the
channel.

```
  name                  size (bytes)
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

#### Requirements

*Initiator*:

- MUST abort if the size of the payload does not match `length`
- MUST abort if the `data` cannot be deserialized into a valid
  `channel_create_tx` object
- MUST abort if the `data` object isn't the offered initial state
- MUST abort if the `data` object isn't mutually signed by both parties.


### `funding_locked`

Message code: 7

Opening a channel requires an on-chain transaction. This transaction needs to be
included in a block and, since we only have probabilistic finality, be
sufficiently confirmed, so that the probability of a chain re-organisation is
negligible.

This message is exchanged by both parties to signal to each other that the above
condition has been met from their point of view and only after both of them
agree on this, can the channel be considered to be opened.

All subsequent messages must use the included `channel_id` instead of the
`temporary_channel_id`.


```
  name                  size (bytes)
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
```


#### Requirements

- A node MUST NOT send the `funding_locked` message unless the `channel_create`
transaction has `minimum_depth` confirmations.

## State update

State updates require consent of both parties.

Each update MUST have a strictly increasing round, which SHOULD start
at `0` on channel initialisation.

Parameters:

- `channel_id`:
- `balances`:
- `state`


### `update`

Message code: 8

Once `funding_locked` messages have been exchanged, the channel enters the
`open` state. Changes to the off-chain state can be effected by sending an
`update` message. The payload of this message must be a singly-signed
off-chain state, where the `updates` element contains a list of operations
to be performed on the previous state, and the `state_hash` is the aggregated
root hash of the resulting state trees. The receiver must verify that the
state is a valid outcome, then return it, co-signed, in an `update_ack`
message.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

### `update_ack`

Message code: 9

In response to an `update` message, the receiving side verifies that the
operations listed in the `updates` list, applied to the most recent co-signed
state, results in a state tree corresponding to `state_hash`. If so, the
state object is co-signed, then returned as payload in an `update_ack`
message.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

### `update_error`

Message code: 10

Since both sides may initiate an `update` request, it is possible that both
may do so at roughly the same time. In particular, in the `epoch` system,
if an `update` request arrives while the fsm is waiting for its client to
sign a new state update, it reverts both its own update attempt and the
other participant's update request by sending an `update_error` message.
The `round` element signifies the round of the fallback state, which must
be the last mutually signed state. The receiver does not reply.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| round                | 4  |
 ---------------------- ----
```

### `deposit_created`

Message code: 11

In order to deposit more funds into the channel, one party can initiate
a `deposit_created` request. The payload is a singly signed
`channel_deposit_tx` object, which includes the state hash and round of the
next off-chain state, after applying a deposit operation with the expected
amount. The initiating side can only deposit coins from its own on-chain
account (same public key) to its own off-chain account in the channel state.

Note that it is possible to deposit a zero amount, essentially making the
operation an on-chain snapshot.

The receiving side verifies the operation and co-signs the state, returning it
in an `deposit_signed` message.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```


### `deposit_signed`

Message code: 12

This is an acknowledgement of a preceding `deposit_created` message (see
above). Upon receipt of a co-signed state, the receiver verifies that it is
indeed the state resulting from the proposed deposit operation. The
`channel_deposit_tx` is then pushed to the chain, and the requisit number of
confirmations (`minimum_depth`) are awaited. Once confirmation has been
received, a `deposit_locked` message is sent, with the hash of the
`channel_deposit_tx` transaction.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

### `deposit_locked`

Message code: 13

This message is sent upon receipt of a `minimum_depth` confirmation for a
`channel_deposit_tx` transaction. The payload is the hash of the
`channel_deposit_tx` transaction object. Once the message has been sent,
the channel returns to the `open` state and the new off-chain state is
useable.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

### `deposit_error`

Message code: 14

Since both sides may initiate a `deposit_created` request, it is possible
that both may do so at roughly the same time. In particular, in the `epoch`
system, if a `deposit_created` request arrives while the fsm is waiting for
its client to sign a new state update, it reverts both its own update attempt
and the other participant's update request by sending a `deposit_error` message.
The `round` element signifies the round of the fallback state, which must
be the last mutually signed state. The receiver does not reply.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| round                | 4  |
 ---------------------- ----
```


### `withdraw_created`

Message code: 15

In order to withdraw coins from the channel, one party can initiate
a `withdraw_created` request. The payload is a singly signed
`channel_withdraw_tx` object, which includes the state hash and round of the
next off-chain state, after applying a withdrawal operation with the expected
amount. The initiating side can only withdraw coins from its own off-chain
account in the channel state (same public key) to its own on-chain account.
Note that it is possible to withdraw a zero amount, essentially making the
operation an on-chain snapshot.

The receiving side verifies the operation and co-signs the state, returning it
in an `withdraw_signed` message.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

### `withdraw_signed`

Message code: 16

This is an acknowledgement of a preceding `withdraw_created` message (see
above). Upon receipt of a co-signed state, the receiver verifies that it is
indeed the state resulting from the proposed withdrawal operation. The
`channel_withdraw_tx` is then pushed to the chain, and the requisit number of
confirmations (`minimum_depth`) are awaited. Once confirmation has been
received, a `withdraw_locked` message is sent, with the hash of the
`channel_withdraw_tx` transaction.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

### `withdraw_locked`

Message code: 17

This message is sent upon receipt of a `minimum_depth` confirmation for a
`channel_withdraw_tx` transaction. The payload is the hash of the
`channel_withdraw_tx` transaction object. Once the message has been sent,
the channel returns to the `open` state and the new off-chain state is
useable.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

### `withdraw_error`

Message code: 18

Since both sides may initiate a `withdraw_created` request, it is possible
that both may do so at roughly the same time. In particular, in the `epoch`
system, if a `withdraw_created` request arrives while the fsm is waiting for
its client to sign a new state update, it reverts both its own update attempt
and the other participant's withdraw request by sending a `withdraw_error`
message. The `round` element signifies the round of the fallback state, which
must be the last mutually signed state. The receiver does not reply.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| round                | 4  |
 ---------------------- ----
```

## Other interaction

### `inband_message`

Message code: 96

Inband messages are arbitrary messages sent between the channel participants.
The payload must be limited to 65,535 bytes. The fsm must deliver an inband
message immediately, and the receiver must process it (e.g. conveying it to
the client) immediately, preserving the message ordering.

One possible use of inband messages could be to synchronize off-chain state
updates, but any application is allowed.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

## Channel closing


### `leave`

Message code: 94

While it is possible to simply drop out of a channel and later reestablish it,
the success of the reestablishing operation depends on the other party keeping
the most recent copy of the state. The polite way to ensure this is to send
a `leave` request. The receiving side is expected to respond with a `leave_ack`.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
```


### `leave_ack`

Message code: 95

This message is sent in response to a `leave` request. The sender may terminate
its side once the message has been delivered. The receiver should wait for
the `leave_ack` before it terminates.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
```

### `shutdown`

Message code: 98

In order to close the channel in an orderly fashion, a `shutdown` message
is sent, passing a singly signed `channel_close_mutual_tx` transaction object
as payload. The sender creates the `channel_close_mutual_tx` from the latest
co-signed state, including the root hash of the corresponding state tree.
The receiver must verify that the payload corresponds to its latest co-signed
state, and then replies with a `shutdown_ack` message.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

### `shutdown_ack`

Message code: 99

This message is sent in response to a verified `shutdown` message. The sender
may close once the message has been delivered. The receiver must, after
verifying the payload of the `shutdown_ack` message (which must be the same
`channel_close_mutual_tx` object, co-signed), push the `channel_close_mutual_tx`
transaction onto the chain, and then terminate.

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| length               | 2  |
 ---------------------- ----
| data                 | N  |
 ---------------------- ----
```

## Channel closing

A channel can be closed under three circumstances:

1. Both parties agree to the close and sign the closing transaction together,
   which then gets broadcasted and included in the blockchain.
2. One party wants to close the channel: the other party might had been missing
   for some time or had been trying to cheat. In this case either side can publish 
   the latest state signed by both parties and claim their balance after the
   negotiated timeout.
3. A malicious party tries to publish an outdated state, which it prefers over a
   later state. In this case the honest party can publish a state signed by both
   with a higher round and thereby prove that the other one is trying to cheat.
   A transaction with a higher round overwrites the one with a lower one.

In the case that both parties decide to close the channel, funds are accessible
immediately after the transaction of their agreement is included in a block,
otherwise they have to wait at least `lock_period` blocks for disputes.

```
A                       B
|                       |
|----   shutdown    --->|
|<---   shutdown    ----|
|          .            |
|          .            |
|  resolve pending op   |
|          .            |
|          .            |
|          .            |
|<-- closing_created ---|
|--- closing_signed  -->|
|                       |
```

In case of both parties want to close the channel in agreement and
there are enough coins left in the channel to pay for the fee, then the
the advised distribution of returning the coins left in the channel is
as follows:

```
if initiator_amount + responder_amount < fee
  return error
else if initiator_amount >= ceil(fee/2) && responder_amount >= floor(fee/2)
  initiator_final := initiator_amount - ceil(fee/2)
  responder_final := responder_amount - floor(fee/2)
else if responder_amount >= ceil(fee/2) && initiator_amount >= floor(fee/2)
  responder_final := responder_amount - ceil(fee/2)
  initiator_final := initiator_amount - floor(fee/2)
else if initiator_amount > responder_amount
  initiator_final := initiator_amount - fee + responder_amount
  responder_final := 0
else
  responder_final := responder_amount - fee + initiator_amount
  initiator_final := 0
  ```

This is an example distribution of the fee. If this is to be accepted as a
norm - it means that one of the parties will propose these final amounts in the
closing transaction and the other, also following this advise, will
happily sign it.
What ends up on-chain is the fee and the closing amounts of
the parties. The process by which they got to agreement is not part of the
protocol itself.


### `shutdown`

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
```


The `shutdown` message initiates the closing of a channel and can be sent by
either party. After a party sends the `shutdown` message, it MUST NOT propose any
more update messages.


#### Requirements

A shutdown cannot be initiated before the on-chain channel opening is signed.

The initiator MUST NOT send a `shutdown` before a `funding_created` and the responder MUST NOT send a `shutdown` before a `funding_signed` has been sent.
Prior to the respective points parties can still safely abort the procedure
without having committed to anything.

### `closing_created`

If the parties agree to a shutdown then they both need to sign the `channel_close_mutual`
transaction

### `closing_signed`


## Local state

Parties need to store local state in order to be able to keep track of state
channel operations.

- `chain_hash`
- `initiator_pubkey`
- `responder_pubkey`
- `initiator_amount`
- `responder_amount`
- `channel_active`
- `round`
- `updated_at`
- `closed`
- [{}]

## Contracts

Execution of a contract inside a state channel requires parties to be able to
initialise a virtual machine to run their smart contracts in.

Contracts are executed in rounds, which are denoted by `round` attribute.

Every party executes each smart contract locally and checks if the signed states
they receive match up with theirs. In the case that states and signatures are
valid, they apply the update and then send out their signature. If there was an
error in either the execution of the contract or the signature does not match
the state, they send a new update with the prior state but an increased round
number—to avoid confusion–and their signature over it, to signal that something
went wrong.

When operating in co-signing mode, contracts might need to be written in a way
to avoid the free option problem.

### On-chain enforcement

- submit code, state, inputs
- code should output new distribution of balances?
- submit a hash of what is expected to be the root of the new state
- parties could choose to continue from there

With on chain enforcement of contracts it becomes possible to unilaterally force
progress by publishing contract, state and input on chain. A miner would then
execute the contract given the state and inputs to produce a new state. This new
state could then either be used for both parties to continue operation from there
or leave it at that.

### Contracts lifecycle

Contracts are part of the [update](#state-update) mechanism: it is different
updates that are being used. Serialization of those can be found [here](../serializations.md#channel-off-chain-update).

First one participant initiates an update round containing a [channel create
contract update](../serializations.md#channel-off-chain-update-create-contract). It contains all the
information needed for a contract creation. The other participant co-signs
the changes and the contract is considered to be created.

After a contract is created it can be called. For this one of the participants
initiates an update round containing a [channel call
contract update](../serializations.md#channel-off-chain-update-call-contract).
It contains all the information needed for a contract call, including the
contract address. The other participant co-signs the changes and the contract
call is considered to be executed. Its results can be extracted from the calls
tree in the state tree.
Part of the call is the `amount` a participants commits to the contract. This
is not to be confused with [gas consumption](#gas-consumption) - `amount` are
the tokens moved from the caller's off-chain balance to the off-chain balance
of the contract been called.

### Contracts referring to on-chain data

Contracts being used in channels off-chain calls have the exact same semantics
as [those being used
on-chain](/contracts/contract_transactions.md#contract-call-transaction). Because of the different environment however,
off-chain callsoff-chain calls  might have different results as the on-chain ones.

Since there is no single source of truth, each participant considers their
current view of the chain to be the correct one. This is essential for the
trustless environment. Every off-chain contract call is based on the top of
the chain, as it is seen by each participant. This could cause some differences
in local contract executions. If those can not be resolved, participants can
always rely on the blockchain as an arbiter by using forcing of progress. Then
the top is used as it is seen by the Bitcoin-NG leader.

It is worth mentioning that both local contracts' executions and the forced
progress ones must be fully deterministic and this implies some restrictions
on using on-chain objects in the off-chain contracts.
This is especially true for the chain-related primitives (e.g. coinbase,
timestamp, block height, difficulty). Please refer to the documentation of the
applicable VM version. Registration and updates of names or asking of oracles
is impossible in the off-chain contract calls.

Using on-chain contracts in off-chain ones is a tricky task. On-chain
contracts reference-count contracts that refer to them. They can be deleted
from the blockchain only once they are no longer referenced by any other
contract.
This can not be enforced for off-chain contracts because there is no knowledge
of them on-chain. Also if we were to use an on-chain contract referencing it
by a registered name, the name on-chain could be changed to point to another
different contract. This opens a security hole especially if one of the
participants is in control of the name.
For these reasons off-chain contracts are not allowed to use on-chain ones,
not even stateless on-chain contracts. Participants can still use well-known
contracts that are present on-chain but they have to copy them into their
off-chain state. That way participants take care of their own data in a
trustless manner - they don't have to rely on other entities keeping contracts
on-chain for them.

### Gas consumption

While making off-chain updates that both parties co-sign, no gas is being
consumed. It is worth mentioning that although contract call updates do include
values for the gas limit and the gas price, those are ignored. Assumption is
that since both participants are executing the contracts locally, they are
equal in their energy consumption.

When a dispute arises and a contract is to be called on-chain, the miner that
includes the transaction should be compensated for the energy used. That's why
when forcing progress of off-chain contract calls gas is consumed. Gas limit
and gas prices are specified in the contract call update itself. Now the
values not being used off-chain come into play. Since the force progress is an
unilateral act, it is the forcer that specifies them and it is the forcer's
on-chain balance that is paying for the consumed gas.
