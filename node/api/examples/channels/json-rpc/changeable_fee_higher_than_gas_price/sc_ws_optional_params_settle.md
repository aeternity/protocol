
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
      "fsm_id": "ba_JsUEIRgUId3yXX5AhWjSTFX9yqdrR4tf4aI4LkngZprP8Wjw"
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
      "fsm_id": "ba_mVlRtOy/phtxppfDlXKVxCrRUyTaioOSb0tWGKZ3kFKX5Bz8"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ6Q2KyBA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422409,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBn/IUhYqhOj7JCB39/gDlEIfCrpNEG6iJb+U4VM+zu8Fxx55UuqlRh88EhYMQLQDhnypWfBX/Vl1F78bhPchMMuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGen7BRbw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422409,
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_mVlRtOy/phtxppfDlXKVxCrRUyTaioOSb0tWGKZ3kFKX5Bz8"
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBn/IUhYqhOj7JCB39/gDlEIfCrpNEG6iJb+U4VM+zu8Fxx55UuqlRh88EhYMQLQDhnypWfBX/Vl1F78bhPchMMuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGen7BRbw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422408,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAOHZrU+qhpgv8vUHSH4X0tZLBvB+s32cP6wFdlxLKHAhisU7F9h27eJQmGxzLmpe7mrh732p/+PhoL6fK/kJDBrhAZ/yFIWKoTo+yQgd/f4A5RCHwq6TRBuoiW/lOFTPs7vBcceeVLqpUYfPBIWDEC0A4Z8qVnwV/1ZdRe/G4T3ITDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnpUCYSH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
  "id": -576460752303422408,
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAOHZrU+qhpgv8vUHSH4X0tZLBvB+s32cP6wFdlxLKHAhisU7F9h27eJQmGxzLmpe7mrh732p/+PhoL6fK/kJDBrhAZ/yFIWKoTo+yQgd/f4A5RCHwq6TRBuoiW/lOFTPs7vBcceeVLqpUYfPBIWDEC0A4Z8qVnwV/1ZdRe/G4T3ITDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnpUCYSH",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_JsUEIRgUId3yXX5AhWjSTFX9yqdrR4tf4aI4LkngZprP8Wjw"
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAOHZrU+qhpgv8vUHSH4X0tZLBvB+s32cP6wFdlxLKHAhisU7F9h27eJQmGxzLmpe7mrh732p/+PhoL6fK/kJDBrhAZ/yFIWKoTo+yQgd/f4A5RCHwq6TRBuoiW/lOFTPs7vBcceeVLqpUYfPBIWDEC0A4Z8qVnwV/1ZdRe/G4T3ITDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnpUCYSH",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAOHZrU+qhpgv8vUHSH4X0tZLBvB+s32cP6wFdlxLKHAhisU7F9h27eJQmGxzLmpe7mrh732p/+PhoL6fK/kJDBrhAZ/yFIWKoTo+yQgd/f4A5RCHwq6TRBuoiW/lOFTPs7vBcceeVLqpUYfPBIWDEC0A4Z8qVnwV/1ZdRe/G4T3ITDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnpUCYSH",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAOHZrU+qhpgv8vUHSH4X0tZLBvB+s32cP6wFdlxLKHAhisU7F9h27eJQmGxzLmpe7mrh732p/+PhoL6fK/kJDBrhAZ/yFIWKoTo+yQgd/f4A5RCHwq6TRBuoiW/lOFTPs7vBcceeVLqpUYfPBIWDEC0A4Z8qVnwV/1ZdRe/G4T3ITDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnpUCYSH",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "message": {
        "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "message": {
        "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
  "id": -576460752303422407,
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
  "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
  "id": -576460752303422407,
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "state": "tx_+QENCwH4hLhAOHZrU+qhpgv8vUHSH4X0tZLBvB+s32cP6wFdlxLKHAhisU7F9h27eJQmGxzLmpe7mrh732p/+PhoL6fK/kJDBrhAZ/yFIWKoTo+yQgd/f4A5RCHwq6TRBuoiW/lOFTPs7vBcceeVLqpUYfPBIWDEC0A4Z8qVnwV/1ZdRe/G4T3ITDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnpUCYSH"
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "state": "tx_+QENCwH4hLhAOHZrU+qhpgv8vUHSH4X0tZLBvB+s32cP6wFdlxLKHAhisU7F9h27eJQmGxzLmpe7mrh732p/+PhoL6fK/kJDBrhAZ/yFIWKoTo+yQgd/f4A5RCHwq6TRBuoiW/lOFTPs7vBcceeVLqpUYfPBIWDEC0A4Z8qVnwV/1ZdRe/G4T3ITDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnpUCYSH"
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBnZi1aqZnxrsNrNiH9QOfQWMP///km+pbE+WeuGHrN+OoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7sgIAAe+vBKy4=",
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
    "signed_tx": "tx_+QHrCwH4QrhAKoQob0NtiwHdLvAi5DEwgqcdEpP5tzGKfm56isugugAATdaTqTkuy3gxfUF2fgiobmFzK1eccLfUI0oXaFMUALkBovkBnzYBoQZ2YtWqmZ8a7DazYh/UDn0FjD///5JvqWxPlnrhh6zfjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAHu4Tv0x"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAKoQob0NtiwHdLvAi5DEwgqcdEpP5tzGKfm56isugugAATdaTqTkuy3gxfUF2fgiobmFzK1eccLfUI0oXaFMUALkBovkBnzYBoQZ2YtWqmZ8a7DazYh/UDn0FjD///5JvqWxPlnrhh6zfjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAHu4Tv0x",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAKoQob0NtiwHdLvAi5DEwgqcdEpP5tzGKfm56isugugAATdaTqTkuy3gxfUF2fgiobmFzK1eccLfUI0oXaFMUALkBovkBnzYBoQZ2YtWqmZ8a7DazYh/UDn0FjD///5JvqWxPlnrhh6zfjqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAHu4Tv0x",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBnZi1aqZnxrsNrNiH9QOfQWMP///km+pbE+WeuGHrN+OoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIbgkQw2Hn40apB/2Q==",
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
    "signed_tx": "tx_+KcLAfhCuEDJomiTQ/HAhQxLkJoNFRteEOSrAT+ALrH2HhS720+zKFTkutxsLTj7JRBIM5pMbw3Cgi6gOCYRNNSh0Qy/BlgDuF/4XTgBoQZ2YtWqmZ8a7DazYh/UDn0FjD///5JvqWxPlnrhh6zfjqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCG4JEMNh5+NJS6eQo="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDJomiTQ/HAhQxLkJoNFRteEOSrAT+ALrH2HhS720+zKFTkutxsLTj7JRBIM5pMbw3Cgi6gOCYRNNSh0Qy/BlgDuF/4XTgBoQZ2YtWqmZ8a7DazYh/UDn0FjD///5JvqWxPlnrhh6zfjqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCG4JEMNh5+NJS6eQo=",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDJomiTQ/HAhQxLkJoNFRteEOSrAT+ALrH2HhS720+zKFTkutxsLTj7JRBIM5pMbw3Cgi6gOCYRNNSh0Qy/BlgDuF/4XTgBoQZ2YtWqmZ8a7DazYh/UDn0FjD///5JvqWxPlnrhh6zfjqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCG4JEMNh5+NJS6eQo=",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
    "channel_id": "ch_u91msWL9MY1QtyHNMPtN4DcKACScGPSSVXuK6gV4V62VP8pFb",
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
      "fsm_id": "ba_eYXtc6xjX8A/W4HC7E9ycaygRmUzpK8TMnaztFA25cmLmCoa"
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
      "fsm_id": "ba_yg61jUWGTa168ZaxnYOPm1UZDl/0SaQzA7nXReJTqq9TrDoW"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ85gA8Cg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422406,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECsY3lGVbEuQ9hARqjlnSiN5/E/a0c/cyK1byIHcC8zjEgZCg1OYFl1Ef+xi9/jsHyTc3/tn9N3uLLkAcqaZtoMuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGfNn+SN8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422406,
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_yg61jUWGTa168ZaxnYOPm1UZDl/0SaQzA7nXReJTqq9TrDoW"
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECsY3lGVbEuQ9hARqjlnSiN5/E/a0c/cyK1byIHcC8zjEgZCg1OYFl1Ef+xi9/jsHyTc3/tn9N3uLLkAcqaZtoMuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGfNn+SN8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422405,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAWodehXCVDdJU92BAMNyLbLQmYxlPDBWGfdsNp5d2Uzy3r316N/wekXn8d2j5xKJFlAhAaWUzE7kjoibevZcDBbhArGN5RlWxLkPYQEao5Z0ojefxP2tHP3MitW8iB3AvM4xIGQoNTmBZdRH/sYvf47B8k3N/7Z/Td7iy5AHKmmbaDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rnx1Y2yr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
  "id": -576460752303422405,
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAWodehXCVDdJU92BAMNyLbLQmYxlPDBWGfdsNp5d2Uzy3r316N/wekXn8d2j5xKJFlAhAaWUzE7kjoibevZcDBbhArGN5RlWxLkPYQEao5Z0ojefxP2tHP3MitW8iB3AvM4xIGQoNTmBZdRH/sYvf47B8k3N/7Z/Td7iy5AHKmmbaDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rnx1Y2yr",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_eYXtc6xjX8A/W4HC7E9ycaygRmUzpK8TMnaztFA25cmLmCoa"
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAWodehXCVDdJU92BAMNyLbLQmYxlPDBWGfdsNp5d2Uzy3r316N/wekXn8d2j5xKJFlAhAaWUzE7kjoibevZcDBbhArGN5RlWxLkPYQEao5Z0ojefxP2tHP3MitW8iB3AvM4xIGQoNTmBZdRH/sYvf47B8k3N/7Z/Td7iy5AHKmmbaDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rnx1Y2yr",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAWodehXCVDdJU92BAMNyLbLQmYxlPDBWGfdsNp5d2Uzy3r316N/wekXn8d2j5xKJFlAhAaWUzE7kjoibevZcDBbhArGN5RlWxLkPYQEao5Z0ojefxP2tHP3MitW8iB3AvM4xIGQoNTmBZdRH/sYvf47B8k3N/7Z/Td7iy5AHKmmbaDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rnx1Y2yr",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAWodehXCVDdJU92BAMNyLbLQmYxlPDBWGfdsNp5d2Uzy3r316N/wekXn8d2j5xKJFlAhAaWUzE7kjoibevZcDBbhArGN5RlWxLkPYQEao5Z0ojefxP2tHP3MitW8iB3AvM4xIGQoNTmBZdRH/sYvf47B8k3N/7Z/Td7iy5AHKmmbaDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rnx1Y2yr",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "message": {
        "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "message": {
        "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
  "id": -576460752303422404,
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
  "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
  "id": -576460752303422404,
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "state": "tx_+QENCwH4hLhAWodehXCVDdJU92BAMNyLbLQmYxlPDBWGfdsNp5d2Uzy3r316N/wekXn8d2j5xKJFlAhAaWUzE7kjoibevZcDBbhArGN5RlWxLkPYQEao5Z0ojefxP2tHP3MitW8iB3AvM4xIGQoNTmBZdRH/sYvf47B8k3N/7Z/Td7iy5AHKmmbaDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rnx1Y2yr"
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "state": "tx_+QENCwH4hLhAWodehXCVDdJU92BAMNyLbLQmYxlPDBWGfdsNp5d2Uzy3r316N/wekXn8d2j5xKJFlAhAaWUzE7kjoibevZcDBbhArGN5RlWxLkPYQEao5Z0ojefxP2tHP3MitW8iB3AvM4xIGQoNTmBZdRH/sYvf47B8k3N/7Z/Td7iy5AHKmmbaDLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rnx1Y2yr"
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBnT2wcizCPqLcp+VUilj6MzGyOy3ARfFqQKWsLfzLVHVoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7sgIAAfVBdy14=",
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
    "signed_tx": "tx_+QHrCwH4QrhA9gPqwmDK35uPuMwavtaNULEOcHg5VxNRxisI7LY6BggzpdYDn/qXhflhIMmBG9uhlY0ZyleC9s1wqiL7rIKzBbkBovkBnzYBoQZ09sHIswj6i3KflVIpY+jMxsjstwEXxakClrC38y1R1aEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAH20Fcrk"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA9gPqwmDK35uPuMwavtaNULEOcHg5VxNRxisI7LY6BggzpdYDn/qXhflhIMmBG9uhlY0ZyleC9s1wqiL7rIKzBbkBovkBnzYBoQZ09sHIswj6i3KflVIpY+jMxsjstwEXxakClrC38y1R1aEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAH20Fcrk",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA9gPqwmDK35uPuMwavtaNULEOcHg5VxNRxisI7LY6BggzpdYDn/qXhflhIMmBG9uhlY0ZyleC9s1wqiL7rIKzBbkBovkBnzYBoQZ09sHIswj6i3KflVIpY+jMxsjstwEXxakClrC38y1R1aEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAH20Fcrk",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBnT2wcizCPqLcp+VUilj6MzGyOy3ARfFqQKWsLfzLVHVoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiX/+GJGE5yoABAIbgkQw2Hn5+edRnHw==",
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
    "signed_tx": "tx_+KcLAfhCuEAVQagii33kip97t2OZJKf4HdJcGhl3+/oUL8+id8G20WpfNiIZVWUnXGRwpfeqkoNUfup3X5TywbHedEdw2r0AuF/4XTgBoQZ09sHIswj6i3KflVIpY+jMxsjstwEXxakClrC38y1R1aEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCG4JEMNh5+fhAZtp4="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAVQagii33kip97t2OZJKf4HdJcGhl3+/oUL8+id8G20WpfNiIZVWUnXGRwpfeqkoNUfup3X5TywbHedEdw2r0AuF/4XTgBoQZ09sHIswj6i3KflVIpY+jMxsjstwEXxakClrC38y1R1aEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCG4JEMNh5+fhAZtp4=",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAVQagii33kip97t2OZJKf4HdJcGhl3+/oUL8+id8G20WpfNiIZVWUnXGRwpfeqkoNUfup3X5TywbHedEdw2r0AuF/4XTgBoQZ09sHIswj6i3KflVIpY+jMxsjstwEXxakClrC38y1R1aEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCG4JEMNh5+fhAZtp4=",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
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
    "channel_id": "ch_tWgmhQG5wAnq6A2RiWBewcwfaASTELz1Dhgv8aoa8LMGpZsFF",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
