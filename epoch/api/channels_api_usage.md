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

Only steps 1 and 3 require chain interactions, step 2 is off-chain.

### HTTP requests
There are two types of HTTP requests:
* Amount-modifying ones - [deposit](#deposit-transaction) and [withdrawal](#withdrawal-transaction)
* Channel-closing ones - [solo close](#solo-close-transaction),
  [slash](#slash-transaction) and [settle](#settle-transaction)

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
  | initiator | ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF |
  | responder | ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf |
  | lock_period | 10 |
  | push_amount | 3 |
  | initiator_amount | 10 |
  | responder_amount | 10 |
  | channel_reserve | 2 |
  | ttl | 1000 |

  The `initiator` will be connecting to the `responder` on localhost:1234
  We will be using following tools

  * [wscat](https://github.com/websockets/wscat)
  * [unpack](https://github.com/aeternity/aepp-sdk-js/blob/develop/examples/sign.js)
  * [sign](https://github.com/aeternity/aepp-sdk-js/blob/develop/examples/sign.js)

  We assume the channel's WebSocket listener is set on port 3014 (default one)

### Initiator WebSocket open
Using the set of prenegotiated parameters the initiator connects
```
$ wscat --connect
'localhost:3014/channel?initiator=ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF&responder=ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf&lock_period=10&push_amount=3&initiator_amount=10&responder_amount=10&channel_reserve=2&ttl=1000&host=localhost&port=1234&role=initiator'

connected (press CTRL+C to quit)
```

Note the `role=initiator` as it is specific

### Responder WebSocket open
Using the set of prenegotiated parameters the responder connects
```
$ wscat --connect
'localhost:3014/channel?initiator=ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF&responder=ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPflock_period=10&push_amount=3&initiator_amount=10&responder_amount=10&channel_reserve=2&ttl=1000&port=1234&role=responder'

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
 'payload': {'tx': 'tx$51fGUKzH6b7XzrzoQU98ygCn61RNsFsTRosQXG5mL1HGGonJMKff3Q8PtyrDeXvnyQtfZ5TPyqRHSueroqiwWL8NWYciN5uoKb7KJGVXKd5cd3jFQX'}
 }
```
Initiator is to decode the transaction, inspect its contents,
```
$ unpack tx\$51fGUKzH6b7XzrzoQU98ygCn61RNsFsTRosQXG5mL1HGGonJMKff3Q8PtyrDeXvnyQtfZ5TPyqRHSueroqiwWL8NWYciN5uoKb7KJGVXKd5cd3jFQX
{
  "tag": 50,
  "version": 1,
  "initiator": "ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF",
  "initiatorAmount": 10,
  "responder": "ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf",
  "responderAmount": 10,
  "channelReserve": 2,
  "lockPeriod": 10,
  "ttl": 1000,
  "fee": 1,
  "nonce": 32
}
```
sign it, encode it
```
$ sign tx\$51fGUKzH6b7XzrzoQU98ygCn61RNsFsTRosQXG5mL1HGGonJMKff3Q8PtyrDeXvnyQtfZ5TPyqRHSueroqiwWL8NWYciN5uoKb7KJGVXKd5cd3jFQX bd7649b9f77384f1964ed58b27449003a87249381ac1177790ba7369fdf69829edc93bbd0c5d4e1bb245799d1c5f6ff8f12b3256130923180878518cc28e3eac
tx$66dpehQZhw1og9Mi7y6WRrBK2uoa6Mv7uWa9xxKY3H1URJi7g5NfmNgdkBUrqJwk7mFoRnUoGsoKzbZUVrruLKycZadpBmGjea598PTZQ3c6qpzDwuLpJ1s6tHjnGosCGtcGd95dbAdaRTptkKX97rDTSrHoAGkm5tqrqTDtP8euvihcwyShZw9VdqFDKdRw9Bk7AAEKFoExZcSU25q2TFX
```
and then post it back via a WebSocket message:
```
{'action': 'initiator_sign',
 'payload': {'tx': 'tx$66dpehQZhw1og9Mi7y6WRrBK2uoa6Mv7uWa9xxKY3H1URJi7g5NfmNgdkBUrqJwk7mFoRnUoGsoKzbZUVrruLKycZadpBmGjea598PTZQ3c6qpzDwuLpJ1s6tHjnGosCGtcGd95dbAdaRTptkKX97rDTSrHoAGkm5tqrqTDtP8euvihcwyShZw9VdqFDKdRw9Bk7AAEKFoExZcSU25q2TFX'}
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
 'payload': {'tx': 'tx$51fGUKzH6b7XzrzoQU98ygCn61RNsFsTRosQXG5mL1HGGonJMKff3Q8PtyrDeXvnyQtfZ5TPyqRHSueroqiwWL8NWYciN5uoKb7KJGVXKd5cd3jFQX'}
 }
```
Note that this is the same transaction. Responder is to decode the transaction, inspect its contents,
```
$ unpack tx\$51fGUKzH6b7XzrzoQU98ygCn61RNsFsTRosQXG5mL1HGGonJMKff3Q8PtyrDeXvnyQtfZ5TPyqRHSueroqiwWL8NWYciN5uoKb7KJGVXKd5cd3jFQX
{
  "tag": 50,
  "version": 1,
  "initiator": "ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF",
  "initiatorAmount": 10,
  "responder": "ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf",
  "responderAmount": 10,
  "channelReserve": 2,
  "lockPeriod": 10,
  "ttl": 1000,
  "fee": 1,
  "nonce": 32
}
```
sign it, encode it
```
$ sign tx\$51fGUKzH6b7XzrzoQU98ygCn61RNsFsTRosQXG5mL1HGGonJMKff3Q8PtyrDeXvnyQtfZ5TPyqRHSueroqiwWL8NWYciN5uoKb7KJGVXKd5cd3jFQX 207718c1fd933a71e82f185527aae8632f7c0ea2c89bf707b52cd40613c658ab83d3800a0fce22c0ff0477faaa600a7d9bb55dd4191e05df7c15330c2a149617
tx$66dpehQZhw1q6EhkGUBajqmqZdS7YJ3HqfPYpPdaw6TkiP6bJiqor2Vw61GdUjfKwqQy1mz5hPhL4eUTfnXtxWZL9Gfbyz1X7sP86EraBJJ228By8LjiLBS5ouj78RTSfVBqKsJmetkSe9PRQ4HKjeLP5kqb8ZvSBiVaFXkqcd9BSV4R8bT6kaC8wpx1cPXM1nzYDFR6FCTGac3XyCQy3CQ
```
and then post it back via a WebSocket message:
```
{'action': 'responder_sign',
 'payload': {'tx': 'tx$66dpehQZhw1q6EhkGUBajqmqZdS7YJ3HqfPYpPdaw6TkiP6bJiqor2Vw61GdUjfKwqQy1mz5hPhL4eUTfnXtxWZL9Gfbyz1X7sP86EraBJJ228By8LjiLBS5ouj78RTSfVBqKsJmetkSe9PRQ4HKjeLP5kqb8ZvSBiVaFXkqcd9BSV4R8bT6kaC8wpx1cPXM1nzYDFR6FCTGac3XyCQy3CQ'}
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
 'payload': {'tx': 'tx$9mmqY8QRoYS9sV8h66ptE1RjHzeQ341B1dMxD68F1NSMXXTzdjp4HsTms6eg1DAFyhpQFA843jk18ZfT5ffc8AMhhuGvDAkQBwki3DhC9zoXqkk4dn6qsVoypryGob9zWridWYhykQf65fbW9D7mnbD3Kz2GuHRwJUAFwEE3r4sV4Cv9yQfdNfUg8mEhXwR3icZZyQuP9qorhT35eShBrqtSf4LUDJXDbkeVGFiAxNxLinZmWW1DKeeEqwcLaWorativSubWghkUj8oUSDaeVB4sw1B5rh9J9og5MFVGwzz1qZQ6c'
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
with sending the messages for off-chain updates. The first one is special - it
it is the initial state that both parties agreed upon when opening the channel. Since
it is prenegotiated, the channel's software produces the update transaction for
the parties and they just have to co-sign it. The initiator sends an `update`
message and the responder agrees upon it with a `update_ack` message.

#### Initiator signs the initial state
The initiator receives a message containing the unsigned transaction
```
{'action': 'sign',
 'tag': 'update',
 'payload': {'tx': 'tx$24BiYGWoVFJWGSmG9nyzfHZ6bsFoxSLc11FF75r64FsuUVg68jB78PyUZMmeqxDdSUYT7EB2WWD4WZDW6MUgx2thFbgy7YjTCtPqLnNKgRxhNuFF4zzshRmH3ufhtzEYJSfHdQHs54hmp8CavSJBGcJo8TWwAZjmipaGSRM3ibnFQcXMSMeM54dpBKFaua6apxzmu1W'}
 }
```

The initiator is to decode the transaction, inspect its contents,
```
$ unpack tx\$24BiYGWoVFJWGSmG9nyzfHZ6bsFoxSLc11FF75r64FsuUVg68jB78PyUZMmeqxDdSUYT7EB2WWD4WZDW6MUgx2thFbgy7YjTCtPqLnNKgRxhNuFF4zzshRmH3ufhtzEYJSfHdQHs54hmp8CavSJBGcJo8TWwAZjmipaGSRM3ibnFQcXMSMeM54dpBKFaua6apxzmu1W
{
  "tag": 57,
  "version": 1,
  "channelId": "NJSRM7GPvpWS9wbBnrb1GB4ScVCJKV36gTVWMXYLoyNXc5gDN",
  "previousRound": 0,
  "round": 1,
  "initiator": "ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF",
  "responder": "ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf",
  "initiatorAmount": 10,
  "responderAmount": 10,
  "updates": [],
  "state": "2jjqoFL5cDJizoRW5ZwHbU3j58g6r99T7U1Bv32HiSkCm528UZ"
}
```
sign it, encode it
```
$ sign tx\$24BiYGWoVFJWGSmG9nyzfHZ6bsFoxSLc11FF75r64FsuUVg68jB78PyUZMmeqxDdSUYT7EB2WWD4WZDW6MUgx2thFbgy7YjTCtPqLnNKgRxhNuFF4zzshRmH3ufhtzEYJSfHdQHs54hmp8CavSJBGcJo8TWwAZjmipaGSRM3ibnFQcXMSMeM54dpBKFaua6apxzmu1W bd7649b9f77384f1964ed58b27449003a87249381ac1177790ba7369fdf69829edc93bbd0c5d4e1bb245799d1c5f6ff8f12b3256130923180878518cc28e3eac
tx$2LkFsSQGnoWdusfSVrrGEFCu9B4Mz1tN7MhHHmC1cFUUwtEj6VPrC51NYLLxsnaroy17MU4rvpnRgT8zicXTchUTNXMth483Y1W1hHXSZDHs9rGWnvovH6EPwk4cMcW7KanKfCHZ5wxcUVJjKP5UVTAyfy5J44BGuG7NQJo6yQjYWmyztm2F1rdfs24h33QRt58JGz7i576imE381eXSNaaxUaPxK4PAn7xRUviV71T9CfcWg6FRwHYXRW7MH9uggtfRZt4kPFkuLQpc2KCSgUqqk1QrhcPbfVgcdCHLLs36
```
and then post it back via a WebSocket message:

```
{'action': 'update',
 'payload': {'tx': 'tx$2LkFsSQGnoWdusfSVrrGEFCu9B4Mz1tN7MhHHmC1cFUUwtEj6VPrC51NYLLxsnaroy17MU4rvpnRgT8zicXTchUTNXMth483Y1W1hHXSZDHs9rGWnvovH6EPwk4cMcW7KanKfCHZ5wxcUVJjKP5UVTAyfy5J44BGuG7NQJo6yQjYWmyztm2F1rdfs24h33QRt58JGz7i576imE381eXSNaaxUaPxK4PAn7xRUviV71T9CfcWg6FRwHYXRW7MH9uggtfRZt4kPFkuLQpc2KCSgUqqk1QrhcPbfVgcdCHLLs36'}
 }
```

#### Responder signing the initial state
The responder receives a message indicating the intention of the initiator to
update the state of the channel.

```
{'action': 'info',
 'payload': {'event': 'update'}
 }
```
After that the responder receives an update acknowledge message
```
{'action': 'sign',
 'tag': 'update_ack',
 'payload': {'tx': 'tx$24BiYGWoVFJWGSmG9nyzfHZ6bsFoxSLc11FF75r64FsuUVg68jB78PyUZMmeqxDdSUYT7EB2WWD4WZDW6MUgx2thFbgy7YjTCtPqLnNKgRxhNuFF4zzshRmH3ufhtzEYJSfHdQHs54hmp8CavSJBGcJo8TWwAZjmipaGSRM3ibnFQcXMSMeM54dpBKFaua6apxzmu1W'}
 }
```
Please note that this is the same transaction as the one that the initiator
signed. Responder is to decode it, inspect its contents,
```
$ unpack tx\$24BiYGWoVFJWGSmG9nyzfHZ6bsFoxSLc11FF75r64FsuUVg68jB78PyUZMmeqxDdSUYT7EB2WWD4WZDW6MUgx2thFbgy7YjTCtPqLnNKgRxhNuFF4zzshRmH3ufhtzEYJSfHdQHs54hmp8CavSJBGcJo8TWwAZjmipaGSRM3ibnFQcXMSMeM54dpBKFaua6apxzmu1W
{
  "tag": 57,
  "version": 1,
  "channelId": "NJSRM7GPvpWS9wbBnrb1GB4ScVCJKV36gTVWMXYLoyNXc5gDN",
  "previousRound": 0,
  "round": 1,
  "initiator": "ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF",
  "responder": "ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf",
  "initiatorAmount": 10,
  "responderAmount": 10,
  "updates": [],
  "state": "2jjqoFL5cDJizoRW5ZwHbU3j58g6r99T7U1Bv32HiSkCm528UZ"
}
```
sign it, encode it
```
$ sign tx\$24BiYGWoVFJWGSmG9nyzfHZ6bsFoxSLc11FF75r64FsuUVg68jB78PyUZMmeqxDdSUYT7EB2WWD4WZDW6MUgx2thFbgy7YjTCtPqLnNKgRxhNuFF4zzshRmH3ufhtzEYJSfHdQHs54hmp8CavSJBGcJo8TWwAZjmipaGSRM3ibnFQcXMSMeM54dpBKFaua6apxzmu1W 207718c1fd933a71e82f185527aae8632f7c0ea2c89bf707b52cd40613c658ab83d3800a0fce22c0ff0477faaa600a7d9bb55dd4191e05df7c15330c2a149617
tx$2LkFsSQGnoWeBTtZJ9922b6BtBHczrn1iLp5B8zp4M18P5Azkj7FSax6zsP7RN5KzVvVWgyZdbCDNdatp9dojhN46dDYbonnvaunDkpprRXjU1bJEXSxsjCdeFyfUioQbQV2xY3Zd7duCZMbNLP1nynSsSFr7e1364Hm9TsWERJREJLMkiER6dvakeLYnMY3ayedfnCDjUwSgEiXC7yTBhjfwHKgHPBfQF7dzWnzRwNPZ6j8f2urppR2mcR6JTW7FpeiWSPgeRF33tUCopccDi7YZBaHYKghgVJiKejAkAod
```
and then post it back via a WebSocket message:
```
{'action': 'update_ack',
 'payload': {'tx': 'tx$2LkFsSQGnoWeBTtZJ9922b6BtBHczrn1iLp5B8zp4M18P5Azkj7FSax6zsP7RN5KzVvVWgyZdbCDNdatp9dojhN46dDYbonnvaunDkpprRXjU1bJEXSxsjCdeFyfUioQbQV2xY3Zd7duCZMbNLP1nynSsSFr7e1364Hm9TsWERJREJLMkiER6dvakeLYnMY3ayedfnCDjUwSgEiXC7yTBhjfwHKgHPBfQF7dzWnzRwNPZ6j8f2urppR2mcR6JTW7FpeiWSPgeRF33tUCopccDi7YZBaHYKghgVJiKejAkAod'}
 }
```

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
  | amount | integer | the amount givem |

Sender and receiver are the channel parties. Both the initiator and responder
can take those roles. Any public key outside of the channel is considered invalid.

#### Start update
##### Trigger an update
The starter sends a message containing the desired change
```
{'action': 'update',
 'tag': 'new',
 'payload': {
    'from': 'ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF',
    'to': 'ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf',
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
    'tx': 'tx$uSRvPk9G4aqeZTGuPHZokSNZK5jBCS3GaoyieTbNmJWXbNkJDVMc6nQLJpxoJD4xTFhZVm1uCMnXwVXWGhdgx2fZVysmWx8aoHMvr8GVTkRQNdJaKHk4ngnXbJiWxZPLunbPLZupEtA9xHQacmQJfKrs79jN414ihCGByPiWfLuLQRsoqvhaMNB7nsB6j9ydPDmfjk6pycustCCzXvLncTxTz6M7uvj6Yog8mBkcEuTPk2gPVoDpRkaKZY1xJGszDoBpLBhqxoc2UjJbH5yuH1RX6zFzbGXNx2Qrqe1'}
}
```
The starter is to decode the transaction, inspect its contents,
```
$ unpack tx\$uSRvPk9G4aqeZTGuPHZokSNZK5jBCS3GaoyieTbNmJWXbNkJDVMc6nQLJpxoJD4xTFhZVm1uCMnXwVXWGhdgx2fZVysmWx8aoHMvr8GVTkRQNdJaKHk4ngnXbJiWxZPLunbPLZupEtA9xHQacmQJfKrs79jN414ihCGByPiWfLuLQRsoqvhaMNB7nsB6j9ydPDmfjk6pycustCCzXvLncTxTz6M7uvj6Yog8mBkcEuTPk2gPVoDpRkaKZY1xJGszDoBpLBhqxoc2UjJbH5yuH1RX6zFzbGXNx2Qrqe1
{
  "tag": 57,
  "version": 1,
  "channelId": "NJSRM7GPvpWS9wbBnrb1GB4ScVCJKV36gTVWMXYLoyNXc5gDN",
  "previousRound": 1,
  "round": 2,
  "initiator": "ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF",
  "responder": "ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf",
  "initiatorAmount": 8,
  "responderAmount": 12,
  "updates": [
    [
      "ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF",
      "ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf",
      2
    ]
  ],
  "state": "TNN5aAZeXSEj6Ebxm8vsaUXXzji1S1kxFLyW5dooDE3kJ9kb3"
}
```
sign it, encode
```
$ sign tx\$uSRvPk9G4aqeZTGuPHZokSNZK5jBCS3GaoyieTbNmJWXbNkJDVMc6nQLJpxoJD4xTFhZVm1uCMnXwVXWGhdgx2fZVysmWx8aoHMvr8GVTkRQNdJaKHk4ngnXbJiWxZPLunbPLZupEtA9xHQacmQJfKrs79jN414ihCGByPiWfLuLQRsoqvhaMNB7nsB6j9ydPDmfjk6pycustCCzXvLncTxTz6M7uvj6Yog8mBkcEuTPk2gPVoDpRkaKZY1xJGszDoBpLBhqxoc2UjJbH5yuH1RX6zFzbGXNx2Qrqe1 bd7649b9f77384f1964ed58b27449003a87249381ac1177790ba7369fdf69829edc93bbd0c5d4e1bb245799d1c5f6ff8f12b3256130923180878518cc28e3eac
tx$64ybAsJEkrVChSiCe5WCvbwKyxLcp8ZXriDPyM9iXHCWwykDR1zyt9hqjNgKtURHRwL3CiB4cwoYGRev8QJpTsebBvt4QfGpJZ5ojwkHtVohE4HZw33xJSxCFBoskvs4adSLDjyH3TpcMENjJ2ttbLvXoss4jGhQdNZdnBZbqDSQFtih6wqz5NoHGt2A8AqrKpZztExYJ7Ljdc46XVLRB7fL2boGvLoNufExXg71pcgwqYrQhp4meK2Dj3SRn1pL12gmQ8TzqQF7oKnB7jkad69aeE18mawmwCFfpEWcTCY9ZKFJgodJ13FeGWfSMq9ecntdV6xfDtZYmbxKDzDUHi9r1eZEBpbQnqPq96LEdWSYQyXpDhe3VzQLcKWMdVdt5aBmbQkTZgUdES
```
it and then post it back via a WebSocket message:
```
{'action': 'update',
 'payload': {
    'tx': 'tx$64ybAsJEkrVChSiCe5WCvbwKyxLcp8ZXriDPyM9iXHCWwykDR1zyt9hqjNgKtURHRwL3CiB4cwoYGRev8QJpTsebBvt4QfGpJZ5ojwkHtVohE4HZw33xJSxCFBoskvs4adSLDjyH3TpcMENjJ2ttbLvXoss4jGhQdNZdnBZbqDSQFtih6wqz5NoHGt2A8AqrKpZztExYJ7Ljdc46XVLRB7fL2boGvLoNufExXg71pcgwqYrQhp4meK2Dj3SRn1pL12gmQ8TzqQF7oKnB7jkad69aeE18mawmwCFfpEWcTCY9ZKFJgodJ13FeGWfSMq9ecntdV6xfDtZYmbxKDzDUHi9r1eZEBpbQnqPq96LEdWSYQyXpDhe3VzQLcKWMdVdt5aBmbQkTZgUdES'
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
    'tx': 'tx$uSRvPk9G4aqeZTGuPHZokSNZK5jBCS3GaoyieTbNmJWXbNkJDVMc6nQLJpxoJD4xTFhZVm1uCMnXwVXWGhdgx2fZVysmWx8aoHMvr8GVTkRQNdJaKHk4ngnXbJiWxZPLunbPLZupEtA9xHQacmQJfKrs79jN414ihCGByPiWfLuLQRsoqvhaMNB7nsB6j9ydPDmfjk6pycustCCzXvLncTxTz6M7uvj6Yog8mBkcEuTPk2gPVoDpRkaKZY1xJGszDoBpLBhqxoc2UjJbH5yuH1RX6zFzbGXNx2Qrqe1'
    }
}
```
Note that this is the same transaction as the one that the starter had already signed. The acknowledger is to decode the transaction, inspect its contents,
```
$ unpack tx\$uSRvPk9G4aqeZTGuPHZokSNZK5jBCS3GaoyieTbNmJWXbNkJDVMc6nQLJpxoJD4xTFhZVm1uCMnXwVXWGhdgx2fZVysmWx8aoHMvr8GVTkRQNdJaKHk4ngnXbJiWxZPLunbPLZupEtA9xHQacmQJfKrs79jN414ihCGByPiWfLuLQRsoqvhaMNB7nsB6j9ydPDmfjk6pycustCCzXvLncTxTz6M7uvj6Yog8mBkcEuTPk2gPVoDpRkaKZY1xJGszDoBpLBhqxoc2UjJbH5yuH1RX6zFzbGXNx2Qrqe1
{
  "tag": 57,
  "version": 1,
  "channelId": "NJSRM7GPvpWS9wbBnrb1GB4ScVCJKV36gTVWMXYLoyNXc5gDN",
  "previousRound": 1,
  "round": 2,
  "initiator": "ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF",
  "responder": "ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf",
  "initiatorAmount": 8,
  "responderAmount": 12,
  "updates": [
    [
      "ak$2oivhvhop4pXTPDG91vGHJRXRPhfpaKoZ3WxKde8FwECvnesYF",
      "ak$214KiPC3Qt4KeFaSp76ak72Qhd3gG4tVoMTqnx64sgyhdcPJPf",
      2
    ]
  ],
  "state": "TNN5aAZeXSEj6Ebxm8vsaUXXzji1S1kxFLyW5dooDE3kJ9kb3"
}
```
sign it, encode it
```
$ sign tx\$uSRvPk9G4aqeZTGuPHZokSNZK5jBCS3GaoyieTbNmJWXbNkJDVMc6nQLJpxoJD4xTFhZVm1uCMnXwVXWGhdgx2fZVysmWx8aoHMvr8GVTkRQNdJaKHk4ngnXbJiWxZPLunbPLZupEtA9xHQacmQJfKrs79jN414ihCGByPiWfLuLQRsoqvhaMNB7nsB6j9ydPDmfjk6pycustCCzXvLncTxTz6M7uvj6Yog8mBkcEuTPk2gPVoDpRkaKZY1xJGszDoBpLBhqxoc2UjJbH5yuH1RX6zFzbGXNx2Qrqe1 207718c1fd933a71e82f185527aae8632f7c0ea2c89bf707b52cd40613c658ab83d3800a0fce22c0ff0477faaa600a7d9bb55dd4191e05df7c15330c2a149617
tx$64ybAsJEkrVCiU99JyZmUMxUnnc7t2adaktwJAbogVSweBjGL6wwaHYeB5Q9bWMtt31HZUwZyrzucSrA73xuyuEMTujSFLhH9X63EZZiQogYwfxXbJnB7pCo8JTJHqF5papQtukUpRnWJB3bfDYxNdQe2Ewa4HZiHMYcSC9Ywiiy6m5vAhMRrrfk2VLYsAMmVjiKvuwJ41XXb18vrR7ooHymcY1WEPPqXVzHkSbcaM3xvii7UGhex4AKKFoGMx9CWSsWVF8uWjhSq1QGB9VNg1wYZLU9R3PstsvzhuV8mqib7yPimrDSL5jbU8dKxDtsXV3bhwMqHrRAnuQBdCm97SWwRzk4t3SDh8dWfiRnBskTX9M49d7nw2GT2F1Wei3x3Uu67fxm1uyWtN
```
and then post it back via a WebSocket message:
```
{'action': 'update_ack',
 'payload': {
    'tx': 'tx$64ybAsJEkrVCiU99JyZmUMxUnnc7t2adaktwJAbogVSweBjGL6wwaHYeB5Q9bWMtt31HZUwZyrzucSrA73xuyuEMTujSFLhH9X63EZZiQogYwfxXbJnB7pCo8JTJHqF5papQtukUpRnWJB3bfDYxNdQe2Ewa4HZiHMYcSC9Ywiiy6m5vAhMRrrfk2VLYsAMmVjiKvuwJ41XXb18vrR7ooHymcY1WEPPqXVzHkSbcaM3xvii7UGhex4AKKFoGMx9CWSsWVF8uWjhSq1QGB9VNg1wYZLU9R3PstsvzhuV8mqib7yPimrDSL5jbU8dKxDtsXV3bhwMqHrRAnuQBdCm97SWwRzk4t3SDh8dWfiRnBskTX9M49d7nw2GT2F1Wei3x3Uu67fxm1uyWtN'
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
    'tx': 'tx$2C9etiP9wZr2iQVj6BUYk5sxHVNgcVhK4ngwv7fjsnnj2S1przQggcqyfhfJGgMPkpzoDfBZM7SyxVQykUCHvJw2N7E5gWSMuiuGjL4fYYUAXkEeyJygCAqKiszgqz8RuBDAfyCX44SsC5Ev1KU84jkui5EVxb'
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
    'tx': 'tx$4L9GSozvWQwFDrkxaT2DZYrXU1sFULxRkpFbKjzAR4XinUwRgFvzm7ct7ZCvq38ZfCUZR73yXHRnd2DURPCmwdj7NarynugJ5JkY5TVN6ZzxVMEs6nsA8Dfu7dA9AoFj3AwaDLdaBuUEXuXTvsLEZy57GCG2v8HLucFkpHRTK63VdG8UNMK429ofMqHo8QyPjdwHYjH43baCSiN21g2hfpL9qWBmGwmcipSKuV5tHKg2aMpURCHM1z1FnRqdosiVM42PJTxSAHv'
    }
}
```
### Acknowledger signing
Then the acknowledger receives a `channel_close_mutual_tx` to sign:
```
{'action': 'sign',
 'tag': 'shutdown_sign_ack',
 'payload': {
    'tx': 'tx$2C9etiP9wZr2iQVj6BUYk5sxHVNgcVhK4ngwv7fjsnnj2S1przQggcqyfhfJGgMPkpzoDfBZM7SyxVQykUCHvJw2N7E5gWSMuiuGjL4fYYUAXkEeyJygCAqKiszgqz8RuBDAfyCX44SsC5Ev1KU84jkui5EVxb'
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
    'tx': 'tx$FhWGD2ecn65dJoYfnYZxL9iNhbqXuTvq7HddtWNuQADQi71B1etAC7NmNG6n3Lq2wr6myPSG2HbGEAvJHJrmgbYuxC4biQGaz2Q7q3NtHJFxBKQxyRK33r4Cj98q3xNZqZ9YXQpE4f5XYjzLZbw6YRRsvdV28rzZHMFbX9rzeXJpxBD1NjtfHsQtVKMNyHABj96rt9DuV3XMmQomUw92TnuKNWUJS5omJ9N2Lq2bcm3TvWg7JvyxyU6DS9FPHwDw4aHcgRSsc5Bp'
    }
}
```

#### Signed channel_close_mutual_tx
Both participants receive the co-signed `channel_close_mutual_tx`:
```
{'action': 'on_chain_tx',
 'payload': {'tx': 'tx$T7f9gwgv5SsoFi3uoKcjZcfG9wXqS52nRHiCZccmc2pYAxc17sfDDNu6EAVgxQQxD2pvbQGBBKpatdkczSQWPxqMdXpgPgKEqEGxzmqJmeNMFR81KotMjPAiJciuinTQ1Gr2jLnfck3mGhnpXT9DrniEYdqnd53nP2XGMPsodRC8dUUMFzANh3YzBn3xsrNA1eHVBu4SZVMGhUHR3baVGKNpdHhsz8RiYTc6bjHBDhRiRPtgfvF4swJGDUsgWpAciLnssdq8AZ9cVy5JyReg3mf8UJaSLfvVUATyN9LN3Jf3pW'
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
curl 'http://127.0.0.1:3013/v2/tx/th$gCajQAyuCHwXFTSTyZWfmvJqNrikJnKfWmBsrPaAUswtNf7VP?tx_encoding=json'
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
                                     'from': 'ak$2KTP6oDmZcPKRoE8DZxHFQA7GCyYoc8TTRek5uCEwXDFovkFqz',
                                     'to': 'ak$2KmumVDr1KQwhzPbbC14t3at6wHD1i6TFAS3PoquPRnEGaiiWs'
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
             'to': 'ak$R2jDydYPpjsWckNte6bUFg6pJiyKRaYaLRBKnQFwZAuEiDxrb'
             }
}
```

Then the `receiver` gets an event containing the info being sent and some
details:

```
{'action': 'message',
 'payload': {'message': {'channel_id': 'ch$6SgSc7a14dGbwMNCsjjQZCYVreVLKkFwBzJEZ58ZSZnV9FiQ1',
                         'from': 'ak$2W2vDXjrDWCtVcJ3aKNHHr8BxJ37xaNg6o88AfxosTTyejiEM',
                         'to': 'ak$R2jDydYPpjsWckNte6bUFg6pJiyKRaYaLRBKnQFwZAuEiDxrb',
                         'info': 'hejsan'
                         }
            }
}
```
