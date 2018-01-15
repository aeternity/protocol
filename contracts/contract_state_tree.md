[back](./contracts.md)
## Contract state tree

The contracts and their interactions reside in a contract state tree that
is included in the root hash. The existence of a contract and the
existence of calls can be proven.

### Contract state tree objects

The contract state tree contains objects:
- The contract definition (code binary)
- The contract store (data binary)
- The contract log (data binary)
- Active flag (Boolean)
- List of refering contracts
- Calls & Return data
- Deposit (amount)
- vm_version

As well as normal account fields.

#### The contract definition

- Created by a contract create transaction.
- Deleted when an inactive contract has no more referers.


### Contract state tree update



### Pruning of contracts
