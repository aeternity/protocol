[back](./contracts.md)
# Virtual Machines on the Æternity blockchain

A smart contract is associated with a virtual machine for the execution of that
contract. The Æternity blockchain supports the virtual machine AEVM - A version
of the Ethereum VM. The AEVM can also use different ABIs, and it is versioned to
ensure that runs on earlier version can still be run to validate the chain in
the presence of consensus breaking VM changes.

A Create Contract transaction and the contract state tree contains a
'vm_version' field and an 'abi_version' field. These fields describes the type
and version of the virtual machine to use for the contract and the type and
version of the application binary interface (ABI) of the contract. (Note that
the serialization packs the version into one integer.)

The current meaning of the VM field is:

| Value (hex) | Machine  | Description
| ----------- | -------- | -----------
|   00        | none     | NO_VM ("Used" in oracles)
|   01        | [AEVM_01](aevm.md)  | For Sophia contracts on the AEVM
|   02        | [AEVM_01](aevm.md)  | For Solidity contracts on the AEVM
|   03        | [AEVM_02](aevm.md)  | Improved AEVM for Sophia, Minerva release
|   04        | [AEVM_03](aevm.md)  | Improved AEVM for Sophia, Fortuna release
|   05-FFFF   |          | UNUSED

The current meaning of the ABI field is:

| Value (hex) | ABI         | Description
| ----------- | ----------- | -----------
|   00        | raw string  | No interpretation - used in oracles
|   01        | [Sophia_01](sophia.md#the-sophia_01-abi)   | For Sophia contracts on the AEVM
|   02        | [Solidity_01](solidity.md#the-solidity_01-abi) | For Solidity contracts on the AEVM
|   03-FFFF   |             | UNUSED

Which VM versions are accepted are different based on consensus protocol versions.

| Protocol version | Operation            | Accepted VM values | Accepted ABI values |
| ---------------- | ---------            | ------------------ | ------------------- |
| Roma             | contract call/create | `0x1`              | `0x1`
|                  | oracle register      | (Not applicable.)  | `0x0`, `0x1`
| Minerva          | contract call        | `0x1`, `0x3`       | `0x1`
|                  | contract create      | `0x3`              | `0x1`
|                  | oracle register      | (Not applicable.)  | `0x0`, `0x1`
| Fortuna          | contract call        | `0x1`, `0x3`, `0x4`| `0x1`
|                  | contract create      | `0x3`, `0x4`       | `0x1`
|                  | oracle register      | (Not applicable.)  | `0x0`, `0x1`

The number after the machine name designates the version of the machine.
In the future new versions of the machine can be implemented with new instructions,
contracts using these machines must use a new vm_version number corresponding
to the new machine version.

The ABI name correspond to the supported languages. All Ethereum VM languages
uses the same ABI (Solidity_1). The languages can in the future be extended
with new functionality and new ABIs reflected by the ABI version number.

For a description of each ABI see the corresponding language description:
[Sophia](sophia.md), [Solidity](solidity.md), [Varna](varna.md).

## The Æternity Ethereum Virtual Machine AEVM
See [The AEVM](./aevm.md).

## Consensus breaking changes between AEVM versions
### AEVM_01 -> AEVM_02
* Oracle query fee of unknown oracle
  * AEVM_01: Succeeded with bogus value
  * AEVM_02: Fails with exception
* New crypto/hash primitives
* New VM instructions (bit shift operations)

### AEVM_02 -> AEVM_03
* New primitive operations (`Auth.tx_hash`)
* New crypto primitives
