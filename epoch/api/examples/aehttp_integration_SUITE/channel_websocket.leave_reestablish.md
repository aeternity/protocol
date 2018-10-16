
#### initiator init (2018-10-16 20:06:03.999)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder init (2018-10-16 20:06:04.6)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### responder <--- (2018-10-16 20:06:05.4)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:06:05.5)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:06:05.8)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1KPCFWHV"
  }
}
```

#### initiator ---> (2018-10-16 20:06:05.29)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HjyBr4huJocRM5B8BR1oatBDoqBnfzyuuzRcrisdU4g62V1HUjpqHQ8d9uxfKfu9SptfHttB9cUZUpdVgDa2s1u3rdr6XSWutz8L2Tn3RYYXiSypJiAijHb6HDmi8Bi42mBAvCXBk8pr3QNPfKDRgJnGHez4v2xJnjh2hpVZSs5yYvyJCsfz5m7rE29eo129dm5S7sBWh7tA1K8N1mK1h8fgriZSJN86Hr7yxr32R4RT6cTHNTGef7w7ggMjmzoix"
  }
}
```

#### responder <--- (2018-10-16 20:06:05.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:06:05.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1KPCFWHV"
  }
}
```

#### responder ---> (2018-10-16 20:06:05.31)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hjyyx7jRszco1YWLikTZUnZvCogz9qQp6VyEUe6KR1cfHPPNKot6hPR52K4iHHf3v5Y4LExhoPUMdRcAf5gazJ2neM8bu4Q2H2L4NzUeFtFg3Qg3rNSz2TLTAq9SCqm9HSyVhyaX6cKd35WjwS3uB2sxy7gsdVGbd3NofspQkbXap5pZwJsSmN5Xrix2q5Lw3dtyjPCGDXp1wSLWQSEzabzhi7E2HrEyvcuB6J5sbkM1tpCxYvGfVJYn11DRJX56G"
  }
}
```

#### initiator <--- (2018-10-16 20:06:05.32)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:06:05.33)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe"
  }
}
```

#### initiator <--- (2018-10-16 20:06:05.34)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe"
  }
}
```

#### initiator <--- (2018-10-16 20:06:05.289)
```javascript
{
  "id": -576460752303423452,
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

#### initiator <--- (2018-10-16 20:06:06.874)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:06.874)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:06.875)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:06.875)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:06.880)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:06.881)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:06.882)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:06.882)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

##### initiator: (2018-10-16 20:06:07.161)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 20:06:07.161)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 20:06:07.161)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 20:06:07.161)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 20:06:07.161)
> Channel is `open` and ready to use

##### responder: (2018-10-16 20:06:07.161)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 20:06:07.193)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- (2018-10-16 20:06:07.197)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "state": "tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.197)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "state": "tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.197)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.198)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder init (2018-10-16 20:06:07.236)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&offchain_tx=tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe&port=12341&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### initiator init (2018-10-16 20:06:07.241)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&offchain_tx=tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe&port=12341&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder <--- (2018-10-16 20:06:07.246)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_reestablished",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.246)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.247)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_reestablished",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.248)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.248)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.249)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmN9t9TvkkhpssPYpVQZ8b8yhNKDyyzVjmFEj6BUKZ8ZqjSkgyZkyM9ugFnLiSqXsa1o4dr77NMMWJDxmqwNeVhNY97nb78WLycHNHcUFrzpwirsqugcoLhsKQFVstFj6VBGnA9jC2c2d3UT77efeh7LinApBY2tXPPXAtzmLhwk46CEsfYgvihoPNwwPvePJdDBMvRnifXJdvyt7aq1b1EfUAYujZ9uBgHqBrWNVcN4aK2xkijFXjytGx5h4NmoXMyHM6AXQNWBfvT6CmRpb3PBsPf4n3RD5mAUDbMi5TDmZX9sR2uGYAuwvATBPwxhSP9KKmBMmmsAKtDUgQu8J17FQzWe",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.280)
```javascript
{
  "id": -576460752303423451,
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

#### initiator ---> (2018-10-16 20:06:07.281)
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

#### initiator <--- (2018-10-16 20:06:07.284)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1onu2HraKHZLn2nR4Jvvj9tD6ZaRZnS3SSTVKe3yJcqGsa6D8HpY1SAxXasNPU187Jo1tScqtN9XQxF2TcSJDd9YVjjwdm8W2kv2qN4oLMNin3bGYKjUkyeyF9jr8tQebCU8MVxhTBSeQuuEnJ8NarMuHagSszb4k"
  }
}
```

#### initiator ---> (2018-10-16 20:06:07.286)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4stCZzh9SFETcNHqAFZs3utx2gTMYbHftchr7cGt6tHMYCE7q7niP2DpmoU28ksbWLKzRVvQzEfhmTodY2VNaqbsYSwFHTuq5RR1bBiRgr2ST8WAdUtTzpFGGC9Abkn9Ao4BAgy3UygLK9Vmw5wpcAnoccRWtZBSei61boYCiz6HRTTW2i5s6SJHsgf1KeZuYD3EC3TF8eQzJmUwt2KW99pB7HK8Ey8TVNgrJa6k8sjiPUVwFRdHSr4hKyyUdFGqforkgAkfES5EYnYH5ZWFgBJ5uEfPhZgMe5uijZvDJfEKYJj"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.290)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.291)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1onu2HraKHZLn2nR4Jvvj9tD6ZaRZnS3SSTVKe3yJcqGsa6D8HpY1SAxXasNPU187Jo1tScqtN9XQxF2TcSJDd9YVjjwdm8W2kv2qN4oLMNin3bGYKjUkyeyF9jr8tQebCU8MVxhTBSeQuuEnJ8NarMuHagSszb4k"
  }
}
```

#### responder ---> (2018-10-16 20:06:07.292)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak52jBs4X7EoDTC4KMrQz9tJZ4Z47tbuWT9vR5XdKU4CewpTifGy7zciLiC3tgUqSc4FvEBoLc86kDjd9AC7WT2SbbYHvbtjQ4pzJSTdq7vULVaq9Nyu6PvxhABwRvSAyA3T7cCEtGESurVdgFcufqwbtwLscorspbBX6VNMohkrrmpFpLSEPJaZBukeHSx6jvLSMcCncxifRi6wq4xR5wsnWEjJVUgF1RLin7jBbq3qCZogeQhWNJPcwjuozT3x5EGxkuUYLKnuDjKUKAAWYVPntWSVDf376VVvf1S8LFuGzDV83"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.297)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkY3F48BwenZnnDPG7BRKtWdthv8Nfa4mNa1pq7HpLMnEF3gvNShrXkBXhYrtUUg2iLjNoS4bTqGfQcTY6rEaCY7d3PBAk3ZxVQcVD7FiJUkuriKAunosN3Cuqq56z9kXeyPgER6tDFqQsdYYPcXaNErhTdND3B8qdKcNjb7ebdijGyYX9XXLwqS2tAok9UwEAsyGoqfM3DYsfnDSs6QgntgJuAZqcF3ratXWQHEhasNTeMWjqXaS7K41AmEn7wRhoCXp5JJQG94WyD5Lr2zVbPk1JG1m5GsNuepVJJWUSHeX7rKWvoGhYcxdmYgnHBWgMTq6PjFehc3JL3SrzWkoJyaxMYvwnnYWsrtj6RzZv7Nt94T6uXyzQ4GP8S59JTNx2mSPx6c5F",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.298)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkY3F48BwenZnnDPG7BRKtWdthv8Nfa4mNa1pq7HpLMnEF3gvNShrXkBXhYrtUUg2iLjNoS4bTqGfQcTY6rEaCY7d3PBAk3ZxVQcVD7FiJUkuriKAunosN3Cuqq56z9kXeyPgER6tDFqQsdYYPcXaNErhTdND3B8qdKcNjb7ebdijGyYX9XXLwqS2tAok9UwEAsyGoqfM3DYsfnDSs6QgntgJuAZqcF3ratXWQHEhasNTeMWjqXaS7K41AmEn7wRhoCXp5JJQG94WyD5Lr2zVbPk1JG1m5GsNuepVJJWUSHeX7rKWvoGhYcxdmYgnHBWgMTq6PjFehc3JL3SrzWkoJyaxMYvwnnYWsrtj6RzZv7Nt94T6uXyzQ4GP8S59JTNx2mSPx6c5F",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.303)
```javascript
{
  "id": -576460752303423450,
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

#### initiator <--- (2018-10-16 20:06:07.304)
```javascript
{
  "id": -576460752303423449,
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

#### responder ---> (2018-10-16 20:06:07.304)
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

#### responder <--- (2018-10-16 20:06:07.308)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1otKY9Q7nUu4hnmxBD4FS7daLNYoQVbPwdioox6TdNpxyyh1nNEZeg8eWhuTACxfyuJQhn5q5MF2qbjeGWg5hLCtMh8FCd9gxL76iCwz5jJ96G2ffATo8Bn3XvHP7qBkNYC6rhoQRmh4Nh2ycxNZEBNb7u4Cm5Min"
  }
}
```

#### responder ---> (2018-10-16 20:06:07.309)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4zh6CoYv6gsfbsGQQoqzAYhxEjEEzDf16b2S2JuDXvnCn4icmzi1cygC8SCniXa7uZF7PvuL2GACDNuKaM8pZbtqgjM9WdeYHQuWUyLvnN4ddnvgpTTqTSF1CVmWsW6hvUEz66V7h5pzHtGAEmTYSH7hLNRqqSPpH4yMdqPBKVqCKBwozPh9R482bbqTgBLFa2LugsxyYrkhwKkUaauWgs2T1zqV4ZyQq3aJE9dgLGPF99wPaNLT4T9xEZyvhkmt2X33KMyTLc5CdqhmeTaJxQMiboYbwgqbV2gmb1TtxqzBorh"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.347)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.349)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1otKY9Q7nUu4hnmxBD4FS7daLNYoQVbPwdioox6TdNpxyyh1nNEZeg8eWhuTACxfyuJQhn5q5MF2qbjeGWg5hLCtMh8FCd9gxL76iCwz5jJ96G2ffATo8Bn3XvHP7qBkNYC6rhoQRmh4Nh2ycxNZEBNb7u4Cm5Min"
  }
}
```

#### initiator ---> (2018-10-16 20:06:07.351)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4qPnDoiyaXQFQ31uyvm9XUzK1ptELQKnqJfLK2fC4zeAjo35WYE6yRtR6eiHrbRcyXknVg8CgtLfLuSn5BaZyv2Dgab7JNULu3WbLk7CHLXEw2vswy6iz2Z9VpR483qns13whEC1H7n5Hbj5G3FMnSPtwajSWkjuznyAvHJBj17NXUgZ2inu8hg9UUy2s6guhEG5g5aQCYGQTwUTNcfcg9ZCtxv9opHLxXJsgQMuvhEyFJiMXWVvrKroCqD8aqxEwdG28wW2gEjLwfnWUXP3gPXXcn1hBCbaawkgZEAGfY2zwyh"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.364)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkTkxhuPHR3ekauZEBKwT69RSyQ9MPGCrSCwsD6wWQh5GqX4vAHWazyNtZaDGCExcnvFa3TPKo3L49XHJZgvEX5w3CaVHWckSU26KnUsmVyuh8dRbJuy1dNY23vJvVXRXfz6iJdYjLHBS36P5eSboyivZ1FfPnaGP46EWyVo25QXZwTEuikRBwNPeoqP24RNxSmcN9URmGudXaoc6xuX3ryMV1on27Ejx6ns8duXQUQz3yQK9urFN17WqQfq2DKb3ihEczSbRsKTFKzyc7oPvsR3HbCmp5nPRCi3NBVrYyUt2tkCir1mNarxvgnxTtZRnJqwmkvHN14wZwwiXTWX4PXfTjksH1uqaygSmAM8fMMtAojKRvkcAdaeFD8DxExcPdixC5D6td",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.368)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkTkxhuPHR3ekauZEBKwT69RSyQ9MPGCrSCwsD6wWQh5GqX4vAHWazyNtZaDGCExcnvFa3TPKo3L49XHJZgvEX5w3CaVHWckSU26KnUsmVyuh8dRbJuy1dNY23vJvVXRXfz6iJdYjLHBS36P5eSboyivZ1FfPnaGP46EWyVo25QXZwTEuikRBwNPeoqP24RNxSmcN9URmGudXaoc6xuX3ryMV1on27Ejx6ns8duXQUQz3yQK9urFN17WqQfq2DKb3ihEczSbRsKTFKzyc7oPvsR3HbCmp5nPRCi3NBVrYyUt2tkCir1mNarxvgnxTtZRnJqwmkvHN14wZwwiXTWX4PXfTjksH1uqaygSmAM8fMMtAojKRvkcAdaeFD8DxExcPdixC5D6td",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.377)
```javascript
{
  "id": -576460752303423448,
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

#### initiator <--- (2018-10-16 20:06:07.380)
```javascript
{
  "id": -576460752303423447,
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

#### responder ---> (2018-10-16 20:06:07.381)
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

#### responder <--- (2018-10-16 20:06:07.388)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1oyk3zwfFgEndYmVJ7B6Rtw74vzNUUHJ53mhRsaDK7aa1TxRu35vuL5PfoM9wwjm5awNLH99WEVemtADyDvxMGD1fv578CiQN1UaxbJwWDtQLZhEUbtvQKtpp6RFaLGp43gSM8JdXbw1txasn1jYwxbP42yYJYfaM"
  }
}
```

#### responder ---> (2018-10-16 20:06:07.390)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4vhajLREjJNp155aJfS45byVWWwVZRrANWVPdKsPDdvT5xepZw8V6YVASm6BgvyN6JzNZST1ypQ5bpNjp3A8rjEAZ8Qc2Fx8YAdJMBvCKgHQvoonu8HxHdjDyZZ1JsxqS2nYHCc3U3VYzazigj9yzA5uxqj6pgxp5JjHjMSC98NsTbNYScsya7QXy2DnCfjdCQkrmFEw8HdX5Nb7uuvVEhQvEEUkXwdcELVL2XAwV5wEa2S1FBy67Ubw2kVRTzCgwb27j1BPGvfTpM9WgseWcdex8p96vC44xy1GRNzUZLVMHd9"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.399)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.400)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1oyk3zwfFgEndYmVJ7B6Rtw74vzNUUHJ53mhRsaDK7aa1TxRu35vuL5PfoM9wwjm5awNLH99WEVemtADyDvxMGD1fv578CiQN1UaxbJwWDtQLZhEUbtvQKtpp6RFaLGp43gSM8JdXbw1txasn1jYwxbP42yYJYfaM"
  }
}
```

#### initiator ---> (2018-10-16 20:06:07.402)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4shK169YASuhZPjQJKF4cyv86dSkBQLYbyUbu6F6knZEuoGBxpNDunM8LYks2auNZmDci9eVYDPopvMRgvfxpVGLCg3J7mste2JAWEVX5E15NgmYZJoX8xFqeQGiGtEX5Fgh5F7RdoZhqjPwJ6eQHNETYpGVSqqVicsNDEHwiKGw3JLNw7si4HDHPW8qhejDQsJeuXTrRNHgRrFokxKxoKHfcLSo7F76XxUhP9wPfCoMcpyU6LroAScurbYv4zZ18Q2rBo3mHtVkzA6NYh66HPNKEr67zbTnQzdpF7JtTZ2xnQm"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.409)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkXiXHSv4QvwjyKnDTkeQGA95Z5p4DBQX2rbngxRB4E55fhygBTBot5P84PuKKi1YeWq1WKiKFWrSJ2K6vnwpc9vmLrn8Dj7BC3PiPvRNq58TZsGExr21RTmoSHGcjAe1t85DJHK5HdFkRUmWvQZ4V4UZKKqm2WYFWh5Cp3my4suPXQ43c5rvoD4zFhYjJD3DjkmJGWpwQpNWUtztjJi1bgUFEEq6fFuCGbue6GSw8JSGM1jT9hqtinnvPVGt5pkvUfJ1HfpKfH4mL1LETn4YreHiomxJakRsRTugAFMa9wkr4BkJ5X2XJVejHSg4T5y3vYiw3F4XF7MFBiMgPNvAAiCxeUpsNC4ZspuBMuiwRnYMJC1MRKDqswCnuXpnaJZ4FFFQj2XN6",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.410)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkXiXHSv4QvwjyKnDTkeQGA95Z5p4DBQX2rbngxRB4E55fhygBTBot5P84PuKKi1YeWq1WKiKFWrSJ2K6vnwpc9vmLrn8Dj7BC3PiPvRNq58TZsGExr21RTmoSHGcjAe1t85DJHK5HdFkRUmWvQZ4V4UZKKqm2WYFWh5Cp3my4suPXQ43c5rvoD4zFhYjJD3DjkmJGWpwQpNWUtztjJi1bgUFEEq6fFuCGbue6GSw8JSGM1jT9hqtinnvPVGt5pkvUfJ1HfpKfH4mL1LETn4YreHiomxJakRsRTugAFMa9wkr4BkJ5X2XJVejHSg4T5y3vYiw3F4XF7MFBiMgPNvAAiCxeUpsNC4ZspuBMuiwRnYMJC1MRKDqswCnuXpnaJZ4FFFQj2XN6",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.415)
```javascript
{
  "id": -576460752303423446,
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

#### initiator <--- (2018-10-16 20:06:07.416)
```javascript
{
  "id": -576460752303423445,
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

#### initiator ---> (2018-10-16 20:06:07.416)
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

#### initiator <--- (2018-10-16 20:06:07.420)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1p5AZrVCisaWZJm2R1HTiVnoJEu8miVjpgcABQVEMq65x2tTUJNdmQ1BzsCUkgLPQMhtmwnoB1uPDoWmZkCvBR9vSQaXQVpeFo2VaX9fbq9WWxasiCnat2cHCogw2FmcB3WvWADxAZ6bKzi5hTnSSY2FZZQH9UaYW"
  }
}
```

#### initiator ---> (2018-10-16 20:06:07.421)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5BZvpYosakeB8rUZPgZZtSwZQd99txAx7W3o5Ds28D1U5KnYjUyNF1CMscGMWu3czTAJgcwh5k7218nPbmfntdb6gNmFgRykTYuk5N5oK4JYJwy3TpYYwz2kUBg9S6jznNF5ccBvzSgxVwhrzHQbAkvKmG8Dc6mXKgp3SnoSAhjF57HfvJbbWf16wL3jgvnC3cQQXzmEEPUKEYKZ2r8tdzTYGjjF8QrZJeaXuppk458t4r52p2EVuVs2a3ideYW3HaJNmL6TEtF7pGFZ8NCV3Nczhc1KJ7xdn7F5b8bHWN2DWcF"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.447)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.448)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1p5AZrVCisaWZJm2R1HTiVnoJEu8miVjpgcABQVEMq65x2tTUJNdmQ1BzsCUkgLPQMhtmwnoB1uPDoWmZkCvBR9vSQaXQVpeFo2VaX9fbq9WWxasiCnat2cHCogw2FmcB3WvWADxAZ6bKzi5hTnSSY2FZZQH9UaYW"
  }
}
```

#### responder ---> (2018-10-16 20:06:07.448)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4znRYhWNzpZaaxjfgHeWnDkRdoXWZHVwpKEHgCqQxQjKQmH3GY7LE7pM1poFgP3cdoKzvtsbNj3un8rinogbJTZrBcrzToe16xzeKvGqY798qUkGieTCHiSQeUW77jZcydQD5NFK5HexbpB8Yx3gcXKbH6wDqa2gNGvXeNDsNxyqeJvgM6JUa8KdzAeZEsS9Z2zFB4FatTDEorRKe8mpdMVRGyBKN7d7y3es94SEFhkuAekuJCGBgdtqKJpRRKYsAFmEfb6wNeTVaZGPvKgNvXzzmwtQDYMFenDR6V6xpn3Qt7J"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.453)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkjuJ4TQEK3ErFNwjG7R57eWrEjQk5N5xmyKWgnSpr2mSbwafupMi9dxkDuKLXykTTymLq3XBpbxrw3mn4XmTY73CLk76qN275chRMEaSxmiiNGgfnJBnDzzNeqhStwX3RxVeBnQ8tdE7paMRnkjM4aFY8ZupYCUZzM2P9rpSRgwp5mSG2EMHknbKJw3NF91QKsKTUB24Lk4FSWZh51P75RzcfhTtdynuDeLZCRAxpKWN8HYvrZviy1HRwHqjCfGdwsRvwbWF5fcbjyM3oMz1iwG67V3LLk853HWcqvnDsgPK9Q1PAu2r7Yw8AYepvZc2bpT7PeUquKFvjL6vcV8ewrSxm6n98MY4N3CXQzGx8RwN6Fp5RHsTzv8MAa7wQcw7fJcwWKPRL",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.453)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkjuJ4TQEK3ErFNwjG7R57eWrEjQk5N5xmyKWgnSpr2mSbwafupMi9dxkDuKLXykTTymLq3XBpbxrw3mn4XmTY73CLk76qN275chRMEaSxmiiNGgfnJBnDzzNeqhStwX3RxVeBnQ8tdE7paMRnkjM4aFY8ZupYCUZzM2P9rpSRgwp5mSG2EMHknbKJw3NF91QKsKTUB24Lk4FSWZh51P75RzcfhTtdynuDeLZCRAxpKWN8HYvrZviy1HRwHqjCfGdwsRvwbWF5fcbjyM3oMz1iwG67V3LLk853HWcqvnDsgPK9Q1PAu2r7Yw8AYepvZc2bpT7PeUquKFvjL6vcV8ewrSxm6n98MY4N3CXQzGx8RwN6Fp5RHsTzv8MAa7wQcw7fJcwWKPRL",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.459)
```javascript
{
  "id": -576460752303423444,
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

#### initiator <--- (2018-10-16 20:06:07.460)
```javascript
{
  "id": -576460752303423443,
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

#### responder ---> (2018-10-16 20:06:07.461)
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

#### responder <--- (2018-10-16 20:06:07.465)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1pAb5i2kC4vEV4kZXuQnRTYAY3sWcRf6KssUfiXigb5n4SVG8NnfQdxsyzEZXRHwGxDHbHFnMzzteT1PNeShf8DGJMxpyMqqBNDZTN2rMD4vqB2JhGKgAcxvyRtAbSzKnszkrmm44SoTJkzokxADXmeNzQeVQ5FB4"
  }
}
```

#### responder ---> (2018-10-16 20:06:07.466)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak56ThE5SPjdbeuPcRohrTAEuhbfvNhLg4aaxdXD9puKH1WjACdh48oRMiRX6baRx8ef6ADuunnJWmDZykgzw5aqrBPLuvnxJG6Nzjqdmdiz6hMjb3RMj7Cp5WkGABm15C4nNGHuE185zA8Sg9ToLxtctfN3KpKbZyqFywPaFAcWmAXH8aGsreF2bt19EBZkBAZ7zHDn67QbQ7Q4nnn1WU5imstfKtHNPUnDYLv9JFQ3CaqfUrpJBteyFrmpAYhR9GBpMTjbH8Rj7QDAYNxGsy8jb8qJKKDAbdsNBQ23oPMPdvz5M"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.498)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.499)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQPPgUoFm8zAfod1AAfCk91vmQMyuvW1TJdjZVfGCX11R1pAb5i2kC4vEV4kZXuQnRTYAY3sWcRf6KssUfiXigb5n4SVG8NnfQdxsyzEZXRHwGxDHbHFnMzzteT1PNeShf8DGJMxpyMqqBNDZTN2rMD4vqB2JhGKgAcxvyRtAbSzKnszkrmm44SoTJkzokxADXmeNzQeVQ5FB4"
  }
}
```

#### initiator ---> (2018-10-16 20:06:07.501)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak51aBZ7bNVHv4sQTTCtoSSnUHsi9wMVbqqDngCwNVR5x8qU9M24Lr4pho51jSjGqwoMYkUC9hLj4gYe5WFchEzCEt6pf2UpeqELCveDH1TY7YYtV5y3D171wNUk5rKXAKHcMzN7P5UofAW3R3YDwPgsU4mvU1x5PriqxeQ7J4DC2cfaVfaBbiJrmArjRfZW8JXUkrCw72T3oQtEPeEdnS6S2XmQHkxBPpvgjiVW5WcuZdSYdTvDYdju5DGuVsTeaQ8YvwhDhqe4suH7TMvc54yoDwMpgniCpu3X5oWr1XMkHgHe6"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.509)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkmFxk7y5Y21ZSr2CYyxPBE9RRN23WsrdusbgD3SPkH5TGiJzY2crTTJ7MeDdNE1SZ2j3c9KgzKc4mDeDNHfY5dDAczefejWgtiVmiR2LdQBvmkT2jCuu3EfeY24bEjyKDahLpeoRwP745gfFt4MudN7xEhGEQoVq6hSXxfh3nsFvu6ZzfFvUd4nf8S42xxdAZDHTsZxGAj3572GKVib9XbE4xkg6UZexim762F5T8TSqoVYPreLc3f9kqAbMGkGWz2QKA3ds6FFQa9z4aFLG7VVTsCVvHZ42kS9Fa6ryLtLwcHuPtFXiY8pULxpyYhWn7CzWvV9VwernXKgYR23zpQjkbeBf5SktJ1iRoHLBJvPcYNvB9BTKx5iReZxsUXRPg12J5g8wB",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.511)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkmFxk7y5Y21ZSr2CYyxPBE9RRN23WsrdusbgD3SPkH5TGiJzY2crTTJ7MeDdNE1SZ2j3c9KgzKc4mDeDNHfY5dDAczefejWgtiVmiR2LdQBvmkT2jCuu3EfeY24bEjyKDahLpeoRwP745gfFt4MudN7xEhGEQoVq6hSXxfh3nsFvu6ZzfFvUd4nf8S42xxdAZDHTsZxGAj3572GKVib9XbE4xkg6UZexim762F5T8TSqoVYPreLc3f9kqAbMGkGWz2QKA3ds6FFQa9z4aFLG7VVTsCVvHZ42kS9Fa6ryLtLwcHuPtFXiY8pULxpyYhWn7CzWvV9VwernXKgYR23zpQjkbeBf5SktJ1iRoHLBJvPcYNvB9BTKx5iReZxsUXRPg12J5g8wB",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.519)
```javascript
{
  "id": -576460752303423442,
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

#### initiator ---> (2018-10-16 20:06:07.616)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- (2018-10-16 20:06:07.620)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "tx": "tx_2M9ipLgcZ9HQpdkaV9DeDUB93zzgx8b9LyyP8QELMU9t864LtKwyPppTfSS6tQaqwviNzanytVj9MsZHcERqh9QSnyWdxnaJTHbiA6goUCW5pFhGc9fTQ"
  }
}
```

#### initiator ---> (2018-10-16 20:06:07.621)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8ZyYzBQtv5rGjjeremigMXEChb1vFmCyRPRrtAjp6n89J2RmpATHQBoVpGvf8Xw1whkAZYB3HYgi3KRwBVNjayKoHzQYFf29Nra4iuEqk3MVzWkWroAhJDbZyhd6EH3ezXB1LUyTy3Seg4ceA3b286Ut2YXugQYkBEvB7wiVaDQyKdRvhuKyAQTHFikZ8bhGLPr5mZrhH2UQ1cNRj"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.622)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "tx": "tx_2M9ipLgcZ9HQpdkaV9DeDUB93zzgx8b9LyyP8QELMU9t864LtKwyPppTfSS6tQaqwviNzanytVj9MsZHcERqh9QSnyWdxnaJTHbiA6goUCW5pFhGc9fTQ"
  }
}
```

#### responder ---> (2018-10-16 20:06:07.623)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8ZzoPA3d3NPkV9MZ9aYNfTFWr1ByrdD92PYMJuUEibGtxLfHHGc2Ztu2pfrd4by1AKbsvGsdniqTLLTgX8tUrwADFT6zHMNBdyLohwBdHsAi4ProEwE1cfaZbSXByBMZV2erB47wk6c8Lhi1Ct17T4E4f3miVC5Bmj13UPpr7UduVp7rZDupzmVMkU2xtrKRzWz6Sz6QMKwVxnABK"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.624)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1XVqwdMZJT3WELPUHXLMKugsEAW6DBsNvDem9rHJC6yBuqtGFYESSgWY9vp64Bm7qT9WLJfYbcHbqVSEFHJLf6XDFNW19ycjFnAfPHkg5VYTxme5SZT4CSREAMCWt5F4oqSZbFaxrtxEwjTmbWViAe1nQc8AmFMXXJLvueKLr2x8Q4trFEWPZXRmpNfiGkrdszLCJJaMW2JPpkxxH3aMh8MbZ9izuHkmzj1dPvQtphFTe29QSQPsu3HWcLAouVmrJ2cxDiJiisfH6dhVkB73y42KSN5tyuLvDPeLCuMvW1",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.625)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### responder <--- (2018-10-16 20:06:07.625)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.631)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1XVqwdMZJT3WELPUHXLMKugsEAW6DBsNvDem9rHJC6yBuqtGFYESSgWY9vp64Bm7qT9WLJfYbcHbqVSEFHJLf6XDFNW19ycjFnAfPHkg5VYTxme5SZT4CSREAMCWt5F4oqSZbFaxrtxEwjTmbWViAe1nQc8AmFMXXJLvueKLr2x8Q4trFEWPZXRmpNfiGkrdszLCJJaMW2JPpkxxH3aMh8MbZ9izuHkmzj1dPvQtphFTe29QSQPsu3HWcLAouVmrJ2cxDiJiisfH6dhVkB73y42KSN5tyuLvDPeLCuMvW1",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.632)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:07.632)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_b55kKgMywM6LUaZpQKtDC129Nu2peESbbmyXD8WcrGpKvsKyX"
  }
}
```
