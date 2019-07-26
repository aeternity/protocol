# Miner Signalled Consensus Upgrade

## Simple Summary

This document describes the proposal of how nodes in the peer-to-peer network may activate a new hard-forking consensus protocol based on miner signalling.

## Motivation

Activating a hard-forking new consensus protocol based on miner signalling prevents diverging the block chain in case a large fraction of the miners have not upgraded their nodes to a version able to follow the new consensus protocol.

## Specification

### Overview

In a chain fork, the new consensus protocol becomes active at a determined height if at least a determined majority of the key blocks in a determined "signalling" block interval in such chain fork contains a determined value in the header field `info`.

The "signalling" block interval has a determined number of confirmations before the determined height at which the new consensus protocol may become active. This is in order to prevent the node from having to aggregate the results of the "signalling" block interval in a too short time interval.

The value in the key block header field `info`:
- Uses the whole field `info` i.e. is not a bitmask.
- Is meant to be a pseudorandom number, so to limit the risk of the same value being used by simultaneous competing consensus protocol proposals.
- Is part of the validation rules of the new consensus protocol on the "signalling" block interval.

### Parameters

Let us call C1 the current consensus protocol version, and H1 the height at which it was first effective. Let us call C2 the proposed new consensus protocol version. C2 must be strictly greater than C1.

Let us call TA the number of key blocks within which the version of the node able to signal and able to follow the new consensus protocol is expected to have been adopted by most willing miners. TA must be positive.
Such number is meant to be configured by the user and to default to approximately two weeks i.e. 6720 (`= 14 * 24 * 20`).

Let us call HS the height at which the "signalling" block interval starts. HS must be greater than H1 + TA.

Let us call TS the number of key blocks of the "signalling" block interval.
Such interval is meant to be approximately a week. So TS is 3360 (`= 7 * 24 * 20`).

Let us call MS the number of key blocks in the "signalling" block interval that is meant to activate the new consensus protocol.
Such number is meant to be 90% of the number of key blocks in the "signalling" block interval. So MS is 3024 (that is - 90% of 3360).

Let us call S the "signal" value in the block header field `info`.
**TODO Select S as pseudorandom.**

Let us call TC the number of confirmations for the "signalling" block interval.
Such number is meant to be configured by the user and to default to approximately two hours i.e. 40 (`= 2 * 20`).

The height at which the new consensus protocol may be active is equal to HS + TS + TC.

## Rationale

The node keeps the decision to activate the new consensus protocol local to the chain fork as taking that decision globally does not enhance the user experience and rather worsens it.
- By taking the decision globally, on bootstrap a node may initially follow a (valid) chain fork distinct from the best valid one hence take the wrong decision.
- As the best valid chain is not necessarily the longest one, by taking the decision globally the node may anyway taint the storage with blocks with eventually wrong consensus protocol.

*NOTE: This design choice may be lifted if problematic during the implementation phase.*

## Backwards Compatibility

The signalling using the block header field `info` is backward compatible, as the meaning of the value of such field is not under consensus.

The activation of the new consensus protocol based on miner signalling is meant to be a temporary measure during the time interval when the new protocol may be activated on the network while the node is running. Once the network reasonably settles on whether to activate the new consensus protocol, the user:
- Is meant to enforce such decision on the eventual node restart either by configuration or by upgrading the node to a new version.
- Shall be recommended to discard the persisted storage on the eventual node restart - as distinct persisted chain forks may have distinct consensus protocols at the same height.

## (possible) Future extensions

### Simultaneous consensus proposals

The usage of the block header field `info` offers room for optimization for accommodating simultaneous hard-forking or soft-forking consensus proposals, by interpreting such `info` field as a bitmask rather than a value.

## Implementation

The implementation needs to cater for the performance of the aggregation of the signalling e.g. slow multiple lookups on the storage.

The implementation needs to consider that the storage may contain blocks with the old and new consensus protocols at heights at which the new consensus protocol should have been applied. This is because the node is aware of multiple chain forks and peers.
