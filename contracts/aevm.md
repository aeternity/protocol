[back](./contracts.md)
# Virtual Machines on the AEternity blockchain

A smart contract is associated with a virtual machine for the execution of that
contract. The AEternity blockchain supports four virtual machines.

1. HLM - A high level machine for executing logical formulas and blockchain operations.
2. WTFVM - A Warded Typed Functional Virtual Machine
3. AEVM - A version of the Etherium VM
3. FAEVM - A fast version of the Etherium VM

# HLM

The High Level Machine can execute AEtherium block chain operations (transactions) and logical tests on
block chain variables in straight line code. A contract on HLM has a two local key->value stores,
one containing numbers and one containg strings.

HLM statements are of the form:
```
 IF BoolExpr THEN Statement ELSE Statement
 IF BoolExpr THEN Statement 
 TX(SpendTx, A, B, Amount)
 TX...
 put_number(StringExpr, Aexpr)
 put_string(StringExpr, StringExpr)

BoolExpr:
 true
 false
 if BoolExpr then BoolExpr else BoolExpr
 BoolExpr or BoolExpr
 BoolExpr and BoolExpr
 ( BoolExpr )
 StringExpr EQOP StringExpr
 AExpr COP AExpr

StringExpr:
 Oracle(ID)
 String
 get_string(StringExpr)

EQOP
 ==
 !=

AExpr:
 Number
 if BoolExpr then AExpr else AExpr
 balance(Account)
 contractbalance
 callvalue
 get_number(StringExpr)
 AExpr AOP AExpr
 ( AExpr )

AOP:
 +
 -
 div
 *

COP:
   >
   <
   >=
   <=
   EQOP
```

A HLM contract has a caller and an owner (creator).

TODO:
 * Describe in detail which transactions are in the language
 * Describe when a transactions is valid (Owner, Caller, balance etc)
 * Describe how Oracle results are decoded and compared
 * Describe how HLM contracts are encoded (bytecode)
 * Describe calling convention
 * Describe return values
 * Describe how the key value stores are encoded

# WTFVM

The Warded Typed Functional Virtual Machine is used to efficeintly and safely execute contracts written in the Sophia language.

The WTFVM machine is Warded. This means that all arithmetic operations are checked for overflow and underflow if applicable.
The machine has a signed arbitrary large number type so for most opertations there should be no overflow.

The WTFVM machine is typed. Every instruction and every instruction argument has a type. All aregument types are checked when
a contract is called. All data is tagged with the types.

The WTFVM machine is functional. The machine supports the execution of functional langugaes with tagged data,
automatic memory management and garbage collection.

The WTFVM is a virtual machine the instructions are on a higher level than pure memory references.

[TODO: Full description of the WTFVM]


## The Aeternity Virtual Machine AEVM

The AEVM is a version of the EVM: https://github.com/ethereum/yellowpaper

The AEVM is emulated inside the AEtherium node an no marshallling of arguments, code and data is necessary.
This makes for fast upstart and faster execution of most smaller contracts.

There are a few differences between the EVM and the AEVM.

The SELFDESTRUCT instruction is not immediate, instead the contract is set in a disabled state where neither
new contractracts nor call transactions can call the contract directly. When all other contracts reffering to
a disabled contract are fully disabled the contract is disabled.

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


## The Fast Aeternity Virtual Machine AEVM

The FAEVM is also version of the EVM: https://github.com/ethereum/yellowpaper and it follows the AEVM exactly.

The FAEVM compiles the contract code to native code on supported hardware. The code will then execute outside
of the AEtherium node and all code, data and arguments need to be marshalled to call the native code. This makes
for slower calls but faster execution for larger contracts.


