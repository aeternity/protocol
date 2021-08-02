
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator
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
      "fsm_id": "ba_BQROqtlSleX/6E+JLEvU2GbXZDIcr4IpuRcEaEG3KR2CHU9a"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder
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
      "fsm_id": "ba_Sl/1cz6aqxIpKHeYbxuzkqaoCnlk/cIoC5cziyf3DCXqZv12"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYCA3r2uw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423486,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAzjJUPh4xANB9Pi5xdNzG9JQXIvlZH+fvJ7Qf5lqPdQkicRV1jNkS4h/G7w/TIroneZmtpkDT5tTk7kV76A34LuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGApueiP4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423486,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_Sl/1cz6aqxIpKHeYbxuzkqaoCnlk/cIoC5cziyf3DCXqZv12"
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAzjJUPh4xANB9Pi5xdNzG9JQXIvlZH+fvJ7Qf5lqPdQkicRV1jNkS4h/G7w/TIroneZmtpkDT5tTk7kV76A34LuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGApueiP4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAM4yVD4eMQDQfT4ucXTcxvSUFyL5WR/n7ye0H+Zaj3UJInEVdYzZEuIfxu8P0yK6J3mZraZA0+bU5O5Fe+gN+C7hAhkkaEIHDoecZvVYFM2gggOfDE45MZQ4NKIsWg9hh8k1VaqAC7o1n6T7+hfUbaw0Btx15eseu6kscpLy0FbWCDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgIlFr9i"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423485,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAM4yVD4eMQDQfT4ucXTcxvSUFyL5WR/n7ye0H+Zaj3UJInEVdYzZEuIfxu8P0yK6J3mZraZA0+bU5O5Fe+gN+C7hAhkkaEIHDoecZvVYFM2gggOfDE45MZQ4NKIsWg9hh8k1VaqAC7o1n6T7+hfUbaw0Btx15eseu6kscpLy0FbWCDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgIlFr9i",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_BQROqtlSleX/6E+JLEvU2GbXZDIcr4IpuRcEaEG3KR2CHU9a"
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAM4yVD4eMQDQfT4ucXTcxvSUFyL5WR/n7ye0H+Zaj3UJInEVdYzZEuIfxu8P0yK6J3mZraZA0+bU5O5Fe+gN+C7hAhkkaEIHDoecZvVYFM2gggOfDE45MZQ4NKIsWg9hh8k1VaqAC7o1n6T7+hfUbaw0Btx15eseu6kscpLy0FbWCDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgIlFr9i",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAM4yVD4eMQDQfT4ucXTcxvSUFyL5WR/n7ye0H+Zaj3UJInEVdYzZEuIfxu8P0yK6J3mZraZA0+bU5O5Fe+gN+C7hAhkkaEIHDoecZvVYFM2gggOfDE45MZQ4NKIsWg9hh8k1VaqAC7o1n6T7+hfUbaw0Btx15eseu6kscpLy0FbWCDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgIlFr9i",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAM4yVD4eMQDQfT4ucXTcxvSUFyL5WR/n7ye0H+Zaj3UJInEVdYzZEuIfxu8P0yK6J3mZraZA0+bU5O5Fe+gN+C7hAhkkaEIHDoecZvVYFM2gggOfDE45MZQ4NKIsWg9hh8k1VaqAC7o1n6T7+hfUbaw0Btx15eseu6kscpLy0FbWCDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgIlFr9i",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+QENCwH4hLhAM4yVD4eMQDQfT4ucXTcxvSUFyL5WR/n7ye0H+Zaj3UJInEVdYzZEuIfxu8P0yK6J3mZraZA0+bU5O5Fe+gN+C7hAhkkaEIHDoecZvVYFM2gggOfDE45MZQ4NKIsWg9hh8k1VaqAC7o1n6T7+hfUbaw0Btx15eseu6kscpLy0FbWCDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgIlFr9i"
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+QENCwH4hLhAM4yVD4eMQDQfT4ucXTcxvSUFyL5WR/n7ye0H+Zaj3UJInEVdYzZEuIfxu8P0yK6J3mZraZA0+bU5O5Fe+gN+C7hAhkkaEIHDoecZvVYFM2gggOfDE45MZQ4NKIsWg9hh8k1VaqAC7o1n6T7+hfUbaw0Btx15eseu6kscpLy0FbWCDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgIlFr9i"
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "message": {
        "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "message": {
        "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "id": -576460752303423484,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423484,
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
  "id": -576460752303423483,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423483,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl8UdfJHKq3VljU1U6yr/P9hQF9UzS9aveVcpjGgugS8AqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCykPMpWs=",
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
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC1SlzQrZiqXvcbWycpUWWYDtyw8ktWiLqQKztGlaQNIGhDG7WWofOGcYWha7slS9P0sd5Hu0FD8wnN6c72xVsNuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspTTrS0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423482,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC1SlzQrZiqXvcbWycpUWWYDtyw8ktWiLqQKztGlaQNIGhDG7WWofOGcYWha7slS9P0sd5Hu0FD8wnN6c72xVsNuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspTTrS0",
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
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBwrPjYOy+SuM06EyW9Jz0vuWU67Y5yYZxlWmn+WY/EKlUQPllYOlKz5B1Y9dbXNReAaJTfa6szvpvqx76D/PAGuEC1SlzQrZiqXvcbWycpUWWYDtyw8ktWiLqQKztGlaQNIGhDG7WWofOGcYWha7slS9P0sd5Hu0FD8wnN6c72xVsNuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQso8X0QS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423481,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuEBwrPjYOy+SuM06EyW9Jz0vuWU67Y5yYZxlWmn+WY/EKlUQPllYOlKz5B1Y9dbXNReAaJTfa6szvpvqx76D/PAGuEC1SlzQrZiqXvcbWycpUWWYDtyw8ktWiLqQKztGlaQNIGhDG7WWofOGcYWha7slS9P0sd5Hu0FD8wnN6c72xVsNuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQso8X0QS"
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuEBwrPjYOy+SuM06EyW9Jz0vuWU67Y5yYZxlWmn+WY/EKlUQPllYOlKz5B1Y9dbXNReAaJTfa6szvpvqx76D/PAGuEC1SlzQrZiqXvcbWycpUWWYDtyw8ktWiLqQKztGlaQNIGhDG7WWofOGcYWha7slS9P0sd5Hu0FD8wnN6c72xVsNuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQso8X0QS"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423480,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423480,
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
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBwrPjYOy+SuM06EyW9Jz0vuWU67Y5yYZxlWmn+WY/EKlUQPllYOlKz5B1Y9dbXNReAaJTfa6szvpvqx76D/PAGuEC1SlzQrZiqXvcbWycpUWWYDtyw8ktWiLqQKztGlaQNIGhDG7WWofOGcYWha7slS9P0sd5Hu0FD8wnN6c72xVsNuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQso8X0QS",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423478,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423478,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl8UdfJHKq3VljU1U6yr/P9hQF9UzS9aveVcpjGgugS8A6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RrqBb5M=",
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
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECwQVz2EO13XzvjLjeI9IMrdixN/euYSNYF9v9yTLjf9ejIbrI7pbuPaL5PFLjv3ZgC0dgSazeU3utGbXjRsi8OuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZtDXd1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423477,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+JALAfhCuECwQVz2EO13XzvjLjeI9IMrdixN/euYSNYF9v9yTLjf9ejIbrI7pbuPaL5PFLjv3ZgC0dgSazeU3utGbXjRsi8OuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZtDXd1",
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
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBN5Jcz+o8Hxn8lf3TjIdhjMBUQBE5dhWjzOakvRWCud7N0K9yjG00jAtw+Svff1eFHUjrj4+p46BsqpLoolAUHuECwQVz2EO13XzvjLjeI9IMrdixN/euYSNYF9v9yTLjf9ejIbrI7pbuPaL5PFLjv3ZgC0dgSazeU3utGbXjRsi8OuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa0Y0au"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423476,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuEBN5Jcz+o8Hxn8lf3TjIdhjMBUQBE5dhWjzOakvRWCud7N0K9yjG00jAtw+Svff1eFHUjrj4+p46BsqpLoolAUHuECwQVz2EO13XzvjLjeI9IMrdixN/euYSNYF9v9yTLjf9ejIbrI7pbuPaL5PFLjv3ZgC0dgSazeU3utGbXjRsi8OuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa0Y0au"
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuEBN5Jcz+o8Hxn8lf3TjIdhjMBUQBE5dhWjzOakvRWCud7N0K9yjG00jAtw+Svff1eFHUjrj4+p46BsqpLoolAUHuECwQVz2EO13XzvjLjeI9IMrdixN/euYSNYF9v9yTLjf9ejIbrI7pbuPaL5PFLjv3ZgC0dgSazeU3utGbXjRsi8OuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa0Y0au"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423475,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423475,
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
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBN5Jcz+o8Hxn8lf3TjIdhjMBUQBE5dhWjzOakvRWCud7N0K9yjG00jAtw+Svff1eFHUjrj4+p46BsqpLoolAUHuECwQVz2EO13XzvjLjeI9IMrdixN/euYSNYF9v9yTLjf9ejIbrI7pbuPaL5PFLjv3ZgC0dgSazeU3utGbXjRsi8OuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa0Y0au",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423473,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423473,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl8UdfJHKq3VljU1U6yr/P9hQF9UzS9aveVcpjGgugS8BKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYMxMtq4=",
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
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECEcTI4hMQZAHGzgV2ka95ys9IWRdH3S0f6r3p5TFXFtt1tmh3/spMoWl3EDoLbGLdgmEvGRcqvr6aoDidavlcKuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDzj1Dd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423472,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+JALAfhCuECEcTI4hMQZAHGzgV2ka95ys9IWRdH3S0f6r3p5TFXFtt1tmh3/spMoWl3EDoLbGLdgmEvGRcqvr6aoDidavlcKuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDzj1Dd",
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
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAvMEP57G6xHAe6h1nPv35xOQOUGT6qyMHe5col72TJJH+smIDBQMzYsvD98g1kkS0CJFRTtBQGlBkdFJjeS9cJuECEcTI4hMQZAHGzgV2ka95ys9IWRdH3S0f6r3p5TFXFtt1tmh3/spMoWl3EDoLbGLdgmEvGRcqvr6aoDidavlcKuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBpxrt/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423471,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuEAvMEP57G6xHAe6h1nPv35xOQOUGT6qyMHe5col72TJJH+smIDBQMzYsvD98g1kkS0CJFRTtBQGlBkdFJjeS9cJuECEcTI4hMQZAHGzgV2ka95ys9IWRdH3S0f6r3p5TFXFtt1tmh3/spMoWl3EDoLbGLdgmEvGRcqvr6aoDidavlcKuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBpxrt/"
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuEAvMEP57G6xHAe6h1nPv35xOQOUGT6qyMHe5col72TJJH+smIDBQMzYsvD98g1kkS0CJFRTtBQGlBkdFJjeS9cJuECEcTI4hMQZAHGzgV2ka95ys9IWRdH3S0f6r3p5TFXFtt1tmh3/spMoWl3EDoLbGLdgmEvGRcqvr6aoDidavlcKuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBpxrt/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423470,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423470,
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
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAvMEP57G6xHAe6h1nPv35xOQOUGT6qyMHe5col72TJJH+smIDBQMzYsvD98g1kkS0CJFRTtBQGlBkdFJjeS9cJuECEcTI4hMQZAHGzgV2ka95ys9IWRdH3S0f6r3p5TFXFtt1tmh3/spMoWl3EDoLbGLdgmEvGRcqvr6aoDidavlcKuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvASg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBpxrt/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423468,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423468,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl8UdfJHKq3VljU1U6yr/P9hQF9UzS9aveVcpjGgugS8BaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RvE/Wb0=",
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
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECvFuOllZg2tXo6Gohg8vjSs70k+MQr1WMLXywEMFwSB4e+d0w4psx0wOG4RIbOzopIuPQKZztJthmK1F/pamAIuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYmmuCU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423467,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+JALAfhCuECvFuOllZg2tXo6Gohg8vjSs70k+MQr1WMLXywEMFwSB4e+d0w4psx0wOG4RIbOzopIuPQKZztJthmK1F/pamAIuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYmmuCU",
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
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECvFuOllZg2tXo6Gohg8vjSs70k+MQr1WMLXywEMFwSB4e+d0w4psx0wOG4RIbOzopIuPQKZztJthmK1F/pamAIuEDujh6ObV7y9cpwGntX1VUvegc37z/+QFWyKjTOGfdM+u670pMtqMZTzlFzWJMH/fNzl+dDmtqViBPryBiOsmQCuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb0PZxr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423466,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuECvFuOllZg2tXo6Gohg8vjSs70k+MQr1WMLXywEMFwSB4e+d0w4psx0wOG4RIbOzopIuPQKZztJthmK1F/pamAIuEDujh6ObV7y9cpwGntX1VUvegc37z/+QFWyKjTOGfdM+u670pMtqMZTzlFzWJMH/fNzl+dDmtqViBPryBiOsmQCuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb0PZxr"
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuECvFuOllZg2tXo6Gohg8vjSs70k+MQr1WMLXywEMFwSB4e+d0w4psx0wOG4RIbOzopIuPQKZztJthmK1F/pamAIuEDujh6ObV7y9cpwGntX1VUvegc37z/+QFWyKjTOGfdM+u670pMtqMZTzlFzWJMH/fNzl+dDmtqViBPryBiOsmQCuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb0PZxr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423465,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423465,
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
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECvFuOllZg2tXo6Gohg8vjSs70k+MQr1WMLXywEMFwSB4e+d0w4psx0wOG4RIbOzopIuPQKZztJthmK1F/pamAIuEDujh6ObV7y9cpwGntX1VUvegc37z/+QFWyKjTOGfdM+u670pMtqMZTzlFzWJMH/fNzl+dDmtqViBPryBiOsmQCuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEb0PZxr",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423463,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423463,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl8UdfJHKq3VljU1U6yr/P9hQF9UzS9aveVcpjGgugS8BqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYI4A93s=",
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
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDIqMILM/vwx1Uz/7k8634ilQJPzE68TbriHCCH6CNaaWGkpHn8ea1LA2zqTnk0iXiSkbniWve9OZUK0eOG+mkFuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAxXmO1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423462,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDIqMILM/vwx1Uz/7k8634ilQJPzE68TbriHCCH6CNaaWGkpHn8ea1LA2zqTnk0iXiSkbniWve9OZUK0eOG+mkFuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAxXmO1",
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
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBFAdhZNgC4dDfPBJghxJNacVIZxmXSEzuhPjTrTJKOfj+BjTYat6gohcB+qrkrZ8oeLk8uaZGm1/XIf7H2b90HuEDIqMILM/vwx1Uz/7k8634ilQJPzE68TbriHCCH6CNaaWGkpHn8ea1LA2zqTnk0iXiSkbniWve9OZUK0eOG+mkFuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAlu+NJ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423461,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuEBFAdhZNgC4dDfPBJghxJNacVIZxmXSEzuhPjTrTJKOfj+BjTYat6gohcB+qrkrZ8oeLk8uaZGm1/XIf7H2b90HuEDIqMILM/vwx1Uz/7k8634ilQJPzE68TbriHCCH6CNaaWGkpHn8ea1LA2zqTnk0iXiSkbniWve9OZUK0eOG+mkFuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAlu+NJ"
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
    "data": {
      "state": "tx_+NILAfiEuEBFAdhZNgC4dDfPBJghxJNacVIZxmXSEzuhPjTrTJKOfj+BjTYat6gohcB+qrkrZ8oeLk8uaZGm1/XIf7H2b90HuEDIqMILM/vwx1Uz/7k8634ilQJPzE68TbriHCCH6CNaaWGkpHn8ea1LA2zqTnk0iXiSkbniWve9OZUK0eOG+mkFuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAlu+NJ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423460,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423460,
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
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBFAdhZNgC4dDfPBJghxJNacVIZxmXSEzuhPjTrTJKOfj+BjTYat6gohcB+qrkrZ8oeLk8uaZGm1/XIf7H2b90HuEDIqMILM/vwx1Uz/7k8634ilQJPzE68TbriHCCH6CNaaWGkpHn8ea1LA2zqTnk0iXiSkbniWve9OZUK0eOG+mkFuEj4RjkCoQZfFHXyRyqt1ZY1NVOsq/z/YUBfVM0vWr3lXKYxoLoEvAag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAlu+NJ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423458,
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423457,
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
    "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
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
  "channel_id": "ch_isgy25rokiTRjwtvBJJjmNUD9NBLr42Af38DYSec6jzQaua96",
  "id": -576460752303423457,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
