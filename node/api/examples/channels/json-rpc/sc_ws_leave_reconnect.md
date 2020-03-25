
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reconnect%2F3760
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
      "fsm_id": "ba_kkRuI7xsYO0sSfY2KMMKJ+OvCgu2qHevyu5QGAEHlos4hR2I"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=true&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reconnect%2F3760
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
      "fsm_id": "ba_GSrVbNpIvSv4a5blrCbC60j2zg3sFTzAMYy8h/Q55X9II6//"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYYYplJ/g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423187,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAwISw0Chxop/ZggUt8QLvcNvPkYzfwNuR8EROQ1Lh1a07g8m9+QF4rb29WRqheINtMzQq1J6Tfp5ohiBb4XYYLuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGGLhFx4Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423187,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_GSrVbNpIvSv4a5blrCbC60j2zg3sFTzAMYy8h/Q55X9II6//"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAwISw0Chxop/ZggUt8QLvcNvPkYzfwNuR8EROQ1Lh1a07g8m9+QF4rb29WRqheINtMzQq1J6Tfp5ohiBb4XYYLuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGGLhFx4Q=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423186,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423186,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_kkRuI7xsYO0sSfY2KMMKJ+OvCgu2qHevyu5QGAEHlos4hR2I"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "message": {
        "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "message": {
        "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "id": -576460752303423185,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423185,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "event": "peer_disconnected"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW%2BF2GC7hAP%2B6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh%2FNB7iD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhjRaTNd&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW%2BF2GC7hAP%2B6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh%2FNB7iD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhjRaTNd&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW&existing_fsm_id=ba_WOenMHaoJdYNkWpK&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW%2BF2GC7hAP%2B6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh%2FNB7iD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhjRaTNd&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW&existing_fsm_id=ba_YH2otQsHrE8RG%2Bpzgwf3QTwcyNGQNARa9XtNcQRtGu9yEwbw&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW%2BF2GC7hAP%2B6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh%2FNB7iD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhjRaTNd&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW&existing_fsm_id=ba_kkRuI7xsYO0sSfY2KMMKJ%2BOvCgu2qHevyu5QGAEHlos4hR2I&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW%2BF2GC7hAP%2B6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh%2FNB7iD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhjRaTNd&port=13179&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_EtZb9+AeZmAHfZXzwCbvPmuFzPX0PaddEj+fnUFAhLStV1Dx"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+QENCwH4hLhAMCEsNAocaKf2YIFLfEC73Dbz5GM38DbkfBETkNS4dWtO4PJvfkBeK29vVkaoXiDbTM0KtSek36eaIYgW+F2GC7hAP+6CjgpRWQT6ZITjuM7v8YnFMLwO3Ao3Zbe8aLQrbKOrCxsy2ntxGw9mD4WotWkxdcrdY3Duzpb56Ulxeh/NB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhjRaTNd"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423184,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423184,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBq+LeKh3BIFsQpVkvEOq1ivp1OmRi+PGEnKxUWjjr5PHAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCymXTJ8A=",
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
  "id": -576460752303423183,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECD5v9zkv2EycZNOsqr393M5CTaXduQMQ5wbgme775thLdnbsVF93Zywcuwd9tBcfw6ddggzY9hOH+tPZA3A4oIuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqAVrWL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423183,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+JALAfhCuECD5v9zkv2EycZNOsqr393M5CTaXduQMQ5wbgme775thLdnbsVF93Zywcuwd9tBcfw6ddggzY9hOH+tPZA3A4oIuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqAVrWL",
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
  "id": -576460752303423182,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECD5v9zkv2EycZNOsqr393M5CTaXduQMQ5wbgme775thLdnbsVF93Zywcuwd9tBcfw6ddggzY9hOH+tPZA3A4oIuEDGzFaq/IwX/WxtccMMovV5+adwyl6i9Toa0mnwmGxkO7+1ZOR5365oMklTWxEci2LgEmQUNwHG771JadFsdhkEuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq62seQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423182,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuECD5v9zkv2EycZNOsqr393M5CTaXduQMQ5wbgme775thLdnbsVF93Zywcuwd9tBcfw6ddggzY9hOH+tPZA3A4oIuEDGzFaq/IwX/WxtccMMovV5+adwyl6i9Toa0mnwmGxkO7+1ZOR5365oMklTWxEci2LgEmQUNwHG771JadFsdhkEuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq62seQ"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuECD5v9zkv2EycZNOsqr393M5CTaXduQMQ5wbgme775thLdnbsVF93Zywcuwd9tBcfw6ddggzY9hOH+tPZA3A4oIuEDGzFaq/IwX/WxtccMMovV5+adwyl6i9Toa0mnwmGxkO7+1ZOR5365oMklTWxEci2LgEmQUNwHG771JadFsdhkEuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq62seQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423181,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423181,
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
  "id": -576460752303423180,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423180,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECD5v9zkv2EycZNOsqr393M5CTaXduQMQ5wbgme775thLdnbsVF93Zywcuwd9tBcfw6ddggzY9hOH+tPZA3A4oIuEDGzFaq/IwX/WxtccMMovV5+adwyl6i9Toa0mnwmGxkO7+1ZOR5365oMklTWxEci2LgEmQUNwHG771JadFsdhkEuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq62seQ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423179,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423179,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBq+LeKh3BIFsQpVkvEOq1ivp1OmRi+PGEnKxUWjjr5PHA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RqqBuUM=",
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
  "id": -576460752303423178,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAaVzMCIT7bz5CPctaN8mU8bGBRCLZN0rjizGzm0Mr+rHeF88YBGBjcZjDUslrKTJGnZsfLSofycHRNwun8zLsPuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZHyiZn"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423178,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAaVzMCIT7bz5CPctaN8mU8bGBRCLZN0rjizGzm0Mr+rHeF88YBGBjcZjDUslrKTJGnZsfLSofycHRNwun8zLsPuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZHyiZn",
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
  "id": -576460752303423177,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAaVzMCIT7bz5CPctaN8mU8bGBRCLZN0rjizGzm0Mr+rHeF88YBGBjcZjDUslrKTJGnZsfLSofycHRNwun8zLsPuEDvEbYoFCJ2Gb7oPKVgnuLrnSdlp3mAu6sXVy5+x7Zmr8OypgXVhFRfbTsTHrbd4vr/UJcHUbA6S+caGsb+rQgMuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZTusjh"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423177,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuEAaVzMCIT7bz5CPctaN8mU8bGBRCLZN0rjizGzm0Mr+rHeF88YBGBjcZjDUslrKTJGnZsfLSofycHRNwun8zLsPuEDvEbYoFCJ2Gb7oPKVgnuLrnSdlp3mAu6sXVy5+x7Zmr8OypgXVhFRfbTsTHrbd4vr/UJcHUbA6S+caGsb+rQgMuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZTusjh"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuEAaVzMCIT7bz5CPctaN8mU8bGBRCLZN0rjizGzm0Mr+rHeF88YBGBjcZjDUslrKTJGnZsfLSofycHRNwun8zLsPuEDvEbYoFCJ2Gb7oPKVgnuLrnSdlp3mAu6sXVy5+x7Zmr8OypgXVhFRfbTsTHrbd4vr/UJcHUbA6S+caGsb+rQgMuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZTusjh"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423176,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423176,
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
  "id": -576460752303423175,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423175,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAaVzMCIT7bz5CPctaN8mU8bGBRCLZN0rjizGzm0Mr+rHeF88YBGBjcZjDUslrKTJGnZsfLSofycHRNwun8zLsPuEDvEbYoFCJ2Gb7oPKVgnuLrnSdlp3mAu6sXVy5+x7Zmr8OypgXVhFRfbTsTHrbd4vr/UJcHUbA6S+caGsb+rQgMuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZTusjh",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423174,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423174,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBq+LeKh3BIFsQpVkvEOq1ivp1OmRi+PGEnKxUWjjr5PHBKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYJAwk9A=",
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
  "id": -576460752303423173,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDG0nHj5CcLSjFAXVFV2xA0EjM5YJMDgeD6nDE6yCG5wYFbGBEf0Q11dTj/dk++BivJtTutiPhcmAb65BK6oVAPuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBkxEjE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423173,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDG0nHj5CcLSjFAXVFV2xA0EjM5YJMDgeD6nDE6yCG5wYFbGBEf0Q11dTj/dk++BivJtTutiPhcmAb65BK6oVAPuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBkxEjE",
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
  "id": -576460752303423172,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBiJiTEDx3KDK0jmUyRgmmM+2/BqHmU04QJky/Rs0Um4kOoT4f4sqe9djjP0HGHvDbqFa7xy8tOclJjy67lp+YFuEDG0nHj5CcLSjFAXVFV2xA0EjM5YJMDgeD6nDE6yCG5wYFbGBEf0Q11dTj/dk++BivJtTutiPhcmAb65BK6oVAPuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDt19D2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423172,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuEBiJiTEDx3KDK0jmUyRgmmM+2/BqHmU04QJky/Rs0Um4kOoT4f4sqe9djjP0HGHvDbqFa7xy8tOclJjy67lp+YFuEDG0nHj5CcLSjFAXVFV2xA0EjM5YJMDgeD6nDE6yCG5wYFbGBEf0Q11dTj/dk++BivJtTutiPhcmAb65BK6oVAPuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDt19D2"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuEBiJiTEDx3KDK0jmUyRgmmM+2/BqHmU04QJky/Rs0Um4kOoT4f4sqe9djjP0HGHvDbqFa7xy8tOclJjy67lp+YFuEDG0nHj5CcLSjFAXVFV2xA0EjM5YJMDgeD6nDE6yCG5wYFbGBEf0Q11dTj/dk++BivJtTutiPhcmAb65BK6oVAPuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDt19D2"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423171,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423171,
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
  "id": -576460752303423170,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423170,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBiJiTEDx3KDK0jmUyRgmmM+2/BqHmU04QJky/Rs0Um4kOoT4f4sqe9djjP0HGHvDbqFa7xy8tOclJjy67lp+YFuEDG0nHj5CcLSjFAXVFV2xA0EjM5YJMDgeD6nDE6yCG5wYFbGBEf0Q11dTj/dk++BivJtTutiPhcmAb65BK6oVAPuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDt19D2",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423169,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423169,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBq+LeKh3BIFsQpVkvEOq1ivp1OmRi+PGEnKxUWjjr5PHBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkWqNFU=",
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
  "id": -576460752303423168,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBgwuBizrMi9iE2hZ8tCjij+1EYOf3NRxr0Yl55HhZmiP30uhlQkvr36nx2bbIZcBxLDyfDAekOaHq1sNEJlMEFuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYv+MNM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423168,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBgwuBizrMi9iE2hZ8tCjij+1EYOf3NRxr0Yl55HhZmiP30uhlQkvr36nx2bbIZcBxLDyfDAekOaHq1sNEJlMEFuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYv+MNM",
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
  "id": -576460752303423167,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA51gMfUx2jrEjNZZNe6esAnm6DCSXkPYEYA4knRFq1IBhwvrS32PhOpFJ9Mn1yV3cpreO+jatbJeNH7wtzDdMHuEBgwuBizrMi9iE2hZ8tCjij+1EYOf3NRxr0Yl55HhZmiP30uhlQkvr36nx2bbIZcBxLDyfDAekOaHq1sNEJlMEFuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbseB2y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423167,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuEA51gMfUx2jrEjNZZNe6esAnm6DCSXkPYEYA4knRFq1IBhwvrS32PhOpFJ9Mn1yV3cpreO+jatbJeNH7wtzDdMHuEBgwuBizrMi9iE2hZ8tCjij+1EYOf3NRxr0Yl55HhZmiP30uhlQkvr36nx2bbIZcBxLDyfDAekOaHq1sNEJlMEFuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbseB2y"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuEA51gMfUx2jrEjNZZNe6esAnm6DCSXkPYEYA4knRFq1IBhwvrS32PhOpFJ9Mn1yV3cpreO+jatbJeNH7wtzDdMHuEBgwuBizrMi9iE2hZ8tCjij+1EYOf3NRxr0Yl55HhZmiP30uhlQkvr36nx2bbIZcBxLDyfDAekOaHq1sNEJlMEFuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbseB2y"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423166,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423166,
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
  "id": -576460752303423165,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423165,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA51gMfUx2jrEjNZZNe6esAnm6DCSXkPYEYA4knRFq1IBhwvrS32PhOpFJ9Mn1yV3cpreO+jatbJeNH7wtzDdMHuEBgwuBizrMi9iE2hZ8tCjij+1EYOf3NRxr0Yl55HhZmiP30uhlQkvr36nx2bbIZcBxLDyfDAekOaHq1sNEJlMEFuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+TxwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbseB2y",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423164,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423164,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBq+LeKh3BIFsQpVkvEOq1ivp1OmRi+PGEnKxUWjjr5PHBqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYEY7nss=",
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
  "id": -576460752303423163,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDErz6h45+5qVhttPbHMDEs6v/doeaicdYWxYr7cd4KJlMVmRvCXFwQxozvjeDSOU4qCxI06rAa8VVptlrOh0QHuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+Txwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBZjEkQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423163,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDErz6h45+5qVhttPbHMDEs6v/doeaicdYWxYr7cd4KJlMVmRvCXFwQxozvjeDSOU4qCxI06rAa8VVptlrOh0QHuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+Txwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBZjEkQ",
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
  "id": -576460752303423162,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDErz6h45+5qVhttPbHMDEs6v/doeaicdYWxYr7cd4KJlMVmRvCXFwQxozvjeDSOU4qCxI06rAa8VVptlrOh0QHuED50tR0N21RXCQBBzRRE1a+4HG6eMA2Lxac0Ygi0Jo3A3NjkU1Lcm+rVvTE1HGINfpX/Z/3zFMRKxidXhZYEjsGuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+Txwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAeuA6L"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423162,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuEDErz6h45+5qVhttPbHMDEs6v/doeaicdYWxYr7cd4KJlMVmRvCXFwQxozvjeDSOU4qCxI06rAa8VVptlrOh0QHuED50tR0N21RXCQBBzRRE1a+4HG6eMA2Lxac0Ygi0Jo3A3NjkU1Lcm+rVvTE1HGINfpX/Z/3zFMRKxidXhZYEjsGuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+Txwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAeuA6L"
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
    "data": {
      "state": "tx_+NILAfiEuEDErz6h45+5qVhttPbHMDEs6v/doeaicdYWxYr7cd4KJlMVmRvCXFwQxozvjeDSOU4qCxI06rAa8VVptlrOh0QHuED50tR0N21RXCQBBzRRE1a+4HG6eMA2Lxac0Ygi0Jo3A3NjkU1Lcm+rVvTE1HGINfpX/Z/3zFMRKxidXhZYEjsGuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+Txwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAeuA6L"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423161,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423161,
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
  "id": -576460752303423160,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423160,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDErz6h45+5qVhttPbHMDEs6v/doeaicdYWxYr7cd4KJlMVmRvCXFwQxozvjeDSOU4qCxI06rAa8VVptlrOh0QHuED50tR0N21RXCQBBzRRE1a+4HG6eMA2Lxac0Ygi0Jo3A3NjkU1Lcm+rVvTE1HGINfpX/Z/3zFMRKxidXhZYEjsGuEj4RjkCoQavi3iodwSBbEKVZLxDqtYr6dTpkYvjxhJysVFo46+Txwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAeuA6L",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423159,
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423159,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423158,
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
    "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
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
  "channel_id": "ch_2LK4HGpZQqqNWmP2oHL73GYhbbwRzZCYp5uybNW2L3bdpwiNEW",
  "id": -576460752303423158,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
