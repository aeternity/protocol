
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
      "fsm_id": "ba_Y1Ck9tJLEFrdCZWzlhyj2JGk2xDkH+zEl21TAY0nIRvcqPwO"
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
      "fsm_id": "ba_rLPIr8yZAhusgGwwa13LHGBNOWn3AuUjh5aEzVWGVXtj29a5"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBtwWDco4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422119,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEC1ROvYhCBLP2PGRagFSMlrdagBjpYTLLHqlNgb7Ra5tN5zGddIsjLq5320SpcOeRxZdV8uuFRbbW4t86sxFi4LuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbfT2GoS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422119,
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_rLPIr8yZAhusgGwwa13LHGBNOWn3AuUjh5aEzVWGVXtj29a5"
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEC1ROvYhCBLP2PGRagFSMlrdagBjpYTLLHqlNgb7Ra5tN5zGddIsjLq5320SpcOeRxZdV8uuFRbbW4t86sxFi4LuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbfT2GoS",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422118,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAtUTr2IQgSz9jxkWoBUjJa3WoAY6WEyyx6pTYG+0WubTecxnXSLIy6ud9tEqXDnkcWXVfLrhUW21uLfOrMRYuC7hAu4w6qTsRxxkuK64ZYLFwh1AJKpx0b3MfeP4a9bJqOIuSIaX0gdfSjdlOiI0N+9+eTz208daJzzSzUY4BW5wYD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG3+QBGTw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
  "id": -576460752303422118,
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAtUTr2IQgSz9jxkWoBUjJa3WoAY6WEyyx6pTYG+0WubTecxnXSLIy6ud9tEqXDnkcWXVfLrhUW21uLfOrMRYuC7hAu4w6qTsRxxkuK64ZYLFwh1AJKpx0b3MfeP4a9bJqOIuSIaX0gdfSjdlOiI0N+9+eTz208daJzzSzUY4BW5wYD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG3+QBGTw==",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Y1Ck9tJLEFrdCZWzlhyj2JGk2xDkH+zEl21TAY0nIRvcqPwO"
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAtUTr2IQgSz9jxkWoBUjJa3WoAY6WEyyx6pTYG+0WubTecxnXSLIy6ud9tEqXDnkcWXVfLrhUW21uLfOrMRYuC7hAu4w6qTsRxxkuK64ZYLFwh1AJKpx0b3MfeP4a9bJqOIuSIaX0gdfSjdlOiI0N+9+eTz208daJzzSzUY4BW5wYD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG3+QBGTw==",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAtUTr2IQgSz9jxkWoBUjJa3WoAY6WEyyx6pTYG+0WubTecxnXSLIy6ud9tEqXDnkcWXVfLrhUW21uLfOrMRYuC7hAu4w6qTsRxxkuK64ZYLFwh1AJKpx0b3MfeP4a9bJqOIuSIaX0gdfSjdlOiI0N+9+eTz208daJzzSzUY4BW5wYD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG3+QBGTw==",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAtUTr2IQgSz9jxkWoBUjJa3WoAY6WEyyx6pTYG+0WubTecxnXSLIy6ud9tEqXDnkcWXVfLrhUW21uLfOrMRYuC7hAu4w6qTsRxxkuK64ZYLFwh1AJKpx0b3MfeP4a9bJqOIuSIaX0gdfSjdlOiI0N+9+eTz208daJzzSzUY4BW5wYD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG3+QBGTw==",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "message": {
        "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "message": {
        "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
  "id": -576460752303422117,
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
  "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
  "id": -576460752303422117,
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "state": "tx_+QEOCwH4hLhAtUTr2IQgSz9jxkWoBUjJa3WoAY6WEyyx6pTYG+0WubTecxnXSLIy6ud9tEqXDnkcWXVfLrhUW21uLfOrMRYuC7hAu4w6qTsRxxkuK64ZYLFwh1AJKpx0b3MfeP4a9bJqOIuSIaX0gdfSjdlOiI0N+9+eTz208daJzzSzUY4BW5wYD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG3+QBGTw=="
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "state": "tx_+QEOCwH4hLhAtUTr2IQgSz9jxkWoBUjJa3WoAY6WEyyx6pTYG+0WubTecxnXSLIy6ud9tEqXDnkcWXVfLrhUW21uLfOrMRYuC7hAu4w6qTsRxxkuK64ZYLFwh1AJKpx0b3MfeP4a9bJqOIuSIaX0gdfSjdlOiI0N+9+eTz208daJzzSzUY4BW5wYD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG3+QBGTw=="
    }
  },
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjt59LjEddCu3XGMbiBKu2/sb9uWvGajlwC1UGeTyQugAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyp7T9bw=",
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjt59LjEddCu3XGMbiBKu2/sb9uWvGajlwC1UGeTyQugAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyp7T9bw=",
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjt59LjEddCu3XGMbiBKu2/sb9uWvGajlwC1UGeTyQugAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyp7T9bw=",
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
  "id": -576460752303422116,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAwhPNFruC/dLyxdmhN0Q74sx7xTPx99iLGIQcmz+l1llgoJs3f8q6vx/seIk2GjQPcC1VDFIAfa+Svg2dn9+ULuEj4RjkCoQY7efS4xHXQrt1xjG4gSrtv7G/blrxmo5cAtVBnk8kLoAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqd7sWE"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
  "id": -576460752303422116,
  "jsonrpc": "2.0",
  "result": "ok",
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
  "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAwhPNFruC/dLyxdmhN0Q74sx7xTPx99iLGIQcmz+l1llgoJs3f8q6vx/seIk2GjQPcC1VDFIAfa+Svg2dn9+ULuEj4RjkCoQY7efS4xHXQrt1xjG4gSrtv7G/blrxmo5cAtVBnk8kLoAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqd7sWE",
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
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
    "data": {
      "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
      "error_code": 42,
      "error_msg": "unknown",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422115,
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
  "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
  "id": -576460752303422115,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422114,
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
    "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
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
  "channel_id": "ch_TCFBizm3XNHeQjDDPKNof9wPtFksneSPy7QXe3LamEwyKsxP4",
  "id": -576460752303422114,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
