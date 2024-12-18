# Channel off-chain state

Payment channels are a means of scaling the on-chain transactions' throughput using the off-chain environment. They provide the means of fast off-chain transfers of coins with zero fees while keeping the same amount of safety the on-chain already provides. Their state usually consists of the latest balances participants have.

State channels enrich this with the functionality of executing smart contracts off-chain with no gas consumption. In order to achieve this, the channel must have a state that those contract calls use and update. This document describes it.

The means for achieving its goal of off-chain communication is reaching consensus. As long as participants agree that something is right, it is right for their state channel. In this sense - rules not only can be bent, they can be broken and participants can store their state in whatever structure they see fit. Although this is not a problem for off-chain consensus, it imposes a problem for using the on-chain as an arbiter in case of a dispute. In order for participants to be safely using a channel, at any point of time they should be able to unilaterally call a contract or close the channel. This relies on on-chain being able to read and - in the case of force progress - deterministically update the channel's off-chain state.

## Structure

The off-chain state has the exact same structure as the on-chain state. As described in [serialization document](../../utility-features/serializations.md#state-trees) the off-chain state consists of subtrees. Those are:

* accounts - where accounts and contract balances are stored
* contracts - where the contracts and their states are stored
* calls - where the contract call from the last update are stored. This tree is being purged at every round so the state of the channel is not enlarged by calls. This is important especially for long running channels with many calls. This has implications for forced progress transactions as if the old calls had not been purged, the `calls` tree would have a different root hash and this would lead to a different `state_hash` of the channel state
* channels - not used, must be an empty tree. Reserved for virtual state channels
* ns - not used, must be an empty tree
* oracles - not used, must be an empty tree

## State hash and round

Using the defined structure a deterministic MPTree can be formed. As it goes with MPTrees, its root hash is considered being a proof that this is the same tree. This is heavily used as most of the on-chain channel transactions and the off-chain one contain a tuple of `channel_id`, `round` and `state_hash`. This tuple is a representation of the channel's state at a certain point of time:

* `channel_id` defines the channel
* `round` is being used to order different channel states - the greater the `round`, the newer the state
* `state_hash` is the root of the State Channel's MPTree of MPTrees

A transaction that has all three defines the channel's state at a certain point of time. This is only valid when this transaction is authenticated by both participants. The only exception is the `channel_force_progress_tx` that has all three elements but is unilaterally authenticated. It is worth noting that the `channel_force_progress_tx` is based on either a co-authenticated transaction or another forced progress.
