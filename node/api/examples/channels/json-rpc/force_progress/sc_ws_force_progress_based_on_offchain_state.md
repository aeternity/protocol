
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
      "fsm_id": "ba_iH316IhF5ebEOAA933I6pQgEZeBxm0cW96krCyYSY52x/Zap"
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
      "fsm_id": "ba_Rp/R0YZiUK15mVgpV47UkWW+eo6cjvNqbEMs+jKMaABogs5n"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYbWdDtMQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423152,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB9cozIcZc8zzFVGA7vaZZsg+K8J8XaTklGW8iHsPEiEJvN8ktmscuHT32iIMs6LRl4X+sZ7PN+vtdDBNGiLeUIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGG7Ez7wI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423152,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_Rp/R0YZiUK15mVgpV47UkWW+eo6cjvNqbEMs+jKMaABogs5n"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEB9cozIcZc8zzFVGA7vaZZsg+K8J8XaTklGW8iHsPEiEJvN8ktmscuHT32iIMs6LRl4X+sZ7PN+vtdDBNGiLeUIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGG7Ez7wI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423151,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAU7cvvngmwDJf85qkulIe7vSkW5ZZ69yTGYKS16JXBleG4t1TFjlETKWr8YP7cxP6dI0nfwfEzExIibjDUpsZBbhAfXKMyHGXPM8xVRgO72mWbIPivCfF2k5JRlvIh7DxIhCbzfJLZrHLh099oiDLOi0ZeF/rGezzfr7XQwTRoi3lCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhsZKUWq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423151,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAU7cvvngmwDJf85qkulIe7vSkW5ZZ69yTGYKS16JXBleG4t1TFjlETKWr8YP7cxP6dI0nfwfEzExIibjDUpsZBbhAfXKMyHGXPM8xVRgO72mWbIPivCfF2k5JRlvIh7DxIhCbzfJLZrHLh099oiDLOi0ZeF/rGezzfr7XQwTRoi3lCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhsZKUWq",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_iH316IhF5ebEOAA933I6pQgEZeBxm0cW96krCyYSY52x/Zap"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAU7cvvngmwDJf85qkulIe7vSkW5ZZ69yTGYKS16JXBleG4t1TFjlETKWr8YP7cxP6dI0nfwfEzExIibjDUpsZBbhAfXKMyHGXPM8xVRgO72mWbIPivCfF2k5JRlvIh7DxIhCbzfJLZrHLh099oiDLOi0ZeF/rGezzfr7XQwTRoi3lCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhsZKUWq",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAU7cvvngmwDJf85qkulIe7vSkW5ZZ69yTGYKS16JXBleG4t1TFjlETKWr8YP7cxP6dI0nfwfEzExIibjDUpsZBbhAfXKMyHGXPM8xVRgO72mWbIPivCfF2k5JRlvIh7DxIhCbzfJLZrHLh099oiDLOi0ZeF/rGezzfr7XQwTRoi3lCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhsZKUWq",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAU7cvvngmwDJf85qkulIe7vSkW5ZZ69yTGYKS16JXBleG4t1TFjlETKWr8YP7cxP6dI0nfwfEzExIibjDUpsZBbhAfXKMyHGXPM8xVRgO72mWbIPivCfF2k5JRlvIh7DxIhCbzfJLZrHLh099oiDLOi0ZeF/rGezzfr7XQwTRoi3lCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhsZKUWq",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "message": {
        "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "message": {
        "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
  "id": -576460752303423150,
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
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423150,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+QENCwH4hLhAU7cvvngmwDJf85qkulIe7vSkW5ZZ69yTGYKS16JXBleG4t1TFjlETKWr8YP7cxP6dI0nfwfEzExIibjDUpsZBbhAfXKMyHGXPM8xVRgO72mWbIPivCfF2k5JRlvIh7DxIhCbzfJLZrHLh099oiDLOi0ZeF/rGezzfr7XQwTRoi3lCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhsZKUWq"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+QENCwH4hLhAU7cvvngmwDJf85qkulIe7vSkW5ZZ69yTGYKS16JXBleG4t1TFjlETKWr8YP7cxP6dI0nfwfEzExIibjDUpsZBbhAfXKMyHGXPM8xVRgO72mWbIPivCfF2k5JRlvIh7DxIhCbzfJLZrHLh099oiDLOi0ZeF/rGezzfr7XQwTRoi3lCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhsZKUWq"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJAqDGHrblf5txU9BzEiN2aWf2oO3b2+8I7hB7hqLuKnpTUBW7CKI=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "vm_version": 6
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
  "id": -576460752303423149,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC+UtM8esmAxUMqcfjzcK2WOAtKB0E1sCByeedTdEx+NbEzPpXKDsMaECQzKlr17HnjaZWaNAfZRhXdK+JHS+oAuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1D2/Vv+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423149,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC+UtM8esmAxUMqcfjzcK2WOAtKB0E1sCByeedTdEx+NbEzPpXKDsMaECQzKlr17HnjaZWaNAfZRhXdK+JHS+oAuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1D2/Vv+",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "vm_version": 6
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
  "id": -576460752303423148,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECj2fdz5tSDNu/Ntxiw1TyliZZeTTY37x0LOTG4oaBvxhCTvB+QKyyPZuXI1Tpwmi6IGBbQ2Lk8TKof/AuXIUAAuEC+UtM8esmAxUMqcfjzcK2WOAtKB0E1sCByeedTdEx+NbEzPpXKDsMaECQzKlr17HnjaZWaNAfZRhXdK+JHS+oAuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1CINdJg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423148,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuECj2fdz5tSDNu/Ntxiw1TyliZZeTTY37x0LOTG4oaBvxhCTvB+QKyyPZuXI1Tpwmi6IGBbQ2Lk8TKof/AuXIUAAuEC+UtM8esmAxUMqcfjzcK2WOAtKB0E1sCByeedTdEx+NbEzPpXKDsMaECQzKlr17HnjaZWaNAfZRhXdK+JHS+oAuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1CINdJg"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuECj2fdz5tSDNu/Ntxiw1TyliZZeTTY37x0LOTG4oaBvxhCTvB+QKyyPZuXI1Tpwmi6IGBbQ2Lk8TKof/AuXIUAAuEC+UtM8esmAxUMqcfjzcK2WOAtKB0E1sCByeedTdEx+NbEzPpXKDsMaECQzKlr17HnjaZWaNAfZRhXdK+JHS+oAuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1CINdJg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJA6DSs0d5zT+S71XBk4fUFBsokGXLzRDXNDvyMBghIq6Gaj4lMl8=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423147,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECI5waUBQ2esr8edMkkmr+ZE/TGqv5uTXcpY38o+G4t2J/WO7iFOw0P9Nq32iIsW91k814JXL/63p9H+gdUjqELuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmqfVtKi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423147,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+JALAfhCuECI5waUBQ2esr8edMkkmr+ZE/TGqv5uTXcpY38o+G4t2J/WO7iFOw0P9Nq32iIsW91k814JXL/63p9H+gdUjqELuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmqfVtKi",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423146,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECI5waUBQ2esr8edMkkmr+ZE/TGqv5uTXcpY38o+G4t2J/WO7iFOw0P9Nq32iIsW91k814JXL/63p9H+gdUjqELuECfRYUOQYRho1XJhHvODvW3Wvenm6jOY/Uzxc96gIVCjaAfiNwoMifIFBlZTcg5lZnucgwhm7U3L61CW8MFErYLuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmqhcAiJ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423146,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuECI5waUBQ2esr8edMkkmr+ZE/TGqv5uTXcpY38o+G4t2J/WO7iFOw0P9Nq32iIsW91k814JXL/63p9H+gdUjqELuECfRYUOQYRho1XJhHvODvW3Wvenm6jOY/Uzxc96gIVCjaAfiNwoMifIFBlZTcg5lZnucgwhm7U3L61CW8MFErYLuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmqhcAiJ"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuECI5waUBQ2esr8edMkkmr+ZE/TGqv5uTXcpY38o+G4t2J/WO7iFOw0P9Nq32iIsW91k814JXL/63p9H+gdUjqELuECfRYUOQYRho1XJhHvODvW3Wvenm6jOY/Uzxc96gIVCjaAfiNwoMifIFBlZTcg5lZnucgwhm7U3L61CW8MFErYLuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmqhcAiJ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 4,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJBKCk4l91nJhEC4ml+q+KxPucmCoX/VZxs0D4U3nhCRtBQ5CRZSo=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423145,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECic+eLe5WczoWA+FOCc4cqQIk7roEjyHl6m/BF6rZ5IDvHWEDRnAqio4VYpctyy4E9kQ7G+5eMs0ogS44y5k8BuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOHrJ1w"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423145,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+JALAfhCuECic+eLe5WczoWA+FOCc4cqQIk7roEjyHl6m/BF6rZ5IDvHWEDRnAqio4VYpctyy4E9kQ7G+5eMs0ogS44y5k8BuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOHrJ1w",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423144,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA59MjzDrVWekrwUALyGaWPOjVdv/aKhD65rmUhUKDpuUFVeVOOaYGKmdEDLisLWZNi7SOz+qsXHQWtuqqn7joAuECic+eLe5WczoWA+FOCc4cqQIk7roEjyHl6m/BF6rZ5IDvHWEDRnAqio4VYpctyy4E9kQ7G+5eMs0ogS44y5k8BuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUN8fiHA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423144,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEA59MjzDrVWekrwUALyGaWPOjVdv/aKhD65rmUhUKDpuUFVeVOOaYGKmdEDLisLWZNi7SOz+qsXHQWtuqqn7joAuECic+eLe5WczoWA+FOCc4cqQIk7roEjyHl6m/BF6rZ5IDvHWEDRnAqio4VYpctyy4E9kQ7G+5eMs0ogS44y5k8BuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUN8fiHA"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEA59MjzDrVWekrwUALyGaWPOjVdv/aKhD65rmUhUKDpuUFVeVOOaYGKmdEDLisLWZNi7SOz+qsXHQWtuqqn7joAuECic+eLe5WczoWA+FOCc4cqQIk7roEjyHl6m/BF6rZ5IDvHWEDRnAqio4VYpctyy4E9kQ7G+5eMs0ogS44y5k8BuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUN8fiHA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJBaBARDoHvJo/gpX+ILDnEN1yLjKMbvQJJg5pUyEHdCwbLzRRXcU=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423143,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBRL0UNBl/7fUNkbaL7TNF15ZBwVBMIL8M838XfVPmyHkIiR7NRtAeQig9fFGmDfeR+NzXrhItpkWx0rr9KDKoEuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy81ip8y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423143,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBRL0UNBl/7fUNkbaL7TNF15ZBwVBMIL8M838XfVPmyHkIiR7NRtAeQig9fFGmDfeR+NzXrhItpkWx0rr9KDKoEuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy81ip8y",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423142,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBRL0UNBl/7fUNkbaL7TNF15ZBwVBMIL8M838XfVPmyHkIiR7NRtAeQig9fFGmDfeR+NzXrhItpkWx0rr9KDKoEuECx1uQIPPIxZDd8VYVubdXAWbo2gA4dXcc0oLZE2OkwfCLXtoAyIsD2syqcT1QEiWYZZE+AE1EoCBTX6Vlpm7gFuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy/Lb33X"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423142,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBRL0UNBl/7fUNkbaL7TNF15ZBwVBMIL8M838XfVPmyHkIiR7NRtAeQig9fFGmDfeR+NzXrhItpkWx0rr9KDKoEuECx1uQIPPIxZDd8VYVubdXAWbo2gA4dXcc0oLZE2OkwfCLXtoAyIsD2syqcT1QEiWYZZE+AE1EoCBTX6Vlpm7gFuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy/Lb33X"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBRL0UNBl/7fUNkbaL7TNF15ZBwVBMIL8M838XfVPmyHkIiR7NRtAeQig9fFGmDfeR+NzXrhItpkWx0rr9KDKoEuECx1uQIPPIxZDd8VYVubdXAWbo2gA4dXcc0oLZE2OkwfCLXtoAyIsD2syqcT1QEiWYZZE+AE1EoCBTX6Vlpm7gFuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy/Lb33X"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJBqCRPcMH9LBOb2JW1FmRdtOTQ9FTTG5TYMdn+OwMYJQc/ambSFY=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423141,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBCrQmWX7mbjzZeJ8SJA0UBrAMwwPSMSG/AKTf/wCljZtufT7cy8sBsgQ3CWos8DlNgD100gFqQXeGW4wjoxtgGuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP1DcUvB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423141,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBCrQmWX7mbjzZeJ8SJA0UBrAMwwPSMSG/AKTf/wCljZtufT7cy8sBsgQ3CWos8DlNgD100gFqQXeGW4wjoxtgGuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP1DcUvB",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423140,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBCrQmWX7mbjzZeJ8SJA0UBrAMwwPSMSG/AKTf/wCljZtufT7cy8sBsgQ3CWos8DlNgD100gFqQXeGW4wjoxtgGuECfbTVqgBelxPHtgziPWwSgWhoPKXMxCd3vPfxO7ZoDdxak3wDl7qUL2Xe841ri/RCgzII3equ5rExP64Op1zQHuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP1FPgcx"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423140,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBCrQmWX7mbjzZeJ8SJA0UBrAMwwPSMSG/AKTf/wCljZtufT7cy8sBsgQ3CWos8DlNgD100gFqQXeGW4wjoxtgGuECfbTVqgBelxPHtgziPWwSgWhoPKXMxCd3vPfxO7ZoDdxak3wDl7qUL2Xe841ri/RCgzII3equ5rExP64Op1zQHuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP1FPgcx"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBCrQmWX7mbjzZeJ8SJA0UBrAMwwPSMSG/AKTf/wCljZtufT7cy8sBsgQ3CWos8DlNgD100gFqQXeGW4wjoxtgGuECfbTVqgBelxPHtgziPWwSgWhoPKXMxCd3vPfxO7ZoDdxak3wDl7qUL2Xe841ri/RCgzII3equ5rExP64Op1zQHuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP1FPgcx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 5,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 5,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 6,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 6,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJB6CsrbuB33ZB7rArVZ7xM8bN2LCroN3l5LRcD+uqSlkit64KXIA=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423139,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECezfSW7j1Nl0bZ8WH19YhOTZcdOyHQLo7XuajSquXd1VkZioUNHxrfNXdxsvSh45WFX4/e+9nylXVOch5WmDkCuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrc2Z+Qu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423139,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+JALAfhCuECezfSW7j1Nl0bZ8WH19YhOTZcdOyHQLo7XuajSquXd1VkZioUNHxrfNXdxsvSh45WFX4/e+9nylXVOch5WmDkCuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrc2Z+Qu",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423138,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBHtrAfVv0esYyhLvyvXAXDXciT2JzAg0Zs9nDTZu2GMLmjpz5EyBQZiGARF9Dn4hVtUfDzp83UO1d6DGvIa1cIuECezfSW7j1Nl0bZ8WH19YhOTZcdOyHQLo7XuajSquXd1VkZioUNHxrfNXdxsvSh45WFX4/e+9nylXVOch5WmDkCuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrcAuYb7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423138,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBHtrAfVv0esYyhLvyvXAXDXciT2JzAg0Zs9nDTZu2GMLmjpz5EyBQZiGARF9Dn4hVtUfDzp83UO1d6DGvIa1cIuECezfSW7j1Nl0bZ8WH19YhOTZcdOyHQLo7XuajSquXd1VkZioUNHxrfNXdxsvSh45WFX4/e+9nylXVOch5WmDkCuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrcAuYb7"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBHtrAfVv0esYyhLvyvXAXDXciT2JzAg0Zs9nDTZu2GMLmjpz5EyBQZiGARF9Dn4hVtUfDzp83UO1d6DGvIa1cIuECezfSW7j1Nl0bZ8WH19YhOTZcdOyHQLo7XuajSquXd1VkZioUNHxrfNXdxsvSh45WFX4/e+9nylXVOch5WmDkCuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrcAuYb7"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 8,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 7,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 7,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJCKArw6gvWbkHyj1kDlmweauYqkAtt8ym6D1MmX2+wTxtizJ+5zE=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423137,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDhR/N/VyyJd9kFY291rENKcEaufrQkAvmsUqnLx+ZiGwJW6NO+tH2ubZnEt0RgARVhKIiVL4eSowuxoXo8t0QOuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYvjmupi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423137,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDhR/N/VyyJd9kFY291rENKcEaufrQkAvmsUqnLx+ZiGwJW6NO+tH2ubZnEt0RgARVhKIiVL4eSowuxoXo8t0QOuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYvjmupi",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423136,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA9n5gniQ5ig/ZadC8MkC6zpQN8Jsm2tQacqvrKPvHhnKhNEdSHH7FZe2OxNlr0YTyZb39jjux5+FwfJm1M6NoDuEDhR/N/VyyJd9kFY291rENKcEaufrQkAvmsUqnLx+ZiGwJW6NO+tH2ubZnEt0RgARVhKIiVL4eSowuxoXo8t0QOuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYsDttXV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423136,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEA9n5gniQ5ig/ZadC8MkC6zpQN8Jsm2tQacqvrKPvHhnKhNEdSHH7FZe2OxNlr0YTyZb39jjux5+FwfJm1M6NoDuEDhR/N/VyyJd9kFY291rENKcEaufrQkAvmsUqnLx+ZiGwJW6NO+tH2ubZnEt0RgARVhKIiVL4eSowuxoXo8t0QOuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYsDttXV"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEA9n5gniQ5ig/ZadC8MkC6zpQN8Jsm2tQacqvrKPvHhnKhNEdSHH7FZe2OxNlr0YTyZb39jjux5+FwfJm1M6NoDuEDhR/N/VyyJd9kFY291rENKcEaufrQkAvmsUqnLx+ZiGwJW6NO+tH2ubZnEt0RgARVhKIiVL4eSowuxoXo8t0QOuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYsDttXV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJCaDvdd2E2VaG+E002HFNFXNih0aUVoTvVSBDpz5OMGuMwFm+RzA=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423135,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECyiM/MJ5YF4VVzBjLweg7m+OtCoqvsOCBiL+j6T3lUKYyMU731xd5AIlvbp6jymQ3PFB2sIBnQqFOqVOxkC34CuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDohHTY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423135,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+JALAfhCuECyiM/MJ5YF4VVzBjLweg7m+OtCoqvsOCBiL+j6T3lUKYyMU731xd5AIlvbp6jymQ3PFB2sIBnQqFOqVOxkC34CuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDohHTY",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423134,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBzKiib/UCSXeDByrvkIrvWQxxF30wgsuIYjZqyX9x4NadHc0a9HCAIAey2A7/MWSKQcL7DT8iqYLuqwbjpdOIMuECyiM/MJ5YF4VVzBjLweg7m+OtCoqvsOCBiL+j6T3lUKYyMU731xd5AIlvbp6jymQ3PFB2sIBnQqFOqVOxkC34CuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDqzdM2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423134,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBzKiib/UCSXeDByrvkIrvWQxxF30wgsuIYjZqyX9x4NadHc0a9HCAIAey2A7/MWSKQcL7DT8iqYLuqwbjpdOIMuECyiM/MJ5YF4VVzBjLweg7m+OtCoqvsOCBiL+j6T3lUKYyMU731xd5AIlvbp6jymQ3PFB2sIBnQqFOqVOxkC34CuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDqzdM2"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBzKiib/UCSXeDByrvkIrvWQxxF30wgsuIYjZqyX9x4NadHc0a9HCAIAey2A7/MWSKQcL7DT8iqYLuqwbjpdOIMuECyiM/MJ5YF4VVzBjLweg7m+OtCoqvsOCBiL+j6T3lUKYyMU731xd5AIlvbp6jymQ3PFB2sIBnQqFOqVOxkC34CuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDqzdM2"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJCqDvDJM0iYilO7grS80Txf4hicibVZxVjY6HZsJzTJ5ymplTRSI=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423133,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBC3ttdI2QiT8yZNoK2SM0HxFQh1FcJJd+1dq1WjXGS/gW0BrtRSNfLZntDGXqalLqgu9PqmKb/+VKf0Jkp9sIKuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecprfxEfv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423133,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBC3ttdI2QiT8yZNoK2SM0HxFQh1FcJJd+1dq1WjXGS/gW0BrtRSNfLZntDGXqalLqgu9PqmKb/+VKf0Jkp9sIKuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecprfxEfv",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423132,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBC3ttdI2QiT8yZNoK2SM0HxFQh1FcJJd+1dq1WjXGS/gW0BrtRSNfLZntDGXqalLqgu9PqmKb/+VKf0Jkp9sIKuEBab6CH0YrU+SmWLPFCfxPMlZGuL8iaO+xZe6IQriPRQ1GLEyrhSsx38xSwsFhVnd/aIEvadRCbA3fiDVzdSAILuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoDBxf9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423132,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBC3ttdI2QiT8yZNoK2SM0HxFQh1FcJJd+1dq1WjXGS/gW0BrtRSNfLZntDGXqalLqgu9PqmKb/+VKf0Jkp9sIKuEBab6CH0YrU+SmWLPFCfxPMlZGuL8iaO+xZe6IQriPRQ1GLEyrhSsx38xSwsFhVnd/aIEvadRCbA3fiDVzdSAILuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoDBxf9"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "state": "tx_+NILAfiEuEBC3ttdI2QiT8yZNoK2SM0HxFQh1FcJJd+1dq1WjXGS/gW0BrtRSNfLZntDGXqalLqgu9PqmKb/+VKf0Jkp9sIKuEBab6CH0YrU+SmWLPFCfxPMlZGuL8iaO+xZe6IQriPRQ1GLEyrhSsx38xSwsFhVnd/aIEvadRCbA3fiDVzdSAILuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoDBxf9"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 9,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 9,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 10,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 10,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
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
    ],
    "contracts": [
      "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+nj4mXf0UdfJRgm4L5FbVvJgFx3rUgij/Xg1PD7l735AYP4T6BjO/y9fLVcbbq+euGKspkj0geiEzuawl02EAKTT5+k/+2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/X4lKCT6ePiZd/RR18lGCbgvkVtW8mAXHetSCKP9eDU8PuXvfhxgICAgICAoGM7/L18tVxtur564YqymSPSB6ITO5rCXTYQApNPn6T/gICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOg+mQXDaDbOGWcenHslGbmWzbWwhDP56xU7w5Sk/D5c72AgICAgID4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAH4SaD6ZBcNoNs4ZZx6ceyUZuZbNtbCEM/nrFTvDlKT8PlzveegN8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSFxAoBAArj4qDemVZJFGKoVINblPxU/hE+HqQP9b6ZjgvOmxY6jZAfTsDA+Qap+QamoLHf8VwmQd/h60Cq2gFj327dttU0dUjlsD+6exE6jEU6+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPkDtqCFzPTTiFBffe8P/CRAwQy7JB9ShQRel6dQYB7SuYQmlvkDkoCgHdyouV7WvK8NcjTQvraEYvxQpM3YKd3dXGkU6L2B2IyAgICAgICAgICAgICAgLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAK+Gagsd/xXCZB3+HrQKraAWPfbt221TR1SOWwP7p7ETqMRTr4Q6EAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSghcz004hQX33vD/wkQMEMuyQfUoUEXpenUGAe0rmEJpb45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMps2tw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ],
    "contracts": [
      "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+nj4mXf0UdfJRgm4L5FbVvJgFx3rUgij/Xg1PD7l735AYP4T6BjO/y9fLVcbbq+euGKspkj0geiEzuawl02EAKTT5+k/+2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/X4lKCT6ePiZd/RR18lGCbgvkVtW8mAXHetSCKP9eDU8PuXvfhxgICAgICAoGM7/L18tVxtur564YqymSPSB6ITO5rCXTYQApNPn6T/gICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOg+mQXDaDbOGWcenHslGbmWzbWwhDP56xU7w5Sk/D5c72AgICAgID4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAH4SaD6ZBcNoNs4ZZx6ceyUZuZbNtbCEM/nrFTvDlKT8PlzveegN8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSFxAoBAArj4qDemVZJFGKoVINblPxU/hE+HqQP9b6ZjgvOmxY6jZAfTsDA+Qap+QamoLHf8VwmQd/h60Cq2gFj327dttU0dUjlsD+6exE6jEU6+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPkDtqCFzPTTiFBffe8P/CRAwQy7JB9ShQRel6dQYB7SuYQmlvkDkoCgHdyouV7WvK8NcjTQvraEYvxQpM3YKd3dXGkU6L2B2IyAgICAgICAgICAgICAgLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAK+Gagsd/xXCZB3+HrQKraAWPfbt221TR1SOWwP7p7ETqMRTr4Q6EAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSghcz004hQX33vD/wkQMEMuyQfUoUEXpenUGAe0rmEJpb45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMps2tw=="
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
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303423131,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423131,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QL7ggJuAbkC9PkC8T8B+QLsuLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdO8fPBmaSVPqmgiBusf3LOGDDJVgVOLC2Epltiext0tvuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQoKoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTbNpXWijWsOX49kkYUP/zdszoKl6Vbyhsx2OfNGEmwErhx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEICKEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggHOoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMC4ufi3QAG4QKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0lX7zIei0DGZIYw95F0AjiQn31YgQLzQWxawu/lJrdBK4cfhvKQKhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChBwehBafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0AYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdFUTlMupXff6BHiZkecmAU9bxHaOfhOFn4Tz6N0u2IMQuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQkJoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwOa/sTo=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBC3ttdI2QiT8yZNoK2SM0HxFQh1FcJJd+1dq1WjXGS/gW0BrtRSNfLZntDGXqalLqgu9PqmKb/+VKf0Jkp9sIKuEBab6CH0YrU+SmWLPFCfxPMlZGuL8iaO+xZe6IQriPRQ1GLEyrhSsx38xSwsFhVnd/aIEvadRCbA3fiDVzdSAILuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoDBxf9",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1h0sosw=="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423130,
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "gas_price": 1000005732
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423130,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "signed_tx": "tx_+Qi7CwHAuQi1+QiyggIJAaEG33b7ipYBqGkP7b/Tpr3+HjAPSe8u/nhi1vUtDyZ2WwmhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BuNT40gsB+IS4QELe210jZCJPzJk2grZIzQfEVCHUVwkl37V2rVaNcZL+BbQGu1FI18tme0MZepqUuqC70+qYpv/5Up/QmSn2wgq4QFpvoIfRitT5KZYs8UJ/E8yVka4vyJo77Fl7ohCuI9FDUYsTKuFKzHfzFLCwWFWd39ogS9p1EJsDd+INXN1IAgu4SPhGOQKhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJCqDvDJM0iYilO7grS80Txf4hicibVZxVjY6HZsJzTJ5ymgu4uPi2ggI+AaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GhBafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0AQqDD0JAhDua4GS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgfbr2GkQpvtgLSNcDkReisbNsqSAITZQMJk1bp+U3Pqu5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaKnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdBABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQALkDiPkDhUABoKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0uQNf+QNcKAGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdO8fPBmaSVPqmgiBusf3LOGDDJVgVOLC2Epltiext0tvuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQoKoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2q6UABoKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0hcQKAQAKsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/UAhwHB0gowK1AcK40rgg==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1000005732,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+Qj+CwH4QrhA9de6N7DTdeJy3bjDoYNUf1EO4khZBYxxAr71/oQmsuoXxfGYjYccj+anLw2SwLBlBvim68CJggRMWOVha4ipCLkItfkIsoICCQGhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBC3ttdI2QiT8yZNoK2SM0HxFQh1FcJJd+1dq1WjXGS/gW0BrtRSNfLZntDGXqalLqgu9PqmKb/+VKf0Jkp9sIKuEBab6CH0YrU+SmWLPFCfxPMlZGuL8iaO+xZe6IQriPRQ1GLEyrhSsx38xSwsFhVnd/aIEvadRCbA3fiDVzdSAILuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoLuLj4toICPgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAEKgw9CQIQ7muBkuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoH269hpEKb7YC0jXA5EXorGzbKkgCE2UDCZNW6flNz6ruQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1AIcBwdIKMCtQHMZNtx0="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhA9de6N7DTdeJy3bjDoYNUf1EO4khZBYxxAr71/oQmsuoXxfGYjYccj+anLw2SwLBlBvim68CJggRMWOVha4ipCLkItfkIsoICCQGhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBC3ttdI2QiT8yZNoK2SM0HxFQh1FcJJd+1dq1WjXGS/gW0BrtRSNfLZntDGXqalLqgu9PqmKb/+VKf0Jkp9sIKuEBab6CH0YrU+SmWLPFCfxPMlZGuL8iaO+xZe6IQriPRQ1GLEyrhSsx38xSwsFhVnd/aIEvadRCbA3fiDVzdSAILuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoLuLj4toICPgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAEKgw9CQIQ7muBkuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoH269hpEKb7YC0jXA5EXorGzbKkgCE2UDCZNW6flNz6ruQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1AIcBwdIKMCtQHMZNtx0=",
      "type": "channel_force_progress_tx"
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhA9de6N7DTdeJy3bjDoYNUf1EO4khZBYxxAr71/oQmsuoXxfGYjYccj+anLw2SwLBlBvim68CJggRMWOVha4ipCLkItfkIsoICCQGhBt92+4qWAahpD+2/06a9/h4wD0nvLv54Ytb1LQ8mdlsJoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBC3ttdI2QiT8yZNoK2SM0HxFQh1FcJJd+1dq1WjXGS/gW0BrtRSNfLZntDGXqalLqgu9PqmKb/+VKf0Jkp9sIKuEBab6CH0YrU+SmWLPFCfxPMlZGuL8iaO+xZe6IQriPRQ1GLEyrhSsx38xSwsFhVnd/aIEvadRCbA3fiDVzdSAILuEj4RjkCoQbfdvuKlgGoaQ/tv9Omvf4eMA9J7y7+eGLW9S0PJnZbCQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoLuLj4toICPgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAEKgw9CQIQ7muBkuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoH269hpEKb7YC0jXA5EXorGzbKkgCE2UDCZNW6flNz6ruQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1AIcBwdIKMCtQHMZNtx0=",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423129,
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
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423129,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423128,
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
    "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
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
  "channel_id": "ch_2hR7FZ3bfyLgXvGu3qHya6tBn42mQgrEieFYrVRY589yRtwANr",
  "id": -576460752303423128,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection

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
      "fsm_id": "ba_efVW9wQdUtSB+BZ4a3xseZkxgGTzFeb+V8vIE90gHbIpChen"
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
      "fsm_id": "ba_mO/201U0qehBs1CJRcVZhmeOcaqWYNh0Ckzci8gp9b6HmGwp"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYdyDVvIA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423127,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBZTg6iSGXXOHBovu1qqRpoNXSn1DvN2oXNZjJzchctL3mWm+OPLYyGthT8a7pnyq8CdTpyKKS9g8cjzMfmk7kOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGHb5nfiQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423127,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_mO/201U0qehBs1CJRcVZhmeOcaqWYNh0Ckzci8gp9b6HmGwp"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBZTg6iSGXXOHBovu1qqRpoNXSn1DvN2oXNZjJzchctL3mWm+OPLYyGthT8a7pnyq8CdTpyKKS9g8cjzMfmk7kOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGHb5nfiQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423126,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAHDNs0FRuMmfRyj/+xrNoFqoSEk7Xg5N/RBWeJnxwOx0HlgPM9OVBsN1FoLbnsZfqossIogr1V4EIInU+u/BlAbhAWU4Ookhl1zhwaL7taqkaaDV0p9Q7zdqFzWYyc3IXLS95lpvjjy2MhrYU/Gu6Z8qvAnU6ciikvYPHI8zH5pO5DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh3C9hBw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423126,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAHDNs0FRuMmfRyj/+xrNoFqoSEk7Xg5N/RBWeJnxwOx0HlgPM9OVBsN1FoLbnsZfqossIogr1V4EIInU+u/BlAbhAWU4Ookhl1zhwaL7taqkaaDV0p9Q7zdqFzWYyc3IXLS95lpvjjy2MhrYU/Gu6Z8qvAnU6ciikvYPHI8zH5pO5DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh3C9hBw",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_efVW9wQdUtSB+BZ4a3xseZkxgGTzFeb+V8vIE90gHbIpChen"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAHDNs0FRuMmfRyj/+xrNoFqoSEk7Xg5N/RBWeJnxwOx0HlgPM9OVBsN1FoLbnsZfqossIogr1V4EIInU+u/BlAbhAWU4Ookhl1zhwaL7taqkaaDV0p9Q7zdqFzWYyc3IXLS95lpvjjy2MhrYU/Gu6Z8qvAnU6ciikvYPHI8zH5pO5DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh3C9hBw",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHDNs0FRuMmfRyj/+xrNoFqoSEk7Xg5N/RBWeJnxwOx0HlgPM9OVBsN1FoLbnsZfqossIogr1V4EIInU+u/BlAbhAWU4Ookhl1zhwaL7taqkaaDV0p9Q7zdqFzWYyc3IXLS95lpvjjy2MhrYU/Gu6Z8qvAnU6ciikvYPHI8zH5pO5DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh3C9hBw",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHDNs0FRuMmfRyj/+xrNoFqoSEk7Xg5N/RBWeJnxwOx0HlgPM9OVBsN1FoLbnsZfqossIogr1V4EIInU+u/BlAbhAWU4Ookhl1zhwaL7taqkaaDV0p9Q7zdqFzWYyc3IXLS95lpvjjy2MhrYU/Gu6Z8qvAnU6ciikvYPHI8zH5pO5DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh3C9hBw",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "message": {
        "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "message": {
        "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
  "id": -576460752303423125,
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
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423125,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+QENCwH4hLhAHDNs0FRuMmfRyj/+xrNoFqoSEk7Xg5N/RBWeJnxwOx0HlgPM9OVBsN1FoLbnsZfqossIogr1V4EIInU+u/BlAbhAWU4Ookhl1zhwaL7taqkaaDV0p9Q7zdqFzWYyc3IXLS95lpvjjy2MhrYU/Gu6Z8qvAnU6ciikvYPHI8zH5pO5DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh3C9hBw"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+QENCwH4hLhAHDNs0FRuMmfRyj/+xrNoFqoSEk7Xg5N/RBWeJnxwOx0HlgPM9OVBsN1FoLbnsZfqossIogr1V4EIInU+u/BlAbhAWU4Ookhl1zhwaL7taqkaaDV0p9Q7zdqFzWYyc3IXLS95lpvjjy2MhrYU/Gu6Z8qvAnU6ciikvYPHI8zH5pO5DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh3C9hBw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSAqDGHrblf5txU9BzEiN2aWf2oO3b2+8I7hB7hqLuKnpTUBZ2QCQ=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "vm_version": 6
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
  "id": -576460752303423124,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECUfOr4nEI27B0eDJ/Za0qouH2hHkHSaG8SVShcBCuZEt/Q7Vn5XLpGfT/dTnvahR6jnQGYCv60i2sl8LyBOs8CuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1CJJnI5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423124,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+JALAfhCuECUfOr4nEI27B0eDJ/Za0qouH2hHkHSaG8SVShcBCuZEt/Q7Vn5XLpGfT/dTnvahR6jnQGYCv60i2sl8LyBOs8CuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1CJJnI5",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "vm_version": 6
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
  "id": -576460752303423123,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA4mobt/kk8DzfClhVulNw+vZnPp914TexqwlPrwbKzTNuY3cG4zj/172Fs8hW4foRFi3khUUKvK+7H+UYYI38OuECUfOr4nEI27B0eDJ/Za0qouH2hHkHSaG8SVShcBCuZEt/Q7Vn5XLpGfT/dTnvahR6jnQGYCv60i2sl8LyBOs8CuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1AXKGTE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423123,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEA4mobt/kk8DzfClhVulNw+vZnPp914TexqwlPrwbKzTNuY3cG4zj/172Fs8hW4foRFi3khUUKvK+7H+UYYI38OuECUfOr4nEI27B0eDJ/Za0qouH2hHkHSaG8SVShcBCuZEt/Q7Vn5XLpGfT/dTnvahR6jnQGYCv60i2sl8LyBOs8CuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1AXKGTE"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEA4mobt/kk8DzfClhVulNw+vZnPp914TexqwlPrwbKzTNuY3cG4zj/172Fs8hW4foRFi3khUUKvK+7H+UYYI38OuECUfOr4nEI27B0eDJ/Za0qouH2hHkHSaG8SVShcBCuZEt/Q7Vn5XLpGfT/dTnvahR6jnQGYCv60i2sl8LyBOs8CuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1AXKGTE"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSA6DSs0d5zT+S71XBk4fUFBsokGXLzRDXNDvyMBghIq6Gaj1eGsQ=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423122,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECmNCzaoYA4rdq5e3Ksma+XHNDCxITFdvolCPoHptVMzOxtVgWNxNCHgcolF9N0LIlIrnw/W33300TTzj5bUigCuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmrlic2D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423122,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+JALAfhCuECmNCzaoYA4rdq5e3Ksma+XHNDCxITFdvolCPoHptVMzOxtVgWNxNCHgcolF9N0LIlIrnw/W33300TTzj5bUigCuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmrlic2D",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423121,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBDlZ37NjMogR6RfIHtmT/+FBE/j8k8FFA8HXRrQY46qhQUzRzeVEh3A3k3546BkFCs9OL46dES1KLa0s1OgnINuECmNCzaoYA4rdq5e3Ksma+XHNDCxITFdvolCPoHptVMzOxtVgWNxNCHgcolF9N0LIlIrnw/W33300TTzj5bUigCuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmrYvd7v"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423121,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEBDlZ37NjMogR6RfIHtmT/+FBE/j8k8FFA8HXRrQY46qhQUzRzeVEh3A3k3546BkFCs9OL46dES1KLa0s1OgnINuECmNCzaoYA4rdq5e3Ksma+XHNDCxITFdvolCPoHptVMzOxtVgWNxNCHgcolF9N0LIlIrnw/W33300TTzj5bUigCuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmrYvd7v"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEBDlZ37NjMogR6RfIHtmT/+FBE/j8k8FFA8HXRrQY46qhQUzRzeVEh3A3k3546BkFCs9OL46dES1KLa0s1OgnINuECmNCzaoYA4rdq5e3Ksma+XHNDCxITFdvolCPoHptVMzOxtVgWNxNCHgcolF9N0LIlIrnw/W33300TTzj5bUigCuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmrYvd7v"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 4,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSBKCk4l91nJhEC4ml+q+KxPucmCoX/VZxs0D4U3nhCRtBQ/Nnpag=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423120,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEALOro39iM+PgjpX+30F9e58q0/hPBwl1kFqrTkvlCEBM0lfKnDROyy+XcFppsETPfok0yIE0O0g6j0M8LnyIoKuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOS/E3Q"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423120,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEALOro39iM+PgjpX+30F9e58q0/hPBwl1kFqrTkvlCEBM0lfKnDROyy+XcFppsETPfok0yIE0O0g6j0M8LnyIoKuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOS/E3Q",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423119,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEADUJOww+Vm/7N5+rbz5RyB389sjKcQFp2nNfzZVtfUoIciawz4pKcuO0tZzpiuX6uIpcogD6x76YrA8dZqC4cDuEALOro39iM+PgjpX+30F9e58q0/hPBwl1kFqrTkvlCEBM0lfKnDROyy+XcFppsETPfok0yIE0O0g6j0M8LnyIoKuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUN79Iei"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423119,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEADUJOww+Vm/7N5+rbz5RyB389sjKcQFp2nNfzZVtfUoIciawz4pKcuO0tZzpiuX6uIpcogD6x76YrA8dZqC4cDuEALOro39iM+PgjpX+30F9e58q0/hPBwl1kFqrTkvlCEBM0lfKnDROyy+XcFppsETPfok0yIE0O0g6j0M8LnyIoKuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUN79Iei"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEADUJOww+Vm/7N5+rbz5RyB389sjKcQFp2nNfzZVtfUoIciawz4pKcuO0tZzpiuX6uIpcogD6x76YrA8dZqC4cDuEALOro39iM+PgjpX+30F9e58q0/hPBwl1kFqrTkvlCEBM0lfKnDROyy+XcFppsETPfok0yIE0O0g6j0M8LnyIoKuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUN79Iei"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSBaBARDoHvJo/gpX+ILDnEN1yLjKMbvQJJg5pUyEHdCwbLyuSXkE=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423118,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDEd9yrYGQQI8lb2jo96KDUdzXVUPZEK6kNpi1A1DsJAY1d1EqApbm735BKIu8gJYzEnKvAfkQPVs1T+wfvcnsAuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy9fo9Ek"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423118,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDEd9yrYGQQI8lb2jo96KDUdzXVUPZEK6kNpi1A1DsJAY1d1EqApbm735BKIu8gJYzEnKvAfkQPVs1T+wfvcnsAuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy9fo9Ek",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423117,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDEd9yrYGQQI8lb2jo96KDUdzXVUPZEK6kNpi1A1DsJAY1d1EqApbm735BKIu8gJYzEnKvAfkQPVs1T+wfvcnsAuED2ztvA2A3fDWqN2U5sP4pY2YKVuhEfCFZ38HG5QxZ3XvS8BHk2yjnEm3K5VVlZzPx3eiyBxJpMw3wma1+gQFwEuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy9nZr7b"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423117,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEDEd9yrYGQQI8lb2jo96KDUdzXVUPZEK6kNpi1A1DsJAY1d1EqApbm735BKIu8gJYzEnKvAfkQPVs1T+wfvcnsAuED2ztvA2A3fDWqN2U5sP4pY2YKVuhEfCFZ38HG5QxZ3XvS8BHk2yjnEm3K5VVlZzPx3eiyBxJpMw3wma1+gQFwEuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy9nZr7b"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEDEd9yrYGQQI8lb2jo96KDUdzXVUPZEK6kNpi1A1DsJAY1d1EqApbm735BKIu8gJYzEnKvAfkQPVs1T+wfvcnsAuED2ztvA2A3fDWqN2U5sP4pY2YKVuhEfCFZ38HG5QxZ3XvS8BHk2yjnEm3K5VVlZzPx3eiyBxJpMw3wma1+gQFwEuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy9nZr7b"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSBqCRPcMH9LBOb2JW1FmRdtOTQ9FTTG5TYMdn+OwMYJQc/dimyyY=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423116,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECQIFOAYne1ZyIFrmuXNCYSd9qJn2WkF2dyC5jy4T9zxa+Jggmzb2B0BqWzPKSJWlD1NfGzHcaFW9VQVWXvPS0FuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP2ZEXrr"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423116,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+JALAfhCuECQIFOAYne1ZyIFrmuXNCYSd9qJn2WkF2dyC5jy4T9zxa+Jggmzb2B0BqWzPKSJWlD1NfGzHcaFW9VQVWXvPS0FuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP2ZEXrr",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423115,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBDFqPevaZ8aR+4tTaf+ro3pUP/k5Ph3LL2DpaYlWjhOZJPSF04cwTA91pAD3W6odvRT0KfbCzedb7YcnRS8z4MuECQIFOAYne1ZyIFrmuXNCYSd9qJn2WkF2dyC5jy4T9zxa+Jggmzb2B0BqWzPKSJWlD1NfGzHcaFW9VQVWXvPS0FuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP3PTzPv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423115,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEBDFqPevaZ8aR+4tTaf+ro3pUP/k5Ph3LL2DpaYlWjhOZJPSF04cwTA91pAD3W6odvRT0KfbCzedb7YcnRS8z4MuECQIFOAYne1ZyIFrmuXNCYSd9qJn2WkF2dyC5jy4T9zxa+Jggmzb2B0BqWzPKSJWlD1NfGzHcaFW9VQVWXvPS0FuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP3PTzPv"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEBDFqPevaZ8aR+4tTaf+ro3pUP/k5Ph3LL2DpaYlWjhOZJPSF04cwTA91pAD3W6odvRT0KfbCzedb7YcnRS8z4MuECQIFOAYne1ZyIFrmuXNCYSd9qJn2WkF2dyC5jy4T9zxa+Jggmzb2B0BqWzPKSJWlD1NfGzHcaFW9VQVWXvPS0FuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP3PTzPv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 5,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 5,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 6,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 6,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSB6CsrbuB33ZB7rArVZ7xM8bN2LCroN3l5LRcD+uqSlkit0OHHdc=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423114,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDhAUIPa4HJNU8Ffe3MCxu7evkE28kRr2JPx/qjG5faYX0WyQCf3B7XnfYABvvUKKs/amX3Dl26MUleY7sQiX8DuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIre3RUAZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423114,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDhAUIPa4HJNU8Ffe3MCxu7evkE28kRr2JPx/qjG5faYX0WyQCf3B7XnfYABvvUKKs/amX3Dl26MUleY7sQiX8DuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIre3RUAZ",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423113,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA5n1ZQX1Q7DnWDbG6OFmxe4enwqJLTmLqPaldAJmG1AdbmAAyJ6x5G52IumIDXQII0xGxt9zxx7Qx5s0sEMpgHuEDhAUIPa4HJNU8Ffe3MCxu7evkE28kRr2JPx/qjG5faYX0WyQCf3B7XnfYABvvUKKs/amX3Dl26MUleY7sQiX8DuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrdXhuAM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423113,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEA5n1ZQX1Q7DnWDbG6OFmxe4enwqJLTmLqPaldAJmG1AdbmAAyJ6x5G52IumIDXQII0xGxt9zxx7Qx5s0sEMpgHuEDhAUIPa4HJNU8Ffe3MCxu7evkE28kRr2JPx/qjG5faYX0WyQCf3B7XnfYABvvUKKs/amX3Dl26MUleY7sQiX8DuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrdXhuAM"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEA5n1ZQX1Q7DnWDbG6OFmxe4enwqJLTmLqPaldAJmG1AdbmAAyJ6x5G52IumIDXQII0xGxt9zxx7Qx5s0sEMpgHuEDhAUIPa4HJNU8Ffe3MCxu7evkE28kRr2JPx/qjG5faYX0WyQCf3B7XnfYABvvUKKs/amX3Dl26MUleY7sQiX8DuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrdXhuAM"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 8,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 7,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 7,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSCKArw6gvWbkHyj1kDlmweauYqkAtt8ym6D1MmX2+wTxti6RKzc4=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423112,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBlwDOy3yfnLKDFpfth43/So0RDUAcsa53zD52Pl0XprPTAnEslTGOnsdLYtDuZdkH6DpE2F4zn/qRR+hc/AvcNuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYsQjwj7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423112,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBlwDOy3yfnLKDFpfth43/So0RDUAcsa53zD52Pl0XprPTAnEslTGOnsdLYtDuZdkH6DpE2F4zn/qRR+hc/AvcNuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYsQjwj7",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423111,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBlZ+7DBlhQVOE3vefWp3lFWoffJNB/MyAStaq4N2d/zUFNeKPhVbZjj+kYLE9uHwEVq0PIGR/l9sHksPjfRxkPuEBlwDOy3yfnLKDFpfth43/So0RDUAcsa53zD52Pl0XprPTAnEslTGOnsdLYtDuZdkH6DpE2F4zn/qRR+hc/AvcNuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYs41V9K"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423111,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEBlZ+7DBlhQVOE3vefWp3lFWoffJNB/MyAStaq4N2d/zUFNeKPhVbZjj+kYLE9uHwEVq0PIGR/l9sHksPjfRxkPuEBlwDOy3yfnLKDFpfth43/So0RDUAcsa53zD52Pl0XprPTAnEslTGOnsdLYtDuZdkH6DpE2F4zn/qRR+hc/AvcNuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYs41V9K"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEBlZ+7DBlhQVOE3vefWp3lFWoffJNB/MyAStaq4N2d/zUFNeKPhVbZjj+kYLE9uHwEVq0PIGR/l9sHksPjfRxkPuEBlwDOy3yfnLKDFpfth43/So0RDUAcsa53zD52Pl0XprPTAnEslTGOnsdLYtDuZdkH6DpE2F4zn/qRR+hc/AvcNuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYs41V9K"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSCaDvdd2E2VaG+E002HFNFXNih0aUVoTvVSBDpz5OMGuMwF5nskM=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423110,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEADBGi3t6o7bKm85pcY5rKQq/1nBSXM3689Wz+FM9G7fT4xDHxQvOHb4zryeIFWWYu+xrjWSgJSgk6RDzPQ3qAJuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDcyMXC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423110,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEADBGi3t6o7bKm85pcY5rKQq/1nBSXM3689Wz+FM9G7fT4xDHxQvOHb4zryeIFWWYu+xrjWSgJSgk6RDzPQ3qAJuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDcyMXC",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423109,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEADBGi3t6o7bKm85pcY5rKQq/1nBSXM3689Wz+FM9G7fT4xDHxQvOHb4zryeIFWWYu+xrjWSgJSgk6RDzPQ3qAJuEC3EO8FjjUpQ3nYg3qwoi4K3LV9fQFsR4W7LfCSN0e/qzFp1RyB9h755CyuGpIQSTE4SKXwlPKGgETEox3VOGQCuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMB0ZDIO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423109,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEADBGi3t6o7bKm85pcY5rKQq/1nBSXM3689Wz+FM9G7fT4xDHxQvOHb4zryeIFWWYu+xrjWSgJSgk6RDzPQ3qAJuEC3EO8FjjUpQ3nYg3qwoi4K3LV9fQFsR4W7LfCSN0e/qzFp1RyB9h755CyuGpIQSTE4SKXwlPKGgETEox3VOGQCuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMB0ZDIO"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEADBGi3t6o7bKm85pcY5rKQq/1nBSXM3689Wz+FM9G7fT4xDHxQvOHb4zryeIFWWYu+xrjWSgJSgk6RDzPQ3qAJuEC3EO8FjjUpQ3nYg3qwoi4K3LV9fQFsR4W7LfCSN0e/qzFp1RyB9h755CyuGpIQSTE4SKXwlPKGgETEox3VOGQCuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMB0ZDIO"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSCqDvDJM0iYilO7grS80Txf4hicibVZxVjY6HZsJzTJ5ymvTCHoU=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423108,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC0366OClAKmJN5ZZcTjtlpFOimBzqkHLY1xNP5Qcyi6+6x474rC/aF+CTGiZzu0c8Kp9HHrq6G0/vm9olaYj4BuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpqxliqj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423108,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC0366OClAKmJN5ZZcTjtlpFOimBzqkHLY1xNP5Qcyi6+6x474rC/aF+CTGiZzu0c8Kp9HHrq6G0/vm9olaYj4BuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpqxliqj",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423107,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC0366OClAKmJN5ZZcTjtlpFOimBzqkHLY1xNP5Qcyi6+6x474rC/aF+CTGiZzu0c8Kp9HHrq6G0/vm9olaYj4BuEDWd4ddOpK7oCGr7vyDs+2AHffN9bhr8SxxFfcWh2KPXwr/0TlW2WBM2rLDV8OPCXMxmJGQr8Am5O3eAufWI3YIuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoCWyeK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423107,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEC0366OClAKmJN5ZZcTjtlpFOimBzqkHLY1xNP5Qcyi6+6x474rC/aF+CTGiZzu0c8Kp9HHrq6G0/vm9olaYj4BuEDWd4ddOpK7oCGr7vyDs+2AHffN9bhr8SxxFfcWh2KPXwr/0TlW2WBM2rLDV8OPCXMxmJGQr8Am5O3eAufWI3YIuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoCWyeK"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "state": "tx_+NILAfiEuEC0366OClAKmJN5ZZcTjtlpFOimBzqkHLY1xNP5Qcyi6+6x474rC/aF+CTGiZzu0c8Kp9HHrq6G0/vm9olaYj4BuEDWd4ddOpK7oCGr7vyDs+2AHffN9bhr8SxxFfcWh2KPXwr/0TlW2WBM2rLDV8OPCXMxmJGQr8Am5O3eAufWI3YIuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoCWyeK"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 9,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 9,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 10,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 10,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
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
    ],
    "contracts": [
      "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+nj4mXf0UdfJRgm4L5FbVvJgFx3rUgij/Xg1PD7l735AYP4T6BjO/y9fLVcbbq+euGKspkj0geiEzuawl02EAKTT5+k/+2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/X4lKCT6ePiZd/RR18lGCbgvkVtW8mAXHetSCKP9eDU8PuXvfhxgICAgICAoGM7/L18tVxtur564YqymSPSB6ITO5rCXTYQApNPn6T/gICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOg+mQXDaDbOGWcenHslGbmWzbWwhDP56xU7w5Sk/D5c72AgICAgID4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAH4SaD6ZBcNoNs4ZZx6ceyUZuZbNtbCEM/nrFTvDlKT8PlzveegN8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSFxAoBAArj4qDemVZJFGKoVINblPxU/hE+HqQP9b6ZjgvOmxY6jZAfTsDA+Qap+QamoLHf8VwmQd/h60Cq2gFj327dttU0dUjlsD+6exE6jEU6+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPkDtqCFzPTTiFBffe8P/CRAwQy7JB9ShQRel6dQYB7SuYQmlvkDkoCgHdyouV7WvK8NcjTQvraEYvxQpM3YKd3dXGkU6L2B2IyAgICAgICAgICAgICAgLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAK+Gagsd/xXCZB3+HrQKraAWPfbt221TR1SOWwP7p7ETqMRTr4Q6EAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSghcz004hQX33vD/wkQMEMuyQfUoUEXpenUGAe0rmEJpb45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMps2tw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ],
    "contracts": [
      "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+nj4mXf0UdfJRgm4L5FbVvJgFx3rUgij/Xg1PD7l735AYP4T6BjO/y9fLVcbbq+euGKspkj0geiEzuawl02EAKTT5+k/+2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/X4lKCT6ePiZd/RR18lGCbgvkVtW8mAXHetSCKP9eDU8PuXvfhxgICAgICAoGM7/L18tVxtur564YqymSPSB6ITO5rCXTYQApNPn6T/gICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOg+mQXDaDbOGWcenHslGbmWzbWwhDP56xU7w5Sk/D5c72AgICAgID4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAH4SaD6ZBcNoNs4ZZx6ceyUZuZbNtbCEM/nrFTvDlKT8PlzveegN8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSFxAoBAArj4qDemVZJFGKoVINblPxU/hE+HqQP9b6ZjgvOmxY6jZAfTsDA+Qap+QamoLHf8VwmQd/h60Cq2gFj327dttU0dUjlsD+6exE6jEU6+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPkDtqCFzPTTiFBffe8P/CRAwQy7JB9ShQRel6dQYB7SuYQmlvkDkoCgHdyouV7WvK8NcjTQvraEYvxQpM3YKd3dXGkU6L2B2IyAgICAgICAgICAgICAgLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAK+Gagsd/xXCZB3+HrQKraAWPfbt221TR1SOWwP7p7ETqMRTr4Q6EAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSghcz004hQX33vD/wkQMEMuyQfUoUEXpenUGAe0rmEJpb45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMps2tw=="
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
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303423106,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423106,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QL7ggJuAbkC9PkC8T8B+QLsuLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdO8fPBmaSVPqmgiBusf3LOGDDJVgVOLC2Epltiext0tvuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQoKoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTbNpXWijWsOX49kkYUP/zdszoKl6Vbyhsx2OfNGEmwErhx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEICKEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggHOoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMC4ufi3QAG4QKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0lX7zIei0DGZIYw95F0AjiQn31YgQLzQWxawu/lJrdBK4cfhvKQKhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChBwehBafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0AYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdFUTlMupXff6BHiZkecmAU9bxHaOfhOFn4Tz6N0u2IMQuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQkJoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwOa/sTo=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC0366OClAKmJN5ZZcTjtlpFOimBzqkHLY1xNP5Qcyi6+6x474rC/aF+CTGiZzu0c8Kp9HHrq6G0/vm9olaYj4BuEDWd4ddOpK7oCGr7vyDs+2AHffN9bhr8SxxFfcWh2KPXwr/0TlW2WBM2rLDV8OPCXMxmJGQr8Am5O3eAufWI3YIuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoCWyeK",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1h0sosw=="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423105,
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "gas_price": 1000006258
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423105,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "signed_tx": "tx_+Qi7CwHAuQi1+QiyggIJAaEGEC4OThKj27oIfM8N6AVqYe9LWzuNxFW+JO52YPRf21KhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChuNT40gsB+IS4QLTfro4KUAqYk3lllxOO2WkU6KYHOqQctjXE0/lBzKLr7rHjvisL9oX4JMaJnO7Rzwqn0ceurobT++b2iVpiPgG4QNZ3h106krugIavu/IOz7YAd9831uGvxLHEV9xaHYo9fCv/ROVbZYEzassNXw48JczGYkZCvwCbk7d4C59Yjdgi4SPhGOQKhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSCqDvDJM0iYilO7grS80Txf4hicibVZxVjY6HZsJzTJ5ymgu4uPi2ggI+AaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGhBafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0AQqDD0JAhDua4nK4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgkiJuzXVi6uXIKRxrYJPU28t81iwq5/yr0NARZt5D15e5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaKnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdBABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQALkDiPkDhUABoKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0uQNf+QNcKAGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdO8fPBmaSVPqmgiBusf3LOGDDJVgVOLC2Epltiext0tvuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQoKoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2q6UABoKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0hcQKAQAKsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/UAhwHB0hmxuqgJ8teTlg==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1000006258,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+Qj+CwH4QrhAgUQfeulp7/TWYZhsoNST6TuIsr5ONbMg2Z0Ba4LKtWwG2crWH/Z/C7LeHfkOwKNZDIhIRnuCintuKn+UP0vQC7kItfkIsoICCQGhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEC0366OClAKmJN5ZZcTjtlpFOimBzqkHLY1xNP5Qcyi6+6x474rC/aF+CTGiZzu0c8Kp9HHrq6G0/vm9olaYj4BuEDWd4ddOpK7oCGr7vyDs+2AHffN9bhr8SxxFfcWh2KPXwr/0TlW2WBM2rLDV8OPCXMxmJGQr8Am5O3eAufWI3YIuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoLuLj4toICPgGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAEKgw9CQIQ7muJyuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoJIibs11YurlyCkca2CT1NvLfNYsKuf8q9DQEWbeQ9eXuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1AIcBwdIZsbqoCfmpnvE="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAgUQfeulp7/TWYZhsoNST6TuIsr5ONbMg2Z0Ba4LKtWwG2crWH/Z/C7LeHfkOwKNZDIhIRnuCintuKn+UP0vQC7kItfkIsoICCQGhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEC0366OClAKmJN5ZZcTjtlpFOimBzqkHLY1xNP5Qcyi6+6x474rC/aF+CTGiZzu0c8Kp9HHrq6G0/vm9olaYj4BuEDWd4ddOpK7oCGr7vyDs+2AHffN9bhr8SxxFfcWh2KPXwr/0TlW2WBM2rLDV8OPCXMxmJGQr8Am5O3eAufWI3YIuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoLuLj4toICPgGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAEKgw9CQIQ7muJyuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoJIibs11YurlyCkca2CT1NvLfNYsKuf8q9DQEWbeQ9eXuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1AIcBwdIZsbqoCfmpnvE=",
      "type": "channel_force_progress_tx"
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAgUQfeulp7/TWYZhsoNST6TuIsr5ONbMg2Z0Ba4LKtWwG2crWH/Z/C7LeHfkOwKNZDIhIRnuCintuKn+UP0vQC7kItfkIsoICCQGhBhAuDk4So9u6CHzPDegFamHvS1s7jcRVviTudmD0X9tSoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEC0366OClAKmJN5ZZcTjtlpFOimBzqkHLY1xNP5Qcyi6+6x474rC/aF+CTGiZzu0c8Kp9HHrq6G0/vm9olaYj4BuEDWd4ddOpK7oCGr7vyDs+2AHffN9bhr8SxxFfcWh2KPXwr/0TlW2WBM2rLDV8OPCXMxmJGQr8Am5O3eAufWI3YIuEj4RjkCoQYQLg5OEqPbugh8zw3oBWph70tbO43EVb4k7nZg9F/bUgqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpoLuLj4toICPgGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAEKgw9CQIQ7muJyuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoJIibs11YurlyCkca2CT1NvLfNYsKuf8q9DQEWbeQ9eXuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1AIcBwdIZsbqoCfmpnvE=",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423104,
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
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423104,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423103,
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
    "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
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
  "channel_id": "ch_88J3wWJGTNr8qUnNvwZMUAxLMJUiyzadG66YkTreTBFQtY4QV",
  "id": -576460752303423103,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection

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
      "fsm_id": "ba_iM3yf+z9AbAnLPKyiJb+1rWMHqO+qAR+b0UVcwPNRyDUEfaQ"
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
      "fsm_id": "ba_9QthMev4a+Sz0tu0cSItLyZ0Y2j7h80XBJMSY73IXGjHSfzr"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYeWjrReg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423102,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDIKFez1YzSGT/bPWRzpZn412gQ9P/g6hSnIu7M4S/08ugSt8NKeh39BnNWrpYTvDwUSILnD45L/3VxTzmPwi4HuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGHtq0iQM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423102,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_9QthMev4a+Sz0tu0cSItLyZ0Y2j7h80XBJMSY73IXGjHSfzr"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDIKFez1YzSGT/bPWRzpZn412gQ9P/g6hSnIu7M4S/08ugSt8NKeh39BnNWrpYTvDwUSILnD45L/3VxTzmPwi4HuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGHtq0iQM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423101,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhABtBna0Y2bUwy5zGclF7o5aioePysg2Wt/WmB3FZOXT7A/3wEilh8UO3oc6Mghc4+RbADFgoEffH+RwmELMiCBrhAyChXs9WM0hk/2z1kc6WZ+NdoEPT/4OoUpyLuzOEv9PLoErfDSnod/QZzVq6WE7w8FEiC5w+OS/91cU85j8IuB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh47t7yd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423101,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhABtBna0Y2bUwy5zGclF7o5aioePysg2Wt/WmB3FZOXT7A/3wEilh8UO3oc6Mghc4+RbADFgoEffH+RwmELMiCBrhAyChXs9WM0hk/2z1kc6WZ+NdoEPT/4OoUpyLuzOEv9PLoErfDSnod/QZzVq6WE7w8FEiC5w+OS/91cU85j8IuB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh47t7yd",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_iM3yf+z9AbAnLPKyiJb+1rWMHqO+qAR+b0UVcwPNRyDUEfaQ"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhABtBna0Y2bUwy5zGclF7o5aioePysg2Wt/WmB3FZOXT7A/3wEilh8UO3oc6Mghc4+RbADFgoEffH+RwmELMiCBrhAyChXs9WM0hk/2z1kc6WZ+NdoEPT/4OoUpyLuzOEv9PLoErfDSnod/QZzVq6WE7w8FEiC5w+OS/91cU85j8IuB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh47t7yd",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABtBna0Y2bUwy5zGclF7o5aioePysg2Wt/WmB3FZOXT7A/3wEilh8UO3oc6Mghc4+RbADFgoEffH+RwmELMiCBrhAyChXs9WM0hk/2z1kc6WZ+NdoEPT/4OoUpyLuzOEv9PLoErfDSnod/QZzVq6WE7w8FEiC5w+OS/91cU85j8IuB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh47t7yd",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABtBna0Y2bUwy5zGclF7o5aioePysg2Wt/WmB3FZOXT7A/3wEilh8UO3oc6Mghc4+RbADFgoEffH+RwmELMiCBrhAyChXs9WM0hk/2z1kc6WZ+NdoEPT/4OoUpyLuzOEv9PLoErfDSnod/QZzVq6WE7w8FEiC5w+OS/91cU85j8IuB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh47t7yd",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "message": {
        "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "message": {
        "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
  "id": -576460752303423100,
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
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423100,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+QENCwH4hLhABtBna0Y2bUwy5zGclF7o5aioePysg2Wt/WmB3FZOXT7A/3wEilh8UO3oc6Mghc4+RbADFgoEffH+RwmELMiCBrhAyChXs9WM0hk/2z1kc6WZ+NdoEPT/4OoUpyLuzOEv9PLoErfDSnod/QZzVq6WE7w8FEiC5w+OS/91cU85j8IuB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh47t7yd"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+QENCwH4hLhABtBna0Y2bUwy5zGclF7o5aioePysg2Wt/WmB3FZOXT7A/3wEilh8UO3oc6Mghc4+RbADFgoEffH+RwmELMiCBrhAyChXs9WM0hk/2z1kc6WZ+NdoEPT/4OoUpyLuzOEv9PLoErfDSnod/QZzVq6WE7w8FEiC5w+OS/91cU85j8IuB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rh47t7yd"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxIAqDq2JFeO2C5etnX2pMEkSiBS8W5pwfxCyOyJ0evVuwZpSuHcR8=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "vm_version": 6
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
  "id": -576460752303423099,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAp41Qfim5fGjn/ycxNuqjN6Cx95XYqlSjbj4b+4vViQ/EXt+eChxCgHmOY6JIRJMPKYIK2GCVahTjAOwKMQyQFuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaUaMohb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423099,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAp41Qfim5fGjn/ycxNuqjN6Cx95XYqlSjbj4b+4vViQ/EXt+eChxCgHmOY6JIRJMPKYIK2GCVahTjAOwKMQyQFuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaUaMohb",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "vm_version": 6
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
  "id": -576460752303423098,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEALOnlcwuQiBxg1czupidqzevUXXVd0kEEQ/4Yl6NC0/V+Fq8IEtAqjuVAsVxK4avYY/NPEBmz8ZxS4rJ7Lo10JuEAp41Qfim5fGjn/ycxNuqjN6Cx95XYqlSjbj4b+4vViQ/EXt+eChxCgHmOY6JIRJMPKYIK2GCVahTjAOwKMQyQFuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaVCdQfd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423098,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEALOnlcwuQiBxg1czupidqzevUXXVd0kEEQ/4Yl6NC0/V+Fq8IEtAqjuVAsVxK4avYY/NPEBmz8ZxS4rJ7Lo10JuEAp41Qfim5fGjn/ycxNuqjN6Cx95XYqlSjbj4b+4vViQ/EXt+eChxCgHmOY6JIRJMPKYIK2GCVahTjAOwKMQyQFuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaVCdQfd"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEALOnlcwuQiBxg1czupidqzevUXXVd0kEEQ/4Yl6NC0/V+Fq8IEtAqjuVAsVxK4avYY/NPEBmz8ZxS4rJ7Lo10JuEAp41Qfim5fGjn/ycxNuqjN6Cx95XYqlSjbj4b+4vViQ/EXt+eChxCgHmOY6JIRJMPKYIK2GCVahTjAOwKMQyQFuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaVCdQfd"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxIA6Cm9p/X/sj7d/Fojx33FpDvS5QO+zGwfIj8fNzJCQarloH6Ulc=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423097,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBqD3XFoadpJI2bqOrAf408q8Wb4C7/I3zJcmc2MNKPgxw09LDsTgWe14OOauLlAtsEtE59BdXU+Z5bZA20AIALuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5aqP2dA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423097,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBqD3XFoadpJI2bqOrAf408q8Wb4C7/I3zJcmc2MNKPgxw09LDsTgWe14OOauLlAtsEtE59BdXU+Z5bZA20AIALuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5aqP2dA",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423096,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAjQLcU1EeGIcNZ3VHF8lRD+LX4k2bqeLB1LqGYTDUTl3r8JjqdkzifZpoMcW2vViX5XXANrtHVam3ZdUPYOrsEuEBqD3XFoadpJI2bqOrAf408q8Wb4C7/I3zJcmc2MNKPgxw09LDsTgWe14OOauLlAtsEtE59BdXU+Z5bZA20AIALuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5YWJVeI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423096,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEAjQLcU1EeGIcNZ3VHF8lRD+LX4k2bqeLB1LqGYTDUTl3r8JjqdkzifZpoMcW2vViX5XXANrtHVam3ZdUPYOrsEuEBqD3XFoadpJI2bqOrAf408q8Wb4C7/I3zJcmc2MNKPgxw09LDsTgWe14OOauLlAtsEtE59BdXU+Z5bZA20AIALuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5YWJVeI"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEAjQLcU1EeGIcNZ3VHF8lRD+LX4k2bqeLB1LqGYTDUTl3r8JjqdkzifZpoMcW2vViX5XXANrtHVam3ZdUPYOrsEuEBqD3XFoadpJI2bqOrAf408q8Wb4C7/I3zJcmc2MNKPgxw09LDsTgWe14OOauLlAtsEtE59BdXU+Z5bZA20AIALuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5YWJVeI"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 4,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 3,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 3,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxIBKDNKNGDVqG8FrLwhQ9R1EVsMVs35QMovKvtD1RlwmEHy+xtFpI=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423095,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBVsPTDvMVYLc1WVo1r3FKrazkRnGt8KP2nrOmvEt73/YPYInZjQGRPK437hToGYkkrYHPj094pVOOtXw5jpcMOuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSASgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8tdAA1g"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423095,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBVsPTDvMVYLc1WVo1r3FKrazkRnGt8KP2nrOmvEt73/YPYInZjQGRPK437hToGYkkrYHPj094pVOOtXw5jpcMOuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSASgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8tdAA1g",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423094,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA0lJCHOKOx5qMs7uQ4fmaUFEl/zdtvdLAxlnLJcMQY/RcR1qq//PRwVyUcuXkV/xq001/TxmjFnqO4KXv7y08DuEBVsPTDvMVYLc1WVo1r3FKrazkRnGt8KP2nrOmvEt73/YPYInZjQGRPK437hToGYkkrYHPj094pVOOtXw5jpcMOuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSASgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8sGQznl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423094,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEA0lJCHOKOx5qMs7uQ4fmaUFEl/zdtvdLAxlnLJcMQY/RcR1qq//PRwVyUcuXkV/xq001/TxmjFnqO4KXv7y08DuEBVsPTDvMVYLc1WVo1r3FKrazkRnGt8KP2nrOmvEt73/YPYInZjQGRPK437hToGYkkrYHPj094pVOOtXw5jpcMOuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSASgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8sGQznl"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEA0lJCHOKOx5qMs7uQ4fmaUFEl/zdtvdLAxlnLJcMQY/RcR1qq//PRwVyUcuXkV/xq001/TxmjFnqO4KXv7y08DuEBVsPTDvMVYLc1WVo1r3FKrazkRnGt8KP2nrOmvEt73/YPYInZjQGRPK437hToGYkkrYHPj094pVOOtXw5jpcMOuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSASgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8sGQznl"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxIBaBKd77tzS0/F6PJCGNIxM1ROuq8JugHifpaqYptO+bBSpqjSQw=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423093,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDzyqTzdto2XCP9ZOl666ocQyUBf5s4qX5j4cnqvnoxYMA9BjEDx5sGIhJdlLoMzT9JqDXULruUvH53W94dC7cIuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUp2UpeK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423093,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDzyqTzdto2XCP9ZOl666ocQyUBf5s4qX5j4cnqvnoxYMA9BjEDx5sGIhJdlLoMzT9JqDXULruUvH53W94dC7cIuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUp2UpeK",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423092,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBA3RY8FCJMI1mUgyMtk0Z3e4WhsDWYi6aAjRNf0ZT7JT39wHmpNO+wUr5deNTf3MQ4tU6Uhp8mg2sg/1833EkIuEDzyqTzdto2XCP9ZOl666ocQyUBf5s4qX5j4cnqvnoxYMA9BjEDx5sGIhJdlLoMzT9JqDXULruUvH53W94dC7cIuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUpWZ+qm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423092,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEBA3RY8FCJMI1mUgyMtk0Z3e4WhsDWYi6aAjRNf0ZT7JT39wHmpNO+wUr5deNTf3MQ4tU6Uhp8mg2sg/1833EkIuEDzyqTzdto2XCP9ZOl666ocQyUBf5s4qX5j4cnqvnoxYMA9BjEDx5sGIhJdlLoMzT9JqDXULruUvH53W94dC7cIuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUpWZ+qm"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEBA3RY8FCJMI1mUgyMtk0Z3e4WhsDWYi6aAjRNf0ZT7JT39wHmpNO+wUr5deNTf3MQ4tU6Uhp8mg2sg/1833EkIuEDzyqTzdto2XCP9ZOl666ocQyUBf5s4qX5j4cnqvnoxYMA9BjEDx5sGIhJdlLoMzT9JqDXULruUvH53W94dC7cIuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUpWZ+qm"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxIBqC3bXBFip8XRh2sPOpYKl5Tsa8eif2V7m95M5kSLfvPhGxh/r4=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423091,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECu4TzSQQII2kq/K2KvxsCZNFuLm3hK+Iz6I6m0n9Vh+Q0vzgTnbVjmB9dFQvEBHAdKjGfsyZo8WbenD1amB1sJuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4RAPj/M"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423091,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+JALAfhCuECu4TzSQQII2kq/K2KvxsCZNFuLm3hK+Iz6I6m0n9Vh+Q0vzgTnbVjmB9dFQvEBHAdKjGfsyZo8WbenD1amB1sJuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4RAPj/M",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423090,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAnlKFAKk6fBV3guEXVrEI6u0E8JmCKuLBZgn/Rm51fu+JTlcarGKF/A9aeQl8nplo6EQWk9KzQevEgpw8IYLMOuECu4TzSQQII2kq/K2KvxsCZNFuLm3hK+Iz6I6m0n9Vh+Q0vzgTnbVjmB9dFQvEBHAdKjGfsyZo8WbenD1amB1sJuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4Q3puNG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423090,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEAnlKFAKk6fBV3guEXVrEI6u0E8JmCKuLBZgn/Rm51fu+JTlcarGKF/A9aeQl8nplo6EQWk9KzQevEgpw8IYLMOuECu4TzSQQII2kq/K2KvxsCZNFuLm3hK+Iz6I6m0n9Vh+Q0vzgTnbVjmB9dFQvEBHAdKjGfsyZo8WbenD1amB1sJuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4Q3puNG"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEAnlKFAKk6fBV3guEXVrEI6u0E8JmCKuLBZgn/Rm51fu+JTlcarGKF/A9aeQl8nplo6EQWk9KzQevEgpw8IYLMOuECu4TzSQQII2kq/K2KvxsCZNFuLm3hK+Iz6I6m0n9Vh+Q0vzgTnbVjmB9dFQvEBHAdKjGfsyZo8WbenD1amB1sJuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4Q3puNG"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 5,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 5,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 6,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 6,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 3,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 3,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxIB6D74ts0zr84T5TVF7oGz5iXPWmsFJZUntsqbVWLyrZFu2rBzY0=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423089,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECn8gwnW/zoiRl7hzULS0wEkkAO14r5JAG8QW1+vZqz/xNfJ3Xo01ImzrXSxbBL63Fl9KHRRvnjYCgNYOne3z4NuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAeg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2RbvhU3Es"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423089,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+JALAfhCuECn8gwnW/zoiRl7hzULS0wEkkAO14r5JAG8QW1+vZqz/xNfJ3Xo01ImzrXSxbBL63Fl9KHRRvnjYCgNYOne3z4NuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAeg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2RbvhU3Es",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423088,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBhthx9b6NUZz1HUZFgO+o1dTzDsqolYoDxpuAU7WZnC6N+Oq0jPxB51XwSvGiNLV69BDio4IwlTb3DLFEurlwKuECn8gwnW/zoiRl7hzULS0wEkkAO14r5JAG8QW1+vZqz/xNfJ3Xo01ImzrXSxbBL63Fl9KHRRvnjYCgNYOne3z4NuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAeg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2RbvHW3Dr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423088,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEBhthx9b6NUZz1HUZFgO+o1dTzDsqolYoDxpuAU7WZnC6N+Oq0jPxB51XwSvGiNLV69BDio4IwlTb3DLFEurlwKuECn8gwnW/zoiRl7hzULS0wEkkAO14r5JAG8QW1+vZqz/xNfJ3Xo01ImzrXSxbBL63Fl9KHRRvnjYCgNYOne3z4NuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAeg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2RbvHW3Dr"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEBhthx9b6NUZz1HUZFgO+o1dTzDsqolYoDxpuAU7WZnC6N+Oq0jPxB51XwSvGiNLV69BDio4IwlTb3DLFEurlwKuECn8gwnW/zoiRl7hzULS0wEkkAO14r5JAG8QW1+vZqz/xNfJ3Xo01ImzrXSxbBL63Fl9KHRRvnjYCgNYOne3z4NuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAeg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2RbvHW3Dr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 8,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 7,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 7,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxICKDZkikRwm9X2aF5+LO31nSuNfLOTaNdzsgt0BKS68TOQT6yVG0=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423087,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAcByuek9AKK5S7dXf2FCCyLiikldAhfhnSR+poF7EmIJ7pJldoHWNZ0U9cNG9APZijRjj7OxX9q7yCrtl0vMwHuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkFTktKl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423087,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAcByuek9AKK5S7dXf2FCCyLiikldAhfhnSR+poF7EmIJ7pJldoHWNZ0U9cNG9APZijRjj7OxX9q7yCrtl0vMwHuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkFTktKl",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423086,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAcByuek9AKK5S7dXf2FCCyLiikldAhfhnSR+poF7EmIJ7pJldoHWNZ0U9cNG9APZijRjj7OxX9q7yCrtl0vMwHuEDx4THwZCtDkiL16aULckh14qlNhv2cCkL++8DmLi4v1dLc6EfPCpENUDFZPtCxc7hY3uEvUmJvsI2hkSpbXHYFuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkGXISzG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423086,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEAcByuek9AKK5S7dXf2FCCyLiikldAhfhnSR+poF7EmIJ7pJldoHWNZ0U9cNG9APZijRjj7OxX9q7yCrtl0vMwHuEDx4THwZCtDkiL16aULckh14qlNhv2cCkL++8DmLi4v1dLc6EfPCpENUDFZPtCxc7hY3uEvUmJvsI2hkSpbXHYFuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkGXISzG"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEAcByuek9AKK5S7dXf2FCCyLiikldAhfhnSR+poF7EmIJ7pJldoHWNZ0U9cNG9APZijRjj7OxX9q7yCrtl0vMwHuEDx4THwZCtDkiL16aULckh14qlNhv2cCkL++8DmLi4v1dLc6EfPCpENUDFZPtCxc7hY3uEvUmJvsI2hkSpbXHYFuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkGXISzG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxICaC6d6qpJPpXzCbSkKxdCaIDbRV0C8Var9vBF6xgzDqRcSQycF4=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423085,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB9SK2nr0a8BtX/6Mo6SwvGYtEiNzdrVOFOGpkKywioBFsbgbue/79RB7VIim9GoLhVnjyf4ivAyV45GC6J7AsMuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXEdGepC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423085,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB9SK2nr0a8BtX/6Mo6SwvGYtEiNzdrVOFOGpkKywioBFsbgbue/79RB7VIim9GoLhVnjyf4ivAyV45GC6J7AsMuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXEdGepC",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423084,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB9SK2nr0a8BtX/6Mo6SwvGYtEiNzdrVOFOGpkKywioBFsbgbue/79RB7VIim9GoLhVnjyf4ivAyV45GC6J7AsMuEDaNGfR7taKCqZ6xhdo6N2zJQ3oFmxPKBmUu72o1MR8YIUjRy8ByUj3hX/RisiJCFjI9Kk6hZI8EYuWZN0UM0AOuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXGQCjJF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423084,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEB9SK2nr0a8BtX/6Mo6SwvGYtEiNzdrVOFOGpkKywioBFsbgbue/79RB7VIim9GoLhVnjyf4ivAyV45GC6J7AsMuEDaNGfR7taKCqZ6xhdo6N2zJQ3oFmxPKBmUu72o1MR8YIUjRy8ByUj3hX/RisiJCFjI9Kk6hZI8EYuWZN0UM0AOuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXGQCjJF"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEB9SK2nr0a8BtX/6Mo6SwvGYtEiNzdrVOFOGpkKywioBFsbgbue/79RB7VIim9GoLhVnjyf4ivAyV45GC6J7AsMuEDaNGfR7taKCqZ6xhdo6N2zJQ3oFmxPKBmUu72o1MR8YIUjRy8ByUj3hX/RisiJCFjI9Kk6hZI8EYuWZN0UM0AOuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXGQCjJF"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxICqCipoS6aEYC2966NhN/h18AIP4uJRH+0o1rYv9JCQweKc9azHU=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423083,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAbdTmZYNTspIkXkEx5Huqo7edzS9ptHmAxj+s7Fmz57aeiLS0I3gy5ENPGGjQgH76SyXZgeRppVdeGXF+6q6sPuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHimD2w07"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423083,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAbdTmZYNTspIkXkEx5Huqo7edzS9ptHmAxj+s7Fmz57aeiLS0I3gy5ENPGGjQgH76SyXZgeRppVdeGXF+6q6sPuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHimD2w07",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423082,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAbdTmZYNTspIkXkEx5Huqo7edzS9ptHmAxj+s7Fmz57aeiLS0I3gy5ENPGGjQgH76SyXZgeRppVdeGXF+6q6sPuECcfIsipCEX8kOwoRfI8jGB/DSs2qPPxvX8NN+TW14PkxpuqvGM4EBQEGUTq+dyUgsSfVF/Dpqo7dDu7zC9nkAKuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHinxig91"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423082,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEAbdTmZYNTspIkXkEx5Huqo7edzS9ptHmAxj+s7Fmz57aeiLS0I3gy5ENPGGjQgH76SyXZgeRppVdeGXF+6q6sPuECcfIsipCEX8kOwoRfI8jGB/DSs2qPPxvX8NN+TW14PkxpuqvGM4EBQEGUTq+dyUgsSfVF/Dpqo7dDu7zC9nkAKuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHinxig91"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "state": "tx_+NILAfiEuEAbdTmZYNTspIkXkEx5Huqo7edzS9ptHmAxj+s7Fmz57aeiLS0I3gy5ENPGGjQgH76SyXZgeRppVdeGXF+6q6sPuECcfIsipCEX8kOwoRfI8jGB/DSs2qPPxvX8NN+TW14PkxpuqvGM4EBQEGUTq+dyUgsSfVF/Dpqo7dDu7zC9nkAKuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHinxig91"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 9,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 9,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 10,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 10,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ],
    "contracts": [
      "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg/xaYlQYtkCkvjp91m5wWsQ67/29bJLlTqoRwdx8JMon5AYP4SaAKIVXE2JtsG1AvpAThaffPRfTfrHqdTK+V+RPcjbtnM+egM4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAr4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6D+4wSC4Ve0F0tyKnD2rVhkBjbEeUnr+0Bzo45NLq2lse2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKf/f4lKD/FpiVBi2QKS+On3WbnBaxDrv/b1skuVOqhHB3HwkyifhxgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGoAohVcTYm2wbUC+kBOFp989F9N+sep1Mr5X5E9yNu2czgKD+4wSC4Ve0F0tyKnD2rVhkBjbEeUnr+0Bzo45NLq2lsYCAgICAgIDj4qBgbM3ZZuQk0sQk/jDaBJq7fvfw8KsOhCO0TPQkyC6Zh8DA+Qap+QamoGLD/LH3mW6RzNEkDR/57kVtMnGZ1jYiqZGdt8o1nJT3+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGLD/LH3mW6RzNEkDR/57kVtMnGZ1jYiqZGdt8o1nJT3+EOhAHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQoHGbA5JQinbIb4EDcQfsvluiJG5kFC58N0+I36KKU6ul+QO2oHGbA5JQinbIb4EDcQfsvluiJG5kFC58N0+I36KKU6ul+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDA4wJ+2Q=="
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
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ],
    "contracts": [
      "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg/xaYlQYtkCkvjp91m5wWsQ67/29bJLlTqoRwdx8JMon5AYP4SaAKIVXE2JtsG1AvpAThaffPRfTfrHqdTK+V+RPcjbtnM+egM4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAr4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6D+4wSC4Ve0F0tyKnD2rVhkBjbEeUnr+0Bzo45NLq2lse2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKf/f4lKD/FpiVBi2QKS+On3WbnBaxDrv/b1skuVOqhHB3HwkyifhxgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGoAohVcTYm2wbUC+kBOFp989F9N+sep1Mr5X5E9yNu2czgKD+4wSC4Ve0F0tyKnD2rVhkBjbEeUnr+0Bzo45NLq2lsYCAgICAgIDj4qBgbM3ZZuQk0sQk/jDaBJq7fvfw8KsOhCO0TPQkyC6Zh8DA+Qap+QamoGLD/LH3mW6RzNEkDR/57kVtMnGZ1jYiqZGdt8o1nJT3+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGLD/LH3mW6RzNEkDR/57kVtMnGZ1jYiqZGdt8o1nJT3+EOhAHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQoHGbA5JQinbIb4EDcQfsvluiJG5kFC58N0+I36KKU6ul+QO2oHGbA5JQinbIb4EDcQfsvluiJG5kFC58N0+I36KKU6ul+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDA4wJ+2Q=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303423081,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423081,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QeoggJuAbkHofkHnj8B+QeZuLn4t0ABuEBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEO5rA+H+wkIbumEBC+DwDa4sljTu1ngCvK5eZ3yXruqsuHH4bykCoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQoKoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDkH0m6usjETybAfrEtQ3CfrQr1s+j6d+GvnkZNyHh84Lhx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEEBKEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggHOoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMC4ufi3QAG4QHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQm+Rmu9YLZ0zm9hVy7r6HZoRT5/Zf51TlFPFcyJV/5YW4cfhvKQKhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChBQWhBXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuEBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEE9oz9Xzqfg+4Ohey944Sei3uQn2KrVf2FooddUQUJfSuHH4bykCoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQkJoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhA1Bh+uKTf+hBCGPMHHle1QbNQ3/TGm1JcvGrScnDU8G7hx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EICKEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggHOoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMC4ufi3QAG4QHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQM1DqWLp7/BedNhM0eYC2/04QYqGep0w0cYLLVTpI9Ui4cfhvKQKhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BBwehBXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuEBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEB6+5MLlh4kKT5l0+6ehKbJcqRDRoGazFUIlySEPJcnGuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQYGoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYAwLi5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAPzT7MBDodQf93/uhrDTLiunfi0XHx5wpg7lCY0X3nbLhx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEDA6EFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVAMC5Ab75AbtAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAAFDjpVvkmOsl5sgNigmLHZyLKy82N6hYAtsti+JzzuLkBdPkBcSkCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQICoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEACCAT+5ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABUAwDB03es=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAbdTmZYNTspIkXkEx5Huqo7edzS9ptHmAxj+s7Fmz57aeiLS0I3gy5ENPGGjQgH76SyXZgeRppVdeGXF+6q6sPuECcfIsipCEX8kOwoRfI8jGB/DSs2qPPxvX8NN+TW14PkxpuqvGM4EBQEGUTq+dyUgsSfVF/Dpqo7dDu7zC9nkAKuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHinxig91",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABonOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC5A4j5A4VAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqELkDX/kDXCgBoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDuawPh/sJCG7phAQvg8A2uLJY07tZ4AryuXmd8l67qrLhx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EKCqEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcp/96rpQAGgc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAqw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl///PAcIg=="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423080,
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "gas_price": 1000009009
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423080,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "signed_tx": "tx_+Qi7CwHAuQi1+QiyggIJAaEGupwA+su2K/p9DtsIsrdytrHYMB7pqodiYd1LjMXljEihAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BuNT40gsB+IS4QBt1OZlg1OykiReQTHke6qjt53NL2m0eYDGP6zsWbPntp6ItLQjeDLkQ08YaNCAfvpLJdmB5GmlV14ZcX7qrqw+4QJx8iyKkIRfyQ7ChF8jyMYH8NKzao8/G9fw035NbXg+TGm6q8YzgQFAQZROr53JSCxJ9UX8Omqjt0O7vML2eQAq4SPhGOQKhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxICqCipoS6aEYC2966NhN/h18AIP4uJRH+0o1rYv9JCQweKQu4uPi2ggI+AaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GhBXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQAQqDD0JAhDua7TG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgM8G4he43lYngmW+XZ0t08YOM9SzNpwZWSqRJCN5Efu65Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaJzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEBABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQALkDiPkDhUABoHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQuQNf+QNcKAGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuEBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEO5rA+H+wkIbumEBC+DwDa4sljTu1ngCvK5eZ3yXruqsuHH4bykCoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQoKoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2w70ABoJCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yn/3qulAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEIXECgEACrDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/8AhwHB0mrKrbQfSGfWCg==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1000009009,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+Qj+CwH4QrhAQXrgkremU68G8YGyQ/wpTgfbuH82l0Z8kJKtW7i0pnzdvc96gCNNrQB6tdIhUqoA5qhdWluax+zHtqJgM/ryDLkItfkIsoICCQGhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxIoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAbdTmZYNTspIkXkEx5Huqo7edzS9ptHmAxj+s7Fmz57aeiLS0I3gy5ENPGGjQgH76SyXZgeRppVdeGXF+6q6sPuECcfIsipCEX8kOwoRfI8jGB/DSs2qPPxvX8NN+TW14PkxpuqvGM4EBQEGUTq+dyUgsSfVF/Dpqo7dDu7zC9nkAKuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHikLuLj4toICPgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAEKgw9CQIQ7mu0xuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoDPBuIXuN5WJ4Jlvl2dLdPGDjPUszacGVkqkSQjeRH7uuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABonOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC5A4j5A4VAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqELkDX/kDXCgBoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDuawPh/sJCG7phAQvg8A2uLJY07tZ4AryuXmd8l67qrLhx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EKCqEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcp/96rpQAGgc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAqw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//AIcBwdJqyq20H7NFIXs="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAQXrgkremU68G8YGyQ/wpTgfbuH82l0Z8kJKtW7i0pnzdvc96gCNNrQB6tdIhUqoA5qhdWluax+zHtqJgM/ryDLkItfkIsoICCQGhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxIoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAbdTmZYNTspIkXkEx5Huqo7edzS9ptHmAxj+s7Fmz57aeiLS0I3gy5ENPGGjQgH76SyXZgeRppVdeGXF+6q6sPuECcfIsipCEX8kOwoRfI8jGB/DSs2qPPxvX8NN+TW14PkxpuqvGM4EBQEGUTq+dyUgsSfVF/Dpqo7dDu7zC9nkAKuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHikLuLj4toICPgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAEKgw9CQIQ7mu0xuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoDPBuIXuN5WJ4Jlvl2dLdPGDjPUszacGVkqkSQjeRH7uuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABonOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC5A4j5A4VAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqELkDX/kDXCgBoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDuawPh/sJCG7phAQvg8A2uLJY07tZ4AryuXmd8l67qrLhx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EKCqEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcp/96rpQAGgc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAqw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//AIcBwdJqyq20H7NFIXs=",
      "type": "channel_force_progress_tx"
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAQXrgkremU68G8YGyQ/wpTgfbuH82l0Z8kJKtW7i0pnzdvc96gCNNrQB6tdIhUqoA5qhdWluax+zHtqJgM/ryDLkItfkIsoICCQGhBrqcAPrLtiv6fQ7bCLK3crax2DAe6aqHYmHdS4zF5YxIoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAbdTmZYNTspIkXkEx5Huqo7edzS9ptHmAxj+s7Fmz57aeiLS0I3gy5ENPGGjQgH76SyXZgeRppVdeGXF+6q6sPuECcfIsipCEX8kOwoRfI8jGB/DSs2qPPxvX8NN+TW14PkxpuqvGM4EBQEGUTq+dyUgsSfVF/Dpqo7dDu7zC9nkAKuEj4RjkCoQa6nAD6y7Yr+n0O2wiyt3K2sdgwHumqh2Jh3UuMxeWMSAqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHikLuLj4toICPgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAEKgw9CQIQ7mu0xuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoDPBuIXuN5WJ4Jlvl2dLdPGDjPUszacGVkqkSQjeRH7uuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABonOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC5A4j5A4VAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqELkDX/kDXCgBoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDuawPh/sJCG7phAQvg8A2uLJY07tZ4AryuXmd8l67qrLhx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EKCqEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcp/96rpQAGgc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAqw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//AIcBwdJqyq20H7NFIXs=",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423079,
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
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423079,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423078,
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
    "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
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
  "channel_id": "ch_2RBgp5pQn9xwApD391ZZXha5wa1ptPvEPcH963jc7bWEgEJdgr",
  "id": -576460752303423078,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection

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
      "fsm_id": "ba_lDDzrzMIOKS7iMcKZLgsC9DC9mvCUlj19Yz8W2rPjEgIujKN"
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
      "fsm_id": "ba_hXH5PsGXBWluah7VFN/oZViRNs1XzavL1IZR+27y3sd/kDG/"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYg9tL8qQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423077,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAlIdZlsB2AV2VQrE++7hbWp7sYiWcEyXjlMFmAKJnxnVDw8z3/Doo9PWofkRsQRGtsnwPizXntY0z9XIOweIMLuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGIAkcfvE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423077,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_hXH5PsGXBWluah7VFN/oZViRNs1XzavL1IZR+27y3sd/kDG/"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAlIdZlsB2AV2VQrE++7hbWp7sYiWcEyXjlMFmAKJnxnVDw8z3/Doo9PWofkRsQRGtsnwPizXntY0z9XIOweIMLuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGIAkcfvE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423076,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAJSHWZbAdgFdlUKxPvu4W1qe7GIlnBMl45TBZgCiZ8Z1Q8PM9/w6KPT1qH5EbEERrbJ8D4s157WNM/VyDsHiDC7hAozMQsHNcSiCzgJoRHxYPcWvVsyYp7MWRaWy98EP+E0+iXLr2wA7OF9WLPo4KIGAYSnj6Haw0RYOoNQdONo3hALiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RiAKQHaR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423076,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAJSHWZbAdgFdlUKxPvu4W1qe7GIlnBMl45TBZgCiZ8Z1Q8PM9/w6KPT1qH5EbEERrbJ8D4s157WNM/VyDsHiDC7hAozMQsHNcSiCzgJoRHxYPcWvVsyYp7MWRaWy98EP+E0+iXLr2wA7OF9WLPo4KIGAYSnj6Haw0RYOoNQdONo3hALiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RiAKQHaR",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_lDDzrzMIOKS7iMcKZLgsC9DC9mvCUlj19Yz8W2rPjEgIujKN"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAJSHWZbAdgFdlUKxPvu4W1qe7GIlnBMl45TBZgCiZ8Z1Q8PM9/w6KPT1qH5EbEERrbJ8D4s157WNM/VyDsHiDC7hAozMQsHNcSiCzgJoRHxYPcWvVsyYp7MWRaWy98EP+E0+iXLr2wA7OF9WLPo4KIGAYSnj6Haw0RYOoNQdONo3hALiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RiAKQHaR",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJSHWZbAdgFdlUKxPvu4W1qe7GIlnBMl45TBZgCiZ8Z1Q8PM9/w6KPT1qH5EbEERrbJ8D4s157WNM/VyDsHiDC7hAozMQsHNcSiCzgJoRHxYPcWvVsyYp7MWRaWy98EP+E0+iXLr2wA7OF9WLPo4KIGAYSnj6Haw0RYOoNQdONo3hALiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RiAKQHaR",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJSHWZbAdgFdlUKxPvu4W1qe7GIlnBMl45TBZgCiZ8Z1Q8PM9/w6KPT1qH5EbEERrbJ8D4s157WNM/VyDsHiDC7hAozMQsHNcSiCzgJoRHxYPcWvVsyYp7MWRaWy98EP+E0+iXLr2wA7OF9WLPo4KIGAYSnj6Haw0RYOoNQdONo3hALiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RiAKQHaR",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "message": {
        "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "message": {
        "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
  "id": -576460752303423075,
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
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423075,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+QENCwH4hLhAJSHWZbAdgFdlUKxPvu4W1qe7GIlnBMl45TBZgCiZ8Z1Q8PM9/w6KPT1qH5EbEERrbJ8D4s157WNM/VyDsHiDC7hAozMQsHNcSiCzgJoRHxYPcWvVsyYp7MWRaWy98EP+E0+iXLr2wA7OF9WLPo4KIGAYSnj6Haw0RYOoNQdONo3hALiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RiAKQHaR"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+QENCwH4hLhAJSHWZbAdgFdlUKxPvu4W1qe7GIlnBMl45TBZgCiZ8Z1Q8PM9/w6KPT1qH5EbEERrbJ8D4s157WNM/VyDsHiDC7hAozMQsHNcSiCzgJoRHxYPcWvVsyYp7MWRaWy98EP+E0+iXLr2wA7OF9WLPo4KIGAYSnj6Haw0RYOoNQdONo3hALiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RiAKQHaR"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PAqDq2JFeO2C5etnX2pMEkSiBS8W5pwfxCyOyJ0evVuwZpSgJ7ME=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "vm_version": 6
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
  "id": -576460752303423074,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECyCk8OmvjF6M+Pche6MrabVdlyOg/MyYkXsEVjpk36ELASJv59mLfphVxaCrS4uJXmKj4mDydSAdTPdmLitJkPuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaVMU9ir"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423074,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+JALAfhCuECyCk8OmvjF6M+Pche6MrabVdlyOg/MyYkXsEVjpk36ELASJv59mLfphVxaCrS4uJXmKj4mDydSAdTPdmLitJkPuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaVMU9ir",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "vm_version": 6
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
  "id": -576460752303423073,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEATDVgLCVeIYmcBOA5j/lURlgyUe26uFOfOoJFAwXsWBuBAAENWGW1p6y7x6wqstGIdvMUq1F71Glgda1tqx3IDuECyCk8OmvjF6M+Pche6MrabVdlyOg/MyYkXsEVjpk36ELASJv59mLfphVxaCrS4uJXmKj4mDydSAdTPdmLitJkPuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaX/lZcC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423073,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEATDVgLCVeIYmcBOA5j/lURlgyUe26uFOfOoJFAwXsWBuBAAENWGW1p6y7x6wqstGIdvMUq1F71Glgda1tqx3IDuECyCk8OmvjF6M+Pche6MrabVdlyOg/MyYkXsEVjpk36ELASJv59mLfphVxaCrS4uJXmKj4mDydSAdTPdmLitJkPuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaX/lZcC"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEATDVgLCVeIYmcBOA5j/lURlgyUe26uFOfOoJFAwXsWBuBAAENWGW1p6y7x6wqstGIdvMUq1F71Glgda1tqx3IDuECyCk8OmvjF6M+Pche6MrabVdlyOg/MyYkXsEVjpk36ELASJv59mLfphVxaCrS4uJXmKj4mDydSAdTPdmLitJkPuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwKg6tiRXjtguXrZ19qTBJEogUvFuacH8QsjsidHr1bsGaX/lZcC"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PA6Cm9p/X/sj7d/Fojx33FpDvS5QO+zGwfIj8fNzJCQarljbGoO8=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423072,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECgLSexx8dU7k0/vhelW5DUMw5p9l+e3pA0QUM4u/G6oDL71EH7BQlt9ZrjNEZthc5feEqRyXgT9twyuEGpLDkOuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5b4L0Sr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423072,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+JALAfhCuECgLSexx8dU7k0/vhelW5DUMw5p9l+e3pA0QUM4u/G6oDL71EH7BQlt9ZrjNEZthc5feEqRyXgT9twyuEGpLDkOuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5b4L0Sr",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423071,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA+zJqFpO+OrT68NFoTdM1pH8jyjwoiykogtjn4WElCu5rbpy0nohQrlVdpLHjRVXYBkE+ZhMOCh97P2QKPbNsNuECgLSexx8dU7k0/vhelW5DUMw5p9l+e3pA0QUM4u/G6oDL71EH7BQlt9ZrjNEZthc5feEqRyXgT9twyuEGpLDkOuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5a0pOg0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423071,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEA+zJqFpO+OrT68NFoTdM1pH8jyjwoiykogtjn4WElCu5rbpy0nohQrlVdpLHjRVXYBkE+ZhMOCh97P2QKPbNsNuECgLSexx8dU7k0/vhelW5DUMw5p9l+e3pA0QUM4u/G6oDL71EH7BQlt9ZrjNEZthc5feEqRyXgT9twyuEGpLDkOuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5a0pOg0"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEA+zJqFpO+OrT68NFoTdM1pH8jyjwoiykogtjn4WElCu5rbpy0nohQrlVdpLHjRVXYBkE+ZhMOCh97P2QKPbNsNuECgLSexx8dU7k0/vhelW5DUMw5p9l+e3pA0QUM4u/G6oDL71EH7BQlt9ZrjNEZthc5feEqRyXgT9twyuEGpLDkOuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwOgpvaf1/7I+3fxaI8d9xaQ70uUDvsxsHyI/HzcyQkGq5a0pOg0"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 4,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 3,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 3,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PBKDNKNGDVqG8FrLwhQ9R1EVsMVs35QMovKvtD1RlwmEHy6K032w=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423070,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBsMJG9cXT1HwibNki1q7aNqwJuJRYpkhMYlMBhA4F7ekLfL7spyNtmqC6fB1zSAbTg5m3j3dWb7qBtDkeMjfQGuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwSgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8vce+jL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423070,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBsMJG9cXT1HwibNki1q7aNqwJuJRYpkhMYlMBhA4F7ekLfL7spyNtmqC6fB1zSAbTg5m3j3dWb7qBtDkeMjfQGuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwSgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8vce+jL",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423069,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBsMJG9cXT1HwibNki1q7aNqwJuJRYpkhMYlMBhA4F7ekLfL7spyNtmqC6fB1zSAbTg5m3j3dWb7qBtDkeMjfQGuEDpf9aikmKXcqR+HjJRVN2Y53Ly8cHAtlAKwSHX1jeU4ZYn897dStOqkbiao7iLcXZdvz8VafZ6XkJ7TEsmYC8AuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwSgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8tixIrc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423069,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEBsMJG9cXT1HwibNki1q7aNqwJuJRYpkhMYlMBhA4F7ekLfL7spyNtmqC6fB1zSAbTg5m3j3dWb7qBtDkeMjfQGuEDpf9aikmKXcqR+HjJRVN2Y53Ly8cHAtlAKwSHX1jeU4ZYn897dStOqkbiao7iLcXZdvz8VafZ6XkJ7TEsmYC8AuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwSgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8tixIrc"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEBsMJG9cXT1HwibNki1q7aNqwJuJRYpkhMYlMBhA4F7ekLfL7spyNtmqC6fB1zSAbTg5m3j3dWb7qBtDkeMjfQGuEDpf9aikmKXcqR+HjJRVN2Y53Ly8cHAtlAKwSHX1jeU4ZYn897dStOqkbiao7iLcXZdvz8VafZ6XkJ7TEsmYC8AuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwSgzSjRg1ahvBay8IUPUdRFbDFbN+UDKLyr7Q9UZcJhB8tixIrc"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PBaBKd77tzS0/F6PJCGNIxM1ROuq8JugHifpaqYptO+bBSi/AAQM=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423068,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDLVZA3r3vtkfqC49irtUG1N2wf2uHDt0m/yKGivMep6JpGhRezFlidXXQPzpzREWRf3TfTYyRXiBLiB9Ch6HkCuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUr2HEfG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423068,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDLVZA3r3vtkfqC49irtUG1N2wf2uHDt0m/yKGivMep6JpGhRezFlidXXQPzpzREWRf3TfTYyRXiBLiB9Ch6HkCuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUr2HEfG",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423067,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECcCL96Th+xO2Y8oGmaTtqXRFOPuXV+2QAx7vuNrKgbkdyn+ojApmy9xXke6A1wMdGNOSKmgL6pZdkBIS7DPgINuEDLVZA3r3vtkfqC49irtUG1N2wf2uHDt0m/yKGivMep6JpGhRezFlidXXQPzpzREWRf3TfTYyRXiBLiB9Ch6HkCuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUpyhSZP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423067,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuECcCL96Th+xO2Y8oGmaTtqXRFOPuXV+2QAx7vuNrKgbkdyn+ojApmy9xXke6A1wMdGNOSKmgL6pZdkBIS7DPgINuEDLVZA3r3vtkfqC49irtUG1N2wf2uHDt0m/yKGivMep6JpGhRezFlidXXQPzpzREWRf3TfTYyRXiBLiB9Ch6HkCuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUpyhSZP"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuECcCL96Th+xO2Y8oGmaTtqXRFOPuXV+2QAx7vuNrKgbkdyn+ojApmy9xXke6A1wMdGNOSKmgL6pZdkBIS7DPgINuEDLVZA3r3vtkfqC49irtUG1N2wf2uHDt0m/yKGivMep6JpGhRezFlidXXQPzpzREWRf3TfTYyRXiBLiB9Ch6HkCuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwWgSne+7c0tPxejyQhjSMTNUTrqvCboB4n6WqmKbTvmwUpyhSZP"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PBqC3bXBFip8XRh2sPOpYKl5Tsa8eif2V7m95M5kSLfvPhKKrAng=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423066,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECMVpKYC6VXk07ibLhYFIAWBJ/ATSwL5zOJVeGtKD+hGS7imYA2kwIPkoAIqVCFZtK2A+59PrSvfMppLmPHzDsAuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4T7FJk2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423066,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+JALAfhCuECMVpKYC6VXk07ibLhYFIAWBJ/ATSwL5zOJVeGtKD+hGS7imYA2kwIPkoAIqVCFZtK2A+59PrSvfMppLmPHzDsAuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4T7FJk2",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423065,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECMVpKYC6VXk07ibLhYFIAWBJ/ATSwL5zOJVeGtKD+hGS7imYA2kwIPkoAIqVCFZtK2A+59PrSvfMppLmPHzDsAuECshjysu5KH93lafRp95ymS8qxB+JXUQolfoui3DwscsbnJyk9B8/hdu1VrDn6Jdw1i2cPQK4NclpnYYuV4DG0FuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4QGIwhc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423065,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuECMVpKYC6VXk07ibLhYFIAWBJ/ATSwL5zOJVeGtKD+hGS7imYA2kwIPkoAIqVCFZtK2A+59PrSvfMppLmPHzDsAuECshjysu5KH93lafRp95ymS8qxB+JXUQolfoui3DwscsbnJyk9B8/hdu1VrDn6Jdw1i2cPQK4NclpnYYuV4DG0FuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4QGIwhc"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuECMVpKYC6VXk07ibLhYFIAWBJ/ATSwL5zOJVeGtKD+hGS7imYA2kwIPkoAIqVCFZtK2A+59PrSvfMppLmPHzDsAuECshjysu5KH93lafRp95ymS8qxB+JXUQolfoui3DwscsbnJyk9B8/hdu1VrDn6Jdw1i2cPQK4NclpnYYuV4DG0FuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwagt21wRYqfF0YdrDzqWCpeU7GvHon9le5veTOZEi37z4QGIwhc"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 5,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 5,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 6,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 6,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 3,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 3,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PB6D74ts0zr84T5TVF7oGz5iXPWmsFJZUntsqbVWLyrZFu0Lpmlg=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423064,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDVizfukoSe981PcFYQV/6vVBhfN3EURF+2E6RzXpas7zkyNFKWDECHUtcN/QKTFOutaYG0fNT71kpgZpF3ISwDuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzweg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2Rbs4peLc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423064,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDVizfukoSe981PcFYQV/6vVBhfN3EURF+2E6RzXpas7zkyNFKWDECHUtcN/QKTFOutaYG0fNT71kpgZpF3ISwDuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzweg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2Rbs4peLc",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423063,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDVEvXBMn5PwfpwXL2Blqm6tLpTwaezXBnxVBZ8lRvNCIZe4FIdNzNR8kqEQwNvEHx7yVqeiIDrqh6+gSI50qUIuEDVizfukoSe981PcFYQV/6vVBhfN3EURF+2E6RzXpas7zkyNFKWDECHUtcN/QKTFOutaYG0fNT71kpgZpF3ISwDuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzweg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2RbsrLqUQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423063,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEDVEvXBMn5PwfpwXL2Blqm6tLpTwaezXBnxVBZ8lRvNCIZe4FIdNzNR8kqEQwNvEHx7yVqeiIDrqh6+gSI50qUIuEDVizfukoSe981PcFYQV/6vVBhfN3EURF+2E6RzXpas7zkyNFKWDECHUtcN/QKTFOutaYG0fNT71kpgZpF3ISwDuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzweg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2RbsrLqUQ"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEDVEvXBMn5PwfpwXL2Blqm6tLpTwaezXBnxVBZ8lRvNCIZe4FIdNzNR8kqEQwNvEHx7yVqeiIDrqh6+gSI50qUIuEDVizfukoSe981PcFYQV/6vVBhfN3EURF+2E6RzXpas7zkyNFKWDECHUtcN/QKTFOutaYG0fNT71kpgZpF3ISwDuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzweg++LbNM6/OE+U1Re6Bs+Ylz1prBSWVJ7bKm1Vi8q2RbsrLqUQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 8,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 7,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 7,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PCKDZkikRwm9X2aF5+LO31nSuNfLOTaNdzsgt0BKS68TOQSDLlQI=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423062,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBg3fkHP3KbPnWPoqjZqL6UA1Z5NC51ZeT2+tpSJOtAXajzw4W4EnGSZx/iMzC8wYQXTesAn5Hh3GFEUtODJj0FuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkH1jzZa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423062,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBg3fkHP3KbPnWPoqjZqL6UA1Z5NC51ZeT2+tpSJOtAXajzw4W4EnGSZx/iMzC8wYQXTesAn5Hh3GFEUtODJj0FuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkH1jzZa",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423061,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBg3fkHP3KbPnWPoqjZqL6UA1Z5NC51ZeT2+tpSJOtAXajzw4W4EnGSZx/iMzC8wYQXTesAn5Hh3GFEUtODJj0FuEDG5cGNZSSKcpdsCTRCrPtR2IbQOq/B2qmEE+KLzCisCGKDuH5u8SKc9Ugfy+VA7wco7Kpl3A+n+fEMTK+qDVkCuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkFwezXR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423061,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEBg3fkHP3KbPnWPoqjZqL6UA1Z5NC51ZeT2+tpSJOtAXajzw4W4EnGSZx/iMzC8wYQXTesAn5Hh3GFEUtODJj0FuEDG5cGNZSSKcpdsCTRCrPtR2IbQOq/B2qmEE+KLzCisCGKDuH5u8SKc9Ugfy+VA7wco7Kpl3A+n+fEMTK+qDVkCuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkFwezXR"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEBg3fkHP3KbPnWPoqjZqL6UA1Z5NC51ZeT2+tpSJOtAXajzw4W4EnGSZx/iMzC8wYQXTesAn5Hh3GFEUtODJj0FuEDG5cGNZSSKcpdsCTRCrPtR2IbQOq/B2qmEE+KLzCisCGKDuH5u8SKc9Ugfy+VA7wco7Kpl3A+n+fEMTK+qDVkCuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwig2ZIpEcJvV9mhefizt9Z0rjXyzk2jXc7ILdASkuvEzkFwezXR"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PCaC6d6qpJPpXzCbSkKxdCaIDbRV0C8Var9vBF6xgzDqRcTgdhuI=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423060,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED7BYEfs1+CrW/WW8xRoLdxvSpbx4E1WE+5Pyv7s6/4SD2HiW7z4Ihr+KVRY4n6Ft/1Mal4V2aeraXfFxj5vg0CuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXHtjCE5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423060,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+JALAfhCuED7BYEfs1+CrW/WW8xRoLdxvSpbx4E1WE+5Pyv7s6/4SD2HiW7z4Ihr+KVRY4n6Ft/1Mal4V2aeraXfFxj5vg0CuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXHtjCE5",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423059,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDoPnVqii3BpLaO056Z7iCiCKQOnKDUJaM4mYuIPMkhG782Q6CDOugrHWEpbENNXv0VTPMCBSGTNQzm9IEYd5gEuED7BYEfs1+CrW/WW8xRoLdxvSpbx4E1WE+5Pyv7s6/4SD2HiW7z4Ihr+KVRY4n6Ft/1Mal4V2aeraXfFxj5vg0CuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXEGSZVP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423059,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEDoPnVqii3BpLaO056Z7iCiCKQOnKDUJaM4mYuIPMkhG782Q6CDOugrHWEpbENNXv0VTPMCBSGTNQzm9IEYd5gEuED7BYEfs1+CrW/WW8xRoLdxvSpbx4E1WE+5Pyv7s6/4SD2HiW7z4Ihr+KVRY4n6Ft/1Mal4V2aeraXfFxj5vg0CuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXEGSZVP"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEDoPnVqii3BpLaO056Z7iCiCKQOnKDUJaM4mYuIPMkhG782Q6CDOugrHWEpbENNXv0VTPMCBSGTNQzm9IEYd5gEuED7BYEfs1+CrW/WW8xRoLdxvSpbx4E1WE+5Pyv7s6/4SD2HiW7z4Ihr+KVRY4n6Ft/1Mal4V2aeraXfFxj5vg0CuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwmguneqqST6V8wm0pCsXQmiA20VdAvFWq/bwResYMw6kXEGSZVP"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PCqCipoS6aEYC2966NhN/h18AIP4uJRH+0o1rYv9JCQweKemhRxQ=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423058,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAChWJGVwWYmmIq2funOxXjjWHAZ3IRxySWKLYUrsaEBWpMUf2OuRzgLjRF7fu8P9SKxpZVx+5ZGslDd5atntUJuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHilPGZ3T"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423058,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAChWJGVwWYmmIq2funOxXjjWHAZ3IRxySWKLYUrsaEBWpMUf2OuRzgLjRF7fu8P9SKxpZVx+5ZGslDd5atntUJuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHilPGZ3T",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423057,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAChWJGVwWYmmIq2funOxXjjWHAZ3IRxySWKLYUrsaEBWpMUf2OuRzgLjRF7fu8P9SKxpZVx+5ZGslDd5atntUJuEAflPw+u5MQxSHc4cbG8zDQrOUQnvOtFC46j4LwKAMUFcbLTJJHUXCjd2JSl2HuJigf2BApJisSentk7N4D+h8MuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHinmBazl"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423057,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEAChWJGVwWYmmIq2funOxXjjWHAZ3IRxySWKLYUrsaEBWpMUf2OuRzgLjRF7fu8P9SKxpZVx+5ZGslDd5atntUJuEAflPw+u5MQxSHc4cbG8zDQrOUQnvOtFC46j4LwKAMUFcbLTJJHUXCjd2JSl2HuJigf2BApJisSentk7N4D+h8MuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHinmBazl"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "state": "tx_+NILAfiEuEAChWJGVwWYmmIq2funOxXjjWHAZ3IRxySWKLYUrsaEBWpMUf2OuRzgLjRF7fu8P9SKxpZVx+5ZGslDd5atntUJuEAflPw+u5MQxSHc4cbG8zDQrOUQnvOtFC46j4LwKAMUFcbLTJJHUXCjd2JSl2HuJigf2BApJisSentk7N4D+h8MuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHinmBazl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 9,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 9,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 10,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 10,
      "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ],
    "contracts": [
      "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg/xaYlQYtkCkvjp91m5wWsQ67/29bJLlTqoRwdx8JMon5AYP4SaAKIVXE2JtsG1AvpAThaffPRfTfrHqdTK+V+RPcjbtnM+egM4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAr4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6D+4wSC4Ve0F0tyKnD2rVhkBjbEeUnr+0Bzo45NLq2lse2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKf/f4lKD/FpiVBi2QKS+On3WbnBaxDrv/b1skuVOqhHB3HwkyifhxgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGoAohVcTYm2wbUC+kBOFp989F9N+sep1Mr5X5E9yNu2czgKD+4wSC4Ve0F0tyKnD2rVhkBjbEeUnr+0Bzo45NLq2lsYCAgICAgIDj4qBgbM3ZZuQk0sQk/jDaBJq7fvfw8KsOhCO0TPQkyC6Zh8DA+Qap+QamoGLD/LH3mW6RzNEkDR/57kVtMnGZ1jYiqZGdt8o1nJT3+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGLD/LH3mW6RzNEkDR/57kVtMnGZ1jYiqZGdt8o1nJT3+EOhAHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQoHGbA5JQinbIb4EDcQfsvluiJG5kFC58N0+I36KKU6ul+QO2oHGbA5JQinbIb4EDcQfsvluiJG5kFC58N0+I36KKU6ul+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDA4wJ+2Q=="
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
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ],
    "contracts": [
      "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg/xaYlQYtkCkvjp91m5wWsQ67/29bJLlTqoRwdx8JMon5AYP4SaAKIVXE2JtsG1AvpAThaffPRfTfrHqdTK+V+RPcjbtnM+egM4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAr4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6D+4wSC4Ve0F0tyKnD2rVhkBjbEeUnr+0Bzo45NLq2lse2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKf/f4lKD/FpiVBi2QKS+On3WbnBaxDrv/b1skuVOqhHB3HwkyifhxgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGoAohVcTYm2wbUC+kBOFp989F9N+sep1Mr5X5E9yNu2czgKD+4wSC4Ve0F0tyKnD2rVhkBjbEeUnr+0Bzo45NLq2lsYCAgICAgIDj4qBgbM3ZZuQk0sQk/jDaBJq7fvfw8KsOhCO0TPQkyC6Zh8DA+Qap+QamoGLD/LH3mW6RzNEkDR/57kVtMnGZ1jYiqZGdt8o1nJT3+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGLD/LH3mW6RzNEkDR/57kVtMnGZ1jYiqZGdt8o1nJT3+EOhAHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQoHGbA5JQinbIb4EDcQfsvluiJG5kFC58N0+I36KKU6ul+QO2oHGbA5JQinbIb4EDcQfsvluiJG5kFC58N0+I36KKU6ul+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDA4wJ+2Q=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303423056,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423056,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QeoggJuAbkHofkHnj8B+QeZuLn4t0ABuEBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEO5rA+H+wkIbumEBC+DwDa4sljTu1ngCvK5eZ3yXruqsuHH4bykCoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQoKoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDkH0m6usjETybAfrEtQ3CfrQr1s+j6d+GvnkZNyHh84Lhx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEEBKEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggHOoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMC4ufi3QAG4QHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQm+Rmu9YLZ0zm9hVy7r6HZoRT5/Zf51TlFPFcyJV/5YW4cfhvKQKhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChBQWhBXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuEBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEE9oz9Xzqfg+4Ohey944Sei3uQn2KrVf2FooddUQUJfSuHH4bykCoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQkJoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhA1Bh+uKTf+hBCGPMHHle1QbNQ3/TGm1JcvGrScnDU8G7hx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EICKEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggHOoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMC4ufi3QAG4QHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQM1DqWLp7/BedNhM0eYC2/04QYqGep0w0cYLLVTpI9Ui4cfhvKQKhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BBwehBXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuEBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEB6+5MLlh4kKT5l0+6ehKbJcqRDRoGazFUIlySEPJcnGuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQYGoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYAwLi5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAPzT7MBDodQf93/uhrDTLiunfi0XHx5wpg7lCY0X3nbLhx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEDA6EFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVAMC5Ab75AbtAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAAFDjpVvkmOsl5sgNigmLHZyLKy82N6hYAtsti+JzzuLkBdPkBcSkCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQICoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEACCAT+5ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABUAwDB03es=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAChWJGVwWYmmIq2funOxXjjWHAZ3IRxySWKLYUrsaEBWpMUf2OuRzgLjRF7fu8P9SKxpZVx+5ZGslDd5atntUJuEAflPw+u5MQxSHc4cbG8zDQrOUQnvOtFC46j4LwKAMUFcbLTJJHUXCjd2JSl2HuJigf2BApJisSentk7N4D+h8MuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHinmBazl",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABonOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC5A4j5A4VAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqELkDX/kDXCgBoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDuawPh/sJCG7phAQvg8A2uLJY07tZ4AryuXmd8l67qrLhx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EKCqEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcp/96rpQAGgc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAqw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl///PAcIg=="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423055,
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
    "gas_price": 1000007625
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423055,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "signed_tx": "tx_+Qi7CwHAuQi1+QiyggIJAaEGNsBZoD+K6pmpTDIaGhe/xow8JD7lLnBsmNxrfpYZn8+hAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChuNT40gsB+IS4QAKFYkZXBZiaYirZ+6c7FeONYcBnchHHJJYothSuxoQFakxR/Y65HOAuNEXt+7w/1IrGllXH7lkayUN3lq2e1Qm4QB+U/D67kxDFIdzhxsbzMNCs5RCe860ULjqPgvAoAxQVxstMkkdRcKN3YlKXYe4mKB/YECkmKxJ6e2Ts3gP6Hwy4SPhGOQKhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PCqCipoS6aEYC2966NhN/h18AIP4uJRH+0o1rYv9JCQweKQu4uPi2ggI+AaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGhBXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQAQqDD0JAhDua58m4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg/WQV9OjUJOkaHHly0X0GufZyf9ndZGW/tk5DtIAgkFS5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaJzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEBABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQALkDiPkDhUABoHOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQuQNf+QNcKAGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuEBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEO5rA+H+wkIbumEBC+DwDa4sljTu1ngCvK5eZ3yXruqsuHH4bykCoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQoKoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2w70ABoJCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yn/3qulAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEIXECgEACrDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/8AhwHB0kH+DpQKQ2sBug==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_stWxNVbPU3ms8yGmgjqMPZDVcX8NVVvdsNAjfH3HaUHnvfycC",
          "gas": 1000000,
          "gas_price": 1000007625,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+Qj+CwH4QrhA8CZd0toNrca8HPkFSnHliems9Hcmy/sjxUISn/WVmb/JGae3J1JsHRDItTI6F3d0TRvbFoE1VZ8YHE8NU0cFAbkItfkIsoICCQGhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEAChWJGVwWYmmIq2funOxXjjWHAZ3IRxySWKLYUrsaEBWpMUf2OuRzgLjRF7fu8P9SKxpZVx+5ZGslDd5atntUJuEAflPw+u5MQxSHc4cbG8zDQrOUQnvOtFC46j4LwKAMUFcbLTJJHUXCjd2JSl2HuJigf2BApJisSentk7N4D+h8MuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHikLuLj4toICPgGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAEKgw9CQIQ7mufJuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoP1kFfTo1CTpGhx5ctF9Brn2cn/Z3WRlv7ZOQ7SAIJBUuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABonOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC5A4j5A4VAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqELkDX/kDXCgBoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDuawPh/sJCG7phAQvg8A2uLJY07tZ4AryuXmd8l67qrLhx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EKCqEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcp/96rpQAGgc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAqw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//AIcBwdJB/g6UCr99Dvg="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhA8CZd0toNrca8HPkFSnHliems9Hcmy/sjxUISn/WVmb/JGae3J1JsHRDItTI6F3d0TRvbFoE1VZ8YHE8NU0cFAbkItfkIsoICCQGhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEAChWJGVwWYmmIq2funOxXjjWHAZ3IRxySWKLYUrsaEBWpMUf2OuRzgLjRF7fu8P9SKxpZVx+5ZGslDd5atntUJuEAflPw+u5MQxSHc4cbG8zDQrOUQnvOtFC46j4LwKAMUFcbLTJJHUXCjd2JSl2HuJigf2BApJisSentk7N4D+h8MuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHikLuLj4toICPgGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAEKgw9CQIQ7mufJuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoP1kFfTo1CTpGhx5ctF9Brn2cn/Z3WRlv7ZOQ7SAIJBUuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABonOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC5A4j5A4VAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqELkDX/kDXCgBoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDuawPh/sJCG7phAQvg8A2uLJY07tZ4AryuXmd8l67qrLhx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EKCqEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcp/96rpQAGgc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAqw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//AIcBwdJB/g6UCr99Dvg=",
      "type": "channel_force_progress_tx"
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhA8CZd0toNrca8HPkFSnHliems9Hcmy/sjxUISn/WVmb/JGae3J1JsHRDItTI6F3d0TRvbFoE1VZ8YHE8NU0cFAbkItfkIsoICCQGhBjbAWaA/iuqZqUwyGhoXv8aMPCQ+5S5wbJjca36WGZ/PoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEAChWJGVwWYmmIq2funOxXjjWHAZ3IRxySWKLYUrsaEBWpMUf2OuRzgLjRF7fu8P9SKxpZVx+5ZGslDd5atntUJuEAflPw+u5MQxSHc4cbG8zDQrOUQnvOtFC46j4LwKAMUFcbLTJJHUXCjd2JSl2HuJigf2BApJisSentk7N4D+h8MuEj4RjkCoQY2wFmgP4rqmalMMhoaF7/GjDwkPuUucGyY3Gt+lhmfzwqgoqaEumhGAtveujYTf4dfACD+LiUR/tKNa2L/SQkMHikLuLj4toICPgGhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChoQVzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqEAEKgw9CQIQ7mufJuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoP1kFfTo1CTpGhx5ctF9Brn2cn/Z3WRlv7ZOQ7SAIJBUuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGic4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhAQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABonOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoXOMREr22hNQej+eqO0NiZlnqaANpQyO7WlbkxoaSKoQEAC5A4j5A4VAAaBzjERK9toTUHo/nqjtDYmZZ6mgDaUMju1pW5MaGkiqELkDX/kDXCgBoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhDuawPh/sJCG7phAQvg8A2uLJY07tZ4AryuXmd8l67qrLhx+G8pAqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EKCqEFc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhABggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcp/96rpQAGgc4xESvbaE1B6P56o7Q2JmWepoA2lDI7taVuTGhpIqhCFxAoBAAqw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//AIcBwdJB/g6UCr99Dvg=",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423054,
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
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423054,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423053,
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
    "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
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
  "channel_id": "ch_R7YusnNx9hMqpqfXHDoeQoJGVHdNT8wKzHJnborrchYvECxRr",
  "id": -576460752303423053,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
