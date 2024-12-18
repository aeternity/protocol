
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
      "fsm_id": "ba_Bhq7Pszb0ZU9tofONNxL7NGx4Ctf7EckghIWMQQEMNAVt1U9"
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
      "fsm_id": "ba_3t97UcQw2grNid5Jj3/7pCO0+No4r8XOYy/fmtPSuHd4O08X"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYE8cfmAw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423426,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDuiT/xZCHvu3ZraLrQGbd3JPVDxOEASEdtEMhEETdJmy+w4Y+uNMXzr9OQJNfkoXHIPWwf+PGrEkmdj4HxQ24MuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGBE3Oi9k="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423426,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_3t97UcQw2grNid5Jj3/7pCO0+No4r8XOYy/fmtPSuHd4O08X"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDuiT/xZCHvu3ZraLrQGbd3JPVDxOEASEdtEMhEETdJmy+w4Y+uNMXzr9OQJNfkoXHIPWwf+PGrEkmdj4HxQ24MuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGBE3Oi9k=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423425,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhA7ok/8WQh77t2a2i60Bm3dyT1Q8ThAEhHbRDIRBE3SZsvsOGPrjTF86/TkCTX5KFxyD1sH/jxqxJJnY+B8UNuDLhA9ocS6Nw5bIMz/Sj+6Az2lCnBk6sSwJCHsWexMIUCLlT9lcYYl0QezSlFTte2hcSumgODMF9B8ymvgin8fLEmD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgSByA06"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423425,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhA7ok/8WQh77t2a2i60Bm3dyT1Q8ThAEhHbRDIRBE3SZsvsOGPrjTF86/TkCTX5KFxyD1sH/jxqxJJnY+B8UNuDLhA9ocS6Nw5bIMz/Sj+6Az2lCnBk6sSwJCHsWexMIUCLlT9lcYYl0QezSlFTte2hcSumgODMF9B8ymvgin8fLEmD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgSByA06",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Bhq7Pszb0ZU9tofONNxL7NGx4Ctf7EckghIWMQQEMNAVt1U9"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhA7ok/8WQh77t2a2i60Bm3dyT1Q8ThAEhHbRDIRBE3SZsvsOGPrjTF86/TkCTX5KFxyD1sH/jxqxJJnY+B8UNuDLhA9ocS6Nw5bIMz/Sj+6Az2lCnBk6sSwJCHsWexMIUCLlT9lcYYl0QezSlFTte2hcSumgODMF9B8ymvgin8fLEmD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgSByA06",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA7ok/8WQh77t2a2i60Bm3dyT1Q8ThAEhHbRDIRBE3SZsvsOGPrjTF86/TkCTX5KFxyD1sH/jxqxJJnY+B8UNuDLhA9ocS6Nw5bIMz/Sj+6Az2lCnBk6sSwJCHsWexMIUCLlT9lcYYl0QezSlFTte2hcSumgODMF9B8ymvgin8fLEmD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgSByA06",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA7ok/8WQh77t2a2i60Bm3dyT1Q8ThAEhHbRDIRBE3SZsvsOGPrjTF86/TkCTX5KFxyD1sH/jxqxJJnY+B8UNuDLhA9ocS6Nw5bIMz/Sj+6Az2lCnBk6sSwJCHsWexMIUCLlT9lcYYl0QezSlFTte2hcSumgODMF9B8ymvgin8fLEmD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgSByA06",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "message": {
        "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "message": {
        "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
  "id": -576460752303423424,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423424,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+QENCwH4hLhA7ok/8WQh77t2a2i60Bm3dyT1Q8ThAEhHbRDIRBE3SZsvsOGPrjTF86/TkCTX5KFxyD1sH/jxqxJJnY+B8UNuDLhA9ocS6Nw5bIMz/Sj+6Az2lCnBk6sSwJCHsWexMIUCLlT9lcYYl0QezSlFTte2hcSumgODMF9B8ymvgin8fLEmD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgSByA06"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+QENCwH4hLhA7ok/8WQh77t2a2i60Bm3dyT1Q8ThAEhHbRDIRBE3SZsvsOGPrjTF86/TkCTX5KFxyD1sH/jxqxJJnY+B8UNuDLhA9ocS6Nw5bIMz/Sj+6Az2lCnBk6sSwJCHsWexMIUCLlT9lcYYl0QezSlFTte2hcSumgODMF9B8ymvgin8fLEmD7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgSByA06"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423423,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423423,
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
    "amount": "1",
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": 17,
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "meta": 17,
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvQ/ajUcjdf3iftCV0Dp7oEusxAKHVf2lLVIBNIA0rXAAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyim3+0E=",
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
  "id": -576460752303423422,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBrZRMhK0+0afgmD24uIefMIxmAFSyD6vevgwG3TMd31uFuXan5XLfLqc0JU4N6RBjyN2QT6XP6kmxILk5+jkECuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrlgOor"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423422,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBrZRMhK0+0afgmD24uIefMIxmAFSyD6vevgwG3TMd31uFuXan5XLfLqc0JU4N6RBjyN2QT6XP6kmxILk5+jkECuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrlgOor",
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
  "id": -576460752303423421,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBrZRMhK0+0afgmD24uIefMIxmAFSyD6vevgwG3TMd31uFuXan5XLfLqc0JU4N6RBjyN2QT6XP6kmxILk5+jkECuEChzfjfeOa1QjGtz6K5JjTyeklsG5BBYDeqEo+VOt4tm+WSJUFaZUBuhl1mHjz4r3vLuKROOJ13wrG/aNjsqg0GuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsquLevT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423421,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEBrZRMhK0+0afgmD24uIefMIxmAFSyD6vevgwG3TMd31uFuXan5XLfLqc0JU4N6RBjyN2QT6XP6kmxILk5+jkECuEChzfjfeOa1QjGtz6K5JjTyeklsG5BBYDeqEo+VOt4tm+WSJUFaZUBuhl1mHjz4r3vLuKROOJ13wrG/aNjsqg0GuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsquLevT"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEBrZRMhK0+0afgmD24uIefMIxmAFSyD6vevgwG3TMd31uFuXan5XLfLqc0JU4N6RBjyN2QT6XP6kmxILk5+jkECuEChzfjfeOa1QjGtz6K5JjTyeklsG5BBYDeqEo+VOt4tm+WSJUFaZUBuhl1mHjz4r3vLuKROOJ13wrG/aNjsqg0GuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsquLevT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423420,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423420,
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
  "id": -576460752303423419,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423419,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBrZRMhK0+0afgmD24uIefMIxmAFSyD6vevgwG3TMd31uFuXan5XLfLqc0JU4N6RBjyN2QT6XP6kmxILk5+jkECuEChzfjfeOa1QjGtz6K5JjTyeklsG5BBYDeqEo+VOt4tm+WSJUFaZUBuhl1mHjz4r3vLuKROOJ13wrG/aNjsqg0GuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsquLevT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423418,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423418,
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
    "amount": "1",
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": 17,
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": 17,
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvQ/ajUcjdf3iftCV0Dp7oEusxAKHVf2lLVIBNIA0rXAA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rt4kt58=",
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
  "id": -576460752303423417,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDjDnmUXcG3cSHU1ameB3eU7Z8t6wgAoc/UltWYNocjfoFJfICedpx7uw+ww1YBFjYbIjK2LP+kBtCawXW4YWoCuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbA8QYG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423417,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDjDnmUXcG3cSHU1ameB3eU7Z8t6wgAoc/UltWYNocjfoFJfICedpx7uw+ww1YBFjYbIjK2LP+kBtCawXW4YWoCuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbA8QYG",
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
  "id": -576460752303423416,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAqtV3uf7ijbjcEgjv2/nPAF/M17Xl6uRsOGoaoAEokg1B0jpAmWqzFqPQP2XWsxxUr5xrAr8qHlkaU/iBktzgGuEDjDnmUXcG3cSHU1ameB3eU7Z8t6wgAoc/UltWYNocjfoFJfICedpx7uw+ww1YBFjYbIjK2LP+kBtCawXW4YWoCuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYvEKDf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423416,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEAqtV3uf7ijbjcEgjv2/nPAF/M17Xl6uRsOGoaoAEokg1B0jpAmWqzFqPQP2XWsxxUr5xrAr8qHlkaU/iBktzgGuEDjDnmUXcG3cSHU1ameB3eU7Z8t6wgAoc/UltWYNocjfoFJfICedpx7uw+ww1YBFjYbIjK2LP+kBtCawXW4YWoCuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYvEKDf"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEAqtV3uf7ijbjcEgjv2/nPAF/M17Xl6uRsOGoaoAEokg1B0jpAmWqzFqPQP2XWsxxUr5xrAr8qHlkaU/iBktzgGuEDjDnmUXcG3cSHU1ameB3eU7Z8t6wgAoc/UltWYNocjfoFJfICedpx7uw+ww1YBFjYbIjK2LP+kBtCawXW4YWoCuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYvEKDf"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423415,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423415,
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
  "id": -576460752303423414,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423414,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAqtV3uf7ijbjcEgjv2/nPAF/M17Xl6uRsOGoaoAEokg1B0jpAmWqzFqPQP2XWsxxUr5xrAr8qHlkaU/iBktzgGuEDjDnmUXcG3cSHU1ameB3eU7Z8t6wgAoc/UltWYNocjfoFJfICedpx7uw+ww1YBFjYbIjK2LP+kBtCawXW4YWoCuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYvEKDf",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423413,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423413,
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": 17,
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": 17,
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvQ/ajUcjdf3iftCV0Dp7oEusxAKHVf2lLVIBNIA0rXABKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYJV1DvY=",
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
  "id": -576460752303423412,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDZPoB+9Ss7rNsp+4+6NxUdkET5ca4A0sTiVShqVTqxpy3Zvj1EG09a5dszlu7g3KGv2lZ8Y9IGYnbnNSVtWzAOuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDkFYyP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423412,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDZPoB+9Ss7rNsp+4+6NxUdkET5ca4A0sTiVShqVTqxpy3Zvj1EG09a5dszlu7g3KGv2lZ8Y9IGYnbnNSVtWzAOuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDkFYyP",
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
  "id": -576460752303423411,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDZPoB+9Ss7rNsp+4+6NxUdkET5ca4A0sTiVShqVTqxpy3Zvj1EG09a5dszlu7g3KGv2lZ8Y9IGYnbnNSVtWzAOuEDlRT5rNV6pV5LLd+8iZK4efCnolPLi0dDI9YZkxn/Uda5KJnPRBJ9DMnWiQqq2YI/8tlBZvpLbvpmn2q3kPGoAuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAxbegE"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423411,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEDZPoB+9Ss7rNsp+4+6NxUdkET5ca4A0sTiVShqVTqxpy3Zvj1EG09a5dszlu7g3KGv2lZ8Y9IGYnbnNSVtWzAOuEDlRT5rNV6pV5LLd+8iZK4efCnolPLi0dDI9YZkxn/Uda5KJnPRBJ9DMnWiQqq2YI/8tlBZvpLbvpmn2q3kPGoAuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAxbegE"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEDZPoB+9Ss7rNsp+4+6NxUdkET5ca4A0sTiVShqVTqxpy3Zvj1EG09a5dszlu7g3KGv2lZ8Y9IGYnbnNSVtWzAOuEDlRT5rNV6pV5LLd+8iZK4efCnolPLi0dDI9YZkxn/Uda5KJnPRBJ9DMnWiQqq2YI/8tlBZvpLbvpmn2q3kPGoAuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAxbegE"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423410,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423410,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000000
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423409,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423409,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDZPoB+9Ss7rNsp+4+6NxUdkET5ca4A0sTiVShqVTqxpy3Zvj1EG09a5dszlu7g3KGv2lZ8Y9IGYnbnNSVtWzAOuEDlRT5rNV6pV5LLd+8iZK4efCnolPLi0dDI9YZkxn/Uda5KJnPRBJ9DMnWiQqq2YI/8tlBZvpLbvpmn2q3kPGoAuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAxbegE",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423408,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423408,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 70000000000000
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000000
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
    "amount": "1",
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": 17,
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "meta": 17,
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvQ/ajUcjdf3iftCV0Dp7oEusxAKHVf2lLVIBNIA0rXABaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RvjJoBw=",
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
  "id": -576460752303423407,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBI0Esbo46gie/vizjVExjQLVC929Vy0fXxLoG07NhpjTmJZWRrVxylKiNEYteG9jT8dXqVHClXm3ek4M2h25sCuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbaFbLA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423407,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBI0Esbo46gie/vizjVExjQLVC929Vy0fXxLoG07NhpjTmJZWRrVxylKiNEYteG9jT8dXqVHClXm3ek4M2h25sCuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbaFbLA",
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
  "id": -576460752303423406,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBI0Esbo46gie/vizjVExjQLVC929Vy0fXxLoG07NhpjTmJZWRrVxylKiNEYteG9jT8dXqVHClXm3ek4M2h25sCuEDeBekkSlyrj87Wb0Ug9sWdQMMU8irUX56+vNXWxq8U4N9m+o/QW33nesW/5Xk9HBNYV3BsfDOVFtmzqVt+mVcOuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaybkCD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423406,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEBI0Esbo46gie/vizjVExjQLVC929Vy0fXxLoG07NhpjTmJZWRrVxylKiNEYteG9jT8dXqVHClXm3ek4M2h25sCuEDeBekkSlyrj87Wb0Ug9sWdQMMU8irUX56+vNXWxq8U4N9m+o/QW33nesW/5Xk9HBNYV3BsfDOVFtmzqVt+mVcOuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaybkCD"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEBI0Esbo46gie/vizjVExjQLVC929Vy0fXxLoG07NhpjTmJZWRrVxylKiNEYteG9jT8dXqVHClXm3ek4M2h25sCuEDeBekkSlyrj87Wb0Ug9sWdQMMU8irUX56+vNXWxq8U4N9m+o/QW33nesW/5Xk9HBNYV3BsfDOVFtmzqVt+mVcOuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaybkCD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423405,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423405,
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
  "id": -576460752303423404,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423404,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBI0Esbo46gie/vizjVExjQLVC929Vy0fXxLoG07NhpjTmJZWRrVxylKiNEYteG9jT8dXqVHClXm3ek4M2h25sCuEDeBekkSlyrj87Wb0Ug9sWdQMMU8irUX56+vNXWxq8U4N9m+o/QW33nesW/5Xk9HBNYV3BsfDOVFtmzqVt+mVcOuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaybkCD",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423403,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423403,
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": 17,
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": 17,
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvQ/ajUcjdf3iftCV0Dp7oEusxAKHVf2lLVIBNIA0rXABqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYMskjdw=",
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
  "id": -576460752303423402,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAuoaE/tmOjM82NkdoW/RsN/c+KHOTqfSbMSy762oJDavPn98IDeTbDrGq1AruEoCTavYsKbP8ka0+4kf8mu5UBuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBbETNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423402,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAuoaE/tmOjM82NkdoW/RsN/c+KHOTqfSbMSy762oJDavPn98IDeTbDrGq1AruEoCTavYsKbP8ka0+4kf8mu5UBuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBbETNb",
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
  "id": -576460752303423401,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAuoaE/tmOjM82NkdoW/RsN/c+KHOTqfSbMSy762oJDavPn98IDeTbDrGq1AruEoCTavYsKbP8ka0+4kf8mu5UBuEBKphIEqGg4ZQUyLI0Qhd358G79vTwYMY9ufgJUwHujEOERfJMqivZ3huSRIxVqliAJ/WmCbk+gJBRiHnlfShQDuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDMFHS5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423401,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEAuoaE/tmOjM82NkdoW/RsN/c+KHOTqfSbMSy762oJDavPn98IDeTbDrGq1AruEoCTavYsKbP8ka0+4kf8mu5UBuEBKphIEqGg4ZQUyLI0Qhd358G79vTwYMY9ufgJUwHujEOERfJMqivZ3huSRIxVqliAJ/WmCbk+gJBRiHnlfShQDuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDMFHS5"
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
    "data": {
      "state": "tx_+NILAfiEuEAuoaE/tmOjM82NkdoW/RsN/c+KHOTqfSbMSy762oJDavPn98IDeTbDrGq1AruEoCTavYsKbP8ka0+4kf8mu5UBuEBKphIEqGg4ZQUyLI0Qhd358G79vTwYMY9ufgJUwHujEOERfJMqivZ3huSRIxVqliAJ/WmCbk+gJBRiHnlfShQDuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDMFHS5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423400,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423400,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000000
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAuoaE/tmOjM82NkdoW/RsN/c+KHOTqfSbMSy762oJDavPn98IDeTbDrGq1AruEoCTavYsKbP8ka0+4kf8mu5UBuEBKphIEqGg4ZQUyLI0Qhd358G79vTwYMY9ufgJUwHujEOERfJMqivZ3huSRIxVqliAJ/WmCbk+gJBRiHnlfShQDuEj4RjkCoQb0P2o1HI3X94n7QldA6e6BLrMQCh1X9pS1SATSANK1wAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDMFHS5",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423398,
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423398,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423397,
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
    "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
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
  "channel_id": "ch_2rZyqt78RMLJX92Ffp4miJySyGfxp3HPGdP41d26wfrVoQP78T",
  "id": -576460752303423397,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
