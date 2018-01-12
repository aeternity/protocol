[back](./contracts.md)
## Contract Transactions

Contract transactions are of three types:
- Create
- Call
- Disable

A contract is also a normal account with a balance.


### Create Contract Transaction

Anyone can create a new contract by submitting a create contract transaction.

The transaction contains:
- The address of the contract owner (the one signing and paying for the transaction) 
- The byte code of the contract
- The VM to use
- A transaction fee
- Optionally: A initial call to the contract including name, args and gas. (Can be used to emulate init function of Ethereum/Solidity contracts)



```
{ owner           :: public_key()
, code            :: hex_bytes()
, vm_version      :: hex_byte()
, fee             :: amount()
, init            :: none() | { gas :: amount()
                              , call_data :: hex_bytes()
                              }
}
```

Where a hex byte is a string of two hex digits preceded with 0x,
and hex bytes is a string of a number of hex bytes preceded with 0x.

Call data is encoded depending on the ABI of the language of the contract.

The transaction has to be signed with the private key of the owner.

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
, contract        :: public_key()
, vm_version      :: hex_byte()
, gas             :: amount()
, call_data       :: hex_bytes()
, fee             :: amount()

}
```

The transaction has to be signed with the private key of the caller.

The call_data is encoded in accordans with the contract language ABI.
(See e.g. the Ring ABI.)