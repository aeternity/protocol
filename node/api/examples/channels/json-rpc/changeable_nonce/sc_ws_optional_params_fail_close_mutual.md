
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
      "fsm_id": "ba_le6qGCBkBfi1C8CSvLTdB324NXrcv3SWwI5coyXja4iyKAOd"
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
      "fsm_id": "ba_Q9dhB1TMk77QSLEeJyJvcwUZ7yvxBQ9EhudEq9pG2/TMNqmA"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBpdjIQNE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422215,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBZ7quU527ZXtVGI+7QQ4D4pfdfW/HSN2xwOkHLMU3FUD+EmQgD/CGTJusjMA4Dd6n9+2C+PlCXSSPqDDKDO7gGuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgaW5WcfX"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422215,
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_Q9dhB1TMk77QSLEeJyJvcwUZ7yvxBQ9EhudEq9pG2/TMNqmA"
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEBZ7quU527ZXtVGI+7QQ4D4pfdfW/HSN2xwOkHLMU3FUD+EmQgD/CGTJusjMA4Dd6n9+2C+PlCXSSPqDDKDO7gGuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgaW5WcfX",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422214,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAFPZDFIzUoX2MS7Cp0MPJGhD5lqZkOAd6b3NI8RkP3N8vUBDojdpLjxLChvhebUUq5D97/qwhc+P6/4+DYOTRA7hAWe6rlOdu2V7VRiPu0EOA+KX3X1vx0jdscDpByzFNxVA/hJkIA/whkybrIzAOA3ep/ftgvj5Ql0kj6gwygzu4BriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGlbx17og=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
  "id": -576460752303422214,
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAFPZDFIzUoX2MS7Cp0MPJGhD5lqZkOAd6b3NI8RkP3N8vUBDojdpLjxLChvhebUUq5D97/qwhc+P6/4+DYOTRA7hAWe6rlOdu2V7VRiPu0EOA+KX3X1vx0jdscDpByzFNxVA/hJkIA/whkybrIzAOA3ep/ftgvj5Ql0kj6gwygzu4BriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGlbx17og==",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_le6qGCBkBfi1C8CSvLTdB324NXrcv3SWwI5coyXja4iyKAOd"
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAFPZDFIzUoX2MS7Cp0MPJGhD5lqZkOAd6b3NI8RkP3N8vUBDojdpLjxLChvhebUUq5D97/qwhc+P6/4+DYOTRA7hAWe6rlOdu2V7VRiPu0EOA+KX3X1vx0jdscDpByzFNxVA/hJkIA/whkybrIzAOA3ep/ftgvj5Ql0kj6gwygzu4BriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGlbx17og==",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAFPZDFIzUoX2MS7Cp0MPJGhD5lqZkOAd6b3NI8RkP3N8vUBDojdpLjxLChvhebUUq5D97/qwhc+P6/4+DYOTRA7hAWe6rlOdu2V7VRiPu0EOA+KX3X1vx0jdscDpByzFNxVA/hJkIA/whkybrIzAOA3ep/ftgvj5Ql0kj6gwygzu4BriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGlbx17og==",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAFPZDFIzUoX2MS7Cp0MPJGhD5lqZkOAd6b3NI8RkP3N8vUBDojdpLjxLChvhebUUq5D97/qwhc+P6/4+DYOTRA7hAWe6rlOdu2V7VRiPu0EOA+KX3X1vx0jdscDpByzFNxVA/hJkIA/whkybrIzAOA3ep/ftgvj5Ql0kj6gwygzu4BriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGlbx17og==",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "message": {
        "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "message": {
        "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
  "id": -576460752303422213,
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
  "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
  "id": -576460752303422213,
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "state": "tx_+QEOCwH4hLhAFPZDFIzUoX2MS7Cp0MPJGhD5lqZkOAd6b3NI8RkP3N8vUBDojdpLjxLChvhebUUq5D97/qwhc+P6/4+DYOTRA7hAWe6rlOdu2V7VRiPu0EOA+KX3X1vx0jdscDpByzFNxVA/hJkIA/whkybrIzAOA3ep/ftgvj5Ql0kj6gwygzu4BriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGlbx17og=="
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "state": "tx_+QEOCwH4hLhAFPZDFIzUoX2MS7Cp0MPJGhD5lqZkOAd6b3NI8RkP3N8vUBDojdpLjxLChvhebUUq5D97/qwhc+P6/4+DYOTRA7hAWe6rlOdu2V7VRiPu0EOA+KX3X1vx0jdscDpByzFNxVA/hJkIA/whkybrIzAOA3ep/ftgvj5Ql0kj6gwygzu4BriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGlbx17og=="
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
  "params": {
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "signed_tx": "tx_+GcLAcC4YvhgNQGhBpy+4gQs34Iqbg6jg5taOb3DexI24D0RIQN4YLHUx2rOoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3872/H/+GHKrSZ0ABAIYPbM7GgACDEtaHFii3tQ==",
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
  "method": "channels.shutdown_sign",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBpy+4gQs34Iqbg6jg5taOb3DexI24D0RIQN4YLHUx2rOoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBpmGnPZA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422212,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEB/GR6j7hJlgnqNFI92E1jKMA+8eQmsyHrtWoMc0jgtuATzfSf5klfIivPUjmXAZ2qpt4wcZsq4jnwAr6Ch7r8NuGD4XjUBoQacvuIELN+CKm4Oo4ObWjm9w3sSNuA9ESEDeGCx1MdqzqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgabpQQcC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
  "id": -576460752303422212,
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEB/GR6j7hJlgnqNFI92E1jKMA+8eQmsyHrtWoMc0jgtuATzfSf5klfIivPUjmXAZ2qpt4wcZsq4jnwAr6Ch7r8NuGD4XjUBoQacvuIELN+CKm4Oo4ObWjm9w3sSNuA9ESEDeGCx1MdqzqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgabpQQcC",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422211,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEB/GR6j7hJlgnqNFI92E1jKMA+8eQmsyHrtWoMc0jgtuATzfSf5klfIivPUjmXAZ2qpt4wcZsq4jnwAr6Ch7r8NuEB/0Bs/BQDl5gumPEwkEJmVRzIE8I7PkeDgBsVuo7DhMu31HthQZEYelTnwsw6Jd3ktkvOTHhXCmLHy5nQqemgCuGD4XjUBoQacvuIELN+CKm4Oo4ObWjm9w3sSNuA9ESEDeGCx1MdqzqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgabO1d5H"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
  "id": -576460752303422211,
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEB/GR6j7hJlgnqNFI92E1jKMA+8eQmsyHrtWoMc0jgtuATzfSf5klfIivPUjmXAZ2qpt4wcZsq4jnwAr6Ch7r8NuEB/0Bs/BQDl5gumPEwkEJmVRzIE8I7PkeDgBsVuo7DhMu31HthQZEYelTnwsw6Jd3ktkvOTHhXCmLHy5nQqemgCuGD4XjUBoQacvuIELN+CKm4Oo4ObWjm9w3sSNuA9ESEDeGCx1MdqzqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgabO1d5H",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEB/GR6j7hJlgnqNFI92E1jKMA+8eQmsyHrtWoMc0jgtuATzfSf5klfIivPUjmXAZ2qpt4wcZsq4jnwAr6Ch7r8NuEB/0Bs/BQDl5gumPEwkEJmVRzIE8I7PkeDgBsVuo7DhMu31HthQZEYelTnwsw6Jd3ktkvOTHhXCmLHy5nQqemgCuGD4XjUBoQacvuIELN+CKm4Oo4ObWjm9w3sSNuA9ESEDeGCx1MdqzqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgabO1d5H",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEB/GR6j7hJlgnqNFI92E1jKMA+8eQmsyHrtWoMc0jgtuATzfSf5klfIivPUjmXAZ2qpt4wcZsq4jnwAr6Ch7r8NuEB/0Bs/BQDl5gumPEwkEJmVRzIE8I7PkeDgBsVuo7DhMu31HthQZEYelTnwsw6Jd3ktkvOTHhXCmLHy5nQqemgCuGD4XjUBoQacvuIELN+CKm4Oo4ObWjm9w3sSNuA9ESEDeGCx1MdqzqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgabO1d5H",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEB/GR6j7hJlgnqNFI92E1jKMA+8eQmsyHrtWoMc0jgtuATzfSf5klfIivPUjmXAZ2qpt4wcZsq4jnwAr6Ch7r8NuEB/0Bs/BQDl5gumPEwkEJmVRzIE8I7PkeDgBsVuo7DhMu31HthQZEYelTnwsw6Jd3ktkvOTHhXCmLHy5nQqemgCuGD4XjUBoQacvuIELN+CKm4Oo4ObWjm9w3sSNuA9ESEDeGCx1MdqzqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgabO1d5H",
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
      "fsm_id": "ba_ygtrf5ZH+99ALOmjvYRF3+EfiEMgBEbLZs49bJ2iBRraQ5mg"
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
      "fsm_id": "ba_UFdYOWnbERySKkp9Nfp5NNE8cL4gygJPyEX/TD1xCkZ/avmw"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBp4Ktlvw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422210,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEDXlfmBI8oWpQjDVgNEtOpLzaUFQ1nAnebjaoopHjaZob7lwoScrE0nuy+Hioujej9t27WL8syb1uqjNdbGg1sPuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgacqDLDw"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422210,
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_UFdYOWnbERySKkp9Nfp5NNE8cL4gygJPyEX/TD1xCkZ/avmw"
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEDXlfmBI8oWpQjDVgNEtOpLzaUFQ1nAnebjaoopHjaZob7lwoScrE0nuy+Hioujej9t27WL8syb1uqjNdbGg1sPuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgacqDLDw",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422209,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAqXvOhp+kaWJANxI5NPpS1b0eeAVV+U16z/SeGxHmPBYM/FvlO7hBO2PN1m3cFQeq7ESfHl+vqxtPdKs9EDfjDLhA15X5gSPKFqUIw1YDRLTqS82lBUNZwJ3m42qKKR42maG+5cKEnKxNJ7svh4qLo3o/bdu1i/LMm9bqozXWxoNbD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGncQvomw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
  "id": -576460752303422209,
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAqXvOhp+kaWJANxI5NPpS1b0eeAVV+U16z/SeGxHmPBYM/FvlO7hBO2PN1m3cFQeq7ESfHl+vqxtPdKs9EDfjDLhA15X5gSPKFqUIw1YDRLTqS82lBUNZwJ3m42qKKR42maG+5cKEnKxNJ7svh4qLo3o/bdu1i/LMm9bqozXWxoNbD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGncQvomw==",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_ygtrf5ZH+99ALOmjvYRF3+EfiEMgBEbLZs49bJ2iBRraQ5mg"
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAqXvOhp+kaWJANxI5NPpS1b0eeAVV+U16z/SeGxHmPBYM/FvlO7hBO2PN1m3cFQeq7ESfHl+vqxtPdKs9EDfjDLhA15X5gSPKFqUIw1YDRLTqS82lBUNZwJ3m42qKKR42maG+5cKEnKxNJ7svh4qLo3o/bdu1i/LMm9bqozXWxoNbD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGncQvomw==",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAqXvOhp+kaWJANxI5NPpS1b0eeAVV+U16z/SeGxHmPBYM/FvlO7hBO2PN1m3cFQeq7ESfHl+vqxtPdKs9EDfjDLhA15X5gSPKFqUIw1YDRLTqS82lBUNZwJ3m42qKKR42maG+5cKEnKxNJ7svh4qLo3o/bdu1i/LMm9bqozXWxoNbD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGncQvomw==",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAqXvOhp+kaWJANxI5NPpS1b0eeAVV+U16z/SeGxHmPBYM/FvlO7hBO2PN1m3cFQeq7ESfHl+vqxtPdKs9EDfjDLhA15X5gSPKFqUIw1YDRLTqS82lBUNZwJ3m42qKKR42maG+5cKEnKxNJ7svh4qLo3o/bdu1i/LMm9bqozXWxoNbD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGncQvomw==",
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
    "channel_id": "ch_2C2rhd1N31F3zdoVQYVEmiGgmMRm2FUSJL3gfpVHDwo2gjHAyF",
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
  "method": "channels.message",
  "params": {
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "message": {
        "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "message": {
        "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
  "id": -576460752303422208,
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
  "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
  "id": -576460752303422208,
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "state": "tx_+QEOCwH4hLhAqXvOhp+kaWJANxI5NPpS1b0eeAVV+U16z/SeGxHmPBYM/FvlO7hBO2PN1m3cFQeq7ESfHl+vqxtPdKs9EDfjDLhA15X5gSPKFqUIw1YDRLTqS82lBUNZwJ3m42qKKR42maG+5cKEnKxNJ7svh4qLo3o/bdu1i/LMm9bqozXWxoNbD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGncQvomw=="
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "state": "tx_+QEOCwH4hLhAqXvOhp+kaWJANxI5NPpS1b0eeAVV+U16z/SeGxHmPBYM/FvlO7hBO2PN1m3cFQeq7ESfHl+vqxtPdKs9EDfjDLhA15X5gSPKFqUIw1YDRLTqS82lBUNZwJ3m42qKKR42maG+5cKEnKxNJ7svh4qLo3o/bdu1i/LMm9bqozXWxoNbD7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGncQvomw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "signed_tx": "tx_+GcLAcC4YvhgNQGhBgxl6gxI8Rncwz10ao51UWS18dYQ3hK1CJQ1bgqaeRCOoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY3872/H/+GHKrSZ0ABAIYPbM7GgACDEtaHIJgvBA==",
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
  "method": "channels.shutdown_sign",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBgxl6gxI8Rncwz10ao51UWS18dYQ3hK1CJQ1bgqaeRCOoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBqGLKnWo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422207,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEBpkJFX8UXT725MNHijKfyl+xQ2k/c2FXqdTeWGYmPpy4Z/1vHkvtDgFYWzqGWz1KWnJX1Asw539emxpAWg1jAPuGD4XjUBoQYMZeoMSPEZ3MM9dGqOdVFktfHWEN4StQiUNW4KmnkQjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgah9d9B7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
  "id": -576460752303422207,
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEBpkJFX8UXT725MNHijKfyl+xQ2k/c2FXqdTeWGYmPpy4Z/1vHkvtDgFYWzqGWz1KWnJX1Asw539emxpAWg1jAPuGD4XjUBoQYMZeoMSPEZ3MM9dGqOdVFktfHWEN4StQiUNW4KmnkQjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgah9d9B7",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422206,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEBpkJFX8UXT725MNHijKfyl+xQ2k/c2FXqdTeWGYmPpy4Z/1vHkvtDgFYWzqGWz1KWnJX1Asw539emxpAWg1jAPuEC7An6f5NslWu+55DEJlwbpcj9jOQKAFN+B0hyePmnEpjS4Hf57Kox0X/UNw9OyugQ9Ow+9RBmnSPNOn4tRUkEBuGD4XjUBoQYMZeoMSPEZ3MM9dGqOdVFktfHWEN4StQiUNW4KmnkQjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaj2CBDC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
  "id": -576460752303422206,
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEBpkJFX8UXT725MNHijKfyl+xQ2k/c2FXqdTeWGYmPpy4Z/1vHkvtDgFYWzqGWz1KWnJX1Asw539emxpAWg1jAPuEC7An6f5NslWu+55DEJlwbpcj9jOQKAFN+B0hyePmnEpjS4Hf57Kox0X/UNw9OyugQ9Ow+9RBmnSPNOn4tRUkEBuGD4XjUBoQYMZeoMSPEZ3MM9dGqOdVFktfHWEN4StQiUNW4KmnkQjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaj2CBDC",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEBpkJFX8UXT725MNHijKfyl+xQ2k/c2FXqdTeWGYmPpy4Z/1vHkvtDgFYWzqGWz1KWnJX1Asw539emxpAWg1jAPuEC7An6f5NslWu+55DEJlwbpcj9jOQKAFN+B0hyePmnEpjS4Hf57Kox0X/UNw9OyugQ9Ow+9RBmnSPNOn4tRUkEBuGD4XjUBoQYMZeoMSPEZ3MM9dGqOdVFktfHWEN4StQiUNW4KmnkQjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaj2CBDC",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEBpkJFX8UXT725MNHijKfyl+xQ2k/c2FXqdTeWGYmPpy4Z/1vHkvtDgFYWzqGWz1KWnJX1Asw539emxpAWg1jAPuEC7An6f5NslWu+55DEJlwbpcj9jOQKAFN+B0hyePmnEpjS4Hf57Kox0X/UNw9OyugQ9Ow+9RBmnSPNOn4tRUkEBuGD4XjUBoQYMZeoMSPEZ3MM9dGqOdVFktfHWEN4StQiUNW4KmnkQjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaj2CBDC",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEBpkJFX8UXT725MNHijKfyl+xQ2k/c2FXqdTeWGYmPpy4Z/1vHkvtDgFYWzqGWz1KWnJX1Asw539emxpAWg1jAPuEC7An6f5NslWu+55DEJlwbpcj9jOQKAFN+B0hyePmnEpjS4Hf57Kox0X/UNw9OyugQ9Ow+9RBmnSPNOn4tRUkEBuGD4XjUBoQYMZeoMSPEZ3MM9dGqOdVFktfHWEN4StQiUNW4KmnkQjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaj2CBDC",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
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
    "channel_id": "ch_6ThBt2UCMFuHghj84iPGNBQ2k54iPRfMAZFAEQcHDwfSo5aYE",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
