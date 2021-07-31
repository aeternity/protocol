[back](./README.md)

# Mempool/TX-pool synchronization

On startup the Aeternity node needs to update (or get from scratch if it is a
completely new node) its list of unconfirmed transactions. New transactions it
will get through gossip, but by construction older transactions that (for some
reason) have not made it onto the chain is not gossiped.

Potentially there is a big overlap between the list of transactions held by the
starting node (transactions are persisted) and the peer it is synchronizing
with; thus to save network bandwidth it is preferrable to only send the missing
transactions. The protocol is straightforward:
  1. the node picks one peer to synchronize with
  2. they each create a MP tree holding their local transactions - In the MP
     tree, each element has as key the hash of the signed transaction and as
     (placeholder) value the empty list.
  3. the initiator asks for a partial unfolding of the peer's tree
  4. the initiator computes what parts of the tree it doesn't know about and
     either goes back to 3. and asks for further information, or
  5. the initiator asks for the missing transactions.

The P2P messages used are listed in [p2p_messages](./p2p_messages.md).

## Unfold serialization

The instructions for unfolding an MP tree are sent over the P2P protocol, thus
they need to be serialized. There are four different messages sent, they are
listed below. Except for the types mentioned in
[p2p_messages](./p2p_messages.md) we also use the type `path` which is path to
a node in an MP-tree, thus it could be an even or odd number of _nibbles_. RLP
require an even number of nibbles, i.e. whole bytes, so we pad with a parity:
  - even number of nibbles add byte with 0
  - odd number of nibbles add a nibble with value 1

The result is an even number of nibbles and the first nibble indicate how it
should be deserialized.

### UNFOLD_NODE
Message is RLP encoded, fields:
  - `type :: int` = 0
  - `path :: path`
  - `node :: byte_array`

### LEAF_NODE
Message is RLP encoded, fields:
  - `type :: int` = 1
  - `leaf :: path`

### SUBTREE_NODE
Message is RLP encoded, fields:
  - `type :: int` = 2
  - `subtree :: path`

### KEY_NODE
Message is RLP encoded, fields:
  - `type :: int` = 3
  - `key  :: byte_array`


