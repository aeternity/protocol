
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
      "fsm_id": "ba_oktuuInGM8fi7a75xG86WIEkDSmUbV8aHQtvJ7cGyliEpU7a"
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
      "fsm_id": "ba_6au9Tl3NdXpMQ31FW0gqBOyewvEUN0obY2dg+YSVutGGmQEH"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBnUzr2jU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422257,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAdet8RjRmJbIKKSANxnC0wVXelGC+y/C8vZ681nIKoCuObruN/5iqXUHLw7/YMxPePCsTc72zNarIl3O37bWMAuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZ1bEWsd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422257,
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_6au9Tl3NdXpMQ31FW0gqBOyewvEUN0obY2dg+YSVutGGmQEH"
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEAdet8RjRmJbIKKSANxnC0wVXelGC+y/C8vZ681nIKoCuObruN/5iqXUHLw7/YMxPePCsTc72zNarIl3O37bWMAuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZ1bEWsd",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422256,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAHXrfEY0ZiWyCikgDcZwtMFV3pRgvsvwvL2evNZyCqArjm67jf+Yql1By8O/2DMT3jwrE3O9szWqyJdzt+21jALhAXtXDhvjuSHq5pDit8PUdTw2v0tqMN9jIl2toOuoDOS71xmZp2heLvRDNPiVOE6jKSi1atBG6fvJQWWF05k/ADriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGdHmYYdg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
  "id": -576460752303422256,
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAHXrfEY0ZiWyCikgDcZwtMFV3pRgvsvwvL2evNZyCqArjm67jf+Yql1By8O/2DMT3jwrE3O9szWqyJdzt+21jALhAXtXDhvjuSHq5pDit8PUdTw2v0tqMN9jIl2toOuoDOS71xmZp2heLvRDNPiVOE6jKSi1atBG6fvJQWWF05k/ADriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGdHmYYdg==",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_oktuuInGM8fi7a75xG86WIEkDSmUbV8aHQtvJ7cGyliEpU7a"
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAHXrfEY0ZiWyCikgDcZwtMFV3pRgvsvwvL2evNZyCqArjm67jf+Yql1By8O/2DMT3jwrE3O9szWqyJdzt+21jALhAXtXDhvjuSHq5pDit8PUdTw2v0tqMN9jIl2toOuoDOS71xmZp2heLvRDNPiVOE6jKSi1atBG6fvJQWWF05k/ADriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGdHmYYdg==",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAHXrfEY0ZiWyCikgDcZwtMFV3pRgvsvwvL2evNZyCqArjm67jf+Yql1By8O/2DMT3jwrE3O9szWqyJdzt+21jALhAXtXDhvjuSHq5pDit8PUdTw2v0tqMN9jIl2toOuoDOS71xmZp2heLvRDNPiVOE6jKSi1atBG6fvJQWWF05k/ADriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGdHmYYdg==",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAHXrfEY0ZiWyCikgDcZwtMFV3pRgvsvwvL2evNZyCqArjm67jf+Yql1By8O/2DMT3jwrE3O9szWqyJdzt+21jALhAXtXDhvjuSHq5pDit8PUdTw2v0tqMN9jIl2toOuoDOS71xmZp2heLvRDNPiVOE6jKSi1atBG6fvJQWWF05k/ADriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGdHmYYdg==",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "message": {
        "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "message": {
        "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
  "id": -576460752303422255,
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
  "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
  "id": -576460752303422255,
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "state": "tx_+QEOCwH4hLhAHXrfEY0ZiWyCikgDcZwtMFV3pRgvsvwvL2evNZyCqArjm67jf+Yql1By8O/2DMT3jwrE3O9szWqyJdzt+21jALhAXtXDhvjuSHq5pDit8PUdTw2v0tqMN9jIl2toOuoDOS71xmZp2heLvRDNPiVOE6jKSi1atBG6fvJQWWF05k/ADriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGdHmYYdg=="
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "state": "tx_+QEOCwH4hLhAHXrfEY0ZiWyCikgDcZwtMFV3pRgvsvwvL2evNZyCqArjm67jf+Yql1By8O/2DMT3jwrE3O9szWqyJdzt+21jALhAXtXDhvjuSHq5pDit8PUdTw2v0tqMN9jIl2toOuoDOS71xmZp2heLvRDNPiVOE6jKSi1atBG6fvJQWWF05k/ADriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGdHmYYdg=="
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
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "signed_tx": "tx_+HwLAcC4d/h1NAGhBqYl8qeJphGDFGq45GjkmUGEHXouEfysUtrJSXGzA2oJoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/OmLnoAKDc0aEz/UgoEcs4ajohf9X9BGhuePf6GLqnUld1F+cQwQKDEtaH/ogX7A==",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBqYl8qeJphGDFGq45GjkmUGEHXouEfysUtrJSXGzA2oJoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBnn/eicM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422254,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEDcG+pm5pxXsAVqCDlpCamBZsGqD4k8m/VVjwR/3V+6KjRYqEew4gPlM4CX6RBBX7sIpfmAuM7HMVwVv3ypa5wAuGD4XjUBoQamJfKniaYRgxRquORo5JlBhB16LhH8rFLayUlxswNqCaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ7k1RA8"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
  "id": -576460752303422254,
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEDcG+pm5pxXsAVqCDlpCamBZsGqD4k8m/VVjwR/3V+6KjRYqEew4gPlM4CX6RBBX7sIpfmAuM7HMVwVv3ypa5wAuGD4XjUBoQamJfKniaYRgxRquORo5JlBhB16LhH8rFLayUlxswNqCaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ7k1RA8",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422253,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEDcG+pm5pxXsAVqCDlpCamBZsGqD4k8m/VVjwR/3V+6KjRYqEew4gPlM4CX6RBBX7sIpfmAuM7HMVwVv3ypa5wAuEDfxJE27LlKJktymchVhypzA6SsEVEVGpWRjLgNrcYsYqXm8P9aJ0f6fCT34c7KGiDe8pKE9V2AcA1LRUa32nwEuGD4XjUBoQamJfKniaYRgxRquORo5JlBhB16LhH8rFLayUlxswNqCaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ7PtbIe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
  "id": -576460752303422253,
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEDcG+pm5pxXsAVqCDlpCamBZsGqD4k8m/VVjwR/3V+6KjRYqEew4gPlM4CX6RBBX7sIpfmAuM7HMVwVv3ypa5wAuEDfxJE27LlKJktymchVhypzA6SsEVEVGpWRjLgNrcYsYqXm8P9aJ0f6fCT34c7KGiDe8pKE9V2AcA1LRUa32nwEuGD4XjUBoQamJfKniaYRgxRquORo5JlBhB16LhH8rFLayUlxswNqCaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ7PtbIe",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEDcG+pm5pxXsAVqCDlpCamBZsGqD4k8m/VVjwR/3V+6KjRYqEew4gPlM4CX6RBBX7sIpfmAuM7HMVwVv3ypa5wAuEDfxJE27LlKJktymchVhypzA6SsEVEVGpWRjLgNrcYsYqXm8P9aJ0f6fCT34c7KGiDe8pKE9V2AcA1LRUa32nwEuGD4XjUBoQamJfKniaYRgxRquORo5JlBhB16LhH8rFLayUlxswNqCaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ7PtbIe",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEDcG+pm5pxXsAVqCDlpCamBZsGqD4k8m/VVjwR/3V+6KjRYqEew4gPlM4CX6RBBX7sIpfmAuM7HMVwVv3ypa5wAuEDfxJE27LlKJktymchVhypzA6SsEVEVGpWRjLgNrcYsYqXm8P9aJ0f6fCT34c7KGiDe8pKE9V2AcA1LRUa32nwEuGD4XjUBoQamJfKniaYRgxRquORo5JlBhB16LhH8rFLayUlxswNqCaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ7PtbIe",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEDcG+pm5pxXsAVqCDlpCamBZsGqD4k8m/VVjwR/3V+6KjRYqEew4gPlM4CX6RBBX7sIpfmAuM7HMVwVv3ypa5wAuEDfxJE27LlKJktymchVhypzA6SsEVEVGpWRjLgNrcYsYqXm8P9aJ0f6fCT34c7KGiDe8pKE9V2AcA1LRUa32nwEuGD4XjUBoQamJfKniaYRgxRquORo5JlBhB16LhH8rFLayUlxswNqCaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ7PtbIe",
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
      "fsm_id": "ba_FfKofABySjRLSnYS3FbC2pJI4dmS24ymjJIUe/+7iPpBfLn4"
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
      "fsm_id": "ba_bF60fDmayGi5gVngtPwYRmWhNXJUpHTu7CIGNVTmcJQXAp8+"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBn8y724s=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422252,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAmwz/G53Wmaum9b3QX62Ilmc9RFr78TTXZB668P/6mJQVhqws82jCQz50Rx8eIIZOabw/AKvwsGC36VXwHxFgOuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZ/R6bss"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422252,
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_bF60fDmayGi5gVngtPwYRmWhNXJUpHTu7CIGNVTmcJQXAp8+"
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEAmwz/G53Wmaum9b3QX62Ilmc9RFr78TTXZB668P/6mJQVhqws82jCQz50Rx8eIIZOabw/AKvwsGC36VXwHxFgOuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZ/R6bss",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422251,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAJsM/xud1pmrpvW90F+tiJZnPURa+/E012QeuvD/+piUFYasLPNowkM+dEcfHiCGTmm8PwCr8LBgt+lV8B8RYDrhAMja4MdLNIWnrHnVaxBZ7Fo1wVUVZYyiIcMDpzK7R+IGl4zp6MoAc1NxEb12JzA5RcFc4jZ6xvO4uQEFJzY+CDriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGf8/TF0Q=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
  "id": -576460752303422251,
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAJsM/xud1pmrpvW90F+tiJZnPURa+/E012QeuvD/+piUFYasLPNowkM+dEcfHiCGTmm8PwCr8LBgt+lV8B8RYDrhAMja4MdLNIWnrHnVaxBZ7Fo1wVUVZYyiIcMDpzK7R+IGl4zp6MoAc1NxEb12JzA5RcFc4jZ6xvO4uQEFJzY+CDriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGf8/TF0Q==",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_FfKofABySjRLSnYS3FbC2pJI4dmS24ymjJIUe/+7iPpBfLn4"
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAJsM/xud1pmrpvW90F+tiJZnPURa+/E012QeuvD/+piUFYasLPNowkM+dEcfHiCGTmm8PwCr8LBgt+lV8B8RYDrhAMja4MdLNIWnrHnVaxBZ7Fo1wVUVZYyiIcMDpzK7R+IGl4zp6MoAc1NxEb12JzA5RcFc4jZ6xvO4uQEFJzY+CDriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGf8/TF0Q==",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAJsM/xud1pmrpvW90F+tiJZnPURa+/E012QeuvD/+piUFYasLPNowkM+dEcfHiCGTmm8PwCr8LBgt+lV8B8RYDrhAMja4MdLNIWnrHnVaxBZ7Fo1wVUVZYyiIcMDpzK7R+IGl4zp6MoAc1NxEb12JzA5RcFc4jZ6xvO4uQEFJzY+CDriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGf8/TF0Q==",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAJsM/xud1pmrpvW90F+tiJZnPURa+/E012QeuvD/+piUFYasLPNowkM+dEcfHiCGTmm8PwCr8LBgt+lV8B8RYDrhAMja4MdLNIWnrHnVaxBZ7Fo1wVUVZYyiIcMDpzK7R+IGl4zp6MoAc1NxEb12JzA5RcFc4jZ6xvO4uQEFJzY+CDriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGf8/TF0Q==",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
    "data": {
      "event": "closed_confirmed"
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_2GB2xAUSQ51t47zSg6UNhqEBtwYUDuKkzXpvjb98NKG4YmY1KE",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "message": {
        "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "message": {
        "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
  "id": -576460752303422250,
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
  "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
  "id": -576460752303422250,
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "state": "tx_+QEOCwH4hLhAJsM/xud1pmrpvW90F+tiJZnPURa+/E012QeuvD/+piUFYasLPNowkM+dEcfHiCGTmm8PwCr8LBgt+lV8B8RYDrhAMja4MdLNIWnrHnVaxBZ7Fo1wVUVZYyiIcMDpzK7R+IGl4zp6MoAc1NxEb12JzA5RcFc4jZ6xvO4uQEFJzY+CDriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGf8/TF0Q=="
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "state": "tx_+QEOCwH4hLhAJsM/xud1pmrpvW90F+tiJZnPURa+/E012QeuvD/+piUFYasLPNowkM+dEcfHiCGTmm8PwCr8LBgt+lV8B8RYDrhAMja4MdLNIWnrHnVaxBZ7Fo1wVUVZYyiIcMDpzK7R+IGl4zp6MoAc1NxEb12JzA5RcFc4jZ6xvO4uQEFJzY+CDriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGf8/TF0Q=="
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
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "signed_tx": "tx_+HwLAcC4d/h1NAGhBhg3yDjBSALlw+MhgcYnUPPOLxDVpiQvkKJOoWP3qkjNoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/OmLnoAKA5h8lYmnwxnMmzI9HJYz8WeQqOJ0lIGp/4HghPxzVzOQKDEtaHXPw6dw==",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBhg3yDjBSALlw+MhgcYnUPPOLxDVpiQvkKJOoWP3qkjNoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBoCFODes=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422249,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEA0ZN0cd38WlADBl8+pUV1MCjrvbRbYS6OeUZ2BdULWE+79nZfEIbil5eC54XBFYkecF8rdnO6OD0fF3vmWZe8EuGD4XjUBoQYYN8g4wUgC5cPjIYHGJ1Dzzi8Q1aYkL5CiTqFj96pIzaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaDhbyTO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
  "id": -576460752303422249,
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEA0ZN0cd38WlADBl8+pUV1MCjrvbRbYS6OeUZ2BdULWE+79nZfEIbil5eC54XBFYkecF8rdnO6OD0fF3vmWZe8EuGD4XjUBoQYYN8g4wUgC5cPjIYHGJ1Dzzi8Q1aYkL5CiTqFj96pIzaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaDhbyTO",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422248,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEADQNB6+ve54b00NmigIvREwniL9VociWDXsCwknmg9WVUBnILWXo0WWFX9Lwz9fpZAXqkH74oOQLeNHUntDjsOuEA0ZN0cd38WlADBl8+pUV1MCjrvbRbYS6OeUZ2BdULWE+79nZfEIbil5eC54XBFYkecF8rdnO6OD0fF3vmWZe8EuGD4XjUBoQYYN8g4wUgC5cPjIYHGJ1Dzzi8Q1aYkL5CiTqFj96pIzaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaAM26ik"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
  "id": -576460752303422248,
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEADQNB6+ve54b00NmigIvREwniL9VociWDXsCwknmg9WVUBnILWXo0WWFX9Lwz9fpZAXqkH74oOQLeNHUntDjsOuEA0ZN0cd38WlADBl8+pUV1MCjrvbRbYS6OeUZ2BdULWE+79nZfEIbil5eC54XBFYkecF8rdnO6OD0fF3vmWZe8EuGD4XjUBoQYYN8g4wUgC5cPjIYHGJ1Dzzi8Q1aYkL5CiTqFj96pIzaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaAM26ik",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEADQNB6+ve54b00NmigIvREwniL9VociWDXsCwknmg9WVUBnILWXo0WWFX9Lwz9fpZAXqkH74oOQLeNHUntDjsOuEA0ZN0cd38WlADBl8+pUV1MCjrvbRbYS6OeUZ2BdULWE+79nZfEIbil5eC54XBFYkecF8rdnO6OD0fF3vmWZe8EuGD4XjUBoQYYN8g4wUgC5cPjIYHGJ1Dzzi8Q1aYkL5CiTqFj96pIzaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaAM26ik",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEADQNB6+ve54b00NmigIvREwniL9VociWDXsCwknmg9WVUBnILWXo0WWFX9Lwz9fpZAXqkH74oOQLeNHUntDjsOuEA0ZN0cd38WlADBl8+pUV1MCjrvbRbYS6OeUZ2BdULWE+79nZfEIbil5eC54XBFYkecF8rdnO6OD0fF3vmWZe8EuGD4XjUBoQYYN8g4wUgC5cPjIYHGJ1Dzzi8Q1aYkL5CiTqFj96pIzaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaAM26ik",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEADQNB6+ve54b00NmigIvREwniL9VociWDXsCwknmg9WVUBnILWXo0WWFX9Lwz9fpZAXqkH74oOQLeNHUntDjsOuEA0ZN0cd38WlADBl8+pUV1MCjrvbRbYS6OeUZ2BdULWE+79nZfEIbil5eC54XBFYkecF8rdnO6OD0fF3vmWZe8EuGD4XjUBoQYYN8g4wUgC5cPjIYHGJ1Dzzi8Q1aYkL5CiTqFj96pIzaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaAM26ik",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
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
    "channel_id": "ch_BfcbZnKQXSh5B5FQL4jP3Qo2TMv4N4vsVE5HdxRBvgeiqGaR3",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
