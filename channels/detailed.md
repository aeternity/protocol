# State channels detailed description 

## Table of Contents

- [Overview](#overview)
	- [On-chain transactions](#on-chain-transactions)
	- [Off-chain transactions](#off-chain-transactions)


## Overview

State channels are a mechanism to scale transaction's throughput with
processing them only by concerned parties while keeping all the trustlessness
the blockchain provides out of the box. Since not all channels' transactions
land on-chain, channels can be cheaper to use and could provide some privacy.
You can read more about motivation behind channels [here](./README.md). The
protocol consists of two distinct transaction types:
* [On-chain transactions](./ON-CHAIN.md)
* [Off-chain transactions](./OFF-CHAIN.md)

### On-chain transactions

In order for a state channel to provide on-chain guarantees and especially the
dispute mechanism, it MUST comply to certain rules that are enforced on-chain
with specific transactions.
A channel can never create coins on-chain. An object is kept in the blockchain
for every opened state channel that has not yet been closed. It tracks various
channel-specific data. Some of the off-chain transactions land on-chain and
then the channel representation is updated accordingly. On-chain persisted
channel data includes:

* Total channel amount - it represents the total amount of tokens dedicated to
  the channel. It is initialized when the channel is opened on-chain and can
  later be updated by various transactions. At no point it can become
  negative.
* Channel `round` - it represents the total amount of channel interactions. It
  is an integer starting with a value of 1 at channel open and it MUST be
  incremented on every state channels' state update. Using it we can compare
  off-chain channel states according to which is preceding which: a bigger
  round means a newer state.
* Channel's `state_hash` - the root of the state channel's off-chain state
  trees as last provided on-chain.

There are two types of on-chain transactions:

* Co-signed transactions are signed by all state channel participants and thus
  represent a state of a mutual agreement and can not be disputed.
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

TODO
