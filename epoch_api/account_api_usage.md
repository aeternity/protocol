[back](./epoch_api.md)
# Account management - intended usage

Each node handles one account.

The following assumes that the node exposes at address 127.0.0.1 the following ports:
* HTTP external API: 3013
* HTTP internal API: 3113

## Retrieve your public key

Retrieve the public key of your node:
```bash
curl http://127.0.0.1:3113/v2/account/pub-key
```
You shall read output like the following:
```
{"pub_key":"ak$3N1WLMewMQPUyQBdEhXRSYee84RQNKJrECwbbseMkNsZhv1XLjpmiqjAkvSRpQ6kgWJMjq9dTmdQ3ekuhpscJk6LpjJYk4"}
```

## Retrieve your balance

In order to retrieve your balance, retrieve your public key then retrieve the balance associated to the retrieved public key (replace the public key in the command):
```bash
curl -G http://127.0.0.1:3013/v2/account/balance --data-urlencode 'pub_key=ak$3N1WLMewMQPUyQBdEhXRSYee84RQNKJrECwbbseMkNsZhv1XLjpmiqjAkvSRpQ6kgWJMjq9dTmdQ3ekuhpscJk6LpjJYk4'
```
You shall read output like the following...
```
{"balance":80}
```
... or - if you do not have tokens yet e.g. because you have not yet mined a block successfully - the following:
```
{"reason":"Account not found"}
```
