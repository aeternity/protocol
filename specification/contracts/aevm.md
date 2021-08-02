# The æternity Ethereum Virtual Machine (AEVM)

The AEVM is a version of the EVM: https://github.com/ethereum/yellowpaper

The AEVM can be emulated inside the æternity node and no marshaling of
arguments, code and data is necessary.  This makes for fast upstart
and faster execution of most smaller contracts.

There are a few differences between the EVM and the AEVM.

The AEVM provides an number of primitive operations that can be
used to interact with the chain.

The SELFDESTRUCT instruction is not immediate, instead the contract is
set in a disabled state where neither new contracts nor call
transactions can call the contract directly. When all other contracts
referring to a disabled contract are fully disabled the contract is
disabled.

## æternity primitive operations

Interaction with the first class objects of the æternity chain (e.g.
oracles, names, and state channels) is done through calls to a
built-in contract at address 0.


The value in the call indicates the tokens that the primop can use from the contract account.
Unused tokens stay on the contract account.

The first argument in the call specifies which primop to call.
The following arguments are encoded as Sophia data.

The total gas of the operation is a sum of the base gas and the op gas.

| OpNo | Name                |          Value |             Arguments | Return value    | Base gas  | Op gas   |
| ---- | ------------------- | -------------- | --------------------- | --------------- | --------- | -------- |
|    1 | Spend               | `Amount : int` | `Recipient : address` | `Nil`           | 12000     |        0 |
|  100 | Oracle register     | (Unused.)      | `Acct : address, Sign : signature, QFee : int, TTL : Chain.ttl, QType : typerep, RType : typerep` | `Oracle : address` | 12000    | Proportional to oracle TTL argument `TTL` (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` and the byte size of the transaction representing this operation, specifically: `byte_size(OracleRegisterTx) * GasPerByte` |
|  101 | Oracle query        | `QFee : int`   | `Oracle : address, Query : 'a, QTTL : Chain.ttl, RTTL : Chain.ttl` | `Query : address` | 12000 | Proportional to oracle query TTL argument `QTTL` (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` and the byte size of the transaction representing this operation, specifically: `byte_size(OracleQueryTx) * GasPerByte` |
|  102 | Oracle respond      | (Unused.)      | `Oracle : address, Query : address, Sign : signature, R : 'b` | `()` | 12000 | Proportional to oracle response TTL argument `RTTL` in oracle query (as found in the oracle query in the state, and interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` and the byte size of the transaction representing this operation, specifically: `byte_size(OracleRespondTx) * GasPerByte` |
|  103 | Oracle extend       | (Unused.)      | `Oracle : address, Sign : signature, TTL : Chain.ttl` | `()` | 12000    | Proportional to oracle TTL argument `TTL` (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` |
|  104 | Oracle get answer   | (Unused.)      | `Oracle : address, Query : address` | `option('b)` | 12000    | 0 |
|  105 | Oracle get question | (Unused.)      | `Oracle : address, Query : address` | `'a` | 12000  | 0 |
|  106 | Oracle query fee    | (Unused.)      | `Oracle : address`    | `int`           | 12000     | 0        |
|  200 | Name resolve        | (Unused.)      | `Name : string, Key : string, Type : typerep` | `option(address)` | 12000 | 0 |
|  201 | Name preclaim       | (Unused.)      | `Account : address, Commitment : hash, Sign : signature` | `()` | 12000 | Proportional to the byte size of the transaction representing this operation, specifically: `byte_size(NamePreclaimTx) * GasPerByte` |
|  202 | Name claim          | (Unused.)      | `Account : address, Name : string, Salt : int, Sign : signature` | `()` | 12000 | Proportional to the byte size of the transaction representing this operation, specifically: `byte_size(NameClaimTx) * GasPerByte` |
|  203 | Name update         | (Unused.)      | TODO | TODO | TODO | TODO |
|  204 | Name transfer       | (Unused.)      | `From : address, To : address, Hash : hash, Sign : signature` | `()` | 12000 | 0 |
|  205 | Name revoke         | (Unused.)      | `Addr : address, Hash : hash, Sign : signature` | `()` | 12000 | 0 |

`GasPerByte` is 20.

Note that the gas cost indicated in the table above does not include the gas required for the call instruction to the primop.

Calling state changing prim-ops in oracles and names's trees in off-chain
environment results in an error with output data `not_allowed_off_chain`.

## Chain specific instructions

The COINBASE instruction return the beneficiary of the current generation
stored in the previous key block.
When executing a contract in a state channel off-chain, COINBASE will return
the beneficiary of the previous key block as seen by the participant executing
the contract. In a forced progress call the COINBASE will return the
current beneficiary.

The TIMESTAMP instruction returns the timestamp of the current micro block.
When executing a contract in a state channel off-chain TIMESTAMP will return
the timestamp of the last block as seen by the participant executing the
contract. In a forced progress call the TIMESTAMP will return the timestamp
of the current micro block.

The DIFFICULTY instruction returns the difficulty of the current
generation stored in the previous key block.
When executing a contract in a state channel off-chain DIFFICULTY will return
the difficulty of the current generation stored in the last key block as seen
by the participant executing the contract. In a forced progress call the
DIFFICULTY will return the difficulty of the current generation.

The BLOCKHASH instruction returns the hash of the key block at the specified height.
If the height is below genesis height the instruction returns 0.
If the height is higher than or equal to the current height the instruction returns 0.
If the height is lower than current height minus 256 the instruction returns 0.
When executing a contract in a state channel (either off-chain or in
a force progress) BLOCKHASH will return the hash of the key block at the
specified heigh as seen by the one executing the contract.

## The Sophia\_AEVM\_01 ABI

### Byte code

The byte code contains meta data about the original sophia source
code.

#### Meta data
The byte code contains meta data for the contract.
- source_code_hash - a Blake2b hash of the source code string of the contract
- type_info - see Type information below
- byte_code - the actual byte code

The layout of the encoding can be found
[here](https://github.com/aeternity/protocol/blob/master/serializations.md#sophia-byte-code). 
The encoding is tagged with the compiler version.

#### Type information
The type information of each function is encoded in the meta data. The function
hash depends both on the function name and the type signature of the function.
The function hash is also the identifier of a function when calling a contract.
In this way, the function prototype in the calling function gets some level of
type verification.

The type information contains:
- fun_hash - A Blake2b hash of the function name and the function types
- fun_name - The function name as a string
- arg_type - The vm encoded typerep of the argument (as a tuple) of the function
- out_type - The vm encoded typerep of the return type of the function

### Memory layout

Sophia values are 256-bit words. In case of unboxed types (`int`,
`address`, and `bool`) this is simply the value. For boxed types
such as tuples and (non-empty) lists, the word is a pointer into the heap
(memory).

More precisely

- Unboxed types are represented as a single big endian 256-bit (32 bytes) word.
  Booleans are represented as 0 for `false` and 1 for `true`. The empty list is
  represented as an unboxed -1. In memory maps are represented by an unboxed
  unique identifier. The contents of the map is stored separately in the VM
  state.

- Boxed types are represented as a 256-bit pointer to a contiguous sequence of
  words, called a *heap object*, on the heap.

  | Value/Type | Heap object                                                                                                                  |
  | ---        | ---                                                                                                                          |
  | Tuple      | The value of each component in left-to-right order.                                                                          |
  | String     | The length (number of bytes), followed by as many words as required to store the character data, padded on the right with 0. |
  |            |                                                                                                                              |

  The following types are represented in terms of other types:

  <table>
  <tr><th>Type</th><th>Representation</th></tr>
  <tr><td>Non-empty list</td><td>A pair of the head and the tail.</td></tr>
  <tr><td>Record</td><td>A tuple of the field values.</td></tr>
  <tr><td>Data type</td>
      <td>A tuple where the first component is a constructor
          tag (starting with 0 for the first constructor), and the following
          components are the constructor arguments. For instance, for<br/><br/>
          <tt>datatype zeroOrTwo = Zero | Two(int, int)</tt><br/><br/>
          <tt>Zero</tt> is encoded as a singleton tuple <tt>(0)</tt> and
          <tt>Two(a, b)</tt> as the triple <tt>(1, a, b)</tt>.
      </td></tr>
  <tr><td>Signature</td><td>A pair of two 256-bit words.</td></tr>
  <tr><td>Option types</td><td><tt>datatype option('a) = None | Some('a)</tt>.</td></tr>
  <tr><td><tt>ttl</tt></td><td><tt>datatype ttl = RelativeTTL(int) | FixedTTL(int)</tt></td></tr>
  <tr><td>Type representations</td>
      <td>
      When types need to be encoded as data, they are represented as the following datatype<br/><br/>
      <div>
      <pre>
        datatype typerep = Word  // any unboxed type
                         | String
                         | List(typerep)
                         | Tuple(list(typerep))
                         | Datatype(list(list(typerep)))
                         | TypeRep
                         | Map(typerep, typerep)
      </pre></div>
      The argument to the <tt>Datatype</tt> constructor is the list of type
      representations of the constructor arguments.
      </td></tr>
  </table>

### Encoding Sophia values as binaries

When communicating Sophia values between a contract and the outside world they
are encoded as a binary containing a heap whose first word is the encoded value
(except in the case of maps, see below). For example, the value `("main", (1, 2, 3))`
can be encoded as
```
Word       0       1       2       3       4       5       6       7
Addr    0x00    0x20    0x40    0x60    0x80    0xA0    0xC0    0xE0
Value   0x20    0x60    0xA0       4   "main"      1       2       3
```
where `"main"` is the 32 byte word obtained by right padding the string
`"main"` with zeroes.

Note that the order of the heap objects on the heap is unspecified. Another
valid encoding of the same value is
```
Word       0       1       2       3       4       5       6       7
Addr    0x00    0x20    0x40    0x60    0x80    0xA0    0xC0    0xE0
Value   0x60       4   "main"   0x20    0xA0       1       2       3
```

A canonical binary representation is obtained by storing heap objects in
depth-first left-to-right order (as in the first example). This is the
representation used in map keys.

#### Binary encoding of Sophia maps

In memory, maps are represented by their unique identifier, but in binary
encodings the identifier is replaced by a boxed representation with a heap
object of the shape
```
    MapSize (N)
    KeySize1
  +----------+
  |   Key1   |
  +----------+
    ValSize1
  +----------+
  |   Val1   |
  +----------+
      ...
    KeySizeN
  +----------+
  |   KeyN   |
  +----------+
    ValSizeN
  +----------+
  |   ValN   |
  +----------+
```
The keys and values are encoded as standalone binaries, so the addresses in
`KeyI` (say) are relative only to the `KeyI` binary.

### Initialization

When a Sophia contract is called the calldata should be a pair of a function
hash and a tuple of arguments, encoded as a binary as described above
The value should be a pair of a function hash and a tuple of arguments
For instance, to call the function `foo` (assuming the function
hash 12345) with arguments `1` and `"bar"`, the calldata should be
(the binary encoding of)
```
  (12345, (1, "bar"))
```
Before the contract starts executing the first word of the encoded calldata
(i.e. the calldata value) is pushed on the stack and the rest of the calldata
heap is written to memory. The result is that the Sophia contract starts with
the value of the calldata on top of the stack.

If the contract state has been initialized it is stored on the heap and a
pointer to it is written to address 0. If the contract state has not been
initialized, for instance, when running the `init` function, 0 is written to
address 0. Note that address 0 contains a *pointer* to the value of the state,
not the value itself.

The compiler is responsible for generating the appropriate dispatch code,
looking at the calldata and calling the correct function.

### Return

When returning from a contract call (using the `RETURN` instruction) the
type information from the meta data is used to encode the return value.
The VM reads the return value from the heap and returns it to the caller,
and reads the updated contract state using the state pointer at address 0.
A contract can write 0 to the state pointer to indicate that the state
did not change.

### Storing the contract state

The contract state is stored in the *store* as a binary heap whose first word
is the value (with maps stored as their identifiers) under key `0x00`.
The type of the state is stored as an encoded type representation under key
`0x01` (***subject to change: contract state type to be stored in contract
metadata***). The list of maps in the contract state is stored under key `0x02`
as a sequence of 256-bit map identifiers. For each map there are mappings
(where `[X]` denotes a single 256-bit word):
```
  [MapId]      => [RealId] [RefCount] [Size] Types
  [RealId] Key => Val
```
`Types` is the binary encoding of the tuple `(KeyType, ValType)` of type
representations for the key and value types of the map. `Key` and `Val` are
stand-alone heap encodings with map identifiers for maps (although for keys
there are no maps). The `RealId` field is an indirection to allow in-place
updates of maps and the `RefCount` field is used to track the number of
occurrences of a map in other maps for the purpose of garbage collection.

The `init` function of a contract should return a pair of the state type
representation and the initial state, which are written to the store by the VM.
Note that the Sophia code for `init` only returns the initial state value--the
compiler is responsible for adding the type representation.

### Remote contract calls

The `CALL` instruction for calling another contract works differently for
Sophia contracts than in the EVM. It expects on the stack (top to bottom):
- `Gas` - the amount of gas to allocate to the call
- `Address` - the address of the contract to call (or 0 for primops)
- `Amount` - the amount of tokens to transfer with the call
- `Calldata` - the calldata value (pair of function hash and arguments)
- `TypeHash` - the function hash of primops that have dynamic types
               (e.g., oracles). Otherwise unused.
- `_` - unused (offset to write return value in the EVM)
- `_` - unused (return value size in the EVM)

The calldata is read from the heap guided by the calldata type and passed to
the called contract. Before the call is made gas is charged for the size of the
expanded calldata (e.g. maps have to be made explicit when passed between
contracts). When the call returns the return value is pushed on top of the
stack, and potential heap objects for the return value written to the top of
the heap. The return type from the contracts meta data is used when writing it
 to the heap. Since maps are handled outside the heap, the caller explicitly
pays gas for handling maps in the return value.

### Delegation signature
Some chain operations (`Oracle.<operation>` and `AENS.<operation>`) has an optional
delegation signature. This is typically used when a user/accounts would like to
allow a contract to act on it's behalf. The exact data to be signed varies for the
different operations, but in *all* cases you should prepend the signature data with
the `network_id` (`ae_mainnet` for the æternity mainnet, etc.).
