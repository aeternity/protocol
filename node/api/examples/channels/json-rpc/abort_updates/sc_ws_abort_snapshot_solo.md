
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
      "fsm_id": "ba_YsPD9sN4MLPtUJeSn5bnW4VVJ8Zvf55OXWahvJvms2dSMGgV"
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
      "fsm_id": "ba_/hz2Ax0IfQ+n+4aigP59J8X4+qp6IfrvplcRNO9WLZ8XsexM"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBunpQT2Y=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422101,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAUJqQ+wwIWbjlHBW4s4BtbsKOGwzx+39MhZPJHUiClMAVOawTXOS+EfxNVCynPKMe5WFE7FDo1E06MDaNlbHAJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbql+8MM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422101,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_/hz2Ax0IfQ+n+4aigP59J8X4+qp6IfrvplcRNO9WLZ8XsexM"
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEAUJqQ+wwIWbjlHBW4s4BtbsKOGwzx+39MhZPJHUiClMAVOawTXOS+EfxNVCynPKMe5WFE7FDo1E06MDaNlbHAJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbql+8MM",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422100,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAEeDlm08KkZZ04y7U9qKANkMMgq3jwSfGe5sxKQunf/Ig49s3u2G0sE5azoGRG6quq7XgMix3Q5UFDaOQXOwxArhAFCakPsMCFm45RwVuLOAbW7CjhsM8ft/TIWTyR1IgpTAFTmsE1zkvhH8TVQspzyjHuVhROxQ6NRNOjA2jZWxwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG65Dr5pQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422100,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAEeDlm08KkZZ04y7U9qKANkMMgq3jwSfGe5sxKQunf/Ig49s3u2G0sE5azoGRG6quq7XgMix3Q5UFDaOQXOwxArhAFCakPsMCFm45RwVuLOAbW7CjhsM8ft/TIWTyR1IgpTAFTmsE1zkvhH8TVQspzyjHuVhROxQ6NRNOjA2jZWxwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG65Dr5pQ==",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_YsPD9sN4MLPtUJeSn5bnW4VVJ8Zvf55OXWahvJvms2dSMGgV"
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAEeDlm08KkZZ04y7U9qKANkMMgq3jwSfGe5sxKQunf/Ig49s3u2G0sE5azoGRG6quq7XgMix3Q5UFDaOQXOwxArhAFCakPsMCFm45RwVuLOAbW7CjhsM8ft/TIWTyR1IgpTAFTmsE1zkvhH8TVQspzyjHuVhROxQ6NRNOjA2jZWxwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG65Dr5pQ==",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAEeDlm08KkZZ04y7U9qKANkMMgq3jwSfGe5sxKQunf/Ig49s3u2G0sE5azoGRG6quq7XgMix3Q5UFDaOQXOwxArhAFCakPsMCFm45RwVuLOAbW7CjhsM8ft/TIWTyR1IgpTAFTmsE1zkvhH8TVQspzyjHuVhROxQ6NRNOjA2jZWxwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG65Dr5pQ==",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAEeDlm08KkZZ04y7U9qKANkMMgq3jwSfGe5sxKQunf/Ig49s3u2G0sE5azoGRG6quq7XgMix3Q5UFDaOQXOwxArhAFCakPsMCFm45RwVuLOAbW7CjhsM8ft/TIWTyR1IgpTAFTmsE1zkvhH8TVQspzyjHuVhROxQ6NRNOjA2jZWxwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG65Dr5pQ==",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "message": {
        "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "message": {
        "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
  "id": -576460752303422099,
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
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422099,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "state": "tx_+QEOCwH4hLhAEeDlm08KkZZ04y7U9qKANkMMgq3jwSfGe5sxKQunf/Ig49s3u2G0sE5azoGRG6quq7XgMix3Q5UFDaOQXOwxArhAFCakPsMCFm45RwVuLOAbW7CjhsM8ft/TIWTyR1IgpTAFTmsE1zkvhH8TVQspzyjHuVhROxQ6NRNOjA2jZWxwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG65Dr5pQ=="
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "state": "tx_+QEOCwH4hLhAEeDlm08KkZZ04y7U9qKANkMMgq3jwSfGe5sxKQunf/Ig49s3u2G0sE5azoGRG6quq7XgMix3Q5UFDaOQXOwxArhAFCakPsMCFm45RwVuLOAbW7CjhsM8ft/TIWTyR1IgpTAFTmsE1zkvhH8TVQspzyjHuVhROxQ6NRNOjA2jZWxwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG65Dr5pQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422098,
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
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422098,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgJzaPWCftHSyt3stV5oHLSta8wa8JjTIlJzHyz8MF+tAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyohh3cc=",
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
  "id": -576460752303422097,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED0EjmND0CRhNM0Oya8l3vG8fb9Wcx9kDunwdTWW9VbyOMxNcecGmnEPpnNz/s5VSwpyjEWZnZoeccNeBPcBzsAuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp9oHlT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422097,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "signed_tx": "tx_+JALAfhCuED0EjmND0CRhNM0Oya8l3vG8fb9Wcx9kDunwdTWW9VbyOMxNcecGmnEPpnNz/s5VSwpyjEWZnZoeccNeBPcBzsAuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp9oHlT",
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
  "id": -576460752303422096,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECAeaHM5YFt5b4dHbO7GmlrR3TZrlrXhb1yS3jS2dBb99zEQ/5KSxzK9qCwVxqF8xBKIG0sByDv+RRRbTfDyQMKuED0EjmND0CRhNM0Oya8l3vG8fb9Wcx9kDunwdTWW9VbyOMxNcecGmnEPpnNz/s5VSwpyjEWZnZoeccNeBPcBzsAuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspWD32/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422096,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "state": "tx_+NILAfiEuECAeaHM5YFt5b4dHbO7GmlrR3TZrlrXhb1yS3jS2dBb99zEQ/5KSxzK9qCwVxqF8xBKIG0sByDv+RRRbTfDyQMKuED0EjmND0CRhNM0Oya8l3vG8fb9Wcx9kDunwdTWW9VbyOMxNcecGmnEPpnNz/s5VSwpyjEWZnZoeccNeBPcBzsAuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspWD32/"
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "state": "tx_+NILAfiEuECAeaHM5YFt5b4dHbO7GmlrR3TZrlrXhb1yS3jS2dBb99zEQ/5KSxzK9qCwVxqF8xBKIG0sByDv+RRRbTfDyQMKuED0EjmND0CRhNM0Oya8l3vG8fb9Wcx9kDunwdTWW9VbyOMxNcecGmnEPpnNz/s5VSwpyjEWZnZoeccNeBPcBzsAuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspWD32/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422095,
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
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422095,
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
  "id": -576460752303422094,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422094,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECAeaHM5YFt5b4dHbO7GmlrR3TZrlrXhb1yS3jS2dBb99zEQ/5KSxzK9qCwVxqF8xBKIG0sByDv+RRRbTfDyQMKuED0EjmND0CRhNM0Oya8l3vG8fb9Wcx9kDunwdTWW9VbyOMxNcecGmnEPpnNz/s5VSwpyjEWZnZoeccNeBPcBzsAuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspWD32/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422093,
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
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422093,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgJzaPWCftHSyt3stV5oHLSta8wa8JjTIlJzHyz8MF+tA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnIRWqM=",
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
  "id": -576460752303422092,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAs6rqMvkx4UZkUxVMpUkIopRV8KY57wWFERJcuN02HqoBSiJ/BAJSob6H9jBlxB61J7LF4r0VnxI0cE0/QR6YJuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ2GeNM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422092,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAs6rqMvkx4UZkUxVMpUkIopRV8KY57wWFERJcuN02HqoBSiJ/BAJSob6H9jBlxB61J7LF4r0VnxI0cE0/QR6YJuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ2GeNM",
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
  "id": -576460752303422091,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAs6rqMvkx4UZkUxVMpUkIopRV8KY57wWFERJcuN02HqoBSiJ/BAJSob6H9jBlxB61J7LF4r0VnxI0cE0/QR6YJuEDYpYnwgFekW9kBa4UrAzBxVbeDH0Cx0TdegkwQQwa00x4CsR8J4M5pUVKf3Dd6ujAGoC4xa/gsqT70TD0unHcJuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYG4Pf7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422091,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "state": "tx_+NILAfiEuEAs6rqMvkx4UZkUxVMpUkIopRV8KY57wWFERJcuN02HqoBSiJ/BAJSob6H9jBlxB61J7LF4r0VnxI0cE0/QR6YJuEDYpYnwgFekW9kBa4UrAzBxVbeDH0Cx0TdegkwQQwa00x4CsR8J4M5pUVKf3Dd6ujAGoC4xa/gsqT70TD0unHcJuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYG4Pf7"
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "state": "tx_+NILAfiEuEAs6rqMvkx4UZkUxVMpUkIopRV8KY57wWFERJcuN02HqoBSiJ/BAJSob6H9jBlxB61J7LF4r0VnxI0cE0/QR6YJuEDYpYnwgFekW9kBa4UrAzBxVbeDH0Cx0TdegkwQQwa00x4CsR8J4M5pUVKf3Dd6ujAGoC4xa/gsqT70TD0unHcJuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYG4Pf7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422090,
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
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422090,
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
  "id": -576460752303422089,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422089,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAs6rqMvkx4UZkUxVMpUkIopRV8KY57wWFERJcuN02HqoBSiJ/BAJSob6H9jBlxB61J7LF4r0VnxI0cE0/QR6YJuEDYpYnwgFekW9kBa4UrAzBxVbeDH0Cx0TdegkwQQwa00x4CsR8J4M5pUVKf3Dd6ujAGoC4xa/gsqT70TD0unHcJuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYG4Pf7",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "signed_tx": "tx_+QEvCwHAuQEp+QEmOwGhBgJzaPWCftHSyt3stV5oHLSta8wa8JjTIlJzHyz8MF+toQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAs6rqMvkx4UZkUxVMpUkIopRV8KY57wWFERJcuN02HqoBSiJ/BAJSob6H9jBlxB61J7LF4r0VnxI0cE0/QR6YJuEDYpYnwgFekW9kBa4UrAzBxVbeDH0Cx0TdegkwQQwa00x4CsR8J4M5pUVKf3Dd6ujAGoC4xa/gsqT70TD0unHcJuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMLeUL4AIG7FyrdvA==",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBgJzaPWCftHSyt3stV5oHLSta8wa8JjTIlJzHyz8MF+toQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEAs6rqMvkx4UZkUxVMpUkIopRV8KY57wWFERJcuN02HqoBSiJ/BAJSob6H9jBlxB61J7LF4r0VnxI0cE0/QR6YJuEDYpYnwgFekW9kBa4UrAzBxVbeDH0Cx0TdegkwQQwa00x4CsR8J4M5pUVKf3Dd6ujAGoC4xa/gsqT70TD0unHcJuEj4RjkCoQYCc2j1gn7R0srd7LVeaBy0rWvMGvCY0yJScx8s/DBfrQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMG0SswAEEe205o",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
  "id": -576460752303422088,
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
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422088,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422087,
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
    "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
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
  "channel_id": "ch_25byCyvEKxeVeWqBNPX3M4EErCkenoRMzHb9ypftJH3VCMCz9",
  "id": -576460752303422087,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
