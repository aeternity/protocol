[back](./README.md)
# Contracts - intended usage

## Introduction
You interact with a Aeternity node through HTTP.
To learn more about contracts and contract life cycles see [the doc](/contracts/contracts.md).

There are two basic types of API calls, off-chain operations and on-chain transactions.

For an up to date list of all HTTP API endpoints and their arguments see
[Epoch HTTP API](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json)

## Off chain operations

An epoch node provides some utility functions to help you create contract transactions.


### Contract Compile
[/debug/contracts/code/compile doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/CompileContract)

### Encode Call Data
[/debug/contracts/code/encode-calldata doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/EncodeCalldata)

### Call
[/debug/contracts/code/call doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/CallContract)

The arguments to the /debug/contracts/code/call endpoint are:
code -- either the byte code of the contract to call (if abi is either "sophia" or "evm") or an address of a contract on chain (if abi is "sophia-address").
function -- the name of the function in the contract to call (if abi is "sophia" or "sophia-address").
arg -- the argument to the call as Sophia constants (when abi is "sophia" or "sophia-address") or as an solidity encoded call-data (if abi is "evm").
abi -- one of "sophia", "sophia-address" or "evm".

### Decode Call Data
[/debug/contracts/code/decode-data doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/DecodeData)

## On chain transactions

An epoch node provides some APIs to format contract transactions and an API for submitting a signed transaction.

There are two contract transactions available: create and call.

You:
* Format the contract transaction using the corresponding API;
* (As for any other transaction) sign offline (i.e. outside of the epoch node) the transaction according to consensus;
* (As for any other transaction) submit the transaction to the epoch node using [its API](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostTransaction).

In order to affect the state of the chain you have to submit the signed transaction to a mining node.

### Contract Create
[/debug/contracts/create doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostContractCreate)

[/debug/contracts/create/compute doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostContractCreateCompute)

### Contract Call
[/debug/contracts/call doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostContractCall)

[/debug/contracts/call/compute doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/internal/PostContractCallCompute)

## Reading chain data

### Contract Call Result
[/transactions/{hash}/info doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/GetTransactionInfoByHash)

