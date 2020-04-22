
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
      "fsm_id": "ba_4V1yRvLGqvKkQTEMeBcRnjSBBbv4bxqrtL2XJEs8hH5LiUCU"
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
      "fsm_id": "ba_6pSIVGJny2Dk95u3+fdeGvYc76JEWLkFTK6emJCs6ZhX0wB4"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBrYMq8E4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422195,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEA8PTx16V2AcqNQn2JETC/2egDA63VlxlRgdQabWAm+slxzTu+vrKrMUN5yuWrA5nWGs8tPQRVk1Ka2pgMhZbMPuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGga37Cjju"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422195,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_6pSIVGJny2Dk95u3+fdeGvYc76JEWLkFTK6emJCs6ZhX0wB4"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEA8PTx16V2AcqNQn2JETC/2egDA63VlxlRgdQabWAm+slxzTu+vrKrMUN5yuWrA5nWGs8tPQRVk1Ka2pgMhZbMPuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGga37Cjju",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422194,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAPD08deldgHKjUJ9iREwv9noAwOt1ZcZUYHUGm1gJvrJcc07vr6yqzFDecrlqwOZ1hrPLT0EVZNSmtqYDIWWzD7hAQdR3eC84L3DL0DcmOr1WtOs20HHLd5dl9njpMJTVwPJ8VAz5ZFzIw8MO8ebzSw7OGlchgoa8XoRUErSpY69HAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGtYH4TJA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422194,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAPD08deldgHKjUJ9iREwv9noAwOt1ZcZUYHUGm1gJvrJcc07vr6yqzFDecrlqwOZ1hrPLT0EVZNSmtqYDIWWzD7hAQdR3eC84L3DL0DcmOr1WtOs20HHLd5dl9njpMJTVwPJ8VAz5ZFzIw8MO8ebzSw7OGlchgoa8XoRUErSpY69HAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGtYH4TJA==",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_4V1yRvLGqvKkQTEMeBcRnjSBBbv4bxqrtL2XJEs8hH5LiUCU"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAPD08deldgHKjUJ9iREwv9noAwOt1ZcZUYHUGm1gJvrJcc07vr6yqzFDecrlqwOZ1hrPLT0EVZNSmtqYDIWWzD7hAQdR3eC84L3DL0DcmOr1WtOs20HHLd5dl9njpMJTVwPJ8VAz5ZFzIw8MO8ebzSw7OGlchgoa8XoRUErSpY69HAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGtYH4TJA==",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAPD08deldgHKjUJ9iREwv9noAwOt1ZcZUYHUGm1gJvrJcc07vr6yqzFDecrlqwOZ1hrPLT0EVZNSmtqYDIWWzD7hAQdR3eC84L3DL0DcmOr1WtOs20HHLd5dl9njpMJTVwPJ8VAz5ZFzIw8MO8ebzSw7OGlchgoa8XoRUErSpY69HAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGtYH4TJA==",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAPD08deldgHKjUJ9iREwv9noAwOt1ZcZUYHUGm1gJvrJcc07vr6yqzFDecrlqwOZ1hrPLT0EVZNSmtqYDIWWzD7hAQdR3eC84L3DL0DcmOr1WtOs20HHLd5dl9njpMJTVwPJ8VAz5ZFzIw8MO8ebzSw7OGlchgoa8XoRUErSpY69HAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGtYH4TJA==",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "message": {
        "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "message": {
        "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
  "id": -576460752303422193,
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422193,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+QEOCwH4hLhAPD08deldgHKjUJ9iREwv9noAwOt1ZcZUYHUGm1gJvrJcc07vr6yqzFDecrlqwOZ1hrPLT0EVZNSmtqYDIWWzD7hAQdR3eC84L3DL0DcmOr1WtOs20HHLd5dl9njpMJTVwPJ8VAz5ZFzIw8MO8ebzSw7OGlchgoa8XoRUErSpY69HAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGtYH4TJA=="
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+QEOCwH4hLhAPD08deldgHKjUJ9iREwv9noAwOt1ZcZUYHUGm1gJvrJcc07vr6yqzFDecrlqwOZ1hrPLT0EVZNSmtqYDIWWzD7hAQdR3eC84L3DL0DcmOr1WtOs20HHLd5dl9njpMJTVwPJ8VAz5ZFzIw8MO8ebzSw7OGlchgoa8XoRUErSpY69HAriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGtYH4TJA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422192,
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422192,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl83o4JyoTpnALQZU8lambEbct+1Hz8NukPwe3/gOZnwAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCytc/SA8=",
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
  "id": -576460752303422191,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBSnsY69FviLZj6IbqzlRT7jXu/gIs+NTApZtOpRUJbPFLar4nLYQgkDV1CzMcE9tHOjUM+Scy7BX5Bag5Cz9EHuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp0pwNs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422191,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBSnsY69FviLZj6IbqzlRT7jXu/gIs+NTApZtOpRUJbPFLar4nLYQgkDV1CzMcE9tHOjUM+Scy7BX5Bag5Cz9EHuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp0pwNs",
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
  "id": -576460752303422190,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBSnsY69FviLZj6IbqzlRT7jXu/gIs+NTApZtOpRUJbPFLar4nLYQgkDV1CzMcE9tHOjUM+Scy7BX5Bag5Cz9EHuEBgiytqRTeLE5fOLmnn4gY3VJDa/wq4fKkhzzwzPGX2Kn1h0dweSFl6wFojMpu9pfciwi+Wa5AEtqP75pBCqn4KuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoZ1+6Q"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422190,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+NILAfiEuEBSnsY69FviLZj6IbqzlRT7jXu/gIs+NTApZtOpRUJbPFLar4nLYQgkDV1CzMcE9tHOjUM+Scy7BX5Bag5Cz9EHuEBgiytqRTeLE5fOLmnn4gY3VJDa/wq4fKkhzzwzPGX2Kn1h0dweSFl6wFojMpu9pfciwi+Wa5AEtqP75pBCqn4KuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoZ1+6Q"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+NILAfiEuEBSnsY69FviLZj6IbqzlRT7jXu/gIs+NTApZtOpRUJbPFLar4nLYQgkDV1CzMcE9tHOjUM+Scy7BX5Bag5Cz9EHuEBgiytqRTeLE5fOLmnn4gY3VJDa/wq4fKkhzzwzPGX2Kn1h0dweSFl6wFojMpu9pfciwi+Wa5AEtqP75pBCqn4KuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoZ1+6Q"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422189,
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422189,
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
  "id": -576460752303422188,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422188,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBSnsY69FviLZj6IbqzlRT7jXu/gIs+NTApZtOpRUJbPFLar4nLYQgkDV1CzMcE9tHOjUM+Scy7BX5Bag5Cz9EHuEBgiytqRTeLE5fOLmnn4gY3VJDa/wq4fKkhzzwzPGX2Kn1h0dweSFl6wFojMpu9pfciwi+Wa5AEtqP75pBCqn4KuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoZ1+6Q",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422187,
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422187,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl83o4JyoTpnALQZU8lambEbct+1Hz8NukPwe3/gOZnwA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RrWBVdI=",
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
  "id": -576460752303422186,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAJ51X9pxFwDD3bIzN6UXJT+Hc1dNkFVKzx7z4k3iaeka/71nknry2k3s/sKTpTF8nV0x4s68Nw3C/D8/Od7OYDuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbOfU17"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422186,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAJ51X9pxFwDD3bIzN6UXJT+Hc1dNkFVKzx7z4k3iaeka/71nknry2k3s/sKTpTF8nV0x4s68Nw3C/D8/Od7OYDuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbOfU17",
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
  "id": -576460752303422185,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAJ51X9pxFwDD3bIzN6UXJT+Hc1dNkFVKzx7z4k3iaeka/71nknry2k3s/sKTpTF8nV0x4s68Nw3C/D8/Od7OYDuEC6HEWRyKJ9WdAhF6n3FNr7oQ7vKQKDFRi66jN0wpalDZ+SzorQnrNTkjk6DJRQ3mLzGaJ/5xPOv8XubES8j58CuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaONjlX"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422185,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+NILAfiEuEAJ51X9pxFwDD3bIzN6UXJT+Hc1dNkFVKzx7z4k3iaeka/71nknry2k3s/sKTpTF8nV0x4s68Nw3C/D8/Od7OYDuEC6HEWRyKJ9WdAhF6n3FNr7oQ7vKQKDFRi66jN0wpalDZ+SzorQnrNTkjk6DJRQ3mLzGaJ/5xPOv8XubES8j58CuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaONjlX"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+NILAfiEuEAJ51X9pxFwDD3bIzN6UXJT+Hc1dNkFVKzx7z4k3iaeka/71nknry2k3s/sKTpTF8nV0x4s68Nw3C/D8/Od7OYDuEC6HEWRyKJ9WdAhF6n3FNr7oQ7vKQKDFRi66jN0wpalDZ+SzorQnrNTkjk6DJRQ3mLzGaJ/5xPOv8XubES8j58CuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaONjlX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422184,
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422184,
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
  "id": -576460752303422183,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422183,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAJ51X9pxFwDD3bIzN6UXJT+Hc1dNkFVKzx7z4k3iaeka/71nknry2k3s/sKTpTF8nV0x4s68Nw3C/D8/Od7OYDuEC6HEWRyKJ9WdAhF6n3FNr7oQ7vKQKDFRi66jN0wpalDZ+SzorQnrNTkjk6DJRQ3mLzGaJ/5xPOv8XubES8j58CuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaONjlX",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422182,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422182,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAJ51X9pxFwDD3bIzN6UXJT+Hc1dNkFVKzx7z4k3iaeka/71nknry2k3s/sKTpTF8nV0x4s68Nw3C/D8/Od7OYDuEC6HEWRyKJ9WdAhF6n3FNr7oQ7vKQKDFRi66jN0wpalDZ+SzorQnrNTkjk6DJRQ3mLzGaJ/5xPOv8XubES8j58CuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaONjlX",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422181,
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422181,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl83o4JyoTpnALQZU8lambEbct+1Hz8NukPwe3/gOZnwBKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCymnfunc=",
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
  "id": -576460752303422180,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB0DjVmDLqDLs9pUkK4VIuSLyyTMk3x2Crwbv78rjneRBv7CM4/IQugQtNbl3RtE0RjarGF7GdsdbQOPBsgOC4BuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8ASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspFhEpd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422180,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB0DjVmDLqDLs9pUkK4VIuSLyyTMk3x2Crwbv78rjneRBv7CM4/IQugQtNbl3RtE0RjarGF7GdsdbQOPBsgOC4BuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8ASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspFhEpd",
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
  "id": -576460752303422179,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB0DjVmDLqDLs9pUkK4VIuSLyyTMk3x2Crwbv78rjneRBv7CM4/IQugQtNbl3RtE0RjarGF7GdsdbQOPBsgOC4BuECCEADHeb1uFsg2mqWWboVFAXfxrqvLSY29w5VXvRQliWBFBOYtbFkwWh12NnKtW4EPxd0GnLx17Xwnptg6VlgBuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8ASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr1cy5O"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422179,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+NILAfiEuEB0DjVmDLqDLs9pUkK4VIuSLyyTMk3x2Crwbv78rjneRBv7CM4/IQugQtNbl3RtE0RjarGF7GdsdbQOPBsgOC4BuECCEADHeb1uFsg2mqWWboVFAXfxrqvLSY29w5VXvRQliWBFBOYtbFkwWh12NnKtW4EPxd0GnLx17Xwnptg6VlgBuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8ASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr1cy5O"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+NILAfiEuEB0DjVmDLqDLs9pUkK4VIuSLyyTMk3x2Crwbv78rjneRBv7CM4/IQugQtNbl3RtE0RjarGF7GdsdbQOPBsgOC4BuECCEADHeb1uFsg2mqWWboVFAXfxrqvLSY29w5VXvRQliWBFBOYtbFkwWh12NnKtW4EPxd0GnLx17Xwnptg6VlgBuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8ASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr1cy5O"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422178,
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422178,
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
  "id": -576460752303422177,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422177,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB0DjVmDLqDLs9pUkK4VIuSLyyTMk3x2Crwbv78rjneRBv7CM4/IQugQtNbl3RtE0RjarGF7GdsdbQOPBsgOC4BuECCEADHeb1uFsg2mqWWboVFAXfxrqvLSY29w5VXvRQliWBFBOYtbFkwWh12NnKtW4EPxd0GnLx17Xwnptg6VlgBuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8ASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr1cy5O",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422176,
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422176,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl83o4JyoTpnALQZU8lambEbct+1Hz8NukPwe3/gOZnwBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Ru/8mMM=",
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
  "id": -576460752303422175,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZM7wqZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422175,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZM7wqZ",
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
  "id": -576460752303422174,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuED9bPoUWnveF4dfL8pr4L/27bRVwTEYa7hi4Hg+OzY5KxsEWwn0W8IASOPrVbpBLQgHnoaAlwuT+YRspPw3aZcGuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY2gibp"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422174,
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+NILAfiEuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuED9bPoUWnveF4dfL8pr4L/27bRVwTEYa7hi4Hg+OzY5KxsEWwn0W8IASOPrVbpBLQgHnoaAlwuT+YRspPw3aZcGuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY2gibp"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "state": "tx_+NILAfiEuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuED9bPoUWnveF4dfL8pr4L/27bRVwTEYa7hi4Hg+OzY5KxsEWwn0W8IASOPrVbpBLQgHnoaAlwuT+YRspPw3aZcGuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY2gibp"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422173,
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422173,
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
  "id": -576460752303422172,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422172,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuED9bPoUWnveF4dfL8pr4L/27bRVwTEYa7hi4Hg+OzY5KxsEWwn0W8IASOPrVbpBLQgHnoaAlwuT+YRspPw3aZcGuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY2gibp",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuED9bPoUWnveF4dfL8pr4L/27bRVwTEYa7hi4Hg+OzY5KxsEWwn0W8IASOPrVbpBLQgHnoaAlwuT+YRspPw3aZcGuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY2gibp",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuED9bPoUWnveF4dfL8pr4L/27bRVwTEYa7hi4Hg+OzY5KxsEWwn0W8IASOPrVbpBLQgHnoaAlwuT+YRspPw3aZcGuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY2gibp",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
  "method": "channels.slash",
  "params": {
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+QKACwHAuQJ6+QJ3NwGhBl83o4JyoTpnALQZU8lambEbct+1Hz8NukPwe3/gOZnwoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuED9bPoUWnveF4dfL8pr4L/27bRVwTEYa7hi4Hg+OzY5KxsEWwn0W8IASOPrVbpBLQgHnoaAlwuT+YRspPw3aZcGuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGSzAkUAAgxLWh3H2448=",
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
  "method": "channels.slash_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422171,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
  "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
  "id": -576460752303422171,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBl83o4JyoTpnALQZU8lambEbct+1Hz8NukPwe3/gOZnwoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBb0GnxbQyGdST1jEOQVIy5TLsoFbO0KpLg7palTNjP7mjImYfyGV4K4ph+K254GxrmC8GWQJ7o7XcC3Fdx+gQJuED9bPoUWnveF4dfL8pr4L/27bRVwTEYa7hi4Hg+OzY5KxsEWwn0W8IASOPrVbpBLQgHnoaAlwuT+YRspPw3aZcGuEj4RjkCoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8AWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGSNwYbAAga9eyqsB",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLBCwH4QrhAQ6Y1JoyyPxsjylUeN5lDnik8Ttp4koiAVzU4P2RlNp3LKTLNTu2vevcNYlfMhLnMP2KbNzZoFv1OYPS3sqBtAbkCePkCdTcBoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAW9Bp8W0MhnUk9YxDkFSMuUy7KBWztCqS4O6WpUzYz+5oyJmH8hleCuKYfitueBsa5gvBlkCe6O13AtxXcfoECbhA/Wz6FFp73heHXy/Ka+C/9u20VcExGGu4YuB4Pjs2OSsbBFsJ9FvCAEjj61W6QS0IB56GgJcLk/mEbKT8N2mXBrhI+EY5AqEGXzejgnKhOmcAtBlTyVqZsRty37UfPw26Q/B7f+A5mfAFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIGvkuzMNQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAQ6Y1JoyyPxsjylUeN5lDnik8Ttp4koiAVzU4P2RlNp3LKTLNTu2vevcNYlfMhLnMP2KbNzZoFv1OYPS3sqBtAbkCePkCdTcBoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAW9Bp8W0MhnUk9YxDkFSMuUy7KBWztCqS4O6WpUzYz+5oyJmH8hleCuKYfitueBsa5gvBlkCe6O13AtxXcfoECbhA/Wz6FFp73heHXy/Ka+C/9u20VcExGGu4YuB4Pjs2OSsbBFsJ9FvCAEjj61W6QS0IB56GgJcLk/mEbKT8N2mXBrhI+EY5AqEGXzejgnKhOmcAtBlTyVqZsRty37UfPw26Q/B7f+A5mfAFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIGvkuzMNQ==",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAQ6Y1JoyyPxsjylUeN5lDnik8Ttp4koiAVzU4P2RlNp3LKTLNTu2vevcNYlfMhLnMP2KbNzZoFv1OYPS3sqBtAbkCePkCdTcBoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAW9Bp8W0MhnUk9YxDkFSMuUy7KBWztCqS4O6WpUzYz+5oyJmH8hleCuKYfitueBsa5gvBlkCe6O13AtxXcfoECbhA/Wz6FFp73heHXy/Ka+C/9u20VcExGGu4YuB4Pjs2OSsbBFsJ9FvCAEjj61W6QS0IB56GgJcLk/mEbKT8N2mXBrhI+EY5AqEGXzejgnKhOmcAtBlTyVqZsRty37UfPw26Q/B7f+A5mfAFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIGvkuzMNQ==",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBl83o4JyoTpnALQZU8lambEbct+1Hz8NukPwe3/gOZnwoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAA/f6+PJA==",
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
    "signed_tx": "tx_+KcLAfhCuEDNgKlBx7HL7GP8M0Ud/wQ53GphkTFVG7m4H7vk6KzDAZ25hidHDUZG6tEfeLuu4WpTvM/altcUsXtdSIf+BZIOuF/4XTgBoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8KEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAP802qfk="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDNgKlBx7HL7GP8M0Ud/wQ53GphkTFVG7m4H7vk6KzDAZ25hidHDUZG6tEfeLuu4WpTvM/altcUsXtdSIf+BZIOuF/4XTgBoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8KEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAP802qfk=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDNgKlBx7HL7GP8M0Ud/wQ53GphkTFVG7m4H7vk6KzDAZ25hidHDUZG6tEfeLuu4WpTvM/altcUsXtdSIf+BZIOuF/4XTgBoQZfN6OCcqE6ZwC0GVPJWpmxG3LftR8/DbpD8Ht/4DmZ8KEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAP802qfk=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
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
    "channel_id": "ch_iwCYr7YpEXkqQLU1RnSs2FK612DbYg9xMp5Upk4d5RnTcs3Co",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

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
      "fsm_id": "ba_rcXmjuek2mREB2Eh6jmQ6DJXjuacmwz724IR6UHPtGRlgnnb"
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
      "fsm_id": "ba_JBl1T4gBLcofFmBxpbDflmNfzpf1LhQzoFhwzMiuckgwGT+4"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBsEnwj1U=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422170,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEARtQUf08DQnjaC9asCPcpKDfhanceIi2ieutzdW/vVJljQzugEHGTBAf2lpvGMd7BtVURqTWlcc9NKAI3g3zkDuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbAqmurP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422170,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_JBl1T4gBLcofFmBxpbDflmNfzpf1LhQzoFhwzMiuckgwGT+4"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEARtQUf08DQnjaC9asCPcpKDfhanceIi2ieutzdW/vVJljQzugEHGTBAf2lpvGMd7BtVURqTWlcc9NKAI3g3zkDuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbAqmurP",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422169,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAEbUFH9PA0J42gvWrAj3KSg34Wp3HiItonrrc3Vv71SZY0M7oBBxkwQH9pabxjHewbVVEak1pXHPTSgCN4N85A7hAxqFX/Vaxv/4PXTxs1i/cu9DJEjg4zpYWIUP1kjoEzHLAhGpPZZ83HFieHT4SQ4A7ywPlyCnRzC4uj859Ji6dALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGwzChSfA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422169,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAEbUFH9PA0J42gvWrAj3KSg34Wp3HiItonrrc3Vv71SZY0M7oBBxkwQH9pabxjHewbVVEak1pXHPTSgCN4N85A7hAxqFX/Vaxv/4PXTxs1i/cu9DJEjg4zpYWIUP1kjoEzHLAhGpPZZ83HFieHT4SQ4A7ywPlyCnRzC4uj859Ji6dALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGwzChSfA==",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_rcXmjuek2mREB2Eh6jmQ6DJXjuacmwz724IR6UHPtGRlgnnb"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAEbUFH9PA0J42gvWrAj3KSg34Wp3HiItonrrc3Vv71SZY0M7oBBxkwQH9pabxjHewbVVEak1pXHPTSgCN4N85A7hAxqFX/Vaxv/4PXTxs1i/cu9DJEjg4zpYWIUP1kjoEzHLAhGpPZZ83HFieHT4SQ4A7ywPlyCnRzC4uj859Ji6dALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGwzChSfA==",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAEbUFH9PA0J42gvWrAj3KSg34Wp3HiItonrrc3Vv71SZY0M7oBBxkwQH9pabxjHewbVVEak1pXHPTSgCN4N85A7hAxqFX/Vaxv/4PXTxs1i/cu9DJEjg4zpYWIUP1kjoEzHLAhGpPZZ83HFieHT4SQ4A7ywPlyCnRzC4uj859Ji6dALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGwzChSfA==",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAEbUFH9PA0J42gvWrAj3KSg34Wp3HiItonrrc3Vv71SZY0M7oBBxkwQH9pabxjHewbVVEak1pXHPTSgCN4N85A7hAxqFX/Vaxv/4PXTxs1i/cu9DJEjg4zpYWIUP1kjoEzHLAhGpPZZ83HFieHT4SQ4A7ywPlyCnRzC4uj859Ji6dALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGwzChSfA==",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "message": {
        "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "message": {
        "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
  "id": -576460752303422168,
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422168,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+QEOCwH4hLhAEbUFH9PA0J42gvWrAj3KSg34Wp3HiItonrrc3Vv71SZY0M7oBBxkwQH9pabxjHewbVVEak1pXHPTSgCN4N85A7hAxqFX/Vaxv/4PXTxs1i/cu9DJEjg4zpYWIUP1kjoEzHLAhGpPZZ83HFieHT4SQ4A7ywPlyCnRzC4uj859Ji6dALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGwzChSfA=="
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+QEOCwH4hLhAEbUFH9PA0J42gvWrAj3KSg34Wp3HiItonrrc3Vv71SZY0M7oBBxkwQH9pabxjHewbVVEak1pXHPTSgCN4N85A7hAxqFX/Vaxv/4PXTxs1i/cu9DJEjg4zpYWIUP1kjoEzHLAhGpPZZ83HFieHT4SQ4A7ywPlyCnRzC4uj859Ji6dALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGwzChSfA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422167,
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422167,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnRvr9ANzexKcP86SMt+ZoUwut36yH+ZLokfef15hpyEAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyiSNkns=",
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
  "id": -576460752303422166,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBDIqDDp3iXftuMXDN1aC0ndxZCYqqocHGk0BX81/xy3KKktUL1OKq/Sp9cnGHIeJ3zxcUxF3VX8KX8zcUJA94JuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrDYB3l"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422166,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBDIqDDp3iXftuMXDN1aC0ndxZCYqqocHGk0BX81/xy3KKktUL1OKq/Sp9cnGHIeJ3zxcUxF3VX8KX8zcUJA94JuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrDYB3l",
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
  "id": -576460752303422165,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBDIqDDp3iXftuMXDN1aC0ndxZCYqqocHGk0BX81/xy3KKktUL1OKq/Sp9cnGHIeJ3zxcUxF3VX8KX8zcUJA94JuEBxbE4262bVdJ1E5tdT0axkYM9N9d9EgEIpkdwbF9+37qSg4u74iiNNFMnHOsMSFhYkV1kSD8JmB8MDLhSG3awGuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqQ5vvg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422165,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+NILAfiEuEBDIqDDp3iXftuMXDN1aC0ndxZCYqqocHGk0BX81/xy3KKktUL1OKq/Sp9cnGHIeJ3zxcUxF3VX8KX8zcUJA94JuEBxbE4262bVdJ1E5tdT0axkYM9N9d9EgEIpkdwbF9+37qSg4u74iiNNFMnHOsMSFhYkV1kSD8JmB8MDLhSG3awGuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqQ5vvg"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+NILAfiEuEBDIqDDp3iXftuMXDN1aC0ndxZCYqqocHGk0BX81/xy3KKktUL1OKq/Sp9cnGHIeJ3zxcUxF3VX8KX8zcUJA94JuEBxbE4262bVdJ1E5tdT0axkYM9N9d9EgEIpkdwbF9+37qSg4u74iiNNFMnHOsMSFhYkV1kSD8JmB8MDLhSG3awGuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqQ5vvg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422164,
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422164,
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
  "id": -576460752303422163,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422163,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBDIqDDp3iXftuMXDN1aC0ndxZCYqqocHGk0BX81/xy3KKktUL1OKq/Sp9cnGHIeJ3zxcUxF3VX8KX8zcUJA94JuEBxbE4262bVdJ1E5tdT0axkYM9N9d9EgEIpkdwbF9+37qSg4u74iiNNFMnHOsMSFhYkV1kSD8JmB8MDLhSG3awGuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqQ5vvg",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422162,
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422162,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnRvr9ANzexKcP86SMt+ZoUwut36yH+ZLokfef15hpyEA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RuEYzFc=",
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
  "id": -576460752303422161,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED0YT8MiNaMBmEvAzYIoSYRxhtxwjdVjYqgU4+Gw9JtzZLpcUgu+TBvgWVazwCLgBqiy7SdoPU+X6nZLWt2PukEuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbtfSYL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422161,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuED0YT8MiNaMBmEvAzYIoSYRxhtxwjdVjYqgU4+Gw9JtzZLpcUgu+TBvgWVazwCLgBqiy7SdoPU+X6nZLWt2PukEuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbtfSYL",
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
  "id": -576460752303422160,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuED0YT8MiNaMBmEvAzYIoSYRxhtxwjdVjYqgU4+Gw9JtzZLpcUgu+TBvgWVazwCLgBqiy7SdoPU+X6nZLWt2PukEuED4GrYd1fXXvzeNQiggxbLVvBnquV+SrLSsjz+SJsOYQTgY7cvXAEuQ2yKMacP4lXBSagt7blM78cA970w3H5YGuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEakMDGh"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422160,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+NILAfiEuED0YT8MiNaMBmEvAzYIoSYRxhtxwjdVjYqgU4+Gw9JtzZLpcUgu+TBvgWVazwCLgBqiy7SdoPU+X6nZLWt2PukEuED4GrYd1fXXvzeNQiggxbLVvBnquV+SrLSsjz+SJsOYQTgY7cvXAEuQ2yKMacP4lXBSagt7blM78cA970w3H5YGuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEakMDGh"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+NILAfiEuED0YT8MiNaMBmEvAzYIoSYRxhtxwjdVjYqgU4+Gw9JtzZLpcUgu+TBvgWVazwCLgBqiy7SdoPU+X6nZLWt2PukEuED4GrYd1fXXvzeNQiggxbLVvBnquV+SrLSsjz+SJsOYQTgY7cvXAEuQ2yKMacP4lXBSagt7blM78cA970w3H5YGuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEakMDGh"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422159,
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422159,
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
  "id": -576460752303422158,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422158,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuED0YT8MiNaMBmEvAzYIoSYRxhtxwjdVjYqgU4+Gw9JtzZLpcUgu+TBvgWVazwCLgBqiy7SdoPU+X6nZLWt2PukEuED4GrYd1fXXvzeNQiggxbLVvBnquV+SrLSsjz+SJsOYQTgY7cvXAEuQ2yKMacP4lXBSagt7blM78cA970w3H5YGuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEakMDGh",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422157,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422157,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuED0YT8MiNaMBmEvAzYIoSYRxhtxwjdVjYqgU4+Gw9JtzZLpcUgu+TBvgWVazwCLgBqiy7SdoPU+X6nZLWt2PukEuED4GrYd1fXXvzeNQiggxbLVvBnquV+SrLSsjz+SJsOYQTgY7cvXAEuQ2yKMacP4lXBSagt7blM78cA970w3H5YGuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEakMDGh",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422156,
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422156,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnRvr9ANzexKcP86SMt+ZoUwut36yH+ZLokfef15hpyEBKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCygZIakA=",
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
  "id": -576460752303422155,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBoAE7UjVlUqajYB857W8Eb6i738ePjk4w7mFNcTV/mg1SzveMzNguUwTkwVM61ArAnJ8ofnSzc7B+pZUxcoc0KuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoE5F+e"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422155,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBoAE7UjVlUqajYB857W8Eb6i738ePjk4w7mFNcTV/mg1SzveMzNguUwTkwVM61ArAnJ8ofnSzc7B+pZUxcoc0KuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoE5F+e",
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
  "id": -576460752303422154,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBoAE7UjVlUqajYB857W8Eb6i738ePjk4w7mFNcTV/mg1SzveMzNguUwTkwVM61ArAnJ8ofnSzc7B+pZUxcoc0KuECm7Zphkd0LQl8Ad8vAuLt5CuNrBAS5ng+kX/olIAYuxsuUmA/g6yWe7j8Yqu15ilsb88yXW9cYrEg33a+M64wBuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp0hucD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422154,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+NILAfiEuEBoAE7UjVlUqajYB857W8Eb6i738ePjk4w7mFNcTV/mg1SzveMzNguUwTkwVM61ArAnJ8ofnSzc7B+pZUxcoc0KuECm7Zphkd0LQl8Ad8vAuLt5CuNrBAS5ng+kX/olIAYuxsuUmA/g6yWe7j8Yqu15ilsb88yXW9cYrEg33a+M64wBuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp0hucD"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+NILAfiEuEBoAE7UjVlUqajYB857W8Eb6i738ePjk4w7mFNcTV/mg1SzveMzNguUwTkwVM61ArAnJ8ofnSzc7B+pZUxcoc0KuECm7Zphkd0LQl8Ad8vAuLt5CuNrBAS5ng+kX/olIAYuxsuUmA/g6yWe7j8Yqu15ilsb88yXW9cYrEg33a+M64wBuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp0hucD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422153,
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422153,
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
  "id": -576460752303422152,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422152,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBoAE7UjVlUqajYB857W8Eb6i738ePjk4w7mFNcTV/mg1SzveMzNguUwTkwVM61ArAnJ8ofnSzc7B+pZUxcoc0KuECm7Zphkd0LQl8Ad8vAuLt5CuNrBAS5ng+kX/olIAYuxsuUmA/g6yWe7j8Yqu15ilsb88yXW9cYrEg33a+M64wBuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp0hucD",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422151,
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422151,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnRvr9ANzexKcP86SMt+ZoUwut36yH+ZLokfef15hpyEBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RvkPf+4=",
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
  "id": -576460752303422150,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAHhCh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422150,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAHhCh",
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
  "id": -576460752303422149,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAduYbfW5prDov6/wWeHLC7WW5iXSjcKdhM2WLtuVqCYRNaO4mmG+3jchrHrBDroOqw4IvTRljt/R9xWe1uTOILuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb5ewym"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422149,
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+NILAfiEuEAduYbfW5prDov6/wWeHLC7WW5iXSjcKdhM2WLtuVqCYRNaO4mmG+3jchrHrBDroOqw4IvTRljt/R9xWe1uTOILuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb5ewym"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "state": "tx_+NILAfiEuEAduYbfW5prDov6/wWeHLC7WW5iXSjcKdhM2WLtuVqCYRNaO4mmG+3jchrHrBDroOqw4IvTRljt/R9xWe1uTOILuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb5ewym"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422148,
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422148,
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
  "id": -576460752303422147,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422147,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAduYbfW5prDov6/wWeHLC7WW5iXSjcKdhM2WLtuVqCYRNaO4mmG+3jchrHrBDroOqw4IvTRljt/R9xWe1uTOILuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb5ewym",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAduYbfW5prDov6/wWeHLC7WW5iXSjcKdhM2WLtuVqCYRNaO4mmG+3jchrHrBDroOqw4IvTRljt/R9xWe1uTOILuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb5ewym",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAduYbfW5prDov6/wWeHLC7WW5iXSjcKdhM2WLtuVqCYRNaO4mmG+3jchrHrBDroOqw4IvTRljt/R9xWe1uTOILuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb5ewym",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+QKACwHAuQJ6+QJ3NwGhBnRvr9ANzexKcP86SMt+ZoUwut36yH+ZLokfef15hpyEoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEAduYbfW5prDov6/wWeHLC7WW5iXSjcKdhM2WLtuVqCYRNaO4mmG+3jchrHrBDroOqw4IvTRljt/R9xWe1uTOILuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGSzAkUAAgxLWh1uo5H4=",
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
  "method": "channels.slash_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422146,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
  "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
  "id": -576460752303422146,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBnRvr9ANzexKcP86SMt+ZoUwut36yH+ZLokfef15hpyEoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAduYbfW5prDov6/wWeHLC7WW5iXSjcKdhM2WLtuVqCYRNaO4mmG+3jchrHrBDroOqw4IvTRljt/R9xWe1uTOILuEBoxerFrAW8I55uDmhkQDOED5OuP0UpxcNOyqCpgB5/8KsrJnaWDEND9Uxt3nQ0sq8w7pNVqCNSY4LDkOGAXvsJuEj4RjkCoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGSNwYbAAgbKTHo72",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLBCwH4QrhA/z4fHXpAmPP9HLd+uzOvhc93GsizfYej9CdUyfRAK0aX8OKoBI41Y8+uZzYqnzPVmxsft3/Vwltn9oDqR4m8CLkCePkCdTcBoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAHbmG31uaaw6L+v8Fnhywu1luYl0o3CnYTNli7blagmETWjuJphvt43Iax6wQ66DqsOCL00ZY7f0fcVntbkziC7hAaMXqxawFvCOebg5oZEAzhA+Trj9FKcXDTsqgqYAef/CrKyZ2lgxDQ/VMbd50NLKvMO6TVagjUmOCw5DhgF77CbhI+EY5AqEGdG+v0A3N7Epw/zpIy35mhTC63frIf5kuiR95/XmGnIQFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIGyd+YBhw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhA/z4fHXpAmPP9HLd+uzOvhc93GsizfYej9CdUyfRAK0aX8OKoBI41Y8+uZzYqnzPVmxsft3/Vwltn9oDqR4m8CLkCePkCdTcBoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAHbmG31uaaw6L+v8Fnhywu1luYl0o3CnYTNli7blagmETWjuJphvt43Iax6wQ66DqsOCL00ZY7f0fcVntbkziC7hAaMXqxawFvCOebg5oZEAzhA+Trj9FKcXDTsqgqYAef/CrKyZ2lgxDQ/VMbd50NLKvMO6TVagjUmOCw5DhgF77CbhI+EY5AqEGdG+v0A3N7Epw/zpIy35mhTC63frIf5kuiR95/XmGnIQFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIGyd+YBhw==",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhA/z4fHXpAmPP9HLd+uzOvhc93GsizfYej9CdUyfRAK0aX8OKoBI41Y8+uZzYqnzPVmxsft3/Vwltn9oDqR4m8CLkCePkCdTcBoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAHbmG31uaaw6L+v8Fnhywu1luYl0o3CnYTNli7blagmETWjuJphvt43Iax6wQ66DqsOCL00ZY7f0fcVntbkziC7hAaMXqxawFvCOebg5oZEAzhA+Trj9FKcXDTsqgqYAef/CrKyZ2lgxDQ/VMbd50NLKvMO6TVagjUmOCw5DhgF77CbhI+EY5AqEGdG+v0A3N7Epw/zpIy35mhTC63frIf5kuiR95/XmGnIQFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIGyd+YBhw==",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBnRvr9ANzexKcP86SMt+ZoUwut36yH+ZLokfef15hpyEoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KABAm+xnuQ==",
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
    "signed_tx": "tx_+KcLAfhCuEDr6jX9Lra5aXfPu2u9CzpnL6mj/DfimaS1JZfzE/iTaDnqR/jCywx9Xrg0BM4zcxyfFN8kMNVq5wwOd9p8jIEFuF/4XTgBoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAQHfdiCU="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDr6jX9Lra5aXfPu2u9CzpnL6mj/DfimaS1JZfzE/iTaDnqR/jCywx9Xrg0BM4zcxyfFN8kMNVq5wwOd9p8jIEFuF/4XTgBoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAQHfdiCU=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDr6jX9Lra5aXfPu2u9CzpnL6mj/DfimaS1JZfzE/iTaDnqR/jCywx9Xrg0BM4zcxyfFN8kMNVq5wwOd9p8jIEFuF/4XTgBoQZ0b6/QDc3sSnD/OkjLfmaFMLrd+sh/mS6JH3n9eYachKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAQHfdiCU=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
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
    "channel_id": "ch_tHD65q4285Ni8tqxX5dQk7XFWzUTG73p9MLLt4UPCqhaZairQ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
