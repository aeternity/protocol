# ORACLES

## Overview and definitions

- An **oracle** is an entity on the blockchain and lives in the **oracle state tree** in a full node.
- An oracle is operated by an **oracle operator**.
- The oracle operator creates an oracle through posting a **oracle register transaction** on the chain.
- The oracle register transaction register an account as an oracle. (One account - one oracle)
- Any user can query an oracle by posting an  **oracle query transaction** on the chain.
- The oracle query transaction creates an **oracle query object** in the oracle state tree.
- The oracle operator scans the transactions on the blockchain for the
  oracle query transaction through whatever means. Probably on the operator's own node.
- The oracle operator responds to the oracle query by posting an **oracle response transaction** on the chain.
- The oracle response transaction modifies the oracle query object by adding the response.
- After the response have been added, the oracle query object is closed, and is now immutable.

## [Oracle life cycle examples](./oracle_life_cycle.md)

## [Oracle state trees](./oracle_state_tree.md)

## [Oracle transactions](./oracle_transactions.md)

## Technical aspects of Oracle operations

### Oracles have a published API

- The API defines the format that queries should have.
- The API defined the format answers will have.

### Oracle responses have a type declaration
- Types should correspond to types in the smart contract language.
- There should be incentives to use simple types in oracle answers (boolean, integer).
  - For example, through access cost in smart contracts.

### Should oracle responses have restrictions on use?
- For example, should only the creator of the query be able to use the
  answer in a smart contract?
- Should the framework support encryption/decryption of answers?

### An oracle query/response has a TTL
- The actual response will remain on the chain.
- The response will be pruned from the state tree after a certain number of blocks.
- The cost of posting the answer should reflect the TTL.
