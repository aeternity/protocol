
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
      "fsm_id": "ba_izvEWEWyIpU6XA+H+/mQ6PTAdMDqOGkmEmMu7/pHFKkdLEtD"
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
      "fsm_id": "ba_VqF5kzUboP8Mw15msS0xF9hcdACKmyrBjbayZ/pdSV88Clum"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBiqthzMY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422341,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAIYC3R+TdDHuQx8hzk/+p7ob8BpF6XIOpJ3RjhlEqQQypOU+w0EIYHzWxk5HkzmJCS9s7q3BHvU9z8EYu08EINuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYrI1nyq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422341,
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_VqF5kzUboP8Mw15msS0xF9hcdACKmyrBjbayZ/pdSV88Clum"
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEAIYC3R+TdDHuQx8hzk/+p7ob8BpF6XIOpJ3RjhlEqQQypOU+w0EIYHzWxk5HkzmJCS9s7q3BHvU9z8EYu08EINuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYrI1nyq",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422340,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhACGAt0fk3Qx7kMfIc5P/qe6G/AaRelyDqSd0Y4ZRKkEMqTlPsNBCGB81sZOR5M5iQkvbO6twR71Pc/BGLtPBCDbhAk7O/9O4NnIgLofnOvgBMrGPnbVCEcxMXCb9AMYDUeyLXeK0w6BTq63ADSKULEZpmEWcavkRw5OnvoFWsx1NeC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGK2hwrbg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
  "id": -576460752303422340,
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhACGAt0fk3Qx7kMfIc5P/qe6G/AaRelyDqSd0Y4ZRKkEMqTlPsNBCGB81sZOR5M5iQkvbO6twR71Pc/BGLtPBCDbhAk7O/9O4NnIgLofnOvgBMrGPnbVCEcxMXCb9AMYDUeyLXeK0w6BTq63ADSKULEZpmEWcavkRw5OnvoFWsx1NeC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGK2hwrbg==",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_izvEWEWyIpU6XA+H+/mQ6PTAdMDqOGkmEmMu7/pHFKkdLEtD"
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhACGAt0fk3Qx7kMfIc5P/qe6G/AaRelyDqSd0Y4ZRKkEMqTlPsNBCGB81sZOR5M5iQkvbO6twR71Pc/BGLtPBCDbhAk7O/9O4NnIgLofnOvgBMrGPnbVCEcxMXCb9AMYDUeyLXeK0w6BTq63ADSKULEZpmEWcavkRw5OnvoFWsx1NeC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGK2hwrbg==",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhACGAt0fk3Qx7kMfIc5P/qe6G/AaRelyDqSd0Y4ZRKkEMqTlPsNBCGB81sZOR5M5iQkvbO6twR71Pc/BGLtPBCDbhAk7O/9O4NnIgLofnOvgBMrGPnbVCEcxMXCb9AMYDUeyLXeK0w6BTq63ADSKULEZpmEWcavkRw5OnvoFWsx1NeC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGK2hwrbg==",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhACGAt0fk3Qx7kMfIc5P/qe6G/AaRelyDqSd0Y4ZRKkEMqTlPsNBCGB81sZOR5M5iQkvbO6twR71Pc/BGLtPBCDbhAk7O/9O4NnIgLofnOvgBMrGPnbVCEcxMXCb9AMYDUeyLXeK0w6BTq63ADSKULEZpmEWcavkRw5OnvoFWsx1NeC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGK2hwrbg==",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "message": {
        "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "message": {
        "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
  "id": -576460752303422339,
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
  "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
  "id": -576460752303422339,
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "state": "tx_+QEOCwH4hLhACGAt0fk3Qx7kMfIc5P/qe6G/AaRelyDqSd0Y4ZRKkEMqTlPsNBCGB81sZOR5M5iQkvbO6twR71Pc/BGLtPBCDbhAk7O/9O4NnIgLofnOvgBMrGPnbVCEcxMXCb9AMYDUeyLXeK0w6BTq63ADSKULEZpmEWcavkRw5OnvoFWsx1NeC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGK2hwrbg=="
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "state": "tx_+QEOCwH4hLhACGAt0fk3Qx7kMfIc5P/qe6G/AaRelyDqSd0Y4ZRKkEMqTlPsNBCGB81sZOR5M5iQkvbO6twR71Pc/BGLtPBCDbhAk7O/9O4NnIgLofnOvgBMrGPnbVCEcxMXCb9AMYDUeyLXeK0w6BTq63ADSKULEZpmEWcavkRw5OnvoFWsx1NeC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGK2hwrbg=="
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
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "signed_tx": "tx_+QGpCwHAuQGj+QGgNgGhBureJ3BLnPmAft/hO5fc1RYw1JBsqc5WLoCqhrJXZdfioQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFUOWUILogYtz9mK/",
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
    "signed_tx": "tx_+QHsCwH4QrhAFSf1iDdHOBLjCIG8dS0xHGdMkv4ytbDqwrsiEouIzEvxl4rxDnVaVwZhFootCghnqXj0Zsg1/CyBUGFpEcgQC7kBo/kBoDYBoQbq3idwS5z5gH7f4TuX3NUWMNSQbKnOVi6AqoayV2XX4qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDllCC6IGLiOXRnQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAFSf1iDdHOBLjCIG8dS0xHGdMkv4ytbDqwrsiEouIzEvxl4rxDnVaVwZhFootCghnqXj0Zsg1/CyBUGFpEcgQC7kBo/kBoDYBoQbq3idwS5z5gH7f4TuX3NUWMNSQbKnOVi6AqoayV2XX4qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDllCC6IGLiOXRnQ==",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAFSf1iDdHOBLjCIG8dS0xHGdMkv4ytbDqwrsiEouIzEvxl4rxDnVaVwZhFootCghnqXj0Zsg1/CyBUGFpEcgQC7kBo/kBoDYBoQbq3idwS5z5gH7f4TuX3NUWMNSQbKnOVi6AqoayV2XX4qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDllCC6IGLiOXRnQ==",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBureJ3BLnPmAft/hO5fc1RYw1JBsqc5WLoCqhrJXZdfioQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAA4IhETvQ==",
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
    "signed_tx": "tx_+KcLAfhCuEAO6hVVGQv1Y7kayVUdesByiRzJTO0yiiZs1wbm+65yNvtrXJaoCOQ82isPTA8cwuPAEsbctoqoxBnYfY+hleQJuF/4XTgBoQbq3idwS5z5gH7f4TuX3NUWMNSQbKnOVi6AqoayV2XX4qEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAOPn7NFA="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAO6hVVGQv1Y7kayVUdesByiRzJTO0yiiZs1wbm+65yNvtrXJaoCOQ82isPTA8cwuPAEsbctoqoxBnYfY+hleQJuF/4XTgBoQbq3idwS5z5gH7f4TuX3NUWMNSQbKnOVi6AqoayV2XX4qEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAOPn7NFA=",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAO6hVVGQv1Y7kayVUdesByiRzJTO0yiiZs1wbm+65yNvtrXJaoCOQ82isPTA8cwuPAEsbctoqoxBnYfY+hleQJuF/4XTgBoQbq3idwS5z5gH7f4TuX3NUWMNSQbKnOVi6AqoayV2XX4qEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAOPn7NFA=",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
    "channel_id": "ch_2nSPBZrkBjqVZpLRpYunWtv21kYRDX9d4XtHsU8C4WW5zQEtxv",
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
      "fsm_id": "ba_ddZCYDwBkCOJbxwHH7sZUjRiY2rxAEv8kWjn9VKLj4KifoE8"
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
      "fsm_id": "ba_Ul2ScYqa6QTIpmEHq21hMXM/mJLY5tzj52wrVRDRzMBVM4An"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBjMEhtac=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422338,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBaiHCZnGC5eO+4IGKEr1xF4eWHvoTdj8KDumikfpfyyBNW843fzlr1VIibsCptmEth/wRMfIxs04UaizeQfeAPuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYww+XCp"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422338,
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_Ul2ScYqa6QTIpmEHq21hMXM/mJLY5tzj52wrVRDRzMBVM4An"
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEBaiHCZnGC5eO+4IGKEr1xF4eWHvoTdj8KDumikfpfyyBNW843fzlr1VIibsCptmEth/wRMfIxs04UaizeQfeAPuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYww+XCp",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422337,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAWohwmZxguXjvuCBihK9cReHlh76E3Y/Cg7popH6X8sgTVvON385a9VSIm7AqbZhLYf8ETHyMbNOFGos3kH3gD7hAeL8/tNlDNrjoIcMp3D7x/dMiD9xSDQWlZ660M/2INlMGxB5PKOirwfMA6M6YbE6aKgYRGgwU9dXFv4QEfyAKBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGMPl+W9g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
  "id": -576460752303422337,
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAWohwmZxguXjvuCBihK9cReHlh76E3Y/Cg7popH6X8sgTVvON385a9VSIm7AqbZhLYf8ETHyMbNOFGos3kH3gD7hAeL8/tNlDNrjoIcMp3D7x/dMiD9xSDQWlZ660M/2INlMGxB5PKOirwfMA6M6YbE6aKgYRGgwU9dXFv4QEfyAKBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGMPl+W9g==",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_ddZCYDwBkCOJbxwHH7sZUjRiY2rxAEv8kWjn9VKLj4KifoE8"
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAWohwmZxguXjvuCBihK9cReHlh76E3Y/Cg7popH6X8sgTVvON385a9VSIm7AqbZhLYf8ETHyMbNOFGos3kH3gD7hAeL8/tNlDNrjoIcMp3D7x/dMiD9xSDQWlZ660M/2INlMGxB5PKOirwfMA6M6YbE6aKgYRGgwU9dXFv4QEfyAKBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGMPl+W9g==",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAWohwmZxguXjvuCBihK9cReHlh76E3Y/Cg7popH6X8sgTVvON385a9VSIm7AqbZhLYf8ETHyMbNOFGos3kH3gD7hAeL8/tNlDNrjoIcMp3D7x/dMiD9xSDQWlZ660M/2INlMGxB5PKOirwfMA6M6YbE6aKgYRGgwU9dXFv4QEfyAKBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGMPl+W9g==",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAWohwmZxguXjvuCBihK9cReHlh76E3Y/Cg7popH6X8sgTVvON385a9VSIm7AqbZhLYf8ETHyMbNOFGos3kH3gD7hAeL8/tNlDNrjoIcMp3D7x/dMiD9xSDQWlZ660M/2INlMGxB5PKOirwfMA6M6YbE6aKgYRGgwU9dXFv4QEfyAKBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGMPl+W9g==",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "message": {
        "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "message": {
        "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
  "id": -576460752303422336,
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
  "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
  "id": -576460752303422336,
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "state": "tx_+QEOCwH4hLhAWohwmZxguXjvuCBihK9cReHlh76E3Y/Cg7popH6X8sgTVvON385a9VSIm7AqbZhLYf8ETHyMbNOFGos3kH3gD7hAeL8/tNlDNrjoIcMp3D7x/dMiD9xSDQWlZ660M/2INlMGxB5PKOirwfMA6M6YbE6aKgYRGgwU9dXFv4QEfyAKBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGMPl+W9g=="
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "state": "tx_+QEOCwH4hLhAWohwmZxguXjvuCBihK9cReHlh76E3Y/Cg7popH6X8sgTVvON385a9VSIm7AqbZhLYf8ETHyMbNOFGos3kH3gD7hAeL8/tNlDNrjoIcMp3D7x/dMiD9xSDQWlZ660M/2INlMGxB5PKOirwfMA6M6YbE6aKgYRGgwU9dXFv4QEfyAKBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGMPl+W9g=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBuEjHY/1wqghoYV1l7Eas3PJ7gmWhyFblwTitZyz34kpoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7uOFqAOZlcOGY=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAtYBVq3UxvcI1GsWTdbms/CwmRs6vOWfwOvBEQKe1B/WJLshuW9PJoSG3KMablpdqkzS3MrTW6lrxIje54On/BLkBovkBnzYBoQbhIx2P9cKoIaGFdZexGrNzye4JlochW5cE4rWcs9+JKaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7jhagDl3RHZ0"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAtYBVq3UxvcI1GsWTdbms/CwmRs6vOWfwOvBEQKe1B/WJLshuW9PJoSG3KMablpdqkzS3MrTW6lrxIje54On/BLkBovkBnzYBoQbhIx2P9cKoIaGFdZexGrNzye4JlochW5cE4rWcs9+JKaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7jhagDl3RHZ0",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAtYBVq3UxvcI1GsWTdbms/CwmRs6vOWfwOvBEQKe1B/WJLshuW9PJoSG3KMablpdqkzS3MrTW6lrxIje54On/BLkBovkBnzYBoQbhIx2P9cKoIaGFdZexGrNzye4JlochW5cE4rWcs9+JKaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7jhagDl3RHZ0",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBuEjHY/1wqghoYV1l7Eas3PJ7gmWhyFblwTitZyz34kpoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAA6zp57yg==",
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
    "signed_tx": "tx_+KcLAfhCuEC6DqmEJUIxxbkTxhQK6b/ECQtGR1GW4YKcv3z4hdRU3rOrjf8oFY/HUFgtXKVf3mIfaUNeYUBOV/2LEzdL6P0FuF/4XTgBoQbhIx2P9cKoIaGFdZexGrNzye4JlochW5cE4rWcs9+JKaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAOooNr9k="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC6DqmEJUIxxbkTxhQK6b/ECQtGR1GW4YKcv3z4hdRU3rOrjf8oFY/HUFgtXKVf3mIfaUNeYUBOV/2LEzdL6P0FuF/4XTgBoQbhIx2P9cKoIaGFdZexGrNzye4JlochW5cE4rWcs9+JKaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAOooNr9k=",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC6DqmEJUIxxbkTxhQK6b/ECQtGR1GW4YKcv3z4hdRU3rOrjf8oFY/HUFgtXKVf3mIfaUNeYUBOV/2LEzdL6P0FuF/4XTgBoQbhIx2P9cKoIaGFdZexGrNzye4JlochW5cE4rWcs9+JKaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAOooNr9k=",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
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
    "channel_id": "ch_2i9pxUuEdk1dYqAW53YGF4Lv8NyHoHcvRYteFamP6LA4NsNndr",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
