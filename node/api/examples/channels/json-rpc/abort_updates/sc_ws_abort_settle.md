
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
      "fsm_id": "ba_+qQN4WS9l4kD4eVN6X8R8DXcFbB14TjsQ2EwJCIpRVTc5VGa"
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
      "fsm_id": "ba_G5iodI/xkpN2pf+PMU/dQZqp0JEEl8g1gyTDDcnxkWJ0IVnZ"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBwpDWaWc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421976,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAx9zRif35L4wT7tFQlP/yfmX2iBn0HU/xP6B2IjBSVxarFXQ8fxDAi9GqlYBiKmsjLVl0oGNVb3Ccl/hRSyj4KuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcIyOsA8"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421976,
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_G5iodI/xkpN2pf+PMU/dQZqp0JEEl8g1gyTDDcnxkWJ0IVnZ"
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEAx9zRif35L4wT7tFQlP/yfmX2iBn0HU/xP6B2IjBSVxarFXQ8fxDAi9GqlYBiKmsjLVl0oGNVb3Ccl/hRSyj4KuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcIyOsA8",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421975,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAMfc0Yn9+S+ME+7RUJT/8n5l9ogZ9B1P8T+gdiIwUlcWqxV0PH8QwIvRqpWAYiprIy1ZdKBjVW9wnJf4UUso+CrhAeaa4nQVFCTrJovkrVldOfZViyAOxYVFaJYqi56fPUbXUnch2UglFd6mbSE+0wmvBLLZXXW75loQcmSaKtQ1jAbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHCUOKR6g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
  "id": -576460752303421975,
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAMfc0Yn9+S+ME+7RUJT/8n5l9ogZ9B1P8T+gdiIwUlcWqxV0PH8QwIvRqpWAYiprIy1ZdKBjVW9wnJf4UUso+CrhAeaa4nQVFCTrJovkrVldOfZViyAOxYVFaJYqi56fPUbXUnch2UglFd6mbSE+0wmvBLLZXXW75loQcmSaKtQ1jAbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHCUOKR6g==",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_+qQN4WS9l4kD4eVN6X8R8DXcFbB14TjsQ2EwJCIpRVTc5VGa"
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAMfc0Yn9+S+ME+7RUJT/8n5l9ogZ9B1P8T+gdiIwUlcWqxV0PH8QwIvRqpWAYiprIy1ZdKBjVW9wnJf4UUso+CrhAeaa4nQVFCTrJovkrVldOfZViyAOxYVFaJYqi56fPUbXUnch2UglFd6mbSE+0wmvBLLZXXW75loQcmSaKtQ1jAbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHCUOKR6g==",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAMfc0Yn9+S+ME+7RUJT/8n5l9ogZ9B1P8T+gdiIwUlcWqxV0PH8QwIvRqpWAYiprIy1ZdKBjVW9wnJf4UUso+CrhAeaa4nQVFCTrJovkrVldOfZViyAOxYVFaJYqi56fPUbXUnch2UglFd6mbSE+0wmvBLLZXXW75loQcmSaKtQ1jAbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHCUOKR6g==",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAMfc0Yn9+S+ME+7RUJT/8n5l9ogZ9B1P8T+gdiIwUlcWqxV0PH8QwIvRqpWAYiprIy1ZdKBjVW9wnJf4UUso+CrhAeaa4nQVFCTrJovkrVldOfZViyAOxYVFaJYqi56fPUbXUnch2UglFd6mbSE+0wmvBLLZXXW75loQcmSaKtQ1jAbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHCUOKR6g==",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "message": {
        "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "message": {
        "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
  "id": -576460752303421974,
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
  "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
  "id": -576460752303421974,
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "state": "tx_+QEOCwH4hLhAMfc0Yn9+S+ME+7RUJT/8n5l9ogZ9B1P8T+gdiIwUlcWqxV0PH8QwIvRqpWAYiprIy1ZdKBjVW9wnJf4UUso+CrhAeaa4nQVFCTrJovkrVldOfZViyAOxYVFaJYqi56fPUbXUnch2UglFd6mbSE+0wmvBLLZXXW75loQcmSaKtQ1jAbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHCUOKR6g=="
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "state": "tx_+QEOCwH4hLhAMfc0Yn9+S+ME+7RUJT/8n5l9ogZ9B1P8T+gdiIwUlcWqxV0PH8QwIvRqpWAYiprIy1ZdKBjVW9wnJf4UUso+CrhAeaa4nQVFCTrJovkrVldOfZViyAOxYVFaJYqi56fPUbXUnch2UglFd6mbSE+0wmvBLLZXXW75loQcmSaKtQ1jAbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHCUOKR6g=="
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "signed_tx": "tx_+QGpCwHAuQGj+QGgNgGhBjyjSFDuhC16WH8WVWAVToYo97hJYNpm72Si6PHcDj2GoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFUOUmEgAgcPfrMPP",
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
    "signed_tx": "tx_+QHsCwH4QrhAFOVJ/3JDzDAnDfmAwTtnS7QGxwFOrKDZBHLZpgj8sPSu7N5M6TIV3kSlzqEIvwRJb96TyiuQyyhzJ49T8l5GDrkBo/kBoDYBoQY8o0hQ7oQtelh/FlVgFU6GKPe4SWDaZu9koujx3A49hqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDlJhIAIHDfkGXQQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAFOVJ/3JDzDAnDfmAwTtnS7QGxwFOrKDZBHLZpgj8sPSu7N5M6TIV3kSlzqEIvwRJb96TyiuQyyhzJ49T8l5GDrkBo/kBoDYBoQY8o0hQ7oQtelh/FlVgFU6GKPe4SWDaZu9koujx3A49hqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDlJhIAIHDfkGXQQ==",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAFOVJ/3JDzDAnDfmAwTtnS7QGxwFOrKDZBHLZpgj8sPSu7N5M6TIV3kSlzqEIvwRJb96TyiuQyyhzJ49T8l5GDrkBo/kBoDYBoQY8o0hQ7oQtelh/FlVgFU6GKPe4SWDaZu9koujx3A49hqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhVDlJhIAIHDfkGXQQ==",
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheOAGhBjyjSFDuhC16WH8WVWAVToYo97hJYNpm72Si6PHcDj2GoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiX/+GJGE5yoABAIYPY36W8ACBxKKIV3U=",
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
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBjyjSFDuhC16WH8WVWAVToYo97hJYNpm72Si6PHcDj2GoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KABDZHJPPQ==",
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
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421973,
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
  "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
  "id": -576460752303421973,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421972,
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
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
  "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
  "id": -576460752303421972,
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
    "channel_id": "ch_ThutEwf9WUg8wvX8DyBds3Yhvr7ChdvEMNukcsGqYaVBHpS8k",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
