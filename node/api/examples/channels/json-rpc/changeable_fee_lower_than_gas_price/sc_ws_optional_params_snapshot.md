
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
      "fsm_id": "ba_EZCqcMutgh9wDe9Ddq9r1BB08IPJKPnrNijZb7XUEZ/mew/H"
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
      "fsm_id": "ba_3dTDzutYcMgtsVDZdZT7BwMJOQWcncBGYeTPMxIJrLMKvA6z"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBh47yBus=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422380,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECNvHlfYCB5wMpYdCrgz+bWyRTvMmBfFmuns85+G3vpMeXstzhZRwVrjMkKnYnmaGPsJRdGn/CW57/dxyrisM4FuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYf7iM54"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422380,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_3dTDzutYcMgtsVDZdZT7BwMJOQWcncBGYeTPMxIJrLMKvA6z"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECNvHlfYCB5wMpYdCrgz+bWyRTvMmBfFmuns85+G3vpMeXstzhZRwVrjMkKnYnmaGPsJRdGn/CW57/dxyrisM4FuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYf7iM54",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422379,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAiO5ZVfjseGaVZrYeUMA145AN3+HCseunNG/hl4UT8R5dxbIFRNQtUGmkVZ5WJoKIKkgMhX3N+6mPzkIyv9fgBrhAjbx5X2AgecDKWHQq4M/m1skU7zJgXxZrp7POfht76THl7Lc4WUcFa4zJCp2J5mhj7CUXRp/wlue/3ccq4rDOBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGH2hZunQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422379,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAiO5ZVfjseGaVZrYeUMA145AN3+HCseunNG/hl4UT8R5dxbIFRNQtUGmkVZ5WJoKIKkgMhX3N+6mPzkIyv9fgBrhAjbx5X2AgecDKWHQq4M/m1skU7zJgXxZrp7POfht76THl7Lc4WUcFa4zJCp2J5mhj7CUXRp/wlue/3ccq4rDOBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGH2hZunQ==",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_EZCqcMutgh9wDe9Ddq9r1BB08IPJKPnrNijZb7XUEZ/mew/H"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAiO5ZVfjseGaVZrYeUMA145AN3+HCseunNG/hl4UT8R5dxbIFRNQtUGmkVZ5WJoKIKkgMhX3N+6mPzkIyv9fgBrhAjbx5X2AgecDKWHQq4M/m1skU7zJgXxZrp7POfht76THl7Lc4WUcFa4zJCp2J5mhj7CUXRp/wlue/3ccq4rDOBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGH2hZunQ==",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAiO5ZVfjseGaVZrYeUMA145AN3+HCseunNG/hl4UT8R5dxbIFRNQtUGmkVZ5WJoKIKkgMhX3N+6mPzkIyv9fgBrhAjbx5X2AgecDKWHQq4M/m1skU7zJgXxZrp7POfht76THl7Lc4WUcFa4zJCp2J5mhj7CUXRp/wlue/3ccq4rDOBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGH2hZunQ==",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAiO5ZVfjseGaVZrYeUMA145AN3+HCseunNG/hl4UT8R5dxbIFRNQtUGmkVZ5WJoKIKkgMhX3N+6mPzkIyv9fgBrhAjbx5X2AgecDKWHQq4M/m1skU7zJgXxZrp7POfht76THl7Lc4WUcFa4zJCp2J5mhj7CUXRp/wlue/3ccq4rDOBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGH2hZunQ==",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "message": {
        "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "message": {
        "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
  "id": -576460752303422378,
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
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422378,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+QEOCwH4hLhAiO5ZVfjseGaVZrYeUMA145AN3+HCseunNG/hl4UT8R5dxbIFRNQtUGmkVZ5WJoKIKkgMhX3N+6mPzkIyv9fgBrhAjbx5X2AgecDKWHQq4M/m1skU7zJgXxZrp7POfht76THl7Lc4WUcFa4zJCp2J5mhj7CUXRp/wlue/3ccq4rDOBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGH2hZunQ=="
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+QEOCwH4hLhAiO5ZVfjseGaVZrYeUMA145AN3+HCseunNG/hl4UT8R5dxbIFRNQtUGmkVZ5WJoKIKkgMhX3N+6mPzkIyv9fgBrhAjbx5X2AgecDKWHQq4M/m1skU7zJgXxZrp7POfht76THl7Lc4WUcFa4zJCp2J5mhj7CUXRp/wlue/3ccq4rDOBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGH2hZunQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422377,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422377,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEOCwH4hLhAiO5ZVfjseGaVZrYeUMA145AN3+HCseunNG/hl4UT8R5dxbIFRNQtUGmkVZ5WJoKIKkgMhX3N+6mPzkIyv9fgBrhAjbx5X2AgecDKWHQq4M/m1skU7zJgXxZrp7POfht76THl7Lc4WUcFa4zJCp2J5mhj7CUXRp/wlue/3ccq4rDOBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGH2hZunQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422376,
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
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422376,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgX4HUcPDumTKSvzq0ahus+LKVEgYm69fLtfRtNMmIpPAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyk50Uks=",
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
  "id": -576460752303422375,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECS9/4C9BF+CdAwGFm2OSI2IBr3D7ubFmN9DyS+3QOW5znmdY8jMv55zqz0co8uoqOxK0reIGVCIiedUh8PeZwLuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqzm6c2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422375,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+JALAfhCuECS9/4C9BF+CdAwGFm2OSI2IBr3D7ubFmN9DyS+3QOW5znmdY8jMv55zqz0co8uoqOxK0reIGVCIiedUh8PeZwLuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqzm6c2",
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
  "id": -576460752303422374,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECS9/4C9BF+CdAwGFm2OSI2IBr3D7ubFmN9DyS+3QOW5znmdY8jMv55zqz0co8uoqOxK0reIGVCIiedUh8PeZwLuECmCShzTLXRLoSNV6teDICZd+rjZvPyEbRjCJgZN+9Ldl8onmG5AekVbrZKP32nhwu4Ad9BBq4wsdxEm+vAW+sCuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrRFYa/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422374,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuECS9/4C9BF+CdAwGFm2OSI2IBr3D7ubFmN9DyS+3QOW5znmdY8jMv55zqz0co8uoqOxK0reIGVCIiedUh8PeZwLuECmCShzTLXRLoSNV6teDICZd+rjZvPyEbRjCJgZN+9Ldl8onmG5AekVbrZKP32nhwu4Ad9BBq4wsdxEm+vAW+sCuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrRFYa/"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuECS9/4C9BF+CdAwGFm2OSI2IBr3D7ubFmN9DyS+3QOW5znmdY8jMv55zqz0co8uoqOxK0reIGVCIiedUh8PeZwLuECmCShzTLXRLoSNV6teDICZd+rjZvPyEbRjCJgZN+9Ldl8onmG5AekVbrZKP32nhwu4Ad9BBq4wsdxEm+vAW+sCuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrRFYa/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422373,
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
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422373,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422372,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422372,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECS9/4C9BF+CdAwGFm2OSI2IBr3D7ubFmN9DyS+3QOW5znmdY8jMv55zqz0co8uoqOxK0reIGVCIiedUh8PeZwLuECmCShzTLXRLoSNV6teDICZd+rjZvPyEbRjCJgZN+9Ldl8onmG5AekVbrZKP32nhwu4Ad9BBq4wsdxEm+vAW+sCuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrRFYa/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422371,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422371,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+QEvCwHAuQEp+QEmOwGhBgX4HUcPDumTKSvzq0ahus+LKVEgYm69fLtfRtNMmIpPoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuECS9/4C9BF+CdAwGFm2OSI2IBr3D7ubFmN9DyS+3QOW5znmdY8jMv55zqz0co8uoqOxK0reIGVCIiedUh8PeZwLuECmCShzTLXRLoSNV6teDICZd+rjZvPyEbRjCJgZN+9Ldl8onmG5AekVbrZKP32nhwu4Ad9BBq4wsdxEm+vAW+sCuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoAhhMLes1BWIGI41rKOw==",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFyCwH4QrhAvo5VYhGa44W/2ue7O2iV0vVpShbdykpr8J+f4Za8LPfiCNFt02wnesna0iRjr47BKSy7D9w10XTw7y+RaGKUB7kBKfkBJjsBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAkvf+AvQRfgnQMBhZtjkiNiAa9w+7mxZjfQ8kvt0Dluc55nWPIzL+ec6s9HKPLqKjsStK3iBlQiInnVIfD3mcC7hApgkoc0y10S6EjVerXgyAmXfq42bz8hG0YwiYGTfvS3ZfKJ5huQHpFW62Sj99p4cLuAHfQQauMLHcRJvrwFvrArhI+EY5AqEGBfgdRw8O6ZMpK/OrRqG6z4spUSBibr18u19G00yYik8CoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIYTC3rNQViBiDs2Cw4="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422370,
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
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422370,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    }
  ],
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgX4HUcPDumTKSvzq0ahus+LKVEgYm69fLtfRtNMmIpPA6CyPuq+gQA2a6qmnwMyrfvY3kyHmlBoHoJrMzYXSPbNfGLiL8Q=",
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
  "id": -576460752303422369,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDC08RqNLpt6TxQlxLThLhs9za2kw+vYHr5UzBDjFMdMGZBr49ah992OGDU4AogphAu1d4PmMUMUS7JcJ73jyYJuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzv5EaK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422369,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDC08RqNLpt6TxQlxLThLhs9za2kw+vYHr5UzBDjFMdMGZBr49ah992OGDU4AogphAu1d4PmMUMUS7JcJ73jyYJuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzv5EaK",
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
  "id": -576460752303422368,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDC08RqNLpt6TxQlxLThLhs9za2kw+vYHr5UzBDjFMdMGZBr49ah992OGDU4AogphAu1d4PmMUMUS7JcJ73jyYJuED8vx/D6ksVgNxpSiAvB1tZXlv2nyDjfDkT1YAYHwtlIuD9diV5At5vHseNVbTBtj3icNmXLdtGnAU5IATqbhEHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXxUu1u0"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422368,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuEDC08RqNLpt6TxQlxLThLhs9za2kw+vYHr5UzBDjFMdMGZBr49ah992OGDU4AogphAu1d4PmMUMUS7JcJ73jyYJuED8vx/D6ksVgNxpSiAvB1tZXlv2nyDjfDkT1YAYHwtlIuD9diV5At5vHseNVbTBtj3icNmXLdtGnAU5IATqbhEHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXxUu1u0"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuEDC08RqNLpt6TxQlxLThLhs9za2kw+vYHr5UzBDjFMdMGZBr49ah992OGDU4AogphAu1d4PmMUMUS7JcJ73jyYJuED8vx/D6ksVgNxpSiAvB1tZXlv2nyDjfDkT1YAYHwtlIuD9diV5At5vHseNVbTBtj3icNmXLdtGnAU5IATqbhEHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXxUu1u0"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422367,
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
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422367,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999997
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000003
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422366,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422366,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDC08RqNLpt6TxQlxLThLhs9za2kw+vYHr5UzBDjFMdMGZBr49ah992OGDU4AogphAu1d4PmMUMUS7JcJ73jyYJuED8vx/D6ksVgNxpSiAvB1tZXlv2nyDjfDkT1YAYHwtlIuD9diV5At5vHseNVbTBtj3icNmXLdtGnAU5IATqbhEHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXxUu1u0",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAA7DvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/3rbPVC"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422365,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422365,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000003
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999997
    }
  ],
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgX4HUcPDumTKSvzq0ahus+LKVEgYm69fLtfRtNMmIpPBKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCygD7Tmk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422364,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB0oIbgotmVS/tlYws3BOpGdutuiHKaUANVDAY59bqBg30LBE4x9vQeeZNaC7d4RA3xBVH8WJ4KfaAeW0J2p9IMuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr82n1F"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422364,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB0oIbgotmVS/tlYws3BOpGdutuiHKaUANVDAY59bqBg30LBE4x9vQeeZNaC7d4RA3xBVH8WJ4KfaAeW0J2p9IMuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr82n1F",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422363,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB0oIbgotmVS/tlYws3BOpGdutuiHKaUANVDAY59bqBg30LBE4x9vQeeZNaC7d4RA3xBVH8WJ4KfaAeW0J2p9IMuEDsUTdJIKERxEx5bXcpSjiY2+TYMp+4yp9cGub0ztg9kWiN0Cwi9NedtdjbwXdB0JRp98X6kPfWs9aZVb3oRF8DuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqeIIbU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422363,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuEB0oIbgotmVS/tlYws3BOpGdutuiHKaUANVDAY59bqBg30LBE4x9vQeeZNaC7d4RA3xBVH8WJ4KfaAeW0J2p9IMuEDsUTdJIKERxEx5bXcpSjiY2+TYMp+4yp9cGub0ztg9kWiN0Cwi9NedtdjbwXdB0JRp98X6kPfWs9aZVb3oRF8DuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqeIIbU"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuEB0oIbgotmVS/tlYws3BOpGdutuiHKaUANVDAY59bqBg30LBE4x9vQeeZNaC7d4RA3xBVH8WJ4KfaAeW0J2p9IMuEDsUTdJIKERxEx5bXcpSjiY2+TYMp+4yp9cGub0ztg9kWiN0Cwi9NedtdjbwXdB0JRp98X6kPfWs9aZVb3oRF8DuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqeIIbU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422362,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422362,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422361,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422361,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB0oIbgotmVS/tlYws3BOpGdutuiHKaUANVDAY59bqBg30LBE4x9vQeeZNaC7d4RA3xBVH8WJ4KfaAeW0J2p9IMuEDsUTdJIKERxEx5bXcpSjiY2+TYMp+4yp9cGub0ztg9kWiN0Cwi9NedtdjbwXdB0JRp98X6kPfWs9aZVb3oRF8DuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqeIIbU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFyCwH4QrhAvo5VYhGa44W/2ue7O2iV0vVpShbdykpr8J+f4Za8LPfiCNFt02wnesna0iRjr47BKSy7D9w10XTw7y+RaGKUB7kBKfkBJjsBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAkvf+AvQRfgnQMBhZtjkiNiAa9w+7mxZjfQ8kvt0Dluc55nWPIzL+ec6s9HKPLqKjsStK3iBlQiInnVIfD3mcC7hApgkoc0y10S6EjVerXgyAmXfq42bz8hG0YwiYGTfvS3ZfKJ5huQHpFW62Sj99p4cLuAHfQQauMLHcRJvrwFvrArhI+EY5AqEGBfgdRw8O6ZMpK/OrRqG6z4spUSBibr18u19G00yYik8CoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIYTC3rNQViBiDs2Cw4=",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFyCwH4QrhAvo5VYhGa44W/2ue7O2iV0vVpShbdykpr8J+f4Za8LPfiCNFt02wnesna0iRjr47BKSy7D9w10XTw7y+RaGKUB7kBKfkBJjsBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAkvf+AvQRfgnQMBhZtjkiNiAa9w+7mxZjfQ8kvt0Dluc55nWPIzL+ec6s9HKPLqKjsStK3iBlQiInnVIfD3mcC7hApgkoc0y10S6EjVerXgyAmXfq42bz8hG0YwiYGTfvS3ZfKJ5huQHpFW62Sj99p4cLuAHfQQauMLHcRJvrwFvrArhI+EY5AqEGBfgdRw8O6ZMpK/OrRqG6z4spUSBibr18u19G00yYik8CoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIYTC3rNQViBiDs2Cw4=",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "��=q�\u0000��3�H\u0007,(��3��]�9\u0015�q�<8h�\u0015�",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422360,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422360,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB0oIbgotmVS/tlYws3BOpGdutuiHKaUANVDAY59bqBg30LBE4x9vQeeZNaC7d4RA3xBVH8WJ4KfaAeW0J2p9IMuEDsUTdJIKERxEx5bXcpSjiY2+TYMp+4yp9cGub0ztg9kWiN0Cwi9NedtdjbwXdB0JRp98X6kPfWs9aZVb3oRF8DuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqeIIbU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422359,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422359,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    }
  ],
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgX4HUcPDumTKSvzq0ahus+LKVEgYm69fLtfRtNMmIpPBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjoSjx4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422358,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECBQS9TlShPxslYC84Ww1A7FAse4Vy28w18ZjDS8O1J3iZ2H1aU7IBnyutkxgXjun4+Gkulq73gn8CwBh2kIPkMuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaoL37a"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422358,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+JALAfhCuECBQS9TlShPxslYC84Ww1A7FAse4Vy28w18ZjDS8O1J3iZ2H1aU7IBnyutkxgXjun4+Gkulq73gn8CwBh2kIPkMuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaoL37a",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422357,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECBQS9TlShPxslYC84Ww1A7FAse4Vy28w18ZjDS8O1J3iZ2H1aU7IBnyutkxgXjun4+Gkulq73gn8CwBh2kIPkMuEDyFrKQY+ipUmxXX8vzt6Yn7gwV+DhNfqBDdMX8SZmfRYYHXyb+L/MUArFcQK8llS4PWiCrQDvJwDiLyqXcpUQIuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZA6D5I"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422357,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuECBQS9TlShPxslYC84Ww1A7FAse4Vy28w18ZjDS8O1J3iZ2H1aU7IBnyutkxgXjun4+Gkulq73gn8CwBh2kIPkMuEDyFrKQY+ipUmxXX8vzt6Yn7gwV+DhNfqBDdMX8SZmfRYYHXyb+L/MUArFcQK8llS4PWiCrQDvJwDiLyqXcpUQIuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZA6D5I"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuECBQS9TlShPxslYC84Ww1A7FAse4Vy28w18ZjDS8O1J3iZ2H1aU7IBnyutkxgXjun4+Gkulq73gn8CwBh2kIPkMuEDyFrKQY+ipUmxXX8vzt6Yn7gwV+DhNfqBDdMX8SZmfRYYHXyb+L/MUArFcQK8llS4PWiCrQDvJwDiLyqXcpUQIuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZA6D5I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422356,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422356,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000001
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422355,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422355,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECBQS9TlShPxslYC84Ww1A7FAse4Vy28w18ZjDS8O1J3iZ2H1aU7IBnyutkxgXjun4+Gkulq73gn8CwBh2kIPkMuEDyFrKQY+ipUmxXX8vzt6Yn7gwV+DhNfqBDdMX8SZmfRYYHXyb+L/MUArFcQK8llS4PWiCrQDvJwDiLyqXcpUQIuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZA6D5I",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422354,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422354,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBgX4HUcPDumTKSvzq0ahus+LKVEgYm69fLtfRtNMmIpPoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuECBQS9TlShPxslYC84Ww1A7FAse4Vy28w18ZjDS8O1J3iZ2H1aU7IBnyutkxgXjun4+Gkulq73gn8CwBh2kIPkMuEDyFrKQY+ipUmxXX8vzt6Yn7gwV+DhNfqBDdMX8SZmfRYYHXyb+L/MUArFcQK8llS4PWiCrQDvJwDiLyqXcpUQIuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMG0rUY8DeaFfhc",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAOsu0DLAPnbvsGV8WUcxJkkCUkMZPFr85+LtK0QGRqV8FGsZF5ACjX475i/fkR6VZHUC8hA59oQpj0CUW5/efArkBKPkBJTsBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAgUEvU5UoT8bJWAvOFsNQOxQLHuFctvMNfGYw0vDtSd4mdh9WlOyAZ8rrZMYF47p+PhpLpau94J/AsAYdpCD5DLhA8haykGPoqVJsV1/L87emJ+4MFfg4TX6gQ3TF/EmZn0WGB18m/i/zFAKxXECvJZUuD1ogq0A7ycA4i8ql3KVECLhI+EY5AqEGBfgdRw8O6ZMpK/OrRqG6z4spUSBibr18u19G00yYik8FoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtK1GPA3witUqA=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422353,
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
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422353,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgX4HUcPDumTKSvzq0ahus+LKVEgYm69fLtfRtNMmIpPBqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyocNHdk=",
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
  "id": -576460752303422352,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDOEBG7x8n9EkJsRlfeG48joT5GGmHY4SGMxqKKApil8zpbdLRLZ4YYnBAzvPzvMDrTCWBm2hsbTQ2KmZHC2PkPuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrFu2YO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422352,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDOEBG7x8n9EkJsRlfeG48joT5GGmHY4SGMxqKKApil8zpbdLRLZ4YYnBAzvPzvMDrTCWBm2hsbTQ2KmZHC2PkPuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrFu2YO",
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
  "id": -576460752303422351,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDOEBG7x8n9EkJsRlfeG48joT5GGmHY4SGMxqKKApil8zpbdLRLZ4YYnBAzvPzvMDrTCWBm2hsbTQ2KmZHC2PkPuEDnvb9mzidOpdcn4yNBWwaIMohT2NiK2Lc3Js9JCrlvqlRWLLcG6AKzIJpneQ3Pc51YbE2trNTMBj5LA4bXI5oHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspCdfbt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422351,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuEDOEBG7x8n9EkJsRlfeG48joT5GGmHY4SGMxqKKApil8zpbdLRLZ4YYnBAzvPzvMDrTCWBm2hsbTQ2KmZHC2PkPuEDnvb9mzidOpdcn4yNBWwaIMohT2NiK2Lc3Js9JCrlvqlRWLLcG6AKzIJpneQ3Pc51YbE2trNTMBj5LA4bXI5oHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspCdfbt"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuEDOEBG7x8n9EkJsRlfeG48joT5GGmHY4SGMxqKKApil8zpbdLRLZ4YYnBAzvPzvMDrTCWBm2hsbTQ2KmZHC2PkPuEDnvb9mzidOpdcn4yNBWwaIMohT2NiK2Lc3Js9JCrlvqlRWLLcG6AKzIJpneQ3Pc51YbE2trNTMBj5LA4bXI5oHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspCdfbt"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422350,
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
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422350,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422349,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422349,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDOEBG7x8n9EkJsRlfeG48joT5GGmHY4SGMxqKKApil8zpbdLRLZ4YYnBAzvPzvMDrTCWBm2hsbTQ2KmZHC2PkPuEDnvb9mzidOpdcn4yNBWwaIMohT2NiK2Lc3Js9JCrlvqlRWLLcG6AKzIJpneQ3Pc51YbE2trNTMBj5LA4bXI5oHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspCdfbt",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422348,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422348,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    }
  ],
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgX4HUcPDumTKSvzq0ahus+LKVEgYm69fLtfRtNMmIpPB6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RveWgfY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422347,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAUqn8NOOT4Eyhno0k1ldtJ6hCavkuRW/GY/ha/O76Mc+jpxW/UsRoWxqDzNTDlv4CIZJu4Ved+VqLXaOmF8+oHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZdw/Bq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422347,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAUqn8NOOT4Eyhno0k1ldtJ6hCavkuRW/GY/ha/O76Mc+jpxW/UsRoWxqDzNTDlv4CIZJu4Ved+VqLXaOmF8+oHuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZdw/Bq",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422346,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAUqn8NOOT4Eyhno0k1ldtJ6hCavkuRW/GY/ha/O76Mc+jpxW/UsRoWxqDzNTDlv4CIZJu4Ved+VqLXaOmF8+oHuEAWtFugaWc5mQu97bpJg68bS7fMNlcGP0tPZAuU2Qo0CRxekuXvJAFL5voOoTxfrGRkB+7/7ZKXKuHweA4OUdYBuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYPpN4A"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422346,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuEAUqn8NOOT4Eyhno0k1ldtJ6hCavkuRW/GY/ha/O76Mc+jpxW/UsRoWxqDzNTDlv4CIZJu4Ved+VqLXaOmF8+oHuEAWtFugaWc5mQu97bpJg68bS7fMNlcGP0tPZAuU2Qo0CRxekuXvJAFL5voOoTxfrGRkB+7/7ZKXKuHweA4OUdYBuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYPpN4A"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "state": "tx_+NILAfiEuEAUqn8NOOT4Eyhno0k1ldtJ6hCavkuRW/GY/ha/O76Mc+jpxW/UsRoWxqDzNTDlv4CIZJu4Ved+VqLXaOmF8+oHuEAWtFugaWc5mQu97bpJg68bS7fMNlcGP0tPZAuU2Qo0CRxekuXvJAFL5voOoTxfrGRkB+7/7ZKXKuHweA4OUdYBuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYPpN4A"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422345,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422345,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000001
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422344,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422344,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAUqn8NOOT4Eyhno0k1ldtJ6hCavkuRW/GY/ha/O76Mc+jpxW/UsRoWxqDzNTDlv4CIZJu4Ved+VqLXaOmF8+oHuEAWtFugaWc5mQu97bpJg68bS7fMNlcGP0tPZAuU2Qo0CRxekuXvJAFL5voOoTxfrGRkB+7/7ZKXKuHweA4OUdYBuEj4RjkCoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKTwegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYPpN4A",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAOsu0DLAPnbvsGV8WUcxJkkCUkMZPFr85+LtK0QGRqV8FGsZF5ACjX475i/fkR6VZHUC8hA59oQpj0CUW5/efArkBKPkBJTsBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAgUEvU5UoT8bJWAvOFsNQOxQLHuFctvMNfGYw0vDtSd4mdh9WlOyAZ8rrZMYF47p+PhpLpau94J/AsAYdpCD5DLhA8haykGPoqVJsV1/L87emJ+4MFfg4TX6gQ3TF/EmZn0WGB18m/i/zFAKxXECvJZUuD1ogq0A7ycA4i8ql3KVECLhI+EY5AqEGBfgdRw8O6ZMpK/OrRqG6z4spUSBibr18u19G00yYik8FoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtK1GPA3witUqA==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAOsu0DLAPnbvsGV8WUcxJkkCUkMZPFr85+LtK0QGRqV8FGsZF5ACjX475i/fkR6VZHUC8hA59oQpj0CUW5/efArkBKPkBJTsBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAgUEvU5UoT8bJWAvOFsNQOxQLHuFctvMNfGYw0vDtSd4mdh9WlOyAZ8rrZMYF47p+PhpLpau94J/AsAYdpCD5DLhA8haykGPoqVJsV1/L87emJ+4MFfg4TX6gQ3TF/EmZn0WGB18m/i/zFAKxXECvJZUuD1ogq0A7ycA4i8ql3KVECLhI+EY5AqEGBfgdRw8O6ZMpK/OrRqG6z4spUSBibr18u19G00yYik8FoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtK1GPA3witUqA==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "�|�U��]x:i�7��nR�\u001f��|)��X�\b��\u0011 ",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBgX4HUcPDumTKSvzq0ahus+LKVEgYm69fLtfRtNMmIpPoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBiRB5ltY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422343,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEAMvyLEKXp1q0G3t0+x+IPbVVmEDVHwL0+htm2qDRgmQl2S6Eh/hMypPqFRUeQFu4UVL0PrWjYEmWRX4DgWXAEBuGD4XjUBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYk2CKA4"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422343,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEAMvyLEKXp1q0G3t0+x+IPbVVmEDVHwL0+htm2qDRgmQl2S6Eh/hMypPqFRUeQFu4UVL0PrWjYEmWRX4DgWXAEBuGD4XjUBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYk2CKA4",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422342,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAMvyLEKXp1q0G3t0+x+IPbVVmEDVHwL0+htm2qDRgmQl2S6Eh/hMypPqFRUeQFu4UVL0PrWjYEmWRX4DgWXAEBuEAqnvMowlGuzmPNAxl8agVrV/QnJfgeClJTMtAQyi9LHK8VHpXW3+YC75k+4rYtwZ8LGXro+SSadSh9fbYPI80IuGD4XjUBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYm+SHsF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
  "id": -576460752303422342,
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAMvyLEKXp1q0G3t0+x+IPbVVmEDVHwL0+htm2qDRgmQl2S6Eh/hMypPqFRUeQFu4UVL0PrWjYEmWRX4DgWXAEBuEAqnvMowlGuzmPNAxl8agVrV/QnJfgeClJTMtAQyi9LHK8VHpXW3+YC75k+4rYtwZ8LGXro+SSadSh9fbYPI80IuGD4XjUBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYm+SHsF",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAMvyLEKXp1q0G3t0+x+IPbVVmEDVHwL0+htm2qDRgmQl2S6Eh/hMypPqFRUeQFu4UVL0PrWjYEmWRX4DgWXAEBuEAqnvMowlGuzmPNAxl8agVrV/QnJfgeClJTMtAQyi9LHK8VHpXW3+YC75k+4rYtwZ8LGXro+SSadSh9fbYPI80IuGD4XjUBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYm+SHsF",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAMvyLEKXp1q0G3t0+x+IPbVVmEDVHwL0+htm2qDRgmQl2S6Eh/hMypPqFRUeQFu4UVL0PrWjYEmWRX4DgWXAEBuEAqnvMowlGuzmPNAxl8agVrV/QnJfgeClJTMtAQyi9LHK8VHpXW3+YC75k+4rYtwZ8LGXro+SSadSh9fbYPI80IuGD4XjUBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYm+SHsF",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAMvyLEKXp1q0G3t0+x+IPbVVmEDVHwL0+htm2qDRgmQl2S6Eh/hMypPqFRUeQFu4UVL0PrWjYEmWRX4DgWXAEBuEAqnvMowlGuzmPNAxl8agVrV/QnJfgeClJTMtAQyi9LHK8VHpXW3+YC75k+4rYtwZ8LGXro+SSadSh9fbYPI80IuGD4XjUBoQYF+B1HDw7pkykr86tGobrPiylRIGJuvXy7X0bTTJiKT6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYm+SHsF",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
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
    "channel_id": "ch_3dUZJTn2D6gH6xcGhJ1E6Vj13RVKjkDZG39xrokHm9QWHkC5Q",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
