[back](./contracts.md)
## Contract Transactions

Contract transactions are of four types:
- Create
- Attach -- Not implemented yet.
- Call
- Disable -- To be decided.

A contract is also a normal account with a balance,
and the normal spend transaction can be applied to the account.

Before a contract is created or called, the miner subtracts from the
creator's/caller's account gas*gas_price (*10^-18) aeons.
The execution of the call will use a certain amount of gas up to
the maximum given: the unused portion of the gas is refunded to the caller's
account; the used portion of the gas is added to the miner's account.

Charges are debited to the account of the creator/caller before the contract is created/called.
This is in order to prevent a malicious user from attempting to craft a contract that spends the balances in such a way that, having already consumed computational effort in the execution of the contract, inhibits the miner from debiting the charges.

### Create Contract Transaction

Anyone can create a new contract by submitting a create contract transaction.

The transaction contains:
- The address of the contract owner (the one signing and paying for the transaction)
- Nonce of the owner/creator account.
- The byte code of the contract
- The VM/ABI to use
- A transaction fee
- A deposit (an even number, 0 is accepted).
- An amount (aeons to transfer to the account, 0 is accepted).
- Gas for the initial call
- Gas price for the call.
- Call data for the initial call (usually including a function name and args, interpreted by the contract).

See [Contract Create Transaction Serialization](../serializations.md#contract-create-transaction) for the serialization specification.

Call data is encoded depending on the ABI of the language of the contract.

The transaction has to be signed with the private key of the owner.

The special variable "caller" will be set to the same value as "owner"
for the initial call.

The contract address is created by hashing, using Blake2b (256 bits digest), the concatenation of:
* The address of the contract owner;
* The nonce encoded as unsigned, big endian byte array, with the minimum number of bytes.

```
 hash(owner, nonce)
```

Before the contract is created, the fee, the deposit and the amount will be
subtracted from the owner account.

The amount will be added to the contract account.

The fee will be added to the miner account.

The deposit will be "held by the contract" until it is deactivated.

The vm_version defines both the virtual machine used for the byte code of the contract
and the binary interface/calling convention used by the contract. The version codes are
listed in the VM description.

If the initial call fails (runs out of gas) the contract is not
created.  The owner loses the fee and the gas (to the miner) but the
amount and the deposit are returned to the owner.

The miner will add the new created contract address, the contract state
and the return data from the initial call to the state tree (if the
init succeeds).


### Attach Contract Transaction

Attach contract code to an existing account.
In this case owner == the account address and no new account will be created,
all other fields are as in create contract.


```
{ owner           :: public_key()
, nonce           :: pos_integer()
, code            :: bytes()
, vm_version      :: byte()
, fee             :: amount()
, deposit         :: amount()
, amount          :: amount()
, gas             :: amount()
, gas_price       :: amount()
, call_data       :: bytes()
}
```

The special variable "caller" will be set to the same value as "owner"
for the initial call.

The miner will add the return data and the state from the initial call
to the state tree.


### Contract call transaction

Anyone can call an existing contract (as long as it isn't disabled).

The transaction contains:
- The address of the caller (the one signing and paying for the transaction)
- The address of the contract
- An optional additional fee to the miner apart from gas.
- Optional amount to transfer to the account before execution (even if the execution fails).
- The amount of gas to use
- The calldata
- A transaction fee

See [Contract Call Transaction Serialization](../serializations.md#contract-call-transaction) for the serialization specification.

The transaction has to be signed with the private key of the caller.

The call_data is encoded in accordance with the contract language ABI.
(See e.g. the Sophia ABI.)

Before the contract is called, the fee and the amount will be subtracted from the caller account.

The amount will be added to the contract account.

The fee will be added to the miner account.

The miner will add the return data and the state of the call to the state
tree.
