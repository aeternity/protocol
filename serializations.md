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

#### Block header

For block headers all fields sizes are statically known and can be
constructed directly as a byte array.

| Fieldname | Size (bytes) |
| --- | --- |
| version      | 8    |
| height       | 8    |
| prev_hash    | 32   |
| txs_hash     | 32   |
| root_hash    | 32   |
| target       | 8    |
| pow_evidence | 168  |
| nonce        | 8    |
| time         | 8    |


#### Block

The only difference between a block and its header is the list of
transactions. The transactions are captured in the header by the
transaction root hash (txs_hash). The block does not currently have a
separate binary serialization form since the block hash is computed
from the block header.

## Dynamic size object serialization

In this section we use `[]` to mean lists, `<name>` to denote fields,
`,` to separate fields in lists. We use `::` to separate fields from
their types . We use `int()` to denote the integer type and `binary()`
to denote the byte array type. Lists are denoted with `[]` in the type
domain (e.g., `[int()]` is a list of integers). We use `++` as the
list concatenation operator. We also use the `bool()` type as the
special case of the integers `0` and `1` used as the boolean type.

### RLP Encoding

We use the Recursive Length Prefix encodng
(https://github.com/ethereum/wiki/wiki/RLP) for serializing objects that
have dynamic sizes of the fields.

RLP ensures that there is only one serialization of each corresponding
object on the lowest level, but it can only encode two primitive
objects, lists and byte arrays.

Objects in Æternity are encoded as lists of fields, where the two
first fields describe the object type and the object version.

```
[ <tag>, <version>, <field1>, <field2>...]
```

Since all values are byte arrays in RLP, `int()` needs to be a byte
array as well. We encode all integers as unsigned, big endian byte
arrays. To avoid ambiguity in the encoding of integers, we adapt the
same scheme as RLP and demand that ingegers are encoded with the
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
| Coinbase transaction | 13 |
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

#### Accounts
```
[ <pubkey>  :: binary()
, <nonce>   :: int()
, <height>  :: int()
, <balance> :: int()
]
```
### Signed transaction
```
[ <signatures>  :: [binary()]
, <transaction> :: binary()
]
```


### Spend transaction
```
[ <sender>    :: binary()
, <recipient> :: binary()
, <amount>    :: int()
, <fee>       :: int()
, <nonce>     :: int()
, <payload>   :: binary()
]
```

### Coinbase transaction
```
[ <acct>   :: binary()
, <height> :: int()
, <reward> :: int()
]
```

#### Oracles
```
[ <owner>           :: binary()
, <query_format>    :: binary()
, <response_format> :: binary()
, <query_fee>       :: int()
, <expires>         :: int()
]
```

#### Oracle queries
```
[ <sender_address> :: binary()
, <sender_nonce>   :: int()
, <oracle_address> :: binary()
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
[ <account>       :: binary()
, <nonce>         :: int()
, <query_spec>    :: binary()
, <response_spec> :: binary()
, <query_fee>     :: int()
, <ttl_type>      :: int()
, <ttl_value>     :: int()
, <fee>           :: int()
]
```

#### Oracle query transaction
```
[ <sender>             :: binary()
, <nonce>              :: int()
, <oracle>             :: binary()
, <query>              :: binary()
, <query_fee>          :: int()
, <query_ttl_type>     :: int()
, <query_ttl_value>    :: int()
, <response_ttl_type>  :: int()
, <response_ttl_value> :: int()
, <fee>                :: int()
```

#### Oracle response transaction
```
[ <oracle>   :: binary()
, <nonce>    :: int()
, <query_id> :: binary()
, <response> :: binary()
, <fee>      :: int()
]
```

#### Oracle extend transaction
```
[ <oracle>    :: binary()
, <nonce>     :: int()
, <ttl_type>  :: int()
, <ttl_value> :: int()
, <fee>       :: int()
]
```

#### Contract
```
[ <pubkey>     :: binary()
, <balance>    :: int()
, <height>     :: int()
, <owner>      :: binary()
, <vm_version> :: int()
, <code>       :: binary()
, <state>      :: binary(),
, <log>        :: binary(),
, <active>     :: bool(),
, <referers>   :: [binary()],
, <deposit>    :: int()
]
```

#### Contract call
```
[ <caller_address>   :: binary()
, <caller_nonce>     :: int()
, <nonce>            :: int()
, <height>           :: int()
, <contract_address> :: binary()
, <gas_used>         :: int()
, <return_value>     :: binary()
, <return_type>      :: int()
]
```

#### Contract create transaction
```
[ <owner>      :: binary()
, <nonce>      :: int()
, <code>       :: binary()
, <vm_version> :: int()
, <fee>        :: int()
, <deposit>    :: int()
, <amount>     :: int()
, <gas>        :: int()
, <gas_price>  :: int()
, <call_data>  :: binary()
]
```

#### Contract call transaction
```
[ <caller>     :: binary()
, <nonce>      :: int()
, <contract>   :: binary()
, <vm_version> :: int()
, <fee>        :: int()
, <amount>     :: int()
, <gas>        :: int()
, <gas_price>  :: int()
, <call_data>  :: binary()
]
```

#### Name service name
```
[ <hash>     :: binary()
, <owner>    :: binary()
, <expires>  :: int()
, <status>   :: binary()
, <ttl>      :: int()
, <pointers> :: binary() TODO: This is currently ambigous
```

#### Name service commitment
```
[ <hash>    :: binary()
, <owner>   :: binary()
, <created> :: int()
, <expires> :: int()
]
```

#### Name service claim transaction
```
[ <account>   :: binary()
, <nonce>     :: int()
, <name>      :: binary()
, <name_salt> :: int()
, <fee>       :: int()
]
```

#### Name service preclaim transaction
```
[ <account>    :: binary()
, <nonce>      :: int()
, <commitment> :: binary()
, <fee>        :: int()
]
```

#### Name service update transaction
```
[ <account>  :: binary()
, <nonce>    :: int()
, <hash>     :: binary()
, <name_ttl> :: int()
, <pointers> :: binary() TODO: This is currently ambigous
, <ttl>      :: int()
, <fee>      :: int()
]
```

#### Name service revoke transaction
```
[ <account> :: binary()
, <nonce>   :: int()
, <hash>    :: binary()
, <fee>     :: int()
]
```

#### Name service transfer transaction
```
[ <account>   :: binary()
, <nonce>     :: int()
, <hash>      :: binary()
, <recipient> :: binary()
, <fee>       :: int()
```
