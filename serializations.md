# Serialization formats

The serialization formats in this document describes the binary format
used to encode the different objects in the binary format that is used
for:

* Hashing (e.g., block hash)
* Insertion in the Merkle Patricia Tree (e.g., state trees, transaction trees).
* Signing transactions (i.e., the serialized form is signed).

Other formats may be used for communication between nodes or for the
user API.



## Static size object serialization

There are two types of blocks:

* micro block - contains a header and a list of transactions.
* key block - contains only a header.

### Key block header

All field sizes are statically known and can be constructed directly as
a byte array.

| Fieldname  | Size (bytes) |
| --- | ---  |
| version     | 8    |
| height      | 8    |
| prev_hash   | 32   |
| state_hash  | 32   |
| miner       | 32   |
| beneficiary | 32   |
| target      | 8    |
| pow         | 168  |
| nonce       | 8    |
| time        | 8    |

### Micro block header

All field sizes of a micro block header are statically known and can be
constructed directly as a byte array.

| Fieldname | Size (bytes) |
| --- | --- |
| version    | 8    |
| height     | 8    |
| prev_hash  | 32   |
| state_hash | 32   |
| txs_hash   | 32   |
| time       | 8    |
| signature  | 64   |

Note that the position for the signature (64 bytes) must be filled
with only zeroes when constructing or validating the signature.

## Dynamic size object serialization

In this section we use `[]` to mean lists, `<name>` to denote fields,
`,` to separate fields in lists. We use `::` to separate fields from
their types . We use `int()` to denote the integer type and `binary()`
to denote the byte array type. Lists are denoted with `[]` in the type
domain (e.g., `[int()]` is a list of integers). We use `++` as the
list concatenation operator. We also use the `bool()` type as the
special case of the integers `0` and `1` used as the boolean type.

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


### RLP Encoding

We use the Recursive Length Prefix encodng
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
| Channel | 58 |
| Channel snapshot transaction | 59 |
| POI | 60 |
| Key block | 100 |
| Micro block | 101 |

#### Accounts
```
[ <nonce>   :: int()
, <balance> :: int()
]
```
### Signed transaction
```
[ <signatures>  :: [binary()]
, <transaction> :: binary()
]
```

Signatures are sorted.

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

#### Oracles
```
[ <owner>           :: id()
, <query_format>    :: binary()
, <response_format> :: binary()
, <query_fee>       :: int()
, <expires>         :: int()
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
[ <oracle>   :: id()
, <nonce>    :: int()
, <query_id> :: binary()
, <response> :: binary()
, <fee>      :: int()
, <ttl>      :: int()
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
, <vm_version> :: int()
, <code>       :: binary()
, <log>        :: binary(),
, <active>     :: bool(),
, <referers>   :: [id()],
, <deposit>    :: int()
]
```

The balance of the account is stored in the account state tree.

The contract storage (or state) which is a key value map from (key::binary() to value::binary())
is stored in its own subtree. The key for a contract storage value is:
```
<contractpubkey><16><key> :: binary()
```
The `<key>` is non-empty.

Each value is just stored as a binary as is - without tag or version.
If the value is the empty binary the key is pruned from the tree.

Contracts with vm_version == 1, i.e. Sophia contracts on the AEVM stores the memory layout of the
state as one binary value at address 0.

Contracts with vm_version == 2, i.e. Solidity contracts on the AEVM
stores the VM storage map containg 256 bit binaries for both keys and
values in the MPT. Undefined keys are treated as having the value 0
and keys bound to the value zero are stored as the empty binary, thus
purging them from the tree.


#### Contract call
```
[ <caller_address>   :: id()
, <caller_nonce>     :: int()
, <height>           :: int()
, <contract_address> :: id()
, <gas_price>        :: int()
, <gas_used>         :: int()
, <return_value>     :: binary()
, <return_type>      :: int()
]
```

#### Contract create transaction
```
[ <owner>      :: id()
, <nonce>      :: int()
, <code>       :: binary()
, <vm_version> :: int()
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
[ <caller>     :: id()
, <nonce>      :: int()
, <contract>   :: id()
, <vm_version> :: int()
, <fee>        :: int()
, <ttl>        :: int()
, <amount>     :: int()
, <gas>        :: int()
, <gas_price>  :: int()
, <call_data>  :: binary()
]
```

#### Name service name
```
[ <owner>    :: id()
, <expires>  :: int()
, <status>   :: binary()
, <ttl>      :: int()
, <pointers> :: binary() TODO: This is currently ambigous
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
, <pointers>   :: binary() TODO: This is currently ambigous
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

### Channels

#### Channel create transaction
```
[ <initiator>        :: id()
, <initiator_amount> :: int()
, <responder>        :: id()
, <responder_amount> :: int()
, <channel_reserve>  :: int()
, <lock_period>      :: int()
, <ttl>              :: int()
, <fee>              :: int()
, <delegates>        :: [id()]
, <state_hash>       :: binary()
, <nonce>            :: int()
]
```

#### Channel deposit transaction
```
[ <channel_id> :: id()
, <from>       :: id()
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
, <to>         :: id()
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
, <from>            :: id()
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
, <from>            :: id()
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
, <from>                   :: id()
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
, <from>            :: id()
, <payload>         :: binary()
, <ttl>             :: int()
, <fee>             :: int()
, <nonce>           :: int()
]
```

The payload is a serialized signed channel off-chain transaction and can not be empty.


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
[ <owner>    			:: id()
, <vm_version>  	:: int()
, <code>  	      :: binary()
, <deposit>  	    :: int()
, <call_data>     :: binary()
]

```

###### Channel off-chain update call contract

This is an update for calling a contract inside channel's off-chain state
tree.

```
[ <caller>  			:: id()
, <contract>      :: id(),
, <vm_version>  	:: int()
, <amount>  	    :: int()
, <call_data>     :: binary()
, <call_stack>    :: [int()]
]

```

#### Channel off-chain transaction

The channel off-chain transaction is not included directly in the transaction tree but indirectly as payload of:
* The channel close solo transaction;
* The channel slash transaction.

```
[ <channel_id>       :: id()
, <round>            :: int()
, <updates>          :: [update()]
, <state_hash>       :: binary()
]
```

#### Channel
```
[ <initiator>        :: id()
, <responder>        :: id()
, <total_amount>     :: int()
, <initiator_amount> :: int()
, <channel_reserve>  :: int()
, <delegates>        :: [id()]
, <state_hash>       :: binary()
, <round>            :: int()
, <lock_period>      :: int()
, <closes_at>        :: int()
]
```

#### Proof of inclusion on state trees (POI) :: poi()
```
[ {<accounts>  :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), [<mpt_value> :: binary()]}]}]}
, {<calls>     :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), [<mpt_value> :: binary()]}]}]}
, {<channels>  :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), [<mpt_value> :: binary()]}]}]}
, {<contracts> :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), [<mpt_value> :: binary()]}]}]}
, {<ns>        :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), [<mpt_value> :: binary()]}]}]}
, {<oracles>   :: [<proof_of_inclusion> :: {<root_hash> :: binary(), [{<mpt_hash> :: binary(), [<mpt_value> :: binary()]}]}]}
]
```

NOTE: `[{<mpt_hash>, <mpt_value>}]` is the sorted list of Merkle Patricia Tree nodes in the proof.
If the subtree (e.g. `<accounts>`) is empty,
then the serialization is just `[]` (e.g. `<accounts>` is `[{<root_hash>, []}]`);
otherwise it is a list of one element `[<proof_of_inclusion>]`
(e.g. `<accounts>` is `[{<root_hash>, [{<mpt_hash>, <mpt_value>}, {<mpt_hash>, <mpt_value>}]}]`;
`<accounts>` is `[{<root_hash>, []}]`).

NOTE: As the POI contains the Merkle Patricia Tree nodes (e.g. not only their hashes):
* Each state subtree does not necessarily contain elements of the same key length.
* The object itself does not contain its own id as it can be derived from the location in the tree.
* The key used for storing each object in each state subtree is not necessarily derived from the object itself.
* The value(s) whose inclusion the POI proves is included in the POI itself.

### Blocks

### Micro block

```
[ <header>       :: binary()
, <transactions> :: [binary()]
]
```
NOTE: The transactions are signed transactions.

### Key block

Key blocks contain no more information that their [headers](#key-block-header). However, in
order to distinguish between key blocks and micro blocks in transport
format, the header is wrapped and tagged in the same way as micro blocks.

```
[ <header>       :: binary()
]
```

