
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
      "fsm_id": "ba_/EBnX58mWSUUQzB9ZLTTXMRV1F3FT4/UnKpa0YlUQbHJw0fs"
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
      "fsm_id": "ba_B0IUgBX9e5YxiW1GF5QeLvfCvmuowB3w/ot049R/GiGyB8p6"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ1hAkoPw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422427,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB3ZIhI1Zkk5mSMoboKV8DqztXHJhth77lFONHn+g/uTi/eoTLqwa5RL4bgUY9R5Div0STdxxLtWX5NGXpQWDsEuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGdXQQ75s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422427,
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_B0IUgBX9e5YxiW1GF5QeLvfCvmuowB3w/ot049R/GiGyB8p6"
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEB3ZIhI1Zkk5mSMoboKV8DqztXHJhth77lFONHn+g/uTi/eoTLqwa5RL4bgUY9R5Div0STdxxLtWX5NGXpQWDsEuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGdXQQ75s=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422426,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAGVYwXiEPEk30478WiKu5lHjqLJwr0E99+saPEnLj5vVqtIqXzu2DfnYXDyQe9dg0FPT1GZuq9DlaYbRvPVlNBLhAd2SISNWZJOZkjKG6ClfA6s7VxyYbYe+5RTjR5/oP7k4v3qEy6sGuUS+G4FGPUeQ4r9Ek3ccS7Vl+TRl6UFg7BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnWcNZty"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
  "id": -576460752303422426,
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAGVYwXiEPEk30478WiKu5lHjqLJwr0E99+saPEnLj5vVqtIqXzu2DfnYXDyQe9dg0FPT1GZuq9DlaYbRvPVlNBLhAd2SISNWZJOZkjKG6ClfA6s7VxyYbYe+5RTjR5/oP7k4v3qEy6sGuUS+G4FGPUeQ4r9Ek3ccS7Vl+TRl6UFg7BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnWcNZty",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_/EBnX58mWSUUQzB9ZLTTXMRV1F3FT4/UnKpa0YlUQbHJw0fs"
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAGVYwXiEPEk30478WiKu5lHjqLJwr0E99+saPEnLj5vVqtIqXzu2DfnYXDyQe9dg0FPT1GZuq9DlaYbRvPVlNBLhAd2SISNWZJOZkjKG6ClfA6s7VxyYbYe+5RTjR5/oP7k4v3qEy6sGuUS+G4FGPUeQ4r9Ek3ccS7Vl+TRl6UFg7BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnWcNZty",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGVYwXiEPEk30478WiKu5lHjqLJwr0E99+saPEnLj5vVqtIqXzu2DfnYXDyQe9dg0FPT1GZuq9DlaYbRvPVlNBLhAd2SISNWZJOZkjKG6ClfA6s7VxyYbYe+5RTjR5/oP7k4v3qEy6sGuUS+G4FGPUeQ4r9Ek3ccS7Vl+TRl6UFg7BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnWcNZty",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGVYwXiEPEk30478WiKu5lHjqLJwr0E99+saPEnLj5vVqtIqXzu2DfnYXDyQe9dg0FPT1GZuq9DlaYbRvPVlNBLhAd2SISNWZJOZkjKG6ClfA6s7VxyYbYe+5RTjR5/oP7k4v3qEy6sGuUS+G4FGPUeQ4r9Ek3ccS7Vl+TRl6UFg7BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnWcNZty",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "message": {
        "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "message": {
        "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
  "id": -576460752303422425,
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
  "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
  "id": -576460752303422425,
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "state": "tx_+QENCwH4hLhAGVYwXiEPEk30478WiKu5lHjqLJwr0E99+saPEnLj5vVqtIqXzu2DfnYXDyQe9dg0FPT1GZuq9DlaYbRvPVlNBLhAd2SISNWZJOZkjKG6ClfA6s7VxyYbYe+5RTjR5/oP7k4v3qEy6sGuUS+G4FGPUeQ4r9Ek3ccS7Vl+TRl6UFg7BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnWcNZty"
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "state": "tx_+QENCwH4hLhAGVYwXiEPEk30478WiKu5lHjqLJwr0E99+saPEnLj5vVqtIqXzu2DfnYXDyQe9dg0FPT1GZuq9DlaYbRvPVlNBLhAd2SISNWZJOZkjKG6ClfA6s7VxyYbYe+5RTjR5/oP7k4v3qEy6sGuUS+G4FGPUeQ4r9Ek3ccS7Vl+TRl6UFg7BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnWcNZty"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAiWN1V"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422424,
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
  "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
  "id": -576460752303422424,
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBq9NqN93pv1/SQlsaH75cUM+6ZeSvf7gXnoQbnhpNcT3AqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyp7OEW4=",
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
  "id": -576460752303422423,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED0sqVr/bm47r3KY0uXZf2g5OHaFjq4UIBgyd6CEvrczOuqi8hyrHrX1ibHpr6vJL3BiqUvKVFp7kVYxWlXI7IDuEj4RjkCoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE9wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqWBs7L"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
  "id": -576460752303422423,
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "signed_tx": "tx_+JALAfhCuED0sqVr/bm47r3KY0uXZf2g5OHaFjq4UIBgyd6CEvrczOuqi8hyrHrX1ibHpr6vJL3BiqUvKVFp7kVYxWlXI7IDuEj4RjkCoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE9wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqWBs7L",
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
  "id": -576460752303422422,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuED0sqVr/bm47r3KY0uXZf2g5OHaFjq4UIBgyd6CEvrczOuqi8hyrHrX1ibHpr6vJL3BiqUvKVFp7kVYxWlXI7IDuED3jL4tEBZ89cNZ5H5YJ8jn4+V6C1RcnfiTRm2tOXnTlYxxIN2qZQ4DArIVDibYxDZYvkjTZCeayPbyvHyn52oHuEj4RjkCoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE9wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqT/vgU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
  "id": -576460752303422422,
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "state": "tx_+NILAfiEuED0sqVr/bm47r3KY0uXZf2g5OHaFjq4UIBgyd6CEvrczOuqi8hyrHrX1ibHpr6vJL3BiqUvKVFp7kVYxWlXI7IDuED3jL4tEBZ89cNZ5H5YJ8jn4+V6C1RcnfiTRm2tOXnTlYxxIN2qZQ4DArIVDibYxDZYvkjTZCeayPbyvHyn52oHuEj4RjkCoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE9wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqT/vgU"
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "state": "tx_+NILAfiEuED0sqVr/bm47r3KY0uXZf2g5OHaFjq4UIBgyd6CEvrczOuqi8hyrHrX1ibHpr6vJL3BiqUvKVFp7kVYxWlXI7IDuED3jL4tEBZ89cNZ5H5YJ8jn4+V6C1RcnfiTRm2tOXnTlYxxIN2qZQ4DArIVDibYxDZYvkjTZCeayPbyvHyn52oHuEj4RjkCoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE9wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqT/vgU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422421,
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
  "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
  "id": -576460752303422421,
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
  "id": -576460752303422420,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
  "id": -576460752303422420,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuED0sqVr/bm47r3KY0uXZf2g5OHaFjq4UIBgyd6CEvrczOuqi8hyrHrX1ibHpr6vJL3BiqUvKVFp7kVYxWlXI7IDuED3jL4tEBZ89cNZ5H5YJ8jn4+V6C1RcnfiTRm2tOXnTlYxxIN2qZQ4DArIVDibYxDZYvkjTZCeayPbyvHyn52oHuEj4RjkCoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE9wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqT/vgU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuED0sqVr/bm47r3KY0uXZf2g5OHaFjq4UIBgyd6CEvrczOuqi8hyrHrX1ibHpr6vJL3BiqUvKVFp7kVYxWlXI7IDuED3jL4tEBZ89cNZ5H5YJ8jn4+V6C1RcnfiTRm2tOXnTlYxxIN2qZQ4DArIVDibYxDZYvkjTZCeayPbyvHyn52oHuEj4RjkCoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE9wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqT/vgU",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuED0sqVr/bm47r3KY0uXZf2g5OHaFjq4UIBgyd6CEvrczOuqi8hyrHrX1ibHpr6vJL3BiqUvKVFp7kVYxWlXI7IDuED3jL4tEBZ89cNZ5H5YJ8jn4+V6C1RcnfiTRm2tOXnTlYxxIN2qZQ4DArIVDibYxDZYvkjTZCeayPbyvHyn52oHuEj4RjkCoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE9wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqT/vgU",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
  "id": -576460752303422419,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
  "id": -576460752303422419,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBq9NqN93pv1/SQlsaH75cUM+6ZeSvf7gXnoQbnhpNcT3oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuED0sqVr/bm47r3KY0uXZf2g5OHaFjq4UIBgyd6CEvrczOuqi8hyrHrX1ibHpr6vJL3BiqUvKVFp7kVYxWlXI7IDuED3jL4tEBZ89cNZ5H5YJ8jn4+V6C1RcnfiTRm2tOXnTlYxxIN2qZQ4DArIVDibYxDZYvkjTZCeayPbyvHyn52oHuEj4RjkCoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE9wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACG4JEMNh5+dwZcGRM=",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAcoBUtgNIBZC2UnT+ED6BFNSijtGfBV/wp6tswvK+iaGgSjuwY5xQ0h7X/Dlnq+JUw+ywHMFLEMXNwiXOvoFODbkCd/kCdDcBoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE96EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhA9LKla/25uO69ymNLl2X9oOTh2hY6uFCAYMneghL63MzrqovIcqx619Ymx6a+ryS9wYqlLylRae5FWMVpVyOyA7hA94y+LRAWfPXDWeR+WCfI5+PlegtUXJ34k0ZtrTl505WMcSDdqmUOAwKyFQ4m2MQ2WL5I02Qnmsj28rx8p+dqB7hI+EY5AqEGr02o33em/X9JCWxofvlxQz7pl5K9/uBeehBueGk1xPcCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhuCRDDYefndUR89T"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAcoBUtgNIBZC2UnT+ED6BFNSijtGfBV/wp6tswvK+iaGgSjuwY5xQ0h7X/Dlnq+JUw+ywHMFLEMXNwiXOvoFODbkCd/kCdDcBoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE96EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhA9LKla/25uO69ymNLl2X9oOTh2hY6uFCAYMneghL63MzrqovIcqx619Ymx6a+ryS9wYqlLylRae5FWMVpVyOyA7hA94y+LRAWfPXDWeR+WCfI5+PlegtUXJ34k0ZtrTl505WMcSDdqmUOAwKyFQ4m2MQ2WL5I02Qnmsj28rx8p+dqB7hI+EY5AqEGr02o33em/X9JCWxofvlxQz7pl5K9/uBeehBueGk1xPcCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhuCRDDYefndUR89T",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAcoBUtgNIBZC2UnT+ED6BFNSijtGfBV/wp6tswvK+iaGgSjuwY5xQ0h7X/Dlnq+JUw+ywHMFLEMXNwiXOvoFODbkCd/kCdDcBoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE96EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhA9LKla/25uO69ymNLl2X9oOTh2hY6uFCAYMneghL63MzrqovIcqx619Ymx6a+ryS9wYqlLylRae5FWMVpVyOyA7hA94y+LRAWfPXDWeR+WCfI5+PlegtUXJ34k0ZtrTl505WMcSDdqmUOAwKyFQ4m2MQ2WL5I02Qnmsj28rx8p+dqB7hI+EY5AqEGr02o33em/X9JCWxofvlxQz7pl5K9/uBeehBueGk1xPcCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhuCRDDYefndUR89T",
      "type": "channel_slash_tx"
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBq9NqN93pv1/SQlsaH75cUM+6ZeSvf7gXnoQbnhpNcT3oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAAxvkXkWg==",
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
    "signed_tx": "tx_+KcLAfhCuEDTySE/tYANxQAr8Rb+Ad+zT5GpeQJyZ60oQR0GdYqHNX39oDwLezKQdtuJSJXlf1zuwBK0rhjTNlqrduWjlc4FuF/4XTgBoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE96EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAMRAhy6Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDTySE/tYANxQAr8Rb+Ad+zT5GpeQJyZ60oQR0GdYqHNX39oDwLezKQdtuJSJXlf1zuwBK0rhjTNlqrduWjlc4FuF/4XTgBoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE96EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAMRAhy6Q=",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDTySE/tYANxQAr8Rb+Ad+zT5GpeQJyZ60oQR0GdYqHNX39oDwLezKQdtuJSJXlf1zuwBK0rhjTNlqrduWjlc4FuF/4XTgBoQavTajfd6b9f0kJbGh++XFDPumXkr3+4F56EG54aTXE96EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAMRAhy6Q=",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
    "channel_id": "ch_2LCtZbS2nCJBUofkxSaTxBukLncohFaqKJbCWxQuSDd4yaeUHd",
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
      "fsm_id": "ba_5WO1wQj5c+LvYvAVcyLZlm+ZPCIrtIdF3tiUI610SetMzbH2"
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
      "fsm_id": "ba_Te2mtZ1Qa9YWCB8kV8EOn8VBclVcCuT59391X7lm4Z7IjT6o"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ4JOcktw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422418,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECTfFWEijk7HAKgacSvO/fBt84JpzYLIC4rKvSrryUL0zIwFGypAtMh8WRhkJ0ZVlf6uBhWGjP5S3OYGh/tsG0HuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGePdZ44M="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422418,
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_Te2mtZ1Qa9YWCB8kV8EOn8VBclVcCuT59391X7lm4Z7IjT6o"
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECTfFWEijk7HAKgacSvO/fBt84JpzYLIC4rKvSrryUL0zIwFGypAtMh8WRhkJ0ZVlf6uBhWGjP5S3OYGh/tsG0HuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGePdZ44M=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422417,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAk3xVhIo5OxwCoGnErzv3wbfOCac2CyAuKyr0q68lC9MyMBRsqQLTIfFkYZCdGVZX+rgYVhoz+UtzmBof7bBtB7hA5HGNi9URDeZOhXqvmO8j/pHPoMdM/hiT13OL95SPwSJkgYf1FzghMln/3Zj5KBvK/meyjWJAex99QBwfhmOUA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnhIDx3X"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
  "id": -576460752303422417,
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAk3xVhIo5OxwCoGnErzv3wbfOCac2CyAuKyr0q68lC9MyMBRsqQLTIfFkYZCdGVZX+rgYVhoz+UtzmBof7bBtB7hA5HGNi9URDeZOhXqvmO8j/pHPoMdM/hiT13OL95SPwSJkgYf1FzghMln/3Zj5KBvK/meyjWJAex99QBwfhmOUA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnhIDx3X",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_5WO1wQj5c+LvYvAVcyLZlm+ZPCIrtIdF3tiUI610SetMzbH2"
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAk3xVhIo5OxwCoGnErzv3wbfOCac2CyAuKyr0q68lC9MyMBRsqQLTIfFkYZCdGVZX+rgYVhoz+UtzmBof7bBtB7hA5HGNi9URDeZOhXqvmO8j/pHPoMdM/hiT13OL95SPwSJkgYf1FzghMln/3Zj5KBvK/meyjWJAex99QBwfhmOUA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnhIDx3X",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAk3xVhIo5OxwCoGnErzv3wbfOCac2CyAuKyr0q68lC9MyMBRsqQLTIfFkYZCdGVZX+rgYVhoz+UtzmBof7bBtB7hA5HGNi9URDeZOhXqvmO8j/pHPoMdM/hiT13OL95SPwSJkgYf1FzghMln/3Zj5KBvK/meyjWJAex99QBwfhmOUA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnhIDx3X",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAk3xVhIo5OxwCoGnErzv3wbfOCac2CyAuKyr0q68lC9MyMBRsqQLTIfFkYZCdGVZX+rgYVhoz+UtzmBof7bBtB7hA5HGNi9URDeZOhXqvmO8j/pHPoMdM/hiT13OL95SPwSJkgYf1FzghMln/3Zj5KBvK/meyjWJAex99QBwfhmOUA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnhIDx3X",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "message": {
        "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "message": {
        "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
  "id": -576460752303422416,
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
  "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
  "id": -576460752303422416,
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "state": "tx_+QENCwH4hLhAk3xVhIo5OxwCoGnErzv3wbfOCac2CyAuKyr0q68lC9MyMBRsqQLTIfFkYZCdGVZX+rgYVhoz+UtzmBof7bBtB7hA5HGNi9URDeZOhXqvmO8j/pHPoMdM/hiT13OL95SPwSJkgYf1FzghMln/3Zj5KBvK/meyjWJAex99QBwfhmOUA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnhIDx3X"
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "state": "tx_+QENCwH4hLhAk3xVhIo5OxwCoGnErzv3wbfOCac2CyAuKyr0q68lC9MyMBRsqQLTIfFkYZCdGVZX+rgYVhoz+UtzmBof7bBtB7hA5HGNi9URDeZOhXqvmO8j/pHPoMdM/hiT13OL95SPwSJkgYf1FzghMln/3Zj5KBvK/meyjWJAex99QBwfhmOUA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnhIDx3X"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAiWN1V"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422415,
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
  "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
  "id": -576460752303422415,
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmusC+4C6AARqPTF9pYt+os2hi+qpa5QhMaGEFbF3n/LAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyoKGJKE=",
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
  "id": -576460752303422414,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBilC+lChva+WCbx+yhwUdmUv3yS3McJBprzTD2tgmnoacpdXjLP+7osaCGlt3ij8AQKLodujiM16gVRVkDfcMFuEj4RjkCoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/ywKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspUNm7q"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
  "id": -576460752303422414,
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBilC+lChva+WCbx+yhwUdmUv3yS3McJBprzTD2tgmnoacpdXjLP+7osaCGlt3ij8AQKLodujiM16gVRVkDfcMFuEj4RjkCoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/ywKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspUNm7q",
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
  "id": -576460752303422413,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBilC+lChva+WCbx+yhwUdmUv3yS3McJBprzTD2tgmnoacpdXjLP+7osaCGlt3ij8AQKLodujiM16gVRVkDfcMFuEDkXGwjTi6DGWDfrjHDGDn/ILGN7Jjn9CMM1Ch7Nhwt5ddeogyVi2JGb1hA/od5mMqIfT9juLMKMBvGyQwIvugBuEj4RjkCoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/ywKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2q3wF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
  "id": -576460752303422413,
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "state": "tx_+NILAfiEuEBilC+lChva+WCbx+yhwUdmUv3yS3McJBprzTD2tgmnoacpdXjLP+7osaCGlt3ij8AQKLodujiM16gVRVkDfcMFuEDkXGwjTi6DGWDfrjHDGDn/ILGN7Jjn9CMM1Ch7Nhwt5ddeogyVi2JGb1hA/od5mMqIfT9juLMKMBvGyQwIvugBuEj4RjkCoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/ywKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2q3wF"
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "state": "tx_+NILAfiEuEBilC+lChva+WCbx+yhwUdmUv3yS3McJBprzTD2tgmnoacpdXjLP+7osaCGlt3ij8AQKLodujiM16gVRVkDfcMFuEDkXGwjTi6DGWDfrjHDGDn/ILGN7Jjn9CMM1Ch7Nhwt5ddeogyVi2JGb1hA/od5mMqIfT9juLMKMBvGyQwIvugBuEj4RjkCoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/ywKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2q3wF"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422412,
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
  "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
  "id": -576460752303422412,
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
  "id": -576460752303422411,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
  "id": -576460752303422411,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBilC+lChva+WCbx+yhwUdmUv3yS3McJBprzTD2tgmnoacpdXjLP+7osaCGlt3ij8AQKLodujiM16gVRVkDfcMFuEDkXGwjTi6DGWDfrjHDGDn/ILGN7Jjn9CMM1Ch7Nhwt5ddeogyVi2JGb1hA/od5mMqIfT9juLMKMBvGyQwIvugBuEj4RjkCoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/ywKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2q3wF",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBilC+lChva+WCbx+yhwUdmUv3yS3McJBprzTD2tgmnoacpdXjLP+7osaCGlt3ij8AQKLodujiM16gVRVkDfcMFuEDkXGwjTi6DGWDfrjHDGDn/ILGN7Jjn9CMM1Ch7Nhwt5ddeogyVi2JGb1hA/od5mMqIfT9juLMKMBvGyQwIvugBuEj4RjkCoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/ywKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2q3wF",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBilC+lChva+WCbx+yhwUdmUv3yS3McJBprzTD2tgmnoacpdXjLP+7osaCGlt3ij8AQKLodujiM16gVRVkDfcMFuEDkXGwjTi6DGWDfrjHDGDn/ILGN7Jjn9CMM1Ch7Nhwt5ddeogyVi2JGb1hA/od5mMqIfT9juLMKMBvGyQwIvugBuEj4RjkCoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/ywKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2q3wF",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
  "id": -576460752303422410,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
  "id": -576460752303422410,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBmusC+4C6AARqPTF9pYt+os2hi+qpa5QhMaGEFbF3n/LoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEBilC+lChva+WCbx+yhwUdmUv3yS3McJBprzTD2tgmnoacpdXjLP+7osaCGlt3ij8AQKLodujiM16gVRVkDfcMFuEDkXGwjTi6DGWDfrjHDGDn/ILGN7Jjn9CMM1Ch7Nhwt5ddeogyVi2JGb1hA/od5mMqIfT9juLMKMBvGyQwIvugBuEj4RjkCoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/ywKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACG4JEMNh5+Mo78iRM=",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAAho/pWltDvU1jZGvbSSHy6DBWpiLnjr+KOqqn3Xx5B9iF4onr0iXVhogIowA6UxTVwrnOdylc97fqDK0RyuDDLkCd/kCdDcBoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/y6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAYpQvpQob2vlgm8fsocFHZlL98ktzHCQaa80w9rYJp6GnKXV4yz/u6LGghpbd4o/AECi6Hbo4jNeoFUVZA33DBbhA5FxsI04ugxlg364xwxg5/yCxjeyY5/QjDNQoezYcLeXXXqIMlYtiRm9YQP6HeZjKiH0/Y7izCjAbxskMCL7oAbhI+EY5AqEGa6wL7gLoABGo9MX2li36izaGL6qlrlCExoYQVsXef8sCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhuCRDDYefjImDW4G"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAAho/pWltDvU1jZGvbSSHy6DBWpiLnjr+KOqqn3Xx5B9iF4onr0iXVhogIowA6UxTVwrnOdylc97fqDK0RyuDDLkCd/kCdDcBoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/y6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAYpQvpQob2vlgm8fsocFHZlL98ktzHCQaa80w9rYJp6GnKXV4yz/u6LGghpbd4o/AECi6Hbo4jNeoFUVZA33DBbhA5FxsI04ugxlg364xwxg5/yCxjeyY5/QjDNQoezYcLeXXXqIMlYtiRm9YQP6HeZjKiH0/Y7izCjAbxskMCL7oAbhI+EY5AqEGa6wL7gLoABGo9MX2li36izaGL6qlrlCExoYQVsXef8sCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhuCRDDYefjImDW4G",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAAho/pWltDvU1jZGvbSSHy6DBWpiLnjr+KOqqn3Xx5B9iF4onr0iXVhogIowA6UxTVwrnOdylc97fqDK0RyuDDLkCd/kCdDcBoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/y6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAYpQvpQob2vlgm8fsocFHZlL98ktzHCQaa80w9rYJp6GnKXV4yz/u6LGghpbd4o/AECi6Hbo4jNeoFUVZA33DBbhA5FxsI04ugxlg364xwxg5/yCxjeyY5/QjDNQoezYcLeXXXqIMlYtiRm9YQP6HeZjKiH0/Y7izCjAbxskMCL7oAbhI+EY5AqEGa6wL7gLoABGo9MX2li36izaGL6qlrlCExoYQVsXef8sCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhuCRDDYefjImDW4G",
      "type": "channel_slash_tx"
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBmusC+4C6AARqPTF9pYt+os2hi+qpa5QhMaGEFbF3n/LoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAAzUbN4hw==",
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
    "signed_tx": "tx_+KcLAfhCuEDZ79s5UxQqqrr7D5IbYO8RpHyR5/dCCBjcnLqWQ2yZJcZ/AVVgM8hB8SD7uq50p9qszezNAGr9kjDxVZB5vV4KuF/4XTgBoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/y6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAM0NMd+Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDZ79s5UxQqqrr7D5IbYO8RpHyR5/dCCBjcnLqWQ2yZJcZ/AVVgM8hB8SD7uq50p9qszezNAGr9kjDxVZB5vV4KuF/4XTgBoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/y6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAM0NMd+Q=",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDZ79s5UxQqqrr7D5IbYO8RpHyR5/dCCBjcnLqWQ2yZJcZ/AVVgM8hB8SD7uq50p9qszezNAGr9kjDxVZB5vV4KuF/4XTgBoQZrrAvuAugAEaj0xfaWLfqLNoYvqqWuUITGhhBWxd5/y6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAM0NMd+Q=",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
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
    "channel_id": "ch_pRLcf6Tk6KXvL9DKB4WXjp9Y1LP54Mg8gfx7n5KtiWVaLsNNd",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
