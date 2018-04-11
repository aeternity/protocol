[back](../SYNC.md)*

# P2P messages

P2P messages are transported using the [Noise
protocol](https://noiseprotocol.org/). Since each message in the Noise protocol
is limited to (65536 - 2) bytes we sometimes have to fragment larger messages
(in particular blocks and transaction pool-chunks). On top of this we use a
simple message format, where 2 bytes (16 bits) are used for a big-endian
encoded message type integer followed by the payload for the particular
message. Since Noise (and the fragmentation) handle message size we need no
length field. The payload is a byte array, and messages are either fixed binary
data or encoded using [RLP](https://github.com/ethereum/wiki/wiki/RLP).

There are currently 13 different P2P messages implemented in
[epoch](https://github.com/aeternity/epoch/blob/master/apps/aecore/src/aec_peer_messages.erl)*
  - [MSG_FRAGMENT](#msg_fragment)
  - [MSG_P2P_RESPONSE](#msg_p2p_response)
  - [MSG_PING](#msg_ping)
  - [MSG_GET_HEADER_BY_HASH](#msg_get_header_by_hash)
  - [MSG_GET_HEADER_BY_HEIGHT](#msg_get_header_by_height)
  - [MSG_HEADER](#msg_header)
  - [MSG_GET_N_SUCCESSORS](#msg_get_n_successors)
  - [MSG_HEADER_HASHES](#msg_header_hashes)
  - [MSG_GET_BLOCK](#msg_get_block)
  - [MSG_TX](#msg_tx)
  - [MSG_BLOCK](#msg_block)
  - [MSG_GET_MEMPOOL](#msg_get_mempool)
  - [MSG_MEMPOOL](#msg_mempool)

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
  - `Object :: byte_array` - an object of type `Type` if Result is
    `true`.

## MSG_PING
*(Tag = 1)*

Message is RLP encoded, fields:
  - `Port :: int` - listen port
  - `Share :: int` - number of peers to share
  - `GenesisHash :: byte_array`
  - `Difficulty :: byte_array` - string representation of float that
    is the total difficulty of the chain.
  - `TopHash :: byte_array`
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

## MSG_HEADER
*(Tag = 4)*

Message is RLP encoded, fields:
  - `Header :: byte_array`

The Header is serialized using the
`aec_headers:serialize_to_binary/1` function.

## MSG_GET_N_SUCCESSORS
*(Tag = 5)*

Message is RLP encoded, fields:
  - `Hash :: byte_array` - header hash to start at
  - `N :: int` - number of header hashes to get

## MSG_HEADER_HASHES
*(Tag = 6)*

Message is RLP encoded, fields:
  - `HeaderHashes :: [byte_array]`

Each header hash contains a 64-bit big endian height and the corresponding
hash, see `aec_peer_messages` for details.

## MSG_GET_BLOCK
*(Tag = 7)*

Message is RLP encoded, fields:
  - `Hash :: byte_array`

## MSG_BLOCK
*(Tag = 11)*

Message is RLP encoded, fields:
  - `Block :: byte_array`

A block is serialized using the `aec_blocks:serialize_to_binary/1` function, it
consists of a header and a list of signed transactions.

## MSG_TX
*(Tag = 9)*

Message is RLP encoded, fields:
  - `Tx :: byte_array`

A signed transaction is serialized using the `aetx_sign:serialize_to_binary/1`.

## MSG_GET_MEMPOOL
*(Tag = 13)*

Message is RLP encoded, fields:

*Note:* No fields, just an empty RLP encoding.

## MSG_MEMPOOL
*(Tag = 14)*

Message is RLP encoded, fields:
  - `Txs :: [byte_array]` - list of serialized signed transactions

