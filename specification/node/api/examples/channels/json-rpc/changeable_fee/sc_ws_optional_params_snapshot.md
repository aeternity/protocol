
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
      "fsm_id": "ba_sqor0rB9COK6vo62dYV/rOPWSpk3gB6yuO+Pgqnl7qN6KwBT"
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
      "fsm_id": "ba_ISXm7btDRnURb8iCZWwkDRl+8Fx0WQ1fETEQdcgUbPpaELeL"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY/COLXwQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422656,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDVOAzSvloEiVswkfHtTULQnKIzh3zkmWxbIXC9gbdpbx55RttWvXIoIA08Jh7GVUVpPOs/qiwlfvtfQamhkCQIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGP7/uiV8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422656,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_ISXm7btDRnURb8iCZWwkDRl+8Fx0WQ1fETEQdcgUbPpaELeL"
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDVOAzSvloEiVswkfHtTULQnKIzh3zkmWxbIXC9gbdpbx55RttWvXIoIA08Jh7GVUVpPOs/qiwlfvtfQamhkCQIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGP7/uiV8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422655,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAgA9Y+P2TklW/3fT18dR22E4H8nbO4ETeL4p+XfldqjxxVB703k+Jcwg6XBF6BxEe8VBZ7BdnvPfDFIVDjGnZCLhA1TgM0r5aBIlbMJHx7U1C0JyiM4d85JlsWyFwvYG3aW8eeUbbVr1yKCANPCYexlVFaTzrP6osJX77X0GpoZAkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rj9xRrQX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422655,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAgA9Y+P2TklW/3fT18dR22E4H8nbO4ETeL4p+XfldqjxxVB703k+Jcwg6XBF6BxEe8VBZ7BdnvPfDFIVDjGnZCLhA1TgM0r5aBIlbMJHx7U1C0JyiM4d85JlsWyFwvYG3aW8eeUbbVr1yKCANPCYexlVFaTzrP6osJX77X0GpoZAkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rj9xRrQX",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_sqor0rB9COK6vo62dYV/rOPWSpk3gB6yuO+Pgqnl7qN6KwBT"
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAgA9Y+P2TklW/3fT18dR22E4H8nbO4ETeL4p+XfldqjxxVB703k+Jcwg6XBF6BxEe8VBZ7BdnvPfDFIVDjGnZCLhA1TgM0r5aBIlbMJHx7U1C0JyiM4d85JlsWyFwvYG3aW8eeUbbVr1yKCANPCYexlVFaTzrP6osJX77X0GpoZAkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rj9xRrQX",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAgA9Y+P2TklW/3fT18dR22E4H8nbO4ETeL4p+XfldqjxxVB703k+Jcwg6XBF6BxEe8VBZ7BdnvPfDFIVDjGnZCLhA1TgM0r5aBIlbMJHx7U1C0JyiM4d85JlsWyFwvYG3aW8eeUbbVr1yKCANPCYexlVFaTzrP6osJX77X0GpoZAkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rj9xRrQX",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAgA9Y+P2TklW/3fT18dR22E4H8nbO4ETeL4p+XfldqjxxVB703k+Jcwg6XBF6BxEe8VBZ7BdnvPfDFIVDjGnZCLhA1TgM0r5aBIlbMJHx7U1C0JyiM4d85JlsWyFwvYG3aW8eeUbbVr1yKCANPCYexlVFaTzrP6osJX77X0GpoZAkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rj9xRrQX",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "message": {
        "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "message": {
        "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
  "id": -576460752303422654,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422654,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+QENCwH4hLhAgA9Y+P2TklW/3fT18dR22E4H8nbO4ETeL4p+XfldqjxxVB703k+Jcwg6XBF6BxEe8VBZ7BdnvPfDFIVDjGnZCLhA1TgM0r5aBIlbMJHx7U1C0JyiM4d85JlsWyFwvYG3aW8eeUbbVr1yKCANPCYexlVFaTzrP6osJX77X0GpoZAkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rj9xRrQX"
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+QENCwH4hLhAgA9Y+P2TklW/3fT18dR22E4H8nbO4ETeL4p+XfldqjxxVB703k+Jcwg6XBF6BxEe8VBZ7BdnvPfDFIVDjGnZCLhA1TgM0r5aBIlbMJHx7U1C0JyiM4d85JlsWyFwvYG3aW8eeUbbVr1yKCANPCYexlVFaTzrP6osJX77X0GpoZAkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rj9xRrQX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422653,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422653,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QENCwH4hLhAgA9Y+P2TklW/3fT18dR22E4H8nbO4ETeL4p+XfldqjxxVB703k+Jcwg6XBF6BxEe8VBZ7BdnvPfDFIVDjGnZCLhA1TgM0r5aBIlbMJHx7U1C0JyiM4d85JlsWyFwvYG3aW8eeUbbVr1yKCANPCYexlVFaTzrP6osJX77X0GpoZAkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rj9xRrQX",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422652,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422652,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnblmlmd46SMzlY6n5uRDPkeAr+LSe+EIOhaiJ9J/QK4AqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCypHtAlI=",
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
  "id": -576460752303422651,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAMRw1WPlDzCS3JTZHAhEDhh0yH2rHWbEQ2kp7u2JQfDzaTX6mtjiY5U9N5CHhBJn2G22Jjm8wdWOYRiz6KbHcAuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoegFEz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422651,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAMRw1WPlDzCS3JTZHAhEDhh0yH2rHWbEQ2kp7u2JQfDzaTX6mtjiY5U9N5CHhBJn2G22Jjm8wdWOYRiz6KbHcAuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoegFEz",
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
  "id": -576460752303422650,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAMRw1WPlDzCS3JTZHAhEDhh0yH2rHWbEQ2kp7u2JQfDzaTX6mtjiY5U9N5CHhBJn2G22Jjm8wdWOYRiz6KbHcAuEBLNE/kmBHxStjaaTd5VNuKHpB+5NOcO8qE/3idX4/pU/qmql4oOCnzgrOXHG1+eR45OOQIFtzCcSl+NJzCYscFuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrJPH2R"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422650,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEAMRw1WPlDzCS3JTZHAhEDhh0yH2rHWbEQ2kp7u2JQfDzaTX6mtjiY5U9N5CHhBJn2G22Jjm8wdWOYRiz6KbHcAuEBLNE/kmBHxStjaaTd5VNuKHpB+5NOcO8qE/3idX4/pU/qmql4oOCnzgrOXHG1+eR45OOQIFtzCcSl+NJzCYscFuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrJPH2R"
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEAMRw1WPlDzCS3JTZHAhEDhh0yH2rHWbEQ2kp7u2JQfDzaTX6mtjiY5U9N5CHhBJn2G22Jjm8wdWOYRiz6KbHcAuEBLNE/kmBHxStjaaTd5VNuKHpB+5NOcO8qE/3idX4/pU/qmql4oOCnzgrOXHG1+eR45OOQIFtzCcSl+NJzCYscFuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrJPH2R"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422649,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422649,
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
  "id": -576460752303422648,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422648,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAMRw1WPlDzCS3JTZHAhEDhh0yH2rHWbEQ2kp7u2JQfDzaTX6mtjiY5U9N5CHhBJn2G22Jjm8wdWOYRiz6KbHcAuEBLNE/kmBHxStjaaTd5VNuKHpB+5NOcO8qE/3idX4/pU/qmql4oOCnzgrOXHG1+eR45OOQIFtzCcSl+NJzCYscFuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrJPH2R",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422647,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422647,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBnblmlmd46SMzlY6n5uRDPkeAr+LSe+EIOhaiJ9J/QK4oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAMRw1WPlDzCS3JTZHAhEDhh0yH2rHWbEQ2kp7u2JQfDzaTX6mtjiY5U9N5CHhBJn2G22Jjm8wdWOYRiz6KbHcAuEBLNE/kmBHxStjaaTd5VNuKHpB+5NOcO8qE/3idX4/pU/qmql4oOCnzgrOXHG1+eR45OOQIFtzCcSl+NJzCYscFuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoAhnBIhhsPP0C0WPUG",
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
    "signed_tx": "tx_+QFxCwH4QrhA6t8DMxJH6Zb7jje5KKUHRMZkizS0OexWhRElylNUYmtbPW2houtjfrqcgbNU9ZLlpoqcAg4BkYbZq3Hm3fhsAbkBKPkBJTsBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhADEcNVj5Q8wktyU2RwIRA4YdMh9qx1mxENpKe7tiUHw82k1+prY4mOVPTeQh4QSZ9httiY5vMHVjmEYs+imx3ALhASzRP5JgR8UrY2mk3eVTbih6QfuTTnDvKhP94nV+P6VP6pqpeKDgp84KzlxxtfnkeOTjkCBbcwnEpfjScwmLHBbhI+EY5AqEGduWaWZ3jpIzOVjqfm5EM+R4Cv4tJ74Qg6FqIn0n9ArgCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIZwSIYbDz9A7dbEdg=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422646,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422646,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnblmlmd46SMzlY6n5uRDPkeAr+LSe+EIOhaiJ9J/QK4A6CyPuq+gQA2a6qmnwMyrfvY3kyHmlBoHoJrMzYXSPbNfMqcfe8=",
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
  "id": -576460752303422645,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAD8bus2OvclapUruWtPbPBpskpAN2zPE2RG37EInnSDIZcn8jeaxVaQ9vKp7Bag9/OKc8ise2Mt5AnIZmm/10AuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXxBxfrq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422645,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAD8bus2OvclapUruWtPbPBpskpAN2zPE2RG37EInnSDIZcn8jeaxVaQ9vKp7Bag9/OKc8ise2Mt5AnIZmm/10AuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXxBxfrq",
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
  "id": -576460752303422644,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAD8bus2OvclapUruWtPbPBpskpAN2zPE2RG37EInnSDIZcn8jeaxVaQ9vKp7Bag9/OKc8ise2Mt5AnIZmm/10AuEA3Yj9BvQFVcXNS4O4EylVjRKMMhXCE3ScqwRdG9NwiRgpgquldsrxTux9D7iQc3gl15VuKa+3s2N5EK2ru1vQEuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXy+4UzS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422644,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEAD8bus2OvclapUruWtPbPBpskpAN2zPE2RG37EInnSDIZcn8jeaxVaQ9vKp7Bag9/OKc8ise2Mt5AnIZmm/10AuEA3Yj9BvQFVcXNS4O4EylVjRKMMhXCE3ScqwRdG9NwiRgpgquldsrxTux9D7iQc3gl15VuKa+3s2N5EK2ru1vQEuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXy+4UzS"
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEAD8bus2OvclapUruWtPbPBpskpAN2zPE2RG37EInnSDIZcn8jeaxVaQ9vKp7Bag9/OKc8ise2Mt5AnIZmm/10AuEA3Yj9BvQFVcXNS4O4EylVjRKMMhXCE3ScqwRdG9NwiRgpgquldsrxTux9D7iQc3gl15VuKa+3s2N5EK2ru1vQEuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXy+4UzS"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422643,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422643,
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
  "id": -576460752303422642,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422642,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAD8bus2OvclapUruWtPbPBpskpAN2zPE2RG37EInnSDIZcn8jeaxVaQ9vKp7Bag9/OKc8ise2Mt5AnIZmm/10AuEA3Yj9BvQFVcXNS4O4EylVjRKMMhXCE3ScqwRdG9NwiRgpgquldsrxTux9D7iQc3gl15VuKa+3s2N5EK2ru1vQEuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXy+4UzS",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAA7DvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/3rbPVC"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422641,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422641,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnblmlmd46SMzlY6n5uRDPkeAr+LSe+EIOhaiJ9J/QK4BKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCytdY/jY=",
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
  "id": -576460752303422640,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBuNKIaxB3d7+bN0eC09CNF2qD+siiQB6vvOLEOj/elBPbpb9ba8ukkEfLrrNDv+qg7JP51GMjW/xaSVXyqtWEGuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqGnIsN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422640,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBuNKIaxB3d7+bN0eC09CNF2qD+siiQB6vvOLEOj/elBPbpb9ba8ukkEfLrrNDv+qg7JP51GMjW/xaSVXyqtWEGuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqGnIsN",
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
  "id": -576460752303422639,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAD3mA1WVpkILZ1NCU0KKEuU3HmRSB1h/3TqEQd52BCFfBLud9gUnNlyveV11er7wMRspQyyxop5dhP/AX2wv0AuEBuNKIaxB3d7+bN0eC09CNF2qD+siiQB6vvOLEOj/elBPbpb9ba8ukkEfLrrNDv+qg7JP51GMjW/xaSVXyqtWEGuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsreBDbL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422639,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEAD3mA1WVpkILZ1NCU0KKEuU3HmRSB1h/3TqEQd52BCFfBLud9gUnNlyveV11er7wMRspQyyxop5dhP/AX2wv0AuEBuNKIaxB3d7+bN0eC09CNF2qD+siiQB6vvOLEOj/elBPbpb9ba8ukkEfLrrNDv+qg7JP51GMjW/xaSVXyqtWEGuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsreBDbL"
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEAD3mA1WVpkILZ1NCU0KKEuU3HmRSB1h/3TqEQd52BCFfBLud9gUnNlyveV11er7wMRspQyyxop5dhP/AX2wv0AuEBuNKIaxB3d7+bN0eC09CNF2qD+siiQB6vvOLEOj/elBPbpb9ba8ukkEfLrrNDv+qg7JP51GMjW/xaSVXyqtWEGuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsreBDbL"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422638,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422638,
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
  "id": -576460752303422637,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422637,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAD3mA1WVpkILZ1NCU0KKEuU3HmRSB1h/3TqEQd52BCFfBLud9gUnNlyveV11er7wMRspQyyxop5dhP/AX2wv0AuEBuNKIaxB3d7+bN0eC09CNF2qD+siiQB6vvOLEOj/elBPbpb9ba8ukkEfLrrNDv+qg7JP51GMjW/xaSVXyqtWEGuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsreBDbL",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA6t8DMxJH6Zb7jje5KKUHRMZkizS0OexWhRElylNUYmtbPW2houtjfrqcgbNU9ZLlpoqcAg4BkYbZq3Hm3fhsAbkBKPkBJTsBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhADEcNVj5Q8wktyU2RwIRA4YdMh9qx1mxENpKe7tiUHw82k1+prY4mOVPTeQh4QSZ9httiY5vMHVjmEYs+imx3ALhASzRP5JgR8UrY2mk3eVTbih6QfuTTnDvKhP94nV+P6VP6pqpeKDgp84KzlxxtfnkeOTjkCBbcwnEpfjScwmLHBbhI+EY5AqEGduWaWZ3jpIzOVjqfm5EM+R4Cv4tJ74Qg6FqIn0n9ArgCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIZwSIYbDz9A7dbEdg==",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA6t8DMxJH6Zb7jje5KKUHRMZkizS0OexWhRElylNUYmtbPW2houtjfrqcgbNU9ZLlpoqcAg4BkYbZq3Hm3fhsAbkBKPkBJTsBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhADEcNVj5Q8wktyU2RwIRA4YdMh9qx1mxENpKe7tiUHw82k1+prY4mOVPTeQh4QSZ9httiY5vMHVjmEYs+imx3ALhASzRP5JgR8UrY2mk3eVTbih6QfuTTnDvKhP94nV+P6VP6pqpeKDgp84KzlxxtfnkeOTjkCBbcwnEpfjScwmLHBbhI+EY5AqEGduWaWZ3jpIzOVjqfm5EM+R4Cv4tJ74Qg6FqIn0n9ArgCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIZwSIYbDz9A7dbEdg==",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "%\u001a�X�3j�'�\u0017�s&\u0014�e\u0019f�&E0���S\b�",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422636,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422636,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAD3mA1WVpkILZ1NCU0KKEuU3HmRSB1h/3TqEQd52BCFfBLud9gUnNlyveV11er7wMRspQyyxop5dhP/AX2wv0AuEBuNKIaxB3d7+bN0eC09CNF2qD+siiQB6vvOLEOj/elBPbpb9ba8ukkEfLrrNDv+qg7JP51GMjW/xaSVXyqtWEGuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsreBDbL",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422635,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422635,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnblmlmd46SMzlY6n5uRDPkeAr+LSe+EIOhaiJ9J/QK4BaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Run5EOU=",
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
  "id": -576460752303422634,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA290zT+SQAZie/VBFtEWdXlzmpyRa6AyeuM5rbLm97U+riRk11GFXIz0CUqNfGxZuUKuEdieb3a2Hg/zEqkS8PuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEakWN0D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422634,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA290zT+SQAZie/VBFtEWdXlzmpyRa6AyeuM5rbLm97U+riRk11GFXIz0CUqNfGxZuUKuEdieb3a2Hg/zEqkS8PuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEakWN0D",
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
  "id": -576460752303422633,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA290zT+SQAZie/VBFtEWdXlzmpyRa6AyeuM5rbLm97U+riRk11GFXIz0CUqNfGxZuUKuEdieb3a2Hg/zEqkS8PuECiyPizWiCY91zFPuCZEURD/c2mESNhP+7eXOw2H7mtWKJA7j+eeDbqxn7Pm2kd7/UaHb8HKB6V2KTjUkMzNpMHuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYnDdZq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422633,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEA290zT+SQAZie/VBFtEWdXlzmpyRa6AyeuM5rbLm97U+riRk11GFXIz0CUqNfGxZuUKuEdieb3a2Hg/zEqkS8PuECiyPizWiCY91zFPuCZEURD/c2mESNhP+7eXOw2H7mtWKJA7j+eeDbqxn7Pm2kd7/UaHb8HKB6V2KTjUkMzNpMHuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYnDdZq"
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEA290zT+SQAZie/VBFtEWdXlzmpyRa6AyeuM5rbLm97U+riRk11GFXIz0CUqNfGxZuUKuEdieb3a2Hg/zEqkS8PuECiyPizWiCY91zFPuCZEURD/c2mESNhP+7eXOw2H7mtWKJA7j+eeDbqxn7Pm2kd7/UaHb8HKB6V2KTjUkMzNpMHuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYnDdZq"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422632,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422632,
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
  "id": -576460752303422631,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422631,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA290zT+SQAZie/VBFtEWdXlzmpyRa6AyeuM5rbLm97U+riRk11GFXIz0CUqNfGxZuUKuEdieb3a2Hg/zEqkS8PuECiyPizWiCY91zFPuCZEURD/c2mESNhP+7eXOw2H7mtWKJA7j+eeDbqxn7Pm2kd7/UaHb8HKB6V2KTjUkMzNpMHuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYnDdZq",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422630,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422630,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBnblmlmd46SMzlY6n5uRDPkeAr+LSe+EIOhaiJ9J/QK4oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEA290zT+SQAZie/VBFtEWdXlzmpyRa6AyeuM5rbLm97U+riRk11GFXIz0CUqNfGxZuUKuEdieb3a2Hg/zEqkS8PuECiyPizWiCY91zFPuCZEURD/c2mESNhP+7eXOw2H7mtWKJA7j+eeDbqxn7Pm2kd7/UaHb8HKB6V2KTjUkMzNpMHuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhnBIhhsPPxm+3ntu",
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
    "signed_tx": "tx_+QFxCwH4QrhAuAkHHHgpXuZ/UlXibD4W9Sj15ptWk64CV9lX35CpsEZqCr88hi2QjKY4BM33QAhvaqe+BiB4V0Fu/ej7f3OLB7kBKPkBJTsBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhANvdM0/kkAGYnv1QRbRFnV5c5qckWugMnrjOa2y5ve1Pq4kZNdRhVyM9AlKjXxsWblCrhHYnm92th4P8xKpEvD7hAosj4s1ogmPdcxT7gmRFEQ/3NphEjYT/u3lzsNh+5rViiQO4/nng26sZ+z5tpHe/1Gh2/Bygeldik41JDMzaTB7hI+EY5AqEGduWaWZ3jpIzOVjqfm5EM+R4Cv4tJ74Qg6FqIn0n9ArgFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIZwSIYbDz8ZIk9LlA=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422629,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422629,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnblmlmd46SMzlY6n5uRDPkeAr+LSe+EIOhaiJ9J/QK4BqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyjJvll8=",
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
  "id": -576460752303422628,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDccbvbmo0IBUb9sqUV6Ft5C0zcJl+8U8nORWUbNI6zqAMNj0qMgqK0Uns/eZym3JXS4b2JwIx0KzFNbHbz12MBuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsphChyb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422628,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDccbvbmo0IBUb9sqUV6Ft5C0zcJl+8U8nORWUbNI6zqAMNj0qMgqK0Uns/eZym3JXS4b2JwIx0KzFNbHbz12MBuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsphChyb",
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
  "id": -576460752303422627,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC9iyYRptPCAeDpt1yUG3IbztRhX+wGr6YsJHdMA1VRPKQ6Dz5qxbIxpZHaA6WH3impXvM58DXu9cWb+qn617EGuEDccbvbmo0IBUb9sqUV6Ft5C0zcJl+8U8nORWUbNI6zqAMNj0qMgqK0Uns/eZym3JXS4b2JwIx0KzFNbHbz12MBuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp5d+nD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422627,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEC9iyYRptPCAeDpt1yUG3IbztRhX+wGr6YsJHdMA1VRPKQ6Dz5qxbIxpZHaA6WH3impXvM58DXu9cWb+qn617EGuEDccbvbmo0IBUb9sqUV6Ft5C0zcJl+8U8nORWUbNI6zqAMNj0qMgqK0Uns/eZym3JXS4b2JwIx0KzFNbHbz12MBuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp5d+nD"
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuEC9iyYRptPCAeDpt1yUG3IbztRhX+wGr6YsJHdMA1VRPKQ6Dz5qxbIxpZHaA6WH3impXvM58DXu9cWb+qn617EGuEDccbvbmo0IBUb9sqUV6Ft5C0zcJl+8U8nORWUbNI6zqAMNj0qMgqK0Uns/eZym3JXS4b2JwIx0KzFNbHbz12MBuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp5d+nD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422626,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422626,
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
  "id": -576460752303422625,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422625,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC9iyYRptPCAeDpt1yUG3IbztRhX+wGr6YsJHdMA1VRPKQ6Dz5qxbIxpZHaA6WH3impXvM58DXu9cWb+qn617EGuEDccbvbmo0IBUb9sqUV6Ft5C0zcJl+8U8nORWUbNI6zqAMNj0qMgqK0Uns/eZym3JXS4b2JwIx0KzFNbHbz12MBuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp5d+nD",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422624,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422624,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnblmlmd46SMzlY6n5uRDPkeAr+LSe+EIOhaiJ9J/QK4B6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RvPyVQY=",
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
  "id": -576460752303422623,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDI0KgTZ9eEE0R3t2gAM86UKcCXR0nVRZxlIVxHai7Wsh8br+f3lWfqV3BFnZvLG/5nw5f3J0PYLL0Ej2bNBbQLuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEazTUrr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422623,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDI0KgTZ9eEE0R3t2gAM86UKcCXR0nVRZxlIVxHai7Wsh8br+f3lWfqV3BFnZvLG/5nw5f3J0PYLL0Ej2bNBbQLuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEazTUrr",
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
  "id": -576460752303422622,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECM1MrLTVprFR/RQ8b4JKBIU58K8WNHHp+qy6dcLXgPrnaA/fmzrE0WJIHvN68xdPogYPlcCd8Y3r77Dcha5boPuEDI0KgTZ9eEE0R3t2gAM86UKcCXR0nVRZxlIVxHai7Wsh8br+f3lWfqV3BFnZvLG/5nw5f3J0PYLL0Ej2bNBbQLuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZnFOHU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422622,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuECM1MrLTVprFR/RQ8b4JKBIU58K8WNHHp+qy6dcLXgPrnaA/fmzrE0WJIHvN68xdPogYPlcCd8Y3r77Dcha5boPuEDI0KgTZ9eEE0R3t2gAM86UKcCXR0nVRZxlIVxHai7Wsh8br+f3lWfqV3BFnZvLG/5nw5f3J0PYLL0Ej2bNBbQLuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZnFOHU"
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "state": "tx_+NILAfiEuECM1MrLTVprFR/RQ8b4JKBIU58K8WNHHp+qy6dcLXgPrnaA/fmzrE0WJIHvN68xdPogYPlcCd8Y3r77Dcha5boPuEDI0KgTZ9eEE0R3t2gAM86UKcCXR0nVRZxlIVxHai7Wsh8br+f3lWfqV3BFnZvLG/5nw5f3J0PYLL0Ej2bNBbQLuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZnFOHU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422621,
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
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422621,
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
  "id": -576460752303422620,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422620,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECM1MrLTVprFR/RQ8b4JKBIU58K8WNHHp+qy6dcLXgPrnaA/fmzrE0WJIHvN68xdPogYPlcCd8Y3r77Dcha5boPuEDI0KgTZ9eEE0R3t2gAM86UKcCXR0nVRZxlIVxHai7Wsh8br+f3lWfqV3BFnZvLG/5nw5f3J0PYLL0Ej2bNBbQLuEj4RjkCoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZnFOHU",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAuAkHHHgpXuZ/UlXibD4W9Sj15ptWk64CV9lX35CpsEZqCr88hi2QjKY4BM33QAhvaqe+BiB4V0Fu/ej7f3OLB7kBKPkBJTsBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhANvdM0/kkAGYnv1QRbRFnV5c5qckWugMnrjOa2y5ve1Pq4kZNdRhVyM9AlKjXxsWblCrhHYnm92th4P8xKpEvD7hAosj4s1ogmPdcxT7gmRFEQ/3NphEjYT/u3lzsNh+5rViiQO4/nng26sZ+z5tpHe/1Gh2/Bygeldik41JDMzaTB7hI+EY5AqEGduWaWZ3jpIzOVjqfm5EM+R4Cv4tJ74Qg6FqIn0n9ArgFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIZwSIYbDz8ZIk9LlA==",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAuAkHHHgpXuZ/UlXibD4W9Sj15ptWk64CV9lX35CpsEZqCr88hi2QjKY4BM33QAhvaqe+BiB4V0Fu/ej7f3OLB7kBKPkBJTsBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhANvdM0/kkAGYnv1QRbRFnV5c5qckWugMnrjOa2y5ve1Pq4kZNdRhVyM9AlKjXxsWblCrhHYnm92th4P8xKpEvD7hAosj4s1ogmPdcxT7gmRFEQ/3NphEjYT/u3lzsNh+5rViiQO4/nng26sZ+z5tpHe/1Gh2/Bygeldik41JDMzaTB7hI+EY5AqEGduWaWZ3jpIzOVjqfm5EM+R4Cv4tJ74Qg6FqIn0n9ArgFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIZwSIYbDz8ZIk9LlA==",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "�=>\u0015��xg�GW�֡�&n���3�\u000eC���h6�",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBnblmlmd46SMzlY6n5uRDPkeAr+LSe+EIOhaiJ9J/QK4oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/+GHLHOiuwBAIYPXtZ/KABBKi708g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422619,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECbtcf7TWTom1CXb+VZ7SPBFxrvQI0IxlqjRmBumy3w+BJ48zxSBHhfS9lSnf7h+cPGglvygFlTYx9fwsjSTBkLuF/4XTUBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAQZcVhjU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422619,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECbtcf7TWTom1CXb+VZ7SPBFxrvQI0IxlqjRmBumy3w+BJ48zxSBHhfS9lSnf7h+cPGglvygFlTYx9fwsjSTBkLuF/4XTUBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAQZcVhjU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422618,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBXr9iPEEPPuyuGgM1v+vWC5P8MFJfKZlf8Lw+/GzyLlsiM8Oz85f0D6imlWs7ShNdUtc9wrA99ssLl29E9rxEOuECbtcf7TWTom1CXb+VZ7SPBFxrvQI0IxlqjRmBumy3w+BJ48zxSBHhfS9lSnf7h+cPGglvygFlTYx9fwsjSTBkLuF/4XTUBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAQWgY7Aw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
  "id": -576460752303422618,
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBXr9iPEEPPuyuGgM1v+vWC5P8MFJfKZlf8Lw+/GzyLlsiM8Oz85f0D6imlWs7ShNdUtc9wrA99ssLl29E9rxEOuECbtcf7TWTom1CXb+VZ7SPBFxrvQI0IxlqjRmBumy3w+BJ48zxSBHhfS9lSnf7h+cPGglvygFlTYx9fwsjSTBkLuF/4XTUBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAQWgY7Aw=",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBXr9iPEEPPuyuGgM1v+vWC5P8MFJfKZlf8Lw+/GzyLlsiM8Oz85f0D6imlWs7ShNdUtc9wrA99ssLl29E9rxEOuECbtcf7TWTom1CXb+VZ7SPBFxrvQI0IxlqjRmBumy3w+BJ48zxSBHhfS9lSnf7h+cPGglvygFlTYx9fwsjSTBkLuF/4XTUBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAQWgY7Aw=",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBXr9iPEEPPuyuGgM1v+vWC5P8MFJfKZlf8Lw+/GzyLlsiM8Oz85f0D6imlWs7ShNdUtc9wrA99ssLl29E9rxEOuECbtcf7TWTom1CXb+VZ7SPBFxrvQI0IxlqjRmBumy3w+BJ48zxSBHhfS9lSnf7h+cPGglvygFlTYx9fwsjSTBkLuF/4XTUBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAQWgY7Aw=",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBXr9iPEEPPuyuGgM1v+vWC5P8MFJfKZlf8Lw+/GzyLlsiM8Oz85f0D6imlWs7ShNdUtc9wrA99ssLl29E9rxEOuECbtcf7TWTom1CXb+VZ7SPBFxrvQI0IxlqjRmBumy3w+BJ48zxSBHhfS9lSnf7h+cPGglvygFlTYx9fwsjSTBkLuF/4XTUBoQZ25ZpZneOkjM5WOp+bkQz5HgK/i0nvhCDoWoifSf0CuKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAQWgY7Aw=",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
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
    "channel_id": "ch_uN4ZWV87SviC5P6AxA9eXhr6wWoohqM9JsRcL3tyTdT3anZfy",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
