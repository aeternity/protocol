
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
      "fsm_id": "ba_QoqasfOVRVjrpQnB9aqdWi58KVYWuGliUgDZBclSDoJAz2Ke"
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
      "fsm_id": "ba_n8Cv2j2xPCP5CtnMGRGMItdmPXJWqPz+Ab9bWgjFy3TRUMHw"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBgabKmTg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422398,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECh+KTU0DL6OOIf36BNQAy5CXP3jFs3qEDc2Q1fSoGm0QNWMmecbozRZlAdDP9qtRZQJ8MZDkTbcxkFUHVuJp8NuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYGffuoy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422398,
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_n8Cv2j2xPCP5CtnMGRGMItdmPXJWqPz+Ab9bWgjFy3TRUMHw"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECh+KTU0DL6OOIf36BNQAy5CXP3jFs3qEDc2Q1fSoGm0QNWMmecbozRZlAdDP9qtRZQJ8MZDkTbcxkFUHVuJp8NuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgYGffuoy",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422397,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAnLPigr+A+YlncVdEAx/hDnuy0dS63NjAll5AE4q7r1zyHakzOOOQN47v7eR1k7fnA5Wd1caaeauFLUURk04yBbhAofik1NAy+jjiH9+gTUAMuQlz94xbN6hA3NkNX0qBptEDVjJnnG6M0WZQHQz/arUWUCfDGQ5E23MZBVB1biafDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGBkuqeaQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
  "id": -576460752303422397,
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAnLPigr+A+YlncVdEAx/hDnuy0dS63NjAll5AE4q7r1zyHakzOOOQN47v7eR1k7fnA5Wd1caaeauFLUURk04yBbhAofik1NAy+jjiH9+gTUAMuQlz94xbN6hA3NkNX0qBptEDVjJnnG6M0WZQHQz/arUWUCfDGQ5E23MZBVB1biafDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGBkuqeaQ==",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_QoqasfOVRVjrpQnB9aqdWi58KVYWuGliUgDZBclSDoJAz2Ke"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAnLPigr+A+YlncVdEAx/hDnuy0dS63NjAll5AE4q7r1zyHakzOOOQN47v7eR1k7fnA5Wd1caaeauFLUURk04yBbhAofik1NAy+jjiH9+gTUAMuQlz94xbN6hA3NkNX0qBptEDVjJnnG6M0WZQHQz/arUWUCfDGQ5E23MZBVB1biafDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGBkuqeaQ==",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAnLPigr+A+YlncVdEAx/hDnuy0dS63NjAll5AE4q7r1zyHakzOOOQN47v7eR1k7fnA5Wd1caaeauFLUURk04yBbhAofik1NAy+jjiH9+gTUAMuQlz94xbN6hA3NkNX0qBptEDVjJnnG6M0WZQHQz/arUWUCfDGQ5E23MZBVB1biafDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGBkuqeaQ==",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAnLPigr+A+YlncVdEAx/hDnuy0dS63NjAll5AE4q7r1zyHakzOOOQN47v7eR1k7fnA5Wd1caaeauFLUURk04yBbhAofik1NAy+jjiH9+gTUAMuQlz94xbN6hA3NkNX0qBptEDVjJnnG6M0WZQHQz/arUWUCfDGQ5E23MZBVB1biafDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGBkuqeaQ==",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
  "id": -576460752303422396,
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
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
  "id": -576460752303422396,
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "state": "tx_+QEOCwH4hLhAnLPigr+A+YlncVdEAx/hDnuy0dS63NjAll5AE4q7r1zyHakzOOOQN47v7eR1k7fnA5Wd1caaeauFLUURk04yBbhAofik1NAy+jjiH9+gTUAMuQlz94xbN6hA3NkNX0qBptEDVjJnnG6M0WZQHQz/arUWUCfDGQ5E23MZBVB1biafDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGBkuqeaQ=="
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "state": "tx_+QEOCwH4hLhAnLPigr+A+YlncVdEAx/hDnuy0dS63NjAll5AE4q7r1zyHakzOOOQN47v7eR1k7fnA5Wd1caaeauFLUURk04yBbhAofik1NAy+jjiH9+gTUAMuQlz94xbN6hA3NkNX0qBptEDVjJnnG6M0WZQHQz/arUWUCfDGQ5E23MZBVB1biafDbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGBkuqeaQ=="
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBhbppYR9n7+EJBPhfWhsEjeHz9AXNKWiodkx4AzDn9ZfoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/FSdDYOKAPDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgKBgkgNGtY=",
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
  "id": -576460752303422395,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEDpOU/5xaYIg4LItGJEdcpzJIufwBwsDUfSjwmzACAY0Rvg2i1I02JFFY69lMI353HE2M4P3KfsxttAcXVcX4gLuHX4czMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2DigDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgYLj9Vgg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
  "id": -576460752303422395,
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "signed_tx": "tx_+L0LAfhCuEDpOU/5xaYIg4LItGJEdcpzJIufwBwsDUfSjwmzACAY0Rvg2i1I02JFFY69lMI353HE2M4P3KfsxttAcXVcX4gLuHX4czMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2DigDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgYLj9Vgg",
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
  "id": -576460752303422394,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P8LAfiEuEBFW+SOhcdaua1jz4lRFvVyAa1afph1z9LvCpr+d2MtUh6KvbQPmgoBC4dAZeRBDgrU1NYUShx25S8kcIN3NLkJuEDpOU/5xaYIg4LItGJEdcpzJIufwBwsDUfSjwmzACAY0Rvg2i1I02JFFY69lMI353HE2M4P3KfsxttAcXVcX4gLuHX4czMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2DigDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgYL1ypiZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
  "id": -576460752303422394,
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P8LAfiEuEBFW+SOhcdaua1jz4lRFvVyAa1afph1z9LvCpr+d2MtUh6KvbQPmgoBC4dAZeRBDgrU1NYUShx25S8kcIN3NLkJuEDpOU/5xaYIg4LItGJEdcpzJIufwBwsDUfSjwmzACAY0Rvg2i1I02JFFY69lMI353HE2M4P3KfsxttAcXVcX4gLuHX4czMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2DigDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgYL1ypiZ",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P8LAfiEuEBFW+SOhcdaua1jz4lRFvVyAa1afph1z9LvCpr+d2MtUh6KvbQPmgoBC4dAZeRBDgrU1NYUShx25S8kcIN3NLkJuEDpOU/5xaYIg4LItGJEdcpzJIufwBwsDUfSjwmzACAY0Rvg2i1I02JFFY69lMI353HE2M4P3KfsxttAcXVcX4gLuHX4czMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2DigDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgYL1ypiZ",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P8LAfiEuEBFW+SOhcdaua1jz4lRFvVyAa1afph1z9LvCpr+d2MtUh6KvbQPmgoBC4dAZeRBDgrU1NYUShx25S8kcIN3NLkJuEDpOU/5xaYIg4LItGJEdcpzJIufwBwsDUfSjwmzACAY0Rvg2i1I02JFFY69lMI353HE2M4P3KfsxttAcXVcX4gLuHX4czMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2DigDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgYL1ypiZ",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P8LAfiEuEBFW+SOhcdaua1jz4lRFvVyAa1afph1z9LvCpr+d2MtUh6KvbQPmgoBC4dAZeRBDgrU1NYUShx25S8kcIN3NLkJuEDpOU/5xaYIg4LItGJEdcpzJIufwBwsDUfSjwmzACAY0Rvg2i1I02JFFY69lMI353HE2M4P3KfsxttAcXVcX4gLuHX4czMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2DigDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgYL1ypiZ",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "state": "tx_+P8LAfiEuEBFW+SOhcdaua1jz4lRFvVyAa1afph1z9LvCpr+d2MtUh6KvbQPmgoBC4dAZeRBDgrU1NYUShx25S8kcIN3NLkJuEDpOU/5xaYIg4LItGJEdcpzJIufwBwsDUfSjwmzACAY0Rvg2i1I02JFFY69lMI353HE2M4P3KfsxttAcXVcX4gLuHX4czMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2DigDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgYL1ypiZ"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "state": "tx_+P8LAfiEuEBFW+SOhcdaua1jz4lRFvVyAa1afph1z9LvCpr+d2MtUh6KvbQPmgoBC4dAZeRBDgrU1NYUShx25S8kcIN3NLkJuEDpOU/5xaYIg4LItGJEdcpzJIufwBwsDUfSjwmzACAY0Rvg2i1I02JFFY69lMI353HE2M4P3KfsxttAcXVcX4gLuHX4czMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUnQ2DigDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgYL1ypiZ"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBhbppYR9n7+EJBPhfWhsEjeHz9AXNKWiodkx4AzDn9ZfoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/Aobiv0KBY8rhhwx3FNZzZtoqk4aiWG2eYbpEkfYl8gYb5T3SICgM10yEpWA==",
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
  "id": -576460752303422393,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEA/MbV0ASIzzv8ZO99gHYrrhdwlUG+m+7BcAkRd2AXgqU1H6xiMH1BF5W4fkRmBbwYFu4BxwYWagi4PC6S+LpIEuHT4cjMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDNVAtSn8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
  "id": -576460752303422393,
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEA/MbV0ASIzzv8ZO99gHYrrhdwlUG+m+7BcAkRd2AXgqU1H6xiMH1BF5W4fkRmBbwYFu4BxwYWagi4PC6S+LpIEuHT4cjMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDNVAtSn8=",
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

#### initiator ---> node
```javascript
{
  "id": -576460752303422392,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEA/MbV0ASIzzv8ZO99gHYrrhdwlUG+m+7BcAkRd2AXgqU1H6xiMH1BF5W4fkRmBbwYFu4BxwYWagi4PC6S+LpIEuEDNXgakvOYeabUzd743N3gqSoiXWBLog+BdRC6wkJ5CCEtMXiPJlUzyvVX51TQAbA3YE20tG+V2c6cQVcAMw6kFuHT4cjMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDNTzcrF8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
  "id": -576460752303422392,
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEA/MbV0ASIzzv8ZO99gHYrrhdwlUG+m+7BcAkRd2AXgqU1H6xiMH1BF5W4fkRmBbwYFu4BxwYWagi4PC6S+LpIEuEDNXgakvOYeabUzd743N3gqSoiXWBLog+BdRC6wkJ5CCEtMXiPJlUzyvVX51TQAbA3YE20tG+V2c6cQVcAMw6kFuHT4cjMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDNTzcrF8=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEA/MbV0ASIzzv8ZO99gHYrrhdwlUG+m+7BcAkRd2AXgqU1H6xiMH1BF5W4fkRmBbwYFu4BxwYWagi4PC6S+LpIEuEDNXgakvOYeabUzd743N3gqSoiXWBLog+BdRC6wkJ5CCEtMXiPJlUzyvVX51TQAbA3YE20tG+V2c6cQVcAMw6kFuHT4cjMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDNTzcrF8=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "message": {
        "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEA/MbV0ASIzzv8ZO99gHYrrhdwlUG+m+7BcAkRd2AXgqU1H6xiMH1BF5W4fkRmBbwYFu4BxwYWagi4PC6S+LpIEuEDNXgakvOYeabUzd743N3gqSoiXWBLog+BdRC6wkJ5CCEtMXiPJlUzyvVX51TQAbA3YE20tG+V2c6cQVcAMw6kFuHT4cjMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDNTzcrF8=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEA/MbV0ASIzzv8ZO99gHYrrhdwlUG+m+7BcAkRd2AXgqU1H6xiMH1BF5W4fkRmBbwYFu4BxwYWagi4PC6S+LpIEuEDNXgakvOYeabUzd743N3gqSoiXWBLog+BdRC6wkJ5CCEtMXiPJlUzyvVX51TQAbA3YE20tG+V2c6cQVcAMw6kFuHT4cjMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDNTzcrF8=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "state": "tx_+P4LAfiEuEA/MbV0ASIzzv8ZO99gHYrrhdwlUG+m+7BcAkRd2AXgqU1H6xiMH1BF5W4fkRmBbwYFu4BxwYWagi4PC6S+LpIEuEDNXgakvOYeabUzd743N3gqSoiXWBLog+BdRC6wkJ5CCEtMXiPJlUzyvVX51TQAbA3YE20tG+V2c6cQVcAMw6kFuHT4cjMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDNTzcrF8="
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "state": "tx_+P4LAfiEuEA/MbV0ASIzzv8ZO99gHYrrhdwlUG+m+7BcAkRd2AXgqU1H6xiMH1BF5W4fkRmBbwYFu4BxwYWagi4PC6S+LpIEuEDNXgakvOYeabUzd743N3gqSoiXWBLog+BdRC6wkJ5CCEtMXiPJlUzyvVX51TQAbA3YE20tG+V2c6cQVcAMw6kFuHT4cjMBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKG4r9CgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDNTzcrF8="
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBhbppYR9n7+EJBPhfWhsEjeHz9AXNKWiodkx4AzDn9ZfoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+GXW6AGGHK96fwgDAIYPY36W8ACBgzHfUAk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422391,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEDph4WutKhM7DC+0QfNzcALrG16MhGQyqh09Cszvr3B/o9T96yDhD6yYTadvuOBpXQUWdDaUNCnr8r7u2Tyr2wAuGD4XjUBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1ugBhhyven8IAwCGD2N+lvAAgYNxalOu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
  "id": -576460752303422391,
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEDph4WutKhM7DC+0QfNzcALrG16MhGQyqh09Cszvr3B/o9T96yDhD6yYTadvuOBpXQUWdDaUNCnr8r7u2Tyr2wAuGD4XjUBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1ugBhhyven8IAwCGD2N+lvAAgYNxalOu",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422390,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuECzQQJvBWPeCnyU8WY7zPJKJXLQJLvRc4QLURG7vfzsh1JLao/1lmTzGZInnbwm8ZWDg8DyNOr8vLeASfY1xLIPuEDph4WutKhM7DC+0QfNzcALrG16MhGQyqh09Cszvr3B/o9T96yDhD6yYTadvuOBpXQUWdDaUNCnr8r7u2Tyr2wAuGD4XjUBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1ugBhhyven8IAwCGD2N+lvAAgYNOPxMb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
  "id": -576460752303422390,
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuECzQQJvBWPeCnyU8WY7zPJKJXLQJLvRc4QLURG7vfzsh1JLao/1lmTzGZInnbwm8ZWDg8DyNOr8vLeASfY1xLIPuEDph4WutKhM7DC+0QfNzcALrG16MhGQyqh09Cszvr3B/o9T96yDhD6yYTadvuOBpXQUWdDaUNCnr8r7u2Tyr2wAuGD4XjUBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1ugBhhyven8IAwCGD2N+lvAAgYNOPxMb",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuECzQQJvBWPeCnyU8WY7zPJKJXLQJLvRc4QLURG7vfzsh1JLao/1lmTzGZInnbwm8ZWDg8DyNOr8vLeASfY1xLIPuEDph4WutKhM7DC+0QfNzcALrG16MhGQyqh09Cszvr3B/o9T96yDhD6yYTadvuOBpXQUWdDaUNCnr8r7u2Tyr2wAuGD4XjUBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1ugBhhyven8IAwCGD2N+lvAAgYNOPxMb",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuECzQQJvBWPeCnyU8WY7zPJKJXLQJLvRc4QLURG7vfzsh1JLao/1lmTzGZInnbwm8ZWDg8DyNOr8vLeASfY1xLIPuEDph4WutKhM7DC+0QfNzcALrG16MhGQyqh09Cszvr3B/o9T96yDhD6yYTadvuOBpXQUWdDaUNCnr8r7u2Tyr2wAuGD4XjUBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1ugBhhyven8IAwCGD2N+lvAAgYNOPxMb",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuECzQQJvBWPeCnyU8WY7zPJKJXLQJLvRc4QLURG7vfzsh1JLao/1lmTzGZInnbwm8ZWDg8DyNOr8vLeASfY1xLIPuEDph4WutKhM7DC+0QfNzcALrG16MhGQyqh09Cszvr3B/o9T96yDhD6yYTadvuOBpXQUWdDaUNCnr8r7u2Tyr2wAuGD4XjUBoQYW6aWEfZ+/hCQT4X1obBI3h8/QFzSloqHZMeAMw5/WX6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/hl1ugBhhyven8IAwCGD2N+lvAAgYNOPxMb",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
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
    "channel_id": "ch_B6GskGeb5y4H9wbjYNEYJaMuXGTBPZ8XxoCmHHYNhU31LMFEL",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
