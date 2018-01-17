[back](./epoch_api.md)
# Spending tokens - intended usage

The following assumes that the node exposes at address 127.0.0.1 the following ports:
* HTTP internal API: 3113

## Send tokens to another account

In order to send tokens, you need to have tokens i.e. a positive (non-zero) balance.
You obtain tokens e.g. after having mined successfully a block or received tokens through a transaction.

You need to know the public key to send tokens to (are returned by the `/account/pub-key` HTTP API).

In order to instruct your node to sign and broadcast a transaction sending tokens to the public key of the other account (recipient - replace the public key in the command):
```bash
curl -X POST -H "Content-Type: application/json" -d '{"recipient_pubkey":"ak$3PzQvEjt1ytvFMwN9STYvkXYnm72yEqkPcvLL9mzbzZ6fdczSb6LKgQwKhRiVvxMhB1boCVQXR8YWUy4XJv1XE3rx2dBik", "amount":2, "fee":1}' http://127.0.0.1:3113/v2/spend-tx
```

Once the transaction is included in a block, the recipient shall receive the specified amount and the miner that specified fee.

## Notes on testing spending tokens

The simplest way for testing sending tokens is setting up a local network of two nodes - disconnected from the testnet.
The reason is that in order to spend tokens from your account you need to obtain tokens in the first place, and in order to obtain tokens you need to mine a block faster than all other miners in the network.
Testing spending tokens in a local network enables obtaining tokens without competing with other miners.

At least one of the two nodes needs to mine - in order to have tokens to spend.

At least one of the two nodes needs to be configured with the peer address of the other node in order for them to form a network.

### Running multiple nodes on same host

Unless you are using Docker, in order to run two nodes on the same host you need to change the node name of each node.
For each node, after having deployed it - and before starting it - you need to change directory (`cd`) to the directory where you deployed the node, then for node 1 run:
```bash
sed -ibkp 's/-sname epoch/-sname epoch1/g' releases/0.5.0/vm.args
```
... while for node 2:
```bash
sed -ibkp 's/-sname epoch/-sname epoch2/g' releases/0.5.0/vm.args
```
