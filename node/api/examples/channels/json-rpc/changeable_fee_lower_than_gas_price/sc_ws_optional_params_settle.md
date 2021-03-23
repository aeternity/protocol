
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
      "fsm_id": "ba_1PKOF7P+NFmx9T9XcsS4B9uephidIE2hxBwsolp9sql0Vt+l"
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
      "fsm_id": "ba_ROpzp+vRGotZnjSjDxjz4FoA0KreN3xTZGTwtU/oJA0Vfxcz"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBkn/Nx0Q=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422317,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBwS38cQLIYb+Hh2x271PD51yugqWkIOVtCDvKDYfwfH+3Ca3DT90yQsPOBdUa38h9bYUXGlMjkM6eOcKUPXDgKuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZJj/n9B"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422317,
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_ROpzp+vRGotZnjSjDxjz4FoA0KreN3xTZGTwtU/oJA0Vfxcz"
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEBwS38cQLIYb+Hh2x271PD51yugqWkIOVtCDvKDYfwfH+3Ca3DT90yQsPOBdUa38h9bYUXGlMjkM6eOcKUPXDgKuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZJj/n9B",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422316,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAZXYJw1B7BjWdLLlNuVaYqe2Tyx7r6TyzXlfGDRLAdtr2yJ8w/i7/dvZtPcwRUeOudEU9DSPKr97oxpwMCHMjArhAcEt/HECyGG/h4dsdu9Tw+dcroKlpCDlbQg7yg2H8Hx/twmtw0/dMkLDzgXVGt/IfW2FFxpTI5DOnjnClD1w4CriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGSZRBnRw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
  "id": -576460752303422316,
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAZXYJw1B7BjWdLLlNuVaYqe2Tyx7r6TyzXlfGDRLAdtr2yJ8w/i7/dvZtPcwRUeOudEU9DSPKr97oxpwMCHMjArhAcEt/HECyGG/h4dsdu9Tw+dcroKlpCDlbQg7yg2H8Hx/twmtw0/dMkLDzgXVGt/IfW2FFxpTI5DOnjnClD1w4CriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGSZRBnRw==",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_1PKOF7P+NFmx9T9XcsS4B9uephidIE2hxBwsolp9sql0Vt+l"
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAZXYJw1B7BjWdLLlNuVaYqe2Tyx7r6TyzXlfGDRLAdtr2yJ8w/i7/dvZtPcwRUeOudEU9DSPKr97oxpwMCHMjArhAcEt/HECyGG/h4dsdu9Tw+dcroKlpCDlbQg7yg2H8Hx/twmtw0/dMkLDzgXVGt/IfW2FFxpTI5DOnjnClD1w4CriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGSZRBnRw==",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAZXYJw1B7BjWdLLlNuVaYqe2Tyx7r6TyzXlfGDRLAdtr2yJ8w/i7/dvZtPcwRUeOudEU9DSPKr97oxpwMCHMjArhAcEt/HECyGG/h4dsdu9Tw+dcroKlpCDlbQg7yg2H8Hx/twmtw0/dMkLDzgXVGt/IfW2FFxpTI5DOnjnClD1w4CriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGSZRBnRw==",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAZXYJw1B7BjWdLLlNuVaYqe2Tyx7r6TyzXlfGDRLAdtr2yJ8w/i7/dvZtPcwRUeOudEU9DSPKr97oxpwMCHMjArhAcEt/HECyGG/h4dsdu9Tw+dcroKlpCDlbQg7yg2H8Hx/twmtw0/dMkLDzgXVGt/IfW2FFxpTI5DOnjnClD1w4CriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGSZRBnRw==",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "message": {
        "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "message": {
        "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
  "id": -576460752303422315,
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
  "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
  "id": -576460752303422315,
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "state": "tx_+QEOCwH4hLhAZXYJw1B7BjWdLLlNuVaYqe2Tyx7r6TyzXlfGDRLAdtr2yJ8w/i7/dvZtPcwRUeOudEU9DSPKr97oxpwMCHMjArhAcEt/HECyGG/h4dsdu9Tw+dcroKlpCDlbQg7yg2H8Hx/twmtw0/dMkLDzgXVGt/IfW2FFxpTI5DOnjnClD1w4CriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGSZRBnRw=="
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "state": "tx_+QEOCwH4hLhAZXYJw1B7BjWdLLlNuVaYqe2Tyx7r6TyzXlfGDRLAdtr2yJ8w/i7/dvZtPcwRUeOudEU9DSPKr97oxpwMCHMjArhAcEt/HECyGG/h4dsdu9Tw+dcroKlpCDlbQg7yg2H8Hx/twmtw0/dMkLDzgXVGt/IfW2FFxpTI5DOnjnClD1w4CriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGSZRBnRw=="
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "signed_tx": "tx_+QGpCwHAuQGj+QGgNgGhBpmUr4MwIblH+ExW9xxrJhxp2lDNGwoV2S+1upAAMOgkoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFUOUmEgAgZN4XoZI",
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
    "signed_tx": "tx_+QHsCwH4QrhARSqJ2+mQqMKxpvJvbML5nhdNrGQO3Mmm3BuP+fpWkpkzyqm3DUME72F6W//Wi7wcywQOLOH51aTYuJA+spGUBLkBo/kBoDYBoQaZlK+DMCG5R/hMVvccayYcadpQzRsKFdkvtbqQADDoJKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDlJhIAIGTSt4vpw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhARSqJ2+mQqMKxpvJvbML5nhdNrGQO3Mmm3BuP+fpWkpkzyqm3DUME72F6W//Wi7wcywQOLOH51aTYuJA+spGUBLkBo/kBoDYBoQaZlK+DMCG5R/hMVvccayYcadpQzRsKFdkvtbqQADDoJKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDlJhIAIGTSt4vpw==",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhARSqJ2+mQqMKxpvJvbML5nhdNrGQO3Mmm3BuP+fpWkpkzyqm3DUME72F6W//Wi7wcywQOLOH51aTYuJA+spGUBLkBo/kBoDYBoQaZlK+DMCG5R/hMVvccayYcadpQzRsKFdkvtbqQADDoJKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDlJhIAIGTSt4vpw==",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "fee": 1,
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBpmUr4MwIblH+ExW9xxrJhxp2lDNGwoV2S+1upAAMOgkoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXte9X0g+JbVRVg==",
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
    "signed_tx": "tx_+KcLAfhCuECEIKP06w+E/aR+D2/98KWINe2TACBuvVcwkgg+4qO94EI6pwc1QaXsWSVRZ2fk0QDMD35DiSGuGDIZFuhT+IACuF/4XTgBoQaZlK+DMCG5R/hMVvccayYcadpQzRsKFdkvtbqQADDoJKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17XvV9IPhsnnWo="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECEIKP06w+E/aR+D2/98KWINe2TACBuvVcwkgg+4qO94EI6pwc1QaXsWSVRZ2fk0QDMD35DiSGuGDIZFuhT+IACuF/4XTgBoQaZlK+DMCG5R/hMVvccayYcadpQzRsKFdkvtbqQADDoJKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17XvV9IPhsnnWo=",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECEIKP06w+E/aR+D2/98KWINe2TACBuvVcwkgg+4qO94EI6pwc1QaXsWSVRZ2fk0QDMD35DiSGuGDIZFuhT+IACuF/4XTgBoQaZlK+DMCG5R/hMVvccayYcadpQzRsKFdkvtbqQADDoJKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17XvV9IPhsnnWo=",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
    "channel_id": "ch_2Ae1u6vW8NzsHgjMbpQ5j6mYqPtqtZVq1evBW9otAgebjkNuLW",
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
      "fsm_id": "ba_r3zeHHZcZPZK8quxFfoxgWXm7r31yFUGAbT1LKVtm1EGYewS"
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
      "fsm_id": "ba_Zkk6xl1b3IAfbbWD6SW9bdcgBcwhbsCm92nHnzDlFf294hmJ"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBlNeHyB4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422314,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECZKe3vfwH/isyKXcTy4XEu7OkQioh3kYx/O1QJCJo6i6deUriisWtqB/ZWgbe9n2GtzW0rESJrfis/y5xeqeMJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZRgU0Tz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422314,
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_Zkk6xl1b3IAfbbWD6SW9bdcgBcwhbsCm92nHnzDlFf294hmJ"
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECZKe3vfwH/isyKXcTy4XEu7OkQioh3kYx/O1QJCJo6i6deUriisWtqB/ZWgbe9n2GtzW0rESJrfis/y5xeqeMJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZRgU0Tz",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422313,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAFdrMVhehSbN7zQJcc8emvTWtVaR7kHdgeagffFcKB7kEYiFd5eHWwTp/cSnf9cMf5EoB5Bq9oOkzUJKaT6sNDLhAmSnt738B/4rMil3E8uFxLuzpEIqId5GMfztUCQiaOounXlK4orFragf2VoG3vZ9hrc1tKxEia34rP8ucXqnjCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGUz8h7sA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
  "id": -576460752303422313,
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAFdrMVhehSbN7zQJcc8emvTWtVaR7kHdgeagffFcKB7kEYiFd5eHWwTp/cSnf9cMf5EoB5Bq9oOkzUJKaT6sNDLhAmSnt738B/4rMil3E8uFxLuzpEIqId5GMfztUCQiaOounXlK4orFragf2VoG3vZ9hrc1tKxEia34rP8ucXqnjCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGUz8h7sA==",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_r3zeHHZcZPZK8quxFfoxgWXm7r31yFUGAbT1LKVtm1EGYewS"
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAFdrMVhehSbN7zQJcc8emvTWtVaR7kHdgeagffFcKB7kEYiFd5eHWwTp/cSnf9cMf5EoB5Bq9oOkzUJKaT6sNDLhAmSnt738B/4rMil3E8uFxLuzpEIqId5GMfztUCQiaOounXlK4orFragf2VoG3vZ9hrc1tKxEia34rP8ucXqnjCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGUz8h7sA==",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAFdrMVhehSbN7zQJcc8emvTWtVaR7kHdgeagffFcKB7kEYiFd5eHWwTp/cSnf9cMf5EoB5Bq9oOkzUJKaT6sNDLhAmSnt738B/4rMil3E8uFxLuzpEIqId5GMfztUCQiaOounXlK4orFragf2VoG3vZ9hrc1tKxEia34rP8ucXqnjCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGUz8h7sA==",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAFdrMVhehSbN7zQJcc8emvTWtVaR7kHdgeagffFcKB7kEYiFd5eHWwTp/cSnf9cMf5EoB5Bq9oOkzUJKaT6sNDLhAmSnt738B/4rMil3E8uFxLuzpEIqId5GMfztUCQiaOounXlK4orFragf2VoG3vZ9hrc1tKxEia34rP8ucXqnjCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGUz8h7sA==",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "message": {
        "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "message": {
        "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
  "id": -576460752303422312,
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
  "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
  "id": -576460752303422312,
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "state": "tx_+QEOCwH4hLhAFdrMVhehSbN7zQJcc8emvTWtVaR7kHdgeagffFcKB7kEYiFd5eHWwTp/cSnf9cMf5EoB5Bq9oOkzUJKaT6sNDLhAmSnt738B/4rMil3E8uFxLuzpEIqId5GMfztUCQiaOounXlK4orFragf2VoG3vZ9hrc1tKxEia34rP8ucXqnjCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGUz8h7sA=="
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "state": "tx_+QEOCwH4hLhAFdrMVhehSbN7zQJcc8emvTWtVaR7kHdgeagffFcKB7kEYiFd5eHWwTp/cSnf9cMf5EoB5Bq9oOkzUJKaT6sNDLhAmSnt738B/4rMil3E8uFxLuzpEIqId5GMfztUCQiaOounXlK4orFragf2VoG3vZ9hrc1tKxEia34rP8ucXqnjCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGUz8h7sA=="
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "signed_tx": "tx_+QGpCwHAuQGj+QGgNgGhBl0DbxbltKCx6QdvTJoVcz0sDuuGu7DHnkAA+HKuaPL4oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFUOUmEgAgZWX3NRQ",
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
    "signed_tx": "tx_+QHsCwH4QrhACYwVvOtzc2bfMIdQRAIRmG7KRCpgcm94tBRlJDp+wx+jsjMI3WXEJTm9sUK167tKWkhd87MHmq4U/PZhB1scArkBo/kBoDYBoQZdA28W5bSgsekHb0yaFXM9LA7rhruwx55AAPhyrmjy+KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDlJhIAIGV4ys9qg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhACYwVvOtzc2bfMIdQRAIRmG7KRCpgcm94tBRlJDp+wx+jsjMI3WXEJTm9sUK167tKWkhd87MHmq4U/PZhB1scArkBo/kBoDYBoQZdA28W5bSgsekHb0yaFXM9LA7rhruwx55AAPhyrmjy+KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDlJhIAIGV4ys9qg==",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhACYwVvOtzc2bfMIdQRAIRmG7KRCpgcm94tBRlJDp+wx+jsjMI3WXEJTm9sUK167tKWkhd87MHmq4U/PZhB1scArkBo/kBoDYBoQZdA28W5bSgsekHb0yaFXM9LA7rhruwx55AAPhyrmjy+KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDlJhIAIGV4ys9qg==",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "fee": 1,
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheOAGhBl0DbxbltKCx6QdvTJoVcz0sDuuGu7DHnkAA+HKuaPL4oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiX/+GJGE5yoABAIYPY3/Vh7CBliYXdug=",
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
    "signed_tx": "tx_+KgLAfhCuEDTl7YXByJdeOPoQnGrcLcE2UrPFcflp+SyGiPTWOI9ICDhl+3NhFVA/ibXzmtw4bzNlcCJAcJxsf1VObxaTs0FuGD4XjgBoQZdA28W5bSgsekHb0yaFXM9LA7rhruwx55AAPhyrmjy+KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGD2N/1YewgZauTczM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KgLAfhCuEDTl7YXByJdeOPoQnGrcLcE2UrPFcflp+SyGiPTWOI9ICDhl+3NhFVA/ibXzmtw4bzNlcCJAcJxsf1VObxaTs0FuGD4XjgBoQZdA28W5bSgsekHb0yaFXM9LA7rhruwx55AAPhyrmjy+KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGD2N/1YewgZauTczM",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KgLAfhCuEDTl7YXByJdeOPoQnGrcLcE2UrPFcflp+SyGiPTWOI9ICDhl+3NhFVA/ibXzmtw4bzNlcCJAcJxsf1VObxaTs0FuGD4XjgBoQZdA28W5bSgsekHb0yaFXM9LA7rhruwx55AAPhyrmjy+KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGD2N/1YewgZauTczM",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
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
    "channel_id": "ch_hxuN5tY5564Wo2ifUvMeWJyXKQB2u1He1YKkiFJYMoh7XiusH",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
