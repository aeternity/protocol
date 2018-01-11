[back](./contracts.md)
## The Ring Language
An AEternity BlockChain Language
The Ring is a dialect of ReasonML ( https://reasonml.github.io/ ).

Ring is customized for smart contracts, that has the potential of being published to a blockchain (the AEternity BlockChain). Thus some unnecessary features of Reason (and OCaml - since Reason is closely related to OCaml) has been removed, and some blockchain specific primitives, constructions and types have been added. This document tries to summarize the changes and additions.

## Language Features
### Contracts
Ring does not have modules. Instead ring has static contracts. Contracts are similar to classes in object oriented languages and support local state and inheritance. More specifically:
- A contract implementation, or simply a contract, is the code for a smart contract and consists of a list of types and functions that may or may not have a definition. A contract where all types and functions are defined is called a concrete contract. Only concrete contracts can be instantiated. Previously we had a notion of contract type, which is now replaced by fully abstract contracts where no types or functions have definitions. Example:

```ocaml
// An abstract contract
contract VotingType = {
  public stateful let vote : string => unit;
};
```
- A contract instance is an entity living on the block chain (or in a state channel). Each instance is associated with a particular contract implementation (at least from the view of high-level language; the low-level details of how to store and check API information on the chain is still to be worked out).
- A contract may define a type state encapsulating its local state. The state must be initialised when instantiating a contract. This is done by the init function which can take arbitrary arguments and is called on contract instance creation.
- Contracts have a public API, comprising the functions and types annotated with the public keyword. These can be used from outside the contract. Functions and types with no annotation (or internal) are part of the internal API and can be used by contracts inheriting (see below) the given contract. Functions and types annotated with private can only be used locally.
- Contracts can inherit one (or more?) other contract(s). In this case the public functions (and types) of the inherited contract are included in the public API and internal functions are included in the internal API of the current contract. The state of the contract contains the states of all inherited contracts as well as the local state. However, the state of an inherited contract cannot be accessed other than through internal functions defined by that contract.
- Open question: should we allow overriding defined functions? I would suggest no, but there might be compelling use cases that I'm missing.

### Mutable state
Ring does not have arbitrary mutable state, but only a limited form of state associated with each contract instance.

- Each contract defines a state type encapsulating its mutable state.
- The value of the state is accessible from inside the contract through an implicitly bound variable state.
- State updates are performed by calling a function put : state => unit (possibly with a better name).
- Aside from the put function (and similar functions for transactions and events), the contract language is purely functional.
- Functions modifying the state need to be annotated with the stateful keyword.

To make it convenient to update parts of a deeply nested state Ring provides special special syntax for map/record updates.
Open question: we likely want to make it possible to have immutable state (parameters). Keep separate from mutable state or annotate certain fields as immutable?

### Types
Ring has the following types:

| Type    | Description                     | Example
| ------- | ------------------------------- | -------:
| uint    | A 256 bit integer               | ```42```
| int     | A 256 bit 2-complement integer  | ```-1```
| address | A 256 bit number given as a hex | ```ff00```
| bool    | A boolean                       | ```true```
| string  | An array of bytes               | ```“Foo”```
| list    | A homogenous immutable singly linked list. | ```[1, 2, 3]```
| tuple   | An ordered heterogenous array   | ```(42, “Foo”, true)```
| record  | An immutable key value store with fixed key names and typed values | ``` type balance = { owner: address, value: uint } ```
| map     | An immutable key value store with dynamic maping of keys of one type to values of one type | ```type accounts = map(string, address)```
| state   | A record of blockstate key, value pairs  |
| transactions | An append only list of blockchain transactions |
| events   | An append only list of blockchain events (or log entries) |

#### Arrays
Ring might not have arrays… Ring might have Maps.

####  Variants
 Depending on how we write the compiler, if they are cheap to include some like to use variant types, while others might not want them.
####  Refs
 Ring has no refs.
####  Object
 Ring will not have objects. (only contracts) 

### Pattern matching
Pattern matching is probably outside the first iteration of Ring, but we definitely want it in the final language.

### Builtins
#### Events
Ring has events which logs a structured message to the contract log in the resulting blockchain transaction.
```
event(name: string, value: any)
```

#### Transactions
Ring can generate blockchain transactions.
```
transaction(tx_type: transaction, argument: record )
```

#### State
A Ring contract has a state. You must declare the state record type in the contract. You can then update the state through mutable record update.
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
Ring does not support inline html syntax.

## The lifetime of a contract
#Killing a contract

There is no selfdestruct instruction in the aevm as in the Etherium Virtual Machine instead there is a disable transaction which the creator of a contract can issue. When a contract is disabled no new contract can call the old contract.

When a contract is posted to the chain all references to other contracts are checked and a reference counter in each contract is increased. You can only post a contract to the chain if all the contracts referred to are enabled.

When a contract is disabled all other contracts it refer to get their reference count decreased.

If a contract is disabled and its reference count is zero a miner can choose to garbage collect the contract.

The reference count of a contract is handled as the account balance and kept in the state tree of the miner and the merkle hash is included in the state hash in each block just as with balances.

The transaction for creating a contract has an extra fee called deposit which has to be an even number. The disable transaction is free but the miner and the creator get half of the deposit fee each at contract disable thus encouraging creators to disable their contracts and miners to pick disable transactions.

## ABI

The Ring AEVM ABI is similar to that of the Solidity/EVM ABI but adapted to
the Ring types.

The first 32 bytes of the calldata is the Keccak (SHA-3) hash of the signature of
the function. The signature is defined as in the Solidity ABI,
i.e. the function name with the parenthesised list of parameter types.
Parameter types are split by a single comma.

The state is appended as an extra argument to the function according to the contracts state type.
(*** subject to change ***)


The arguments are encoded according to their types as follows:

Arguments of types uint, address, and bool are encoded as a big endian 256-bit word (32 bytes).

Arguments of other types are encoded as a pointer to the position of their place in the calldata
with (the number of arguments *  32) subtracted.

String arguments are encoded with a 32 byte length (number of bytes) and as few 256-bit words
as needed padded on the right with 0.

A list is a series of cons cells each cell two 256-bit words, where the first word is data
encoded in the same way as arguments and the second argument is either an address or
nil (encoded as a 256-bit word with all bits = 1).

A tuple of size N is encoded in the same way as N arguments (functions arguments are in reality a tuple).

Records are encoded as tuples.

Maps are encoded as a list of tuples, (key, value). ***This is subject to change***

The contract code start by getting the function "name" (hash):

```
PUSH1 0
CALLDATALOAD
```

Then for each function in the contract it executes

```
DUP1
PUSH32 'function hash'
EQ
JUMPI function address
```

Then each exported function starts with an exported entry point where it executes
code to fetch the arguments to memory

```
JUMPDEST
PUSH32 1 ; Skip the function name in the calldata
CALLDATALOAD
...
PUSH32 Arity ; Skip other arguments
CALLDATALOAD

; Fetch data to memory
PUSH1  0  ; Address 0 in mem
PUSH   Arity + 1 ; # words to skip and
DUP              ; Size = calldatasize - (arity+1)
CALLDATASIZE  
SWAP1
SUB         
CALLDATACOPY     ; copy from [arity+1..Size] to mem(0)

JUMPDEST         ; for local calls
                 ; code for function body
```
