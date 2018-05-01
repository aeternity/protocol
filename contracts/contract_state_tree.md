[back](./contracts.md)
## Contract state tree

The contracts reside in a contract state tree that
is included in the root hash. The existence of a contract can be proven.
Interactions, i.e. calls and return values, are stored in their own
state tree for one block. The existance of the call in that block can be proven.

### Contract state tree objects

The contract state tree contains objects:
- The contract definition (code binary)
- The contract store (data binary)
- The contract log (data binary)
- Active flag (Boolean)
- List of refering contracts
- Deposit (amount)
- vm_version

See [Contract Serialization](../serializations.md#contract) for the serialization specification.

#### The contract definition

- Created by a contract create transaction.
- Deleted when an inactive contract has no more referers.

### Contract state tree update

### Pruning of contracts

## Calls state tree

The calls state tree contains all calls done in the block
and their return values.

See [Call Serialization](../serializations.md#call) for the serialization specification.

- Calls & Return data
```
      	CONTRACT_INTERACTION_TYPE,
      	CONTRACT_INTERACTION_VSN,
      	caller_address,
      	caller_nonce,
      	height,
      	contract_address,
      	gas_used,
      	return_value
```
