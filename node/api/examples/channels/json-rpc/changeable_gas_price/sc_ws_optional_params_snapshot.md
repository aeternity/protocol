
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
      "fsm_id": "ba_vQcZ+FyhtNeMzMeSih9xM6tzMIY+HXQhPUVj3rnM3jgB2rML"
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
      "fsm_id": "ba_Z/kIBKAE7SuXj9+lAFumTB29eEILCuY32SWf9Z1jP2Q6bFXJ"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZXnrSuGg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422564,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAXM6Qgw87UH6zoWUlXCTiDu5oCEC1ME9io6McRheT1ARBp2/Ty0yOaWzJMWr2DWdovUfDL0zU6HeJK3Pm9UE8CuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGV39jCjE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422564,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_Z/kIBKAE7SuXj9+lAFumTB29eEILCuY32SWf9Z1jP2Q6bFXJ"
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAXM6Qgw87UH6zoWUlXCTiDu5oCEC1ME9io6McRheT1ARBp2/Ty0yOaWzJMWr2DWdovUfDL0zU6HeJK3Pm9UE8CuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGV39jCjE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422563,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAFzOkIMPO1B+s6FlJVwk4g7uaAhAtTBPYqOjHEYXk9QEQadv08tMjmlsyTFq9g1naL1Hwy9M1Oh3iStz5vVBPArhApZ+u3ONxz24bWe96HBotkDqBn81e92z/G4v6R2Hs+49D+gV0u/GEm28MEd4FfoV/i8ivyJZl5IQNqe+9P+icBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RldUGDg+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422563,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAFzOkIMPO1B+s6FlJVwk4g7uaAhAtTBPYqOjHEYXk9QEQadv08tMjmlsyTFq9g1naL1Hwy9M1Oh3iStz5vVBPArhApZ+u3ONxz24bWe96HBotkDqBn81e92z/G4v6R2Hs+49D+gV0u/GEm28MEd4FfoV/i8ivyJZl5IQNqe+9P+icBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RldUGDg+",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_vQcZ+FyhtNeMzMeSih9xM6tzMIY+HXQhPUVj3rnM3jgB2rML"
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAFzOkIMPO1B+s6FlJVwk4g7uaAhAtTBPYqOjHEYXk9QEQadv08tMjmlsyTFq9g1naL1Hwy9M1Oh3iStz5vVBPArhApZ+u3ONxz24bWe96HBotkDqBn81e92z/G4v6R2Hs+49D+gV0u/GEm28MEd4FfoV/i8ivyJZl5IQNqe+9P+icBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RldUGDg+",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFzOkIMPO1B+s6FlJVwk4g7uaAhAtTBPYqOjHEYXk9QEQadv08tMjmlsyTFq9g1naL1Hwy9M1Oh3iStz5vVBPArhApZ+u3ONxz24bWe96HBotkDqBn81e92z/G4v6R2Hs+49D+gV0u/GEm28MEd4FfoV/i8ivyJZl5IQNqe+9P+icBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RldUGDg+",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFzOkIMPO1B+s6FlJVwk4g7uaAhAtTBPYqOjHEYXk9QEQadv08tMjmlsyTFq9g1naL1Hwy9M1Oh3iStz5vVBPArhApZ+u3ONxz24bWe96HBotkDqBn81e92z/G4v6R2Hs+49D+gV0u/GEm28MEd4FfoV/i8ivyJZl5IQNqe+9P+icBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RldUGDg+",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "message": {
        "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "message": {
        "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
  "id": -576460752303422562,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422562,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+QENCwH4hLhAFzOkIMPO1B+s6FlJVwk4g7uaAhAtTBPYqOjHEYXk9QEQadv08tMjmlsyTFq9g1naL1Hwy9M1Oh3iStz5vVBPArhApZ+u3ONxz24bWe96HBotkDqBn81e92z/G4v6R2Hs+49D+gV0u/GEm28MEd4FfoV/i8ivyJZl5IQNqe+9P+icBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RldUGDg+"
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+QENCwH4hLhAFzOkIMPO1B+s6FlJVwk4g7uaAhAtTBPYqOjHEYXk9QEQadv08tMjmlsyTFq9g1naL1Hwy9M1Oh3iStz5vVBPArhApZ+u3ONxz24bWe96HBotkDqBn81e92z/G4v6R2Hs+49D+gV0u/GEm28MEd4FfoV/i8ivyJZl5IQNqe+9P+icBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RldUGDg+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422561,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422561,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QENCwH4hLhAFzOkIMPO1B+s6FlJVwk4g7uaAhAtTBPYqOjHEYXk9QEQadv08tMjmlsyTFq9g1naL1Hwy9M1Oh3iStz5vVBPArhApZ+u3ONxz24bWe96HBotkDqBn81e92z/G4v6R2Hs+49D+gV0u/GEm28MEd4FfoV/i8ivyJZl5IQNqe+9P+icBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RldUGDg+",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422560,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422560,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqY/eTlFAvUNrKMcCel6vXYBVkmbaSVLarAVTWs3N1s8AqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCypgMbAU=",
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
  "id": -576460752303422559,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECI8n39rboE6MlXw9uio1WIODGOqGJNdw0pSJ/WPtHTcBpv7tivb8Cza5+Bq0ZDV9LBuMW8ffKB1LPbe1Mesh8AuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrO/ime"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422559,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+JALAfhCuECI8n39rboE6MlXw9uio1WIODGOqGJNdw0pSJ/WPtHTcBpv7tivb8Cza5+Bq0ZDV9LBuMW8ffKB1LPbe1Mesh8AuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrO/ime",
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
  "id": -576460752303422558,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAAilZVcLoUzP7lfXAdd7oKMjGI2dkRQwFJSexpILRMJhCTbUKgq4wcx+PtEIbofLyqXENX6NeCOLnKW3Rs/7YLuECI8n39rboE6MlXw9uio1WIODGOqGJNdw0pSJ/WPtHTcBpv7tivb8Cza5+Bq0ZDV9LBuMW8ffKB1LPbe1Mesh8AuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoNzPM5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422558,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuEAAilZVcLoUzP7lfXAdd7oKMjGI2dkRQwFJSexpILRMJhCTbUKgq4wcx+PtEIbofLyqXENX6NeCOLnKW3Rs/7YLuECI8n39rboE6MlXw9uio1WIODGOqGJNdw0pSJ/WPtHTcBpv7tivb8Cza5+Bq0ZDV9LBuMW8ffKB1LPbe1Mesh8AuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoNzPM5"
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuEAAilZVcLoUzP7lfXAdd7oKMjGI2dkRQwFJSexpILRMJhCTbUKgq4wcx+PtEIbofLyqXENX6NeCOLnKW3Rs/7YLuECI8n39rboE6MlXw9uio1WIODGOqGJNdw0pSJ/WPtHTcBpv7tivb8Cza5+Bq0ZDV9LBuMW8ffKB1LPbe1Mesh8AuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoNzPM5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422557,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422557,
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
  "id": -576460752303422556,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422556,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAAilZVcLoUzP7lfXAdd7oKMjGI2dkRQwFJSexpILRMJhCTbUKgq4wcx+PtEIbofLyqXENX6NeCOLnKW3Rs/7YLuECI8n39rboE6MlXw9uio1WIODGOqGJNdw0pSJ/WPtHTcBpv7tivb8Cza5+Bq0ZDV9LBuMW8ffKB1LPbe1Mesh8AuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoNzPM5",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422555,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422555,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBqY/eTlFAvUNrKMcCel6vXYBVkmbaSVLarAVTWs3N1s8oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAAilZVcLoUzP7lfXAdd7oKMjGI2dkRQwFJSexpILRMJhCTbUKgq4wcx+PtEIbofLyqXENX6NeCOLnKW3Rs/7YLuECI8n39rboE6MlXw9uio1WIODGOqGJNdw0pSJ/WPtHTcBpv7tivb8Cza5+Bq0ZDV9LBuMW8ffKB1LPbe1Mesh8AuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoAhhMG0rUY8FhiAx0S",
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
    "signed_tx": "tx_+QFxCwH4QrhAM9qzD6LTxNvYOuZyiV4c2xh9B7gw/I7UW7onT5IeAcrTXpYdBRAYBUXT6ocmyUSFfKON3GVOqelcoYv9jQocBLkBKPkBJTsBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAAIpWVXC6FMz+5X1wHXe6CjIxiNnZEUMBSUnsaSC0TCYQk21CoKuMHMfj7RCG6Hy8qlxDV+jXgji5ylt0bP+2C7hAiPJ9/a26BOjJV8PboqNViDgxjqhiTXcNKUif1j7R03Aab+7Yr2/As2ufgatGQ1fSwbjFvH3ygdSz23tTHrIfALhI+EY5AqEGpj95OUUC9Q2soxwJ6Xq9dgFWSZtpJUtqsBVNazc3WzwCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIYTBtK1GPBY/irBfw=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422554,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422554,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqY/eTlFAvUNrKMcCel6vXYBVkmbaSVLarAVTWs3N1s8A6CyPuq+gQA2a6qmnwMyrfvY3kyHmlBoHoJrMzYXSPbNfECDfnE=",
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
  "id": -576460752303422553,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECLud2/hhfyIPvibHj7OCuVfcGi0MS9BvUUQN/JQ2W7CS2rxoCJ5muZM8SPKyKM46MOhD7IuUXggxtw79J767MGuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzlUS2G"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422553,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+JALAfhCuECLud2/hhfyIPvibHj7OCuVfcGi0MS9BvUUQN/JQ2W7CS2rxoCJ5muZM8SPKyKM46MOhD7IuUXggxtw79J767MGuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzlUS2G",
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
  "id": -576460752303422552,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBqidnVbsO7khYXLp41+6lybxderkbyLI24cXoOOlx6VhVJoSd0kHyGeJIAh9965tvj+7cynIG+cG4hEIRZOgEOuECLud2/hhfyIPvibHj7OCuVfcGi0MS9BvUUQN/JQ2W7CS2rxoCJ5muZM8SPKyKM46MOhD7IuUXggxtw79J767MGuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXyC4ZOg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422552,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuEBqidnVbsO7khYXLp41+6lybxderkbyLI24cXoOOlx6VhVJoSd0kHyGeJIAh9965tvj+7cynIG+cG4hEIRZOgEOuECLud2/hhfyIPvibHj7OCuVfcGi0MS9BvUUQN/JQ2W7CS2rxoCJ5muZM8SPKyKM46MOhD7IuUXggxtw79J767MGuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXyC4ZOg"
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuEBqidnVbsO7khYXLp41+6lybxderkbyLI24cXoOOlx6VhVJoSd0kHyGeJIAh9965tvj+7cynIG+cG4hEIRZOgEOuECLud2/hhfyIPvibHj7OCuVfcGi0MS9BvUUQN/JQ2W7CS2rxoCJ5muZM8SPKyKM46MOhD7IuUXggxtw79J767MGuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXyC4ZOg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422551,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422551,
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
  "id": -576460752303422550,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422550,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBqidnVbsO7khYXLp41+6lybxderkbyLI24cXoOOlx6VhVJoSd0kHyGeJIAh9965tvj+7cynIG+cG4hEIRZOgEOuECLud2/hhfyIPvibHj7OCuVfcGi0MS9BvUUQN/JQ2W7CS2rxoCJ5muZM8SPKyKM46MOhD7IuUXggxtw79J767MGuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXyC4ZOg",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAA7DvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/3rbPVC"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422549,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422549,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqY/eTlFAvUNrKMcCel6vXYBVkmbaSVLarAVTWs3N1s8BKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyvIAhBU=",
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
  "id": -576460752303422548,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECM5bk1ebrySONd0iTj9QafSeU4hDkigwmKXPwxU3kstkod365tRmIN1VqVUh2CEM/eYQBt6DJXU3schOD6H7oDuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsos9u2e"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422548,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+JALAfhCuECM5bk1ebrySONd0iTj9QafSeU4hDkigwmKXPwxU3kstkod365tRmIN1VqVUh2CEM/eYQBt6DJXU3schOD6H7oDuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsos9u2e",
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
  "id": -576460752303422547,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECM5bk1ebrySONd0iTj9QafSeU4hDkigwmKXPwxU3kstkod365tRmIN1VqVUh2CEM/eYQBt6DJXU3schOD6H7oDuEDn6dQccANUNj3xd1AexsaLaM0anz1Cl0+XxE9vI5DN9uiZb8ifYsz6473fZ5kji9yYnEwdoMVESeWtGafPmB8OuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoSpeFA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422547,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuECM5bk1ebrySONd0iTj9QafSeU4hDkigwmKXPwxU3kstkod365tRmIN1VqVUh2CEM/eYQBt6DJXU3schOD6H7oDuEDn6dQccANUNj3xd1AexsaLaM0anz1Cl0+XxE9vI5DN9uiZb8ifYsz6473fZ5kji9yYnEwdoMVESeWtGafPmB8OuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoSpeFA"
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuECM5bk1ebrySONd0iTj9QafSeU4hDkigwmKXPwxU3kstkod365tRmIN1VqVUh2CEM/eYQBt6DJXU3schOD6H7oDuEDn6dQccANUNj3xd1AexsaLaM0anz1Cl0+XxE9vI5DN9uiZb8ifYsz6473fZ5kji9yYnEwdoMVESeWtGafPmB8OuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoSpeFA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422546,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422546,
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
  "id": -576460752303422545,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422545,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECM5bk1ebrySONd0iTj9QafSeU4hDkigwmKXPwxU3kstkod365tRmIN1VqVUh2CEM/eYQBt6DJXU3schOD6H7oDuEDn6dQccANUNj3xd1AexsaLaM0anz1Cl0+XxE9vI5DN9uiZb8ifYsz6473fZ5kji9yYnEwdoMVESeWtGafPmB8OuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoSpeFA",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAM9qzD6LTxNvYOuZyiV4c2xh9B7gw/I7UW7onT5IeAcrTXpYdBRAYBUXT6ocmyUSFfKON3GVOqelcoYv9jQocBLkBKPkBJTsBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAAIpWVXC6FMz+5X1wHXe6CjIxiNnZEUMBSUnsaSC0TCYQk21CoKuMHMfj7RCG6Hy8qlxDV+jXgji5ylt0bP+2C7hAiPJ9/a26BOjJV8PboqNViDgxjqhiTXcNKUif1j7R03Aab+7Yr2/As2ufgatGQ1fSwbjFvH3ygdSz23tTHrIfALhI+EY5AqEGpj95OUUC9Q2soxwJ6Xq9dgFWSZtpJUtqsBVNazc3WzwCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIYTBtK1GPBY/irBfw==",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAM9qzD6LTxNvYOuZyiV4c2xh9B7gw/I7UW7onT5IeAcrTXpYdBRAYBUXT6ocmyUSFfKON3GVOqelcoYv9jQocBLkBKPkBJTsBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAAIpWVXC6FMz+5X1wHXe6CjIxiNnZEUMBSUnsaSC0TCYQk21CoKuMHMfj7RCG6Hy8qlxDV+jXgji5ylt0bP+2C7hAiPJ9/a26BOjJV8PboqNViDgxjqhiTXcNKUif1j7R03Aab+7Yr2/As2ufgatGQ1fSwbjFvH3ygdSz23tTHrIfALhI+EY5AqEGpj95OUUC9Q2soxwJ6Xq9dgFWSZtpJUtqsBVNazc3WzwCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIYTBtK1GPBY/irBfw==",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "D)`�m�V�fK�?9�+'?�ph��v^C��sY,\u0010�",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422544,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422544,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECM5bk1ebrySONd0iTj9QafSeU4hDkigwmKXPwxU3kstkod365tRmIN1VqVUh2CEM/eYQBt6DJXU3schOD6H7oDuEDn6dQccANUNj3xd1AexsaLaM0anz1Cl0+XxE9vI5DN9uiZb8ifYsz6473fZ5kji9yYnEwdoMVESeWtGafPmB8OuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoSpeFA",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422543,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422543,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqY/eTlFAvUNrKMcCel6vXYBVkmbaSVLarAVTWs3N1s8BaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rj26jTo=",
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
  "id": -576460752303422542,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECVh0f9cJLdLJ0zUioPEZcODzp0yqx3POQAYnJPPFkCU5G6GLHrqSOgyI0oZaE24bVL8ejhTOVEq2R9tqKtszkDuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaYMe1B"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422542,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+JALAfhCuECVh0f9cJLdLJ0zUioPEZcODzp0yqx3POQAYnJPPFkCU5G6GLHrqSOgyI0oZaE24bVL8ejhTOVEq2R9tqKtszkDuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaYMe1B",
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
  "id": -576460752303422541,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECVh0f9cJLdLJ0zUioPEZcODzp0yqx3POQAYnJPPFkCU5G6GLHrqSOgyI0oZaE24bVL8ejhTOVEq2R9tqKtszkDuEC5T2or4dZxEaxoRFCYPspL2L9RlRlmYlxRgvvg1iqhgS6vSHciZhiGJCkKtY+B2/VymZSf91v0kv4QKLCb4o8GuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ7/m3d"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422541,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuECVh0f9cJLdLJ0zUioPEZcODzp0yqx3POQAYnJPPFkCU5G6GLHrqSOgyI0oZaE24bVL8ejhTOVEq2R9tqKtszkDuEC5T2or4dZxEaxoRFCYPspL2L9RlRlmYlxRgvvg1iqhgS6vSHciZhiGJCkKtY+B2/VymZSf91v0kv4QKLCb4o8GuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ7/m3d"
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuECVh0f9cJLdLJ0zUioPEZcODzp0yqx3POQAYnJPPFkCU5G6GLHrqSOgyI0oZaE24bVL8ejhTOVEq2R9tqKtszkDuEC5T2or4dZxEaxoRFCYPspL2L9RlRlmYlxRgvvg1iqhgS6vSHciZhiGJCkKtY+B2/VymZSf91v0kv4QKLCb4o8GuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ7/m3d"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422540,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422540,
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
  "id": -576460752303422539,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422539,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECVh0f9cJLdLJ0zUioPEZcODzp0yqx3POQAYnJPPFkCU5G6GLHrqSOgyI0oZaE24bVL8ejhTOVEq2R9tqKtszkDuEC5T2or4dZxEaxoRFCYPspL2L9RlRlmYlxRgvvg1iqhgS6vSHciZhiGJCkKtY+B2/VymZSf91v0kv4QKLCb4o8GuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ7/m3d",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422538,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422538,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBqY/eTlFAvUNrKMcCel6vXYBVkmbaSVLarAVTWs3N1s8oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuECVh0f9cJLdLJ0zUioPEZcODzp0yqx3POQAYnJPPFkCU5G6GLHrqSOgyI0oZaE24bVL8ejhTOVEq2R9tqKtszkDuEC5T2or4dZxEaxoRFCYPspL2L9RlRlmYlxRgvvg1iqhgS6vSHciZhiGJCkKtY+B2/VymZSf91v0kv4QKLCb4o8GuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMG0rUY8CPNY/s1",
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
    "signed_tx": "tx_+QFxCwH4QrhAj1EZKfEbRKw0VXq5iy1gJk9QL8ik4SH9aQWgkP6OLY/HbtRrutyKSufVOEavDGSugOHRkSMX7odUcsJwowc2D7kBKPkBJTsBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAlYdH/XCS3SydM1IqDxGXDg86dMqsdzzkAGJyTzxZAlORuhix66kjoMiNKGWhNuG1S/Ho4UzlRKtkfbairbM5A7hAuU9qK+HWcRGsaERQmD7KS9i/UZUZZmJcUYL74NYqoYEur0h3ImYYhiQpCrWPgdv1cpmUn/db9JL+ECiwm+KPBrhI+EY5AqEGpj95OUUC9Q2soxwJ6Xq9dgFWSZtpJUtqsBVNazc3WzwFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtK1GPAjZjXopg=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422537,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422537,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqY/eTlFAvUNrKMcCel6vXYBVkmbaSVLarAVTWs3N1s8BqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyrZGJ0k=",
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
  "id": -576460752303422536,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC/ltwFcVzwdhYk/SsD/FhDyi5WRA5fnbIT9CzWrf2wHwf12NClyz7svT/sv1hW9pFhs3jd1CjG+G8DzjoQsnkAuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsovsRk6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422536,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC/ltwFcVzwdhYk/SsD/FhDyi5WRA5fnbIT9CzWrf2wHwf12NClyz7svT/sv1hW9pFhs3jd1CjG+G8DzjoQsnkAuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsovsRk6",
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
  "id": -576460752303422535,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC/ltwFcVzwdhYk/SsD/FhDyi5WRA5fnbIT9CzWrf2wHwf12NClyz7svT/sv1hW9pFhs3jd1CjG+G8DzjoQsnkAuEDOxLmbTbsrDs18O8kBLQdecwSAczJn/KluKwTfJNU9uYPEYf8U4Mp/ZMbpMM84GrnE6p2PHfgFcU7pLeIRJ/0JuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsogiNA7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422535,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuEC/ltwFcVzwdhYk/SsD/FhDyi5WRA5fnbIT9CzWrf2wHwf12NClyz7svT/sv1hW9pFhs3jd1CjG+G8DzjoQsnkAuEDOxLmbTbsrDs18O8kBLQdecwSAczJn/KluKwTfJNU9uYPEYf8U4Mp/ZMbpMM84GrnE6p2PHfgFcU7pLeIRJ/0JuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsogiNA7"
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuEC/ltwFcVzwdhYk/SsD/FhDyi5WRA5fnbIT9CzWrf2wHwf12NClyz7svT/sv1hW9pFhs3jd1CjG+G8DzjoQsnkAuEDOxLmbTbsrDs18O8kBLQdecwSAczJn/KluKwTfJNU9uYPEYf8U4Mp/ZMbpMM84GrnE6p2PHfgFcU7pLeIRJ/0JuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsogiNA7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422534,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422534,
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
  "id": -576460752303422533,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422533,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC/ltwFcVzwdhYk/SsD/FhDyi5WRA5fnbIT9CzWrf2wHwf12NClyz7svT/sv1hW9pFhs3jd1CjG+G8DzjoQsnkAuEDOxLmbTbsrDs18O8kBLQdecwSAczJn/KluKwTfJNU9uYPEYf8U4Mp/ZMbpMM84GrnE6p2PHfgFcU7pLeIRJ/0JuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsogiNA7",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422532,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422532,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqY/eTlFAvUNrKMcCel6vXYBVkmbaSVLarAVTWs3N1s8B6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rp/uQLU=",
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
  "id": -576460752303422531,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEATi0QiCgXz9Upha+DzAFylQ1gj3xFnlsn0BifRVgk4hwzQ1WwodHKtxYKy675cPcsQp9XSzrRMW6WDerpE2WoAuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYhWqqa"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422531,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+JALAfhCuEATi0QiCgXz9Upha+DzAFylQ1gj3xFnlsn0BifRVgk4hwzQ1WwodHKtxYKy675cPcsQp9XSzrRMW6WDerpE2WoAuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYhWqqa",
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
  "id": -576460752303422530,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEATi0QiCgXz9Upha+DzAFylQ1gj3xFnlsn0BifRVgk4hwzQ1WwodHKtxYKy675cPcsQp9XSzrRMW6WDerpE2WoAuECvsvixmydgtJ8AYEU1I5ILhF/x8DAZE1SSWW2YCXVoqdMQ1/p3o0rP+QyH0UBhVu5vuua+ob5ueYTAW/kk7YQFuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb4zka6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422530,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuEATi0QiCgXz9Upha+DzAFylQ1gj3xFnlsn0BifRVgk4hwzQ1WwodHKtxYKy675cPcsQp9XSzrRMW6WDerpE2WoAuECvsvixmydgtJ8AYEU1I5ILhF/x8DAZE1SSWW2YCXVoqdMQ1/p3o0rP+QyH0UBhVu5vuua+ob5ueYTAW/kk7YQFuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb4zka6"
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "state": "tx_+NILAfiEuEATi0QiCgXz9Upha+DzAFylQ1gj3xFnlsn0BifRVgk4hwzQ1WwodHKtxYKy675cPcsQp9XSzrRMW6WDerpE2WoAuECvsvixmydgtJ8AYEU1I5ILhF/x8DAZE1SSWW2YCXVoqdMQ1/p3o0rP+QyH0UBhVu5vuua+ob5ueYTAW/kk7YQFuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb4zka6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422529,
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
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422529,
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
  "id": -576460752303422528,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422528,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEATi0QiCgXz9Upha+DzAFylQ1gj3xFnlsn0BifRVgk4hwzQ1WwodHKtxYKy675cPcsQp9XSzrRMW6WDerpE2WoAuECvsvixmydgtJ8AYEU1I5ILhF/x8DAZE1SSWW2YCXVoqdMQ1/p3o0rP+QyH0UBhVu5vuua+ob5ueYTAW/kk7YQFuEj4RjkCoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb4zka6",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAj1EZKfEbRKw0VXq5iy1gJk9QL8ik4SH9aQWgkP6OLY/HbtRrutyKSufVOEavDGSugOHRkSMX7odUcsJwowc2D7kBKPkBJTsBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAlYdH/XCS3SydM1IqDxGXDg86dMqsdzzkAGJyTzxZAlORuhix66kjoMiNKGWhNuG1S/Ho4UzlRKtkfbairbM5A7hAuU9qK+HWcRGsaERQmD7KS9i/UZUZZmJcUYL74NYqoYEur0h3ImYYhiQpCrWPgdv1cpmUn/db9JL+ECiwm+KPBrhI+EY5AqEGpj95OUUC9Q2soxwJ6Xq9dgFWSZtpJUtqsBVNazc3WzwFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtK1GPAjZjXopg==",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAj1EZKfEbRKw0VXq5iy1gJk9QL8ik4SH9aQWgkP6OLY/HbtRrutyKSufVOEavDGSugOHRkSMX7odUcsJwowc2D7kBKPkBJTsBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAlYdH/XCS3SydM1IqDxGXDg86dMqsdzzkAGJyTzxZAlORuhix66kjoMiNKGWhNuG1S/Ho4UzlRKtkfbairbM5A7hAuU9qK+HWcRGsaERQmD7KS9i/UZUZZmJcUYL74NYqoYEur0h3ImYYhiQpCrWPgdv1cpmUn/db9JL+ECiwm+KPBrhI+EY5AqEGpj95OUUC9Q2soxwJ6Xq9dgFWSZtpJUtqsBVNazc3WzwFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtK1GPAjZjXopg==",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": ")��q\u0005\u000f�3/���^1��o����\u0001P�\\\u001f�*�&%",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBqY/eTlFAvUNrKMcCel6vXYBVkmbaSVLarAVTWs3N1s8oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/+GHLHOiuwBAIYPXtZ/KABZrQtQgg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422527,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDkodjd0Mku1TUHeO83nnAoPK57phUg6EPTTISFC9up0vEJ/x8gT59mOOX92yQJmvI+l5WegnfnyRqi1/lMHvgJuF/4XTUBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAWbGPVT0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422527,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDkodjd0Mku1TUHeO83nnAoPK57phUg6EPTTISFC9up0vEJ/x8gT59mOOX92yQJmvI+l5WegnfnyRqi1/lMHvgJuF/4XTUBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAWbGPVT0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422526,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuECbFtV3TuD2HORaUqIdyhzCNuw2cevevdF/K48EVaNglgfej/TIaBK1Iw3SqAAOsMzjjeSJtytA58kztAB0iw0CuEDkodjd0Mku1TUHeO83nnAoPK57phUg6EPTTISFC9up0vEJ/x8gT59mOOX92yQJmvI+l5WegnfnyRqi1/lMHvgJuF/4XTUBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAWb6bt60="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
  "id": -576460752303422526,
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECbFtV3TuD2HORaUqIdyhzCNuw2cevevdF/K48EVaNglgfej/TIaBK1Iw3SqAAOsMzjjeSJtytA58kztAB0iw0CuEDkodjd0Mku1TUHeO83nnAoPK57phUg6EPTTISFC9up0vEJ/x8gT59mOOX92yQJmvI+l5WegnfnyRqi1/lMHvgJuF/4XTUBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAWb6bt60=",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECbFtV3TuD2HORaUqIdyhzCNuw2cevevdF/K48EVaNglgfej/TIaBK1Iw3SqAAOsMzjjeSJtytA58kztAB0iw0CuEDkodjd0Mku1TUHeO83nnAoPK57phUg6EPTTISFC9up0vEJ/x8gT59mOOX92yQJmvI+l5WegnfnyRqi1/lMHvgJuF/4XTUBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAWb6bt60=",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECbFtV3TuD2HORaUqIdyhzCNuw2cevevdF/K48EVaNglgfej/TIaBK1Iw3SqAAOsMzjjeSJtytA58kztAB0iw0CuEDkodjd0Mku1TUHeO83nnAoPK57phUg6EPTTISFC9up0vEJ/x8gT59mOOX92yQJmvI+l5WegnfnyRqi1/lMHvgJuF/4XTUBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAWb6bt60=",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECbFtV3TuD2HORaUqIdyhzCNuw2cevevdF/K48EVaNglgfej/TIaBK1Iw3SqAAOsMzjjeSJtytA58kztAB0iw0CuEDkodjd0Mku1TUHeO83nnAoPK57phUg6EPTTISFC9up0vEJ/x8gT59mOOX92yQJmvI+l5WegnfnyRqi1/lMHvgJuF/4XTUBoQamP3k5RQL1DayjHAnper12AVZJm2klS2qwFU1rNzdbPKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAWb6bt60=",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
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
    "channel_id": "ch_2GDag6eJXGN5v9ArZbXeuNteDJ17ubd5k5jvz8QvvsBNJg7RGX",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
