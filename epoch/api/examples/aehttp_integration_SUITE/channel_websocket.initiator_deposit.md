
#### initiator init (2018-10-16 17:14:12.803)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder init (2018-10-16 17:14:12.807)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### responder <--- (2018-10-16 17:14:13.807)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 17:14:13.810)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 17:14:13.818)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSwSGd7X7"
  }
}
```

#### initiator ---> (2018-10-16 17:14:13.856)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmY2zjBxUnqeE3sSLz242dXzb7knKX7gzxZFCaJg27MkXzFF6tjtu551LVPquVxD9VUdA9LpGRbSAQYu7HBQrzEmVCzEGSVsEBoo3jiB7axRYySXnm59oYfUzJWAsQd4capx61KEVhHy6Q8U9xF8YNykgrUpW6BoKn4bqLigfEdM4rirX3KKmqH1WJNRgnDjy7vms4McmQxWTktDPekkXGSNKvGJx6C1dardcSA7N62SsrmdpDeuHRZkgyocpuar6"
  }
}
```

#### responder <--- (2018-10-16 17:14:13.857)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 17:14:13.857)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSwSGd7X7"
  }
}
```

#### responder ---> (2018-10-16 17:14:13.858)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmmWr8mYmXLCFwqhws2iMCSS1yzTNBVyYRyPE2RUAfcviR9WXB8p7nkZ7gcmV7EwpK5gYwhznxHHcmBegRUSw86P4y2xLC2pvtwrMUCKyausaLKV24DHoXsqyyjxK4U6xwMVrYRMVtEMWRz6sAmveHgKkynED69U9MpNexrZ7xdx1spXzNuYg2tyfBeSzoom2gwPnH6XDKrLMZ59NJ1exNA4CPd1QwG2C51tQteicx4gCrKm67dr4bCmEcVzniYqF"
  }
}
```

#### initiator <--- (2018-10-16 17:14:13.859)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 17:14:13.860)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmQr4hW9Z3NuvrEEhaFc2R3bU8wGob6atuCH1CMYtdNcq13U47MaCPU499thQDZ12aCiEJtyH8Z6BhpThp3QPqPx9ieEjiWMPC3LLaimAeuraTorCpDyFfqPa3QoR3Fm6tJyWDHNwv6JZzCTgPt6QR8E5YLZdhxYkBcgRi3w7nubtQgPvYQdXPqRJfYkFkJggJWz11gDkRPKTyKubFbnj6LRooqNgtkHVww5fD6YLSmoULRMeuWL4sS2M6pP5sUDp5APordR1wvCLbD7rimUoSrnMoTzdP9beQC6cMHrmKfzRsyfzLGMJrhAgYefEEarcR13c2EtFKxunRdu3gERCHwjCqbS"
  }
}
```

#### initiator <--- (2018-10-16 17:14:13.861)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmQr4hW9Z3NuvrEEhaFc2R3bU8wGob6atuCH1CMYtdNcq13U47MaCPU499thQDZ12aCiEJtyH8Z6BhpThp3QPqPx9ieEjiWMPC3LLaimAeuraTorCpDyFfqPa3QoR3Fm6tJyWDHNwv6JZzCTgPt6QR8E5YLZdhxYkBcgRi3w7nubtQgPvYQdXPqRJfYkFkJggJWz11gDkRPKTyKubFbnj6LRooqNgtkHVww5fD6YLSmoULRMeuWL4sS2M6pP5sUDp5APordR1wvCLbD7rimUoSrnMoTzdP9beQC6cMHrmKfzRsyfzLGMJrhAgYefEEarcR13c2EtFKxunRdu3gERCHwjCqbS"
  }
}
```

#### initiator <--- (2018-10-16 17:14:14.805)
```javascript
{
  "id": -576460752303423441,
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

#### responder <--- (2018-10-16 17:14:15.383)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:15.384)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:15.385)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:15.385)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:15.389)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:15.389)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:15.390)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmQr4hW9Z3NuvrEEhaFc2R3bU8wGob6atuCH1CMYtdNcq13U47MaCPU499thQDZ12aCiEJtyH8Z6BhpThp3QPqPx9ieEjiWMPC3LLaimAeuraTorCpDyFfqPa3QoR3Fm6tJyWDHNwv6JZzCTgPt6QR8E5YLZdhxYkBcgRi3w7nubtQgPvYQdXPqRJfYkFkJggJWz11gDkRPKTyKubFbnj6LRooqNgtkHVww5fD6YLSmoULRMeuWL4sS2M6pP5sUDp5APordR1wvCLbD7rimUoSrnMoTzdP9beQC6cMHrmKfzRsyfzLGMJrhAgYefEEarcR13c2EtFKxunRdu3gERCHwjCqbS",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:15.391)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmQr4hW9Z3NuvrEEhaFc2R3bU8wGob6atuCH1CMYtdNcq13U47MaCPU499thQDZ12aCiEJtyH8Z6BhpThp3QPqPx9ieEjiWMPC3LLaimAeuraTorCpDyFfqPa3QoR3Fm6tJyWDHNwv6JZzCTgPt6QR8E5YLZdhxYkBcgRi3w7nubtQgPvYQdXPqRJfYkFkJggJWz11gDkRPKTyKubFbnj6LRooqNgtkHVww5fD6YLSmoULRMeuWL4sS2M6pP5sUDp5APordR1wvCLbD7rimUoSrnMoTzdP9beQC6cMHrmKfzRsyfzLGMJrhAgYefEEarcR13c2EtFKxunRdu3gERCHwjCqbS",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

##### initiator: (2018-10-16 17:14:15.895)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 17:14:15.895)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 17:14:15.895)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 17:14:15.895)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 17:14:15.895)
> Channel is `open` and ready to use

##### responder: (2018-10-16 17:14:15.895)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 17:14:15.939)
```javascript
{
  "id": -576460752303423440,
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

#### initiator ---> (2018-10-16 17:14:15.940)
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

#### initiator <--- (2018-10-16 17:14:15.946)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8DsNVgYWsNxD9gKXeocxwtetdGw5LdNdfkdTFRPYEraCxFWXinaTWS1rzdxkHYctHbcNQZ1BF6j6nR1rnFiS18jVxUXs7TVLLWG9zYUKbsdXSznecQLRds8UMBoFRtUruDsWcb3WXBDaWhHBZdAqJN2GpHSNZjb2"
  }
}
```

#### initiator ---> (2018-10-16 17:14:15.948)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4r16FacHLqJWy9tWLLdL6EnaTofKxGY9UUMZbQQvNZ3FPiM5Upn4CyL9rUYn1mi9dQjc9McbZSRTfgwpoH36iydfZq31nPeD6X8W1yCdkRs39aPqoj8t7RbpQQAEtZmnaJdDtkSc3JSDLvSmSZKQ887Z4NZBXUSU6G38N1kB9ib41pukt49iSaAF5gscpAdvQDRmXfNQCTMKa1EzjLBvhhBpkmY8ijCpmBnHWcUDepp9yJvP5MHj9xA5o5PvYtPqCe5S65JwtKP5jyULN9pRWHoJpFhNGGhTNNZhXBgNn1TgsY5"
  }
}
```

#### responder <--- (2018-10-16 17:14:15.953)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:15.953)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8DsNVgYWsNxD9gKXeocxwtetdGw5LdNdfkdTFRPYEraCxFWXinaTWS1rzdxkHYctHbcNQZ1BF6j6nR1rnFiS18jVxUXs7TVLLWG9zYUKbsdXSznecQLRds8UMBoFRtUruDsWcb3WXBDaWhHBZdAqJN2GpHSNZjb2"
  }
}
```

#### responder ---> (2018-10-16 17:14:15.954)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4sQdxrKpfxebbBnn3zgjb6qbeuF5XWs4HakwTa9m1ZxwqZWNiED4DibPjWrfam78R1wKGc8nJ4wRjfCcTDVTynDQpLPF9W2XKi7X4p3UW1YuV7Qv2GCjHPt9qDDi26fM3SZyaads1A9Zwc6MD9mwLUJG4DABut4KKGxt4YjvwntV2L9mfHjXSsqFjWkj37PyUP7By1sJmeX4HWTmwrTT2gShXHNJQodmNDSZbUEG3xrMzR2jiKjAp8jhVVUWrCdBxoz4wJN8psYuzYNkVF7arAnYyDGvPRdEYVWquY8bY7dRdgo"
  }
}
```

#### responder <--- (2018-10-16 17:14:15.959)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkUofcbGqTMysTG1wqmtGD7us5JftSaJTzUXX87aCSZxzcVpC9kDoX79CiuBan53q9BMiMEsDdBZKkvs6YXQHbd7uxy8ZAYB3ZXFwp6PLJ5ytUTqsRiCjJQZhTPYdSSz1WBwPR1A3wyi3CmY8G8JUb1MARr2Tu5WUNdBZpMuTnRiiz44k2jzbWwgwLCPYSZrMHZ4LnU1gMqYi6YDK4oNYUk9x62beBcryJUDWWAywLUNJVGXARfXSfTeodFkitiPg4wvNoAiuDm77veKoGovAT4pxTFgaRdNL9HsMDP8fCyzg1h4UUGSHJVyCWuZyRCJn4bUTq37iNeRLdwUjERh7xzGdoToJXggqcXVDb2fDpwWZeLASNx6BAFGFd3QfjdGrWojYyk7YC",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:15.960)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkUofcbGqTMysTG1wqmtGD7us5JftSaJTzUXX87aCSZxzcVpC9kDoX79CiuBan53q9BMiMEsDdBZKkvs6YXQHbd7uxy8ZAYB3ZXFwp6PLJ5ytUTqsRiCjJQZhTPYdSSz1WBwPR1A3wyi3CmY8G8JUb1MARr2Tu5WUNdBZpMuTnRiiz44k2jzbWwgwLCPYSZrMHZ4LnU1gMqYi6YDK4oNYUk9x62beBcryJUDWWAywLUNJVGXARfXSfTeodFkitiPg4wvNoAiuDm77veKoGovAT4pxTFgaRdNL9HsMDP8fCyzg1h4UUGSHJVyCWuZyRCJn4bUTq37iNeRLdwUjERh7xzGdoToJXggqcXVDb2fDpwWZeLASNx6BAFGFd3QfjdGrWojYyk7YC",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:15.964)
```javascript
{
  "id": -576460752303423439,
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

#### initiator <--- (2018-10-16 17:14:15.965)
```javascript
{
  "id": -576460752303423438,
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

#### responder ---> (2018-10-16 17:14:15.965)
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

#### responder <--- (2018-10-16 17:14:15.969)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8KHtME5z4ig8ufreYwJJPwffijGubw2FAdeUM1fT6PJq4wT6quZmHaDQKVXSdhEqQSxi7oSqAAtcxFXXcfXJXEzS5DRyazfw55pvPub52yTu4wj9yPNjaSpVsdfrLD3uSmfPqFWQe7qc23aZrALykGkJ2KUZ3rCh"
  }
}
```

#### responder ---> (2018-10-16 17:14:15.970)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5B4mboT1nf7QsXdHi4AfiAXvwrswnSQFjEVtCSGn2qpRDpxmoT5xscJoBUatgKuhur6wCGgwdHSAJEgiietCpRBXi1A3bVrVcSkXyLzCx13djkD4jPhvY1WsFmbMEDEU47jCD5eXWq4GXDsZqKPdvAeS3PeoLpmDgntH756Q5X5JDvgLnrAzWWWKQupRrBF5vygtT1Q2kDnsxEtxiqzYSo51FWgqJ99n1DcGbChYhKnFfWaJqNerZixVoBEFTjBpbJhSnHG9cy8ATL476KxmZsw66hGpuWi1SjE64tCeMeCiW5L"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.7)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.9)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8KHtME5z4ig8ufreYwJJPwffijGubw2FAdeUM1fT6PJq4wT6quZmHaDQKVXSdhEqQSxi7oSqAAtcxFXXcfXJXEzS5DRyazfw55pvPub52yTu4wj9yPNjaSpVsdfrLD3uSmfPqFWQe7qc23aZrALykGkJ2KUZ3rCh"
  }
}
```

#### initiator ---> (2018-10-16 17:14:16.12)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4oAjd5deSPU2xbSsdRR4bbBFNYMaUKyiWcsugS29XasfxNc9yA3r2qxwex8EQSbPguFo2jgkuiYN2AYpQoejkpW4YyditbAYM7JHHt1UGMJarHv5JD1k9FjufZwbyQrdQaL78U6iHCDRnkHPRA5rwwXbGiAVCoQ1UvifdVGcHcz1DQDzLqNV17JTVn6kUD2yGGk21GZTdYUkmnXJYBx6tZddQpXvXVbAVgXfx64EiWC6DmTo6hpWMAmpAFRckqdWmaLYDe592WmJVu5gRRNHGNQhcu76kodnBFmKGxmygtfzZxf"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.26)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkPw7RZZ8qv5tQ5QBDnyQYSaeHds92oWGxdHko8y1rXyQya5AqdL82iy7upx64t3RzXQibf2gZrnwHvBvESM32Er9xwUbJchuKh1WxmFrccEnX59DyJt84aJ1qffGBGRjwcbQi8P5shjWwQRJqu4JFrxbQES67NntLngwSEMkS18fENuHqtM2yCGsTKfTjfuh5ZkitYtcJrQsvPHgh4bRPu9t7BJ99mdZs2nTAgAEDzvK7d5D8vfakKTGdPDyZjJcqCJsJgbGtppfEQYxjS6xiyxhW3DR8fmtdDzKBzCfzAygUfAXkr67YRLk1ijARfwBMEKDdXyjphyU7bWSHYYP86TdU2djzdk8ukwXRi16Amn5eG7vMKmQzeXuZvCL85bT3CG86FV8J",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:16.28)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkPw7RZZ8qv5tQ5QBDnyQYSaeHds92oWGxdHko8y1rXyQya5AqdL82iy7upx64t3RzXQibf2gZrnwHvBvESM32Er9xwUbJchuKh1WxmFrccEnX59DyJt84aJ1qffGBGRjwcbQi8P5shjWwQRJqu4JFrxbQES67NntLngwSEMkS18fENuHqtM2yCGsTKfTjfuh5ZkitYtcJrQsvPHgh4bRPu9t7BJ99mdZs2nTAgAEDzvK7d5D8vfakKTGdPDyZjJcqCJsJgbGtppfEQYxjS6xiyxhW3DR8fmtdDzKBzCfzAygUfAXkr67YRLk1ijARfwBMEKDdXyjphyU7bWSHYYP86TdU2djzdk8ukwXRi16Amn5eG7vMKmQzeXuZvCL85bT3CG86FV8J",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.35)
```javascript
{
  "id": -576460752303423437,
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

#### initiator <--- (2018-10-16 17:14:16.37)
```javascript
{
  "id": -576460752303423436,
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

#### responder ---> (2018-10-16 17:14:16.38)
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

#### responder <--- (2018-10-16 17:14:16.43)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8QiQCmdTG4Q4ffPmT49JBFCQHAqyacvNagY6GVR8q8urZCsDWkw1wWxZQwEENUKw65vLcrmG3RWZEg7EKvPxTF7kJAHuAZPLkTKAnGYVXZj9NcGzg8f4MqaqWr8VtAEutjfy5odiyz5WFoGBePUEBWFCmFZFP9xt"
  }
}
```

#### responder ---> (2018-10-16 17:14:16.45)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak519snsJiRPC1GTw3SR3NrMMo5oD5b5Cok3196u9kXCLHnY9Zf72EEZ1Lexu1kf7MVzETPMqyDaXpKkrt7xR1R4YPyMhusKCD4DDmcVk7vR5duUq3sKhFbt6jguti3ZYhHnDcfZPxfAoqpzgtaeJxcLAVDqXEnPXkdBdEF9jES9W8fMK25vkH4FTLj8x6Vvdak2yMB9CtNJMNtX75wGAbhWEqSjy7ryrp6YxBzXVv3fxvgkCmGQwpEeUq6Spap426R3UiYiAw8zTDrq6gPqajyBvgoWee6yaTcifW3ytNtmZGFwA"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.49)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.50)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8QiQCmdTG4Q4ffPmT49JBFCQHAqyacvNagY6GVR8q8urZCsDWkw1wWxZQwEENUKw65vLcrmG3RWZEg7EKvPxTF7kJAHuAZPLkTKAnGYVXZj9NcGzg8f4MqaqWr8VtAEutjfy5odiyz5WFoGBePUEBWFCmFZFP9xt"
  }
}
```

#### initiator ---> (2018-10-16 17:14:16.51)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4qZXmEWPhvourEsHDBmufRbpqpsL76fLkRP3Nv1dKaUKfQoGN8gJV2W6JADbqjZ4De9p7rW9QNzkwNNjRVmxa8WeQm2sQhELNX9UBZMpeHAS796SfuZnjxm2NTesALVJr3Xte1vuU8Jh9buyAD2cPABQWknjwUpBzmzVNf8utQD4JymW8ZUqY39XNxG2LmWGaq4uaHVZwpBTUMJ5kpQWA3SpvioaCnQ4TTeXvudcEC6Qs5ECEK12PXcZ9ogg9TDGqNuARGgyg9FeGmiPLzhmzfwVuqZQgX9jpxQ9iQ8U55oS1Nb"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.55)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkU3iy4gv4xmd59n3kxtodkAPgZv2NUunBuV97anx6PC1YTuQUXj9j1CPTjAR4EtFDWMUDm23MiDHKJQ1PNAL7X2g49P4KAHJEFiWR3UNZgFfR3e1L11zTASd9dvbZjSmUeTf24JQ3YPn54Sa6XWCRTeJNkr2AL9aPUyqMqQ8FaeuPYH48HrdfA99kGRBuDzgoY1hN14f7kshL3t9GkNzew9Lp48zuoScYk8NN8uSGJCT1Pt8pAXQP8jp5ExA3zMHVra7uMVG4K5sbh9rsDqYZqtKS8a2jLgdVUpp71o2CzKAueCbXdCF4UbQ72uDjMKdLRp36fuqfetFLfeemRzdjvDP9m84zDvoep9DwKsd8xFqKBL27KNGVGd3XbvH1G1rBeM6dXzBx",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:16.55)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkU3iy4gv4xmd59n3kxtodkAPgZv2NUunBuV97anx6PC1YTuQUXj9j1CPTjAR4EtFDWMUDm23MiDHKJQ1PNAL7X2g49P4KAHJEFiWR3UNZgFfR3e1L11zTASd9dvbZjSmUeTf24JQ3YPn54Sa6XWCRTeJNkr2AL9aPUyqMqQ8FaeuPYH48HrdfA99kGRBuDzgoY1hN14f7kshL3t9GkNzew9Lp48zuoScYk8NN8uSGJCT1Pt8pAXQP8jp5ExA3zMHVra7uMVG4K5sbh9rsDqYZqtKS8a2jLgdVUpp71o2CzKAueCbXdCF4UbQ72uDjMKdLRp36fuqfetFLfeemRzdjvDP9m84zDvoep9DwKsd8xFqKBL27KNGVGd3XbvH1G1rBeM6dXzBx",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.60)
```javascript
{
  "id": -576460752303423435,
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

#### initiator <--- (2018-10-16 17:14:16.61)
```javascript
{
  "id": -576460752303423434,
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

#### initiator ---> (2018-10-16 17:14:16.62)
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

#### initiator <--- (2018-10-16 17:14:16.65)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8W8v4KAvTQ7zRevtMA9xHoF6JbeHGh51uuJK1rebT7PHR3ksjLgDUGFLGy57VstBLWVFuixTtraudgkxv2LPo97SdK7dr9dZNciu9dLb5eRGMzQEPaCh4bKaG8Fw8Eh5Yid5yiaqsLej57na9xvMPdccrADLjpFb"
  }
}
```

#### initiator ---> (2018-10-16 17:14:16.66)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak57EQss2HaTnFJL3CKxVyYxhCYr16zwG4FLtm3kEqM32H63kbhXefnSPbfa8V4jypTBP3zBJ9sXxq4V8Cn99QfjPQvbN1HypoYkwo3MMY8h9f1wToE6vUj48wqYuBH3KfDU6P3mKBbMQwD3bTF2ybFztJABzHkeWbkmSkYhVJDSwrcPhdZUnvuwAShXKWmhsXQZVWwdKUFyaibTwCxLm7fzA8vS95gyLN1w7P853pCxaCJ4RHqG6ejDwf6AbbXLRVRRkdC3H11TqvSLptQm8P8JtaiK8Zcu3BtHreqA9j1gt1URN"
  }
}
```

#### responder <--- (2018-10-16 17:14:16.97)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:16.97)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8W8v4KAvTQ7zRevtMA9xHoF6JbeHGh51uuJK1rebT7PHR3ksjLgDUGFLGy57VstBLWVFuixTtraudgkxv2LPo97SdK7dr9dZNciu9dLb5eRGMzQEPaCh4bKaG8Fw8Eh5Yid5yiaqsLej57na9xvMPdccrADLjpFb"
  }
}
```

#### responder ---> (2018-10-16 17:14:16.98)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak55GDh61XfeGRosyxGccFLwNfenGxdkh3tA8o5AsVUoDaHPsBYtKMJmu8muirwS8TY6kkaVxUNEdFx56kdwJA2Aa3Ntq72myXUdTPH8hwRufEZTyz61o3begTy2zScNLuEjRi4BU38J6Yvs1ZCTXy9ZYby1LZPsSDWH42d18pgdsDxgfzVCZDPGK5JVjmYGjRZnmoATJRn486DUbk4TLVwSen4BXkkiyz1Nq5aohbyPAQwMuQQDocMVSwhFCcUK9VkBqK6FbYrZXZN5xJvRH1v8N6EzreX5YTyxb4dsftxzfyDeZ"
  }
}
```

#### responder <--- (2018-10-16 17:14:16.103)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDksbvjLPnxc5CpxoLmKHJMa8vL7VaCYngvSSXJUfFUYjv2s4YnkWAYaRstcT4E9wsDUbCSPZGPTiVncFD3oMUxebe19HEz5NDBtw5TarH5F2ferMoM3GHFU3Qg5ybFTTKieRe1Qk74moMj64HzjTiMN746VQionrgMQq985yG7DnqnZW7UbEjgvrCm1ADZZBUE1euxTkbgKsZkQrsfLHhgXpptdYCusWPn7woTQRwoo9i31gjHw9QmY351B2Rvyj1bj7kn7x2uDQubwsqGG9gMGQpyDfWX7gwSzSrMgsQrXDsCRrEKAUSjobAnCpHdGPXZcrxi7iB1EKsBJ1j8ryKS4c5yDLtpArUydBP5NL1ZazkJf8VNhqEyWzfYDSbx8UfUDxNzPWqP",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.104)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDksbvjLPnxc5CpxoLmKHJMa8vL7VaCYngvSSXJUfFUYjv2s4YnkWAYaRstcT4E9wsDUbCSPZGPTiVncFD3oMUxebe19HEz5NDBtw5TarH5F2ferMoM3GHFU3Qg5ybFTTKieRe1Qk74moMj64HzjTiMN746VQionrgMQq985yG7DnqnZW7UbEjgvrCm1ADZZBUE1euxTkbgKsZkQrsfLHhgXpptdYCusWPn7woTQRwoo9i31gjHw9QmY351B2Rvyj1bj7kn7x2uDQubwsqGG9gMGQpyDfWX7gwSzSrMgsQrXDsCRrEKAUSjobAnCpHdGPXZcrxi7iB1EKsBJ1j8ryKS4c5yDLtpArUydBP5NL1ZazkJf8VNhqEyWzfYDSbx8UfUDxNzPWqP",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.108)
```javascript
{
  "id": -576460752303423433,
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

#### initiator <--- (2018-10-16 17:14:16.110)
```javascript
{
  "id": -576460752303423432,
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

#### responder ---> (2018-10-16 17:14:16.110)
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

#### responder <--- (2018-10-16 17:14:16.114)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8bZRuriPejqvBeU1FHqHjrFsQ3z7XzidQnKL7SvWJe7uXjhSrTfXFQSsbpdor2W8TMqbcyQ7ovkRoXGdkS9GKFNNk41kKgpA7CHfYzTLWkFdywMDLZQpeugzrK3Wzskej3zUjG4FprWv4DCAap8ozZF98vWpSEnG"
  }
}
```

#### responder ---> (2018-10-16 17:14:16.115)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4v5MP2CuP2Q6wPiy5c8JxnXX3DeWLBTXpu7JvFAebwYjtgp3FE4CAi39MgS22An7LRx2E6XJjNy5eT5yBD4rnX9oTjbvLTKsm3WSr2bhM6JPWRPXKMyxtoZm5ACWZEbaJgiKZC8wMBTKaDXb3wdm6NqB7STubz4tQAx3PzssU2QTuWNmmkM1fbyGBh76WrgZteWaUWrwGrh7smXPrQcfmbwvnDbAWahgdHg5dHdwSsSDEXTHtmAHx2kED6UroY4fiY8d9BsHjKKsgChU6kdpe8yvX2Yd3c3Jtv92mzBC7jQCRH7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.146)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.146)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTMs2x2a8qfefUK5LpadWz5uQaES2tr3FxrEE5NMnyNor8bZRuriPejqvBeU1FHqHjrFsQ3z7XzidQnKL7SvWJe7uXjhSrTfXFQSsbpdor2W8TMqbcyQ7ovkRoXGdkS9GKFNNk41kKgpA7CHfYzTLWkFdywMDLZQpeugzrK3Wzskej3zUjG4FprWv4DCAap8ozZF98vWpSEnG"
  }
}
```

#### initiator ---> (2018-10-16 17:14:16.147)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4wPcZh2CgkWADxa5xu5wRMm4a4Fm9rpx2vj62HtA671dczGtqQfySjN589ZnFjBBUrUEm9oxTUhyQm2NvRwvJJ44VC8ubNJGndEioq26pCVR9JJB1sHsRBPeV6tjgYLG4xU1dsRXuwqLi7qJM6kCCjk4sER1g2a8WvrCvDUGwT5udy5ybBKpFsm7UDfhKsoY8tehWE81tuSddivduMpUTMEx7ZYqNP3bipWwpPLKMGAsp35XmMDEJSNvYuFeLxJfBw934Gfa7YwMg7K5da1KjvZohLT6BgJy2e5ThZU5DSCJ2gJ"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.152)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkboqbKdFjEvpbfeZezFebX5iRyYtKLNodaopQuq6XpbnPVCwnus9NiyviFqmknnkDJYke1CNJype7oXDcoFMhwBxcEWdZf9eGzFuXAnYkceLvdECJR55sQg5QXQU3FoU2EH92DQ3sCfRShzwjydpJUTweyAegjYnf9JhGViFFUSN4Sajw8ReGUjwXuDPAQAJCtLH6ReG5Vq6CMfh8Ub6UTQXvYEMn7emQwx3tzqMDZ4Wy1PWpJDL9K5Z2rRN9eTqeEZAt2Lj5vNPGJhHvkzSKec1gARMqgNpyE2AXTXrSXcbMMuEVzHfhH252JEXyCtmkEq7B3yyToC68Hzv45Sv8YF7X6G2e71FFcERXkfpk3smwVhKnr1gVrQyQiujfXu32eMypsVBG",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:16.153)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkboqbKdFjEvpbfeZezFebX5iRyYtKLNodaopQuq6XpbnPVCwnus9NiyviFqmknnkDJYke1CNJype7oXDcoFMhwBxcEWdZf9eGzFuXAnYkceLvdECJR55sQg5QXQU3FoU2EH92DQ3sCfRShzwjydpJUTweyAegjYnf9JhGViFFUSN4Sajw8ReGUjwXuDPAQAJCtLH6ReG5Vq6CMfh8Ub6UTQXvYEMn7emQwx3tzqMDZ4Wy1PWpJDL9K5Z2rRN9eTqeEZAt2Lj5vNPGJhHvkzSKec1gARMqgNpyE2AXTXrSXcbMMuEVzHfhH252JEXyCtmkEq7B3yyToC68Hzv45Sv8YF7X6G2e71FFcERXkfpk3smwVhKnr1gVrQyQiujfXu32eMypsVBG",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.157)
```javascript
{
  "id": -576460752303423431,
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

#### initiator ---> (2018-10-16 17:14:16.232)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.239)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "tx": "tx_2C9es4FjJC2PjRAMBS8VhaP2Td13cn5krWN7BHdJV6U44McPcwqWGYCcAMY11hb44nWCsL6hbyhzkXNapQGjbscnmejoovsMr5byFqPgPqaREghRBx5eDQyGyft37CNiWNRVY62T8V9GkoEgXVaVfChDBhktcX"
  }
}
```

#### initiator ---> (2018-10-16 17:14:16.242)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "tx": "tx_2WsEQsiC5Xsnna5tZr3HFZExbVQFXckmtLACodLBJwAUhW2T2gM34aHFaBYN2yfQ1rq9UAiRyFEcrAbTMA53BbcHYhPXijNrMHxcjSdJ1qYTeR9Wti46eEkiTHMh1mouQKAGGtYWoCN7KjBaH82GZbeAGUgEeKYjhAxtHkUhtQDPd8LJizSZNeGEjyXxVBHkXcg7EpeCyPq2ZoKau1XFKaY4rSpaaimAmf7TMrN7EK8cGE9opECZYcFAi7CkoYXVxVX"
  }
}
```

#### responder <--- (2018-10-16 17:14:16.243)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_created",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:16.244)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "tx": "tx_2C9es4FjJC2PjRAMBS8VhaP2Td13cn5krWN7BHdJV6U44McPcwqWGYCcAMY11hb44nWCsL6hbyhzkXNapQGjbscnmejoovsMr5byFqPgPqaREghRBx5eDQyGyft37CNiWNRVY62T8V9GkoEgXVaVfChDBhktcX"
  }
}
```

#### responder ---> (2018-10-16 17:14:16.245)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "tx": "tx_2WsEQsiC5XsnSKaQQmnsdBvsqgyTSRrSHtTJU3UsGStT5NRbJHuAP5YgFNKKXDJYvcaqXqWPeP4H3EU2DeLZHUJudX6VqAz5cZBAzhEyQWdQruxiNrT7CKNTpJJYA8PgKE5ezxDf4F7VrFfodBDbUtwFCJuVfapJPup3bgstyqzTchTj7555kNuiHBB3YyJDUbWEdGnqJuWjkADabvoHCUcnu8cxqTU2jx19eZVkS3MbQ1WfBw58KUHXGxAVLupiru4"
  }
}
```

#### responder <--- (2018-10-16 17:14:16.246)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBzV7SdgXrTudrn8XdY3aJFbpfH9dGDWrQ9GKDZaEzE6QqeX2K9akni2AeqgkY8N2CGUhDbV96FFSNjF3GgB6rvJmeo6e3okcntAFH58nKsu8e6JwZ6G7qqxMVKFfFjbpY2TN28p5XqJyd92SfnHNpYep586Koar91Qf6CJFu41f3v88mu5BP7HEYtLKTSxfYsNC4xTh3bk5tEu2tXThmsTFsE4MeW5auifLA7Qe5hcrHzHb9aX9MUpUHG4fCwibPSFFKFh6iZ9cUWZwNTGpj4WP7FutR8fhcQigAyah3TFB4eFAyAH4UACpow5JNcccuRaHKMKzwV1rfcvptiqT",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:16.247)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBzV7SdgXrTudrn8XdY3aJFbpfH9dGDWrQ9GKDZaEzE6QqeX2K9akni2AeqgkY8N2CGUhDbV96FFSNjF3GgB6rvJmeo6e3okcntAFH58nKsu8e6JwZ6G7qqxMVKFfFjbpY2TN28p5XqJyd92SfnHNpYep586Koar91Qf6CJFu41f3v88mu5BP7HEYtLKTSxfYsNC4xTh3bk5tEu2tXThmsTFsE4MeW5auifLA7Qe5hcrHzHb9aX9MUpUHG4fCwibPSFFKFh6iZ9cUWZwNTGpj4WP7FutR8fhcQigAyah3TFB4eFAyAH4UACpow5JNcccuRaHKMKzwV1rfcvptiqT",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:20.25)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_deposit_locked",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:20.25)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_deposit_locked",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:20.26)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_locked",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:20.26)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_locked",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### responder <--- (2018-10-16 17:14:20.29)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBzV7SdgXrTudrn8XdY3aJFbpfH9dGDWrQ9GKDZaEzE6QqeX2K9akni2AeqgkY8N2CGUhDbV96FFSNjF3GgB6rvJmeo6e3okcntAFH58nKsu8e6JwZ6G7qqxMVKFfFjbpY2TN28p5XqJyd92SfnHNpYep586Koar91Qf6CJFu41f3v88mu5BP7HEYtLKTSxfYsNC4xTh3bk5tEu2tXThmsTFsE4MeW5auifLA7Qe5hcrHzHb9aX9MUpUHG4fCwibPSFFKFh6iZ9cUWZwNTGpj4WP7FutR8fhcQigAyah3TFB4eFAyAH4UACpow5JNcccuRaHKMKzwV1rfcvptiqT",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```

#### initiator <--- (2018-10-16 17:14:20.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBzV7SdgXrTudrn8XdY3aJFbpfH9dGDWrQ9GKDZaEzE6QqeX2K9akni2AeqgkY8N2CGUhDbV96FFSNjF3GgB6rvJmeo6e3okcntAFH58nKsu8e6JwZ6G7qqxMVKFfFjbpY2TN28p5XqJyd92SfnHNpYep586Koar91Qf6CJFu41f3v88mu5BP7HEYtLKTSxfYsNC4xTh3bk5tEu2tXThmsTFsE4MeW5auifLA7Qe5hcrHzHb9aX9MUpUHG4fCwibPSFFKFh6iZ9cUWZwNTGpj4WP7FutR8fhcQigAyah3TFB4eFAyAH4UACpow5JNcccuRaHKMKzwV1rfcvptiqT",
    "channel_id": "ch_2g16QqxzCV8pNPRPwZpCDNN7NKcGrMTJ2wGMXeTSpMBFEPcuxt"
  }
}
```
