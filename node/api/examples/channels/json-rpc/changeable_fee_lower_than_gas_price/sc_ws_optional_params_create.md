
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=1&gas_price=1000001234&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator
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
      "fsm_id": "ba_xyC4hgLHOeajGwAUEXx0a2VPaWjU6zNcOZLeb+VQExSwgvha"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=1&gas_price=1000001234&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder
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
      "fsm_id": "ba_dSqZA1Lihlx962+zt5cxuF1nPX0gxL8NO2gF5SDMYae9kEVa"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeyMN6MCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ/nJp8gw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422403,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDYSFpaT4VrwSsSJsvqY7QFExNFpkMDX2csKsxBrBvd5Q8rgKfqTRgBcXqVndoaIDt5WwuPF8F0EBUFIRfmLoQFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnsjDejAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGfwlXOlc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422403,
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_dSqZA1Lihlx962+zt5cxuF1nPX0gxL8NO2gF5SDMYae9kEVa"
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDYSFpaT4VrwSsSJsvqY7QFExNFpkMDX2csKsxBrBvd5Q8rgKfqTRgBcXqVndoaIDt5WwuPF8F0EBUFIRfmLoQFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnsjDejAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGfwlXOlc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422402,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAxI+bHjWQFs1D5spamU9IYJcKSTyL1GYAN6m8FATpz8dyEhkkNOdkGCLT5MsbjYs2EOchRi2mHZ6e0oR+00O0C7hA2EhaWk+Fa8ErEibL6mO0BRMTRaZDA19nLCrMQawb3eUPK4Cn6k0YAXF6lZ3aGiA7eVsLjxfBdBAVBSEX5i6EBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rn/ut9+H"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
  "id": -576460752303422402,
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAxI+bHjWQFs1D5spamU9IYJcKSTyL1GYAN6m8FATpz8dyEhkkNOdkGCLT5MsbjYs2EOchRi2mHZ6e0oR+00O0C7hA2EhaWk+Fa8ErEibL6mO0BRMTRaZDA19nLCrMQawb3eUPK4Cn6k0YAXF6lZ3aGiA7eVsLjxfBdBAVBSEX5i6EBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rn/ut9+H",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_xyC4hgLHOeajGwAUEXx0a2VPaWjU6zNcOZLeb+VQExSwgvha"
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAxI+bHjWQFs1D5spamU9IYJcKSTyL1GYAN6m8FATpz8dyEhkkNOdkGCLT5MsbjYs2EOchRi2mHZ6e0oR+00O0C7hA2EhaWk+Fa8ErEibL6mO0BRMTRaZDA19nLCrMQawb3eUPK4Cn6k0YAXF6lZ3aGiA7eVsLjxfBdBAVBSEX5i6EBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rn/ut9+H",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAxI+bHjWQFs1D5spamU9IYJcKSTyL1GYAN6m8FATpz8dyEhkkNOdkGCLT5MsbjYs2EOchRi2mHZ6e0oR+00O0C7hA2EhaWk+Fa8ErEibL6mO0BRMTRaZDA19nLCrMQawb3eUPK4Cn6k0YAXF6lZ3aGiA7eVsLjxfBdBAVBSEX5i6EBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rn/ut9+H",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAxI+bHjWQFs1D5spamU9IYJcKSTyL1GYAN6m8FATpz8dyEhkkNOdkGCLT5MsbjYs2EOchRi2mHZ6e0oR+00O0C7hA2EhaWk+Fa8ErEibL6mO0BRMTRaZDA19nLCrMQawb3eUPK4Cn6k0YAXF6lZ3aGiA7eVsLjxfBdBAVBSEX5i6EBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rn/ut9+H",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "message": {
        "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "message": {
        "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
  "id": -576460752303422401,
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
  "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
  "id": -576460752303422401,
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "state": "tx_+QENCwH4hLhAxI+bHjWQFs1D5spamU9IYJcKSTyL1GYAN6m8FATpz8dyEhkkNOdkGCLT5MsbjYs2EOchRi2mHZ6e0oR+00O0C7hA2EhaWk+Fa8ErEibL6mO0BRMTRaZDA19nLCrMQawb3eUPK4Cn6k0YAXF6lZ3aGiA7eVsLjxfBdBAVBSEX5i6EBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rn/ut9+H"
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "state": "tx_+QENCwH4hLhAxI+bHjWQFs1D5spamU9IYJcKSTyL1GYAN6m8FATpz8dyEhkkNOdkGCLT5MsbjYs2EOchRi2mHZ6e0oR+00O0C7hA2EhaWk+Fa8ErEibL6mO0BRMTRaZDA19nLCrMQawb3eUPK4Cn6k0YAXF6lZ3aGiA7eVsLjxfBdBAVBSEX5i6EBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rn/ut9+H"
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBrV0RN6zOxP4iq94mxg+OYRq0yaDGsItQSUkrPruPD8CoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBgMrmisg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422400,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEAWtw/rXk3cNPdiM7S1V/zDYp4yY/m1myH1GoL9LvheCeG4Mobsd1TqCm5c3KHzDRRsUmFPfDNqkPezG2mmBHQNuGD4XjUBoQa1dETeszsT+IqveJsYPjmEatMmgxrCLUElJKz67jw/AqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYBdedJ4"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
  "id": -576460752303422400,
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEAWtw/rXk3cNPdiM7S1V/zDYp4yY/m1myH1GoL9LvheCeG4Mobsd1TqCm5c3KHzDRRsUmFPfDNqkPezG2mmBHQNuGD4XjUBoQa1dETeszsT+IqveJsYPjmEatMmgxrCLUElJKz67jw/AqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYBdedJ4",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422399,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAWtw/rXk3cNPdiM7S1V/zDYp4yY/m1myH1GoL9LvheCeG4Mobsd1TqCm5c3KHzDRRsUmFPfDNqkPezG2mmBHQNuED9RK0r2IA+5TfhaWEAskrlEIhO/nxsFSy9FyJkUZC6D8flQByI7yJJSEDMLIMIZhUdeAIJXpKbJ0yVLPf62NwCuGD4XjUBoQa1dETeszsT+IqveJsYPjmEatMmgxrCLUElJKz67jw/AqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCvLWMu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
  "id": -576460752303422399,
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAWtw/rXk3cNPdiM7S1V/zDYp4yY/m1myH1GoL9LvheCeG4Mobsd1TqCm5c3KHzDRRsUmFPfDNqkPezG2mmBHQNuED9RK0r2IA+5TfhaWEAskrlEIhO/nxsFSy9FyJkUZC6D8flQByI7yJJSEDMLIMIZhUdeAIJXpKbJ0yVLPf62NwCuGD4XjUBoQa1dETeszsT+IqveJsYPjmEatMmgxrCLUElJKz67jw/AqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCvLWMu",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAWtw/rXk3cNPdiM7S1V/zDYp4yY/m1myH1GoL9LvheCeG4Mobsd1TqCm5c3KHzDRRsUmFPfDNqkPezG2mmBHQNuED9RK0r2IA+5TfhaWEAskrlEIhO/nxsFSy9FyJkUZC6D8flQByI7yJJSEDMLIMIZhUdeAIJXpKbJ0yVLPf62NwCuGD4XjUBoQa1dETeszsT+IqveJsYPjmEatMmgxrCLUElJKz67jw/AqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCvLWMu",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAWtw/rXk3cNPdiM7S1V/zDYp4yY/m1myH1GoL9LvheCeG4Mobsd1TqCm5c3KHzDRRsUmFPfDNqkPezG2mmBHQNuED9RK0r2IA+5TfhaWEAskrlEIhO/nxsFSy9FyJkUZC6D8flQByI7yJJSEDMLIMIZhUdeAIJXpKbJ0yVLPf62NwCuGD4XjUBoQa1dETeszsT+IqveJsYPjmEatMmgxrCLUElJKz67jw/AqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCvLWMu",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAWtw/rXk3cNPdiM7S1V/zDYp4yY/m1myH1GoL9LvheCeG4Mobsd1TqCm5c3KHzDRRsUmFPfDNqkPezG2mmBHQNuED9RK0r2IA+5TfhaWEAskrlEIhO/nxsFSy9FyJkUZC6D8flQByI7yJJSEDMLIMIZhUdeAIJXpKbJ0yVLPf62NwCuGD4XjUBoQa1dETeszsT+IqveJsYPjmEatMmgxrCLUElJKz67jw/AqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCvLWMu",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
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
    "channel_id": "ch_2Nv1CPXdNohgd1AoMptW7hhLpPLLLvPSrqQarMwZ344bzms4sF",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
