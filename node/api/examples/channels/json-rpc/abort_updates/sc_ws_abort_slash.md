
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
      "fsm_id": "ba_UfxFSX4+1rf8E1bpkWvmaTmjcYoEUeop9UY6YNDCn/D3CPQb"
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
      "fsm_id": "ba_nHtinhw0S/jwol4j54J3erpwESsyumwEcSz/UZPYEQ55loaz"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBvBReuWg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422080,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECz9YN0jJ5K3T9Q8l3MSFIgH38JbYFoyu1qbfC6sb2I18omleiWiAgxhF86crQWIBYbRwTnWCoHd1SMP37sdGQLuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbymWnjQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422080,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_nHtinhw0S/jwol4j54J3erpwESsyumwEcSz/UZPYEQ55loaz"
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECz9YN0jJ5K3T9Q8l3MSFIgH38JbYFoyu1qbfC6sb2I18omleiWiAgxhF86crQWIBYbRwTnWCoHd1SMP37sdGQLuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbymWnjQ",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422079,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAPRJ77X0zHF+127hR1Qk3+agNEyI2o5JYvFGIIjqaj/LdiadP501w1vd0e6EbWFaY671K9pDDlFMLXm+zEPXlDLhAs/WDdIyeSt0/UPJdzEhSIB9/CW2BaMrtam3wurG9iNfKJpXologIMYRfOnK0FiAWG0cE51gqB3dUjD9+7HRkC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG80XGi1A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422079,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAPRJ77X0zHF+127hR1Qk3+agNEyI2o5JYvFGIIjqaj/LdiadP501w1vd0e6EbWFaY671K9pDDlFMLXm+zEPXlDLhAs/WDdIyeSt0/UPJdzEhSIB9/CW2BaMrtam3wurG9iNfKJpXologIMYRfOnK0FiAWG0cE51gqB3dUjD9+7HRkC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG80XGi1A==",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_UfxFSX4+1rf8E1bpkWvmaTmjcYoEUeop9UY6YNDCn/D3CPQb"
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAPRJ77X0zHF+127hR1Qk3+agNEyI2o5JYvFGIIjqaj/LdiadP501w1vd0e6EbWFaY671K9pDDlFMLXm+zEPXlDLhAs/WDdIyeSt0/UPJdzEhSIB9/CW2BaMrtam3wurG9iNfKJpXologIMYRfOnK0FiAWG0cE51gqB3dUjD9+7HRkC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG80XGi1A==",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAPRJ77X0zHF+127hR1Qk3+agNEyI2o5JYvFGIIjqaj/LdiadP501w1vd0e6EbWFaY671K9pDDlFMLXm+zEPXlDLhAs/WDdIyeSt0/UPJdzEhSIB9/CW2BaMrtam3wurG9iNfKJpXologIMYRfOnK0FiAWG0cE51gqB3dUjD9+7HRkC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG80XGi1A==",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAPRJ77X0zHF+127hR1Qk3+agNEyI2o5JYvFGIIjqaj/LdiadP501w1vd0e6EbWFaY671K9pDDlFMLXm+zEPXlDLhAs/WDdIyeSt0/UPJdzEhSIB9/CW2BaMrtam3wurG9iNfKJpXologIMYRfOnK0FiAWG0cE51gqB3dUjD9+7HRkC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG80XGi1A==",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "message": {
        "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "message": {
        "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
  "id": -576460752303422078,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422078,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+QEOCwH4hLhAPRJ77X0zHF+127hR1Qk3+agNEyI2o5JYvFGIIjqaj/LdiadP501w1vd0e6EbWFaY671K9pDDlFMLXm+zEPXlDLhAs/WDdIyeSt0/UPJdzEhSIB9/CW2BaMrtam3wurG9iNfKJpXologIMYRfOnK0FiAWG0cE51gqB3dUjD9+7HRkC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG80XGi1A=="
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+QEOCwH4hLhAPRJ77X0zHF+127hR1Qk3+agNEyI2o5JYvFGIIjqaj/LdiadP501w1vd0e6EbWFaY671K9pDDlFMLXm+zEPXlDLhAs/WDdIyeSt0/UPJdzEhSIB9/CW2BaMrtam3wurG9iNfKJpXologIMYRfOnK0FiAWG0cE51gqB3dUjD9+7HRkC7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG80XGi1A=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422077,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422077,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvNXSzg2XFr1K6EV22gnXzbuZMsxcCtAmBzkrWFauP+bAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCymlpVnc=",
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
  "id": -576460752303422076,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDXNSikeKxagbAbG542RBdPpeebyi3CIXTmivGGRnTOyopmon01fVLgRGYX4YXbG22MkfnGEugNL8kblHbIdMsOuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspDvoSI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422076,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDXNSikeKxagbAbG542RBdPpeebyi3CIXTmivGGRnTOyopmon01fVLgRGYX4YXbG22MkfnGEugNL8kblHbIdMsOuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspDvoSI",
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
  "id": -576460752303422075,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECnNHLJS5b+6fh/nKJBcI5Lrug8tJ8j5LO8E+OZtWAztR8YZcZdvqQmR0CVRml1joYtHFWQP8rXi0kTkdXHOcsJuEDXNSikeKxagbAbG542RBdPpeebyi3CIXTmivGGRnTOyopmon01fVLgRGYX4YXbG22MkfnGEugNL8kblHbIdMsOuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqh/dE7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422075,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+NILAfiEuECnNHLJS5b+6fh/nKJBcI5Lrug8tJ8j5LO8E+OZtWAztR8YZcZdvqQmR0CVRml1joYtHFWQP8rXi0kTkdXHOcsJuEDXNSikeKxagbAbG542RBdPpeebyi3CIXTmivGGRnTOyopmon01fVLgRGYX4YXbG22MkfnGEugNL8kblHbIdMsOuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqh/dE7"
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+NILAfiEuECnNHLJS5b+6fh/nKJBcI5Lrug8tJ8j5LO8E+OZtWAztR8YZcZdvqQmR0CVRml1joYtHFWQP8rXi0kTkdXHOcsJuEDXNSikeKxagbAbG542RBdPpeebyi3CIXTmivGGRnTOyopmon01fVLgRGYX4YXbG22MkfnGEugNL8kblHbIdMsOuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqh/dE7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422074,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422074,
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
  "id": -576460752303422073,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422073,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECnNHLJS5b+6fh/nKJBcI5Lrug8tJ8j5LO8E+OZtWAztR8YZcZdvqQmR0CVRml1joYtHFWQP8rXi0kTkdXHOcsJuEDXNSikeKxagbAbG542RBdPpeebyi3CIXTmivGGRnTOyopmon01fVLgRGYX4YXbG22MkfnGEugNL8kblHbIdMsOuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqh/dE7",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422072,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422072,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvNXSzg2XFr1K6EV22gnXzbuZMsxcCtAmBzkrWFauP+bA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RqAVF9Y=",
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
  "id": -576460752303422071,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDfbKzW3q/Sn34+JHRxtS0ssFu+Nanius8qRVxDOvD7SQWgIa1EVLE9Z1c2298+LXiLDjThk0JpJSJ/uheAyuYDuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZZy1K4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422071,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDfbKzW3q/Sn34+JHRxtS0ssFu+Nanius8qRVxDOvD7SQWgIa1EVLE9Z1c2298+LXiLDjThk0JpJSJ/uheAyuYDuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZZy1K4",
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
  "id": -576460752303422070,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDMpQl9qPazLenQ+ni+COdzYla5jbd5LqN6RSjOBmwTAgZjO0iUCKx2YUH9L+0M/ORmgeXEN9RDim6fJd/48ewAuEDfbKzW3q/Sn34+JHRxtS0ssFu+Nanius8qRVxDOvD7SQWgIa1EVLE9Z1c2298+LXiLDjThk0JpJSJ/uheAyuYDuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYkNQjU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422070,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+NILAfiEuEDMpQl9qPazLenQ+ni+COdzYla5jbd5LqN6RSjOBmwTAgZjO0iUCKx2YUH9L+0M/ORmgeXEN9RDim6fJd/48ewAuEDfbKzW3q/Sn34+JHRxtS0ssFu+Nanius8qRVxDOvD7SQWgIa1EVLE9Z1c2298+LXiLDjThk0JpJSJ/uheAyuYDuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYkNQjU"
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+NILAfiEuEDMpQl9qPazLenQ+ni+COdzYla5jbd5LqN6RSjOBmwTAgZjO0iUCKx2YUH9L+0M/ORmgeXEN9RDim6fJd/48ewAuEDfbKzW3q/Sn34+JHRxtS0ssFu+Nanius8qRVxDOvD7SQWgIa1EVLE9Z1c2298+LXiLDjThk0JpJSJ/uheAyuYDuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYkNQjU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422069,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422069,
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
  "id": -576460752303422068,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422068,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDMpQl9qPazLenQ+ni+COdzYla5jbd5LqN6RSjOBmwTAgZjO0iUCKx2YUH9L+0M/ORmgeXEN9RDim6fJd/48ewAuEDfbKzW3q/Sn34+JHRxtS0ssFu+Nanius8qRVxDOvD7SQWgIa1EVLE9Z1c2298+LXiLDjThk0JpJSJ/uheAyuYDuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYkNQjU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422067,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422067,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDMpQl9qPazLenQ+ni+COdzYla5jbd5LqN6RSjOBmwTAgZjO0iUCKx2YUH9L+0M/ORmgeXEN9RDim6fJd/48ewAuEDfbKzW3q/Sn34+JHRxtS0ssFu+Nanius8qRVxDOvD7SQWgIa1EVLE9Z1c2298+LXiLDjThk0JpJSJ/uheAyuYDuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYkNQjU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422066,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422066,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvNXSzg2XFr1K6EV22gnXzbuZMsxcCtAmBzkrWFauP+bBKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCypJvoaI=",
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
  "id": -576460752303422065,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDgOGfrRgiKBcz+ZnpMu48oOtSRmiVZB7NgbpQDZummz5CpFKzix/yNhIDRt4Jgh0pwZo3PZuMlMwm4yWPF06IGuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspwrSBh"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422065,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDgOGfrRgiKBcz+ZnpMu48oOtSRmiVZB7NgbpQDZummz5CpFKzix/yNhIDRt4Jgh0pwZo3PZuMlMwm4yWPF06IGuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspwrSBh",
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
  "id": -576460752303422064,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBQD894PytN05x3QBXondzUKZjOcfWX5fBtM2DfJpyedtpJCMKSI61tSxXHvgrlTmrEHKXK6Tzroi9oFz2nmOYBuEDgOGfrRgiKBcz+ZnpMu48oOtSRmiVZB7NgbpQDZummz5CpFKzix/yNhIDRt4Jgh0pwZo3PZuMlMwm4yWPF06IGuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqXJF5O"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422064,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+NILAfiEuEBQD894PytN05x3QBXondzUKZjOcfWX5fBtM2DfJpyedtpJCMKSI61tSxXHvgrlTmrEHKXK6Tzroi9oFz2nmOYBuEDgOGfrRgiKBcz+ZnpMu48oOtSRmiVZB7NgbpQDZummz5CpFKzix/yNhIDRt4Jgh0pwZo3PZuMlMwm4yWPF06IGuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqXJF5O"
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+NILAfiEuEBQD894PytN05x3QBXondzUKZjOcfWX5fBtM2DfJpyedtpJCMKSI61tSxXHvgrlTmrEHKXK6Tzroi9oFz2nmOYBuEDgOGfrRgiKBcz+ZnpMu48oOtSRmiVZB7NgbpQDZummz5CpFKzix/yNhIDRt4Jgh0pwZo3PZuMlMwm4yWPF06IGuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqXJF5O"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422063,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422063,
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
  "id": -576460752303422062,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422062,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBQD894PytN05x3QBXondzUKZjOcfWX5fBtM2DfJpyedtpJCMKSI61tSxXHvgrlTmrEHKXK6Tzroi9oFz2nmOYBuEDgOGfrRgiKBcz+ZnpMu48oOtSRmiVZB7NgbpQDZummz5CpFKzix/yNhIDRt4Jgh0pwZo3PZuMlMwm4yWPF06IGuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqXJF5O",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422061,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422061,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvNXSzg2XFr1K6EV22gnXzbuZMsxcCtAmBzkrWFauP+bBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgCBubA=",
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
  "id": -576460752303422060,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB8wjq3ejwuSXEvPWnQlTE24QFIDNeSF9EyH5Ygu8DqSxBJvr4iVGng2TMBnvA4Ic33RBduC4ZH1+k+MaDKVR8MuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbgTDee"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422060,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB8wjq3ejwuSXEvPWnQlTE24QFIDNeSF9EyH5Ygu8DqSxBJvr4iVGng2TMBnvA4Ic33RBduC4ZH1+k+MaDKVR8MuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbgTDee",
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
  "id": -576460752303422059,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB8wjq3ejwuSXEvPWnQlTE24QFIDNeSF9EyH5Ygu8DqSxBJvr4iVGng2TMBnvA4Ic33RBduC4ZH1+k+MaDKVR8MuEDdDYg6jzIDMsIoqRdpcVF8Gnd2T0aF4eCDT/+EsqJRo0dsFwdazXlY5508qDS2ubtlSf67z3t8tAGgcFNigdMAuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaP6vvZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422059,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+NILAfiEuEB8wjq3ejwuSXEvPWnQlTE24QFIDNeSF9EyH5Ygu8DqSxBJvr4iVGng2TMBnvA4Ic33RBduC4ZH1+k+MaDKVR8MuEDdDYg6jzIDMsIoqRdpcVF8Gnd2T0aF4eCDT/+EsqJRo0dsFwdazXlY5508qDS2ubtlSf67z3t8tAGgcFNigdMAuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaP6vvZ"
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "state": "tx_+NILAfiEuEB8wjq3ejwuSXEvPWnQlTE24QFIDNeSF9EyH5Ygu8DqSxBJvr4iVGng2TMBnvA4Ic33RBduC4ZH1+k+MaDKVR8MuEDdDYg6jzIDMsIoqRdpcVF8Gnd2T0aF4eCDT/+EsqJRo0dsFwdazXlY5508qDS2ubtlSf67z3t8tAGgcFNigdMAuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaP6vvZ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422058,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422058,
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
  "id": -576460752303422057,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422057,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB8wjq3ejwuSXEvPWnQlTE24QFIDNeSF9EyH5Ygu8DqSxBJvr4iVGng2TMBnvA4Ic33RBduC4ZH1+k+MaDKVR8MuEDdDYg6jzIDMsIoqRdpcVF8Gnd2T0aF4eCDT/+EsqJRo0dsFwdazXlY5508qDS2ubtlSf67z3t8tAGgcFNigdMAuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaP6vvZ",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEB8wjq3ejwuSXEvPWnQlTE24QFIDNeSF9EyH5Ygu8DqSxBJvr4iVGng2TMBnvA4Ic33RBduC4ZH1+k+MaDKVR8MuEDdDYg6jzIDMsIoqRdpcVF8Gnd2T0aF4eCDT/+EsqJRo0dsFwdazXlY5508qDS2ubtlSf67z3t8tAGgcFNigdMAuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaP6vvZ",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEB8wjq3ejwuSXEvPWnQlTE24QFIDNeSF9EyH5Ygu8DqSxBJvr4iVGng2TMBnvA4Ic33RBduC4ZH1+k+MaDKVR8MuEDdDYg6jzIDMsIoqRdpcVF8Gnd2T0aF4eCDT/+EsqJRo0dsFwdazXlY5508qDS2ubtlSf67z3t8tAGgcFNigdMAuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaP6vvZ",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBvNXSzg2XFr1K6EV22gnXzbuZMsxcCtAmBzkrWFauP+boQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEB8wjq3ejwuSXEvPWnQlTE24QFIDNeSF9EyH5Ygu8DqSxBJvr4iVGng2TMBnvA4Ic33RBduC4ZH1+k+MaDKVR8MuEDdDYg6jzIDMsIoqRdpcVF8Gnd2T0aF4eCDT/+EsqJRo0dsFwdazXlY5508qDS2ubtlSf67z3t8tAGgcFNigdMAuEj4RjkCoQbzV0s4Nlxa9SuhFdtoJ1827mTLMXArQJgc5K1hWrj/mwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGSNwYbAAgb6raq/e",
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
  "id": -576460752303422056,
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422056,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422055,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
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
  "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
  "id": -576460752303422055,
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
    "channel_id": "ch_2rApWDaHtTqLvHJX8RFhW3UjfW1og2t74PzUcMEwj2su25ut3r",
    "data": {
      "event": "died"
    }
  },
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
      "fsm_id": "ba_do8Ss3r3WdqQ5eNNuIQybCXsvrgVqi4+oDXFD8saLs6KGnjh"
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
      "fsm_id": "ba_zUAffPOnYPDQteGdPgf07ujLDT0QBHPSLpbcRdtoIwpzU84U"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBvjEjQSI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422054,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuED8o/XSVIzgaVjlaet1L51ht2/0KAkHOBZX8PZdCZUoqx0FQ3O/GHZwLuJudBnSUwycfWmgc3+75f0rcJdO8FcKuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgb7j2XeI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422054,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_zUAffPOnYPDQteGdPgf07ujLDT0QBHPSLpbcRdtoIwpzU84U"
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+MwLAfhCuED8o/XSVIzgaVjlaet1L51ht2/0KAkHOBZX8PZdCZUoqx0FQ3O/GHZwLuJudBnSUwycfWmgc3+75f0rcJdO8FcKuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgb7j2XeI",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422053,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhA2/B90YkPEw6Cg/lloaAAA7Zn1w28WGoHMfZezqgPozYtjmPj+bX4dBKMOz/4tBwgg4VDYyupuG6cvNpN2lUeBrhA/KP10lSM4GlY5WnrdS+dYbdv9CgJBzgWV/D2XQmVKKsdBUNzvxh2cC7ibnQZ0lMMnH1poHN/u+X9K3CXTvBXCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG+fXPhJA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422053,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhA2/B90YkPEw6Cg/lloaAAA7Zn1w28WGoHMfZezqgPozYtjmPj+bX4dBKMOz/4tBwgg4VDYyupuG6cvNpN2lUeBrhA/KP10lSM4GlY5WnrdS+dYbdv9CgJBzgWV/D2XQmVKKsdBUNzvxh2cC7ibnQZ0lMMnH1poHN/u+X9K3CXTvBXCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG+fXPhJA==",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_do8Ss3r3WdqQ5eNNuIQybCXsvrgVqi4+oDXFD8saLs6KGnjh"
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhA2/B90YkPEw6Cg/lloaAAA7Zn1w28WGoHMfZezqgPozYtjmPj+bX4dBKMOz/4tBwgg4VDYyupuG6cvNpN2lUeBrhA/KP10lSM4GlY5WnrdS+dYbdv9CgJBzgWV/D2XQmVKKsdBUNzvxh2cC7ibnQZ0lMMnH1poHN/u+X9K3CXTvBXCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG+fXPhJA==",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhA2/B90YkPEw6Cg/lloaAAA7Zn1w28WGoHMfZezqgPozYtjmPj+bX4dBKMOz/4tBwgg4VDYyupuG6cvNpN2lUeBrhA/KP10lSM4GlY5WnrdS+dYbdv9CgJBzgWV/D2XQmVKKsdBUNzvxh2cC7ibnQZ0lMMnH1poHN/u+X9K3CXTvBXCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG+fXPhJA==",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhA2/B90YkPEw6Cg/lloaAAA7Zn1w28WGoHMfZezqgPozYtjmPj+bX4dBKMOz/4tBwgg4VDYyupuG6cvNpN2lUeBrhA/KP10lSM4GlY5WnrdS+dYbdv9CgJBzgWV/D2XQmVKKsdBUNzvxh2cC7ibnQZ0lMMnH1poHN/u+X9K3CXTvBXCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG+fXPhJA==",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "message": {
        "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "message": {
        "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
  "id": -576460752303422052,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422052,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+QEOCwH4hLhA2/B90YkPEw6Cg/lloaAAA7Zn1w28WGoHMfZezqgPozYtjmPj+bX4dBKMOz/4tBwgg4VDYyupuG6cvNpN2lUeBrhA/KP10lSM4GlY5WnrdS+dYbdv9CgJBzgWV/D2XQmVKKsdBUNzvxh2cC7ibnQZ0lMMnH1poHN/u+X9K3CXTvBXCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG+fXPhJA=="
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+QEOCwH4hLhA2/B90YkPEw6Cg/lloaAAA7Zn1w28WGoHMfZezqgPozYtjmPj+bX4dBKMOz/4tBwgg4VDYyupuG6cvNpN2lUeBrhA/KP10lSM4GlY5WnrdS+dYbdv9CgJBzgWV/D2XQmVKKsdBUNzvxh2cC7ibnQZ0lMMnH1poHN/u+X9K3CXTvBXCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG+fXPhJA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422051,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422051,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrJtH2FRNFJ0hBrnbcPRJeaATsHNo7rpxu9RnoEEFqCMAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCynN80no=",
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
  "id": -576460752303422050,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAOSygnsDqzyd1jaFV/hP+4r+KcVFU4QMle6LQrTvRiPuggOHx/v9T+/4E1MfseMSU20NbTwb1vj50H8ucYbkEAuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrFCQ3t"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422050,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAOSygnsDqzyd1jaFV/hP+4r+KcVFU4QMle6LQrTvRiPuggOHx/v9T+/4E1MfseMSU20NbTwb1vj50H8ucYbkEAuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrFCQ3t",
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
  "id": -576460752303422049,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAOSygnsDqzyd1jaFV/hP+4r+KcVFU4QMle6LQrTvRiPuggOHx/v9T+/4E1MfseMSU20NbTwb1vj50H8ucYbkEAuEDF0lENfixbqcPiCeWIIehW68mAgHsss/uKVc8g2Z9FFLlfmyn2D8WqMFdAwDdDFWW6q3OSWj1IeI0gwoEinYcAuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspWZQ8R"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422049,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+NILAfiEuEAOSygnsDqzyd1jaFV/hP+4r+KcVFU4QMle6LQrTvRiPuggOHx/v9T+/4E1MfseMSU20NbTwb1vj50H8ucYbkEAuEDF0lENfixbqcPiCeWIIehW68mAgHsss/uKVc8g2Z9FFLlfmyn2D8WqMFdAwDdDFWW6q3OSWj1IeI0gwoEinYcAuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspWZQ8R"
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+NILAfiEuEAOSygnsDqzyd1jaFV/hP+4r+KcVFU4QMle6LQrTvRiPuggOHx/v9T+/4E1MfseMSU20NbTwb1vj50H8ucYbkEAuEDF0lENfixbqcPiCeWIIehW68mAgHsss/uKVc8g2Z9FFLlfmyn2D8WqMFdAwDdDFWW6q3OSWj1IeI0gwoEinYcAuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspWZQ8R"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422048,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422048,
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
  "id": -576460752303422047,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422047,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAOSygnsDqzyd1jaFV/hP+4r+KcVFU4QMle6LQrTvRiPuggOHx/v9T+/4E1MfseMSU20NbTwb1vj50H8ucYbkEAuEDF0lENfixbqcPiCeWIIehW68mAgHsss/uKVc8g2Z9FFLlfmyn2D8WqMFdAwDdDFWW6q3OSWj1IeI0gwoEinYcAuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspWZQ8R",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422046,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422046,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrJtH2FRNFJ0hBrnbcPRJeaATsHNo7rpxu9RnoEEFqCMA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RrEruxY=",
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
  "id": -576460752303422045,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA2CIczCKfUWVWnvHZcCzxUU8T6Q5ViHs57sPHdfVDooc7It8ZtgeEBvrlkwlGd7mHvt65QGi21eapavM/s/08EuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaDudEr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422045,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA2CIczCKfUWVWnvHZcCzxUU8T6Q5ViHs57sPHdfVDooc7It8ZtgeEBvrlkwlGd7mHvt65QGi21eapavM/s/08EuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaDudEr",
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
  "id": -576460752303422044,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA2CIczCKfUWVWnvHZcCzxUU8T6Q5ViHs57sPHdfVDooc7It8ZtgeEBvrlkwlGd7mHvt65QGi21eapavM/s/08EuED7K4jXCsvWui50qE043DzAngACpPS7QOmpK7EiW+6epRXNEsKDhTe/9zSKYmbpXCemXNPemaR6wsblBJsSrZcPuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZF2xFh"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422044,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+NILAfiEuEA2CIczCKfUWVWnvHZcCzxUU8T6Q5ViHs57sPHdfVDooc7It8ZtgeEBvrlkwlGd7mHvt65QGi21eapavM/s/08EuED7K4jXCsvWui50qE043DzAngACpPS7QOmpK7EiW+6epRXNEsKDhTe/9zSKYmbpXCemXNPemaR6wsblBJsSrZcPuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZF2xFh"
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+NILAfiEuEA2CIczCKfUWVWnvHZcCzxUU8T6Q5ViHs57sPHdfVDooc7It8ZtgeEBvrlkwlGd7mHvt65QGi21eapavM/s/08EuED7K4jXCsvWui50qE043DzAngACpPS7QOmpK7EiW+6epRXNEsKDhTe/9zSKYmbpXCemXNPemaR6wsblBJsSrZcPuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZF2xFh"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422043,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422043,
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
  "id": -576460752303422042,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422042,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA2CIczCKfUWVWnvHZcCzxUU8T6Q5ViHs57sPHdfVDooc7It8ZtgeEBvrlkwlGd7mHvt65QGi21eapavM/s/08EuED7K4jXCsvWui50qE043DzAngACpPS7QOmpK7EiW+6epRXNEsKDhTe/9zSKYmbpXCemXNPemaR6wsblBJsSrZcPuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZF2xFh",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422041,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422041,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA2CIczCKfUWVWnvHZcCzxUU8T6Q5ViHs57sPHdfVDooc7It8ZtgeEBvrlkwlGd7mHvt65QGi21eapavM/s/08EuED7K4jXCsvWui50qE043DzAngACpPS7QOmpK7EiW+6epRXNEsKDhTe/9zSKYmbpXCemXNPemaR6wsblBJsSrZcPuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZF2xFh",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422040,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422040,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrJtH2FRNFJ0hBrnbcPRJeaATsHNo7rpxu9RnoEEFqCMBKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyp00TDc=",
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
  "id": -576460752303422039,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAN9QaGhf5uxX7s1nuKSJdk6nqRQ9Y8vpONSlwAKeTSXDZCTs8hfCE47/ebC/7uiFHNIFQsv5hxU5igWTba/v0DuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoCX77g"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422039,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAN9QaGhf5uxX7s1nuKSJdk6nqRQ9Y8vpONSlwAKeTSXDZCTs8hfCE47/ebC/7uiFHNIFQsv5hxU5igWTba/v0DuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoCX77g",
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
  "id": -576460752303422038,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAN9QaGhf5uxX7s1nuKSJdk6nqRQ9Y8vpONSlwAKeTSXDZCTs8hfCE47/ebC/7uiFHNIFQsv5hxU5igWTba/v0DuEDpXMqnoqyeDImXDv6TTIL+IlmThM2UV45lOf8eeSM/Z1J0BMRgmgu7DuFTWGnd/4EuOHNieJ4gyITslXrJG28OuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsovlWIT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422038,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+NILAfiEuEAN9QaGhf5uxX7s1nuKSJdk6nqRQ9Y8vpONSlwAKeTSXDZCTs8hfCE47/ebC/7uiFHNIFQsv5hxU5igWTba/v0DuEDpXMqnoqyeDImXDv6TTIL+IlmThM2UV45lOf8eeSM/Z1J0BMRgmgu7DuFTWGnd/4EuOHNieJ4gyITslXrJG28OuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsovlWIT"
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+NILAfiEuEAN9QaGhf5uxX7s1nuKSJdk6nqRQ9Y8vpONSlwAKeTSXDZCTs8hfCE47/ebC/7uiFHNIFQsv5hxU5igWTba/v0DuEDpXMqnoqyeDImXDv6TTIL+IlmThM2UV45lOf8eeSM/Z1J0BMRgmgu7DuFTWGnd/4EuOHNieJ4gyITslXrJG28OuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsovlWIT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422037,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422037,
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
  "id": -576460752303422036,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422036,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAN9QaGhf5uxX7s1nuKSJdk6nqRQ9Y8vpONSlwAKeTSXDZCTs8hfCE47/ebC/7uiFHNIFQsv5hxU5igWTba/v0DuEDpXMqnoqyeDImXDv6TTIL+IlmThM2UV45lOf8eeSM/Z1J0BMRgmgu7DuFTWGnd/4EuOHNieJ4gyITslXrJG28OuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsovlWIT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422035,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422035,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrJtH2FRNFJ0hBrnbcPRJeaATsHNo7rpxu9RnoEEFqCMBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rtn42iw=",
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
  "id": -576460752303422034,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDqjR2576+vzzp9GJy3ldQhJlBMEw+Gf+isEEsBBZ37nZ29z/+Y2+/aYmwLvhbv/VmsvG96OmkFFalLU1tLEugMuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaKu/Pm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422034,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDqjR2576+vzzp9GJy3ldQhJlBMEw+Gf+isEEsBBZ37nZ29z/+Y2+/aYmwLvhbv/VmsvG96OmkFFalLU1tLEugMuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaKu/Pm",
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
  "id": -576460752303422033,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECTOwWlxhXHEj48bRcg1f71R9tWK9vu0lm0tC75A2hKFAPucwxndAWexSgWG35SMdVuRVhhKDLOa590/3mMXIkCuEDqjR2576+vzzp9GJy3ldQhJlBMEw+Gf+isEEsBBZ37nZ29z/+Y2+/aYmwLvhbv/VmsvG96OmkFFalLU1tLEugMuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYJ7O1J"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422033,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+NILAfiEuECTOwWlxhXHEj48bRcg1f71R9tWK9vu0lm0tC75A2hKFAPucwxndAWexSgWG35SMdVuRVhhKDLOa590/3mMXIkCuEDqjR2576+vzzp9GJy3ldQhJlBMEw+Gf+isEEsBBZ37nZ29z/+Y2+/aYmwLvhbv/VmsvG96OmkFFalLU1tLEugMuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYJ7O1J"
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "state": "tx_+NILAfiEuECTOwWlxhXHEj48bRcg1f71R9tWK9vu0lm0tC75A2hKFAPucwxndAWexSgWG35SMdVuRVhhKDLOa590/3mMXIkCuEDqjR2576+vzzp9GJy3ldQhJlBMEw+Gf+isEEsBBZ37nZ29z/+Y2+/aYmwLvhbv/VmsvG96OmkFFalLU1tLEugMuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYJ7O1J"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422032,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422032,
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
  "id": -576460752303422031,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422031,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECTOwWlxhXHEj48bRcg1f71R9tWK9vu0lm0tC75A2hKFAPucwxndAWexSgWG35SMdVuRVhhKDLOa590/3mMXIkCuEDqjR2576+vzzp9GJy3ldQhJlBMEw+Gf+isEEsBBZ37nZ29z/+Y2+/aYmwLvhbv/VmsvG96OmkFFalLU1tLEugMuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYJ7O1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECTOwWlxhXHEj48bRcg1f71R9tWK9vu0lm0tC75A2hKFAPucwxndAWexSgWG35SMdVuRVhhKDLOa590/3mMXIkCuEDqjR2576+vzzp9GJy3ldQhJlBMEw+Gf+isEEsBBZ37nZ29z/+Y2+/aYmwLvhbv/VmsvG96OmkFFalLU1tLEugMuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYJ7O1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECTOwWlxhXHEj48bRcg1f71R9tWK9vu0lm0tC75A2hKFAPucwxndAWexSgWG35SMdVuRVhhKDLOa590/3mMXIkCuEDqjR2576+vzzp9GJy3ldQhJlBMEw+Gf+isEEsBBZ37nZ29z/+Y2+/aYmwLvhbv/VmsvG96OmkFFalLU1tLEugMuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYJ7O1J",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBrJtH2FRNFJ0hBrnbcPRJeaATsHNo7rpxu9RnoEEFqCMoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuECTOwWlxhXHEj48bRcg1f71R9tWK9vu0lm0tC75A2hKFAPucwxndAWexSgWG35SMdVuRVhhKDLOa590/3mMXIkCuEDqjR2576+vzzp9GJy3ldQhJlBMEw+Gf+isEEsBBZ37nZ29z/+Y2+/aYmwLvhbv/VmsvG96OmkFFalLU1tLEugMuEj4RjkCoQaybR9hUTRSdIQa523D0SXmgE7BzaO66cbvUZ6BBBagjAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGR7ISegAQWknsbo=",
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
  "method": "channels.slash_sign",
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
  "id": -576460752303422030,
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422030,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422029,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
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
  "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
  "id": -576460752303422029,
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
    "channel_id": "ch_2MafF2BhQWPXxHW6ZNxb52BR9W6aVW2R64pH1dThuR3Mey1z1J",
    "data": {
      "event": "died"
    }
  },
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
      "fsm_id": "ba_LPAS/fn9abUygFnQdLgwpdliX5oBh92/g4CdiQdMgywKmOmW"
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
      "fsm_id": "ba_GpbjUqcr8rrE7pHBl2Fr6oiiIpM+SelsWNDWMvhOsMZzeKHC"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBwCfhsIs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422028,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAzvNst4fgW+gguocQPj94sh3332/JuFYqsEHL0HQtOylY069zo4hsRDxVKbj+4Gwtp5m1gGzMKN533blquPUUAuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcAzhQPl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422028,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_GpbjUqcr8rrE7pHBl2Fr6oiiIpM+SelsWNDWMvhOsMZzeKHC"
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEAzvNst4fgW+gguocQPj94sh3332/JuFYqsEHL0HQtOylY069zo4hsRDxVKbj+4Gwtp5m1gGzMKN533blquPUUAuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcAzhQPl",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422027,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAM7zbLeH4FvoILqHED4/eLId999vybhWKrBBy9B0LTspWNOvc6OIbEQ8VSm4/uBsLaeZtYBszCjed925arj1FALhAoGIsoBailO6FLGVbeqncGSzSCDAJsfJ/r4O129FUv2yd42US8Pv49Mv0z0XfjYudv9ZZUBDUfeODUQ78oBk4BbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHA8DADHg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422027,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAM7zbLeH4FvoILqHED4/eLId999vybhWKrBBy9B0LTspWNOvc6OIbEQ8VSm4/uBsLaeZtYBszCjed925arj1FALhAoGIsoBailO6FLGVbeqncGSzSCDAJsfJ/r4O129FUv2yd42US8Pv49Mv0z0XfjYudv9ZZUBDUfeODUQ78oBk4BbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHA8DADHg==",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_LPAS/fn9abUygFnQdLgwpdliX5oBh92/g4CdiQdMgywKmOmW"
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAM7zbLeH4FvoILqHED4/eLId999vybhWKrBBy9B0LTspWNOvc6OIbEQ8VSm4/uBsLaeZtYBszCjed925arj1FALhAoGIsoBailO6FLGVbeqncGSzSCDAJsfJ/r4O129FUv2yd42US8Pv49Mv0z0XfjYudv9ZZUBDUfeODUQ78oBk4BbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHA8DADHg==",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAM7zbLeH4FvoILqHED4/eLId999vybhWKrBBy9B0LTspWNOvc6OIbEQ8VSm4/uBsLaeZtYBszCjed925arj1FALhAoGIsoBailO6FLGVbeqncGSzSCDAJsfJ/r4O129FUv2yd42US8Pv49Mv0z0XfjYudv9ZZUBDUfeODUQ78oBk4BbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHA8DADHg==",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAM7zbLeH4FvoILqHED4/eLId999vybhWKrBBy9B0LTspWNOvc6OIbEQ8VSm4/uBsLaeZtYBszCjed925arj1FALhAoGIsoBailO6FLGVbeqncGSzSCDAJsfJ/r4O129FUv2yd42US8Pv49Mv0z0XfjYudv9ZZUBDUfeODUQ78oBk4BbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHA8DADHg==",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "message": {
        "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "message": {
        "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
  "id": -576460752303422026,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422026,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+QEOCwH4hLhAM7zbLeH4FvoILqHED4/eLId999vybhWKrBBy9B0LTspWNOvc6OIbEQ8VSm4/uBsLaeZtYBszCjed925arj1FALhAoGIsoBailO6FLGVbeqncGSzSCDAJsfJ/r4O129FUv2yd42US8Pv49Mv0z0XfjYudv9ZZUBDUfeODUQ78oBk4BbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHA8DADHg=="
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+QEOCwH4hLhAM7zbLeH4FvoILqHED4/eLId999vybhWKrBBy9B0LTspWNOvc6OIbEQ8VSm4/uBsLaeZtYBszCjed925arj1FALhAoGIsoBailO6FLGVbeqncGSzSCDAJsfJ/r4O129FUv2yd42US8Pv49Mv0z0XfjYudv9ZZUBDUfeODUQ78oBk4BbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHA8DADHg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422025,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422025,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBu33ml9iOJ+RATsKqUoMJ9G7E4eaQp1H2w2w8X0KJNS1AqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyiO8uc4=",
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
  "id": -576460752303422024,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA3UNr+nUbCtaU27M0cn0cxDf/3oa0Z6JVuwT6M2S5RPTZwZxy3FcJUwyMpWKw91KzTpCCHPgvxit2gZx1rmfQJuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsooWJLT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422024,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA3UNr+nUbCtaU27M0cn0cxDf/3oa0Z6JVuwT6M2S5RPTZwZxy3FcJUwyMpWKw91KzTpCCHPgvxit2gZx1rmfQJuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsooWJLT",
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
  "id": -576460752303422023,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA3UNr+nUbCtaU27M0cn0cxDf/3oa0Z6JVuwT6M2S5RPTZwZxy3FcJUwyMpWKw91KzTpCCHPgvxit2gZx1rmfQJuECOrhO7T6KdhhjLYRqbtnYiOPuVm3543Z+bwx1WyRkL/FLpWUbhxEM6meqd8qeZ+UnEueenNg6P2oUFA6okKGMOuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqWVssT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422023,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+NILAfiEuEA3UNr+nUbCtaU27M0cn0cxDf/3oa0Z6JVuwT6M2S5RPTZwZxy3FcJUwyMpWKw91KzTpCCHPgvxit2gZx1rmfQJuECOrhO7T6KdhhjLYRqbtnYiOPuVm3543Z+bwx1WyRkL/FLpWUbhxEM6meqd8qeZ+UnEueenNg6P2oUFA6okKGMOuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqWVssT"
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+NILAfiEuEA3UNr+nUbCtaU27M0cn0cxDf/3oa0Z6JVuwT6M2S5RPTZwZxy3FcJUwyMpWKw91KzTpCCHPgvxit2gZx1rmfQJuECOrhO7T6KdhhjLYRqbtnYiOPuVm3543Z+bwx1WyRkL/FLpWUbhxEM6meqd8qeZ+UnEueenNg6P2oUFA6okKGMOuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqWVssT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422022,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422022,
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
  "id": -576460752303422021,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422021,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA3UNr+nUbCtaU27M0cn0cxDf/3oa0Z6JVuwT6M2S5RPTZwZxy3FcJUwyMpWKw91KzTpCCHPgvxit2gZx1rmfQJuECOrhO7T6KdhhjLYRqbtnYiOPuVm3543Z+bwx1WyRkL/FLpWUbhxEM6meqd8qeZ+UnEueenNg6P2oUFA6okKGMOuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqWVssT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422020,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422020,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBu33ml9iOJ+RATsKqUoMJ9G7E4eaQp1H2w2w8X0KJNS1A6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjrM9bQ=",
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
  "id": -576460752303422019,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEALgoQvdbJfSDKF8Lta8vLCno51D/KChcgg+Tv2gTitmnLX3hOBPWkEDh9HYt4d1849cS3fqHOwjm+3QGff3GsKuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYvufvD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422019,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEALgoQvdbJfSDKF8Lta8vLCno51D/KChcgg+Tv2gTitmnLX3hOBPWkEDh9HYt4d1849cS3fqHOwjm+3QGff3GsKuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYvufvD",
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
  "id": -576460752303422018,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEALgoQvdbJfSDKF8Lta8vLCno51D/KChcgg+Tv2gTitmnLX3hOBPWkEDh9HYt4d1849cS3fqHOwjm+3QGff3GsKuED/shPnhJkYkZ36iMbbZI5pl3mi3Q/OxMfBZAJK2ZrK7tTWTmbAQPKTG6YlYWypSwBzZBCburAX89ApK1N+yykHuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZLOmkT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422018,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+NILAfiEuEALgoQvdbJfSDKF8Lta8vLCno51D/KChcgg+Tv2gTitmnLX3hOBPWkEDh9HYt4d1849cS3fqHOwjm+3QGff3GsKuED/shPnhJkYkZ36iMbbZI5pl3mi3Q/OxMfBZAJK2ZrK7tTWTmbAQPKTG6YlYWypSwBzZBCburAX89ApK1N+yykHuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZLOmkT"
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+NILAfiEuEALgoQvdbJfSDKF8Lta8vLCno51D/KChcgg+Tv2gTitmnLX3hOBPWkEDh9HYt4d1849cS3fqHOwjm+3QGff3GsKuED/shPnhJkYkZ36iMbbZI5pl3mi3Q/OxMfBZAJK2ZrK7tTWTmbAQPKTG6YlYWypSwBzZBCburAX89ApK1N+yykHuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZLOmkT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422017,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422017,
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
  "id": -576460752303422016,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422016,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEALgoQvdbJfSDKF8Lta8vLCno51D/KChcgg+Tv2gTitmnLX3hOBPWkEDh9HYt4d1849cS3fqHOwjm+3QGff3GsKuED/shPnhJkYkZ36iMbbZI5pl3mi3Q/OxMfBZAJK2ZrK7tTWTmbAQPKTG6YlYWypSwBzZBCburAX89ApK1N+yykHuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZLOmkT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422015,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422015,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEALgoQvdbJfSDKF8Lta8vLCno51D/KChcgg+Tv2gTitmnLX3hOBPWkEDh9HYt4d1849cS3fqHOwjm+3QGff3GsKuED/shPnhJkYkZ36iMbbZI5pl3mi3Q/OxMfBZAJK2ZrK7tTWTmbAQPKTG6YlYWypSwBzZBCburAX89ApK1N+yykHuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZLOmkT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422014,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422014,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBu33ml9iOJ+RATsKqUoMJ9G7E4eaQp1H2w2w8X0KJNS1BKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCymapxKI=",
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
  "id": -576460752303422013,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAJhoN5jIF0ETokaAF400Sun6OD1VfdmHfWWvNRtssubiKLSYJpe9o84qUO1CllLblMe4i6nRMk4SvwK+ffofUCuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspvxO6B"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422013,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAJhoN5jIF0ETokaAF400Sun6OD1VfdmHfWWvNRtssubiKLSYJpe9o84qUO1CllLblMe4i6nRMk4SvwK+ffofUCuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspvxO6B",
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
  "id": -576460752303422012,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEADb3rPMx//bWOYfwAht4O6IxK/NKMQgjn6yMdzX5+iHUOb6uJ0ZzLTEgklPwC3wQTFsIphCKBDzlH9siR4d3MHuEAJhoN5jIF0ETokaAF400Sun6OD1VfdmHfWWvNRtssubiKLSYJpe9o84qUO1CllLblMe4i6nRMk4SvwK+ffofUCuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoATcti"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422012,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+NILAfiEuEADb3rPMx//bWOYfwAht4O6IxK/NKMQgjn6yMdzX5+iHUOb6uJ0ZzLTEgklPwC3wQTFsIphCKBDzlH9siR4d3MHuEAJhoN5jIF0ETokaAF400Sun6OD1VfdmHfWWvNRtssubiKLSYJpe9o84qUO1CllLblMe4i6nRMk4SvwK+ffofUCuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoATcti"
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+NILAfiEuEADb3rPMx//bWOYfwAht4O6IxK/NKMQgjn6yMdzX5+iHUOb6uJ0ZzLTEgklPwC3wQTFsIphCKBDzlH9siR4d3MHuEAJhoN5jIF0ETokaAF400Sun6OD1VfdmHfWWvNRtssubiKLSYJpe9o84qUO1CllLblMe4i6nRMk4SvwK+ffofUCuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoATcti"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422011,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422011,
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
  "id": -576460752303422010,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422010,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEADb3rPMx//bWOYfwAht4O6IxK/NKMQgjn6yMdzX5+iHUOb6uJ0ZzLTEgklPwC3wQTFsIphCKBDzlH9siR4d3MHuEAJhoN5jIF0ETokaAF400Sun6OD1VfdmHfWWvNRtssubiKLSYJpe9o84qUO1CllLblMe4i6nRMk4SvwK+ffofUCuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoATcti",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422009,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422009,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBu33ml9iOJ+RATsKqUoMJ9G7E4eaQp1H2w2w8X0KJNS1BaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RvNoFoI=",
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
  "id": -576460752303422008,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED/XsadnCwv0WWAniriwWSNMv6uXJwnb7KSmeHEUIyF2/d/8NuBiENGUXHTNondCi2OgepXl0wSCNU4dC+nzkUNuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ93F5j"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422008,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+JALAfhCuED/XsadnCwv0WWAniriwWSNMv6uXJwnb7KSmeHEUIyF2/d/8NuBiENGUXHTNondCi2OgepXl0wSCNU4dC+nzkUNuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ93F5j",
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
  "id": -576460752303422007,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBxW8KvBAsdxC1/aCkCRRfBtkFQmX/yExbeyxXE26k3qcMbPd3JwRT1Jly09jtQRvuIUYRYEbJQcD7uJ+sE4+QKuED/XsadnCwv0WWAniriwWSNMv6uXJwnb7KSmeHEUIyF2/d/8NuBiENGUXHTNondCi2OgepXl0wSCNU4dC+nzkUNuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY+qP2R"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422007,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+NILAfiEuEBxW8KvBAsdxC1/aCkCRRfBtkFQmX/yExbeyxXE26k3qcMbPd3JwRT1Jly09jtQRvuIUYRYEbJQcD7uJ+sE4+QKuED/XsadnCwv0WWAniriwWSNMv6uXJwnb7KSmeHEUIyF2/d/8NuBiENGUXHTNondCi2OgepXl0wSCNU4dC+nzkUNuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY+qP2R"
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "state": "tx_+NILAfiEuEBxW8KvBAsdxC1/aCkCRRfBtkFQmX/yExbeyxXE26k3qcMbPd3JwRT1Jly09jtQRvuIUYRYEbJQcD7uJ+sE4+QKuED/XsadnCwv0WWAniriwWSNMv6uXJwnb7KSmeHEUIyF2/d/8NuBiENGUXHTNondCi2OgepXl0wSCNU4dC+nzkUNuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY+qP2R"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422006,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422006,
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
  "id": -576460752303422005,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422005,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBxW8KvBAsdxC1/aCkCRRfBtkFQmX/yExbeyxXE26k3qcMbPd3JwRT1Jly09jtQRvuIUYRYEbJQcD7uJ+sE4+QKuED/XsadnCwv0WWAniriwWSNMv6uXJwnb7KSmeHEUIyF2/d/8NuBiENGUXHTNondCi2OgepXl0wSCNU4dC+nzkUNuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY+qP2R",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBxW8KvBAsdxC1/aCkCRRfBtkFQmX/yExbeyxXE26k3qcMbPd3JwRT1Jly09jtQRvuIUYRYEbJQcD7uJ+sE4+QKuED/XsadnCwv0WWAniriwWSNMv6uXJwnb7KSmeHEUIyF2/d/8NuBiENGUXHTNondCi2OgepXl0wSCNU4dC+nzkUNuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY+qP2R",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBu33ml9iOJ+RATsKqUoMJ9G7E4eaQp1H2w2w8X0KJNS1oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBxW8KvBAsdxC1/aCkCRRfBtkFQmX/yExbeyxXE26k3qcMbPd3JwRT1Jly09jtQRvuIUYRYEbJQcD7uJ+sE4+QKuED/XsadnCwv0WWAniriwWSNMv6uXJwnb7KSmeHEUIyF2/d/8NuBiENGUXHTNondCi2OgepXl0wSCNU4dC+nzkUNuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGSNwYbAAgcGgzO8i",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
  "id": -576460752303422004,
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422004,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422003,
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBxW8KvBAsdxC1/aCkCRRfBtkFQmX/yExbeyxXE26k3qcMbPd3JwRT1Jly09jtQRvuIUYRYEbJQcD7uJ+sE4+QKuED/XsadnCwv0WWAniriwWSNMv6uXJwnb7KSmeHEUIyF2/d/8NuBiENGUXHTNondCi2OgepXl0wSCNU4dC+nzkUNuEj4RjkCoQbt95pfYjifkQE7CqlKDCfRuxOHmkKdR9sNsPF9CiTUtQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY+qP2R",
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
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
  "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
  "id": -576460752303422003,
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
    "channel_id": "ch_2ooZ4MKV63H55jdymEZb4W72ceYrkDAsLeKQx1j2iML8nKZTMz",
    "data": {
      "event": "died"
    }
  },
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
      "fsm_id": "ba_6sD0yO7vvG4dnEbNb1JM4LMlMFuW7LSMX3ieAiGytlCg/C1H"
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
      "fsm_id": "ba_AxksVHTltHvnx8p0rZNiEPRqNYQuzaECe/L3A5S4n8Dpq8/s"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBwegaxPA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422002,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECdbqGqOZ5zTzMzlVQbwAd9F/1zpUOqDA0CAEb2/PCBbcXSSE/b5S8IvAWyKw2gK8PCOv2LiB9uTueHAtIy2+UAuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcG1HT09"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422002,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_AxksVHTltHvnx8p0rZNiEPRqNYQuzaECe/L3A5S4n8Dpq8/s"
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECdbqGqOZ5zTzMzlVQbwAd9F/1zpUOqDA0CAEb2/PCBbcXSSE/b5S8IvAWyKw2gK8PCOv2LiB9uTueHAtIy2+UAuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgcG1HT09",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422001,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAm8HDLByInoI8cgnnZwF/xRWQ0ZIVmnovh6glSRUNUfqQgzaGc7urbN8Ej2ncgUStL/qevtfVhJgGmwfcajaZAbhAnW6hqjmec08zM5VUG8AHfRf9c6VDqgwNAgBG9vzwgW3F0khP2+UvCLwFsisNoCvDwjr9i4gfbk7nhwLSMtvlALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHBJEj/iA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303422001,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAm8HDLByInoI8cgnnZwF/xRWQ0ZIVmnovh6glSRUNUfqQgzaGc7urbN8Ej2ncgUStL/qevtfVhJgGmwfcajaZAbhAnW6hqjmec08zM5VUG8AHfRf9c6VDqgwNAgBG9vzwgW3F0khP2+UvCLwFsisNoCvDwjr9i4gfbk7nhwLSMtvlALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHBJEj/iA==",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_6sD0yO7vvG4dnEbNb1JM4LMlMFuW7LSMX3ieAiGytlCg/C1H"
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAm8HDLByInoI8cgnnZwF/xRWQ0ZIVmnovh6glSRUNUfqQgzaGc7urbN8Ej2ncgUStL/qevtfVhJgGmwfcajaZAbhAnW6hqjmec08zM5VUG8AHfRf9c6VDqgwNAgBG9vzwgW3F0khP2+UvCLwFsisNoCvDwjr9i4gfbk7nhwLSMtvlALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHBJEj/iA==",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAm8HDLByInoI8cgnnZwF/xRWQ0ZIVmnovh6glSRUNUfqQgzaGc7urbN8Ej2ncgUStL/qevtfVhJgGmwfcajaZAbhAnW6hqjmec08zM5VUG8AHfRf9c6VDqgwNAgBG9vzwgW3F0khP2+UvCLwFsisNoCvDwjr9i4gfbk7nhwLSMtvlALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHBJEj/iA==",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAm8HDLByInoI8cgnnZwF/xRWQ0ZIVmnovh6glSRUNUfqQgzaGc7urbN8Ej2ncgUStL/qevtfVhJgGmwfcajaZAbhAnW6hqjmec08zM5VUG8AHfRf9c6VDqgwNAgBG9vzwgW3F0khP2+UvCLwFsisNoCvDwjr9i4gfbk7nhwLSMtvlALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHBJEj/iA==",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "message": {
        "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "message": {
        "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
  "id": -576460752303422000,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303422000,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+QEOCwH4hLhAm8HDLByInoI8cgnnZwF/xRWQ0ZIVmnovh6glSRUNUfqQgzaGc7urbN8Ej2ncgUStL/qevtfVhJgGmwfcajaZAbhAnW6hqjmec08zM5VUG8AHfRf9c6VDqgwNAgBG9vzwgW3F0khP2+UvCLwFsisNoCvDwjr9i4gfbk7nhwLSMtvlALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHBJEj/iA=="
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+QEOCwH4hLhAm8HDLByInoI8cgnnZwF/xRWQ0ZIVmnovh6glSRUNUfqQgzaGc7urbN8Ej2ncgUStL/qevtfVhJgGmwfcajaZAbhAnW6hqjmec08zM5VUG8AHfRf9c6VDqgwNAgBG9vzwgW3F0khP2+UvCLwFsisNoCvDwjr9i4gfbk7nhwLSMtvlALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoHBJEj/iA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421999,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421999,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi0XhYEitcEZT2M1QPfKpZ4jcP7D2pjs1fXde7Ut7ENSAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyvesWN4=",
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
  "id": -576460752303421998,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED+/yU3zHnQWD/b5VDY0BicIm3DaU/wyc3ySgV2pMcGKQAOZaGEz3iy7lcSUCOYJyGjPRk3kwzKZfqoUeYrcgMGuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqgwLWz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421998,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+JALAfhCuED+/yU3zHnQWD/b5VDY0BicIm3DaU/wyc3ySgV2pMcGKQAOZaGEz3iy7lcSUCOYJyGjPRk3kwzKZfqoUeYrcgMGuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqgwLWz",
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
  "id": -576460752303421997,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEByv6zeAbrodu6qCwO/4xI6iq5RwZlVfpzNlJantb2Mm6sUxk8nBFNY4Wz93KhXx1/RC6W6azvRDBbTC9JkJBwKuED+/yU3zHnQWD/b5VDY0BicIm3DaU/wyc3ySgV2pMcGKQAOZaGEz3iy7lcSUCOYJyGjPRk3kwzKZfqoUeYrcgMGuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrZ9IFF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421997,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+NILAfiEuEByv6zeAbrodu6qCwO/4xI6iq5RwZlVfpzNlJantb2Mm6sUxk8nBFNY4Wz93KhXx1/RC6W6azvRDBbTC9JkJBwKuED+/yU3zHnQWD/b5VDY0BicIm3DaU/wyc3ySgV2pMcGKQAOZaGEz3iy7lcSUCOYJyGjPRk3kwzKZfqoUeYrcgMGuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrZ9IFF"
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+NILAfiEuEByv6zeAbrodu6qCwO/4xI6iq5RwZlVfpzNlJantb2Mm6sUxk8nBFNY4Wz93KhXx1/RC6W6azvRDBbTC9JkJBwKuED+/yU3zHnQWD/b5VDY0BicIm3DaU/wyc3ySgV2pMcGKQAOZaGEz3iy7lcSUCOYJyGjPRk3kwzKZfqoUeYrcgMGuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrZ9IFF"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421996,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421996,
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
  "id": -576460752303421995,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421995,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEByv6zeAbrodu6qCwO/4xI6iq5RwZlVfpzNlJantb2Mm6sUxk8nBFNY4Wz93KhXx1/RC6W6azvRDBbTC9JkJBwKuED+/yU3zHnQWD/b5VDY0BicIm3DaU/wyc3ySgV2pMcGKQAOZaGEz3iy7lcSUCOYJyGjPRk3kwzKZfqoUeYrcgMGuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrZ9IFF",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421994,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421994,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi0XhYEitcEZT2M1QPfKpZ4jcP7D2pjs1fXde7Ut7ENSA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmVHpus=",
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
  "id": -576460752303421993,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBm49wDZyAaa10n9r+wzIe6DGN57yGLm0/jFXhQPLHjJn+iAMYWh9eVvLlFxgHrL1REqGFROkD58k6znBfPhCEFuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaVE4GQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421993,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBm49wDZyAaa10n9r+wzIe6DGN57yGLm0/jFXhQPLHjJn+iAMYWh9eVvLlFxgHrL1REqGFROkD58k6znBfPhCEFuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaVE4GQ",
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
  "id": -576460752303421992,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBm49wDZyAaa10n9r+wzIe6DGN57yGLm0/jFXhQPLHjJn+iAMYWh9eVvLlFxgHrL1REqGFROkD58k6znBfPhCEFuEDBWuwDx7NJygYKHjZno50Wg2mPTrnaFr/FeAz0nBp4tIuscJn7g36HmmeX09dz+5v7Nqt4obHrsJ651VJPNrQJuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbYamnO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421992,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+NILAfiEuEBm49wDZyAaa10n9r+wzIe6DGN57yGLm0/jFXhQPLHjJn+iAMYWh9eVvLlFxgHrL1REqGFROkD58k6znBfPhCEFuEDBWuwDx7NJygYKHjZno50Wg2mPTrnaFr/FeAz0nBp4tIuscJn7g36HmmeX09dz+5v7Nqt4obHrsJ651VJPNrQJuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbYamnO"
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+NILAfiEuEBm49wDZyAaa10n9r+wzIe6DGN57yGLm0/jFXhQPLHjJn+iAMYWh9eVvLlFxgHrL1REqGFROkD58k6znBfPhCEFuEDBWuwDx7NJygYKHjZno50Wg2mPTrnaFr/FeAz0nBp4tIuscJn7g36HmmeX09dz+5v7Nqt4obHrsJ651VJPNrQJuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbYamnO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421991,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421991,
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
  "id": -576460752303421990,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421990,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBm49wDZyAaa10n9r+wzIe6DGN57yGLm0/jFXhQPLHjJn+iAMYWh9eVvLlFxgHrL1REqGFROkD58k6znBfPhCEFuEDBWuwDx7NJygYKHjZno50Wg2mPTrnaFr/FeAz0nBp4tIuscJn7g36HmmeX09dz+5v7Nqt4obHrsJ651VJPNrQJuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbYamnO",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421989,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421989,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBm49wDZyAaa10n9r+wzIe6DGN57yGLm0/jFXhQPLHjJn+iAMYWh9eVvLlFxgHrL1REqGFROkD58k6znBfPhCEFuEDBWuwDx7NJygYKHjZno50Wg2mPTrnaFr/FeAz0nBp4tIuscJn7g36HmmeX09dz+5v7Nqt4obHrsJ651VJPNrQJuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbYamnO",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421988,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421988,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi0XhYEitcEZT2M1QPfKpZ4jcP7D2pjs1fXde7Ut7ENSBKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCypR9W0Q=",
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
  "id": -576460752303421987,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEADqTJqrBiTo2cND9YR9D/xwMphCIps94w/HWw8x4lwd9v5ZK6mP3YbsAr3qHiV0mB9agsuxfPRpPDMbYkjbqEBuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsooGnMV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421987,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+JALAfhCuEADqTJqrBiTo2cND9YR9D/xwMphCIps94w/HWw8x4lwd9v5ZK6mP3YbsAr3qHiV0mB9agsuxfPRpPDMbYkjbqEBuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsooGnMV",
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
  "id": -576460752303421986,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEADqTJqrBiTo2cND9YR9D/xwMphCIps94w/HWw8x4lwd9v5ZK6mP3YbsAr3qHiV0mB9agsuxfPRpPDMbYkjbqEBuEDQOi1zFuxdnH9OKxz0CsVDqVUhgDhoabjiwUm6XMPhOBDGkpY6p335BMfaQjQm4C/XdnPE5S2JduhqvgYKEegAuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqEKVQP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421986,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+NILAfiEuEADqTJqrBiTo2cND9YR9D/xwMphCIps94w/HWw8x4lwd9v5ZK6mP3YbsAr3qHiV0mB9agsuxfPRpPDMbYkjbqEBuEDQOi1zFuxdnH9OKxz0CsVDqVUhgDhoabjiwUm6XMPhOBDGkpY6p335BMfaQjQm4C/XdnPE5S2JduhqvgYKEegAuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqEKVQP"
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+NILAfiEuEADqTJqrBiTo2cND9YR9D/xwMphCIps94w/HWw8x4lwd9v5ZK6mP3YbsAr3qHiV0mB9agsuxfPRpPDMbYkjbqEBuEDQOi1zFuxdnH9OKxz0CsVDqVUhgDhoabjiwUm6XMPhOBDGkpY6p335BMfaQjQm4C/XdnPE5S2JduhqvgYKEegAuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqEKVQP"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421985,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421985,
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
  "id": -576460752303421984,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421984,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEADqTJqrBiTo2cND9YR9D/xwMphCIps94w/HWw8x4lwd9v5ZK6mP3YbsAr3qHiV0mB9agsuxfPRpPDMbYkjbqEBuEDQOi1zFuxdnH9OKxz0CsVDqVUhgDhoabjiwUm6XMPhOBDGkpY6p335BMfaQjQm4C/XdnPE5S2JduhqvgYKEegAuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqEKVQP",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421983,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421983,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi0XhYEitcEZT2M1QPfKpZ4jcP7D2pjs1fXde7Ut7ENSBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rk5pk8A=",
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
  "id": -576460752303421982,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDds5cjsUaisvkYSXyGckxvn0oaJ/5P+FWVRn0vzCDrIp6XCAxozzSsnzVGRJg6bAEvLe64L1zqdUplRLIViPkKuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZJfMCb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421982,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDds5cjsUaisvkYSXyGckxvn0oaJ/5P+FWVRn0vzCDrIp6XCAxozzSsnzVGRJg6bAEvLe64L1zqdUplRLIViPkKuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZJfMCb",
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
  "id": -576460752303421981,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDNQx9RpBI6i3hJHPhCEVZZhbiNkWdaOpsKPF5ByE4joBAmxmPGjGlmCOUx8R1Ob/eHU0/o6zDCjGFNMSft+l0MuEDds5cjsUaisvkYSXyGckxvn0oaJ/5P+FWVRn0vzCDrIp6XCAxozzSsnzVGRJg6bAEvLe64L1zqdUplRLIViPkKuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbHcy0r"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421981,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+NILAfiEuEDNQx9RpBI6i3hJHPhCEVZZhbiNkWdaOpsKPF5ByE4joBAmxmPGjGlmCOUx8R1Ob/eHU0/o6zDCjGFNMSft+l0MuEDds5cjsUaisvkYSXyGckxvn0oaJ/5P+FWVRn0vzCDrIp6XCAxozzSsnzVGRJg6bAEvLe64L1zqdUplRLIViPkKuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbHcy0r"
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "state": "tx_+NILAfiEuEDNQx9RpBI6i3hJHPhCEVZZhbiNkWdaOpsKPF5ByE4joBAmxmPGjGlmCOUx8R1Ob/eHU0/o6zDCjGFNMSft+l0MuEDds5cjsUaisvkYSXyGckxvn0oaJ/5P+FWVRn0vzCDrIp6XCAxozzSsnzVGRJg6bAEvLe64L1zqdUplRLIViPkKuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbHcy0r"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421980,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421980,
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
  "id": -576460752303421979,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421979,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDNQx9RpBI6i3hJHPhCEVZZhbiNkWdaOpsKPF5ByE4joBAmxmPGjGlmCOUx8R1Ob/eHU0/o6zDCjGFNMSft+l0MuEDds5cjsUaisvkYSXyGckxvn0oaJ/5P+FWVRn0vzCDrIp6XCAxozzSsnzVGRJg6bAEvLe64L1zqdUplRLIViPkKuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbHcy0r",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEDNQx9RpBI6i3hJHPhCEVZZhbiNkWdaOpsKPF5ByE4joBAmxmPGjGlmCOUx8R1Ob/eHU0/o6zDCjGFNMSft+l0MuEDds5cjsUaisvkYSXyGckxvn0oaJ/5P+FWVRn0vzCDrIp6XCAxozzSsnzVGRJg6bAEvLe64L1zqdUplRLIViPkKuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbHcy0r",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEDNQx9RpBI6i3hJHPhCEVZZhbiNkWdaOpsKPF5ByE4joBAmxmPGjGlmCOUx8R1Ob/eHU0/o6zDCjGFNMSft+l0MuEDds5cjsUaisvkYSXyGckxvn0oaJ/5P+FWVRn0vzCDrIp6XCAxozzSsnzVGRJg6bAEvLe64L1zqdUplRLIViPkKuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbHcy0r",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBi0XhYEitcEZT2M1QPfKpZ4jcP7D2pjs1fXde7Ut7ENSoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEDNQx9RpBI6i3hJHPhCEVZZhbiNkWdaOpsKPF5ByE4joBAmxmPGjGlmCOUx8R1Ob/eHU0/o6zDCjGFNMSft+l0MuEDds5cjsUaisvkYSXyGckxvn0oaJ/5P+FWVRn0vzCDrIp6XCAxozzSsnzVGRJg6bAEvLe64L1zqdUplRLIViPkKuEj4RjkCoQYtF4WBIrXBGU9jNUD3yqWeI3D+w9qY7NX13Xu1LexDUgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGR7ISegAQ/GQV6k=",
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
  "method": "channels.slash_sign",
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
  "id": -576460752303421978,
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421978,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421977,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
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
  "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
  "id": -576460752303421977,
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
    "channel_id": "ch_Lrp59R5KQVzcNogBvghUPRYzRyauWqxA81LzmiVCXFF18iKU6",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
