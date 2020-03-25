
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
      "fsm_id": "ba_LCG6dhPlDXAKoZtNLlZFIbxKw7wlpjKcUtFj5SCXBQp33GPt"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

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
      "fsm_id": "ba_5fRhzy9O1Xk8zhguXxDxivFUszv+Cz02Kbdm4PyEDBvACJfC"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBxrSp6rM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421951,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECwpgLpP9FghOPJWZ0eoeRHpTnhgPZPB9cAfPRKoyNeXyqtjhrrm+B6uxC36J1N0zB3t8SDt8qqOY+hrpQMGTgDuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcYGbuth"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421951,
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_5fRhzy9O1Xk8zhguXxDxivFUszv+Cz02Kbdm4PyEDBvACJfC"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECwpgLpP9FghOPJWZ0eoeRHpTnhgPZPB9cAfPRKoyNeXyqtjhrrm+B6uxC36J1N0zB3t8SDt8qqOY+hrpQMGTgDuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcYGbuth",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421950,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAsKYC6T/RYITjyVmdHqHkR6U54YD2TwfXAHz0SqMjXl8qrY4a65vgersQt+idTdMwd7fEg7fKqjmPoa6UDBk4A7hAtmTgiMTxUGJ1oy0V6kYAC267FrbHRpE56Yytsys+QhxPhchXdaJOVz0MSZOBQ5dn7D+b+a3SuWIT2gHH8+zxAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHGo9ujsw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
  "id": -576460752303421950,
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAsKYC6T/RYITjyVmdHqHkR6U54YD2TwfXAHz0SqMjXl8qrY4a65vgersQt+idTdMwd7fEg7fKqjmPoa6UDBk4A7hAtmTgiMTxUGJ1oy0V6kYAC267FrbHRpE56Yytsys+QhxPhchXdaJOVz0MSZOBQ5dn7D+b+a3SuWIT2gHH8+zxAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHGo9ujsw==",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_LCG6dhPlDXAKoZtNLlZFIbxKw7wlpjKcUtFj5SCXBQp33GPt"
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAsKYC6T/RYITjyVmdHqHkR6U54YD2TwfXAHz0SqMjXl8qrY4a65vgersQt+idTdMwd7fEg7fKqjmPoa6UDBk4A7hAtmTgiMTxUGJ1oy0V6kYAC267FrbHRpE56Yytsys+QhxPhchXdaJOVz0MSZOBQ5dn7D+b+a3SuWIT2gHH8+zxAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHGo9ujsw==",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAsKYC6T/RYITjyVmdHqHkR6U54YD2TwfXAHz0SqMjXl8qrY4a65vgersQt+idTdMwd7fEg7fKqjmPoa6UDBk4A7hAtmTgiMTxUGJ1oy0V6kYAC267FrbHRpE56Yytsys+QhxPhchXdaJOVz0MSZOBQ5dn7D+b+a3SuWIT2gHH8+zxAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHGo9ujsw==",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAsKYC6T/RYITjyVmdHqHkR6U54YD2TwfXAHz0SqMjXl8qrY4a65vgersQt+idTdMwd7fEg7fKqjmPoa6UDBk4A7hAtmTgiMTxUGJ1oy0V6kYAC267FrbHRpE56Yytsys+QhxPhchXdaJOVz0MSZOBQ5dn7D+b+a3SuWIT2gHH8+zxAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHGo9ujsw==",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "message": {
        "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "message": {
        "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
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
  "id": -576460752303421949,
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
  "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
  "id": -576460752303421949,
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "state": "tx_+QEOCwH4hLhAsKYC6T/RYITjyVmdHqHkR6U54YD2TwfXAHz0SqMjXl8qrY4a65vgersQt+idTdMwd7fEg7fKqjmPoa6UDBk4A7hAtmTgiMTxUGJ1oy0V6kYAC267FrbHRpE56Yytsys+QhxPhchXdaJOVz0MSZOBQ5dn7D+b+a3SuWIT2gHH8+zxAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHGo9ujsw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "state": "tx_+QEOCwH4hLhAsKYC6T/RYITjyVmdHqHkR6U54YD2TwfXAHz0SqMjXl8qrY4a65vgersQt+idTdMwd7fEg7fKqjmPoa6UDBk4A7hAtmTgiMTxUGJ1oy0V6kYAC267FrbHRpE56Yytsys+QhxPhchXdaJOVz0MSZOBQ5dn7D+b+a3SuWIT2gHH8+zxAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHGo9ujsw=="
    }
  },
  "version": 1
}
```
