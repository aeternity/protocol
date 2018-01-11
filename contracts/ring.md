[back](./contracts.md)
## The Ring Language
An AEternity BlockChain Language
The Ring is a dialect of ReasonML ( https://reasonml.github.io/ ).

Ring is customized for smart contracts, that has the potential of being published to a blockchain (the AEternity BlockChain). Thus some unnecessary features of Reason (and OCaml - since Reason is closely related to OCaml) has been removed, and some blockchain specific primitives, constructions and types have been added. This document tries to summarize the changes and additions.

## Language Features
### Contracts
Ring does not have modules. Instead ring has static contracts. Contracts are similar to classes in object oriented languages and support local state and inheritance. More specifically:
A contract implementation, or simply a contract, is the code for a smart contract and consists of a list of types and functions that may or may not have a definition. A contract where all types and functions are defined is called a concrete contract. Only concrete contracts can be instantiated. Previously we had a notion of contract type, which is now replaced by fully abstract contracts where no types or functions have definitions. Example:

```ocaml
// An abstract contract
contract VotingType = {
  public stateful let vote : string => unit;
};
```

A contract instance is an entity living on the block chain (or in a state channel). Each instance is associated with a particular contract implementation (at least from the view of high-level language; the low-level details of how to store and check API information on the chain is still to be worked out).

A contract may define a type state encapsulating its local state. The state must be initialised when instantiating a contract. This is done by the init function which can take arbitrary arguments and is called on contract instance creation.

Contracts have a public API, comprising the functions and types annotated with the public keyword. These can be used from outside the contract. Functions and types with no annotation (or internal) are part of the internal API and can be used by contracts inheriting (see below) the given contract. Functions and types annotated with private can only be used locally.

Contracts can inherit one (or more?) other contract(s). In this case the public functions (and types) of the inherited contract are included in the public API and internal functions are included in the internal API of the current contract. The state of the contract contains the states of all inherited contracts as well as the local state. However, the state of an inherited contract cannot be accessed other than through internal functions defined by that contract.

Open question: should we allow overriding defined functions? I would suggest no, but there might be compelling use cases that I'm missing.

### Mutable state
Ring does not have arbitrary mutable state, but only a limited form of state associated with each contract instance.

Each contract defines a state type encapsulating its mutable state.

The value of the state is accessible from inside the contract through an implicitly bound variable state.

State updates are performed by calling a function put : state => unit (possibly with a better name).

Aside from the put function (and similar functions for transactions and events), the contract language is purely functional.

Functions modifying the state need to be annotated with the stateful keyword.

To make it convenient to update parts of a deeply nested state Ring provides special special syntax for map/record updates.
Open question: we likely want to make it possible to have immutable state (parameters). Keep separate from mutable state or annotate certain fields as immutable?

### Types
Ring has the following types:

| Type    | Description                     | Example
| ------- | ------------------------------- | -------:
| uint    | A 256 bit number                | 42
| address | A 256 bit number given as a hex | ff00
| string  | An array of bytes               | “Foo”
| bool    | A boolean                       | true
| tuple   | An ordered heterogenous array   | (42, “Foo”, true)
| record  | An immutable key value store with fixed key names and typed values | ``` type balance = { owner: Address, value: UInt } ```
| list    | A homogenous immutable singly linked list. | [1, 2, 3]
| state   | A record of blockstate key, value pairs  |
| transaction | A blockchain transaction |
| Arrays  | Ring might not have arrays… Ring might have Maps. From looking at Solidity examples, maps (mapping from key to value) is a common idiom - this suggests we should try to support them. Reason has a (slightly clunky) Map library/API - perhaps we can do something on top of this?   |
| Variants | Depending on how we write the compiler, if they are cheap to include some like to use variant types, while others might not want them. |
| Refs    | Ring has no refs. |
| Object  | Ring will not have objects. (only contracts) |

### Pattern matching
Pattern matching is probably outside the first iteration of Ring, but we definitely want it in the final language. |

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
