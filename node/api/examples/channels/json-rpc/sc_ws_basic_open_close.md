
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
      "fsm_id": "ba_j5r5E5mdhQFag+ObX+RXEvr4qFyzkWcVSRlDy169qe3DD8TM"
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
      "fsm_id": "ba_8ZDO4Vq7V4/DxE4c0znoqUzL3YTX0oRnfhsWLHKZRdUHUdLa"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYDMmE4pg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423456,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAWfG2f7J6OlQClux800P58isBpSsCZkxN3E5OYYTAXiemge8bm+aEkdGiGkoNd/6ebUQPMq00JqvPnsV1Kg64BuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGA1s5k3c="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423456,
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_8ZDO4Vq7V4/DxE4c0znoqUzL3YTX0oRnfhsWLHKZRdUHUdLa"
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAWfG2f7J6OlQClux800P58isBpSsCZkxN3E5OYYTAXiemge8bm+aEkdGiGkoNd/6ebUQPMq00JqvPnsV1Kg64BuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGA1s5k3c=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423455,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAFnxtn+yejpUApbsfNND+fIrAaUrAmZMTdxOTmGEwF4npoHvG5vmhJHRohpKDXf+nm1EDzKtNCarz57FdSoOuAbhAr0pHgif1xezYZbr3n/7F9jzWbUBTy6qbU2K1YiSU1Y+qnMUmcGbRYieWsNPbt3kONBG+OrvisSXsTHbUD7SoCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgN3M95P"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423455,
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAFnxtn+yejpUApbsfNND+fIrAaUrAmZMTdxOTmGEwF4npoHvG5vmhJHRohpKDXf+nm1EDzKtNCarz57FdSoOuAbhAr0pHgif1xezYZbr3n/7F9jzWbUBTy6qbU2K1YiSU1Y+qnMUmcGbRYieWsNPbt3kONBG+OrvisSXsTHbUD7SoCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgN3M95P",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_j5r5E5mdhQFag+ObX+RXEvr4qFyzkWcVSRlDy169qe3DD8TM"
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAFnxtn+yejpUApbsfNND+fIrAaUrAmZMTdxOTmGEwF4npoHvG5vmhJHRohpKDXf+nm1EDzKtNCarz57FdSoOuAbhAr0pHgif1xezYZbr3n/7F9jzWbUBTy6qbU2K1YiSU1Y+qnMUmcGbRYieWsNPbt3kONBG+OrvisSXsTHbUD7SoCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgN3M95P",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFnxtn+yejpUApbsfNND+fIrAaUrAmZMTdxOTmGEwF4npoHvG5vmhJHRohpKDXf+nm1EDzKtNCarz57FdSoOuAbhAr0pHgif1xezYZbr3n/7F9jzWbUBTy6qbU2K1YiSU1Y+qnMUmcGbRYieWsNPbt3kONBG+OrvisSXsTHbUD7SoCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgN3M95P",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFnxtn+yejpUApbsfNND+fIrAaUrAmZMTdxOTmGEwF4npoHvG5vmhJHRohpKDXf+nm1EDzKtNCarz57FdSoOuAbhAr0pHgif1xezYZbr3n/7F9jzWbUBTy6qbU2K1YiSU1Y+qnMUmcGbRYieWsNPbt3kONBG+OrvisSXsTHbUD7SoCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgN3M95P",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "message": {
        "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "message": {
        "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
  "id": -576460752303423454,
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
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423454,
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+QENCwH4hLhAFnxtn+yejpUApbsfNND+fIrAaUrAmZMTdxOTmGEwF4npoHvG5vmhJHRohpKDXf+nm1EDzKtNCarz57FdSoOuAbhAr0pHgif1xezYZbr3n/7F9jzWbUBTy6qbU2K1YiSU1Y+qnMUmcGbRYieWsNPbt3kONBG+OrvisSXsTHbUD7SoCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgN3M95P"
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+QENCwH4hLhAFnxtn+yejpUApbsfNND+fIrAaUrAmZMTdxOTmGEwF4npoHvG5vmhJHRohpKDXf+nm1EDzKtNCarz57FdSoOuAbhAr0pHgif1xezYZbr3n/7F9jzWbUBTy6qbU2K1YiSU1Y+qnMUmcGbRYieWsNPbt3kONBG+OrvisSXsTHbUD7SoCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgN3M95P"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423453,
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
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423453,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": 17,
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "meta": 17,
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuT5e+XKyThqAiYvV0hkUvVSNtVsV+gHRhQ1zF3Da0Y1AqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCypDy6co=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
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
  "id": -576460752303423452,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECqp0rQ4DAAmyd9R5ePFyzBsFaUJs5rPfvy9GqDYTIFh6O8OFMKX/sRCXYz7B6736j11qJElCr+lhnb7DDCmyEPuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoQEmy0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423452,
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+JALAfhCuECqp0rQ4DAAmyd9R5ePFyzBsFaUJs5rPfvy9GqDYTIFh6O8OFMKX/sRCXYz7B6736j11qJElCr+lhnb7DDCmyEPuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoQEmy0",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
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
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEChqBX584g5NqyU34EyIJ+sw56z4HRKnDegoiIk2TjjzkNqZeNF+CWW7Mfpfem3DkzArYm2uwSaWQopFCMgH+EPuECqp0rQ4DAAmyd9R5ePFyzBsFaUJs5rPfvy9GqDYTIFh6O8OFMKX/sRCXYz7B6736j11qJElCr+lhnb7DDCmyEPuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqkdq01"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuEChqBX584g5NqyU34EyIJ+sw56z4HRKnDegoiIk2TjjzkNqZeNF+CWW7Mfpfem3DkzArYm2uwSaWQopFCMgH+EPuECqp0rQ4DAAmyd9R5ePFyzBsFaUJs5rPfvy9GqDYTIFh6O8OFMKX/sRCXYz7B6736j11qJElCr+lhnb7DDCmyEPuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqkdq01"
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuEChqBX584g5NqyU34EyIJ+sw56z4HRKnDegoiIk2TjjzkNqZeNF+CWW7Mfpfem3DkzArYm2uwSaWQopFCMgH+EPuECqp0rQ4DAAmyd9R5ePFyzBsFaUJs5rPfvy9GqDYTIFh6O8OFMKX/sRCXYz7B6736j11qJElCr+lhnb7DDCmyEPuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqkdq01"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423450,
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
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423450,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEChqBX584g5NqyU34EyIJ+sw56z4HRKnDegoiIk2TjjzkNqZeNF+CWW7Mfpfem3DkzArYm2uwSaWQopFCMgH+EPuECqp0rQ4DAAmyd9R5ePFyzBsFaUJs5rPfvy9GqDYTIFh6O8OFMKX/sRCXYz7B6736j11qJElCr+lhnb7DDCmyEPuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqkdq01",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423448,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423448,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": 17,
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": 17,
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuT5e+XKyThqAiYvV0hkUvVSNtVsV+gHRhQ1zF3Da0Y1A6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhwer8c=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303423447,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDX98yJy9GcBN+WnmF6Q4cYsPTAKH9oK6b3zUJRPlzSutOCr7U17qqAanfg4+BZ93F2wV9QN8szjyKX5TB6p9wCuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYvi7G9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423447,
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDX98yJy9GcBN+WnmF6Q4cYsPTAKH9oK6b3zUJRPlzSutOCr7U17qqAanfg4+BZ93F2wV9QN8szjyKX5TB6p9wCuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYvi7G9",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECMRwqWEN55+eeZ2N6jqgDYveFQy+q1XL6ozZUO8X5VMq8zZxtI0Lv6z32FSaOvP40oUJivu8CujBgwMlw93HMFuEDX98yJy9GcBN+WnmF6Q4cYsPTAKH9oK6b3zUJRPlzSutOCr7U17qqAanfg4+BZ93F2wV9QN8szjyKX5TB6p9wCuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb96LkH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuECMRwqWEN55+eeZ2N6jqgDYveFQy+q1XL6ozZUO8X5VMq8zZxtI0Lv6z32FSaOvP40oUJivu8CujBgwMlw93HMFuEDX98yJy9GcBN+WnmF6Q4cYsPTAKH9oK6b3zUJRPlzSutOCr7U17qqAanfg4+BZ93F2wV9QN8szjyKX5TB6p9wCuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb96LkH"
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuECMRwqWEN55+eeZ2N6jqgDYveFQy+q1XL6ozZUO8X5VMq8zZxtI0Lv6z32FSaOvP40oUJivu8CujBgwMlw93HMFuEDX98yJy9GcBN+WnmF6Q4cYsPTAKH9oK6b3zUJRPlzSutOCr7U17qqAanfg4+BZ93F2wV9QN8szjyKX5TB6p9wCuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb96LkH"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423445,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423445,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000001
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECMRwqWEN55+eeZ2N6jqgDYveFQy+q1XL6ozZUO8X5VMq8zZxtI0Lv6z32FSaOvP40oUJivu8CujBgwMlw93HMFuEDX98yJy9GcBN+WnmF6Q4cYsPTAKH9oK6b3zUJRPlzSutOCr7U17qqAanfg4+BZ93F2wV9QN8szjyKX5TB6p9wCuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb96LkH",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423443,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423443,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000001
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": 17,
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": 17,
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuT5e+XKyThqAiYvV0hkUvVSNtVsV+gHRhQ1zF3Da0Y1BKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYLcLCtM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303423442,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED2fXRBwuxtJg/5S3hIrHI0tR/MzbLcKT5ubdHbzBsek9sh2rYmETLZwMKR50TEnYC4CArqhs4+bG1fHay29YoHuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDMIJ6z"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423442,
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+JALAfhCuED2fXRBwuxtJg/5S3hIrHI0tR/MzbLcKT5ubdHbzBsek9sh2rYmETLZwMKR50TEnYC4CArqhs4+bG1fHay29YoHuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDMIJ6z",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303423441,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEASK8LH09bVwXDI9SEXUVoOZQg8BOAMrXH6Fk1hsUR3j0jDPSb7vN/Yjo7a/XuMGpTQ3RqsutE0wIJvAGdd4wkHuED2fXRBwuxtJg/5S3hIrHI0tR/MzbLcKT5ubdHbzBsek9sh2rYmETLZwMKR50TEnYC4CArqhs4+bG1fHay29YoHuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBg0CfO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423441,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuEASK8LH09bVwXDI9SEXUVoOZQg8BOAMrXH6Fk1hsUR3j0jDPSb7vN/Yjo7a/XuMGpTQ3RqsutE0wIJvAGdd4wkHuED2fXRBwuxtJg/5S3hIrHI0tR/MzbLcKT5ubdHbzBsek9sh2rYmETLZwMKR50TEnYC4CArqhs4+bG1fHay29YoHuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBg0CfO"
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuEASK8LH09bVwXDI9SEXUVoOZQg8BOAMrXH6Fk1hsUR3j0jDPSb7vN/Yjo7a/XuMGpTQ3RqsutE0wIJvAGdd4wkHuED2fXRBwuxtJg/5S3hIrHI0tR/MzbLcKT5ubdHbzBsek9sh2rYmETLZwMKR50TEnYC4CArqhs4+bG1fHay29YoHuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBg0CfO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423440,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423440,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000000
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEASK8LH09bVwXDI9SEXUVoOZQg8BOAMrXH6Fk1hsUR3j0jDPSb7vN/Yjo7a/XuMGpTQ3RqsutE0wIJvAGdd4wkHuED2fXRBwuxtJg/5S3hIrHI0tR/MzbLcKT5ubdHbzBsek9sh2rYmETLZwMKR50TEnYC4CArqhs4+bG1fHay29YoHuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBg0CfO",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423438,
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
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423438,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 70000000000000
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": 17,
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "meta": 17,
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuT5e+XKyThqAiYvV0hkUvVSNtVsV+gHRhQ1zF3Da0Y1BaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rha9P8M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
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
  "id": -576460752303423437,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA86EntCXz0PpaB2AdzSTks2mo3HUT1gcRmShvdIW10c92Zdeq+x6VngJMl+UYrDZ2Z/GcN2pCxfTa2oNBjDFcGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaF0lKK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423437,
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA86EntCXz0PpaB2AdzSTks2mo3HUT1gcRmShvdIW10c92Zdeq+x6VngJMl+UYrDZ2Z/GcN2pCxfTa2oNBjDFcGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaF0lKK",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
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
  "id": -576460752303423436,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA86EntCXz0PpaB2AdzSTks2mo3HUT1gcRmShvdIW10c92Zdeq+x6VngJMl+UYrDZ2Z/GcN2pCxfTa2oNBjDFcGuECQ/zkcN9VaZYEAFJp7R44u7WwybB4kZQy/hjkN+Pv1PzgY1wZYkwnwjCe4RdzLyLlt8fp6aSDuZhyDLLvnozIGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaTkiXz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423436,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuEA86EntCXz0PpaB2AdzSTks2mo3HUT1gcRmShvdIW10c92Zdeq+x6VngJMl+UYrDZ2Z/GcN2pCxfTa2oNBjDFcGuECQ/zkcN9VaZYEAFJp7R44u7WwybB4kZQy/hjkN+Pv1PzgY1wZYkwnwjCe4RdzLyLlt8fp6aSDuZhyDLLvnozIGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaTkiXz"
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuEA86EntCXz0PpaB2AdzSTks2mo3HUT1gcRmShvdIW10c92Zdeq+x6VngJMl+UYrDZ2Z/GcN2pCxfTa2oNBjDFcGuECQ/zkcN9VaZYEAFJp7R44u7WwybB4kZQy/hjkN+Pv1PzgY1wZYkwnwjCe4RdzLyLlt8fp6aSDuZhyDLLvnozIGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaTkiXz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423435,
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
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423435,
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

#### initiator ---> node
```javascript
{
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA86EntCXz0PpaB2AdzSTks2mo3HUT1gcRmShvdIW10c92Zdeq+x6VngJMl+UYrDZ2Z/GcN2pCxfTa2oNBjDFcGuECQ/zkcN9VaZYEAFJp7R44u7WwybB4kZQy/hjkN+Pv1PzgY1wZYkwnwjCe4RdzLyLlt8fp6aSDuZhyDLLvnozIGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaTkiXz",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423433,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423433,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000001
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": 17,
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": 17,
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuT5e+XKyThqAiYvV0hkUvVSNtVsV+gHRhQ1zF3Da0Y1BqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYKFAWbw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303423432,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB806uxZjbFh5e10rv3ve1O0BtA642OpEQ5Q7iQD/nadomHvzdvvJgMUFwXpoMYCrKR0QOWSFtkIEvT3iohFgAGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWA5DMWR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423432,
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB806uxZjbFh5e10rv3ve1O0BtA642OpEQ5Q7iQD/nadomHvzdvvJgMUFwXpoMYCrKR0QOWSFtkIEvT3iohFgAGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWA5DMWR",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAeXLDNFk0CdU3LTkSW6cUv6EPtBBgjs2pVL3PFL0QuCt5TqjQse9rW661L+u1VJXsQNBGLmvoZzNxSlRDJMvMPuEB806uxZjbFh5e10rv3ve1O0BtA642OpEQ5Q7iQD/nadomHvzdvvJgMUFwXpoMYCrKR0QOWSFtkIEvT3iohFgAGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBJf+kb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuEAeXLDNFk0CdU3LTkSW6cUv6EPtBBgjs2pVL3PFL0QuCt5TqjQse9rW661L+u1VJXsQNBGLmvoZzNxSlRDJMvMPuEB806uxZjbFh5e10rv3ve1O0BtA642OpEQ5Q7iQD/nadomHvzdvvJgMUFwXpoMYCrKR0QOWSFtkIEvT3iohFgAGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBJf+kb"
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
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "state": "tx_+NILAfiEuEAeXLDNFk0CdU3LTkSW6cUv6EPtBBgjs2pVL3PFL0QuCt5TqjQse9rW661L+u1VJXsQNBGLmvoZzNxSlRDJMvMPuEB806uxZjbFh5e10rv3ve1O0BtA642OpEQ5Q7iQD/nadomHvzdvvJgMUFwXpoMYCrKR0QOWSFtkIEvT3iohFgAGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBJf+kb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423430,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423430,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000000
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423429,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423429,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAeXLDNFk0CdU3LTkSW6cUv6EPtBBgjs2pVL3PFL0QuCt5TqjQse9rW661L+u1VJXsQNBGLmvoZzNxSlRDJMvMPuEB806uxZjbFh5e10rv3ve1O0BtA642OpEQ5Q7iQD/nadomHvzdvvJgMUFwXpoMYCrKR0QOWSFtkIEvT3iohFgAGuEj4RjkCoQbk+Xvlysk4agImL1dIZFL1UjbVbFfoB0YUNcxdw2tGNQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBJf+kb",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423428,
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
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423428,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423427,
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jqr9vjPiaNk2H4iE3pV9FCayL1BbyT4nDk4WHd6HTE16ZswWu",
  "id": -576460752303423427,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
