# The Æternity Ethereum Virtual Machine (AEVM)

The AEVM is a version of the EVM: https://github.com/ethereum/yellowpaper

The AEVM can be emulated inside the Æternity node and no marshaling of
arguments, code and data is necessary.  This makes for fast upstart
and faster execution of most smaller contracts.

There are a few differences between the EVM and the AEVM.

The AEVM provides an number of primitive operations that can be
used to interact with the chain.

The SELFDESTRUCT instruction is not immediate, instead the contract is
set in a disabled state where neither new contracts nor call
transactions can call the contract directly. When all other contracts
referring to a disabled contract are fully disabled the contract is
disabled.

## Æternity primitive operations

Interaction with the first class objects of the Æternity chain (e.g.
oracles, names, and state channels) is done through calls to a
built-in contract at address 0.

The value in the call indicates the tokens that the primop can use from the contract account.
Unused tokens stay on the contract account.

The first argument in the call specifies which primop to call.
The following arguments are encoded as Sophia data.

| OpNo | Name                |          Value |             Arguments | Return value    |
| ---- | ------------------- | -------------- | --------------------- | --------------- |
|    1 | Spend               | `Amount : int` | `Recipient : address` | `Nil`           |
|  100 | Oracle register     | (Unused.)      | `Acct : address, Sign : signature, QFee : int, TTL : int, QType : typerep, RType : typerep` | `Oracle : address` |
|  101 | Oracle query        | `QFee : int`   | `Oracle : address, Query : 'a, QTTL : int, RTTL : int` | `query : address` |
|  102 | Oracle respond      | (Unused.)      | `Oracle : address, Query : address, Sign : signature, R : 'b` | `()` |
|  103 | Oracle extend       | (Unused.)      | `Oracle : address, Sign : signature, TTL : int` | `()` |
|  104 | Oracle get answer   | (Unused.)      | `Oracle : address, Query : address` | `option('b)` |
|  105 | Oracle get question | (Unused.)      | `Oracle : address, Query : address` | `'a` |
|  106 | Oracle query fee    | (Unused.)      | `Oracle : address`    | `int`           |

## Chain specific instructions

The COINBASE instruction retern the beneficiary of the previous block.
When executing a contract in a state chennel (either off-chain or in
a force progress) COINBASE will return 0.


