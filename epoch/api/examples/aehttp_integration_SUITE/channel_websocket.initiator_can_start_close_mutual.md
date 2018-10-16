
#### initiator init (2018-10-16 17:13:53.528)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder init (2018-10-16 17:13:53.534)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### responder <--- (2018-10-16 17:13:54.534)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 17:13:54.536)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 17:13:54.545)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSvsfgnCG"
  }
}
```

#### initiator ---> (2018-10-16 17:13:54.582)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkNmCEp9hFAzm4fKVmQEVoXyymAhXWgQsAaJaPAx8hG3LZGSqhZpoAPxs4RJKtBDoPdTbWc6qcsvrzETLXmmoC1K67wRRSDAtkBLdrnhbGDQLxj5hXhZvzQhHRjSikfp662Ynm9LgZsw4AcJtiRM7CmtecMntiCUq1FC2AmXLfu6W5Vbsi1NM4JC9szySJ2Eo3a38CGKbZXnVmMyKBjwj4DKaTobMFf3NCA3syr4jLW1pot59C1z5sCjNuubwcBh3"
  }
}
```

#### responder <--- (2018-10-16 17:13:54.583)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 17:13:54.584)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSvsfgnCG"
  }
}
```

#### responder ---> (2018-10-16 17:13:54.585)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hkmy876Y4RfgiUaY2rbuNS2nQGc7ujaEs3S3DYoHbYExLbMr3px37aYFErUs6VZt222jUJrehYacdB6FpnpzcJFiSGdn8bYraDnWdANmE6cWJ7R5SAbomWfHU958PzEPDwBXmTHfZpmHNoRrMApxCiDDNTxhYi35A2gHnb1ddKWt9QzomHZzr81P8rUR3RmzeVU46xiKSe1qCpm2RiVdD1vLfYDwyD9LZWEzhM3q2m42oVdv3qfQNmPSENqkD9w6q"
  }
}
```

#### initiator <--- (2018-10-16 17:13:54.587)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 17:13:54.588)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNrQr6MCog9S7vbRT9V3Ka4vihLXXczHURtkxJCoGCr7NhFtaajkCEAKvZxvAh1fdi8xdatR2DbgLVrgfHpHzCWL1tTBvADouQvcjToB7U8dsg696zxs8rpxTHaHv5rCN9U3RkmQdvadDDmxC7ryhJ933LDqMQ7YpPPbNUA5ztWc1SovKDDB537ouFpsnMXAt99kPUqDf8FkrEGUWVM4Fwtww3RC6WVPWb1jW7PsKGyWZQGvVA26namrGiy8GYm6zpF9F3EZvHSrbzuZRYXpUpwzZj47Y9KLRELsqjRnHfgw9eEF5HfYdJTniidDAPA4AHWK9KbDrzcvppkBATd8BKF3EZ4"
  }
}
```

#### initiator <--- (2018-10-16 17:13:54.588)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNrQr6MCog9S7vbRT9V3Ka4vihLXXczHURtkxJCoGCr7NhFtaajkCEAKvZxvAh1fdi8xdatR2DbgLVrgfHpHzCWL1tTBvADouQvcjToB7U8dsg696zxs8rpxTHaHv5rCN9U3RkmQdvadDDmxC7ryhJ933LDqMQ7YpPPbNUA5ztWc1SovKDDB537ouFpsnMXAt99kPUqDf8FkrEGUWVM4Fwtww3RC6WVPWb1jW7PsKGyWZQGvVA26namrGiy8GYm6zpF9F3EZvHSrbzuZRYXpUpwzZj47Y9KLRELsqjRnHfgw9eEF5HfYdJTniidDAPA4AHWK9KbDrzcvppkBATd8BKF3EZ4"
  }
}
```

#### initiator <--- (2018-10-16 17:13:55.401)
```javascript
{
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### responder <--- (2018-10-16 17:13:56.986)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:56.987)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:56.987)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:56.987)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:56.994)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:56.994)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:56.995)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNrQr6MCog9S7vbRT9V3Ka4vihLXXczHURtkxJCoGCr7NhFtaajkCEAKvZxvAh1fdi8xdatR2DbgLVrgfHpHzCWL1tTBvADouQvcjToB7U8dsg696zxs8rpxTHaHv5rCN9U3RkmQdvadDDmxC7ryhJ933LDqMQ7YpPPbNUA5ztWc1SovKDDB537ouFpsnMXAt99kPUqDf8FkrEGUWVM4Fwtww3RC6WVPWb1jW7PsKGyWZQGvVA26namrGiy8GYm6zpF9F3EZvHSrbzuZRYXpUpwzZj47Y9KLRELsqjRnHfgw9eEF5HfYdJTniidDAPA4AHWK9KbDrzcvppkBATd8BKF3EZ4",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:56.995)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNrQr6MCog9S7vbRT9V3Ka4vihLXXczHURtkxJCoGCr7NhFtaajkCEAKvZxvAh1fdi8xdatR2DbgLVrgfHpHzCWL1tTBvADouQvcjToB7U8dsg696zxs8rpxTHaHv5rCN9U3RkmQdvadDDmxC7ryhJ933LDqMQ7YpPPbNUA5ztWc1SovKDDB537ouFpsnMXAt99kPUqDf8FkrEGUWVM4Fwtww3RC6WVPWb1jW7PsKGyWZQGvVA26namrGiy8GYm6zpF9F3EZvHSrbzuZRYXpUpwzZj47Y9KLRELsqjRnHfgw9eEF5HfYdJTniidDAPA4AHWK9KbDrzcvppkBATd8BKF3EZ4",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

##### initiator: (2018-10-16 17:13:57.187)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 17:13:57.187)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 17:13:57.187)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 17:13:57.187)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 17:13:57.187)
> Channel is `open` and ready to use

##### responder: (2018-10-16 17:13:57.187)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 17:13:57.231)
```javascript
{
  "id": -576460752303423473,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator ---> (2018-10-16 17:13:57.232)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.238)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkBmSmsGfoAHy7heAJfxNaX5fqv2zuRg2RBkam34ME3zD9N9Nk5nFzmx1hv2NPQnuyBVajPZjfkiVNRqc3rRHBC1EPziajwXMEjZXqsrVEZzuudEQWhQKhSm6zN3v3tFWkiuKodCKM42TcssE9e8cbwg8nEJSsEgs"
  }
}
```

#### initiator ---> (2018-10-16 17:13:57.240)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4syrRE2JJWh36y7pECXNHaYZNobwQJQzStF1EjR25WruzxehxJuaxPruRU4eRVxGTKCHZQQip2LA4uoQBV1mMxSoKwzExJuG5NSfQRsrwhcGRdiFSDmYJ5hGkYCUo4Ktf9Ro1tFCy2WMF9Uj6UZ16qmJZ14S74HugSvkEvua8rjLGN8erV5myxqm4HYk2W6RPC5eCsQZBwAaMkDp1FRyfvAYijBYDtzFRKrLMZzj68edyVzt8XtzM5LJAd3LwoimZnbPmGC34mfBt5qnuwy2WVjQGrksyKyAtczNNGx7oVFTZRg"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.248)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.250)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkBmSmsGfoAHy7heAJfxNaX5fqv2zuRg2RBkam34ME3zD9N9Nk5nFzmx1hv2NPQnuyBVajPZjfkiVNRqc3rRHBC1EPziajwXMEjZXqsrVEZzuudEQWhQKhSm6zN3v3tFWkiuKodCKM42TcssE9e8cbwg8nEJSsEgs"
  }
}
```

#### responder ---> (2018-10-16 17:13:57.251)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4keCC62ekiHcywPdUaALGXVUxX76BFL2mNbRj9sjKnA1nMcVk9eY19v3YyRRnHoTzS4yvR5KRfdg2SuJ1jvVkSEYJ9oYwDMgMP8nXgtdGJjZtFgjaEavA4NM1YJeduQxB9pXLoonG1DnTPA71V3qDRyt1HAp1efmGRnkVhoRryJHGF8S9FnJhtccRJ7FieXvjGLN7JxdYHp2qG8nusQ7993xCYTT5Fac2RhujpP6LKFXW14EvcT8of7A4c3Qbkhu9SnjyBceRwENVkMxNEXYsUc87xuPfhVXX23HHHLuZh3QEcs"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.257)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKbBUYCJkiw7yQdNac3PMgXkwinbaGyNkCjF8ZM4kqKwE4hfeBSj1U2YLNbWYynqj2n83kdwu7Bx56Rpj9EuYutPuxHfCtPcUe6ge4buaC5YXmd8HMNJsPqyG3jVQZdFjGNM3XfmGT1csthVt7iZN3xa8PXt1hWfVAcjybmfiMu2r53Ce9UztgU7qzK3GxmpBMdMa7izH13tBZ5z4hxNEV6gSAuctxSEwWtqJzZgMBFsbBCGUZ7CM3DW1MWeMoLpmxDwfNiL99cnPrfo2FxBwMqVFK24uugwLgcNQsJDPcX1a3HLmyGpAReaAw52o2CbHZCLNCeWFwHsDXxFGCkXP3jt5DLqvQkg2HwN9nfG2CwjAYDdTGytz7uZ7gNpWxqLvuTpANc2J",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.258)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKbBUYCJkiw7yQdNac3PMgXkwinbaGyNkCjF8ZM4kqKwE4hfeBSj1U2YLNbWYynqj2n83kdwu7Bx56Rpj9EuYutPuxHfCtPcUe6ge4buaC5YXmd8HMNJsPqyG3jVQZdFjGNM3XfmGT1csthVt7iZN3xa8PXt1hWfVAcjybmfiMu2r53Ce9UztgU7qzK3GxmpBMdMa7izH13tBZ5z4hxNEV6gSAuctxSEwWtqJzZgMBFsbBCGUZ7CM3DW1MWeMoLpmxDwfNiL99cnPrfo2FxBwMqVFK24uugwLgcNQsJDPcX1a3HLmyGpAReaAw52o2CbHZCLNCeWFwHsDXxFGCkXP3jt5DLqvQkg2HwN9nfG2CwjAYDdTGytz7uZ7gNpWxqLvuTpANc2J",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.262)
```javascript
{
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 698
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 402
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:13:57.264)
```javascript
{
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 402
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 698
    }
  ]
}
```

#### responder ---> (2018-10-16 17:13:57.264)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.268)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkHBxdQp8zW1tshBHCodi2a6SwNNqAjKdv4mbrdLG5aiqG45wsCmZmv9Z2mb4jZQs62qvSe1Papt1YGMGtGE9hJGAWjchDUhwyK8JFEyEffqHXaAusgSde2T8WovWxCpZJGhD2HfDTzeV8EAcSBJm3rQ9zGRQVZpT"
  }
}
```

#### responder ---> (2018-10-16 17:13:57.269)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4mZJicYNG1tMf24m7d96iKCXtYrpCGsdJ7gcKSAK4Bjsj9bVNPQDoBHBPGGGTBrqto8ncXyiAUHaAq2Anau5psYV4v5q35v29QNj4pMS1juj5UknhUrK5BTkfW3wntDbEADxff7ZqgKfKF5Vn9NATLLm8JzvcHX6JnvAioGsqw1ij1vhgahKBs9DU6pC6QRFazdyVPNAGhpisBfM7CtSk8bbE3aGAugoeaFxwe9TPQTVimPR6xVVZMTSeTB3DL2Z8JS5XRcdu595NKDoyq5DUSjqEJUGcTGN6DRszGK8fH5YjCZ"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.308)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.309)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkHBxdQp8zW1tshBHCodi2a6SwNNqAjKdv4mbrdLG5aiqG45wsCmZmv9Z2mb4jZQs62qvSe1Papt1YGMGtGE9hJGAWjchDUhwyK8JFEyEffqHXaAusgSde2T8WovWxCpZJGhD2HfDTzeV8EAcSBJm3rQ9zGRQVZpT"
  }
}
```

#### initiator ---> (2018-10-16 17:13:57.313)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4oEjBQ2FANLy9anCKv4JW5pyag7hWMhMnYdjRPkWL2shbHRHkwEMS4tGBxXAd6cSp5KniLTdbS9AxPDC8w8JfgEobzEpkqHKHeDG32NL8UYEgzuz2eAhEFh41SL8xidSiaSGuJqkbLyXhvuEgdfEYJbaYGcioFr8uaJSFiv9Luff3LwYbtQTozs53PuZ8EAWoSLwbV6dQLxqW4S7CKyGJdGQs4nSyn8miU4gW5XXz3KfAxhosPcSqgNW78gHusuPwmgXfJq8ASvKdUEYosLPJeiTza7MgWW5hpg1coR5temAeaJ"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.326)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkMAVRAma5qPSJqz646JVRJvjaxAYHmfamk7CHZ8SCKHvmehmLaB2tewH75QtZP5fVHwp1gVZo4V9vGzVdQmCZc6A8zAC2hG15tNYPJJH1EEYR2gPGWE4CDU3Hecxr6oej4sqXjzmH2Gfy8vKcRzVBbFtcoWG8vPfzZjwv7dQBJer1y8weq4GDLf3rvR45Z1P1NgXgA6B1hdSVtYZngTZr5g9KTqrHpHtRpCeempgsJwevFPYzj7jLKqhTEBr31MaVkjoU4kUzpYBATht4RgNAAXLfF68fMJy8XHFEYEmqhM5SCPQCwNdzeYN4yhmqp7YmrNPLjpoWRHkTFJJiidfV3HafZxsJr7icYdLJWQaWFTprYJ6t6LfyPK8ETLSQeG1y2s1zXGQR",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.329)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkMAVRAma5qPSJqz646JVRJvjaxAYHmfamk7CHZ8SCKHvmehmLaB2tewH75QtZP5fVHwp1gVZo4V9vGzVdQmCZc6A8zAC2hG15tNYPJJH1EEYR2gPGWE4CDU3Hecxr6oej4sqXjzmH2Gfy8vKcRzVBbFtcoWG8vPfzZjwv7dQBJer1y8weq4GDLf3rvR45Z1P1NgXgA6B1hdSVtYZngTZr5g9KTqrHpHtRpCeempgsJwevFPYzj7jLKqhTEBr31MaVkjoU4kUzpYBATht4RgNAAXLfF68fMJy8XHFEYEmqhM5SCPQCwNdzeYN4yhmqp7YmrNPLjpoWRHkTFJJiidfV3HafZxsJr7icYdLJWQaWFTprYJ6t6LfyPK8ETLSQeG1y2s1zXGQR",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.338)
```javascript
{
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:13:57.340)
```javascript
{
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 17:13:57.340)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.345)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkNcUUxMcBqjpdgiQ6vUhosdBVowu9RDmL7fDn75wpLKrkKW4Y48pRrti8DHrULVxmfoYwhKpU5VwpgvybX6odJPUjgUco3RMegcYdbvfAG6XqEikaRixRRDUA2PAWA1ZkEhnGqnXortPMyrEEQS1V5u4jCQhw3og"
  }
}
```

#### responder ---> (2018-10-16 17:13:57.346)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5Bcb8Scan2PbdDZUpbb9bTCCkg5uc6x1Lvcosh2D4fRPjefz2qAoCWVfukv1NerdiG7v5WEFXGxqYpguRn5Q8fKzkehmKWazuWgVmpP7GwcKrKC9gTSjxUPccwjuX7G6VhkNPNLq4FDNFKg1hrQtDKVJ6wK6XQxRhuPjRA7mP39ZPy8HLMM8MadkTmgcxwiC1aNaUyMrLwkW4fXqqo9DarRiZtbwto9234xVTgB263cC244muWhgGBBDJAgR7foX7WiU2HGpzWHm56a4j6vkjswXuP94N2saLrExMFyjyL7A7YJ"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.350)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.351)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkNcUUxMcBqjpdgiQ6vUhosdBVowu9RDmL7fDn75wpLKrkKW4Y48pRrti8DHrULVxmfoYwhKpU5VwpgvybX6odJPUjgUco3RMegcYdbvfAG6XqEikaRixRRDUA2PAWA1ZkEhnGqnXortPMyrEEQS1V5u4jCQhw3og"
  }
}
```

#### initiator ---> (2018-10-16 17:13:57.352)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak58GnmfSTCUk5xSHBtiGdZAhAQVXapSF6H7K5QFcETTA9t7dJRsrMLrU3qbtR1qYbzvaPp1jWKpQr3w4oN6UL1NcfbtxHJh7H3Q2rMQ7bw5McDpmg3MMyGkNL4cE4xK5x2DT16qhXo7uARqvqMinBdnpVFUKLm5KtZWCLsEvF9vbBujmj7r66rRvC12M5aCV5MovgxWmVJdu7hT51AEEPrcKSwqcCeHtgduJpRGNyRdSRMHEGKniSvPaKWaGcaYmFoCByTeC5UaFvuJzpkrHzmFTBc6cjDcx8zq75YuQ2XdhpGzK"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.356)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkxn3SYVHNM4d5aVpnKYrM4HNgCgYPWyAindA4DrFLUhZodKd76EStT6CpoRj9nYSo6Kz3GxZctAmfAmmWdT1YnCuoWuz2dTst8RHS6zSjAokLHmS8xiijZiDAnqQZVB3xhTyXKAZyZZCf1Uem38MrCNEZZ9beAfk9QydLAJz1VXTtad2ow6sK9XVCSrFRY62bkoDa5sGhfo9o32B4tByQKiZN5xksKpHG6vg325jZaAZ6AJZqyHcgCtZ9ZgwHRFsifm632PmWp2vmYxzZeCkoDovRFYZr8nyuAq74FpzRyLrRVHBpym719UUpcEiXCoCTrrSWSjdy7eB9x6LmjwyYgXpgJ6C3xfJe9en3SKdZADu3cTR398bmpBzwQP5N6SxBoyD6PyUF",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.357)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkxn3SYVHNM4d5aVpnKYrM4HNgCgYPWyAindA4DrFLUhZodKd76EStT6CpoRj9nYSo6Kz3GxZctAmfAmmWdT1YnCuoWuz2dTst8RHS6zSjAokLHmS8xiijZiDAnqQZVB3xhTyXKAZyZZCf1Uem38MrCNEZZ9beAfk9QydLAJz1VXTtad2ow6sK9XVCSrFRY62bkoDa5sGhfo9o32B4tByQKiZN5xksKpHG6vg325jZaAZ6AJZqyHcgCtZ9ZgwHRFsifm632PmWp2vmYxzZeCkoDovRFYZr8nyuAq74FpzRyLrRVHBpym719UUpcEiXCoCTrrSWSjdy7eB9x6LmjwyYgXpgJ6C3xfJe9en3SKdZADu3cTR398bmpBzwQP5N6SxBoyD6PyUF",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.361)
```javascript
{
  "id": -576460752303423468,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 400
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 700
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:13:57.362)
```javascript
{
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 700
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 400
    }
  ]
}
```

#### initiator ---> (2018-10-16 17:13:57.363)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.366)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkU2zLVu5PBTkPgFX12VMvRfsXEkCqVNQfLRSXUKQSJoHcAPikdt1xcBUzF8jbk4D26NUEZX2KWaJDhaiBd3EyCPB4qJMUdfaGr2GzxikiLnepcqzHsGb8AxCuJWbkETjQDeuAkjehDTcBJNcjyt8hDGUp75Nq2Zr"
  }
}
```

#### initiator ---> (2018-10-16 17:13:57.367)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4nRGAQ5tc3MHVhKe3adyKKwb8omTkXGoH72yeGbx41sCFAMJcH7K99FCwKK8bmeyEtuxxX4t8VktYGY9MUjHGuYqxxFyQZNV3bd577eUpT8n3gYCxZ72wibcbVXmPi3AAT2anSStMft7SRaHSr5ckKdE9Q87yjyhPM6d15qggSh8nLbKqcVvMu5t9HrdvxhUGzUFpBApoZaKxXGU16enEVeVmDsuvGPAWozKPKGtDARvySBG2v1MhL8dHRiBkfEwJM78PXMtccLi8PpPRmbHgGgpQmVrm1WxUNPCPJnhxX35fNt"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.403)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.405)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkU2zLVu5PBTkPgFX12VMvRfsXEkCqVNQfLRSXUKQSJoHcAPikdt1xcBUzF8jbk4D26NUEZX2KWaJDhaiBd3EyCPB4qJMUdfaGr2GzxikiLnepcqzHsGb8AxCuJWbkETjQDeuAkjehDTcBJNcjyt8hDGUp75Nq2Zr"
  }
}
```

#### responder ---> (2018-10-16 17:13:57.408)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4nJ3wvVC6741vAtvwWMXKVDhBWn5LRCQrJ1CEYWUkeLJ2Y4XtbrnQHQXBy8FvYKXzsUD9zRChpkZ6aNzLVXskuqR18HFV1G4qqEZgDdG9pJF4aRJYhMb7kGnZpMnzWjtqB7V4MTXirBiUQqPXvLzzUvnc6qLKNrHxue4ySDWiKGDBhUnZKcNJda85es3jogkGGYCBvG58C6gmpysMWqWoM1dpsfZTmHasjwwWeW2FpqAt1SZKgaXcazCqNhsWDhjzgiZakXS9NTakApidPTb5N6wCfCo3RdgG1AnDbpp44zTREx"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.419)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkNRydStxsXi8X97bHr9yNhGbEPFX3AR4b3ujwpbH1UNYy7JaTKLD6CGcZASFxP7yQmrQNTDF77UNFbAQNzQz7iJaLH8PT4ZXVdAB7ThqTE9NvLRYovB4NmtfrBF1YiG3FTyddMsTqUT7mPZRqMzj63g79Bcovd9g7SQj9EzndPXCiyKj4GHzpXsx1dX2hqC5S24bnkkRggHRAXQX9NSqFLFQhFRJ3qKLT3m9uYqEQWb7ipqKh3sBPtCHy1yNVY6zmegzpJ1qzLycFCjAapKF836nqu3pRYtUJDWXoKCuJ6ZmNCyrWeNhoEQXkpZBECWqk1hC4eW9ZLRxL47kBpp8WxVmgisphqRtyeCTfj1A1R1yVYksxZjgS6gaom2JYFUAqpQ4nYf6c",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.422)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkNRydStxsXi8X97bHr9yNhGbEPFX3AR4b3ujwpbH1UNYy7JaTKLD6CGcZASFxP7yQmrQNTDF77UNFbAQNzQz7iJaLH8PT4ZXVdAB7ThqTE9NvLRYovB4NmtfrBF1YiG3FTyddMsTqUT7mPZRqMzj63g79Bcovd9g7SQj9EzndPXCiyKj4GHzpXsx1dX2hqC5S24bnkkRggHRAXQX9NSqFLFQhFRJ3qKLT3m9uYqEQWb7ipqKh3sBPtCHy1yNVY6zmegzpJ1qzLycFCjAapKF836nqu3pRYtUJDWXoKCuJ6ZmNCyrWeNhoEQXkpZBECWqk1hC4eW9ZLRxL47kBpp8WxVmgisphqRtyeCTfj1A1R1yVYksxZjgS6gaom2JYFUAqpQ4nYf6c",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.429)
```javascript
{
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:13:57.431)
```javascript
{
  "id": -576460752303423465,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 17:13:57.431)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.435)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkZTWC3SYaXBg9fnduAAhNUgech636o22ADSTd4bKHqXuirLHsksKjkP2K6hRwtgA8wiowoxgEajpPY6P22r7VJe7BaCTxArB1Rb3QKqW9Sd2SZnyErUiiVKdVVJBcsXJaZ2HvJD4ejKoAPnDAq6bJ8u16sPkjdhi"
  }
}
```

#### responder ---> (2018-10-16 17:13:57.437)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4pwgCSwEy1h2cWUTSSb5uWLPAt1mdbVYxGX4pWZ8H9Ra3YGd9saNWnbViERGktn2Mg2d9aM7wGpr8TFG7pLEgdGzfH6mZ3gKSbUwZiDkz41gexKFjnopdNRsk8Z98y3k8W5R7YFksPme6MgtVFwdFEXze9byfGopkn6rXzuW4b4zgRwifkLcEiNxwtA26mtybvKNtpA58x8WbWcvhYyMEvbQoNTxgVU3REGHcnXcSAzAYwxNtVqSHhoHJRqpT2FwZK5HgZV4QU24euuG7WpxGVGNPmriobfPgv3FLhFA23yNqh7"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.464)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.466)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQUKxvrof6t3MkGkckiDKbkF2wWaXvbH2TPmdpyFKAToDNkZTWC3SYaXBg9fnduAAhNUgech636o22ADSTd4bKHqXuirLHsksKjkP2K6hRwtgA8wiowoxgEajpPY6P22r7VJe7BaCTxArB1Rb3QKqW9Sd2SZnyErUiiVKdVVJBcsXJaZ2HvJD4ejKoAPnDAq6bJ8u16sPkjdhi"
  }
}
```

#### initiator ---> (2018-10-16 17:13:57.469)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4k2BnMJTM9URZEoU25eAa4yQp9dnG6bYEB1YJe1m2ZbD5uAJPxwUDxJRipPN7JetJHUSYV2u3RnpLJCsFG4W3yW9VGn6ddtmyXMiTurNYYGidzr5HT3RKyp7yAjGcYEXRUUramudiVxw4DJHnTXZss24BjpQYAdYxAnqJDxg92HUfT15EubE1ahcZBTTqbqVKMeLhqW1DDWr9K6dZz3tNNBtd88FBpRyEmea3rmH6EHdKWNXNLDa1JPc1vseGm89RKZdKexx6Ltk8HfJF3yVZuPS2FoPzVR4B7XfPrCWh3bEmYh"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.482)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkJXH9d8HCnVM1BXRZWdKhGp3WDPNoAGhLB3tVBk5fdnbkHkcvxQbYmWVA8agsRQSC5W8zeU5Dpb74CPzet6H6a7C8mB9wWpgsthJfcS9MP5FFJoyQcyzqziSTwRBLuf9gbapJEMMeAAQc1CzWuGVKzzQeuwHpNbmAAqYgjAaPB1BXwTuBjFWd8CA3tFXjY2mNUA6ot8cczXzB3MtGhAmuJ1J4spDws9AwgHSEKQSE7AMhVCfbHpNMok8JDLtNn7FNE5MAh6R9Pkhq3jUtceGJNx3q8HmS2PfCFpNiUq74t4hiVXm8qezttChh211XcrLuzFgy8d3LcwPz7fy2b5EtemB5PunFmTXZDWZa5cMAzdyosGCd7yRTGi8ArBqm5KeVcwCN3CFH",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.483)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkJXH9d8HCnVM1BXRZWdKhGp3WDPNoAGhLB3tVBk5fdnbkHkcvxQbYmWVA8agsRQSC5W8zeU5Dpb74CPzet6H6a7C8mB9wWpgsthJfcS9MP5FFJoyQcyzqziSTwRBLuf9gbapJEMMeAAQc1CzWuGVKzzQeuwHpNbmAAqYgjAaPB1BXwTuBjFWd8CA3tFXjY2mNUA6ot8cczXzB3MtGhAmuJ1J4spDws9AwgHSEKQSE7AMhVCfbHpNMok8JDLtNn7FNE5MAh6R9Pkhq3jUtceGJNx3q8HmS2PfCFpNiUq74t4hiVXm8qezttChh211XcrLuzFgy8d3LcwPz7fy2b5EtemB5PunFmTXZDWZa5cMAzdyosGCd7yRTGi8ArBqm5KeVcwCN3CFH",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.489)
```javascript
{
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 400
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 700
    }
  ]
}
```

#### initiator ---> (2018-10-16 17:13:57.571)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- (2018-10-16 17:13:57.578)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "tx": "tx_2M9ipLgcZajQoubLyouPV6e6zLFV2ejvgJiv1rA1Z3rs9fCNRWEAnC7M5zNoZzKhy8JMQRaXoy6VwSVLtwN3RbVmx1u5MTR6M7oKCi8MrBfCfFBZUnxRs"
  }
}
```

#### initiator ---> (2018-10-16 17:13:57.581)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8ZyWBWy48QPvEcRYhDbw8t4Ra8ZmEhCYnzfBCSM1KhJQUNV7mRg8RL9bEMktArRyK3h3CSLnwvSRGPAMhrYcbUnf36NWSncmcXVtScK2tihsQ99R8gRGty93K9Nmejh98k6foybYnqQnFmHbY9jrFRdMkmPJvV4LxSzffqHrRrp9gu4KupCwvbyXDAz1xJHwFuKc1j8hsZUZ8ZJ9B"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.582)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "tx": "tx_2M9ipLgcZajQoubLyouPV6e6zLFV2ejvgJiv1rA1Z3rs9fCNRWEAnC7M5zNoZzKhy8JMQRaXoy6VwSVLtwN3RbVmx1u5MTR6M7oKCi8MrBfCfFBZUnxRs"
  }
}
```

#### responder ---> (2018-10-16 17:13:57.583)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8ZzJ67opZiCfWTHzzrT99uJUjv5fm5NNSGCfKmymRq3ptmS5J2SiQbY4qpbvL9BxMFt1Wna1kT5Nh1G4dpVggrzyinqUMvKyPzhCnfUE49yXgKf731TTFpyj7V6Sm8X3bLAznhzCo2MUDvPCi2b3SKoWmyzAPpFrLz6Nm9PhmHdpw7C7ozfJ3MG5a5j77KLpvkQAneznC68SLiSzz"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.585)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1XR2JEQ8BAFR6Kv573P59XEwcGSoYErcRWREVcuDiXe5Dsn3EzezEz3sm6u3yLkSUJFqqMChqmYiF8JXahLcJCqkWEF5Tmyrrqoe3EgkVWdit1vmYHDkxejiAmjeo2EV7WU6PTZDpuBV5ZG79iUykEUdp2ZyhoyEW9DLnSCEuk6B1ozrnEdWwwTyoe6qxxR4vpwYBtnjY9pgN9WUXCJU19xvexBAaQ29mfQuPULSFJbgoehdd6h2uGWxfGZ3Y6oYMkmmd8jYcaqkaFLiggjsTNcPc3PXuu7XzNognojgCJ",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.585)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### responder <--- (2018-10-16 17:13:57.585)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.592)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1XR2JEQ8BAFR6Kv573P59XEwcGSoYErcRWREVcuDiXe5Dsn3EzezEz3sm6u3yLkSUJFqqMChqmYiF8JXahLcJCqkWEF5Tmyrrqoe3EgkVWdit1vmYHDkxejiAmjeo2EV7WU6PTZDpuBV5ZG79iUykEUdp2ZyhoyEW9DLnSCEuk6B1ozrnEdWwwTyoe6qxxR4vpwYBtnjY9pgN9WUXCJU19xvexBAaQ29mfQuPULSFJbgoehdd6h2uGWxfGZ3Y6oYMkmmd8jYcaqkaFLiggjsTNcPc3PXuu7XzNognojgCJ",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.592)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:57.593)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2wLhefQKWedVYAfxSrYqjkH1JHpuZa3Axp8mA45o75AT9Zx8tN"
  }
}
```
