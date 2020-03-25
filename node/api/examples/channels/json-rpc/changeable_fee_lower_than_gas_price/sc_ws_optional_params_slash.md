
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
      "fsm_id": "ba_QrXpEHyfSCjAYUZVSyZX+CGKq7B3cx4429WFuuYtW0u55hue"
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
      "fsm_id": "ba_2NnT0Wk6R3G8sz5mkX2GJEr0xuTpNi32uZUVIG6TmhTAx0ka"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBjWUGqws=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422335,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuED7L9BzeCVBfaSeJUPNFhIK0d1svragJTyPImcL2keo5ZikajXICbIgh1/UCu8bJhCvsW8/JoURffCecEMVPiQJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgY0MOXay"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422335,
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_2NnT0Wk6R3G8sz5mkX2GJEr0xuTpNi32uZUVIG6TmhTAx0ka"
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "signed_tx": "tx_+MwLAfhCuED7L9BzeCVBfaSeJUPNFhIK0d1svragJTyPImcL2keo5ZikajXICbIgh1/UCu8bJhCvsW8/JoURffCecEMVPiQJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgY0MOXay",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422334,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAcutPhW6YTG7itQRpN+Hi8PcfjuIZ7BcyNoAJOqVL01wUL4Ksg2lZgDYMJ/0Z9LFagFrSv1nS/4nTLJiuZopKCbhA+y/Qc3glQX2kniVDzRYSCtHdbL62oCU8jyJnC9pHqOWYpGo1yAmyIIdf1ArvGyYQr7FvPyaFEX3wnnBDFT4kCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGNixWjvw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
  "id": -576460752303422334,
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAcutPhW6YTG7itQRpN+Hi8PcfjuIZ7BcyNoAJOqVL01wUL4Ksg2lZgDYMJ/0Z9LFagFrSv1nS/4nTLJiuZopKCbhA+y/Qc3glQX2kniVDzRYSCtHdbL62oCU8jyJnC9pHqOWYpGo1yAmyIIdf1ArvGyYQr7FvPyaFEX3wnnBDFT4kCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGNixWjvw==",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_QrXpEHyfSCjAYUZVSyZX+CGKq7B3cx4429WFuuYtW0u55hue"
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAcutPhW6YTG7itQRpN+Hi8PcfjuIZ7BcyNoAJOqVL01wUL4Ksg2lZgDYMJ/0Z9LFagFrSv1nS/4nTLJiuZopKCbhA+y/Qc3glQX2kniVDzRYSCtHdbL62oCU8jyJnC9pHqOWYpGo1yAmyIIdf1ArvGyYQr7FvPyaFEX3wnnBDFT4kCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGNixWjvw==",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAcutPhW6YTG7itQRpN+Hi8PcfjuIZ7BcyNoAJOqVL01wUL4Ksg2lZgDYMJ/0Z9LFagFrSv1nS/4nTLJiuZopKCbhA+y/Qc3glQX2kniVDzRYSCtHdbL62oCU8jyJnC9pHqOWYpGo1yAmyIIdf1ArvGyYQr7FvPyaFEX3wnnBDFT4kCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGNixWjvw==",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAcutPhW6YTG7itQRpN+Hi8PcfjuIZ7BcyNoAJOqVL01wUL4Ksg2lZgDYMJ/0Z9LFagFrSv1nS/4nTLJiuZopKCbhA+y/Qc3glQX2kniVDzRYSCtHdbL62oCU8jyJnC9pHqOWYpGo1yAmyIIdf1ArvGyYQr7FvPyaFEX3wnnBDFT4kCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGNixWjvw==",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "message": {
        "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "message": {
        "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
  "id": -576460752303422333,
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
  "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
  "id": -576460752303422333,
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "state": "tx_+QEOCwH4hLhAcutPhW6YTG7itQRpN+Hi8PcfjuIZ7BcyNoAJOqVL01wUL4Ksg2lZgDYMJ/0Z9LFagFrSv1nS/4nTLJiuZopKCbhA+y/Qc3glQX2kniVDzRYSCtHdbL62oCU8jyJnC9pHqOWYpGo1yAmyIIdf1ArvGyYQr7FvPyaFEX3wnnBDFT4kCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGNixWjvw=="
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "state": "tx_+QEOCwH4hLhAcutPhW6YTG7itQRpN+Hi8PcfjuIZ7BcyNoAJOqVL01wUL4Ksg2lZgDYMJ/0Z9LFagFrSv1nS/4nTLJiuZopKCbhA+y/Qc3glQX2kniVDzRYSCtHdbL62oCU8jyJnC9pHqOWYpGo1yAmyIIdf1ArvGyYQr7FvPyaFEX3wnnBDFT4kCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGNixWjvw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAiWN1V"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422332,
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
  "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
  "id": -576460752303422332,
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiqMWMV04++rQ7n/75/zqUyA4x3Ffwq87ANqjSb0LWvzAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyud9if4=",
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
  "id": -576460752303422331,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBtFfeveh5hZQLcVF+MfNQ0OK/x3PDJo69WJy16ZFKf3VJawSAjPsxcDYzHGiQjAGUVZL7EwnbXK+wEZOQcXzYKuEj4RjkCoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r8wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqBkIL1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
  "id": -576460752303422331,
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBtFfeveh5hZQLcVF+MfNQ0OK/x3PDJo69WJy16ZFKf3VJawSAjPsxcDYzHGiQjAGUVZL7EwnbXK+wEZOQcXzYKuEj4RjkCoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r8wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqBkIL1",
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
  "id": -576460752303422330,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBtFfeveh5hZQLcVF+MfNQ0OK/x3PDJo69WJy16ZFKf3VJawSAjPsxcDYzHGiQjAGUVZL7EwnbXK+wEZOQcXzYKuEC5y1SggTnUWsQwBmuhD2OJkGYrESEMaEwmz2x+B7i66V5VoRqJ6LLZJgBkqIJlO0EyareiRWb8FYGKfYz3wT4FuEj4RjkCoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r8wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrVm11b"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
  "id": -576460752303422330,
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "state": "tx_+NILAfiEuEBtFfeveh5hZQLcVF+MfNQ0OK/x3PDJo69WJy16ZFKf3VJawSAjPsxcDYzHGiQjAGUVZL7EwnbXK+wEZOQcXzYKuEC5y1SggTnUWsQwBmuhD2OJkGYrESEMaEwmz2x+B7i66V5VoRqJ6LLZJgBkqIJlO0EyareiRWb8FYGKfYz3wT4FuEj4RjkCoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r8wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrVm11b"
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "state": "tx_+NILAfiEuEBtFfeveh5hZQLcVF+MfNQ0OK/x3PDJo69WJy16ZFKf3VJawSAjPsxcDYzHGiQjAGUVZL7EwnbXK+wEZOQcXzYKuEC5y1SggTnUWsQwBmuhD2OJkGYrESEMaEwmz2x+B7i66V5VoRqJ6LLZJgBkqIJlO0EyareiRWb8FYGKfYz3wT4FuEj4RjkCoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r8wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrVm11b"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422329,
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
  "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
  "id": -576460752303422329,
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
  "id": -576460752303422328,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
  "id": -576460752303422328,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBtFfeveh5hZQLcVF+MfNQ0OK/x3PDJo69WJy16ZFKf3VJawSAjPsxcDYzHGiQjAGUVZL7EwnbXK+wEZOQcXzYKuEC5y1SggTnUWsQwBmuhD2OJkGYrESEMaEwmz2x+B7i66V5VoRqJ6LLZJgBkqIJlO0EyareiRWb8FYGKfYz3wT4FuEj4RjkCoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r8wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrVm11b",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBtFfeveh5hZQLcVF+MfNQ0OK/x3PDJo69WJy16ZFKf3VJawSAjPsxcDYzHGiQjAGUVZL7EwnbXK+wEZOQcXzYKuEC5y1SggTnUWsQwBmuhD2OJkGYrESEMaEwmz2x+B7i66V5VoRqJ6LLZJgBkqIJlO0EyareiRWb8FYGKfYz3wT4FuEj4RjkCoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r8wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrVm11b",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBtFfeveh5hZQLcVF+MfNQ0OK/x3PDJo69WJy16ZFKf3VJawSAjPsxcDYzHGiQjAGUVZL7EwnbXK+wEZOQcXzYKuEC5y1SggTnUWsQwBmuhD2OJkGYrESEMaEwmz2x+B7i66V5VoRqJ6LLZJgBkqIJlO0EyareiRWb8FYGKfYz3wT4FuEj4RjkCoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r8wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrVm11b",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
  "id": -576460752303422327,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
  "id": -576460752303422327,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBiqMWMV04++rQ7n/75/zqUyA4x3Ffwq87ANqjSb0LWvzoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBtFfeveh5hZQLcVF+MfNQ0OK/x3PDJo69WJy16ZFKf3VJawSAjPsxcDYzHGiQjAGUVZL7EwnbXK+wEZOQcXzYKuEC5y1SggTnUWsQwBmuhD2OJkGYrESEMaEwmz2x+B7i66V5VoRqJ6LLZJgBkqIJlO0EyareiRWb8FYGKfYz3wT4FuEj4RjkCoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r8wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACGGSNyaiFwgY+I8esg",
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
    "signed_tx": "tx_+QLBCwH4QrhAm1vv1woWuSw2fpV0nDPjxL9AVDJ0hqJLqCMVEsto5WS0dBCoxWI5vPyXQKiwWAZ2xVETgnY24esSiLRlbU3BBLkCePkCdTcBoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r86EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAbRX3r3oeYWUC3FRfjHzUNDiv8dzwyaOvVictemRSn91SWsEgIz7MXA2MxxokIwBlFWS+xMJ21yvsBGTkHF82CrhAuctUoIE51FrEMAZroQ9jiZBmKxEhDGhMJs9sfge4uuleVaEaieiy2SYAZKiCZTtBMmq3okVm/BWBin2M98E+BbhI+EY5AqEGKoxYxXTj76tDuf/vn/OpTIDjHcV/CrzsA2qNJvQta/MCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkjcmohcIGPcbH6Fw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAm1vv1woWuSw2fpV0nDPjxL9AVDJ0hqJLqCMVEsto5WS0dBCoxWI5vPyXQKiwWAZ2xVETgnY24esSiLRlbU3BBLkCePkCdTcBoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r86EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAbRX3r3oeYWUC3FRfjHzUNDiv8dzwyaOvVictemRSn91SWsEgIz7MXA2MxxokIwBlFWS+xMJ21yvsBGTkHF82CrhAuctUoIE51FrEMAZroQ9jiZBmKxEhDGhMJs9sfge4uuleVaEaieiy2SYAZKiCZTtBMmq3okVm/BWBin2M98E+BbhI+EY5AqEGKoxYxXTj76tDuf/vn/OpTIDjHcV/CrzsA2qNJvQta/MCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkjcmohcIGPcbH6Fw==",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAm1vv1woWuSw2fpV0nDPjxL9AVDJ0hqJLqCMVEsto5WS0dBCoxWI5vPyXQKiwWAZ2xVETgnY24esSiLRlbU3BBLkCePkCdTcBoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r86EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAbRX3r3oeYWUC3FRfjHzUNDiv8dzwyaOvVictemRSn91SWsEgIz7MXA2MxxokIwBlFWS+xMJ21yvsBGTkHF82CrhAuctUoIE51FrEMAZroQ9jiZBmKxEhDGhMJs9sfge4uuleVaEaieiy2SYAZKiCZTtBMmq3okVm/BWBin2M98E+BbhI+EY5AqEGKoxYxXTj76tDuf/vn/OpTIDjHcV/CrzsA2qNJvQta/MCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkjcmohcIGPcbH6Fw==",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBiqMWMV04++rQ7n/75/zqUyA4x3Ffwq87ANqjSb0LWvzoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAA7Inzi4A==",
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
    "signed_tx": "tx_+KcLAfhCuEBOMa0kTwKo6JX3Rx4hk7A2+4RaIteL0HLVQ1GybyxhLyzzVlxemL6jqNZ2WyLVcdPLBvEa0XdgD7QI53aIWfYFuF/4XTgBoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r86EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAO7Yd140="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBOMa0kTwKo6JX3Rx4hk7A2+4RaIteL0HLVQ1GybyxhLyzzVlxemL6jqNZ2WyLVcdPLBvEa0XdgD7QI53aIWfYFuF/4XTgBoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r86EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAO7Yd140=",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBOMa0kTwKo6JX3Rx4hk7A2+4RaIteL0HLVQ1GybyxhLyzzVlxemL6jqNZ2WyLVcdPLBvEa0XdgD7QI53aIWfYFuF/4XTgBoQYqjFjFdOPvq0O5/++f86lMgOMdxX8KvOwDao0m9C1r86EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAO7Yd140=",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
    "channel_id": "ch_Kjqa5HPPnwCmmUnzTwux5rexMXwcxboZMegfzvZaPswyud1LR",
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
      "fsm_id": "ba_4FCms2ZVPEW/DwKZqadu9a2WIqp8T3wcZZsQolXIKqvjvqdy"
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
      "fsm_id": "ba_PSkIPtnQfK9vk3HyXtBuC8quihwwHPrTrN43+PeYrJ4z6bgr"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBkBOn83Y=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422326,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECFz8ZsuUH73LhrFqZcSyheyGekMRkwU3ms4FheujZ/jg8YnnuEyOxuwO0T5G7oeKQ3OH3i5bIKQ9zLQIGNKwILuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZCx33zM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422326,
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_PSkIPtnQfK9vk3HyXtBuC8quihwwHPrTrN43+PeYrJ4z6bgr"
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECFz8ZsuUH73LhrFqZcSyheyGekMRkwU3ms4FheujZ/jg8YnnuEyOxuwO0T5G7oeKQ3OH3i5bIKQ9zLQIGNKwILuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZCx33zM",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422325,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAhc/GbLlB+9y4axamXEsoXshnpDEZMFN5rOBYXro2f44PGJ57hMjsbsDtE+Ru6HikNzh94uWyCkPcy0CBjSsCC7hA/BzRi4oHJDOOo8rs4kXaegl96jyEQZ7isAzmtKWFZNp2X3yLrkU8Oia2vEwpzOwQrblph1GVz6Q883Nu/2YWCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGQ0MKa8w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
  "id": -576460752303422325,
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAhc/GbLlB+9y4axamXEsoXshnpDEZMFN5rOBYXro2f44PGJ57hMjsbsDtE+Ru6HikNzh94uWyCkPcy0CBjSsCC7hA/BzRi4oHJDOOo8rs4kXaegl96jyEQZ7isAzmtKWFZNp2X3yLrkU8Oia2vEwpzOwQrblph1GVz6Q883Nu/2YWCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGQ0MKa8w==",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_4FCms2ZVPEW/DwKZqadu9a2WIqp8T3wcZZsQolXIKqvjvqdy"
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAhc/GbLlB+9y4axamXEsoXshnpDEZMFN5rOBYXro2f44PGJ57hMjsbsDtE+Ru6HikNzh94uWyCkPcy0CBjSsCC7hA/BzRi4oHJDOOo8rs4kXaegl96jyEQZ7isAzmtKWFZNp2X3yLrkU8Oia2vEwpzOwQrblph1GVz6Q883Nu/2YWCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGQ0MKa8w==",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAhc/GbLlB+9y4axamXEsoXshnpDEZMFN5rOBYXro2f44PGJ57hMjsbsDtE+Ru6HikNzh94uWyCkPcy0CBjSsCC7hA/BzRi4oHJDOOo8rs4kXaegl96jyEQZ7isAzmtKWFZNp2X3yLrkU8Oia2vEwpzOwQrblph1GVz6Q883Nu/2YWCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGQ0MKa8w==",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAhc/GbLlB+9y4axamXEsoXshnpDEZMFN5rOBYXro2f44PGJ57hMjsbsDtE+Ru6HikNzh94uWyCkPcy0CBjSsCC7hA/BzRi4oHJDOOo8rs4kXaegl96jyEQZ7isAzmtKWFZNp2X3yLrkU8Oia2vEwpzOwQrblph1GVz6Q883Nu/2YWCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGQ0MKa8w==",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "message": {
        "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "message": {
        "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
  "id": -576460752303422324,
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
  "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
  "id": -576460752303422324,
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "state": "tx_+QEOCwH4hLhAhc/GbLlB+9y4axamXEsoXshnpDEZMFN5rOBYXro2f44PGJ57hMjsbsDtE+Ru6HikNzh94uWyCkPcy0CBjSsCC7hA/BzRi4oHJDOOo8rs4kXaegl96jyEQZ7isAzmtKWFZNp2X3yLrkU8Oia2vEwpzOwQrblph1GVz6Q883Nu/2YWCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGQ0MKa8w=="
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "state": "tx_+QEOCwH4hLhAhc/GbLlB+9y4axamXEsoXshnpDEZMFN5rOBYXro2f44PGJ57hMjsbsDtE+Ru6HikNzh94uWyCkPcy0CBjSsCC7hA/BzRi4oHJDOOo8rs4kXaegl96jyEQZ7isAzmtKWFZNp2X3yLrkU8Oia2vEwpzOwQrblph1GVz6Q883Nu/2YWCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGQ0MKa8w=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAiWN1V"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422323,
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
  "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
  "id": -576460752303422323,
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqzHcBbVWOyWkKstays9WQ7dnhfrGDZYnDkSy8nmbrCUAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyrKLMFE=",
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
  "id": -576460752303422322,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECm5R+bLyXDzLr86kUW9WziMiKXJgTz0H+DnSswwPim38b5dhNPjwdxz3nk4Vi5MGTf1pu++RO+oPJPbs+TqsAPuEj4RjkCoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoGmEfa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
  "id": -576460752303422322,
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "signed_tx": "tx_+JALAfhCuECm5R+bLyXDzLr86kUW9WziMiKXJgTz0H+DnSswwPim38b5dhNPjwdxz3nk4Vi5MGTf1pu++RO+oPJPbs+TqsAPuEj4RjkCoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoGmEfa",
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
  "id": -576460752303422321,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECm5R+bLyXDzLr86kUW9WziMiKXJgTz0H+DnSswwPim38b5dhNPjwdxz3nk4Vi5MGTf1pu++RO+oPJPbs+TqsAPuECqftW4yswwHHUOmFWhcet0nbtH0c/1GuoXDrXJYo8XbqpKpAvkI4U7RMAxfnOtnTR3Q97yq81SCmZYw6E/r6wHuEj4RjkCoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqfe9Ji"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
  "id": -576460752303422321,
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "state": "tx_+NILAfiEuECm5R+bLyXDzLr86kUW9WziMiKXJgTz0H+DnSswwPim38b5dhNPjwdxz3nk4Vi5MGTf1pu++RO+oPJPbs+TqsAPuECqftW4yswwHHUOmFWhcet0nbtH0c/1GuoXDrXJYo8XbqpKpAvkI4U7RMAxfnOtnTR3Q97yq81SCmZYw6E/r6wHuEj4RjkCoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqfe9Ji"
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "state": "tx_+NILAfiEuECm5R+bLyXDzLr86kUW9WziMiKXJgTz0H+DnSswwPim38b5dhNPjwdxz3nk4Vi5MGTf1pu++RO+oPJPbs+TqsAPuECqftW4yswwHHUOmFWhcet0nbtH0c/1GuoXDrXJYo8XbqpKpAvkI4U7RMAxfnOtnTR3Q97yq81SCmZYw6E/r6wHuEj4RjkCoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqfe9Ji"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422320,
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
  "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
  "id": -576460752303422320,
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
  "id": -576460752303422319,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
  "id": -576460752303422319,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECm5R+bLyXDzLr86kUW9WziMiKXJgTz0H+DnSswwPim38b5dhNPjwdxz3nk4Vi5MGTf1pu++RO+oPJPbs+TqsAPuECqftW4yswwHHUOmFWhcet0nbtH0c/1GuoXDrXJYo8XbqpKpAvkI4U7RMAxfnOtnTR3Q97yq81SCmZYw6E/r6wHuEj4RjkCoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqfe9Ji",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECm5R+bLyXDzLr86kUW9WziMiKXJgTz0H+DnSswwPim38b5dhNPjwdxz3nk4Vi5MGTf1pu++RO+oPJPbs+TqsAPuECqftW4yswwHHUOmFWhcet0nbtH0c/1GuoXDrXJYo8XbqpKpAvkI4U7RMAxfnOtnTR3Q97yq81SCmZYw6E/r6wHuEj4RjkCoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqfe9Ji",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECm5R+bLyXDzLr86kUW9WziMiKXJgTz0H+DnSswwPim38b5dhNPjwdxz3nk4Vi5MGTf1pu++RO+oPJPbs+TqsAPuECqftW4yswwHHUOmFWhcet0nbtH0c/1GuoXDrXJYo8XbqpKpAvkI4U7RMAxfnOtnTR3Q97yq81SCmZYw6E/r6wHuEj4RjkCoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqfe9Ji",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
  "id": -576460752303422318,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
  "id": -576460752303422318,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBqzHcBbVWOyWkKstays9WQ7dnhfrGDZYnDkSy8nmbrCUoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuECm5R+bLyXDzLr86kUW9WziMiKXJgTz0H+DnSswwPim38b5dhNPjwdxz3nk4Vi5MGTf1pu++RO+oPJPbs+TqsAPuECqftW4yswwHHUOmFWhcet0nbtH0c/1GuoXDrXJYo8XbqpKpAvkI4U7RMAxfnOtnTR3Q97yq81SCmZYw6E/r6wHuEj4RjkCoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACGGR7KUfkIPJUookg=",
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
    "signed_tx": "tx_+QLACwH4QrhAclnHChsNIhviAH9qiY9PF0LIT3NdIzfxWOvYkY7QtWdss9l4SqcdkdH86wwpYNOd0APmDZtXXi6B9fZAeYjDD7kCd/kCdDcBoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhApuUfmy8lw8y6/OpFFvVs4jIilyYE89B/g50rMMD4pt/G+XYTT48Hcc955OFYuTBk39abvvkTvqDyT27Pk6rAD7hAqn7VuMrMMBx1DphVoXHrdJ27R9HP9RrqFw61yWKPF26qSqQL5COFO0TAMX5zrZ00d0Pe8qvNUgpmWMOhP6+sB7hI+EY5AqEGrMdwFtVY7JaQqy1rKz1ZDt2eF+sYNlicORLLyeZusJQCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeylH5CDwWiIoY"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAclnHChsNIhviAH9qiY9PF0LIT3NdIzfxWOvYkY7QtWdss9l4SqcdkdH86wwpYNOd0APmDZtXXi6B9fZAeYjDD7kCd/kCdDcBoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhApuUfmy8lw8y6/OpFFvVs4jIilyYE89B/g50rMMD4pt/G+XYTT48Hcc955OFYuTBk39abvvkTvqDyT27Pk6rAD7hAqn7VuMrMMBx1DphVoXHrdJ27R9HP9RrqFw61yWKPF26qSqQL5COFO0TAMX5zrZ00d0Pe8qvNUgpmWMOhP6+sB7hI+EY5AqEGrMdwFtVY7JaQqy1rKz1ZDt2eF+sYNlicORLLyeZusJQCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeylH5CDwWiIoY",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAclnHChsNIhviAH9qiY9PF0LIT3NdIzfxWOvYkY7QtWdss9l4SqcdkdH86wwpYNOd0APmDZtXXi6B9fZAeYjDD7kCd/kCdDcBoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhApuUfmy8lw8y6/OpFFvVs4jIilyYE89B/g50rMMD4pt/G+XYTT48Hcc955OFYuTBk39abvvkTvqDyT27Pk6rAD7hAqn7VuMrMMBx1DphVoXHrdJ27R9HP9RrqFw61yWKPF26qSqQL5COFO0TAMX5zrZ00d0Pe8qvNUgpmWMOhP6+sB7hI+EY5AqEGrMdwFtVY7JaQqy1rKz1ZDt2eF+sYNlicORLLyeZusJQCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeylH5CDwWiIoY",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBqzHcBbVWOyWkKstays9WQ7dnhfrGDZYnDkSy8nmbrCUoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAA9gxlKeQ==",
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
    "signed_tx": "tx_+KcLAfhCuEB1QlkD7EOUoLiSwv/4GA1hhuFaLnGCNV4DS/FJ2h4ogXqtqJe+nslrAeDAz010g0cWDSY2xlooJb9LQA8XHvEBuF/4XTgBoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAPR0ybC8="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB1QlkD7EOUoLiSwv/4GA1hhuFaLnGCNV4DS/FJ2h4ogXqtqJe+nslrAeDAz010g0cWDSY2xlooJb9LQA8XHvEBuF/4XTgBoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAPR0ybC8=",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB1QlkD7EOUoLiSwv/4GA1hhuFaLnGCNV4DS/FJ2h4ogXqtqJe+nslrAeDAz010g0cWDSY2xlooJb9LQA8XHvEBuF/4XTgBoQasx3AW1VjslpCrLWsrPVkO3Z4X6xg2WJw5EsvJ5m6wlKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAPR0ybC8=",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
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
    "channel_id": "ch_2K6Qj2AmPDnM16NBXyeZmP4eKWm5haa8S5xT3TbYmWmekvTmq2",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
