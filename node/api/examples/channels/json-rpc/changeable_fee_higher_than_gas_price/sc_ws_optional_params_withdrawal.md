
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
      "fsm_id": "ba_hwc58/m5gYoTVB44n7UHMgaDF2lSpQSJ3NPCe8CW4gRhVgr5"
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
      "fsm_id": "ba_uRiK95bgig08XIi+Y/wFMGpT+hypgz71L86fOSqDo66o+b/1"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZs+ubisQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422481,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBGZtuqGpeSbxqnEYwSHMLyiHGC2N1j3fX4ge3kx0/Z37eULzAwtW4qjcUvl6PYYOe3edmvZ834byolzHKGCA4JuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGbLDr63k="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422481,
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_uRiK95bgig08XIi+Y/wFMGpT+hypgz71L86fOSqDo66o+b/1"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBGZtuqGpeSbxqnEYwSHMLyiHGC2N1j3fX4ge3kx0/Z37eULzAwtW4qjcUvl6PYYOe3edmvZ834byolzHKGCA4JuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGbLDr63k=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422480,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhARmbbqhqXkm8apxGMEhzC8ohxgtjdY931+IHt5MdP2d+3lC8wMLVuKo3FL5ej2GDnt3nZr2fN+G8qJcxyhggOCbhAivtlFulTJwNvxFBKDqJHhzq0/8FMQWk5DGoA27ert0SbELYLg3elIGxYTxhpCJ1iKC3fG70YhsMAa8EKJhLyDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmxqBONP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "id": -576460752303422480,
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhARmbbqhqXkm8apxGMEhzC8ohxgtjdY931+IHt5MdP2d+3lC8wMLVuKo3FL5ej2GDnt3nZr2fN+G8qJcxyhggOCbhAivtlFulTJwNvxFBKDqJHhzq0/8FMQWk5DGoA27ert0SbELYLg3elIGxYTxhpCJ1iKC3fG70YhsMAa8EKJhLyDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmxqBONP",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_hwc58/m5gYoTVB44n7UHMgaDF2lSpQSJ3NPCe8CW4gRhVgr5"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhARmbbqhqXkm8apxGMEhzC8ohxgtjdY931+IHt5MdP2d+3lC8wMLVuKo3FL5ej2GDnt3nZr2fN+G8qJcxyhggOCbhAivtlFulTJwNvxFBKDqJHhzq0/8FMQWk5DGoA27ert0SbELYLg3elIGxYTxhpCJ1iKC3fG70YhsMAa8EKJhLyDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmxqBONP",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARmbbqhqXkm8apxGMEhzC8ohxgtjdY931+IHt5MdP2d+3lC8wMLVuKo3FL5ej2GDnt3nZr2fN+G8qJcxyhggOCbhAivtlFulTJwNvxFBKDqJHhzq0/8FMQWk5DGoA27ert0SbELYLg3elIGxYTxhpCJ1iKC3fG70YhsMAa8EKJhLyDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmxqBONP",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARmbbqhqXkm8apxGMEhzC8ohxgtjdY931+IHt5MdP2d+3lC8wMLVuKo3FL5ej2GDnt3nZr2fN+G8qJcxyhggOCbhAivtlFulTJwNvxFBKDqJHhzq0/8FMQWk5DGoA27ert0SbELYLg3elIGxYTxhpCJ1iKC3fG70YhsMAa8EKJhLyDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmxqBONP",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
  "id": -576460752303422479,
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
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "id": -576460752303422479,
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "state": "tx_+QENCwH4hLhARmbbqhqXkm8apxGMEhzC8ohxgtjdY931+IHt5MdP2d+3lC8wMLVuKo3FL5ej2GDnt3nZr2fN+G8qJcxyhggOCbhAivtlFulTJwNvxFBKDqJHhzq0/8FMQWk5DGoA27ert0SbELYLg3elIGxYTxhpCJ1iKC3fG70YhsMAa8EKJhLyDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmxqBONP"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "state": "tx_+QENCwH4hLhARmbbqhqXkm8apxGMEhzC8ohxgtjdY931+IHt5MdP2d+3lC8wMLVuKo3FL5ej2GDnt3nZr2fN+G8qJcxyhggOCbhAivtlFulTJwNvxFBKDqJHhzq0/8FMQWk5DGoA27ert0SbELYLg3elIGxYTxhpCJ1iKC3fG70YhsMAa8EKJhLyDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmxqBONP"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBgPpL+9FBaQSNDLvmy8gH7bhU9Kr4Ff/NScsNP3M6slRoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhuCRDDYefqDc0aEz/UgoEcs4ajohf9X9BGhuePf6GLqnUld1F+cQwQJty6+VFw==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422478,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDejhqtRyoGrti4qQq5e551rGwZjcOEhmJqMysvTaal5aQDataL3vnw9+XTaZExHgT+raxVgozeFDKihGmcA7UCuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECbYoP9oY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "id": -576460752303422478,
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDejhqtRyoGrti4qQq5e551rGwZjcOEhmJqMysvTaal5aQDataL3vnw9+XTaZExHgT+raxVgozeFDKihGmcA7UCuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECbYoP9oY=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422477,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEDZxS2AW91BGeMcIF4GjIAH6Ev9eQuQ6pNgGmv9jCofoqj10ApJSa3tNbAf1aKFlUEWUvLOZaLc/TavI49P1KUAuEDejhqtRyoGrti4qQq5e551rGwZjcOEhmJqMysvTaal5aQDataL3vnw9+XTaZExHgT+raxVgozeFDKihGmcA7UCuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECbb1URVI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "id": -576460752303422477,
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEDZxS2AW91BGeMcIF4GjIAH6Ev9eQuQ6pNgGmv9jCofoqj10ApJSa3tNbAf1aKFlUEWUvLOZaLc/TavI49P1KUAuEDejhqtRyoGrti4qQq5e551rGwZjcOEhmJqMysvTaal5aQDataL3vnw9+XTaZExHgT+raxVgozeFDKihGmcA7UCuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECbb1URVI=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEDZxS2AW91BGeMcIF4GjIAH6Ev9eQuQ6pNgGmv9jCofoqj10ApJSa3tNbAf1aKFlUEWUvLOZaLc/TavI49P1KUAuEDejhqtRyoGrti4qQq5e551rGwZjcOEhmJqMysvTaal5aQDataL3vnw9+XTaZExHgT+raxVgozeFDKihGmcA7UCuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECbb1URVI=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello back",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
      }
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEDZxS2AW91BGeMcIF4GjIAH6Ev9eQuQ6pNgGmv9jCofoqj10ApJSa3tNbAf1aKFlUEWUvLOZaLc/TavI49P1KUAuEDejhqtRyoGrti4qQq5e551rGwZjcOEhmJqMysvTaal5aQDataL3vnw9+XTaZExHgT+raxVgozeFDKihGmcA7UCuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECbb1URVI=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEDZxS2AW91BGeMcIF4GjIAH6Ev9eQuQ6pNgGmv9jCofoqj10ApJSa3tNbAf1aKFlUEWUvLOZaLc/TavI49P1KUAuEDejhqtRyoGrti4qQq5e551rGwZjcOEhmJqMysvTaal5aQDataL3vnw9+XTaZExHgT+raxVgozeFDKihGmcA7UCuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECbb1URVI=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "state": "tx_+P4LAfiEuEDZxS2AW91BGeMcIF4GjIAH6Ev9eQuQ6pNgGmv9jCofoqj10ApJSa3tNbAf1aKFlUEWUvLOZaLc/TavI49P1KUAuEDejhqtRyoGrti4qQq5e551rGwZjcOEhmJqMysvTaal5aQDataL3vnw9+XTaZExHgT+raxVgozeFDKihGmcA7UCuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECbb1URVI="
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "state": "tx_+P4LAfiEuEDZxS2AW91BGeMcIF4GjIAH6Ev9eQuQ6pNgGmv9jCofoqj10ApJSa3tNbAf1aKFlUEWUvLOZaLc/TavI49P1KUAuEDejhqtRyoGrti4qQq5e551rGwZjcOEhmJqMysvTaal5aQDataL3vnw9+XTaZExHgT+raxVgozeFDKihGmcA7UCuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECbb1URVI="
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
    "info": "Hello",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
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
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBgPpL+9FBaQSNDLvmy8gH7bhU9Kr4Ff/NScsNP3M6slRoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhuCRDDYefqDZtcOT2QHMSn7Ye3r6M+jqyyVjQiph/medhaKMSYXlhQMslfcRoQ==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422476,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAtHBPRwdGNIUr9LZnpOb46foM1sIO3+AW+4O7nL12Wcqz5qag/5XFyO8btUOHRu4CQrarsBb+k9t0R47DvYuIAuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDLGUofkg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "id": -576460752303422476,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAtHBPRwdGNIUr9LZnpOb46foM1sIO3+AW+4O7nL12Wcqz5qag/5XFyO8btUOHRu4CQrarsBb+k9t0R47DvYuIAuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDLGUofkg=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422475,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAtHBPRwdGNIUr9LZnpOb46foM1sIO3+AW+4O7nL12Wcqz5qag/5XFyO8btUOHRu4CQrarsBb+k9t0R47DvYuIAuECtyUbEaOyFgL2z7kX+WUUGQJ6zFBACa4H6JeURSPem+yRsZRQ3LG+YIOPRkw3xZgb/KV2ns9+2SQlRovxtn/YNuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDLFemU/w="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "id": -576460752303422475,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAtHBPRwdGNIUr9LZnpOb46foM1sIO3+AW+4O7nL12Wcqz5qag/5XFyO8btUOHRu4CQrarsBb+k9t0R47DvYuIAuECtyUbEaOyFgL2z7kX+WUUGQJ6zFBACa4H6JeURSPem+yRsZRQ3LG+YIOPRkw3xZgb/KV2ns9+2SQlRovxtn/YNuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDLFemU/w=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAtHBPRwdGNIUr9LZnpOb46foM1sIO3+AW+4O7nL12Wcqz5qag/5XFyO8btUOHRu4CQrarsBb+k9t0R47DvYuIAuECtyUbEaOyFgL2z7kX+WUUGQJ6zFBACa4H6JeURSPem+yRsZRQ3LG+YIOPRkw3xZgb/KV2ns9+2SQlRovxtn/YNuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDLFemU/w=",
      "type": "channel_withdraw_tx"
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
    "info": "Hello",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "message": {
        "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
      }
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAtHBPRwdGNIUr9LZnpOb46foM1sIO3+AW+4O7nL12Wcqz5qag/5XFyO8btUOHRu4CQrarsBb+k9t0R47DvYuIAuECtyUbEaOyFgL2z7kX+WUUGQJ6zFBACa4H6JeURSPem+yRsZRQ3LG+YIOPRkw3xZgb/KV2ns9+2SQlRovxtn/YNuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDLFemU/w=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAtHBPRwdGNIUr9LZnpOb46foM1sIO3+AW+4O7nL12Wcqz5qag/5XFyO8btUOHRu4CQrarsBb+k9t0R47DvYuIAuECtyUbEaOyFgL2z7kX+WUUGQJ6zFBACa4H6JeURSPem+yRsZRQ3LG+YIOPRkw3xZgb/KV2ns9+2SQlRovxtn/YNuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDLFemU/w=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "state": "tx_+P4LAfiEuEAtHBPRwdGNIUr9LZnpOb46foM1sIO3+AW+4O7nL12Wcqz5qag/5XFyO8btUOHRu4CQrarsBb+k9t0R47DvYuIAuECtyUbEaOyFgL2z7kX+WUUGQJ6zFBACa4H6JeURSPem+yRsZRQ3LG+YIOPRkw3xZgb/KV2ns9+2SQlRovxtn/YNuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDLFemU/w="
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "state": "tx_+P4LAfiEuEAtHBPRwdGNIUr9LZnpOb46foM1sIO3+AW+4O7nL12Wcqz5qag/5XFyO8btUOHRu4CQrarsBb+k9t0R47DvYuIAuECtyUbEaOyFgL2z7kX+WUUGQJ6zFBACa4H6JeURSPem+yRsZRQ3LG+YIOPRkw3xZgb/KV2ns9+2SQlRovxtn/YNuHT4cjQBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDLFemU/w="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBgPpL+9FBaQSNDLvmy8gH7bhU9Kr4Ff/NScsNP3M6slRoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/2GHLHOiuv/AIYPXtZ/KABubeo43w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422474,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAOpTFo/Rfl16iSZgC57xDiCZOmv+9E3aqPhXCG8BdsX29mIaYkxMdEgnqtLV6BY966Vw2aS/vanDMsO4S4F0AKuF/4XTUBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAbrdJnSw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "id": -576460752303422474,
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAOpTFo/Rfl16iSZgC57xDiCZOmv+9E3aqPhXCG8BdsX29mIaYkxMdEgnqtLV6BY966Vw2aS/vanDMsO4S4F0AKuF/4XTUBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAbrdJnSw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422473,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAOpTFo/Rfl16iSZgC57xDiCZOmv+9E3aqPhXCG8BdsX29mIaYkxMdEgnqtLV6BY966Vw2aS/vanDMsO4S4F0AKuECzniJ5jkdJhCP2pfRfEfhEPYX8NECCXR5AuncHtEiAUtzhQouTJAhGSJqiuqQgb1D77QxEogMrMvrx9wDRoj8CuF/4XTUBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAbqU0Mac="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
  "id": -576460752303422473,
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAOpTFo/Rfl16iSZgC57xDiCZOmv+9E3aqPhXCG8BdsX29mIaYkxMdEgnqtLV6BY966Vw2aS/vanDMsO4S4F0AKuECzniJ5jkdJhCP2pfRfEfhEPYX8NECCXR5AuncHtEiAUtzhQouTJAhGSJqiuqQgb1D77QxEogMrMvrx9wDRoj8CuF/4XTUBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAbqU0Mac=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAOpTFo/Rfl16iSZgC57xDiCZOmv+9E3aqPhXCG8BdsX29mIaYkxMdEgnqtLV6BY966Vw2aS/vanDMsO4S4F0AKuECzniJ5jkdJhCP2pfRfEfhEPYX8NECCXR5AuncHtEiAUtzhQouTJAhGSJqiuqQgb1D77QxEogMrMvrx9wDRoj8CuF/4XTUBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAbqU0Mac=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAOpTFo/Rfl16iSZgC57xDiCZOmv+9E3aqPhXCG8BdsX29mIaYkxMdEgnqtLV6BY966Vw2aS/vanDMsO4S4F0AKuECzniJ5jkdJhCP2pfRfEfhEPYX8NECCXR5AuncHtEiAUtzhQouTJAhGSJqiuqQgb1D77QxEogMrMvrx9wDRoj8CuF/4XTUBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAbqU0Mac=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAOpTFo/Rfl16iSZgC57xDiCZOmv+9E3aqPhXCG8BdsX29mIaYkxMdEgnqtLV6BY966Vw2aS/vanDMsO4S4F0AKuECzniJ5jkdJhCP2pfRfEfhEPYX8NECCXR5AuncHtEiAUtzhQouTJAhGSJqiuqQgb1D77QxEogMrMvrx9wDRoj8CuF/4XTUBoQYD6S/vRQWkEjQy75svIB+24VPSq+BX/zUnLDT9zOrJUaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAbqU0Mac=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2iu79594fVX4c8vU7sDDSsekDL3qJy2ZRZPU2igmEzuoat8BZ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
