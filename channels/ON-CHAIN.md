# On-chain

- [Establishment](#establishing-channel-on-chain)
	- [`channel_create`](#channel_create)
- [Updates](#updating-channel-on-chain)
	- [`channel_deposit`](#channel_deposit)
	- [`channel_withdraw`](#channel_withdraw)
	- [`channel_snapshot_solo`](#channel_snapshot_solo)
- [Closing](#closing-channel-on-chain)
	- [`channel_close_mutual`](#channel_close_mutual)
	- [`channel_close_solo`](#channel_close_solo)
	- [`channel_slash`](#channel_slash)
	- [`channel_settle`](#channel_settlement)
- [Force progress](#force-progress-on-chain)

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

Each on-chain updating transaction provides two fields that are essential for
future conflict resolution: `round` and `state_hash`. The state hash is the
root hash of the channel state tree after the on-chain has been applied to the
local state tree. The `round` is the _next_ state channel internal round. Thus
the on-chain update transaction represents on-chain the next off-chain state
of the channel. This way we can solo close a channel according to the last
on-chain state. All we have to do is to provide a proof of inclusion having
the same `state_hash`.

## Establishing channel on-chain

All of the on-chain operations could be submitted by any peer but we assume that
the initiating peer pays for the setup of the channel. Therefore the `initiator`
MUST pay the standard transaction fees.

(***TODO***: should fees be directly be deducted from channel balance?)
(***TODO***: should a third party be able to open a channel for others?)


### `channel_create`

The `channel_create` transaction is used to register a channel on-chain and its
inclusion on-chain causes the specified amounts to be locked up.

e.g.

```
Account(initiator).balance := Account(initiator).balance - initiator_amount

Account(responder).balance := Account(responder).balance - responder_amount

Channel(cid).amount := initiator_amount + responder_amount
```

Serialization defined [here](../serializations.md#channel-create-transaction)

- `initiator`: public key/address of the initiating peer
- `responder`: public key/address of the responding peer
- `initiator_amount`: unsigned amount of tokens the initiator commits to the channel
- `responder_amount`: unsigned amount of tokens the responder commits to the channel
- `lock_period`: minimal block height interval between a channel_close_solo/last channel_slash transaction and the channel_settle transaction
- `ttl`
- `fee`
- `delegates`: a list of delegate addresses. The delegates play a role in the
  solo closing sequence: except for the participants of the channel, they are
  the only ones that can provide a slash transaction.
- `state_hash`: the root hash of the channel state tree; This is not validated, just kept in the channel's object
- `nonce`

The `ttl` is in absolute chain height. The involved parties will want
to set the `ttl` to a value quite a bit larger than the present chain height, to avoid
uncertainty. If the fees included are low and transaction pressure is high,
then the transaction might end up being stuck in the mempool for an extended
period. `ttl` is optional, no `ttl` means a transaction that is valid "forever".

The `fee` and `nonce` refer to the `initiator` account, i.e. the `fee` MUST be taken from their balance and the `nonce` of their account MUST be incremented.



#### Requirements

`Account(initiator).balance >= initiator_amount + fee`

`Account(responder).balance >= responder_amount`

`initiator_amount >= channel_reserve`

`responder_amount >= channel_reserve`

## Updating channel on-chain

An update to an open channel requires the signatures of all
participants and a channel identification (`channel_id`).

Both `channel_deposit` and `channel_withdraw` MUST be signed by all involved
parties, since changing channel balances might change the dynamics of code
running in a channel.

The `channel_id` is computed from the public key of the initiator, the
nonce of the create transaction and the public key of the responder
using Blake2b (256 bits digest).

```
channel_id = Blake2b(initiator || channel_create_tx_nonce || responder)
                        32                  32                  32
```

### `channel_deposit`

Depositing funds into a channel after creation should allow channels to be more
long lived due to the increased ease of balancing them out. The amount of tokens
sent along with this transaction will get locked up just like the initial
deposit.

While it could be desirable to allow anyone to deposit into a channel, we are
going to restrict deposits to the peers of a channel. That means, the `from`
field MUST be an address of one of the participants of the targeted channel and
the standard transaction fee MUST be paid by the `from` account.

This operation is not mandatory for normal channel operation.

Serialization defined [here](../serializations.md#channel-deposit-transaction)


- `channel_id`: channel id as recorded on-chain
- `from`: sender of the deposit
- `amount`: amount of tokens deposited
- `ttl`:
- `fee`:
- `state_hash`: the root hash of the channel state tree after the deposit had been applied; This is not validated, just kept in the channel's object
- `round`: the channel's internal round that applies the deposit
- `nonce`: account nonce of the submitter

Note that the `round` should be incremented on each off-chain update. This is enforced by all
on-chain transactions that have either `round` or a `payload` (with a `round` included) must have a
`round` greater of equal to the last on-chain `round`.


### `channel_withdraw`

Channels should generally not be used to hold significant amounts of tokens but
being able to withdraw locked tokens might still be of use.

The `to` account MUST be a participant in the target channel. The `amount`
MUST be less or equal than the sum of all participants balances, i.e. channels
cannot create tokens out of thin air. The fee is paid by the `to` account and that
account should hold enough tokens to pay the fee, i.e., the fee is subtracted before
the withdrawn tokens arrive.

Serialization defined [here](../serializations.md#channel-withdraw-transaction)


- `channel_id`: channel id as recorded on-chain
- `to`: receiver of the withdraw
- `amount`: amount of tokens withdrawn
- `ttl`:
- `fee`:
- `state_hash`: the root hash of the channel state tree after the withdraw had been applied; This is not validated, just kept in the channel's object
- `round`: the channel's internal round that applies the withdraw
- `nonce`: the `to` account nonce

Note that the `round` should be incremented on each off-chain update. This is enforced by all
on-chain transactions that have either `round` or a `payload` (with a `round` included) must have a
`round` greater of equal to the last on-chain `round`.

(***TODO***: should a channel be considered closed if all the tokens are taken from it?)

### `channel_snapshot_solo`

At any point of time any of the participants can initiate the solo closing sequence. After the `channel_close_solo`
is posted and included in the chain - a `lock_period` block height timer is
started. This is the time frame the other party is expected to dispute the
closing state provided in the `channel_close_solo` transaction. In order to make
channels both secure and so they operate in a trustless manner even when one is
offline, we provide the functionality of snapshots.
Snapshot is a way providing on-chain a newer state (represented by a `round`
and a `state_hash`). After it is included - the channel can not be closed
using some older state than the one being provided.

The `from` account MUST be a participant in the target channel. The `payload`
MUST be a co-signed off-chain state. It MUST be part of the same channel
(containing same channel id) and it MUST have a `round` greater than the
one currently present on-chain.

Serialization defined [here](../serializations.md#channel-snapshot-solo-transaction)


- `channel_id`: channel id as recorded on-chain
- `from`: the account that posts the transaction
- `payload`: co-signed off-chain state of the same channel
- `ttl`:
- `fee`:
- `nonce`: the `from` account nonce


## Closing channel on-chain

### `channel_close_mutual`


Serialization defined [here](../serializations.md#channel-close-mutual-transaction)


- `channel_id`: channel id as recorded on-chain
- `initiator_amount_final`: final balance for the initiator
- `responder_amount_final`: final balance for the responder
- `ttl`:
- `fee`:
- `nonce`: taken from the `initiator` account

`initiator_amount_final` and `responder_amount_final` are the agreed upon distribution of
tokens. The initiator's account is returned the `initiator_amount_final` and
the responder's account is returned `responder_amount_final`. The channel
must have enough total to pay for the fee as well as the agreed
amounts. The total of a channel is computed by adding the amounts of
the initiator and responder (before the close) and the fee.

#### Requirements

This transaction MUST have valid signatures of all involved parties.

After this transaction has been included in a block, the channel MUST be
considered closed and allow no further modifications.

`channel total ==
  transcation initiator_amount_final + responder_amount_final + fee`

### `channel_close_solo`

In order to close a channel unilaterally, a participant has to send a
`channel_close_solo` transaction. This is only necessary if one peer stops
responding but can also be used by an malicious peer trying to close a channel
with a state that hasn't been agreed on by all participants.

With the inclusion of this transaction on-chain, the timer, during which
disputes in the form of `channel_slash` will be considered, is started.


Serialization defined [here](../serializations.md#channel-close-solo-transaction)


- `channel_id`: channel id as recorded on-chain
- `from`: participant of the channel that posts the closing transaction
- `payload`: empty or a transaction proving that the proof of inclusion is part of the channel
- `poi`: proof of inclusion
- `ttl`
- `nonce`: taken from the `from`'s account
- `fee`

Proof of inclusion represents the channel's internal state. At the
bare minimum it has to include all accounts and their balances. It must provide enough information to
close the channel. Miners are to check balances in it and use this data to update the
channel's on-chain representation. This is how the poster initiates the solo closing sequence.
If there are any contracts in the channel and those have balances of their own - they are
not provided in the proof of inclusion but they are rather to be force-pushed in
subsequent transactions. It is up to participants to decide if they want to
post them at all. Thus the accumulative balances of the accounts in
the solo-close transaction can be lower than the channel balance persisted
on-chain.

Payload is a valid transaction that has:
* `state_hash` equal to the proof of inclusion's root hash. This is a proof
  that the PoI is a correct one
* `channel_id` being the same as the transaction `channel_id`
* `round` being greater than the last on-chain `round` for that channel id. If
  the last on-chain transaction had been produced by forced progress, chain had
  been produced by a force progress transaction - the `round` can also be equal
  to it. In this case the co-signed payload overwrites the on-chain produced
  single-signed force progress

The payload can be either empty or a signed transaction.
If the payload is empty, the channel is closed according to
the last on-chain transaction. In this case the proof of
inclusion root must be equal to the one persisted for the channel on-chain.
If the payload is a transaction it MUST be a channel_offchain_tx. It MUST be co-signed.

### `channel_slash`

If a malicious party sent a `channel_close_solo` with an outdated state, the
honest party has the opportunity to issue a `channel_slash` transaction. This
transaction needs to include a state signed by all peers with a higher sequence
number.


Serialization defined [here](../serializations.md#channel-slash-transaction)


- `channel_id`: channel id as recorded on-chain
- `from`: participant or delegate of the channel that posts the slashing transaction
- `payload`: transaction proving that the proof of inclusion is part of the channel
- `poi`: proof of inclusion
- `ttl`
- `nonce`: taken from the `from`'s account
- `fee`

Proof of inclusion represents the channel's internal state. It has to include both participant
accounts and their balances.
If there are any contracts in the channel and those have balances of their own, they are
not provided in the proof of inclusion but they are rather to be force-pushed in
subsequent transactions. It is up to participants to decide if they want to
post them at all. Thus the accumulative balances of the accounts in
the slash transaction can be lower than the channel balance persisted
on-chain.

Payload is a valid transaction that has:
* `state_hash` equal to the proof of inclusion's root hash
* `channel_id` being the same as the transaction `channel_id`
* `round` being greater than the last on-chain `round` for that channel id. If
  the last on-chain transaction had been produced by forced progress, the
  `round` can also be equal to it. In this case the co-signed payload overwrites
  the on-chain produced single-signed force progress

The payload can be either empty or a signed transaction.
If the payload is empty - the channel is closed according to
the last on-chain transaction. In this case the proof of
inclusion root must be equal to the one persisted for the channel on-chain.
If the payload is a transaction it MUST be a channel_offchain_tx. It MUST be co-signed.



#### Requirements

MUST be signed using private key corresponding to the public key `from`.

### `channel_settle`

The settlement transaction is the last one in the lifecycle of a channel, but
only required if the parties involved did not manage to cooperate when trying
to close the channel. It has to be issued after all possible disputes are
resolved and then redistributes the locked funds.

The `channel_settle` MUST only be included in a block if:

- a `channel_close_solo` transaction was published and has expired, i.e.
`blockheight(top) - blockheight(channel_close_solo_tx) >= lock_period`
- there are no outstanding `channel_slash` transactions, which means that
  either none were published or the most recent one expired



Serialization defined [here](../serializations.md#channel-settle-transaction)


- `channel_id`: channel id as recorded on-chain
- `from`: participant of the channel that posts the settling transaction
- `initiator_amount_final`: unsigned amount of tokens the initiator gets from the channel
- `responder_amount_final`: unsigned amount of tokens the responder gets from the channel
- `ttl`
- `fee`
- `nonce`: taken from the `from`'s account

#### Requirements

After this transaction has been included in a block, the channel MUST be
considered closed and allow no further modifications.

The transaction MUST be signed using private key corresponding to the public key `from`.

The amounts must correspond to the ones on-chain, provided by the last
channel_close_solo or channel_slash.

## Channel state tree

Each block MUST commit to a Patricia Merkle tree of open channels, where the
`channel_id` specifies the path.
At a leaf, nodes store information pertaining to the current state of the given
channel.

- `channel_id`
- `initiator_pubkey`
- `responder_pubkey`
- `channel_amount`
- `initiator_amount`
- `responder_amount`
- `channel_reserve`
- `state_hash`: last published state_hash 
- `round`: last published round
- `lock_period`: agreed upon locking period by peers
- `closes_at`: on-chain channel closing height
- `force_blocked_until`: on-chain channel height after which a new force
  progress can be included in a block

Keeping track of the `state_hash`, `round`, `closes_at`, `force_blocked_until` and `lock_period` is
necessary for nodes to be able to assess the validity of `channel_slash` and
`channel_settle` transactions.
Serialization defined [here](../serializations.md#channel)

## Force progress on-chain

Forcing progress is the mechanism to be used when a dispute
arises between parties and one of them wants to use the blockchain as an
arbiter. The poster provides enough state so that an off-chain contract can be
executed on-chain and thus producing the channel's next off-chain state.

This can happen both while a channel is closing or while it is still active. If the
channel is not closing - participants can continue using it from the
on-chain produced state or initiate a closing. If the channel is already
closing, the force-progress updates what are the currently expected closing
amounts for each participant (according to the contract's execution).

The force progress is based on what is considered to be the latest off-chain
state. We have no way of proving that this is the case so there is a time frame
provided for the other participant to dispute it. This time frame is
measured in block height and it works exactly like the `lock_period` does for
closing sequences - a new force progress can not be posted until a certain chain
height is reached. It is worth mentioning that what is to be
disputed is the off-chain state that the force progress had been based on but not
the forcing of progress itself. If an older state had been provided by the
forcing party, the other party can post a newer co-signed off-chain state (via a
snapshot for example). The co-signed state with the same or greater round will
replace the on-chain produced one. This is to address the possible attack of
a malicious actor making a couple of subsequent force pushes so even if one
started from some old state, eventually a `round` number is produced greater
than the one co-signed off-chain.

### `channel_force_progress_tx`

The `channel_force_progress_tx` can be included in a block if either the last
on-chain transaction for the targeted channel is not a force progress one or
the block height timer had passed.

It consists of:

- `channel_id`: channel id as recorded on-chain
- `from`: participant of the channel that posts the force progress transaction
- `payload`: empty or a transaction proving that the proof of inclusion is part of the channel
- `solo_payload`: a transaction representing the change to be applied on the
  channel's state
- `addresses` - a list of ids for accounts and contracts provided in the proof
  of inclusion
- `poi`: proof of inclusion for the old channel state
- `ttl`
- `nonce`: taken from the `from`'s account
- `fee`

Proof of inclusion represents the internal channel state. It  
has to include all accounts, all contracts and their balances.
Based on this structure, the next `state_hash` is going to be computed
thus providing insufficient set of accounts and contracts provided will result
in a different channel `state_hash`.

The payload can be either empty or a signed transaction.
If the payload is empty, the last on-chain persisted state is used. In this
case the proof of inclusion root hash must be equal to the one persisted for
the channel on-chain. The round being used is the one stored in the channel on-chain.
If the payload is a transaction it MUST be a channel_offchain_tx. It MUST be co-signed.

An off-chain transaction payload is a valid transaction if it has:
* `state_hash` equal to the proof of inclusion's root hash. This is a proof
  that the PoI is a correct one
* `channel_id` being the same as the transaction `channel_id`
* `round` being greater to the last on-chain `round` for that channel id.

The solo_payload can not be empty. It MUST be a signed transaction.
It MUST be a channel_offchain_tx

An off-chain transaction solo payload is a valid transaction if it has:
* `channel_id` being the same as the transaction `channel_id`
* `round` being the incremented by one `round` provided in the `payload`. 
* `updates` has a single update that is a call to a contract. The caller of
  this update MUST be the poster of the force progress transaction. `gas` and
  `gas_price` are specified. The gas fees are going to be paid by the poster
  of the transaction.
* `state_hash` will be the root hash of the updated channel's state trees.
  After applying the contract call to the provided `poi` and updating accounts
  accodingly - a new channel's state tree is produced. It SHOULD have the same
  root hash as the one provided in the `solo_payload`

Serialization defined [here](../serializations.md#channel-solo-force-progress-transaction)

### Force progress side effects

#### Updating channel object

A channel state trees are recreated according to the `poi` being provided. The
update provided in the `updates` of the `solo_payload` is a contract call one.
It is applied on the channel's state trees and modifies them. The modified
trees have a root hash. It might be:

- equal to the `state_hash` provided in the `solo_payload`. This hash
  indeed is the expected result of the contract call and the blockchain has
  confirmed it. The on-chain channel object is updated accordingly:
  - channel's state hash is updated to be the newly computed one
  - channel's round is the one in the `solo_payload`
  - if the channel had been in a closing state, closing balances of
    participants are updated according to the ones in the modified channel state trees

- not equal to the `state_hash` provided in the `solo_payload`. The hash
  provided was not confirmed to be the expected one. The on-chain channel
  object is NOT modified

#### Call object

If the `channel_force_progress_tx` is a valid one - the contract call in the
`solo_payload`'s `updates` is executed upon the MPT that had been produced by
the `poi`. The output is a new MPT that will represent the new off-chain
channel state. Participants are to either continue using the channel or close
it. If there is no later off-chain update, they should use this produced MPT
in both cases.

The contract execution consumes gas. The `update` itself
defines both the gas limit and the gas price. After the contract call has been
executed and the real gas consumption has been calculated, the balance of the
account posting the transaction is updated to pay the gas fee. Since this is not
a co-signed transaction but rather a unilateral one, the initiator of the
progress enforcement pays the fees.

The contract call produces on-chain a new call object in the on-chain state
trees for contract calls. Usually calls have a key that is composed by
the contract's address, the caller's address and the caller's nonce. Since
the off-chain contract is not persisted on-chain, it does not have an address
that can be used in that manner. The calls produced by forcing progress use
the `channel_force_progress_tx`'s hash instead.

Since the miner is expending resources for the contract's execution, the gas
fees are paid and the call object is created for every force progress,
no matter if it was successful to update the on-chain channel object or not.

