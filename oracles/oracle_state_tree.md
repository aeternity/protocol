[back](./oracles.md)
## Oracle state tree

The oracle state tree contain oracle objects. Each oracle also have a separate
tree with queries for this particular tree. The existence of an oracle and the
existence of query/response will have to be proven when two parties contract
with each other. In the name of efficiency the queries are not stored directly
in the oracle object, instead the oracle object contains the root_hash of a
separate Merkle tree containing the queries for the oracle.

### Oracle state tree objects

- The oracle state tree contains oracle objects
- The query state trees (one per oracle object) contain query objects.

#### The oracle object

- Created by an oracle register transaction.
- Deleted when its TTL expires.

#### The oracle query object

- Created by an oracle query transaction.
- Closed by an oracle response transaction.
- Immutable once it is closed.
- Deleted when it expires (When the query expire for an open query, and when
the response expire for a closed query)

The expiry is determined at creation time by the query TTL, and the response
TTL in the oracle query transaction. If/When an oracle response transaction is
accepted on the chain, the expiry is updated according to the response TTL.

```
{ query_id       :: id()
, oracle_address :: pubkey()
, query          :: query()
, response       :: oracle_response()
, expires        :: block_height()
, response_ttl   :: relative_ttl()
, fee            :: integer()
}
```

### Oracle state tree update

The oracle state tree is pruned when the TTL of an object is reached in the
height of the chain. We define the operation order as:

1. Delete the expired objects. Object should be deleted in ascending order of their IDs.
2. Insert new object in the transaction order of the block.

Note that the sorted order of the IDs is the same as the in-order
traversal of the tree.

### Handling of TTL of objects

We will keep a cache of the objects sorted by TTL and ID. Such cache
has the benefits:
- The next object to delete is the first object in the cache.
  - The TTL is lower than the block height -> We are done.
  - The TTL is equal to the block height -> Delete the object.
- The cache can be reconstructed by doing an in-order traversal of the
  oracle state tree.

### Pruning of oracle query objects

If the oracle query has not been given a response, the poster of
the query should be refunded the oracle query fee. If the oracle has
responded, the oracle was already given the funds at response time.

**NOTE:** The refunding has not yet been implemented
