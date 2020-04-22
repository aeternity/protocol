
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
      "fsm_id": "ba_x7IJi+Hk62ars861+fzItRDdtIeKsFKCbZ4sXQK4AiPy0Ta7"
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
      "fsm_id": "ba_js1iur93LCrYJ8MgK0lcyMoOkzAGI7pcFIZSle6wNxhvPD8/"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYx/lR64A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422844,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA45hqso7CTJ5NUrNmKET+7ekDDwnfCVaZHCYpN5Qwl+LDvG8IMBC98nyT2gpGf7zvYnQXRyojAw27OectnVJ4MuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGMT58Fg0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422844,
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_js1iur93LCrYJ8MgK0lcyMoOkzAGI7pcFIZSle6wNxhvPD8/"
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEA45hqso7CTJ5NUrNmKET+7ekDDwnfCVaZHCYpN5Qwl+LDvG8IMBC98nyT2gpGf7zvYnQXRyojAw27OectnVJ4MuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGMT58Fg0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422843,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhANmibMw6G5apHtTunjFIctnq34R5kAN4fHgKXtfj2l1+vYqQ7aC9HkrLFmYodxkW5QeFKyl6qvmDooBoUej+xCLhAOOYarKOwkyeTVKzZihE/u3pAw8J3wlWmRwmKTeUMJfiw7xvCDAQvfJ8k9oKRn+872J0F0cqIwMNuznnLZ1SeDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjEY81hD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422843,
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhANmibMw6G5apHtTunjFIctnq34R5kAN4fHgKXtfj2l1+vYqQ7aC9HkrLFmYodxkW5QeFKyl6qvmDooBoUej+xCLhAOOYarKOwkyeTVKzZihE/u3pAw8J3wlWmRwmKTeUMJfiw7xvCDAQvfJ8k9oKRn+872J0F0cqIwMNuznnLZ1SeDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjEY81hD",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_x7IJi+Hk62ars861+fzItRDdtIeKsFKCbZ4sXQK4AiPy0Ta7"
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhANmibMw6G5apHtTunjFIctnq34R5kAN4fHgKXtfj2l1+vYqQ7aC9HkrLFmYodxkW5QeFKyl6qvmDooBoUej+xCLhAOOYarKOwkyeTVKzZihE/u3pAw8J3wlWmRwmKTeUMJfiw7xvCDAQvfJ8k9oKRn+872J0F0cqIwMNuznnLZ1SeDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjEY81hD",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhANmibMw6G5apHtTunjFIctnq34R5kAN4fHgKXtfj2l1+vYqQ7aC9HkrLFmYodxkW5QeFKyl6qvmDooBoUej+xCLhAOOYarKOwkyeTVKzZihE/u3pAw8J3wlWmRwmKTeUMJfiw7xvCDAQvfJ8k9oKRn+872J0F0cqIwMNuznnLZ1SeDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjEY81hD",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhANmibMw6G5apHtTunjFIctnq34R5kAN4fHgKXtfj2l1+vYqQ7aC9HkrLFmYodxkW5QeFKyl6qvmDooBoUej+xCLhAOOYarKOwkyeTVKzZihE/u3pAw8J3wlWmRwmKTeUMJfiw7xvCDAQvfJ8k9oKRn+872J0F0cqIwMNuznnLZ1SeDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjEY81hD",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
  "id": -576460752303422842,
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
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422842,
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "state": "tx_+QENCwH4hLhANmibMw6G5apHtTunjFIctnq34R5kAN4fHgKXtfj2l1+vYqQ7aC9HkrLFmYodxkW5QeFKyl6qvmDooBoUej+xCLhAOOYarKOwkyeTVKzZihE/u3pAw8J3wlWmRwmKTeUMJfiw7xvCDAQvfJ8k9oKRn+872J0F0cqIwMNuznnLZ1SeDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjEY81hD"
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "state": "tx_+QENCwH4hLhANmibMw6G5apHtTunjFIctnq34R5kAN4fHgKXtfj2l1+vYqQ7aC9HkrLFmYodxkW5QeFKyl6qvmDooBoUej+xCLhAOOYarKOwkyeTVKzZihE/u3pAw8J3wlWmRwmKTeUMJfiw7xvCDAQvfJ8k9oKRn+872J0F0cqIwMNuznnLZ1SeDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjEY81hD"
    }
  },
  "version": 1
}
```
