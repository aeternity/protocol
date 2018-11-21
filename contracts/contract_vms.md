[back](./contracts.md)
# Virtual Machines on the Æternity blockchain

A smart contract is associated with a virtual machine for the execution of that
contract. The Æternity blockchain supports four virtual machines.

1. HLM - A high level machine for executing logical formulas and blockchain operations.
2. FTWVM - A Functional Typed Warded Virtual Machine
3. AEVM - A version of the Ethereum VM
3. FAEVM - A fast version of the Ethereum VM

A Create Contract transaction and the contract state tree contains a
'vm_version' field. This field both describes the type and version of the
virtual machine to use for the contract and the type and version
of the application binary interface (ABI) of the contract.

The current meaning of this field is:

| Value (hex) | Machine  | ABI         | Description
| ----------- | -------- | ----------- | -----------
|   00        |          |             | NO_VM (Used in oracles)
|   01        | [AEVM_01](aevm.md)  | [Sophia_01](sophia.md#the-sophia_01-abi)   | For Sophia contracts on the AEVM
|   02        | [AEVM_01](aevm.md)  | [Solidity_01](solidity.md#the-solidity_01-abi) | For Solidity contracts on the AEVM
|   03        | [FTWVM_01](contract_vms.md#ftwvm) | Sophia_02   | For Sophia contracts on the FTWVM
|   04        | [HLM_01](contract_vms.md#hlm)   | Varna_01    | For Varna contracts on the HLM
|   05        | [FAEVM_01](aevm.md#the-fast-%C3%86ternity-virtual-machine-faevm) | [Solidity_01](solidity.md#the-solidity_01-abi)| For fast execution of Solidity contracts
| 06-FF       |          |             | UNUSED

*NOTE:* Currently the only value accepted in ContractCreateTx, ContractCallTx, and ChannelForceProgressTx is `0x01`.

The machine names corresponds to the machines described below (HLM, FTWVM, AEVM).
The number after the machine name designates the version of the machine.
In the future new versions of the machine can be implemented with new instructions,
contracts using these machines must use a new vm_version number corresponding
to the new machine version.

The ABI name correspond to the supported languages. All Ethereum VM languages
uses the same ABI (Solidity_00). The languages can in the future be extended
with new functionality and new ABIs reflected by the ABI version number.

For a description of each ABI see the corresponding language description:
[Sophia](sophia.md), [Solidity](solidity.md), [Varna](varna.md).

# HLM

The High Level Machine can execute Ethereum block chain operations
(transactions) and logical tests on block chain variables in straight
line code. A contract on HLM has a two local key->value stores, one
containing numbers and one containing strings.

The cost for executing a HLM contract is directly proportional to the size of CODE+STORE.
That is the gas used is bytesize(CODE+STORE) before contract execution.

This allows for blindingly fast and cheap contracts with a known cost to be executed on the Æternity chain.

HLM statements are of the form:
```
 IF BoolExpr THEN Statement ELSE Statement
 IF BoolExpr THEN Statement
 TX(SpendTx, A, B, Amount)
 TX...
 put_number(StringExpr, Aexpr)
 put_string(StringExpr, StringExpr)

BoolExpr:
 true
 false
 if BoolExpr then BoolExpr else BoolExpr
 BoolExpr or BoolExpr
 BoolExpr and BoolExpr
 ( BoolExpr )
 StringExpr EQOP StringExpr
 AExpr COP AExpr

StringExpr:
 Oracle(ID)
 String
 get_string(StringExpr)

EQOP
 ==
 !=

AExpr:
 Number
 if BoolExpr then AExpr else AExpr
 balance(Account)
 contractbalance
 callvalue
 get_number(StringExpr)
 AExpr AOP AExpr
 ( AExpr )

AOP:
 +
 -
 div
 *

COP:
   >
   <
   >=
   <=
   EQOP
```

A HLM contract has a caller and an owner (creator).

TODO:
 * Describe in detail which transactions are in the language
 * Describe when a transactions is valid (Owner, Caller, balance etc)
 * Describe how Oracle results are decoded and compared
 * Describe how HLM contracts are encoded (bytecode)
 * Describe calling convention
 * Describe return values
 * Describe how the key value stores are encoded

# FTWVM

The Functional Typed Warded Virtual Machine is used to efficiently and safely execute contracts written in the Sophia language.

The FTWVM machine is Warded. This means that all arithmetic operations are checked for overflow and underflow if applicable.
The machine has a signed arbitrary large number type so for most operations there should be no overflow.

The FTWVM machine is typed. Every instruction and every instruction argument has a type. All argument types are checked when
a contract is called. All data is tagged with the types.

The FTWVM machine is functional. The machine supports the execution of functional languages with tagged data,
automatic memory management and garbage collection.

The FTWVM is a virtual machine the instructions are on a higher level than pure memory references.

[TODO: Full description of the FTWVM]

## The Æternity Ethereum Virtual Machine AEVM and the FAEVM
See [The AEVM](./aevm.md).
