
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
      "fsm_id": "ba_LARtdCLsT0K0OdNstG+AVxBGLmpyX3vXMY/DOPlJsECtiHbL"
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
      "fsm_id": "ba_YhqUvSGmB6590EuR/qA1af+s868tP+RNlmYlt3gnizPSrCVc"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZaD/o7gA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422525,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBr7CDC4LE8spP4miPgq1KkF1UfDMz/aA0+7LsYHFdR3fnVCPnV3kJ0JNglNLhPGY4y9FRAVK2/9AiVf7sLGeQNuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGWiJ3OAw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422525,
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_YhqUvSGmB6590EuR/qA1af+s868tP+RNlmYlt3gnizPSrCVc"
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBr7CDC4LE8spP4miPgq1KkF1UfDMz/aA0+7LsYHFdR3fnVCPnV3kJ0JNglNLhPGY4y9FRAVK2/9AiVf7sLGeQNuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGWiJ3OAw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422524,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAa+wgwuCxPLKT+Joj4KtSpBdVHwzM/2gNPuy7GBxXUd351Qj51d5CdCTYJTS4TxmOMvRUQFStv/QIlX+7CxnkDbhA9ekFHKWUImdQhVAEX+++8qK8iIbAHoM7QeKXILSc8vFwtr6qSkzrHPx/xhcCmjHqqNpKWPHiimbjpBFgwXAZDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlrVDbV7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
  "id": -576460752303422524,
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAa+wgwuCxPLKT+Joj4KtSpBdVHwzM/2gNPuy7GBxXUd351Qj51d5CdCTYJTS4TxmOMvRUQFStv/QIlX+7CxnkDbhA9ekFHKWUImdQhVAEX+++8qK8iIbAHoM7QeKXILSc8vFwtr6qSkzrHPx/xhcCmjHqqNpKWPHiimbjpBFgwXAZDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlrVDbV7",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_LARtdCLsT0K0OdNstG+AVxBGLmpyX3vXMY/DOPlJsECtiHbL"
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAa+wgwuCxPLKT+Joj4KtSpBdVHwzM/2gNPuy7GBxXUd351Qj51d5CdCTYJTS4TxmOMvRUQFStv/QIlX+7CxnkDbhA9ekFHKWUImdQhVAEX+++8qK8iIbAHoM7QeKXILSc8vFwtr6qSkzrHPx/xhcCmjHqqNpKWPHiimbjpBFgwXAZDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlrVDbV7",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAa+wgwuCxPLKT+Joj4KtSpBdVHwzM/2gNPuy7GBxXUd351Qj51d5CdCTYJTS4TxmOMvRUQFStv/QIlX+7CxnkDbhA9ekFHKWUImdQhVAEX+++8qK8iIbAHoM7QeKXILSc8vFwtr6qSkzrHPx/xhcCmjHqqNpKWPHiimbjpBFgwXAZDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlrVDbV7",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAa+wgwuCxPLKT+Joj4KtSpBdVHwzM/2gNPuy7GBxXUd351Qj51d5CdCTYJTS4TxmOMvRUQFStv/QIlX+7CxnkDbhA9ekFHKWUImdQhVAEX+++8qK8iIbAHoM7QeKXILSc8vFwtr6qSkzrHPx/xhcCmjHqqNpKWPHiimbjpBFgwXAZDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlrVDbV7",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "message": {
        "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "message": {
        "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
  "id": -576460752303422523,
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
  "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
  "id": -576460752303422523,
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "state": "tx_+QENCwH4hLhAa+wgwuCxPLKT+Joj4KtSpBdVHwzM/2gNPuy7GBxXUd351Qj51d5CdCTYJTS4TxmOMvRUQFStv/QIlX+7CxnkDbhA9ekFHKWUImdQhVAEX+++8qK8iIbAHoM7QeKXILSc8vFwtr6qSkzrHPx/xhcCmjHqqNpKWPHiimbjpBFgwXAZDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlrVDbV7"
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "state": "tx_+QENCwH4hLhAa+wgwuCxPLKT+Joj4KtSpBdVHwzM/2gNPuy7GBxXUd351Qj51d5CdCTYJTS4TxmOMvRUQFStv/QIlX+7CxnkDbhA9ekFHKWUImdQhVAEX+++8qK8iIbAHoM7QeKXILSc8vFwtr6qSkzrHPx/xhcCmjHqqNpKWPHiimbjpBFgwXAZDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlrVDbV7"
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
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBkSD6m9+7ejkeMQ3ikvJDkqb3BZr6tms1DmDd+eqe+AQoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7uOFqAW4HGdBQ=",
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
    "signed_tx": "tx_+QHrCwH4QrhAqK8E7kqgB8n1QAzUD0LYCxgXhqGPZe5V1k/9DtE0ifDd8TtWHxZbR/Qs/b6t7vQO8GkiaqbLm9+NqmPWBPRaDbkBovkBnzYBoQZEg+pvfu3o5HjEN4pLyQ5Km9wWa+rZrNQ5g3fnqnvgEKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7jhagFtaV9d8"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAqK8E7kqgB8n1QAzUD0LYCxgXhqGPZe5V1k/9DtE0ifDd8TtWHxZbR/Qs/b6t7vQO8GkiaqbLm9+NqmPWBPRaDbkBovkBnzYBoQZEg+pvfu3o5HjEN4pLyQ5Km9wWa+rZrNQ5g3fnqnvgEKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7jhagFtaV9d8",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAqK8E7kqgB8n1QAzUD0LYCxgXhqGPZe5V1k/9DtE0ifDd8TtWHxZbR/Qs/b6t7vQO8GkiaqbLm9+NqmPWBPRaDbkBovkBnzYBoQZEg+pvfu3o5HjEN4pLyQ5Km9wWa+rZrNQ5g3fnqnvgEKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7jhagFtaV9d8",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBkSD6m9+7ejkeMQ3ikvJDkqb3BZr6tms1DmDd+eqe+AQoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAAk8nIlvg==",
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
    "signed_tx": "tx_+KcLAfhCuEBTgyunY3zXLRnfPxDPi5mxGBqDXJwQXjeaW2A4gWQgP6YzJljos0zis3JXyoqbYWSGsr1l1ycYu0SPo/3oBUQAuF/4XTgBoQZEg+pvfu3o5HjEN4pLyQ5Km9wWa+rZrNQ5g3fnqnvgEKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAJLwHzDg="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBTgyunY3zXLRnfPxDPi5mxGBqDXJwQXjeaW2A4gWQgP6YzJljos0zis3JXyoqbYWSGsr1l1ycYu0SPo/3oBUQAuF/4XTgBoQZEg+pvfu3o5HjEN4pLyQ5Km9wWa+rZrNQ5g3fnqnvgEKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAJLwHzDg=",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBTgyunY3zXLRnfPxDPi5mxGBqDXJwQXjeaW2A4gWQgP6YzJljos0zis3JXyoqbYWSGsr1l1ycYu0SPo/3oBUQAuF/4XTgBoQZEg+pvfu3o5HjEN4pLyQ5Km9wWa+rZrNQ5g3fnqnvgEKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAJLwHzDg=",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
    "channel_id": "ch_XB8cctFYHqstQJEteM4ntTVmMybSoSQA4jDXXBnuKnHGWo19m",
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
      "fsm_id": "ba_Hh7aMnv9q6OfWcGuqjnfeUFkivCRhSNfMzQT71MU1RB1NRgJ"
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
      "fsm_id": "ba_2Ny0+8qjwiKsCpZopBaU48dSc/3aoNrj7imBEKYgVOGslUhx"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZcm5G9Gw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422522,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBGQpLu/VFgX0iKKY3mKnqBoJUy8jYx8weT2seSiZ31ySa52ZwN0vzXMtWa/+0cd6YrWh53HA1k92DC6FvcL0wKuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGXJS/5oo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422522,
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_2Ny0+8qjwiKsCpZopBaU48dSc/3aoNrj7imBEKYgVOGslUhx"
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBGQpLu/VFgX0iKKY3mKnqBoJUy8jYx8weT2seSiZ31ySa52ZwN0vzXMtWa/+0cd6YrWh53HA1k92DC6FvcL0wKuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGXJS/5oo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422521,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhARkKS7v1RYF9IiimN5ip6gaCVMvI2MfMHk9rHkomd9ckmudmcDdL81zLVmv/tHHemK1oedxwNZPdgwuhb3C9MCrhAg+JMiBL+i+folaxq1VUCF4RAA3As7XwMqMk3B/+GEdQjS6d5cvUOPeCnUubn9HazN32dBZG9LMigeGvf/hTRAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlylkQoB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
  "id": -576460752303422521,
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhARkKS7v1RYF9IiimN5ip6gaCVMvI2MfMHk9rHkomd9ckmudmcDdL81zLVmv/tHHemK1oedxwNZPdgwuhb3C9MCrhAg+JMiBL+i+folaxq1VUCF4RAA3As7XwMqMk3B/+GEdQjS6d5cvUOPeCnUubn9HazN32dBZG9LMigeGvf/hTRAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlylkQoB",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Hh7aMnv9q6OfWcGuqjnfeUFkivCRhSNfMzQT71MU1RB1NRgJ"
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhARkKS7v1RYF9IiimN5ip6gaCVMvI2MfMHk9rHkomd9ckmudmcDdL81zLVmv/tHHemK1oedxwNZPdgwuhb3C9MCrhAg+JMiBL+i+folaxq1VUCF4RAA3As7XwMqMk3B/+GEdQjS6d5cvUOPeCnUubn9HazN32dBZG9LMigeGvf/hTRAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlylkQoB",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARkKS7v1RYF9IiimN5ip6gaCVMvI2MfMHk9rHkomd9ckmudmcDdL81zLVmv/tHHemK1oedxwNZPdgwuhb3C9MCrhAg+JMiBL+i+folaxq1VUCF4RAA3As7XwMqMk3B/+GEdQjS6d5cvUOPeCnUubn9HazN32dBZG9LMigeGvf/hTRAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlylkQoB",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARkKS7v1RYF9IiimN5ip6gaCVMvI2MfMHk9rHkomd9ckmudmcDdL81zLVmv/tHHemK1oedxwNZPdgwuhb3C9MCrhAg+JMiBL+i+folaxq1VUCF4RAA3As7XwMqMk3B/+GEdQjS6d5cvUOPeCnUubn9HazN32dBZG9LMigeGvf/hTRAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlylkQoB",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "message": {
        "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "message": {
        "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
  "id": -576460752303422520,
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
  "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
  "id": -576460752303422520,
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "state": "tx_+QENCwH4hLhARkKS7v1RYF9IiimN5ip6gaCVMvI2MfMHk9rHkomd9ckmudmcDdL81zLVmv/tHHemK1oedxwNZPdgwuhb3C9MCrhAg+JMiBL+i+folaxq1VUCF4RAA3As7XwMqMk3B/+GEdQjS6d5cvUOPeCnUubn9HazN32dBZG9LMigeGvf/hTRAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlylkQoB"
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "state": "tx_+QENCwH4hLhARkKS7v1RYF9IiimN5ip6gaCVMvI2MfMHk9rHkomd9ckmudmcDdL81zLVmv/tHHemK1oedxwNZPdgwuhb3C9MCrhAg+JMiBL+i+folaxq1VUCF4RAA3As7XwMqMk3B/+GEdQjS6d5cvUOPeCnUubn9HazN32dBZG9LMigeGvf/hTRAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlylkQoB"
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
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBuZBUCYC8qzKJJiQHb9AK3Hgh9iS+8O19eWzqxv8Ff3CoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7uOFqAJfp6WO0=",
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
    "signed_tx": "tx_+QHrCwH4QrhAO/IpQFoiGXztWIZozPe1wlAw+ka25GSmeuEnq50G7ojGiCy4If3004TpxLOG5JCtqXX6O2W5VWAaTor3JNS6CrkBovkBnzYBoQbmQVAmAvKsyiSYkB2/QCtx4IfYkvvDtfXls6sb/BX9wqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7jhagCUuQvg8"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAO/IpQFoiGXztWIZozPe1wlAw+ka25GSmeuEnq50G7ojGiCy4If3004TpxLOG5JCtqXX6O2W5VWAaTor3JNS6CrkBovkBnzYBoQbmQVAmAvKsyiSYkB2/QCtx4IfYkvvDtfXls6sb/BX9wqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7jhagCUuQvg8",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAO/IpQFoiGXztWIZozPe1wlAw+ka25GSmeuEnq50G7ojGiCy4If3004TpxLOG5JCtqXX6O2W5VWAaTor3JNS6CrkBovkBnzYBoQbmQVAmAvKsyiSYkB2/QCtx4IfYkvvDtfXls6sb/BX9wqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7jhagCUuQvg8",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBuZBUCYC8qzKJJiQHb9AK3Hgh9iS+8O19eWzqxv8Ff3CoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAAmS2czCw==",
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
    "signed_tx": "tx_+KcLAfhCuECh65v0MN1PSr7k0fdWuppVt3qjTtzALD1Nr/FiXQSiXH+lxXEKJw7N29vZQWSqO4f32AMHUiDilyiPFgZ6lfMDuF/4XTgBoQbmQVAmAvKsyiSYkB2/QCtx4IfYkvvDtfXls6sb/BX9wqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAJo9kRvc="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECh65v0MN1PSr7k0fdWuppVt3qjTtzALD1Nr/FiXQSiXH+lxXEKJw7N29vZQWSqO4f32AMHUiDilyiPFgZ6lfMDuF/4XTgBoQbmQVAmAvKsyiSYkB2/QCtx4IfYkvvDtfXls6sb/BX9wqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAJo9kRvc=",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECh65v0MN1PSr7k0fdWuppVt3qjTtzALD1Nr/FiXQSiXH+lxXEKJw7N29vZQWSqO4f32AMHUiDilyiPFgZ6lfMDuF/4XTgBoQbmQVAmAvKsyiSYkB2/QCtx4IfYkvvDtfXls6sb/BX9wqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAJo9kRvc=",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
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
    "channel_id": "ch_2kQZNvV57HrFSVL4tTEoh7YZEC2fYTL5ttAuYaHgidUPzRmoJm",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
