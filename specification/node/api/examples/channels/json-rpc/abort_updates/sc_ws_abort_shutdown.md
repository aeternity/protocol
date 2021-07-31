
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
      "fsm_id": "ba_mSN5KSeZUeiP2rfrfaU19lLQjcgGqEMIU28jFqZ6ryrNsXT7"
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
      "fsm_id": "ba_qTeLw0Owf9apCBl53l6UurPndFgQcDwbI2hXog1FJnRo93r9"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBu9RsTf4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422086,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuED+3yfwLUfl3cMCAbW+kidU0KUkxGax2EsTn4A9QXNI95GSKAEHYBN9bH044M0FjqSdUn0TCNKxpq8HnFOKlH4AuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbtwTXkQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422086,
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_qTeLw0Owf9apCBl53l6UurPndFgQcDwbI2hXog1FJnRo93r9"
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "signed_tx": "tx_+MwLAfhCuED+3yfwLUfl3cMCAbW+kidU0KUkxGax2EsTn4A9QXNI95GSKAEHYBN9bH044M0FjqSdUn0TCNKxpq8HnFOKlH4AuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbtwTXkQ",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422085,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhA79tf7DfgCJu/wiLTkx6LyoC4wd3MCebTQZHxRjOQvID2PW+Kt6b1NEWpJsENeAIoo/MRoKLj9isnnLoH/3xmCLhA/t8n8C1H5d3DAgG1vpInVNClJMRmsdhLE5+APUFzSPeRkigBB2ATfWx9OODNBY6knVJ9EwjSsaavB5xTipR+ALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG7epJgHg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
  "id": -576460752303422085,
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhA79tf7DfgCJu/wiLTkx6LyoC4wd3MCebTQZHxRjOQvID2PW+Kt6b1NEWpJsENeAIoo/MRoKLj9isnnLoH/3xmCLhA/t8n8C1H5d3DAgG1vpInVNClJMRmsdhLE5+APUFzSPeRkigBB2ATfWx9OODNBY6knVJ9EwjSsaavB5xTipR+ALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG7epJgHg==",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_mSN5KSeZUeiP2rfrfaU19lLQjcgGqEMIU28jFqZ6ryrNsXT7"
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhA79tf7DfgCJu/wiLTkx6LyoC4wd3MCebTQZHxRjOQvID2PW+Kt6b1NEWpJsENeAIoo/MRoKLj9isnnLoH/3xmCLhA/t8n8C1H5d3DAgG1vpInVNClJMRmsdhLE5+APUFzSPeRkigBB2ATfWx9OODNBY6knVJ9EwjSsaavB5xTipR+ALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG7epJgHg==",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhA79tf7DfgCJu/wiLTkx6LyoC4wd3MCebTQZHxRjOQvID2PW+Kt6b1NEWpJsENeAIoo/MRoKLj9isnnLoH/3xmCLhA/t8n8C1H5d3DAgG1vpInVNClJMRmsdhLE5+APUFzSPeRkigBB2ATfWx9OODNBY6knVJ9EwjSsaavB5xTipR+ALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG7epJgHg==",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhA79tf7DfgCJu/wiLTkx6LyoC4wd3MCebTQZHxRjOQvID2PW+Kt6b1NEWpJsENeAIoo/MRoKLj9isnnLoH/3xmCLhA/t8n8C1H5d3DAgG1vpInVNClJMRmsdhLE5+APUFzSPeRkigBB2ATfWx9OODNBY6knVJ9EwjSsaavB5xTipR+ALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG7epJgHg==",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "message": {
        "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "message": {
        "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
  "id": -576460752303422084,
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
  "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
  "id": -576460752303422084,
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "state": "tx_+QEOCwH4hLhA79tf7DfgCJu/wiLTkx6LyoC4wd3MCebTQZHxRjOQvID2PW+Kt6b1NEWpJsENeAIoo/MRoKLj9isnnLoH/3xmCLhA/t8n8C1H5d3DAgG1vpInVNClJMRmsdhLE5+APUFzSPeRkigBB2ATfWx9OODNBY6knVJ9EwjSsaavB5xTipR+ALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG7epJgHg=="
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "state": "tx_+QEOCwH4hLhA79tf7DfgCJu/wiLTkx6LyoC4wd3MCebTQZHxRjOQvID2PW+Kt6b1NEWpJsENeAIoo/MRoKLj9isnnLoH/3xmCLhA/t8n8C1H5d3DAgG1vpInVNClJMRmsdhLE5+APUFzSPeRkigBB2ATfWx9OODNBY6knVJ9EwjSsaavB5xTipR+ALiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG7epJgHg=="
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBgYIFerHM1JYR2AiPy8jyT/6rFp7p2AJvLAxdUIqcW9goQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBvKqOdW4=",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBgYIFerHM1JYR2AiPy8jyT/6rFp7p2AJvLAxdUIqcW9goQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY3+rniy/+GHLHOiuwBAIYPXtZ/KABBNYH6Ng==",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBgYIFerHM1JYR2AiPy8jyT/6rFp7p2AJvLAxdUIqcW9goQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBvKqOdW4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422083,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEAsmwmRw0WemEY70IB4TMmBCRbqmlmKwG1AISpS9KSXQ8YPC3ejGxz4OVspzW+vg0igyeXoVTiU2LyKqxRNLEAPuGD4XjUBoQYGCBXqxzNSWEdgIj8vI8k/+qxae6dgCbywMXVCKnFvYKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgbwoZTS9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
  "id": -576460752303422083,
  "jsonrpc": "2.0",
  "result": "ok",
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
  "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1018,
        "message": "Not allowed at current channel state"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.shutdown_sign",
      "params": {
        "error": 42
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEAsmwmRw0WemEY70IB4TMmBCRbqmlmKwG1AISpS9KSXQ8YPC3ejGxz4OVspzW+vg0igyeXoVTiU2LyKqxRNLEAPuGD4XjUBoQYGCBXqxzNSWEdgIj8vI8k/+qxae6dgCbywMXVCKnFvYKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgbwoZTS9",
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
  "method": "channels.shutdown_sign_ack",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
    "data": {
      "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
      "error_code": 42,
      "error_msg": "unknown",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422082,
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
  "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
  "id": -576460752303422082,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422081,
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
    "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
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
  "channel_id": "ch_3f4zCrFTFC81nCCu89ySMB4NEzZKJ91jUwf2LoNCJaNQR5FRf",
  "id": -576460752303422081,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
