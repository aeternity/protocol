# Virtual machines on the æternity blockchain

A smart contract is associated with a virtual machine for the execution of that
contract. The æternity blockchain supports the virtual machine AEVM - A version
of the Ethereum VM. The AEVM can also use different ABIs, and it is versioned to
ensure that runs on earlier version can still be run to validate the chain in
the presence of consensus breaking VM changes.

A Create Contract transaction and the contract state tree contains a
'vm_version' field and an 'abi_version' field. These fields describes the type
and version of the virtual machine to use for the contract and the type and
version of the application binary interface (ABI) of the contract. (Note that
the serialization packs the version into one integer.)

The current meaning of the VM field is:

| Value (hex) | Machine            | Description                                    |
|-------------|--------------------|------------------------------------------------|
|          00 | none               | NO_VM ("Used" in oracles)                      |
|          01 | [AEVM_01](aevm.md) | For Sophia contracts on the AEVM               |
|          02 | [AEVM_01](aevm.md) | For Solidity contracts on the AEVM             |
|          03 | [AEVM_02](aevm.md) | Improved AEVM for Sophia, Minerva release      |
|          04 | [AEVM_03](aevm.md) | Improved AEVM for Sophia, Fortuna release      |
|          05 | [FATE_01](fate.md) | For Sophia contracts using FATE (Lima release) |
|          06 | [AEVM_04](aevm.md) | Improved AEVM for Sophia, Lima release         |
|          07 | [FATE_02](fate.md) | For Sophia contracts using FATE (Iris release) |
|     07-FFFF |                    | UNUSED                                         |

The current meaning of the ABI field is:

| Value (hex) | ABI                                            | Description                         |
|-------------|------------------------------------------------|-------------------------------------|
|          00 | raw string                                     | No interpretation - used in oracles |
|          01 | [Sophia_AEVM_01](aevm.md#the-sophia_aevm_01-abi) | For Sophia contracts on the AEVM    |
|          02 | [Solidity_01](solidity.md#the-solidity_01-abi) | For Solidity contracts on the AEVM  |
|          03 | [Sophia_FATE_01](fate.md)                      | For Sophia contracts using FATE     |
|     04-FFFF |                                                | UNUSED                              |

Which VM versions are accepted are different based on consensus protocol versions.

| Protocol version | Operation            | Accepted VM values                       | Accepted ABI values |
|------------------|----------------------|------------------------------------------|---------------------|
| Roma             | contract call/create | `0x1`                                    | `0x1`               |
|                  | oracle register      | (Not applicable.)                        | `0x0`, `0x1`        |
| Minerva          | contract call        | `0x1`, `0x3`                             | `0x1`               |
|                  | contract create      | `0x3`                                    | `0x1`               |
|                  | oracle register      | (Not applicable.)                        | `0x0`, `0x1`        |
| Fortuna          | contract call        | `0x1`, `0x3`, `0x4`                      | `0x1`               |
|                  | contract create      | `0x3`, `0x4`                             | `0x1`               |
|                  | oracle register      | (Not applicable.)                        | `0x0`, `0x1`        |
| Lima             | contract call        | `0x1`, `0x3`, `0x4`, `0x5`, `0x6`        | `0x1`, `0x3`        |
|                  | contract create      | `0x5`, `0x6`                             | `0x1`, `0x3`        |
|                  | oracle register      | (Not applicable.)                        | `0x0`, `0x1`, `0x3` |
| Iris             | contract call        | `0x1`, `0x3`, `0x4`, `0x5`, `0x6`, `0x7` | `0x1`, `0x3`        |
|                  | contract create      | `0x7`                                    | `0x3`               |
|                  | oracle register      | (Not applicable.)                        | `0x0`, `0x3`        |

The number after the machine name designates the version of the machine.
In the future new versions of the machine can be implemented with new instructions,
contracts using these machines must use a new vm_version number corresponding
to the new machine version.

The ABI name correspond to the supported languages. All Ethereum VM languages
uses the same ABI (Solidity_1). The languages can in the future be extended
with new functionality and new ABIs reflected by the ABI version number.

For a description of each ABI see the corresponding language description:
[Sophia](https://github.com/aeternity/aesophia),
[Solidity](solidity.md).

## The æternity Ethereum virtual machine AEVM
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

### AEVM_03 -> AEVM_04
* New crypto primitives
* Memory gas adjustments
* Updated arguments for AENS-functions
* Support for `payable`

## Consensus breaking changes between FATE versions
### FATE_01 -> FATE_02
* Added operations
  * Crypto pairing operations (BLS12-381)
  * String functions (`to_list`, `from_list`, etc)
  * `AENS.update`, `AENS.lookup`, `Oracle.expire`
* Bug fixes
* Gas model adjustments
