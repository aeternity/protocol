# FATE
The fast æternity transaction engine.

## Design

The high level machine (or the fast æternity transaction engine) has
æternity transactions as its basic operations and it operates
directly on the state tree of the æternity chain. This is a new
paradigm in blockchain virtual machine specifications which makes it
possible to create type safe and efficient implementations of the
machine.

Every operation is typed and all values are typed (either by being
stored in a typed memory or by a tag). Any type violation results in
an exception and reverts all state changes. In version 1.0 there will
be no catch instruction.

In addition to normal machine instructions, such as ADD, the machine
also has support for constructing most of the transactions available on
the æternity chain from native low level chain transaction
instructions.

The instruction memory is divided into functions and basic
blocks. Only basic blocks can be indexed and used as jump
destinations.

There are instructions to operate on the chain state tree in a safe and formalized way.

FATE is "functional" in the sense that "updates" of data structures,
such as tuples, lists or maps do not change the old values of the
structure. Instead a new version is created, unless specific
operations to write to the contract store are used.

FATE does have the ability to write the value of an operation back to the
same register or stack position as one of the arguments, in effect updating
the memory. Thus, any other references to the structure before the operation
will have the same structure as before the operation.

### Objectives

#### Type safety

FATE solves some fundamental problems programmers run into when coding for
Ethereum: integer overflow, weak type checking and poor data
flow. FATE checks all arithmetic operations to keep the right meaning
of it. Also you can't implicitly cast types (eg integers to booleans).

In EVM contracts are not typed. When calling a function, EVM will try
to find which function you wanted to use by looking at the data that
you send into the code. In FATE, you have actual functions and the
functions have types - function call has to match the function type.

FATE ultimately makes a safer coding platform for smart contracts.

#### Rich data types

FATE has more built in data types: like maps, lists.

#### Faster transactions, smaller code size

Having a higher level instructions makes the code deployed smaller and
it reduces the blockchain size. Smaller code and smaller hashes also
keeps a blockchain network from clogging up and results in cheaper
transactions.

## Components

### Machine State
* Current contract: Address
* Current owner: Address
* Caller: Address
* Code: Code of current contract
* Memory: Several components as defined below
* CF, current function: Hash of current function
* CBB, current basic block: Index of current basic block.
* EC, Execution continuation: A list of instructions left in the current basic block.

### Memory
The machine memory is divided into:

* The chain top (block height, etc)
* Event stream
* The account state tree
* The contract store
* The execution/code memory
* Execution stack (push/pop on call/return)
* Accumulator stack (push/pop on instruction level)
* Local storage/stack/environment/context (push/pop on let...in...end)

#### The execution memory

The code to execute is stored in the execution memory. The execution
memory is a three level map. The key on the top level is a contract
address. The second level is a map from function hashes to a map of
basic blocks. The keys in the map of basic blocks are indices to basic
blocks (a 0 based, dense enumeration). The values are lists of
instructions.

When a contract is called the code of the contract is read from the
state tree into the execution memory. At this point the machine
implementation can deserialize the serialized version of FATE code
into instructions and basic blocks.

The serialization format for FATE code is described in Appendix 1:
[Fate instruction set and serialization](#appendix-1-fate-serialization).

#### The chain

The chain "memory" contains information about the current block and
the current iteration. These values are available through special
instructions.

* Beneficiary
* Timestamp
* (Block) Height
* Difficulty
* Gaslimit
* Address
* Balance
* Caller
* Value

#### The contract store

The permanent storage of a contract. Stored in the chain state
tree. This is a key value store that is mapped to the contract state
by the compiler.

The compiler can choose how to represent the contract state in the
store. For instance, save the entire state under a single key (this is
how it works in AEVM at the moment), or it could flatten any state
records and store each field under a separate key.

#### The state tree

Contains all accounts, oracles and contracts on the chain. Most values
such as account balances can be read directly through specific load
instructions. Some values can be changed through transaction
instructions.

#### The local storage

The local storage is a key value store.
The key is a an integer. The value can be of any FATE type.
The local store is local to a function call.

#### The accumulator stack

The accumulator stack is a stack of typed values. The top of the stack
can be used as an argument to an operation. Values can be pushed to
the stack and popped from the stack.

#### The execution stack

The execution stack contain return addresses as a tuple in the form of
{contract address, function hash, and basic block index}.

#### The event stream

A contract can emit events similar to the EVM.

## Types

The machine supports the following types:

* Integer (signed arbitrary precision integers)
* Boolean (true | false)
* Strings (arbitrary size byte arrays)
* Bytes (fixed size byte arrays)
* Bits (An arbitrary size bitmap)
* Address (A pointer into the state tree)
* Contract Address (A pointer to a contract)
* Oracle (A pointer to an oracle)
* Oracle Query (A pointer to an oracle query)
* Channel (A pointer to a channel)
* Tuples (a typed series of values)
* Lists (a list of values of a specific type)
* Maps (a key value store)
* Store Map (a key value store mapped to the contract state)
* Variant Types (a set of tagged and typed values)
* Type (a representation of a FATE type)

These types can be used as argument and return types of functions and
also as the type of the elements in the contract store.

### Integer

The type Integer, is used for any integer, infinitely large or small
(below zero).

Examples:

```
 0
 1
-1
589465789334
-51315353513513131656462262
```

### Boolean

The Boolean type only has two values, true or false.

Examples (all of them):
```
 true
 false
```

Operations on booleans include:

*   `and`, `or`, `not`
*   conditional jumps

### Addresses, Contract Addresses, Oracles, Oracle Querries, Channels

Values of any address type are 32-byte (256-bit) pointers to
entities on the chain (Accounts, Oracles, Contracts, etc)

Examples:
```
<<ak_2HNb8bivUoJTcaxD6VKDy2wPHvTuQgQRJ3dkF9RSyVFqBkMneC>>
```

### Strings

Strings are stored as byte arrays. From VM version `FATE_02` they are strictly
UTF-8 encoded unicode characters. In particular operations `String.to_list` and
`String.from_list` ensure that they only contain well formed code points.

Examples:
```
"Hello world"
"eof"
```

### Bytes

In VM versions `FATE_01` and `FATE_02` only fixed (size known at compile time)
size byte arrays exist. With the change to Strings, making them UTF-8 encoded
byte arrays, there is a need for general arbitrary length byte arrays. These
are introduced in `FATE_03` - and a couple of new operations handling (and
converting) byte arrays are added. Technical note: the bytes type was `{bytes,
N} / bytes(n)` - to change as little as possible arbitrary size byte arrays
have the type `{bytes, -1} / bytes()`.

### Tuples

Tuples have an arity indicating the number of elements in the
tuple. Each element in the tuple has a type. The 0-tuple is also
sometimes called unit.
The maximum number of elements in the tuple is 255 (included).

Examples:
```
 {}                Type: unit
 {1, 2}            Type: Tuple(Integer, Integer)
 {"foo", 42, true} Type: Tuple(String, Integer, Boolean)
```

### Lists

Lists are monomorphic series of values. Hence lists have a type. There
is also an empty list (or Nil).

Examples:
```
[]                   Type: Nil
[1, 2, 3]            Type: List(Integer)
[true, true, false]  Type: List(Boolean)
```

### Maps

Maps are monomorphic key value stores, that is the key is always the
same type for all elements in a map and the value has the same type in
all mappings in a map.  The key can have any type except a map.  The
value can have any type including a map.

Examples:
```
#{ (1, "foo"), (2, "bar") }
```
Type: Map(Integer, String)

```
#{ ("Fruit prices", #{ ("banana", 42), ("apple", 12)}),
   ("Stock prices", #{("Apple", 142), ("Orange", 112)}) }
```
Type: Map(String, Map(String, Integer))

### Variant Types

The variant type is a type consisting of a list of sizes and a tag (index)
where each tag represents a series of values of specified types. For
example you could have the Option type which could be None or
Some(Integer). The sizes of the variant are 0 and 1 (there are two variants),
The value None would be indicated by tag 0. The value
Some(42) would be represented by tag 1 followed by the integer 42.

Examples:
```
  (| [0,1] | 0 | () |)      ;; None
  (| [0,1] | 1 | (42) |)    ;; Some(42)

  (| 4 | 3 | (42, "foo", true) |) ;; Three(42, "foo", true)
```

Note that the tuple syntax for the elements does not indicate a Fate
tuple but a series of values.

### TypeRep

A TypeRep is the representation of a type as a value.
A TypeRep is one of

* integer
* boolean
* any
* {list, T}
* {tuple, Ts}
* address
* contract
* oracle
* oracle_query
* channel
* bits
* {bytes, N}
* {map, K, V}
* string
* {variant, ListOfVariants}
* {tvar, N}

where T, K and V are TypeReps, Ts is a list of TypeReps ([T1, T2, ... ]),
and ListOfVariants is a list ([]) of tuples of TypeReps
([{tuple, [Ts1]}, {tuple, [Ts2]} ... ]). N is a byte (0...255).

## Operations

All operations are typed. An operand can be the accumulator, an
immediate, a name, a reference to a field in the state tree, or a
reference to the contract state. The operand must be of the right
type.

### Operands

Operand specifiers are

*  immediate
*  arg
*  var
*  a (accumulator == stack 0)


The specifiers are encoded as

|      what |bits|
| --------- | -- |
| immediate | 11 |
|       var | 10 |
|       arg | 01 |
|     stack | 00 |

Operand specifiers for operations with 1 to 4 arguments
are stored in the byte following the opcode.
Operand specifiers for operations with 5 to 8 arguments
are stored in the two bytes following the opcode.
Note that for many operation the first argument (arg0) is
the destination for the operation.


| value: | arg3 | arg3 | arg2 | arg2 | arg1 | arg1 | arg0 | arg0 |
| ---    | ---  | ---  | ---  | ---  | ---  | ---  | ---  | ---  |
| bit:   |    7 |   6  |    5 |    4 |    3 |    2 |    1 |   0  |


| value: | arg8 | arg7 | arg6 | arg6 | arg5 | arg5 | arg4 | arg4 |
| ---    | ---  | ---  | ---  | ---  | ---  | ---  | ---  | ---  |
| bit:   |    7 |   6  |    5 |    4 |    3 |    2 |    1 |   0  |



Unused arguments should be set to 0.

E.g. an a :=  immediate + a would have the bit
pattern 00 11 00 00.

Each use of the accumulator pops an argument from the stack.
Writing to the accumulator pushes a value to the stack.

### Operations

#### Description of operations

| Name | Args | Description | Arg types | Res type | Added in VM version |
| ---- | ---- | ----------- | --------- | -------- | ------------------- |
| `RETURN` |  | Return from function call, top of stack is return value . The type of the retun value has to match the return type of the function. | {} | any | `FATE_01` |
| `RETURNR` | Arg0 | Push Arg0 and return from function. The type of the retun value has to match the return type of the function. | {any} | any | `FATE_01` |
| `CALL` | Arg0 | Call the function Arg0 with args on stack. The types of the arguments has to match the argument typs of the function. | {string} | any | `FATE_01` |
| `CALL_R` | Arg0 Identifier Arg2 Arg3 Arg4 | Remote call to contract Arg0 and function Arg1 of type Arg2 => Arg3 with value Arg4. The types of the arguments has to match the argument types of the function. | {contract,string,typerep,typerep,integer} | any | `FATE_01` |
| `CALL_T` | Arg0 | Tail call to function Arg0. The types of the arguments has to match the argument typs of the function. And the return type of the called function has to match the type of the current function. | {string} | any | `FATE_01` |
| `CALL_GR` | Arg0 Identifier Arg2 Arg3 Arg4 Arg5 | Remote call with gas cap in Arg4. Otherwise as CALL_R. | {contract,string,typerep,typerep,integer,integer} | any | `FATE_01` |
| `JUMP` | Integer | Jump to a basic block. The basic block has to exist in the current function. | {integer} | none | `FATE_01` |
| `JUMPIF` | Arg0 Integer | Conditional jump to a basic block. If Arg0 then jump to Arg1. | {boolean,integer} | none | `FATE_01` |
| `SWITCH_V2` | Arg0 Integer Integer | Conditional jump to a basic block on variant tag. | {variant,integer,ingeger} | none | `FATE_01` |
| `SWITCH_V3` | Arg0 Integer Integer Integer | Conditional jump to a basic block on variant tag. | {variant,integer,integer,ingeger} | none | `FATE_01` |
| `SWITCH_VN` | Arg0 [Integers] | Conditional jump to a basic block on variant tag. | {variant,{list,integer}} | none | `FATE_01` |
| `CALL_VALUE` | Arg0 | The value sent in the current remote call. | {} | integer | `FATE_01` |
| `PUSH` | Arg0 | Push argument to stack. | {any} | any | `FATE_01` |
| `DUPA` |  | Duplicate top of stack. | {any} | any | `FATE_01` |
| `DUP` | Arg0 | push Arg0 stack pos on top of stack. | {any} | any | `FATE_01` |
| `POP` | Arg0 | Arg0 := top of stack. | {integer} | integer | `FATE_01` |
| `INCA` |  | Increment accumulator. | {integer} | integer | `FATE_01` |
| `INC` | Arg0 | Increment argument. | {integer} | integer | `FATE_01` |
| `DECA` |  | Decrement accumulator. | {integer} | integer | `FATE_01` |
| `DEC` | Arg0 | Decrement argument. | {integer} | integer | `FATE_01` |
| `ADD` | Arg0 Arg1 Arg2 | Arg0 := Arg1 + Arg2. | {integer,integer} | integer | `FATE_01` |
| `SUB` | Arg0 Arg1 Arg2 | Arg0 := Arg1 - Arg2. | {integer,integer} | integer | `FATE_01` |
| `MUL` | Arg0 Arg1 Arg2 | Arg0 := Arg1 * Arg2. | {integer,integer} | integer | `FATE_01` |
| `DIV` | Arg0 Arg1 Arg2 | Arg0 := Arg1 / Arg2. | {integer,integer} | integer | `FATE_01` |
| `MOD` | Arg0 Arg1 Arg2 | Arg0 := Arg1 mod Arg2. | {integer,integer} | integer | `FATE_01` |
| `POW` | Arg0 Arg1 Arg2 | Arg0 := Arg1  ^ Arg2. | {integer,integer} | integer | `FATE_01` |
| `STORE` | Arg0 Arg1 | Arg0 := Arg1. | {any} | any | `FATE_01` |
| `SHA3` | Arg0 Arg1 | Arg0 := sha3(Arg1). | {any} | hash | `FATE_01` |
| `SHA256` | Arg0 Arg1 | Arg0 := sha256(Arg1). | {any} | hash | `FATE_01` |
| `BLAKE2B` | Arg0 Arg1 | Arg0 := blake2b(Arg1). | {any} | hash | `FATE_01` |
| `LT` | Arg0 Arg1 Arg2 | Arg0 := Arg1  < Arg2. | {integer,integer} | boolean | `FATE_01` |
| `GT` | Arg0 Arg1 Arg2 | Arg0 := Arg1  > Arg2. | {integer,integer} | boolean | `FATE_01` |
| `EQ` | Arg0 Arg1 Arg2 | Arg0 := Arg1  = Arg2. | {integer,integer} | boolean | `FATE_01` |
| `ELT` | Arg0 Arg1 Arg2 | Arg0 := Arg1 =< Arg2. | {integer,integer} | boolean | `FATE_01` |
| `EGT` | Arg0 Arg1 Arg2 | Arg0 := Arg1 >= Arg2. | {integer,integer} | boolean | `FATE_01` |
| `NEQ` | Arg0 Arg1 Arg2 | Arg0 := Arg1 /= Arg2. | {integer,integer} | boolean | `FATE_01` |
| `AND` | Arg0 Arg1 Arg2 | Arg0 := Arg1 and Arg2. | {boolean,boolean} | boolean | `FATE_01` |
| `OR` | Arg0 Arg1 Arg2 | Arg0 := Arg1  or Arg2. | {boolean,boolean} | boolean | `FATE_01` |
| `NOT` | Arg0 Arg1 | Arg0 := not Arg1. | {boolean} | boolean | `FATE_01` |
| `TUPLE` | Arg0 Integer | Arg0 := tuple of size = Arg1. Elements on stack. | {integer} | tuple | `FATE_01` |
| `ELEMENT` | Arg0 Arg1 Arg2 | Arg1 := element(Arg2, Arg3). | {integer,tuple} | any | `FATE_01` |
| `SETELEMENT` | Arg0 Arg1 Arg2 Arg3 | Arg0 := a new tuple similar to Arg2, but with element number Arg1 replaced by Arg3. | {integer,tuple,any} | tuple | `FATE_01` |
| `MAP_EMPTY` | Arg0 | Arg0 := #{}. | {} | map | `FATE_01` |
| `MAP_LOOKUP` | Arg0 Arg1 Arg2 | Arg0 := lookup key Arg2 in map Arg1. | {map,any} | any | `FATE_01` |
| `MAP_LOOKUPD` | Arg0 Arg1 Arg2 Arg3 | Arg0 := lookup key Arg2 in map Arg1 if key exists in map otherwise Arg0 := Arg3. | {map,any,any} | any | `FATE_01` |
| `MAP_UPDATE` | Arg0 Arg1 Arg2 Arg3 | Arg0 := update key Arg2 in map Arg1 with value Arg3. | {map,any,any} | map | `FATE_01` |
| `MAP_DELETE` | Arg0 Arg1 Arg2 | Arg0 := delete key Arg2 from map Arg1. | {map,any} | map | `FATE_01` |
| `MAP_MEMBER` | Arg0 Arg1 Arg2 | Arg0 := true if key Arg2 is in map Arg1. | {map,any} | boolean | `FATE_01` |
| `MAP_FROM_LIST` | Arg0 Arg1 | Arg0 := make a map from (key, value) list in Arg1. | {{list,{tuple,[any,any]}}} | map | `FATE_01` |
| `MAP_SIZE` | Arg0 Arg1 | Arg0 := The size of the map Arg1. | {map} | integer | `FATE_01` |
| `MAP_TO_LIST` | Arg0 Arg1 | Arg0 := The tuple list representation of the map Arg1. | {map} | list | `FATE_01` |
| `IS_NIL` | Arg0 Arg1 | Arg0 := true if Arg1 == []. | {list} | boolean | `FATE_01` |
| `CONS` | Arg0 Arg1 Arg2 | Arg0 := [Arg1|Arg2]. | {any,list} | list | `FATE_01` |
| `HD` | Arg0 Arg1 | Arg0 := head of list Arg1. | {list} | any | `FATE_01` |
| `TL` | Arg0 Arg1 | Arg0 := tail of list Arg1. | {list} | list | `FATE_01` |
| `LENGTH` | Arg0 Arg1 | Arg0 := length of list Arg1. | {list} | integer | `FATE_01` |
| `NIL` | Arg0 | Arg0 := []. | {} | list | `FATE_01` |
| `APPEND` | Arg0 Arg1 Arg2 | Arg0 := Arg1 ++ Arg2. | {list,list} | list | `FATE_01` |
| `STR_JOIN` | Arg0 Arg1 Arg2 | Arg0 := string Arg1 followed by string Arg2. | {string,string} | string | `FATE_01` |
| `INT_TO_STR` | Arg0 Arg1 | Arg0 := turn integer Arg1 into a string. | {integer} | string | `FATE_01` |
| `ADDR_TO_STR` | Arg0 Arg1 | Arg0 := turn address Arg1 into a string. | {address} | string | `FATE_01` |
| `STR_REVERSE` | Arg0 Arg1 | Arg0 := the reverse of string Arg1. | {string} | string | `FATE_01` |
| `STR_LENGTH` | Arg0 Arg1 | Arg0 := The length of the string Arg1. | {string} | integer | `FATE_01` |
| `BYTES_TO_INT` | Arg0 Arg1 | Arg0 := bytes_to_int(Arg1) | {bytes} | integer | `FATE_01` |
| `BYTES_TO_STR` | Arg0 Arg1 | Arg0 := bytes_to_str(Arg1) | {bytes} | string | `FATE_01` |
| `BYTES_CONCAT` | Arg0 Arg1 Arg2 | Arg0 := bytes_concat(Arg1, Arg2) | {bytes,bytes} | bytes | `FATE_01` |
| `BYTES_SPLIT` | Arg0 Arg1 Arg2 | Arg0 := bytes_split(Arg2, Arg1), where Arg2 is the length of the first chunk. | {bytes,integer} | bytes | `FATE_01` |
| `INT_TO_ADDR` | Arg0 Arg1 | Arg0 := turn integer Arg1 into an address. | {integer} | address | `FATE_01` |
| `VARIANT` | Arg0 Arg1 Arg2 Arg3 | Arg0 := create a variant of size Arg1 with the tag Arg2 (Arg2 < Arg1) and take Arg3 elements from the stack. | {integer,integer,integer} | variant | `FATE_01` |
| `VARIANT_TEST` | Arg0 Arg1 Arg2 | Arg0 := true if variant Arg1 has the tag Arg2. | {variant,integer} | boolean | `FATE_01` |
| `VARIANT_ELEMENT` | Arg0 Arg1 Arg2 | Arg0 := element number Arg2 from variant Arg1. | {variant,integer} | any | `FATE_01` |
| `BITS_NONEA` |  | push an empty bitmap on the stack. | {} | bits | `FATE_01` |
| `BITS_NONE` | Arg0 | Arg0 := empty bitmap. | {} | bits | `FATE_01` |
| `BITS_ALLA` |  | push a full bitmap on the stack. | {} | bits | `FATE_01` |
| `BITS_ALL` | Arg0 | Arg0 := full bitmap. | {} | bits | `FATE_01` |
| `BITS_ALL_N` | Arg0 Arg1 | Arg0 := bitmap with Arg1 bits set. | {integer} | bits | `FATE_01` |
| `BITS_SET` | Arg0 Arg1 Arg2 | Arg0 := set bit Arg2 of bitmap Arg1. | {bits,integer} | bits | `FATE_01` |
| `BITS_CLEAR` | Arg0 Arg1 Arg2 | Arg0 := clear bit Arg2 of bitmap Arg1. | {bits,integer} | bits | `FATE_01` |
| `BITS_TEST` | Arg0 Arg1 Arg2 | Arg0 := true if bit Arg2 of bitmap Arg1 is set. | {bits,integer} | boolean | `FATE_01` |
| `BITS_SUM` | Arg0 Arg1 | Arg0 := sum of set bits in bitmap Arg1. Exception if infinit bitmap. | {bits} | integer | `FATE_01` |
| `BITS_OR` | Arg0 Arg1 Arg2 | Arg0 := Arg1 v Arg2. | {bits,bits} | bits | `FATE_01` |
| `BITS_AND` | Arg0 Arg1 Arg2 | Arg0 := Arg1 ^ Arg2. | {bits,bits} | bits | `FATE_01` |
| `BITS_DIFF` | Arg0 Arg1 Arg2 | Arg0 := Arg1 - Arg2. | {bits,bits} | bits | `FATE_01` |
| `BALANCE` | Arg0 | Arg0 := The current contract balance. | {} | integer | `FATE_01` |
| `ORIGIN` | Arg0 | Arg0 := Address of contract called by the call transaction. | {} | address | `FATE_01` |
| `CALLER` | Arg0 | Arg0 := The address that signed the call transaction. | {} | address | `FATE_01` |
| `BLOCKHASH` | Arg0 Arg1 | Arg0 := The blockhash at height. | {integer} | variant | `FATE_01` |
| `BENEFICIARY` | Arg0 | Arg0 := The address of the current beneficiary. | {} | address | `FATE_01` |
| `TIMESTAMP` | Arg0 | Arg0 := The current timestamp. Unrelaiable, don't use for anything. | {} | integer | `FATE_01` |
| `GENERATION` | Arg0 | Arg0 := The block height of the cureent generation. | {} | integer | `FATE_01` |
| `MICROBLOCK` | Arg0 | Arg0 := The current micro block number. | {} | integer | `FATE_01` |
| `DIFFICULTY` | Arg0 | Arg0 := The current difficulty. | {} | integer | `FATE_01` |
| `GASLIMIT` | Arg0 | Arg0 := The current gaslimit. | {} | integer | `FATE_01` |
| `GAS` | Arg0 | Arg0 := The amount of gas left. | {} | integer | `FATE_01` |
| `ADDRESS` | Arg0 | Arg0 := The current contract address. | {} | address | `FATE_01` |
| `GASPRICE` | Arg0 | Arg0 := The current gas price. | {} | integer | `FATE_01` |
| `LOG0` | Arg0 | Create a log message in the call object. | {string} | none | `FATE_01` |
| `LOG1` | Arg0 Arg1 | Create a log message with one topic in the call object. | {integer,string} | none | `FATE_01` |
| `LOG2` | Arg0 Arg1 Arg2 | Create a log message with two topics in the call object. | {integer,integer,string} | none | `FATE_01` |
| `LOG3` | Arg0 Arg1 Arg2 Arg3 | Create a log message with three topics in the call object. | {integer,integer,integer,string} | none | `FATE_01` |
| `LOG4` | Arg0 Arg1 Arg2 Arg3 Arg4 | Create a log message with four topics in the call object. | {integer,integer,integer,integer,string} | none | `FATE_01` |
| `SPEND` | Arg0 Arg1 | Transfer Arg1 coins to account Arg0. (If the contract account has at least that many coins. | {address,integer} | none | `FATE_01` |
| `ORACLE_REGISTER` | Arg0 Arg1 Arg2 Arg3 Arg4 Arg5 Arg6 | Arg0 := New oracle with address Arg2, query fee Arg3, TTL Arg4, query type Arg5 and response type Arg6. Arg0 contains delegation signature. | {signature,address,integer,variant,typerep,typerep} | oracle | `FATE_01` |
| `ORACLE_QUERY` | Arg0 Arg1 Arg2 Arg3 Arg4 Arg5 Arg6 Arg7 | Arg0 := New oracle query for oracle Arg1, question in Arg2, query fee in Arg3, query TTL in Arg4, response TTL in Arg5. Typereps for checking oracle type is in Arg6 and Arg7. | {oracle,any,integer,variant,variant,typerep,typerep} | oracle_query | `FATE_01` |
| `ORACLE_RESPOND` | Arg0 Arg1 Arg2 Arg3 Arg4 Arg5 | Respond as oracle Arg1 to query in Arg2 with response Arg3. Arg0 contains delegation signature. Typereps for checking oracle type is in Arg4 and Arg5. | {signature,oracle,oracle_query,any,typerep,typerep} | none | `FATE_01` |
| `ORACLE_EXTEND` | Arg0 Arg1 Arg2 | Extend oracle in Arg1 with TTL in Arg2. Arg0 contains delegation signature. | {signature,oracle,variant} | none | `FATE_01` |
| `ORACLE_GET_ANSWER` | Arg0 Arg1 Arg2 Arg3 Arg4 | Arg0 := option variant with answer (if any) from oracle query in Arg1 given by oracle Arg0. Typereps for checking oracle type is in Arg3 and Arg4. | {oracle,oracle_query,typerep,typerep} | any | `FATE_01` |
| `ORACLE_GET_QUESTION` | Arg0 Arg1 Arg2 Arg3 Arg4 | Arg0 := question in oracle query Arg2 given to oracle Arg1. Typereps for checking oracle type is in Arg3 and Arg4. | {oracle,oracle_query,typerep,typerep} | any | `FATE_01` |
| `ORACLE_QUERY_FEE` | Arg0 Arg1 | Arg0 := query fee for oracle Arg1 | {oracle} | integer | `FATE_01` |
| `AENS_RESOLVE` | Arg0 Arg1 Arg2 Arg3 | Resolve name in Arg0 with tag Arg1. Arg2 describes the type parameter of the resolved name. | {string,string,typerep} | variant | `FATE_01` |
| `AENS_PRECLAIM` | Arg0 Arg1 Arg2 | Preclaim the hash in Arg2 for address in Arg1. Arg0 contains delegation signature. | {signature,address,hash} | none | `FATE_01` |
| `AENS_CLAIM` | Arg0 Arg1 Arg2 Arg3 Arg4 | Attempt to claim the name in Arg2 for address in Arg1 at a price in Arg4. Arg3 contains the salt used to hash the preclaim. Arg0 contains delegation signature. | {signature,address,string,integer,integer} | none | `FATE_01` |
| `AENS_UPDATE` | Arg0 Arg1 Arg2 Arg3 Arg4 Arg5 | Updates name in Arg2 for address in Arg1. Arg3 contains optional ttl (of type Chain.ttl), Arg4 contains optional client_ttl (of type int), Arg5 contains optional pointers (of type map(string, pointee)) | {signature,address,string,variant,variant,variant} | none | `FATE_01` |
| `AENS_TRANSFER` | Arg0 Arg1 Arg2 Arg3 | Transfer ownership of name Arg3 from account Arg1 to Arg2. Arg0 contains delegation signature. | {signature,address,address,string} | none | `FATE_01` |
| `AENS_REVOKE` | Arg0 Arg1 Arg2 | Revoke the name in Arg2 from owner Arg1. Arg0 contains delegation signature. | {signature,address,string} | none | `FATE_01` |
| `BALANCE_OTHER` | Arg0 Arg1 | Arg0 := The balance of address Arg1. | {address} | integer | `FATE_01` |
| `VERIFY_SIG` | Arg0 Arg1 Arg2 Arg3 | Arg0 := verify_sig(Hash, PubKey, Signature) | {bytes,address,bytes} | boolean | `FATE_01` |
| `VERIFY_SIG_SECP256K1` | Arg0 Arg1 Arg2 Arg3 | Arg0 := verify_sig_secp256k1(Hash, PubKey, Signature) | {bytes,bytes,bytes} | boolean | `FATE_01` |
| `CONTRACT_TO_ADDRESS` | Arg0 Arg1 | Arg0 := Arg1 - A no-op type conversion | {contract} | address | `FATE_01` |
| `AUTH_TX_HASH` | Arg0 | If in GA authentication context return Some(TxHash) otherwise None. | {} | variant | `FATE_01` |
| `ORACLE_CHECK` | Arg0 Arg1 Arg2 Arg3 | Arg0 := is Arg1 an oracle with the given query (Arg2) and response (Arg3) types | {oracle,typerep,typerep} | bool | `FATE_01` |
| `ORACLE_CHECK_QUERY` | Arg0 Arg1 Arg2 Arg3 Arg4 | Arg0 := is Arg2 a query for the oracle Arg1 with the given types (Arg3, Arg4) | {oracle,oracle_query,typerep,typerep} | bool | `FATE_01` |
| `IS_ORACLE` | Arg0 Arg1 | Arg0 := is Arg1 an oracle | {address} | bool | `FATE_01` |
| `IS_CONTRACT` | Arg0 Arg1 | Arg0 := is Arg1 a contract | {address} | bool | `FATE_01` |
| `IS_PAYABLE` | Arg0 Arg1 | Arg0 := is Arg1 a payable address | {address} | bool | `FATE_01` |
| `CREATOR` | Arg0 | Arg0 := contract creator | {} | address | `FATE_01` |
| `ECVERIFY_SECP256K1` | Arg0 Arg1 Arg2 Arg3 | Arg0 := ecverify_secp256k1(Hash, Addr, Signature) | {bytes,bytes,bytes} | bytes | `FATE_01` |
| `ECRECOVER_SECP256K1` | Arg0 Arg1 Arg2 | Arg0 := ecrecover_secp256k1(Hash, Signature) | {bytes,bytes} | bytes | `FATE_01` |
| `ADDRESS_TO_CONTRACT` | Arg0 Arg1 | Arg0 := Arg1 - A no-op type conversion | {address} | contract | `FATE_01` |
| `BLS12_381_G1_NEG` | Arg0 Arg1 | Arg0 := BLS12_381.g1_neg(Arg1) - Negate a G1-value | {tuple} | tuple | `FATE_02` |
| `BLS12_381_G1_NORM` | Arg0 Arg1 | Arg0 := BLS12_381.g1_normalize(Arg1) - Normalize a G1-value | {tuple} | tuple | `FATE_02` |
| `BLS12_381_G1_VALID` | Arg0 Arg1 | Arg0 := BLS12_381.g1_valid(Arg1) - Check if G1-value is a valid group member | {tuple} | bool | `FATE_02` |
| `BLS12_381_G1_IS_ZERO` | Arg0 Arg1 | Arg0 := BLS12_381.g1_is_zero(Arg1) - Check if G1-value is zero | {tuple} | bool | `FATE_02` |
| `BLS12_381_G1_ADD` | Arg0 Arg1 Arg2 | Arg0 := BLS12_381.g1_add(Arg1, Arg2) - Add two G1-values | {tuple,tuple} | tuple | `FATE_02` |
| `BLS12_381_G1_MUL` | Arg0 Arg1 Arg2 | Arg0 := BLS12_381.g1_mul(Arg1, Arg2) - Scalar multiplication for a G1-value (Arg1), and an Fr-value | {tuple,tuple} | tuple | `FATE_02` |
| `BLS12_381_G2_NEG` | Arg0 Arg1 | Arg0 := BLS12_381.g2_neg(Arg1) - Negate a G2-value | {tuple} | tuple | `FATE_02` |
| `BLS12_381_G2_NORM` | Arg0 Arg1 | Arg0 := BLS12_381.g2_normalize(Arg1) - Normalize a G2-value | {tuple} | tuple | `FATE_02` |
| `BLS12_381_G2_VALID` | Arg0 Arg1 | Arg0 := BLS12_381.g2_valid(Arg1) - Check if G2-value is a valid group member | {tuple} | bool | `FATE_02` |
| `BLS12_381_G2_IS_ZERO` | Arg0 Arg1 | Arg0 := BLS12_381.g2_is_zero(Arg1) - Check if G2-value is zero | {tuple} | bool | `FATE_02` |
| `BLS12_381_G2_ADD` | Arg0 Arg1 Arg2 | Arg0 := BLS12_381.g2_add(Arg1, Arg2) - Add two G2-values | {tuple,tuple} | tuple | `FATE_02` |
| `BLS12_381_G2_MUL` | Arg0 Arg1 Arg2 | Arg0 := BLS12_381.g2_mul(Arg1, Arg2) - Scalar multiplication for a G2-value (Arg2), and an Fr-value | {tuple,tuple} | tuple | `FATE_02` |
| `BLS12_381_GT_INV` | Arg0 Arg1 | Arg0 := BLS12_381.gt_inv(Arg1) - Invert a GT-value | {tuple} | tuple | `FATE_02` |
| `BLS12_381_GT_ADD` | Arg0 Arg1 Arg2 | Arg0 := BLS12_381.gt_add(Arg1, Arg2) - Add two GT-values | {tuple,tuple} | tuple | `FATE_02` |
| `BLS12_381_GT_MUL` | Arg0 Arg1 Arg2 | Arg0 := BLS12_381.gt_mul(Arg1, Arg2) - Multiply two GT-values | {tuple,tuple} | tuple | `FATE_02` |
| `BLS12_381_GT_POW` | Arg0 Arg1 Arg2 | Arg0 := BLS12_381.gt_pow(Arg1, Arg2) - Scalar exponentiation for a GT-value (Arg2), and an Fr-value | {tuple,tuple} | tuple | `FATE_02` |
| `BLS12_381_GT_IS_ONE` | Arg0 Arg1 | Arg0 := BLS12_381.gt_is_one(Arg1) - Check if a GT value is "one" | {tuple} | bool | `FATE_02` |
| `BLS12_381_PAIRING` | Arg0 Arg1 Arg2 | Arg0 := BLS12_381.pairing(Arg1, Arg2) - Find the pairing of a G1-value (Arg1) and a G2-value (Arg2) | {tuple,tuple} | tuple | `FATE_02` |
| `BLS12_381_MILLER_LOOP` | Arg0 Arg1 Arg2 | Arg0 := BLS12_381.miller_loop(Arg1, Arg2) - Do the Miller-loop step of pairing for a G1-value (Arg1) and a G2-value (Arg2) | {tuple,tuple} | tuple | `FATE_02` |
| `BLS12_381_FINAL_EXP` | Arg0 Arg1 | Arg0 := BLS12_381.final_exp(Arg1) - Do the final exponentiation in pairing | {tuple} | tuple | `FATE_02` |
| `BLS12_381_INT_TO_FR` | Arg0 Arg1 | Arg0 := to_montgomery(Arg1) - Convert (Big)integer to Montgomery representation (32 bytes) | {tuple} | tuple | `FATE_02` |
| `BLS12_381_INT_TO_FP` | Arg0 Arg1 | Arg0 := to_montgomery(Arg1) - Convert (Big)integer to Montgomery representation (48 bytes) | {tuple} | tuple | `FATE_02` |
| `BLS12_381_FR_TO_INT` | Arg0 Arg1 | Arg0 := from_montgomery(Arg1) - Convert Montgomery representation (32 bytes) to integer | {tuple} | tuple | `FATE_02` |
| `BLS12_381_FP_TO_INT` | Arg0 Arg1 | Arg0 := from_montgomery(Arg1) - Convert Montgomery representation (48 bytes) to integer | {tuple} | tuple | `FATE_02` |
| `AENS_LOOKUP` | Arg0 Arg1 | Lookup the name of Arg0. Returns option(AENS.name) | {string} | variant | `FATE_02` |
| `ORACLE_EXPIRY` | Arg0 Arg1 | Arg0 := expiry block for oracle Arg1 | {oracle} | int | `FATE_02` |
| `AUTH_TX` | Arg0 | If in GA authentication context return Some(Tx) otherwise None. | {} | variant | `FATE_02` |
| `STR_TO_LIST` | Arg0 Arg1 | Arg0 := string converted to list of characters | {string} | list | `FATE_02` |
| `STR_FROM_LIST` | Arg0 Arg1 | Arg0 := string converted from list of characters | {list} | string | `FATE_02` |
| `STR_TO_UPPER` | Arg0 Arg1 | Arg0 := to_upper(string) | {string} | string | `FATE_02` |
| `STR_TO_LOWER` | Arg0 Arg1 | Arg0 := to_lower(string) | {string} | string | `FATE_02` |
| `CHAR_TO_INT` | Arg0 Arg1 | Arg0 := integer representation of UTF-8 character | {char} | int | `FATE_02` |
| `CHAR_FROM_INT` | Arg0 Arg1 | Arg0 := Some(UTF-8 character) from integer if valid, None if not valid. | {int} | variant | `FATE_02` |
| `CALL_PGR` | Arg0 Identifier Arg2 Arg3 Arg4 Arg5 Arg6 | Potentially protected remote call. Arg5 is protected flag, otherwise as CALL_GR. | {contract,string,typerep,typerep,integer,integer,bool} | variant | `FATE_02` |
| `CREATE` | Arg0 Arg1 Arg2 | Deploys a contract with a bytecode Arg1 and value Arg3. The `init` arguments should be placed on the stack and match the type in Arg2. Writes contract address to the top of the accumulator stack. If an account on the resulting address did exist before the call, the `payable` flag will be updated. | {contract_bytearray,typerep,integer} | contract | `FATE_02` |
| `CLONE` | Arg0 Arg1 Arg2 Arg3 | Clones the contract under Arg1 and deploys it with value of Arg3. The `init` arguments should be placed on the stack and match the type in Arg2. Writes contract (or `None` on fail when protected) to the top of the accumulator stack. Does not copy the existing contract's store – it will be initialized by a fresh call to the `init` function. If an account on the resulting address did exist before the call, the `payable` flag will be updated. | {contract,typerep,integer,bool} | any | `FATE_02` |
| `CLONE_G` | Arg0 Arg1 Arg2 Arg3 Arg4 | Like `CLONE` but additionally limits the gas of the `init` call by Arg3 | {contract,typerep,integer,integer,bool} | any | `FATE_02` |
| `BYTECODE_HASH` | Arg0 Arg1 | Arg0 := hash of the deserialized contract's bytecode under address given in Arg1 (or `None` on fail). Fails on AEVM contracts and contracts deployed before Iris. | {contract} | variant | `FATE_02` |
| `FEE` | Arg0 | Arg0 := The fee for the current call tx. | {} | integer | `FATE_02` |
| `ADDRESS_TO_BYTES` | Arg0 Arg1 | Arg0 := the fixed size byte representation of the address Arg1 | {address} | bytes | `FATE_03` |
| `POSEIDON` | Arg0 Arg1 Arg2 | Arg0 := the Poseidon hash of Arg1 and Arg2 - all integers in the BLS12-381 scalar field | {integer, integer} | integer | `FATE_03` |
| `MULMOD` | Arg0 Arg1 Arg2 Arg3 | Arg0 := (Arg1 * Arg2) mod Arg3 | {integer, integer, integer} | integer | `FATE_03` |
| `BAND` | Arg0 Arg1 Arg2 | Arg0 := Arg1 & Arg2 | {integer, integer} | integer | `FATE_03` |
| `BOR` | Arg0 Arg1 Arg2 | Arg0 := Arg1 | Arg2 | {integer, integer} | integer | `FATE_03` |
| `BXOR` | Arg0 Arg1 Arg2 | Arg0 := Arg1 ^ Arg2 | {integer, integer} | integer | `FATE_03` |
| `BNOT` | Arg0 Arg1 | Arg0 := ~Arg1 | {integer} | integer | `FATE_03` |
| `BSL` | Arg0 Arg1 Arg2 | Arg0 := Arg1 << Arg2 | {integer, integer} | integer | `FATE_03` |
| `BSR` | Arg0 Arg1 Arg2 | Arg0 := Arg1 >> Arg2 | {integer, integer} | integer | `FATE_03` |
| `BYTES_SPLIT_ANY` | Arg0 Arg1 Arg2 | Arg0 := bytes\_split\_any(Arg1, Arg2), where a positive Arg2 is the length of the first chunk, and a negative Arg2 is the length of the second chunk. Returns None if byte array is not long enough. | {bytes, integer} | variant | `FATE_03` |
| `BYTES_SIZE` | Arg0 Arg1 | Arg0 := bytes\_size(Arg1), returns the number of bytes in the byte array. | {bytes} | integer | `FATE_03` |
| `BYTES_TO_FIXED_SIZE` | Arg0 Arg1 Arg2 | Arg0 := bytes\_to\_fixe\_size(Arg1, Arg2), returns Some(Arg1') if byte\_size(Arg1) == Arg2, None otherwise. The type of Arg1' is bytes(Arg2) but the value is unchanged | {bytes, integer} | variant | `FATE_03` |
| `INT_TO_BYTES` | Arg0 Arg1 Arg2 | Arg0 := turn integer Arg1 into a byte array (big endian) length Arg2 (truncating if not fit). | {integer, integer} | bytes | `FATE_03` |
| `STR_TO_BYTES` | Arg0 Arg1 | Arg0 := turn string Arg1 into the corresponding byte array. | {string} | bytes | `FATE_03` |
| `DEACTIVATE` |  | Mark the current contract for deactivation. | {} | none | `FATE_01` |
| `ABORT` | Arg0 | Abort execution (dont use all gas) with error message in Arg0. | {string} | none | `FATE_01` |
| `EXIT` | Arg0 | Abort execution (use upp all gas) with error message in Arg0. | {string} | none | `FATE_01` |
| `NOP` |  | The no op. does nothing. | {} | none | `FATE_01` |

#### Opcodes, Flags and Gas

| Opcode | Name | Ends basic block | Allowed in auth | Allowed offchain | Gas cost |
| ------ | ---- | ---------------- | --------------- | ---------------- | -------- |
| 0x0 | `RETURN` | true | true | true | 10 |
| 0x1 | `RETURNR` | true | true | true | 10 |
| 0x2 | `CALL` | true | true | true | 10 |
| 0x3 | `CALL_R` | true | false | true | 100 |
| 0x4 | `CALL_T` | true | true | true | 10 |
| 0x5 | `CALL_GR` | true | false | true | 100 |
| 0x6 | `JUMP` | true | true | true | 10 |
| 0x7 | `JUMPIF` | true | true | true | 10 |
| 0x8 | `SWITCH_V2` | true | true | true | 10 |
| 0x9 | `SWITCH_V3` | true | true | true | 10 |
| 0xa | `SWITCH_VN` | true | true | true | 10 |
| 0xb | `CALL_VALUE` | false | true | true | 10 |
| 0xc | `PUSH` | false | true | true | 10 |
| 0xd | `DUPA` | false | true | true | 10 |
| 0xe | `DUP` | false | true | true | 10 |
| 0xf | `POP` | false | true | true | 10 |
| 0x10 | `INCA` | false | true | true | 10 |
| 0x11 | `INC` | false | true | true | 10 |
| 0x12 | `DECA` | false | true | true | 10 |
| 0x13 | `DEC` | false | true | true | 10 |
| 0x14 | `ADD` | false | true | true | 10 |
| 0x15 | `SUB` | false | true | true | 10 |
| 0x16 | `MUL` | false | true | true | 10 |
| 0x17 | `DIV` | false | true | true | 10 |
| 0x18 | `MOD` | false | true | true | 10 |
| 0x19 | `POW` | false | true | true | 10 |
| 0x1a | `STORE` | false | true | true | 10 |
| 0x1b | `SHA3` | false | true | true | 100 |
| 0x1c | `SHA256` | false | true | true | 100 |
| 0x1d | `BLAKE2B` | false | true | true | 100 |
| 0x1e | `LT` | false | true | true | 10 |
| 0x1f | `GT` | false | true | true | 10 |
| 0x20 | `EQ` | false | true | true | 10 |
| 0x21 | `ELT` | false | true | true | 10 |
| 0x22 | `EGT` | false | true | true | 10 |
| 0x23 | `NEQ` | false | true | true | 10 |
| 0x24 | `AND` | false | true | true | 10 |
| 0x25 | `OR` | false | true | true | 10 |
| 0x26 | `NOT` | false | true | true | 10 |
| 0x27 | `TUPLE` | false | true | true | 10 |
| 0x28 | `ELEMENT` | false | true | true | 10 |
| 0x29 | `SETELEMENT` | false | true | true | 10 |
| 0x2a | `MAP_EMPTY` | false | true | true | 10 |
| 0x2b | `MAP_LOOKUP` | false | true | true | 10 |
| 0x2c | `MAP_LOOKUPD` | false | true | true | 10 |
| 0x2d | `MAP_UPDATE` | false | true | true | 10 |
| 0x2e | `MAP_DELETE` | false | true | true | 10 |
| 0x2f | `MAP_MEMBER` | false | true | true | 10 |
| 0x30 | `MAP_FROM_LIST` | false | true | true | 10 |
| 0x31 | `MAP_SIZE` | false | true | true | 10 |
| 0x32 | `MAP_TO_LIST` | false | true | true | 10 |
| 0x33 | `IS_NIL` | false | true | true | 10 |
| 0x34 | `CONS` | false | true | true | 10 |
| 0x35 | `HD` | false | true | true | 10 |
| 0x36 | `TL` | false | true | true | 10 |
| 0x37 | `LENGTH` | false | true | true | 10 |
| 0x38 | `NIL` | false | true | true | 10 |
| 0x39 | `APPEND` | false | true | true | 10 |
| 0x3a | `STR_JOIN` | false | true | true | 10 |
| 0x3b | `INT_TO_STR` | false | true | true | 100 |
| 0x3c | `ADDR_TO_STR` | false | true | true | 100 |
| 0x3d | `STR_REVERSE` | false | true | true | 100 |
| 0x3e | `STR_LENGTH` | false | true | true | 10 |
| 0x3f | `BYTES_TO_INT` | false | true | true | 10 |
| 0x40 | `BYTES_TO_STR` | false | true | true | 100 |
| 0x41 | `BYTES_CONCAT` | false | true | true | 10 |
| 0x42 | `BYTES_SPLIT` | false | true | true | 10 |
| 0x43 | `INT_TO_ADDR` | false | true | true | 10 |
| 0x44 | `VARIANT` | false | true | true | 10 |
| 0x45 | `VARIANT_TEST` | false | true | true | 10 |
| 0x46 | `VARIANT_ELEMENT` | false | true | true | 10 |
| 0x47 | `BITS_NONEA` | false | true | true | 10 |
| 0x48 | `BITS_NONE` | false | true | true | 10 |
| 0x49 | `BITS_ALLA` | false | true | true | 10 |
| 0x4a | `BITS_ALL` | false | true | true | 10 |
| 0x4b | `BITS_ALL_N` | false | true | true | 10 |
| 0x4c | `BITS_SET` | false | true | true | 10 |
| 0x4d | `BITS_CLEAR` | false | true | true | 10 |
| 0x4e | `BITS_TEST` | false | true | true | 10 |
| 0x4f | `BITS_SUM` | false | true | true | 10 |
| 0x50 | `BITS_OR` | false | true | true | 10 |
| 0x51 | `BITS_AND` | false | true | true | 10 |
| 0x52 | `BITS_DIFF` | false | true | true | 10 |
| 0x53 | `BALANCE` | false | true | true | 10 |
| 0x54 | `ORIGIN` | false | true | true | 10 |
| 0x55 | `CALLER` | false | true | true | 10 |
| 0x56 | `BLOCKHASH` | false | true | true | 1000 (iris), 10 (lima) |
| 0x57 | `BENEFICIARY` | false | true | true | 10 |
| 0x58 | `TIMESTAMP` | false | true | true | 10 |
| 0x59 | `GENERATION` | false | true | true | 10 |
| 0x5a | `MICROBLOCK` | false | true | true | 10 |
| 0x5b | `DIFFICULTY` | false | true | true | 10 |
| 0x5c | `GASLIMIT` | false | true | true | 10 |
| 0x5d | `GAS` | false | true | true | 10 |
| 0x5e | `ADDRESS` | false | true | true | 10 |
| 0x5f | `GASPRICE` | false | true | true | 10 |
| 0x60 | `LOG0` | false | true | true | 1000 |
| 0x61 | `LOG1` | false | true | true | 1100 |
| 0x62 | `LOG2` | false | true | true | 1200 |
| 0x63 | `LOG3` | false | true | true | 1300 |
| 0x64 | `LOG4` | false | true | true | 1400 |
| 0x65 | `SPEND` | false | false | true | 5000 (iris), 100 (lima) |
| 0x66 | `ORACLE_REGISTER` | false | false | false | 10000 (iris), 100 (lima) |
| 0x67 | `ORACLE_QUERY` | false | false | false | 10000 (iris), 100 (lima) |
| 0x68 | `ORACLE_RESPOND` | false | false | false | 10000 (iris), 100 (lima) |
| 0x69 | `ORACLE_EXTEND` | false | false | false | 10000 (iris), 100 (lima) |
| 0x6a | `ORACLE_GET_ANSWER` | false | false | true | 2000 (iris), 100 (lima) |
| 0x6b | `ORACLE_GET_QUESTION` | false | false | true | 2000 (iris), 100 (lima) |
| 0x6c | `ORACLE_QUERY_FEE` | false | false | true | 2000 (iris), 100 (lima) |
| 0x6d | `AENS_RESOLVE` | false | false | true | 2000 (iris), 100 (lima) |
| 0x6e | `AENS_PRECLAIM` | false | false | false | 10000 (iris), 100 (lima) |
| 0x6f | `AENS_CLAIM` | false | false | false | 10000 (iris), 100 (lima) |
| 0x70 | `AENS_UPDATE` | false | false | false | 10000 (iris), 100 (lima) |
| 0x71 | `AENS_TRANSFER` | false | false | false | 10000 (iris), 100 (lima) |
| 0x72 | `AENS_REVOKE` | false | false | false | 10000 (iris), 100 (lima) |
| 0x73 | `BALANCE_OTHER` | false | true | true | 2000 (iris), 50 (lima) |
| 0x74 | `VERIFY_SIG` | false | true | true | 1300 |
| 0x75 | `VERIFY_SIG_SECP256K1` | false | true | true | 1300 |
| 0x76 | `CONTRACT_TO_ADDRESS` | false | true | true | 10 |
| 0x77 | `AUTH_TX_HASH` | false | true | true | 10 |
| 0x78 | `ORACLE_CHECK` | false | false | true | 100 |
| 0x79 | `ORACLE_CHECK_QUERY` | false | false | true | 100 |
| 0x7a | `IS_ORACLE` | false | false | true | 100 |
| 0x7b | `IS_CONTRACT` | false | false | true | 100 |
| 0x7c | `IS_PAYABLE` | false | false | true | 100 |
| 0x7d | `CREATOR` | false | true | true | 10 |
| 0x7e | `ECVERIFY_SECP256K1` | false | true | true | 1300 |
| 0x7f | `ECRECOVER_SECP256K1` | false | true | true | 1300 |
| 0x80 | `ADDRESS_TO_CONTRACT` | false | true | true | 10 |
| 0x81 | `BLS12_381_G1_NEG` | false | true | true | 100 |
| 0x82 | `BLS12_381_G1_NORM` | false | true | true | 100 |
| 0x83 | `BLS12_381_G1_VALID` | false | true | true | 2000 |
| 0x84 | `BLS12_381_G1_IS_ZERO` | false | true | true | 30 |
| 0x85 | `BLS12_381_G1_ADD` | false | true | true | 100 |
| 0x86 | `BLS12_381_G1_MUL` | false | true | true | 1000 |
| 0x87 | `BLS12_381_G2_NEG` | false | true | true | 100 |
| 0x88 | `BLS12_381_G2_NORM` | false | true | true | 100 |
| 0x89 | `BLS12_381_G2_VALID` | false | true | true | 2000 |
| 0x8a | `BLS12_381_G2_IS_ZERO` | false | true | true | 30 |
| 0x8b | `BLS12_381_G2_ADD` | false | true | true | 100 |
| 0x8c | `BLS12_381_G2_MUL` | false | true | true | 1000 |
| 0x8d | `BLS12_381_GT_INV` | false | true | true | 100 |
| 0x8e | `BLS12_381_GT_ADD` | false | true | true | 100 |
| 0x8f | `BLS12_381_GT_MUL` | false | true | true | 100 |
| 0x90 | `BLS12_381_GT_POW` | false | true | true | 2000 |
| 0x91 | `BLS12_381_GT_IS_ONE` | false | true | true | 30 |
| 0x92 | `BLS12_381_PAIRING` | false | true | true | 12000 |
| 0x93 | `BLS12_381_MILLER_LOOP` | false | true | true | 5000 |
| 0x94 | `BLS12_381_FINAL_EXP` | false | true | true | 7000 |
| 0x95 | `BLS12_381_INT_TO_FR` | false | true | true | 30 |
| 0x96 | `BLS12_381_INT_TO_FP` | false | true | true | 30 |
| 0x97 | `BLS12_381_FR_TO_INT` | false | true | true | 30 |
| 0x98 | `BLS12_381_FP_TO_INT` | false | true | true | 30 |
| 0x99 | `AENS_LOOKUP` | false | false | true | 2000 |
| 0x9a | `ORACLE_EXPIRY` | false | false | true | 2000 |
| 0x9b | `AUTH_TX` | false | true | true | 100 |
| 0x9c | `STR_TO_LIST` | false | true | true | 100 |
| 0x9d | `STR_FROM_LIST` | false | true | true | 100 |
| 0x9e | `STR_TO_UPPER` | false | true | true | 100 |
| 0x9f | `STR_TO_LOWER` | false | true | true | 100 |
| 0xa0 | `CHAR_TO_INT` | false | true | true | 10 |
| 0xa1 | `CHAR_FROM_INT` | false | true | true | 10 |
| 0xa2 | `CALL_PGR` | true | false | true | 100 |
| 0xa3 | `CREATE` | true | false | true | 10000 |
| 0xa4 | `CLONE` | true | false | true | 5000 |
| 0xa5 | `CLONE_G` | true | false | true | 5000 |
| 0xa6 | `BYTECODE_HASH` | false | true | true | 100 |
| 0xa7 | `FEE` | false | true | true | 10 |
| 0xa8 | `ADDRESS_TO_BYTES` | false | true | true | 10 |
| 0xa9 | `POSEIDON` | false | true | true | 6000 |
| 0xaa | `MULMOD` | false | true | true | 10 |
| 0xab | `BAND` | false | true | true | 10 |
| 0xac | `BOR` | false | true | true | 10 |
| 0xad | `BXOR` | false | true | true | 10 |
| 0xae | `BNOT` | false | true | true | 10 |
| 0xaf | `BSL` | false | true | true | 10 |
| 0xb0 | `BSR` | false | true | true | 10 |
| 0xb1 | `BYTES_SPLIT_ANY` | false | true | true | 10 |
| 0xb2 | `BYTES_SIZE` | false | true | true | 10 |
| 0xb3 | `BYTES_TO_FIXED_SIZE` | false | true | true | 10 |
| 0xb4 | `INT_TO_BYTES` | false | true | true | 10 |
| 0xb5 | `STR_TO_BYTES` | false | true | true | 10 |
| 0xfa | `DEACTIVATE` | false | true | true | 10 |
| 0xfb | `ABORT` | true | true | true | 10 |
| 0xfc | `EXIT` | true | true | true | 10 |
| 0xfd | `NOP` | false | true | true | 1 |

## Gas
Each instruction uses the base gas as described in the table above.
In addition to the instruction base cost (some) instructions also
cost gas in relation to the memory they use. The base cost for
memory is one gas per "cell" used. A cell is the memory word of
an underlying machine which is defined to be a 64-bit word.

Each use of a a cell is counted and for each 1024 cells used
the price is increased by 1. If a contract uses 1024 cells it
will cost 1024 gas, if it uses 1025 cells it will cost 1026 gas.
Using 2049 cells costs 3072 gas and so on.

When calculating the cell cost the total number of cells
used after the instruction is used to determine the price for all
new cells used by the instruction. So if you have used 1020 cells
and then one instruction uses 5 new cells, then the gas cost
for that instruction is 10 and not 6.

Each use of a stack slot (a push) costs gas in the same way and
is also counted towards the number of used cells. Each pop of
a stack slot does not cost gas and does not decrease the gas cost
either but it reduced the count of number of cells in use.

The instructions uses cells in the following way.

### ADD, SUB, MUL, DIV, MOD
After the operation is done the size of the absolute value of the
result is calculated, and one cell is used per 64 bits that has a 1 set.
Integers -18446744073709551615 to 18446744073709551615 uses 1 cell,
and integers -340282366920938463463374607431768211456 to -18446744073709551616
and 18446744073709551616 to 340282366920938463463374607431768211456
uses 2 cells, and so on.

### POW
The result of the pow instruction is computed recursively
and for each step in the recursion the words used are
calculated and the operation is aborted if all gas is used up.
Given the function words which calculates the number of cells in
an integer as described above (1 per 64 bits used).
The number of cells are calculated as follows.

```
pow(a, b)    := pow(a, b, 1)

pow(a, b, r) := r  when b = 0
pow(a, b, r) := cells += words(a) * 2, pow(a*a, b/2, r) when b rem 2 = 0
pow(a, b, r) := cells += words(r) + words(a) * 3, pow(a*a, b/2, r*a)
```

### TUPLE
For creating a tuple you have already payed gas for the elements when
you pushed them on the stack with other operations, then the new tuple
increase the cell count by the size of the tuple plus 2.

Note that creating the tuple pops the elements from the stack so the
cell count only increases by 2 by the make_tuple instruction, but
the gas cost is the cost for size+2 cells.

Note also that when calculating cell cost the total number of cells
used after the instruction is used to determine the price for all
new cells used by the instruction.

### SETELEMENT
The number of cells used is the tuple size + 2.

### MAP_EMPTY
The cell cost is 2.

### MAP_UPDATE
The cell cost is 2.

### MAP_FROM_LIST
The cell cost is 2 + length of the list.

### MAP_TO_LIST
The cell cost is 2 * length of the list.

### CONS
The cell cost is 2.

### APPEND
The cell cost is 2 * length of the first list.

### STR_JOIN
The cell cost is 1 cell per 8 bytes in the joined string + 1 cell.

### INT_TO_STR
The cell cost is 1 cell per 8 bytes in the produced string + 1 cell.

### ADDR_TO_STR
The cell cost is 1 cell per 8 bytes in the produced string + 1 cell.

### STR_REVERSE
The cell cost is 1 cell per 8 bytes in the produced string + 1 cell.

### INT_TO_ADDR
The cell cost is 1 cell per 8 bytes in the produced address + 1 cell.

### BITS_NONE, BITS_NONEA, BITS_ALL, BITS_ALLA
The cell cost is 1 cell.

### BITS_ALL_N
The cell cost is 1 for every 64 bits used.

### BITS_SET, BITS_CLEAR
The cell cost is 1 for every 64 bits used by the resulting bit field.

### BYTES_CONCAT
The cell cost is 1 cell per 8 bytes in the produced byte array.

### BYTES_TO_STR
The cell cost is 1 cell per 8 bytes in resulting string + 1 cell.

### BYTES_SPLIT
The number of cells used is the tuple size which is 2 + 2.

### AUTH_TX_HASH
If in auth context the number of cells used is 2 + 2, otherwise
the number of cells used is 1 + 2.

### VARIANT
The cell cost is two times the length of the list of arities plus one for
each element in the variant plus four.


# Appendix 1: FATE serialization
A more formal description of the serialization can be found in
the general [serialization document](../serializations.md).
Here we will try to describe the serialization more with words.

FATE code is serialized in three chunks:

1. Code: The code itself.
2. Symbols: An optional symbol table.
3. Annotations: Optional additional information.

Each chunk is an RLP encoding of a byte array that is
the serialization of the chunk. They all have to be there
in the serialization but they can be empty.
An empty code chunk is just the RPL encoding of the empty byte array,
i.e the byte 128.
Symbols and Annotations can be empty but they have to be there as
the RLP encoding of the RLP encoding of the empty map i.e. the bytes 130, 47, 0.

An empty FATE contract is encoded as the byte sequence 128, 130, 47, 0, 130, 47, 0.


# Notation

Some notes on notation and definition of terms used in this document.

## Bits

Bits are counted from the least significant bit, starting on 0. When
bits are written out they are written from the most significant bit to
the least significant bit.

Example the number 1 in a byte would be written in binary as:
```
00000001
```
And we would say that bit 0 is set to 1. All other bits 1 to 7 are set to 0.

## Word size

The word size of the machine is 8 bits (one byte) but each type and instruction
uses words of varying sizes, all multiples of bytes though.
