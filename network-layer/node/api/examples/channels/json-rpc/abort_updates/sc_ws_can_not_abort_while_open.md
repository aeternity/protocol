
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
      "fsm_id": "ba_pMZRpID2FenPKJ+HuJnrugYtPtOg3j5djs6nQpSwmkfMAk28"
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
      "fsm_id": "ba_yFuZi0bWcZGYo0s2TCF8zQ+uMlNxUOYsTwO5LPd+DNh2SNwE"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBxGKYKaQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421971,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBDXsbHlVHlecZEroiUgcI0HkMhc9ds3jDy3udaf2rvW4Xzp8nulZwT2zbQW99Hv5KnIdhlHbUYE++grRCcaucEuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcTuEr7w"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421971,
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_yFuZi0bWcZGYo0s2TCF8zQ+uMlNxUOYsTwO5LPd+DNh2SNwE"
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEBDXsbHlVHlecZEroiUgcI0HkMhc9ds3jDy3udaf2rvW4Xzp8nulZwT2zbQW99Hv5KnIdhlHbUYE++grRCcaucEuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcTuEr7w",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421970,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAQ17Gx5VR5XnGRK6IlIHCNB5DIXPXbN4w8t7nWn9q71uF86fJ7pWcE9s20FvfR7+SpyHYZR21GBPvoK0QnGrnBLhAVLrqa7kllvvzKP9Ft0fpnJri3FqEyM1I1N+wC4pQF5JEQjKAbUX29W5bTi+dpNlqy9RnWk9ZoU2AoAwhYCMFD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHE7PsLkg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
  "id": -576460752303421970,
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAQ17Gx5VR5XnGRK6IlIHCNB5DIXPXbN4w8t7nWn9q71uF86fJ7pWcE9s20FvfR7+SpyHYZR21GBPvoK0QnGrnBLhAVLrqa7kllvvzKP9Ft0fpnJri3FqEyM1I1N+wC4pQF5JEQjKAbUX29W5bTi+dpNlqy9RnWk9ZoU2AoAwhYCMFD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHE7PsLkg==",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_pMZRpID2FenPKJ+HuJnrugYtPtOg3j5djs6nQpSwmkfMAk28"
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAQ17Gx5VR5XnGRK6IlIHCNB5DIXPXbN4w8t7nWn9q71uF86fJ7pWcE9s20FvfR7+SpyHYZR21GBPvoK0QnGrnBLhAVLrqa7kllvvzKP9Ft0fpnJri3FqEyM1I1N+wC4pQF5JEQjKAbUX29W5bTi+dpNlqy9RnWk9ZoU2AoAwhYCMFD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHE7PsLkg==",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAQ17Gx5VR5XnGRK6IlIHCNB5DIXPXbN4w8t7nWn9q71uF86fJ7pWcE9s20FvfR7+SpyHYZR21GBPvoK0QnGrnBLhAVLrqa7kllvvzKP9Ft0fpnJri3FqEyM1I1N+wC4pQF5JEQjKAbUX29W5bTi+dpNlqy9RnWk9ZoU2AoAwhYCMFD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHE7PsLkg==",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAQ17Gx5VR5XnGRK6IlIHCNB5DIXPXbN4w8t7nWn9q71uF86fJ7pWcE9s20FvfR7+SpyHYZR21GBPvoK0QnGrnBLhAVLrqa7kllvvzKP9Ft0fpnJri3FqEyM1I1N+wC4pQF5JEQjKAbUX29W5bTi+dpNlqy9RnWk9ZoU2AoAwhYCMFD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHE7PsLkg==",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "message": {
        "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "message": {
        "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
  "id": -576460752303421969,
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
  "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
  "id": -576460752303421969,
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "state": "tx_+QEOCwH4hLhAQ17Gx5VR5XnGRK6IlIHCNB5DIXPXbN4w8t7nWn9q71uF86fJ7pWcE9s20FvfR7+SpyHYZR21GBPvoK0QnGrnBLhAVLrqa7kllvvzKP9Ft0fpnJri3FqEyM1I1N+wC4pQF5JEQjKAbUX29W5bTi+dpNlqy9RnWk9ZoU2AoAwhYCMFD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHE7PsLkg=="
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
    "data": {
      "state": "tx_+QEOCwH4hLhAQ17Gx5VR5XnGRK6IlIHCNB5DIXPXbN4w8t7nWn9q71uF86fJ7pWcE9s20FvfR7+SpyHYZR21GBPvoK0QnGrnBLhAVLrqa7kllvvzKP9Ft0fpnJri3FqEyM1I1N+wC4pQF5JEQjKAbUX29W5bTi+dpNlqy9RnWk9ZoU2AoAwhYCMFD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHE7PsLkg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1018,
        "message": "Not allowed at current channel state"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update",
      "params": {
        "error": 42
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
  "method": "channels.update",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1018,
        "message": "Not allowed at current channel state"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update",
      "params": {
        "error": 42
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
  "id": -576460752303421968,
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
  "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
  "id": -576460752303421968,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421967,
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
    "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
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
  "channel_id": "ch_Rz8XojzyYX1goLZn8ReBtiZiAijqFnHRdtZAagZDJUtnuQ2T3",
  "id": -576460752303421967,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
