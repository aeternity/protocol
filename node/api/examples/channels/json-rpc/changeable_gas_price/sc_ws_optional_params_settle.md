
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
      "fsm_id": "ba_2TNAYnBApR+hTx67ZMIj7rAOb6u19BoMNEj7WNxbwHpmNJ8m"
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
      "fsm_id": "ba_UK0v+u+e7R/Fd+g56bNTmLm2V4SOF8oim9oFGKax9agHYV1Q"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZiy+mXNQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422501,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDIDW6rCDHJONPvwP0h3PLBRo26oziVL7yLtrsXuUlCSLD2nxa2ldUx+c/29lxnKSyHMIkP9MOUQ2lnlxHuQjQHuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGYjpFdls="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422501,
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_UK0v+u+e7R/Fd+g56bNTmLm2V4SOF8oim9oFGKax9agHYV1Q"
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDIDW6rCDHJONPvwP0h3PLBRo26oziVL7yLtrsXuUlCSLD2nxa2ldUx+c/29lxnKSyHMIkP9MOUQ2lnlxHuQjQHuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGYjpFdls=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422500,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAZnIHHhbV2HTgwNke9RHoDuoCxm7Zgl+8g2nneChnDwP+EKp2IFbLrCTVIMZnZRtpbazjA2CJvhwsLWwmANjsBbhAyA1uqwgxyTjT78D9IdzywUaNuqM4lS+8i7a7F7lJQkiw9p8WtpXVMfnP9vZcZykshzCJD/TDlENpZ5cR7kI0B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmJX7c9C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
  "id": -576460752303422500,
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAZnIHHhbV2HTgwNke9RHoDuoCxm7Zgl+8g2nneChnDwP+EKp2IFbLrCTVIMZnZRtpbazjA2CJvhwsLWwmANjsBbhAyA1uqwgxyTjT78D9IdzywUaNuqM4lS+8i7a7F7lJQkiw9p8WtpXVMfnP9vZcZykshzCJD/TDlENpZ5cR7kI0B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmJX7c9C",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_2TNAYnBApR+hTx67ZMIj7rAOb6u19BoMNEj7WNxbwHpmNJ8m"
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAZnIHHhbV2HTgwNke9RHoDuoCxm7Zgl+8g2nneChnDwP+EKp2IFbLrCTVIMZnZRtpbazjA2CJvhwsLWwmANjsBbhAyA1uqwgxyTjT78D9IdzywUaNuqM4lS+8i7a7F7lJQkiw9p8WtpXVMfnP9vZcZykshzCJD/TDlENpZ5cR7kI0B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmJX7c9C",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAZnIHHhbV2HTgwNke9RHoDuoCxm7Zgl+8g2nneChnDwP+EKp2IFbLrCTVIMZnZRtpbazjA2CJvhwsLWwmANjsBbhAyA1uqwgxyTjT78D9IdzywUaNuqM4lS+8i7a7F7lJQkiw9p8WtpXVMfnP9vZcZykshzCJD/TDlENpZ5cR7kI0B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmJX7c9C",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAZnIHHhbV2HTgwNke9RHoDuoCxm7Zgl+8g2nneChnDwP+EKp2IFbLrCTVIMZnZRtpbazjA2CJvhwsLWwmANjsBbhAyA1uqwgxyTjT78D9IdzywUaNuqM4lS+8i7a7F7lJQkiw9p8WtpXVMfnP9vZcZykshzCJD/TDlENpZ5cR7kI0B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmJX7c9C",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "message": {
        "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "message": {
        "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
  "id": -576460752303422499,
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
  "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
  "id": -576460752303422499,
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "state": "tx_+QENCwH4hLhAZnIHHhbV2HTgwNke9RHoDuoCxm7Zgl+8g2nneChnDwP+EKp2IFbLrCTVIMZnZRtpbazjA2CJvhwsLWwmANjsBbhAyA1uqwgxyTjT78D9IdzywUaNuqM4lS+8i7a7F7lJQkiw9p8WtpXVMfnP9vZcZykshzCJD/TDlENpZ5cR7kI0B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmJX7c9C"
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "state": "tx_+QENCwH4hLhAZnIHHhbV2HTgwNke9RHoDuoCxm7Zgl+8g2nneChnDwP+EKp2IFbLrCTVIMZnZRtpbazjA2CJvhwsLWwmANjsBbhAyA1uqwgxyTjT78D9IdzywUaNuqM4lS+8i7a7F7lJQkiw9p8WtpXVMfnP9vZcZykshzCJD/TDlENpZ5cR7kI0B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmJX7c9C"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBjTaX9IZX9vER5ThQBlmwb+LrCarEP2iF7abQ1bXIuLRoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7sgIAAY9e2i/Y=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhACA8R/4ixQulNjv0BqrpZGH5qoQLoyZBsVx+WigQVYrVXaEnm4xG7ntfyn5YlSQP5w+Bne8b0EDg7j1cli4XoB7kBovkBnzYBoQY02l/SGV/bxEeU4UAZZsG/i6wmqxD9ohe2m0NW1yLi0aEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAGPNzntW"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhACA8R/4ixQulNjv0BqrpZGH5qoQLoyZBsVx+WigQVYrVXaEnm4xG7ntfyn5YlSQP5w+Bne8b0EDg7j1cli4XoB7kBovkBnzYBoQY02l/SGV/bxEeU4UAZZsG/i6wmqxD9ohe2m0NW1yLi0aEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAGPNzntW",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhACA8R/4ixQulNjv0BqrpZGH5qoQLoyZBsVx+WigQVYrVXaEnm4xG7ntfyn5YlSQP5w+Bne8b0EDg7j1cli4XoB7kBovkBnzYBoQY02l/SGV/bxEeU4UAZZsG/i6wmqxD9ohe2m0NW1yLi0aEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAGPNzntW",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBjTaX9IZX9vER5ThQBlmwb+LrCarEP2iF7abQ1bXIuLRoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXte9X0gqKJWJAQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBmJQED5YvvlhB1QE0huLlfgYUUL8aSOskletbkn/WRR4LB90+2dlbdZOyhsXWZNHLTI1/piySbet1fEje7N68CuF/4XTgBoQY02l/SGV/bxEeU4UAZZsG/i6wmqxD9ohe2m0NW1yLi0aEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17XvV9IKoGvef0="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBmJQED5YvvlhB1QE0huLlfgYUUL8aSOskletbkn/WRR4LB90+2dlbdZOyhsXWZNHLTI1/piySbet1fEje7N68CuF/4XTgBoQY02l/SGV/bxEeU4UAZZsG/i6wmqxD9ohe2m0NW1yLi0aEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17XvV9IKoGvef0=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBmJQED5YvvlhB1QE0huLlfgYUUL8aSOskletbkn/WRR4LB90+2dlbdZOyhsXWZNHLTI1/piySbet1fEje7N68CuF/4XTgBoQY02l/SGV/bxEeU4UAZZsG/i6wmqxD9ohe2m0NW1yLi0aEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17XvV9IKoGvef0=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
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
    "channel_id": "ch_QH4TRFoASts35XCTTWVLQ6qxxwXAWVyWwSTt6jQUvcwsQwqLM",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

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
      "fsm_id": "ba_UEo0jjZ+O4IdGDfJ2pBsuLXYP0nOKQL2KyrMh2Dv8hIWKmmd"
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
      "fsm_id": "ba_SWuM2SqT2m5CqleZRh3hlMztvGMqkn5B1B5gRC4YmO24bd75"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZk/hhIdg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422498,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDUQy/1kavOjnp85wzKiiaQYFV4Vg1tVWTaJAjEDsVauvkWYpihKM39uA6nd32w7IK5Pz7p7PXyrUuaFKyzrAQPuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGZOwLNuQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422498,
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_SWuM2SqT2m5CqleZRh3hlMztvGMqkn5B1B5gRC4YmO24bd75"
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDUQy/1kavOjnp85wzKiiaQYFV4Vg1tVWTaJAjEDsVauvkWYpihKM39uA6nd32w7IK5Pz7p7PXyrUuaFKyzrAQPuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGZOwLNuQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422497,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhA1EMv9ZGrzo56fOcMyoomkGBVeFYNbVVk2iQIxA7FWrr5FmKYoSjN/bgOp3d9sOyCuT8+6ez18q1LmhSss6wED7hA/5pU86Ql1a5a8He7VXwPSijui1/32GF5OmLgC6lvksR4NKw9Sc3mKRi7QOw9ZQUe+BvJCzKW49OHNmkjyC8NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmQvH/Qt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
  "id": -576460752303422497,
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhA1EMv9ZGrzo56fOcMyoomkGBVeFYNbVVk2iQIxA7FWrr5FmKYoSjN/bgOp3d9sOyCuT8+6ez18q1LmhSss6wED7hA/5pU86Ql1a5a8He7VXwPSijui1/32GF5OmLgC6lvksR4NKw9Sc3mKRi7QOw9ZQUe+BvJCzKW49OHNmkjyC8NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmQvH/Qt",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_UEo0jjZ+O4IdGDfJ2pBsuLXYP0nOKQL2KyrMh2Dv8hIWKmmd"
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhA1EMv9ZGrzo56fOcMyoomkGBVeFYNbVVk2iQIxA7FWrr5FmKYoSjN/bgOp3d9sOyCuT8+6ez18q1LmhSss6wED7hA/5pU86Ql1a5a8He7VXwPSijui1/32GF5OmLgC6lvksR4NKw9Sc3mKRi7QOw9ZQUe+BvJCzKW49OHNmkjyC8NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmQvH/Qt",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA1EMv9ZGrzo56fOcMyoomkGBVeFYNbVVk2iQIxA7FWrr5FmKYoSjN/bgOp3d9sOyCuT8+6ez18q1LmhSss6wED7hA/5pU86Ql1a5a8He7VXwPSijui1/32GF5OmLgC6lvksR4NKw9Sc3mKRi7QOw9ZQUe+BvJCzKW49OHNmkjyC8NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmQvH/Qt",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA1EMv9ZGrzo56fOcMyoomkGBVeFYNbVVk2iQIxA7FWrr5FmKYoSjN/bgOp3d9sOyCuT8+6ez18q1LmhSss6wED7hA/5pU86Ql1a5a8He7VXwPSijui1/32GF5OmLgC6lvksR4NKw9Sc3mKRi7QOw9ZQUe+BvJCzKW49OHNmkjyC8NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmQvH/Qt",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "message": {
        "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "message": {
        "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
  "id": -576460752303422496,
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
  "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
  "id": -576460752303422496,
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "state": "tx_+QENCwH4hLhA1EMv9ZGrzo56fOcMyoomkGBVeFYNbVVk2iQIxA7FWrr5FmKYoSjN/bgOp3d9sOyCuT8+6ez18q1LmhSss6wED7hA/5pU86Ql1a5a8He7VXwPSijui1/32GF5OmLgC6lvksR4NKw9Sc3mKRi7QOw9ZQUe+BvJCzKW49OHNmkjyC8NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmQvH/Qt"
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "state": "tx_+QENCwH4hLhA1EMv9ZGrzo56fOcMyoomkGBVeFYNbVVk2iQIxA7FWrr5FmKYoSjN/bgOp3d9sOyCuT8+6ez18q1LmhSss6wED7hA/5pU86Ql1a5a8He7VXwPSijui1/32GF5OmLgC6lvksR4NKw9Sc3mKRi7QOw9ZQUe+BvJCzKW49OHNmkjyC8NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmQvH/Qt"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBlvx+zxohvxf7tZkI0Bs9VC+j5Dv9voUmmLHPZ+svIwmoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7sgIAAZWbRySo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhA9E6t1M8h6bMrRTWz19Tdmg5Iwirda7jtwdgPjdVQALkr9knanti+Iq5wu9MprgWjnDTsQFYXRYyZO+Y7YdtxDrkBovkBnzYBoQZb8fs8aIb8X+7WZCNAbPVQvo+Q7/b6FJpixz2frLyMJqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAGUwOEQT"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA9E6t1M8h6bMrRTWz19Tdmg5Iwirda7jtwdgPjdVQALkr9knanti+Iq5wu9MprgWjnDTsQFYXRYyZO+Y7YdtxDrkBovkBnzYBoQZb8fs8aIb8X+7WZCNAbPVQvo+Q7/b6FJpixz2frLyMJqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAGUwOEQT",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA9E6t1M8h6bMrRTWz19Tdmg5Iwirda7jtwdgPjdVQALkr9knanti+Iq5wu9MprgWjnDTsQFYXRYyZO+Y7YdtxDrkBovkBnzYBoQZb8fs8aIb8X+7WZCNAbPVQvo+Q7/b6FJpixz2frLyMJqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAGUwOEQT",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBlvx+zxohvxf7tZkI0Bs9VC+j5Dv9voUmmLHPZ+svIwmoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiX/+GJGE5yoABAIYPXte9X0hmRb8Gdw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECoFvAfQkfm0cR4pzJl2mpo9HtQArwZzl312awnaRsqkzdU7/5GX5Bw7ZrJAN0Bxx94q25CZan3tKbjBRstcEEMuF/4XTgBoQZb8fs8aIb8X+7WZCNAbPVQvo+Q7/b6FJpixz2frLyMJqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGD17XvV9IZvV/jOU="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECoFvAfQkfm0cR4pzJl2mpo9HtQArwZzl312awnaRsqkzdU7/5GX5Bw7ZrJAN0Bxx94q25CZan3tKbjBRstcEEMuF/4XTgBoQZb8fs8aIb8X+7WZCNAbPVQvo+Q7/b6FJpixz2frLyMJqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGD17XvV9IZvV/jOU=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECoFvAfQkfm0cR4pzJl2mpo9HtQArwZzl312awnaRsqkzdU7/5GX5Bw7ZrJAN0Bxx94q25CZan3tKbjBRstcEEMuF/4XTgBoQZb8fs8aIb8X+7WZCNAbPVQvo+Q7/b6FJpixz2frLyMJqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGD17XvV9IZvV/jOU=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
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
    "channel_id": "ch_hVcq6uptd7ujpyRT6ray2QwurnU5WkWWraSg2FkD1JiyCFRd9",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
