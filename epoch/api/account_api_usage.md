[back](./README.md)
# Account management - intended usage

Each node handles one account.

The following assumes that the node exposes at address 127.0.0.1 the following ports:
* User API external HTTP endpoint: 3013
* User API internal HTTP endpoint: 3113

## Retrieve your balance

Retrieve balance for given public key (replace the public key in the command):
```bash
curl -G 'http://127.0.0.1:3013/v2/accounts/ak_N1WLMewMQPUyQBdEhXRSYee84RQNKJrECwbbseMkNsZhv1X'
```
You shall read output like the following...
```
{"balance":80, "id":"ak_N1WLMewMQPUyQBdEhXRSYee84RQNKJrECwbbseMkNsZhv1X", "nonce":0}
```
... or - if you do not have tokens yet e.g. because you have not yet mined a block successfully - the following:
```
{"reason":"Account not found"}
```

**NOTE** node beneficiary public key can be found in configuration file (`mining > beneficiary` parameter).
```
cat epoch.yaml

--CUT--
mining:
    beneficiary: "ak_jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdF"
--CUT--
```
