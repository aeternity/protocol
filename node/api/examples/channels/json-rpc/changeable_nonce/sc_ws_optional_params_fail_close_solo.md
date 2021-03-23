
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
      "fsm_id": "ba_BdnvpRtRuhwI+hT6/rwzargf+aLgb0mX8WlCBHsgzn2eDO1G"
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
      "fsm_id": "ba_1u23obcKTcYPj0BjfGTk4yoHasdjPu/i8SEng0kZdMHQEWX4"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBqVS6s4I=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422205,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEA0FluGkyXwbRLC2C9eRCMbZnc49Ljz2xhWZLMkmt1R9pvx/xzDRzl1WrFMno9VCTgPIYO60N5uRUt2Ht9Z3lYHuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgamJ5SXP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422205,
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_1u23obcKTcYPj0BjfGTk4yoHasdjPu/i8SEng0kZdMHQEWX4"
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEA0FluGkyXwbRLC2C9eRCMbZnc49Ljz2xhWZLMkmt1R9pvx/xzDRzl1WrFMno9VCTgPIYO60N5uRUt2Ht9Z3lYHuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgamJ5SXP",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422204,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhANBZbhpMl8G0SwtgvXkQjG2Z3OPS489sYVmSzJJrdUfab8f8cw0c5dVqxTJ6PVQk4DyGDutDebkVLdh7fWd5WB7hAuPVQ8gdNvZv0pIdCvnq1LYa/KVa4+VK6X7J6A4gwjGWZzcOUvZW7EijmHtEtPLmj4r9D0aWY6lfL6U9Rg9qXALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGpXrsydw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
  "id": -576460752303422204,
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhANBZbhpMl8G0SwtgvXkQjG2Z3OPS489sYVmSzJJrdUfab8f8cw0c5dVqxTJ6PVQk4DyGDutDebkVLdh7fWd5WB7hAuPVQ8gdNvZv0pIdCvnq1LYa/KVa4+VK6X7J6A4gwjGWZzcOUvZW7EijmHtEtPLmj4r9D0aWY6lfL6U9Rg9qXALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGpXrsydw==",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_BdnvpRtRuhwI+hT6/rwzargf+aLgb0mX8WlCBHsgzn2eDO1G"
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhANBZbhpMl8G0SwtgvXkQjG2Z3OPS489sYVmSzJJrdUfab8f8cw0c5dVqxTJ6PVQk4DyGDutDebkVLdh7fWd5WB7hAuPVQ8gdNvZv0pIdCvnq1LYa/KVa4+VK6X7J6A4gwjGWZzcOUvZW7EijmHtEtPLmj4r9D0aWY6lfL6U9Rg9qXALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGpXrsydw==",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhANBZbhpMl8G0SwtgvXkQjG2Z3OPS489sYVmSzJJrdUfab8f8cw0c5dVqxTJ6PVQk4DyGDutDebkVLdh7fWd5WB7hAuPVQ8gdNvZv0pIdCvnq1LYa/KVa4+VK6X7J6A4gwjGWZzcOUvZW7EijmHtEtPLmj4r9D0aWY6lfL6U9Rg9qXALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGpXrsydw==",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhANBZbhpMl8G0SwtgvXkQjG2Z3OPS489sYVmSzJJrdUfab8f8cw0c5dVqxTJ6PVQk4DyGDutDebkVLdh7fWd5WB7hAuPVQ8gdNvZv0pIdCvnq1LYa/KVa4+VK6X7J6A4gwjGWZzcOUvZW7EijmHtEtPLmj4r9D0aWY6lfL6U9Rg9qXALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGpXrsydw==",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "message": {
        "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "message": {
        "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
  "id": -576460752303422203,
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
  "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
  "id": -576460752303422203,
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "state": "tx_+QEOCwH4hLhANBZbhpMl8G0SwtgvXkQjG2Z3OPS489sYVmSzJJrdUfab8f8cw0c5dVqxTJ6PVQk4DyGDutDebkVLdh7fWd5WB7hAuPVQ8gdNvZv0pIdCvnq1LYa/KVa4+VK6X7J6A4gwjGWZzcOUvZW7EijmHtEtPLmj4r9D0aWY6lfL6U9Rg9qXALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGpXrsydw=="
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "state": "tx_+QEOCwH4hLhANBZbhpMl8G0SwtgvXkQjG2Z3OPS489sYVmSzJJrdUfab8f8cw0c5dVqxTJ6PVQk4DyGDutDebkVLdh7fWd5WB7hAuPVQ8gdNvZv0pIdCvnq1LYa/KVa4+VK6X7J6A4gwjGWZzcOUvZW7EijmHtEtPLmj4r9D0aWY6lfL6U9Rg9qXALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGpXrsydw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "signed_tx": "tx_+QGrCwHAuQGl+QGiNgGhBmbFEXnzd0ek1BgfPY56DmmqtoOLuWrpBXfPA1Smd7A+oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFUzkx9gAgxLWh0J+VoQ=",
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
  "method": "channels.close_solo_sign",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBmbFEXnzd0ek1BgfPY56DmmqtoOLuWrpBXfPA1Smd7A+oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBqoZ0zkc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422202,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuECn3xQgn4zFGzDJ8KQNyB1sbsaXyyY1JsQR2eHJkmmZ2JU2NTW1mo/P6oOlNcnEq26OkFKq2k0QUVzdn40sDvIJuGD4XjUBoQZmxRF583dHpNQYHz2Oeg5pqraDi7lq6QV3zwNUpnewPqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaqQJO0A"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
  "id": -576460752303422202,
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "signed_tx": "tx_+KgLAfhCuECn3xQgn4zFGzDJ8KQNyB1sbsaXyyY1JsQR2eHJkmmZ2JU2NTW1mo/P6oOlNcnEq26OkFKq2k0QUVzdn40sDvIJuGD4XjUBoQZmxRF583dHpNQYHz2Oeg5pqraDi7lq6QV3zwNUpnewPqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaqQJO0A",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422201,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEB0NDGmuFWny/bHXOBJPI48ZcW5vnMc6wMDUZiwosL6FOqg3+c0+NYGApMYJjTo+99mEOeDUBgbKIH2Z5oX8+0DuECn3xQgn4zFGzDJ8KQNyB1sbsaXyyY1JsQR2eHJkmmZ2JU2NTW1mo/P6oOlNcnEq26OkFKq2k0QUVzdn40sDvIJuGD4XjUBoQZmxRF583dHpNQYHz2Oeg5pqraDi7lq6QV3zwNUpnewPqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgarIlfLW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
  "id": -576460752303422201,
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEB0NDGmuFWny/bHXOBJPI48ZcW5vnMc6wMDUZiwosL6FOqg3+c0+NYGApMYJjTo+99mEOeDUBgbKIH2Z5oX8+0DuECn3xQgn4zFGzDJ8KQNyB1sbsaXyyY1JsQR2eHJkmmZ2JU2NTW1mo/P6oOlNcnEq26OkFKq2k0QUVzdn40sDvIJuGD4XjUBoQZmxRF583dHpNQYHz2Oeg5pqraDi7lq6QV3zwNUpnewPqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgarIlfLW",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEB0NDGmuFWny/bHXOBJPI48ZcW5vnMc6wMDUZiwosL6FOqg3+c0+NYGApMYJjTo+99mEOeDUBgbKIH2Z5oX8+0DuECn3xQgn4zFGzDJ8KQNyB1sbsaXyyY1JsQR2eHJkmmZ2JU2NTW1mo/P6oOlNcnEq26OkFKq2k0QUVzdn40sDvIJuGD4XjUBoQZmxRF583dHpNQYHz2Oeg5pqraDi7lq6QV3zwNUpnewPqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgarIlfLW",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEB0NDGmuFWny/bHXOBJPI48ZcW5vnMc6wMDUZiwosL6FOqg3+c0+NYGApMYJjTo+99mEOeDUBgbKIH2Z5oX8+0DuECn3xQgn4zFGzDJ8KQNyB1sbsaXyyY1JsQR2eHJkmmZ2JU2NTW1mo/P6oOlNcnEq26OkFKq2k0QUVzdn40sDvIJuGD4XjUBoQZmxRF583dHpNQYHz2Oeg5pqraDi7lq6QV3zwNUpnewPqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgarIlfLW",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEB0NDGmuFWny/bHXOBJPI48ZcW5vnMc6wMDUZiwosL6FOqg3+c0+NYGApMYJjTo+99mEOeDUBgbKIH2Z5oX8+0DuECn3xQgn4zFGzDJ8KQNyB1sbsaXyyY1JsQR2eHJkmmZ2JU2NTW1mo/P6oOlNcnEq26OkFKq2k0QUVzdn40sDvIJuGD4XjUBoQZmxRF583dHpNQYHz2Oeg5pqraDi7lq6QV3zwNUpnewPqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgarIlfLW",
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
      "fsm_id": "ba_JXXPQqTdgD7DmibrRKiiU9KaMMTUxDbfdQP4IJEtaK4azUXg"
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
      "fsm_id": "ba_DJzuwVmz3Fj8mganl9ot/HE2NjLjo44+tmrWpvbh3WW7zbw1"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBq3ECmoE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422200,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECo8xS0pokusb7r0M8EsJKSfUYX56P36MjuWmHJ7sfqjSmpLOCKqQwlIPK8R26YX+cw+edzt08XK02IXDp/xWoDuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgavfbVEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422200,
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_DJzuwVmz3Fj8mganl9ot/HE2NjLjo44+tmrWpvbh3WW7zbw1"
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECo8xS0pokusb7r0M8EsJKSfUYX56P36MjuWmHJ7sfqjSmpLOCKqQwlIPK8R26YX+cw+edzt08XK02IXDp/xWoDuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgavfbVEF",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422199,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAqPMUtKaJLrG+69DPBLCSkn1GF+ej9+jI7lphye7H6o0pqSzgiqkMJSDyvEdumF/nMPnnc7dPFytNiFw6f8VqA7hAwHUmAZDaXH6oyvD4On2TCMO2Hc67WeCZ2td3mJwLRcuK+7ADAtJeHRrhjmn5PwTEC2NXv1/PJETtnukkAvkyBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGrePxQGw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
  "id": -576460752303422199,
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAqPMUtKaJLrG+69DPBLCSkn1GF+ej9+jI7lphye7H6o0pqSzgiqkMJSDyvEdumF/nMPnnc7dPFytNiFw6f8VqA7hAwHUmAZDaXH6oyvD4On2TCMO2Hc67WeCZ2td3mJwLRcuK+7ADAtJeHRrhjmn5PwTEC2NXv1/PJETtnukkAvkyBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGrePxQGw==",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_JXXPQqTdgD7DmibrRKiiU9KaMMTUxDbfdQP4IJEtaK4azUXg"
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAqPMUtKaJLrG+69DPBLCSkn1GF+ej9+jI7lphye7H6o0pqSzgiqkMJSDyvEdumF/nMPnnc7dPFytNiFw6f8VqA7hAwHUmAZDaXH6oyvD4On2TCMO2Hc67WeCZ2td3mJwLRcuK+7ADAtJeHRrhjmn5PwTEC2NXv1/PJETtnukkAvkyBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGrePxQGw==",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAqPMUtKaJLrG+69DPBLCSkn1GF+ej9+jI7lphye7H6o0pqSzgiqkMJSDyvEdumF/nMPnnc7dPFytNiFw6f8VqA7hAwHUmAZDaXH6oyvD4On2TCMO2Hc67WeCZ2td3mJwLRcuK+7ADAtJeHRrhjmn5PwTEC2NXv1/PJETtnukkAvkyBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGrePxQGw==",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAqPMUtKaJLrG+69DPBLCSkn1GF+ej9+jI7lphye7H6o0pqSzgiqkMJSDyvEdumF/nMPnnc7dPFytNiFw6f8VqA7hAwHUmAZDaXH6oyvD4On2TCMO2Hc67WeCZ2td3mJwLRcuK+7ADAtJeHRrhjmn5PwTEC2NXv1/PJETtnukkAvkyBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGrePxQGw==",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
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
    "channel_id": "ch_nG7m6WNjb5FWwz5wPhsVAh9kDovcGmdSx9pudfA1rmv4rBxAp",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "message": {
        "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
      }
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "message": {
        "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
  "id": -576460752303422198,
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
  "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
  "id": -576460752303422198,
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "state": "tx_+QEOCwH4hLhAqPMUtKaJLrG+69DPBLCSkn1GF+ej9+jI7lphye7H6o0pqSzgiqkMJSDyvEdumF/nMPnnc7dPFytNiFw6f8VqA7hAwHUmAZDaXH6oyvD4On2TCMO2Hc67WeCZ2td3mJwLRcuK+7ADAtJeHRrhjmn5PwTEC2NXv1/PJETtnukkAvkyBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGrePxQGw=="
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "state": "tx_+QEOCwH4hLhAqPMUtKaJLrG+69DPBLCSkn1GF+ej9+jI7lphye7H6o0pqSzgiqkMJSDyvEdumF/nMPnnc7dPFytNiFw6f8VqA7hAwHUmAZDaXH6oyvD4On2TCMO2Hc67WeCZ2td3mJwLRcuK+7ADAtJeHRrhjmn5PwTEC2NXv1/PJETtnukkAvkyBbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGrePxQGw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "signed_tx": "tx_+QGrCwHAuQGl+QGiNgGhBv0iXIrlq1k10DQfz4wI+lvWH4M2j2YrxJWnLPcXOrYHoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFUzkx9gAgxLWh9S68f0=",
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
  "method": "channels.close_solo_sign",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBv0iXIrlq1k10DQfz4wI+lvWH4M2j2YrxJWnLPcXOrYHoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBrDhJdMs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422197,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEB5pbXduI8QWgOplxJLZNq6Nn7GUT+LcBvUOIEqJ3XnY1XLgrhDwNKHRizJ/RkXE+HtxSeAHvGxaxpuLsPkuKINuGD4XjUBoQb9IlyK5atZNdA0H8+MCPpb1h+DNo9mK8SVpyz3Fzq2B6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgazCvdae"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
  "id": -576460752303422197,
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEB5pbXduI8QWgOplxJLZNq6Nn7GUT+LcBvUOIEqJ3XnY1XLgrhDwNKHRizJ/RkXE+HtxSeAHvGxaxpuLsPkuKINuGD4XjUBoQb9IlyK5atZNdA0H8+MCPpb1h+DNo9mK8SVpyz3Fzq2B6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgazCvdae",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422196,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEB2A/ZgdfXqnxh5au5DnbVE/dR4hQwkfiHKtQ15C2iEpK6iMRjr0B8n0Lki9y7ubbqI2P+oq7HJB1FlH4se86QNuEB5pbXduI8QWgOplxJLZNq6Nn7GUT+LcBvUOIEqJ3XnY1XLgrhDwNKHRizJ/RkXE+HtxSeAHvGxaxpuLsPkuKINuGD4XjUBoQb9IlyK5atZNdA0H8+MCPpb1h+DNo9mK8SVpyz3Fzq2B6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgawg3pv/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
  "id": -576460752303422196,
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEB2A/ZgdfXqnxh5au5DnbVE/dR4hQwkfiHKtQ15C2iEpK6iMRjr0B8n0Lki9y7ubbqI2P+oq7HJB1FlH4se86QNuEB5pbXduI8QWgOplxJLZNq6Nn7GUT+LcBvUOIEqJ3XnY1XLgrhDwNKHRizJ/RkXE+HtxSeAHvGxaxpuLsPkuKINuGD4XjUBoQb9IlyK5atZNdA0H8+MCPpb1h+DNo9mK8SVpyz3Fzq2B6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgawg3pv/",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEB2A/ZgdfXqnxh5au5DnbVE/dR4hQwkfiHKtQ15C2iEpK6iMRjr0B8n0Lki9y7ubbqI2P+oq7HJB1FlH4se86QNuEB5pbXduI8QWgOplxJLZNq6Nn7GUT+LcBvUOIEqJ3XnY1XLgrhDwNKHRizJ/RkXE+HtxSeAHvGxaxpuLsPkuKINuGD4XjUBoQb9IlyK5atZNdA0H8+MCPpb1h+DNo9mK8SVpyz3Fzq2B6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgawg3pv/",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEB2A/ZgdfXqnxh5au5DnbVE/dR4hQwkfiHKtQ15C2iEpK6iMRjr0B8n0Lki9y7ubbqI2P+oq7HJB1FlH4se86QNuEB5pbXduI8QWgOplxJLZNq6Nn7GUT+LcBvUOIEqJ3XnY1XLgrhDwNKHRizJ/RkXE+HtxSeAHvGxaxpuLsPkuKINuGD4XjUBoQb9IlyK5atZNdA0H8+MCPpb1h+DNo9mK8SVpyz3Fzq2B6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgawg3pv/",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEB2A/ZgdfXqnxh5au5DnbVE/dR4hQwkfiHKtQ15C2iEpK6iMRjr0B8n0Lki9y7ubbqI2P+oq7HJB1FlH4se86QNuEB5pbXduI8QWgOplxJLZNq6Nn7GUT+LcBvUOIEqJ3XnY1XLgrhDwNKHRizJ/RkXE+HtxSeAHvGxaxpuLsPkuKINuGD4XjUBoQb9IlyK5atZNdA0H8+MCPpb1h+DNo9mK8SVpyz3Fzq2B6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgawg3pv/",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
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
    "channel_id": "ch_2vUyVcyJzoKh4j8Ni7fcMLuCfYtQpsAgMpkYd3FngVfZ1PBL48",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
