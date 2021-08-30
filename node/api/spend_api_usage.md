# Spending tokens - intended usage

The following assumes that the node exposes at address 127.0.0.1 the following ports:

* User API internal HTTP endpoint: 3113

## Send tokens to another account

In order to send tokens, you need to have tokens i.e. a positive (non-zero) balance.
You obtain tokens e.g. after having mined successfully a block or received tokens through a transaction.

In order to transfer tokens from an account (`sender_id`) to another account (`recipient_id`):

* prepare spend transaction as per [specification](../../serializations.md). In order to ease the initial integration, the æternity node provides [/debug/transactions/spend endpoint](https://api-docs.aeternity.io#/internal/PostSpend)):
``` bash
curl -X POST -H "Content-Type: application/json" -d '{"sender_id":"...", "recipient_id":"...", "amount":2, "fee":1, "ttl":1234, "payload":"any public message"}' http://127.0.0.1:3113/v2/debug/transactions/spend
{"tx":"..."}
```
* sign the prepared transaction (e.g. by using the SDK)
* post the signed transaction to the [/transactions endpoint](https://api-docs.aeternity.io#/external/PostTransaction)

Once the transaction is included in a block, the recipient shall receive the specified amount and the miner that specified fee. The `ttl` has to
reflect the current height of the chain, it specify at what height the transaction expire and can't be included on the chain.

## Notes on testing spending tokens

The simplest way for testing sending tokens is setting up a local network of two nodes - disconnected from the testnet.
The reason is that in order to spend tokens from your account you need to obtain tokens in the first place, and in order to obtain tokens you need to mine a block faster than all other miners in the network.
Testing spending tokens in a local network enables obtaining tokens without competing with other miners.

At least one of the two nodes needs to mine - in order to have tokens to spend.

At least one of the two nodes needs to be configured with the peer address of the other node in order for them to form a network.

### Running multiple nodes on same host

This is mainly purposed for development.

If you are using the release binaries (i.e. not the Docker image) and you want to run two nodes on the same host:
* Deploy the release binary in two different locations - one per node;
* For each node, before starting the node edit the user configuration file to specify distinct TCP ports;
* For each node, before starting the node change the node name of each node.

In order to change the node name of node #1, change directory (`cd`) to the directory where you deployed node #1 then run (change "2.0.0" in the command with the version of the release you deployed):
```bash
sed -ibkp 's/-sname aeternity/-sname aeternity1/g' releases/2.0.0/vm.args
```

In order to change the node name of node #2, change directory (`cd`) to the directory where you deployed node #2 then run (change "2.0.0" in the command with the version of the release you deployed):
```bash
sed -ibkp 's/-sname aeternity/-sname aeternity2/g' releases/2.0.0/vm.args
```
