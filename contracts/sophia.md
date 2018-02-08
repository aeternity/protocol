[back](./contracts.md)
## The Sophia Language
An AEternity BlockChain Language
The Sophia is a dialect of ReasonML ( https://reasonml.github.io/ ).

Sophia is customized for smart contracts, which can be published
to a blockchain (the AEternity BlockChain). Thus some
unnecessary features of Reason (and OCaml - since Reason is closely
related to OCaml) have been removed, and some blockchain specific
primitives, constructions and types have been added. This document
tries to summarize the changes and additions.

## Language Features
### Contracts

Sophia does not have modules. Instead sophia has static
contracts. Contracts are similar to classes in object oriented
languages and support local state and inheritance. More specifically:

- A contract implementation, or simply a contract, is the code for a
  smart contract and consists of a list of types and functions that
  may or may not have a definition. A contract where all types and
  functions are defined is called a concrete contract. Only concrete
  contracts can be instantiated. (Used in a create contract transaction.)

- A contract can be abstract where no types or functions have definitions. Example:

```ocaml
// An abstract contract
contract VotingType = {
  public stateful let vote : string => unit;
};
```

- A contract instance is an entity living on the block chain (or in a state channel). Each
instance is associated with a particular contract implementation (at
least from the view of high-level language; the low-level details of
how to store and check API information on the chain is still to be
worked out).
- A contract may define a type state encapsulating its local
  state. The state must be initialised when instantiating a
  contract. This is done by the init function which can take arbitrary
  arguments and is called on contract instance creation.
- Contracts have a public API, comprising the functions and types
  annotated with the public keyword. These can be used from outside
  the contract. Functions and types with no annotation (or internal)
  are part of the internal API and can be used by contracts inheriting
  (see below) the given contract. Functions and types annotated with
  private can only be used locally.
- Contracts can inherit one (or more?) other contract(s). In this case
  the public functions (and types) of the inherited contract are
  included in the public API and internal functions are included in
  the internal API of the current contract. The state of the contract
  contains the states of all inherited contracts as well as the local
  state. However, the state of an inherited contract cannot be
  accessed other than through internal functions defined by that
  contract.
- Open question: should we allow overriding defined functions? I would
  suggest no, but there might be compelling use cases that I'm
  missing.

### Mutable state

Sophia does not have arbitrary mutable state, but only a limited form of
state associated with each contract instance.

- Each contract defines a state type encapsulating its mutable state.
- The value of the state is accessible from inside the contract
  through an implicitly bound variable state.
- State updates are performed by calling a function put : state =>
  unit (possibly with a better name).
- Aside from the put function (and similar functions for transactions
  and events), the contract language is purely functional.
- Functions modifying the state need to be annotated with the stateful keyword.

To make it convenient to update parts of a deeply nested state Sophia
provides special syntax for map/record updates.  Open
question: we likely want to make it possible to have immutable state
(parameters). Keep separate from mutable state or annotate certain
fields as immutable?

### Types
Sophia has the following types:

| Type    | Description                     | Example
| ------- | ------------------------------- | -------:
| uint    | A 256 bit integer               | ```42```
| int     | A 256 bit 2-complement integer  | ```-1```
| address | A 256 bit number given as a hex | ```ff00```
| bool    | A Boolean                       | ```true```
| string  | An array of bytes               | ```“Foo”```
| list    | A homogeneous immutable singly linked list. | ```[1, 2, 3]```
| tuple   | An ordered heterogeneous array   | ```(42, “Foo”, true)```
| record  | An immutable key value store with fixed key names and typed values | ``` type balance = { owner: address, value: uint } ```
| map     | An immutable key value store with dynamic mapping of keys of one type to values of one type | ```type accounts = map(string, address)```
| state   | A record of blockstate key, value pairs  |
| transactions | An append only list of blockchain transactions |
| events   | An append only list of blockchain events (or log entries) |

#### Reason types not in Sophia
- Arrays
- Variants
- Refs
- Object

### Pattern matching
Pattern matching is probably outside the first iteration of Sophia, but
we definitely want it in the final language.

### Builtins
#### Events
Sophia has events which logs a structured message to the contract log in
the resulting blockchain transaction.

```
event(name: string, value: any)
```

#### Transactions
Sophia can generate blockchain transactions.
```
transaction(tx_type: transaction, argument: record )
```

#### State

A Sophia contract has a state. You must declare the state record type in
the contract. You can then update the state through mutable record
update.

```
type state = { mutable field: string
             , mutable value: uint};
let state = {field: “”, value : 0};
let store_value = (f: string, v: uint) => {
    state.field = f;
    state.value = v;
}
```
#### Contract primitives
```
creator() : () => address
```
The address (pubkey) of the entity signing for the contract creation transaction
```
caller() : () => address
```
The address of the entity currently calling the contract.
```
value() : () => uint
```
The amount of coins transferred to the contract when calling.
```
balance() : () => uint
```
The amount of coins currently in the contract account
```
contract_address() : () => address;
```
The address of the contract.

Block references
```
block_height() : () => uint;    /* Current block number */
block_timestamp() : () => uint; /* Block timestamp */
```


### Exception
There is one exception: abort (reason:string)

### JSX
Sophia does not support inline html syntax.

## The lifetime of a contract

# Killing a contract

There is no selfdestruct instruction in the aevm as in the Ethereum
Virtual Machine instead there is a disable transaction which the
creator of a contract can issue. When a contract is disabled no new
contract can call the old contract.

When a contract is posted to the chain all references to other
contracts are checked and a reference counter in each contract is
increased. You can only post a contract to the chain if all the
contracts referred to are enabled.

When a contract is disabled all other contracts it refer to get their
reference count decreased.

If a contract is disabled and its reference count is zero a miner can
choose to garbage collect the contract.

The reference count of a contract is handled as the account balance
and kept in the state tree of the miner and the merkle hash is
included in the state hash in each block just as with balances.

The transaction for creating a contract has an extra fee called
deposit which has to be an even number. The disable transaction is
free but the miner and the creator get half of the deposit fee each at
contract disable thus encouraging creators to disable their contracts
and miners to pick disable transactions.

## ABI

The calldata contains a tuple with function name and argument. E.g. ("main", (1,2,3))
The compiler will generate entry coad to
load the calldata to memory and then create a pattern matching switch on the function name
and call the function with the second element as the argument.
e.g.
```
 CALLDATALOAD
 MLOAD
```

```
 case Data of
  ("main", arg) : main(arg)

```
Data is laid out in memory as follows:

Data of types uint, address, and bool are encoded as a big endian 256-bit word (32 bytes).

Data of other types are encoded as a pointer to the position of their place in the calldata.

String arguments are encoded with a 32 byte length (number of bytes) and as few 256-bit words
as needed padded on the right with 0.

A list is a series of cons cells each cell two 256-bit words, where the first word is data
encoded in the same way as arguments and the second argument is either an address or
nil (encoded as a 256-bit word with all bits = 1).

A tuple of size N is encoded in the same way as N arguments (functions
arguments are in reality a tuple).

Records are encoded as tuples.

Maps are encoded as a list of tuples, (key, value). ***This is subject to change***

Return values are encoded in the same way as arguments.

The contract code start by getting the calldata):

```
PUSH1 0       ;; MLOAD Address 0
DUP           ;; Used for CALLDATACOPY address 0
CALLDATASIZE
CALLDATACOPY
MLOAD

```

The above could also be implemented as a search tree looking at one
byte at the time of the function hash if that produces smaller
code. The compiler could also choose to truncate the hash to the
shortest unique prefix and shift the incoming hash down. E.g if there
are only three functions in the contract and their hashes starts with
0xA, 0xB nd 0xC respectively.

(Given that the contract invocation checks that the function call is to a valid address/hash before calling AEVM.)

The shortest unique suffix could also be used, and the hash could be ANDed with the suffix length instead.

Then each exported function starts with an exported entry point where it executes
code to fetch the arguments to memory.


### Local function calls

A local function call pushes the return address then the arguments.
The callee pops the arguments and local variables then swaps the
return address and the return value on the stack and jumps to
the return value leaving only the return value on the stack.

Call id(x):

```
            PUSHx RetAddress
            DUP2              ; Get argument
            PUSHx CalleeAdr
            JUMP

:RetAddress JUMPDEST          ; SP(0) contains ret address.
```

Return:

```
            SWAP1            ; Swap retvalue with first arg (only one arg in this fun)
            POP              ; Drop the argument
            SWAP1            ; Swap retval and retaddress
            JUMP             ; return to the caller

```

