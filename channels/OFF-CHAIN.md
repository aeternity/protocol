# Off-chain

## Messages

- [Control messages](#control-messages)
	- [`error`](#error)
	- [`ping`/`pong`](#ping_pong)
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


## Control messages


### `error`

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

In order to establish a channel both peers need to agree on the initial
conditions, e.g. funding amounts, minimum reserve and lock time.

By default the initiator of the channel will pay the fee for the opening
transaction.


### `channel_open`

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

(***TODO***: should the initiator send along fee and nonce as well so that the
responder can assemble the `channel_create` themselves?)

In the future state channels might exist across different chains, at which point
specifying a `chain_hash` will become meaningful.

The `lock_period` can be chosen freely. Setting it too high might lock up funds
for too long in the case of non-cooperation and setting it too low could leave
a peer without enough time to react to a malicious peer trying to unilaterally
close a channel.

Having the ability to include a `push_amount`, which credits funds to the other
peer, simplifies the common case of wanting to open a channel and pay someone
immediately. An exchange might want to send you funds via this mechanism, since
it only requires only one on-chain transaction and has the side effect of also
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
- `channel_reserve` is too large or small
- `responder_amount` is too large
- `initiator_amount` is too small


### `channel_accept`

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
| responder_pubkey     | 32 |
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


#### Requirements

*Responder*:

- `chain_hash` MUST identify the chain to be used
- `temporary_channel_id` MUST be unique between the involved peers
- `lock_period` SHOULD be sufficient time to safely publish transactions to the
  blockchain to stop a cheater
- `responder_pubkey` MUST be a valid ed25519 pubkey


### `funding_created`

In order to open a channel on chain, peers need to cooperate and co-sign the
`channel_create` transaction. The `funding_created` message is used by the
initiator to send their signature to the responder.

```
  name                  size (bytes)
 ---------------------- ----
| temporary_channel_id | 32 |
 ---------------------- ----
| signature            | 64 |
 ---------------------- ----
```


#### Requirements

*Responder*:

- MUST abort if the signature is invalid for the provided transaction data


### `funding_signed`

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

Opening a channel requires an on-chain transaction. This transaction needs to be
included in a block and, since we only have probabilistic finality, be
sufficiently confirmed, s.t. the probability of a chain re-organisation is
negligible.

This message is exchanged by both peers to signal to each other that the above
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

State updates require consent of both peers.

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
either party. After a peer sends the `shutdown` message, it MUST NOT propose any
more update messages.


#### Requirements

A shutdown cannot be initiated before the on-chain channel opening is not signed.

The initiator MUST NOT send a `shutdown` before a `funding_created` and the responder MUST NOT send a `shutdown` before a `funding_signed` has been sent.
Prior to the respective points peers can still safely abort the procedure
without having committed to anything.

### `closing_created`

If the peers agree to a shutdown then they both need to sign the `channel_close_mutual`
transaction

### `closing_signed`

### `closing_created`


## Local state

Peers need to store local state in order to be able to keep track of state
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

## Contracts

Execution of a contract inside a state channel requires peers to be able to
initialise a virtual machine to run their smart contracts in.

### Contract execution

Contracts are executed in rounds, which are denoted by sequence numbers.

Every peer executes each smart contract locally and checks if the signed states
they receive match up with theirs. In the case that states and signatures are
valid, they apply the update and then send out their signature. If there was an
error in either the execution of the contract or the signature does not match
the state, they send a new update with the prior state but an increased round number—to avoid confusion–and their signature over it, to signal that something
went wrong.

When operating in co-signing mode, contracts might need to be written in a way
to avoid the free option problem.


### Initialisation


