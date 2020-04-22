
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
      "fsm_id": "ba_ZG0hvKdgSOCMyu/1pVJaOCyUYc260bVVPLZg5Qzy/rcuM9pd"
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
      "fsm_id": "ba_knxLP5sD1jjfseqxzLqAsWtp92AT5gkS9gSDbid85mSnQOws"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBuCCkgAs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422113,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAE59cKL9B6lHmxcS6E00dKJA/qg7REidIm/XY3OsXsjAA3KHZB08fI23wCWllSyvM9VNKXI65jze7XyrIverAJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbiwmXXE"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422113,
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_knxLP5sD1jjfseqxzLqAsWtp92AT5gkS9gSDbid85mSnQOws"
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEAE59cKL9B6lHmxcS6E00dKJA/qg7REidIm/XY3OsXsjAA3KHZB08fI23wCWllSyvM9VNKXI65jze7XyrIverAJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbiwmXXE",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422112,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhABOfXCi/QepR5sXEuhNNHSiQP6oO0RInSJv12NzrF7IwANyh2QdPHyNt8AlpZUsrzPVTSlyOuY83u18qyL3qwCbhA/FFqf68sEjFzTvlbxu94EC9OmG74YyisuMfDwwRZ7EYiAegHX1R60BlXg2sK6PQL91yIdec+OokcdczjdR8FDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG4xpnJug=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
  "id": -576460752303422112,
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhABOfXCi/QepR5sXEuhNNHSiQP6oO0RInSJv12NzrF7IwANyh2QdPHyNt8AlpZUsrzPVTSlyOuY83u18qyL3qwCbhA/FFqf68sEjFzTvlbxu94EC9OmG74YyisuMfDwwRZ7EYiAegHX1R60BlXg2sK6PQL91yIdec+OokcdczjdR8FDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG4xpnJug==",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_ZG0hvKdgSOCMyu/1pVJaOCyUYc260bVVPLZg5Qzy/rcuM9pd"
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhABOfXCi/QepR5sXEuhNNHSiQP6oO0RInSJv12NzrF7IwANyh2QdPHyNt8AlpZUsrzPVTSlyOuY83u18qyL3qwCbhA/FFqf68sEjFzTvlbxu94EC9OmG74YyisuMfDwwRZ7EYiAegHX1R60BlXg2sK6PQL91yIdec+OokcdczjdR8FDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG4xpnJug==",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhABOfXCi/QepR5sXEuhNNHSiQP6oO0RInSJv12NzrF7IwANyh2QdPHyNt8AlpZUsrzPVTSlyOuY83u18qyL3qwCbhA/FFqf68sEjFzTvlbxu94EC9OmG74YyisuMfDwwRZ7EYiAegHX1R60BlXg2sK6PQL91yIdec+OokcdczjdR8FDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG4xpnJug==",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhABOfXCi/QepR5sXEuhNNHSiQP6oO0RInSJv12NzrF7IwANyh2QdPHyNt8AlpZUsrzPVTSlyOuY83u18qyL3qwCbhA/FFqf68sEjFzTvlbxu94EC9OmG74YyisuMfDwwRZ7EYiAegHX1R60BlXg2sK6PQL91yIdec+OokcdczjdR8FDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG4xpnJug==",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "message": {
        "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "message": {
        "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
  "id": -576460752303422111,
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
  "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
  "id": -576460752303422111,
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "state": "tx_+QEOCwH4hLhABOfXCi/QepR5sXEuhNNHSiQP6oO0RInSJv12NzrF7IwANyh2QdPHyNt8AlpZUsrzPVTSlyOuY83u18qyL3qwCbhA/FFqf68sEjFzTvlbxu94EC9OmG74YyisuMfDwwRZ7EYiAegHX1R60BlXg2sK6PQL91yIdec+OokcdczjdR8FDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG4xpnJug=="
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "state": "tx_+QEOCwH4hLhABOfXCi/QepR5sXEuhNNHSiQP6oO0RInSJv12NzrF7IwANyh2QdPHyNt8AlpZUsrzPVTSlyOuY83u18qyL3qwCbhA/FFqf68sEjFzTvlbxu94EC9OmG74YyisuMfDwwRZ7EYiAegHX1R60BlXg2sK6PQL91yIdec+OokcdczjdR8FDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG4xpnJug=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBsA8HlBquksC5dSLLA5ZbVk6Hu8H/FhxYBTO6bqXpcVQoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/FSIpYAKAPDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgKBuVCbl2Y=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainDeposit"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBsA8HlBquksC5dSLLA5ZbVk6Hu8H/FhxYBTO6bqXpcVQoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/AoHKQAKBy7d2KOPanIgoeBduOtHrSep+GXgzluZAMk579K2VI8wJBovsT+w==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainDeposit"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBsA8HlBquksC5dSLLA5ZbVk6Hu8H/FhxYBTO6bqXpcVQoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/FSIpYAKAPDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgKBuVCbl2Y=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainDeposit"
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
  "id": -576460752303422110,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEB/C2p970z6X1/gVgQlGsCon3T2ndn8BV35ElxmxVNEDLbvouvCCYOjDX4esnv8UC3aV5SiH+H13C8Wm4TL5cQFuHX4czMBoQbAPB5QarpLAuXUiywOWW1ZOh7vB/xYcWAUzum6l6XFUKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUiKWACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgblDI/4N"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
  "id": -576460752303422110,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
      "method": "channels.deposit_tx",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "signed_tx": "tx_+L0LAfhCuEB/C2p970z6X1/gVgQlGsCon3T2ndn8BV35ElxmxVNEDLbvouvCCYOjDX4esnv8UC3aV5SiH+H13C8Wm4TL5cQFuHX4czMBoQbAPB5QarpLAuXUiywOWW1ZOh7vB/xYcWAUzum6l6XFUKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUiKWACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgblDI/4N",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainDeposit"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
    "data": {
      "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
  "id": -576460752303422109,
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
  "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
  "id": -576460752303422109,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422108,
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
    "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
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
  "channel_id": "ch_2TfP6QrnYEk7f3hRSnDfxHhGRmdH1AvTnxdwM15EYuWpyqryc2",
  "id": -576460752303422108,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
