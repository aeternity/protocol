# On-chain

Operating a state channel requires, at least, an initial setup via a
`channel_create` transaction, that locks up a configurable amount of coins from
each involved party in the channel. This requires consent, in the form of
signatures, from all participants.

In the ideal case, all on-chain transactions get signed off by all participants,
implying that there are no disagreements. These operations can be committed
immediately and will generally override all operations initiated unilaterally.

Transactions not signed off by everyone, except the `channel_snapshot_solo`, can
be disputed via `channel_slash` and `channel_force_progress_tx` transactions.
During normal operation, these solo transactions can be disputed indefinitely.
If the channel is in the closing state, disputes have to happen within the
pre-negotiated `lock_period`, given that closure requires a bounded finality.

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
	+ [`channel_settle`](#channel_settle)
- [Disputing updates](#disputing-updates)
	+ [`channel_slash`](#channel_slash)
- [Forcing progress](#forcing-progress)
	+ [`channel_force_progress_tx`](#channel_force_progress_tx)
- [Channel state tree](#channel-state-tree)

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

- `initiator_id`: account id of the initiating peer
- `responder_id`: account id of the responding peer
- `initiator_amount`: unsigned amount of coins the initiator commits to the
  channel
- `responder_amount`: unsigned amount of coins the responder commits to the
  channel
- `lock_period`: period for disputes after solo operations
- `delegate_ids`: a list of delegate account ids. The delegates play a role in
  the solo closing sequence: except for the participants of the channel, they
  are the only ones that can provide a slash transaction.
- `state_hash`: the root hash of the channel state tree; This is not validated,
  just kept in the channel's object
- `ttl`: blockheight target until which this transaction can be included
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


## Updating a channel

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
the standard transaction fee MUST be paid by the `from_id` account.

This operation is not mandatory for normal channel operation.

Serialization defined [here](../serializations.md#channel-deposit-transaction)

- `channel_id`: channel id as recorded on-chain
- `from_id`: sender of the deposit
- `amount`: amount of coins deposited
- `state_hash`: the root hash of the channel state tree after the deposit had
  been applied; This is not validated, just kept in the channel's object
- `round`: the channel's internal round that applies the deposit
- `ttl`: blockheight target until which this transaction can be included
- `fee`: transaction fee
- `nonce`: `from_id`'s account nonce

Note that the `round` SHOULD be incremented on each off-chain update. This
means, in order for an on-chain transaction, referring to off-chain state, to
be considered valid, it MUST include a `round` bigger than the currently
recorded `Channel(channel_id).round`.

If this transaction is valid then it sets:

- `Channel(channel_id).round := round`
- `Channel(channel_id).solo_round := round`
- `Channel(channel_id).state_hash := state_hash`
- `Channel(channel_id).total_amount := Channel(channel_id).total_amount + amount`


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
- `ttl`: blockheight target until which this transaction can be included
- `fee`: transaction fee
- `nonce`: `to`'s account nonce

The `to` account MUST be a participant in the target channel. The `amount` MUST
be less or equal than the sum of all participants balances, i.e. channels cannot
create coins out of thin air. The fee is paid by the `to` account and that
account should hold enough coins to pay the fee, i.e., the fee is subtracted
before the withdrawn coins arrive.

Note that the `round` SHOULD be incremented on each off-chain update. This
means, in order for an on-chain transaction, referring to off-chain state, to
be considered valid, it MUST include a `round` bigger than or equal to the
currently recorded `Channel(channel_id).round`.

If this transaction is valid then it sets:

- `Channel(channel_id).round := round`
- `Channel(channel_id).solo_round := round`
- `Channel(channel_id).state_hash := state_hash`
- `Channel(channel_id).total_amount := Channel(channel_id).total_amount - amount`


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
- `ttl`: blockheight target until which this transaction can be included
- `fee`: transaction fee
- `nonce`: the `from_id` account nonce

The `from_id` account MUST be a participant in the target channel. The `payload`
MUST be a co-signed off-chain state. It MUST be part of the same channel
(containing same channel id) and it MUST have a `round` greater than the
one currently recorded on-chain.

This transaction MUST NOT trigger the `lock_period` and MUST NOT be used when
the channel is in the locked state. It can be used to overwrite a state produced
by a `channel_force_progress_tx` while the channel is in the open state.

If this transaction is valid then it sets:

- `Channel(channel_id).round := payload.round`
- `Channel(channel_id).solo_round := payload.round`
- `Channel(channel_id).state_hash := payload.state_hash`


## Closing a channel

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
- `ttl`: blockheight target until which this transaction can be included
- `fee`: transaction fee
- `nonce`: the `from_id` account nonce

`initiator_amount_final` and `responder_amount_final` are the agreed upon distribution of coins.
The initiator's and responder's account balances are incremented by
`initiator_amount_final` and `responder_amount_final` respectively.
The channel MUST have enough total coins to pay for the fee as well as the
agreed upon amounts. The total closing amount of a channel is computed by
adding the amounts of the initiator and responder (before the close) and the
fee. If this total closing amount is lower than the total amount coins already
dedicated to the channel, the excess of coins is [locked](../consensus/locking.md).


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

With the inclusion of this transaction on-chain, the channel enters the `locked`
state, during which the `channel_close_solo` can be disputed.

Serialization defined [here](../serializations.md#channel-close-solo-transaction)

- `channel_id`: channel id as recorded on-chain
- `from_id`: participant of the channel that posts the closing transaction
- `payload`: empty or a transaction proving that the proof of inclusion is part
  of the channel
- `poi`: proof of inclusion
- `ttl`: blockheight target until which this transaction can be included
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

The `payload` can be either empty or a signed transaction.


#### Empty payload

If the payload is empty, the last on-chain persisted state and `solo_round` are
used. In this case the proof of inclusion root hash MUST be equal to the one
persisted for the channel on-chain. If that state was produced unilaterally,
i.e. via a `channel_force_progress_tx`, making
`Channel(channel_id).round != Channel(channel_id).solo_round`, the solo close is
based on the `solo_round` and thus can still be disputed.

- `Channel(channel_id).locked_until := Block.height + Channel(channel_id).lock_period`


#### Transaction payload

If the payload is a transaction it MUST be a `channel_offchain_tx`. It MUST be
co-signed.

Payload is a valid transaction that has:

* `state_hash` equal to the proof of inclusion's root hash. This is a proof
  that the PoI is correct
* `channel_id` being the same as the transaction `channel_id`
* `round` greater than `Channel(channel_id).round`. If
  `Channel(channel_id).solo_round > Channel(channel_id).round`, then
  this close will invalidate progress produced on-chain

If true, the following changes will be made:

- `Channel(channel_id).round := payload.round`
- `Channel(channel_id).solo_round := payload.round`
- `Channel(channel_id).state_hash := payload.state_hash`
- `Channel(channel_id).locked_until := Block.height + Channel(channel_id).lock_period`


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
- `ttl`: blockheight target until which this transaction can be included
- `fee`: transaction fee
- `nonce`: taken from the `from_id`'s account


#### Requirements

After this transaction has been included in a block, the channel MUST be
considered closed and allow no further modifications.

The transaction MUST be signed using private key corresponding to the public key `from_id`.

The amounts must correspond to the ones on-chain, provided by the last
`channel_close_solo` or `channel_slash`. The sum of those final amounts form
the total closing amount of the channel. If this total closing amount is lower
than the total amount coins already dedicated to the channel, the excess of
coins is [locked](../consensus/locking.md).

## Forcing progress

Forcing progress is the mechanism to be used when a dispute arises between
parties and one of them wants to use the blockchain as an arbiter. The poster
provides the off-chain state so that an off-chain contract can be executed
on-chain and thus producing the channel's next off-chain state.

This can happen both while a channel is closing or while it is still active. If
the channel is not closing, participants can continue using it from the on-chain
produced state or initiate a closing. If the channel is already closing, the
force-progress updates what are the currently expected closing amounts for each
participant (according to the contract's execution).

The force progress is based on what is considered to be the latest off-chain
state. We have no way of proving that this state is actually up-to-date so any
progress on chain can always be disputed by providing a co-signed state with a
higher round number than the round number that the to be disputed
`channel_force_progress_tx` transaction used.

If the channel is in the closing state, issuing a `channel_force_progress_tx`
locks it for `lock_period` blocks, during which the update can be disputed. This
lock is necessary to prevent the channel from being closed immediately after
a new round has been produced on chain.

It is worth mentioning that what is to be disputed is the off-chain state that
the force progress had been based on and not the forcing of progress itself. If
an older state had been provided by the forcing party, the other party can post
a newer co-signed off-chain state (via a snapshot for example). The co-signed
state with the same or greater round will replace the on-chain produced one.


### `channel_force_progress_tx`

Serialization defined [here](../serializations.md#channel-solo-force-progress-transaction)

- `channel_id`: channel id as recorded on-chain
- `from_id`: participant of the channel that posts the force progress transaction
- `payload`: empty or a transaction proving that the state trees are part of the
  channel
- `round`: channel's next round
- `update`: channel off-chain update that contains the contract call with gas
  limit and gas prices to be consumed for the on-chain execution
- `state_hash`: channel's expected new root hash of off-chain state trees
- `offchain_trees`: the full state channel's state trees
- `ttl`: blockheight target until which this transaction can be included
- `fee`: transaction fee
- `nonce`: taken from the `from_id`'s account

The `offchain_trees` is the full off-chain state trees set: all accounts and
all contracts. It MUST include both participants' off-chain accounts.
Based on the `offchain_trees`, the next state is going to be computed and its
root hash will become the new state's `state_hash`. The newly produced state
trees will be different than the provided ones at least with the newly added
`call` object. Thus even if the contract call fails a new `state_hash` is
produced.

If this transaction is sent while the channel is in the `closing` state, it will
transition the channel into the `locked` state for the next `lock_period` blocks.

The payload can be either empty or a signed transaction.


#### Empty Payload

If the payload is empty, the last on-chain persisted state and `solo_round` are
used. In this case the state trees root hash MUST be equal to the one persisted
for the channel on-chain.

If the contract execution is successful, the channel will be updated with:

- `Channel(channel_id).solo_round := Channel(channel_id).solo_round + 1`
- `Channel(channel_id).state_hash := state_hash`

Additionally, if the channel is in the `closing` state:

- `Channel(channel_id).locked_until := Block.height + Channel(channel_id).lock_period`


#### Transaction Payload

If the payload is a transaction it MUST be a `channel_offchain_tx`. It MUST be
co-signed.

An off-chain transaction payload is a valid transaction if it has:

* `state_hash` equal to the state trees' root hash. This is a proof
  that the `offchain_trees` are something both participants had agreed upon
* `channel_id` being the same as the transaction `channel_id`
* `round` greater than `Channel(channel_id).round`

The update MUST be a call to a contract. The caller of this update MUST be the
poster of the force progress transaction. `amount`, `gas` and `gas_price` are
specified in the update as well. The gas fees are going to be paid by the poster
of the transaction.
The state_hash will be the root hash of the updated channel's state trees. After
applying the contract call to the provided `offchain_trees` and updating accounts
accordingly, a new channel's state tree is produced. It MUST have the same
value of root hash as the state hash. If those do not match the force progress
fails but since this can only be determined after the call had been executed, a
call object is added on-chain and gas is consumed.

If the contract call succeeded, the channel state will be updated:

- `Channel(channel_id).round := payload.round`
- `Channel(channel_id).solo_round := payload.round + 1`
- `Channel(channel_id).state_hash := state_hash`

Additionally, if the channel is in the `closing` state:

- `Channel(channel_id).locked_until := Block.height + Channel(channel_id).lock_period`


#### Force progress side effects

##### Updating channel object

Channel state trees are recreated according to the `offchain_trees` being
provided. The update is an off-chain contract call. It is applied on the
channel's state trees and modifies them. The modified trees have a root
hash. It might be:

- equal to the `state_hash` provided in the force progress transaction.
  This hash indeed is the expected result of the contract call and the
  blockchain has confirmed it. The on-chain channel object is updated
  accordingly:
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

A special case would be the forcer providing an invalid update call to be
forced. Examples for an invalid update calls would be:

* A remote call to a missing contract
* Spending too much coins in the call so a participants's off-chain balance
  goes bellow the `channel_reserve` threshold
* Contract call being terminated due to a `out_of_gas` exception

In this case the contract can not be executed and the forcing of progress
fails to produce a new state. The end result is exactly the same as if there
had been a mismatch of the produced `state_hash` and the expected one.


##### Call object

If the `channel_force_progress_tx` is valid, the contract call in the `update`
is executed upon the MPT that had been produced by the `offchain_trees`.
The output is a new MPT that will represent the new off-chain channel state.
Participants are to either continue using the channel or close it. If there is
no later off-chain update, they are expected to use this produced MPT in both
cases.

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


## Disputing updates

Disputes should be considered anomalies, which only happen whenever one party
tries to unilaterally publish an outdated state while:

- closing a channel unilaterally
- forcing progress
- or slashing

and can be disputed via `channel_slash`, `channel_force_progress_tx`,
`channel_snapshot_solo` transactions.

Since disputes can themselves be challenged, we could end up in situations,
where a malicious party progresses rounds rapidly via `channel_force_progress_tx`
transactions, depriving the other party of the ability to dispute. To prevent
this situation we can either:

1. enforce each dispute to always have to wait for the `lock_period` to expire
   and have only one dispute per period
2. or not restrict the number consecutive disputes but always have the option of
   challenging the first element of any chain of disputes, invalidating the full
   chain.

We choose to use the second strategy because it allows faster progress in the
case of a peer that disappeared while still guaranteeing safety. This makes
keeping track of the proper states more complex but we assume a peer
disappearing has a higher likelihood than them being actively malicious.
Therefore we try to optimise for that case.


### Force progress dispute with closing channel

If the channel is in the closing state, which only happens via a
`channel_close_solo`, then each dispute triggers an extension of the channel
lock by `lock_period` blocks. If a channel is locked, the same rules as above
apply. That is, as many `channel_force_progress_tx` or `channel_slash`
transactions as desired can be submitted—each one extending the lock—but as long
as the channel is locked, the entire chain can be invalidated if a state with a
higher round number can be posted.

Having the lock is necessary here because otherwise a malicious party might post
a `channel_force_progress_tx` or `channel_slash` containing an outdated state
and then immediately try to have the channel be settled based on the result.


### Force progress dispute with open channel example

Setup:

- Bob and Alice open a channel between each other with `lock_period := 100`
- At `chain_height := 1000` Bob posts a `channel_force_progress_tx` with a
  payload containing `round := 23` and  produces `round := 24` on chain
- The channel state will now contain 23 as the latest `round` and 24 as
  the `solo_round`

With the selected strategy, Bob does not have to wait for the `lock_period` to
expire and can post as many `channel_force_progress_tx` as he wants, e.g. at
`chain_height := 1001` he produces `solo_round := 25` and by `chain_height := 1011`
arrives at `solo_round := 31`. The `round` is still at 23.

Now if Alice returns at `chain_height := 1110`, she can still dispute the
*initial* update issued by Bob at `chain_height := 1000` by providing a
co-signed payload with `round := 24` or higher via either a `channel_force_progress_tx`
or a `channel_snapshot_solo`.


### Force progress dispute with closing channel example

Setup:

- Bob and Alice open a channel between each other with `lock_period := 100`
- At `chain_height := 1000` Bob posts a `channel_close_solo` with a
  payload containing `round := 23`. The channel is now locked until
  `chain_height == 1100`

With the selected strategy, Bob has to wait for the `lock_period` to expire, if
he wants to settle the channel. But while the channel is locked, he can still
post as many `channel_force_progress_tx` as he wants, e.g. at
`chain_height := 1001` he produces `solo_round := 24` and by `chain_height := 1011`
arrives at `solo_round := 31`. Each subsequent operation issued bumps the
`lock_period` ahead. That is, by `chain_height == 1011` the `lock_period` is set
to run out at `chain_height == 1111`.

Now it is important to note, that at even at `chain_height := 1110` Alice can
still dispute the *initial* update issued by Bob at `chain_height := 1000` by
providing a co-signed payload with `round := 24` or higher but her dispute would
bump the lock by `lock_period` too.


### `channel_slash`

If a malicious party sent a `channel_close_solo` or `channel_force_progress_tx`
with an outdated state, the honest party has the opportunity to issue a
`channel_slash` transaction. This transaction MUST include a state with a higher
`round` number than the one being disputed, signed by all peers for a successful
challenge.

Serialization defined [here](../serializations.md#channel-slash-transaction)


- `channel_id`: channel id as recorded on-chain
- `from_id`: channel participant or delegate that posts the slashing transaction
- `payload`: transaction proving that the proof of inclusion is part of the
  channel
- `poi`: proof of inclusion
- `ttl`: blockheight target until which this transaction can be included
- `fee`: transaction fee
- `nonce`: taken from the `from_id`'s account

The proof of inclusion represents the channel's internal state. It has to
include both participants' accounts and their balances.
If there are any contracts in the channel and those have balances of their own,
they are not provided in the proof of inclusion but they are rather to be force
pushed in subsequent transactions. It is up to participants to decide if they
want to post them at all. Thus the accumulative balances of the accounts in the
slash transaction can be lower than the channel balance persisted on-chain.

The payload can be either empty or a signed transaction.


#### Empty payload

If the payload is empty, the last on-chain persisted state and `solo_round` are
used. In this case the proof of inclusion root hash MUST be equal to the one
persisted for the channel on-chain. If that state was produced unilaterally,
i.e. via a `channel_force_progress_tx`, making
`Channel(channel_id).round != Channel(channel_id).solo_round`, the slash is
based on the `solo_round` and thus can still be disputed.

- `Channel(channel_id).locked_until := Block.height + Channel(channel_id).lock_period`


#### Transaction payload

If the payload is a transaction it MUST be a `channel_offchain_tx`. It MUST be
co-signed.

Payload is a valid transaction that has:

* `state_hash` equal to the proof of inclusion's root hash. This is a proof
  that the PoI is correct
* `channel_id` being the same as the transaction `channel_id`
* `round` greater than `Channel(channel_id).round`. If
  `Channel(channel_id).solo_round > Channel(channel_id).round`, then
  this slash will invalidate progress produced on-chain

If true, the following changes will be made:

- `Channel(channel_id).round := payload.round`
- `Channel(channel_id).solo_round := payload.round`
- `Channel(channel_id).state_hash := payload.state_hash`
- `Channel(channel_id).locked_until := Block.height + Channel(channel_id).lock_period`


#### Requirements

MUST be signed using private key corresponding to the public key `from_id`.


## Channel state tree

Each block MUST commit to a Merkle Patricia tree of open channels, where the
`channel_id` specifies the path.
At a leaf, nodes store information pertaining to the current state of the given
channel.

- `channel_id`
- `initiator_id`
- `responder_id`
- `delegator_ids`
- `total_amount`
- `initiator_amount`
- `responder_amount`
- `channel_reserve`
- `state_hash`: last published state_hash
- `round`: last known co-signed round
- `solo_round`: last round produced via a `channel_force_progress_tx`
- `lock_period`: agreed upon locking period by peers
- `locked_until`: on-chain channel height after which the channel can be settled

Keeping track of the `state_hash`, `round`, `locked_until`, and `lock_period` is
necessary for nodes to be able to assess the validity of `channel_slash` and
`channel_settle` transactions.

The `locked_until` is initialised with `0` and will stay `0` until the channel
enters the `closing` state.

Serialization defined [here](../serializations.md#channel)


