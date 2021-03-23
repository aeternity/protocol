
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
      "fsm_id": "ba_IWT8pwwq0VkSLj+OaEPm6XKksTn4Za7khp5S8IUzVM73a8Qr"
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
      "fsm_id": "ba_9sBrIIw76dvp29JWCHO1TMFWi0KwfuExaGYTpUYbZqcqfMWd"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZvdvMqsw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422472,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECRTqXYsWgZ6ey+LJGlVqDbXoRIKE9fQ+2ESZ60NT/wO6AOSvTHT2rfAx0byZ0qT17Q+3/gie70J5tmaHrS6d8DuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGb68D7L4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422472,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_9sBrIIw76dvp29JWCHO1TMFWi0KwfuExaGYTpUYbZqcqfMWd"
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECRTqXYsWgZ6ey+LJGlVqDbXoRIKE9fQ+2ESZ60NT/wO6AOSvTHT2rfAx0byZ0qT17Q+3/gie70J5tmaHrS6d8DuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGb68D7L4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422471,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAkU6l2LFoGensviyRpVag216ESChPX0PthEmetDU/8DugDkr0x09q3wMdG8mdKk9e0Pt/4Inu9CebZmh60unfA7hAwvVft/8U6xVXt/MF+IPHR2JDeNpy5zwKA59aPbL6BaF4v3uImDtMTVZz+HRs79OEKJcAlDUHEdyFjkjrRJAABbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rm9YK3Ho"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422471,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAkU6l2LFoGensviyRpVag216ESChPX0PthEmetDU/8DugDkr0x09q3wMdG8mdKk9e0Pt/4Inu9CebZmh60unfA7hAwvVft/8U6xVXt/MF+IPHR2JDeNpy5zwKA59aPbL6BaF4v3uImDtMTVZz+HRs79OEKJcAlDUHEdyFjkjrRJAABbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rm9YK3Ho",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_IWT8pwwq0VkSLj+OaEPm6XKksTn4Za7khp5S8IUzVM73a8Qr"
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAkU6l2LFoGensviyRpVag216ESChPX0PthEmetDU/8DugDkr0x09q3wMdG8mdKk9e0Pt/4Inu9CebZmh60unfA7hAwvVft/8U6xVXt/MF+IPHR2JDeNpy5zwKA59aPbL6BaF4v3uImDtMTVZz+HRs79OEKJcAlDUHEdyFjkjrRJAABbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rm9YK3Ho",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAkU6l2LFoGensviyRpVag216ESChPX0PthEmetDU/8DugDkr0x09q3wMdG8mdKk9e0Pt/4Inu9CebZmh60unfA7hAwvVft/8U6xVXt/MF+IPHR2JDeNpy5zwKA59aPbL6BaF4v3uImDtMTVZz+HRs79OEKJcAlDUHEdyFjkjrRJAABbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rm9YK3Ho",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAkU6l2LFoGensviyRpVag216ESChPX0PthEmetDU/8DugDkr0x09q3wMdG8mdKk9e0Pt/4Inu9CebZmh60unfA7hAwvVft/8U6xVXt/MF+IPHR2JDeNpy5zwKA59aPbL6BaF4v3uImDtMTVZz+HRs79OEKJcAlDUHEdyFjkjrRJAABbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rm9YK3Ho",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "message": {
        "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "message": {
        "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
  "id": -576460752303422470,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422470,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+QENCwH4hLhAkU6l2LFoGensviyRpVag216ESChPX0PthEmetDU/8DugDkr0x09q3wMdG8mdKk9e0Pt/4Inu9CebZmh60unfA7hAwvVft/8U6xVXt/MF+IPHR2JDeNpy5zwKA59aPbL6BaF4v3uImDtMTVZz+HRs79OEKJcAlDUHEdyFjkjrRJAABbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rm9YK3Ho"
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+QENCwH4hLhAkU6l2LFoGensviyRpVag216ESChPX0PthEmetDU/8DugDkr0x09q3wMdG8mdKk9e0Pt/4Inu9CebZmh60unfA7hAwvVft/8U6xVXt/MF+IPHR2JDeNpy5zwKA59aPbL6BaF4v3uImDtMTVZz+HRs79OEKJcAlDUHEdyFjkjrRJAABbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rm9YK3Ho"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422469,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422469,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QENCwH4hLhAkU6l2LFoGensviyRpVag216ESChPX0PthEmetDU/8DugDkr0x09q3wMdG8mdKk9e0Pt/4Inu9CebZmh60unfA7hAwvVft/8U6xVXt/MF+IPHR2JDeNpy5zwKA59aPbL6BaF4v3uImDtMTVZz+HRs79OEKJcAlDUHEdyFjkjrRJAABbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rm9YK3Ho",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422468,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422468,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnKzy7qDoZgUwtHrvRKheg8nVMrANgtOPro/tNZvhE+jAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyl3k7E0=",
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
  "id": -576460752303422467,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAb3BwnjVSyD414RqLfBdbWJZpNjecAx8ZBsRMdCR51ODdw41vyEHcUDCdJX351cS7u+EJhD1nlCEem0mHdzLkLuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrN/Tvd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422467,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAb3BwnjVSyD414RqLfBdbWJZpNjecAx8ZBsRMdCR51ODdw41vyEHcUDCdJX351cS7u+EJhD1nlCEem0mHdzLkLuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrN/Tvd",
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
  "id": -576460752303422466,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAb3BwnjVSyD414RqLfBdbWJZpNjecAx8ZBsRMdCR51ODdw41vyEHcUDCdJX351cS7u+EJhD1nlCEem0mHdzLkLuEB0y8D9zxcWgZXCFW3iWrcZy+ADfrInhBGskHBVC+a+jyoYcnp/0zbPq6IwKXNIA4lnvJRK/sAEk3UpYSG0Vd4LuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp+qNNG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422466,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEAb3BwnjVSyD414RqLfBdbWJZpNjecAx8ZBsRMdCR51ODdw41vyEHcUDCdJX351cS7u+EJhD1nlCEem0mHdzLkLuEB0y8D9zxcWgZXCFW3iWrcZy+ADfrInhBGskHBVC+a+jyoYcnp/0zbPq6IwKXNIA4lnvJRK/sAEk3UpYSG0Vd4LuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp+qNNG"
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEAb3BwnjVSyD414RqLfBdbWJZpNjecAx8ZBsRMdCR51ODdw41vyEHcUDCdJX351cS7u+EJhD1nlCEem0mHdzLkLuEB0y8D9zxcWgZXCFW3iWrcZy+ADfrInhBGskHBVC+a+jyoYcnp/0zbPq6IwKXNIA4lnvJRK/sAEk3UpYSG0Vd4LuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp+qNNG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422465,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422465,
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
  "id": -576460752303422464,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422464,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAb3BwnjVSyD414RqLfBdbWJZpNjecAx8ZBsRMdCR51ODdw41vyEHcUDCdJX351cS7u+EJhD1nlCEem0mHdzLkLuEB0y8D9zxcWgZXCFW3iWrcZy+ADfrInhBGskHBVC+a+jyoYcnp/0zbPq6IwKXNIA4lnvJRK/sAEk3UpYSG0Vd4LuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp+qNNG",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422463,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422463,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBnKzy7qDoZgUwtHrvRKheg8nVMrANgtOPro/tNZvhE+joQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAb3BwnjVSyD414RqLfBdbWJZpNjecAx8ZBsRMdCR51ODdw41vyEHcUDCdJX351cS7u+EJhD1nlCEem0mHdzLkLuEB0y8D9zxcWgZXCFW3iWrcZy+ADfrInhBGskHBVC+a+jyoYcnp/0zbPq6IwKXNIA4lnvJRK/sAEk3UpYSG0Vd4LuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoAhuCRDDYefnBDuytN",
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
    "signed_tx": "tx_+QFxCwH4QrhA7DJnGLYrnMXcyl/N7jHeFoM8E2ONQo5Ho4afFai5oRK4/S1VrujKPCpnvlRT8iBNyadbMvgZjZ1Hw8RB+6CnCrkBKPkBJTsBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAG9wcJ41Usg+NeEai3wXW1iWaTY3nAMfGQbETHQkedTg3cONb8hB3FAwnSV9+dXEu7vhCYQ9Z5QhHptJh3cy5C7hAdMvA/c8XFoGVwhVt4lq3GcvgA36yJ4QRrJBwVQvmvo8qGHJ6f9M2z6uiMClzSAOJZ7yUSv7ABJN1KWEhtFXeC7hI+EY5AqEGcrPLuoOhmBTC0eu9EqF6DydUysA2C04+uj+01m+ET6MCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIbgkQw2Hn5w5p9p+g=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422462,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422462,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnKzy7qDoZgUwtHrvRKheg8nVMrANgtOPro/tNZvhE+jA6CyPuq+gQA2a6qmnwMyrfvY3kyHmlBoHoJrMzYXSPbNfKoBSjE=",
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
  "id": -576460752303422461,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECqfAxiWYjWWQ/nnaR7tk5rcbxDls7K/zMF4HX6tk5Qs0qKtSzIv0WH1WYYoufYWW8Ko0AOoUY1SScl6GJrmKsHuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXxO2KR0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422461,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+JALAfhCuECqfAxiWYjWWQ/nnaR7tk5rcbxDls7K/zMF4HX6tk5Qs0qKtSzIv0WH1WYYoufYWW8Ko0AOoUY1SScl6GJrmKsHuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXxO2KR0",
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
  "id": -576460752303422460,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBXHrplOHRZHNj4HxJrVgYMwdYOgBsfieVx4aZ+dediOzOsduHSuspAEV1f28w/ijuOsfW04Jnbfd3ITYIn9gIHuECqfAxiWYjWWQ/nnaR7tk5rcbxDls7K/zMF4HX6tk5Qs0qKtSzIv0WH1WYYoufYWW8Ko0AOoUY1SScl6GJrmKsHuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzZWiLr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422460,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEBXHrplOHRZHNj4HxJrVgYMwdYOgBsfieVx4aZ+dediOzOsduHSuspAEV1f28w/ijuOsfW04Jnbfd3ITYIn9gIHuECqfAxiWYjWWQ/nnaR7tk5rcbxDls7K/zMF4HX6tk5Qs0qKtSzIv0WH1WYYoufYWW8Ko0AOoUY1SScl6GJrmKsHuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzZWiLr"
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEBXHrplOHRZHNj4HxJrVgYMwdYOgBsfieVx4aZ+dediOzOsduHSuspAEV1f28w/ijuOsfW04Jnbfd3ITYIn9gIHuECqfAxiWYjWWQ/nnaR7tk5rcbxDls7K/zMF4HX6tk5Qs0qKtSzIv0WH1WYYoufYWW8Ko0AOoUY1SScl6GJrmKsHuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzZWiLr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422459,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422459,
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
  "id": -576460752303422458,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422458,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBXHrplOHRZHNj4HxJrVgYMwdYOgBsfieVx4aZ+dediOzOsduHSuspAEV1f28w/ijuOsfW04Jnbfd3ITYIn9gIHuECqfAxiWYjWWQ/nnaR7tk5rcbxDls7K/zMF4HX6tk5Qs0qKtSzIv0WH1WYYoufYWW8Ko0AOoUY1SScl6GJrmKsHuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowOgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzZWiLr",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAA7DvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/3rbPVC"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422457,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422457,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnKzy7qDoZgUwtHrvRKheg8nVMrANgtOPro/tNZvhE+jBKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyu/WDTE=",
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
  "id": -576460752303422456,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEANWtv04IqBxwI0USiQqTMd7ck4KA26kuxeiRMJrEYVA4QuCkmOhNmfdat/U5o1E9kMOzrEHqnlK6z03cfZnA0KuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspfjxwF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422456,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+JALAfhCuEANWtv04IqBxwI0USiQqTMd7ck4KA26kuxeiRMJrEYVA4QuCkmOhNmfdat/U5o1E9kMOzrEHqnlK6z03cfZnA0KuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspfjxwF",
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
  "id": -576460752303422455,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEANWtv04IqBxwI0USiQqTMd7ck4KA26kuxeiRMJrEYVA4QuCkmOhNmfdat/U5o1E9kMOzrEHqnlK6z03cfZnA0KuECkV33XNfjPcqYi6ZedpCro1ejPS6DSjB3qaYCQfMm52VOS0s4PWiZVsMtY4MgcSrfH4STL9+sgfs+V3EXC1DQJuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspiF+ah"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422455,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEANWtv04IqBxwI0USiQqTMd7ck4KA26kuxeiRMJrEYVA4QuCkmOhNmfdat/U5o1E9kMOzrEHqnlK6z03cfZnA0KuECkV33XNfjPcqYi6ZedpCro1ejPS6DSjB3qaYCQfMm52VOS0s4PWiZVsMtY4MgcSrfH4STL9+sgfs+V3EXC1DQJuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspiF+ah"
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEANWtv04IqBxwI0USiQqTMd7ck4KA26kuxeiRMJrEYVA4QuCkmOhNmfdat/U5o1E9kMOzrEHqnlK6z03cfZnA0KuECkV33XNfjPcqYi6ZedpCro1ejPS6DSjB3qaYCQfMm52VOS0s4PWiZVsMtY4MgcSrfH4STL9+sgfs+V3EXC1DQJuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspiF+ah"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422454,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422454,
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
  "id": -576460752303422453,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422453,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEANWtv04IqBxwI0USiQqTMd7ck4KA26kuxeiRMJrEYVA4QuCkmOhNmfdat/U5o1E9kMOzrEHqnlK6z03cfZnA0KuECkV33XNfjPcqYi6ZedpCro1ejPS6DSjB3qaYCQfMm52VOS0s4PWiZVsMtY4MgcSrfH4STL9+sgfs+V3EXC1DQJuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspiF+ah",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA7DJnGLYrnMXcyl/N7jHeFoM8E2ONQo5Ho4afFai5oRK4/S1VrujKPCpnvlRT8iBNyadbMvgZjZ1Hw8RB+6CnCrkBKPkBJTsBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAG9wcJ41Usg+NeEai3wXW1iWaTY3nAMfGQbETHQkedTg3cONb8hB3FAwnSV9+dXEu7vhCYQ9Z5QhHptJh3cy5C7hAdMvA/c8XFoGVwhVt4lq3GcvgA36yJ4QRrJBwVQvmvo8qGHJ6f9M2z6uiMClzSAOJZ7yUSv7ABJN1KWEhtFXeC7hI+EY5AqEGcrPLuoOhmBTC0eu9EqF6DydUysA2C04+uj+01m+ET6MCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIbgkQw2Hn5w5p9p+g==",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA7DJnGLYrnMXcyl/N7jHeFoM8E2ONQo5Ho4afFai5oRK4/S1VrujKPCpnvlRT8iBNyadbMvgZjZ1Hw8RB+6CnCrkBKPkBJTsBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAG9wcJ41Usg+NeEai3wXW1iWaTY3nAMfGQbETHQkedTg3cONb8hB3FAwnSV9+dXEu7vhCYQ9Z5QhHptJh3cy5C7hAdMvA/c8XFoGVwhVt4lq3GcvgA36yJ4QRrJBwVQvmvo8qGHJ6f9M2z6uiMClzSAOJZ7yUSv7ABJN1KWEhtFXeC7hI+EY5AqEGcrPLuoOhmBTC0eu9EqF6DydUysA2C04+uj+01m+ET6MCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKAIbgkQw2Hn5w5p9p+g==",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "d����\u000b�ӄ�o`��T���i\u0016iq��{\u001f�W�e4",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422452,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422452,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEANWtv04IqBxwI0USiQqTMd7ck4KA26kuxeiRMJrEYVA4QuCkmOhNmfdat/U5o1E9kMOzrEHqnlK6z03cfZnA0KuECkV33XNfjPcqYi6ZedpCro1ejPS6DSjB3qaYCQfMm52VOS0s4PWiZVsMtY4MgcSrfH4STL9+sgfs+V3EXC1DQJuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspiF+ah",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422451,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422451,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnKzy7qDoZgUwtHrvRKheg8nVMrANgtOPro/tNZvhE+jBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmZFFOE=",
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
  "id": -576460752303422450,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDuLFCnzWW42XYTD0teGU5LpPe+kPI3CfulqZrhgZelyEksp4lzXNZc2ob/eSj4n/1d0acAogzfkf8cGtRnpc4MuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4/HaP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422450,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDuLFCnzWW42XYTD0teGU5LpPe+kPI3CfulqZrhgZelyEksp4lzXNZc2ob/eSj4n/1d0acAogzfkf8cGtRnpc4MuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4/HaP",
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
  "id": -576460752303422449,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBxpatifjyG9XNgyWRP/WHiWo4o3Za26JhX1gJ1sqHHZ4JOI/Z14bfli4nMUVi+LvkLanm7HFJhNiuG3dMzeEQFuEDuLFCnzWW42XYTD0teGU5LpPe+kPI3CfulqZrhgZelyEksp4lzXNZc2ob/eSj4n/1d0acAogzfkf8cGtRnpc4MuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaEhSqB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422449,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEBxpatifjyG9XNgyWRP/WHiWo4o3Za26JhX1gJ1sqHHZ4JOI/Z14bfli4nMUVi+LvkLanm7HFJhNiuG3dMzeEQFuEDuLFCnzWW42XYTD0teGU5LpPe+kPI3CfulqZrhgZelyEksp4lzXNZc2ob/eSj4n/1d0acAogzfkf8cGtRnpc4MuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaEhSqB"
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEBxpatifjyG9XNgyWRP/WHiWo4o3Za26JhX1gJ1sqHHZ4JOI/Z14bfli4nMUVi+LvkLanm7HFJhNiuG3dMzeEQFuEDuLFCnzWW42XYTD0teGU5LpPe+kPI3CfulqZrhgZelyEksp4lzXNZc2ob/eSj4n/1d0acAogzfkf8cGtRnpc4MuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaEhSqB"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422448,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422448,
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
  "id": -576460752303422447,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422447,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBxpatifjyG9XNgyWRP/WHiWo4o3Za26JhX1gJ1sqHHZ4JOI/Z14bfli4nMUVi+LvkLanm7HFJhNiuG3dMzeEQFuEDuLFCnzWW42XYTD0teGU5LpPe+kPI3CfulqZrhgZelyEksp4lzXNZc2ob/eSj4n/1d0acAogzfkf8cGtRnpc4MuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaEhSqB",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422446,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422446,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBnKzy7qDoZgUwtHrvRKheg8nVMrANgtOPro/tNZvhE+joQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEBxpatifjyG9XNgyWRP/WHiWo4o3Za26JhX1gJ1sqHHZ4JOI/Z14bfli4nMUVi+LvkLanm7HFJhNiuG3dMzeEQFuEDuLFCnzWW42XYTD0teGU5LpPe+kPI3CfulqZrhgZelyEksp4lzXNZc2ob/eSj4n/1d0acAogzfkf8cGtRnpc4MuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhuCRDDYefi2M0QsL",
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
    "signed_tx": "tx_+QFxCwH4QrhAHJBhTV127r9+gQJlIdyOiSotH4ORefeycwOjuBuwA8fsXdRTtih0cPJwN2dr7Fftj289SOdAOHb0A0VoY5VRD7kBKPkBJTsBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAcaWrYn48hvVzYMlkT/1h4lqOKN2WtuiYV9YCdbKhx2eCTiP2deG35YuJzFFYvi75C2p5uxxSYTYrht3TM3hEBbhA7ixQp81luNl2Ew9LXhlOS6T3vpDyNwn7pama4YGXpchJLKeJc1zWXNqG/3ko+J/9XdGnAKIM35H/HBrUZ6XODLhI+EY5AqEGcrPLuoOhmBTC0eu9EqF6DydUysA2C04+uj+01m+ET6MFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIbgkQw2Hn4t4YV2Cw=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422445,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422445,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnKzy7qDoZgUwtHrvRKheg8nVMrANgtOPro/tNZvhE+jBqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCysWfNkg=",
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
  "id": -576460752303422444,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECjJvXoL5GhFAuykhsamssYZfvYeDRZrSVt/RVrqY4LyKjA9P85Ms58LUgGeICZBhDhQclsEr1blveHom+wdaUAuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqXMQuh"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422444,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+JALAfhCuECjJvXoL5GhFAuykhsamssYZfvYeDRZrSVt/RVrqY4LyKjA9P85Ms58LUgGeICZBhDhQclsEr1blveHom+wdaUAuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqXMQuh",
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
  "id": -576460752303422443,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB4gVTC6uX2bL79u6Oqp/hiC6dAau4kj0Ai7mLT2sLZxps1eUeV9musdtBr/W9iZaq5pIkUFZbl4ks0UydXt8sEuECjJvXoL5GhFAuykhsamssYZfvYeDRZrSVt/RVrqY4LyKjA9P85Ms58LUgGeICZBhDhQclsEr1blveHom+wdaUAuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspVbgsq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422443,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEB4gVTC6uX2bL79u6Oqp/hiC6dAau4kj0Ai7mLT2sLZxps1eUeV9musdtBr/W9iZaq5pIkUFZbl4ks0UydXt8sEuECjJvXoL5GhFAuykhsamssYZfvYeDRZrSVt/RVrqY4LyKjA9P85Ms58LUgGeICZBhDhQclsEr1blveHom+wdaUAuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspVbgsq"
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuEB4gVTC6uX2bL79u6Oqp/hiC6dAau4kj0Ai7mLT2sLZxps1eUeV9musdtBr/W9iZaq5pIkUFZbl4ks0UydXt8sEuECjJvXoL5GhFAuykhsamssYZfvYeDRZrSVt/RVrqY4LyKjA9P85Ms58LUgGeICZBhDhQclsEr1blveHom+wdaUAuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspVbgsq"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422442,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422442,
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
  "id": -576460752303422441,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422441,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB4gVTC6uX2bL79u6Oqp/hiC6dAau4kj0Ai7mLT2sLZxps1eUeV9musdtBr/W9iZaq5pIkUFZbl4ks0UydXt8sEuECjJvXoL5GhFAuykhsamssYZfvYeDRZrSVt/RVrqY4LyKjA9P85Ms58LUgGeICZBhDhQclsEr1blveHom+wdaUAuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspVbgsq",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422440,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422440,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnKzy7qDoZgUwtHrvRKheg8nVMrANgtOPro/tNZvhE+jB6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rs07nMw=",
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
  "id": -576460752303422439,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDGa5k0TTormFS/b+zNVjk4IvVvR9TdLJsoqrgGbPVUJdZZGLUrQFEOKDRUg0862ftcNkGTRSaAndae+W5RaTMGuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYjL3nH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422439,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDGa5k0TTormFS/b+zNVjk4IvVvR9TdLJsoqrgGbPVUJdZZGLUrQFEOKDRUg0862ftcNkGTRSaAndae+W5RaTMGuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYjL3nH",
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
  "id": -576460752303422438,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECXuMDEsV2voAkrHyRXClq4zsYHIT0EXF5ZYfp+t1vvYaXA+MteAZDN32n2mpB/rsG/p7IG4ZEtOwO/79Jso/EFuEDGa5k0TTormFS/b+zNVjk4IvVvR9TdLJsoqrgGbPVUJdZZGLUrQFEOKDRUg0862ftcNkGTRSaAndae+W5RaTMGuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZSNeph"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422438,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuECXuMDEsV2voAkrHyRXClq4zsYHIT0EXF5ZYfp+t1vvYaXA+MteAZDN32n2mpB/rsG/p7IG4ZEtOwO/79Jso/EFuEDGa5k0TTormFS/b+zNVjk4IvVvR9TdLJsoqrgGbPVUJdZZGLUrQFEOKDRUg0862ftcNkGTRSaAndae+W5RaTMGuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZSNeph"
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "state": "tx_+NILAfiEuECXuMDEsV2voAkrHyRXClq4zsYHIT0EXF5ZYfp+t1vvYaXA+MteAZDN32n2mpB/rsG/p7IG4ZEtOwO/79Jso/EFuEDGa5k0TTormFS/b+zNVjk4IvVvR9TdLJsoqrgGbPVUJdZZGLUrQFEOKDRUg0862ftcNkGTRSaAndae+W5RaTMGuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZSNeph"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422437,
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
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422437,
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
  "id": -576460752303422436,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422436,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECXuMDEsV2voAkrHyRXClq4zsYHIT0EXF5ZYfp+t1vvYaXA+MteAZDN32n2mpB/rsG/p7IG4ZEtOwO/79Jso/EFuEDGa5k0TTormFS/b+zNVjk4IvVvR9TdLJsoqrgGbPVUJdZZGLUrQFEOKDRUg0862ftcNkGTRSaAndae+W5RaTMGuEj4RjkCoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPowegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZSNeph",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAHJBhTV127r9+gQJlIdyOiSotH4ORefeycwOjuBuwA8fsXdRTtih0cPJwN2dr7Fftj289SOdAOHb0A0VoY5VRD7kBKPkBJTsBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAcaWrYn48hvVzYMlkT/1h4lqOKN2WtuiYV9YCdbKhx2eCTiP2deG35YuJzFFYvi75C2p5uxxSYTYrht3TM3hEBbhA7ixQp81luNl2Ew9LXhlOS6T3vpDyNwn7pama4YGXpchJLKeJc1zWXNqG/3ko+J/9XdGnAKIM35H/HBrUZ6XODLhI+EY5AqEGcrPLuoOhmBTC0eu9EqF6DydUysA2C04+uj+01m+ET6MFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIbgkQw2Hn4t4YV2Cw==",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAHJBhTV127r9+gQJlIdyOiSotH4ORefeycwOjuBuwA8fsXdRTtih0cPJwN2dr7Fftj289SOdAOHb0A0VoY5VRD7kBKPkBJTsBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAcaWrYn48hvVzYMlkT/1h4lqOKN2WtuiYV9YCdbKhx2eCTiP2deG35YuJzFFYvi75C2p5uxxSYTYrht3TM3hEBbhA7ixQp81luNl2Ew9LXhlOS6T3vpDyNwn7pama4YGXpchJLKeJc1zWXNqG/3ko+J/9XdGnAKIM35H/HBrUZ6XODLhI+EY5AqEGcrPLuoOhmBTC0eu9EqF6DydUysA2C04+uj+01m+ET6MFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIbgkQw2Hn4t4YV2Cw==",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "Kě?\u0012\u0004\u0018\\\\ؕ��Y9�[�ؾ�]y����\u0015=\u001a\u0018",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBnKzy7qDoZgUwtHrvRKheg8nVMrANgtOPro/tNZvhE+joQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/+GHLHOiuwBAIYPXtZ/KABx3M4Kow==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422435,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEA23EpJj9ATF4OB7iZ+tkb1mc/ZZSGV7pGrH/Vm3piVOT5EEEizQUwh4bgFhoXYdqfhNLxe6z62zP4WyIv7PX0PuF/4XTUBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAcY2YNIw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422435,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEA23EpJj9ATF4OB7iZ+tkb1mc/ZZSGV7pGrH/Vm3piVOT5EEEizQUwh4bgFhoXYdqfhNLxe6z62zP4WyIv7PX0PuF/4XTUBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAcY2YNIw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422434,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEA23EpJj9ATF4OB7iZ+tkb1mc/ZZSGV7pGrH/Vm3piVOT5EEEizQUwh4bgFhoXYdqfhNLxe6z62zP4WyIv7PX0PuEB17gKL8qanRkPUA8I+d+BXaHx5ie1J5X44mZBE/8bpjGgPIyu1IVdHzPbUPyPSbsWI/pU+7BeD/Ls7P0jSLUAFuF/4XTUBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAcTYeGVU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
  "id": -576460752303422434,
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEA23EpJj9ATF4OB7iZ+tkb1mc/ZZSGV7pGrH/Vm3piVOT5EEEizQUwh4bgFhoXYdqfhNLxe6z62zP4WyIv7PX0PuEB17gKL8qanRkPUA8I+d+BXaHx5ie1J5X44mZBE/8bpjGgPIyu1IVdHzPbUPyPSbsWI/pU+7BeD/Ls7P0jSLUAFuF/4XTUBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAcTYeGVU=",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEA23EpJj9ATF4OB7iZ+tkb1mc/ZZSGV7pGrH/Vm3piVOT5EEEizQUwh4bgFhoXYdqfhNLxe6z62zP4WyIv7PX0PuEB17gKL8qanRkPUA8I+d+BXaHx5ie1J5X44mZBE/8bpjGgPIyu1IVdHzPbUPyPSbsWI/pU+7BeD/Ls7P0jSLUAFuF/4XTUBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAcTYeGVU=",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEA23EpJj9ATF4OB7iZ+tkb1mc/ZZSGV7pGrH/Vm3piVOT5EEEizQUwh4bgFhoXYdqfhNLxe6z62zP4WyIv7PX0PuEB17gKL8qanRkPUA8I+d+BXaHx5ie1J5X44mZBE/8bpjGgPIyu1IVdHzPbUPyPSbsWI/pU+7BeD/Ls7P0jSLUAFuF/4XTUBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAcTYeGVU=",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEA23EpJj9ATF4OB7iZ+tkb1mc/ZZSGV7pGrH/Vm3piVOT5EEEizQUwh4bgFhoXYdqfhNLxe6z62zP4WyIv7PX0PuEB17gKL8qanRkPUA8I+d+BXaHx5ie1J5X44mZBE/8bpjGgPIyu1IVdHzPbUPyPSbsWI/pU+7BeD/Ls7P0jSLUAFuF/4XTUBoQZys8u6g6GYFMLR670SoXoPJ1TKwDYLTj66P7TWb4RPo6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAcTYeGVU=",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
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
    "channel_id": "ch_sWvBp1CxWpp2FFXyDDSvcjDesE43qBxi5cbGWb5nPHGQYWNg8",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection
