
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
      "fsm_id": "ba_H4uZZW4WeJV39H205aTn+grc26wX+GDhIsWiKg6MIAGhAYZP"
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
      "fsm_id": "ba_g+n7DjI9HUpQ0MddIMEy1jecYvGv5p/RIX7uo1ajLSu2io0L"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZRCNkpnQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422582,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBV7rFNATNFnrPT4CMn7lZCnW+4C20Ib6i+DSvU+lSc5RGolwpJiM1CZCkxunWPCmoh5amVFhDMv1Cgbcb08lMFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGUcjzV50="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422582,
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_g+n7DjI9HUpQ0MddIMEy1jecYvGv5p/RIX7uo1ajLSu2io0L"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBV7rFNATNFnrPT4CMn7lZCnW+4C20Ib6i+DSvU+lSc5RGolwpJiM1CZCkxunWPCmoh5amVFhDMv1Cgbcb08lMFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGUcjzV50=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422581,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhARouEpyhzuacBcwKuRpWyoARrs+JGMUbMXyKH1/7m5SROiieS+k2NqM4jb8mWX+bN/QyXzPr8u+UGSQaeyIz3D7hAVe6xTQEzRZ6z0+AjJ+5WQp1vuAttCG+ovg0r1PpUnOURqJcKSYjNQmQpMbp1jwpqIeWplRYQzL9QoG3G9PJTBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlEc0HPI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
  "id": -576460752303422581,
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhARouEpyhzuacBcwKuRpWyoARrs+JGMUbMXyKH1/7m5SROiieS+k2NqM4jb8mWX+bN/QyXzPr8u+UGSQaeyIz3D7hAVe6xTQEzRZ6z0+AjJ+5WQp1vuAttCG+ovg0r1PpUnOURqJcKSYjNQmQpMbp1jwpqIeWplRYQzL9QoG3G9PJTBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlEc0HPI",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_H4uZZW4WeJV39H205aTn+grc26wX+GDhIsWiKg6MIAGhAYZP"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhARouEpyhzuacBcwKuRpWyoARrs+JGMUbMXyKH1/7m5SROiieS+k2NqM4jb8mWX+bN/QyXzPr8u+UGSQaeyIz3D7hAVe6xTQEzRZ6z0+AjJ+5WQp1vuAttCG+ovg0r1PpUnOURqJcKSYjNQmQpMbp1jwpqIeWplRYQzL9QoG3G9PJTBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlEc0HPI",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARouEpyhzuacBcwKuRpWyoARrs+JGMUbMXyKH1/7m5SROiieS+k2NqM4jb8mWX+bN/QyXzPr8u+UGSQaeyIz3D7hAVe6xTQEzRZ6z0+AjJ+5WQp1vuAttCG+ovg0r1PpUnOURqJcKSYjNQmQpMbp1jwpqIeWplRYQzL9QoG3G9PJTBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlEc0HPI",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARouEpyhzuacBcwKuRpWyoARrs+JGMUbMXyKH1/7m5SROiieS+k2NqM4jb8mWX+bN/QyXzPr8u+UGSQaeyIz3D7hAVe6xTQEzRZ6z0+AjJ+5WQp1vuAttCG+ovg0r1PpUnOURqJcKSYjNQmQpMbp1jwpqIeWplRYQzL9QoG3G9PJTBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlEc0HPI",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
  "id": -576460752303422580,
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
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
  "id": -576460752303422580,
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "state": "tx_+QENCwH4hLhARouEpyhzuacBcwKuRpWyoARrs+JGMUbMXyKH1/7m5SROiieS+k2NqM4jb8mWX+bN/QyXzPr8u+UGSQaeyIz3D7hAVe6xTQEzRZ6z0+AjJ+5WQp1vuAttCG+ovg0r1PpUnOURqJcKSYjNQmQpMbp1jwpqIeWplRYQzL9QoG3G9PJTBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlEc0HPI"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "state": "tx_+QENCwH4hLhARouEpyhzuacBcwKuRpWyoARrs+JGMUbMXyKH1/7m5SROiieS+k2NqM4jb8mWX+bN/QyXzPr8u+UGSQaeyIz3D7hAVe6xTQEzRZ6z0+AjJ+5WQp1vuAttCG+ovg0r1PpUnOURqJcKSYjNQmQpMbp1jwpqIeWplRYQzL9QoG3G9PJTBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlEc0HPI"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBhp1mTs1l7f2IPGjtAJ4B/yZn3/clJRoA4bgjhqPEFljoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/Aobiv0KAPDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgJSKoOYZg==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainDeposit"
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
  "id": -576460752303422579,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDxctVhfHGM7MGnYelctjVpdvOk6BRLVtcHTTUGO5d/uej8x0rXjt7WIGfy/fcR9XNPtRF+5H0OIeUVL6MlLr0OuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9CgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CUjlz+0Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
  "id": -576460752303422579,
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDxctVhfHGM7MGnYelctjVpdvOk6BRLVtcHTTUGO5d/uej8x0rXjt7WIGfy/fcR9XNPtRF+5H0OIeUVL6MlLr0OuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9CgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CUjlz+0Q=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainDeposit"
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
  "id": -576460752303422578,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBITVCNwe1AqP/kmXgaKOyb4h8EKhSq+AFdG0Q2IJsvpMP1JV5bAq/cg8m65YLubNZdvDqM9m8o+nGa0SJjWLEJuEDxctVhfHGM7MGnYelctjVpdvOk6BRLVtcHTTUGO5d/uej8x0rXjt7WIGfy/fcR9XNPtRF+5H0OIeUVL6MlLr0OuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9CgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CUsypm1Q="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
  "id": -576460752303422578,
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBITVCNwe1AqP/kmXgaKOyb4h8EKhSq+AFdG0Q2IJsvpMP1JV5bAq/cg8m65YLubNZdvDqM9m8o+nGa0SJjWLEJuEDxctVhfHGM7MGnYelctjVpdvOk6BRLVtcHTTUGO5d/uej8x0rXjt7WIGfy/fcR9XNPtRF+5H0OIeUVL6MlLr0OuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9CgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CUsypm1Q=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBITVCNwe1AqP/kmXgaKOyb4h8EKhSq+AFdG0Q2IJsvpMP1JV5bAq/cg8m65YLubNZdvDqM9m8o+nGa0SJjWLEJuEDxctVhfHGM7MGnYelctjVpdvOk6BRLVtcHTTUGO5d/uej8x0rXjt7WIGfy/fcR9XNPtRF+5H0OIeUVL6MlLr0OuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9CgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CUsypm1Q=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBITVCNwe1AqP/kmXgaKOyb4h8EKhSq+AFdG0Q2IJsvpMP1JV5bAq/cg8m65YLubNZdvDqM9m8o+nGa0SJjWLEJuEDxctVhfHGM7MGnYelctjVpdvOk6BRLVtcHTTUGO5d/uej8x0rXjt7WIGfy/fcR9XNPtRF+5H0OIeUVL6MlLr0OuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9CgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CUsypm1Q=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBITVCNwe1AqP/kmXgaKOyb4h8EKhSq+AFdG0Q2IJsvpMP1JV5bAq/cg8m65YLubNZdvDqM9m8o+nGa0SJjWLEJuEDxctVhfHGM7MGnYelctjVpdvOk6BRLVtcHTTUGO5d/uej8x0rXjt7WIGfy/fcR9XNPtRF+5H0OIeUVL6MlLr0OuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9CgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CUsypm1Q=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "state": "tx_+P4LAfiEuEBITVCNwe1AqP/kmXgaKOyb4h8EKhSq+AFdG0Q2IJsvpMP1JV5bAq/cg8m65YLubNZdvDqM9m8o+nGa0SJjWLEJuEDxctVhfHGM7MGnYelctjVpdvOk6BRLVtcHTTUGO5d/uej8x0rXjt7WIGfy/fcR9XNPtRF+5H0OIeUVL6MlLr0OuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9CgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CUsypm1Q="
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "state": "tx_+P4LAfiEuEBITVCNwe1AqP/kmXgaKOyb4h8EKhSq+AFdG0Q2IJsvpMP1JV5bAq/cg8m65YLubNZdvDqM9m8o+nGa0SJjWLEJuEDxctVhfHGM7MGnYelctjVpdvOk6BRLVtcHTTUGO5d/uej8x0rXjt7WIGfy/fcR9XNPtRF+5H0OIeUVL6MlLr0OuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9CgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CUsypm1Q="
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBhp1mTs1l7f2IPGjtAJ4B/yZn3/clJRoA4bgjhqPEFljoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/Aobiv0KBY8rhhwx3FNZzZtoqk4aiWG2eYbpEkfYl8gYb5T3SICgMhSgeYLA==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainDeposit"
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
  "id": -576460752303422577,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBLEnZ0kv3SNy/bUeWeSQkb5c0y7so3y6m6TiFWR+fH4KYM/Qsk+hFtmMEChdhfskpc+H1EquOQrxGb1hmslQsBuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDIQ2L+dQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
  "id": -576460752303422577,
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBLEnZ0kv3SNy/bUeWeSQkb5c0y7so3y6m6TiFWR+fH4KYM/Qsk+hFtmMEChdhfskpc+H1EquOQrxGb1hmslQsBuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDIQ2L+dQ=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainDeposit"
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
  "id": -576460752303422576,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBLEnZ0kv3SNy/bUeWeSQkb5c0y7so3y6m6TiFWR+fH4KYM/Qsk+hFtmMEChdhfskpc+H1EquOQrxGb1hmslQsBuECZ7ZXe8fEiaj4qp0rcO3+lqLly9N+Ki5nh9yTusXwCJluwQGBK90N3qxWaO2cHhlBXrEfk0uyfQYg3Zjzkk3oGuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDIc60OtY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
  "id": -576460752303422576,
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBLEnZ0kv3SNy/bUeWeSQkb5c0y7so3y6m6TiFWR+fH4KYM/Qsk+hFtmMEChdhfskpc+H1EquOQrxGb1hmslQsBuECZ7ZXe8fEiaj4qp0rcO3+lqLly9N+Ki5nh9yTusXwCJluwQGBK90N3qxWaO2cHhlBXrEfk0uyfQYg3Zjzkk3oGuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDIc60OtY=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBLEnZ0kv3SNy/bUeWeSQkb5c0y7so3y6m6TiFWR+fH4KYM/Qsk+hFtmMEChdhfskpc+H1EquOQrxGb1hmslQsBuECZ7ZXe8fEiaj4qp0rcO3+lqLly9N+Ki5nh9yTusXwCJluwQGBK90N3qxWaO2cHhlBXrEfk0uyfQYg3Zjzkk3oGuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDIc60OtY=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "message": {
        "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBLEnZ0kv3SNy/bUeWeSQkb5c0y7so3y6m6TiFWR+fH4KYM/Qsk+hFtmMEChdhfskpc+H1EquOQrxGb1hmslQsBuECZ7ZXe8fEiaj4qp0rcO3+lqLly9N+Ki5nh9yTusXwCJluwQGBK90N3qxWaO2cHhlBXrEfk0uyfQYg3Zjzkk3oGuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDIc60OtY=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBLEnZ0kv3SNy/bUeWeSQkb5c0y7so3y6m6TiFWR+fH4KYM/Qsk+hFtmMEChdhfskpc+H1EquOQrxGb1hmslQsBuECZ7ZXe8fEiaj4qp0rcO3+lqLly9N+Ki5nh9yTusXwCJluwQGBK90N3qxWaO2cHhlBXrEfk0uyfQYg3Zjzkk3oGuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDIc60OtY=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "state": "tx_+P4LAfiEuEBLEnZ0kv3SNy/bUeWeSQkb5c0y7so3y6m6TiFWR+fH4KYM/Qsk+hFtmMEChdhfskpc+H1EquOQrxGb1hmslQsBuECZ7ZXe8fEiaj4qp0rcO3+lqLly9N+Ki5nh9yTusXwCJluwQGBK90N3qxWaO2cHhlBXrEfk0uyfQYg3Zjzkk3oGuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDIc60OtY="
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "state": "tx_+P4LAfiEuEBLEnZ0kv3SNy/bUeWeSQkb5c0y7so3y6m6TiFWR+fH4KYM/Qsk+hFtmMEChdhfskpc+H1EquOQrxGb1hmslQsBuECZ7ZXe8fEiaj4qp0rcO3+lqLly9N+Ki5nh9yTusXwCJluwQGBK90N3qxWaO2cHhlBXrEfk0uyfQYg3Zjzkk3oGuHT4cjMBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDIc60OtY="
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBhp1mTs1l7f2IPGjtAJ4B/yZn3/clJRoA4bgjhqPEFljoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rnizAGGHLHOiuwDAIYPXtZ/KABTfApidg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422575,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEARHbfkp3ZnmhYn+6eRt26TmvgeIbzOwI+gX8VSVIE8VGf6xuN3GRsQtOPanx+sE5GRIRW/ZhT7EMRyfIdgby8KuF/4XTUBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAU4Se/60="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
  "id": -576460752303422575,
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEARHbfkp3ZnmhYn+6eRt26TmvgeIbzOwI+gX8VSVIE8VGf6xuN3GRsQtOPanx+sE5GRIRW/ZhT7EMRyfIdgby8KuF/4XTUBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAU4Se/60=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422574,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEARHbfkp3ZnmhYn+6eRt26TmvgeIbzOwI+gX8VSVIE8VGf6xuN3GRsQtOPanx+sE5GRIRW/ZhT7EMRyfIdgby8KuECMerRzMN22hx43dOVtQWoleJtDkYz4SP5l6roQI4/qZfECeom3J30jBdU224O3T7qngbXSmvTrm675+54Z2E0CuF/4XTUBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAUw3+BEk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
  "id": -576460752303422574,
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEARHbfkp3ZnmhYn+6eRt26TmvgeIbzOwI+gX8VSVIE8VGf6xuN3GRsQtOPanx+sE5GRIRW/ZhT7EMRyfIdgby8KuECMerRzMN22hx43dOVtQWoleJtDkYz4SP5l6roQI4/qZfECeom3J30jBdU224O3T7qngbXSmvTrm675+54Z2E0CuF/4XTUBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAUw3+BEk=",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEARHbfkp3ZnmhYn+6eRt26TmvgeIbzOwI+gX8VSVIE8VGf6xuN3GRsQtOPanx+sE5GRIRW/ZhT7EMRyfIdgby8KuECMerRzMN22hx43dOVtQWoleJtDkYz4SP5l6roQI4/qZfECeom3J30jBdU224O3T7qngbXSmvTrm675+54Z2E0CuF/4XTUBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAUw3+BEk=",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEARHbfkp3ZnmhYn+6eRt26TmvgeIbzOwI+gX8VSVIE8VGf6xuN3GRsQtOPanx+sE5GRIRW/ZhT7EMRyfIdgby8KuECMerRzMN22hx43dOVtQWoleJtDkYz4SP5l6roQI4/qZfECeom3J30jBdU224O3T7qngbXSmvTrm675+54Z2E0CuF/4XTUBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAUw3+BEk=",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEARHbfkp3ZnmhYn+6eRt26TmvgeIbzOwI+gX8VSVIE8VGf6xuN3GRsQtOPanx+sE5GRIRW/ZhT7EMRyfIdgby8KuECMerRzMN22hx43dOVtQWoleJtDkYz4SP5l6roQI4/qZfECeom3J30jBdU224O3T7qngbXSmvTrm675+54Z2E0CuF/4XTUBoQYadZk7NZe39iDxo7QCeAf8mZ9/3JSUaAOG4I4ajxBZY6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAUw3+BEk=",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
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
    "channel_id": "ch_CesQadXu6TpNBfMMpari9KNSG7yowZRNkRp7UdpUSqLytz3FD",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
