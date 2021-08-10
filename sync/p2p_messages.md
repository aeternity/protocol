# P2P messages

P2P messages are transported using the [Noise
protocol](https://noiseprotocol.org/). Since each message in the Noise protocol
is limited to (65536 - 2) bytes we sometimes have to fragment larger messages
(in particular blocks and transaction pool-chunks). On top of this we use a
simple message format, where 2 bytes (16 bits) are used for a big-endian encoded
message type integer followed by the payload for the particular message. Since
Noise (and the fragmentation) handle message size we need no length field. The
payload is a byte array, and messages are either fixed binary data or encoded
using [RLP](https://github.com/ethereum/wiki/wiki/RLP).

The following P2P messages are implemented in
the [æternity node](https://github.com/aeternity/aeternity/blob/master/apps/aecore/src/aec_peer_messages.erl):

  - [MSG_FRAGMENT](#msg_fragment)
  - [MSG_P2P_RESPONSE](#msg_p2p_response)
  - [MSG_PING](#msg_ping)
  - [MSG_GET_HEADER_BY_HASH](#msg_get_header_by_hash)
  - [MSG_GET_HEADER_BY_HEIGHT](#msg_get_header_by_height)
  - [MSG_HEADER](#msg_header)
  - [MSG_GET_N_SUCCESSORS](#msg_get_n_successors)
  - [MSG_HEADER_HASHES](#msg_header_hashes)
  - [MSG_GET_BLOCK_TXS](#msg_get_block_txs)
  - [MSG_GET_GENERATION](#msg_get_generation)
  - [MSG_TXS](#msg_txs)
  - [MSG_BLOCK_TXS](#msg_block_txs)
  - [MSG_KEY_BLOCK](#msg_key_block)
  - [MSG_MICRO_BLOCK](#msg_micro_block)
  - [MSG_GENERATION](#msg_generation)
  - [MSG_TX_POOL_SYNC_INIT](#msg_tx_pool_sync_init)
  - [MSG_TX_POOL_SYNC_UNFOLD](#msg_tx_pool_sync_unfold)
  - [MSG_TX_POOL_SYNC_GET](#msg_tx_pool_sync_get)
  - [MSG_TX_POOL_SYNC_FINISH](#msg_tx_pool_sync_finish)
  - [MSG_GET_NODE_INFO](#msg_get_node_info)
  - [MSG_NODE_INFO](#msg_node_info)
  - [MSG_CLOSE](#msg_close)

Each message type (except for `MSG_FRAGMENT`) is versioned such that the
message can easily be changed while still maintaining backwards compatibility
by adding logic to handle several versions of a message.

## Types

In the following we use some types to abbreviate the documentation here is how
various types should be interpreted (corresponds to their encoding):

  - `uint16` - 16 bit, big endian unsigned integer.
  - `byte_array` - variable sized byte array (either the last field in a
    static message or RLP encoded).
  - `bool` - representing `true` or `false` - encoded as 0 or 1.
  - `int` - variable (RLP encoded) integer
  - `[X]` - variable (RLP encoded) list of `X`:s


## MSG_FRAGMENT
*(Tag = 0)*

Fields:

  - `N :: int16` - fragment N of M
  - `M :: int16` - total number of fragments
  - `Data :: byte_array`

*NOTE:* Data is either (65536 - 6) bytes or `N` is equal to `M`.

## MSG_P2P_RESPONSE
*(Tag = 100)*

Message is RLP encoded, fields:

  - `Result :: bool` - `true` means ok, `false` means error.
  - `Type :: int` - the type of the response
  - `Reason :: byte_array` - Human readable (UTF8) reason (only set
    if Result is `false`)*
  - `Object :: byte_array` - an object of type `Type` if Result is `true`.

## MSG_PING
*(Tag = 1)*

Message is RLP encoded, fields:

  - `Port :: int` - listen port
  - `Share :: int` - number of peers to share
  - `GenesisHash :: byte_array`
  - `Difficulty :: int` - the total difficulty of the chain.
  - `TopHash :: byte_array`
  - `sync_allowed :: bool` - if the sender of this ping message is accepting
    synchronization messages.
  - `Peers :: [byte_array]` - list of shared peers

Peers are serialized/deserialized in `aec_peer_messages`

## MSG_GET_HEADER_BY_HASH
*(Tag = 3)*

Message is RLP encoded, fields:

  - `Hash :: byte_array`

## MSG_GET_HEADER_BY_HEIGHT
*(Tag = 15)*

Message is RLP encoded, fields:

  - `Height :: int`
  - `TopHash :: byte_array` - to ensure we get a header at height from the right fork

## MSG_HEADER
*(Tag = 4)*

Message is RLP encoded, fields:

  - `Header :: byte_array`

The Header is serialized using the
`aec_headers:serialize_to_binary/1` function.

## MSG_GET_N_SUCCESSORS
*(Tag = 5)*

Message is RLP encoded, fields:

  - `FromHash :: byte_array` - header hash to start at
  - `TargetHash :: byte_array` - target header hash (to ensure we get headers from the right fork)
  - `N :: int` - number of header hashes to get

## MSG_HEADER_HASHES
*(Tag = 6)*

Message is RLP encoded, fields:

  - `HeaderHashes :: [byte_array]`

Each header hash contains a 64-bit big endian height and the corresponding
hash, see `aec_peer_messages` for details.

## MSG_GET_BLOCK_TXS
*(Tag = 7)*

Message is RLP encoded, fields:

  - `Hash :: byte_array - The block we fetch TXs from`
  - `TxHashes :: [byte_array] - List of TxHashes to fetch TXs for`

## MSG_GET_GENERATION
*(Tag = 8)*

Message is RLP encoded, fields:

  - `Hash :: byte_array`
  - `Forward :: bool`

## MSG_TXS
*(Tag = 9)*

Message is RLP encoded, fields:

  - `Txs:: [byte_array]`

A signed transaction is serialized as a tagged and versioned
[signed transaction](../serializations.md#signed-transaction).

## MSG_BLOCK_TXS
*(Tag = 13)

Message is RLP encoded, fields:

  - `Hash :: byte_array - The block we fetch TXs from`
  - `Txs :: [byte_array] - List of serialized signed TXs`

A signed transaction is serialized as a tagged and versioned
[signed transaction](../serializations.md#signed-transaction).

## MSG_KEY_BLOCK
*(Tag = 10)

Message is RLP encoded, fields:

  - `KeyBlock :: byte_array - Serialized key block`

The key block is [serialized](../serializations.md#key-block).

## MSG_MICRO_BLOCK
*(Tag = 11)

Message is RLP encoded, fields:

  - `MicroBlock :: byte_array - Serialized micro block`
  - `Light :: bool - flag if micro block is light or normal`

A normal micro block is [serialized](../serializations.md#micro-block).
A light micro block is serialized using
`aec_peer_connection:serialize_light_micro_block/1` - in effect replacing the
list of serialized signed transactions with a list of transaction hashes.

## MSG_GENERATION
*(Tag = 12)*

Message is RLP encoded, fields:

  - `KeyBlock :: byte_array`
  - `MicroBlocks :: [byte_array]`
  - `Forward :: bool`

The key block and each of the microblocks are serialized using the `aec_blocks:serialize_to_binary/1` function.

## MSG_TX_POOL_SYNC_INIT
*(Tag = 20)*

Message has no body.

## MSG_TX_POOL_SYNC_UNFOLD
*(Tag = 21)*

Message is RLP encoded, fields:
  - `Unfolds :: [byte_array]`

Unfolds are serialized in `aec_tx_pool_sync` - the serialization is described in
[tx_pool_sync])(./tx_pool_sync.md).

## MSG_TX_POOL_SYNC_GET
*(Tag = 22)*

Message is RLP encoded, fields:

  - `TxHashes :: [byte_array]`

## MSG_TX_POOL_SYNC_FINISH
*(Tag = 23)*

Message is RLP encoded, fields:

  - `Done :: bool`

## MSG_GET_NODE_INFO
*(Tag = 125)*

This message has no fields.

This is to be used for network monitoring.

## MSG_NODE_INFO
*(Tag = 126)*

Message is RLP encoded, fields:

  - `Version` :: byte_array - the version of the node
  - `Revision` :: byte_array - the revision of the node
  - `Vendor` :: byte_array - a string to differentiate between different protocol imlementations
  - `OS` :: byte_array - the operating system the node is being ran
  - `NetworkId` :: byte_array - the node's expectation of the `network_id`. This has heavy impact on authentication validations
  - `VerifiedPeers` :: integer - the amount of peers the node consideres to be verified
  - `UnverifiedPeers` :: integer - the amount of peers the node consideres to be unverified

This message is the response for the [MSG_GET_NODE_INFO](#msg_get_node_info)
message. It is important to note that respoding to it is not required by the
p2p protocol as a peer might prefer keeping this information private.

## MSG_CLOSE
*(Tag = 127)*

This message has no fields.
