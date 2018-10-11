[back](./contracts.md)
# The Solidity Language

Æternity supports the Solidity language bytecode and ABI.

For a full description of Solidity see [The Solidity Specification](https://solidity.readthedocs.io).


## The Solidity_01 ABI

Note that the Solidity_01 ABI specifies that the create contract initial call returns the actual
bytecode to be stored in the contract state tree to be used for future calls.

See [The Solidity Specification:ABI](https://solidity.readthedocs.io/en/develop/abi-spec.html)

### Storing the contract state

Contracts store the VM storage map containing 256 bit binaries for both keys and values in the MPT.
Undefined keys are treated as having the value 0 and keys bound to the value zero are stored as the empty binary, thus purging them from the tree.
