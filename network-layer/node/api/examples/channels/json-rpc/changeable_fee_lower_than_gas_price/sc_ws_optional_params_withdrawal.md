
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
      "fsm_id": "ba_Vhj+uIXuHlc186u9bOJwa3HkpXufwuc8+jzKr7AHQ5mXArk3"
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
      "fsm_id": "ba_TXZE7BiMYctOzcyu6SXBfT1T9v4q+nDXg2it/u4PXsJBvdAN"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBhJBWVrU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422389,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAdY8SLYTETIywGxY89g6Tkzi5nQBCUR8J6pgnB+k8OLWoGSe21GgOOYzbH9B1hEE0uTC2/ZMdipkmvsf43lqUGuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYS+rOSV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422389,
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_TXZE7BiMYctOzcyu6SXBfT1T9v4q+nDXg2it/u4PXsJBvdAN"
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEAdY8SLYTETIywGxY89g6Tkzi5nQBCUR8J6pgnB+k8OLWoGSe21GgOOYzbH9B1hEE0uTC2/ZMdipkmvsf43lqUGuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYS+rOSV",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422388,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAHWPEi2ExEyMsBsWPPYOk5M4uZ0AQlEfCeqYJwfpPDi1qBknttRoDjmM2x/QdYRBNLkwtv2THYqZJr7H+N5alBrhAgfhBRIObdnIIiH6TxArkndMAuO4koeJVb2QEU4PyY21wwZLav4FhG0zpMcOAQezikhgz/jOyP6jO1mDTZo2jDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGEiHoV0w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
  "id": -576460752303422388,
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAHWPEi2ExEyMsBsWPPYOk5M4uZ0AQlEfCeqYJwfpPDi1qBknttRoDjmM2x/QdYRBNLkwtv2THYqZJr7H+N5alBrhAgfhBRIObdnIIiH6TxArkndMAuO4koeJVb2QEU4PyY21wwZLav4FhG0zpMcOAQezikhgz/jOyP6jO1mDTZo2jDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGEiHoV0w==",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Vhj+uIXuHlc186u9bOJwa3HkpXufwuc8+jzKr7AHQ5mXArk3"
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAHWPEi2ExEyMsBsWPPYOk5M4uZ0AQlEfCeqYJwfpPDi1qBknttRoDjmM2x/QdYRBNLkwtv2THYqZJr7H+N5alBrhAgfhBRIObdnIIiH6TxArkndMAuO4koeJVb2QEU4PyY21wwZLav4FhG0zpMcOAQezikhgz/jOyP6jO1mDTZo2jDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGEiHoV0w==",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAHWPEi2ExEyMsBsWPPYOk5M4uZ0AQlEfCeqYJwfpPDi1qBknttRoDjmM2x/QdYRBNLkwtv2THYqZJr7H+N5alBrhAgfhBRIObdnIIiH6TxArkndMAuO4koeJVb2QEU4PyY21wwZLav4FhG0zpMcOAQezikhgz/jOyP6jO1mDTZo2jDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGEiHoV0w==",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAHWPEi2ExEyMsBsWPPYOk5M4uZ0AQlEfCeqYJwfpPDi1qBknttRoDjmM2x/QdYRBNLkwtv2THYqZJr7H+N5alBrhAgfhBRIObdnIIiH6TxArkndMAuO4koeJVb2QEU4PyY21wwZLav4FhG0zpMcOAQezikhgz/jOyP6jO1mDTZo2jDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGEiHoV0w==",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
  "id": -576460752303422387,
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
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
  "id": -576460752303422387,
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "state": "tx_+QEOCwH4hLhAHWPEi2ExEyMsBsWPPYOk5M4uZ0AQlEfCeqYJwfpPDi1qBknttRoDjmM2x/QdYRBNLkwtv2THYqZJr7H+N5alBrhAgfhBRIObdnIIiH6TxArkndMAuO4koeJVb2QEU4PyY21wwZLav4FhG0zpMcOAQezikhgz/jOyP6jO1mDTZo2jDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGEiHoV0w=="
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "state": "tx_+QEOCwH4hLhAHWPEi2ExEyMsBsWPPYOk5M4uZ0AQlEfCeqYJwfpPDi1qBknttRoDjmM2x/QdYRBNLkwtv2THYqZJr7H+N5alBrhAgfhBRIObdnIIiH6TxArkndMAuO4koeJVb2QEU4PyY21wwZLav4FhG0zpMcOAQezikhgz/jOyP6jO1mDTZo2jDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGEiHoV0w=="
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBkA+JrbN2AIysCJDIUBWZ3Zs0IN5aO2bMCNxhQ8bmmayoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/FSdDYOKDc0aEz/UgoEcs4ajohf9X9BGhuePf6GLqnUld1F+cQwQKBhf4N1hc=",
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
  "id": -576460752303422386,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEC09Wo+ldDGP6/Lu08ynZMznwpqUR1bxxgo1htHOngMUJ+m4RVvDgH246VP0C0LOn+od53Apu7x22bgbLMylGUHuHX4czQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2Dig3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgYVqRQ9F"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
  "id": -576460752303422386,
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "signed_tx": "tx_+L0LAfhCuEC09Wo+ldDGP6/Lu08ynZMznwpqUR1bxxgo1htHOngMUJ+m4RVvDgH246VP0C0LOn+od53Apu7x22bgbLMylGUHuHX4czQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2Dig3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgYVqRQ9F",
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
  "id": -576460752303422385,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P8LAfiEuECdg/iucT1DxKFuh7rF1EjfcmJECSpAHLsnNCAGC2NtYgucRK8qRA8phyQoWTjZv/ncOMQxIfYIClJuLa669CYKuEC09Wo+ldDGP6/Lu08ynZMznwpqUR1bxxgo1htHOngMUJ+m4RVvDgH246VP0C0LOn+od53Apu7x22bgbLMylGUHuHX4czQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2Dig3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgYW0IU/T"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
  "id": -576460752303422385,
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P8LAfiEuECdg/iucT1DxKFuh7rF1EjfcmJECSpAHLsnNCAGC2NtYgucRK8qRA8phyQoWTjZv/ncOMQxIfYIClJuLa669CYKuEC09Wo+ldDGP6/Lu08ynZMznwpqUR1bxxgo1htHOngMUJ+m4RVvDgH246VP0C0LOn+od53Apu7x22bgbLMylGUHuHX4czQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2Dig3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgYW0IU/T",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P8LAfiEuECdg/iucT1DxKFuh7rF1EjfcmJECSpAHLsnNCAGC2NtYgucRK8qRA8phyQoWTjZv/ncOMQxIfYIClJuLa669CYKuEC09Wo+ldDGP6/Lu08ynZMznwpqUR1bxxgo1htHOngMUJ+m4RVvDgH246VP0C0LOn+od53Apu7x22bgbLMylGUHuHX4czQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2Dig3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgYW0IU/T",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P8LAfiEuECdg/iucT1DxKFuh7rF1EjfcmJECSpAHLsnNCAGC2NtYgucRK8qRA8phyQoWTjZv/ncOMQxIfYIClJuLa669CYKuEC09Wo+ldDGP6/Lu08ynZMznwpqUR1bxxgo1htHOngMUJ+m4RVvDgH246VP0C0LOn+od53Apu7x22bgbLMylGUHuHX4czQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2Dig3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgYW0IU/T",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P8LAfiEuECdg/iucT1DxKFuh7rF1EjfcmJECSpAHLsnNCAGC2NtYgucRK8qRA8phyQoWTjZv/ncOMQxIfYIClJuLa669CYKuEC09Wo+ldDGP6/Lu08ynZMznwpqUR1bxxgo1htHOngMUJ+m4RVvDgH246VP0C0LOn+od53Apu7x22bgbLMylGUHuHX4czQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2Dig3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgYW0IU/T",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "state": "tx_+P8LAfiEuECdg/iucT1DxKFuh7rF1EjfcmJECSpAHLsnNCAGC2NtYgucRK8qRA8phyQoWTjZv/ncOMQxIfYIClJuLa669CYKuEC09Wo+ldDGP6/Lu08ynZMznwpqUR1bxxgo1htHOngMUJ+m4RVvDgH246VP0C0LOn+od53Apu7x22bgbLMylGUHuHX4czQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2Dig3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgYW0IU/T"
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "state": "tx_+P8LAfiEuECdg/iucT1DxKFuh7rF1EjfcmJECSpAHLsnNCAGC2NtYgucRK8qRA8phyQoWTjZv/ncOMQxIfYIClJuLa669CYKuEC09Wo+ldDGP6/Lu08ynZMznwpqUR1bxxgo1htHOngMUJ+m4RVvDgH246VP0C0LOn+od53Apu7x22bgbLMylGUHuHX4czQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2Dig3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgYW0IU/T"
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBkA+JrbN2AIysCJDIUBWZ3Zs0IN5aO2bMCNxhQ8bmmayoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/Aobiv0KDZtcOT2QHMSn7Ye3r6M+jqyyVjQiph/medhaKMSYXlhQM2AiYi6A==",
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
  "id": -576460752303422384,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDW7m83kC/3JJlYGIzf3DqVUjRPM+AUdSRCDQxzdhyJ+HELk6qJ6dnlf6/PcMczFhohll78VhfW/de8X5F90QkFuHT4cjQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDNmlgWE0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
  "id": -576460752303422384,
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDW7m83kC/3JJlYGIzf3DqVUjRPM+AUdSRCDQxzdhyJ+HELk6qJ6dnlf6/PcMczFhohll78VhfW/de8X5F90QkFuHT4cjQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDNmlgWE0=",
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
  "id": -576460752303422383,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEDW7m83kC/3JJlYGIzf3DqVUjRPM+AUdSRCDQxzdhyJ+HELk6qJ6dnlf6/PcMczFhohll78VhfW/de8X5F90QkFuED0Eggf8upZHBDAQntMljQShpMg6ABDaCdhIDuVv+AWDIEZDRCGGbtegCNjx3hfDZ0mREVtESGAq+pGDGdJmwkLuHT4cjQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDNrFT7dI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
  "id": -576460752303422383,
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEDW7m83kC/3JJlYGIzf3DqVUjRPM+AUdSRCDQxzdhyJ+HELk6qJ6dnlf6/PcMczFhohll78VhfW/de8X5F90QkFuED0Eggf8upZHBDAQntMljQShpMg6ABDaCdhIDuVv+AWDIEZDRCGGbtegCNjx3hfDZ0mREVtESGAq+pGDGdJmwkLuHT4cjQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDNrFT7dI=",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEDW7m83kC/3JJlYGIzf3DqVUjRPM+AUdSRCDQxzdhyJ+HELk6qJ6dnlf6/PcMczFhohll78VhfW/de8X5F90QkFuED0Eggf8upZHBDAQntMljQShpMg6ABDaCdhIDuVv+AWDIEZDRCGGbtegCNjx3hfDZ0mREVtESGAq+pGDGdJmwkLuHT4cjQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDNrFT7dI=",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "message": {
        "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEDW7m83kC/3JJlYGIzf3DqVUjRPM+AUdSRCDQxzdhyJ+HELk6qJ6dnlf6/PcMczFhohll78VhfW/de8X5F90QkFuED0Eggf8upZHBDAQntMljQShpMg6ABDaCdhIDuVv+AWDIEZDRCGGbtegCNjx3hfDZ0mREVtESGAq+pGDGdJmwkLuHT4cjQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDNrFT7dI=",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEDW7m83kC/3JJlYGIzf3DqVUjRPM+AUdSRCDQxzdhyJ+HELk6qJ6dnlf6/PcMczFhohll78VhfW/de8X5F90QkFuED0Eggf8upZHBDAQntMljQShpMg6ABDaCdhIDuVv+AWDIEZDRCGGbtegCNjx3hfDZ0mREVtESGAq+pGDGdJmwkLuHT4cjQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDNrFT7dI=",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "state": "tx_+P4LAfiEuEDW7m83kC/3JJlYGIzf3DqVUjRPM+AUdSRCDQxzdhyJ+HELk6qJ6dnlf6/PcMczFhohll78VhfW/de8X5F90QkFuED0Eggf8upZHBDAQntMljQShpMg6ABDaCdhIDuVv+AWDIEZDRCGGbtegCNjx3hfDZ0mREVtESGAq+pGDGdJmwkLuHT4cjQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDNrFT7dI="
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "state": "tx_+P4LAfiEuEDW7m83kC/3JJlYGIzf3DqVUjRPM+AUdSRCDQxzdhyJ+HELk6qJ6dnlf6/PcMczFhohll78VhfW/de8X5F90QkFuED0Eggf8upZHBDAQntMljQShpMg6ABDaCdhIDuVv+AWDIEZDRCGGbtegCNjx3hfDZ0mREVtESGAq+pGDGdJmwkLuHT4cjQBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDNrFT7dI="
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBkA+JrbN2AIysCJDIUBWZ3Zs0IN5aO2bMCNxhQ8bmmayoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/2GHK96fwf/AIYPY36W8ACBhiu/VJs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422382,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuED8G0LLUl/xASYH6bF/JfmgspRu1pzYQeQM0qC/Z/BrTJFJlD8/+q54ah3/1oG7rZDlCiQKOc2pkXgOHra4jAgOuGD4XjUBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf9hhyven8H/wCGD2N+lvAAgYYzc9KW"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
  "id": -576460752303422382,
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "signed_tx": "tx_+KgLAfhCuED8G0LLUl/xASYH6bF/JfmgspRu1pzYQeQM0qC/Z/BrTJFJlD8/+q54ah3/1oG7rZDlCiQKOc2pkXgOHra4jAgOuGD4XjUBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf9hhyven8H/wCGD2N+lvAAgYYzc9KW",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422381,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuED8G0LLUl/xASYH6bF/JfmgspRu1pzYQeQM0qC/Z/BrTJFJlD8/+q54ah3/1oG7rZDlCiQKOc2pkXgOHra4jAgOuED+Pmg3bASUp9C/fJ91aId4pIoLeenZY9OUIK+0eLPOsamq3cMHyPLmw1aW6WfYnWhoVz+A4EnzAHcXgYHY5nABuGD4XjUBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf9hhyven8H/wCGD2N+lvAAgYbu8sBI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
  "id": -576460752303422381,
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuED8G0LLUl/xASYH6bF/JfmgspRu1pzYQeQM0qC/Z/BrTJFJlD8/+q54ah3/1oG7rZDlCiQKOc2pkXgOHra4jAgOuED+Pmg3bASUp9C/fJ91aId4pIoLeenZY9OUIK+0eLPOsamq3cMHyPLmw1aW6WfYnWhoVz+A4EnzAHcXgYHY5nABuGD4XjUBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf9hhyven8H/wCGD2N+lvAAgYbu8sBI",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuED8G0LLUl/xASYH6bF/JfmgspRu1pzYQeQM0qC/Z/BrTJFJlD8/+q54ah3/1oG7rZDlCiQKOc2pkXgOHra4jAgOuED+Pmg3bASUp9C/fJ91aId4pIoLeenZY9OUIK+0eLPOsamq3cMHyPLmw1aW6WfYnWhoVz+A4EnzAHcXgYHY5nABuGD4XjUBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf9hhyven8H/wCGD2N+lvAAgYbu8sBI",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuED8G0LLUl/xASYH6bF/JfmgspRu1pzYQeQM0qC/Z/BrTJFJlD8/+q54ah3/1oG7rZDlCiQKOc2pkXgOHra4jAgOuED+Pmg3bASUp9C/fJ91aId4pIoLeenZY9OUIK+0eLPOsamq3cMHyPLmw1aW6WfYnWhoVz+A4EnzAHcXgYHY5nABuGD4XjUBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf9hhyven8H/wCGD2N+lvAAgYbu8sBI",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuED8G0LLUl/xASYH6bF/JfmgspRu1pzYQeQM0qC/Z/BrTJFJlD8/+q54ah3/1oG7rZDlCiQKOc2pkXgOHra4jAgOuED+Pmg3bASUp9C/fJ91aId4pIoLeenZY9OUIK+0eLPOsamq3cMHyPLmw1aW6WfYnWhoVz+A4EnzAHcXgYHY5nABuGD4XjUBoQZAPia2zdgCMrAiQyFAVmd2bNCDeWjtmzAjcYUPG5pmsqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf9hhyven8H/wCGD2N+lvAAgYbu8sBI",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
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
    "channel_id": "ch_VHzk2A9oCM5cp6pWLACLkPYBHMoW2Hr3S4oH6eanjwJoQJTfG",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
