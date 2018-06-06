[back](./README.md)
# Contracts - intended usage

## Introduction
You interact with a Aeternity node through HTTP.
To learn more about contracts and contract life cycles see [the doc](/contracts/contracts.md).

There are two basic types of API calls, off-chain operations and on-chain transactions.

In order to affect the state of the chain you have to submit a signed transaction
to a mining node.

For an up to date list of all HTTP API endpoints and their arguments see
[Epoch HTTP API](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json)

## Off chain operations

An epoch node provides some utility functions to help you create contract transactions.


### Contract Compile
[/contract/compile doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/CompileContract)



### Encode Call Data
[/contract/encode-calldata doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/EncodeCalldata)

### Call
[/contract/call doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/CallContract)

The arguments to the /contract/call endpoint are:
code -- either the byte code of the contract to call (if abi is either "sophia" or "evm") or an address of a contract on chain (if abi is "sophia-address").
function -- the name of the function in the contract to call (if abi is "sophia" or "sophia-address").
arg -- the argument to the call as Sophia constants (when abi is "sophia" or "sophia-address") or as an solidity encoded call-data (if abi is "evm").
abi -- one of "sophia", "sophia-address" or "evm".


## On chain transactions

There are two contract transactions available.


### Contract Create
[/tx/contract/create doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostContractCreate)

### Contract Call
[/tx/contract/call doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostContractCall)

## Reading chain data

### Contract Call Result
[tx/{tx_hash}/contract-call doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/GetContractCallFromTx)

