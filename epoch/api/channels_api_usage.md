[back](./README.md)
# Channels - intended usage

## Introduction
You interact with an Aeternity node both through HTTP requests and WebSocket
connections.
To learn more about channels and their life cycle see [the doc](/channels/README.md).

In each channel there are two WebSocket client parties. For each channel, a new WebSocket connection is opened. Once the channel is opened - participants are
equal in every regard. They have different roles while opening and we have
names for them - `initiator` and `responder`. For short we will call them _the
parties_.

There are two basic types of interaction: persisted connection events and HTTP API calls.

### WebSocket life cycle
These are used for the scenario when all parties behave correctly and as
expected. The flow is the following:

1. [Channel open](#channel-open)
2. [Channel off-chain update](#channel-off-chain-update)
3. [Channel mutual close](#channel-mutual-close)

There are a some WebSocket events that can occur while the connection is open
but are not necessarily part of the channel's life cycle.

* [Update error](#update-error)

* [Update conflict](#update-conflict)

* [Generic messages](#generic-messages)

* [Deposit](#deposit-events)

* [Withdrawal](#withdraw-events)

Only steps 1 and 3 require chain interactions, step 2 is off-chain.

### HTTP requests
There are two types of HTTP requests:
* Total amount-modifying ones - [deposit](#deposit-transaction) and [withdrawal](#withdraw-transaction)
* [Channel-closing ones](#solo-closing-sequence) - [solo close](#solo-close-on-chain-transaction), [slash](#slash-on-chain-transaction) and [settle](#settle-on-chain-transaction)

## Channel open
In order to use a channel, it must be opened. Both parties negotiate parameters for the channel - for example the amounts to participate. Some of those are relevant to the chain and end up in a`channel_create_tx` that is posted on the chain. Once a certain amount of blocks have been mined on top of the one that included it, the channel is considered to be opened.

### Channel parameters
Each channel has a set of parameters that is required for opening a
connection. Most of those are part of the `channel_create_tx` which is included
in the chain, and the others are metadata used for the connection itself.

  | Name | Type | Description | Required | Part of the `channel_create_tx` |
  | ---- | ---- | ----------- | -------- |------------------------------ |
  | initiator | string | initiator's public key | Yes | Yes |
  | responder | string | responder's public key | Yes | Yes |
  | lock_period | integer | amount of blocks for disputing a solo close | Yes | Yes |
  | push_amount | integer | initial deposit in favour of the responder by the initiator | Yes | No |
  | initiator_amount | integer | amount of tokens the initiator has committed to the channel | Yes | Yes |
  | responder_amount | integer | amount of tokens the responder has committed to the channel | Yes | Yes |
  | channel_reserve | integer | the minimum amount both peers need to maintain | Yes | Yes |
  | ttl | integer | minimum block height to include the `channel_create_tx` | No | Yes |
  | host | string | host of the `responder`'s node| Yes | No |
  | port | integer | the port of the `responder`s node| Yes | No |
  | timeouts | object | the maximum lenght of time waiting for the other party to respond in the different states| No | No |
  | minimum_depth | integer | the minimum amount of blocks to be mined | No | No |

  In the following examples we will be using the following parameters:

  | Name | Value |
  | ---- | ----- |
  | initiator | ak$ngu1K7uGv9rd9GcEWQkLug6REi6MwWjnFM9WpWYYV9tNz5pQn |
  | responder | ak$zJSpztzPp3ftQmXMUiBgcnmLnCijCViwsfgPo7oHTYhZVchYG |
  | lock_period | 10 |
  | push_amount | 3 |
  | initiator_amount | 10 |
  | responder_amount | 10 |
  | channel_reserve | 2 |
  | ttl | 1000 |

  The `initiator` will be connecting to the `responder` on localhost:1234
  We will be using following tools

  * [wscat](https://github.com/websockets/wscat)
  * [unpack](https://github.com/aeternity/aepp-sdk-js/blob/develop/examples/unpack.js)
  * [sign](https://github.com/aeternity/aepp-sdk-js/blob/develop/examples/sign.js)

  We assume the channel's WebSocket listener is set on port 3014 (default one)

### Initiator WebSocket open
Using the set of prenegotiated parameters the initiator connects
```
$ wscat --connect
'localhost:3014/channel?initiator=ak$ngu1K7uGv9rd9GcEWQkLug6REi6MwWjnFM9WpWYYV9tNz5pQn&responder=ak$zJSpztzPp3ftQmXMUiBgcnmLnCijCViwsfgPo7oHTYhZVchYG&lock_period=10&push_amount=3&initiator_amount=10&responder_amount=10&channel_reserve=2&ttl=1000&host=localhost&port=1234&role=initiator'

connected (press CTRL+C to quit)
```

Note the `role=initiator` as it is specific

### Responder WebSocket open
Using the set of prenegotiated parameters the responder connects
```
$ wscat --connect
'localhost:3014/channel?initiator=k$ngu1K7uGv9rd9GcEWQkLug6REi6MwWjnFM9WpWYYV9tNz5pQn&responder=ak$zJSpztzPp3ftQmXMUiBgcnmLnCijCViwsfgPo7oHTYhZVchYG&lock_period=10&push_amount=3&initiator_amount=10&responder_amount=10&channel_reserve=2&ttl=1000&port=1234&role=responder'

connected (press CTRL+C to quit)
```

Note the `role=responder` as it is specific. Note also that the `host` is missing - it is not required for the responder.

### Connection opened messages
Parties' WebSocket clients receive messages for the opening of the TCP
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
 'tag': 'initiator_sign',
 'payload': {'tx': 'tx$2mXFj7hModynefAE4NPfgh42ozJMfLgBvowCPzw7vo6E86V3Q1PLbukpVJvqCCtxifaWeaQVhVD6LDwEvSEUyZSJvWMn1Am57yasMuz4KxxvrzisP6hha2FnKkks1nJvRznCM2LK4J34oaKDqiGUNsDATZXiU8VYJ3'}
 }
```
Initiator is to decode the transaction, inspect its contents,
```
$ unpack tx\$2mXFj7hModynefAE4NPfgh42ozJMfLgBvowCPzw7vo6E86V3Q1PLbukpVJvqCCtxifaWeaQVhVD6LDwEvSEUyZSJvWMn1Am57yasMuz4KxxvrzisP6hha2FnKkks1nJvRznCM2LK4J34oaKDqiGUNsDATZXiU8VYJ3
{
  "tag": 50,
  "version": 1,
  "initiator": "ak$3jS5Em9khbNzSiyWp8QhfWT1XrRk4nPXRKTPfWQYCVYP4Suh1n",
  "initiatorAmount": 10,
  "responder": "ak$3w3d4SvqpVGohzURw6i91DZgTPvNS3NWawmvYV1nwTwCBajwbV",
  "responderAmount": 10,
  "channelReserve": 2,
  "lockPeriod": 10,
  "ttl": 1000,
  "fee": 1,
  "nonce": -4.003539619888448e+76
}
```
sign it, encode it
```
$ sign tx\$2mXFj7hModynefAE4NPfgh42ozJMfLgBvowCPzw7vo6E86V3Q1PLbukpVJvqCCtxifaWeaQVhVD6LDwEvSEUyZSJvWMn1Am57yasMuz4KxxvrzisP6hha2FnKkks1nJvRznCM2LK4J34oaKDqiGUNsDATZXiU8VYJ3 ca344006e557cd3010b457b048a3184a1e084d139f4382836ff612c012d3dcf767bd6a6d50f142ab71b95841a9976b4720ab87f43cab0eedc72aca6e6b0a9805
tx$3FGkRsVGnkoW6Sh99usX2tx7GGuK3MdUk2ZHLSfJ7cZ4yTmq1QfYm4sk1EGbTC2LMD8Rv7UT9PXHE62jPnuCsnGzQ1o3PJCY99vgzrDEPifyEXMnQJ9MwCHDDbvekbRQSz5h4LyckN9P5aUpC8fM8XmTBFW5D6NXotaRw8ScDHLdtEzpLnQgd66VQ5w5N54wWZRTgepmzNbgVUpXx4dFq9Ssk5UvceaQgMpRegKHKPNuYKJu1sjECsmiLU2zreVQVBkhGR5
```
and then post it back via a WebSocket message:
```
{'action': 'initiator_sign',
 'payload': {'tx': 'tx$3FGkRsVGnkoW6Sh99usX2tx7GGuK3MdUk2ZHLSfJ7cZ4yTmq1QfYm4sk1EGbTC2LMD8Rv7UT9PXHE62jPnuCsnGzQ1o3PJCY99vgzrDEPifyEXMnQJ9MwCHDDbvekbRQSz5h4LyckN9P5aUpC8fM8XmTBFW5D6NXotaRw8ScDHLdtEzpLnQgd66VQ5w5N54wWZRTgepmzNbgVUpXx4dFq9Ssk5UvceaQgMpRegKHKPNuYKJu1sjECsmiLU2zreVQVBkhGR5'}
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
 'tag': 'responder_sign',
 'payload': {'tx': 'tx$2mXFj7hModynefAE4NPfgh42ozJMfLgBvowCPzw7vo6E86V3Q1PLbukpVJvqCCtxifaWeaQVhVD6LDwEvSEUyZSJvWMn1Am57yasMuz4KxxvrzisP6hha2FnKkks1nJvRznCM2LK4J34oaKDqiGUNsDATZXiU8VYJ3'}
 }
```
Note that this is the same transaction. Responder is to decode the transaction, inspect its contents,
```
$ unpack tx\$2mXFj7hModynefAE4NPfgh42ozJMfLgBvowCPzw7vo6E86V3Q1PLbukpVJvqCCtxifaWeaQVhVD6LDwEvSEUyZSJvWMn1Am57yasMuz4KxxvrzisP6hha2FnKkks1nJvRznCM2LK4J34oaKDqiGUNsDATZXiU8VYJ3
{
  "tag": 50,
  "version": 1,
  "initiator": "ak$3jS5Em9khbNzSiyWp8QhfWT1XrRk4nPXRKTPfWQYCVYP4Suh1n",
  "initiatorAmount": 10,
  "responder": "ak$3w3d4SvqpVGohzURw6i91DZgTPvNS3NWawmvYV1nwTwCBajwbV",
  "responderAmount": 10,
  "channelReserve": 2,
  "lockPeriod": 10,
  "ttl": 1000,
  "fee": 1,
  "nonce": -4.003539619888448e+76
}
```
sign it, encode it
```
$ sign tx\$2mXFj7hModynefAE4NPfgh42ozJMfLgBvowCPzw7vo6E86V3Q1PLbukpVJvqCCtxifaWeaQVhVD6LDwEvSEUyZSJvWMn1Am57yasMuz4KxxvrzisP6hha2FnKkks1nJvRznCM2LK4J34oaKDqiGUNsDATZXiU8VYJ3 36fe65f93169b8cf762b299d5436ef672360ef9c584e2c1aeaaf42716b68b89b821bc24797ebb7b1710b4ce85d4ea518865d6d632fd424a5f788bfd968191027
tx$3FGkRsVGnkoU1QD2o72uHQ44p92BENnKbs8bfTpFpeDCJgB2km8V5a6iJTQHLwnWyGNw7bjoEGQp4rhiB9cNmB9CfMM6RDZiuDcT7pYmUtxp7LpBjTN5awF2hhTZFdKHD6AQ6FaLQu17MehqAiEaW6YezXapuR1m7hpS1wGtMnpZNQ9UnBUbRn7vb6t3YV3MSL34CtwATq92wo8qis4fq9Nwdjr47gMDEn8e4Xy2gsDakKXrHFpJGG6nPhxqfNiprnLB8zx
```
and then post it back via a WebSocket message:
```
{'action': 'responder_sign',
 'payload': {'tx': 'tx$3FGkRsVGnkoU1QD2o72uHQ44p92BENnKbs8bfTpFpeDCJgB2km8V5a6iJTQHLwnWyGNw7bjoEGQp4rhiB9cNmB9CfMM6RDZiuDcT7pYmUtxp7LpBjTN5awF2hhTZFdKHD6AQ6FaLQu17MehqAiEaW6YezXapuR1m7hpS1wGtMnpZNQ9UnBUbRn7vb6t3YV3MSL34CtwATq92wo8qis4fq9Nwdjr47gMDEn8e4Xy2gsDakKXrHFpJGG6nPhxqfNiprnLB8zx'}
 }
```
#### Initiator is informed
The initiator receives the following message
```
{'action': 'info',
 'payload': {'event': 'funding_signed'}
 }
```

#### Signed channel_create_tx
Both participants receive the co-signed `channel_create_tx`:
```
{'action': 'on_chain_tx',
 'payload': {'tx': 'tx$4sC4ko4JsBtBakCNPouAqompH1vgWdHM37oAPrmi5L6TymmsWz1ayRoLbPEf74KZcm3b3FtpaXoA8ckAndSav1W62HTGYc1uZVkLGe8SRub2CFwyhvV3kxVjiNLv8V71ST4vnDMicPSsDNLQ9AXs3aZx3YbCmS9CooUyPUBLxcjpd474zSACf1TFULVnLCm7FJisYFWqfa34tUCtAjzTpuYrp8DNz68Jayqjs7W5zVbf7t1d4UxusrLDUCVz7pgKzB9btd7itGEzoXPSx7pMr46fg8Mc93T5PUwJA4kFird54rMHdP81W1yfWp1U7gJFy2cwc6u9zrYkvc8CJMFpd9NXL9S98YU8d'
            }
}
```
Using its hash, participants can track its progress on the chain: entering the mempool, block inclusion and a number of confirmations.

#### Transaction in mempool
At this point both parties had received the co-signed the `channel_create_tx` transaction. The transaction is posted by the state
channel's software to the node and goes to the mempool. Having calculated its hash, one can validate it using the external HTTP API:
```
$ curl 'http://localhost:3013/v2/tx/th$8XtyEosPowxYFzHg1vzLa6oHeBjE8edmT8Dmww7m7iehDEFcZ?tx_encoding=json'
```
if the `block_hash` is `none` - then the transaction is still in the mempool.

### Block inclusion
When the transaction is included in a block - this is the first confirmation. A block height timer is
started and it ends after `minimum_depth + 1` confirmations. Default value for
it is 4, so 5 blocks need to be mined. As a result, each party will receive
two kinds of confirmation.

An update from one's own node that the block height needed is reached:
```
{'action': 'info',
 'payload': {'event': 'own_funding_locked'}
 }
```
An update from one's own node that the other party had confirmed that the block
height needed is reached:
```
{'action': 'info',
 'payload': {'event': 'funding_locked'}
 }
```

### Initial state
After both parties have confirmed that the funding is signed - they can proceed
with sending the messages for off-chain updates. The inital state is the one
described in the create transaction.

#### Open confirmation
After both parties have co-signed the state update both of them will receive a info for the channel open:
```
{'action': 'info',
 'payload': {'event': 'open'}
 }
```

From this point on, the channel is considered to be opened.

## Channel off-chain update
After the channel has been opened and before it has been closed there is a
channel state that is updated when needed. The updates are off-chain and
broadcasted only between parties in the channel. The state represents the last
distribution of the total channel balance. A state is considered to be valid only if both parties have agreed upon it. The latest channel state is the last valid state.
At any time the latest state can be used for unilaterally closing the channel.

### Channel state
Both parties persist their own version of the state. It cointains:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel|
  | initiator | string | initiator's public key |
  | responder | string | responder's public key |
  | initiator amount | integer | new initiator's amount |
  | responder amount| integer | new responder's amount |
  | updates | [update] | update being applied |
  | state | string | placeholder |
  | previous round | integer | reference for the previous round the changes are based at |
  | round | integer | current round |

Each subsequent state has a `round` increased with 1 and a reference to the
previous round. The values of the amounts are the new ones: the result of applying the
update on the referenced round's values.

The `state` field is a placeholder for future use.

Since both participants are peers, they can both trigger new updates to the
state - they are peers.
Since one of them starts the update and the other acknowledges is below we are
going to use `starter` and `acknowledger`. Both the initiator and the
responder can take either of the roles.

### Update
The update is a change to be applied on top of the latest state. It has the
following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | from | string | sender's public key |
  | to | string | receiver's public key |
  | amount | integer | the amount given |

Sender and receiver are the channel parties. Both the initiator and responder
can take those roles. Any public key outside of the channel is considered invalid.

#### Start update
##### Trigger an update
The starter sends a message containing the desired change
```
{'action': 'update',
 'tag': 'new',
 'payload': {
    'from': 'ak$ngu1K7uGv9rd9GcEWQkLug6REi6MwWjnFM9WpWYYV9tNz5pQn',
    'to': 'ak$zJSpztzPp3ftQmXMUiBgcnmLnCijCViwsfgPo7oHTYhZVchYG',
    'amount': 1
    }
 }
```
The `starter` might take the role of `from` or `to` so the `starter` can
trigger sending or request for tokens.

##### Starter signs updated state
The starter receives a message containing the updated channel state as an
off-chain transaction
```
{'action': 'sign',
 'tag': 'update',
 'payload' {
    'tx': 'tx$2ZiP3BBgqkz3aMsPgUmy6G5r19jaNm9jDnz1Y5CJ9uYvEhuiRNiB9HHiF5uzL5XuKBD8eV8brAof9LjBHWtmHVhLaxDi7FRe2N8Ncg6icdukfMstuXWQuqmgrKZX3EKy8s7vBmhZ1LqK88Fpt1Wid31KVqdSZoTSRT3rkF4Gy2LcKYpRVGypDxn4SsFweC9Pk2EutLFzH83'}
}
```
The starter is to decode the transaction, inspect its contents,
```
$ unpack tx\$2ZiP3BBgqkz3aMsPgUmy6G5r19jaNm9jDnz1Y5CJ9uYvEhuiRNiB9HHiF5uzL5XuKBD8eV8brAof9LjBHWtmHVhLaxDi7FRe2N8Ncg6icdukfMstuXWQuqmgrKZX3EKy8s7vBmhZ1LqK88Fpt1Wid31KVqdSZoTSRT3rkF4Gy2LcKYpRVGypDxn4SsFweC9Pk2EutLFzH83
{
  "tag": 57,
  "version": 1,
  "channelId": "DscwCPJtAYxE8LyW67qRTRX8M6oAiRXVeNYmedNc4npctCNptd",
  "round": 2,
  "updates": [
    [
      0,
      "ak$ngu1K7uGv9rd9GcEWQkLug6REi6MwWjnFM9WpWYYV9tNz5pQn",
      "ak$zJSpztzPp3ftQmXMUiBgcnmLnCijCViwsfgPo7oHTYhZVchYG",
      1
    ]
  ],
  "state": "28hEspzAtCMPTNHaSrrxJhWqg2hC2kYCHL6iBQX9m5CsGLhRXm"
}
```
sign it, encode
```
$ sign tx\$2ZiP3BBgqkz3aMsPgUmy6G5r19jaNm9jDnz1Y5CJ9uYvEhuiRNiB9HHiF5uzL5XuKBD8eV8brAof9LjBHWtmHVhLaxDi7FRe2N8Ncg6icdukfMstuXWQuqmgrKZX3EKy8s7vBmhZ1LqK88Fpt1Wid31KVqdSZoTSRT3rkF4Gy2LcKYpRVGypDxn4SsFweC9Pk2EutLFzH83 ca344006e557cd3010b457b048a3184a1e084d139f4382836ff612c012d3dcf767bd6a6d50f142ab71b95841a9976b4720ab87f43cab0eedc72aca6e6b0a9805
tx$2zGVUPYVUQUUTpegj3RnUsHaESFjXV3VUURBukPEv2Hz4iLYxnMWAHiji2dN5sp15DdnbRcfaE6KwYKrmBB9zcavmJpaedY33bzF2q1XS6HFinrZXJNEpHE6A18wTUp6zm8wSJY1Dm3UUR5KQhEUtGWbo97A42HYhApNiMjZz5XB8fY8GsCcv2LkntJ75ucUu9CUWwHr5rBdf2mkLqKWsxaxmMFsNHbeYKjKanAyjc6T4BGhMvxHSDZgfYLc1NsvRkC8RPa3DNkqCSQo49vSRptjcy3jV8ENkU5W1MjimSmfdaH9
```
it and then post it back via a WebSocket message:
```
{'action': 'update',
 'payload': {
    'tx': 'tx$2zGVUPYVUQUUTpegj3RnUsHaESFjXV3VUURBukPEv2Hz4iLYxnMWAHiji2dN5sp15DdnbRcfaE6KwYKrmBB9zcavmJpaedY33bzF2q1XS6HFinrZXJNEpHE6A18wTUp6zm8wSJY1Dm3UUR5KQhEUtGWbo97A42HYhApNiMjZz5XB8fY8GsCcv2LkntJ75ucUu9CUWwHr5rBdf2mkLqKWsxaxmMFsNHbeYKjKanAyjc6T4BGhMvxHSDZgfYLc1NsvRkC8RPa3DNkqCSQo49vSRptjcy3jV8ENkU5W1MjimSmfdaH9'
    }
}
```
#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```
{'action': 'info',
 'payload': {'event': 'update'}
 }
```
Then the acknowledger receives a new message containing the updated channel state as an
off-chain transaction
```
{'action': 'sign',
 'tag': 'update_ack',
 'payload' {
    'tx': 'tx$2ZiP3BBgqkz3aMsPgUmy6G5r19jaNm9jDnz1Y5CJ9uYvEhuiRNiB9HHiF5uzL5XuKBD8eV8brAof9LjBHWtmHVhLaxDi7FRe2N8Ncg6icdukfMstuXWQuqmgrKZX3EKy8s7vBmhZ1LqK88Fpt1Wid31KVqdSZoTSRT3rkF4Gy2LcKYpRVGypDxn4SsFweC9Pk2EutLFzH83'
    }
}
```
Note that this is the same transaction as the one that the starter had already signed. The acknowledger is to decode the transaction, inspect its contents,
```
$ unpack tx\$2ZiP3BBgqkz3aMsPgUmy6G5r19jaNm9jDnz1Y5CJ9uYvEhuiRNiB9HHiF5uzL5XuKBD8eV8brAof9LjBHWtmHVhLaxDi7FRe2N8Ncg6icdukfMstuXWQuqmgrKZX3EKy8s7vBmhZ1LqK88Fpt1Wid31KVqdSZoTSRT3rkF4Gy2LcKYpRVGypDxn4SsFweC9Pk2EutLFzH83
{
  "tag": 57,
  "version": 1,
  "channelId": "DscwCPJtAYxE8LyW67qRTRX8M6oAiRXVeNYmedNc4npctCNptd",
  "round": 2,
  "updates": [
    [
      0,
      "ak$ngu1K7uGv9rd9GcEWQkLug6REi6MwWjnFM9WpWYYV9tNz5pQn",
      "ak$zJSpztzPp3ftQmXMUiBgcnmLnCijCViwsfgPo7oHTYhZVchYG",
      1
    ]
  ],
  "state": "28hEspzAtCMPTNHaSrrxJhWqg2hC2kYCHL6iBQX9m5CsGLhRXm"
}
```
sign it, encode it
```
$ sign tx\$2ZiP3BBgqkz3aMsPgUmy6G5r19jaNm9jDnz1Y5CJ9uYvEhuiRNiB9HHiF5uzL5XuKBD8eV8brAof9LjBHWtmHVhLaxDi7FRe2N8Ncg6icdukfMstuXWQuqmgrKZX3EKy8s7vBmhZ1LqK88Fpt1Wid31KVqdSZoTSRT3rkF4Gy2LcKYpRVGypDxn4SsFweC9Pk2EutLFzH83 36fe65f93169b8cf762b299d5436ef672360ef9c584e2c1aeaaf42716b68b89b821bc24797ebb7b1710b4ce85d4ea518865d6d632fd424a5f788bfd968191027
tx$2zGVUPYVUQUUYM6zKmaPmg7nmUWrmZ8MZzQ8r9T13SD2WrN17CL2XK96tbfRZFoHMjuRX5ARBP4Sdw1fwnCBrgp2mixxBPAwVdNd17pVpZwFiNaetcwa6h8zjFZu9q2pZniqyS8HzyA7LRaGCFrZ77oWR2biie22GgU9VE4iCQd2oK62SmRKYhgaPsma185a8oDEU4jx4kMdCCfNpqAmBtKqe7G2nrqYS9EM8TvbKSyYf6TjC31jGq9n6pi5ukBT2hVeZ7Mi2HXoKJ7e5fF4tkzHHcisjGSe6PyccdkoCajgp1fr
```
and then post it back via a WebSocket message:
```
{'action': 'update_ack',
 'payload': {
    'tx': 'tx$2zGVUPYVUQUUYM6zKmaPmg7nmUWrmZ8MZzQ8r9T13SD2WrN17CL2XK96tbfRZFoHMjuRX5ARBP4Sdw1fwnCBrgp2mixxBPAwVdNd17pVpZwFiNaetcwa6h8zjFZu9q2pZniqyS8HzyA7LRaGCFrZ77oWR2biie22GgU9VE4iCQd2oK62SmRKYhgaPsma185a8oDEU4jx4kMdCCfNpqAmBtKqe7G2nrqYS9EM8TvbKSyYf6TjC31jGq9n6pi5ukBT2hVeZ7Mi2HXoKJ7e5fF4tkzHHcisjGSe6PyccdkoCajgp1fr'
  }
}
```
#### Finish update
After both the parties had signed the new updated state of the channel - it is
considered the latest one. Corresponding info messages are sent to both
parties to indicate it.
```
{'action': 'info',
 'payload': {'event': 'update_finalized'}
 }
```
After that a new state updated can be triggered.

## Channel mutual close
At any moment after the channel is opened, a closing procedure can be
triggered. This can be done by either of the parties. The process is similar to
the [off-chain updates](#channel-off-chain-update). The most notable change is the
special transaction co-signed by both parties. It is called
`channel_close_mutual_tx`. After gathering singatures it will end up on the
chain and has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel|
  | from | string | initiator's public key |
  | initiator_amount | integer | final amount of tokens to be awarded by the initiator |
  | responder_amount | integer | final amount of tokens to be awarded by the responder |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | nonce | integer | initiator's nonce |

Since any of the participants can initiate a closing, we will use `starter`
for the peer that triggers the process and `acknowledger` for the other one.

### Initiate mutual close
The starter sends the following message and triggers the closing procedure:
```
{'action': 'shutdown'}
```

### Starter signing
Then the starter receives a `channel_close_mutual_tx` to sign:
```
{'action': 'sign',
 'tag': 'shutdown_sign',
 'payload': {
    'tx': 'tx$SUBGDUaJgWhDYs73EPSiX42Xd3PSmHAhRmwd1th9ibGipCVVbsdS96roQZEH4MF'
    }
}
```
Starter is to decode the transaction, inspect its contents,
```
$ unpack tx\$2C9etiP9wZr2iQVj6BUYk5sxHVNgcVhK4ngwv7fjsnnj2S1przQggcqyfhfJGgMPkpzoDfBZM7SyxVQykUCHvJw2N7E5gWSMuiuGjL4fYYUAXkEeyJygCAqKiszgqz8RuBDAfyCX44SsC5Ev1KU84jkui5EVxb
{
  "tag": 53,
  "version": 1,
  "channelId": "2LvsrNZqzei11qdv8PQuDvPD7tro8sgBSjRo5GJPnbmGsmTb6B",
  "initiatorAmount": 6.377576942165202e+154,
  "responderAmount": 6,
  "ttl": 3,
  "fee": 1000,
  "nonce": 1
}
```
sign it, encode it
```
$ sign tx\$2C9etiP9wZr2iQVj6BUYk5sxHVNgcVhK4ngwv7fjsnnj2S1przQggcqyfhfJGgMPkpzoDfBZM7SyxVQykUCHvJw2N7E5gWSMuiuGjL4fYYUAXkEeyJygCAqKiszgqz8RuBDAfyCX44SsC5Ev1KU84jkui5EVxb --file starter_key
tx$4L9GSozvWQwFDrkxaT2DZYrXU1sFULxRkpFbKjzAR4XinUwRgFvzm7ct7ZCvq38ZfCUZR73yXHRnd2DURPCmwdj7NarynugJ5JkY5TVN6ZzxVMEs6nsA8Dfu7dA9AoFj3AwaDLdaBuUEXuXTvsLEZy57GCG2v8HLucFkpHRTK63VdG8UNMK429ofMqHo8QyPjdwHYjH43baCSiN21g2hfpL9qWBmGwmcipSKuV5tHKg2aMpURCHM1z1FnRqdosiVM42PJTxSAHv
```
and then post it back via a WebSocket message:
```
{'action': 'shutdown_sign',
 'payload': {
    'tx': 'tx$8oWtHcfnWDSQV6Wdehp1MdXYhcbV29a7tWe3LWDqU5RwKvMhzPQLiSJKaYhtw4NLaBN1m3pmEtsVjoygkohXi9i8e3vpYgenphdKJmYLrFqjouxmyC5yKbsQUY8m9i4EzcMNuHmrLwrXrrPhKC1qY25Pxb6u74VEVuk'
    }
}
```
### Acknowledger signing
Then the acknowledger receives a `channel_close_mutual_tx` to sign:
```
{'action': 'sign',
 'tag': 'shutdown_sign_ack',
 'payload': {
    'tx': 'tx$SUBGDUaJgWhDYs73EPSiX42Xd3PSmHAhRmwd1th9ibGipCVVbsdS96roQZEH4MF'
    }
}
```
Note that this is the same transaction. The acknowledger is to decode the transaction, inspect its contents,
```
$ unpack tx\$2C9etiP9wZr2iQVj6BUYk5sxHVNgcVhK4ngwv7fjsnnj2S1przQggcqyfhfJGgMPkpzoDfBZM7SyxVQykUCHvJw2N7E5gWSMuiuGjL4fYYUAXkEeyJygCAqKiszgqz8RuBDAfyCX44SsC5Ev1KU84jkui5EVxb
{
  "tag": 53,
  "version": 1,
  "channelId": "2LvsrNZqzei11qdv8PQuDvPD7tro8sgBSjRo5GJPnbmGsmTb6B",
  "initiatorAmount": 6.377576942165202e+154,
  "responderAmount": 6,
  "ttl": 3,
  "fee": 1000,
  "nonce": 1
}
```
sign it, encode it
```
$ sign tx\$2C9etiP9wZr2iQVj6BUYk5sxHVNgcVhK4ngwv7fjsnnj2S1przQggcqyfhfJGgMPkpzoDfBZM7SyxVQykUCHvJw2N7E5gWSMuiuGjL4fYYUAXkEeyJygCAqKiszgqz8RuBDAfyCX44SsC5Ev1KU84jkui5EVxb --file acknowledger_key
```
and then post it back via a WebSocket message:
```
{'action': 'shutdown_sign_ack',
 'payload': {
    'tx': 'tx$8oWtHcfnWDSYu4SfLLLHqYqM5JXiCZd6De7fLQZesMHrArZeWzP7893EVpBpUR56tKUeJXJ3YUTuqB8a4efiHaw6ai3GKwoeu3ZyzfGPUfb5EMG6viv2dM8mhtKqaG7fkEAWuswbmFN4bDjXANbAK2sMU36yfBc9p1h'
    }
}
```

#### Signed channel_close_mutual_tx
Both participants receive the co-signed `channel_close_mutual_tx`:
```
{'action': 'on_chain_tx',
 'payload': {'tx': 'tx$ERkuTBJfEHtrmDkFz7BaigSKsnqmsCc8MorKFUwAW5VmpSoatcN3Njy2Vda8asojeshjb7SoXsqevaDLzXj78GSPwTTfYJmJtwrewTwK3LSFBe5BEYMA8rxNAWSahW1ecp1wbkBgpdiUQn1Q1UFLcYVpWYGpTWFH5DXn69iz6kFWX8sa7c5PSTaLenjVZEkbV9pEgKHKbjfovvd15Jc821y3zhQvtfhcYKS89r7gnhi81LWsjnSghmjANgjiC'
            }
}
```
Using its hash, participants can track its progress on the chain: entering the mempool, block inclusion and a number of confirmations.

### Channel closing
After both parties have received the co-signed `channel_close_mutual_tx` transaction, it is posted on the chain and the microservice handling the off-chain
requests dies. Parties receive the following info:
```
{'action': 'info',
 'payload': {'event': 'died'}
 }
```
Then the WebSocket connection is closed.

### Tracking the progress of the onchain transaction
After calculating the hash of the co-signed `channel_close_mutual_tx` parties can track
its progress as they would do with any on-chain transaction
```
curl 'http://127.0.0.1:3013/v2/tx/th$2qkN973cNJiejXVJoXkXbttf1iKetWJCSY1W5VUBh3pnRS1kCC?tx_encoding=json'
```
if the `block_hash` is `none` - then the transaction is still in the mempool.

### Other WebSocket events
#### Update error
Updates are not always successful, for example one participant tries to spend
more tokens that one currently has in the channel's balance. This diverges
from the update flow [described above](#channel-off-chain-update).

Example message for when the `from` does not have enough tokens to spend
```
{'action': 'error',
 'payload': {'reason': 'insufficient_balance',
             'request': {'action': 'update',
                         'payload': {'amount': 10000,
                                     'from': 'ak$4Kr76woCtc3ehZ45K1sCrmgKX6gnh7qGhjSU1GZYqfLTTjtCgn',
                                     'to': 'ak$35Wxqf2cbzQF5hEV1j9AdXQFTMxqKCwM7iMKNGcqSv47MXAj68'
                                     },
                          'tag': 'new'
                          }
              }
}
```

The structure is having a `reason` and `request` holding the request being
sent. Possible error reasons are:

* `insufficient_balance` - when `from` does not have enough tokens in the
  channel. Keep in mind that there is a minimal amount of `channel_reserve`
  tokens to be kept by both parties.

* `negative_amount` - the `udpate` event contained a negative amount

* `invalid_pubkeys` - at least one of the addresses in the `update` event is
  not present in the channel.

#### Update conflict

Since updates can be triggered by either party, it is possible both
participants to start an `update` almost simultaneously. If a new `update` is
started by a participant while the other participant has started an `update` of
ones' own - a conflict occurs. Then both `update`-s are invalidated and the
state is reverted to the last mutually signed one. Both participant receive a
message containing a reference to the correct state.
```
{'action': 'conflict',
 'payload': {'channel_id': 'ch$WmpDbaiCs5roqRCL5KEKbpsDNJSbcbiUvt2cs1qyj4sM9HA3b',
             'round': 42
             }
}
```

#### Generic messages

There is the functionality to send participants messages containing
information. In the scope of this - we are going to be calling those a `sender`
and a `receiver`. These roles can be taken by any of the participants, anytime.

The `sender` pushes a message with the following structure:

```
{'action': 'message',
 'payload': {'info': 'hejsan',
             'to': 'ak$35Wxqf2cbzQF5hEV1j9AdXQFTMxqKCwM7iMKNGcqSv47MXAj68'
             }
}
```

Then the `receiver` gets an event containing the info being sent and some
details:

```
{'action': 'message',
 'payload': {'message': {'channel_id': 'ch$6SgSc7a14dGbwMNCsjjQZCYVreVLKkFwBzJEZ58ZSZnV9FiQ1',
                         'from': 'ak$4Kr76woCtc3ehZ45K1sCrmgKX6gnh7qGhjSU1GZYqfLTTjtCgn',
                         'to': 'ak$35Wxqf2cbzQF5hEV1j9AdXQFTMxqKCwM7iMKNGcqSv47MXAj68',
                         'info': 'hejsan'
                         }
            }
}
```

#### Total balance update events

After the channel has been opened it has a total balance of tokens committed to
it. This balance is persisted as part of the on-chain channel state. Upon
closing a channel on-chain, the closing balances of the participants are
checked against this balance. Under no circumstances can the sum of the closing balances
be greater than the total balance on-chain.

Participants are able to modify the total balance: the following two functionalities are available:

* deposit - when a participant wants to commit more tokens from his on-chain
  balance to the channel total balance
* withdrawal - when a participant wants to transfer tokens out of the channel
  on-chain balance to one's personal account

### Deposit events

After the channel had been opened any of the participants can initiate a
deposit. The process closely resembles the [update](#update). The most notable
difference is the transaction has been co-signed: it is `channel_deposit_tx` and
after the procedure is finished, it is posted on-chain.

Since both the initiator and responder can deposit tokens, in the scope of this description we
will call the participant that commits tokens to the channel a depositor and
the other party - acknowledger. Note that any public key outside of the channel participants
is considered invalid for the depositor role.

#### Deposit transaction
The `channel_deposit_tx` is a change to be applied on top of the latest channel state. It also is
posted on-chain and is included in a block. It has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel|
  | from | string | depositor's public key |
  | amount | integer | the amount committed to the channel |
  | ttl | integer | minimum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | state_hash | string | the root of the internal channel state hash after the deposit |
  | round | integer | the next channel round |
  | nonce | integer | depositor's nonce |

#### Start deposit

Any of the participants can initiate a deposit. Only requirements are:
* Channel is already opened
* No off-chain update/deposit/withdrawal is currently being performed
* Channel is not being closed or in a solo closing state
* The deposit must be equal to or greater than zero, and cannot exceed the
  available balance on the depositor's account

##### Trigger a deposit

The depositor sends a WebSocket message containing the desired change
```
{'action': 'deposit',
 'payload': {
    'amount': 2
    }
 }
```

##### Depositor signs updated state
The depositor receives a message containing the updated channel state as a
`channel_deposit_tx` transaction
```
{'action': 'sign',
 'tag': 'deposit_tx',
 'payload' {
    'tx': 'tx$2C9es4FjJF3MtD1M3Np7tUzgCk8AE3ARVJe94Sxmh63feCNt2CekXvjLhBPS2i8pQ8JKGQfgzMQnvfntEdYmMYo7D1UP59UUQ31Bss5G1gz8sPhzmrx1cXCawF9eB27gjYVhTnaLXwUEqdJfHqfATuwLqJtc1p'}
}
```
The depositor is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'deposit_tx',
 'payload': {
    'tx': 'tx$i2WsEQsiC5XsnyKgLeXGW6b9ys87yoQzNB65csymQbK9AsuWApenk9ViHpzxb2oJwUCGiqzA1Cc1D6pJAjkLcQ6w3m8Bhvt41HSqtpSpEd1MciHMcFg1xsZG9CsPu1NUBey9EupgXFJtZ4caNMXcV4evV7ocBjzdBcJo5CUMQgapQZ8ajgUrPgfqQTb3Gq8FFCuHHaHytA7fTNik4KAAvyHiEDutXf1VJxXG2oYkpoNTQGuriV3g4Hxrms3r7LD8ko91'
    }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```
{'action': 'info',
 'payload': {'event': 'deposit_created'}
 }
```
Then the acknowledger receives a new message containing the deposit
transaction for confirmation:
```
{'action': 'sign',
 'tag': 'deposit_ack',
 'payload' {
    'tx': 'tx$2C9es4FjJF3MtD1M3Np7tUzgCk8AE3ARVJe94Sxmh63feCNt2CekXvjLhBPS2i8pQ8JKGQfgzMQnvfntEdYmMYo7D1UP59UUQ31Bss5G1gz8sPhzmrx1cXCawF9eB27gjYVhTnaLXwUEqdJfHqfATuwLqJtc1p'
    }
}
```
Note that this is the same transaction as the one that the depositor had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'deposit_ack',
 'payload': {
    'tx': 'tx$2WsEQsiC5Xso1aHppqY8EwniUa9demV2SAdrNckji4H5ZRDnakiMPAWRv4SSksecqXBCriNTTFg6c3dXK9TzmRV7DoqkKH68Vh7XbVGS7g9CQfaj46S8wgsFBdJtoBMnHV3xbbzSz36cMAAN3eosKaA74TMkgXWgrDCD619RnmskuyvArGbgy6fMFqSniG1s9a3WoTMLoFyw6ucpxgS523Dk3SQEbPAxznbL9KsBEjsCroe4HBVZZG5bX3LU8ZX9PUy'
  }
}
```

#### Finish deposit
After both parties had signed the deposit transaction, the transaction is posted on-chain and
both parties receive it:
```
{'action': 'on_chain_tx',
 'payload': {'tx': 'tx$3cDMp6242sBycND2FPT2jcDWFceRgA7zL3ckU8VzLQdvf2Uqjx5CKkjMXbYrmYjMnLnDihVTrF2fCLqNG93BTAsCNWT6QiJwdmXrTXLQ2d2d7rAc5bYepTC2w3LyrZ37jhx3dN7ATusjXtSu6jw9N8exaPxnjKD3twye5B6bdqbZEHKXXtqStUmaTmUDofEWtGaUCxTWKCboMH7T2mxEjzxgpaH2fbHRxA3GmxaTaKWoTfbnvqragH9QVo6QxiCRAGNUEkbRbPw8m1qPUKjVFWWQSZ9VcCdXte3DitS3anXv7jtTKAA7uuj5pbdG4qi64dDLTd52sSQP6JZpzMxa6oyJTDo5s'
            }
}
```
They are both to compute the transaction hash. Using it,
participants can track its progress on the chain: entering the mempool, block
inclusion and a number of confirmations.

After the `minimum_depth` block confirmations each participant is informed
for the deposit progress on-chain by one's own node:
```
{'action': 'info',
 'payload': {'event': 'own_deposit_locked'}
 }
```
An update from one's own node that the other party had confirmed that the block
height needed is reached:
```
{'action': 'info',
 'payload': {'event': 'deposit_locked'}
 }
```
With this the deposit sequence is complete and the channel can continue with
other updates. Note that the deposit transaction's `round` and `state_hash`
are the ones considered latest from the channel's perspective. For example the
next correct off-chain update/deposit/withdrawal shall have a deposit
transaction's `round` plus one.

### Withdraw events

After the channel had been opened any of the participants can initiate a
withdrawal. The process closely resembles the [update](#update). The most notable
difference is that the transaction has been co-signed: it is `channel_withdraw_tx` and
after the procedure is finished - it is being posted on-chain.

Since both the initiator and responder can withdraw tokens, in the scope of this description we
will call the participant that commits tokens to the channel a withdrawer and
the other party - an acknowledger. Note that any public key outside of the channel participants
is considered invalid for the withdrawer role.

#### Withdraw transaction
The `channel_withdraw_tx` is a change to be applied on top of the latest channel state. It also is
posted on-chain and is included in a block. It has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel|
  | to | string | withdrawer's public key |
  | amount | integer | the amount taken out from the channel |
  | ttl | integer | minimum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | state_hash | string | the root of the internal channel state hash after the withdraw |
  | round | integer | the next channel round |
  | nonce | integer | withdrawer's nonce |

#### Start withdraw

Any of the participants can initiate a withdrawal. The only requirements are:
* Channel is already opened
* No off-chain update/deposit/withdrawal is currently being performed
* Channel is not being closed or in a solo closing state
* The withdrawal amount must be equal to or greater than zero, and cannot
  exceed the available balance on the channel (minus the `channel_reserve`)

##### Trigger a withdrawal

The withdrawer sends a WebSocket message containing the desired change
```
{'action': 'withdraw',
 'payload': {
    'amount': 2
    }
 }
```

##### Withdrawer signs updated state
The withdrawer receives a message containing the updated channel state as a
`channel_withdraw_tx` transaction
```
{'action': 'sign',
 'tag': 'withdraw_tx',
 'payload' {
    'tx': 'tx$2C9estKT2f86WwC7LCa18cDTTmMCrXM7N2AcrXKmgnTo9DNchXjNmewbgNX2YW4RYk8iHkVRnPpeYLRgh6xH96mHNxCMW4aUL2hgTe6iqdrKyM5eqMbCN9YgTdDvUzDyASJwoicxXb7UeDF5kFWvsEMxXBKGX2'}
}
```
The withdrawer is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'withdraw_tx',
 'payload': {
    'tx': 'tx$2WsEQsiC5Xsn85g88TmLYonFu2r8HT53jQPJ7f6Ai9uvnZGwnExRyJ51nHS2mU4g2FUTf2PHUsgs22X5Nwg1E1Zy8ofuoJAttqhXpySyYJhCwdWXYKF6bapSXCLwQoKJ9bWLYYZqudsiPfwv43ekzgJHtaWozzFjrEq835B7Xbd8LSd4znVh2FRWfAPW1Zvsm6nKjN2NfEPndwbps7zgqvbQYeKngwFk952CLtDEpGfXXiS5pUp5ExYTwsxGE4E6LKV'
    }
}
```

#### Acknowledger update
The acknowledger receives an info message indicating an upcoming change:
```
{'action': 'info',
 'payload': {'event': 'withdraw_created'}
 }
```
Then the acknowledger receives a new message containing the withdraw
transaction for confirmation:
```
{'action': 'sign',
 'tag': 'withdraw_ack',
 'payload' {
    'tx': 'tx$2C9estKT2f86WwC7LCa18cDTTmMCrXM7N2AcrXKmgnTo9DNchXjNmewbgNX2YW4RYk8iHkVRnPpeYLRgh6xH96mHNxCMW4aUL2hgTe6iqdrKyM5eqMbCN9YgTdDvUzDyASJwoicxXb7UeDF5kFWvsEMxXBKGX2'}
    }
}
```
Note that this is the same transaction as the one that the withdrawer has already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'withdraw_ack',
 'payload': {
    'tx': 'tx$2WsEQsiC5XsmkQF6BS1aUhB55XkktxRJi2ZWbpCbGVHgQNPQzUeaEJk57RrhWBagGqNUyUA9YY6PrZhTiXcYs6dK1BxASu8EummTYvfpTjfnA8hU21pw6Ms9fWbJbhBbLNai4hLGPEJZ12r1UHqxLTnq6nJ69vw6szeisRzVJ3XYNpvGgSR5dVyW7Yd2VvtW5CGEMCXCHVYquD8gt6RMBDDr1Q6LeLUTomBpgFGQknjKv56tLtZ2FHkWWa9mU22jXMS'
  }
}
```

#### Finish withdrawal
After both the parties had signed the withdraw transaction, the transaction is posted on-chain and
both parties receive it:
```
{'action': 'on_chain_tx',
 'payload': {'tx': 'tx$3cDMp6242sByJUzkqj5qREcZdMg99K3hYXtj8LTJrYvFEcd2FUa4CNfUzhnUQDkzaeeexK1ejuYPMJDD5bwjuGibBYLE1AYPPncdzwe9dHhATA2ftRgouyUxztZoQKQ1jNCDUpgkWcYPiBBRfSUJhoGGLzTfMHrfU5UiiMkcCkv6CmSWEm8JsiGAciJFJzzsRQyCJTZ6a6JM7ztBikcs9sQsG6crEdfnMwjG3zEowFT4wpaYZAxH849Y7m3c3pQkkABtcAkXznZEmtS89H9GWaecxKWkaAipz6WvCKAu33haGb4SM3apigLUYZc6xa2KyTJ8CutCKYWP8Jacua6z8B4hg4qM4'
            }
}
```
They are both to compute the transaction hash. Using it,
participants can track its progress on the chain: entering the mempool, block
inclusion and a number of confirmations.

After the `minimum_depth` block confirmations each participant is informed
for the withdraw progress on-chain by one's own node:
```
{'action': 'info',
 'payload': {'event': 'own_withdraw_locked'}
 }
```
An update from one's own node that the other party had confirmed that the block
height needed is reached:
```
{'action': 'info',
 'payload': {'event': 'withdraw_locked'}
 }
```
With this the withdrawal sequence is complete and the channel can continue with
other updates. Note that the withdraw transaction's `round` and `state_hash`
are the ones considered latest from the channel's perspective. For example the
next correct off-chain update/deposit/withdrawal shall have a withdraw
transaction's `round` plus one.

### Solo closing sequence
At any moment in time after the channel had been opened any participant can
initiate a solo closing. The mutual closing takes just one block
inclusion for the effects to take place. The solo closing sequence requires a
couple of blocks and at least 2 transaction fees to be paid. This makes the
solo closing sequence both slower and more expensive. It is intended to be
used when the other party is trying to cheat or is not responding for a while.
This is called a dispute and it is taken to the chain to resolve it. Dispute
resolution has the following steps:

1. single `channel_solo_close` transaction
2. zero or a couple of `channel_slash` transactions
3. single `channel_settle` transaction

The second step is not required and a `channel_solo_close` could be followed
either by zero, one or more `channel_slash` transactions, each subsequent one 
presenting a newer state and overwriting the previous one. Those are settled by
a `channel_settle` transaction that finally closes the channel. Let's discuss
those in detail.

#### Payload and proof of inclusion
The idea behind `channel_solo_close` and `channel_settle` is for parties to
provide, on-chain, the latest channel internal state so that the channel can be closed.
First comes the `channel_solo_close` that provides some off-chain state. Then a
`channel_slash` can be posted but it is checked that it has a newer state than the
`channel_solo_close` one. Then parties can post more `channel_slash` transactions
but those are always checked to be containing a newer channel state than the last
received on-chain. If one party tries to cheat by posting some old state - the other
party can present to the chain a newer channel state and this overwrites the previous
posted one. Thus the comparison on channel states is important. This is done
by comparing rounds.

Both `channel_solo_close` and `channel_slash` contain a `payload` field. This
is either a binary containing a `channel_offchain` transaction or an empty
binary.

If it is a `channel_offchain` transaction - it must be co-signed by both
participants. It also contains a `channel_id`, `round` and `state_hash`.
The `channel_id` in combination with the correct singatures verifies that
this off-chain transaction indeed is part of the channel off-chain state. The
`round` represents the height of the channel's state at the time the
transaction was co-signed by the parties. The higher the round, the newer the
transaction is. This `round` must be greater than the last on-chain one for that channel.
The `state_hash` is the internal channel state tree root hash
at that `round` height.

If the transaction's `payload` is empty - then the latest on-chain state for
this channel is used. Both `channel_deposit` and `channel_withdraw`
transactions contain a `round` and a `state_hash` and the latest received one
overwrites the previous one. If there had been none of those, then the
`channel_create` transaction is used: it has a `state_hash` and an implicit
`round = 1`.

Either by having a value in the `payload` or not having one, the
`channel_solo_close` and `channel_slash` provide a channnel's `round` and a `state_hash`.
In order to determine the order of the channel's states received - we compare
the `rounds` and keep the state with the greatest `round`, considered to be
the _newest_ and _latest_ state. They also provide the `state_hash` the
channel's state tree had at this `round`.

Both `channel_solo_close` and `channel_slash` contain a `poi` field. This is
the proof of inclusion for participants' balances in the channel state: all
the insignificant data in the channel's MPT (Matricia Perkel Tree) is replaced
by corresponding hashes.
The root hash of the PoI must be equal to the `state_hash` provided by the `payload`.
This guarantees that the PoI indeed is a proof of inclusion for tree at this height.

#### Solo close on-chain transaction
The `channel_close_solo` transaction is the one that triggers the solo closing
sequence. After it is included on-chain channel enters a _closing_ state and
any subsequent withdrawal or deposits are considered invalid. Preconditions for
the `channel_close_solo` to be valid are:

* channel is opened on-chain
* channel is not in a _closing_ state but not yet closed - no `channel_close_solo` has been
  included in a block yet

Any participant in the channel can post a `channel_close_solo` transaction. In
the scope of this description we will call the one that posts the transaction
_solo closer_.
The transaction has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel to close |
  | from | string | solo closer's public key |
  | payload | binary | closing payload |
  | poi | binary | closing proof of inclusion |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | nonce | integer | solo closer's nonce |

`payload` and `poi` are validated as [described above](#payload-and-proof-of-inclusion)

#### Slash on-chain transaction
After the channel is already in a _closing_ state, both participants can provide
a newer state via the `channel_slash` transaction. Preconditions for
the `channel_slash` to be valid are:

* channel is opened on-chain
* channel is still in a _closing_ state - no `channel_settle` has been
  included in a block yet

Any participant in the channel can post a `channel_slash` transaction. In
the scope of this description we will call the one that posts the transaction
_slasher_.
The transaction has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel to slash |
  | from | string | slasher's public key |
  | payload | binary | slashing payload |
  | poi | binary | slashing proof of inclusion |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | nonce | integer | slasher's nonce |

`payload` and `poi` are validated as [described above](#payload-and-proof-of-inclusion)

#### Settle on-chain transaction
After the `channel_close_solo` and all the `channel_slash` transactions,
it is time to finally close the channel. One of the participants posts a
`channel_settle` transaction that enforces closing of the channel. This
happens according to the latest channel state that was sent on-chain. The
`channel_settle` just finalizes the channel closing with the last received
state, redistributes tokens to participants and closes the channel. No further
disputes are possible after that.


In order to give parties time to slash a closing channel and update its state
with a newer one, there is a timeframe only after which the `channel_settle`
can be posted. This is measured in blocks mined on top of the last received
transaction for that channel (either `channel_close_solo` or `channel_slash`).
The amount itself is prenegotiated before opening the channel and is part of
the `channel_create` transaction - it is the value of `lock_period`. Under no
condition a `channel_settle` can be included in a block before passing the
`lock_period` amount of blocks on top of the last `channel_close_solo` or
`channel_slash` transaction. Every next included `channel_slash` restarts the
timer. It is worth noting that since those transactions must include a `payload`
newer than the prevous on-chain one - this timer can not be postponed
indefinitely. Preconditions for the `channel_settle` to be valid are:

* channel is opened on-chain
* channel is still in a _closing_ state - no other `channel_settle` has been
  included in a block yet
* at least `lock_period` blocks has been mined on top of the last
  `channel_close_solo` or `channel_slash`

Any participant in the channel can post a `channel_settle` transaction. In
the scope of this description we will call the one that posts the transaction
_settler_.
The transaction has the following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel to settle |
  | from | string | settler's public key |
  | initiator_amount | integer | initiator final amount |
  | responder_amount | integer | responder final amount |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | nonce | integer | settler's nonce |

The amounts are the exact amounts stored in the channel object on-chain.
