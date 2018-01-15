[back](./contracts.md)
## Contract Transactions

Contract transactions are of four types:
- Create
- Attach
- Call
- Disable -- To be decided.

A contract is also a normal account with a balance,
and the normal spend transaction can be applied to the account.


### Create Contract Transaction

Anyone can create a new contract by submitting a create contract transaction.

The transaction contains:
- The address of the contract owner (the one signing and paying for the transaction) 
- The byte code of the contract
- The VM to use
- A transaction fee
- Gas for the initial call
- Call data for the initial call (usually including a function name and args, interpreted by the contract).


```
{ owner           :: public_key()
, nonce           :: pos_integer()
, code            :: hex_bytes()
, vm_version      :: hex_byte()
, fee             :: amount()
, gas             :: amount()
, call_data       :: hex_bytes()
}
```

Where a hex byte is a string of two hex digits preceded with 0x,
and hex bytes is a string of a number of hex bytes preceded with 0x.

Call data is encoded depending on the ABI of the language of the contract.

The transaction has to be signed with the private key of the owner.

The miner will add the new created contract address, the contract state
and the return data from the initial call to the state tree.


### Attach Contract Transaction

Attach contract code to an existing accont.
In this case owner == the acount addrres and no new account will be created,
all other fields are as in create contract.


```
{ owner           :: public_key()
, nonce           :: pos_integer()
, code            :: hex_bytes()
, vm_version      :: hex_byte()
, fee             :: amount()
, gas             :: amount()
, call_data       :: hex_bytes()
}
```

The miner will add the return data and the state from the initial call
to the state tree.


### Contract call transaction

Anyone can call an existing contract (as long as it isn't disabled).

The transaction contains:
- The address of the caller (the one signing and paying for the transaction)
- The address of the contract
- The amount of gas to use
- The calldata
- A transaction fee

```
{ caller          :: public_key()
, nonce           :: pos_integer()
, contract        :: public_key()
, vm_version      :: hex_byte()
, gas             :: amount()
, call_data       :: hex_bytes()
, fee             :: amount()

}
```

The transaction has to be signed with the private key of the caller.

The call_data is encoded in accordance with the contract language ABI.
(See e.g. the Ring ABI.)

The miner will add the return data and the state of the call to the state
tree.
