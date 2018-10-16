
#### initiator init (2018-10-16 20:06:26.242)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder init (2018-10-16 20:06:26.247)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### responder <--- (2018-10-16 20:06:27.248)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:06:27.251)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:06:27.259)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1L5uygst"
  }
}
```

#### initiator ---> (2018-10-16 20:06:27.281)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HokhLJicJNuJCkdc8aBLgdZtW4aLCLo3HPaSaR6pqzgF6B3oJD4GzxHfLZ9DEZyrNgWwg9Ngwr3tsGq5JdstpLQeAqvnCYrC2synXwK9jZGGEikj4neJsNtntN5B2f2MNT6YXojb1F477yzMqeGUaGtJsfeXqocZYGjYztSTaUeMD35VBxEhLx2k43CvyYMWf9SKpdfzKQEUZhHV1XbvuWCZhnpJV2aYYrHbt3V4orshDuCtiAKCDzUaFaVXTKhaj"
  }
}
```

#### responder <--- (2018-10-16 20:06:27.282)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:06:27.282)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1L5uygst"
  }
}
```

#### responder ---> (2018-10-16 20:06:27.283)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkEJQvbguuMDZvdvLNshsGo668wAwMHHPrxvhQUJqQ1jkBmU2J1b2uniP9XUZuHNQZvLAo8RzHgDu8KneNyDUtANVmKBganU4Bpf1rATpTNFVUCE4csDsxKma2fYyVT9jinGbzmzPWJaPBXpRUyHB2fzyvD46Q1U29bJ8Mb2pqpT5P7nfF3tc2p8Lx5PGrHJe5t49nBG5s49vnytDmazw9g5ofn4b1mpeMuLRZmECYMewCxtWooFA5hZ1yFu5Qdt1"
  }
}
```

#### initiator <--- (2018-10-16 20:06:27.285)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:06:27.285)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNbs7SRuZ6oZMDjQYGRXrQqfopUSywafi4EUn6Hfry69mB7jCgX5AabQwxi6nfoVMyGxXRgc5VFpg85iQ9mp5EF2FTJHTjx9PrGxSw4exgzdGKtCp3KYywzh7MHLi3RrdiusnFbEBQBdU6pMRWCuamHBdeAZnxwcPnvo9uoFB9kvFZgfrAfqiVLVNiUFShghokMiQN6xqG7WdHhbtTBMXbChtZMxpbS41prDYSyfw3VatCB3faHonFsE4NHRYDbydnsgBtKPtiYa8sSg7AUQ97NRivue6q9D5FMT3Xm29RU1PFW7fKQWNTtHAKBeY7qfxvgJyuV1K7d7LPEqv1HhgJD9AQV"
  }
}
```

#### initiator <--- (2018-10-16 20:06:27.286)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNbs7SRuZ6oZMDjQYGRXrQqfopUSywafi4EUn6Hfry69mB7jCgX5AabQwxi6nfoVMyGxXRgc5VFpg85iQ9mp5EF2FTJHTjx9PrGxSw4exgzdGKtCp3KYywzh7MHLi3RrdiusnFbEBQBdU6pMRWCuamHBdeAZnxwcPnvo9uoFB9kvFZgfrAfqiVLVNiUFShghokMiQN6xqG7WdHhbtTBMXbChtZMxpbS41prDYSyfw3VatCB3faHonFsE4NHRYDbydnsgBtKPtiYa8sSg7AUQ97NRivue6q9D5FMT3Xm29RU1PFW7fKQWNTtHAKBeY7qfxvgJyuV1K7d7LPEqv1HhgJD9AQV"
  }
}
```

#### initiator <--- (2018-10-16 20:06:28.289)
```javascript
{
  "id": -576460752303423408,
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

#### initiator <--- (2018-10-16 20:06:30.17)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:30.17)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:30.18)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:30.19)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:30.23)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:30.23)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:30.24)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNbs7SRuZ6oZMDjQYGRXrQqfopUSywafi4EUn6Hfry69mB7jCgX5AabQwxi6nfoVMyGxXRgc5VFpg85iQ9mp5EF2FTJHTjx9PrGxSw4exgzdGKtCp3KYywzh7MHLi3RrdiusnFbEBQBdU6pMRWCuamHBdeAZnxwcPnvo9uoFB9kvFZgfrAfqiVLVNiUFShghokMiQN6xqG7WdHhbtTBMXbChtZMxpbS41prDYSyfw3VatCB3faHonFsE4NHRYDbydnsgBtKPtiYa8sSg7AUQ97NRivue6q9D5FMT3Xm29RU1PFW7fKQWNTtHAKBeY7qfxvgJyuV1K7d7LPEqv1HhgJD9AQV",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:30.25)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNbs7SRuZ6oZMDjQYGRXrQqfopUSywafi4EUn6Hfry69mB7jCgX5AabQwxi6nfoVMyGxXRgc5VFpg85iQ9mp5EF2FTJHTjx9PrGxSw4exgzdGKtCp3KYywzh7MHLi3RrdiusnFbEBQBdU6pMRWCuamHBdeAZnxwcPnvo9uoFB9kvFZgfrAfqiVLVNiUFShghokMiQN6xqG7WdHhbtTBMXbChtZMxpbS41prDYSyfw3VatCB3faHonFsE4NHRYDbydnsgBtKPtiYa8sSg7AUQ97NRivue6q9D5FMT3Xm29RU1PFW7fKQWNTtHAKBeY7qfxvgJyuV1K7d7LPEqv1HhgJD9AQV",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

##### initiator: (2018-10-16 20:06:31.367)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 20:06:31.367)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 20:06:31.367)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 20:06:31.367)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 20:06:31.367)
> Channel is `open` and ready to use

##### responder: (2018-10-16 20:06:31.367)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:06:31.402)
```javascript
{
  "id": -576460752303423407,
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

#### initiator ---> (2018-10-16 20:06:31.402)
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

#### initiator <--- (2018-10-16 20:06:31.407)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmDofvabHhN2WNGNBrc4g2Dw1zwicq85nBpTMrnV1Bq1PMd1vz1dR9BnP3T5BQ6f8AeVMhdvs2kZxCohy1KvajXffDoPLV5E9AkRLmP3EEnGA8BtBdWVrmj4zKT3wAL1C3WQfXEXAAFxrgow2PcGZjwQ8XaUCbd3Xm"
  }
}
```

#### initiator ---> (2018-10-16 20:06:31.408)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4tMLGCu43aCqutDNQM3sf8pJGyMAYwcMjpHHkKJmXwJgZkXAWyKuDV7MnRWhrHFPFGwV5v8zbXQ5sFfZ5gGJMcxQmh7mH7WCUrGPTW5RqXzKFsbTWHBjCKoTTT9tFYpwBSCjgbA8AGaUVNXkHJY7GHxM21cwqt9LT9ZbuELHPPA6C9qFoZAuCqh8kw6333JyjjniiSKFncHvm6kyZQGbF3oBnmHq4Y3HfjhwJRPz1GtgMXckJiAzcTLFq9UAmRna6V2DdKX18Chy3WEy8UYBxz93iufjAz3FyV9vxbzfehJsFa5"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.413)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.413)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmDofvabHhN2WNGNBrc4g2Dw1zwicq85nBpTMrnV1Bq1PMd1vz1dR9BnP3T5BQ6f8AeVMhdvs2kZxCohy1KvajXffDoPLV5E9AkRLmP3EEnGA8BtBdWVrmj4zKT3wAL1C3WQfXEXAAFxrgow2PcGZjwQ8XaUCbd3Xm"
  }
}
```

#### responder ---> (2018-10-16 20:06:31.414)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4zg7UZzsnxbrWfyyeMHUmYAzfhSr49kfoxewuakkk9yuHqXDqwcY1wrBMKkevutA4w17CigjhouX5YeKpfW1iCMbkV5RGwLYJoufzVb44Dn3kh9Ln5BMV7XB4JDxpQMeybXk9STtrLt6VY8arZ4inD6wED39xG4AovJXJkuGpvNp8deMM2TQkwwpkxeyXnVrWkc3WdiqX6La4FdRgWnZbca6Eeb1UpvLQfDokoDwQiCnnMqMPMf91tMDiJqj64tf8GjYaQCr6rmXUiWqMDL71APEo4ttXPo8Cnm6z2Xnj9wXW7h"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.420)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkYqtVpHmz8ZSvMgbdX5EHaVUyk82e2XFC6DkfRohDLuRMC9pVDX8PvN59LxjiM2zt6MTpVJp2TKbPWKDCDsPsFJfspSp8SbbYSG3At2MQovqQW6YUFD8Xj1LTaUMwkQGePGNAh5U938U84DyudxTn3RjeeuNbCnCKtpXAPS4dC3BMTHr36GyKR2QohGnsHUufmjkMFMMk37SgAgpXLgh3VskFNy4BCvhkP2i8rDQHkqKtsGD5H251QL65dLk8nJ3WuXaxvS5iwt1NegJ8zh4tN6DZ9ssuvfA2KcXEhAnRqAsEhGYRqTzf3uCvNaPDGmjeFySLcraRQXppgwyXy7kXsqdfuZhF789fMFgnZxXiFNtJxytHZjkVAJGkJf5kvV9zAPMyrZ8K",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.420)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkYqtVpHmz8ZSvMgbdX5EHaVUyk82e2XFC6DkfRohDLuRMC9pVDX8PvN59LxjiM2zt6MTpVJp2TKbPWKDCDsPsFJfspSp8SbbYSG3At2MQovqQW6YUFD8Xj1LTaUMwkQGePGNAh5U938U84DyudxTn3RjeeuNbCnCKtpXAPS4dC3BMTHr36GyKR2QohGnsHUufmjkMFMMk37SgAgpXLgh3VskFNy4BCvhkP2i8rDQHkqKtsGD5H251QL65dLk8nJ3WuXaxvS5iwt1NegJ8zh4tN6DZ9ssuvfA2KcXEhAnRqAsEhGYRqTzf3uCvNaPDGmjeFySLcraRQXppgwyXy7kXsqdfuZhF789fMFgnZxXiFNtJxytHZjkVAJGkJf5kvV9zAPMyrZ8K",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.425)
```javascript
{
  "id": -576460752303423406,
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

#### initiator <--- (2018-10-16 20:06:31.427)
```javascript
{
  "id": -576460752303423405,
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

#### responder ---> (2018-10-16 20:06:31.427)
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

#### responder <--- (2018-10-16 20:06:31.431)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmDu6SS8qAZNEJ2MiyWBzjBgPEkgzfqF8h1igM6XVWb15U2cje63SnRk52a7GAqcg3EzkWyPrDjfTdTCapEANDEj15kme3wFL6KcQeDvQzABaSQKakMEB8wC4cDbU9GnHpr8e2SMs8rDGeb4mEGWkPGQpMtr3L9d9V"
  }
}
```

#### responder ---> (2018-10-16 20:06:31.432)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4pRNRbc4T8BorLDPqFCRL3pidSXvtrwQ3M835WW4Kxt8CCVnsZo4woKT2r2Zmqj18iWX6uHwPxMeEwuQ4G623ntzXQYgYjpyYZHdcw8c2Xwt2PUerWobrUNYgmmZuixC9uZHqFSLBM6CukiGN6pUvaH7bfQf1zrgCzE38qAcwDNyYno2y66VBfGYqmgK9RefV6nsTY6bbHVVUkEBi9eCaz8kmi3DzaNyN3TeYMdAkX6NuUYYo8R1pnAzUWjGvRUNr9Berk2Fzbcu8DLeDmiXx1JetsXArQuetmAmpZ1uAEQjGfJ"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.437)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.437)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmDu6SS8qAZNEJ2MiyWBzjBgPEkgzfqF8h1igM6XVWb15U2cje63SnRk52a7GAqcg3EzkWyPrDjfTdTCapEANDEj15kme3wFL6KcQeDvQzABaSQKakMEB8wC4cDbU9GnHpr8e2SMs8rDGeb4mEGWkPGQpMtr3L9d9V"
  }
}
```

#### initiator ---> (2018-10-16 20:06:31.438)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak57DFtZ6wZvJMYYSDwRshp1VhEZqUnS5UfBV82VQ1Sd3u9tKUH7Nj9ibyrPFMeBWREqKvW9PNXrzHPNAZfSGKM8TmzxVqe62Axe2atHF3fRnoofg69zM1t2aSA79b3LYJHdxijPzZeSMsady6HDpXLmKLZ6EMVEvXi5uzHjCDGZ59Hbgj8cUArgPdfyFpYgEfNarvN7AixHsB8nhE69yyDVRQbxg36ebJC1JgoeHcVsocH5ss2vzED61dnUWuiKEVejkECxV4YrwNG488btdS2YTCKTVSMChSjyB3oafLmEouB2V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.443)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkS5ywNRBmf1dHmkRjhVocxxjMF9BdUDt93wV4dRkvbLHy5ZRHRhQSyEKUaTyFqQ4K9f9VGZMft97FzRowkpSYnfnJ6zNod6dQTTpNzg9mx9QYmvCztAGTcwa4my4pyS9uknkvN1VbiA7bFzVSnMV9P6gHKVEEEX6qMwLCiANjakr8o34899jCjPnivUhGKQzn8TfPfoToBKsB4yqvVW14Y5W6FmMA8KvLVfLzTwrB6Y1135JdSHrsQmeMWbzFnyFHc5fSu2Hjkr1q9uumUfEDZR8cZW7KG3ahpYcPzk63Y9auypFCDWE1FmAYfkAAChwf8txeFMY1Y4FFrEsZvntFS2Tk6ex86tRGojUmB7QhXiqVeJ4kUbnwoNLRnutSB2inJGGy6XRc",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.444)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkS5ywNRBmf1dHmkRjhVocxxjMF9BdUDt93wV4dRkvbLHy5ZRHRhQSyEKUaTyFqQ4K9f9VGZMft97FzRowkpSYnfnJ6zNod6dQTTpNzg9mx9QYmvCztAGTcwa4my4pyS9uknkvN1VbiA7bFzVSnMV9P6gHKVEEEX6qMwLCiANjakr8o34899jCjPnivUhGKQzn8TfPfoToBKsB4yqvVW14Y5W6FmMA8KvLVfLzTwrB6Y1135JdSHrsQmeMWbzFnyFHc5fSu2Hjkr1q9uumUfEDZR8cZW7KG3ahpYcPzk63Y9auypFCDWE1FmAYfkAAChwf8txeFMY1Y4FFrEsZvntFS2Tk6ex86tRGojUmB7QhXiqVeJ4kUbnwoNLRnutSB2inJGGy6XRc",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.448)
```javascript
{
  "id": -576460752303423404,
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

#### initiator <--- (2018-10-16 20:06:31.449)
```javascript
{
  "id": -576460752303423403,
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

#### responder ---> (2018-10-16 20:06:31.449)
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

#### responder <--- (2018-10-16 20:06:31.452)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmDzWxHgNdkhxDnMG6QJqixyuyK8Zjow2pRmZy21FCKkgVWt9kktp35gpBfYxxaPm8vdi9UTAecv5ZjdAWwREsAj8PyiVyWp3VzyttcHNQemqghz9ZnfJR5JqtPjLbmsMWMcyWrs6EgTEArcfPKsk73dcJ2mMSZhXX"
  }
}
```

#### responder ---> (2018-10-16 20:06:31.453)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4sTHHcr9MxcbbjiHfbFBYJ4mNdDeyrNxhD1auRTmZtRuwjz9AavyaEnH5WDg3C6Yv7hK3SqfHkGZP97t79SceeEJHFVHWdjP4BygEisFTQAe9uEEV1BuESphJXDdDRMKq4cst1tSAW8Ae6EsMsPMvvcireqgk1P2bkKYN6P7aXQX2YGxej65PuuY4K6GRYhgtAyFCLBRggL5r6kDR3xfwzRnNqnNFkX8PCT89xqRKvYZLmux9HC3RW4Z2ReyJFCBKeH5uFyMaKVQBD7Hohf6g3n1jhJWmuDoR1FcjuVqn5F5DWq"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.457)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.458)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmDzWxHgNdkhxDnMG6QJqixyuyK8Zjow2pRmZy21FCKkgVWt9kktp35gpBfYxxaPm8vdi9UTAecv5ZjdAWwREsAj8PyiVyWp3VzyttcHNQemqghz9ZnfJR5JqtPjLbmsMWMcyWrs6EgTEArcfPKsk73dcJ2mMSZhXX"
  }
}
```

#### initiator ---> (2018-10-16 20:06:31.459)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4piXeVBqTSFaawcfqQf8cHKeP2m8L4mqrVpUe2bGTMjaBCRpcP9JJ4kmFLJE6dkuevMGV7YFnXbPKWqu5kyLfE1xxiw2wRC9Syz7UQZCC1wdLpJUfSx1tdcFf32ui2uSZWauFwWrCEeooeGJFRQXmkmBYxPoB9S46QvQMHVZ95qZMKtHGWD4a831xcEPLsZEW6jZWpjP2eq9rcJgXp292QwfhbHY26FS5kZn26k5fFotCLPXvXsiFVF7G32DCSonCXVabwWpizEoShgimtjofSyNpiyiWsjZa6toDEiWxJ8SqkQ"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.463)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSbUti13YBLj2AwVfkBwYYz7MQjvTqbpM4YHsE8ba32sQtukJ55Qt1feMyomnZ9fC1uRwY2boQCsNsBaveVp4mYbRbLVBXPr1uhB8d9P2SLAiJwNBtKJDMfgMMWeSzhuaDqWfa6ypUjHaCkpESyC2NyakR3dYeAy1d4KXCeEaToaSudki3xeKoUfNGH38yqzNQmv93aojdUwiVsrnqpEpEAPcPJg8xKS7C47qzQx1bH3FQ99YD6GYGh1hNRee5qz1FvRy34toUAX6rUQV76uAEZyyNQh7zjVvnjqLDZG3yzRMUBPWDhbLGU9CyNzzjsziDMD2VLpbpZRzSMtnT9cJ4sTjpq9BUxWPpfjH3VWCK9s5ow463MtP68ZLaeJsrzaWnAGZaeLD",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.464)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSbUti13YBLj2AwVfkBwYYz7MQjvTqbpM4YHsE8ba32sQtukJ55Qt1feMyomnZ9fC1uRwY2boQCsNsBaveVp4mYbRbLVBXPr1uhB8d9P2SLAiJwNBtKJDMfgMMWeSzhuaDqWfa6ypUjHaCkpESyC2NyakR3dYeAy1d4KXCeEaToaSudki3xeKoUfNGH38yqzNQmv93aojdUwiVsrnqpEpEAPcPJg8xKS7C47qzQx1bH3FQ99YD6GYGh1hNRee5qz1FvRy34toUAX6rUQV76uAEZyyNQh7zjVvnjqLDZG3yzRMUBPWDhbLGU9CyNzzjsziDMD2VLpbpZRzSMtnT9cJ4sTjpq9BUxWPpfjH3VWCK9s5ow463MtP68ZLaeJsrzaWnAGZaeLD",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.468)
```javascript
{
  "id": -576460752303423402,
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

#### initiator <--- (2018-10-16 20:06:31.469)
```javascript
{
  "id": -576460752303423401,
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

#### initiator ---> (2018-10-16 20:06:31.469)
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

#### initiator <--- (2018-10-16 20:06:31.472)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmE5wU9Dv6x3g9YLoDJRD1ZqcCd3L349Ua4c2iYvGF3GCS5pBL2BWu9ccWjQHmJzPThQEb96pKQKp1eyi7ThChKg3AUDvFovHPnXoWY86WG2ws6snoPYxtn2JH7123hN9dMTTftnQsdcobtjsJmvdbd4UoZC428pPr"
  }
}
```

#### initiator ---> (2018-10-16 20:06:31.473)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak54GK3ee7B9fpWm1h52QY9uHga3x7THkGY8YEsDTfy4Ewajbsrr4tHidYKnbFtp7zQDUDYWMG7PHWrybuKBpJMgfS7ZEQSs1LpUexSd2PKy77MGruWFCrhdfQKiULyU4Ws134AyCBANH2VVCnbqi81UEofPwAhxzUK4JebknxHoMxe1jnnkk2FtYgMdysKYdKhP1oJiq1o7XW2hLxJYmCEPujcke6aCZBXbfovNLNAPFGdmCznqhwZWCbxd71L9c6FU2fLP4zyiu5CfYJaGzT1r436fS9rHSyH8qt1FcvnRMVSbZ"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.515)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.517)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmE5wU9Dv6x3g9YLoDJRD1ZqcCd3L349Ua4c2iYvGF3GCS5pBL2BWu9ccWjQHmJzPThQEb96pKQKp1eyi7ThChKg3AUDvFovHPnXoWY86WG2ws6snoPYxtn2JH7123hN9dMTTftnQsdcobtjsJmvdbd4UoZC428pPr"
  }
}
```

#### responder ---> (2018-10-16 20:06:31.520)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak55BFsyiXbVQ7wZpk1YVCxGrBJUUVLkXtav7VsPPgPXH7d6ooyi8A6D7Lri2nvhyzyX7wCUFZAiQD2gX3G4tFPeAMJoSVwdBxwfZt6YrTKQdmAim9i9dJLL8AZBnbtxunCDZtSKvqVQoVFi11nhE5R5twLViqZfvctK5KRf1mvT5HwJ3MZq8imf4FXsiiigdJUqJ7PFwDRBZ1huB2qmnUahGPCeJiiNMPGEYfaprvJX2bRQoBYcKRC1vADL5jTJRc8KhHXdNfqxbEGhsKujVgWpNXQH4iUsszUjhJzfJHZQySDrr"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.532)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkqtNexdGxabBhY7iTyLzUxxHTNY5LExdKVLxMjAJuAqmGjnFPTk87DxLejQ9abZNCt61U7r5PYptKSz7rcL8BKd5AFuCtH4pZqo4n9P9JTAKyNk8ZZHyvnHdkqMMUU9ajpkdEiMeztrCTiq2rNBghkiyy7DVfGTgdbaFPzPvsU9HAC6KNd7dtebFr6jdZJHf7GMp3rr1aY2sEXv4Z4fjY1Gbgme7NYnRZR4CtFSBr5UHdQxzh4TepXXD4u59t6ATu8Zr6ZuJz8rmc1UM199CLQ1pnhMubVAUcedrNS7K7ZRPSbhDeXA6wzJECKjn59LZ6zWyDnXxPruEA9uFeVNYMUPiyYVfAJmZp7PWBT4MnhXj2ZqqUoEvRAcxvV7wk1FHtsrsxAacW",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.532)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkqtNexdGxabBhY7iTyLzUxxHTNY5LExdKVLxMjAJuAqmGjnFPTk87DxLejQ9abZNCt61U7r5PYptKSz7rcL8BKd5AFuCtH4pZqo4n9P9JTAKyNk8ZZHyvnHdkqMMUU9ajpkdEiMeztrCTiq2rNBghkiyy7DVfGTgdbaFPzPvsU9HAC6KNd7dtebFr6jdZJHf7GMp3rr1aY2sEXv4Z4fjY1Gbgme7NYnRZR4CtFSBr5UHdQxzh4TepXXD4u59t6ATu8Zr6ZuJz8rmc1UM199CLQ1pnhMubVAUcedrNS7K7ZRPSbhDeXA6wzJECKjn59LZ6zWyDnXxPruEA9uFeVNYMUPiyYVfAJmZp7PWBT4MnhXj2ZqqUoEvRAcxvV7wk1FHtsrsxAacW",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.539)
```javascript
{
  "id": -576460752303423400,
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

#### initiator <--- (2018-10-16 20:06:31.540)
```javascript
{
  "id": -576460752303423399,
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

#### responder ---> (2018-10-16 20:06:31.541)
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

#### responder <--- (2018-10-16 20:06:31.545)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmEBMyzmTa9PQ5JLLLCYXiXaySS1hsmJq5FsMCrxkZoFtYVQyz6bYYPaJVrSNY3wwLHudQUZoWPRKSJUKvMvzB2jP2RcDpfwUKMisPP1HFdxNBKKDnT64BNNx3jCFctasFBwJ2WKWmXKfaf2bNGJQgrgcEQSKxdxJ6"
  }
}
```

#### responder ---> (2018-10-16 20:06:31.546)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak54dKgcGMg5g29AtNCXo8PeYBB3zj9E7kFFdjwVoZfhWSSxcZpSkFTRXDvsssNN118qbMou1kgRgVCADMhdHvdBCLRFSzeZgqpS8mutCUh8QE9ZCz8vzzcsWqDojmQArDcNsEKp2R2ZvimSHL7AeiGpAWgorzBT1xPfu69Q3N2WPgZqxP1ZgU2E8GtWSDEDoZJGp95Sd4Deqoaxn7CNYhUYd3i8JP2eEq2dS6ReY77xPL8qTNJmVq2SDUNHGz8hAR78PR5aScm6ZMZKwjdVsbBxCcZhjsJ3baoSPhKxZtHU5oeUW"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.573)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.575)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTqsMyzjxRMewZyetRu59PTeKjT7jGmFayrY4kaxm4QhmEBMyzmTa9PQ5JLLLCYXiXaySS1hsmJq5FsMCrxkZoFtYVQyz6bYYPaJVrSNY3wwLHudQUZoWPRKSJUKvMvzB2jP2RcDpfwUKMisPP1HFdxNBKKDnT64BNNx3jCFctasFBwJ2WKWmXKfaf2bNGJQgrgcEQSKxdxJ6"
  }
}
```

#### initiator ---> (2018-10-16 20:06:31.577)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak52mvuvErBJYUebWWDp3CVfXY4Ho68dGg7aYHhGWMAKU7exXagfG5zT1UxzuYkn5AYMJp3tWoaUAb2vHs8QeiLtKaEbLWJGQg5wGNF9AP9z8BkPqmQrkGbr4Xm4roWW11bTb5RmKGEZ5uqbroNmuEhC4HQGZuLTbguFXC35XdGXvpZfmVLyLFGEpHpSB82Bm1bMPoQqAgHFe92JCBGRxvLh1LAbBkMxz4pabDj8eDWzQgjXASnv2VQtyxkVKhyssxuua5vhBTYUsx2PpV9Wr7GfSdruxy24tddhGn5avd68doxnb"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.594)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkoKsPs6rX3ePVgTUoFuRBmUtvsEizmExijKNCTqr7WrD3GRCJzS2SCqGfZiSxbbYXD69TbQfzZpLHE3acVEwKVP7jZ2RnHW6px464x8x1FD4LA8xN816Htpsfg5fuLJ6xbqxraXjmosFmU4VFfTgA79pYK6b3vV9FAswNFgBVRpvDg7ZKt1pV5KF3mUydPHqFynVTjzYkinSeWfeVNZoDn57bUF7J8DwJZPiFZuLH77VTNyYtnXAuDHftoDawyAtkgd3v74MKuQvNFo13XmoGQF626d2dnt5QGYSmF3zZ2ZpQtxrbamvz5UbAEnJfs5G3qQSAqyQyjGgUqS7J4haVj19Sb24wRYax1fbtZ4L8uBL1pJW11L8YrkS1YdiaRQ6rugTJntUk",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.595)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkoKsPs6rX3ePVgTUoFuRBmUtvsEizmExijKNCTqr7WrD3GRCJzS2SCqGfZiSxbbYXD69TbQfzZpLHE3acVEwKVP7jZ2RnHW6px464x8x1FD4LA8xN816Htpsfg5fuLJ6xbqxraXjmosFmU4VFfTgA79pYK6b3vV9FAswNFgBVRpvDg7ZKt1pV5KF3mUydPHqFynVTjzYkinSeWfeVNZoDn57bUF7J8DwJZPiFZuLH77VTNyYtnXAuDHftoDawyAtkgd3v74MKuQvNFo13XmoGQF626d2dnt5QGYSmF3zZ2ZpQtxrbamvz5UbAEnJfs5G3qQSAqyQyjGgUqS7J4haVj19Sb24wRYax1fbtZ4L8uBL1pJW11L8YrkS1YdiaRQ6rugTJntUk",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.606)
```javascript
{
  "id": -576460752303423398,
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

#### responder ---> (2018-10-16 20:06:31.697)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- (2018-10-16 20:06:31.704)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "tx": "tx_2C9estKT2vnrZ4gbPt7MbDSHZMVeJALqLQ1Y7aztamx57DN4TFfLfCmrwJv9Sg9AKxqRRTF6HdWzCdHY5Bs9TeWf8uw4d5AQit12HX65ycz5Vk4BQEmCup3rt7TktiSC6psDYxB2uSxmmjr4QQbUdgmEXd9ifw"
  }
}
```

#### responder ---> (2018-10-16 20:06:31.706)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_2WsEQsiC5Xso6BSP9HfgvuXytUL4xzxFVd2sRe7ZZQV2ykbio6UTFT4Fk4vqK95ycRoisEwWNTziK7v6SZiMrcTeriQgkwySt9MBycPHs5xXEKwrcg4GqdF3emTS9gVfTK4Ts65auiJRFUG3AcigetMqNNtn4NjchwabGCPVWXBX1oFj2LvKwLEuzj27aDbuxyfC5uS2LV1X5TvJJebk2GaE6EPycP1ZXoNF3yn2gZ2MxsJmhF7NMPMpBcEDJki5tP3"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.707)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_created",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.708)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "tx": "tx_2C9estKT2vnrZ4gbPt7MbDSHZMVeJALqLQ1Y7aztamx57DN4TFfLfCmrwJv9Sg9AKxqRRTF6HdWzCdHY5Bs9TeWf8uw4d5AQit12HX65ycz5Vk4BQEmCup3rt7TktiSC6psDYxB2uSxmmjr4QQbUdgmEXd9ifw"
  }
}
```

#### initiator ---> (2018-10-16 20:06:31.709)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_2WsEQsiC5Xsmsck2ps7fTznMTy9HDiJqdXQ7aFZFhpVgrVWaWBFFiPbAFzGXY3U8MMTVcwW8euBqz3nZFwR44TEPx8Ha6Dzmfhk4yXJtoiCox3R7xybAUfNMJMhReE4UgULoKM6RAktD61w2d7QT63kaubjWxC3J5nqBXuKHJZe6Lw21dx6MWJ5F986AnP5xVJ3RCg72665x12mTJoBTddaw2Wnby7TNAdeWcd2gYvqveG8NrjjpHSk1Z3FBjL5Lghp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:31.711)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByWtU25KFVHazE6JzHjB3o4EZp2LJTFyXzvyVnf4AmnxJ9m9F5Yk6SLAhvkNiG5AT3xEvoJM7dwZsqvtKUbSHuBcZeawFLqvpyg7VvDt86AZm9UsWm9gexL2na35TpzpgtKM2TNTpR5uoRw4ee2xtNtpL4tMMR3KXuPn5yweUN1NKoZSNuNRVo3JJYTweUw2EAMH8Sqq3e7MzMgBfwijgRqK9JG6Grr9HFMtp8XtZgakf8PDtCXhtttbU66m2pW9qFxLZphHpd59UK9tk387DoHVo7E49yJxaHMuKrG9VbqwFL17mjX1UW8pp8fJj94iyMa6JpaM6EC8jWFsrxw",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:31.712)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByWtU25KFVHazE6JzHjB3o4EZp2LJTFyXzvyVnf4AmnxJ9m9F5Yk6SLAhvkNiG5AT3xEvoJM7dwZsqvtKUbSHuBcZeawFLqvpyg7VvDt86AZm9UsWm9gexL2na35TpzpgtKM2TNTpR5uoRw4ee2xtNtpL4tMMR3KXuPn5yweUN1NKoZSNuNRVo3JJYTweUw2EAMH8Sqq3e7MzMgBfwijgRqK9JG6Grr9HFMtp8XtZgakf8PDtCXhtttbU66m2pW9qFxLZphHpd59UK9tk387DoHVo7E49yJxaHMuKrG9VbqwFL17mjX1UW8pp8fJj94iyMa6JpaM6EC8jWFsrxw",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:34.283)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:34.284)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:34.284)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:34.285)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### responder <--- (2018-10-16 20:06:34.288)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByWtU25KFVHazE6JzHjB3o4EZp2LJTFyXzvyVnf4AmnxJ9m9F5Yk6SLAhvkNiG5AT3xEvoJM7dwZsqvtKUbSHuBcZeawFLqvpyg7VvDt86AZm9UsWm9gexL2na35TpzpgtKM2TNTpR5uoRw4ee2xtNtpL4tMMR3KXuPn5yweUN1NKoZSNuNRVo3JJYTweUw2EAMH8Sqq3e7MzMgBfwijgRqK9JG6Grr9HFMtp8XtZgakf8PDtCXhtttbU66m2pW9qFxLZphHpd59UK9tk387DoHVo7E49yJxaHMuKrG9VbqwFL17mjX1UW8pp8fJj94iyMa6JpaM6EC8jWFsrxw",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```

#### initiator <--- (2018-10-16 20:06:34.288)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByWtU25KFVHazE6JzHjB3o4EZp2LJTFyXzvyVnf4AmnxJ9m9F5Yk6SLAhvkNiG5AT3xEvoJM7dwZsqvtKUbSHuBcZeawFLqvpyg7VvDt86AZm9UsWm9gexL2na35TpzpgtKM2TNTpR5uoRw4ee2xtNtpL4tMMR3KXuPn5yweUN1NKoZSNuNRVo3JJYTweUw2EAMH8Sqq3e7MzMgBfwijgRqK9JG6Grr9HFMtp8XtZgakf8PDtCXhtttbU66m2pW9qFxLZphHpd59UK9tk387DoHVo7E49yJxaHMuKrG9VbqwFL17mjX1UW8pp8fJj94iyMa6JpaM6EC8jWFsrxw",
    "channel_id": "ch_2ofBVjPDmJYsf6W3dRubttRbKzMW1KoDu86TmpshK8bnYahe9V"
  }
}
```
