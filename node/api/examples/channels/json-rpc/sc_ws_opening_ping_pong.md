
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_61Hfn0RdxDq+ebMce/X/9E8q3tnPol9r1qRUP3Krou7qYRo5"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_ktuhEDXyVYsX5H1SSJwAUDEvtwpnL2+3Q1M8GuZW0vWa0kZ7"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### initiator info
> Received an WebSocket connection accepted

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYF1at+KA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423396,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEC9oAoX1ti0Tq7zEHcWVTzqZkMj5+3e2mDFi08wxPLYk8Ww/evmOEFsFIy11X+q3UaEZqpzA1NNe4OmLO/RgTUFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGBRRXnx8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423396,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_ktuhEDXyVYsX5H1SSJwAUDEvtwpnL2+3Q1M8GuZW0vWa0kZ7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEC9oAoX1ti0Tq7zEHcWVTzqZkMj5+3e2mDFi08wxPLYk8Ww/evmOEFsFIy11X+q3UaEZqpzA1NNe4OmLO/RgTUFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGBRRXnx8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423395,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAvaAKF9bYtE6u8xB3FlU86mZDI+ft3tpgxYtPMMTy2JPFsP3r5jhBbBSMtdV/qt1GhGaqcwNTTXuDpizv0YE1BbhA6/ECjOGKmTlrapSNLI1xiNrCGjFXaoZjGFuTogrj405zXCZSenE0PSoYAkV5Rp0G9Sp/1EBQjxRkRhKPZCvBBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgUrbmeH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
  "id": -576460752303423395,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAvaAKF9bYtE6u8xB3FlU86mZDI+ft3tpgxYtPMMTy2JPFsP3r5jhBbBSMtdV/qt1GhGaqcwNTTXuDpizv0YE1BbhA6/ECjOGKmTlrapSNLI1xiNrCGjFXaoZjGFuTogrj405zXCZSenE0PSoYAkV5Rp0G9Sp/1EBQjxRkRhKPZCvBBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgUrbmeH",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_61Hfn0RdxDq+ebMce/X/9E8q3tnPol9r1qRUP3Krou7qYRo5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAvaAKF9bYtE6u8xB3FlU86mZDI+ft3tpgxYtPMMTy2JPFsP3r5jhBbBSMtdV/qt1GhGaqcwNTTXuDpizv0YE1BbhA6/ECjOGKmTlrapSNLI1xiNrCGjFXaoZjGFuTogrj405zXCZSenE0PSoYAkV5Rp0G9Sp/1EBQjxRkRhKPZCvBBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgUrbmeH",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAvaAKF9bYtE6u8xB3FlU86mZDI+ft3tpgxYtPMMTy2JPFsP3r5jhBbBSMtdV/qt1GhGaqcwNTTXuDpizv0YE1BbhA6/ECjOGKmTlrapSNLI1xiNrCGjFXaoZjGFuTogrj405zXCZSenE0PSoYAkV5Rp0G9Sp/1EBQjxRkRhKPZCvBBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgUrbmeH",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAvaAKF9bYtE6u8xB3FlU86mZDI+ft3tpgxYtPMMTy2JPFsP3r5jhBbBSMtdV/qt1GhGaqcwNTTXuDpizv0YE1BbhA6/ECjOGKmTlrapSNLI1xiNrCGjFXaoZjGFuTogrj405zXCZSenE0PSoYAkV5Rp0G9Sp/1EBQjxRkRhKPZCvBBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgUrbmeH",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "message": {
        "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "message": {
        "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello back",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423394,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
  "id": -576460752303423394,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "state": "tx_+QENCwH4hLhAvaAKF9bYtE6u8xB3FlU86mZDI+ft3tpgxYtPMMTy2JPFsP3r5jhBbBSMtdV/qt1GhGaqcwNTTXuDpizv0YE1BbhA6/ECjOGKmTlrapSNLI1xiNrCGjFXaoZjGFuTogrj405zXCZSenE0PSoYAkV5Rp0G9Sp/1EBQjxRkRhKPZCvBBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgUrbmeH"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "state": "tx_+QENCwH4hLhAvaAKF9bYtE6u8xB3FlU86mZDI+ft3tpgxYtPMMTy2JPFsP3r5jhBbBSMtdV/qt1GhGaqcwNTTXuDpizv0YE1BbhA6/ECjOGKmTlrapSNLI1xiNrCGjFXaoZjGFuTogrj405zXCZSenE0PSoYAkV5Rp0G9Sp/1EBQjxRkRhKPZCvBBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgUrbmeH"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423393,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
  "id": -576460752303423393,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423392,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kAgbNDfzDxi1rbJZAEqe93U3WszrgncPrb38koG9fpgEXNRLu",
  "id": -576460752303423392,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
