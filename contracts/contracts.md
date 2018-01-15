# Smart Contracts

## Overview and definitions

- A smart **Contract** is a program on the blockchain that lives in the **contract state tree** in a full node.
- A contract runs on a virtual machine.
- A contract is owned by an **contract owner**.
- The contract owner creates a contract through posting a **create contract transaction** on the chain.
- Alternatively an owener can attach a contract to an existing account through an **attach contract transaction**.
- The contract creation transaction register an account as a contract. (One account - one contract)
- No one will have the private key for accounts created with create contract.
- Any user can call an exported function in a contract by posting a  **contract call transaction** on the chain.
- Contract can be written in a high level language which is compiled to the VM byte code.

## [Contract life cycle examples](./contract_life_cycle.md)

There is no kill instruction in the Aeternity virtual machine, instead there is a deactivation instruction.
When a contract is disabled it can only be called from other contracts already created on the chain.
One can not create a new contract on the chain that calls a disabled contract neither directly nor indirectly.

A typically contract life cycle looks like this:
1. Contract A with a function f is created by owner O.
2. Anyone can call the function f in A (call A.f()) any number of times.
3. Another contract B that refers to A.f is created.
4. Contract A is deactivated by O.
5. No one can call A directly any more, and no new contract can refer to contracts A and B, but calls though B still goes to A.f.
6. Contract B is deactivated by its owner, and has no referring contracts, it is deallocated as is contract A. (removed form the contract state tree)

## [The AEVM](./aevm.md)

AEternity plan to support multiple virtual machines.
In order to make transition from Ethereum easy the first VM (AEVM) will be very similar to the EVM.
A field in the contract specifies which virtual machine to be used.
In the future we plan to provide at least one more virtual machine which addresses some of the
security issues with the EVM.

## [Ring: The first contract language](./ring.md)

Ring is a functional Ocaml like language which syntax most resembles that of Reason.

## [Contract state trees](./contract_state_tree.md)


## [Contract transactions](./contract_transactions.md)

## Technical aspects of Contract operations

### Contracts have a published API

The API defines the format that calls should have.

### Contracts are typed

There are 4 basic types (uint, address, string, bool), 4 composed
types (tuple, list, record, map), and 3 block chain specific types
(state, transactions and events).


