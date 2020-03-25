
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
      "fsm_id": "ba_eqK+FFIq9XOX/IRDe/RcBmV1EXM1V3xsmh0IQpUW22an6DfO"
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
      "fsm_id": "ba_VgtNnys3vf5Nbl8ahFmGlWUfILGRFz4N0twi87J/ytnOF7Pt"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZKaXEbcA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422593,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDYd3FlNu7dLbgLe2JofI9RZ1lzuH7vlQjUkr7qbpmO/693FG0YvwBxgppX/FsU7znDGZ3uZvXhv/qaUJaKcQQEuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGSrI/Nns="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422593,
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_VgtNnys3vf5Nbl8ahFmGlWUfILGRFz4N0twi87J/ytnOF7Pt"
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDYd3FlNu7dLbgLe2JofI9RZ1lzuH7vlQjUkr7qbpmO/693FG0YvwBxgppX/FsU7znDGZ3uZvXhv/qaUJaKcQQEuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGSrI/Nns=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422592,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAvuNoTEU6gXGSV/qJURHNRPZJ+scfQXvGy6vZe3L5qJ9NKXFFCbKL2AFeidopcl5pETfC3hyEzfBCqruma/TjBrhA2HdxZTbu3S24C3tiaHyPUWdZc7h+75UI1JK+6m6Zjv+vdxRtGL8AcYKaV/xbFO85wxmd7mb14b/6mlCWinEEBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkrMKqJP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
  "id": -576460752303422592,
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAvuNoTEU6gXGSV/qJURHNRPZJ+scfQXvGy6vZe3L5qJ9NKXFFCbKL2AFeidopcl5pETfC3hyEzfBCqruma/TjBrhA2HdxZTbu3S24C3tiaHyPUWdZc7h+75UI1JK+6m6Zjv+vdxRtGL8AcYKaV/xbFO85wxmd7mb14b/6mlCWinEEBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkrMKqJP",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_eqK+FFIq9XOX/IRDe/RcBmV1EXM1V3xsmh0IQpUW22an6DfO"
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAvuNoTEU6gXGSV/qJURHNRPZJ+scfQXvGy6vZe3L5qJ9NKXFFCbKL2AFeidopcl5pETfC3hyEzfBCqruma/TjBrhA2HdxZTbu3S24C3tiaHyPUWdZc7h+75UI1JK+6m6Zjv+vdxRtGL8AcYKaV/xbFO85wxmd7mb14b/6mlCWinEEBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkrMKqJP",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAvuNoTEU6gXGSV/qJURHNRPZJ+scfQXvGy6vZe3L5qJ9NKXFFCbKL2AFeidopcl5pETfC3hyEzfBCqruma/TjBrhA2HdxZTbu3S24C3tiaHyPUWdZc7h+75UI1JK+6m6Zjv+vdxRtGL8AcYKaV/xbFO85wxmd7mb14b/6mlCWinEEBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkrMKqJP",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAvuNoTEU6gXGSV/qJURHNRPZJ+scfQXvGy6vZe3L5qJ9NKXFFCbKL2AFeidopcl5pETfC3hyEzfBCqruma/TjBrhA2HdxZTbu3S24C3tiaHyPUWdZc7h+75UI1JK+6m6Zjv+vdxRtGL8AcYKaV/xbFO85wxmd7mb14b/6mlCWinEEBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkrMKqJP",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "message": {
        "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "message": {
        "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
  "id": -576460752303422591,
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
  "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
  "id": -576460752303422591,
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "state": "tx_+QENCwH4hLhAvuNoTEU6gXGSV/qJURHNRPZJ+scfQXvGy6vZe3L5qJ9NKXFFCbKL2AFeidopcl5pETfC3hyEzfBCqruma/TjBrhA2HdxZTbu3S24C3tiaHyPUWdZc7h+75UI1JK+6m6Zjv+vdxRtGL8AcYKaV/xbFO85wxmd7mb14b/6mlCWinEEBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkrMKqJP"
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "state": "tx_+QENCwH4hLhAvuNoTEU6gXGSV/qJURHNRPZJ+scfQXvGy6vZe3L5qJ9NKXFFCbKL2AFeidopcl5pETfC3hyEzfBCqruma/TjBrhA2HdxZTbu3S24C3tiaHyPUWdZc7h+75UI1JK+6m6Zjv+vdxRtGL8AcYKaV/xbFO85wxmd7mb14b/6mlCWinEEBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkrMKqJP"
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
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBvmNYblAOpNfOryG2HOZSe2D3h8AIwlIpN9f4X/J/gtCoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7sgIAAS7UlTJA=",
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
    "signed_tx": "tx_+QHrCwH4QrhAnebeQMdHi9mXZHs3lj1ltInE9VrvGogj8te9PhXKoD+Hg2qxd6XBjfHvfkva/+w0v0Xg7NHAAX6eJ8kpxPaVCrkBovkBnzYBoQb5jWG5QDqTXzq8hthzmUntg94fACMJSKTfX+F/yf4LQqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAEsoobAj"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAnebeQMdHi9mXZHs3lj1ltInE9VrvGogj8te9PhXKoD+Hg2qxd6XBjfHvfkva/+w0v0Xg7NHAAX6eJ8kpxPaVCrkBovkBnzYBoQb5jWG5QDqTXzq8hthzmUntg94fACMJSKTfX+F/yf4LQqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAEsoobAj",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAnebeQMdHi9mXZHs3lj1ltInE9VrvGogj8te9PhXKoD+Hg2qxd6XBjfHvfkva/+w0v0Xg7NHAAX6eJ8kpxPaVCrkBovkBnzYBoQb5jWG5QDqTXzq8hthzmUntg94fACMJSKTfX+F/yf4LQqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAEsoobAj",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
  "method": "channels.settle",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBvmNYblAOpNfOryG2HOZSe2D3h8AIwlIpN9f4X/J/gtCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIZwSIYbDz8gU1vpHA==",
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
    "signed_tx": "tx_+KcLAfhCuEB6I7dWcCLPbjimX9MXSE4czP+BmNqK97sUr/+kc6isTVU2F+cVqe0PEgY+YSBXzM2qzei9YOhkgfTbY1rXvVAIuF/4XTgBoQb5jWG5QDqTXzq8hthzmUntg94fACMJSKTfX+F/yf4LQqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGcEiGGw8/IP7I0jM="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB6I7dWcCLPbjimX9MXSE4czP+BmNqK97sUr/+kc6isTVU2F+cVqe0PEgY+YSBXzM2qzei9YOhkgfTbY1rXvVAIuF/4XTgBoQb5jWG5QDqTXzq8hthzmUntg94fACMJSKTfX+F/yf4LQqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGcEiGGw8/IP7I0jM=",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB6I7dWcCLPbjimX9MXSE4czP+BmNqK97sUr/+kc6isTVU2F+cVqe0PEgY+YSBXzM2qzei9YOhkgfTbY1rXvVAIuF/4XTgBoQb5jWG5QDqTXzq8hthzmUntg94fACMJSKTfX+F/yf4LQqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGcEiGGw8/IP7I0jM=",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
    "channel_id": "ch_2tuUiXx6zuADNBLR5riWfDQLLtUWtVVGX4GjwRLK8WDfm4mGEa",
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
      "fsm_id": "ba_f4pkHy9o6GY7EEcTHvW95vZwFBLKn1pExH+bZp3hHLNMk/GY"
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
      "fsm_id": "ba_1oTFN87K1Vkcw/s4LmGTMmg0rEKJcUa1OmqzBXqPv2eb2tGj"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZMepcXGA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422590,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEChPLtPC4rrbIeFiGeTQ8M2RKlf7LOyYzf7dAxMuRDuFXTx1b+8JTS+u+lG6EcbCWGCnAch5czHKVFz91RP7kAKuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGTLrDA+A="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422590,
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_1oTFN87K1Vkcw/s4LmGTMmg0rEKJcUa1OmqzBXqPv2eb2tGj"
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEChPLtPC4rrbIeFiGeTQ8M2RKlf7LOyYzf7dAxMuRDuFXTx1b+8JTS+u+lG6EcbCWGCnAch5czHKVFz91RP7kAKuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGTLrDA+A=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422589,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhACSgW7QyS8Yr0TOWYLTqpdv6fZYUnHZHSqmInksMJWpo19LiqHjRvnxRXQ3l5ZWWU1vpsrmGFTKXJRJVaFVNNDLhAoTy7TwuK62yHhYhnk0PDNkSpX+yzsmM3+3QMTLkQ7hV08dW/vCU0vrvpRuhHGwlhgpwHIeXMxylRc/dUT+5ACriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkxBWGnO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
  "id": -576460752303422589,
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhACSgW7QyS8Yr0TOWYLTqpdv6fZYUnHZHSqmInksMJWpo19LiqHjRvnxRXQ3l5ZWWU1vpsrmGFTKXJRJVaFVNNDLhAoTy7TwuK62yHhYhnk0PDNkSpX+yzsmM3+3QMTLkQ7hV08dW/vCU0vrvpRuhHGwlhgpwHIeXMxylRc/dUT+5ACriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkxBWGnO",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_f4pkHy9o6GY7EEcTHvW95vZwFBLKn1pExH+bZp3hHLNMk/GY"
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhACSgW7QyS8Yr0TOWYLTqpdv6fZYUnHZHSqmInksMJWpo19LiqHjRvnxRXQ3l5ZWWU1vpsrmGFTKXJRJVaFVNNDLhAoTy7TwuK62yHhYhnk0PDNkSpX+yzsmM3+3QMTLkQ7hV08dW/vCU0vrvpRuhHGwlhgpwHIeXMxylRc/dUT+5ACriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkxBWGnO",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhACSgW7QyS8Yr0TOWYLTqpdv6fZYUnHZHSqmInksMJWpo19LiqHjRvnxRXQ3l5ZWWU1vpsrmGFTKXJRJVaFVNNDLhAoTy7TwuK62yHhYhnk0PDNkSpX+yzsmM3+3QMTLkQ7hV08dW/vCU0vrvpRuhHGwlhgpwHIeXMxylRc/dUT+5ACriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkxBWGnO",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhACSgW7QyS8Yr0TOWYLTqpdv6fZYUnHZHSqmInksMJWpo19LiqHjRvnxRXQ3l5ZWWU1vpsrmGFTKXJRJVaFVNNDLhAoTy7TwuK62yHhYhnk0PDNkSpX+yzsmM3+3QMTLkQ7hV08dW/vCU0vrvpRuhHGwlhgpwHIeXMxylRc/dUT+5ACriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkxBWGnO",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "message": {
        "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "message": {
        "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
  "id": -576460752303422588,
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
  "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
  "id": -576460752303422588,
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "state": "tx_+QENCwH4hLhACSgW7QyS8Yr0TOWYLTqpdv6fZYUnHZHSqmInksMJWpo19LiqHjRvnxRXQ3l5ZWWU1vpsrmGFTKXJRJVaFVNNDLhAoTy7TwuK62yHhYhnk0PDNkSpX+yzsmM3+3QMTLkQ7hV08dW/vCU0vrvpRuhHGwlhgpwHIeXMxylRc/dUT+5ACriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkxBWGnO"
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "state": "tx_+QENCwH4hLhACSgW7QyS8Yr0TOWYLTqpdv6fZYUnHZHSqmInksMJWpo19LiqHjRvnxRXQ3l5ZWWU1vpsrmGFTKXJRJVaFVNNDLhAoTy7TwuK62yHhYhnk0PDNkSpX+yzsmM3+3QMTLkQ7hV08dW/vCU0vrvpRuhHGwlhgpwHIeXMxylRc/dUT+5ACriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkxBWGnO"
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
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBmbEoTtohsrPdRKz2Hf6nvsxyNx7EwuVKvEgjkApRPMpoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7sgIAATezZg+c=",
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
    "signed_tx": "tx_+QHrCwH4QrhAAqrH4Vr8IBDoUh2opsZ5FsGznx/1VFCfjvYV1OGhxj3ILdvAe3YXneiHDN5jMwPaUHGhuNclqhS4f9eMVo0nD7kBovkBnzYBoQZmxKE7aIbKz3USs9h3+p77McjcexMLlSrxII5AKUTzKaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAE2mB+yS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAAqrH4Vr8IBDoUh2opsZ5FsGznx/1VFCfjvYV1OGhxj3ILdvAe3YXneiHDN5jMwPaUHGhuNclqhS4f9eMVo0nD7kBovkBnzYBoQZmxKE7aIbKz3USs9h3+p77McjcexMLlSrxII5AKUTzKaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAE2mB+yS",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAAqrH4Vr8IBDoUh2opsZ5FsGznx/1VFCfjvYV1OGhxj3ILdvAe3YXneiHDN5jMwPaUHGhuNclqhS4f9eMVo0nD7kBovkBnzYBoQZmxKE7aIbKz3USs9h3+p77McjcexMLlSrxII5AKUTzKaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAE2mB+yS",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
  "method": "channels.settle",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBmbEoTtohsrPdRKz2Hf6nvsxyNx7EwuVKvEgjkApRPMpoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiX/+GJGE5yoABAIZwSIYbDz9OgjMCRw==",
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
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBBXiRFI/woVgj5j4c5h/JIQ0UGEbx7cC6MVrWuYwBylIkx7vJuaXwTV849lWWsd7m8qXGBQyOVX0wgZ6m9xP8FuF/4XTgBoQZmxKE7aIbKz3USs9h3+p77McjcexMLlSrxII5AKUTzKaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGcEiGGw8/Ttk5Frk="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBBXiRFI/woVgj5j4c5h/JIQ0UGEbx7cC6MVrWuYwBylIkx7vJuaXwTV849lWWsd7m8qXGBQyOVX0wgZ6m9xP8FuF/4XTgBoQZmxKE7aIbKz3USs9h3+p77McjcexMLlSrxII5AKUTzKaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGcEiGGw8/Ttk5Frk=",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBBXiRFI/woVgj5j4c5h/JIQ0UGEbx7cC6MVrWuYwBylIkx7vJuaXwTV849lWWsd7m8qXGBQyOVX0wgZ6m9xP8FuF/4XTgBoQZmxKE7aIbKz3USs9h3+p77McjcexMLlSrxII5AKUTzKaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGcEiGGw8/Ttk5Frk=",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
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
    "channel_id": "ch_nG5DvZjK3Ypj8NigJFC5BW9j64uwJgpE8gvbxqug4hAu96LA5",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
