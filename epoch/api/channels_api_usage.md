[back](./README.md)
# Channels - intended usage

## Introduction
You interact with a Aeternity node both through HTTP requests and Websocket
connections.
To learn more about channels and their life cycle see [the doc](/channels/README.md).

In each channel there are two websocket client parties. Once the channel is opened - they are
equal in every regard. They have different roles while opening and we have
names for them - `initiator` and `responder`. For short we will call them _the
parties_.

There are two basic types of interactions: persisted connection events and HTTP API calls.

### Websocket life cycle
These are used for the scenrio when all parties behave correctly and as
expected. The flow is the following:

1. [Channel open](#channel-open)
2. Update channel state
3. Channel mutual close

Only steps 1 and 3 require chain interactions, step 2 is off-chain.

### HTTP requests
There are two types of HTTP requests:
* Channel amounts modifying ones - [deposit](#deposit-transaction) and [withdrawal](#withdrawal-transaction)
* Channel close ones - [solo close](#solo-close-transaction),
  [slash](#slash-transaction) and [settle](#settle-transaction)

## Channel open
In order to use a channel - it must be opened. Both parties negotiate conditions for the channel - for example the amounts to participate. Some of those are relevant to the chain and end up in a`channel_create_tx` that is posted on the chain. Then after a certain amounts of blocks are mined on top of the one that included it - the channel is considered to be opened.

### Channel parameters
Each channel has a set of parameters that is required for opening a
connection. Most of those are part of the `channel_create_tx` that is included
in the chain and the others are meta data used for the connection itself.

  | Name | Type | Description | Required | Part of the `channel_create_tx` |
  | ---- | ---- | ----------- | -------- |------------------------------ |
  | initiator | string | initiator's public key | Yes | Yes |
  | responder | string | responder's public key | Yes | Yes |
  | lock_period | integer | amount of blocks for disputing a solo close | Yes | Yes |
  | push_amount | integer | initial deposit in favour of the responder by the initiator | Yes | Yes |
  | initiator_amount | integer | amount of tokens the initiator has commited to the channel | Yes | Yes |
  | responder_amount | integer | amount of tokens the responder has commited to the channel | Yes | Yes |
  | channel_reserve | integer | the minimum amount both peers need to maintain | Yes | Yes |
  | ttl | integer | minimum block height to include the `channel_create_tx` | Yes | Yes |
  | host | string | host of the `responder`'s node| Yes | No |
  | port | integer | the port of the `responder`s node| Yes | No |
  | timeouts | object | the maximum lenght of time waiting for the other party to respond in the different states| No | No |
  | minimum_depth | integer | the minimum amount of blocks to be mined | No | No |

  In the following examples we will be using the following parameters:

  | Name | Value |
  | ---- | ----- |
  | initiator | ak$3YGRJv1QMgNbeDzvqX7qJrZWJDaHGmrHYHifxSbhSEgn6anuNYCNPrzsB911xTbZ35bvJYWLyYjrQaQKfvja9gkpvYMfEZ |
  | responder | ak$3gVuduh7vR9G7Hq3TpFaA7q9oQkMZZF2VsUxDYZabNeKC1uaqtjpKSth7wPn9dxnUzsHoT2fa6GPUzepbDXMHyC2F3HupT |
  | lock_period | 10 |
  | push_amount | 3 |
  | initiator_amount | 10 |
  | responder_amount | 10 |
  | channel_reserve | 2 |
  | ttl | 1000 |

  The `initiator` will be connecting the `responder` on localhost:1234
  We will be using the tool [wscat](https://github.com/websockets/wscat)
  We assume the channel's websocket listener is set on port 3014 (default one)

### Initiator websocket open
Using the set of prenegotiated parameters the initiator connects
```
$ wscat --connect
'localhost:3014/channel?initiator=ak$3YGRJv1QMgNbeDzvqX7qJrZWJDaHGmrHYHifxSbhSEgn6anuNYCNPrzsB911xTbZ35bvJYWLyYjrQaQKfvja9gkpvYMfEZ&responder=ak$3gVuduh7vR9G7Hq3TpFaA7q9oQkMZZF2VsUxDYZabNeKC1uaqtjpKSth7wPn9dxnUzsHoT2fa6GPUzepbDXMHyC2F3HupT&lock_period=10&push_amount=3&initiator_amount=10&responder_amount=10&channel_reserve=2&ttl=1000&host=localhost&port=1234&role=initiator'

connected (press CTRL+C to quit)
```

Note the `role=initiator` as it is specific

### Responder websocket open
Using the set of prenegotiated parameters the responder connects
```
$ wscat --connect
'localhost:3014/channel?initiator=ak$3YGRJv1QMgNbeDzvqX7qJrZWJDaHGmrHYHifxSbhSEgn6anuNYCNPrzsB911xTbZ35bvJYWLyYjrQaQKfvja9gkpvYMfEZ&responder=ak$3gVuduh7vR9G7Hq3TpFaA7q9oQkMZZF2VsUxDYZabNeKC1uaqtjpKSth7wPn9dxnUzsHoT2fa6GPUzepbDXMHyC2F3HupT&lock_period=10&push_amount=3&initiator_amount=10&responder_amount=10&channel_reserve=2&ttl=1000&port=1234&role=responder'

connected (press CTRL+C to quit)
```

Note the `role=responder` as it is specific. Note also that the `host` is missing - it is not required for the responder.

### Connection opened messages
Parties websocket clients receive messages for the opening of the TCP
connection.

#### Initiator connection opened message
The initiator receives the following message
```
{'action': 'info',
 'payload': {'event': 'channel_accept'}
 }
```
#### Responder connection opened message
The responder receives the following message
```
{'action': 'info',
 'payload': {'event': 'channel_open'}
 }
```

### Create transaction signing
The `channel_create_tx` is sent subsequently to both parties and they co-sign
it. Then it is posted to the chain.

#### Initiator signs the tx
The initiator receives a message containing the unsigned transaction
```
{'action': 'sign',
 'payload': {'tx': 'tx$3KVbfQyL3812oUXuaKFrU35yh918LtZS9vSX3xkkyCCQUCReBH3znrhhcKEfv7Et2Unz3Wasec9Ty97xs4VCB3k2GBjhp1bHtYuNcD1JVKCbvfY68JyiVcCzdQJh1SfDtjMLxwaJtQGhUbaF2VySaBwFBTKTzHVCL58owtfXzt972GZEGmEtrdyY7Z1NNg25yhrPyAyGvKZY6WV'}
 }
```
Initiator is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a websocket message:
```
{'action': 'initiator_signed',
 'payload': {'tx': 'tx$Vb6U4dbYYjKr1eq2iU9ftCb3sVLoq3NzBdSpLqgrARkYJ1VgcubZhXRXDuYqoMFrtpJsxpfA5yq4woAUwc4SVYFHZNoUpLqpxbgtDBxDfFz3h3FBzLasqQcNAqqzjiufeuhmnFVWB1oLBTqdKGYTVsamt4zwL3bct7dVVrYfx2X51kXoom5WwPwmQxKjMSFtKgoYaDgNUx6RNLwnCjdJ1J1Jvcm5mi7JuaRsTzvr4HAmzWm6U9oXwSHih7VQ5VGJ5pA85nbCi6MPgmwZZFCU2xY5mKx4uo6jCXgnqQAQEpqpipuhLsoVnNRU3aY6B'}
 }
```

Please note that the these are just example transactions and you're to have
different values for those.

#### Responder is informed
The responder receives the following message
```
{'action': 'info',
 'payload': {'event': 'funding_created'}
 }
```

#### Responder signs the tx
After being informed for the initiator's signing the responder receives a message containing the unsigned transaction to be signed as well
```
{'action': 'sign',
 'payload': {'tx': 'tx$3KVbfQyL3812oUXuaKFrU35yh918LtZS9vSX3xkkyCCQUCReBH3znrhhcKEfv7Et2Unz3Wasec9Ty97xs4VCB3k2GBjhp1bHtYuNcD1JVKCbvfY68JyiVcCzdQJh1SfDtjMLxwaJtQGhUbaF2VySaBwFBTKTzHVCL58owtfXzt972GZEGmEtrdyY7Z1NNg25yhrPyAyGvKZY6WV'}
 }
```
Note that this is the same transaction. Responder is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a websocket message:
```
{'action': 'responder_signed',
 'payload': {'tx': 'tx$7Uf44dj9jVkgNb4hbCsUamkEL3869mVK5ks4f6Ywi8FBCR4WBrJd6FnVPkpRoV3yU9Y7nqYeGZQ3VfSqvtU5eWJmAUW4dBDyZ68TsgC5kkJn23TMatabo5AowBLBARS2Kji6hEbyta1i1EaKfsj95jcmr4ncKy3VQnur3gDvZpN6sLFSthow7Lh5QDCSVuXzQNhZyTMPayunH7BuWgjEi8FmDJTp2hyR4NeReAaYxFHCD2qZ5kQLzGFHgU9zaydb8X3gB3Bi4fjUoToNmUWTLC9aXF69USSY4SLQZY2C4oV6PbmQTeKdFoahXmmG'}
 }
```
#### Initiator is informed
The initiator receives the following message
```
{'action': 'info',
 'payload': {'event': 'funding_signed'}
 }
```

#### Transaction in mempool
At this point both parties had signed the `channel_create_tx` transaction and
were informed for each other's signing. The transaction is posted by the state
channel's software to the node and goes to the mempool. One can validate it
using the HTTP API:
```
$ curl 'http://localhost:3013/v2/tx/th$hNyHzj4dSzyBqReAMR36GGz1mhuXxQFuES3AnPkXkuY2w6dZb?tx_encoding=json'
```
if the `block_hash` is `none` - then the transaction is still in the mempool.

### Block inclusion
When the transaction is included in a block - this is the first confirmation. A block height timer
started and it ends with `minimum_depth + 1` confirmations. Default value for
it is 4, so 5 blocks need to be mined. After it each party receives two
messages indicating this.

Update from one's node that the block height needed is reached:
```
{'action': 'info',
 'payload': {'event': 'own_funding_locked'}
 }
```
Update from one's node that the other party had confirmed that the block
height needed is reached:
```
{'action': 'info',
 'payload': {'event': 'funding_locked'}
 }
```

From this point on - the state channel is considered to be opened.
