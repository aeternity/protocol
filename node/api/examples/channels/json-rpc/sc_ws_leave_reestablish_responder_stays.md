
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_responder_stays%2F3750
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
      "fsm_id": "ba_PmK5bqSrKnN+og0B9VCk4utnjzvb6GjlCXBsXSiXhz9zmLqz"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=true&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_responder_stays%2F3750
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
      "fsm_id": "ba_NpuQ11qmW0gzCOL6yXMylF2fye6tkJbhnGpePI7SP41ZyfqW"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYXWkFacQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423217,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAlnNuEVDZ0ZIsaoAPasdet6hQiVAczNtjSD+CYez6MvQl6qdXe9txDC9BTRTW/0xqGchMXp2iotvSqIwpygasHuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGF1ImPZU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423217,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_NpuQ11qmW0gzCOL6yXMylF2fye6tkJbhnGpePI7SP41ZyfqW"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAlnNuEVDZ0ZIsaoAPasdet6hQiVAczNtjSD+CYez6MvQl6qdXe9txDC9BTRTW/0xqGchMXp2iotvSqIwpygasHuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGF1ImPZU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423216,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423216,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_PmK5bqSrKnN+og0B9VCk4utnjzvb6GjlCXBsXSiXhz9zmLqz"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "message": {
        "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "message": {
        "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "id": -576460752303423215,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423215,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "event": "peer_disconnected"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa&existing_fsm_id=ba_PmK5bqSrKnN%2Bog0B9VCk4utnjzvb6GjlCXBsXSiXhz9zmLqz&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g%2FgmHs%2BjL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4%2FhTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF%2BiWu4WXSjLiFB%2FD2%2FPk5Zs9hBkP4XgPmMRRWJZjBLiD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4Rhdl07C3&port=13179&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_2YN58/5pVzatLRoFnh2v1dxd5DhfZAzRzYRL/kRhgdMhwlFd"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+QENCwH4hLhAJZzbhFQ2dGSLGqAD2rHXreoUIlQHMzbY0g/gmHs+jL0JeqnV3vbcQwvQU0U1v9MahnITF6doqLb0qiMKcoGrB7hARcbW0b4/hTdBeRVx0zhzoodzYqhqjBQHWTGTiZTBbKYyF+iWu4WXSjLiFB/D2/Pk5Zs9hBkP4XgPmMRRWJZjBLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rhdl07C3"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423214,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423214,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBo2Bknyl1Hdp5FKxMWpGWVJ+nfAwAIn0TZWjPkaQ1eylAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCysb4G2g=",
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
  "id": -576460752303423213,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECm6BFSaw2qbeZjcxyAg8Vv7TwOTtlpygKdsi8+PaQrcc2vKquD6Few3blLd1kVUP0N0u8Gy0XkVG/sa313M8sNuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr9DD9H"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423213,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+JALAfhCuECm6BFSaw2qbeZjcxyAg8Vv7TwOTtlpygKdsi8+PaQrcc2vKquD6Few3blLd1kVUP0N0u8Gy0XkVG/sa313M8sNuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr9DD9H",
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
  "id": -576460752303423212,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAcxCgHYwPxqQqleO9FKN9Ec9HrxGH4oI0TlWVj2+n9PtZbTZapEWOcpMQpCN9gVkcVJFBSq/zYpUBwSOfIeuYJuECm6BFSaw2qbeZjcxyAg8Vv7TwOTtlpygKdsi8+PaQrcc2vKquD6Few3blLd1kVUP0N0u8Gy0XkVG/sa313M8sNuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr8MXoX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423212,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuEAcxCgHYwPxqQqleO9FKN9Ec9HrxGH4oI0TlWVj2+n9PtZbTZapEWOcpMQpCN9gVkcVJFBSq/zYpUBwSOfIeuYJuECm6BFSaw2qbeZjcxyAg8Vv7TwOTtlpygKdsi8+PaQrcc2vKquD6Few3blLd1kVUP0N0u8Gy0XkVG/sa313M8sNuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr8MXoX"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuEAcxCgHYwPxqQqleO9FKN9Ec9HrxGH4oI0TlWVj2+n9PtZbTZapEWOcpMQpCN9gVkcVJFBSq/zYpUBwSOfIeuYJuECm6BFSaw2qbeZjcxyAg8Vv7TwOTtlpygKdsi8+PaQrcc2vKquD6Few3blLd1kVUP0N0u8Gy0XkVG/sa313M8sNuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr8MXoX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423211,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423211,
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
  "id": -576460752303423210,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423210,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAcxCgHYwPxqQqleO9FKN9Ec9HrxGH4oI0TlWVj2+n9PtZbTZapEWOcpMQpCN9gVkcVJFBSq/zYpUBwSOfIeuYJuECm6BFSaw2qbeZjcxyAg8Vv7TwOTtlpygKdsi8+PaQrcc2vKquD6Few3blLd1kVUP0N0u8Gy0XkVG/sa313M8sNuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr8MXoX",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423209,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423209,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBo2Bknyl1Hdp5FKxMWpGWVJ+nfAwAIn0TZWjPkaQ1eylA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhUIPuk=",
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
  "id": -576460752303423208,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBdtei+sZg8ywPSxh6W8nPs6PW22xOI4KWqmJ5JLZfpI2lleBGfMLpQ2pxMUOj8UW7981h146zwfzyWxbYjui8LuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbyCuHq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423208,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBdtei+sZg8ywPSxh6W8nPs6PW22xOI4KWqmJ5JLZfpI2lleBGfMLpQ2pxMUOj8UW7981h146zwfzyWxbYjui8LuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbyCuHq",
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
  "id": -576460752303423207,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBdtei+sZg8ywPSxh6W8nPs6PW22xOI4KWqmJ5JLZfpI2lleBGfMLpQ2pxMUOj8UW7981h146zwfzyWxbYjui8LuEDtsAs8YxzixuPfhNv/AuWlUviFJJtUcR2xpaomOUNoQdJJ5sYiamXIUepfx13Q9A9PCCxuP3Ue920+N8bcNUwCuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYBqBrv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423207,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuEBdtei+sZg8ywPSxh6W8nPs6PW22xOI4KWqmJ5JLZfpI2lleBGfMLpQ2pxMUOj8UW7981h146zwfzyWxbYjui8LuEDtsAs8YxzixuPfhNv/AuWlUviFJJtUcR2xpaomOUNoQdJJ5sYiamXIUepfx13Q9A9PCCxuP3Ue920+N8bcNUwCuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYBqBrv"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuEBdtei+sZg8ywPSxh6W8nPs6PW22xOI4KWqmJ5JLZfpI2lleBGfMLpQ2pxMUOj8UW7981h146zwfzyWxbYjui8LuEDtsAs8YxzixuPfhNv/AuWlUviFJJtUcR2xpaomOUNoQdJJ5sYiamXIUepfx13Q9A9PCCxuP3Ue920+N8bcNUwCuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYBqBrv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423206,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423206,
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
  "id": -576460752303423205,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423205,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBdtei+sZg8ywPSxh6W8nPs6PW22xOI4KWqmJ5JLZfpI2lleBGfMLpQ2pxMUOj8UW7981h146zwfzyWxbYjui8LuEDtsAs8YxzixuPfhNv/AuWlUviFJJtUcR2xpaomOUNoQdJJ5sYiamXIUepfx13Q9A9PCCxuP3Ue920+N8bcNUwCuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYBqBrv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423204,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423204,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBo2Bknyl1Hdp5FKxMWpGWVJ+nfAwAIn0TZWjPkaQ1eylBKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYI9xe60=",
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
  "id": -576460752303423203,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBqim78lxIhHEwgOM+Hc6wpI+7BACgnsYFldRI7lWIy+Dt3z8pXP8aDaYU+0mRXXveDzeYXJO9zDqZLmY6qfZwPuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCs+eH3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423203,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBqim78lxIhHEwgOM+Hc6wpI+7BACgnsYFldRI7lWIy+Dt3z8pXP8aDaYU+0mRXXveDzeYXJO9zDqZLmY6qfZwPuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCs+eH3",
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
  "id": -576460752303423202,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBqim78lxIhHEwgOM+Hc6wpI+7BACgnsYFldRI7lWIy+Dt3z8pXP8aDaYU+0mRXXveDzeYXJO9zDqZLmY6qfZwPuEDDoP1+U1LkN44D5syo2EKzOMSbRbinXUe6nxe0Tf4OdEDa1j5DmFm1GUUEeB9si1MZGBVuJiJ3kr9lK5btqNIMuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCvsWeR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423202,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuEBqim78lxIhHEwgOM+Hc6wpI+7BACgnsYFldRI7lWIy+Dt3z8pXP8aDaYU+0mRXXveDzeYXJO9zDqZLmY6qfZwPuEDDoP1+U1LkN44D5syo2EKzOMSbRbinXUe6nxe0Tf4OdEDa1j5DmFm1GUUEeB9si1MZGBVuJiJ3kr9lK5btqNIMuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCvsWeR"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuEBqim78lxIhHEwgOM+Hc6wpI+7BACgnsYFldRI7lWIy+Dt3z8pXP8aDaYU+0mRXXveDzeYXJO9zDqZLmY6qfZwPuEDDoP1+U1LkN44D5syo2EKzOMSbRbinXUe6nxe0Tf4OdEDa1j5DmFm1GUUEeB9si1MZGBVuJiJ3kr9lK5btqNIMuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCvsWeR"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423201,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423201,
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
  "id": -576460752303423200,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423200,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBqim78lxIhHEwgOM+Hc6wpI+7BACgnsYFldRI7lWIy+Dt3z8pXP8aDaYU+0mRXXveDzeYXJO9zDqZLmY6qfZwPuEDDoP1+U1LkN44D5syo2EKzOMSbRbinXUe6nxe0Tf4OdEDa1j5DmFm1GUUEeB9si1MZGBVuJiJ3kr9lK5btqNIMuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCvsWeR",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423199,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423199,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBo2Bknyl1Hdp5FKxMWpGWVJ+nfAwAIn0TZWjPkaQ1eylBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rpyxdos=",
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
  "id": -576460752303423198,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDewttqfl2Ko3yysb95LTrc4aesuFmd8WMNes2ssWspW6xiDNJyPEW/CwMwzIAhUnyPDGelaq9n3uhIx/WCN08CuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbbTFvJ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423198,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDewttqfl2Ko3yysb95LTrc4aesuFmd8WMNes2ssWspW6xiDNJyPEW/CwMwzIAhUnyPDGelaq9n3uhIx/WCN08CuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbbTFvJ",
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
  "id": -576460752303423197,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECaP9pBf0CXvymflOSKIr2+ropjmCAuG8p61U8lZRn2+1bSsxA6lMhmAcioSCuCWl+3n3QSrcZciHxl9zWH3mkGuEDewttqfl2Ko3yysb95LTrc4aesuFmd8WMNes2ssWspW6xiDNJyPEW/CwMwzIAhUnyPDGelaq9n3uhIx/WCN08CuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbPP+9I"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423197,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuECaP9pBf0CXvymflOSKIr2+ropjmCAuG8p61U8lZRn2+1bSsxA6lMhmAcioSCuCWl+3n3QSrcZciHxl9zWH3mkGuEDewttqfl2Ko3yysb95LTrc4aesuFmd8WMNes2ssWspW6xiDNJyPEW/CwMwzIAhUnyPDGelaq9n3uhIx/WCN08CuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbPP+9I"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuECaP9pBf0CXvymflOSKIr2+ropjmCAuG8p61U8lZRn2+1bSsxA6lMhmAcioSCuCWl+3n3QSrcZciHxl9zWH3mkGuEDewttqfl2Ko3yysb95LTrc4aesuFmd8WMNes2ssWspW6xiDNJyPEW/CwMwzIAhUnyPDGelaq9n3uhIx/WCN08CuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbPP+9I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423196,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423196,
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
  "id": -576460752303423195,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423195,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECaP9pBf0CXvymflOSKIr2+ropjmCAuG8p61U8lZRn2+1bSsxA6lMhmAcioSCuCWl+3n3QSrcZciHxl9zWH3mkGuEDewttqfl2Ko3yysb95LTrc4aesuFmd8WMNes2ssWspW6xiDNJyPEW/CwMwzIAhUnyPDGelaq9n3uhIx/WCN08CuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbPP+9I",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423194,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423194,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBo2Bknyl1Hdp5FKxMWpGWVJ+nfAwAIn0TZWjPkaQ1eylBqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYGiz9kc=",
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
  "id": -576460752303423193,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDW3CwHB4j8L3Oj5eUEuyXI4wmVv1K5W4LBTvswEwpNYqdhvZPIS8bCnQehqMsCYycBMoh677knKb17zPt2beEIuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWB6A59m"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423193,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDW3CwHB4j8L3Oj5eUEuyXI4wmVv1K5W4LBTvswEwpNYqdhvZPIS8bCnQehqMsCYycBMoh677knKb17zPt2beEIuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWB6A59m",
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
  "id": -576460752303423192,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDW3CwHB4j8L3Oj5eUEuyXI4wmVv1K5W4LBTvswEwpNYqdhvZPIS8bCnQehqMsCYycBMoh677knKb17zPt2beEIuEDhif3Y7ffaYoJPW4lZK9wV4+B1A/OaMH0HmBqxHhisYtOdQrUcRFEYnSE1rK+RZ9i7glGgIBKYvfzzxJwXNkUDuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCQcxop"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423192,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuEDW3CwHB4j8L3Oj5eUEuyXI4wmVv1K5W4LBTvswEwpNYqdhvZPIS8bCnQehqMsCYycBMoh677knKb17zPt2beEIuEDhif3Y7ffaYoJPW4lZK9wV4+B1A/OaMH0HmBqxHhisYtOdQrUcRFEYnSE1rK+RZ9i7glGgIBKYvfzzxJwXNkUDuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCQcxop"
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
    "data": {
      "state": "tx_+NILAfiEuEDW3CwHB4j8L3Oj5eUEuyXI4wmVv1K5W4LBTvswEwpNYqdhvZPIS8bCnQehqMsCYycBMoh677knKb17zPt2beEIuEDhif3Y7ffaYoJPW4lZK9wV4+B1A/OaMH0HmBqxHhisYtOdQrUcRFEYnSE1rK+RZ9i7glGgIBKYvfzzxJwXNkUDuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCQcxop"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423191,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423191,
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
  "id": -576460752303423190,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423190,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDW3CwHB4j8L3Oj5eUEuyXI4wmVv1K5W4LBTvswEwpNYqdhvZPIS8bCnQehqMsCYycBMoh677knKb17zPt2beEIuEDhif3Y7ffaYoJPW4lZK9wV4+B1A/OaMH0HmBqxHhisYtOdQrUcRFEYnSE1rK+RZ9i7glGgIBKYvfzzxJwXNkUDuEj4RjkCoQaNgZJ8pdR3aeRSsTFqRllSfp3wMACJ9E2Voz5GkNXspQag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCQcxop",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423189,
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423189,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423188,
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
    "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
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
  "channel_id": "ch_25Kau8ciLow6wX2kj7bMNNETf33EAzaMuXN88AmZ24VAnkyJLa",
  "id": -576460752303423188,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
