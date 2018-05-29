# Off-chain

## Messages

- [Overview](#overview)
- [Control messages](#control-messages)
	- [`error`](#error)
	- [`ping`/`pong`](#pingpong)
- [Establishment](#establishing-channel-off-chain)
	- [`channel_open`](#channel_open)
	- [`channel_accept`](#channel_accept)
	- [`funding_created`](#funding_created)
	- [`funding_signed`](#funding_signed)
	- [`funding_locked`](#funding_locked)
	- [`channel_reestablish`](#channel_reestablish)
- Updates
	- [`update_contract_init`](#update_init_contract)
	- [`update_exec_func`](#update_exec_fun)
	- [`update_exec_result`](#update_exec_result)
	- [`update_deposit_created`](#update_deposit)
	- [`update_deposit_signed`](#update_deposit)
	- [`update_deposit_locked`](#update_deposit)
	- [`update_withdrawal_created`](#update_withdrawal)
	- [`update_withdrawal_signed`](#update_withdrawal)
	- [`update_withdrawal_locked`](#update_withdrawal)
- Closing
	- [`shutdown`](#shutdown)
	- [`closing_created`](#closing_created)
	- [`closing_signed`](#closing_signed)


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

Each message is identified by a 1-byte message code. The size of the following message is defined by the type – see the description of each individual message type.

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
| funding_created  | 4  |
| funding_signed   | 5  |
| funding_locked   | 6  |
| update           | 7  |
| update_ack       | 8  |
| update_error     | 9  |
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
  tokens a party is to lose in case of acting maliciously
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


### `funding_created`

Message code: 4

In order to open a channel on chain, parties need to cooperate and co-sign the
`channel_create` transaction. The `funding_created` message is used by the
initiator to send their signature to the responder.

```
  name                  size (bytes)
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| transaction_data     | 32 |
 ---------------------- ----
| signature            | 64 |
 ---------------------- ----
```


#### Requirements

*Responder*:

- MUST abort if the signature is invalid for the provided transaction data


### `funding_signed`

Message code: 5

If the responder was able to validate the initiator's signature sent in the
`funding_created` message, then it should proceed to respond with its
`funding_signed` message, unless the initiator specified a `push_amount > 0` in
the `channel_open` message. In the latter case, they should wait for the
initiator to send the initial state signed by them.


```
  name                  size (bytes)
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| signature            | 64 |
 ---------------------- ----
```


### `funding_locked`

Message code: 6

Opening a channel requires an on-chain transaction. This transaction needs to be
included in a block and, since we only have probabilistic finality, be
sufficiently confirmed, so that the probability of a chain re-organisation is
negligible.

This message is exchanged by both parties to signal to each other that the above
condition has been met from their point of view and only after both of them
agree on this, can the channel be considered to be opened.


```
  name                  size (bytes)
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| transaction_id       | 32 |
 ---------------------- ----
```


#### Requirements

A node MUST NOT send the `funding_locked` message unless the `channel_create`
transaction has `minimum_depth` confirmations.

## Initialise contract

### `update_init_contract`


## State update

State updates require consent of both parties.

Each update MUST have a strictly increasing sequence number, which SHOULD start
at `0` on channel initialisation.

Parameters:

- `channel_id`:
- `balances`:
- `state`


### `update_exec_func`



### `update_exec_result`

## Deposit

Depositing funds into a channel should increase the longevity of channels, since
it makes balancing them easier but seeing as this incurs an on-chain transaction
we'd still like to avoid it, if possible.


### `update_deposit`

```
  name                  size (bytes)
 ---------------------- ----
| channel_id           | 32 |
 ---------------------- ----
| amount               | 8  |
 ---------------------- ----
```


## Withdrawal

### `update_withdrawal`

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


## Channel closing

A channel can be closed under three circumstances:

1. Both parties agree to the close and sign the closing transaction together,
   which then gets broadcast to the blockchain.
2. One party wants to close the channel or the channel gets closed due to an
   error. In this case either side can publish the latest state signed by both
   parties and claim their balance after the negotiated timeout.
3. A malicious party tries to publish an outdated state, which it prefers over a
   later state. In this case the honest party can publish a state signed by both
   with a higher nonce and thereby prove that the other one is trying to cheat.

In the case that both parties decide to close the channel, funds are accessible
immediately, otherwise they have to wait at least `lock_period` blocks.

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
- `sequence_number`
- `updated_at`
- `closed`
- [{}]

## Contracts

Execution of a contract inside a state channel requires parties to be able to
initialise a virtual machine to run their smart contracts in.

Contracts are executed in rounds, which are denoted by sequence numbers.

Every party executes each smart contract locally and checks if the signed states
they receive match up with theirs. In the case that states and signatures are
valid, they apply the update and then send out their signature. If there was an
error in either the execution of the contract or the signature does not match
the state, they send a new update with the prior state but an increased round number—to avoid confusion–and their signature over it, to signal that something
went wrong.

When operating in co-signing mode, contracts might need to be written in a way
to avoid the free option problem.

### On-chain enforcement

- submit code, state, inputs
- code should output new distribution of balances?
- parties could choose to continue from there

With on chain enforcement of contracts it becomes possible to unilaterally force
progress by publishing contract, state and input on chain. A miner would then
execute the contract given the state and inputs to produce a new state. This new
state could then either be used for both parties to continue operation from there
or leave it at that.

### Initialisation
