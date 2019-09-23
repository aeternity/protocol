# FATE
The Fast æternity Transaction Engine
ISA

Version 20190307

* 20181209 Initial Draft
* 20181210 Second Draft - New execution model.
* 20181211 Third Draft - Fleshing out description.
* 20181212 4th Draft - Data serialization schema.
* 20190306 5th Draft - Instructions.
* 20190307 6th Draft - New data serialization schema.

WARNING: Work in progress, major parts are missing and nothing is settled yet.

## Design 

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

FATE does have the ability to write the value of an operation back to the
same register or stack position as one of the arguments, in effect updating
the memory. Still, any other references to the structure before the operation
will have the same structure as before the operation.

### Objectives

#### Type safety

FATE solves a fundamental problem programmers run into when coding for Ethereum: integer overflow, weak type checking and poore data flow. FATE checks all aritmetic operations to keep the right meanining of it. Also you can't implicitly cast types (eg integers to booleans). 

In EVM contracts are not typed. When calling a function, EVM will try to find which function you wanted to use by looking at the data that you send into the code. In FATE, you have actual functions and the functions have types - function call has to match the function type.

FATE ultimately makes a safer coding platform for smart contracts.

#### Rich data types

FATE has more built in data types: like maps, lists.

#### Faster transactions, smaller code size

Having a higher level instructions makes the code deployed smaller and it reduces the blockchain size. Smaller code and smaller hashes also keeps a blockchain network from clogging up.

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
* Integer (signed arbitrary precision integers) [I]
* Boolean (true | false) [B]
* Addresses (A pointer into the state tree) [A]
* Strings (utf8 encoded byte arrays) [S]
* Tuples (), ('a), ('a, 'b, ...) [T]
* Lists: Cons cells (‘a) | Nil (Ʇ)  [L],[C],[Ʇ]
* Maps (‘a, ‘b),  (Key: ‘a -> Value: ‘b)  ‘a not a map [M]
* Variant Types, (| Size | Tag | Elements  |)  [V]
* Bits <Bits> or !<Bits>
* TypeRep [R]

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

Strings are byte arrays of UTF-8 encoded unicode characters. (These
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
all mappings in a map.  The key can have any type except a map.  The
value can have any type including a map.

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

The variant type is a type consisting of a size and a tag (index)
where each tag represents a series of values of specified types. For
example you could have the Option type which could be None or
Some(Integer). The size of the variant is 2 (there are two variants),
The value None would be indicated by tag 0. The value
Some(42) would be represented by tag 1 followed by the integer.

Examples:
```
  (| 2 | 0 | [] |)      ;; None
  (| 2 | 1 | (42) |)    ;; Some(42)

  (| 4 | 3 | (42, “foo”, true) |) ;; Three(42, "foo", true)
```

Note that the tuple syntax for the elements does not indicate a Fate
tuple but a series of values.

### TypeRep

A TypeRep is the representation of a type as a value.
A typerep is one of
* integer
* boolean
* {list, T}
* {tuple, Ts}
* address
* bits
* {map, K, V}
* string
* {variant, ListOfVariants}

where T, K and V are TypeReps, Ts is a list of typereps ([T1, T2, ... ]),
and ListOfVariants is a list ([]) of tuples of typereps
([{tuple, [Ts1]}, {tuple, [Ts2]} ... ]).

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
*  stack

*  a (accumulator == stack 0)


The specifiers are encoded as


| immediate | 11 |
| --------- | --- |
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

### Operations


| OpCode | Name | Args | Description |
| ---    | ---  | ---  |        ---  |
| 0x0 | 'RETURN' |  | Return from function call pop stack to arg0. The type of the retun value has to match the return type of the function. |
| 0x1 | 'RETURNR' | Arg0 | Return from function call copy Arg0 to arg0. The type of the retun value has to match the return type of the function. |
| 0x2 | 'CALL' | Identifier | Call given function with args on stack. The types of the arguments has to match the argument typs of the function. |
| 0x3 | 'CALL_R' | Arg0 Identifier | Remote call to given contract and function.  The types of the arguments has to match the argument typs of the function. |
| 0x4 | 'CALL_T' | Identifier | Tail call to given function. The types of the arguments has to match the argument typs of the function. And the return type of the called function has to match the type of the current function. |
| 0x5 | 'CALL_TR' | Arg0 Identifier | Remote tail call to given contract and function. The types of the arguments has to match the argument typs of the function. And the return type of the called function has to match the type of the current function. |
| 0x6 | 'JUMP' | Integer | Jump to a basic block. The basic block has to exist in the current function. |
| 0x7 | 'JUMPIF' | Arg0 Integer | Conditional jump to a basic block. If Arg0 then jump to Arg1. |
| 0x8 | 'SWITCH_V2' | Arg0 Integer Integer | Conditional jump to a basic block on variant tag. |
| 0x9 | 'SWITCH_V3' | Arg0 Integer Integer Integer | Conditional jump to a basic block on variant tag. |
| 0xa | 'SWITCH_VN' | Arg0 [Integers] | Conditional jump to a basic block on variant tag. |
| 0xb | 'PUSH' | Arg0 | Push argument to stack. |
| 0xc | 'DUPA' |  | push copy of accumulator on stack. |
| 0xd | 'DUP' | Arg0 | push Arg0 stack pos on top of stack. |
| 0xe | 'POP' | Arg0 | Arg0 := top of stack. |
| 0xf | 'STORE' | Arg0 Arg1 | Arg0 := Arg1. |
| 0x10 | 'INCA' |  | Increment accumulator. |
| 0x11 | 'INC' | Arg0 | Increment argument. |
| 0x12 | 'DECA' |  | Decrement accumulator. |
| 0x13 | 'DEC' | Arg0 | Decrement argument. |
| 0x14 | 'ADD' | Arg0 Arg1 Arg2 | Arg0 := Arg1 + Arg2. |
| 0x15 | 'SUB' | Arg0 Arg1 Arg2 | Arg0 := Arg1 - Arg2. |
| 0x16 | 'MUL' | Arg0 Arg1 Arg2 | Arg0 := Arg1 * Arg2. |
| 0x17 | 'DIV' | Arg0 Arg1 Arg2 | Arg0 := Arg1 / Arg2. |
| 0x18 | 'MOD' | Arg0 Arg1 Arg2 | Arg0 := Arg1 mod Arg2. |
| 0x19 | 'POW' | Arg0 Arg1 Arg2 | Arg0 := Arg1  ^ Arg2. |
| 0x20 | 'LT' | Arg0 Arg1 Arg2 | Arg0 := Arg1  < Arg2. |
| 0x21 | 'GT' | Arg0 Arg1 Arg2 | Arg0 := Arg1  > Arg2. |
| 0x22 | 'EQ' | Arg0 Arg1 Arg2 | Arg0 := Arg1  = Arg2. |
| 0x23 | 'ELT' | Arg0 Arg1 Arg2 | Arg0 := Arg1 =< Arg2. |
| 0x24 | 'EGT' | Arg0 Arg1 Arg2 | Arg0 := Arg1 >= Arg2. |
| 0x25 | 'NEQ' | Arg0 Arg1 Arg2 | Arg0 := Arg1 /= Arg2. |
| 0x26 | 'AND' | Arg0 Arg1 Arg2 | Arg0 := Arg1 and Arg2. |
| 0x27 | 'OR' | Arg0 Arg1 Arg2 | Arg0 := Arg1  or Arg2. |
| 0x28 | 'NOT' | Arg0 Arg1 | Arg0 := not Arg1. |
| 0x29 | 'TUPLE' | Integer | Create a tuple of size = Arg0. Elements on stack. |
| 0x2a | 'ELEMENT' | Type Arg1 Arg2 Arg3 | Arg1 := element(Arg2, Arg3). The element should be of type Arg1 |
| 0x2b | 'MAP_EMPTY' | Arg0 | Arg0 := #{}. |
| 0x2c | 'MAP_LOOKUP' | Arg0 Arg1 Arg2 | Arg0 := lookup key Arg2 in map Arg1. |
| 0x2d | 'MAP_LOOKUPD' | Arg0 Arg1 Arg2 Arg3 | Arg0 := lookup key Arg2 in map Arg1 if key exists in map otherwise Arg0 := Arg3. |
| 0x2e | 'MAP_UPDATE' | Arg0 Arg1 Arg2 Arg3 | Arg0 := update key Arg2 in map Arg1 with value Arg3. |
| 0x2f | 'MAP_DELETE' | Arg0 Arg1 Arg2 | Arg0 := delete key Arg2 from map Arg1. |
| 0x30 | 'MAP_MEMBER' | Arg0 Arg1 Arg2 | Arg0 := true if key Arg2 is in map Arg1. |
| 0x31 | 'MAP_FROM_LIST' | Arg0 Arg1 | Arg0 := make a map from (key, value) list in Arg1. |
| 0x32 | 'NIL' | Arg0 | Arg0 := []. |
| 0x33 | 'IS_NIL' | Arg0 Arg1 | Arg0 := true if Arg1 == []. |
| 0x34 | 'CONS' | Arg0 Arg1 Arg2 | Arg0 := [Arg1|Arg2]. |
| 0x35 | 'HD' | Arg0 Arg1 | Arg0 := head of list Arg1. |
| 0x36 | 'TL' | Arg0 Arg1 | Arg0 := tail of list Arg1. |
| 0x37 | 'LENGTH' | Arg0 Arg1 | Arg0 := length of list Arg1. |
| 0x38 | 'STR_EQ' | Arg0 Arg1 Arg2 | Arg0 := true iff the strings Arg1 and Arg2 are the same. |
| 0x39 | 'STR_JOIN' | Arg0 Arg1 Arg2 | Arg0 := string Arg1 followed by string Arg2. |
| 0x40 | 'INT_TO_STR' | Arg0 Arg1 | Arg0 := turn integer Arg1 into a string. |
| 0x41 | 'ADDR_TO_STR' | Arg0 Arg1 | Arg0 := turn address Arg1 into a string. |
| 0x42 | 'STR_REVERSE' | Arg0 Arg1 | Arg0 := the reverse of string Arg1. |
| 0x43 | 'INT_TO_ADDR' | Arg0 Arg1 | Arg0 := turn integer Arg1 into an address. |
| 0x44 | 'VARIANT' | Arg0 Arg1 Arg2 Arg3 | Arg0 := create a variant of size Arg1 with the tag Arg2 (Arg2 < Arg1) and take Arg3 elements from the stack. |
| 0x45 | 'VARIANT_TEST' | Arg0 Arg1 Arg2 | Arg0 := true if variant Arg1 has the tag Arg2. |
| 0x46 | 'VARIANT_ELEMENT' | Arg0 Arg1 Arg2 | Arg0 := element number Arg2 from variant Arg1. |
| 0x47 | 'BITS_NONEA' |  | accumulator := empty bitmap. |
| 0x48 | 'BITS_NONE' | Arg0 | Arg0 := empty bitmap. |
| 0x49 | 'BITS_ALLA' |  | accumulator := full bitmap. |
| 0x50 | 'BITS_ALL' | Arg0 | Arg0 := full bitmap. |
| 0x51 | 'BITS_ALL_N' | Arg0 Arg1 | Arg0 := bitmap with Arg1 bits set. |
| 0x52 | 'BITS_SET' | Arg0 Arg1 Arg2 | Arg0 := set bit Arg2 of bitmap Arg1. |
| 0x53 | 'BITS_CLEAR' | Arg0 Arg1 Arg2 | Arg0 := clear bit Arg2 of bitmap Arg1. |
| 0x54 | 'BITS_TEST' | Arg0 Arg1 Arg2 | Arg0 := true if bit Arg2 of bitmap Arg1 is set. |
| 0x55 | 'BITS_SUM' | Arg0 Arg1 | Arg0 := sum of set bits in bitmap Arg1. Exception if infinit bitmap. |
| 0x56 | 'BITS_OR' | Arg0 Arg1 Arg2 | Arg0 := Arg1 v Arg2. |
| 0x57 | 'BITS_AND' | Arg0 Arg1 Arg2 | Arg0 := Arg1 ^ Arg2. |
| 0x58 | 'BITS_DIFF' | Arg0 Arg1 Arg2 | Arg0 := Arg1 - Arg2. |
| 0x59 | 'ADDRESS' | Arg0 | Arg0 := The current contract address. |
| 0x5a | 'BALANCE' | Arg0 | Arg0 := The current contract address. |
| 0x5b | 'ORIGIN' | Arg0 | Arg0 := Address of contract called by the call transaction. |
| 0x5c | 'CALLER' | Arg0 | Arg0 := The address that signed the call transaction. |
| 0x5d | 'GASPRICE' | Arg0 | Arg0 := The current gas price. |
| 0x5e | 'BLOCKHASH' | Arg0 | Arg0 := The current blockhash. |
| 0x5f | 'BENEFICIARY' | Arg0 | Arg0 := The address of the current beneficiary. |
| 0x60 | 'TIMESTAMP' | Arg0 | Arg0 := The current timestamp. Unrelaiable, don't use for anything. |
| 0x61 | 'GENERATION' | Arg0 | Arg0 := The block height of the cureent generation. |
| 0x62 | 'MICROBLOCK' | Arg0 | Arg0 := The current micro block number. |
| 0x63 | 'DIFFICULTY' | Arg0 | Arg0 := The current difficulty. |
| 0x64 | 'GASLIMIT' | Arg0 | Arg0 := The current gaslimit. |
| 0x65 | 'GAS' | Arg0 | Arg0 := The amount of gas left. |
| 0x66 | 'LOG0' | Arg0 Arg1 | Create a log message in the call object. |
| 0x67 | 'LOG1' | Arg0 Arg1 Arg2 | Create a log message with one topic in the call object. |
| 0x68 | 'LOG2' | Arg0 Arg1 Arg2 Arg3 | Create a log message with two topics in the call object. |
| 0x69 | 'LOG3' | Arg0 Arg1 Arg2 Arg3 Arg4 | Create a log message with three topics in the call object. |
| 0x6a | 'LOG4' | Arg0 Arg1 Arg2 Arg3 Arg4 Arg5 | Create a log message with four topics in the call object. |
| 0x6b | 'DEACTIVATE' |  | Mark the current contract for deactivation. |
| 0x6c | 'SPEND' | Arg0 Arg1 | Transfer Arg0 tokens to account Arg1. (If the contract account has at least that many tokens. |
| 0x6d | 'ORACLE_REGISTER' | Arg0 Arg1 Arg2 Arg3 Arg4 Arg5 |  |
| 0x6e | 'ORACLE_QUERY' |  |  |
| 0x6f | 'ORACLE_RESPOND' |  |  |
| 0x70 | 'ORACLE_EXTEND' |  |  |
| 0x71 | 'ORACLE_GET_ANSWER' |  |  |
| 0x72 | 'ORACLE_GET_QUESTION' |  |  |
| 0x73 | 'ORACLE_QUERY_FEE' |  |  |
| 0x74 | 'AENS_RESOLVE' |  |  |
| 0x75 | 'AENS_PRECLAIM' |  |  |
| 0x76 | 'AENS_CLAIM' |  |  |
| 0x77 | 'AENS_UPDATE' |  |  |
| 0x78 | 'AENS_TRANSFER' |  |  |
| 0x79 | 'AENS_REVOKE' |  |  |
| 0x7a | 'ECVERIFY' |  |  |
| 0x7b | 'SHA3' |  |  |
| 0x7c | 'SHA256' |  |  |
| 0x7d | 'BLAKE2B' |  |  |
| 0xf9 | 'DUMMY7ARG' | Arg0 Arg1 Arg2 Arg3 Arg4 Arg5 Arg6 | Temporary dummy instruction to test 7 args. |
| 0xfa | 'DUMMY8ARG' | Arg0 Arg1 Arg2 Arg3 Arg4 Arg5 Arg6 Arg7 | Temporary dummy instruction to test 8 args. |
| 0xfb | 'ABORT' | Arg0 | Abort execution (dont use all gas) with error message in Arg0. |
| 0xfc | 'EXIT' | Arg0 | Abort execution (use upp all gas) with error message in Arg0. |
| 0xfd | 'NOP' |  | The no op. does nothing. |




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


Done:

* Sophia stand alone (Robert)
* AEVM opcodes  -> repo  (Robert)
* AEVM /Sophia ABI code in separate library/cleanup
* Sophia server http interface (separate repo)
* Sophia contract interface (also called “ABI”) 45 min
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
Integer: 0
Boolean: 1
List: 2 + type
Tuple: 3, size,  [types]
Address: 4
Bits: 5
Map: 6 + type + type
String: 7
Variant: 8 + size + [3, size, type]


# Appendix 2: Fate ABI

The Fate ABI describes how Fate data are serialized to byte representations.

## ABI Serializations

In the ABI (arguments to remote calls, remote return values, in the
store and in oracles) data is serialized to bytes by a staged tag
scheme describing the types of data.  When we say "RLP encoded
integer" below we mean an integer encoded as the smalles big endian byte array
then this byte array is RLP encoded.

```
integer      : sxxxxxx0 : 6 bit integer with sign bit when integer < 64
string       : xxxxxx01 | size | [bytes] : when 0 < size < 64
string       : 00000001 | RLP encoded byte array : when size >= 64
list         : 00000011 | RLP encoded (length - 16) | [encoded elements] : when length >= 16
list         : xxxx0011 | [encoded elements] : when 0 < length < 16, xxxx = length
             : xxxx0111 : FREE (For typedefs in future)
tuple        : 00001011 | RLP encoded (size - 16) | [encoded elements] : when size >= 16
tuple        : xxxx1011 | [encoded elements] : when 0 < size(tuple) < 16
map          : 00101111 | RLP encoded size | [encoded key, encoded value]
tuple        : 00111111 : when size(tuple) == 0
bits         : 01001111 | RLP encoded integer when bits are finate
string       : 01011111 : when size == 0
integer      : 01101111 | RLP encoded (integer - 64) when size >= 64 and integer >= 0
false        : 01111111
             : 10001111 : FREE (Possibly for bytecode in the future.)
address      : 10011111 | [32 bytes]
variant      : 10101111 | RLP encoded variant size field | encoded tag | encoded values
list         : 10111111 : when length == 0
bits         : 11001111 | RLP encoded integer : when bits are in infinite
map          : 11011111 : when size == 0
integer      : 11101111 | RLP encoded ((- integer) - 64)
true         : 11111111
```

# Notation

Some notes on notation and definition of terms used in this document.

## Bits

Bits are counted from the least significant bit, starting on 0. When
bits are written out they are written from the most significant bit to
the least significant bit.

Example the number 1 in a byte would be written in binary as:
```
0000001
```
And we would say that bit 0 is set to 1. All other bits 1 to 7 are set to 0.

## Word size

The word size of the machine is 8 bits (one byte) but each type and instruction
uses words of varying sizes, all multiples of bytes though.
