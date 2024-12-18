# P2P messages

P2P messages are transported using the [Noise protocol](https://noiseprotocol.org/). Since each message in the Noise protocol is limited to (65536 - 2) bytes we sometimes have to fragment larger messages (in particular blocks and transaction pool-chunks). On top of this we use a simple message format, where 2 bytes (16 bits) are used for a big-endian encoded message type integer followed by the payload for the particular message. Since Noise (and the fragmentation) handle message size we need no length field. The payload is a byte array, and messages are either fixed binary data or encoded using [RLP](https://github.com/ethereum/wiki/wiki/RLP).

The following P2P messages are implemented in the [æternity node](https://github.com/aeternity/aeternity/blob/master/apps/aecore/src/aec_peer_messages.erl):

* [MSG\_FRAGMENT](p2p_messages.md#msg_fragment)
* [MSG\_P2P\_RESPONSE](p2p_messages.md#msg_p2p_response)
* [MSG\_PING](p2p_messages.md#msg_ping)
* [MSG\_GET\_HEADER\_BY\_HASH](p2p_messages.md#msg_get_header_by_hash)
* [MSG\_GET\_HEADER\_BY\_HEIGHT](p2p_messages.md#msg_get_header_by_height)
* [MSG\_HEADER](p2p_messages.md#msg_header)
* [MSG\_GET\_N\_SUCCESSORS](p2p_messages.md#msg_get_n_successors)
* [MSG\_HEADER\_HASHES](p2p_messages.md#msg_header_hashes)
* [MSG\_GET\_BLOCK\_TXS](p2p_messages.md#msg_get_block_txs)
* [MSG\_GET\_GENERATION](p2p_messages.md#msg_get_generation)
* [MSG\_TXS](p2p_messages.md#msg_txs)
* [MSG\_BLOCK\_TXS](p2p_messages.md#msg_block_txs)
* [MSG\_KEY\_BLOCK](p2p_messages.md#msg_key_block)
* [MSG\_MICRO\_BLOCK](p2p_messages.md#msg_micro_block)
* [MSG\_GENERATION](p2p_messages.md#msg_generation)
* [MSG\_TX\_POOL\_SYNC\_INIT](p2p_messages.md#msg_tx_pool_sync_init)
* [MSG\_TX\_POOL\_SYNC\_UNFOLD](p2p_messages.md#msg_tx_pool_sync_unfold)
* [MSG\_TX\_POOL\_SYNC\_GET](p2p_messages.md#msg_tx_pool_sync_get)
* [MSG\_TX\_POOL\_SYNC\_FINISH](p2p_messages.md#msg_tx_pool_sync_finish)
* [MSG\_GET\_NODE\_INFO](p2p_messages.md#msg_get_node_info)
* [MSG\_NODE\_INFO](p2p_messages.md#msg_node_info)
* [MSG\_CLOSE](p2p_messages.md#msg_close)

Each message type (except for `MSG_FRAGMENT`) is versioned such that the message can easily be changed while still maintaining backwards compatibility by adding logic to handle several versions of a message.

## Types

In the following we use some types to abbreviate the documentation here is how various types should be interpreted (corresponds to their encoding):

* `uint16` - 16 bit, big endian unsigned integer.
* `byte_array` - variable sized byte array (either the last field in a static message or RLP encoded).
* `bool` - representing `true` or `false` - encoded as 0 or 1.
* `int` - variable (RLP encoded) integer
* `[X]` - variable (RLP encoded) list of `X`:s

## MSG\_FRAGMENT

_(Tag = 0)_

Fields:

* `N :: uint16` - fragment N of M
* `M :: uint16` - total number of fragments
* `Data :: byte_array`

_NOTE:_ Data is either (65536 - 6) bytes or `N` is equal to `M`.

## MSG\_P2P\_RESPONSE

_(Tag = 100)_

Message is RLP encoded, fields:

* `Result :: bool` - `true` means ok, `false` means error.
* `Type :: int` - the type of the response
* `Reason :: byte_array` - Human readable (UTF8) reason (only set if Result is `false`)\*
* `Object :: byte_array` - an object of type `Type` if Result is `true`.

## MSG\_PING

_(Tag = 1)_

Message is RLP encoded, fields:

### Version 1

* `Port :: int` - listen port.
* `Share :: int` - number of peers to share.
* `GenesisHash :: byte_array`
* `Difficulty :: int` - the total difficulty of the chain.
* `TopHash :: byte_array`
* `SyncAllowed :: bool` - if the sender of this ping message is accepting synchronization messages.
* `Peers :: [byte_array]` - list of shared peers.

### Version 2

* `Versions :: list`
  * `Protocol :: binary` - type of message, currently only "ping" is supported.
  * `Vsns :: [int]` - versions supported
* `Port :: int` - listen port.
* `Share :: int` - number of peers to share.
* `GenesisHash :: byte_array`
* `Height :: int` - current height.
* `Difficulty :: int` - the total difficulty of the chain.
* `TopHash :: byte_array`
* `SyncAllowed :: bool` - if the sender of this ping message is accepting synchronization messages.
* `Capabilities :: byte_array` - list of supported capabilites.
* `Peers :: [byte_array]` - list of shared peers.

Peers are serialized/deserialized in `aec_peer_messages`

## MSG\_GET\_HEADER\_BY\_HASH

_(Tag = 3)_

Message is RLP encoded, fields:

* `Hash :: byte_array`

## MSG\_GET\_HEADER\_BY\_HEIGHT

_(Tag = 15)_

Message is RLP encoded, fields:

* `Height :: int`
* `TopHash :: byte_array` - to ensure we get a header at height from the right fork

## MSG\_HEADER

_(Tag = 4)_

Message is RLP encoded, fields:

* `Header :: byte_array`

The Header is serialized using the `aec_headers:serialize_to_binary/1` function.

## MSG\_GET\_N\_SUCCESSORS

_(Tag = 5)_

Message is RLP encoded, fields:

* `FromHash :: byte_array` - header hash to start at
* `TargetHash :: byte_array` - target header hash (to ensure we get headers from the right fork)
* `N :: int` - number of header hashes to get

## MSG\_HEADER\_HASHES

_(Tag = 6)_

Message is RLP encoded, fields:

* `HeaderHashes :: [byte_array]`

Each header hash contains a 64-bit big endian height and the corresponding hash, see `aec_peer_messages` for details.

## MSG\_GET\_BLOCK\_TXS

_(Tag = 7)_

Message is RLP encoded, fields:

* `Hash :: byte_array - The block we fetch TXs from`
* `TxHashes :: [byte_array] - List of TxHashes to fetch TXs for`

## MSG\_GET\_GENERATION

_(Tag = 8)_

Message is RLP encoded, fields:

* `Hash :: byte_array`
* `Forward :: bool`

## MSG\_TXS

_(Tag = 9)_

Message is RLP encoded, fields:

* `Txs:: [byte_array]`

A signed transaction is serialized as a tagged and versioned [signed transaction](../../utility-features/serializations.md#signed-transaction).

## MSG\_BLOCK\_TXS

\*(Tag = 13)

Message is RLP encoded, fields:

* `Hash :: byte_array - The block we fetch TXs from`
* `Txs :: [byte_array] - List of serialized signed TXs`

A signed transaction is serialized as a tagged and versioned [signed transaction](../../utility-features/serializations.md#signed-transaction).

## MSG\_KEY\_BLOCK

\*(Tag = 10)

Message is RLP encoded, fields:

* `KeyBlock :: byte_array - Serialized key block`

The key block is [serialized](../../utility-features/serializations.md#key-block).

## MSG\_MICRO\_BLOCK

\*(Tag = 11)

Message is RLP encoded, fields:

* `MicroBlock :: byte_array - Serialized micro block`
* `Light :: bool - flag if micro block is light or normal`

A normal micro block is [serialized](../../utility-features/serializations.md#micro-block). A light micro block is serialized using `aec_peer_connection:serialize_light_micro_block/1` - in effect replacing the list of serialized signed transactions with a list of transaction hashes.

## MSG\_GENERATION

_(Tag = 12)_

Message is RLP encoded, fields:

* `KeyBlock :: byte_array`
* `MicroBlocks :: [byte_array]`
* `Forward :: bool`

The key block and each of the microblocks are serialized using the `aec_blocks:serialize_to_binary/1` function.

## MSG\_TX\_POOL\_SYNC\_INIT

_(Tag = 20)_

Message has no body.

## MSG\_TX\_POOL\_SYNC\_UNFOLD

_(Tag = 21)_

Message is RLP encoded, fields:

* `Unfolds :: [byte_array]`

Unfolds are serialized in `aec_tx_pool_sync` - the serialization is described in \[tx\_pool\_sync])(./tx\_pool\_sync.md).

## MSG\_TX\_POOL\_SYNC\_GET

_(Tag = 22)_

Message is RLP encoded, fields:

* `TxHashes :: [byte_array]`

## MSG\_TX\_POOL\_SYNC\_FINISH

_(Tag = 23)_

Message is RLP encoded, fields:

* `Done :: bool`

## MSG\_GET\_NODE\_INFO

_(Tag = 125)_

This message has no fields.

This is to be used for network monitoring.

## MSG\_NODE\_INFO

_(Tag = 126)_

Message is RLP encoded, fields:

* `Version` :: byte\_array - the version of the node
* `Revision` :: byte\_array - the revision of the node
* `Vendor` :: byte\_array - a string to differentiate between different protocol implementations
* `OS` :: byte\_array - the operating system the node is being ran
* `NetworkId` :: byte\_array - the node's expectation of the `network_id`. This has heavy impact on authentication validations
* `VerifiedPeers` :: integer - the amount of peers the node consideres to be verified
* `UnverifiedPeers` :: integer - the amount of peers the node consideres to be unverified

This message is the response for the [MSG\_GET\_NODE\_INFO](p2p_messages.md#msg_get_node_info) message. It is important to note that responding to it is not required by the p2p protocol as a peer might prefer keeping this information private.

## MSG\_CLOSE

_(Tag = 127)_

This message has no fields.
