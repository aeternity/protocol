
#### initiator init (2018-10-16 20:26:08.348)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:26:08.353)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:26:09.353)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:26:09.355)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:26:09.365)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBp9bK94L"
  }
}
```

#### initiator ---> (2018-10-16 20:26:09.405)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmEyDhVeYt4MXnW6ApyYFMBy7t6zWiMDFVfW6aPnn7kuswBTKyBYrAT3TxZN6QwZ39agucW2wdGidvGGzAPvupkzTnmJkYjsCbXMSLM53aZHJQ4BaLFuakNWqv7xz6bDfQZWBgPaRzizT5sa4yMhwrw6tNkgAV2U8bKVHs7itbHdEXa77QzHGDs9xEDgez5qYmab15iNjwWMd5yoNrHEhUiTeoE6ygQM65JQDCmiodWmfD4x826KuNSW7KGVEenMj"
  }
}
```

#### responder <--- (2018-10-16 20:26:09.406)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:26:09.407)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBp9bK94L"
  }
}
```

#### responder ---> (2018-10-16 20:26:09.408)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkTQK2LygNLMPzgnkNAg5LPHD3pmiWoiE6ULay8bmDi7tHTrcU7YbPyTbGmaLWjUBkLPbRB5p3rDhHBGQizyd8Y1GGtWRjo4zydNhpxD7jGAJ7oN9H7FY5C1FPTMZZmE6GegaPXBWuFKmBAfjfwzX13edN4AVR7m3jhHtcLAeShWw8DNzCmLe9u7yvwCU95pw1EboaUjyS495XCth8rs52hu8gDS2DMFAAdkHiDREr8HboemcEkT5xyBRwVkKFo25"
  }
}
```

#### initiator <--- (2018-10-16 20:26:09.409)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:26:09.410)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNzPWDRTVCo8WD3Sj8tFvuXN75TFD948c8nnS9zufDdZCtuDzfYQQDY6A7kZg8UJT14SMPBGKJet7kH7nhTDGZwPjtHSdTM1yhmz2Bu4FQRyKiHeT4MUg7y2GSWb8asgrrBTGSeZcpHXpnSAzEuJRcuBiLPc8HotWQBCWazAqzELs9w2DRK5hrxPy43W1JW79NnYMvUAPanb87B62T6PNmjHzBAfjArvBt7ZHkSGrb2sG5ndCwL36uegYTDPevvmNofc29TAAo5tgp2FJgChUrq7pDEuauzx8CYV5RL1dGWysivUs8zF61yM19kb3eL8A2t4FriMhhWfMXpz7CK9sKcvkMX"
  }
}
```

#### initiator <--- (2018-10-16 20:26:09.411)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNzPWDRTVCo8WD3Sj8tFvuXN75TFD948c8nnS9zufDdZCtuDzfYQQDY6A7kZg8UJT14SMPBGKJet7kH7nhTDGZwPjtHSdTM1yhmz2Bu4FQRyKiHeT4MUg7y2GSWb8asgrrBTGSeZcpHXpnSAzEuJRcuBiLPc8HotWQBCWazAqzELs9w2DRK5hrxPy43W1JW79NnYMvUAPanb87B62T6PNmjHzBAfjArvBt7ZHkSGrb2sG5ndCwL36uegYTDPevvmNofc29TAAo5tgp2FJgChUrq7pDEuauzx8CYV5RL1dGWysivUs8zF61yM19kb3eL8A2t4FriMhhWfMXpz7CK9sKcvkMX"
  }
}
```

#### initiator <--- (2018-10-16 20:26:10.470)
```javascript
{
  "id": -576460752303423419,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:26:11.393)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.393)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.394)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.395)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.399)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.400)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.401)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNzPWDRTVCo8WD3Sj8tFvuXN75TFD948c8nnS9zufDdZCtuDzfYQQDY6A7kZg8UJT14SMPBGKJet7kH7nhTDGZwPjtHSdTM1yhmz2Bu4FQRyKiHeT4MUg7y2GSWb8asgrrBTGSeZcpHXpnSAzEuJRcuBiLPc8HotWQBCWazAqzELs9w2DRK5hrxPy43W1JW79NnYMvUAPanb87B62T6PNmjHzBAfjArvBt7ZHkSGrb2sG5ndCwL36uegYTDPevvmNofc29TAAo5tgp2FJgChUrq7pDEuauzx8CYV5RL1dGWysivUs8zF61yM19kb3eL8A2t4FriMhhWfMXpz7CK9sKcvkMX",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.401)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNzPWDRTVCo8WD3Sj8tFvuXN75TFD948c8nnS9zufDdZCtuDzfYQQDY6A7kZg8UJT14SMPBGKJet7kH7nhTDGZwPjtHSdTM1yhmz2Bu4FQRyKiHeT4MUg7y2GSWb8asgrrBTGSeZcpHXpnSAzEuJRcuBiLPc8HotWQBCWazAqzELs9w2DRK5hrxPy43W1JW79NnYMvUAPanb87B62T6PNmjHzBAfjArvBt7ZHkSGrb2sG5ndCwL36uegYTDPevvmNofc29TAAo5tgp2FJgChUrq7pDEuauzx8CYV5RL1dGWysivUs8zF61yM19kb3eL8A2t4FriMhhWfMXpz7CK9sKcvkMX",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator: (2018-10-16 20:26:11.781)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:26:11.781)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:26:11.781)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:26:11.781)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:26:11.781)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:26:11.781)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:26:11.815)
```javascript
{
  "id": -576460752303423418,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:26:11.815)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.819)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqAcJJsx6FRdrfr2KjCYM8dtkAeMTgGXheLsWa5yoNshvU99CDvB5hLNyfcb4a9fiPLaH4pnGBbTKUHpRnQjT8YuiJvM7DScfEBooYUWUGF2JiQDcKTDRALQqKmmqGDVmWiL6THBiMhxPQ7dTJv7ZneoUhmvvoDSt"
  }
}
```

#### initiator ---> (2018-10-16 20:26:11.821)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak51qeXkq2kFb52PC9h9RCnZAn4TihJmN3VC3oreUsktrQCQHuRRwtJXfsvRoxS68bqM8bVYHk3vYQMJDiKH8TgrGFeNTTcdNZzrLjcz2LAxQqNVsu6zyDaK8fuJjiRHefevVMmhRUc2HdZpPHuDUkwEVDBakeYMYjnHyfo2EeZ6fpU9rrBSNFp7D4jXLKMCNRW9Copo5Go5ThGHKWbWC39oxgP7a4mpN2aXZSa21sAXrenFZyTw3coHVCc3dhR57oQAwrENUugQet9dTGFt1cshYhve3K9s7zoovgpxz2ymexxtq"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.825)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.825)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqAcJJsx6FRdrfr2KjCYM8dtkAeMTgGXheLsWa5yoNshvU99CDvB5hLNyfcb4a9fiPLaH4pnGBbTKUHpRnQjT8YuiJvM7DScfEBooYUWUGF2JiQDcKTDRALQqKmmqGDVmWiL6THBiMhxPQ7dTJv7ZneoUhmvvoDSt"
  }
}
```

#### responder ---> (2018-10-16 20:26:11.826)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak58QFRSV9ZEHtvWdVWM1mw3y1GcZT2Uoavn5Vokywizuzgb8vMd7rkw3DE1VGcXAj7is5sNXVom51z96JBs8sJ2Z18iVyiw6cvG6qtRRG7kcnRKdpN3WYqf3PTygRjqMJoLvAxTyVdVDvrZAtxoEQz9jhSeS7tMDPJujQPVYJJakETYSi7jCo9W6M65A2YbjedRQbWRszfxxc1BFAL4ohJLS3sDRWW8kyGmePuuLYphs4rZdzzo4gJv2JCL5fi1fzs3FcAvgu4PGYZpPkqbX8TTv7eJfuNTc6nPh3z4G2YksF73G"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.831)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkmiYoDQaC6grMYrPe1vpvAxAzVDf32ZwZ6BuzeEee5wqpdmYibLuYN1CWxU39igkaANMKfegg7gxBHjR5iv7GmLdicebK6Hz5p6GAhkhCq7qSBXcn78n5govUUoCD6zSpfvGADxe6jPBz4xQBw6wPz9szseTWwnMGerte6nrSNjxnAc9W3Y2kaSKfS6JjYECGEQDH37i39RA94uQB48YzqgWTxWfyjCC9AAU7F8sdxadmsd8edC2zAPTi7n6wXfz54p8ZTrXz5WEwmB82CiXm1QJ5XvMUhQ631K6Ko8BSQ2gocL8wXQtP4U36NgNxBPkRhYmX2XwaE3cc1ucASdCWc9YBQous7eux9BphHA5L6zofvMfXz1t4fdrhKubiJGj2YHgVQDoi",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.832)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkmiYoDQaC6grMYrPe1vpvAxAzVDf32ZwZ6BuzeEee5wqpdmYibLuYN1CWxU39igkaANMKfegg7gxBHjR5iv7GmLdicebK6Hz5p6GAhkhCq7qSBXcn78n5govUUoCD6zSpfvGADxe6jPBz4xQBw6wPz9szseTWwnMGerte6nrSNjxnAc9W3Y2kaSKfS6JjYECGEQDH37i39RA94uQB48YzqgWTxWfyjCC9AAU7F8sdxadmsd8edC2zAPTi7n6wXfz54p8ZTrXz5WEwmB82CiXm1QJ5XvMUhQ631K6Ko8BSQ2gocL8wXQtP4U36NgNxBPkRhYmX2XwaE3cc1ucASdCWc9YBQous7eux9BphHA5L6zofvMfXz1t4fdrhKubiJGj2YHgVQDoi",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.836)
```javascript
{
  "id": -576460752303423417,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 698
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 402
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:26:11.838)
```javascript
{
  "id": -576460752303423416,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 402
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 698
    }
  ]
}
```

#### responder ---> (2018-10-16 20:26:11.838)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.842)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqG2pARVZSmMnRqZSdKVtG9zNmnEghwBtkYnngBitg36TrdhVPQjgRXTnP3kr2bce2WLN8zVttKcbVhCjhQqLNNdgFVAWHCPrtSjp8mB4bUqX72XF5fgnR9jWDu5vwYVx6JQPf1LNVGDcqBsdC61XPFfDdFoCsoUq"
  }
}
```

#### responder ---> (2018-10-16 20:26:11.843)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4mwtQyC4e3dsjd8XERCWZ7pUxFfzgscSd1HiLiFPkBRSfFbEL736y6Sjtd7FWB4pwJ9nyCAQcEm1kJwJ4AN8HeezCrW66kNsETdxJTFFTuFrbpZXWsZZrR9gtPG2WeYHUd2askDNcceNPnxajv82Hhsee4QB9hgJD4ckDgPjTQZTugqPnDTNWmEjn38e4mFHrz3mGYcn2enmNFxWs4qKg5eE21caAxhCyRMBUtsDEcVp19LBPSiKZgirJxq1zmEdjSbA3tqHMBAPvWNHAhCJWJXZdmX74LKxEMGsMUQTdW3pnFS"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.847)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.848)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqG2pARVZSmMnRqZSdKVtG9zNmnEghwBtkYnngBitg36TrdhVPQjgRXTnP3kr2bce2WLN8zVttKcbVhCjhQqLNNdgFVAWHCPrtSjp8mB4bUqX72XF5fgnR9jWDu5vwYVx6JQPf1LNVGDcqBsdC61XPFfDdFoCsoUq"
  }
}
```

#### initiator ---> (2018-10-16 20:26:11.849)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak52Et9qeQLf3w8ECcK8zT5VLrutf6rxw1vZtzJU2zbWPy9SfL4qvEzepHRGtKEjHZgctHF9AgjbXe4FKvYe1Sd3TiyaCbpeSJ8rbGF8GmtUnmEheHQWraNtJhppQB2x6CxQCN1N9xJq9zjkXFqS8e9dQsvNJAXum52dkYgGMEgkVhWycFeXwrYdomp2gVYER8jMduzdnLNzEGH2wPLGQW1GY9w9wSmvhzvVFA1ovyQCpDVqgkamY7NkiZJNue39hngp8D8uoEtVEBku7EUWzoxzEwNvsFvfFmtZYcLWSfLMCJHab"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.853)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkMqK1DGKAocezeYGF3K8yNYJX8Dvt8Uk4QEp3N9ieQuZ3Jc8aStDfMcsDVkYgyjgRr9o7JNwcsRG6xDYUMV8VMDME4HejfhByzcExtGD7XPG4qeNazgS3iz5wsakViKd5E7pyPrxziCNn4WqjDmPPW14davZwmQE9uqmgxU2KoXuZrjn6XivZK5tRGJPL6Nx3huh5kfUgyFYJsD5G4jMppgcu6RWwWHgaWogrBxtCTYP8rbz3GvQ9oy3ErGZanV85i7Tk8RALU7L4LZ4xCwG35Zg19uvbpQwoxSwot7FY1AueteBNNoViabAoQE77TL4tgZqC4cbVQ3w6SeE2sVhQKFTWjuHH2E1E99mjD9BHsYx9f51uwHZ2qsdxeo7J4joJH2tsXfAd",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.854)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkMqK1DGKAocezeYGF3K8yNYJX8Dvt8Uk4QEp3N9ieQuZ3Jc8aStDfMcsDVkYgyjgRr9o7JNwcsRG6xDYUMV8VMDME4HejfhByzcExtGD7XPG4qeNazgS3iz5wsakViKd5E7pyPrxziCNn4WqjDmPPW14davZwmQE9uqmgxU2KoXuZrjn6XivZK5tRGJPL6Nx3huh5kfUgyFYJsD5G4jMppgcu6RWwWHgaWogrBxtCTYP8rbz3GvQ9oy3ErGZanV85i7Tk8RALU7L4LZ4xCwG35Zg19uvbpQwoxSwot7FY1AueteBNNoViabAoQE77TL4tgZqC4cbVQ3w6SeE2sVhQKFTWjuHH2E1E99mjD9BHsYx9f51uwHZ2qsdxeo7J4joJH2tsXfAd",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.858)
```javascript
{
  "id": -576460752303423415,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:26:11.859)
```javascript
{
  "id": -576460752303423414,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 20:26:11.860)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.864)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqMTL1y32e75iBq6ZXSLt3TX7LDokgd62AbgQbfUaQnhVLu7c4G6w5UCwUVTdmNhji9Hze3pKmaEXn7nSQfhzJNkzUS2Rrm7GZpE4X88V656mQh5jrwiAEUB7rss1XGFB5Jpg8iGB81pejsmsijiCYXVpUdbeC87z"
  }
}
```

#### responder ---> (2018-10-16 20:26:11.865)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak54WdVZ3QGzeETKHJiqqNAtauEWLuDe3mjeHrGkY6NLTe8Yp7PUPvFhmcWiRvUt8J4axnNBFXkBxRwuALoBkhTumj6gcZT8JLPjtS7RdQVZBqp1CrRhVzAkXGnstRNBYiER9uvRu6Uj9HUW89UXk6SLuWKhsR6qrjkLbJ97rZMWPt8SwoqFgeYSCwBuPvAgXPde2WCKSBZJgY8UM95i8ULYstfdyNPEJZMttjxora9B1FATdjQ8cMmKJbLnfe4Y9FR1YeBqQe3gZmU5SHXuTLHxXa8uuPZxiDbnJn5amhQijsiR8"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.869)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.869)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqMTL1y32e75iBq6ZXSLt3TX7LDokgd62AbgQbfUaQnhVLu7c4G6w5UCwUVTdmNhji9Hze3pKmaEXn7nSQfhzJNkzUS2Rrm7GZpE4X88V656mQh5jrwiAEUB7rss1XGFB5Jpg8iGB81pejsmsijiCYXVpUdbeC87z"
  }
}
```

#### initiator ---> (2018-10-16 20:26:11.870)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak53reSrQ2sF1rPA2WzKF3rSWNniowgRwpS1ANbeeVcqehirmRUQHvbtfsjfPW2HcyjkmoiRFseLz2n5CQnVm9BLiGRHG7qUPXLBcstpKco2gSymFwuSfu6dZiN19KotFdw3wTi9NEA7Kp8pCDmAsHXPBF2H7Pidfg5qkKaSFLUfDd1Sahtv5tH5Hkpd9EnkwsHV3UShpk2BmZf4SfKNnhWDf52RaVRkxSoQtYu8oPsE322dUNwVmYNNgPaGUKp34iYBMzEgj8ujgxLD8j5iwyjBiahywXwUrm9Fz6oAmbi7UhArL"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.875)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkqBgvdiPvuXiqF55pf691AnnfR7xt26ds9iQiN3C4RNPpsG5fFro8j5UxZxH3pUCRyjca6Vn1ej5MfwhPPTxAoFgSJgxhtzJ7qnRopw2Mza6YwLwBvDumWQ4JdZrDysWBsc1fd6YZCXsL5RCsyEwbPQcfkfB4mriU7Sd7P887hLmTCYfvZBubQ6zkTX8MqCUQCrd5cVcN2KeineaLY8YfmxKqsT3w6LQfUz1YuSitCAcKhVU1u8zFceY5YjJvwm16aHVFMGDGR46hpSU1URzCi5BHL2YJS3tmR5QiPtBM9cGcLK1VxDH5CFQYpvrVjaHAEiASoWrJyuEeJ61dbAK8ENNYFmyUjEff5ztNCxkKpyYuB1LPzgj2J4mwJVh1TDRPeebnSwio",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.876)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkqBgvdiPvuXiqF55pf691AnnfR7xt26ds9iQiN3C4RNPpsG5fFro8j5UxZxH3pUCRyjca6Vn1ej5MfwhPPTxAoFgSJgxhtzJ7qnRopw2Mza6YwLwBvDumWQ4JdZrDysWBsc1fd6YZCXsL5RCsyEwbPQcfkfB4mriU7Sd7P887hLmTCYfvZBubQ6zkTX8MqCUQCrd5cVcN2KeineaLY8YfmxKqsT3w6LQfUz1YuSitCAcKhVU1u8zFceY5YjJvwm16aHVFMGDGR46hpSU1URzCi5BHL2YJS3tmR5QiPtBM9cGcLK1VxDH5CFQYpvrVjaHAEiASoWrJyuEeJ61dbAK8ENNYFmyUjEff5ztNCxkKpyYuB1LPzgj2J4mwJVh1TDRPeebnSwio",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.880)
```javascript
{
  "id": -576460752303423413,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 400
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 700
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:26:11.881)
```javascript
{
  "id": -576460752303423412,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 700
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 400
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:26:11.882)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.885)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqSsqsWaVqSodwpdgRZ5LUYUwqy4fcLE5tVYNLXErb8WzvwPYEUGqfAcSwwhRnUw1SFTAZzjYqMK8KZZXvBMQvZHeykvsx8ktGJGYhZNjk1p3dPpgBRmfzXoM66RBwPBrGu6WigvdFPUM6CwUmKKsxzoqhQ3vaGJu"
  }
}
```

#### initiator ---> (2018-10-16 20:26:11.886)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak58iWAuTbhgKKsiPhUYZTPcv1W3iEY5U3FyxAjmW39PRySerNyWoAviPtDUydyCLTgzCNrjmHk5gV76gRbEzV3HMq7ZyGbuZCevE1yLV3AKCA1UQjD9TqENE2FhERBh8qFZGbpT4Zo27cftntKET3mHLqYSyU6KrVbMwvjm3etwEzDzhitNJ1yFLKh4yyuJCib2A9hzHFVPCpwoE1V54Mrk84hF1prYHC6A7Dxk5epeZ7Whz7qdDm8k3JSpkfPi9YvAh1WfSWTmBrXjZ5GXpSbMNY8j4Z1LctsiXsRfAFW2t3VJ2"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.920)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.920)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqSsqsWaVqSodwpdgRZ5LUYUwqy4fcLE5tVYNLXErb8WzvwPYEUGqfAcSwwhRnUw1SFTAZzjYqMK8KZZXvBMQvZHeykvsx8ktGJGYhZNjk1p3dPpgBRmfzXoM66RBwPBrGu6WigvdFPUM6CwUmKKsxzoqhQ3vaGJu"
  }
}
```

#### responder ---> (2018-10-16 20:26:11.921)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4mWhBqLWLW5jFJRRAWuztooM8qzXdinuFkoTbcWvvh7fR4zW5NEEpn46PWKBGaTneC4f2D2Di7KJV5YmY7fpbBpMLMPJBAPyLpRvcs9R4mGiSj9GL9JMYnCtNErju4mrqANXrackxTSetzwYqytYbMAu3ro9raDS5PABMf6RTGixehsvgLLAnmkQk297fHE2V8neGCtLm54QokakbjJYBHipuds1LUY989zYSLFr9331dPcQrW6GXDNG5gw5nHLm4sdoXghKDgRjdJLHatvbkyJbfj9CefJwK2AKofcGPMoxR7K"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.927)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkM5zunJmCcQZHMMhPQFW6UfT54LhMfCkaiVoHwhonDFKvb2q9fRZgRZQU2XmMAfh7oRWtYa7E7MkHccZRNarwnnDT7B3UXPdWcxWuWQG2SEDCdgDpQaJG3TnNsi6Zuv5vyUr8gKTPC3eDRErutbaxrsGsjTWbJpfAEMEzg9x21xEpkdSd7DJe4mAUZ7dbrRpTKMx4LmkgE1cTyMKDaaCqQ4Bj679jwiVZqoTfsZkVDuPLeTLrob3btUcRMi5wpi2egt5pp4YiojkXAozJ3trBwsEH3zHwmtZYyPd2VMjsxwT3hEjnoS6FEGSSAWv6Yw5evrj9pv55gckuwW5hrkk9jnZgN4pxckAZ3mxsDkAx53XfseLK6KXijtdWrFreNN62MqrqXuCi",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.928)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkM5zunJmCcQZHMMhPQFW6UfT54LhMfCkaiVoHwhonDFKvb2q9fRZgRZQU2XmMAfh7oRWtYa7E7MkHccZRNarwnnDT7B3UXPdWcxWuWQG2SEDCdgDpQaJG3TnNsi6Zuv5vyUr8gKTPC3eDRErutbaxrsGsjTWbJpfAEMEzg9x21xEpkdSd7DJe4mAUZ7dbrRpTKMx4LmkgE1cTyMKDaaCqQ4Bj679jwiVZqoTfsZkVDuPLeTLrob3btUcRMi5wpi2egt5pp4YiojkXAozJ3trBwsEH3zHwmtZYyPd2VMjsxwT3hEjnoS6FEGSSAWv6Yw5evrj9pv55gckuwW5hrkk9jnZgN4pxckAZ3mxsDkAx53XfseLK6KXijtdWrFreNN62MqrqXuCi",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.933)
```javascript
{
  "id": -576460752303423411,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:26:11.935)
```javascript
{
  "id": -576460752303423410,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 20:26:11.935)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.940)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqYJMj47y2nXZhpAoKg2sc4aaT6wtdztGzhTeScywtHuYKRwqPxqSPMhFfNsDEvsw5RDFeATBY5UQLxwqqBTJAP1cvKkH1tY5vZCZHr3L5FdG229xXNTvXYHHCLn2dykuud9BnAghxtG4YHhrfANnMaVkrJabHHx8"
  }
}
```

#### responder ---> (2018-10-16 20:26:11.941)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4jxwi76KKgkVzwhBHikkrjSUQLsyghtJUnTyecPhvLJQFNXcoZzXcMX6oDoDCDn3ELNLaSLDg4zmsjchsYK46JexpkVQpcYZW9YCRBJJNY4wb3FXNnVgridKcxd7c5QVxrBqP9ak6fFp4QgdVQ7XQWkHWWBK6FDdawidAUoYuYuuYBPQNddYdpVQoaPnKXLgDg741j6bvryd4X9E9JXvvNSNfggLjoeBrHPpufspVS4uJrRP2ez3rsiBF5eE9SpNEKj822skDLgkRqaWE4fK74PcmgNnkDvJ8PXqtq9yfG9sLmn"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.974)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.976)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRw2MZhroq5UZyaHm3cVRp7Wgjhq8WRv5smoxfrE8FdaQqYJMj47y2nXZhpAoKg2sc4aaT6wtdztGzhTeScywtHuYKRwqPxqSPMhFfNsDEvsw5RDFeATBY5UQLxwqqBTJAP1cvKkH1tY5vZCZHr3L5FdG229xXNTvXYHHCLn2dykuud9BnAghxtG4YHhrfANnMaVkrJabHHx8"
  }
}
```

#### initiator ---> (2018-10-16 20:26:11.979)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4peEu4pU4aiegHUwqyk4LXx7GV8qcrpRH7sU41PCzLegCdN81pw5hYQp13mN4oNcxLzyFB3PWFXwyyGfUBcgUr13tzdWb2LVRecauypvGdeHBD6oxmRpQy2fRLQwNShns5vtG8VZuRPGTMMYPJZqXudUp85WsG7CgZwHQJsHTdrSgAGSDvuTFdcS45m3vcivGfzwUTMfLfoSxibcMjF9hzajsu9ZTqYU6Ybc4s3o9rexvWAGW7LaVAAqpzuTZbY8nVgRUaFmYYSouaAosGAg27DZiuLCXZfkaqZDegeFstdNNt2"
  }
}
```

#### initiator <--- (2018-10-16 20:26:11.994)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkJRhpX4q6wXymRJRuTBjKG3RdT3MdqiBx6UojHBJdLDjqhsoKaHundsNyRREetmXxjcWit5NkTnXQBkWY7TXMi4KauZxS1hrX9Yi2bnmBB5zQGNvdBKbVy4okM8AtxXVdjLd9hPs9bX6xDArwfbP6WCskwUD53LYeCo3GaPHmCemTNC54H3AsUQFv695QMwGQjRtMHhAksoAtQapjsuDxL7jN4JASsBjY1sqpe1ZhhBykGsDXDcgC29e6QmNw49PUvBu1ZwQnWXkxtnsLfVL6aLhwp7wAVnjuJ6jo1Q4wdKVjEEHtMgNg81YkbZTrktv87eMk4EyCtckvwhTddif5AWtzvhPnK4zwQCm8W9WYVwuePyhQuoAMdMscvdWvC1Qci8fua5D8",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:11.994)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkJRhpX4q6wXymRJRuTBjKG3RdT3MdqiBx6UojHBJdLDjqhsoKaHundsNyRREetmXxjcWit5NkTnXQBkWY7TXMi4KauZxS1hrX9Yi2bnmBB5zQGNvdBKbVy4okM8AtxXVdjLd9hPs9bX6xDArwfbP6WCskwUD53LYeCo3GaPHmCemTNC54H3AsUQFv695QMwGQjRtMHhAksoAtQapjsuDxL7jN4JASsBjY1sqpe1ZhhBykGsDXDcgC29e6QmNw49PUvBu1ZwQnWXkxtnsLfVL6aLhwp7wAVnjuJ6jo1Q4wdKVjEEHtMgNg81YkbZTrktv87eMk4EyCtckvwhTddif5AWtzvhPnK4zwQCm8W9WYVwuePyhQuoAMdMscvdWvC1Qci8fua5D8",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:12.3)
```javascript
{
  "id": -576460752303423409,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 400
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 700
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:26:12.93)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- (2018-10-16 20:26:12.106)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "tx": "tx_2C9estKT2n5RtT1q94zBzumrq4B4XyHNcQottR641Lt2mqhXGVukCY4EaBYScEACDjJaE9VnjZk3uFsNrJuPuVamuroQcS7Uu3mWX15birHxbxXipL2ZsmtRJaNh8Md2YpnZ8Lu9HVKUVw3EmxFeL8tM1i1987"
  }
}
```

#### initiator ---> (2018-10-16 20:26:12.110)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_2WsEQsiC5Xsno5FgzWT3bH3Dam36VJ7sAqACcWNBEuM7uudS26pfxCgV6rDdvoJxoSrQQNEbxpRZwmiWcXQU8kzirNFKRi9Mp6yteHKGeQdn1pe3NE6tRyF1LRjTBRt9hcaPDUQU7osjhXiXwd3jx6CWiMVo6YxYseNEZT8q4iSiqGLPHj43PHo9Cbw39j8TV6oc92suSzh4WSzoNoVaUZf4m6jM3A4D1qKRr8gfAtLRmi1c8oWD73ZzWGvAQfWeUNR"
  }
}
```

#### responder <--- (2018-10-16 20:26:12.111)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_created",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:12.112)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "tx": "tx_2C9estKT2n5RtT1q94zBzumrq4B4XyHNcQottR641Lt2mqhXGVukCY4EaBYScEACDjJaE9VnjZk3uFsNrJuPuVamuroQcS7Uu3mWX15birHxbxXipL2ZsmtRJaNh8Md2YpnZ8Lu9HVKUVw3EmxFeL8tM1i1987"
  }
}
```

#### responder ---> (2018-10-16 20:26:12.113)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_2WsEQsiC5XsmiSk7UPCUxwCnyocJuBPBPUQQHPQk9fuvAchi8jtWUYC2QrVRtobud8YvoFT3eDX4j231btVSp5GpVv2WZUNiPYzuXU1TxCZDJ4SY4Eoyn7Yi7NguWb9eS1ie8FXbi2nCsVa52aF7rXtSdH7uFG3EbyAdgsaZpkUdv8T3xgQQrw2VpnXaxvWBEG8UrB2Pv6FEbGKjvNMFXJ5xFmXpNWnmAvwMsrkLLtNnPFCBCrHeMSrNmwatRpJsQJ5"
  }
}
```

#### responder <--- (2018-10-16 20:26:12.116)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByF7sWhHTh8cgspmRNQrigJFjaBrz9P4e6dkak7CT5mJmaXgH6BZeixupaRj6i87zew5qY5EUB11x91eSpLoUWSXVTcVrnMdP6nfhyuvfkE9XoGgdiAUyknKkMvC932WAEv7id2g2tBPLefhs5bKwMeKnz6RhBXMjhE6jW2E36DrnncHs43r8zTPd8TwGgXKMr8kuvNWAjX6WYe6B3KnFw3H9YuFjkgPofb4H91uMcWwB9CPdRRQuJkAe1Uz8nnJuVsjyLSmid2jVyVAU1sMKS75aZR9zjJ38UXzVG6UDBAfSQDEvGupic9uAmQbRsAzwn4Xs91mn1wadsBTLCP",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:12.116)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByF7sWhHTh8cgspmRNQrigJFjaBrz9P4e6dkak7CT5mJmaXgH6BZeixupaRj6i87zew5qY5EUB11x91eSpLoUWSXVTcVrnMdP6nfhyuvfkE9XoGgdiAUyknKkMvC932WAEv7id2g2tBPLefhs5bKwMeKnz6RhBXMjhE6jW2E36DrnncHs43r8zTPd8TwGgXKMr8kuvNWAjX6WYe6B3KnFw3H9YuFjkgPofb4H91uMcWwB9CPdRRQuJkAe1Uz8nnJuVsjyLSmid2jVyVAU1sMKS75aZR9zjJ38UXzVG6UDBAfSQDEvGupic9uAmQbRsAzwn4Xs91mn1wadsBTLCP",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:13.732)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:13.733)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:13.733)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:13.733)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:13.736)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByF7sWhHTh8cgspmRNQrigJFjaBrz9P4e6dkak7CT5mJmaXgH6BZeixupaRj6i87zew5qY5EUB11x91eSpLoUWSXVTcVrnMdP6nfhyuvfkE9XoGgdiAUyknKkMvC932WAEv7id2g2tBPLefhs5bKwMeKnz6RhBXMjhE6jW2E36DrnncHs43r8zTPd8TwGgXKMr8kuvNWAjX6WYe6B3KnFw3H9YuFjkgPofb4H91uMcWwB9CPdRRQuJkAe1Uz8nnJuVsjyLSmid2jVyVAU1sMKS75aZR9zjJ38UXzVG6UDBAfSQDEvGupic9uAmQbRsAzwn4Xs91mn1wadsBTLCP",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```

#### responder <--- (2018-10-16 20:26:13.737)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByF7sWhHTh8cgspmRNQrigJFjaBrz9P4e6dkak7CT5mJmaXgH6BZeixupaRj6i87zew5qY5EUB11x91eSpLoUWSXVTcVrnMdP6nfhyuvfkE9XoGgdiAUyknKkMvC932WAEv7id2g2tBPLefhs5bKwMeKnz6RhBXMjhE6jW2E36DrnncHs43r8zTPd8TwGgXKMr8kuvNWAjX6WYe6B3KnFw3H9YuFjkgPofb4H91uMcWwB9CPdRRQuJkAe1Uz8nnJuVsjyLSmid2jVyVAU1sMKS75aZR9zjJ38UXzVG6UDBAfSQDEvGupic9uAmQbRsAzwn4Xs91mn1wadsBTLCP",
    "channel_id": "ch_2HMWHQTfv1t2NPJUkAPVETkNDmC4PqnTx5rgBqe2Ldynq9TvWZ"
  }
}
```
