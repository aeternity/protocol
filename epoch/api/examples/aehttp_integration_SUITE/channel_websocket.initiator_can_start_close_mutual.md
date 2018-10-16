
#### initiator init (2018-10-16 20:05:56.359)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder init (2018-10-16 20:05:56.363)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### responder <--- (2018-10-16 20:05:57.365)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:05:57.367)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:05:57.372)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1K1Dzrrz"
  }
}
```

#### initiator ---> (2018-10-16 20:05:57.394)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmcZviW7wosY3wDcjD79iMvZKtV6UsLxpsSMXB3zVdJvGCcs8Wd5hSAkhJCo3FiiHxvvUyKjJGpK5RQVp9Eayk49V1vH2RXLyosM8p6hBUkZQjByEfpz1u79CjVkC52ieLTJdPsHamZumGvdq5eKmYugpB9kNJXxf3rEaGmqUPepe3oHpBTsPHh3Mer3LR9kyMVTaak5Q7gugkKJi19MUXGEfe3Q1U2Tpr5gmdJkkLTA9gbz34MB2AHevWYTnPV1j"
  }
}
```

#### responder <--- (2018-10-16 20:05:57.395)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:05:57.395)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1K1Dzrrz"
  }
}
```

#### responder ---> (2018-10-16 20:05:57.396)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HnuiJ9hw7i3YYb9RzqUjVJKoof1yjSTqPkGk3L7bW2uARzNktBptCBeQzx1bFGVUQXqziNxEi6zZxb4KiRLatuBow7PN1xTc7FsmqLv92Fmc3HwguZEnuaiUpemApwVT8is3Du2KkQXjFTrqXCf2qXz1zdoB8n8MJQBi7iZoJPh1a4ojTSsyMuQwY2HKP4akAjsBUzgTfj5kK4Dn7ELWzCSLusFFUPqudpvsM5ZfpWRHxjw6ZuefZ8TBsaei5svH6"
  }
}
```

#### initiator <--- (2018-10-16 20:05:57.398)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:05:57.398)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmQyrinxnBKjZWLakRVbVURUxWbwKwMuqMgThXYjCk6qwYCEAJRhZgrN8WtPrS4YHqwtG4PH5Ksa4WQ8UV1ACbBWEUcuA4qvRAb4MTfVbiirqeTV6vM2DRFQcMuzKXqHGhEX86tWf1WdLmG48MGUdHRuyP5jj4qZ3HBciErAk5pbkvNC58ofQebEQbxdScCXJiP1XQ1bB2HdQHuF8iXQZYPkZugdrQGYgJW9vCEfNBReYXS91EzSPe45veJyaxqJnCQjw1vsZ4wRA5iJW4gdDxyqfZJSVc8Nh7Wn9aFc84n92pr1VyoZw2bzyiMcMWpDCYxVZAz4KT8XcYw4mM6so5yC7ncR"
  }
}
```

#### initiator <--- (2018-10-16 20:05:57.399)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmQyrinxnBKjZWLakRVbVURUxWbwKwMuqMgThXYjCk6qwYCEAJRhZgrN8WtPrS4YHqwtG4PH5Ksa4WQ8UV1ACbBWEUcuA4qvRAb4MTfVbiirqeTV6vM2DRFQcMuzKXqHGhEX86tWf1WdLmG48MGUdHRuyP5jj4qZ3HBciErAk5pbkvNC58ofQebEQbxdScCXJiP1XQ1bB2HdQHuF8iXQZYPkZugdrQGYgJW9vCEfNBReYXS91EzSPe45veJyaxqJnCQjw1vsZ4wRA5iJW4gdDxyqfZJSVc8Nh7Wn9aFc84n92pr1VyoZw2bzyiMcMWpDCYxVZAz4KT8XcYw4mM6so5yC7ncR"
  }
}
```

#### initiator <--- (2018-10-16 20:05:57.831)
```javascript
{
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:05:58.194)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.195)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.195)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.198)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.201)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.202)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.203)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmQyrinxnBKjZWLakRVbVURUxWbwKwMuqMgThXYjCk6qwYCEAJRhZgrN8WtPrS4YHqwtG4PH5Ksa4WQ8UV1ACbBWEUcuA4qvRAb4MTfVbiirqeTV6vM2DRFQcMuzKXqHGhEX86tWf1WdLmG48MGUdHRuyP5jj4qZ3HBciErAk5pbkvNC58ofQebEQbxdScCXJiP1XQ1bB2HdQHuF8iXQZYPkZugdrQGYgJW9vCEfNBReYXS91EzSPe45veJyaxqJnCQjw1vsZ4wRA5iJW4gdDxyqfZJSVc8Nh7Wn9aFc84n92pr1VyoZw2bzyiMcMWpDCYxVZAz4KT8XcYw4mM6so5yC7ncR",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.203)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmQyrinxnBKjZWLakRVbVURUxWbwKwMuqMgThXYjCk6qwYCEAJRhZgrN8WtPrS4YHqwtG4PH5Ksa4WQ8UV1ACbBWEUcuA4qvRAb4MTfVbiirqeTV6vM2DRFQcMuzKXqHGhEX86tWf1WdLmG48MGUdHRuyP5jj4qZ3HBciErAk5pbkvNC58ofQebEQbxdScCXJiP1XQ1bB2HdQHuF8iXQZYPkZugdrQGYgJW9vCEfNBReYXS91EzSPe45veJyaxqJnCQjw1vsZ4wRA5iJW4gdDxyqfZJSVc8Nh7Wn9aFc84n92pr1VyoZw2bzyiMcMWpDCYxVZAz4KT8XcYw4mM6so5yC7ncR",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

##### initiator: (2018-10-16 20:05:58.501)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 20:05:58.501)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 20:05:58.501)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 20:05:58.501)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 20:05:58.501)
> Channel is `open` and ready to use

##### responder: (2018-10-16 20:05:58.501)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:05:58.533)
```javascript
{
  "id": -576460752303423473,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:05:58.534)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.540)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7UFmQx1Ycg75zgWEKHCGRSZqLwy35ECe4GkDfZvdGjNHgosmbHE1WsF6rJXmR5tJxt6Ce5UyBv5XybeWPL3oUEeXX2QgW94UBbFLSpcWKZB3ZuDg7PoxrtyztFZDdrtkRUoBVvexspw3Rc2iXVaGoDVR9YwzkSMa"
  }
}
```

#### initiator ---> (2018-10-16 20:05:58.541)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4w1wDVAmMmy2BtLuV6fBwV8YZzH159wisHjRtYAvTHhHbddmSE97d1mfjpt36VBN5SZkBZPhyNPL2cMx6nQeiwxVmQot3t1ZRaVcfDZBKqxyJkyn5FyF2ZGkzJQrcitwGD3CsRoqEDzwRw3tqirKGkbgAqkV39nZuRWsDXxScRASRKp626eHJ75ReXDYfbQFnqFc4rS85SUL9XD1JsbdHxRt6nmgkjhB6hue7tsk1fTdAtKJJncP3r1zMQe1YXhuRZAg3dG2d73VyWyDZ6WARAYPSut55gzchvDP7EUm67CfHRQ"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.546)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.547)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7UFmQx1Ycg75zgWEKHCGRSZqLwy35ECe4GkDfZvdGjNHgosmbHE1WsF6rJXmR5tJxt6Ce5UyBv5XybeWPL3oUEeXX2QgW94UBbFLSpcWKZB3ZuDg7PoxrtyztFZDdrtkRUoBVvexspw3Rc2iXVaGoDVR9YwzkSMa"
  }
}
```

#### responder ---> (2018-10-16 20:05:58.548)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak51JEBGt6TKBryJRuZkxPkMjhz2uT9QrjK4PrwddmxMhoqtrG2i5rU8QCgF3Um5oNREkL3Fu2hJVG9NgfvXyiV6rTDtLJw7NP8op62rHckyM1K9D1B8x1Wdhb6NsNKHare5HkDJ8u4cxNMmHKbCoqdx7RM4YAZ8UMqWACStbCKqmZhdzJMG6tVPSNXvT3kyVr3vjPRNC3TpT8MeENTTJWiuqVH4PQ1gEmzatedTQUXuqksirYE1ggTxFyPs3AGC5qeWoxyGks739Ecg3zgRRW2ZyHbRZ5DpDPAniZ82qXTJHDxYc"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.555)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkdRgCHmrwfn7EsmuRLcpQ39Xfx86rSybCsd7MJHoshCmjSBfQcZQd5NhDgRVghQfSPuhE4fBWMcWNAmnQYWAf1kQo3LsomxPsfZqWGM7eKKxictsvreNZdkwwyMXGAU3BbmnAXBAfDCHw78tCcUZUQ7E7xJgfbT8j9CoVm8pVQrzTo9PYCXs9dxXm3U94PmeghEE5j1GzMnhMJWb6ghbqK18Ggfv2ZBuC5NoeFkZJ8a89JCZpVANvvzznWtXcaiCFkKL2Wz3a1XYFD9eqCg67ozMBrTPGuMiqmtTwBaTfABWP11pkgR2V4Ys3sNdq65tkD187qx6gJzE43F6fcBtTtXvJTjeMiRyCK2JAxoH8n6Gv2XQA9LsmFvkXnS3qMWsnC44q5DTT",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.556)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkdRgCHmrwfn7EsmuRLcpQ39Xfx86rSybCsd7MJHoshCmjSBfQcZQd5NhDgRVghQfSPuhE4fBWMcWNAmnQYWAf1kQo3LsomxPsfZqWGM7eKKxictsvreNZdkwwyMXGAU3BbmnAXBAfDCHw78tCcUZUQ7E7xJgfbT8j9CoVm8pVQrzTo9PYCXs9dxXm3U94PmeghEE5j1GzMnhMJWb6ghbqK18Ggfv2ZBuC5NoeFkZJ8a89JCZpVANvvzznWtXcaiCFkKL2Wz3a1XYFD9eqCg67ozMBrTPGuMiqmtTwBaTfABWP11pkgR2V4Ys3sNdq65tkD187qx6gJzE43F6fcBtTtXvJTjeMiRyCK2JAxoH8n6Gv2XQA9LsmFvkXnS3qMWsnC44q5DTT",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.561)
```javascript
{
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 698
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 402
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:05:58.563)
```javascript
{
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 402
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 698
    }
  ]
}
```

#### responder ---> (2018-10-16 20:05:58.564)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.568)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7ZgHGVZ1p1q1kg3MDQWyPBw59vLsnPZ9FY4hycQx2j4Q6QgRfhFekpw5yLcYA3SBZPV1yYUAB1axd6GKHZqHBHzPUQiFNAFPknKDHhoFhUbMnLcnx88L524Heo6CadzXmCmghmMwU5M1CjmZBjkv8EBFTvqinmYa"
  }
}
```

#### responder ---> (2018-10-16 20:05:58.569)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4qaJsdipufdqBLC8US446ah1GCH5gEDtfoJH3PDwdwGguCpUCxHyYYgHLni5AgsiGQG8ZmykkwEYFbxZ2tNe3wKYWu9BDXb8EbfiBb3yiZXzcpvW55zGUon1TveCJLSzbu53bH9azbz4ghnWyN4UjqkXDmy3ABVVjH5smnLs1PfnqiRksaQJ2Tmm5XyHmQu9QgALx7cffewtaMsFCTyAFaT1ugepwAuKWy7SUPXbZjzEz8Lvvkh29wWqdpSTcjVb972xzHkV1bmFfsoYCJ88kudfHQB5euuuhoQJdDJmaWt2wo9"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.573)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.574)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7ZgHGVZ1p1q1kg3MDQWyPBw59vLsnPZ9FY4hycQx2j4Q6QgRfhFekpw5yLcYA3SBZPV1yYUAB1axd6GKHZqHBHzPUQiFNAFPknKDHhoFhUbMnLcnx88L524Heo6CadzXmCmghmMwU5M1CjmZBjkv8EBFTvqinmYa"
  }
}
```

#### initiator ---> (2018-10-16 20:05:58.575)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4m8GZ5bmTzYwNmsydDJjgBCWC3EL8uVb3hc7rGsSiwhPNrrnjCZs1iXqRZRvgc5VpdbX5nzYr46f9W8CpYeRGc5BzqyJGa8jdC9C36zoe7KBqNWZJRDaYQbECEA9EScc6LdLZgwVtXf9Z4GauwxsjUR2HxZKo38XTRCK9zAmnw3REmPfoVJeCBupTht7HEc7USEiRwMpCjNbiVU1fu3wKiNRjaYuA9soyJj1SPc3f4HPyNjzkRfBN1sYaVxUDTZ49M9U3KMRuYAJr3yK4fdy9wZ6GuT3U6oLd2PhiEJTs7oLFGL"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.580)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkLRSuLVfVFbVmpXwXhZrbbo9YWdDZEnX5fNmWFBxyETsqYFUSDBMBAExto754fMYthg6mcd6uhDNXfTrXa3EhavLuMBz2QrKjHCdfXqxkY2TfymzM6H9NdgiB43JQLeyFjZRHBX9negdk2CYpKTcCACJ1Hiy1JZNGDDTqmJYcF4r4QeWeYWqcCK4evtPqfPaLziZDVEm5rg1wUMy7vqYPa53xM3ursemexcVywvqcZYKxmB9AfQbpcdtmWyHu9ZcHWw571tPEYswf6rWYPojfxydzxP3q1Nga9n5XbTWGj47uUigZb8ebDC2vVQX8Q36MYFekMTS1QHqU3pAR8NrXSJaSx5r1YPPphMK8pACHWmB64c8uQenHHYWtqszwgFizCC5ba9aZ",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.581)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkLRSuLVfVFbVmpXwXhZrbbo9YWdDZEnX5fNmWFBxyETsqYFUSDBMBAExto754fMYthg6mcd6uhDNXfTrXa3EhavLuMBz2QrKjHCdfXqxkY2TfymzM6H9NdgiB43JQLeyFjZRHBX9negdk2CYpKTcCACJ1Hiy1JZNGDDTqmJYcF4r4QeWeYWqcCK4evtPqfPaLziZDVEm5rg1wUMy7vqYPa53xM3ursemexcVywvqcZYKxmB9AfQbpcdtmWyHu9ZcHWw571tPEYswf6rWYPojfxydzxP3q1Nga9n5XbTWGj47uUigZb8ebDC2vVQX8Q36MYFekMTS1QHqU3pAR8NrXSJaSx5r1YPPphMK8pACHWmB64c8uQenHHYWtqszwgFizCC5ba9aZ",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.586)
```javascript
{
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:05:58.588)
```javascript
{
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 20:05:58.588)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.592)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7f6o836V1MYwWfaU7XMyAVToiMuwm5TGfaxKu6AdmUfRag6YLYcuQmgF4nKKtpXHF2SeUbnb4GCtuWr1zphw7J7hhMaAwixoS9oTg4kgC4rc61BcPZFcD8qZpvxf5j4DGh7B8Gb3JKJXUHfiF6kduSyBbr5VbNhU"
  }
}
```

#### responder ---> (2018-10-16 20:05:58.593)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak55LBxjuceotkti9MKMuK4zTFvvfEivBueJBmwoJJHWvrorKTaN8oukiDqtZMG2BVThe4hws3MVwXpqbqqt3ncNs5KES4932pHnYSD1hAzqJuRN4UQ5Hcq8a7CB9YQXtBCbivHe8WpMk11Gu8ux29AEjGoWhQMnAhHp7YErdg35Birj5rpLDrzbZqp7qosh4dcPJFnGbice9chRQHqB1D5NQMxVArfRKTFaYcbQgbhb7qG38TnNoW6Kn4xwkf2ZkjKARta38SaFR3mWc7oBz6AZz4mW7DoThicMnpooEStuE6AsG"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.597)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.597)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7f6o836V1MYwWfaU7XMyAVToiMuwm5TGfaxKu6AdmUfRag6YLYcuQmgF4nKKtpXHF2SeUbnb4GCtuWr1zphw7J7hhMaAwixoS9oTg4kgC4rc61BcPZFcD8qZpvxf5j4DGh7B8Gb3JKJXUHfiF6kduSyBbr5VbNhU"
  }
}
```

#### initiator ---> (2018-10-16 20:05:58.598)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak55saK5y2TrxtcYbLYY56ZVzGTuEX1ag8oQ5G56S5PahkcyhvvGKwwqXwm64pxCSQ43Luvj568tuDQHTP5Ue6znYPpUuc4jWmYCztJCogvvBGNeYrHpdJmMAMBXyyaSk7uiDJ9VfRXgwLjvMR6oHpqaFZicqstmz4KgWmni1KL8u6g1XexaCQ9dc1cRNRwmhYjGQNM4VDtpAG5nLyMTRV9RytWhUCLvfWSDpuFGdHihSyRekUWFqjgfz7cQLy2QTxWorbtZYagpkm3MkUR5RP8NX5ij5FKMZx9mo4aXSmNo4CiZ5"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.604)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDksikbwoL3gWJtLQ2Ra48k8J6oZqR9kJQ29Lf7AXFmsEzFUxK3DtjeM84WSmm4i1bU5kDpsL6A1YwZMaE5cWDB3SeRy6Kg9jPu71pGzEzD8db5qbKhPTHMWtwXB3nf1zqC5Wbvxy8bCcAPM8GFQHK2c8YXsdUj2K2efbnWBT4oCATzVQsf9KvdacCNpRfWQNRTmQGRvrMjySgPYwWJfjjofCChVn8sVQaCbLLWVXqArj4iP3kSLf1EK8QQtjFU97MJ5KFgCF25Eo2wo8JNudG519j4i4gVia7SvsyiKWq4dB8X1rCQ56YeQKMbUBGGiXMgG6exFhGQbsaBoRrKXy369hjpjf2js3FYhnnyCKLCgvpUnTUN2UCufC75a6WyfcBuUjS9jcz8",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.605)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDksikbwoL3gWJtLQ2Ra48k8J6oZqR9kJQ29Lf7AXFmsEzFUxK3DtjeM84WSmm4i1bU5kDpsL6A1YwZMaE5cWDB3SeRy6Kg9jPu71pGzEzD8db5qbKhPTHMWtwXB3nf1zqC5Wbvxy8bCcAPM8GFQHK2c8YXsdUj2K2efbnWBT4oCATzVQsf9KvdacCNpRfWQNRTmQGRvrMjySgPYwWJfjjofCChVn8sVQaCbLLWVXqArj4iP3kSLf1EK8QQtjFU97MJ5KFgCF25Eo2wo8JNudG519j4i4gVia7SvsyiKWq4dB8X1rCQ56YeQKMbUBGGiXMgG6exFhGQbsaBoRrKXy369hjpjf2js3FYhnnyCKLCgvpUnTUN2UCufC75a6WyfcBuUjS9jcz8",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.609)
```javascript
{
  "id": -576460752303423468,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 400
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 700
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:05:58.610)
```javascript
{
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 700
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 400
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:05:58.610)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.613)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7kXJyadxChGsGf7b1djFmMA32GgF1Hu2JRR5S1BgUzBN9c87bqKmUhUa8de8dR9c1ny69FSFqfwLpsPcX6fmGF2UBrzTEqChDhi5buUmoKxnUtpqzSv5urHxYCe71DrLGXbLABugFUsxWQsdh9e8Usqh8GpkbUrD"
  }
}
```

#### initiator ---> (2018-10-16 20:05:58.614)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4sKuYAUeczb17DDy3YbibyhbBj5d99FBk8utxM9CnKbKKJPpcS3BRAYHRFMo6VfGvGoTKqKhLSYPVjwvisSD7aeNbuBGUrTM3D7CvE4VvxhAw2xTt9Jwcg9Df61rxaJW5nVHZhQuCZe61vn5LKCXMFuas3dwPgULWTEvnCqmfmkkranjCunWGaTgL1hGQQscF3iB1SiVy2d1HsrqMthQRs9jdqqj4vhboVXUBY1tk6qUDT2LYVPDvsNiqwEbywDqgaQfwKZeLfh92aT7vaKhNx4Uo2tVL5z11f4bWKEuNCyVMto"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.643)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.643)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7kXJyadxChGsGf7b1djFmMA32GgF1Hu2JRR5S1BgUzBN9c87bqKmUhUa8de8dR9c1ny69FSFqfwLpsPcX6fmGF2UBrzTEqChDhi5buUmoKxnUtpqzSv5urHxYCe71DrLGXbLABugFUsxWQsdh9e8Usqh8GpkbUrD"
  }
}
```

#### responder ---> (2018-10-16 20:05:58.644)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak55CXbBgpUgm2ciPusU5EkJWYAeXkQfNG33aNPejAHe14fPFKHr466MSbtNaT7tVJ94kej1BuuuFruuacEzZ8ZnUZBMoTQQJiQeYivPKvDizM1Rsz7QKczgS8ENSbv5jK49oWdctT1tUqTFqQjMWKfLkancFPAKzJyFruH6qRSuUjNvXA8bniYmtooA9kS1H9FWp73XJryFDexS4hSsDkuZcQWY34obWEiYRUu8qyHD741oMEzBMkzQfPj4MdSJr4kDFTMR6vnaBinkSqNpSf1xmQbG5LvrYcwAdkCg4uDeByg5Q"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.648)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkX5izti4PsuoD214mx1TQJgw3ZjjVnfyBde3pG1WwHDkBQGgVeVi9tci9iAZHkETe4PDZJmyjy9yvnbjaNZCnxeNk264SrXUwps7AJGWhfYKFuWye8XvqeGRJ6SLVw1GEvkuedrB6MmEjeig7HQyBPx83JJKj75Q7XCZ1dkRXbVP51mm15dXBQMne8yWEScZ9G1XHKZV8QbYYyqgMUygLJUvLJFgeXA3m4R8hZDaSxqQLzGPuYzgUAhVGrHLLPTX5UwZPm8ypSbt6GF4Hp3sDgzLbVgGybyC2WAXQFV1hafZiJ1BwpWRU3kcPTh5erdbhz451DfgtDJMueJHjU3rn6ReSEF8jPNyiSgTRCddsLLuR8T3YwZ6Yc6rZNszSYfjdTd7rQLnR",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.649)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkX5izti4PsuoD214mx1TQJgw3ZjjVnfyBde3pG1WwHDkBQGgVeVi9tci9iAZHkETe4PDZJmyjy9yvnbjaNZCnxeNk264SrXUwps7AJGWhfYKFuWye8XvqeGRJ6SLVw1GEvkuedrB6MmEjeig7HQyBPx83JJKj75Q7XCZ1dkRXbVP51mm15dXBQMne8yWEScZ9G1XHKZV8QbYYyqgMUygLJUvLJFgeXA3m4R8hZDaSxqQLzGPuYzgUAhVGrHLLPTX5UwZPm8ypSbt6GF4Hp3sDgzLbVgGybyC2WAXQFV1hafZiJ1BwpWRU3kcPTh5erdbhz451DfgtDJMueJHjU3rn6ReSEF8jPNyiSgTRCddsLLuR8T3YwZ6Yc6rZNszSYfjdTd7rQLnR",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.653)
```javascript
{
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:05:58.655)
```javascript
{
  "id": -576460752303423465,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 20:05:58.655)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.659)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7qwpq8BRQ2zo2eehum3xj6XGqF45iTFXVgjZk3g1EysUZCvmgFMQifAZFfiuNNhUcJMuUiRSpmSmUN1RRLTEyJNL9FJ26rPcntmxSnfXBFP6hLFq3z1NWCwjAPsgCSZx71Rgmj1a9BjwGhbhBXRDiVy7yX4JM3c7"
  }
}
```

#### responder ---> (2018-10-16 20:05:58.660)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak57fisGZ1D88aQnMXqJhRVdo7DKe82w6EmyJbXxnZc76a4NNQ1YkFUVVFdZjbJVcFBcF9VSRRcNga9pGfoSwjvfq6po1tEwAAajHK5HZxoTrRd79Akm5nyCfYh2HFTqVrFodMWEPZFMtjuQH1ARme2n9oCnhwJap6EEZ3RurR8g6PWxVntV4VeUa6BxhFMDdPAEdCZJwpUyVcEu3rSqid9ygj7EnEJdVL3mwUJ66aXn7eszaKodNTHNfZikq4778qMWBrzsLBQyKEqqM4EaxMXr6omWk4U9hL9wYCTe8AkNfUKW2"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.699)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.700)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMJkUUYge7RZXaix538gN7mBPhPQjzWxgakP5mceVsQfp7qwpq8BRQ2zo2eehum3xj6XGqF45iTFXVgjZk3g1EysUZCvmgFMQifAZFfiuNNhUcJMuUiRSpmSmUN1RRLTEyJNL9FJ26rPcntmxSnfXBFP6hLFq3z1NWCwjAPsgCSZx71Rgmj1a9BjwGhbhBXRDiVy7yX4JM3c7"
  }
}
```

#### initiator ---> (2018-10-16 20:05:58.703)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4kCGdPYE3YrUUkgiQwufT1Aj3irkC1ztSMTS5qMxqTimRBu2gP46bpgQ4iSogBATFc2AbQ9VKMusQbVKqfVnJXeWpXhDijw8QvYyYLddQoCJyCh7L49Fde24NfXk3NmLgkuXqgjXUTn4aiHyGs93t469YGERDUPsjxsQbUzpDESFpJxggdKJWd6KM5joHc9itDbG4otuhsAdEW4TESSBodJxUNFDL5gZzCqa3y6JmpQcqPGTcZbdz21qFcFUTVgrGMG7jZb4dGZaNgqnD5E2J9mwumkxiV6WZjNucyMeEKUmg6H"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.717)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkJpcbapJxZPa8pBWgnXNHbeaHQAFJAkLMckP59UQQ9a4mNbn2vZmkf6ah1jwpUANmNxXyCRi6tXyFAcUs4QQCfa3BdwmNm1te5YFipVfkZq9XJrQAS2Pz67Dzn5WZTyp2VVVHD2Sxe4JQzgCuzC5WS5szPh4zCoix7GVmtZofkhU9r4QNMeKSspdKyzCvqgCfGe5CMLtTK71LsJSyW3czbzB5ZnrmkHq6CryRbSaWhoZa1gQpY7UJDyqGJYsP9ocjA1guMefKBnx9oYPrBTX3ew6VJWhWg7C7gihHWjnbyAbUKW9K7Q5RAPWKwHcUrVn4zmLoDVCBBk8GB52qY7gDLiK56ReoBhpoTPpBUgXv9va9ksUuEgKfXheAPxqXTSPhD1DVEeuB",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.719)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkJpcbapJxZPa8pBWgnXNHbeaHQAFJAkLMckP59UQQ9a4mNbn2vZmkf6ah1jwpUANmNxXyCRi6tXyFAcUs4QQCfa3BdwmNm1te5YFipVfkZq9XJrQAS2Pz67Dzn5WZTyp2VVVHD2Sxe4JQzgCuzC5WS5szPh4zCoix7GVmtZofkhU9r4QNMeKSspdKyzCvqgCfGe5CMLtTK71LsJSyW3czbzB5ZnrmkHq6CryRbSaWhoZa1gQpY7UJDyqGJYsP9ocjA1guMefKBnx9oYPrBTX3ew6VJWhWg7C7gihHWjnbyAbUKW9K7Q5RAPWKwHcUrVn4zmLoDVCBBk8GB52qY7gDLiK56ReoBhpoTPpBUgXv9va9ksUuEgKfXheAPxqXTSPhD1DVEeuB",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.727)
```javascript
{
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 400
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 700
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:05:58.794)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- (2018-10-16 20:05:58.803)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "tx": "tx_2M9ipLgcYxXvXrauiM2uwr1VUqCQZnuTZvSeDrkVYaqyGdGxV1ni6toLf3fEAUBxjK2Q6CvFzc9jGBS35fGr4HfqSexDpCdvuq6uE7ZRM6pHS5R3gx31D"
  }
}
```

#### initiator ---> (2018-10-16 20:05:58.807)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8a1JbJTSxXpRK7pA3QiYrgz24uFw8hmcJkgxXoKtqHbrGhmwyaEpgnj6wTKX9dfw6Dx5hqiVn9du2M35XWTgH9wwsYKxEqVzwej3kQKZC6vGtAiGoD2gwwSnYBmEsasKsDcjPoFGGpFbUf3XGpix5nRS2Nub1Y4SvA89zzm4ZJ1tG5Uub2xRYWN6cH9ZMWEz83gv4bSftUJFtUnDm"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.809)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "tx": "tx_2M9ipLgcYxXvXrauiM2uwr1VUqCQZnuTZvSeDrkVYaqyGdGxV1ni6toLf3fEAUBxjK2Q6CvFzc9jGBS35fGr4HfqSexDpCdvuq6uE7ZRM6pHS5R3gx31D"
  }
}
```

#### responder ---> (2018-10-16 20:05:58.810)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8ZysmTsgYFecGMjhEyAzvJ8uewud7M1GFMxkPhiw28TskdS6hP9BHfz3oKBTbe6srknbdrKfhcbuqzTjCi9RyGHRAwGEhaRH88VaA4h6aLrPLcYPKEaQ7sKs6EbLTTmHGoBen6YzJNL4rWTjtiFSjsYd37pTuHixB2zq1Bn9XfyrjKwok55tRZRJPNUznktBCxF2q8QVDTk2m1hjY"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.813)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1Y48c1YrtHQDa7miK1LqTvPxjE75nwetTzj7zRkURubshYQkdvvFtqYdQwpu3jd6dpMwbsE3TFuuj4STSRzpyo8SEiwjehQDuuNUbuedw2TrDd5DE4kbWK6Gbh45eyWa3aet5WpZqh5mRttjZ4qP28o23YsjGtaTpP6nNohLeRqAHEUDnjRC1GCukLQzv8p5T2BUACxcEaPdFw9oWQKuAgbvNjDq3eTeJ3kMd6YUBY92r8tF6HshyLbFuKHUVgMHBPbfUmUevV8rDsx4ZsGqUFodAmTNYBUAcGKYCFH1cP",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.814)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### responder <--- (2018-10-16 20:05:58.814)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.822)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1Y48c1YrtHQDa7miK1LqTvPxjE75nwetTzj7zRkURubshYQkdvvFtqYdQwpu3jd6dpMwbsE3TFuuj4STSRzpyo8SEiwjehQDuuNUbuedw2TrDd5DE4kbWK6Gbh45eyWa3aet5WpZqh5mRttjZ4qP28o23YsjGtaTpP6nNohLeRqAHEUDnjRC1GCukLQzv8p5T2BUACxcEaPdFw9oWQKuAgbvNjDq3eTeJ3kMd6YUBY92r8tF6HshyLbFuKHUVgMHBPbfUmUevV8rDsx4ZsGqUFodAmTNYBUAcGKYCFH1cP",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.823)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```

#### initiator <--- (2018-10-16 20:05:58.823)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_21UBAUstAMB3cYYeGTrAVxiGq2TqLuFQddWboFy42CBEkYfL1"
  }
}
```
