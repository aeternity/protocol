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

## Establishing channel on-chain

All of the on-chain operations could be submitted by any peer but we assume that
the initiating peer pays for the setup of the channel. Therefore the `initiator`
MUST pay the standard transaction fees.

(***TODO***: should fees be directly be deducted from channel balance?)
(***TODO***: should a third party be able to open a channel for others?)


### `channel_create`

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


#### Requirements

`Account(initiator).balance >= initiator_amount + fee`

## Updating channel on-chain

An update to an open channel requires the signatures of all participants.

Both `channel_deposit` and `channel_withdraw` MUST be signed by all involved
parties, since changing channel balances might change the dynamics of code
running in a channel.


### `channel_deposit`

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
- `nonce`: the transaction number of the submitting account


### `channel_withdraw`

Channels should generally not be used to hold significant amounts of coins but
being able to withdraw locked coins might still be of some use.

The `from` account MUST be a participant in the target channel. The `amount`
MUST be less or equal than the sum of all participants balances, i.e. channels
cannot create coins out of thin air.

- `channel_id`:
- `amount`:
- `from`:
- `fee`:
- `nonce`

To give an example, suppose `A` initially deposited `10` coins and `B` deposited `5` coins. Now `B` issues a `channel_withdraw` transaction, which MUST be signed
by both `A` and `B`, with `amount: 6`. Given that both peers agreed to this
value, the updated channel state would now have a balance of `9` and record.


## Closing channel on-chain

### `channel_close_mutual`

- `channel_id`:
- `amount`: signed
- `fee`
- `nonce`

`amount` is the change in balance for both peers, e.g. if the initiator sent 2
coins, then the amount should be `2`, and the final balances for both peers are
then:

`initiator_final = initiator_start + amount - fee/2`
`responder_final = responder_start - amount - fee/2`


#### Requirements

This transaction MUST have valid signatures of all involved parties.

### `channel_close_solo`

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

### `channel_slash`

If a malicious party sent a `channel_close_solo` with an outdated state, the
honest party has the opportunity to issue a `channel_slash` transaction. This
transaction needs to include a state signed by all peers with a higher sequence
number and if successful, causes the malicious party to forfeit its channel balance.

- `channel_id`:

### `channel_settle`

The settlement transaction is the last one in the lifecycle of a channel, after
all possible disputes are resolved. This transaction then redistributes the
locked funds.

The `channel_settle` MUST only be included in a block if:

- a `channel_close_solo` transaction was published and has expired, i.e.
`blockheight(top) - blockheight(channel_close_solo_tx) >= lock_period`
- there are no outstanding `channel_slash` transactions, which means that
  either none were published or the most recent one expired

- `channel_id`:

## Channel state tree

Each block MUST commit to a Patricia Merkle tree of open channels, where the
`channel_id` specifies the path.
At a leaf, nodes store information pertaining to the current state of the given
channel.

- `channel_id`
- `initiator_pubkey`
- `responder_pubkey`
- `initiator_amount`
- `responder_amount`
- `sequence_number`: last published sequence number
- `updated_at`: last on-chain update to the channel
- `lock_period`: agreed upon locking period by peers

Keeping track of the `sequence_number`, `updated_at` and `lock_period` is
necessary for nodes to be able to assess the validity of `channel_slash` and
`channel_settle` transactions.
