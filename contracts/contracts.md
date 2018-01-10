# Smart Contracts

## Overview and definitions

- A smart **Contract** is a program on the blockchain that lives in the **contract state tree** in a full node.
- The programs runs on a virtual machine. The contract specifies which virtual machine to be used.
  At first there will only be one virtual machine available the AEVM closly resembling the EVM.
- A contract is owned by an **contract owner**.
- The contract owner creates a contract through posting a **contract creation transaction** on the chain.
- The contract creation transaction register an account as a contract. (One account - one contract)
- Any user can call an exported function in a contract by posting a  **contract call transaction** on the chain.
- Contract can be written in a high level language which is compiled to the VM bytecode.

## [The AEVM](./aevm.md)

## [The first contract language Ring](./ring.md)

## [Contract life cycle examples](./contract_life_cycle.md)

## [Contract state trees](./contract_state_tree.md)

## [Contract transactions](./contract_transactions.md)

## Technical aspects of Contract operations

### Contracts have a published API

The API defines the format that calls should have.

### Contracts are typed


### A contract can be deactivated

There is no kill instruction in the Aetherium virutal machine, instead there is a deactivation instruction.
When a contract is disabled it can only be called from other contracts already created on the chain.
One can not create a new contract on the chain that calls a disabled contract neither directly or indirectly.
