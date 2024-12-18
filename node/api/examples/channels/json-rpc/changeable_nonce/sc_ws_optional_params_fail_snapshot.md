
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
      "fsm_id": "ba_/QKIjSrRoB8H3Ooi7IKo/75CTBEpFJ7OD5KRCz409faLd7gG"
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
      "fsm_id": "ba_K++RHWzWoH6M4GWTDiJFfa/mNu6YPB+YyVghG1GqcD7dN1fM"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBobVvk4U=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422247,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBzWdgSqffDdhqGGzETKjGBo8IccXk0HUii3QH3p+16GU0Y5TYbP1WG4I/ynDpwnBi6qWwvaOApOOXRpiF4ewUMuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgaEHe0u9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422247,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_K++RHWzWoH6M4GWTDiJFfa/mNu6YPB+YyVghG1GqcD7dN1fM"
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEBzWdgSqffDdhqGGzETKjGBo8IccXk0HUii3QH3p+16GU0Y5TYbP1WG4I/ynDpwnBi6qWwvaOApOOXRpiF4ewUMuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgaEHe0u9",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422246,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAMRMXMmJY35Uj5HHXdZugB97Paxy9FWV2MupUURe7HBWqvJ0/O7W45DJnhAmjGu/DcWro+eSEeeCe+mzy5ZHnA7hAc1nYEqn3w3YahhsxEyoxgaPCHHF5NB1Iot0B96ftehlNGOU2Gz9VhuCP8pw6cJwYuqlsL2jgKTjl0aYheHsFDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGhDtO1lw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422246,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAMRMXMmJY35Uj5HHXdZugB97Paxy9FWV2MupUURe7HBWqvJ0/O7W45DJnhAmjGu/DcWro+eSEeeCe+mzy5ZHnA7hAc1nYEqn3w3YahhsxEyoxgaPCHHF5NB1Iot0B96ftehlNGOU2Gz9VhuCP8pw6cJwYuqlsL2jgKTjl0aYheHsFDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGhDtO1lw==",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_/QKIjSrRoB8H3Ooi7IKo/75CTBEpFJ7OD5KRCz409faLd7gG"
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAMRMXMmJY35Uj5HHXdZugB97Paxy9FWV2MupUURe7HBWqvJ0/O7W45DJnhAmjGu/DcWro+eSEeeCe+mzy5ZHnA7hAc1nYEqn3w3YahhsxEyoxgaPCHHF5NB1Iot0B96ftehlNGOU2Gz9VhuCP8pw6cJwYuqlsL2jgKTjl0aYheHsFDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGhDtO1lw==",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAMRMXMmJY35Uj5HHXdZugB97Paxy9FWV2MupUURe7HBWqvJ0/O7W45DJnhAmjGu/DcWro+eSEeeCe+mzy5ZHnA7hAc1nYEqn3w3YahhsxEyoxgaPCHHF5NB1Iot0B96ftehlNGOU2Gz9VhuCP8pw6cJwYuqlsL2jgKTjl0aYheHsFDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGhDtO1lw==",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAMRMXMmJY35Uj5HHXdZugB97Paxy9FWV2MupUURe7HBWqvJ0/O7W45DJnhAmjGu/DcWro+eSEeeCe+mzy5ZHnA7hAc1nYEqn3w3YahhsxEyoxgaPCHHF5NB1Iot0B96ftehlNGOU2Gz9VhuCP8pw6cJwYuqlsL2jgKTjl0aYheHsFDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGhDtO1lw==",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "message": {
        "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "message": {
        "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
  "id": -576460752303422245,
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
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422245,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "state": "tx_+QEOCwH4hLhAMRMXMmJY35Uj5HHXdZugB97Paxy9FWV2MupUURe7HBWqvJ0/O7W45DJnhAmjGu/DcWro+eSEeeCe+mzy5ZHnA7hAc1nYEqn3w3YahhsxEyoxgaPCHHF5NB1Iot0B96ftehlNGOU2Gz9VhuCP8pw6cJwYuqlsL2jgKTjl0aYheHsFDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGhDtO1lw=="
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "state": "tx_+QEOCwH4hLhAMRMXMmJY35Uj5HHXdZugB97Paxy9FWV2MupUURe7HBWqvJ0/O7W45DJnhAmjGu/DcWro+eSEeeCe+mzy5ZHnA7hAc1nYEqn3w3YahhsxEyoxgaPCHHF5NB1Iot0B96ftehlNGOU2Gz9VhuCP8pw6cJwYuqlsL2jgKTjl0aYheHsFDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGhDtO1lw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422244,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422244,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEOCwH4hLhAMRMXMmJY35Uj5HHXdZugB97Paxy9FWV2MupUURe7HBWqvJ0/O7W45DJnhAmjGu/DcWro+eSEeeCe+mzy5ZHnA7hAc1nYEqn3w3YahhsxEyoxgaPCHHF5NB1Iot0B96ftehlNGOU2Gz9VhuCP8pw6cJwYuqlsL2jgKTjl0aYheHsFDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGhDtO1lw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422243,
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
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422243,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuvkmdnuxvNoQG05GGXAYB8tSd1Dxwt0oAZ8SJkkep1bAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyvYpP70=",
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
  "id": -576460752303422242,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBCWJh2g+3D3maed5GttpfZwhHJ2IctWNEJRheCAz870jtTwv68nUTESuXFZXsfHXupPRdv981wXNhyBZHaEyIFuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsphn/aS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422242,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBCWJh2g+3D3maed5GttpfZwhHJ2IctWNEJRheCAz870jtTwv68nUTESuXFZXsfHXupPRdv981wXNhyBZHaEyIFuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsphn/aS",
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
  "id": -576460752303422241,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAZDpVd/FjyIM1t7ia0faQkAwcB7VAxFnxXREd9xzdaHT1CWg7DhK8sBgrqCEJQ3msqQ8+pTQtQ8Wm2KAK0LAwPuEBCWJh2g+3D3maed5GttpfZwhHJ2IctWNEJRheCAz870jtTwv68nUTESuXFZXsfHXupPRdv981wXNhyBZHaEyIFuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoCz+ji"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422241,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "state": "tx_+NILAfiEuEAZDpVd/FjyIM1t7ia0faQkAwcB7VAxFnxXREd9xzdaHT1CWg7DhK8sBgrqCEJQ3msqQ8+pTQtQ8Wm2KAK0LAwPuEBCWJh2g+3D3maed5GttpfZwhHJ2IctWNEJRheCAz870jtTwv68nUTESuXFZXsfHXupPRdv981wXNhyBZHaEyIFuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoCz+ji"
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "state": "tx_+NILAfiEuEAZDpVd/FjyIM1t7ia0faQkAwcB7VAxFnxXREd9xzdaHT1CWg7DhK8sBgrqCEJQ3msqQ8+pTQtQ8Wm2KAK0LAwPuEBCWJh2g+3D3maed5GttpfZwhHJ2IctWNEJRheCAz870jtTwv68nUTESuXFZXsfHXupPRdv981wXNhyBZHaEyIFuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoCz+ji"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422240,
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
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422240,
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
  "id": -576460752303422239,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422239,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAZDpVd/FjyIM1t7ia0faQkAwcB7VAxFnxXREd9xzdaHT1CWg7DhK8sBgrqCEJQ3msqQ8+pTQtQ8Wm2KAK0LAwPuEBCWJh2g+3D3maed5GttpfZwhHJ2IctWNEJRheCAz870jtTwv68nUTESuXFZXsfHXupPRdv981wXNhyBZHaEyIFuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoCz+ji",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422238,
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
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422238,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuvkmdnuxvNoQG05GGXAYB8tSd1Dxwt0oAZ8SJkkep1bA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rn25d6s=",
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
  "id": -576460752303422237,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA7cQWytRJWZmxg/OmLJoPxUQvRQajSQR8spv8+LL3nLVfGqU6q1BKGaa04NfbCDPytY7aVq3j+S87uHebfWakPuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBqSRU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422237,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA7cQWytRJWZmxg/OmLJoPxUQvRQajSQR8spv8+LL3nLVfGqU6q1BKGaa04NfbCDPytY7aVq3j+S87uHebfWakPuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBqSRU",
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
  "id": -576460752303422236,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA7cQWytRJWZmxg/OmLJoPxUQvRQajSQR8spv8+LL3nLVfGqU6q1BKGaa04NfbCDPytY7aVq3j+S87uHebfWakPuEBxEACTCXV78tJZMFS2QIpTP5O+zeClMmbewydjGHRL+AtsjF4LpJ/b8JDD5c/VAkfiKtIj81KL8ZOhJZFxf7gAuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYEhSSl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422236,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "state": "tx_+NILAfiEuEA7cQWytRJWZmxg/OmLJoPxUQvRQajSQR8spv8+LL3nLVfGqU6q1BKGaa04NfbCDPytY7aVq3j+S87uHebfWakPuEBxEACTCXV78tJZMFS2QIpTP5O+zeClMmbewydjGHRL+AtsjF4LpJ/b8JDD5c/VAkfiKtIj81KL8ZOhJZFxf7gAuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYEhSSl"
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "state": "tx_+NILAfiEuEA7cQWytRJWZmxg/OmLJoPxUQvRQajSQR8spv8+LL3nLVfGqU6q1BKGaa04NfbCDPytY7aVq3j+S87uHebfWakPuEBxEACTCXV78tJZMFS2QIpTP5O+zeClMmbewydjGHRL+AtsjF4LpJ/b8JDD5c/VAkfiKtIj81KL8ZOhJZFxf7gAuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYEhSSl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422235,
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
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422235,
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
  "id": -576460752303422234,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422234,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA7cQWytRJWZmxg/OmLJoPxUQvRQajSQR8spv8+LL3nLVfGqU6q1BKGaa04NfbCDPytY7aVq3j+S87uHebfWakPuEBxEACTCXV78tJZMFS2QIpTP5O+zeClMmbewydjGHRL+AtsjF4LpJ/b8JDD5c/VAkfiKtIj81KL8ZOhJZFxf7gAuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYEhSSl",
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
  "params": {
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "signed_tx": "tx_+QExCwHAuQEr+QEoOwGhBuvkmdnuxvNoQG05GGXAYB8tSd1Dxwt0oAZ8SJkkep1boQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEA7cQWytRJWZmxg/OmLJoPxUQvRQajSQR8spv8+LL3nLVfGqU6q1BKGaa04NfbCDPytY7aVq3j+S87uHebfWakPuEBxEACTCXV78tJZMFS2QIpTP5O+zeClMmbewydjGHRL+AtsjF4LpJ/b8JDD5c/VAkfiKtIj81KL8ZOhJZFxf7gAuEj4RjkCoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdWwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMUyXKIAIMS1oeZPgAP",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBuvkmdnuxvNoQG05GGXAYB8tSd1Dxwt0oAZ8SJkkep1boQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBotC4rM0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422233,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuECnnJuyatgyblNuPbWXWP4kqDcgD3j76NOOHT9U8JM/1+75bnBgaWz5DDsI4HUdRlC4D5n2pjLVvDtGFS5ZBtQPuGD4XjUBoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdW6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaIAh0Ra"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422233,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "signed_tx": "tx_+KgLAfhCuECnnJuyatgyblNuPbWXWP4kqDcgD3j76NOOHT9U8JM/1+75bnBgaWz5DDsI4HUdRlC4D5n2pjLVvDtGFS5ZBtQPuGD4XjUBoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdW6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaIAh0Ra",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422232,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAEEYeMfyPcx+tbOb74yZ2BflaPcTjeJr30dBICos0wTn5lnAPQWV51web+gUGE6a8z3Q5p0ppT6yylI4oEy6oAuECnnJuyatgyblNuPbWXWP4kqDcgD3j76NOOHT9U8JM/1+75bnBgaWz5DDsI4HUdRlC4D5n2pjLVvDtGFS5ZBtQPuGD4XjUBoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdW6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaJxGC3S"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
  "id": -576460752303422232,
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAEEYeMfyPcx+tbOb74yZ2BflaPcTjeJr30dBICos0wTn5lnAPQWV51web+gUGE6a8z3Q5p0ppT6yylI4oEy6oAuECnnJuyatgyblNuPbWXWP4kqDcgD3j76NOOHT9U8JM/1+75bnBgaWz5DDsI4HUdRlC4D5n2pjLVvDtGFS5ZBtQPuGD4XjUBoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdW6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaJxGC3S",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAEEYeMfyPcx+tbOb74yZ2BflaPcTjeJr30dBICos0wTn5lnAPQWV51web+gUGE6a8z3Q5p0ppT6yylI4oEy6oAuECnnJuyatgyblNuPbWXWP4kqDcgD3j76NOOHT9U8JM/1+75bnBgaWz5DDsI4HUdRlC4D5n2pjLVvDtGFS5ZBtQPuGD4XjUBoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdW6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaJxGC3S",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAEEYeMfyPcx+tbOb74yZ2BflaPcTjeJr30dBICos0wTn5lnAPQWV51web+gUGE6a8z3Q5p0ppT6yylI4oEy6oAuECnnJuyatgyblNuPbWXWP4kqDcgD3j76NOOHT9U8JM/1+75bnBgaWz5DDsI4HUdRlC4D5n2pjLVvDtGFS5ZBtQPuGD4XjUBoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdW6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaJxGC3S",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAEEYeMfyPcx+tbOb74yZ2BflaPcTjeJr30dBICos0wTn5lnAPQWV51web+gUGE6a8z3Q5p0ppT6yylI4oEy6oAuECnnJuyatgyblNuPbWXWP4kqDcgD3j76NOOHT9U8JM/1+75bnBgaWz5DDsI4HUdRlC4D5n2pjLVvDtGFS5ZBtQPuGD4XjUBoQbr5JnZ7sbzaEBtORhlwGAfLUndQ8cLdKAGfEiZJHqdW6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaJxGC3S",
      "type": "channel_close_mutual_tx"
    }
  },
  "version": 1
}
```

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
      "fsm_id": "ba_VBiArVa8ULZtrAwk88RFbMieRf299GzShsob+2nHfIn8eF16"
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
      "fsm_id": "ba_TcFb/0qs1srfs0Jz5yc6gj8sVJJBxfK8U3yJqLdqjYHp3kmj"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBo0tdGpU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422231,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEC84DF79jZP0zK4opkKDKrNqvPeaSiYBdQJL9/6Ty8bEVNA9nkTv+ftoQfB0BN7M+ov9J5rXusFy96mnTF5XOEIuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgaPRxYss"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422231,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_TcFb/0qs1srfs0Jz5yc6gj8sVJJBxfK8U3yJqLdqjYHp3kmj"
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEC84DF79jZP0zK4opkKDKrNqvPeaSiYBdQJL9/6Ty8bEVNA9nkTv+ftoQfB0BN7M+ov9J5rXusFy96mnTF5XOEIuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgaPRxYss",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422230,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAvOAxe/Y2T9MyuKKZCgyqzarz3mkomAXUCS/f+k8vGxFTQPZ5E7/n7aEHwdATezPqL/Sea17rBcvepp0xeVzhCLhA7r+uXxUC5juqzTDryTlY2KmuKbSsIVYx0EkXs+foRxpjUqv6yYvP15Jl24Xed1WERQXUPe7e6u4PRiUQs+ebCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGj/SSMfg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422230,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAvOAxe/Y2T9MyuKKZCgyqzarz3mkomAXUCS/f+k8vGxFTQPZ5E7/n7aEHwdATezPqL/Sea17rBcvepp0xeVzhCLhA7r+uXxUC5juqzTDryTlY2KmuKbSsIVYx0EkXs+foRxpjUqv6yYvP15Jl24Xed1WERQXUPe7e6u4PRiUQs+ebCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGj/SSMfg==",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_VBiArVa8ULZtrAwk88RFbMieRf299GzShsob+2nHfIn8eF16"
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAvOAxe/Y2T9MyuKKZCgyqzarz3mkomAXUCS/f+k8vGxFTQPZ5E7/n7aEHwdATezPqL/Sea17rBcvepp0xeVzhCLhA7r+uXxUC5juqzTDryTlY2KmuKbSsIVYx0EkXs+foRxpjUqv6yYvP15Jl24Xed1WERQXUPe7e6u4PRiUQs+ebCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGj/SSMfg==",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAvOAxe/Y2T9MyuKKZCgyqzarz3mkomAXUCS/f+k8vGxFTQPZ5E7/n7aEHwdATezPqL/Sea17rBcvepp0xeVzhCLhA7r+uXxUC5juqzTDryTlY2KmuKbSsIVYx0EkXs+foRxpjUqv6yYvP15Jl24Xed1WERQXUPe7e6u4PRiUQs+ebCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGj/SSMfg==",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAvOAxe/Y2T9MyuKKZCgyqzarz3mkomAXUCS/f+k8vGxFTQPZ5E7/n7aEHwdATezPqL/Sea17rBcvepp0xeVzhCLhA7r+uXxUC5juqzTDryTlY2KmuKbSsIVYx0EkXs+foRxpjUqv6yYvP15Jl24Xed1WERQXUPe7e6u4PRiUQs+ebCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGj/SSMfg==",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "event": "closed_confirmed"
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
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
    "channel_id": "ch_2nta2QRNpExGmsf8MEBn5dsRaGH8oz4m5AB2c5WHHUFZHhA1cb",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "message": {
        "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "message": {
        "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
  "id": -576460752303422229,
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
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422229,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "state": "tx_+QEOCwH4hLhAvOAxe/Y2T9MyuKKZCgyqzarz3mkomAXUCS/f+k8vGxFTQPZ5E7/n7aEHwdATezPqL/Sea17rBcvepp0xeVzhCLhA7r+uXxUC5juqzTDryTlY2KmuKbSsIVYx0EkXs+foRxpjUqv6yYvP15Jl24Xed1WERQXUPe7e6u4PRiUQs+ebCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGj/SSMfg=="
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "state": "tx_+QEOCwH4hLhAvOAxe/Y2T9MyuKKZCgyqzarz3mkomAXUCS/f+k8vGxFTQPZ5E7/n7aEHwdATezPqL/Sea17rBcvepp0xeVzhCLhA7r+uXxUC5juqzTDryTlY2KmuKbSsIVYx0EkXs+foRxpjUqv6yYvP15Jl24Xed1WERQXUPe7e6u4PRiUQs+ebCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGj/SSMfg=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422228,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422228,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEOCwH4hLhAvOAxe/Y2T9MyuKKZCgyqzarz3mkomAXUCS/f+k8vGxFTQPZ5E7/n7aEHwdATezPqL/Sea17rBcvepp0xeVzhCLhA7r+uXxUC5juqzTDryTlY2KmuKbSsIVYx0EkXs+foRxpjUqv6yYvP15Jl24Xed1WERQXUPe7e6u4PRiUQs+ebCLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGj/SSMfg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422227,
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
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422227,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhztHhEWTDCsS82rn+UGkwyCu+Sfzb4hswwNd4oIV9xtAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyqJV3aM=",
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
  "id": -576460752303422226,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECoeKTJVym8hFTrnaqk8ZM7HyIqwo6U3IS8SBeU5C+BDWLYEri991DI1QW2QVmt/QjSfADHs0AizTYc0xO6UHwGuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspmP8Gc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422226,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "signed_tx": "tx_+JALAfhCuECoeKTJVym8hFTrnaqk8ZM7HyIqwo6U3IS8SBeU5C+BDWLYEri991DI1QW2QVmt/QjSfADHs0AizTYc0xO6UHwGuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspmP8Gc",
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
  "id": -576460752303422225,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA9uOOlCxcOh1um9ra2rPLRrJxSIix7vXtLxqY05JLnJRv8LBZCuucS+K7zGEHnVegalQdCrUhP5pNXuvllhWQGuECoeKTJVym8hFTrnaqk8ZM7HyIqwo6U3IS8SBeU5C+BDWLYEri991DI1QW2QVmt/QjSfADHs0AizTYc0xO6UHwGuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrklrhr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422225,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "state": "tx_+NILAfiEuEA9uOOlCxcOh1um9ra2rPLRrJxSIix7vXtLxqY05JLnJRv8LBZCuucS+K7zGEHnVegalQdCrUhP5pNXuvllhWQGuECoeKTJVym8hFTrnaqk8ZM7HyIqwo6U3IS8SBeU5C+BDWLYEri991DI1QW2QVmt/QjSfADHs0AizTYc0xO6UHwGuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrklrhr"
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "state": "tx_+NILAfiEuEA9uOOlCxcOh1um9ra2rPLRrJxSIix7vXtLxqY05JLnJRv8LBZCuucS+K7zGEHnVegalQdCrUhP5pNXuvllhWQGuECoeKTJVym8hFTrnaqk8ZM7HyIqwo6U3IS8SBeU5C+BDWLYEri991DI1QW2QVmt/QjSfADHs0AizTYc0xO6UHwGuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrklrhr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422224,
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
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422224,
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
  "id": -576460752303422223,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422223,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA9uOOlCxcOh1um9ra2rPLRrJxSIix7vXtLxqY05JLnJRv8LBZCuucS+K7zGEHnVegalQdCrUhP5pNXuvllhWQGuECoeKTJVym8hFTrnaqk8ZM7HyIqwo6U3IS8SBeU5C+BDWLYEri991DI1QW2QVmt/QjSfADHs0AizTYc0xO6UHwGuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrklrhr",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422222,
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
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422222,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhztHhEWTDCsS82rn+UGkwyCu+Sfzb4hswwNd4oIV9xtA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgO/WfY=",
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
  "id": -576460752303422221,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECKhOi35ewUdWvmYTd27Vp61OPxzwgApIqb1X97A8JnKLEssBwDrx/CZdMj3rchyfsrhNie/r+FbtyvATg9H/0AuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEadZKcz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422221,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "signed_tx": "tx_+JALAfhCuECKhOi35ewUdWvmYTd27Vp61OPxzwgApIqb1X97A8JnKLEssBwDrx/CZdMj3rchyfsrhNie/r+FbtyvATg9H/0AuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEadZKcz",
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
  "id": -576460752303422220,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBUam0Sh5uCtlGarbkMgDevcg06yajWf75PT7RC/fqsKKhuPtl2eZprc+36frLAgqUj+FfBZE1tDyFR57ScETYMuECKhOi35ewUdWvmYTd27Vp61OPxzwgApIqb1X97A8JnKLEssBwDrx/CZdMj3rchyfsrhNie/r+FbtyvATg9H/0AuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEax4PHs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422220,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "state": "tx_+NILAfiEuEBUam0Sh5uCtlGarbkMgDevcg06yajWf75PT7RC/fqsKKhuPtl2eZprc+36frLAgqUj+FfBZE1tDyFR57ScETYMuECKhOi35ewUdWvmYTd27Vp61OPxzwgApIqb1X97A8JnKLEssBwDrx/CZdMj3rchyfsrhNie/r+FbtyvATg9H/0AuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEax4PHs"
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "state": "tx_+NILAfiEuEBUam0Sh5uCtlGarbkMgDevcg06yajWf75PT7RC/fqsKKhuPtl2eZprc+36frLAgqUj+FfBZE1tDyFR57ScETYMuECKhOi35ewUdWvmYTd27Vp61OPxzwgApIqb1X97A8JnKLEssBwDrx/CZdMj3rchyfsrhNie/r+FbtyvATg9H/0AuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEax4PHs"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422219,
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
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422219,
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
  "id": -576460752303422218,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422218,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBUam0Sh5uCtlGarbkMgDevcg06yajWf75PT7RC/fqsKKhuPtl2eZprc+36frLAgqUj+FfBZE1tDyFR57ScETYMuECKhOi35ewUdWvmYTd27Vp61OPxzwgApIqb1X97A8JnKLEssBwDrx/CZdMj3rchyfsrhNie/r+FbtyvATg9H/0AuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEax4PHs",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "signed_tx": "tx_+QExCwHAuQEr+QEoOwGhBhztHhEWTDCsS82rn+UGkwyCu+Sfzb4hswwNd4oIV9xtoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEBUam0Sh5uCtlGarbkMgDevcg06yajWf75PT7RC/fqsKKhuPtl2eZprc+36frLAgqUj+FfBZE1tDyFR57ScETYMuECKhOi35ewUdWvmYTd27Vp61OPxzwgApIqb1X97A8JnKLEssBwDrx/CZdMj3rchyfsrhNie/r+FbtyvATg9H/0AuEj4RjkCoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbQOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMUyXKIAIMS1ocMn1pW",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBhztHhEWTDCsS82rn+UGkwyCu+Sfzb4hswwNd4oIV9xtoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW5/+GHK96fwgBAIYPY36W8ACBpEf76XQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422217,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuECgcaw7ZK8OjusSv+OS7kX7sGnopa6BOsSAJCnXTkuxbRjxl4YN2d+t7g0vPRUyIfTneP26GJZhy6z43kLxv68FuGD4XjUBoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaQmkJmS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422217,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "signed_tx": "tx_+KgLAfhCuECgcaw7ZK8OjusSv+OS7kX7sGnopa6BOsSAJCnXTkuxbRjxl4YN2d+t7g0vPRUyIfTneP26GJZhy6z43kLxv68FuGD4XjUBoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaQmkJmS",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422216,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEApKFuvqEEv2vdcULoKhbao6U8fHu+XpaEyfUWjAWUGbCMyj4XM4RHh7VZGIYYnkTlol6z/lTo0LThEX+gMWaAJuECgcaw7ZK8OjusSv+OS7kX7sGnopa6BOsSAJCnXTkuxbRjxl4YN2d+t7g0vPRUyIfTneP26GJZhy6z43kLxv68FuGD4XjUBoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaSAxK6u"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
  "id": -576460752303422216,
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEApKFuvqEEv2vdcULoKhbao6U8fHu+XpaEyfUWjAWUGbCMyj4XM4RHh7VZGIYYnkTlol6z/lTo0LThEX+gMWaAJuECgcaw7ZK8OjusSv+OS7kX7sGnopa6BOsSAJCnXTkuxbRjxl4YN2d+t7g0vPRUyIfTneP26GJZhy6z43kLxv68FuGD4XjUBoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaSAxK6u",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEApKFuvqEEv2vdcULoKhbao6U8fHu+XpaEyfUWjAWUGbCMyj4XM4RHh7VZGIYYnkTlol6z/lTo0LThEX+gMWaAJuECgcaw7ZK8OjusSv+OS7kX7sGnopa6BOsSAJCnXTkuxbRjxl4YN2d+t7g0vPRUyIfTneP26GJZhy6z43kLxv68FuGD4XjUBoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaSAxK6u",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEApKFuvqEEv2vdcULoKhbao6U8fHu+XpaEyfUWjAWUGbCMyj4XM4RHh7VZGIYYnkTlol6z/lTo0LThEX+gMWaAJuECgcaw7ZK8OjusSv+OS7kX7sGnopa6BOsSAJCnXTkuxbRjxl4YN2d+t7g0vPRUyIfTneP26GJZhy6z43kLxv68FuGD4XjUBoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaSAxK6u",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEApKFuvqEEv2vdcULoKhbao6U8fHu+XpaEyfUWjAWUGbCMyj4XM4RHh7VZGIYYnkTlol6z/lTo0LThEX+gMWaAJuECgcaw7ZK8OjusSv+OS7kX7sGnopa6BOsSAJCnXTkuxbRjxl4YN2d+t7g0vPRUyIfTneP26GJZhy6z43kLxv68FuGD4XjUBoQYc7R4RFkwwrEvNq5/lBpMMgrvkn82+IbMMDXeKCFfcbaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1uf/hhyven8IAQCGD2N+lvAAgaSAxK6u",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
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
    "channel_id": "ch_Djt9ybBGbr5s7YmjCj6FEoejAnnMRdLroYxZgMu4QRbM3c7vU",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
