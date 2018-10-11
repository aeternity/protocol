# On-chain

Operating a state channel requires, at least, an initial setup via a
`channel_create` transaction, that locks up a configurable amount of coins from
each involved party in the channel. This requires consent, in the form of
signatures, from all participants.

Transactions not signed off by everyone, except the `channel_snapshot_solo`, are
subject to a `lock_period`, which is negotiated off-chain and then put into the
`channel_create` transaction. These operations are only committed after the
`lock_period` runs out, to allow others to dispute the proposed update.
Committed here means that the update can no longer be disputed.

In the ideal case, all on-chain transactions get signed off by all participants,
implying that there are no disagreements. These operations can be committed
immediately and will generally override all operations initiated unilaterally.

Each transaction updating on-chain state provides two fields essential for
future conflict resolution: `round` and `state_hash`. The state hash is the root
hash of the channel's state tree after the on-chain has been applied to the
local state tree. The `round` is the _next_ state channel internal round. Thus
the on-chain update transaction represents on-chain the next off-chain state
of the channel. This way we can solo close a channel according to the last
on-chain state. All we have to do is to provide a proof of inclusion having
the same `state_hash`.


- [Establishing a channel](#establishing-a-channel)
	+ [`channel_create`](#channel_create)
- [Updating a channel](#updating-a-channel)
	+ [`channel_deposit`](#channel_deposit)
	+ [`channel_withdraw`](#channel_withdraw)
	+ [`channel_snapshot_solo`](#channel_snapshot_solo)
- [Closing a channel](#closing-a-channel)
	+ [`channel_close_mutual`](#channel_close_mutual)
	+ [`channel_close_solo`](#channel_close_solo)
	+ [`channel_settle`](#channel_settlement)
- [Disputing updates](#disputing-updates)
	+ [`channel_slash`](#channel_slash)
- [Forcing progress on-chain](#forcing-progress)
	+ [`channel_force_progress_tx`](#channel_force_progress_tx)

- [Channel state tree](#channel_state_tree)

## Establishing a channel

All of the on-chain operations could be submitted by any peer but we assume that
the initiating peer pays for the setup of the channel. Therefore the `initiator`
MUST pay the standard transaction fees.


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
- `initiator_amount`: unsigned amount of coins the initiator commits to the
  channel
- `responder_amount`: unsigned amount of coins the responder commits to the
  channel
- `lock_period`: period for disputes after solo operations
- `delegates`: a list of delegate addresses. The delegates play a role in the
  solo closing sequence: except for the participants of the channel, they are
  the only ones that can provide a slash transaction.
- `state_hash`: the root hash of the channel state tree; This is not validated,
  just kept in the channel's object
- `ttl`: blockheight target until this transaction can be included
- `fee`: transaction fee
- `nonce`: `initiator`'s account nonce


The length of the `lock_period` is a trade-off between responsiveness, e.g. how
fast solo operations can be committed, and security. Choosing a `lock_period`
that gives participants enough time to react to potential malicious solo
operations is crucial.

The `ttl` is in absolute chain height. The involved parties will want to set the
`ttl` to a value quite a bit larger than the present chain height, to avoid
uncertainty. If the fees included are low and transaction pressure is high, then
the transaction might end up being stuck in the mempool for an extended period.
`ttl` is optional, no `ttl` means a transaction that is valid "forever".

The `fee` and `nonce` refer to the `initiator` account, i.e. the `fee` MUST be
taken from their balance and the `nonce` of their account MUST be incremented.


#### Requirements

`Account(initiator).balance >= initiator_amount + fee`

`Account(responder).balance >= responder_amount`

`initiator_amount >= channel_reserve`

`responder_amount >= channel_reserve`


## Updating a channel on-chain

An update to an open channel requires the signatures of all participants and a
channel identification (`channel_id`).

Both `channel_deposit` and `channel_withdraw` MUST be signed by all involved
parties, since changing channel balances might change the dynamics of code
running in a channel.

The `channel_id` is computed from the public key of the initiator, the nonce of
the create transaction and the public key of the responder using Blake2b (256
bits digest).

```
channel_id = Blake2b(initiator || channel_create_tx_nonce || responder)
                        32                  32                  32
```


### `channel_deposit`

Depositing funds into a channel after creation should allow channels to be more
long lived due to the increased ease of balancing them out. The amount of coins
sent along with this transaction will get locked up just like the initial
deposit.

While it could be desirable to allow anyone to deposit into a channel, we are
going to restrict deposits to the peers of a channel. That means, the `from_id`
field MUST be an address of one of the participants of the targeted channel and
the standard transaction fee MUST be paid by the `from` account.

This operation is not mandatory for normal channel operation.

Serialization defined [here](../serializations.md#channel-deposit-transaction)

- `channel_id`: channel id as recorded on-chain
- `from_id`: sender of the deposit
- `amount`: amount of coins deposited
- `state_hash`: the root hash of the channel state tree after the deposit had
  been applied; This is not validated, just kept in the channel's object
- `round`: the channel's internal round that applies the deposit
- `ttl`: blockheight target until this transaction can be included
- `fee`: transaction fee
- `nonce`: `from_id`'s account nonce

Note that the `round` should be incremented on each off-chain update. This is
enforced by all on-chain transactions that have either `round` or a `payload`
(with a `round` included) must have a `round` greater of equal to the last on-
chain `round`.


### `channel_withdraw`

Channels should generally not be used to hold significant amounts of coins but
being able to withdraw locked coins might still be of use.

Serialization defined [here](../serializations.md#channel-withdraw-transaction)

- `channel_id`: channel id as recorded on-chain
- `to`: receiver of the withdraw
- `amount`: amount of coins withdrawn
- `state_hash`: the root hash of the channel state tree after the withdraw had
  been applied; This is not validated, just kept in the channel's object
- `round`: the channel's internal round that applies the withdraw
- `ttl`: blockheight target until this transaction can be included
- `fee`: transaction fee
- `nonce`: `to`'s account nonce

The `to` account MUST be a participant in the target channel. The `amount` MUST
be less or equal than the sum of all participants balances, i.e. channels cannot
create coins out of thin air. The fee is paid by the `to` account and that
account should hold enough coins to pay the fee, i.e., the fee is subtracted
before the withdrawn coins arrive.

Note that the `round` should be incremented on each off-chain update. This is enforced by all
on-chain transactions that have either `round` or a `payload` (with a `round` included) must have a
`round` greater of equal to the last on-chain `round`.


### `channel_snapshot_solo`

In order to make channels both secure and trustless even when one party goes
offline, we provide the functionality of snapshots.
Snapshots provide a recent off-chain state to be recorded on-chain. This state
is represented by a `round` and a `state_hash`. After its inclusion the channel
can not be closed using an older state—as indicated by the `round`—than the one
provided in the snapshot.


Serialization defined [here](../serializations.md#channel-snapshot-solo-transaction)

- `channel_id`: channel id as recorded on-chain
- `from_id`: the account that posts the transaction
- `payload`: co-signed off-chain state of the same channel
- `ttl`: blockheight target until this transaction can be included
- `fee`: transaction fee
- `nonce`: the `from_id` account nonce

The `from_id` account MUST be a participant in the target channel. The `payload`
MUST be a co-signed off-chain state. It MUST be part of the same channel
(containing same channel id) and it MUST have a `round` greater than the
one currently recorded on-chain.

This transaction does not trigger the `lock_period` and can not be used in
disputes.


## Closing channel on-chain

We expect channels to be only closed in the case of non-cooperation or malicious
behaviour. If all parties decide to close the channel, closing is just a matter
of issuing one on-chain transaction, signed by everyone involved.

In the case of a solo closing, operations are subject to the `lock_period`,
during which they can be disputed via a `channel_slash`.


### `channel_close_mutual`

Serialization defined [here](../serializations.md#channel-close-mutual-transaction)

- `channel_id`: channel id as recorded on-chain
- `from_id`: the account that posts the transaction
- `initiator_amount_final`: final balance for the initiator
- `responder_amount_final`: final balance for the responder
- `ttl`: blockheight target until this transaction can be included
- `fee`: transaction fee
- `nonce`: the `from_id` account nonce

`initiator_amount_final` and `responder_amount_final` are the agreed upon distribution of coins.
The initiator's and responder's account balances are incremented by
`initiator_amount_final` and `responder_amount_final` respectively.
The channel must have enough total coins to pay for the fee as well as the
agreed upon amounts. The total of a channel is computed by adding the amounts of
the initiator and responder (before the close) and the fee.


#### Requirements

This transaction MUST have valid signatures of all involved parties.

This transaction MUST NOT be disputed and any ongoing dispute MUST be considered
resolved by this transaction.

After this transaction has been included in a block, the channel MUST be
considered closed and allow no further modifications.

`channel total ==
  transcation initiator_amount_final + responder_amount_final + fee`


### `channel_close_solo`

In order to close a channel unilaterally, a participant has to send a
`channel_close_solo` transaction. This is only necessary if one peer stops
responding but can also be used by an malicious peer trying to close a channel
with a state that hasn't been agreed on by all participants.

At any point a channel participant can initiate the solo closing sequence.
After the `channel_close_solo` is posted and included in the chain a
`lock_period` block height timer is started.
This lock period is required to give the other party an opportunity to dispute
the state, that the closing sequence is based on. This can be done via the
`channel_slash` and `channel_force_progress_tx` transactions.

With the inclusion of this transaction on-chain, the timer, during which
disputes in the form of `channel_slash` will be considered, is started.

Serialization defined [here](../serializations.md#channel-close-solo-transaction)

- `channel_id`: channel id as recorded on-chain
- `from_id`: participant of the channel that posts the closing transaction
- `payload`: empty or a transaction proving that the proof of inclusion is part
  of the channel
- `poi`: proof of inclusion
- `ttl`: blockheight target until this transaction can be included
- `fee`: transaction fee
- `nonce`: taken from the `from_id`'s account

Proof of inclusion represents the channel's internal state. At the bare minimum
it has to include all accounts and their balances. It must provide enough
information to close the channel. Miners are to check balances in it and use
this data to update the channel's on-chain representation. This is how the
poster initiates the solo closing sequence.
If there are any contracts in the channel and those have balances of their own,
they are not provided in the proof of inclusion but they are rather to be force-
pushed in subsequent transactions. It is up to participants to decide if they
want to post them at all. Thus the accumulative balances of the accounts in the
solo-close transaction can be lower than the channel balance persisted on-chain.

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
If the payload is empty, the channel is closed according to the last on-chain
transaction. In this case the proof of inclusion root must be equal to the one
persisted for the channel on-chain.
If the payload is a transaction it MUST be a channel_offchain_tx. It MUST be co-signed.


### `channel_settle`

The settlement transaction is the last one in the lifecycle of a channel, but
only required if the parties involved did not manage to cooperate when trying
to close the channel. It has to be issued after all possible disputes are
resolved to then redistribute the locked coins.

The `channel_settle` MUST only be included in a block if:

- a `channel_close_solo` transaction was published and has expired, i.e.
`blockheight(top) - blockheight(channel_close_solo_tx) >= lock_period`
- there are no open disputes, which means that the channel is not currently
  locked from a prior solo action

Serialization defined [here](../serializations.md#channel-settle-transaction)

- `channel_id`: channel id as recorded on-chain
- `from_id`: participant of the channel that posts the settling transaction
- `initiator_amount_final`: unsigned amount of coins the initiator gets from the
  channel
- `responder_amount_final`: unsigned amount of coins the responder gets from the
  channel
- `ttl`: blockheight target until this transaction can be included
- `fee`: transaction fee
- `nonce`: taken from the `from_id`'s account


#### Requirements

After this transaction has been included in a block, the channel MUST be
considered closed and allow no further modifications.

The transaction MUST be signed using private key corresponding to the public key `from_id`.

The amounts must correspond to the ones on-chain, provided by the last
`channel_close_solo` or `channel_slash`.


## Disputing updates

Disputes should be considered anomalies, which only happen whenever one party
tries to unilaterally publish an outdated state when:

- closing a channel unilaterally
- forcing progress
- or slashing

All of these events trigger the `lock_period`, during which they can be
challenged via `channel_slash` and `channel_force_progress_tx`.

Since disputes can themselves be challenged, we could end up in situations,
where a malicious party progresses rounds rapidly depriving the other party of
the ability to dispute. To prevent this situation we can either:

1. enforce each dispute to always have to wait for the `lock_period` to expire
   and have only one dispute per period
2. or not restrict the number consecutive disputes but always have the option of
   disputing the first element of the chain of disputes, invalidating the full
   chain. In other words, the chain of updates or disputes only ends after its
   last `lock_period` expires.

We choose to use the second strategy because it allows faster progress in the
case of a peer that disappeared while still guaranteeing safety. This makes
keeping track of the proper states more complex but we assume a peer
disappearing has a higher likelihood than being actively malicious. Therefore
we try to optimise for that case.


### Force progress dispute example

Setup:

- Bob and Alice open a channel between each other with `lock_period := 100`
- At `chain_height := 1000` Bob posts a `channel_force_progress_tx` with a
  payload containing `round := 23`. The channel is now locked until
  `chain_height == 1100` and produces `round := 24` on chain

With strategy (2), Bob does not have to wait for the `lock_period` to expire
and can post as many `channel_force_progress_tx` as he wants, e.g. at
`chain_height := 1001` he produces `round := 25` and by `chain_height := 1011`
arrives at `round := 31`. Each subsequent operation issued bumps the
`lock_period` ahead. That is, by `chain_height == 1011` the `lock_period` is set 
to run out at `chain_height == 1111`.
Now it is important to note, that at even at `chain_height := 1110` Alice can
still dispute the *initial* update issued by Bob at `chain_height := 1000` by
providing a payload with `round := 24` or higher.


### `channel_slash`

If a malicious party sent a `channel_close_solo` or `channel_force_progress_tx`
with an outdated state, the honest party has the opportunity to issue a
`channel_slash` transaction. This transaction MUST include a state with a higher
round number signed by all peers for a successful challenge.

Serialization defined [here](../serializations.md#channel-slash-transaction)


- `channel_id`: channel id as recorded on-chain
- `from_id`: channel participant or delegate that posts the slashing transaction
- `payload`: transaction proving that the proof of inclusion is part of the
  channel
- `poi`: proof of inclusion
- `ttl`: blockheight target until this transaction can be included
- `fee`: transaction fee
- `nonce`: taken from the `from_id`'s account

The proof of inclusion represents the channel's internal state. It has to
include both participants' accounts and their balances.
If there are any contracts in the channel and those have balances of their own,
they are not provided in the proof of inclusion but they are rather to be force
pushed in subsequent transactions. It is up to participants to decide if they
want to post them at all. Thus the accumulative balances of the accounts in the
slash transaction can be lower than the channel balance persisted on-chain.

Payload is a valid transaction that has:

* `state_hash` equal to the proof of inclusion's root hash
* `channel_id` being the same as the transaction `channel_id`
* `round` being greater than the last on-chain `round` for that channel id. If
  the last on-chain transaction had been produced by forced progress, the
  `round` can also be equal to it. In this case the co-signed payload overwrites
  the on-chain produced single-signed force progress

The payload can be either empty or a signed transaction.
If the payload is empty, the channel is closed according to the last on-chain
transaction. In this case the proof of inclusion root must be equal to the one
persisted for the channel on-chain.
If the payload is a transaction it MUST be a channel_offchain_tx. It MUST be co-signed.


#### Requirements

MUST be signed using private key corresponding to the public key `from_id`.


## Forcing progress on-chain

Forcing progress is the mechanism to be used when a dispute arises between
parties and one of them wants to use the blockchain as an arbiter. The poster
provides enough state so that an off-chain contract can be executed on-chain and
thus producing the channel's next off-chain state.

This can happen both while a channel is closing or while it is still active. If
the channel is not closing, participants can continue using it from the on-chain
produced state or initiate a closing. If the channel is already closing, the
force-progress updates what are the currently expected closing amounts for each
participant (according to the contract's execution).

The force progress is based on what is considered to be the latest off-chain
state. We have no way of proving that this is the case so there is a time frame
provided for the other participant to dispute it. This time frame is measured in
block height and it works exactly like the `lock_period` does for closing
sequences. A new force progress can not be posted until a certain chain height
is reached. The value of the block height timer is the same as the one of the
`lock_period`.

It is worth mentioning that what is to be disputed is the off-chain state that
the force progress had been based on but not the forcing of progress itself. If
an older state had been provided by the forcing party, the other party can post
a newer co-signed off-chain state (via a snapshot for example). The co-signed
state with the same or greater round will replace the on-chain produced one.
This is to address the possible attack of a malicious actor making a couple of
subsequent force pushes so even if one started from some old state, eventually a
`round` number is produced greater than the one co-signed off-chain.


### `channel_force_progress_tx`

The `channel_force_progress_tx` can be included in a block if either the last
on-chain transaction for the targeted channel is not a force progress one or
the block height timer for force progressing had passed.

It consists of:

- `channel_id`: channel id as recorded on-chain
- `from_id`: participant of the channel that posts the force progress transaction
- `payload`: empty or a transaction proving that the proof of inclusion is part of the channel
- `round`: channel's next round
- `update`: channel off-chain update that contains the contract call with gas
  limit and gas prices to be consumed for the on-chain execution
- `state_hash`: channel's expected new root hash of off-chain state trees
- `addresses` - a list of ids for accounts and contracts provided in the proof
  of inclusion
- `poi`: proof of inclusion for the old channel state
- `ttl`: blockheight target until this transaction can be included
- `fee`: transaction fee
- `nonce`: taken from the `from_id`'s account

Proof of inclusion represents the internal channel state. It has to include all
accounts, all contracts and their balances.
Based on this structure, the next `state_hash` is going to be computed, thus
providing insufficient set of accounts and contracts provided will result in a
different channel `state_hash`.

The payload can be either empty or a signed transaction.
If the payload is empty, the last on-chain persisted state is used. In this case
the proof of inclusion root hash must be equal to the one persisted for the
channel on-chain. The round being used is the one stored in the channel on-
chain.
If the payload is a transaction it MUST be a `channel_offchain_tx`. It MUST be
co-signed.

An off-chain transaction payload is a valid transaction if it has:

* `state_hash` equal to the proof of inclusion's root hash. This is a proof
  that the PoI is a correct one
* `channel_id` being the same as the transaction `channel_id`
* `round` being greater to the last on-chain `round` for that channel id.

The round MUST be the incremented by one `round` provided in the `payload`.
The update MUST be a call to a contract. The caller of this update MUST be the
poster of the force progress transaction. `amount`, `gas` and `gas_price` are
specified in the update as well. The gas fees are going to be paid by the poster
of the transaction.
The state_hash will be the root hash of the updated channel's state trees. After
applying the contract call to the provided `poi` and updating accounts
accordingly, a new channel's state tree is produced. It SHOULD have the same
value of root hash as the state hash. If those do not match the force progress
fails but since this can only be determined after the call had been executed, a
call object is added on-chain and gas is consumed.

Serialization defined [here](../serializations.md#channel-solo-force-progress-transaction)


#### Force progress side effects

##### Updating channel object

Channel state trees are recreated according to the `poi` being provided. The
update is an off-chain contract call. It is applied on the channel's state trees
and modifies them. The modified trees have a root hash. It might be:

- equal to the `state_hash` provided in the force progress transaction. This hash
  indeed is the expected result of the contract call and the blockchain has
  confirmed it. The on-chain channel object is updated accordingly:
  - channel's state hash is updated to be the newly computed one
  - channel's round is the one in the force progress transaction
  - if the channel had been in a closing state, closing balances of
    participants are updated according to the ones in the modified channel state
    trees
- not equal to the `state_hash` provided in the force progress transaction. The
  hash provided was not confirmed to be the expected one. In this case the force
  progress fails and no new state channel state is created. The on-chain channel
  object is NOT modified and thus - the `round` and `state_hash` as stored
  on-chain remain unchanged. Gas is still consumed and a call object is created
  on-chain. 

A special case would be the forcer providing an invalid update call to be forced.
Examples for an invalid update calls would be:

* A remote call to a missing contract
* Spending too much coins in the call so a participants's off-chain balance
  goes bellow the `channel_reserve` threshold
* Contract call being terminated due to a `out_of_gas` exception

In this case the contract can not be executed and the forcing of progress
fails to produce a new state. The end result is exactly the same as if there
had been a mismatch of the produced `state_hash` and the expected one.

##### Call object

If the `channel_force_progress_tx` is a valid one - the contract call in the
`update` is executed upon the MPT that had been produced by the `poi`. The
output is a new MPT that will represent the new off-chain channel state.
Participants are to either continue using the channel or close it. If there
is no later off-chain update, they are expected to use this produced MPT in both cases.

The contract execution consumes gas. The `update` itself defines both the gas
limit and the gas price. After the contract call has been executed and the real
gas consumption has been calculated, the balance of the account posting the
transaction is updated to pay the gas fee. Since this is not a co-signed
transaction but rather a unilateral one, the initiator of the progress
enforcement pays the fees.

The contract call produces on-chain a new call object in the on-chain state
trees for contract calls. Usually calls have a key that is composed by the
contract's address, the caller's address and the caller's nonce. Since the off-
chain contract is not persisted on-chain, it does not have an address that can
be used in that manner. The calls produced by forcing progress use the
`channel_force_progress_tx`'s hash instead.

Since the miner is expending resources for the contract's execution, the gas
fees are paid and the call object is created for every force progress, no matter
if it was successful to update the on-chain channel object or not.


## Channel state tree

Each block MUST commit to a Merkle Patricia tree of open channels, where the
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

Keeping track of the `state_hash`, `round`, `closes_at`, `force_blocked_until`
and `lock_period` is necessary for nodes to be able to assess the validity of
`channel_slash` and `channel_settle` transactions.

Serialization defined [here](../serializations.md#channel)


