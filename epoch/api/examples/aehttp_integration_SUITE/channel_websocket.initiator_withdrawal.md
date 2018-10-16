
#### initiator init (2018-10-16 20:06:20.476)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder init (2018-10-16 20:06:20.481)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### responder <--- (2018-10-16 20:06:21.481)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:06:21.483)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:06:21.488)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1KrkHH3a"
  }
}
```

#### initiator ---> (2018-10-16 20:06:21.510)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmpuTxkiBqJd1WyhHCggbNTSk16yEcNGcnTLYNMroQGXcuu9EFeWoEkVmNNWRk4tEdpyY2gDbfi5yJ9gUb4s2T4kZcq6NzbnJTAx8nM4qTyXAd9HT27geyo7krdCsJx51Rvwq7wM3ure97YKWtYJQ6dUWZzdwEYgw5Ec1WEPdWsWChHDB5DCedheFMLYwPHLAbte49z14SK8M7KUTC9vuTNxngiUKiZigsMnyZkjc9KFabGUoiet3xWaoA8tbvPRw"
  }
}
```

#### responder <--- (2018-10-16 20:06:21.511)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:06:21.512)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1KrkHH3a"
  }
}
```

#### responder ---> (2018-10-16 20:06:21.513)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkKAQUC5v4Pi4tERoT4NN1E6DqR3Hvhb3E66ACWWft2hpo4sxhCNeivs2nv3Pf5vU5nLrTVKmsNM8XaLgi8GpB5rnMjGA1xug6nPMNwgM5ZhgXk81geAPUvvA2DVQv7Tfz4JWapEUw9embufRycFVPDc3jrVnBRhRzSKr5LUKdMTYUEnuFTvj3U4M45yK5tW77QTaTvMkA2b25hmDEGxTHsfM9tVMgUPHTFuo6tyi5K7PeatHRr6sjs9WocwKfHVa"
  }
}
```

#### initiator <--- (2018-10-16 20:06:21.514)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:06:21.515)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNkDuND4m1UsQugVJArTEm8UeExY4pTfSjxkpm33QVd8v8TpyTyMjeaMDTUk48MaQNjL3DG1VWeqQQozUug5me1iBmxapkzRJPxtfr5AjPpSTegDx4tWomLyP1ecZnvjkXNUsDwmkRRUk267AY5ShLQVKatqjGrGLKgaNCzZCB2tVM7SPHbVdTReCm7ThPbkb29mht3AfL5rZPJnNov9ejGsTNy2j1TZzZ62wJLT98GZPUou3N8Pij4XbETSgnUXye244YuGpT3J597eSx2amt9AsyWzAaXbjTsHUztVLzKuQGSPMLPHQCUjALwmT5Nhv7RzUCjgpUHigG2Fqr6Ut2q53Fb"
  }
}
```

#### initiator <--- (2018-10-16 20:06:21.527)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNkDuND4m1UsQugVJArTEm8UeExY4pTfSjxkpm33QVd8v8TpyTyMjeaMDTUk48MaQNjL3DG1VWeqQQozUug5me1iBmxapkzRJPxtfr5AjPpSTegDx4tWomLyP1ecZnvjkXNUsDwmkRRUk267AY5ShLQVKatqjGrGLKgaNCzZCB2tVM7SPHbVdTReCm7ThPbkb29mht3AfL5rZPJnNov9ejGsTNy2j1TZzZ62wJLT98GZPUou3N8Pij4XbETSgnUXye244YuGpT3J597eSx2amt9AsyWzAaXbjTsHUztVLzKuQGSPMLPHQCUjALwmT5Nhv7RzUCjgpUHigG2Fqr6Ut2q53Fb"
  }
}
```

#### initiator <--- (2018-10-16 20:06:23.290)
```javascript
{
  "id": -576460752303423419,
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

#### initiator <--- (2018-10-16 20:06:24.404)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.405)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.405)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.406)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.411)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.413)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNkDuND4m1UsQugVJArTEm8UeExY4pTfSjxkpm33QVd8v8TpyTyMjeaMDTUk48MaQNjL3DG1VWeqQQozUug5me1iBmxapkzRJPxtfr5AjPpSTegDx4tWomLyP1ecZnvjkXNUsDwmkRRUk267AY5ShLQVKatqjGrGLKgaNCzZCB2tVM7SPHbVdTReCm7ThPbkb29mht3AfL5rZPJnNov9ejGsTNy2j1TZzZ62wJLT98GZPUou3N8Pij4XbETSgnUXye244YuGpT3J597eSx2amt9AsyWzAaXbjTsHUztVLzKuQGSPMLPHQCUjALwmT5Nhv7RzUCjgpUHigG2Fqr6Ut2q53Fb",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.413)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.415)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNkDuND4m1UsQugVJArTEm8UeExY4pTfSjxkpm33QVd8v8TpyTyMjeaMDTUk48MaQNjL3DG1VWeqQQozUug5me1iBmxapkzRJPxtfr5AjPpSTegDx4tWomLyP1ecZnvjkXNUsDwmkRRUk267AY5ShLQVKatqjGrGLKgaNCzZCB2tVM7SPHbVdTReCm7ThPbkb29mht3AfL5rZPJnNov9ejGsTNy2j1TZzZ62wJLT98GZPUou3N8Pij4XbETSgnUXye244YuGpT3J597eSx2amt9AsyWzAaXbjTsHUztVLzKuQGSPMLPHQCUjALwmT5Nhv7RzUCjgpUHigG2Fqr6Ut2q53Fb",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

##### initiator: (2018-10-16 20:06:24.457)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 20:06:24.457)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 20:06:24.457)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 20:06:24.457)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 20:06:24.457)
> Channel is `open` and ready to use

##### responder: (2018-10-16 20:06:24.457)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:06:24.506)
```javascript
{
  "id": -576460752303423418,
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

#### initiator ---> (2018-10-16 20:06:24.507)
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

#### initiator <--- (2018-10-16 20:06:24.514)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7B7obWg6eTLrMBHvUjJqez7XuYvrwYFBorE7eWZDsbtNu5nhBQoLsaRhzo2dLxREzAcf5hGWj2BhtHo2F6DgBSVjPAGqF6CHQgtSF6AGbS4ryL7i2nFh8iGQHUVeJMb6WrsUi1E8QNDSkMWUSHje83igny3RsRok"
  }
}
```

#### initiator ---> (2018-10-16 20:06:24.515)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5ALy5wiN3UPnHqtEqx9KP7ykadchMrrgRtNAFaWPQkMcG1khPu3S5KMGaLGjBx3FwD4hJMXLmsrUAEnQjYywdtHkEwjwo9i5uXF9GabmiRgUVXaiQV1yvHSNZ1VJ6G1Bi7sDPVQaKZ1m3cDAk8mzeXQnbhUVdq8vwjsd4g1prpVukW129ZbZUvDUiqEQwBBKnLb9qUWbd1cyjUkvwP734iJFYzUAE2Gc5ex1bEkda1L29QJC5GeCkCqXyXKhagGTFtcxEAz8iqqiKE926d6x9ynfYxBFJcwgHgFLZNn5qbUPj9n"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.521)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.521)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7B7obWg6eTLrMBHvUjJqez7XuYvrwYFBorE7eWZDsbtNu5nhBQoLsaRhzo2dLxREzAcf5hGWj2BhtHo2F6DgBSVjPAGqF6CHQgtSF6AGbS4ryL7i2nFh8iGQHUVeJMb6WrsUi1E8QNDSkMWUSHje83igny3RsRok"
  }
}
```

#### responder ---> (2018-10-16 20:06:24.522)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5BJks5uXXTBs22drPE85EMGHbhh5uaMuMm9nTntq99n3pu719cGMcTYw1DGEb16brWozE42zU9X66t1ZEBHY2ywgCxE7XjZsfcUb4vjng9iMTiiHo2AApmGJACN5YBU7CuSeaaoS3F9NbZCJMPH8o67hfmNJDxAtA77csj98gEtKJq9LQHW7281Fzpqb2rD1HyYWiaVP3fb1yNG5LcH44RSMPQoaTwN7APaN8nt4WVVcTzFgEYWy3yGXwznGEfadoD26g47JM7xsqw8a1NTRmmaKkPQwUUUuKL8AFP7tea5JHsN"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.527)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDm2LeanENFTARY6n1VWYTpHrAAaE8VSh5h5jRL8KNhBbEVVA57s94yaeqxre9ewTfBWv88w3PBfrDP8ja3dampJE2rzcdk54yW1ohPv8Gj8gTar5JQgRpTMBKTk9yPV3Z7Z2YEBLPKxsraf1d2TMdhh4RtkiDbrnerpPDfX8nFnfL26JviK44p9wYukwwahvYAkCvvdzkneopmtrQgLSBFwqTW5iPpoZidRHEY2p6onoyz9L9bQoZ8ZHsmuPhvEZzXXsbsJii8jeSwExhBhBabrKKYZsJeb6C3TcWbk5NShz82DAczJjcxWJubsxFcpxfNeDCk4kEHgjYdCaL21RNcteaZWh2qXDaLUFS66g5PmoSkC32eZmLXtTZ9QNbWQzGUCU8eZ1Hm",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.528)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDm2LeanENFTARY6n1VWYTpHrAAaE8VSh5h5jRL8KNhBbEVVA57s94yaeqxre9ewTfBWv88w3PBfrDP8ja3dampJE2rzcdk54yW1ohPv8Gj8gTar5JQgRpTMBKTk9yPV3Z7Z2YEBLPKxsraf1d2TMdhh4RtkiDbrnerpPDfX8nFnfL26JviK44p9wYukwwahvYAkCvvdzkneopmtrQgLSBFwqTW5iPpoZidRHEY2p6onoyz9L9bQoZ8ZHsmuPhvEZzXXsbsJii8jeSwExhBhBabrKKYZsJeb6C3TcWbk5NShz82DAczJjcxWJubsxFcpxfNeDCk4kEHgjYdCaL21RNcteaZWh2qXDaLUFS66g5PmoSkC32eZmLXtTZ9QNbWQzGUCU8eZ1Hm",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.532)
```javascript
{
  "id": -576460752303423417,
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

#### initiator <--- (2018-10-16 20:06:24.533)
```javascript
{
  "id": -576460752303423416,
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

#### responder ---> (2018-10-16 20:06:24.533)
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

#### responder <--- (2018-10-16 20:06:24.538)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7GYKT4DZqo4n7Aq3NrdYcjUmiXJhehbh17YbxZ3YdbaVJgbMFppz7Y7h7q7Q5uy7ag1URAFhi7h8XnQq9L19tVqbLYaQ77PCysxK5yM1yMVBBmWpsWa4LqLh422dF8gsraqyuqw6zcdQXVFK6XvHT4QX7Lp11WbC"
  }
}
```

#### responder ---> (2018-10-16 20:06:24.540)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5768v2Mu8tMVA2q4wARa8bZsNzbmpQD7RjgehVgRfRXVxegy3kgegapEEkCZvKNdGg8GS3KUBzwGPEAqRRmR4QLdJMYCbH731Ar4TRhPB6kuTKC2uh7sAdkXS6MPxUYDbUFwVnwLEv3EM9yRG2AthdTSc8HyF4ua62mjKRsBShf8LoEE6QCYEpBBk5UnEFbRgcvQigaa1wnLuDEGy8fBdxWLcx6o5uER16NJFEg1ahosUpn84sdHHux2r9k7jBxsqAdQAipieutdntFss1guy7gPYMuqUvpEpm2iWmnFfgiuo2r"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.544)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.545)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7GYKT4DZqo4n7Aq3NrdYcjUmiXJhehbh17YbxZ3YdbaVJgbMFppz7Y7h7q7Q5uy7ag1URAFhi7h8XnQq9L19tVqbLYaQ77PCysxK5yM1yMVBBmWpsWa4LqLh422dF8gsraqyuqw6zcdQXVFK6XvHT4QX7Lp11WbC"
  }
}
```

#### initiator ---> (2018-10-16 20:06:24.545)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5Aa9XaE3VWVRZshQTSXCuFA8qhjLhr3mLduFaGAxYHp9w7DtgkVJ2RiMXh5mNf4mLJ6gZoaexzEZyZQ8g5md6ecBn9QoUHTbCUE5VSJf8n8SFS6HMB6u8vvq3mAzhwD9krdEnpdhAWUPbnMnaXz87Voq8Dym8XXbqZ3KkreCKDGsL23kPZGp4z9qq9rsphtcn7zSb1EhXCLAj4MXoi84GodbmHrNcz9tfq56VaynuL6CkXEFzybsAFfmESPma1kjSx6NkxSH2aLLUnwryRGgbX5rZtPo6oRhmtvwqgxspwVhwUm"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.550)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkvk1xn8asJAr984CCZPJ8EVbndfnWqZxPMGX3WxgZQRzZ8xDLFarqrurTjCBqht2NwsUu49g7LM1WUZtJAvvZJfU9H1SVtdQSbucQSEVXwYZPLqUAgDMNJ8wHeoqR1FFvV1yETwA6uvJL11NbcnTFs911QiK3X5mWrbYjsNBXJq1BGqp6JegMCyk71UyC619jrw5oo5rFfa1MkPGdfPXG2ooymFunj1rPR1bjPtsJVFRaDcsjZBCLQGDiAevk9DybQjrJvTLp9iZB2AKoX2GY3Z35R3Gq5CqcCcyNYkmMBgj9yD9f5bspPtAjrdZPQ1r3TE5E3PPajDieiB8BQYFrApj3bAx2LmPmHyBKJvRkVdanLvgH1xvA3xDzKkaeiKUWhbbRjxZu",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.551)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkvk1xn8asJAr984CCZPJ8EVbndfnWqZxPMGX3WxgZQRzZ8xDLFarqrurTjCBqht2NwsUu49g7LM1WUZtJAvvZJfU9H1SVtdQSbucQSEVXwYZPLqUAgDMNJ8wHeoqR1FFvV1yETwA6uvJL11NbcnTFs911QiK3X5mWrbYjsNBXJq1BGqp6JegMCyk71UyC619jrw5oo5rFfa1MkPGdfPXG2ooymFunj1rPR1bjPtsJVFRaDcsjZBCLQGDiAevk9DybQjrJvTLp9iZB2AKoX2GY3Z35R3Gq5CqcCcyNYkmMBgj9yD9f5bspPtAjrdZPQ1r3TE5E3PPajDieiB8BQYFrApj3bAx2LmPmHyBKJvRkVdanLvgH1xvA3xDzKkaeiKUWhbbRjxZu",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.555)
```javascript
{
  "id": -576460752303423415,
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

#### initiator <--- (2018-10-16 20:06:24.557)
```javascript
{
  "id": -576460752303423414,
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

#### responder ---> (2018-10-16 20:06:24.557)
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

#### responder <--- (2018-10-16 20:06:24.560)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7MxqJbm338nhsANAGyUYQ31WGxsmdPVpRASDt2oENMBWnx1TvgCEmUrrDGpBph4DGJy6vDa8bNK4pCzXrasopVxuZVSKgg6cfFSZULJSTwkRVS5eJwhLUx7yE9u5kDkZN5BULMACpravo39U9tv1EHCTFGDvh1Tm"
  }
}
```

#### responder ---> (2018-10-16 20:06:24.561)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4tJoL4651BH7Y2UgW5eMFBU2nXajihusNLczHHkXA99ykdmZsxo2ASjUBUgX9QcQDWxoMHEBPsbGJvYrEx5JECMucz6KA8cDFeLMYJ2wzgm55HWDLHEX3xMn35ZwbaPUhR2B8A9RVQX9THw9smofX85XgMbS4hCBqsGq4eUjPFdUYxJxkNcQBvfr6hN9hmacDQaDUB3JKEfkCsHgDWU55Ety9hXbXN5CuwFy5eUjSrycSQZYq3WWg9qCM8q4yTMwnCqZpePJ2aui69iWm7i8dCAFRJ5kLaZSz1au3r44QD2yFxw"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.565)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.565)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7MxqJbm338nhsANAGyUYQ31WGxsmdPVpRASDt2oENMBWnx1TvgCEmUrrDGpBph4DGJy6vDa8bNK4pCzXrasopVxuZVSKgg6cfFSZULJSTwkRVS5eJwhLUx7yE9u5kDkZN5BULMACpravo39U9tv1EHCTFGDvh1Tm"
  }
}
```

#### initiator ---> (2018-10-16 20:06:24.566)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak56obGcdMuLtFmakhM7t99Z3MhG8NYzpMWmgWUEzqCgfVG2FiYodPyeT1V2sXxzDBTonRtWbfsb69JRsEDVXcHF4B6nfWira8AAeFX4yXXP5UCfZaSQbeu6EGHRhjPwxSAq9PpzPdaDBpQue6K5W4DYdRJtKepbfEQnW6Ci1RvoUPjkftEbHjFs4iWPT3ugbkDD7jdsHjz37FkQjyam7qwb1Vw178SA44zWET1gSGDW3MyXFpkXYhMrcTryEJi2cnR93og4bKDEn4t83hkDUWtKvZs88zws4igkbCmbzi6qgyaRe"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.570)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkYmXtoic2n7VTWriJDAU4GjEZekS3nNnD3rtVMgxMd9P8VSJVDj9hqkjKpoBBwLiBHeWKNKhu7E7eC65z7jb4W7YAHQmH8tGVpkHw61RemchZX5UTCtbYz5Tq6wYzHjGTiztsfmHEYtoQkSVJsNUpHJrhzhAxUD7LY7zti7Z3274WwxYPffcCjBXycSnHcrASss86ZVLYXqfEJd3zzm9YBxeokYikX3PdsLFHSL53viiJbCpasFvt91ECxJ9FV3AcqoHgx2NSLU2fr9quMS4vzpfPPb3r7fmWW2GRACh1vLQDowM5TsS5mP9JY579WU4zjTzoWVLS5f1dtQdMogSkM2W3ZwrtM4EYRCHuzz9SRfnXbEMo1UNNLNUHWe89BLZtoK9DV9gw",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.571)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkYmXtoic2n7VTWriJDAU4GjEZekS3nNnD3rtVMgxMd9P8VSJVDj9hqkjKpoBBwLiBHeWKNKhu7E7eC65z7jb4W7YAHQmH8tGVpkHw61RemchZX5UTCtbYz5Tq6wYzHjGTiztsfmHEYtoQkSVJsNUpHJrhzhAxUD7LY7zti7Z3274WwxYPffcCjBXycSnHcrASss86ZVLYXqfEJd3zzm9YBxeokYikX3PdsLFHSL53viiJbCpasFvt91ECxJ9FV3AcqoHgx2NSLU2fr9quMS4vzpfPPb3r7fmWW2GRACh1vLQDowM5TsS5mP9JY579WU4zjTzoWVLS5f1dtQdMogSkM2W3ZwrtM4EYRCHuzz9SRfnXbEMo1UNNLNUHWe89BLZtoK9DV9gw",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.575)
```javascript
{
  "id": -576460752303423413,
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

#### initiator <--- (2018-10-16 20:06:24.576)
```javascript
{
  "id": -576460752303423412,
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

#### initiator ---> (2018-10-16 20:06:24.577)
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

#### initiator <--- (2018-10-16 20:06:24.580)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7TPMA9JWEUWdd9uHB5qpzthjase4sbwa3ztyQwpH5rhTMt33Bxu6qQfBH88zZHgY35VYasDoNn3WjZY8NrqdySsg3zrbynLWSoMBQB2Y5CrbtKisuqMpBfaMwRaXfiYgMufdNGUqn2AMqAMPbwoVoi4xmgpeqiHu"
  }
}
```

#### initiator ---> (2018-10-16 20:06:24.580)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4up8bPHPP74Mzvrr6TQHAcingau6g5gox5qWTB3mNVWJeRt6guubEWX8WV6amg7SWCKeFZZczYSsqAUtfjvF7VQDJjrMHotyNAV9uQcg4y7fRHs6Q4NGSNyWvJJJqo84VZMGZEyxwbKZW3LdLEkHVrzrmKVL61QLSpngN4mt7PHkb7rXY83AE74DKGczpyezHPtyv1y8ZhwKbRCnJGqV4jHAcYpYoKi6VnwxrtmdsH6aQ9neqz3ErWMjEiX9dvuRSny1Y2HTX29inHbZ6giVESrpihGdLvy7SH4mDMzZwKfeYLE"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.611)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.611)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7TPMA9JWEUWdd9uHB5qpzthjase4sbwa3ztyQwpH5rhTMt33Bxu6qQfBH88zZHgY35VYasDoNn3WjZY8NrqdySsg3zrbynLWSoMBQB2Y5CrbtKisuqMpBfaMwRaXfiYgMufdNGUqn2AMqAMPbwoVoi4xmgpeqiHu"
  }
}
```

#### responder ---> (2018-10-16 20:06:24.612)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4pnDKDAASMNB6WqA7RL9oKWt4cbDdY9mVxL8TBVWHvrnnH5WgiYgZBh4ejYGbGfjQwj493RAV6k2gyY9mmt5LdLhoQ5QdLGaMb7yCZ145eJyi74MH2YmPpmuQS8xoaYpBgqsa9ueHpvNR25TKMyYiZAjAEn3UeU4HhzjnUQXrvoHzHXqh2d6QqceEZUSUWR3F8cMuFmGQgeJDq36v71GWGufovEFwAvUgV8FSxLCLwT5vKXFhdAvuPU1MvMgSBtkiqFk4iwj1kkViLMHyzR6UF7eBwPrXCF8ZGSnsxykvByzwNb"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.616)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkShpDt1LdzdBhtuvzCJS4VvapgpHYotw3NdzNaF7hw45WrLq6TREvsHyURuappiVMfKvaKPToJGvFK9jHpmd7Vd6uPN15NoG3wLbi7cPtgX4kHSCeLXNQK4wPDn8BSKFLf8z3tYQi8gXNmLuPMrFxY68NS942J23aB6Gvi5yxeENSDTKzYnoUvM5EtDpTQTwwhVRfu33GDBBhdSdaGwUnGgvA8S5krgUuCTYEXNYyF7eaMANybMCzk8234xcV6LKjdKaFqsbnQqF9WFXBjBDuXDRhJQv8aNjDEAmiD7KqqJeSyACGNqesKq82BvD7yRFbfJPudmpnyDre4jsQr3aM6Bq3U7X6btBYfV8LFckHE8jNFujuEsv7FMbn4eHtr1MigBLE1RbY",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.617)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkShpDt1LdzdBhtuvzCJS4VvapgpHYotw3NdzNaF7hw45WrLq6TREvsHyURuappiVMfKvaKPToJGvFK9jHpmd7Vd6uPN15NoG3wLbi7cPtgX4kHSCeLXNQK4wPDn8BSKFLf8z3tYQi8gXNmLuPMrFxY68NS942J23aB6Gvi5yxeENSDTKzYnoUvM5EtDpTQTwwhVRfu33GDBBhdSdaGwUnGgvA8S5krgUuCTYEXNYyF7eaMANybMCzk8234xcV6LKjdKaFqsbnQqF9WFXBjBDuXDRhJQv8aNjDEAmiD7KqqJeSyACGNqesKq82BvD7yRFbfJPudmpnyDre4jsQr3aM6Bq3U7X6btBYfV8LFckHE8jNFujuEsv7FMbn4eHtr1MigBLE1RbY",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.621)
```javascript
{
  "id": -576460752303423411,
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

#### initiator <--- (2018-10-16 20:06:24.622)
```javascript
{
  "id": -576460752303423410,
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

#### responder ---> (2018-10-16 20:06:24.623)
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

#### responder <--- (2018-10-16 20:06:24.626)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7Yos1gqyRpEZP9SQ5DAXxe4yPr1uamJ5FGDTizJbqrPZmUqhGNvk5NMAQADmJFEQdatMvLCzMsYwP49wH6d7gWDY1PAAqoXS1zR4F4DHT8Gv6m9ryNT6n2E8Zcp6rwGJCPVyyoajfj2LbT5T6Kab3LCPcw4Twu3J"
  }
}
```

#### responder ---> (2018-10-16 20:06:24.626)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4qzv1waiw4CvcLnqLZurZw1Ewv6wzDMitBURZ7pFCjxGB457uHbd3vbFE5uEXnjFPA7XCTocmUv1BibA8JBicNf5L9SbEH7JJtR2czjStJJXCJ9k9YFBKduP9gH2iFK1nx3L17uvASAnyJx3QHZ98dJeWZoiu9CMgdUhEca47cxB4CeYhCCBhKrsi29zDy1cjRorrViq2sV7WozdwbkQZXHuxsZ6wE3Fwzz8feyS6bjirEH7j864ooRZGe7kNG7qDNMQWwxcjv2U9NMhtmyP7s68K21WWxxBc316zd7LXtZwoFL"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.666)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.668)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQXsQhbrY8BuRQBdV28pfQfZFZJL5Nr5M8bypbuys7hkP7Yos1gqyRpEZP9SQ5DAXxe4yPr1uamJ5FGDTizJbqrPZmUqhGNvk5NMAQADmJFEQdatMvLCzMsYwP49wH6d7gWDY1PAAqoXS1zR4F4DHT8Gv6m9ryNT6n2E8Zcp6rwGJCPVyyoajfj2LbT5T6Kab3LCPcw4Twu3J"
  }
}
```

#### initiator ---> (2018-10-16 20:06:24.671)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4vHuHGtV4Her9jD7rj5NQwmjrxHTnnMnTCHQ73CJ2XTmpS5FjpDx7WQiqYAkZ5mQm68oWcTKsRYBoKgiTshF9c8aRDdkWgWVNikkk4ka6VeVVmN7whhPQiz62quD1dcVpDRKn7pZrwBDar9FdwSQodKM1zco5C1WjdFNxpM9DQhWqyRynhNK9FEdarEX2iA2LQ1qHCpYbGpi1w5PqQq6ZevgmRjF1Hb8Z2WZxP7jmx4jakSPRsszzqqGiGkbpv8GkpUh7yD8cST7YxYpwYydNeNzmirrnAcTGCohQN6yQkM5BdS"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.685)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkUoN22ZKuD9joEXUhPhMuPN69nrHnzmQqc7EWdbsUdCd4QSuMuys4kLuhbt8tjdcrC73ow26WnH8fhzr2JZmruDA8bbcQ5G8FQXnKwpiXZMJMdUy2ZGXDvZwffHByoN7XVZEuzUJZQatxqCcRcjgeJV7grkC1wHWvWzycbcVSDrnQo1PM6rRDqL5PPB9CsJaiCWGZy2nV6ZsAdQafUFExnD59FNfhTXczG8zz9FvVUPCetXkb6qnv54zJ6DfGm32ViYatnLVYE2Pv2oA17yAT3BQ713t1cjmCr4ZCHz4H7LBkHsoa9Y5VeJVGZS6JFDCQkkKTBePK66WgxuYzxJPSGARKR15aRmXSbHDR68EpapTcbzqo6gXMCNh6hh2d8cio5FDp8knf",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.687)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkUoN22ZKuD9joEXUhPhMuPN69nrHnzmQqc7EWdbsUdCd4QSuMuys4kLuhbt8tjdcrC73ow26WnH8fhzr2JZmruDA8bbcQ5G8FQXnKwpiXZMJMdUy2ZGXDvZwffHByoN7XVZEuzUJZQatxqCcRcjgeJV7grkC1wHWvWzycbcVSDrnQo1PM6rRDqL5PPB9CsJaiCWGZy2nV6ZsAdQafUFExnD59FNfhTXczG8zz9FvVUPCetXkb6qnv54zJ6DfGm32ViYatnLVYE2Pv2oA17yAT3BQ713t1cjmCr4ZCHz4H7LBkHsoa9Y5VeJVGZS6JFDCQkkKTBePK66WgxuYzxJPSGARKR15aRmXSbHDR68EpapTcbzqo6gXMCNh6hh2d8cio5FDp8knf",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.695)
```javascript
{
  "id": -576460752303423409,
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

#### initiator ---> (2018-10-16 20:06:24.755)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.763)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "tx": "tx_2C9estKT2fhPPdsuQ2xos58hYNqBiuHxFMv1zKyTZBPxqneiahVNpfxMYW7mQLQJL9nd7karTFqzL54WTiWJ5y68ioMjdaYrYTPYFExV9hUg6docd5RENxKgE2RGaQk3EURhfDfGX7xa8REfnS26ni67DcRZ9t"
  }
}
```

#### initiator ---> (2018-10-16 20:06:24.767)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_2WsEQsiC5XsmwaBE37PHeoJRJDQnv6rkEGH1NJ2udfcPkqRWb1BjhKZMb7efSF8g7j63HLxnADFoMEuu8pFGYgZNp4DdvxTTe7T73q4Ca7MbNdFpmGh9Nswmd5yZWkGQivTtcbfDMWJt7CTGudipgiKkTYrqcHYZoaiL7q1UE17SYGzjSDoHwCZCbNH7cA42J4V3GfVnmy1JXULQhcUmcGA4Vfk4wcHta4uZPtXv1G3jKwM5mks3kQp16VM7b6xdqBx"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.768)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_created",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.769)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "tx": "tx_2C9estKT2fhPPdsuQ2xos58hYNqBiuHxFMv1zKyTZBPxqneiahVNpfxMYW7mQLQJL9nd7karTFqzL54WTiWJ5y68ioMjdaYrYTPYFExV9hUg6docd5RENxKgE2RGaQk3EURhfDfGX7xa8REfnS26ni67DcRZ9t"
  }
}
```

#### responder ---> (2018-10-16 20:06:24.769)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_2WsEQsiC5Xsn4eFK7R9befxeMWh1t9eYpxzfS7EJZDqZ7nkSkzNLAd3Hw7q6BkV113nFgTWTigoK2BvpEYkSXC2kZirKPpjvvVpVhtkGgvojGDha1aRGptpfZNbyRANKcYGT3hW1g4TExFiLo3jx3zbcnsUUt3HhaJQx3viyni8heEDNXAUehw7YCyEpbyV8XyvxmCgHxBRfvJjKSBH4feURxpbUncPSjTu55tSqXMhM25Z91ikbd4zdjJ6YXmBCkyB"
  }
}
```

#### responder <--- (2018-10-16 20:06:24.771)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBydguKSNsTY14E7TuuTKv7EfpT8ud32MdVsy1zxaZ23AXrEvEeXm6VinMzSEWHjq4scaWARYjczH2tx36K6NdMocmq4kNzZzpgvfyyaBUHqii6G6yUArsdQ7HFBRsirsKh5F7zwEGJBLG1vJJttKi4SmMFXdZ6Ys9jrjJLSYNX8SD69L6quBEvG7ESGb5G6v2t8vUeS7joM1Hf3u55aBvTAvrTgMcNEheLVR9AyxFeCjf4e8Hi5BGdFUhicf9ijytAzN9MWSprBQYr4a6oDmKhVfEmGNMybKoWfhUU6JHA6QbUMY2tT6L74n7sdfJVPrDjWCjB9cCnGxiR5zddu",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:24.772)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBydguKSNsTY14E7TuuTKv7EfpT8ud32MdVsy1zxaZ23AXrEvEeXm6VinMzSEWHjq4scaWARYjczH2tx36K6NdMocmq4kNzZzpgvfyyaBUHqii6G6yUArsdQ7HFBRsirsKh5F7zwEGJBLG1vJJttKi4SmMFXdZ6Ys9jrjJLSYNX8SD69L6quBEvG7ESGb5G6v2t8vUeS7joM1Hf3u55aBvTAvrTgMcNEheLVR9AyxFeCjf4e8Hi5BGdFUhicf9ijytAzN9MWSprBQYr4a6oDmKhVfEmGNMybKoWfhUU6JHA6QbUMY2tT6L74n7sdfJVPrDjWCjB9cCnGxiR5zddu",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:26.9)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:26.10)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:26.10)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:26.11)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### initiator <--- (2018-10-16 20:06:26.14)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBydguKSNsTY14E7TuuTKv7EfpT8ud32MdVsy1zxaZ23AXrEvEeXm6VinMzSEWHjq4scaWARYjczH2tx36K6NdMocmq4kNzZzpgvfyyaBUHqii6G6yUArsdQ7HFBRsirsKh5F7zwEGJBLG1vJJttKi4SmMFXdZ6Ys9jrjJLSYNX8SD69L6quBEvG7ESGb5G6v2t8vUeS7joM1Hf3u55aBvTAvrTgMcNEheLVR9AyxFeCjf4e8Hi5BGdFUhicf9ijytAzN9MWSprBQYr4a6oDmKhVfEmGNMybKoWfhUU6JHA6QbUMY2tT6L74n7sdfJVPrDjWCjB9cCnGxiR5zddu",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```

#### responder <--- (2018-10-16 20:06:26.14)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBydguKSNsTY14E7TuuTKv7EfpT8ud32MdVsy1zxaZ23AXrEvEeXm6VinMzSEWHjq4scaWARYjczH2tx36K6NdMocmq4kNzZzpgvfyyaBUHqii6G6yUArsdQ7HFBRsirsKh5F7zwEGJBLG1vJJttKi4SmMFXdZ6Ys9jrjJLSYNX8SD69L6quBEvG7ESGb5G6v2t8vUeS7joM1Hf3u55aBvTAvrTgMcNEheLVR9AyxFeCjf4e8Hi5BGdFUhicf9ijytAzN9MWSprBQYr4a6oDmKhVfEmGNMybKoWfhUU6JHA6QbUMY2tT6L74n7sdfJVPrDjWCjB9cCnGxiR5zddu",
    "channel_id": "ch_uAdv6WGhzuHiZsLj2SB5NvUbRWAp1tkWBb1fPVcxZRxecT6ze"
  }
}
```
