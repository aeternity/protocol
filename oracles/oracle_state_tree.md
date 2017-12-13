[back](./oracles.md)
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
