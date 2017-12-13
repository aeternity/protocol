[back](./oracles.md)
## Oracle state tree

The oracles and their interactions reside in an oracle state tree that
is included in the root hash. The existence of an oracle and the
existence of query/response will have to be proven when two parites
contract with eachother.

### Oracle state tree objects

The oracle state tree contains two types of objects:
- The oracle definition
- The oracle interaction

#### The oracle definition

- Created by an oracle register transaction.
- Deleted when its TTL expires.

#### The oracle interaction

- Created by an oracle query transaction.
- Closed by an oracle response transaction.
- Immutable once it is closed.
- Deleted when it expires

The expiry is determined at creation time by the TTL of the oracle
query transaction. If an oracle response transaction is accepted on
the chain, the expiry is updated according to the response TTL.

```
{ sender_address :: pubkey()
, sender_nonce   :: integer()
, oracle_address :: pubkey()
, response       :: oracle_response()
, expires        :: block_height()
, response_ttl   :: relative_ttl()
, fee            :: integer()
}
```

### Oracle state tree update

The oracle state tree is pruned when an objects TTL is reached in the
height of the chain. Since the GB Merkle trees are sensitive to the
order of operations we define the operation order as:

1. Delete the expired objects. Object are deleted in ascending order of their IDs.
2. Insert new object in the transaction order of the block.

Note that the sorted order of the IDs is the same as the in-order
traversal of the tree.

### Handling of TTL of objects

We will keep a cache of the objects sorted by TTL and ID. Such cache
has the benefits:
- The next object to delete is the first object in the cache.
  - The TTL is lower than the block height -> We are done.
  - The TTL is equal to the block height -> Delete the object.
- The cache can be recontructed by doing an in-order traversal of the
  oracle state tree.

### Pruning of oracle interaction objects

If the oracle interaction has not been given a response, the poster of
the query should be refunded the oracle query fee. If the oracle has
responded, the oracle was already given the funds at response time.

### TODO:
- Should the oracle state tree be a separate tree or
  be joined with the accounts state tree?
- Define the contents of the oracle interaction object.
