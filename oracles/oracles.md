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

## Oracle life cycle examples

### The football game results oracle

Alice is a big fan of football and she wants to share the results of games.

Alice registers an oracle by submitting a oracle register transaction
to the chain.

Alice pays a fee for submitting the transaction.

Alice needs to include some information in the transaction
- A short description of the oracle: "Ask me for football game results".
- A query fee for covering her costs.
- A declaration of the query format.
- A declaration of the response format.

Alice is running a node in the network. Alice registers a subscription
in her local node so she will be notified when someone posts a query
to her oracle.

Bob wants to use the result of a specific game on the block chain.

Bob finds Alice's oracle on the chain and posts a query transaction to
the chain.

Bob pays a fee for submitting the transaction. The fee is collected by
the miner.

Bob pays a fee posting a query to the oracle. The fee is transfered to
the oracle's account.

The query transaction contains:
- The address or Alice's oracle.
- A query in the format declared by Alice's oracle.
- A transaction fee for the miner.
- A transfer of coin to Alice's oracle.
- A TTL for the query (If Alice's oracle doesn't answer the query
  within the given time, Bob is refunded the coins)

Bob registers a subscription on a node for getting notified when there
is a response on his query

When Bob's query transaction gets accepted into the chain, Alice's
event subscription triggers and she gets notified that there is a new
query on the chain.

The event contains:
- The address of the sender account,
- The location of the transaction (?).

When the match has been played, and there is a result, Alice posts an
oracle response transaction on the chain.

The response transaction contains:
- The address of the sender account.
- The location of the query transaction (?).
- The result as defined in the oracle definition.
- A TTL for the response.

Alice pays a transaction fee for posting the transaction. The fee is
collected by the miner. And as part of the transaction Alice's oracle
receives the fee for the query.

When the response transaction has been accepted to the chain, Bob's
event subscription notifies him that there is a response.

The event contains:
- The location of the transaction (?).
- The content of the response.
- The TTL of the response.

Bob can now use the response by:
- Executing a smart contract which references the response.
- Use a public API of a node to get the answer.


## Technical aspects of Oracle operations

### An Oracle operator is an off blockchain entity that is inspecting blocks

We try to keep Oracle operation separate from regular node operation. The
Oracle have to be able to read and react to events on the chain. One could
imagine that being able to run an Oracle might be a typical incentive for
running a node?!

### Nodes need to maintain oracles trees and oracles answer trees

Oracle/answer trees are to make answer retrieval efficient.

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

### We start with one question oracles to avoid indexing answers per oracles

**TODO**: Is there a lot to be gained by this simplification?
**ANSWER**: Probably not.

### An oracle query/response has a TTL

- The actual response will remain on the chain.
- The response will be pruned from the state tree after a certain number of blocks.
- The cost of posting the answer should reflect the TTL.

## Transaction types related to Oracles:

### Oracle register transaction
- Contains:
  - The oracle "owner"
  - A unique oracle address (a public key - proof of priv key should be given?!)
  - Query format definition
  - Response format definition
  - Query fee
  - Transaction fee

Questions/Later:
- Exact format for queries (API).
  - Protobuf or something similar?
- Exaxt format for responses.
- Fee for posting a query. The fee can be 0.
  - Fees are flat to begin with.
  - We could imagine fees to be proportional to something.
- Should Oracles have a TTL?

```
{ oracle_owner    :: {public_key(), nonce()}
, oracle_address  :: public_key()
, query_format    :: format_definition()
, response_format :: format_definition()
, query_fee       :: amount()
, fee             :: amount()
(, ttl             :: time_in_msecs()) }
```

### Oracle query transaction
- Contains:
  - The sender (address) + nonce
  - The oracle (address)
  - The query in binary format
  - The query fee - locked up until either:
    - The oracle answers and receive the fee
    - The TTL expire and the sender gets a refund
  - Query TTL
  - Response TTL
  - The transaction fee

Questions/Comments/Later:
- The Transaction ID is the hash of {sender_address, nonce, oracle_address}
- Should the query format be checked by the miner?
- The size of this TX is variable (the Query), so fee/gas will vary - also the
sender will pay for storing the query, thus the TTL will also affect the
transaction fee.
- The query fee should cover the possibly variable size (response format) of
the response.
- The response TTL is how long the response will live in the state tree.
- What is a sensible default?
- Should the response TTL be refunded if there is no response?

```
{ sender_address  :: public_key()
, nonce           :: nonce()
, oracle_address  :: public_key()
, query           :: binary()
, query_fee       :: amount()
, query_ttl       :: time_in_msecs()
, response_ttl    :: time_in_msecs()
, fee             :: amount() }
```

### Oracle response
- Contains
  - The query ID
  - The response in binary format
  - The transaction fee
  - Response TTL

### Questions/Later:
- The response Transaction ID (if needed) is the hash of {query_id, response}.
- Should we have a notification?
  - Callback to the query?
- Any callback is paid by the oracle.
  - The oracle operator needs to use funds from the query fee.
  - Returned fee - If the oracle for some reason could not
    provide an answer it might want to return (part of) the fee?!
- Response should have a TTL?
- Note the oracle will pay for the payload (the response) so there is an
  incentive to keep it precise (and small).

```
{ query_id        :: tx_id()
, response        :: binary()
, fee             :: amount()
, ttl             :: time_in_msecs() }
```

(Open question: should there be a generic _DATA TX_ and should the Oracle
answer be a special instance of this transaction.)


## Oracle state tree

The oracle interactions resides in an oracle state tree that is
included in the root hash. The existence of an oracle and the
existence of query/response will have to be proven when two parites
contract with eachother.

The oracle state tree is pruned when a TTL is reached in the height of
the chain. Since the GB Merkle trees are sensitive to the order of
operations we define the operation order as:

1. Delete the expired objects. Object are deleted in ascending order of their IDs.
2. Insert new object in the transaction order of the block.

Note that the sorted order of the IDs is the same as the in-order
traversal of the tree.

We will keep a cache of the objects sorted by TTL and ID. Such cache
has the benefits:
- The next object to delete is the first object in the cache.
  - The TTL is lower than the block height -> We are done.
  - The TTL is equal to the block height -> Delete the object.
- The cache can be recontructed by doing an in-order traversal of the
  oracle state tree.

**TODO**: Should the oracle state tree be a separate tree or
  be joined with the accounts state tree?
