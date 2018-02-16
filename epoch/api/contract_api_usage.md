[back](./README.md)
# Contracts - intended usage

## Introduction
You interact with a Aeternity node through HTTP.
To learn more about contracts and contract life cycles see [the doc](/contracts/contracts.md).

The following assumes that the node exposes at address 127.0.0.1 the following ports:
* HTTP external API: 3013
* HTTP internal API: 3113

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

## On chain transactions

There are two contract transactions available.


### Contract Create
[/tx/contract/create doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostContractCreate)

### Contract Call
[/tx/contract/call doc](https://aeternity.github.io/epoch-api-docs/?config=https://raw.githubusercontent.com/aeternity/epoch/master/apps/aehttp/priv/swagger.json#/external/PostContractCall)
