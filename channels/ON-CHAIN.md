# On-chain

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
- `round`: the internal channel's round that applies the deposit
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
- `round`: the internal channel's round that applies the withdraw
- `nonce`: the `to` account nonce

Note that the `round` should be incremented on each off-chain update. This is enforced by all
on-chain transactions that have either `round` or a `payload` (with a `round` included) must have a
`round` greater of equal to the last on-chain `round`.

(***TODO***: should a channel be considered closed if all the tokens are taken from it?)

## Closing channel on-chain

### `channel_close_mutual`


Serialization defined [here](../serializations.md#channel-close-mutual-transaction)


- `channel_id`: channel id as recorded on-chain
- `initiator_amount`: final balance for the initiator
- `responder_amount`: final balance for the responder
- `ttl`:
- `fee`:
- `nonce`: taken from the `initiator` account

`initiator_amount` and `responder_amount` are the agreed upon distribution of
tokens. The initiator's account is returned the `initiator_amount` and
the responder's account is returned `responder_amount`. The channel
must have enough total to pay for the fee as well as the agreed
amounts. The total of a channel is computed by adding the amounts of
the initiator and responder (before the close).

#### Requirements

This transaction MUST have valid signatures of all involved parties.

After this transaction has been included in a block, the channel MUST be
considered closed and allow no further modifications.

`channel total ==
  transcation initiator_amount + responder_amount + fee`

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

Proof of inclusion represents the internal channel. At the
bare minimum it has to include all accounts and their balances but can also
include contracts and contract calls. It must provide enough information to
close the channel. Miners are to check balances in it and use this data to initiate the
procedure of channel solo closing.

Payload is a valid transaction that has:
* `state_hash` equal to the proof of inclusion's root hash. This is a proof
  that the PoI is a correct one
* `channel_id` being the same as the transaction `channel_id`
* `round` being greater or equal to the last on-chain `round` for that channel id

The payload can be either empty or a signed transaction.
If the payload is empty - the channel is closed according to
the last on-chain transaction. In this case the proof of
inclusion root must be equal to the one persisted for the channel on-chain.
If the playload is a transaction it could be:
* channel_offchain: then it MUST be co-signed
* transaction for on-chain forcing progress on a channel's state: this is not
  yet implemented but it will be unilaterally signed

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

Proof of inclusion represents the internal channel state. At the
bare minimum it has to include all accounts and their balances but can also
include contracts and contract calls.

Payload is a valid transaction that has:
* `state_hash` equal to the proof of inclusion's root hash
* `channel_id` being the same as the transaction `channel_id`
* `round` being greater or equal to the last on-chain `round` for that channel id

The payload can be either empty or a signed transaction.
If the payload is empty - the channel is closed according to
the last on-chain transaction. In this case the proof of
inclusion root must be equal to the one persisted for the channel on-chain.
If the playload is a transaction it could be:
* channel_offchain: then it MUST be co-signed
* transaction for on-chain forcing progress on a channel's state: this is not
  yet implemented but it will be unilaterally signed



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
- `initiator_amount`: unsigned amount of tokens the initiator gets from the channel
- `responder_amount`: unsigned amount of tokens the responder gets from the channel
- `ttl`
- `fee`
- `nonce`: taken from the `from`'s account

#### Requirements

After this transaction has been included in a block, the channel MUST be
considered closed and allow no further modifications.

MUST be signed using private key corresponding to the public key `from`.

## Channel state tree

Each block MUST commit to a Patricia Merkle tree of open channels, where the
`channel_id` specifies the path.
At a leaf, nodes store information pertaining to the current state of the given
channel.

- `channel_id`
- `initiator_pubkey`
- `responder_pubkey`
- `total_amount`
- `initiator_amount`
- `channel_reserve`
- `state_hash`: last published state_hash 
- `round`: last published round
- `closes_at`: on-chain channel closing height
- `lock_period`: agreed upon locking period by peers

Keeping track of the `state_hash`, `round`, `closes_at` and `lock_period` is
necessary for nodes to be able to assess the validity of `channel_slash` and
`channel_settle` transactions.
Serialization defined [here](../serializations.md#channel)
