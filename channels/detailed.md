# State channels detailed description 

This document provides a detailed description of how state channels work.
While the [README.md](./README.md) answers the question _why_, this document
focuses on all the _how_-s. The provided State Channels WebSocket API is
described [here](../api/channels_api_usage.md).

## Table of Contents

- [Overview](#overview)
	- [On-chain transactions](#on-chain-transactions)
	- [Off-chain transactions](#off-chain-transactions)


## Overview

State channels are a mechanism for scaling transaction's throughput with
processing them only by concerned parties while keeping all the trustlessness
the blockchain provides. This is achieved by having distinct transaction types
for the various actions. The protocol consists of two distinct transaction
types:
* [On-chain transactions](./ON-CHAIN.md)
* [Off-chain transactions](./OFF-CHAIN.md)
The main difference between the two is that on-chain ones update on-chain
state persisted for the channel, while the off-chain ones are much cheaper.
Except for opening and closing sequences, on-chain transactions can land
on-chain in any order and they can be based on either off-chain transactions
or on-chain ones.

### On-chain transactions

In order for a state channel to provide on-chain guarantees and especially the
dispute mechanism, it MUST comply to certain rules that are enforced on-chain
with specific transactions.
An object is kept in the blockchain for every opened state channel that has
not yet been closed. It tracks various channel-specific data. Some of the
off-chain transactions land on-chain and then the channel representation is
updated accordingly. On-chain persisted channel data includes:

* Total channel amount - it represents the total amount of tokens dedicated to
  the channel. It is initialized when the channel is opened on-chain and can
  later be updated by various transactions. At no point it can become
  negative. Channels can not create new coins.
* Channel `round` - it represents the total count of interactions in a
  specific channel. It is an integer starting with a value of 1 at channel
  open and it MUST be incremented on every state channels' state update. Using
  it we can compare off-chain channel states according to which is preceding
  which: a bigger round means a newer state.
* Channel's `state_hash` - the root of the state channel's off-chain state
  trees as last provided on-chain.

There are two types of on-chain transactions:

* Co-signed transactions are signed by all state channel participants and thus
  represent a state of a mutual agreement. They can not be disputed.
* Solo transactions are signed by just one participant and represent one's
  unilateral intention. All but the `channel_settle_tx` provide a co-signed
  state. This state might not be the latest channel's state and thus it can
  be disputed with providing a newer co-signed state and thus invalidating
  the unilateral transaction altogether. After every solo transaction a
  dispute timer is started and the channel can not be closed untill this timer
  expires.

A full list of on-chain transactions is:
* [`channel_create`](./ON-CHAIN.md#channel_create) - a co-signed transaction
  for opening a channel.
* [`channel_deposit`](./ON-CHAIN.md#channel_deposit) - a co-signed transaction
  for one participant dedicating more coins to the channel. This increases the
  channel's total amount.
* [`channel_withdraw`](./ON-CHAIN.md#channel_withdraw) - a co-signed transaction
  for one participant taking some coins out of the channel. This decreases the
  channel's total amount.
* [`channel_snapshot_solo`](./ON-CHAIN.md#channel_snapshot_solo) - a solo
  transaction for a participant or a delegate to provide a co-signed channel
  off-chain state on-chain and updating the on-chain persisted `round` and
  `state_hash`.
* [`channel_close_mutual`](./ON-CHAIN.md#channel_close_mutual) - a co-signed
  transaction for closing a state channel with an agreement. Effects are
  instant and non-disputable.
* [`channel_close_solo`](./ON-CHAIN.md#channel_close_solo) - a solo transaction
  for initiating the solo closing sequence. A participants provides a
  co-signed `state_hash` of the root of the off-chain state trees and a proof
  of inclusion for both participants' balances.
* [`channel_settle`](./ON-CHAIN.md#channel_settle) - a solo transaction for
  finalising the solo closing sequence. The latest channel state is enforced
  as a final state and tokens are redistributed accordingly. This transaction
  is final and can not be disputed.
* [`channel_force_progress`](./ON-CHAIN.md#channel_force_progress_tx) - a solo
  transaction for executing off-chain contracts on-chain. If one party is
  missing or refusing to sign a valid contract call, the other party can use
  the blockchain as an arbiter. The forcing party provides enough information
  for the contract call to be executed on-chain. A successful
  `channel_force_progress` produces on-chain the next off-chain state. From
  then on participants can either continue using it or rather base a channel
  close on it. It is worth mentioning that a malicious party can have a couple
  of on-chain produced states thus forming a chain of on-chain produced
  channel states. A co-signed off-chain channel state can replace any on-chain
  produced channel state with the same or smaller `round` thus invalidating
  all subsequent on-chain produced channel states.

### Off-chain transactions

Once a channel is established, participants can start exchanging off-chain
transactions. A basic rule would be that if a participant or participants don't
feel a need for updating on-chain persisted channel object, they should use
off-chain transactions. They cost no fee, neither they cost any gas. This
makes them much cheaper than on-chain transactions: except for electricity
and bandwidth costs, off-chain transactions are free. This makes them suitable
for various purposes, for example micro payments. Nevertheless off-chain
transactions are not a silver bullet and certain conditions like computation
heavy contracts might result in those contracts becoming too expensive to
force progress on-chain. All off-chain transactions are co-signed as to prove
participants' mutual agreement upon the change being applied.

#### Off-chain state

Each state channel has its own set of trees for keeping balances, contracts
and calls. In order to achieve a trustless communication, this set of trees
is to be kept and updated locally by all participants. Although this is not
enforced as participants are free to use any approach they want to, there are
certain expectations for the data if a channel has to touch the blockchain,
especially in a situation of a dispute.

There are a couple of important parameters of the channel's state:
* `state_hash` being the root of the channel off-chain state trees
* `round` being the total count of channel updates

Those are also persisted in the channel on-chain object as most on-chain
transactions also update the persisted object with the latest channel data.
This adds some important guarantees for disabling posting some old state in a
dispute.

#### Off-chain transaction

Changes in the channel off-chain states are done via off-chain transactions.
Each one is two-phased: one participant offers the other for a certain change
to be applied and the other either agrees or refuses. Agreement is proven by
signing the off-chain transaction itself.
It consists of:
* `channel_id` - the ID of the state channel. This is importent if this state
  update is to be brought on-chain in a dispute
* `round` - the new round to be, if the off-chain transaction succeeds. This
  MUST be the incremented previous round.
* list of updates - those are to be applied in the correct order.
* `state_hash` - the root of the channel's state trees after the updates had
  been applied to them

Co-siging such a transaction makes the updated state the new channels'
off-chain state, the `round` in the transaction is the lates round. If a
disputed arrises a honest party is to use the very latest channel state.

#### Off-chain updates

A full list of supported updates is:
* [`transfer`](../serializations.md#channel-off-chain-update-transfer) - when
  tokens are being moved from one account to another inside the off-chain
  state
* [`deposit`](../serializations.md#channel-off-chain-update-deposit) - when
  tokens are being added to an off-chain account. This modifies the total
  amount of tokens inside the channel off-chain state.
* [`withdrawal`](../serializations.md#channel-off-chain-update-withdrawal) -
  when tokens are being subtracted to an off-chain account. This modifies the
  total amount of tokens inside the channel off-chain state.
* [`create a
  contract`](../serializations.md#channel-off-chain-update-create-contract) -
  for creating a new smart contract in the channel's off-chain state
* [`call a
  contract`](../serializations.md#channel-off-chain-update-call-contract) -
  for calling an existing smart contract in the channel's off-chain state

