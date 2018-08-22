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

| OpNo | Name                |          Value |             Arguments | Return value    | Gas cost |
| ---- | ------------------- | -------------- | --------------------- | --------------- | -------- |
|    1 | Spend               | `Amount : int` | `Recipient : address` | `Nil`           | 0        |
|  100 | Oracle register     | (Unused.)      | `Acct : address, Sign : signature, QFee : int, TTL : Chain.ttl, QType : typerep, RType : typerep` | `Oracle : address` | Proportional to oracle TTL argument `TTL` (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` |
|  101 | Oracle query        | `QFee : int`   | `Oracle : address, Query : 'a, QTTL : Chain.ttl, RTTL : Chain.ttl` | `query : address` | Proportional to oracle query TTL argument `QTTL` (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` |
|  102 | Oracle respond      | (Unused.)      | `Oracle : address, Query : address, Sign : signature, R : 'b` | `()` | Proportional to oracle response TTL argument `RTTL` in oracle query (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` |
|  103 | Oracle extend       | (Unused.)      | `Oracle : address, Sign : signature, TTL : Chain.ttl` | `()` | Proportional to oracle TTL argument `TTL` (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` |
|  104 | Oracle get answer   | (Unused.)      | `Oracle : address, Query : address` | `option('b)` | 0 |
|  105 | Oracle get question | (Unused.)      | `Oracle : address, Query : address` | `'a` | 0     |
|  106 | Oracle query fee    | (Unused.)      | `Oracle : address`    | `int`           | 0        |

Note that the gas cost indicated in the table above does not include the gas required for the call instruction to the primop.

## Chain specific instructions

The COINBASE instruction return the beneficiary of the current generation
stored in the previous key block.
When executing a contract in a state channel (either off-chain or in
a force progress) COINBASE will return 0.

The TIMESTAMP instruction returns the timestamp of the current micro block.
When executing a contract in a state channel (either off-chain or in
a force progress) TIMESTAMP will return *TODO*.

The DIFFICULTY instruction returns the difficulty of the current
generation stored in the previous key block.
When executing a contract in a state channel (either off-chain or in
a force progress) DIFFICULTY will return 0.


