# Miner Signalled Consensus Upgrade

A consensus protocol upgrade based on miner signalling outcome can be referred
to as a _conditional_ consesus upgrade. A hard-fork (in the context of a
consensus protocol upgrade based on miner signalling) happens with a key block,
therefore, using the term "block" in the following text refers to a "key
block". A consensus protocol upgrade not based on any condition is
_unconditional_ protocol upgrade.

## Simple Summary

This document describes how nodes in the network signal the readiness for a new
consensus protocol, its activation, and a hard-fork at a certain height.

## Motivation

Activating a new consensus protocol based on miner signalling outcome prevents
the block chain to diverge in case a large fraction of the miners have not
upgraded their nodes to a version able to follow the new consensus protocol; or
in case the majority of the miners is against consensus protocol upgrade.

## Specification

### Overview

On a node configured for a consensus upgrade based on miner signalling outcome,
the new consensus protocol becomes active at a determined height if at least a
determined majority of the blocks between two determined block heights
(signalling interval) contains a predefined signal. Such consesus protocol
upgrade happens per chain fork.

The signalling interval has a determined number of confirmations before the
determined height at which the new consensus protocol may become active (fork
height). This is in order to:
- Prevent the node from having to aggregate the results of the signalling
  interval in a too short time interval.
- Prevent a user from restarting the node and configuring the new consensus
  protocol unconditionally when the signalling outcome is not confirmed with
  reasonably high probability.

The signal value is part of a block header in the signalling interval:
- Is meant to be a pseudorandom number, so to limit the risk of the same value
  being used by simultaneous competing consensus protocol proposals.
- Is not necessarily part of the validation rules of the new consensus
  protocol. For the sake of clarity: miner signalling is orthogonal to the
  validation rules of the new consensus protocol. This means that if the
  network reasonably settles - via miner signalling - on activating the new
  consensus protocol and a user starts a node configuring the new consensus
  protocol as unconditionally effective at the same height as the (past) miner
  signalled consensus protocol upgrade height, the node may - depending on the
  chain forks observed on the network - follow as best valid chain a chain fork
  that upgraded to the new consensus protocol at the configured height even if
  without a majority of blocks with expected signal in the signalling interval.

### Parameters

In order for the miner signalled consensus protocol upgrade to succeed, each
node participating in this protocol upgrade must have the same set of
parameters.

Assumptions:
- Let us call C1 the current consensus protocol version, and H1 the height at
  which it was first effective.

#### New consensus protocol version

The proposed new consensus protocol version.

It must be strictly greater than C1 (strictly monotonically increasing
consensus protocol version).

#### Signal

The signal value is part of a block header.

It should be pseudorandom.

#### Signalling interval start

The height at which the signalling interval starts - included. Let us call it
HS.

HS should cater for the time required by most willing miners to adopt a version
of the node able to signal and able to follow the new consensus protocol
e.g. at least two weeks.

HS must be strictly greater than H1.

#### Signalling interval end

The height at which the signalling interval ends - excluded. Let us call it HE.

HE must be strictly greater than HS.

The difference between HE and HS is recommended to be approximately a week
i.e. 3360 (`= 7 * 24 * 20`).

#### New consensus protocol height (fork height)

The height at which the new consensus protocol may be activated. Let us call it
H2.

H2 should cater for the time required by the node for aggregating the results
of the signalling interval.

H2 must be strictly greater than HE.

The difference between H2 and HE is recommended to be approximately two hours
i.e. 40 (`= 2 * 20`).

#### Majority

The number of blocks in the signalling interval (containing a signal) that
is meant to activate the new consensus protocol.

It must be positive.

It is recommended to be 90% of (HE - HS). So it is 3024 (that is - 90% of 3360)
if (HE - HS) is 3360.

NOTE: HS is included in the signalling interval and HE is excluded from it.
For example, if HS is 100 and HE is 200, there are 100 blocks between
(including HS, excluding HE) and so it is easier to define the majority,
i.e. 90 blocks out of 100 (as opposed to 99 or 101).

## Rationale

### New consensus protocol activation per chain fork

The decision is local to a chain fork, based on its height, rather than global
in the node. If it was done globally, it could not be guaranteed that the best
valid chain were the longest. So such global decision would be ineffective in
preventing chain forks with distinct consensus protocol versions from being
stored locally for the same height. As a result, the user experience would be
worse:
- By taking the decision globally, on bootstrap a node may initially follow a
  (valid) chain fork distinct from the best valid one hence take the wrong
  decision.
- As the best valid chain is not necessarily the longest one, by taking the
  decision globally, the node may anyway taint the storage with blocks with
  eventually wrong consensus protocol.

### Signal value not necessarily part of new consensus protocol

The miner signalling is orthogonal to the validation rules of the new consensus
protocol for the sake of simplicity of the implementations.

This is not detrimental as the new consensus protocol may include arbitrary
constraints.

## Implementation

### User configuration

A user may specify via the user configuration file the greatest consensus
protocol to be activated depending on miner signalling. At node startup, the
node must parse, validate and load such configuration.

#### Node restarts and configuration changes

The implementation needs to be resilient to node restarts with accidental
distinct miner signalling parameters in the configuration. For example, a user
may write an unintended miner signalling configuration, start the node, realize
that the node is running with an incorrect configuration, stop the node, fix
the configuration, then - with the same persisted storage - start (again) the
node: the node needs not to consider any potential block signal identified
under the previous incorrect configuration.

### Signalling outcome computation

A node that has configuration for miner signalled consesus upgrade must be
able to compute the signalling outcome, per given configuration, for block at
height H2 - 1.

To compute the signalling outcome:
- The implementation needs to cater for the performance of the aggregation of
the signalling e.g. slow multiple lookups on the storage.
- The implementation needs to consider that the storage may contain blocks with
the old and new consensus protocols at heights at which the new consensus
protocol should have been applied. This is because the node should be aware of
multiple chain forks and peers.

The block header field `info` is used for storing the signal in the signalling
interval.

### Blocks connected to the genesis

The conductor process is the entry point for all changes to the chain storage,
it enforces that each block being inserted is connected to the genesis. The
fork signalling outcome might not be present at fork height (the consensus
protocol is yet unknown) due to signalling outcome being computed. The
components that try to insert new blocks into the block chain (which is
controlled by the conductor process) need to handle this situation whenever:
- An untrusted block is meant to be inserted into the storage. This includes
  the cases of:
  - Sync worker process intending to add one block to the storage.
  - Gossip.
  - User HTTP API (posting a new block).
- A trusted block is meant to be inserted into the storage. These blocks are
  not validated. This includes the cases of:
  - Locally mined or signed block.
  - Mined block submitted by Stratum server (if node configured as Stratum
    server).
- A block candidate (eventually leading to a trusted block) is prepared. This
  includes the cases of key block and micro block.

### State channels

The implementation of state channels needs to ensure that the network reasonably
settles on whether to activate the new consensus protocol before accepting or
producing off-chain transaction payloads.

## Backwards Compatibility

The signalling using the block header field `info` is backward compatible, as
the meaning of the value of such field is not under consensus.

The activation of the new consensus protocol based on miner signalling is meant
to be a temporary measure during the time interval when the new protocol may be
activated on the network while the node is running. Once the network reasonably
settles on whether to activate the new consensus protocol, the user:
- Is meant to enforce such decision on the eventual node restart either by
  configuration or by upgrading the node to a new version.
- Shall be recommended to discard the persisted storage on the eventual node
  restart - as distinct persisted chain forks may have distinct consensus
  protocols at the same height.

In order to enable non-mutually authorized channel transactions to be included
on chain with mutually-authorized-agreed-offline payload, channel transactions
valid under the current consensus protocol must be valid also under the
proposed new consensus protocol.

## Possible future extensions

### Simultaneous consensus proposals

The usage of the block header field `info` offers room for optimization for
accommodating simultaneous hard-forking or soft-forking consensus proposals, by
interpreting such `info` field as a bitmask rather than a value.

### Soft-forking consensus proposals

This proposal may be extended to soft-forking consensus proposals - as opposed
to only hard-forking ones - by relaxing the strict monotonicity of consensus
versions.

Such extension should preferably be accompanied by a working implementation.
