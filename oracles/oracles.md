# ORACLES

## Overview and definitions

- An **oracle** is an entity on the blockchain and lives in the **oracle state tree** in a full node.
- An oracle is operated by an **oracle operator**.
- The oracle operator creates an oracle through posting a **oracle register transaction** on the chain.
- Any user can query an oracle by posting an  **oracle query transaction** on the chain.
- The oracle operator scans the transactions on the blockchain for the
  oracle query transaction through whatever means. Probably on the operator's own node.
- The oracle operator creates an **oracle response** by posting an **oracle response transaction** on the chain.
- The oracle response lives in the oracle state tree as well.

## Technical aspects of Oracle operations

### An Oracle operator is an off blockchain entity that is inspecting blocks

We try to keep Oracle operation separate from regular node operation. The
Oracle have to be able to read and react to events on the chain. One could
imagine that being able to run an Oracle might be a typical incentive for
running a node?!

### Nodes need to maintain oracles trees and oracles answer trees

Oracle/answer trees are to make answer retrieval efficient

### We start with one question oracles to avoid indexing answers per oracles

TODO: Is there a lot to be gained by this simplification?

### An oracle query/response has a TTL?

This means that we can prune the state trees. (In the chain it lives for ever
obviously)

## Transaction types related to Oracles:
  - Oracle register: publish API, optionally set fee
  - Oracle query: use API, include fee for oracle posting answer, optionally
  include (flat) fee set by oracle
  - Oracle response: uses funds from oracle query fee

(Open question: should there be a generic _DATA TX_ and should the Oracle
answer be a special instance of this transaction.)

### Oracle register
  - Oracle Address
  - Oracle API - Protobuf or something similar?
  - Query fee (I.e. what does it cost to ask a question)

Posting an ORACLE_REGISTER_TX costs a (flat?) fee.

### Oracle query
  - Oracle address
  - QueryID (address + nonce?)
  - Query data (following the API?)
  - Query fee

Posting an ORACLE_QUERY_TX costs a fee.

### Oracle response
  - QueryID
  - Query response (following the API?)
  - (Later: Returned fee - If the oracle for some reason could not provide an
  answer it might want to return (part of) the fee?!)

Posting an ORACLE_RESPONSE_TX costs a fee (should be covered by the 'Query fee'
in the ORACLE_QUERY_TX)
