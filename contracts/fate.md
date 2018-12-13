# FATE
The Fast æternity Transaction Engine
ISA

Version 20181212

* 20181209 Initial Draft
* 20181210 Second Draft - New execution model.
* 20181211 Third Draft - Fleshing out description.
* 20181212 4th Draft - Data serialization schema.

WARNING: Work in progress, major parts are missing and nothing is settled yet.

## Idea

The high level machine (or the Fast æternity Transaction Engine) has
aeternity transactions as its basic operations and it operates
directly on the state tree of the aeternity chain. This is a new
paradigm in blockchain virtual machine specifications which makes it
possible to create type safe and efficient implementations of the
machine.

Every operation is typed and all values are typed (either by being
stored in a typed memory or by a tag). Any type violation results in
an exception and reverts all state changes. In version 1.0 there will
be no catch instruction.

In addition to normal machine instructions, such as ADD, the machine
also has support for constructing all the transactions available on
the æternity chain from native low level chain transaction
instructions.

The instruction memory is divided into functions and basic
blocks. Only basic blocks can be indexed and used as jump
destinations.

There are instructions to operate on the chain state tree in a safe and formalized way.

FATE is “functional” in the sense that “updates” of data structures,
such as tuples, lists or maps does not change the old values of the
structure, instead a new version is created. Unless specific
operations to write to the contract store are used.

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
Fate instruction set and serialization.

#### The chain

The chain “memory” contains information about the current block and
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

The local storage is a stack of key value storages. That is, a list of
maps. When reading a key, the machine first looks in the first map of
the list. If a key is found and the type is correct the value is
returned. If the type is incorrect an exception is thrown. If no value
is found in the first map, the machine will look in the next map in
the list and so on. If the key does not exist in any of the maps an
exception is thrown.

The key is a an integer (32 bit).

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
* Void [0]
* Integer (signed arbitrary precision integers) [I]
* Boolean (true | false) [B]
* Addresses (A pointer into the state tree) [A]
* Strings (utf8 encoded byte arrays) [S]
* Tuples [T]
* Lists: Cons cells (‘a) | Nil (Ʇ)  [L],[C],[Ʇ]
* Maps (‘a, ‘b),  (Key: ‘a -> Value: ‘b)  ‘a not a map [M]
* Variant Types, (Name, [  [Type] ])  [V]
* TypeRep [R]

These types can be used as argument and return types of functions and
also as the type of the elements in the contract store.

### Void

The type Void indicates the lack of any value.

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
*   and, or, not
*   conditional jumps

### Addresses

Values of the type Address are 32-bytes (256-bits) pointers to
entities on the chain (Accounts, Oracles, Contracts, etc)

Examples:
```
<<ak_2HNb8bivUoJTcaxD6VKDy2wPHvTuQgQRJ3dkF9RSyVFqBkMneC>>
```

### Strings

Strings are byte arrays od UTF-8 encoded unicode characters. (These
can be used as non-indexable arrays of bytes.)

Examples:
```
“Hello world”
  “eof”
```

### Tuples

Tuples have an arity indicating the number of elements in the
tuple. Each element in the tuple has a type. The 0-tuple is also
sometimes called unit.

Examples:
```
 {}                Type: unit
 {1, 2}            Type: Tuple(Integer, Integer)
 {“foo”, 42, true} Type: Tuple(String, Integer, Boolean)
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
all mappings in a map.  The key kan have any type except a map.  The
value kan have any type including a map.

Examples:
```
#{ (1, “foo”), (2, “bar”) }
```
Type: Map(Integer, String)
```
#{ (“Fruit prices”, #{ (“banana”, 42), (“apple”, 12)}),
   (“Stock prices”, #{(“Apple”, 142), (“Orange”, 112)}) }
```

### Variant Types

The variant type is a type consisting of a tag (index) where each tag
represents a series of values of specified types. For example you
could have the Option type which could be None or Some(Integer). The
value None would be indicated by tag 0. The value Some(42) would be
represented by tag 1 followed by the integer.

Examples:
```
  (0, [])
  (1, [42])
  (3, [42, “foo”, true])
```

Note that the list syntax here does not indicate a Fate list but a
series of values.

### TypeRep

A TypeRep is the representation of a type as a value.


## Operations

All operations are typed. An operand can be the accumulator, an
immediate, a name, a reference to a field in the state tree, or a
reference to the contract state. The operand must be of the right
type.

### Operands

Operand specifiers are
*  a - accumulator - 00
*  i - immediate - 01
*  m - memory/name - 10
*  s - state/name - 11

Operand specifiers for binary operations are stored in the byte
following the opcode.

| value: | arg3 | arg3 | arg2 | arg2 | arg1 | arg1 | dest | dest |
| bit:   |    7 |   6  |    5 |    4 |    3 |    2 |    1 |   0  |

Unused arguments should be set to 0.

E.g. an accumulator + immediate -> accumulator would have the bit
pattern 00 01 00 00.

### Arithmetic operations ([I] x [I] -> [I])
#### ADD
#### SUB
#### DIV
#### MUL
#### MOD
#### EXP
#### BAND
#### BOR
#### BNOT

### Logic operations ([B] x [B] -> [B])
#### AND
#### OR
#### NOT (unary)

### Comparison ([I] x [I] -> [B])
#### LT
#### GT
#### EQ
#### ISZERO


### Memory
#### MLOADI ([N] -> [I])
#### MLOADA ([N]-> [A])
#### MLOADB ([N]-> [B])
#### MLOADC ([N]-> [C])
#### MLOADM ([N]-> [M])
#### MLOADS ([N]-> [S])
#### MLOADT ([N]-> [T])

### Store
#### MSTORE[‘a]
#### SLOAD[‘a]
#### SSTORE[‘a]

### Control flow

#### JUMPDEST
#### JUMP
#### JUMPI
#### CALL
#### RETURN

### Events
### Hashing
#### Blake ([S] -> [A])

### Spend
#### Spend ([I,A] -> [B])
Send N tokens to account address. Returns true if successful.
#### Spend ([I,A] -> [I])
Send N tokens to account address. Returns the balance left if successful and throws an exception if not.

TODO:
Think about calls that take non-spendable tokens by default.
Oracle
register
query
respond
extend
get_answer
get_question
query_fee
Name
resolve
preclaim
claim
transfer
revoke

## Gas
## Exceptions

There could be a use for exception handling in remote calls, but
decided that this is rather easy to add in a later stage and can be
postponed.



## Execution model

F entry   {Hash, Code} or {Hash, Type, Flags, Code}

Base blocks are lists of lists of instructions.


### Notes
This is not part of the specification... just some work in progress.

#### Version management

Adding features to VM or changing VM will result in hard fork, because
people that did not update their software cannot handle new
contracts. Therefore, the only thing we can add in “roma” release are
additions to Sophia that are compiled to existing byte code
format. For example some string library. Later this string library can
work with build-in primops, such that compilation becomes easier and
byte code shorter.

#### Testing

We need test infrastructure that can compile contracts with different
compilers and check that hashes do not change accidentaly for
contracts compiled with old version, but new code. We also need
infrastructure for interoperability: calling old contract from new.

#### Backend for Development kit

Compiler and VM must offer support for a fancy web interface SDK. Such
         as debugger, good error messages, etc. Distribution as NPM packet.

#### MetaData

There is a request for more meta data in compiled code such that
contract API can be retrieved and such that one can send source code
to a server that can validate it and offer tab completion.


#### TOdos

* Contact aeps team to find responsible contact  (TA)
* Sophia stand alone (Robert)
* AEVM opcodes  -> repo  (Robert)
* AEVM /Sophia ABI code in separate library/cleanup
* Sophia server http interface (separate repo)
* Sophia contract interface (also called “ABI”) 45 min
* Trace / debug
* Side effects (Tx : contract)
* Non spendables (fun and contract)
* Events in Sophia (Roma)    (Hans)
* Test compatible versions
* Stateful, Pure recognized by Sophia compiler
* Recursive types in Sophia
* Sophia inheritance (compile time code organization)
* Polymorphism
* Standard Lib

* FATE spec (Erik)
** ABI
** Instruction set
** State
* Primops spec  (Tobias)
* VM
* Sophia backend -> FATE  (Ulf)
* Refactor Tx -> Primop
* Gas pricing
* State tree (cache / handling) + side effect checking
* Implement instruction set
* De-serialization
* New instruction hash (Blake)
* Hash on arbitrary VM objects
** String hash
** Phash

* Hard fork support
* VM version handling


# Appendix 1: Fate instruction set and serialization

Most instructions are encoded as one byte opcode (7-bits), one byte
operand specifiers and 0 to 3 variable size arguments.

The 7th bit (counting from 0) is used for future extensions beyond 127 instructions.

Encoding of types
Immediates in code (constants) are encoded by the instruction type and then depending on the type of the immediate as follows:
Integer:  Encoded with RLP where the first type bit is reused as a sign bit.
Boolean: One byte, false: 0, true: 1.
Addresses: 32 bytes
Byte arrays: RLP encoded.
Tuples: 1 byte length, [encoded types], [encoded elements]
Lists: encoded type, RLP encoded size, [encoded elements] (Size can be 0)
Maps: encoded key type, encoded value type, 1 byte size, [encoded key, encoded value] 
           Note: immediate maps are limited in size to 255 for larger map constants the compiler must create two or more maps and merge them. 

Byte encoded type descriptors:
Void: 0
Integer: 1
Boolean: 2
Address: 3
String: 4
Tuple: 5 + [types]
Nil: 6
List: 7 + type
Map: 8 + type + type   
Variant Type: 9 + RLP size + [RLP size +  [type]]
Empty map: 10


# Appendix 2: Fate ABI
The Fate ABI describes how Fate data are serialized to byte representations.
ABI Encoding
In the ABI (arguments to remote calls, remote return values, in the store and in oracles) data is serialized to bytes by a staged tag scheme describing the types of data:

```
small integer: sxxxxxx0 6 bit integer with sign bit
short string : xxxxxx01 (at least one x =/= 0) xxxxxx = byte array size + [bytes]
string       : 00000001 + RLP encoded array
tuple        : xxxx1011 + [encoded elements] when 0 < size(tuple) < 16
tuple        : 00001011 + 1 byte size + [encoded elements]
list         : xxxx0011 + typerep + [encoded elements],  0 < length < 16, xxxx = length
list         : 00000011 + typerep + encoded length + [encoded elements]
                    111  Set below
               xxxx0111 Free (16)
               00001111 Free
               10001111 Free
               01001111 Free
               11001111 Free
map          : 00101111 + RLP encoded size + typerep(A) + typerep(B) + [encoded key, encoded value]
variant type : 10101111 + RLP encoded size + [RLP encoded size + [typereps]]
integer      : 10101111 + RLP encoded integer
-integer     : 01101111 + RLP encoded integer
long list    : 00011111 + typerep + RLP encoded length + [Elements]
address      : 10011111 + [32 bytes]
""           : 01011111
#{}          : 11011111
{}/unit      : 00111111
nil          : 10111111
false        : 01111111
true         : 11111111
```

