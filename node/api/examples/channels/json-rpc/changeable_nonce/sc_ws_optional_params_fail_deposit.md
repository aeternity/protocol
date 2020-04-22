
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
      "fsm_id": "ba_dwUQ6bonyEq4sjx3R+KeFfz+hY7bTCAZqrOCEPJqTPPav2m0"
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
      "fsm_id": "ba_WoAO+uKpLYBrGl/+QtQXryl3RoLiJEM2fXcwm2sZSmn+RG3k"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBmZCqRB8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422267,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECWZgr8PFvPxhq2YKtZXUCaKJF6Dc9/AIP0omE8ZhxgUd0zfrrvIWIYEh+DMMRI1pcMIYRgsQWfJXY5xBrJ2zsJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZmTNs67"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422267,
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_WoAO+uKpLYBrGl/+QtQXryl3RoLiJEM2fXcwm2sZSmn+RG3k"
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECWZgr8PFvPxhq2YKtZXUCaKJF6Dc9/AIP0omE8ZhxgUd0zfrrvIWIYEh+DMMRI1pcMIYRgsQWfJXY5xBrJ2zsJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZmTNs67",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422266,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAlmYK/Dxbz8YatmCrWV1AmiiReg3PfwCD9KJhPGYcYFHdM3667yFiGBIfgzDESNaXDCGEYLEFnyV2OcQayds7CbhAw9UcPlkjtw7MMc1k9mjEioVGzY/HpD+gOdQZpngppnFywZbivViMNYVDW4SGGGzWkvBtM/bz/vOpmfvkd7l1C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGZWjyUuA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
  "id": -576460752303422266,
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAlmYK/Dxbz8YatmCrWV1AmiiReg3PfwCD9KJhPGYcYFHdM3667yFiGBIfgzDESNaXDCGEYLEFnyV2OcQayds7CbhAw9UcPlkjtw7MMc1k9mjEioVGzY/HpD+gOdQZpngppnFywZbivViMNYVDW4SGGGzWkvBtM/bz/vOpmfvkd7l1C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGZWjyUuA==",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_dwUQ6bonyEq4sjx3R+KeFfz+hY7bTCAZqrOCEPJqTPPav2m0"
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAlmYK/Dxbz8YatmCrWV1AmiiReg3PfwCD9KJhPGYcYFHdM3667yFiGBIfgzDESNaXDCGEYLEFnyV2OcQayds7CbhAw9UcPlkjtw7MMc1k9mjEioVGzY/HpD+gOdQZpngppnFywZbivViMNYVDW4SGGGzWkvBtM/bz/vOpmfvkd7l1C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGZWjyUuA==",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAlmYK/Dxbz8YatmCrWV1AmiiReg3PfwCD9KJhPGYcYFHdM3667yFiGBIfgzDESNaXDCGEYLEFnyV2OcQayds7CbhAw9UcPlkjtw7MMc1k9mjEioVGzY/HpD+gOdQZpngppnFywZbivViMNYVDW4SGGGzWkvBtM/bz/vOpmfvkd7l1C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGZWjyUuA==",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAlmYK/Dxbz8YatmCrWV1AmiiReg3PfwCD9KJhPGYcYFHdM3667yFiGBIfgzDESNaXDCGEYLEFnyV2OcQayds7CbhAw9UcPlkjtw7MMc1k9mjEioVGzY/HpD+gOdQZpngppnFywZbivViMNYVDW4SGGGzWkvBtM/bz/vOpmfvkd7l1C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGZWjyUuA==",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "message": {
        "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "message": {
        "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
  "id": -576460752303422265,
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
  "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
  "id": -576460752303422265,
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "state": "tx_+QEOCwH4hLhAlmYK/Dxbz8YatmCrWV1AmiiReg3PfwCD9KJhPGYcYFHdM3667yFiGBIfgzDESNaXDCGEYLEFnyV2OcQayds7CbhAw9UcPlkjtw7MMc1k9mjEioVGzY/HpD+gOdQZpngppnFywZbivViMNYVDW4SGGGzWkvBtM/bz/vOpmfvkd7l1C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGZWjyUuA=="
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "state": "tx_+QEOCwH4hLhAlmYK/Dxbz8YatmCrWV1AmiiReg3PfwCD9KJhPGYcYFHdM3667yFiGBIfgzDESNaXDCGEYLEFnyV2OcQayds7CbhAw9UcPlkjtw7MMc1k9mjEioVGzY/HpD+gOdQZpngppnFywZbivViMNYVDW4SGGGzWkvBtM/bz/vOpmfvkd7l1C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGZWjyUuA=="
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
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "signed_tx": "tx_+HwLAcC4d/h1MwGhBtEdu3yA6TA0mdDTjpaY4qB/e5BvXswqwnt9izOCL12qoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/OmLnoAKAPDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgKDEtaH2LD07g==",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBtEdu3yA6TA0mdDTjpaY4qB/e5BvXswqwnt9izOCL12qoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBmiM58h4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422264,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEBvPh9tNbXD0plFK9FMs7ANsAanK9pMFoSRiY6gNoX8H3WWHoz/emDRPBaII7ju7G/XHOZ23vFgBi6Tcjaa0V0GuGD4XjUBoQbRHbt8gOkwNJnQ046WmOKgf3uQb17MKsJ7fYszgi9dqqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZppffqG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
  "id": -576460752303422264,
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEBvPh9tNbXD0plFK9FMs7ANsAanK9pMFoSRiY6gNoX8H3WWHoz/emDRPBaII7ju7G/XHOZ23vFgBi6Tcjaa0V0GuGD4XjUBoQbRHbt8gOkwNJnQ046WmOKgf3uQb17MKsJ7fYszgi9dqqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZppffqG",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422263,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAmglpKM2Bm2HdCIX53HzJhgrqwAQ/7jp72jMf5YUUYDkFjPyE4je/tjDjtIWk83H51FE+OCnZAOBsxo5V8tZUFuEBvPh9tNbXD0plFK9FMs7ANsAanK9pMFoSRiY6gNoX8H3WWHoz/emDRPBaII7ju7G/XHOZ23vFgBi6Tcjaa0V0GuGD4XjUBoQbRHbt8gOkwNJnQ046WmOKgf3uQb17MKsJ7fYszgi9dqqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoKl+8t"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
  "id": -576460752303422263,
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAmglpKM2Bm2HdCIX53HzJhgrqwAQ/7jp72jMf5YUUYDkFjPyE4je/tjDjtIWk83H51FE+OCnZAOBsxo5V8tZUFuEBvPh9tNbXD0plFK9FMs7ANsAanK9pMFoSRiY6gNoX8H3WWHoz/emDRPBaII7ju7G/XHOZ23vFgBi6Tcjaa0V0GuGD4XjUBoQbRHbt8gOkwNJnQ046WmOKgf3uQb17MKsJ7fYszgi9dqqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoKl+8t",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAmglpKM2Bm2HdCIX53HzJhgrqwAQ/7jp72jMf5YUUYDkFjPyE4je/tjDjtIWk83H51FE+OCnZAOBsxo5V8tZUFuEBvPh9tNbXD0plFK9FMs7ANsAanK9pMFoSRiY6gNoX8H3WWHoz/emDRPBaII7ju7G/XHOZ23vFgBi6Tcjaa0V0GuGD4XjUBoQbRHbt8gOkwNJnQ046WmOKgf3uQb17MKsJ7fYszgi9dqqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoKl+8t",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAmglpKM2Bm2HdCIX53HzJhgrqwAQ/7jp72jMf5YUUYDkFjPyE4je/tjDjtIWk83H51FE+OCnZAOBsxo5V8tZUFuEBvPh9tNbXD0plFK9FMs7ANsAanK9pMFoSRiY6gNoX8H3WWHoz/emDRPBaII7ju7G/XHOZ23vFgBi6Tcjaa0V0GuGD4XjUBoQbRHbt8gOkwNJnQ046WmOKgf3uQb17MKsJ7fYszgi9dqqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoKl+8t",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAmglpKM2Bm2HdCIX53HzJhgrqwAQ/7jp72jMf5YUUYDkFjPyE4je/tjDjtIWk83H51FE+OCnZAOBsxo5V8tZUFuEBvPh9tNbXD0plFK9FMs7ANsAanK9pMFoSRiY6gNoX8H3WWHoz/emDRPBaII7ju7G/XHOZ23vFgBi6Tcjaa0V0GuGD4XjUBoQbRHbt8gOkwNJnQ046WmOKgf3uQb17MKsJ7fYszgi9dqqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoKl+8t",
      "type": "channel_close_mutual_tx"
    }
  },
  "version": 1
}
```

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
      "fsm_id": "ba_mx3LYn2tFD3uhIr/rgVNqWd2SscKp2H8mZR28iE6shG56uQg"
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
      "fsm_id": "ba_eN3MhHOked1NnGQ/e2XFDZfoXuRWZsbWqxe88vc55OjcfWmD"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBm+AA2xk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422262,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBkz8dOU9DqnKZp+YCvGK1900+THNTGU99P6QZ8F4Rzk0/Rue18UIL1MzAMzMX2PdAuuvkrHzD0k0mpLPcntSUDuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZvNkMKa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422262,
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_eN3MhHOked1NnGQ/e2XFDZfoXuRWZsbWqxe88vc55OjcfWmD"
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEBkz8dOU9DqnKZp+YCvGK1900+THNTGU99P6QZ8F4Rzk0/Rue18UIL1MzAMzMX2PdAuuvkrHzD0k0mpLPcntSUDuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZvNkMKa",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422261,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAZM/HTlPQ6pymafmArxitfdNPkxzUxlPfT+kGfBeEc5NP0bntfFCC9TMwDMzF9j3QLrr5Kx8w9JNJqSz3J7UlA7hApeRRKXReXtsrDKMWX/3jg/ofdLv3xXDRw1Jf2xEY+I4QqD2GJNBmUzoO+dHXENCny41nAvoPy55rEhOoDeqqDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGb0EOJFQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
  "id": -576460752303422261,
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAZM/HTlPQ6pymafmArxitfdNPkxzUxlPfT+kGfBeEc5NP0bntfFCC9TMwDMzF9j3QLrr5Kx8w9JNJqSz3J7UlA7hApeRRKXReXtsrDKMWX/3jg/ofdLv3xXDRw1Jf2xEY+I4QqD2GJNBmUzoO+dHXENCny41nAvoPy55rEhOoDeqqDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGb0EOJFQ==",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_mx3LYn2tFD3uhIr/rgVNqWd2SscKp2H8mZR28iE6shG56uQg"
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAZM/HTlPQ6pymafmArxitfdNPkxzUxlPfT+kGfBeEc5NP0bntfFCC9TMwDMzF9j3QLrr5Kx8w9JNJqSz3J7UlA7hApeRRKXReXtsrDKMWX/3jg/ofdLv3xXDRw1Jf2xEY+I4QqD2GJNBmUzoO+dHXENCny41nAvoPy55rEhOoDeqqDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGb0EOJFQ==",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAZM/HTlPQ6pymafmArxitfdNPkxzUxlPfT+kGfBeEc5NP0bntfFCC9TMwDMzF9j3QLrr5Kx8w9JNJqSz3J7UlA7hApeRRKXReXtsrDKMWX/3jg/ofdLv3xXDRw1Jf2xEY+I4QqD2GJNBmUzoO+dHXENCny41nAvoPy55rEhOoDeqqDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGb0EOJFQ==",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAZM/HTlPQ6pymafmArxitfdNPkxzUxlPfT+kGfBeEc5NP0bntfFCC9TMwDMzF9j3QLrr5Kx8w9JNJqSz3J7UlA7hApeRRKXReXtsrDKMWX/3jg/ofdLv3xXDRw1Jf2xEY+I4QqD2GJNBmUzoO+dHXENCny41nAvoPy55rEhOoDeqqDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGb0EOJFQ==",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "event": "died"
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
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
    "channel_id": "ch_2b6bHkPFpMfERfWzdqezdJoKtfrEUjho1SoFKxn5f5HhyUHYyG",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "message": {
        "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "message": {
        "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
  "id": -576460752303422260,
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
  "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
  "id": -576460752303422260,
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "state": "tx_+QEOCwH4hLhAZM/HTlPQ6pymafmArxitfdNPkxzUxlPfT+kGfBeEc5NP0bntfFCC9TMwDMzF9j3QLrr5Kx8w9JNJqSz3J7UlA7hApeRRKXReXtsrDKMWX/3jg/ofdLv3xXDRw1Jf2xEY+I4QqD2GJNBmUzoO+dHXENCny41nAvoPy55rEhOoDeqqDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGb0EOJFQ=="
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "state": "tx_+QEOCwH4hLhAZM/HTlPQ6pymafmArxitfdNPkxzUxlPfT+kGfBeEc5NP0bntfFCC9TMwDMzF9j3QLrr5Kx8w9JNJqSz3J7UlA7hApeRRKXReXtsrDKMWX/3jg/ofdLv3xXDRw1Jf2xEY+I4QqD2GJNBmUzoO+dHXENCny41nAvoPy55rEhOoDeqqDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGb0EOJFQ=="
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
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "signed_tx": "tx_+HwLAcC4d/h1MwGhBuhPULm11ZRWMe2wFQL2bDyX1zf/Grzc0mgp7Xqo66MRoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/OmLnoAKBy7d2KOPanIgoeBduOtHrSep+GXgzluZAMk579K2VI8wKDEtaHZa4bOQ==",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBuhPULm11ZRWMe2wFQL2bDyX1zf/Grzc0mgp7Xqo66MRoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBnNDqb8c=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422259,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEDj31vm9PDfpDpQlTq6eJPpR2krptRKQweYfbKEWEdg39/WPerQlHTWtxIuGTF7uraG9u3zHptRugfETv3DEu4EuGD4XjUBoQboT1C5tdWUVjHtsBUC9mw8l9c3/xq83NJoKe16qOujEaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZxXkUGt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
  "id": -576460752303422259,
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEDj31vm9PDfpDpQlTq6eJPpR2krptRKQweYfbKEWEdg39/WPerQlHTWtxIuGTF7uraG9u3zHptRugfETv3DEu4EuGD4XjUBoQboT1C5tdWUVjHtsBUC9mw8l9c3/xq83NJoKe16qOujEaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZxXkUGt",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422258,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEBqWCGt99nmBXlcG8fkwj6cGmV9U8HP2qJqGNK87sfwrf10OknM9vVeRvUbL7guNLq+nmop9ZTW6uIR3m3PRbMBuEDj31vm9PDfpDpQlTq6eJPpR2krptRKQweYfbKEWEdg39/WPerQlHTWtxIuGTF7uraG9u3zHptRugfETv3DEu4EuGD4XjUBoQboT1C5tdWUVjHtsBUC9mw8l9c3/xq83NJoKe16qOujEaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZx1J6I9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
  "id": -576460752303422258,
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEBqWCGt99nmBXlcG8fkwj6cGmV9U8HP2qJqGNK87sfwrf10OknM9vVeRvUbL7guNLq+nmop9ZTW6uIR3m3PRbMBuEDj31vm9PDfpDpQlTq6eJPpR2krptRKQweYfbKEWEdg39/WPerQlHTWtxIuGTF7uraG9u3zHptRugfETv3DEu4EuGD4XjUBoQboT1C5tdWUVjHtsBUC9mw8l9c3/xq83NJoKe16qOujEaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZx1J6I9",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEBqWCGt99nmBXlcG8fkwj6cGmV9U8HP2qJqGNK87sfwrf10OknM9vVeRvUbL7guNLq+nmop9ZTW6uIR3m3PRbMBuEDj31vm9PDfpDpQlTq6eJPpR2krptRKQweYfbKEWEdg39/WPerQlHTWtxIuGTF7uraG9u3zHptRugfETv3DEu4EuGD4XjUBoQboT1C5tdWUVjHtsBUC9mw8l9c3/xq83NJoKe16qOujEaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZx1J6I9",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEBqWCGt99nmBXlcG8fkwj6cGmV9U8HP2qJqGNK87sfwrf10OknM9vVeRvUbL7guNLq+nmop9ZTW6uIR3m3PRbMBuEDj31vm9PDfpDpQlTq6eJPpR2krptRKQweYfbKEWEdg39/WPerQlHTWtxIuGTF7uraG9u3zHptRugfETv3DEu4EuGD4XjUBoQboT1C5tdWUVjHtsBUC9mw8l9c3/xq83NJoKe16qOujEaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZx1J6I9",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEBqWCGt99nmBXlcG8fkwj6cGmV9U8HP2qJqGNK87sfwrf10OknM9vVeRvUbL7guNLq+nmop9ZTW6uIR3m3PRbMBuEDj31vm9PDfpDpQlTq6eJPpR2krptRKQweYfbKEWEdg39/WPerQlHTWtxIuGTF7uraG9u3zHptRugfETv3DEu4EuGD4XjUBoQboT1C5tdWUVjHtsBUC9mw8l9c3/xq83NJoKe16qOujEaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZx1J6I9",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
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
    "channel_id": "ch_2mK3UeKhm6Dh3DUguhMDvXojmciK9ivHq3cUjf7qfftVRKevmz",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
