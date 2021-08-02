
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
      "fsm_id": "ba_50OAWcG8LhcxJjzYnwocsm7FtnhFnvwJsGd70a15dVZYt2pD"
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
      "fsm_id": "ba_w7gRam0OZu2EEkaOEtWxpOnBNvFNrDjATvwpZAIYBDFATt7E"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY8e7lo9Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422665,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECZl49i+1SgkNu09m08t1XzquGqGHr60WoDJN/Ir44ObICu4eq2QvtYDXLv5vQFEEeL6HEEdYQS2I5nHERwAHAIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGPCtAxy8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422665,
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_w7gRam0OZu2EEkaOEtWxpOnBNvFNrDjATvwpZAIYBDFATt7E"
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECZl49i+1SgkNu09m08t1XzquGqGHr60WoDJN/Ir44ObICu4eq2QvtYDXLv5vQFEEeL6HEEdYQS2I5nHERwAHAIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGPCtAxy8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422664,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAmZePYvtUoJDbtPZtPLdV86rhqhh6+tFqAyTfyK+ODmyAruHqtkL7WA1y7+b0BRBHi+hxBHWEEtiOZxxEcABwCLhAzuIz0TsqKNzvXvN99DAqsnBVthyHqwAA4Ri5FZHJUBmGK7Ii9Ss9EPiaVqDGU7WmrY1v4p3Rww52Ietnhm76BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjysWAv/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
  "id": -576460752303422664,
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAmZePYvtUoJDbtPZtPLdV86rhqhh6+tFqAyTfyK+ODmyAruHqtkL7WA1y7+b0BRBHi+hxBHWEEtiOZxxEcABwCLhAzuIz0TsqKNzvXvN99DAqsnBVthyHqwAA4Ri5FZHJUBmGK7Ii9Ss9EPiaVqDGU7WmrY1v4p3Rww52Ietnhm76BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjysWAv/",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_50OAWcG8LhcxJjzYnwocsm7FtnhFnvwJsGd70a15dVZYt2pD"
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAmZePYvtUoJDbtPZtPLdV86rhqhh6+tFqAyTfyK+ODmyAruHqtkL7WA1y7+b0BRBHi+hxBHWEEtiOZxxEcABwCLhAzuIz0TsqKNzvXvN99DAqsnBVthyHqwAA4Ri5FZHJUBmGK7Ii9Ss9EPiaVqDGU7WmrY1v4p3Rww52Ietnhm76BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjysWAv/",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAmZePYvtUoJDbtPZtPLdV86rhqhh6+tFqAyTfyK+ODmyAruHqtkL7WA1y7+b0BRBHi+hxBHWEEtiOZxxEcABwCLhAzuIz0TsqKNzvXvN99DAqsnBVthyHqwAA4Ri5FZHJUBmGK7Ii9Ss9EPiaVqDGU7WmrY1v4p3Rww52Ietnhm76BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjysWAv/",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAmZePYvtUoJDbtPZtPLdV86rhqhh6+tFqAyTfyK+ODmyAruHqtkL7WA1y7+b0BRBHi+hxBHWEEtiOZxxEcABwCLhAzuIz0TsqKNzvXvN99DAqsnBVthyHqwAA4Ri5FZHJUBmGK7Ii9Ss9EPiaVqDGU7WmrY1v4p3Rww52Ietnhm76BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjysWAv/",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
  "id": -576460752303422663,
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
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
  "id": -576460752303422663,
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "state": "tx_+QENCwH4hLhAmZePYvtUoJDbtPZtPLdV86rhqhh6+tFqAyTfyK+ODmyAruHqtkL7WA1y7+b0BRBHi+hxBHWEEtiOZxxEcABwCLhAzuIz0TsqKNzvXvN99DAqsnBVthyHqwAA4Ri5FZHJUBmGK7Ii9Ss9EPiaVqDGU7WmrY1v4p3Rww52Ietnhm76BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjysWAv/"
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "state": "tx_+QENCwH4hLhAmZePYvtUoJDbtPZtPLdV86rhqhh6+tFqAyTfyK+ODmyAruHqtkL7WA1y7+b0BRBHi+hxBHWEEtiOZxxEcABwCLhAzuIz0TsqKNzvXvN99DAqsnBVthyHqwAA4Ri5FZHJUBmGK7Ii9Ss9EPiaVqDGU7WmrY1v4p3Rww52Ietnhm76BLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjysWAv/"
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBrkl6u9/L9Q4mZaDycBgZHXM+Uokw4jHDQWoYDrMX2R1oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhnBIhhsPP6Dc0aEz/UgoEcs4ajohf9X9BGhuePf6GLqnUld1F+cQwQI9k/yhig==",
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
  "id": -576460752303422662,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAeT7aTD6G6Fcqz2fkR22e7L7kPwaGYONhLpEsyvO0YNFQRMtwMt8H4Hq9JIZeriv+YvGR7kTFbnfAU4H11fYoBuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECPbUFSTE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
  "id": -576460752303422662,
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAeT7aTD6G6Fcqz2fkR22e7L7kPwaGYONhLpEsyvO0YNFQRMtwMt8H4Hq9JIZeriv+YvGR7kTFbnfAU4H11fYoBuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECPbUFSTE=",
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
  "id": -576460752303422661,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAeT7aTD6G6Fcqz2fkR22e7L7kPwaGYONhLpEsyvO0YNFQRMtwMt8H4Hq9JIZeriv+YvGR7kTFbnfAU4H11fYoBuECU6QvOg3R8fDR1qAzw1Rcsg/vHZ9UiIx67u7KGNHekavW12b5mnWXEmTArCesBU5xqQ+T90TUakpPV3OMjarsHuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECPelg6ZE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
  "id": -576460752303422661,
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAeT7aTD6G6Fcqz2fkR22e7L7kPwaGYONhLpEsyvO0YNFQRMtwMt8H4Hq9JIZeriv+YvGR7kTFbnfAU4H11fYoBuECU6QvOg3R8fDR1qAzw1Rcsg/vHZ9UiIx67u7KGNHekavW12b5mnWXEmTArCesBU5xqQ+T90TUakpPV3OMjarsHuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECPelg6ZE=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAeT7aTD6G6Fcqz2fkR22e7L7kPwaGYONhLpEsyvO0YNFQRMtwMt8H4Hq9JIZeriv+YvGR7kTFbnfAU4H11fYoBuECU6QvOg3R8fDR1qAzw1Rcsg/vHZ9UiIx67u7KGNHekavW12b5mnWXEmTArCesBU5xqQ+T90TUakpPV3OMjarsHuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECPelg6ZE=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAeT7aTD6G6Fcqz2fkR22e7L7kPwaGYONhLpEsyvO0YNFQRMtwMt8H4Hq9JIZeriv+YvGR7kTFbnfAU4H11fYoBuECU6QvOg3R8fDR1qAzw1Rcsg/vHZ9UiIx67u7KGNHekavW12b5mnWXEmTArCesBU5xqQ+T90TUakpPV3OMjarsHuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECPelg6ZE=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAeT7aTD6G6Fcqz2fkR22e7L7kPwaGYONhLpEsyvO0YNFQRMtwMt8H4Hq9JIZeriv+YvGR7kTFbnfAU4H11fYoBuECU6QvOg3R8fDR1qAzw1Rcsg/vHZ9UiIx67u7KGNHekavW12b5mnWXEmTArCesBU5xqQ+T90TUakpPV3OMjarsHuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECPelg6ZE=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "state": "tx_+P4LAfiEuEAeT7aTD6G6Fcqz2fkR22e7L7kPwaGYONhLpEsyvO0YNFQRMtwMt8H4Hq9JIZeriv+YvGR7kTFbnfAU4H11fYoBuECU6QvOg3R8fDR1qAzw1Rcsg/vHZ9UiIx67u7KGNHekavW12b5mnWXEmTArCesBU5xqQ+T90TUakpPV3OMjarsHuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECPelg6ZE="
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "state": "tx_+P4LAfiEuEAeT7aTD6G6Fcqz2fkR22e7L7kPwaGYONhLpEsyvO0YNFQRMtwMt8H4Hq9JIZeriv+YvGR7kTFbnfAU4H11fYoBuECU6QvOg3R8fDR1qAzw1Rcsg/vHZ9UiIx67u7KGNHekavW12b5mnWXEmTArCesBU5xqQ+T90TUakpPV3OMjarsHuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+g3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECPelg6ZE="
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBrkl6u9/L9Q4mZaDycBgZHXM+Uokw4jHDQWoYDrMX2R1oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhnBIhhsPP6DZtcOT2QHMSn7Ye3r6M+jqyyVjQiph/medhaKMSYXlhQMYgfPQhw==",
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
  "id": -576460752303422660,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDCpyzHbCdjdq6LqE7I+wwqCuzLZfoC/2uHtVFWaO4dDKJQYyM6mMUXCO9xTCNzmEfNGfgu1ZnK13VhxkdOKLQFuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDGN0Rl/I="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
  "id": -576460752303422660,
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDCpyzHbCdjdq6LqE7I+wwqCuzLZfoC/2uHtVFWaO4dDKJQYyM6mMUXCO9xTCNzmEfNGfgu1ZnK13VhxkdOKLQFuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDGN0Rl/I=",
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
  "id": -576460752303422659,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAf434NzQiZfXgdHBTLJMWMuzIcLhbJoSeSvgDf5cOnb8ISjHGtpKJplU74CIk21QL+I9FV6jIsOLdJ8Er546gJuEDCpyzHbCdjdq6LqE7I+wwqCuzLZfoC/2uHtVFWaO4dDKJQYyM6mMUXCO9xTCNzmEfNGfgu1ZnK13VhxkdOKLQFuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDGBr5nss="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
  "id": -576460752303422659,
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAf434NzQiZfXgdHBTLJMWMuzIcLhbJoSeSvgDf5cOnb8ISjHGtpKJplU74CIk21QL+I9FV6jIsOLdJ8Er546gJuEDCpyzHbCdjdq6LqE7I+wwqCuzLZfoC/2uHtVFWaO4dDKJQYyM6mMUXCO9xTCNzmEfNGfgu1ZnK13VhxkdOKLQFuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDGBr5nss=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAf434NzQiZfXgdHBTLJMWMuzIcLhbJoSeSvgDf5cOnb8ISjHGtpKJplU74CIk21QL+I9FV6jIsOLdJ8Er546gJuEDCpyzHbCdjdq6LqE7I+wwqCuzLZfoC/2uHtVFWaO4dDKJQYyM6mMUXCO9xTCNzmEfNGfgu1ZnK13VhxkdOKLQFuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDGBr5nss=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "message": {
        "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAf434NzQiZfXgdHBTLJMWMuzIcLhbJoSeSvgDf5cOnb8ISjHGtpKJplU74CIk21QL+I9FV6jIsOLdJ8Er546gJuEDCpyzHbCdjdq6LqE7I+wwqCuzLZfoC/2uHtVFWaO4dDKJQYyM6mMUXCO9xTCNzmEfNGfgu1ZnK13VhxkdOKLQFuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDGBr5nss=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAf434NzQiZfXgdHBTLJMWMuzIcLhbJoSeSvgDf5cOnb8ISjHGtpKJplU74CIk21QL+I9FV6jIsOLdJ8Er546gJuEDCpyzHbCdjdq6LqE7I+wwqCuzLZfoC/2uHtVFWaO4dDKJQYyM6mMUXCO9xTCNzmEfNGfgu1ZnK13VhxkdOKLQFuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDGBr5nss=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "state": "tx_+P4LAfiEuEAf434NzQiZfXgdHBTLJMWMuzIcLhbJoSeSvgDf5cOnb8ISjHGtpKJplU74CIk21QL+I9FV6jIsOLdJ8Er546gJuEDCpyzHbCdjdq6LqE7I+wwqCuzLZfoC/2uHtVFWaO4dDKJQYyM6mMUXCO9xTCNzmEfNGfgu1ZnK13VhxkdOKLQFuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDGBr5nss="
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "state": "tx_+P4LAfiEuEAf434NzQiZfXgdHBTLJMWMuzIcLhbJoSeSvgDf5cOnb8ISjHGtpKJplU74CIk21QL+I9FV6jIsOLdJ8Er546gJuEDCpyzHbCdjdq6LqE7I+wwqCuzLZfoC/2uHtVFWaO4dDKJQYyM6mMUXCO9xTCNzmEfNGfgu1ZnK13VhxkdOKLQFuHT4cjQBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+g2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDGBr5nss="
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBrkl6u9/L9Q4mZaDycBgZHXM+Uokw4jHDQWoYDrMX2R1oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/2GHLHOiuv/AIYPXtZ/KAA+p0gL1Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422658,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAftzAWr80RWQboIcTsdUiccRXSMYJJ9F1y6xex8cvpEaI4JOGzoReBp7/btMpzRp56Veowsc2j+TA0eU1X57kJuF/4XTUBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAPsakviA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
  "id": -576460752303422658,
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAftzAWr80RWQboIcTsdUiccRXSMYJJ9F1y6xex8cvpEaI4JOGzoReBp7/btMpzRp56Veowsc2j+TA0eU1X57kJuF/4XTUBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAPsakviA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422657,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAGWMNytuYg6U486odIPdk07KVMaSIzyb0gN7UKf6ltuuWIXaiQdR8i85j/VEOazAX0c6DadnGO2OL7+StTXFMFuEAftzAWr80RWQboIcTsdUiccRXSMYJJ9F1y6xex8cvpEaI4JOGzoReBp7/btMpzRp56Veowsc2j+TA0eU1X57kJuF/4XTUBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAPpzz7/8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
  "id": -576460752303422657,
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAGWMNytuYg6U486odIPdk07KVMaSIzyb0gN7UKf6ltuuWIXaiQdR8i85j/VEOazAX0c6DadnGO2OL7+StTXFMFuEAftzAWr80RWQboIcTsdUiccRXSMYJJ9F1y6xex8cvpEaI4JOGzoReBp7/btMpzRp56Veowsc2j+TA0eU1X57kJuF/4XTUBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAPpzz7/8=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAGWMNytuYg6U486odIPdk07KVMaSIzyb0gN7UKf6ltuuWIXaiQdR8i85j/VEOazAX0c6DadnGO2OL7+StTXFMFuEAftzAWr80RWQboIcTsdUiccRXSMYJJ9F1y6xex8cvpEaI4JOGzoReBp7/btMpzRp56Veowsc2j+TA0eU1X57kJuF/4XTUBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAPpzz7/8=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAGWMNytuYg6U486odIPdk07KVMaSIzyb0gN7UKf6ltuuWIXaiQdR8i85j/VEOazAX0c6DadnGO2OL7+StTXFMFuEAftzAWr80RWQboIcTsdUiccRXSMYJJ9F1y6xex8cvpEaI4JOGzoReBp7/btMpzRp56Veowsc2j+TA0eU1X57kJuF/4XTUBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAPpzz7/8=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAGWMNytuYg6U486odIPdk07KVMaSIzyb0gN7UKf6ltuuWIXaiQdR8i85j/VEOazAX0c6DadnGO2OL7+StTXFMFuEAftzAWr80RWQboIcTsdUiccRXSMYJJ9F1y6xex8cvpEaI4JOGzoReBp7/btMpzRp56Veowsc2j+TA0eU1X57kJuF/4XTUBoQa5Jervfy/UOJmWg8nAYGR1zPlKJMOIxw0FqGA6zF9kdaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAPpzz7/8=",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
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
    "channel_id": "ch_2QYMtUjbE7xh4AFpQuc7NVxrMu1UsntuKadrmQ7ZRNUtK6kSex",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
