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
  * [Transfer](#transfer)
  * [Create a contract](#create-a-contract)
  * [Call a contract](#call-a-contract)
3. [Channel mutual close](#channel-mutual-close)

There are a some WebSocket events that can occur while the connection is open
but are not necessarily part of the channel's life cycle.

* [Update error](#update-error)

* [Update conflict](#update-conflict)

* [Generic messages](#generic-messages)

* [Deposit](#deposit-events)

* [Withdrawal](#withdraw-events)

* [Getting state](#getting-state)

  * [Balances](#get-balances)

  * [Proof of inclusion](#get-proof-of-inclusion)

  * [Contract call](#get-contract-call)

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
  | initiator | ak$4Kr76woCtc3ehZ45K1sCrmgKX6gnh7qGhjSU1GZYqfLTTjtCgn |
  | responder | ak$35Wxqf2cbzQF5hEV1j9AdXQFTMxqKCwM7iMKNGcqSv47MXAj68 |
  | lock_period | 10 |
  | push_amount | 3 |
  | initiator_amount | 10 |
  | responder_amount | 10 |
  | channel_reserve | 2 |
  | ttl | 1000 |

  The `initiator` will be connecting to the `responder` on localhost:1234
  We will be using the tool [wscat](https://github.com/websockets/wscat)
  We assume the channel's WebSocket listener is set on port 3014 (default one)

### Initiator WebSocket open
Using the set of prenegotiated parameters the initiator connects
```
$ wscat --connect
'localhost:3014/channel?initiator=ak$4Kr76woCtc3ehZ45K1sCrmgKX6gnh7qGhjSU1GZYqfLTTjtCgn&responder=ak$35Wxqf2cbzQF5hEV1j9AdXQFTMxqKCwM7iMKNGcqSv47MXAj68&lock_period=10&push_amount=3&initiator_amount=10&responder_amount=10&channel_reserve=2&ttl=1000&host=localhost&port=1234&role=initiator'

connected (press CTRL+C to quit)
```

Note the `role=initiator` as it is specific

### Responder WebSocket open
Using the set of prenegotiated parameters the responder connects
```
$ wscat --connect
'localhost:3014/channel?initiator=ak$4Kr76woCtc3ehZ45K1sCrmgKX6gnh7qGhjSU1GZYqfLTTjtCgn&responder=ak$35Wxqf2cbzQF5hEV1j9AdXQFTMxqKCwM7iMKNGcqSv47MXAj68&lock_period=10&push_amount=3&initiator_amount=10&responder_amount=10&channel_reserve=2&ttl=1000&port=1234&role=responder'

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
 'tag': 'initiator_signed',
 'payload': {'tx': 'tx$6GDUCeNUH5DYb7RB6Aa9WNHwPzjj8jWwp1rt9iyimoJvpKe7NeCAcWryYY965s6Y8F7FxHyYffSxE5VhLPdm1gWiJFCG3Qd2FuZzs9vi4zhmY5MvHQpWrtuPdMd71YCu8kL5VNGkCQVPBLHWddCeuFRyknZPR3b'}
 }
```
Initiator is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'initiator_signed',
 'payload': {'tx': 'tx$7gq4gp1GGiqdJ1qEZv5h4UiUdaPS4BtwyR1FitViBERzHjntzwCUWLgVM6khGeLuYMehyhbPuqYD6HwR5r1bQb9BTKt3WcaGgBQhUx8CFdjTA2QPhZnGrE5k8uuturu7uaeRLXeyUQJMyoSf5xZzD3DrzomkUJuYb1r3E6pHvNxjUbq2Qo4xoDYp6kjBo5nzNdAEnwk8iwn1opLjFRDX519nPAfEujqsTrkjCScu2FjaUwqkvSnVA8JT8v4FumsdP5ua'}
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
 'tag': 'responder_signed',
 'payload': {'tx': 'tx$6GDUCeNUH5DYb7RB6Aa9WNHwPzjj8jWwp1rt9iyimoJvpKe7NeCAcWryYY965s6Y8F7FxHyYffSxE5VhLPdm1gWiJFCG3Qd2FuZzs9vi4zhmY5MvHQpWrtuPdMd71YCu8kL5VNGkCQVPBLHWddCeuFRyknZPR3b'}
 }
```
Note that this is the same transaction. Responder is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'responder_signed',
 'payload': {'tx': 'tx$6GDUCeNUH5DYb7RB6Aa9WNHwPzjj8jWwp1rt9iyimoJvpKe7NeCAcWryYY965s6Y8F7FxHyYffSxE5VhLPdm1gWiJFCG3Qd2FuZzs9vi4zhmY5MvHQpWrtuPdMd71YCu8kL5VNGkCQVPBLHWddCeuFRyknZPR3b'}
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
 'payload': {'tx': 'tx$9mmqY8QRoYS8QR5nyRkWwTyhwecE8NzHotRK1yMjvfvyPfsaBNwWFDrmzG3M5rHKARm39AqeJpgN4Aj7V57yP4KusptAvMA2r3y593vr51ubXN8zo8t8qg7Arb32wWhmYDvRXVGKhfYoqu91BpkammeY69xCjGuQrXKDk3t9aPCcrvM3PbERAMvkmvD9dsb2H5iujGin8qZTy42xsUYS6QcTiaomxo8CmieGSvZkAai1KCZ84MZzsAjsR1FP54Su7rfBPXZTd5u2AmyF7LwZoHQsJEspLnzXxun2MtKTkhR3du8PY'
            }
}
```
Using its hash, participants can track its progress on the chain: entering the mempool, block inclusion and a number of confirmations.

#### Transaction in mempool
At this point both parties had received the co-signed the `channel_create_tx` transaction. The transaction is posted by the state
channel's software to the node and goes to the mempool. Having calculated its hash, one can validate it using the external HTTP API:
```
$ curl 'http://localhost:3013/v2/tx/th$hNyHzj4dSzyBqReAMR36GGz1mhuXxQFuES3AnPkXkuY2w6dZb?tx_encoding=json'
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
broadcasted only between parties in the channel. The state is a full state
tree that holds all the latest accounts, contracts and contract calls.
A state is considered to be valid only if both parties have agreed upon it.
Agreement it proven with signing a message that contains the channel id, round
and root of the state tree (state_hash). States are ordered by their round - the greater the round,
the newer the state. The latest channel state is the last valid state, having
the greatest round. At any time the latest state can be used for unilaterally closing the channel.

### Channel state
There are a couple of different types that could define the channel state.
Those are deposit, withdrawal and off-chain transactions. They all containt at
least the following data:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | channel id | string | ID of the channel|
  | state_hash | string | root of the state tree |
  | round | integer | current round |

You can find further information for them as it follows:

* [deposit transaction](../../serializations.md#channel-deposit-transaction)
* [withdrawal transaction](../../serializations.md#channel-withdraw-transaction)
* [off-chain transaction](../../serializations.md#channel-off-chain-transaction)

Each subsequent state has a `round` increased with 1

Since both participants are peers, they can both trigger new updates to the
state.
Since one of them starts the update and the other acknowledges is below we are
going to use `starter` and `acknowledger`. Both the initiator and the
responder can take either of the roles.

### Transfer
The transfer update is moving tokens from one channel account to another. The update is a change to be applied on top of the latest state. It has the
following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | from | string | sender's public key |
  | to | string | receiver's public key |
  | amount | integer | the amount given |

Sender and receiver are the channel parties. Both the initiator and responder
can take those roles. Any public key outside of the channel is considered invalid.

#### Start transfer update
##### Trigger a transfer update
The starter sends a message containing the desired change
```
{'action': 'update',
 'tag': 'new',
 'payload': {
    'from': 'ak$3YGRJv1QMgNbeDzvqX7qJrZWJDaHGmrHYHifxSbhSEgn6anuNYCNPrzsB911xTbZ35bvJYWLyYjrQaQKfvja9gkpvYMfEZ',
    'to': 'ak$3gVuduh7vR9G7Hq3TpFaA7q9oQkMZZF2VsUxDYZabNeKC1uaqtjpKSth7wPn9dxnUzsHoT2fa6GPUzepbDXMHyC2F3HupT',
    'amount': 2
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
    'tx': 'tx$21uV5so71tzLyBzTGBd5qd318n8Z33ninWoJzuBBKa3y3cLv8jL1gBsUpwoT1Wzs57fpxgxk7asMpuxcKpYxRnH1Qk679DjPUjLx3Lu6eNnPnfDwb4NpMq5tmm1Sq1j4MLfi6mFLadQ4CyuiENcytACQgkiU2CP8jWHKDCxAprKxP7EnXRKGbyaXkQRjvxmd5BK5XpnPHMoLb4zrrQfex5Wi8SkJjxWrhRyTr7u8jqyyebVPYmz3iRnnoEHfiECzBLdAYBz12U4VgUNrYug8C3ns5GcB1ytaUmggpDGY4K97dyYR8aMorFfqY6rPjwpRoL1BjbJgUBw54VVgMEijfeVCNcyw8wrVJnZeUAQKSesJcPhWShY717GVeQfGGHLzJhTY7iYBUUQCLfoVms86jJ3vMo1d9DpnahpCXfrZeR2PExg8Cn9DXc'}
}
```
The starter is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'update',
 'payload': {
    'tx': 'tx$xCHADUvUikbjGRcBmioKtXFQKpGs7yZHvhkcjByxQDG5xnCpU6YVQs4qyBZL6h18xjTSy1wtUFe8ipKMHLp6VmU2KwLgd4mbUtqELz6w9wV6PGTex6ZS2y7TtqZsDuesGFTZqYET8syCor8kzGjemUkzvwHMJdKsQ5guDWj1C2EcuNR3MnK9heJLbKuf19peGDvijjS8zdCD1pxE4QcsVi9pAGUBCgFyKx8FkDzhv6LxjysuxdmuZqeTGq49s71QdVB74Y1DAQUq5JsH1kyhadFxVepS6FYmcBC4xK8h1sefipPAAVFY7YwNtj2W6U9CTCqSVAQSrpfGAo6322gSneD8aRKoGpQpy1NfxVePKqM5igmd1B6QDGcEYDigBzzNwrXpuYqjrdG5eB6C6ehwAxNskmiudbEuKrjwNL5JzExxrR21L5oQCDc3RMyPdeWJxs8eJfHCrWyzyAwsykV4hVGxddbsbrDWd3re42N5HARXpQG6Gq6aMGnSHJAKbXCWxys4Si6Wjpey7HyEgT1hYoxqtmwEGhW96Ksig'
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
    'tx': 'tx$21uV5so71tzLyBzTGBd5qd318n8Z33ninWoJzuBBKa3y3cLv8jL1gBsUpwoT1Wzs57fpxgxk7asMpuxcKpYxRnH1Qk679DjPUjLx3Lu6eNnPnfDwb4NpMq5tmm1Sq1j4MLfi6mFLadQ4CyuiENcytACQgkiU2CP8jWHKDCxAprKxP7EnXRKGbyaXkQRjvxmd5BK5XpnPHMoLb4zrrQfex5Wi8SkJjxWrhRyTr7u8jqyyebVPYmz3iRnnoEHfiECzBLdAYBz12U4VgUNrYug8C3ns5GcB1ytaUmggpDGY4K97dyYR8aMorFfqY6rPjwpRoL1BjbJgUBw54VVgMEijfeVCNcyw8wrVJnZeUAQKSesJcPhWShY717GVeQfGGHLzJhTY7iYBUUQCLfoVms86jJ3vMo1d9DpnahpCXfrZeR2PExg8Cn9DXc'
    }
}
```
Note that this is the same transaction as the one that the starter had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'update_ack',
 'payload': {
    'tx': 'tx$xCHADUvUikbjGRcBmj4YQkTJGCoGV6JQVdJW2FU1ZAYGhdayeCZerGqPWbRz4Eduq1KtjUbBJgdxSF3UKyChKMXne3dEDnChRdiUop4HYkHJ8GF3xQpbSspvST5qPTJqvcCstQCDXmJMLiYiWQ2hoPXL3a1qiiVmSwx2ztVuVqsEf1NsQCbMiNeJj8Uvrcp2FKN8TG2VoMTBTiMcCdLGXhX31EaLYTTDVyFTXGgFRUTdAsHgBjcQzm9hgQS75QjhKY7VtyUBCisUEQp8Dcr76rpdT1Qy9n8JYKboPkFZpY9DVx9We2hstbP3fjgZVLgDRAvLoC5YppVE7GZgUbRp6PMmbPUyc3qFYaxA82g7TzndipqnrKuuGzDjoPaM2w5evx1TvXAF5u1beac2kW7kJyKjLfLhjKQ8bnwBwcZ3WpdRfCVe55LtPwYEoZQJtdzojjVcuLmgJjbb2GDHioi8KXTasHre5oZKwkyYByMqzDafVTMT3kJqvdQG6HKAm8XGP6LGRsZFcpkn5jGtGbq7PRpTbAn1RbHWvRAEH'
  }
}
```
#### Finish update
After both the parties have signed the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
co-signed off-chain update so the participants can persist it locally.
```
{'action': 'update',
 'payload': {
		'state': 'tx$3XPhV5wAjiGDkUqu4PWDEXdXEztp6iG1VYDCKU7U46Rgpk79c3cB1ZTnsYSYYyadgA5mU4ww2hzJePnu355nTZnGJTxYeGUS8ct8Zwgf6DTYxW8uKuwDbqtyX4xzPxVbPyhweeNM5s7nqqEojhg4tiwW9hXnrvvj9YyJqK8r77K5ZVoSHN7kg6TowztWjGqhGfeMVnRzkgyNWJvNgUCaUbHi9U2dgL4cX78XbhAiqPdn7emCsF4JhPJumXyMr54oToU6fb4QpmYiWXku3TVymK9vgz49FS53PYebtSZzrhTkgMM9mF7VguJ2Jfx9s2VCdhFeEMj58E2jFL4VfFeUnvc6xUD4jHdfspojDqa6hjWTSQ4bwguC5ZPLDWsnTArFTWYpQi7S9H2coebFNdCLb'}
 }
```
After that a new state updated can be triggered.

### Create a contract
The create contract update is creating a contract inside the channel's internal state tree. The update is a change to be applied on top of the latest state. It has the
following structure:

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | vm_version | integer | version of the AEVM |
  | deposit | integer | initial amount the owner of the contract commits to it |
  | code | string | hex encoded compiled AEVM byte code |
  | call_data | string | hex encoded compiled AEVM call data for the code |

That would create a contract with the poster being the `owner` of it. Poster
commits initially a `deposit` amount of tokens to the new contract.

#### Start create contract update
##### Trigger a create contract update
The owner sends a message containing the desired change
```
{'action': 'update',
 'tag': 'new_contract',
 'payload' :{
    'code' : '0x36600060203762000062620000366020518080805180516004146200007d57505b5080518051600414620000db57505b5060011951005b805903906000518059600081529081818162000058915b805081590391505090565b8352505060005250f35b8059039060008052f35b5990565b50806200012c9080905090565b602001517f696e69740000000000000000000000000000000000000000000000000000000014620000ae5762000020565b5050829150620000bd6200006c565b596000815290818181620000d1916200004d565b835250505b905090565b602001517f6d61696e00000000000000000000000000000000000000000000000000000000146200010c576200002f565b602001515159506000516200007090805180826200017691600091505090565b59600081529081818162000141918091505090565b835250509050620000d6565b825180599081525060208401602084038393509350935050600082136200014d57809250505090565b915050806000525959905090509056',
    'call_data': '0x0000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000004696e69740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e0',
    'deposit': 10,
    'vm_version': 1}
}
```
##### Owner signs updated state
The owner receives a message containing the updated channel state as an
off-chain transaction

```
{'action': 'sign',
 'tag': 'update',
 'payload' {
    'tx': 'tx$JgoYCDwwyZGhYZcpejLVGEP2us4MVhHom43vJBRf5mfthGBErZrcPgBDCExqbZoX98TpqyutbUxs1ZhyJMEmXJrAzTivT17BHP8km5Zmsf6wBNk9kw6hKvn2gsHtb5ktHRLKu7oCiwsG2ro6VePKZCKV1Fo51d4bVkPEZmKkNqrrzuN6mHn88rYT3esKH848edtP9CMpyDDiV8DvsMsYmw5ZEzpUwKxf9UrEYPkfNzxm9Fax9tQscio8tGgTJh6xS6xEs8hH2R38kM9xjNBnhgwSS1VAk2jNT2VZz4NpRjYe2n9HabNo2SyYd5kPK3voVEV896GG8htzFCpytBptUZUmWrt3b8zfWtAkwboZRjzEF3AXBn7jpBcBgu9zFhpT6iwTAL5ACQcKNEu7bzJV4MBpNjEn7DXKBnBHXqDyk2URQenfXNnyJg9Aw1Mx1V5h5nmUYqi363u775f978MXaqoTyjBWSUZq14ZJ8H9GcAMBGiZTp3Rxa7fAvMUcCGwt34WCVEe4TWu9HcyKrMUebtpM5P5aMdQS3jVUaz26zMaJiCjjngx14zjrfSV1Wnfh5ESr7s4dyRXTHnG5tZFCFSAguEKTrZiZP2yTP7r1cNfJ15PoGHXCLLCNNoTAYDghAon8MhwcGBJhoqQ5gaAdYBwjKU92mJqBwU11KruxVkj2D1JYGgUyt1SJHo7tzeSHXX6N7RxKeHez9ST9qWSUEog1QF64RhJstdnBYcR6njscN7wh8GY4o6w2h6dauh5wzrCUvYc4B3reh4To9LgmL6hbHsXBMXbeCXCjVhZv24D7GZXZB68RTzxBy5SuJysEDZYSUSErStSHoqZbwzXaLieXsiMrhppyWDSNJAduJr7UrMuH2nWz5vPae714uwQKKGkEvakh3ZAC1nqZ1KrD6Jo59fyP6mPGYEpvpkte7WRtdHypRsiCus7nisFVzUg3p7hB6LdQYMoBAJ'}
}
```

The owner is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:

```
{'action': 'update',
 'payload': {
    'tx': 'tx$8YK7n5J3XLNE1t6pvhTLvFPWcoZyers5MonYRCYm6ahvRPpuBeF2kQML9D9AYjMAsPVbqjLajCMyAYV1irNBd5MLzcBugVRRHBW1kAPNvYUpQX4b5NBovAzZh3ULQ22hYfAXSJ9tXmmqteDG3eaQjFGQj1p1cUs29wqeXmMwRouxofovtprfnyTgEUqmvRn5TyxSECQTVoNgGvU7ERxEETynaL2AAxqMU67BLC5r4KY2SMRTX4aaJmeyC7spxDTfFM11w2fbVCgDusgdDhQiUSKR2cRT16EYkHM1bTPSJXhzBkN7ASRXCkBP9XqX8p9bri1U7bcvCTJNwojLUQxhzbwdUMhfMXtR63m1QV7bmpYJaSiAx5Xt4P31Yb6ZYAkKNrG4GXSsufioUvVHqBGKPTvbng1H1vHt871Afc4jUhPfzBhQ1Tz1brxMAc8rsSYFzTyn6z6EZsBGvZqXVFVUzkSv4BjaVm2d1iN8PyJwsQkeAuNHgMzKyvNVC2t1i2kZxCqCuPZcAiKQGqvPco3WPYvDWcxAdgfKvu4hTPAvxvef4zskmdbgNGtfR6BJV6SC1qDCrxF14BUMKF2ayJRhNL67Cm2HZPQ7TBbcTF3gHHTmmQdYzvKeu9xNzUoZsR5P5WaEirYmGdsi3rcWkpnoTmiKkMSyxDDZVh5Km9r9Mks33YHVnKpkWfpVq81xac2GNYyyjaFFuZjEggpgmZwWHmvVkkaFBAFdcWLqYrE8xTVFsXKth3ppopnuZD3TuYDmFTGkB46FPKF3suireqA2hPyZTnfEWsYNH177UDKFprpR8Cz7kvwz6pBHo7A9qMmDjN7N4GwBXspxyjddJRAvtPgtJsTDRrFKFzmtF3Nfm789gp2FYxV6S6FjYHfR2cWLJhnCvCBbDECiEtfJh2Pn4enLmPumZQfsnV8BgXz1hMDtXcMf6NzhP3kJEh2NebZpVidi64A1xAvRu9zxJkoWFhVN7eUDQhYFmGE1Avt9PY2xPEiuCMzgcp6zNrv5mWgf4AsrQM9T3gWhD52yU7SFw3KV4QMjHRJLFaJuXgFMGSaohpwzUu669p'
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
    'tx': 'tx$JgoYCDwwyZGhYZcpejLVGEP2us4MVhHom43vJBRf5mfthGBErZrcPgBDCExqbZoX98TpqyutbUxs1ZhyJMEmXJrAzTivT17BHP8km5Zmsf6wBNk9kw6hKvn2gsHtb5ktHRLKu7oCiwsG2ro6VePKZCKV1Fo51d4bVkPEZmKkNqrrzuN6mHn88rYT3esKH848edtP9CMpyDDiV8DvsMsYmw5ZEzpUwKxf9UrEYPkfNzxm9Fax9tQscio8tGgTJh6xS6xEs8hH2R38kM9xjNBnhgwSS1VAk2jNT2VZz4NpRjYe2n9HabNo2SyYd5kPK3voVEV896GG8htzFCpytBptUZUmWrt3b8zfWtAkwboZRjzEF3AXBn7jpBcBgu9zFhpT6iwTAL5ACQcKNEu7bzJV4MBpNjEn7DXKBnBHXqDyk2URQenfXNnyJg9Aw1Mx1V5h5nmUYqi363u775f978MXaqoTyjBWSUZq14ZJ8H9GcAMBGiZTp3Rxa7fAvMUcCGwt34WCVEe4TWu9HcyKrMUebtpM5P5aMdQS3jVUaz26zMaJiCjjngx14zjrfSV1Wnfh5ESr7s4dyRXTHnG5tZFCFSAguEKTrZiZP2yTP7r1cNfJ15PoGHXCLLCNNoTAYDghAon8MhwcGBJhoqQ5gaAdYBwjKU92mJqBwU11KruxVkj2D1JYGgUyt1SJHo7tzeSHXX6N7RxKeHez9ST9qWSUEog1QF64RhJstdnBYcR6njscN7wh8GY4o6w2h6dauh5wzrCUvYc4B3reh4To9LgmL6hbHsXBMXbeCXCjVhZv24D7GZXZB68RTzxBy5SuJysEDZYSUSErStSHoqZbwzXaLieXsiMrhppyWDSNJAduJr7UrMuH2nWz5vPae714uwQKKGkEvakh3ZAC1nqZ1KrD6Jo59fyP6mPGYEpvpkte7WRtdHypRsiCus7nisFVzUg3p7hB6LdQYMoBAJ'}
    }
}
```
Note that this is the same transaction as the one that the owner had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'update_ack',
 'payload': {
    'tx': 'tx$8YK7n5J3XLNE1EoLatcNhJSoTnv2zUqxS6N3iVgqiBc4bjnTyoarR2qYZa5oJX4td78HnuHddPqe47DbbtWmY5SiK2rAurz59V49Pie5z1i7bPZzGa1QXo5obJG4kX64hVhHD2Wcz54vdfKFjEtQv4muUHjXfxav9LNja6rvRbUiASepmVa2B3ykbBVjhivkszNqubEwQ6NKiTC7G5NJnvFq5YFzDxWjrJfDmHsuz8TGETdYYHk6oQPhnudfQ4pXyp4zvzC2RG9KKLTWG2YkgL4w6QGFoHM6zFFw1NAR7vfGucBnSdf6Mb7Vwt2qBcm3CkHrP3ShvksQsE6GTuaniBGF3bE1xc3psBDa6rXKUiTpAx9W4W7N2Pe9qWmZMcfsG4iwMMvaAvkshW6usmTHFL8xcsmq5hd8VRDNQajoT5XaLhwnt3erfUYcZcAkHwvPjsrGya6L8rxa5d5yibPjZPYdmZiuD6XNabSKnt66b2d4b8S1QjVFkjUvibMAMWGngfFPGgs2uoiCsZ4bHsrgHTSvrDvN9v1vn7hMRvyvcVboBgv5uqtau3jDe3fybZZNDfY1hbxABTZeqNZ5BSE2mdGxftqQew1XCFwKyJZCz3CTPm3Wf9ab3U28GuLm4Bf74N7MzHr91qzhNAzcv7fKGru2JHxho6Hfhj16Fr2ME1XxQYmMo8neo65dtYY1cV5qcg94qVaTkTFAtCvjbWat36pubFG82EgbPf7Ptcfv1wPR6VZeikYzmW2j1DQvebs2EQv6qqwCXByqM4NMcZenvLwCkkK6vnaX4Jzpqpdvu5iEatso2wqdgE7f9iZrv5u86vw6vsej7sVVRUjiVpLYeJfEqXP9Zirm2p2qPGaSD9zXvnGS5uz3dxUH4pnkRmwoB8cXbPYvfLagmNYQXXzbxhi1BfSYbtGq7dfXLrZuzdxwGpLbv5HwPQKKtKUaeUpYTQ2XPBtga16sTuSbDw7xmBY76ywBHjnPt6n9RqoUT1WWj3jkGPvtKKkiWThiG9jzQP9P8mBCS22w2QLm6EwPuJ6sVTkr7nMWAaVcgY1qKJbUmneFi4x8fr'
  }
}
```
#### Finish update
After both the parties have signed the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
co-signed off-chain update so the participants can persist it locally.
```
{'action': 'update',
 'payload': {
    'state': 'tx$DxpMPQqimD6NuzKT6SWXsnQY3c9hVxqughSXAkRZJQzCbUDM8HazSos6Xqkpw2ndfRu8NQwDLbU4SsLKb7xasMShPYRfW9oe55pEdXLZi9ZMa4nMKzSN45sxsupiJ815VnNNKTwqH8G8yU1snTKCUz4Sed2xUAjx5KADR5eEbNfDUMhseczXyYZ6tj9ahYVnjqdxqgBuLmrEXq8LMirPzNAfzKaz55NaLMxXkMCpRdxy9mBXLpwcvRM8DxzBbK7n28r3GKk99x9fwgP5Tv2psyyAEMgxhFznXVTvVnSZY1zT8eKc5LJEL6LKBxSkXJXdTqeZWmjeRZruEqcmygFD4Tvpr6LpSyXStoL9tV4B4nyYuJdpESNd35H6eL57MSKrpSpGSnnhgefJ4pqXmEut9XcKT1TsXR1BbTvDDYnBAgZhxvwq1NB9CQy2pibnz1G5XHJVu6QmSj5yQUxRYtsksbAkXL5xhiSZ6DWwynqVKiSThwvU9wHYDFJuWLYKrUCJuA1zu4fmfvhsuL2FSMW2wft1ELm53UpkrPRq68nGeegYMYuMCpoGUruvDCwVPwhP8DKq1cSrhRSxn6HzMCDa7zBQKrmKnksQbdeWWxSgVEosxtvdLtNZ6tDYPJe4q78a5PkyGVDdiAkYYo1CmRt46wYoMvYQPiG6vpt3fTK2oambanFSdXjtK4MBXZxpUKA4bhwTFjiFadCkkGAgkGkaHP6ztnYQP11YGP4huyfZH6WoYXwmWVXahipTAoQFpTPQTp9wLy3QS2o8iY7wT1SSweYNuzgwh31LFfcbs8pXNuJ5NFqUR5ygRQQcaVcq2D6dv35YSNi7pfzpgLk1WGdwbPfTpAssNCwETda6r1k6zwWmn3nqL8hsy381KyrQPRkHbeaYG2msZd61QEZFm1CHkbx5xMp17jiTMJ2gZwVx6SpSGCxLogpWBxxcTPfUKphW5bVUYn5aoxZsgBcg5MrExouV6fk82GYoAsZ4yR1F6J3onJkBejMvd6XXSPYAx2dS22VGJhjQpzy6woBgwiVCV3kCSfnoaru6NzkkjVfW7THTvWz2dLbMoToFnPLnaypEjfh1heF2Ypr8QmV3XLrzwHQ7G8ZPFLRDm2jL5Zp6rnZLErD9wbyiiRGda7mQqg1wR1FznsJ3XXatpJmn'}
 }
```
After that a new state updated can be triggered.

#### Contract address computation
The created contract is part of the state tree. It has its own balance and its
place in the contracts subtree of the channel's state tree. In order to
inspect its balance or call the contract one needs its address.

Computation of this address is done exactly as it is in on-chain contracts -
it is a hashed version of the channel's owner pubkey and the nonce. Only
difference is that nonce is not computated in channels and the update round is
used instead.

### Call a contract
The call contract update is calling a preexisting contract inside the channel's internal state tree. The update is a change to be applied on top of the latest state. It has the
following structure.

  | Name | Type | Description |
  | ---- | ---- | ----------- |
  | contract | string | address of the contract to call |
  | vm_version | integer | version of the AEVM |
  | amount | integer | amount the caller of the contract commits to it |
  | call_data | string | hex encoded compiled AEVM call data for the code |

That would call a contract with the poster being the `caller` of it. Poster
commits an `amount` amount of tokens to the contract.

The call would also create a `call` object inside the channel state tree. It contains the result of the contract call.

#### Start call a contract update
##### Trigger a contract call update
The caller sends a message containing the desired change
```
{'action': 'update',
 'tag': 'call_contract',
 'payload' :{
			'contract': 'ct$9sRA9AVE4BYTAkh5RNfJYmwQe1NZ4MErasQLXZkFWG43TPBqa',
			'vm_version': 1,
			'amount': 0,
			'call_data': '0x0000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000046d61696e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002a'
		},
}

```

##### Caller signs updated state
The caller receives a message containing the updated channel state as an
off-chain transaction

```
{'action': 'sign',
 'tag': 'update',
 'payload' {
    'tx': 'tx$Sweh544j3PL6BzGK8Sk6dqW9ywspMup8J8ETuajNnTGkx3vTbwCS8K8LWAPNSBrkDUWEQCxDR2Kyvuv2v19YtsiNxcetmwWwEjYicTaZ1nZ84PvVs5WoP4LgSgur5yaiDwvoY4xkk5dGjfiXGYWE7udn8HwbZdHUQPXWtJdeGhcApf31SPYWUkW3hWk8sKZeHKU6f9aLQgiSsP2MNoqzfiTL1xppK4NPrS6gje7iVGdz8zBbQ1TRXcTsN7pecY8fSPMwKhEtH88jRbmXouYxatBUvYLy4vRiQJBcsZaCXhHKezoXqggPsPDUjfaM1P1FMrC3GxWS3CHotuR588TuvaUwPBVjwwoMYL1MJcTYLvejnDktsisFtfhH811h7R7pazQuhqbmMSWhRkYMLfXXwTXs32q334CMEZpz1UpWWA1DRJMBUVWmE7FmPedZDaqobUbNe2CKPk8oMG9apvdrrxE6cQRGupVyjXNor'}
}
```

The caller is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:

```
{'action': 'update',
 'payload': {
    'tx': 'tx$C4TACwXiGbsZf6sCqqEkZU7ngzvoDdqPHQMfNVGZUMQhsT9Nj64j3DbGYE6nB8V7R56zmfY8zuGCjAWgZecsby4RCwDtm5nE57DcX3srHgrzt4NS1mFUq9Vuan57SXT8n4xA5BFjz8WvKEqFptsHqzRhv6veY5o9cmTi4ea1t21BaCdfZiVg6mkf4pvrAzsNtnQ149BxuCLqLJJdaJXVWzJthDXBHLcHmDRTvqYRpnH8gD2veHizbJqnvApeVGwMJ9m5rZc3Tw3EDcZnsiFzKXBiZ1FMMBqZtiNzCCRhhn7uANkJiSi8e8iHcBJLyFRPzSgU6KTVNVGcc2CZVh2RQcMoJXWecdHHeMiCnGaX2MiT2EyjEox9a7kZBkTAAnoeri5F2GhGvdK98a275PjaCrA16xizH2DnvRdw92HFA2PgjQmHE3SgxB7MMhTAkaR3LcqmR5KfwLqikneU9DNM5PQzvYTh1J7rupP9AHXUhhFpGQXYcakXQfmEt2D3D4E3zBGDWqJRfVG8xmxYftzefkx5X5CpeWnCyiCepnUSbNyHFxZS4vyzvhZnTHmWVZksyY68MJAMmERk9'
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
    'tx': 'tx$Sweh544j3PL6BzGK8Sk6dqW9ywspMup8J8ETuajNnTGkx3vTbwCS8K8LWAPNSBrkDUWEQCxDR2Kyvuv2v19YtsiNxcetmwWwEjYicTaZ1nZ84PvVs5WoP4LgSgur5yaiDwvoY4xkk5dGjfiXGYWE7udn8HwbZdHUQPXWtJdeGhcApf31SPYWUkW3hWk8sKZeHKU6f9aLQgiSsP2MNoqzfiTL1xppK4NPrS6gje7iVGdz8zBbQ1TRXcTsN7pecY8fSPMwKhEtH88jRbmXouYxatBUvYLy4vRiQJBcsZaCXhHKezoXqggPsPDUjfaM1P1FMrC3GxWS3CHotuR588TuvaUwPBVjwwoMYL1MJcTYLvejnDktsisFtfhH811h7R7pazQuhqbmMSWhRkYMLfXXwTXs32q334CMEZpz1UpWWA1DRJMBUVWmE7FmPedZDaqobUbNe2CKPk8oMG9apvdrrxE6cQRGupVyjXNor'
    }
}
```
Note that this is the same transaction as the one that the caller had already signed. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
```
{'action': 'update_ack',
 'payload': {
    'tx': 'tx$C4TACwXiGbsZg1Z9ChAEuaVJge62Uax5riSw4Tpp763SKTwLLGjhqPDUqjb9swx5X2G6XnpQk72v1yhFSLZvPtUv4JgoimKLqhAVUSoHB3btwEUTdgb3kVbaS6WLiaF86cqBZiDwbiL3GpThgZK7VhYedXFZK6PdK2RjywURhC9s8PNwP19Zetj19VkL4MYn1Z5tkoEh387dMfh9Mfh9jPf7gaBJjvwxNLuMjqHQXwSKPEpR8jYBF4cuzwaZzWeUSPKMxp44wDWQqqG8MTMwR1i8JbZjbAFtuj49TJWMw6xrvXski8XieHLHXrx5y4873CgD1FhRQT374Yvb5mYBTMtsYc8ttUCPiwi7AQteey7h1iRJgGc5bcd2omdGG8BmQZETfLaqwqXWN7mXXxPGfJQUaknHdocTum9FNyncYiAt6Y7znFJ1rZT2UkHvKwbvtJvhftWBJPrbExfeFMypn9DoW4SoaQ7RjBcmz5PWdt79BjRXhZpM7qbjvGF9i1f2cXiQFeKcj9FxXdzttN28kdtDvpYWdBbWcSMaWAYy7EBnMRHrGo2XdcDeJeGQdGnSBKaMHdN5LVhKF'
  }
}
```
#### Finish update
After both the parties have signed the new updated state of the channel - it is
considered the latest one. Corresponding update messages are sent to both
parties to indicate it. The payload of the message contains the latest
co-signed off-chain update so the participants can persist it locally.

```
{'action': 'update',
 'payload': {
    'state': 'tx$L1mTJpyV97nWgMAFmrqcwECSThovgaU9qv5DYeqn3YQgzjCShS96n6u2rACsXyXAJyRrqGNTv2ytC1LgmH8zSuD6SkDTEiT2eCGuCsM1xXyZGooq14nu8naSZ3rhJEwBoZLTn3Tt86W3eUc1rPs2HaFwtxwsFhFu4dXHJTjmaVjigG8Juhvq1oQytscRCPVt9sjijr8h1mCCj73yhnsvwwJuMLi9WgspqwJfHHRVc8RWPtvKg6hbUKxn4cEP2M1rpXhVEUhCAkgKVfm58m4xvnuCNhvJhi37cGeSMSJkdrs64111jnQY2nwpiiS5dRW8c3VcHt1Zm8Sg1fyQgdmgbr3Rwbez1L6hCndppgX1DA2UniQB1y7eqC8nYMe4DUmXxnjcFxCQyaiTCBGavjcZiQUThHzwoACJ1yf4fr1HXZ2BzsgeSsuE2AuvphAvtiPSDmRUiFwxt1KGg3YRBxsSqs2Ums7D6QDoju11VH3k8ERcb9Hj6uJmHFC2yGu48jKHPB8bUCm1qDBZqEiDBVTQo6E1AiSLtvJmLoRd1gyUZ4pvCPPmGPQJ4Qsb16xH6q4YnJVMVQb7TWSs5PorsdqV1XPKg8rZSwSZJGZ1gT7fkf75ocXt986k3PMNCa98cDQmwbqFuqYYC4iMixj6k2txsFYUCyxrucHidNC8MFC'}
 }
```

#### Getting a call result
All calls are stored in the channel state tree. In order to extract one out of
there and inspect it, one shall send a WebSocket event
```
{'action': 'get',
 'tag': 'contract_call',
 'payload': {
    'contract_address': 'ct$9sRA9AVE4BYTAkh5RNfJYmwQe1NZ4MErasQLXZkFWG43TPBqa',
    'caller_address': 'ak$2YeNqB4jQ1DG7QvUKgCkKeZAiXb2rnzkEoLTS8XeKF8Smgit2e',
    'round': 8
		}
}
```
The `contract_address` is the address of the contract that had been called, the `round` is the round of the update and
`caller_address` is the address of the caller.

Then the call is returned through an incoming message:
```
{'action': 'get',
 'tag': 'contract_call',
 'payload': {
      'contract_address': 'ct$9sRA9AVE4BYTAkh5RNfJYmwQe1NZ4MErasQLXZkFWG43TPBqa',
			'caller_address': 'ak$2YeNqB4jQ1DG7QvUKgCkKeZAiXb2rnzkEoLTS8XeKF8Smgit2e',
      'caller_nonce': 8,
      'gas_price': 0,
			'gas_used': 524,
      'height': 8,
      'return_type': 'ok',
      'return_value': '0x000000000000000000000000000000000000000000000000000000000000002A'
		}
}
```

It is worth mentioning that since this is an off-chain transaction the gas price specified is not consumed.
That amount of gas represents the amount of computations. It could be used for
aproximation for the gas needed for executing a contract on-chain if a similar amount of
computations are required. Computation heavy contracts might be just too
expensive to be force progressed on-chain, so please use with caution.


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
  | initiator_amount_final | integer | final amount of tokens to be awarded by the initiator |
  | responder_amount_final | integer | final amount of tokens to be awarded by the responder |
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
Starter is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
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
Note that this is the same transaction. The acknowledger is to decode the transaction, inspect its contents, sign it, encode
it and then post it back via a WebSocket message:
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

### Getting state
At any moment in time any participant can ask one's own FSM for various views of
the latest channel state. This is to help wallet apps but they shall not trust
FSM and compute state locally.

#### Get balances
In order to get the balances as those are part from the channel's state tree, a
participant sends a WebSocket message
```
{'action': 'get',
 'tag': 'balances'
 'payload': {
    'accounts': ['ak$Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
                 'ak$V6an1xhec1xVaAhLuak7QoEbi6t7w5hEtYWp9bMKaJ19i6A9E']
  }
}
```

The `accounts` section of the payload contains a list of addresses to fetch
balances of. Those can be either account balances or a contract ones, encoded
as an account addresses.

A response of this call looks like
```
{'action': 'get',
 'tag': 'balances'
 'payload': [
		{'account': 'ak$Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
     'balance': 700},
    {'account': 'ak$V6an1xhec1xVaAhLuak7QoEbi6t7w5hEtYWp9bMKaJ19i6A9E',
     'balance': 400}
	]
}
```

If a certain account address had not being found in the state tree - it is simply
skipped in the response.

#### Get proof of inclusion
In order to build and use different services, one might need to provide a third party
a minimified view of the internal channel's state.

In order to fetch a proof of inclusion from the latest modified state tree,
a participant sends a WebSocket message
```
{'action': 'get',
 'tag': 'poi'
 'payload': {
    'accounts': ['ak$Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
						  	 'ak$V6an1xhec1xVaAhLuak7QoEbi6t7w5hEtYWp9bMKaJ19i6A9E'],
    'contracts': ['ct$2dCUAWYZdrWfACz3a2faJeKVTVrfDYxCQHCqAt5zM15f3u2UfA']
  }
}
```

The `accounts` section of the payload contains a list of addresses to include in the
proof of inclusion. Almost same goes with the contract addesses listed in `contracts` section:
only difference being that contract's accounts will be automatically be added
to proof of inclusion as well as their state.

A response of this call looks like
```
{'action': 'get',
 'tag': 'balances'
 'payload': {
    'poi': 'pi$g1JxqVQDQdvjvekeM8hEnVeMFUgfF7YYNjjtrvir7q5tAKq2hFVdtvQo7q4p5Aix1S5XNvKabjEwQVvYVezmnq9VWYoJcmctc5mAu6xVj7KgDk3aG5E7topuuLPXEyGP6hAzRPbr2KzQrQ7KZvTdH15bY1WW7D7XGBRmuiDgYiDj8MAVVjqRFnBS5C6GgevgCkUpKX2tyQL7Y3svSNwDiGxV1b3G6xMbhDeStzgtZ9SrsCaLArP1g9wCDJkChEDXneCmMcvEv2acGwsmXHPfT1uy8oSTVny8tbivnnET7XVdjPJZWuvFbwGAmywa4fRF7wkzn4FQjasLo24DRS5fGYg7Z3uwnFbt4U8sn6yg4FvUBUweW28qMjFRAqVJPH6JKU6o8kZjgRjXsC2L7fbhRkYboecoft11FkFuFXdPjsCj3XGXWtTTAXihPooyTpbjp9yszXZqVxLZ7ms7zc6qtPS8Arq8yTf7UmManvhpYKreDMUqPLtkbUTy32LmeRGBUdhhCzUSg49EHtRo5ti8SCrARQt11ScBJnytnok4o3WvmNVq7SRcWPQgH3ABa8g9csirhcZcrx4f2LQoJwQ2VRnkZUUuxDPNEGRwprVWeCU7KfB3CU86z1eHDQWLnodaxLLJnM1fvpdbrjknRcTSTUjPR7rHcsWVmtkNTVqajCZJKUZN2izAAq5qnQUZwkgFLokynCkMGnkV4woi8j4YKusqXUGZ9w5iFfFsSRjw7brqEBySpQa3QayBBmqKu5CF3pTvikRyGhigCDhmyB3QUQ9SQNr2e4r91hoJmfLXN9o1mkW5ndCuVkKoJjSqiscshpZnvUWVKhQZoHEacdZM5z6U42DfqEVDUR6ptokdNpkJtQtuKo1YD1SyhXgvoHh2d2QCpR29wgRkUKswEDru4sFMRaaxk4uL2MpJg3XaAFhxv6WeKeELCGuYRn9yFnhT9pntUkoFWSghcBkk73uN8sYGo9EkDFkV59Gyrra2hm8Dj7iSUUMqJSMApssN8dWzL9HhC5Hb12mFy8ZzAw1jdYmEYXSmjP859A8cKdP6StwwjuhLacfqv7BkFsQX6Rg4w3ykjRPF2Aj2cf4rTMsNnU4bKFmGYc5RPctTx5pj6PchPyX8GgXMf7EfedQNv7rtT8pCLZ199MRCnPy1X3HURAb8PE9Mj8aZz21N8FDU3nT2XraYKE4DBfnwPnqTV6YNcUVk7AYbJ42BZ2AhTwtZzDovZ3FhK6RvjvUtU4MBPcbYFnidFeqNHq3uM1UeWyaHZJwRoQiptojxCPaDLr7gfNb4jUYRihbbczgNgWwbBsahC75rJWUn7C3dSzJYBY5BbRtgAUivU7tQAhE1SCZ79RDsHwo9Md6iFdX1W1YRB3U9b4gi2NN3HfH4dnA7ediYgB1r9eNGh8mw8SYXSruHFLV59LkSRyR9rFeTCUSTt418fNZAftdbqWhd1UceLZhB3QsdKA8UmSKZcjx1q8ZF83m5zDDgJnkkpiqoHRpZ5pzogPWR8HiJpaDUySD1D8yGgMuGbfsxLhrBm9oDqB1QDqKEWgtsBgu5ZYNob7DqY9cwmsfKnssuNofMG3MqpsYe28ZwEAGfVi1wm87QkSNqyCHYUa3yQ7woeR4ZvQwWJPF3GcXKpBhjVuJusE'
	}
}
```

If a certain address of an account or a contract had not being found in the state tree -
the response is an error.

#### Get contract calls
In order to inspect the result value of a contract call, a participant sends a
WebSocket message
```
{'action': 'get',
 'tag': 'contract_call',
 'payload': {'caller': 'ak$Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
						 'contract': 'ct$2qSaJ7pe3MTdPpzS69ZdtQsVTPSoj7yyYL2KJLxKQoAAHJQdjq',
						 'round': 11
	}
}
```
The combination of a `caller`, `contract` and a `round` of execution determines the
contract call. Providing an incorrect set of those results in an error response.

A non-error response of this call looks like this

```
{'action': 'get',
 'tag': 'contract_call',
 'payload': {
		'caller_address': 'ak$Y1NRjHuoc3CGMYMvCmdHSBpJsMDR6Ra2t5zjhRcbtMeXXLpLH',
    'caller_nonce': 11,
    'contract_address': 'ct$2qSaJ7pe3MTdPpzS69ZdtQsVTPSoj7yyYL2KJLxKQoAAHJQdjq',
    'gas_price': 0,
		'gas_used': 561,
    'height': 11,
    'return_type': 'ok',
    'return_value': '0x0000000000000000000000000000000000000000000000000000000000000015'
	}
}
```

It is worth mentioning that the gas is not consumed, because this is an off-chain contract call.
It would be consumed if it were a on-chain one. This could happen if a call with a similar
computations amount is to be forced on-chain.

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
  | initiator_amount_final | integer | initiator final amount |
  | responder_amount_final | integer | responder final amount |
  | ttl | integer | maximum block height to include the transaction |
  | fee | integer | fee to be paid to the miner |
  | nonce | integer | settler's nonce |

The amounts are the exact amounts stored in the channel object on-chain.
