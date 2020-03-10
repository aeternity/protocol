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

The total gas of the operation is a sum of the base gas and the op gas.

| OpNo | Name                |          Value |             Arguments | Return value    | Base gas  | Op gas   |
| ---- | ------------------- | -------------- | --------------------- | --------------- | --------- | -------- |
|    1 | Spend               | `Amount : int` | `Recipient : address` | `Nil`           | 12000     |        0 |
|  100 | Oracle register     | (Unused.)      | `Acct : address, Sign : signature, QFee : int, TTL : Chain.ttl, QType : typerep, RType : typerep` | `Oracle : address` | 12000    | Proportional to oracle TTL argument `TTL` (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` and the byte size of the transaction representing this operation, specifically: `byte_size(OracleRegisterTx) * GasPerByte` |
|  101 | Oracle query        | `QFee : int`   | `Oracle : address, Query : 'a, QTTL : Chain.ttl, RTTL : Chain.ttl` | `Query : address` | 12000 | Proportional to oracle query TTL argument `QTTL` (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` and the byte size of the transaction representing this operation, specifically: `byte_size(OracleQueryTx) * GasPerByte` |
|  102 | Oracle respond      | (Unused.)      | `Oracle : address, Query : address, Sign : signature, R : 'b` | `()` | 12000 | Proportional to oracle response TTL argument `RTTL` in oracle query (as found in the oracle query in the state, and interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` and the byte size of the transaction representing this operation, specifically: `byte_size(OracleRespondTx) * GasPerByte` |
|  103 | Oracle extend       | (Unused.)      | `Oracle : address, Sign : signature, TTL : Chain.ttl` | `()` | 12000    | Proportional to oracle TTL argument `TTL` (interpreted as relative), specifically: `ceiling(32000 * RelativeTTL / floor(60 * 24 * 365 / key_block_interval))` |
|  104 | Oracle get answer   | (Unused.)      | `Oracle : address, Query : address` | `option('b)` | 12000    | 0 |
|  105 | Oracle get question | (Unused.)      | `Oracle : address, Query : address` | `'a` | 12000  | 0 |
|  106 | Oracle query fee    | (Unused.)      | `Oracle : address`    | `int`           | 12000     | 0        |
|  200 | Name resolve        | (Unused.)      | `Name : string, Key : string, Type : typerep` | `option(address)` | 12000 | 0 |
|  201 | Name preclaim       | (Unused.)      | `Account : address, Commitment : hash, Sign : signature` | `()` | 12000 | Proportional to the byte size of the transaction representing this operation, specifically: `byte_size(NamePreclaimTx) * GasPerByte` |
|  202 | Name claim          | (Unused.)      | `Account : address, Name : string, Salt : int, Sign : signature` | `()` | 12000 | Proportional to the byte size of the transaction representing this operation, specifically: `byte_size(NameClaimTx) * GasPerByte` |
|  203 | Name update         | (Unused.)      | TODO | TODO | TODO | TODO |
|  204 | Name transfer       | (Unused.)      | `From : address, To : address, Hash : hash, Sign : signature` | `()` | 12000 | 0 |
|  205 | Name revoke         | (Unused.)      | `Addr : address, Hash : hash, Sign : signature` | `()` | 12000 | 0 |

`GasPerByte` is 20.

Note that the gas cost indicated in the table above does not include the gas required for the call instruction to the primop.

Calling state changing prim-ops in oracles and names's trees in off-chain
environment results in an error with output data `not_allowed_off_chain`.

## Chain specific instructions

The COINBASE instruction return the beneficiary of the current generation
stored in the previous key block.
When executing a contract in a state channel off-chain, COINBASE will return
the beneficiary of the previous key block as seen by the participant executing
the contract. In a forced progress call the COINBASE will return the
current beneficiary.

The TIMESTAMP instruction returns the timestamp of the current micro block.
When executing a contract in a state channel off-chain TIMESTAMP will return
the timestamp of the last block as seen by the participant executing the
contract. In a forced progress call the TIMESTAMP will return the timestamp
of the current micro block.

The DIFFICULTY instruction returns the difficulty of the current
generation stored in the previous key block.
When executing a contract in a state channel off-chain DIFFICULTY will return
the difficulty of the current generation stored in the last key block as seen
by the participant executing the contract. In a forced progress call the
DIFFICULTY will return the difficulty of the current generation.

The BLOCKHASH instruction returns the hash of the key block at the specified height.
If the height is below genesis height the instruction returns 0.
If the height is higher than or equal to the current height the instruction returns 0.
If the height is lower than current height minus 256 the instruction returns 0.
When executing a contract in a state channel (either off-chain or in
a force progress) BLOCKHASH will return the hash of the key block at the
specified heigh as seen by the one executing the contract.
