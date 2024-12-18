
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
      "fsm_id": "ba_D20k4LQmCnLEada2Aa9Qwd0zJXcKFW+mhWVp7lduxgNA5Q7H"
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
      "fsm_id": "ba_PEcKhx2oCpDzkeAH+uQlqtOn53hWUgqpsjBo1oIFRxTk++X3"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY53pduKw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422674,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECDcn0QMMeK4vMPgOrQ6scSn7ro1el2neDuKBlzs+GeI1u5pECzDyLQPZGTwzZTFTE3BY8qVyH+G6g91BU4JY4PuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGOZiwgOw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422674,
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_PEcKhx2oCpDzkeAH+uQlqtOn53hWUgqpsjBo1oIFRxTk++X3"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECDcn0QMMeK4vMPgOrQ6scSn7ro1el2neDuKBlzs+GeI1u5pECzDyLQPZGTwzZTFTE3BY8qVyH+G6g91BU4JY4PuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGOZiwgOw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422673,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhATMy8niaLsZpGqILNuCiXAS+gWxooBufVc0siSbJt1atbzJ+c7G2gn5OPOJz2pNpDrYJFE8VgArlbE5kZ2xRUCLhAg3J9EDDHiuLzD4Dq0OrHEp+66NXpdp3g7igZc7PhniNbuaRAsw8i0D2Rk8M2UxUxNwWPKlch/huoPdQVOCWOD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjngdqAO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
  "id": -576460752303422673,
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhATMy8niaLsZpGqILNuCiXAS+gWxooBufVc0siSbJt1atbzJ+c7G2gn5OPOJz2pNpDrYJFE8VgArlbE5kZ2xRUCLhAg3J9EDDHiuLzD4Dq0OrHEp+66NXpdp3g7igZc7PhniNbuaRAsw8i0D2Rk8M2UxUxNwWPKlch/huoPdQVOCWOD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjngdqAO",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_D20k4LQmCnLEada2Aa9Qwd0zJXcKFW+mhWVp7lduxgNA5Q7H"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhATMy8niaLsZpGqILNuCiXAS+gWxooBufVc0siSbJt1atbzJ+c7G2gn5OPOJz2pNpDrYJFE8VgArlbE5kZ2xRUCLhAg3J9EDDHiuLzD4Dq0OrHEp+66NXpdp3g7igZc7PhniNbuaRAsw8i0D2Rk8M2UxUxNwWPKlch/huoPdQVOCWOD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjngdqAO",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhATMy8niaLsZpGqILNuCiXAS+gWxooBufVc0siSbJt1atbzJ+c7G2gn5OPOJz2pNpDrYJFE8VgArlbE5kZ2xRUCLhAg3J9EDDHiuLzD4Dq0OrHEp+66NXpdp3g7igZc7PhniNbuaRAsw8i0D2Rk8M2UxUxNwWPKlch/huoPdQVOCWOD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjngdqAO",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhATMy8niaLsZpGqILNuCiXAS+gWxooBufVc0siSbJt1atbzJ+c7G2gn5OPOJz2pNpDrYJFE8VgArlbE5kZ2xRUCLhAg3J9EDDHiuLzD4Dq0OrHEp+66NXpdp3g7igZc7PhniNbuaRAsw8i0D2Rk8M2UxUxNwWPKlch/huoPdQVOCWOD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjngdqAO",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
  "id": -576460752303422672,
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
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
  "id": -576460752303422672,
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "open"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "state": "tx_+QENCwH4hLhATMy8niaLsZpGqILNuCiXAS+gWxooBufVc0siSbJt1atbzJ+c7G2gn5OPOJz2pNpDrYJFE8VgArlbE5kZ2xRUCLhAg3J9EDDHiuLzD4Dq0OrHEp+66NXpdp3g7igZc7PhniNbuaRAsw8i0D2Rk8M2UxUxNwWPKlch/huoPdQVOCWOD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjngdqAO"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "state": "tx_+QENCwH4hLhATMy8niaLsZpGqILNuCiXAS+gWxooBufVc0siSbJt1atbzJ+c7G2gn5OPOJz2pNpDrYJFE8VgArlbE5kZ2xRUCLhAg3J9EDDHiuLzD4Dq0OrHEp+66NXpdp3g7igZc7PhniNbuaRAsw8i0D2Rk8M2UxUxNwWPKlch/huoPdQVOCWOD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjngdqAO"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
  "method": "channels.deposit",
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBnRVr01eAfnf3w8qFlOIokRne2D2g6c2as2AC4fVkFotoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhnBIhhsPP6APDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgI6LNX7qA==",
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
  "id": -576460752303422671,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBKnoSvGprGo7vfQbmUFaod5+fUCyJuPtHpg1lGO7c7MgTZecmBlhKOFAzn27e2S9/W1SUu7c4VQ3yTprAUb5EGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4COuD6+Wc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
  "id": -576460752303422671,
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBKnoSvGprGo7vfQbmUFaod5+fUCyJuPtHpg1lGO7c7MgTZecmBlhKOFAzn27e2S9/W1SUu7c4VQ3yTprAUb5EGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4COuD6+Wc=",
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

#### responder ---> node
```javascript
{
  "id": -576460752303422670,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBKnoSvGprGo7vfQbmUFaod5+fUCyJuPtHpg1lGO7c7MgTZecmBlhKOFAzn27e2S9/W1SUu7c4VQ3yTprAUb5EGuEBydKQ9DEulrQ133d6UffCRza+AuRODzk5dlxxXEcVaGku8vLBIDzs/yl4w108VSuTxvXYoj7TancLeBcky8AEPuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4COgC5gfY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
  "id": -576460752303422670,
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBKnoSvGprGo7vfQbmUFaod5+fUCyJuPtHpg1lGO7c7MgTZecmBlhKOFAzn27e2S9/W1SUu7c4VQ3yTprAUb5EGuEBydKQ9DEulrQ133d6UffCRza+AuRODzk5dlxxXEcVaGku8vLBIDzs/yl4w108VSuTxvXYoj7TancLeBcky8AEPuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4COgC5gfY=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBKnoSvGprGo7vfQbmUFaod5+fUCyJuPtHpg1lGO7c7MgTZecmBlhKOFAzn27e2S9/W1SUu7c4VQ3yTprAUb5EGuEBydKQ9DEulrQ133d6UffCRza+AuRODzk5dlxxXEcVaGku8vLBIDzs/yl4w108VSuTxvXYoj7TancLeBcky8AEPuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4COgC5gfY=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBKnoSvGprGo7vfQbmUFaod5+fUCyJuPtHpg1lGO7c7MgTZecmBlhKOFAzn27e2S9/W1SUu7c4VQ3yTprAUb5EGuEBydKQ9DEulrQ133d6UffCRza+AuRODzk5dlxxXEcVaGku8vLBIDzs/yl4w108VSuTxvXYoj7TancLeBcky8AEPuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4COgC5gfY=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBKnoSvGprGo7vfQbmUFaod5+fUCyJuPtHpg1lGO7c7MgTZecmBlhKOFAzn27e2S9/W1SUu7c4VQ3yTprAUb5EGuEBydKQ9DEulrQ133d6UffCRza+AuRODzk5dlxxXEcVaGku8vLBIDzs/yl4w108VSuTxvXYoj7TancLeBcky8AEPuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4COgC5gfY=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "state": "tx_+P4LAfiEuEBKnoSvGprGo7vfQbmUFaod5+fUCyJuPtHpg1lGO7c7MgTZecmBlhKOFAzn27e2S9/W1SUu7c4VQ3yTprAUb5EGuEBydKQ9DEulrQ133d6UffCRza+AuRODzk5dlxxXEcVaGku8vLBIDzs/yl4w108VSuTxvXYoj7TancLeBcky8AEPuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4COgC5gfY="
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "state": "tx_+P4LAfiEuEBKnoSvGprGo7vfQbmUFaod5+fUCyJuPtHpg1lGO7c7MgTZecmBlhKOFAzn27e2S9/W1SUu7c4VQ3yTprAUb5EGuEBydKQ9DEulrQ133d6UffCRza+AuRODzk5dlxxXEcVaGku8vLBIDzs/yl4w108VSuTxvXYoj7TancLeBcky8AEPuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIZwSIYbDz+gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4COgC5gfY="
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
  "method": "channels.deposit",
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBnRVr01eAfnf3w8qFlOIokRne2D2g6c2as2AC4fVkFotoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhnBIhhsPP6BY8rhhwx3FNZzZtoqk4aiWG2eYbpEkfYl8gYb5T3SICgMXVswxWA==",
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
  "id": -576460752303422669,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDM2MXT+lAkAg+KNut2M9Cb5fv3c+FKHX3tTdsESXh/1OMWQw4ZjNjaLyj7392oa+aVHGPLK1SYNuTRAcHjXoMGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDFyoRSUg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
  "id": -576460752303422669,
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDM2MXT+lAkAg+KNut2M9Cb5fv3c+FKHX3tTdsESXh/1OMWQw4ZjNjaLyj7392oa+aVHGPLK1SYNuTRAcHjXoMGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDFyoRSUg=",
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

#### initiator ---> node
```javascript
{
  "id": -576460752303422668,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBGi3vql2spP6t8X0/kPeX4xFRTLrZkwDU3nTdeq/hnM22DOALmqEkATCXPSGQ2PxP5TyuzoTMMfS7idyv4OJgLuEDM2MXT+lAkAg+KNut2M9Cb5fv3c+FKHX3tTdsESXh/1OMWQw4ZjNjaLyj7392oa+aVHGPLK1SYNuTRAcHjXoMGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDFzxoEj4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
  "id": -576460752303422668,
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBGi3vql2spP6t8X0/kPeX4xFRTLrZkwDU3nTdeq/hnM22DOALmqEkATCXPSGQ2PxP5TyuzoTMMfS7idyv4OJgLuEDM2MXT+lAkAg+KNut2M9Cb5fv3c+FKHX3tTdsESXh/1OMWQw4ZjNjaLyj7392oa+aVHGPLK1SYNuTRAcHjXoMGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDFzxoEj4=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBGi3vql2spP6t8X0/kPeX4xFRTLrZkwDU3nTdeq/hnM22DOALmqEkATCXPSGQ2PxP5TyuzoTMMfS7idyv4OJgLuEDM2MXT+lAkAg+KNut2M9Cb5fv3c+FKHX3tTdsESXh/1OMWQw4ZjNjaLyj7392oa+aVHGPLK1SYNuTRAcHjXoMGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDFzxoEj4=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "message": {
        "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBGi3vql2spP6t8X0/kPeX4xFRTLrZkwDU3nTdeq/hnM22DOALmqEkATCXPSGQ2PxP5TyuzoTMMfS7idyv4OJgLuEDM2MXT+lAkAg+KNut2M9Cb5fv3c+FKHX3tTdsESXh/1OMWQw4ZjNjaLyj7392oa+aVHGPLK1SYNuTRAcHjXoMGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDFzxoEj4=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBGi3vql2spP6t8X0/kPeX4xFRTLrZkwDU3nTdeq/hnM22DOALmqEkATCXPSGQ2PxP5TyuzoTMMfS7idyv4OJgLuEDM2MXT+lAkAg+KNut2M9Cb5fv3c+FKHX3tTdsESXh/1OMWQw4ZjNjaLyj7392oa+aVHGPLK1SYNuTRAcHjXoMGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDFzxoEj4=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "state": "tx_+P4LAfiEuEBGi3vql2spP6t8X0/kPeX4xFRTLrZkwDU3nTdeq/hnM22DOALmqEkATCXPSGQ2PxP5TyuzoTMMfS7idyv4OJgLuEDM2MXT+lAkAg+KNut2M9Cb5fv3c+FKHX3tTdsESXh/1OMWQw4ZjNjaLyj7392oa+aVHGPLK1SYNuTRAcHjXoMGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDFzxoEj4="
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "state": "tx_+P4LAfiEuEBGi3vql2spP6t8X0/kPeX4xFRTLrZkwDU3nTdeq/hnM22DOALmqEkATCXPSGQ2PxP5TyuzoTMMfS7idyv4OJgLuEDM2MXT+lAkAg+KNut2M9Cb5fv3c+FKHX3tTdsESXh/1OMWQw4ZjNjaLyj7392oa+aVHGPLK1SYNuTRAcHjXoMGuHT4cjMBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIZwSIYbDz+gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDFzxoEj4="
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBnRVr01eAfnf3w8qFlOIokRne2D2g6c2as2AC4fVkFotoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rnizAGGHLHOiuwDAIYPXtZ/KAA7SLp0fw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422667,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBOHU71HQnsGGGAi0CACTN3X1AurDdAWsAWXZJsXIVIerlCjiyvd6tYfwd/3hrdok7T83md9mbeCvHpfLEl+0YJuF/4XTUBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAO3wvWY0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
  "id": -576460752303422667,
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBOHU71HQnsGGGAi0CACTN3X1AurDdAWsAWXZJsXIVIerlCjiyvd6tYfwd/3hrdok7T83md9mbeCvHpfLEl+0YJuF/4XTUBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAO3wvWY0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422666,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBOHU71HQnsGGGAi0CACTN3X1AurDdAWsAWXZJsXIVIerlCjiyvd6tYfwd/3hrdok7T83md9mbeCvHpfLEl+0YJuEBSWfcS2u+28N7DMKDr/UxUeqsVbmz/5uDeojlN59MrbiDkcH+n5PGTzK+feI85u72WQ/+2Dt3WaZRfMgIb92cLuF/4XTUBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAO2kptJg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
  "id": -576460752303422666,
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBOHU71HQnsGGGAi0CACTN3X1AurDdAWsAWXZJsXIVIerlCjiyvd6tYfwd/3hrdok7T83md9mbeCvHpfLEl+0YJuEBSWfcS2u+28N7DMKDr/UxUeqsVbmz/5uDeojlN59MrbiDkcH+n5PGTzK+feI85u72WQ/+2Dt3WaZRfMgIb92cLuF/4XTUBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAO2kptJg=",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBOHU71HQnsGGGAi0CACTN3X1AurDdAWsAWXZJsXIVIerlCjiyvd6tYfwd/3hrdok7T83md9mbeCvHpfLEl+0YJuEBSWfcS2u+28N7DMKDr/UxUeqsVbmz/5uDeojlN59MrbiDkcH+n5PGTzK+feI85u72WQ/+2Dt3WaZRfMgIb92cLuF/4XTUBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAO2kptJg=",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBOHU71HQnsGGGAi0CACTN3X1AurDdAWsAWXZJsXIVIerlCjiyvd6tYfwd/3hrdok7T83md9mbeCvHpfLEl+0YJuEBSWfcS2u+28N7DMKDr/UxUeqsVbmz/5uDeojlN59MrbiDkcH+n5PGTzK+feI85u72WQ/+2Dt3WaZRfMgIb92cLuF/4XTUBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAO2kptJg=",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBOHU71HQnsGGGAi0CACTN3X1AurDdAWsAWXZJsXIVIerlCjiyvd6tYfwd/3hrdok7T83md9mbeCvHpfLEl+0YJuEBSWfcS2u+28N7DMKDr/UxUeqsVbmz/5uDeojlN59MrbiDkcH+n5PGTzK+feI85u72WQ/+2Dt3WaZRfMgIb92cLuF/4XTUBoQZ0Va9NXgH5398PKhZTiKJEZ3tg9oOnNmrNgAuH1ZBaLaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAO2kptJg=",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
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
    "channel_id": "ch_tEccGHaXjsAtPvdA4CC4CSRPTdD9DsKDq4sU4Wc39MRAyk2dz",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
