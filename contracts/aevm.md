# The Æternity Ethereum Virtual Machine (AEVM)

The AEVM is a version of the EVM: https://github.com/ethereum/yellowpaper

The AEVM is emulated inside the Ethereum node an no marshaling of
arguments, code and data is necessary.  This makes for fast upstart
and faster execution of most smaller contracts.

There are a few differences between the EVM and the AEVM.

The SELFDESTRUCT instruction is not immediate, instead the contract is
set in a disabled state where neither new contracts nor call
transactions can call the contract directly. When all other contracts
referring to a disabled contract are fully disabled the contract is
disabled.

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


