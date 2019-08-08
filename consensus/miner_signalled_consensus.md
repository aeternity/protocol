# Miner Signalled Consensus Upgrade

## Simple Summary

This document describes the proposal of how nodes in the peer-to-peer network
may activate a new hard-forking consensus protocol based on miner signalling.

## Motivation

Activating a hard-forking new consensus protocol based on miner signalling
prevents diverging the block chain in case a large fraction of the miners have
not upgraded their nodes to a version able to follow the new consensus protocol.

## Specification

### Overview

On a node configured for a miner-signalled consensus upgrade,
per chain fork,
the new consensus protocol becomes active at a determined
height if at least a determined majority of the key blocks in a determined
"signalling" block interval in such chain fork contains a determined value in
the header field `info`.

The "signalling" block interval has a determined number of confirmations before
the determined height at which the new consensus protocol may become
active. This is in order to prevent the node from having to aggregate the
results of the "signalling" block interval in a too short time interval.

The value in the field `info` in the key block headers in the
"signalling" block interval:
- Uses the whole field `info` i.e. is not a bitmask.
- Is meant to be a pseudorandom number, so to limit the risk of the same value
  being used by simultaneous competing consensus protocol proposals.
- Is not necessarily part of the validation rules of the new consensus
  protocol.
  For the sake of clarity: the miner signalling is orthogonal to the
  validation rules of the new consensus protocol.
  This means that, if the network resonably settles - via miner
  signalling - on activating the new consensus protocol and a user
  starts a node configuring the new consensus protocol as
  unconditionally effective at the same height as the (past)
  miner-signalled consensus upgrade height, the node may - depending
  on the chain forks observed on the network - follow as best valid
  chain a chain fork that upgraded to the new consensus protocol at
  the configured height even if without a majority of "signals" in the
  "signalling" block interval.

### Parameters

In order for the miner-signalled consensus protocol upgrade to succeed, each
node must have the same set of parameters.

Assumptions:
- Let us call C1 the current consensus protocol version, and H1 the height at
  which it was first effective.

#### New consensus protocol version

The proposed new consensus protocol version.

It must be strictly greater than C1 (strictly monotonically increasing consensus
protocol version).

#### Signal

The "signal" value in the block header field `info`.

It should be pseudorandom.

#### Signalling block interval start

The height at which the "signalling" block interval starts -
included. Let us call it HS.

HS should cater for the time required by most willing miners to adopt a version
of the node able to signal and able to follow the new consensus protocol e.g. at
least two weeks.

HS must be strictly greater than H1.

#### Signalling block interval end

The height at which the "signalling" block interval ends -
excluded. Let us call it HE.

HE must be strictly greater than HS.

The difference between HE and HS is recommended to be approximately a
week i.e. 3360 (`= 7 * 24 * 20`).

#### Proposed new consensus protocol height

The height at which the new consensus protocol may be active. Let us call it H2.

H2 should cater for the time required by the node for aggregating the results of
the "signalling" block interval.

H2 must be strictly greater than HE.

The difference between H2 and HE is recommended to be approximately two
hours i.e. 40 (`= 2 * 20`).

#### Majority

The number of key blocks in the "signalling" block interval that is meant to
activate the new consensus protocol.

It must be positive.

It is recommended to be 90% of (HE - HS). So it is 3024 (that is - 90%
of 3360) if (HE - HS) is 3360.

## Rationale

### New consensus protocol activation per chain fork

The node keeps the decision to activate the new consensus protocol local to the
chain fork as taking that decision globally does not enhance the user experience
and rather worsens it.
- By taking the decision globally, on bootstrap a node may initially follow a
  (valid) chain fork distinct from the best valid one hence take the wrong
  decision.
- As the best valid chain is not necessarily the longest one, by taking the
  decision globally the node may anyway taint the storage with blocks with
  eventually wrong consensus protocol.

*NOTE: This design choice may be lifted if problematic during the implementation
 phase.*

### Value of the info field not necessarily part of new consensus protocol

The miner signalling is orthogonal to the validation rules of the new
consensus protocol for the sake of simplicity of the implementations.

This is not detrimental as the new consensus protocol may include
arbitrary constraints.

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

## (possible) Future extensions

### Simultaneous consensus proposals

The usage of the block header field `info` offers room for optimization for
accommodating simultaneous hard-forking or soft-forking consensus proposals, by
interpreting such `info` field as a bitmask rather than a value.

### Soft-forking consensus proposals

This proposal may be extended to soft-forking consensus proposals - as opposed
to only hard-forking ones - by relaxing the strict monotonicity of consensus
versions.

Such extension should preferably be accompanied by a working implementation.

## Implementation

Any implementation needs to cater for the performance of the aggregation of the
signalling e.g. slow multiple lookups on the storage.

Any implementation needs to consider that the storage may contain blocks with
the old and new consensus protocols at heights at which the new consensus
protocol should have been applied. This is because the node should be aware of
multiple chain forks and peers.

Any implementation needs to be resilient to node restarts with
accidental distinct miner signalling parameters in the configuration.
For example, a user may write an unintended miner signalling
configuration, start the node, realize that the node is running with
an incorrect configuration, stop the node, fix the configuration, then
- with the same persisted storage - start (again) the node: the node
needs not to consider any potential key block "signal" identified
under the previous incorrect configuration.

The reference implementation of the node is meant to implement this
specification. **TODO Not implemented yet.**
