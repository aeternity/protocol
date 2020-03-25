
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
      "fsm_id": "ba_k9tCFx3LekigaqK6uF1WjudgSbFEf3qMVrXRPY9Am4De581T"
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
      "fsm_id": "ba_i9BUKIx1MVkliJq267XRoXQ/MdfKYBu4PBiVM8NPTyU068+I"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZUeIgkPg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422573,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAGURxlEXwJPxIOFcRX6PmjMbeiK1xsickOQ+7GhkaUIamMBdHUXi836RAvNQLlw190S6oB42EkStISVde/ImgJuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGVOcj4l0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422573,
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_i9BUKIx1MVkliJq267XRoXQ/MdfKYBu4PBiVM8NPTyU068+I"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAGURxlEXwJPxIOFcRX6PmjMbeiK1xsickOQ+7GhkaUIamMBdHUXi836RAvNQLlw190S6oB42EkStISVde/ImgJuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGVOcj4l0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422572,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhABlEcZRF8CT8SDhXEV+j5ozG3oitcbInJDkPuxoZGlCGpjAXR1F4vN+kQLzUC5cNfdEuqAeNhJErSElXXvyJoCbhA6I3CVJZnnQFVoRAMeddpFKLXdwvB8Cohx/UkIRQ03GRvyyYEVrsU2+iB9sxWiTouwx06RnPpEsg9oEUsraXACLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlSHSa8E"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
  "id": -576460752303422572,
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhABlEcZRF8CT8SDhXEV+j5ozG3oitcbInJDkPuxoZGlCGpjAXR1F4vN+kQLzUC5cNfdEuqAeNhJErSElXXvyJoCbhA6I3CVJZnnQFVoRAMeddpFKLXdwvB8Cohx/UkIRQ03GRvyyYEVrsU2+iB9sxWiTouwx06RnPpEsg9oEUsraXACLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlSHSa8E",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_k9tCFx3LekigaqK6uF1WjudgSbFEf3qMVrXRPY9Am4De581T"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhABlEcZRF8CT8SDhXEV+j5ozG3oitcbInJDkPuxoZGlCGpjAXR1F4vN+kQLzUC5cNfdEuqAeNhJErSElXXvyJoCbhA6I3CVJZnnQFVoRAMeddpFKLXdwvB8Cohx/UkIRQ03GRvyyYEVrsU2+iB9sxWiTouwx06RnPpEsg9oEUsraXACLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlSHSa8E",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABlEcZRF8CT8SDhXEV+j5ozG3oitcbInJDkPuxoZGlCGpjAXR1F4vN+kQLzUC5cNfdEuqAeNhJErSElXXvyJoCbhA6I3CVJZnnQFVoRAMeddpFKLXdwvB8Cohx/UkIRQ03GRvyyYEVrsU2+iB9sxWiTouwx06RnPpEsg9oEUsraXACLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlSHSa8E",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABlEcZRF8CT8SDhXEV+j5ozG3oitcbInJDkPuxoZGlCGpjAXR1F4vN+kQLzUC5cNfdEuqAeNhJErSElXXvyJoCbhA6I3CVJZnnQFVoRAMeddpFKLXdwvB8Cohx/UkIRQ03GRvyyYEVrsU2+iB9sxWiTouwx06RnPpEsg9oEUsraXACLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlSHSa8E",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
  "id": -576460752303422571,
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
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
  "id": -576460752303422571,
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "open"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "state": "tx_+QENCwH4hLhABlEcZRF8CT8SDhXEV+j5ozG3oitcbInJDkPuxoZGlCGpjAXR1F4vN+kQLzUC5cNfdEuqAeNhJErSElXXvyJoCbhA6I3CVJZnnQFVoRAMeddpFKLXdwvB8Cohx/UkIRQ03GRvyyYEVrsU2+iB9sxWiTouwx06RnPpEsg9oEUsraXACLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlSHSa8E"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "state": "tx_+QENCwH4hLhABlEcZRF8CT8SDhXEV+j5ozG3oitcbInJDkPuxoZGlCGpjAXR1F4vN+kQLzUC5cNfdEuqAeNhJErSElXXvyJoCbhA6I3CVJZnnQFVoRAMeddpFKLXdwvB8Cohx/UkIRQ03GRvyyYEVrsU2+iB9sxWiTouwx06RnPpEsg9oEUsraXACLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RlSHSa8E"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBlVdEVIq+4sZ+LaCsHiSQtT+hIN6msaZGy0bGvIKVU27oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/Aobiv0KDc0aEz/UgoEcs4ajohf9X9BGhuePf6GLqnUld1F+cQwQJVvCVNhA==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422570,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECAcjgb7c5RyDF7F0XNzWJMbQnLhIVT9fCvriZIi3tbiykqHjq97WTjfOdF9RL0Y+5gjb/Yju+hWWbffw2Cc4wJuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9Cg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECVY1Yjlc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
  "id": -576460752303422570,
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECAcjgb7c5RyDF7F0XNzWJMbQnLhIVT9fCvriZIi3tbiykqHjq97WTjfOdF9RL0Y+5gjb/Yju+hWWbffw2Cc4wJuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9Cg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECVY1Yjlc=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422569,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECAcjgb7c5RyDF7F0XNzWJMbQnLhIVT9fCvriZIi3tbiykqHjq97WTjfOdF9RL0Y+5gjb/Yju+hWWbffw2Cc4wJuECiGBJJT8aTyzhJrFHKlQd7PDjI1nSGwKFqplzvTuQwCC+BXJm8C0L3xSBcP8D0N8j+aIB1UONPbvu0scOCLv4MuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9Cg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECVYB5QD4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
  "id": -576460752303422569,
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECAcjgb7c5RyDF7F0XNzWJMbQnLhIVT9fCvriZIi3tbiykqHjq97WTjfOdF9RL0Y+5gjb/Yju+hWWbffw2Cc4wJuECiGBJJT8aTyzhJrFHKlQd7PDjI1nSGwKFqplzvTuQwCC+BXJm8C0L3xSBcP8D0N8j+aIB1UONPbvu0scOCLv4MuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9Cg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECVYB5QD4=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECAcjgb7c5RyDF7F0XNzWJMbQnLhIVT9fCvriZIi3tbiykqHjq97WTjfOdF9RL0Y+5gjb/Yju+hWWbffw2Cc4wJuECiGBJJT8aTyzhJrFHKlQd7PDjI1nSGwKFqplzvTuQwCC+BXJm8C0L3xSBcP8D0N8j+aIB1UONPbvu0scOCLv4MuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9Cg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECVYB5QD4=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello back",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
      }
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECAcjgb7c5RyDF7F0XNzWJMbQnLhIVT9fCvriZIi3tbiykqHjq97WTjfOdF9RL0Y+5gjb/Yju+hWWbffw2Cc4wJuECiGBJJT8aTyzhJrFHKlQd7PDjI1nSGwKFqplzvTuQwCC+BXJm8C0L3xSBcP8D0N8j+aIB1UONPbvu0scOCLv4MuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9Cg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECVYB5QD4=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECAcjgb7c5RyDF7F0XNzWJMbQnLhIVT9fCvriZIi3tbiykqHjq97WTjfOdF9RL0Y+5gjb/Yju+hWWbffw2Cc4wJuECiGBJJT8aTyzhJrFHKlQd7PDjI1nSGwKFqplzvTuQwCC+BXJm8C0L3xSBcP8D0N8j+aIB1UONPbvu0scOCLv4MuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9Cg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECVYB5QD4=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "state": "tx_+P4LAfiEuECAcjgb7c5RyDF7F0XNzWJMbQnLhIVT9fCvriZIi3tbiykqHjq97WTjfOdF9RL0Y+5gjb/Yju+hWWbffw2Cc4wJuECiGBJJT8aTyzhJrFHKlQd7PDjI1nSGwKFqplzvTuQwCC+BXJm8C0L3xSBcP8D0N8j+aIB1UONPbvu0scOCLv4MuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9Cg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECVYB5QD4="
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "state": "tx_+P4LAfiEuECAcjgb7c5RyDF7F0XNzWJMbQnLhIVT9fCvriZIi3tbiykqHjq97WTjfOdF9RL0Y+5gjb/Yju+hWWbffw2Cc4wJuECiGBJJT8aTyzhJrFHKlQd7PDjI1nSGwKFqplzvTuQwCC+BXJm8C0L3xSBcP8D0N8j+aIB1UONPbvu0scOCLv4MuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKG4r9Cg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECVYB5QD4="
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
    "info": "Hello",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
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
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
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
  "method": "channels.message",
  "params": {
    "info": "Hello",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBlVdEVIq+4sZ+LaCsHiSQtT+hIN6msaZGy0bGvIKVU27oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/Aobiv0KDZtcOT2QHMSn7Ye3r6M+jqyyVjQiph/medhaKMSYXlhQMi0Z2hOQ==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422568,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECSVOrRRVYWO4+J7/L6Z+ClVs9fcospYoCf2yO2G2paCS8qSzWIwUsbi3NdfJTRdQHBd6eV976P0imyu6Ez/zgMuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDIpwLMZs="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
  "id": -576460752303422568,
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECSVOrRRVYWO4+J7/L6Z+ClVs9fcospYoCf2yO2G2paCS8qSzWIwUsbi3NdfJTRdQHBd6eV976P0imyu6Ez/zgMuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDIpwLMZs=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422567,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAyt+tEWtbdgzdtKAhsGDZneYDwRkqe4GUbKu0HTuWtmm5wR1tyU4sPr31wt1DZPriJ6K8IsKnn+T4RupI8oUkHuECSVOrRRVYWO4+J7/L6Z+ClVs9fcospYoCf2yO2G2paCS8qSzWIwUsbi3NdfJTRdQHBd6eV976P0imyu6Ez/zgMuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDIsggy6g="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
  "id": -576460752303422567,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAyt+tEWtbdgzdtKAhsGDZneYDwRkqe4GUbKu0HTuWtmm5wR1tyU4sPr31wt1DZPriJ6K8IsKnn+T4RupI8oUkHuECSVOrRRVYWO4+J7/L6Z+ClVs9fcospYoCf2yO2G2paCS8qSzWIwUsbi3NdfJTRdQHBd6eV976P0imyu6Ez/zgMuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDIsggy6g=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAyt+tEWtbdgzdtKAhsGDZneYDwRkqe4GUbKu0HTuWtmm5wR1tyU4sPr31wt1DZPriJ6K8IsKnn+T4RupI8oUkHuECSVOrRRVYWO4+J7/L6Z+ClVs9fcospYoCf2yO2G2paCS8qSzWIwUsbi3NdfJTRdQHBd6eV976P0imyu6Ez/zgMuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDIsggy6g=",
      "type": "channel_withdraw_tx"
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
    "info": "Hello",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "message": {
        "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
      }
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAyt+tEWtbdgzdtKAhsGDZneYDwRkqe4GUbKu0HTuWtmm5wR1tyU4sPr31wt1DZPriJ6K8IsKnn+T4RupI8oUkHuECSVOrRRVYWO4+J7/L6Z+ClVs9fcospYoCf2yO2G2paCS8qSzWIwUsbi3NdfJTRdQHBd6eV976P0imyu6Ez/zgMuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDIsggy6g=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAyt+tEWtbdgzdtKAhsGDZneYDwRkqe4GUbKu0HTuWtmm5wR1tyU4sPr31wt1DZPriJ6K8IsKnn+T4RupI8oUkHuECSVOrRRVYWO4+J7/L6Z+ClVs9fcospYoCf2yO2G2paCS8qSzWIwUsbi3NdfJTRdQHBd6eV976P0imyu6Ez/zgMuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDIsggy6g=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "state": "tx_+P4LAfiEuEAyt+tEWtbdgzdtKAhsGDZneYDwRkqe4GUbKu0HTuWtmm5wR1tyU4sPr31wt1DZPriJ6K8IsKnn+T4RupI8oUkHuECSVOrRRVYWO4+J7/L6Z+ClVs9fcospYoCf2yO2G2paCS8qSzWIwUsbi3NdfJTRdQHBd6eV976P0imyu6Ez/zgMuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDIsggy6g="
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "state": "tx_+P4LAfiEuEAyt+tEWtbdgzdtKAhsGDZneYDwRkqe4GUbKu0HTuWtmm5wR1tyU4sPr31wt1DZPriJ6K8IsKnn+T4RupI8oUkHuECSVOrRRVYWO4+J7/L6Z+ClVs9fcospYoCf2yO2G2paCS8qSzWIwUsbi3NdfJTRdQHBd6eV976P0imyu6Ez/zgMuHT4cjQBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9Cg2bXDk9kBzEp+2Ht6+jPo6sslY0IqYf5nnYWijEmF5YUDIsggy6g="
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBlVdEVIq+4sZ+LaCsHiSQtT+hIN6msaZGy0bGvIKVU27oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/2GHLHOiuv/AIYPXtZ/KABWuBLRSA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422566,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECfmG1vqWKA1WHInBGe26HsyvOxurXZWmibVrG9A6ViR9pj3LLTK/0KBD4pySuZbOYsXIAIwLFfsMkGTJl2wnUEuF/4XTUBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAVqxv1Ug="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
  "id": -576460752303422566,
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECfmG1vqWKA1WHInBGe26HsyvOxurXZWmibVrG9A6ViR9pj3LLTK/0KBD4pySuZbOYsXIAIwLFfsMkGTJl2wnUEuF/4XTUBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAVqxv1Ug=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422565,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAOBJToVz39ZBWOo38kMlb/66YQvFjW29g8IrwO8LN2j5kuatGTBOZ5rUMHMiV2sj6B0UlMHovJghg12PpvJGwMuECfmG1vqWKA1WHInBGe26HsyvOxurXZWmibVrG9A6ViR9pj3LLTK/0KBD4pySuZbOYsXIAIwLFfsMkGTJl2wnUEuF/4XTUBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAVsoo87c="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
  "id": -576460752303422565,
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAOBJToVz39ZBWOo38kMlb/66YQvFjW29g8IrwO8LN2j5kuatGTBOZ5rUMHMiV2sj6B0UlMHovJghg12PpvJGwMuECfmG1vqWKA1WHInBGe26HsyvOxurXZWmibVrG9A6ViR9pj3LLTK/0KBD4pySuZbOYsXIAIwLFfsMkGTJl2wnUEuF/4XTUBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAVsoo87c=",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAOBJToVz39ZBWOo38kMlb/66YQvFjW29g8IrwO8LN2j5kuatGTBOZ5rUMHMiV2sj6B0UlMHovJghg12PpvJGwMuECfmG1vqWKA1WHInBGe26HsyvOxurXZWmibVrG9A6ViR9pj3LLTK/0KBD4pySuZbOYsXIAIwLFfsMkGTJl2wnUEuF/4XTUBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAVsoo87c=",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAOBJToVz39ZBWOo38kMlb/66YQvFjW29g8IrwO8LN2j5kuatGTBOZ5rUMHMiV2sj6B0UlMHovJghg12PpvJGwMuECfmG1vqWKA1WHInBGe26HsyvOxurXZWmibVrG9A6ViR9pj3LLTK/0KBD4pySuZbOYsXIAIwLFfsMkGTJl2wnUEuF/4XTUBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAVsoo87c=",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAOBJToVz39ZBWOo38kMlb/66YQvFjW29g8IrwO8LN2j5kuatGTBOZ5rUMHMiV2sj6B0UlMHovJghg12PpvJGwMuECfmG1vqWKA1WHInBGe26HsyvOxurXZWmibVrG9A6ViR9pj3LLTK/0KBD4pySuZbOYsXIAIwLFfsMkGTJl2wnUEuF/4XTUBoQZVXRFSKvuLGfi2grB4kkLU/oSDeprGmRstGxryClVNu6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv9hhyxzorr/wCGD17WfygAVsoo87c=",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
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
    "channel_id": "ch_ebVqatA9bjmnKADq4ZAm3cWk7k4ocS5nZ7jUjPDYySq1i6aY3",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection
