
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3578%5Binitiator44initiator%5D
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
      "fsm_id": "ba_OfYIgpwytcuicxFs3XcRyj9ES8w7Xb0kpb0u33PVsaNsbvcp"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3578%5Binitiator44initiator%5D
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
      "fsm_id": "ba_VNugqO8FNJHfDHHOHLnTGjm3EqIaU4E8jEbM/FQ/QltzP3vb"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYQhzIJAA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423295,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBtKhth3pcwWifSFKPXBsP0o5TI1aV0eO8yjKj+QK1cI40nJiPiovA5btnJaR8sJASpZ3pdPgvxuDBuVFdg33gEuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGEP2AYxY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423295,
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_VNugqO8FNJHfDHHOHLnTGjm3EqIaU4E8jEbM/FQ/QltzP3vb"
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBtKhth3pcwWifSFKPXBsP0o5TI1aV0eO8yjKj+QK1cI40nJiPiovA5btnJaR8sJASpZ3pdPgvxuDBuVFdg33gEuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGEP2AYxY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423294,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAbSobYd6XMFon0hSj1wbD9KOUyNWldHjvMoyo/kCtXCONJyYj4qLwOW7ZyWkfLCQEqWd6XT4L8bgwblRXYN94BLhAoa2DiW3QhWsZG9u89kJtKw85cHMlo3xPeijRPZJbGwdPZc38xANXv01qlsKwNbONw/Xxssxy+Qin23U2SDYHBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhDeD4ll"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
  "id": -576460752303423294,
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAbSobYd6XMFon0hSj1wbD9KOUyNWldHjvMoyo/kCtXCONJyYj4qLwOW7ZyWkfLCQEqWd6XT4L8bgwblRXYN94BLhAoa2DiW3QhWsZG9u89kJtKw85cHMlo3xPeijRPZJbGwdPZc38xANXv01qlsKwNbONw/Xxssxy+Qin23U2SDYHBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhDeD4ll",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_OfYIgpwytcuicxFs3XcRyj9ES8w7Xb0kpb0u33PVsaNsbvcp"
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAbSobYd6XMFon0hSj1wbD9KOUyNWldHjvMoyo/kCtXCONJyYj4qLwOW7ZyWkfLCQEqWd6XT4L8bgwblRXYN94BLhAoa2DiW3QhWsZG9u89kJtKw85cHMlo3xPeijRPZJbGwdPZc38xANXv01qlsKwNbONw/Xxssxy+Qin23U2SDYHBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhDeD4ll",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbSobYd6XMFon0hSj1wbD9KOUyNWldHjvMoyo/kCtXCONJyYj4qLwOW7ZyWkfLCQEqWd6XT4L8bgwblRXYN94BLhAoa2DiW3QhWsZG9u89kJtKw85cHMlo3xPeijRPZJbGwdPZc38xANXv01qlsKwNbONw/Xxssxy+Qin23U2SDYHBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhDeD4ll",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbSobYd6XMFon0hSj1wbD9KOUyNWldHjvMoyo/kCtXCONJyYj4qLwOW7ZyWkfLCQEqWd6XT4L8bgwblRXYN94BLhAoa2DiW3QhWsZG9u89kJtKw85cHMlo3xPeijRPZJbGwdPZc38xANXv01qlsKwNbONw/Xxssxy+Qin23U2SDYHBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhDeD4ll",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "message": {
        "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "message": {
        "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
  "id": -576460752303423293,
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
  "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
  "id": -576460752303423293,
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "state": "tx_+QENCwH4hLhAbSobYd6XMFon0hSj1wbD9KOUyNWldHjvMoyo/kCtXCONJyYj4qLwOW7ZyWkfLCQEqWd6XT4L8bgwblRXYN94BLhAoa2DiW3QhWsZG9u89kJtKw85cHMlo3xPeijRPZJbGwdPZc38xANXv01qlsKwNbONw/Xxssxy+Qin23U2SDYHBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhDeD4ll"
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "state": "tx_+QENCwH4hLhAbSobYd6XMFon0hSj1wbD9KOUyNWldHjvMoyo/kCtXCONJyYj4qLwOW7ZyWkfLCQEqWd6XT4L8bgwblRXYN94BLhAoa2DiW3QhWsZG9u89kJtKw85cHMlo3xPeijRPZJbGwdPZc38xANXv01qlsKwNbONw/Xxssxy+Qin23U2SDYHBriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhDeD4ll"
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
  "id": -576460752303423292,
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
  "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
  "id": -576460752303423292,
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjHNNy0P5I8m9r1WX2bNgnxeVkHirD8O1y/RGJynpj9rAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyp1zbx8=",
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
  "id": -576460752303423291,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBSyEEW3f3eBKqW3nMn37fU3LWUuwMl5vsC6jPhEp5P6450eRDSS2xzx1eAKZOM1FzjEkwkZNjutE/X7lZsrdQNuEj4RjkCoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/awKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspAQtyv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
  "id": -576460752303423291,
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBSyEEW3f3eBKqW3nMn37fU3LWUuwMl5vsC6jPhEp5P6450eRDSS2xzx1eAKZOM1FzjEkwkZNjutE/X7lZsrdQNuEj4RjkCoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/awKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspAQtyv",
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
  "id": -576460752303423290,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBCU215ya32NxmANWOunTE30h0HZ51f5Xz+r6Pxcvikhxg9CYoNt6QZ5cbSiXbe2BDG3932L4oq2KkIgke3no0BuEBSyEEW3f3eBKqW3nMn37fU3LWUuwMl5vsC6jPhEp5P6450eRDSS2xzx1eAKZOM1FzjEkwkZNjutE/X7lZsrdQNuEj4RjkCoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/awKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspNbPYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
  "id": -576460752303423290,
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "state": "tx_+NILAfiEuEBCU215ya32NxmANWOunTE30h0HZ51f5Xz+r6Pxcvikhxg9CYoNt6QZ5cbSiXbe2BDG3932L4oq2KkIgke3no0BuEBSyEEW3f3eBKqW3nMn37fU3LWUuwMl5vsC6jPhEp5P6450eRDSS2xzx1eAKZOM1FzjEkwkZNjutE/X7lZsrdQNuEj4RjkCoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/awKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspNbPYS"
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "state": "tx_+NILAfiEuEBCU215ya32NxmANWOunTE30h0HZ51f5Xz+r6Pxcvikhxg9CYoNt6QZ5cbSiXbe2BDG3932L4oq2KkIgke3no0BuEBSyEEW3f3eBKqW3nMn37fU3LWUuwMl5vsC6jPhEp5P6450eRDSS2xzx1eAKZOM1FzjEkwkZNjutE/X7lZsrdQNuEj4RjkCoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/awKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspNbPYS"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423289,
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
  "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
  "id": -576460752303423289,
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
  "id": -576460752303423288,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
  "id": -576460752303423288,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBCU215ya32NxmANWOunTE30h0HZ51f5Xz+r6Pxcvikhxg9CYoNt6QZ5cbSiXbe2BDG3932L4oq2KkIgke3no0BuEBSyEEW3f3eBKqW3nMn37fU3LWUuwMl5vsC6jPhEp5P6450eRDSS2xzx1eAKZOM1FzjEkwkZNjutE/X7lZsrdQNuEj4RjkCoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/awKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspNbPYS",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBCU215ya32NxmANWOunTE30h0HZ51f5Xz+r6Pxcvikhxg9CYoNt6QZ5cbSiXbe2BDG3932L4oq2KkIgke3no0BuEBSyEEW3f3eBKqW3nMn37fU3LWUuwMl5vsC6jPhEp5P6450eRDSS2xzx1eAKZOM1FzjEkwkZNjutE/X7lZsrdQNuEj4RjkCoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/awKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspNbPYS",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBCU215ya32NxmANWOunTE30h0HZ51f5Xz+r6Pxcvikhxg9CYoNt6QZ5cbSiXbe2BDG3932L4oq2KkIgke3no0BuEBSyEEW3f3eBKqW3nMn37fU3LWUuwMl5vsC6jPhEp5P6450eRDSS2xzx1eAKZOM1FzjEkwkZNjutE/X7lZsrdQNuEj4RjkCoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/awKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspNbPYS",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
  "id": -576460752303423287,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
  "id": -576460752303423287,
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBjHNNy0P5I8m9r1WX2bNgnxeVkHirD8O1y/RGJynpj9roQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBCU215ya32NxmANWOunTE30h0HZ51f5Xz+r6Pxcvikhxg9CYoNt6QZ5cbSiXbe2BDG3932L4oq2KkIgke3no0BuEBSyEEW3f3eBKqW3nMn37fU3LWUuwMl5vsC6jPhEp5P6450eRDSS2xzx1eAKZOM1FzjEkwkZNjutE/X7lZsrdQNuEj4RjkCoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/awKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACGGR7ISegAEkwVJwk=",
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
    "signed_tx": "tx_+QLACwH4QrhAcvv+lmMfKuykuHDUCSCGc3gm3YkwC2CZ/upHJlws2QJsV5P62ugw15+Ctl6qdtJOPq9pBjGjyAchISoVKC4lCrkCd/kCdDcBoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/a6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAQlNtecmt9jcZgDVjrp0xN9IdB2edX+V8/q+j8XL4pIcYPQmKDbekGeXG0ol23tgQxt/d9i+KKtipCIJHt56NAbhAUshBFt393gSqlt5zJ9+31Ny1lLsDJeb7Auoz4RKeT+uOdHkQ0ktsc8dXgCmTjNRc4xJMJGTY7rRP1+5WbK3UDbhI+EY5AqEGMc03LQ/kjyb2vVZfZs2CfF5WQeKsPw7XL9EYnKemP2sCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoABK2zCgI"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAcvv+lmMfKuykuHDUCSCGc3gm3YkwC2CZ/upHJlws2QJsV5P62ugw15+Ctl6qdtJOPq9pBjGjyAchISoVKC4lCrkCd/kCdDcBoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/a6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAQlNtecmt9jcZgDVjrp0xN9IdB2edX+V8/q+j8XL4pIcYPQmKDbekGeXG0ol23tgQxt/d9i+KKtipCIJHt56NAbhAUshBFt393gSqlt5zJ9+31Ny1lLsDJeb7Auoz4RKeT+uOdHkQ0ktsc8dXgCmTjNRc4xJMJGTY7rRP1+5WbK3UDbhI+EY5AqEGMc03LQ/kjyb2vVZfZs2CfF5WQeKsPw7XL9EYnKemP2sCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoABK2zCgI",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAcvv+lmMfKuykuHDUCSCGc3gm3YkwC2CZ/upHJlws2QJsV5P62ugw15+Ctl6qdtJOPq9pBjGjyAchISoVKC4lCrkCd/kCdDcBoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/a6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAQlNtecmt9jcZgDVjrp0xN9IdB2edX+V8/q+j8XL4pIcYPQmKDbekGeXG0ol23tgQxt/d9i+KKtipCIJHt56NAbhAUshBFt393gSqlt5zJ9+31Ny1lLsDJeb7Auoz4RKeT+uOdHkQ0ktsc8dXgCmTjNRc4xJMJGTY7rRP1+5WbK3UDbhI+EY5AqEGMc03LQ/kjyb2vVZfZs2CfF5WQeKsPw7XL9EYnKemP2sCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoABK2zCgI",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBjHNNy0P5I8m9r1WX2bNgnxeVkHirD8O1y/RGJynpj9roQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAAGMsd+ew==",
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
    "signed_tx": "tx_+KcLAfhCuEBHn8RNUxy+sZfIRNriT/Wohn0SzeS4uHwuKwo8IaZfJF45w3lirTuTOznCmYgv4tEvGfbYl0eAgE0WaU9Yo+IIuF/4XTgBoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/a6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygABq17cco="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBHn8RNUxy+sZfIRNriT/Wohn0SzeS4uHwuKwo8IaZfJF45w3lirTuTOznCmYgv4tEvGfbYl0eAgE0WaU9Yo+IIuF/4XTgBoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/a6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygABq17cco=",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBHn8RNUxy+sZfIRNriT/Wohn0SzeS4uHwuKwo8IaZfJF45w3lirTuTOznCmYgv4tEvGfbYl0eAgE0WaU9Yo+IIuF/4XTgBoQYxzTctD+SPJva9Vl9mzYJ8XlZB4qw/Dtcv0Ricp6Y/a6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygABq17cco=",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
    "channel_id": "ch_Nw7hxSMfUc3EWfKD418gpBCGfuLoPfq2kqVxh5Rh684itHw9V",
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
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3578%5Binitiator44responder%5D
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
      "fsm_id": "ba_8uXqhI/t/IncOUUhbl6mvc6JcETFYmAucft68uO6sXJF8Ikr"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3578%5Binitiator44responder%5D
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
      "fsm_id": "ba_stttgI3Bc4d9FG7TeNKpigdEB95mANuTnt0yu8e9Lm5lxNe5"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYTgNXBnA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423286,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECXdSnTgwmndnv8Z23skz3JXS/Xx1D0PpthVb3YvR2a1BJqHMqGWs55wQFiPG50fHs7a3nl/U49GNQLjCUAVi0DuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGE7hcQ+s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423286,
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_stttgI3Bc4d9FG7TeNKpigdEB95mANuTnt0yu8e9Lm5lxNe5"
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECXdSnTgwmndnv8Z23skz3JXS/Xx1D0PpthVb3YvR2a1BJqHMqGWs55wQFiPG50fHs7a3nl/U49GNQLjCUAVi0DuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGE7hcQ+s=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423285,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhANLRfna9mN1ZRMeTutWqE+HOhf7jrrDtFnO75PEx7gXSg9MAvxO1uqSfchZ2RsQ5EhprZIPeUVHxBVHjPJBQ6ALhAl3Up04MJp3Z7/Gdt7JM9yV0v18dQ9D6bYVW92L0dmtQSahzKhlrOecEBYjxudHx7O2t55f1OPRjUC4wlAFYtA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhOp3cwt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
  "id": -576460752303423285,
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhANLRfna9mN1ZRMeTutWqE+HOhf7jrrDtFnO75PEx7gXSg9MAvxO1uqSfchZ2RsQ5EhprZIPeUVHxBVHjPJBQ6ALhAl3Up04MJp3Z7/Gdt7JM9yV0v18dQ9D6bYVW92L0dmtQSahzKhlrOecEBYjxudHx7O2t55f1OPRjUC4wlAFYtA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhOp3cwt",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_8uXqhI/t/IncOUUhbl6mvc6JcETFYmAucft68uO6sXJF8Ikr"
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhANLRfna9mN1ZRMeTutWqE+HOhf7jrrDtFnO75PEx7gXSg9MAvxO1uqSfchZ2RsQ5EhprZIPeUVHxBVHjPJBQ6ALhAl3Up04MJp3Z7/Gdt7JM9yV0v18dQ9D6bYVW92L0dmtQSahzKhlrOecEBYjxudHx7O2t55f1OPRjUC4wlAFYtA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhOp3cwt",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhANLRfna9mN1ZRMeTutWqE+HOhf7jrrDtFnO75PEx7gXSg9MAvxO1uqSfchZ2RsQ5EhprZIPeUVHxBVHjPJBQ6ALhAl3Up04MJp3Z7/Gdt7JM9yV0v18dQ9D6bYVW92L0dmtQSahzKhlrOecEBYjxudHx7O2t55f1OPRjUC4wlAFYtA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhOp3cwt",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhANLRfna9mN1ZRMeTutWqE+HOhf7jrrDtFnO75PEx7gXSg9MAvxO1uqSfchZ2RsQ5EhprZIPeUVHxBVHjPJBQ6ALhAl3Up04MJp3Z7/Gdt7JM9yV0v18dQ9D6bYVW92L0dmtQSahzKhlrOecEBYjxudHx7O2t55f1OPRjUC4wlAFYtA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhOp3cwt",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "message": {
        "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "message": {
        "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
  "id": -576460752303423284,
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
  "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
  "id": -576460752303423284,
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "state": "tx_+QENCwH4hLhANLRfna9mN1ZRMeTutWqE+HOhf7jrrDtFnO75PEx7gXSg9MAvxO1uqSfchZ2RsQ5EhprZIPeUVHxBVHjPJBQ6ALhAl3Up04MJp3Z7/Gdt7JM9yV0v18dQ9D6bYVW92L0dmtQSahzKhlrOecEBYjxudHx7O2t55f1OPRjUC4wlAFYtA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhOp3cwt"
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "state": "tx_+QENCwH4hLhANLRfna9mN1ZRMeTutWqE+HOhf7jrrDtFnO75PEx7gXSg9MAvxO1uqSfchZ2RsQ5EhprZIPeUVHxBVHjPJBQ6ALhAl3Up04MJp3Z7/Gdt7JM9yV0v18dQ9D6bYVW92L0dmtQSahzKhlrOecEBYjxudHx7O2t55f1OPRjUC4wlAFYtA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhOp3cwt"
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
  "id": -576460752303423283,
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
  "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
  "id": -576460752303423283,
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuB+LEnoQwlVG7BfirKNlr8womsf61C0NqdEbBExlVM8AqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyo0Bx+4=",
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
  "id": -576460752303423282,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBPMVpdpeGvEA3pEV3Q8VbzAVnfcHQNDpLrLbi9Ha6eEWxzWfnNHWnzztNDTwBILX56gj1jbKRJSNsUPDNV3hUPuEj4RjkCoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspSGjPj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
  "id": -576460752303423282,
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBPMVpdpeGvEA3pEV3Q8VbzAVnfcHQNDpLrLbi9Ha6eEWxzWfnNHWnzztNDTwBILX56gj1jbKRJSNsUPDNV3hUPuEj4RjkCoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspSGjPj",
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
  "id": -576460752303423281,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBPMVpdpeGvEA3pEV3Q8VbzAVnfcHQNDpLrLbi9Ha6eEWxzWfnNHWnzztNDTwBILX56gj1jbKRJSNsUPDNV3hUPuEDzutqOF8iaTjmU9PmAoFUcK2CCy5pyphJ9Jj1jMvZy0hhWdpCNv0p3p5FsDKwkAHPwnYDfqvdBOu11tq6DrF0EuEj4RjkCoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspodnFi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
  "id": -576460752303423281,
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "state": "tx_+NILAfiEuEBPMVpdpeGvEA3pEV3Q8VbzAVnfcHQNDpLrLbi9Ha6eEWxzWfnNHWnzztNDTwBILX56gj1jbKRJSNsUPDNV3hUPuEDzutqOF8iaTjmU9PmAoFUcK2CCy5pyphJ9Jj1jMvZy0hhWdpCNv0p3p5FsDKwkAHPwnYDfqvdBOu11tq6DrF0EuEj4RjkCoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspodnFi"
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "state": "tx_+NILAfiEuEBPMVpdpeGvEA3pEV3Q8VbzAVnfcHQNDpLrLbi9Ha6eEWxzWfnNHWnzztNDTwBILX56gj1jbKRJSNsUPDNV3hUPuEDzutqOF8iaTjmU9PmAoFUcK2CCy5pyphJ9Jj1jMvZy0hhWdpCNv0p3p5FsDKwkAHPwnYDfqvdBOu11tq6DrF0EuEj4RjkCoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspodnFi"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423280,
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
  "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
  "id": -576460752303423280,
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
  "id": -576460752303423279,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
  "id": -576460752303423279,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBPMVpdpeGvEA3pEV3Q8VbzAVnfcHQNDpLrLbi9Ha6eEWxzWfnNHWnzztNDTwBILX56gj1jbKRJSNsUPDNV3hUPuEDzutqOF8iaTjmU9PmAoFUcK2CCy5pyphJ9Jj1jMvZy0hhWdpCNv0p3p5FsDKwkAHPwnYDfqvdBOu11tq6DrF0EuEj4RjkCoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspodnFi",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBPMVpdpeGvEA3pEV3Q8VbzAVnfcHQNDpLrLbi9Ha6eEWxzWfnNHWnzztNDTwBILX56gj1jbKRJSNsUPDNV3hUPuEDzutqOF8iaTjmU9PmAoFUcK2CCy5pyphJ9Jj1jMvZy0hhWdpCNv0p3p5FsDKwkAHPwnYDfqvdBOu11tq6DrF0EuEj4RjkCoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspodnFi",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBPMVpdpeGvEA3pEV3Q8VbzAVnfcHQNDpLrLbi9Ha6eEWxzWfnNHWnzztNDTwBILX56gj1jbKRJSNsUPDNV3hUPuEDzutqOF8iaTjmU9PmAoFUcK2CCy5pyphJ9Jj1jMvZy0hhWdpCNv0p3p5FsDKwkAHPwnYDfqvdBOu11tq6DrF0EuEj4RjkCoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspodnFi",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
  "id": -576460752303423278,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
  "id": -576460752303423278,
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBuB+LEnoQwlVG7BfirKNlr8womsf61C0NqdEbBExlVM8oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEBPMVpdpeGvEA3pEV3Q8VbzAVnfcHQNDpLrLbi9Ha6eEWxzWfnNHWnzztNDTwBILX56gj1jbKRJSNsUPDNV3hUPuEDzutqOF8iaTjmU9PmAoFUcK2CCy5pyphJ9Jj1jMvZy0hhWdpCNv0p3p5FsDKwkAHPwnYDfqvdBOu11tq6DrF0EuEj4RjkCoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACGGR7ISegAB75jQV8=",
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
    "signed_tx": "tx_+QLACwH4QrhAGxHLhXIYOQ19rBOnC1SbQ6ZwZj7CEm0iUax9Sympr5qTztotrXsrkuQIZ9C3161hFviF19x2FtYJi4WR6CJJBrkCd/kCdDcBoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhATzFaXaXhrxAN6RFd0PFW8wFZ33B0DQ6S6y24vR2unhFsc1n5zR1p887TQ08ASC1+eoI9Y2ykSUjbFDwzVd4VD7hA87rajhfImk45lPT5gKBVHCtggsuacqYSfSY9YzL2ctIYVnaQjb9Kd6eRbAysJABz8J2A36r3QTrtdbaug6xdBLhI+EY5AqEG4H4sSehDCVUbsF+Kso2WvzCiax/rULQ2p0RsETGVUzwCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoAAd27dFv"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAGxHLhXIYOQ19rBOnC1SbQ6ZwZj7CEm0iUax9Sympr5qTztotrXsrkuQIZ9C3161hFviF19x2FtYJi4WR6CJJBrkCd/kCdDcBoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhATzFaXaXhrxAN6RFd0PFW8wFZ33B0DQ6S6y24vR2unhFsc1n5zR1p887TQ08ASC1+eoI9Y2ykSUjbFDwzVd4VD7hA87rajhfImk45lPT5gKBVHCtggsuacqYSfSY9YzL2ctIYVnaQjb9Kd6eRbAysJABz8J2A36r3QTrtdbaug6xdBLhI+EY5AqEG4H4sSehDCVUbsF+Kso2WvzCiax/rULQ2p0RsETGVUzwCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoAAd27dFv",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAGxHLhXIYOQ19rBOnC1SbQ6ZwZj7CEm0iUax9Sympr5qTztotrXsrkuQIZ9C3161hFviF19x2FtYJi4WR6CJJBrkCd/kCdDcBoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhATzFaXaXhrxAN6RFd0PFW8wFZ33B0DQ6S6y24vR2unhFsc1n5zR1p887TQ08ASC1+eoI9Y2ykSUjbFDwzVd4VD7hA87rajhfImk45lPT5gKBVHCtggsuacqYSfSY9YzL2ctIYVnaQjb9Kd6eRbAysJABz8J2A36r3QTrtdbaug6xdBLhI+EY5AqEG4H4sSehDCVUbsF+Kso2WvzCiax/rULQ2p0RsETGVUzwCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoAAd27dFv",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBuB+LEnoQwlVG7BfirKNlr8womsf61C0NqdEbBExlVM8oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAAISFmvKw==",
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
    "signed_tx": "tx_+KcLAfhCuECE+JzKxYxwTD6qzZZCs+E9Y8P3Iqi5QeeTKqqty8P5A+6/MjOeCkXZ8a1ZR4b6Xqufc+y6RTHl6ka9XmsM3aQOuF/4XTgBoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygACHrnDZY="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECE+JzKxYxwTD6qzZZCs+E9Y8P3Iqi5QeeTKqqty8P5A+6/MjOeCkXZ8a1ZR4b6Xqufc+y6RTHl6ka9XmsM3aQOuF/4XTgBoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygACHrnDZY=",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECE+JzKxYxwTD6qzZZCs+E9Y8P3Iqi5QeeTKqqty8P5A+6/MjOeCkXZ8a1ZR4b6Xqufc+y6RTHl6ka9XmsM3aQOuF/4XTgBoQbgfixJ6EMJVRuwX4qyjZa/MKJrH+tQtDanRGwRMZVTPKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygACHrnDZY=",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
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
    "channel_id": "ch_2hsNPxADhK7wJLKqaFw4oWmdzzAcB1AaPxiaVF1T1T7F7ZSa8V",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
