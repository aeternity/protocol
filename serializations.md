# Serialization formats

The serialization formats in this document describes the binary format
used to encode the different objects in the binary format that is used
for:

* Hashing (e.g., block hash)
* Insertion in the Merkle Patricia Tree (e.g., state trees, transaction trees).
* Signing transactions (i.e., the (hash of the) serialized form is signed).

Other formats may be used for communication between nodes or for the
user API.

## Blocks and headers

There are two types of blocks:

* micro block - contains a header and a list of transactions.
* key block - contains only a header.

Blocks are serialized in a staged manner for uniformity. The key block
does not contain any more information than the header, so the
representation of the block and the header is the same. Micro blocks
has a static size header and a dynamic size "body".

The header starts with a version number (32 bits), followed by a
reserved flags field (32 bits). The first flag bit marks the header as
a key or micro header. Other flag fields are defined separately for
the header types. Note that unused flags must be set to zero.

| Header type flag | Header type |
| ---              | ---         |
| 0                | micro       |
| 1                | key         |

### Key block/header

All field sizes are statically known and can be constructed directly
as a byte array. The header starts with a version number (32 bits),
followed by a reserved flags field (32 bits).

For flag bits:
* In Roma release, only one flag bit is used, to mark the header as a key header.
* In Minerva release, another bit is used, to mark the presence of an optional info field in the header.
* Other flags must be set to zero.

| Fieldname  | Size (bytes) | Notes |
| --- | ---  | --- |
| version     | 32 bits | |
| key_tag     | 1 bit   | |
| info_flag   | 1 bit            | From Minerva protocol |
| unused_flag | 1 bit (set to 0) | For Roma protocol |
| unused_flags| 30 bits (all set to 0) | |
| height      | 8    | |
| prev_hash   | 32   | |
| prev_key_hash | 32   | |
| state_hash  | 32   | |
| miner       | 32   | |
| beneficiary | 32   | |
| target      | 4    | |
| pow         | 168  | |
| nonce       | 8    | |
| time        | 8    | |
| info        | 0 or 4 | From Minerva protocol |

Note:

* The info field is either present, and of size 4 bytes, or not
  present (0 bytes). The presence of the info field must be signalled
  by setting the info_flag to 1. The contents of the info field has no
  current interpretation, but the plan is to use it to signal
  information about the miners (e.g., if the miners are aware of a
  coming hard fork).

### Micro block

| Fieldname    | Size |
| ---          | ---  |
| Micro Header | 216 or 238 bytes (see below) |
| [Micro Body](#micro-body)| variable |

### Micro block header

| Fieldname | Size (bytes) |
| --- | --- |
| version    | 32 bits |
| micro_tag  | 1 bit   |
| has_fraud  | 1 bit   |
| unused_flags| 30 bits (all set to 0) |
| height     | 8    |
| prev_hash  | 32   |
| prev_key_hash | 32   |
| state_hash | 32   |
| txs_hash   | 32   |
| time       | 8    |
| fraud_hash | 0 or 32 |
| signature  | 64   |

Note:

* The field for *signature* (64 bytes) must be filled
  with only zeroes when constructing or validating the signature.

* The micro block header has two valid sizes depending on whether the
  block contains Proof of Fraud or not. This is signalled using the
  *has_fraud* flag.

| has_fraud | fraud_hash size |
| ---       | ---             |
| 1         | 32 bytes        |
| 0         | 0  bytes        |



## Dynamic size object serialization

In this section we use `[]` to mean lists, `<name>` to denote fields,
`,` to separate fields in lists. We use `::` to separate fields from
their types . We use `int()` to denote the integer type and `binary()`
to denote the byte array type. Variable length lists are denoted with
`[]` in the type domain (e.g., `[int()]` is a list of integers).
Fixed length lists are denoted with '{}' (e.g. '{int(), int()}')
denotes a list of exactly two integers. We use `++` as the list
concatenation operator. We also use the `bool()` type as the special
case of the integers `0` and `1` used as the boolean type.

### The id() type

The special type `id()` is a `binary()` denoting a tagged binary
(e.g., hash or public key) referring to an object in the chain (e.g.,
account, oracle) . The first byte is a tag denoting which type of
identifier, and the remaining 32 bytes is the identifier itself. This
is used to distinguish between identifiers where there can be
ambiguity.

| Id tag | Identifier type |
| ---    | ---             |
| 1      | account         |
| 2      | name            |
| 3      | commitment      |
| 4      | oracle          |
| 5      | contract        |
| 6      | channel         |

In Erlang notation, the `id()` type pattern is:
```
<<Tag:1/unsigned-integer-unit:8, Hash:32/binary-unit:8>>
```

### The call_return_type() type

The special type `call_return_type()` is an `int()` denoting the outcome of a contract call.

| Value | Return type |
| ---   | ---         |
| 0     | ok          |
| 1     | error       |
| 2     | revert      |

### RLP Encoding

We use the Recursive Length Prefix encoding
(https://github.com/ethereum/wiki/wiki/RLP) for serializing objects that
have dynamic sizes of the fields.

RLP ensures that there is only one serialization of each corresponding
object on the lowest level, but it can only encode two primitive
objects, lists and byte arrays.

RLP ensures that the serialization is a non-empty byte array.

Objects in Æternity are encoded as lists of fields, where the two
first fields describe the object type and the object version.

```
[ <tag>, <version>, <field1>, <field2>...]
```

Since all values are byte arrays in RLP, `int()` needs to be a byte
array as well. We encode all integers as unsigned, big endian byte
arrays. To avoid ambiguity in the encoding of integers, we adapt the
same scheme as RLP and demand that integers are encoded with the
minimal number of bytes (i.e., disallow leading zeroes in the encoded
byte array). Negative integers is not used in the serialization format
since they are not needed. If the need arises, the scheme should be
extended.


### Binary serialization

The serialization, `S`, of a dynamic size object, `O`, is defined as

```
S(O) = rlp([tag(O), vsn(O)] ++ fields(O))
```

where the tag is given in the table below, and the fields are in the
subsequent sections divided by object.


#### Table of object tags
| Type | Tag |
|---|---|
| Account | 10 |
| Signed transaction | 11 |
| Spend transaction | 12 |
| Oracle | 20 |
| Oracle query | 21 |
| Oracle register transaction | 22 |
| Oracle query transaction | 23 |
| Oracle response transaction | 24 |
| Oracle extend transaction | 25 |
| Name service name | 30|
| Name service commitment | 31 |
| Name service claim transaction | 32 |
| Name service preclaim transaction | 33 |
| Name service update transaction | 34 |
| Name service revoke transaction | 35 |
| Name service transfer transaction | 36 |
| Contract | 40 |
| Contract call | 41 |
| Contract create transaction | 42 |
| Contract call transaction | 43 |
| Channel create transaction | 50 |
| Channel deposit transaction | 51 |
| Channel withdraw transaction | 52 |
| Channel force progress transaction | 521 |
| Channel close mutual transaction | 53 |
| Channel close solo transaction | 54 |
| Channel slash transaction | 55 |
| Channel settle transaction | 56 |
| Channel off-chain transaction | 57 |
| Channel off-chain update transfer | 570 |
| Channel off-chain update deposit | 571 |
| Channel off-chain update withdrawal | 572 |
| Channel off-chain update create contract | 573 |
| Channel off-chain update call contract | 574 |
| Channel client reconnect transaction | 575 |
| Channel | 58 |
| Channel snapshot transaction | 59 |
| POI | 60 |
| Trees with DB | 61 |
| State trees | 62 |
| Merkle Patricia tree | 63 |
| Merkle Patricia tree's value | 64 |
| Contracts' Merkle Patricia tree's value | 621 |
| Contract Calls' Merkle Patricia tree's value | 622 |
| Channels' Merkle Patricia tree's value | 623 |
| Nameservice's Merkle Patricia tree's value | 624 |
| Oracles' Merkle Patricia tree's value | 625 |
| Accounts' Merkle Patricia tree's value | 626 |
| Sophia byte code | 70 |
| Generalized accounts attach transaction | 80 |
| Generalized accounts meta transaction | 81 |
| PayingFor transaction | 82 |
| Key block | 100 |
| Micro block | 101 |
| Light micro block | 102 |
| Proof of Fraud | 200 |

#### Accounts (version 1, Basic accounts))
```
[ <nonce>   :: int()
, <balance> :: int()
]
```

#### Accounts (version 2, Generalized accounts, from Fortuna release)
```
[ <flags>       :: int()
, <nonce>       :: int()
, <balance>     :: int()
, <ga_contract> :: id()
, <ga_auth_fun> :: binary()
]
```

#### Accounts (version 3, Normal accounts with flags, from Lima release)
```
[ <flags>       :: int()
, <nonce>       :: int()
, <balance>     :: int()
]
```

### Signed transaction
```
[ <signatures>  :: [binary()]
, <transaction> :: binary()
]
```

Type signatures are sorted.

### Spend transaction
```
[ <sender>    :: id()
, <recipient> :: id()
, <amount>    :: int()
, <fee>       :: int()
, <ttl>       :: int()
, <nonce>     :: int()
, <payload>   :: binary()
]
```

The recipient must be one of the following:
* An account identifier.
* An oracle identifier.
* A contract identifier.
* A name identifier, whose related name entry has an identifier as value of pointer with key `account_pubkey`.
  If multiple pointer entries are present for such key, then the first of such entries is used.

#### Oracles
```
[ <owner>           :: id()
, <query_format>    :: binary()
, <response_format> :: binary()
, <query_fee>       :: int()
, <expires>         :: int()
, <abi_version>>    :: int()
]
```

#### Oracle queries
```
[ <sender_address> :: id()
, <sender_nonce>   :: int()
, <oracle_address> :: id()
, <query>          :: binary()
, <has_response>   :: bool()
, <response>       :: binary()
, <expires>        :: int()
, <response_ttl>   :: int()
, <fee>            :: int()
]
```

#### Oracle register transaction
```
[ <account>       :: id()
, <nonce>         :: int()
, <query_spec>    :: binary()
, <response_spec> :: binary()
, <query_fee>     :: int()
, <ttl_type>      :: int()
, <ttl_value>     :: int()
, <fee>           :: int()
, <ttl>           :: int()
, <abi_version>   :: int()
]
```

#### Oracle query transaction
```
[ <sender>             :: id()
, <nonce>              :: int()
, <oracle>             :: id()
, <query>              :: binary()
, <query_fee>          :: int()
, <query_ttl_type>     :: int()
, <query_ttl_value>    :: int()
, <response_ttl_type>  :: int()
, <response_ttl_value> :: int()
, <fee>                :: int()
, <ttl>                :: int()
```

#### Oracle response transaction
```
[ <oracle>             :: id()
, <nonce>              :: int()
, <query_id>           :: binary()
, <response>           :: binary()
, <response_ttl_type>  :: int()
, <response_ttl_value> :: int()
, <fee>                :: int()
, <ttl>                :: int()
]
```

#### Oracle extend transaction
```
[ <oracle>    :: id()
, <nonce>     :: int()
, <ttl_type>  :: int()
, <ttl_value> :: int()
, <fee>       :: int()
, <ttl>       :: int()
]
```

#### Contract

For a contract with address `<contractpubkey>`, the fields of the contract object (to which tag and version need to be prepended) are:

```
[ <owner>      :: id()
, <ct_version> :: int()
, <code>       :: binary()
, <log>        :: binary(),
, <active>     :: bool(),
, <referers>   :: [id()],
, <deposit>    :: int()
]
```

The log field is always the empty binary.

The balance of the account is stored in the account state tree.

The contract storage (or state) which is a key value map from (key::binary() to value::binary())
is stored in its own subtree. The key for a contract storage value is:
```
<contractpubkey><16><key> :: binary()
```
The `<key>` is non-empty.

Each value is just stored as a binary as is - without tag or version.
If the value is the empty binary the key is pruned from the tree.

The content of the contract store depends on [the ABI and the VM version](/contracts/contract_vms.md).

#### Contract call
```
[ <caller_id>        :: id()
, <caller_nonce>     :: int()
, <height>           :: int()
, <contract_id>      :: id()
, <gas_price>        :: int()
, <gas_used>         :: int()
, <return_value>     :: binary()
, <return_type>      :: call_return_type()
, <log>              :: [ { <address> :: id, [ <topics> :: binary() ], <data> :: binary() } ]
]
```

#### Contract create transaction
```
[ <owner>      :: id()
, <nonce>      :: int()
, <code>       :: binary()
, <ct_version> :: int()
, <fee>        :: int()
, <ttl>        :: int()
, <deposit>    :: int()
, <amount>     :: int()
, <gas>        :: int()
, <gas_price>  :: int()
, <call_data>  :: binary()
]
```

#### Contract call transaction
```
[ <caller>      :: id()
, <nonce>       :: int()
, <contract>    :: id()
, <abi_version> :: int()
, <fee>         :: int()
, <ttl>         :: int()
, <amount>      :: int()
, <gas>         :: int()
, <gas_price>   :: int()
, <call_data>   :: binary()
]
```

#### Name service name
```
[ <owner>      :: id()
, <expires_by> :: int()
, <status>     :: binary()
, <client_ttl> :: int()
, <pointers>   :: [{binary(), id()}]
```

#### Name service commitment
```
[ <owner>   :: id()
, <created> :: int()
, <expires> :: int()
]
```

#### Name service claim transaction
```
[ <account>   :: id()
, <nonce>     :: int()
, <name>      :: binary() %% The actual name, not the hash
, <name_salt> :: int()
, <name_fee>  :: int()
, <fee>       :: int()
, <ttl>       :: int()
]
```

#### Name service preclaim transaction
```
[ <account>    :: id()
, <nonce>      :: int()
, <commitment> :: id()
, <fee>        :: int()
, <ttl>        :: int()
]
```

#### Name service update transaction
```
[ <account>    :: id()
, <nonce>      :: int()
, <hash>       :: id()
, <name_ttl>   :: int()
, <pointers>   :: [{binary(), id()}]
, <client_ttl> :: int()
, <fee>        :: int()
, <ttl>        :: int()
]
```

#### Name service revoke transaction
```
[ <account> :: id()
, <nonce>   :: int()
, <hash>    :: id()
, <fee>     :: int()
, <ttl>     :: int()
]
```

#### Name service transfer transaction
```
[ <account>   :: id()
, <nonce>     :: int()
, <hash>      :: id()
, <recipient> :: id()
, <fee>       :: int()
, <ttl>       :: int()
]
```

The recipient must be one of the following:
* An account identifier.
* A name identifier, whose related name entry has an identifier as value of pointer with key `account_pubkey`.
  If multiple pointer entries are present for such key, then the first of such entries is used.

### Channels

#### Channel create transaction (version 1, until Iris release)
```
[ <initiator>        :: id()
, <initiator_amount> :: int()
, <responder>        :: id()
, <responder_amount> :: int()
, <channel_reserve>  :: int()
, <lock_period>      :: int()
, <ttl>              :: int()
, <fee>              :: int()
, <delegate_ids>     :: [id()]
, <state_hash>       :: binary()
, <nonce>            :: int()
]
```

#### Channel create transaction (version 2, from Iris release)
```
[ <initiator>               :: id()
, <initiator_amount>        :: int()
, <responder>               :: id()
, <responder_amount>        :: int()
, <channel_reserve>         :: int()
, <lock_period>             :: int()
, <ttl>                     :: int()
, <fee>                     :: int()
, <initiator_delegate_ids>  :: [id()]
, <responder_delegate_ids>  :: [id()]
, <state_hash>              :: binary()
, <nonce>                   :: int()
]
```

#### Channel deposit transaction
```
[ <channel_id> :: id()
, <from_id>    :: id()
, <amount>     :: int()
, <ttl>        :: int()
, <fee>        :: int()
, <state_hash> :: binary()
, <round>      :: int()
, <nonce>      :: int()
]
```

#### Channel withdraw transaction
```
[ <channel_id> :: id()
, <to_id>      :: id()
, <amount>     :: int()
, <ttl>        :: int()
, <fee>        :: int()
, <state_hash> :: binary()
, <round>      :: int()
, <nonce>      :: int()
]
```

#### Channel close mutual transaction
```
[ <channel_id>             :: id()
, <from_id>                :: id()
, <initiator_amount_final> :: int()
, <responder_amount_final> :: int()
, <ttl>                    :: int()
, <fee>                    :: int()
, <nonce>                  :: int()
]
```

#### Channel close solo transaction
```
[ <channel_id>      :: id()
, <from_id>         :: id()
, <payload>         :: binary()
, <poi>             :: poi()
, <ttl>             :: int()
, <fee>             :: int()
, <nonce>           :: int()
]
```

The payload is a serialized signed channel off-chain transaction or it is empty.

#### Channel slash transaction
```
[ <channel_id>      :: id()
, <from_id>         :: id()
, <payload>         :: binary()
, <poi>             :: poi()
, <ttl>             :: int()
, <fee>             :: int()
, <nonce>           :: int()
]
```

The payload is a serialized signed channel off-chain transaction or it is empty.

#### Channel settle transaction
```
[ <channel_id>             :: id()
, <from_id>                :: id()
, <initiator_amount_final> :: int()
, <responder_amount_final> :: int()
, <ttl>                    :: int()
, <fee>                    :: int()
, <nonce>                  :: int()
]
```

#### Channel snapshot solo transaction
```
[ <channel_id>      :: id()
, <from_id>         :: id()
, <payload>         :: binary()
, <ttl>             :: int()
, <fee>             :: int()
, <nonce>           :: int()
]
```

The payload is a serialized signed channel off-chain transaction and can not be empty.


#### Channel solo force progress transaction
```
[ <channel_id>      :: id()
, <from_id>         :: id()
, <payload>         :: binary()
, <round>           :: int()
, <update>          :: binary()
, <state_hash>      :: binary()
, <offchain_trees>  :: trees()
, <ttl>             :: int()
, <fee>             :: int()
, <nonce>           :: int()
]
```

The payload is a serialized co-signed channel off-chain transaction or it is empty.
The round is the new channel's round that will be produced by the forcing of
progress.
The update is the contract call update to be applied on the old channel's
state.
The state hash is the expected root hash of the produced channel's state trees
after the update had been applied to the channel state provided in the proof
of inclusion.
The proof of inclusion has the same root hash as the state hash of the co-signed
payload.

#### Channel off-chain update

Channel update rounds are described by various updates, that are defined in
this subsection. Each mention of type update() in the rest of this document is
meant to be understood as referring to any one of these updates. If not specified
something different, any of the addresses involved could belong to a participant,
contract or even some other address part of the off-chain state tree of this channel.

###### Channel off-chain update transfer

This is an internal off-chain transfer from one address to another.

```
[ <from>    			:: id()
, <to>      			:: id()
, <amount>  			:: int()
]

```

###### Channel off-chain update deposit

This is an internal off-chain balance increment. It is used by the
`channel_deposit_tx` internal representation.

```
[ <from>    			:: id()
, <amount>  			:: int()
]

```

###### Channel off-chain update withdrawal

This is an internal off-chain balance decrement. It is used by the
`channel_withdraw_tx` internal representation.

```
[ <to>      			:: id()
, <amount>  			:: int()
]

```

###### Channel off-chain update create contract

This is an update for creating new contracts inside channel's off-chain state
tree.

```
[ <owner>      :: id()
, <ct_version> :: int()
, <code>       :: binary()
, <deposit>    :: int()
, <call_data>  :: binary()
]

```

###### Channel off-chain update call contract

This is an update for calling a contract inside channel's off-chain state
tree.

```
[ <caller>      :: id()
, <contract>    :: id(),
, <abi_version> :: int()
, <amount>      :: int()
, <call_data>   :: binary()
, <call_stack>  :: [int()]
, <gas_price>   :: int()
, <gas_limit>   :: int()
]

```

#### Channel off-chain transaction

The channel off-chain transaction is not included directly in the transaction tree but indirectly as payload of:
* The channel close solo transaction.
* The channel slash transaction.
* The channel snapshot solo transaction.
* The channel force progress transaction.

version 1, until Fortuna release
```
[ <channel_id>       :: id()
, <round>            :: int()
, <updates>          :: [update()]
, <state_hash>       :: binary()
]
```

version 2, from Fortuna release
```
[ <channel_id>       :: id()
, <round>            :: int()
, <state_hash>       :: binary()
]
```

#### Channel client reconnect transaction

The channel client reconnect transaction is used only when a Websocket client
wants to reconnect to an already running FSM. It cannot be introduced into the
mempool. The elements of the transaction are:
* The channel id of the channel that the client wants to connect to
* A round (integer), which must be higher than at the last attempt
* The role (`initiator` or `responder`) of the FSM instance in question
* The public key of the client; must correspond to the private key used for
  signing the transaction.

```
[ <channel_id>    :: id()
, <round>         :: int()
, <role>          :: binary()
, <pub_key>       :: id()
]
```

#### Channel (version 1, until Fortuna release)
```
[ <initiator>           :: id()
, <responder>           :: id()
, <channel_amount>      :: int()
, <initiator_amount>    :: int()
, <responder_amount>    :: int()
, <channel_reserve>     :: int()
, <delegate_ids>        :: [id()]
, <state_hash>          :: binary()
, <round>               :: int()
, <solo_round>          :: int()
, <lock_period>         :: int()
, <locked_until>        :: int()
]
```

#### Channel (version 2, from Fortuna release)
```
[ <initiator>           :: id()
, <responder>           :: id()
, <channel_amount>      :: int()
, <initiator_amount>    :: int()
, <responder_amount>    :: int()
, <channel_reserve>     :: int()
, <delegate_ids>        :: [id()]
, <state_hash>          :: binary()
, <round>               :: int()
, <solo_round>          :: int()
, <lock_period>         :: int()
, <locked_until>        :: int()
, <initiator_auth>      :: binary()
, <responder_auth>      :: binary()
]
```

#### Channel (version 3, from Iris release)
```
[ <initiator>               :: id()
, <responder>               :: id()
, <channel_amount>          :: int()
, <initiator_amount>        :: int()
, <responder_amount>        :: int()
, <channel_reserve>         :: int()
, <initiator_delegate_ids>  :: [id()]
, <responder_delegate_ids>  :: [id()]
, <state_hash>              :: binary()
, <round>                   :: int()
, <solo_round>              :: int()
, <lock_period>             :: int()
, <locked_until>            :: int()
, <initiator_auth>          :: binary()
, <responder_auth>          :: binary()
]
```

#### Proof of inclusion on state trees (POI) :: poi()
```
[ {<accounts>  :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), <mpt_value> :: [binary()]}]}]}
, {<calls>     :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), <mpt_value> :: [binary()]}]}]}
, {<channels>  :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), <mpt_value> :: [binary()]}]}]}
, {<contracts> :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), <mpt_value> :: [binary()]}]}]}
, {<ns>        :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), <mpt_value> :: [binary()]}]}]}
, {<oracles>   :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), <mpt_value> :: [binary()]}]}]}
]
```

If a subtree (e.g. `<accounts>`) is empty, then its serialization is just `[]` (e.g. `<accounts>` is `[]`) otherwise it contains at least its root hash (e.g. `<accounts>` is `[{<root_hash>, []}]`).

NOTE: `[{<mpt_hash>, <mpt_value>}]` is the sorted list of Merkle Patricia Tree nodes in the proof.

NOTE: As the POI contains the Merkle Patricia Tree nodes (e.g. not only their hashes):
* Each state subtree does not necessarily contain elements of the same key length.
* The object itself does not contain its own id as it can be derived from the location in the tree.
* The key used for storing each object in each state subtree is not necessarily derived from the object itself.
* The value(s) whose inclusion the POI proves is included in the POI itself.

#### Merkle Patricia Value
```
[ <key>        :: binary()
, <val>        :: binary()
]
```
#### Merkle Patricia Tree :: mtree()
```
[ <values>        :: [binary()]
]
```

All Merkle Patricia Values are serialized.

#### State trees :: trees()
```
[ <contracts>   ::  binary()
, <calls>       ::  binary()
, <channels>    ::  binary()
, <ns>          ::  binary()
, <oracles>     ::  binary()
, <accounts>    ::  binary()
]
```

All binaries are serialized as follows:

##### Contracts' state tree
```
[ <contracts>    :: binary()
]
```

The binary is a serialized Merkle Patricia Tree.

##### Contract Calls' state tree
```
[ <calls>        ::  binary()
]
```

The binary is a serialized Merkle Patricia Tree.

##### Channels' state tree
```
[ <channels>     :: binary()
]
```

The binary is a serialized Merkle Patricia Tree.

##### Nameservice's state tree
```
[ <mtree>       :: binary()
]
```

The binary is a serialized Merkle Patricia Tree.

##### Oracles' state tree
```
[ <otree>       :: binary()
]
```

The binary is a serialized Merkle Patricia Tree.

##### Accounts' state tree
```
[ <accounts>      :: binary()
]
```

The binary is a serialized Merkle Patricia Tree.

#### Sophia byte code (version 1, Roma release)
```
[ <source code hash> :: binary()
, <type info>        :: [{<fun_hash> :: binary(), <fun_name> :: binary(), <arg_type> :: binary(), <out_type> :: binary()}]
, <byte code>        :: binary()
]
```

#### Sophia byte code (version 2, Minerva release)
```
[ <source code hash> :: binary()
, <type info>        :: [{<fun_hash> :: binary(), <fun_name> :: binary(), <arg_type> :: binary(), <out_type> :: binary()}]
, <byte code>        :: binary()
, <compiler version> :: binary()
]
```

#### Sophia byte code (version 3, Lima release)
```
[ <source code hash> :: binary()
, <type info>        :: [{<fun_hash> :: binary(), <fun_name> :: binary(), <payable> :: bool(), <arg_type> :: binary(), <out_type> :: binary()}]
, <byte code>        :: binary()
, <compiler version> :: binary()
, <payable>          :: bool()
]
```

### Generalized accounts
Generalized accounts are available from version 3, Fortuna release. A
generalized account is interchangeable with a basic (non-generalized) account
everywhere, the only difference is that it is not able to directly sign a
transaction. Instead the transaction has to be wrapped in a [meta
transaction](#generalized-accounts-meta-transaction) with the correct
authorization data.

#### Generalized accounts attach transaction
```
[ <owner_id>   :: id()
, <nonce>      :: int()
, <code>       :: binary()
, <auth_fun>   :: binary()
, <ct_version> :: int()
, <fee>        :: int()
, <ttl>        :: int()
, <gas>        :: int()
, <gas_price>  :: int()
, <call_data>  :: binary()
]
```

#### Generalized accounts meta transaction

##### Meta transaction  version 1, pre Iris

```
[ <ga_id>       :: id()
, <auth_data>   :: binary()
, <abi_version> :: int()
, <fee>         :: int()
, <gas>         :: int()
, <gas_price>   :: int()
, <ttl>         :: int()
, <tx>          :: binary()
]
```

##### Meta transaction  version 2, from Iris on

```
[ <ga_id>       :: id()
, <auth_data>   :: binary()
, <abi_version> :: int()
, <fee>         :: int()
, <gas>         :: int()
, <gas_price>   :: int()
, <tx>          :: binary()
]
```

### PayingFor
The `PayingFor` transaction is available from version 5, Iris release. By using
it,  an account `P` can pay for the transaction (transaction fee + gas) of another
account `A`.

#### PayingFor transaction
```
[ <payer_id> :: id()
, <nonce>    :: int()
, <fee>      :: int()
, <tx>       :: binary()
]
```


#### Micro Body
```
[ <transactions>    :: [binary()]
, <proof_of_fraud>> :: [binary()]
]
```
NOTE:
* The *transactions* are signed transactions.
* The *proof_of_fraud* list is either empty (i.e., no fraud) or has one element (i.e., contains one proof of fraud).


#### Proof of fraud
```
[ <header1>  :: binary()
, <header2>  :: binary()
, <pubkey>   :: binary()
]
```

## Serialization of FATE contracts

FATE contracts uses a recursive BNF like definition.
There are serialisations (RLP, FATE), sequences of serializations (`S1, S2, ...`),
sequences of bytes (`<< .... >>`) and sequences of bits (`<<< ... >>>`).

Fate Code uses both RLP enodings and pure byte arrays (or binary) encodings.
In the description here we write `RLP(X)` for the RLP encoding of `X`, where
X is a name of an encoding described above or below in the description of
the FATE encoding. We write `<X, Y>` for a byte array made of the sequence of
the byte encodings of `X` and `Y`. We write `X(Y)` to denote the encoding
of the type `Y` using the encoding `X`.

We write `< >` for the empty sequence and use `|` for alternatives. We
use hexadecimal numbers to represent specific bytes used to indicate
what is encoded, e.g. `0xfe` for a function. We use `_` to denote any
byte in a byte sequence `<< _ >>` or any encoding in a encoding
sequence ` _, `.

We use `<<< X, Y >>>` to denote the bitpattern of the bits `X` followed
by the bits `Y` where the bits on the left (`X`) are the most significant bits.
A bitpattern should produce a number of bits devisable by 8, if not the pattern
should be padded with zeroes on the left (in the high order) until it is devisable by 8.
We use ```<<< xy >>>``` as a shorthand for ```<<< x, y >>>``` when `x` and `y` are
just 0 or 1 and not a recursive definition.


We use `; Text` to denote a comment that is not part of the encoding but
used to make the meaning of the encoding clear.

### FATE top level
A fate contract is serialized as follows
```
Contract ::=
  RLP(Code),
  RLP(Symbols),
  RLP(Annotations)
```

### Code
Functions are sorted on their name (a name in this setting is the 4 first bytes of the blake2b
hash of the program level readable name). Only one function of each name is allowed.
```
Code ::=
  < >
| Function , Code


```

### Function
```
Function ::=
  0xfe,
  Id,
  Attributes,
  Type Signature,
  Instructions
```

### Id
The Id is four bytes. The convention used by the reference compiler and
other tools is that this name is the first 4 bytes of the blake2b hash of
the function name. This is also true for the special `init` function.
that is called by the `contract_create` transaction. This function
must have the following Id: `<<0x44, 0xd6, 0x44, 0x1f>>`.

But on a protocol level all other name could be any 4 bytes,
just as long as all functions in the same contract have different Ids.
```
Id ::=
  << _, _, _, _>>

```

### Attributes
Attributes are encoded as the data encoding of the integer encoding
the bit pattern where each bit indicates one attribute as follows:
* bit 0: private
* bit 1: payable

```
Attributes :==
  Integer(A)

A :==
  0 ;; No attribute
  1 ;; private
  2 ;; payable
  3 ;; private and payable

```

### Type Signature
The type signature of a function defines the type of the function.
Types are given in FATE's type language.
Given a list of the types of the arguments (Args) and the
return type (RetType) the type signature is encoded as follows.

```
Type Signature ::=
  Type({tuple, Args}),
  Type(RetType)
```

### Instructions
The code itself is encoded as a series of instructions that
can be broken up into basic blocks.
```
Instructions ::=
  Instruction
| Instruction, Instructions
```

### Instruction
Each instruction is encoded by its opcode and for opcodes taking
an argument the addressing mode it uses followed by the argument.
Depending on the number of arguments to an instruction the
addressing mode can take up one or two bytes.

```
Instruction ::=
  Opcode,
  AddressingMode,
  Arguments
```

### Opcode

```
Opcode ::=
  0x00 ; 'RETURN'
| 0x01 ; 'RETURNR'
| 0x02 ; 'CALL'
| 0x03 ; 'CALL_R'
| 0x04 ; 'CALL_T'
| 0x05 ; 'CALL_GR'
| 0x06 ; 'JUMP'
| 0x07 ; 'JUMPIF'
| 0x08 ; 'SWITCH_V2'
| 0x09 ; 'SWITCH_V3'
| 0x0a ; 'SWITCH_VN'
| 0x0b ; 'CALL_VALUE'
| 0x0c ; 'PUSH'
| 0x0d ; 'DUPA'
| 0x0e ; 'DUP'
| 0x0f ; 'POP'
| 0x10 ; 'INCA'
| 0x11 ; 'INC'
| 0x12 ; 'DECA'
| 0x13 ; 'DEC'
| 0x14 ; 'ADD'
| 0x15 ; 'SUB'
| 0x16 ; 'MUL'
| 0x17 ; 'DIV'
| 0x18 ; 'MOD'
| 0x19 ; 'POW'
| 0x1a ; 'STORE'
| 0x1b ; 'SHA3'
| 0x1c ; 'SHA256'
| 0x1d ; 'BLAKE2B'
| 0x1e ; 'LT'
| 0x1f ; 'GT'
| 0x20 ; 'EQ'
| 0x21 ; 'ELT'
| 0x22 ; 'EGT'
| 0x23 ; 'NEQ'
| 0x24 ; 'AND'
| 0x25 ; 'OR'
| 0x26 ; 'NOT'
| 0x27 ; 'TUPLE'
| 0x28 ; 'ELEMENT'
| 0x29 ; 'SETELEMENT'
| 0x2a ; 'MAP_EMPTY'
| 0x2b ; 'MAP_LOOKUP'
| 0x2c ; 'MAP_LOOKUPD'
| 0x2d ; 'MAP_UPDATE'
| 0x2e ; 'MAP_DELETE'
| 0x2f ; 'MAP_MEMBER'
| 0x30 ; 'MAP_FROM_LIST'
| 0x31 ; 'MAP_SIZE'
| 0x32 ; 'MAP_TO_LIST'
| 0x33 ; 'IS_NIL'
| 0x34 ; 'CONS'
| 0x35 ; 'HD'
| 0x36 ; 'TL'
| 0x37 ; 'LENGTH'
| 0x38 ; 'NIL'
| 0x39 ; 'APPEND'
| 0x3a ; 'STR_JOIN'
| 0x3b ; 'INT_TO_STR'
| 0x3c ; 'ADDR_TO_STR'
| 0x3d ; 'STR_REVERSE'
| 0x3e ; 'STR_LENGTH'
| 0x3f ; 'BYTES_TO_INT'
| 0x40 ; 'BYTES_TO_STR'
| 0x41 ; 'BYTES_CONCAT'
| 0x42 ; 'BYTES_SPLIT'
| 0x43 ; 'INT_TO_ADDR'
| 0x44 ; 'VARIANT'
| 0x45 ; 'VARIANT_TEST'
| 0x46 ; 'VARIANT_ELEMENT'
| 0x47 ; 'BITS_NONEA'
| 0x48 ; 'BITS_NONE'
| 0x49 ; 'BITS_ALLA'
| 0x4a ; 'BITS_ALL'
| 0x4b ; 'BITS_ALL_N'
| 0x4c ; 'BITS_SET'
| 0x4d ; 'BITS_CLEAR'
| 0x4e ; 'BITS_TEST'
| 0x4f ; 'BITS_SUM'
| 0x50 ; 'BITS_OR'
| 0x51 ; 'BITS_AND'
| 0x52 ; 'BITS_DIFF'
| 0x53 ; 'BALANCE'
| 0x54 ; 'ORIGIN'
| 0x55 ; 'CALLER'
| 0x56 ; 'BLOCKHASH'
| 0x57 ; 'BENEFICIARY'
| 0x58 ; 'TIMESTAMP'
| 0x59 ; 'GENERATION'
| 0x5a ; 'MICROBLOCK'
| 0x5b ; 'DIFFICULTY'
| 0x5c ; 'GASLIMIT'
| 0x5d ; 'GAS'
| 0x5e ; 'ADDRESS'
| 0x5f ; 'GASPRICE'
| 0x60 ; 'LOG0'
| 0x61 ; 'LOG1'
| 0x62 ; 'LOG2'
| 0x63 ; 'LOG3'
| 0x64 ; 'LOG4'
| 0x65 ; 'SPEND'
| 0x66 ; 'ORACLE_REGISTER'
| 0x67 ; 'ORACLE_QUERY'
| 0x68 ; 'ORACLE_RESPOND'
| 0x69 ; 'ORACLE_EXTEND'
| 0x6a ; 'ORACLE_GET_ANSWER'
| 0x6b ; 'ORACLE_GET_QUESTION'
| 0x6c ; 'ORACLE_QUERY_FEE'
| 0x6d ; 'AENS_RESOLVE'
| 0x6e ; 'AENS_PRECLAIM'
| 0x6f ; 'AENS_CLAIM'
| 0x70 ; 'AENS_UPDATE'
| 0x71 ; 'AENS_TRANSFER'
| 0x72 ; 'AENS_REVOKE'
| 0x73 ; 'BALANCE_OTHER'
| 0x74 ; 'VERIFY_SIG'
| 0x75 ; 'VERIFY_SIG_SECP256K1'
| 0x76 ; 'CONTRACT_TO_ADDRESS'
| 0x77 ; 'AUTH_TX_HASH'
| 0x78 ; 'ORACLE_CHECK'
| 0x79 ; 'ORACLE_CHECK_QUERY'
| 0x7a ; 'IS_ORACLE'
| 0x7b ; 'IS_CONTRACT'
| 0x7c ; 'IS_PAYABLE'
| 0x7d ; 'CREATOR'
| 0x7e ; 'ECVERIFY_SECP256K1'
| 0x7f ; 'ECRECOVER_SECP256K1'
| 0xfa ; 'DEACTIVATE'
| 0xfb ; 'ABORT'
| 0xfc ; 'EXIT'
| 0xfd ; 'NOP'
| 0xfe ; 'FUNCTION' only used outside of BBs
| 0xff ; 'EXTEND' reserved for extending instruction set to two bytes, not used yet.

```


### AddressingMode

```
AddressingMode ::=
  < >
| LowAddressingMode
| HighAddressingMode | LowAddressingMode

LowAddressingMode ::=
  <<< Mode, Mode, Mode, Mode >>> ; Arg3 Arg2 Arg1 Arg0

HighAddressingMode ::=
  <<< Mode, Mode, Mode, Mode >>> ; Arg7 Arg6 Arg5 Arg4

Mode ::=
  <<< 00 >>> ; top of stack (or unused if arity < this pos) Arguments empty
| <<< 01 >>> ; function argument N, N given by Arguments
| <<< 10 >>> ; variable N or store -N if N is negative, N given by Arguments
| <<< 11 >>> ; immediate, value given by arguments

```


### Arguments

```
Arguments ::=
  < >
| Argument, Arguments

Argument ::=
  Integer(N) ; For function argument, variable or store.
| Data(D)    ; For immediates
```


### Data

```
Data(D) ::=
  Boolean
| Integer
| String
| Bytes
| Bits
| Address
| ContractAddress
| Oracle
| OracleQuery
| Channel
| Tuple
| List
| Map
| StoreMap
| Variant
| Type
```

#### Boolean
```
Boolean ::=
  <<<11111111>>> ; True
| <<<01111111>>> ; False
```

#### Integer
```
Integer(I) ::=
  <<< 0,  I, 0 >>>                     ; When abs(I) <  64, I >= 0
| <<< 1, -I, 0 >>>                     ; When abs(I) <  64, I <  0
| <<< 01101111 >>>, LargeInt(I - 64)   ; When abs(I) >= 64, I >= 0
| <<< 11101111 >>>, LargeInt(-I - 64)  ; When abs(I) >= 64, I <  0

LargeInt(I) ::=
  RLP(Unsigned(I))

;; Encode an unsigned int
;; where 'shr' is bitwise shift right, and 'band' is bitwise and.
Unsigned(I) ::=
  << 0 >> ;; When I = 0
| Unsigned(I shr 8), (I band 0xff)

```

#### String
A FATE string is just a byte array. The function size(S) gives the
number of bytes in the byte array.

```
String(S) ::=
  <<< 01011111 >>>                           ; when size(S)  =  0 , S is empty ("")
| <<< size(S), 01 >>>, S                     ; when size(S) <  64
| <<< 00000001 >>>, Integer(size(S) - 64), S ; when size(S) >= 64
```

#### Bits
A FATE bitmap is represented as an integer, a negative integer
is used for a bitmap with infinitely many 1 bits on the left.
```
Bits(B) ::=
  <<< 01001111 >>> LargeInt( B) ; when B >= 0
| <<< 11001111 >>> LargeInt(-B) ; when B <  0
```

#### Bytes

```
Bytes(B) ::=
  <<<10011111>>>, <<<00000001>>>, String(B)
```

#### Address

```
Address(A) ::=
  <<<10011111>>>, <<<00000000>>>, RLP(A)
```

#### ContractAddress

```
ContractAddress(C) ::=
  <<<10011111>>>, <<<00000010>>>, RLP(C)
```

#### Oracle

```
Oracle(O) ::=
  <<<10011111>>>, <<<00000011>>>, RLP(O)
```

#### OracleQuery

```
OracleQuery(Q) ::=
  <<<10011111>>>, <<<00000100>>>, RLP(Q)
```

#### Channel

```
Channel(C) ::=
  <<<10011111>>>, <<<00000101>>>, RLP(C)
```


#### Tuple
The function tuple_size gives the number of elements of the tuple.
The elements are serialized in order from left to right.

```
Tuple(T) ::=
  <<< 00111111 >>>                                        ; for the empty tuple (Unit)
| <<< tuple_size(T), 1011 >>>, Elements                   ; when tuple_size(T) < 16
| <<< 00001011 >>>, Integer(tuple_size(T) - 16), Elements ; Otherwise

Elements ::=
  Data
| Data, Elements
```

####  List
The function length gives the number of elements in the list.
The elements of the list are serialized in order from left to right.

```
List(L) ::=
  <<< length(L),  0011 >>>, ListElements(L) ; when length(L) < 16
  <<< 00011111 >>>, RLP(length(L) - 16), ListElements(L)

ListElements ::=
  Data
| Data, ListElements

```

#### Map
The function map_size gives the number of key value pairs in the map.
The key value pairs are serialized in key order with the smallest
key in the order given by the FATE data order. Each pair is
serialized toghether, first the key and then the value.

There must not be any duplicate keys in the map.

```
Map(M) ::=
  <<< 00101111 >>>, RLP(map_size(M)), MapElements

MapElements ::=
  Key, Val
| Key, Value, MapElements

```


#### StoreMap
A store map is just the ID (an integer) of the map in the contract store.
See the description of FATE for a longer explanation of Store Maps.

```
StoreMap(ID) ::=
  <<< 10111111 >>>, Integer(ID)
```

#### Variant
See the description of FATE for a longer explanation of variant types.
A Variant have a number of different "variants" each with an arity.
There can at most be 255 variants and there has to be at least 1 arity.
The arity describes how many different elements each variant has.
Each arity can be in the range of 0 to 255.
The function arities gives a list of the arities of each variant of the variant.
The specific variant is defined by the "tag" which is the ordinal of the
arity in the list of arities, given byt the function tag.
The value of the variant is serialized as an tuple of the elements
of the variant given by the variant_elements function.

```
Variant(V) ::=
  <<<10101111>>>, RLP(arities(V)), << tag(V) >>, Tuple(variant_elements(V))
```

#### Type


```
Type(T) ::=
  IntegerType
| BooleanType
| ListType(list_element_type(T))
| TupleType(tuple_element_types(T))
| AddressType
| ContractType
| OracleType
| OracleQueryType
| ChannelType
| BitsType
| MapType(T)
| StringType
| VariantType(T)
| BytesType(bytes_types_size(T))
| AnyType
| VarType(var_type_id(T))

IntegerType      ::= <<< 00000111 >>>
BooleanType      ::= <<< 00010111 >>>
ListType(ET)     ::= <<< 00100111 >>>, Type(ET)
TupleType(ETs)   ::= <<< 00110111 >>>, length(ETs), TupleElementTypes(ETs)
AddressType      ::= <<< 01000111 >>>, <<< 00000000 >>>
ContractType     ::= <<< 01000111 >>>, <<< 00000010 >>>
OracleType       ::= <<< 01000111 >>>, <<< 00000011 >>>
OracleQueryType  ::= <<< 01000111 >>>, <<< 00000100 >>>
ChannelType      ::= <<< 01000111 >>>, <<< 00000101 >>>
BitsType         ::= <<< 01010111 >>>
MapType(T)       ::= <<< 01100111 >>>, Type(key_type(T)), Type(value_type(T))
StringType       ::= <<< 01110111 >>>
VariantType(T)   ::= <<< 10000111 >>>, << size(type_arities(T)) >>, VariantTypes(variant_type_elements(T))
BytesType(N)     ::= <<< 10010111 >>>, Integer(N)
AnyType          ::= <<< 11110111 >>>
VarType(N)       ::= <<< 11100111 >>>, << N >>

TupleElementTypes(T) ::= < > | Type, TupleElementTypes

VariantTypes(T)      ::= < > | Type, VariantTypes

```
