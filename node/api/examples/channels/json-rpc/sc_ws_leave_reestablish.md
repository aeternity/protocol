
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish%2F3734
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
      "fsm_id": "ba_ixiBsqQuOCrif1Jj0YEgC2q1ooMLqzE2pv7YM0t6kFs5V2sB"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish%2F3734
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
      "fsm_id": "ba_5aWi/kLQgPTsMmQEmEh2x8H57c58Bu3UDaZCjE561r5fN2Av"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYV7ZzQ0Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423277,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDuga9DpMa2EQhkVWyae//evKbln5izM6BVyH/lUVLRhHEjl6Ljg+YNmsr/d83mPEhi3hFLNqdsbnfoy+QNCZ4LuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGFRmoa3w="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423277,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_5aWi/kLQgPTsMmQEmEh2x8H57c58Bu3UDaZCjE561r5fN2Av"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDuga9DpMa2EQhkVWyae//evKbln5izM6BVyH/lUVLRhHEjl6Ljg+YNmsr/d83mPEhi3hFLNqdsbnfoy+QNCZ4LuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGFRmoa3w=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423276,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423276,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_ixiBsqQuOCrif1Jj0YEgC2q1ooMLqzE2pv7YM0t6kFs5V2sB"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "message": {
        "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "message": {
        "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "id": -576460752303423275,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423275,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP&existing_fsm_id=ba_5aWi%2FkLQgPTsMmQEmEh2x8H57c58Bu3UDaZCjE561r5fN2Av&offchain_tx=tx_%2BQENCwH4hLhAGEur%2B3%2BbEGdpyurvuD5EN00%2B5ksGtadY4N31YE%2Bmq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv%2F3rym5Z%2BYszOgVch%2F5VFS0YRxI5ei44PmDZrK%2F3fN5jxIYt4RSzanbG536MvkDQmeC7iD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhVsqt1P&port=13180&protocol=json-rpc&role=responder
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
      "fsm_id": "ba_iF+PzjWoYoNiab/u5M5fkdWF3AILtp/pWdZNeA0Y3rvkdXex"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP&existing_fsm_id=ba_ixiBsqQuOCrif1Jj0YEgC2q1ooMLqzE2pv7YM0t6kFs5V2sB&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAGEur%2B3%2BbEGdpyurvuD5EN00%2B5ksGtadY4N31YE%2Bmq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv%2F3rym5Z%2BYszOgVch%2F5VFS0YRxI5ei44PmDZrK%2F3fN5jxIYt4RSzanbG536MvkDQmeC7iD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhVsqt1P&port=13180&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_eU7rv+yA3Stb43zrS8hlErgERW02d3p5G1IPHVRtsurQF5wY"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+QENCwH4hLhAGEur+3+bEGdpyurvuD5EN00+5ksGtadY4N31YE+mq72G3wLjFfKv7Lmj08pjh5XZXyxPn0sK8AQ2RQSJpAE2B7hA7oGvQ6TGthEIZFVsmnv/3rym5Z+YszOgVch/5VFS0YRxI5ei44PmDZrK/3fN5jxIYt4RSzanbG536MvkDQmeC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhVsqt1P"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423274,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423274,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtQ5VnXCA0PWIGCiPxC/RufWEs5Wr6Ua0j9nrGtgtt0lAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyrMul14=",
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
  "id": -576460752303423273,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAjo+R2uOU7NiN2YkNABP45HI69sPGIcWbSCCZHTTrwKnRp0zkEcFxxm1dha7n1orEy8jpcHy2QV1fXNGRawmADuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrTHJeX"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423273,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAjo+R2uOU7NiN2YkNABP45HI69sPGIcWbSCCZHTTrwKnRp0zkEcFxxm1dha7n1orEy8jpcHy2QV1fXNGRawmADuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrTHJeX",
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
  "id": -576460752303423272,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAjo+R2uOU7NiN2YkNABP45HI69sPGIcWbSCCZHTTrwKnRp0zkEcFxxm1dha7n1orEy8jpcHy2QV1fXNGRawmADuEBANFagSxznjh1zcEVgmnJMgH0XQ95Yfmr3yR+gTckO4T0aR38RX0U94rae+LRTV6ucjxCYxBmNtMxlkRt0Mi0KuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq0Q6kD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423272,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuEAjo+R2uOU7NiN2YkNABP45HI69sPGIcWbSCCZHTTrwKnRp0zkEcFxxm1dha7n1orEy8jpcHy2QV1fXNGRawmADuEBANFagSxznjh1zcEVgmnJMgH0XQ95Yfmr3yR+gTckO4T0aR38RX0U94rae+LRTV6ucjxCYxBmNtMxlkRt0Mi0KuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq0Q6kD"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuEAjo+R2uOU7NiN2YkNABP45HI69sPGIcWbSCCZHTTrwKnRp0zkEcFxxm1dha7n1orEy8jpcHy2QV1fXNGRawmADuEBANFagSxznjh1zcEVgmnJMgH0XQ95Yfmr3yR+gTckO4T0aR38RX0U94rae+LRTV6ucjxCYxBmNtMxlkRt0Mi0KuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq0Q6kD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423271,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423271,
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
  "id": -576460752303423270,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423270,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAjo+R2uOU7NiN2YkNABP45HI69sPGIcWbSCCZHTTrwKnRp0zkEcFxxm1dha7n1orEy8jpcHy2QV1fXNGRawmADuEBANFagSxznjh1zcEVgmnJMgH0XQ95Yfmr3yR+gTckO4T0aR38RX0U94rae+LRTV6ucjxCYxBmNtMxlkRt0Mi0KuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq0Q6kD",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423269,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423269,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtQ5VnXCA0PWIGCiPxC/RufWEs5Wr6Ua0j9nrGtgtt0lA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoZT7MA=",
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
  "id": -576460752303423268,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAr0nBj5KfWviUONh7gj/6uMmFBWcyrJOoH7edEzotWZ/zCkvmCDfMhiDEWQKQb5QJjyPkytjJASO90PgU4nd0OuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYzzvIC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423268,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAr0nBj5KfWviUONh7gj/6uMmFBWcyrJOoH7edEzotWZ/zCkvmCDfMhiDEWQKQb5QJjyPkytjJASO90PgU4nd0OuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYzzvIC",
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
  "id": -576460752303423267,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAr0nBj5KfWviUONh7gj/6uMmFBWcyrJOoH7edEzotWZ/zCkvmCDfMhiDEWQKQb5QJjyPkytjJASO90PgU4nd0OuEA74Typl7Z1PU2ooMDH/pJeDQA2L4Ff9FxYq5yhgh+k+e+xvej7LYP0bF93KfjxGxBEABp9KHqjHN2tO27WY+ANuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZMiwuD"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423267,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuEAr0nBj5KfWviUONh7gj/6uMmFBWcyrJOoH7edEzotWZ/zCkvmCDfMhiDEWQKQb5QJjyPkytjJASO90PgU4nd0OuEA74Typl7Z1PU2ooMDH/pJeDQA2L4Ff9FxYq5yhgh+k+e+xvej7LYP0bF93KfjxGxBEABp9KHqjHN2tO27WY+ANuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZMiwuD"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuEAr0nBj5KfWviUONh7gj/6uMmFBWcyrJOoH7edEzotWZ/zCkvmCDfMhiDEWQKQb5QJjyPkytjJASO90PgU4nd0OuEA74Typl7Z1PU2ooMDH/pJeDQA2L4Ff9FxYq5yhgh+k+e+xvej7LYP0bF93KfjxGxBEABp9KHqjHN2tO27WY+ANuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZMiwuD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423266,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423266,
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
  "id": -576460752303423265,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423265,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAr0nBj5KfWviUONh7gj/6uMmFBWcyrJOoH7edEzotWZ/zCkvmCDfMhiDEWQKQb5QJjyPkytjJASO90PgU4nd0OuEA74Typl7Z1PU2ooMDH/pJeDQA2L4Ff9FxYq5yhgh+k+e+xvej7LYP0bF93KfjxGxBEABp9KHqjHN2tO27WY+ANuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZMiwuD",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423264,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423264,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtQ5VnXCA0PWIGCiPxC/RufWEs5Wr6Ua0j9nrGtgtt0lBKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYKEQqnM=",
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
  "id": -576460752303423263,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED8eegF7aWOsUImonRfrsd/X3bx5AMfBtBrYoZoSOE6CW0cWUPQwkqHNq8VUXz3+B5KidUiZakNvoTCitDUhcgHuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAIqPSe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423263,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+JALAfhCuED8eegF7aWOsUImonRfrsd/X3bx5AMfBtBrYoZoSOE6CW0cWUPQwkqHNq8VUXz3+B5KidUiZakNvoTCitDUhcgHuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAIqPSe",
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
  "id": -576460752303423262,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECPbNvltZ5d/U/WQ2cXPbKva9CTpZjma9OZV1J/mir97gO17VfM0eFliadU2weMQixkrSySSe+PnTq5GDwGqJQCuED8eegF7aWOsUImonRfrsd/X3bx5AMfBtBrYoZoSOE6CW0cWUPQwkqHNq8VUXz3+B5KidUiZakNvoTCitDUhcgHuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCALRt5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423262,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuECPbNvltZ5d/U/WQ2cXPbKva9CTpZjma9OZV1J/mir97gO17VfM0eFliadU2weMQixkrSySSe+PnTq5GDwGqJQCuED8eegF7aWOsUImonRfrsd/X3bx5AMfBtBrYoZoSOE6CW0cWUPQwkqHNq8VUXz3+B5KidUiZakNvoTCitDUhcgHuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCALRt5"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuECPbNvltZ5d/U/WQ2cXPbKva9CTpZjma9OZV1J/mir97gO17VfM0eFliadU2weMQixkrSySSe+PnTq5GDwGqJQCuED8eegF7aWOsUImonRfrsd/X3bx5AMfBtBrYoZoSOE6CW0cWUPQwkqHNq8VUXz3+B5KidUiZakNvoTCitDUhcgHuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCALRt5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423261,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423261,
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
  "id": -576460752303423260,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423260,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECPbNvltZ5d/U/WQ2cXPbKva9CTpZjma9OZV1J/mir97gO17VfM0eFliadU2weMQixkrSySSe+PnTq5GDwGqJQCuED8eegF7aWOsUImonRfrsd/X3bx5AMfBtBrYoZoSOE6CW0cWUPQwkqHNq8VUXz3+B5KidUiZakNvoTCitDUhcgHuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCALRt5",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423259,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423259,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtQ5VnXCA0PWIGCiPxC/RufWEs5Wr6Ua0j9nrGtgtt0lBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkVSmVw=",
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
  "id": -576460752303423258,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAmhhQwyLUqfJ5EI3QS/0ofFYhpndT5EguUT8aEinxfJrmYaWplFwumoAH21JsdCoygXqxM50WsmRc+z6vA24QGuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbpf1ia"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423258,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAmhhQwyLUqfJ5EI3QS/0ofFYhpndT5EguUT8aEinxfJrmYaWplFwumoAH21JsdCoygXqxM50WsmRc+z6vA24QGuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbpf1ia",
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
  "id": -576460752303423257,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAmhhQwyLUqfJ5EI3QS/0ofFYhpndT5EguUT8aEinxfJrmYaWplFwumoAH21JsdCoygXqxM50WsmRc+z6vA24QGuECQRSAW4UQcfm5bm0dz8XZ2w76R8VwhlgtdT9rffJXLFtsz0fRaEUJ7M8BsLzqWXgLOCfxdP4pnY7nBdjspQocOuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZVGZ1E"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423257,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuEAmhhQwyLUqfJ5EI3QS/0ofFYhpndT5EguUT8aEinxfJrmYaWplFwumoAH21JsdCoygXqxM50WsmRc+z6vA24QGuECQRSAW4UQcfm5bm0dz8XZ2w76R8VwhlgtdT9rffJXLFtsz0fRaEUJ7M8BsLzqWXgLOCfxdP4pnY7nBdjspQocOuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZVGZ1E"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuEAmhhQwyLUqfJ5EI3QS/0ofFYhpndT5EguUT8aEinxfJrmYaWplFwumoAH21JsdCoygXqxM50WsmRc+z6vA24QGuECQRSAW4UQcfm5bm0dz8XZ2w76R8VwhlgtdT9rffJXLFtsz0fRaEUJ7M8BsLzqWXgLOCfxdP4pnY7nBdjspQocOuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZVGZ1E"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423256,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423256,
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
  "id": -576460752303423255,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423255,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAmhhQwyLUqfJ5EI3QS/0ofFYhpndT5EguUT8aEinxfJrmYaWplFwumoAH21JsdCoygXqxM50WsmRc+z6vA24QGuECQRSAW4UQcfm5bm0dz8XZ2w76R8VwhlgtdT9rffJXLFtsz0fRaEUJ7M8BsLzqWXgLOCfxdP4pnY7nBdjspQocOuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZVGZ1E",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423254,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423254,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtQ5VnXCA0PWIGCiPxC/RufWEs5Wr6Ua0j9nrGtgtt0lBqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYCWFJPU=",
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
  "id": -576460752303423253,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECOZSwBhxUTdI5JWBTADAtieKvbx77m8/B9AWaZIMBCXsP07vya5hqB05Qdjk0O8zo5nKuP/MjxVWBc7mSXXooKuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCnN6mt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423253,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "signed_tx": "tx_+JALAfhCuECOZSwBhxUTdI5JWBTADAtieKvbx77m8/B9AWaZIMBCXsP07vya5hqB05Qdjk0O8zo5nKuP/MjxVWBc7mSXXooKuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCnN6mt",
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
  "id": -576460752303423252,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECOZSwBhxUTdI5JWBTADAtieKvbx77m8/B9AWaZIMBCXsP07vya5hqB05Qdjk0O8zo5nKuP/MjxVWBc7mSXXooKuEDwf68Iv9vPGme8YOMp42VajzMpkswl6FoQpK0JTBrYFWtTn81joo+T7QzYiG9L1xkIkSp2qBF5H0XS2uq7YSkEuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCNNWzv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423252,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuECOZSwBhxUTdI5JWBTADAtieKvbx77m8/B9AWaZIMBCXsP07vya5hqB05Qdjk0O8zo5nKuP/MjxVWBc7mSXXooKuEDwf68Iv9vPGme8YOMp42VajzMpkswl6FoQpK0JTBrYFWtTn81joo+T7QzYiG9L1xkIkSp2qBF5H0XS2uq7YSkEuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCNNWzv"
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
    "data": {
      "state": "tx_+NILAfiEuECOZSwBhxUTdI5JWBTADAtieKvbx77m8/B9AWaZIMBCXsP07vya5hqB05Qdjk0O8zo5nKuP/MjxVWBc7mSXXooKuEDwf68Iv9vPGme8YOMp42VajzMpkswl6FoQpK0JTBrYFWtTn81joo+T7QzYiG9L1xkIkSp2qBF5H0XS2uq7YSkEuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCNNWzv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423251,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423251,
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
  "id": -576460752303423250,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423250,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECOZSwBhxUTdI5JWBTADAtieKvbx77m8/B9AWaZIMBCXsP07vya5hqB05Qdjk0O8zo5nKuP/MjxVWBc7mSXXooKuEDwf68Iv9vPGme8YOMp42VajzMpkswl6FoQpK0JTBrYFWtTn81joo+T7QzYiG9L1xkIkSp2qBF5H0XS2uq7YSkEuEj4RjkCoQbUOVZ1wgND1iBgoj8Qv0bn1hLOVq+lGtI/Z6xrYLbdJQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCNNWzv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423249,
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423249,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423248,
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
    "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
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
  "channel_id": "ch_2cTyeMJEDKtSQioBZH4f1oGwS8F16CZ22hLiZnNeujKJKUzfoP",
  "id": -576460752303423248,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
