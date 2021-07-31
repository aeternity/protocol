# Contracts - intended usage

## Introduction
You interact with a Aeternity node through HTTP.
To learn more about contracts and contract life cycles see [the doc](/contracts/contracts.md).

There are two basic types of API calls, off-chain operations and on-chain transactions.

For an up to date list of all HTTP API endpoints and their arguments see
[Aeternity node HTTP API](https://api-docs.aeternity.io)

## Sophia calldata creation

A number of functions described below create calldata for contract call or
contract create transactions ([code/encode-calldata](#encode-call-data),
[code/call](#call), [create/compute](#contract-create),
[call/compute](#contract-call)). These support two ways of specifying the
function and arguments to the call:
- **Unchecked (legacy)**: Function name (except for `create/compute`) and arguments
  as a Sophia constant tuple. No checks are made to ensure that the given
  arguments match what the contracts expects.
- **Checked**: An argument `call` containing Sophia source code for a contract
  snippet containing (at least) a prototype for the function to be called and a
  special function `__call()` whose body is a single call to this function. This
  contract is type checked and the given arguments are checked to be compatible
  with the type that the called contract expects.

  For example, to call a function `swap` that expects a record argument you can
  give the following `call`:
  ```
  contract CallExample =
    record pt = {x : int, y : int}
    function swap : pt => pt
    function __call() = swap({x = 3, y = 4})
  ```
  The call contract can contain more definitions than are needed to type check
  the call. In particular, it can be the complete source code of the contract
  to be called, with an added `__call` function.

## Off chain operations

An Aeternity node provides some utility functions to help you create contract transactions and test contracts.


### Contract Compile
TODO => http compiler & other tools

### Encode Call Data
TODO => http compiler & other tools

### Call
TODO stil relevant?

### Dry-run
[/debug/transactions/dry-run](https://api-docs.aeternity.io#/internal/DryRunTxs)

The arguments to the /debug/transactions/dry-run endpoint are:
* `txs` - a list of *unsigned* transactions to execute.
* `top` - an optional blockhash at which to do the dry-run (if not specified `top` hash will be used).
* `accounts` - a list of "extra" accounts to be used in the dry-run.

### Decode Call Data
TODO => http compiler & other tools

## On chain transactions

An Aeternity node provides some APIs to format contract transactions and an API for submitting a signed transaction.

There are two contract transactions available: create and call.

You:
* Format the contract transaction using the corresponding API;
* (As for any other transaction) sign offline (i.e. outside of the Aeternity node) the transaction according to consensus;
* (As for any other transaction) submit the transaction to the Aeternity node using [its API](https://api-docs.aeternity.io/#/external/PostTransaction).

In order to affect the state of the chain you have to submit the signed transaction to a mining node.

### Contract Create
[/debug/contracts/create](https://api-docs.aeternity.io#/internal/PostContractCreate)

### Contract Call
[/debug/contracts/call](https://api-docs.aeternity.io#/internal/PostContractCall)

## Reading chain data

### Contract Call Result
[/transactions/{hash}/info](https://api-docs.aeternity.io#/external/GetTransactionInfoByHash)

