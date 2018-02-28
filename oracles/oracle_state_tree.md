[back](./oracles.md)
## Oracle state tree

The oracle state tree contain oracle objects and oracle query objects. The
existence of an oracle and the existence of query/response will have to be
proven when two parties contract with each other. Oracles and queries are
stored in the same tree; where a query has an id that is the concatenation of
the oracle id and a query id. Thus the queries in effect form a subtree of the
oracle and can be iterated over, etc.

### Oracle state tree objects

- The oracle state tree contains
  - Oracle objects
  - Query objects

#### The oracle object

- Created by an oracle register transaction.
- Deleted when its TTL expires.
- Updated with a new (longer) TTL on oracle extend transaction.

```
{ owner           :: pubkey()
, query_format    :: type_spec()
, response_format :: type_spec()
, query_fee       :: amount()
, expires         :: block_height()
}
```

#### The oracle query object

- Created by an oracle query transaction.
- Closed by an oracle response transaction.
- Immutable once it is closed.
- Deleted when it expires (When the query expire for an open query, and when
the response expire for a closed query)

The expiry is determined at creation time by the query TTL, and the response
TTL in the oracle query transaction. If/When an oracle response transaction is
accepted on the chain, the expiry is updated according to the response TTL.
*Note:* If the maximal TTL of the query (query TTL + response TTL) is longer
than the TTL of the Oracle, then the query is *rejected*.

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

