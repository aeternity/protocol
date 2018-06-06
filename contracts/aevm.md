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
built in contract at address 0.

The first argument in the call specifies witch primop to call.
The following arguments are encoded as Sophia data.

| OpNo | Name                |             Arguments | Return value    |
| ---- | ------------------- | --------------------- | --------------- |
|    1 | Spend               | `Recipient : address` | `Nil`           |
|  100 | Oracle register     | `Acct : address , Sign : signature, QFee : int, TTL : int, QType : typerep, RType : typerep` | `Oracle : address` |
|  101 | Oracle query        | `Oracle : address, Query : ('a,'b) , QTTL : int, RTTL : int` | `query : oracle_query('a, 'b)` |
|  102 | Oracle respond      | `Oracle : address, Query : address , Sign : signature, R : 'a` | `()` |
|  103 | Oracle extend       | `Oracle : address, Sign : signature, Fee : integer, TTL : integer` | `()` |
|  104 | Oracle get answer   | `Oracle : address, Query : address`   | `option('b)` |
|  105 | Oracle get question | `Oracle : address, Query : address`   | `'a` |
|  106 | Oracle query fee    | `Oracle : address`    | `int`           |

## New instructions

[TODO: Describe these instructions.]

There is a PUSH N instruction.

AEVM also has some new instructions that will make it into the EVM at some point:

```
JUMPTO jump_target
JUMPIF jump_target
BEGINSUB n_args, n_results
JUMPSUB jump_target
RETURNSUB
SHL
SHR
SAR
ROL
```


## The Fast Æternity Virtual Machine FAEVM

The FAEVM is also version of the EVM: https://github.com/ethereum/yellowpaper and it follows the AEVM exactly.

The FAEVM compiles the contract code to native code on supported hardware. The code will then execute outside
of the Ethereum node and all code, data and arguments need to be marshaled to call the native code. This makes
for slower calls but faster execution for larger contracts.


