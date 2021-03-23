
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=123456789876543&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator
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
      "fsm_id": "ba_c06FKbS8rHbvPqhaXU2oIMzdZDClrwbNJ6Zdf5IGAfyZdOgA"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=123456789876543&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder
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
      "fsm_id": "ba_vPp/qX59hb5M7pTMo4eGbEZsODYEskO1ZkzcX7d5D1858Z4I"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhnBIhhsPP8CgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY3pn6HAQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422679,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBc41hBRED+XCRgn9A6Dy5fOB+rEsb4JShFCWBVHjIA6y52FnWEZFf/aP5A6pRbe8yNkCJ8ScDd4xTM132B/MABuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIZwSIYbDz/AoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGN3YNLsw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422679,
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_vPp/qX59hb5M7pTMo4eGbEZsODYEskO1ZkzcX7d5D1858Z4I"
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBc41hBRED+XCRgn9A6Dy5fOB+rEsb4JShFCWBVHjIA6y52FnWEZFf/aP5A6pRbe8yNkCJ8ScDd4xTM132B/MABuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIZwSIYbDz/AoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGN3YNLsw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422678,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAUXpsvC1XtxMXFDcLcBJ2QwKBJ5XsF44z+Q3HHNjAtHF4TFCOqoeLbMfI6Z5EZm7GNmPYTqGCju9YtVs2l3bwB7hAXONYQURA/lwkYJ/QOg8uXzgfqxLG+CUoRQlgVR4yAOsudhZ1hGRX/2j+QOqUW3vMjZAifEnA3eMUzNd9gfzAAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGcEiGGw8/wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rjfxd+KZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
  "id": -576460752303422678,
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAUXpsvC1XtxMXFDcLcBJ2QwKBJ5XsF44z+Q3HHNjAtHF4TFCOqoeLbMfI6Z5EZm7GNmPYTqGCju9YtVs2l3bwB7hAXONYQURA/lwkYJ/QOg8uXzgfqxLG+CUoRQlgVR4yAOsudhZ1hGRX/2j+QOqUW3vMjZAifEnA3eMUzNd9gfzAAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGcEiGGw8/wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rjfxd+KZ",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_c06FKbS8rHbvPqhaXU2oIMzdZDClrwbNJ6Zdf5IGAfyZdOgA"
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAUXpsvC1XtxMXFDcLcBJ2QwKBJ5XsF44z+Q3HHNjAtHF4TFCOqoeLbMfI6Z5EZm7GNmPYTqGCju9YtVs2l3bwB7hAXONYQURA/lwkYJ/QOg8uXzgfqxLG+CUoRQlgVR4yAOsudhZ1hGRX/2j+QOqUW3vMjZAifEnA3eMUzNd9gfzAAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGcEiGGw8/wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rjfxd+KZ",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAUXpsvC1XtxMXFDcLcBJ2QwKBJ5XsF44z+Q3HHNjAtHF4TFCOqoeLbMfI6Z5EZm7GNmPYTqGCju9YtVs2l3bwB7hAXONYQURA/lwkYJ/QOg8uXzgfqxLG+CUoRQlgVR4yAOsudhZ1hGRX/2j+QOqUW3vMjZAifEnA3eMUzNd9gfzAAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGcEiGGw8/wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rjfxd+KZ",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAUXpsvC1XtxMXFDcLcBJ2QwKBJ5XsF44z+Q3HHNjAtHF4TFCOqoeLbMfI6Z5EZm7GNmPYTqGCju9YtVs2l3bwB7hAXONYQURA/lwkYJ/QOg8uXzgfqxLG+CUoRQlgVR4yAOsudhZ1hGRX/2j+QOqUW3vMjZAifEnA3eMUzNd9gfzAAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGcEiGGw8/wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rjfxd+KZ",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "message": {
        "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "message": {
        "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
  "id": -576460752303422677,
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
  "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
  "id": -576460752303422677,
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "event": "open"
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "state": "tx_+QENCwH4hLhAUXpsvC1XtxMXFDcLcBJ2QwKBJ5XsF44z+Q3HHNjAtHF4TFCOqoeLbMfI6Z5EZm7GNmPYTqGCju9YtVs2l3bwB7hAXONYQURA/lwkYJ/QOg8uXzgfqxLG+CUoRQlgVR4yAOsudhZ1hGRX/2j+QOqUW3vMjZAifEnA3eMUzNd9gfzAAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGcEiGGw8/wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rjfxd+KZ"
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "state": "tx_+QENCwH4hLhAUXpsvC1XtxMXFDcLcBJ2QwKBJ5XsF44z+Q3HHNjAtHF4TFCOqoeLbMfI6Z5EZm7GNmPYTqGCju9YtVs2l3bwB7hAXONYQURA/lwkYJ/QOg8uXzgfqxLG+CUoRQlgVR4yAOsudhZ1hGRX/2j+QOqUW3vMjZAifEnA3eMUzNd9gfzAAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGcEiGGw8/wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rjfxd+KZ"
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBnFRkBxc6do/S56aINq6erV1lHWV+cDQZ6i4MDj4Ds1FoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/+GHLHOiuwBAIYPXtZ/KAA4D/FgMg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422676,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBHTSyi7fg/CmwQ7Furb5hFgszjXcwpRdhR1U6+9tU4n0PYDLeAaXrenl+OpKD7m7VoNnHYyzqf5fXXceTRDN8DuF/4XTUBoQZxUZAcXOnaP0uemiDaunq1dZR1lfnA0GeouDA4+A7NRaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAOF+dwFg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
  "id": -576460752303422676,
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBHTSyi7fg/CmwQ7Furb5hFgszjXcwpRdhR1U6+9tU4n0PYDLeAaXrenl+OpKD7m7VoNnHYyzqf5fXXceTRDN8DuF/4XTUBoQZxUZAcXOnaP0uemiDaunq1dZR1lfnA0GeouDA4+A7NRaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAOF+dwFg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422675,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBHTSyi7fg/CmwQ7Furb5hFgszjXcwpRdhR1U6+9tU4n0PYDLeAaXrenl+OpKD7m7VoNnHYyzqf5fXXceTRDN8DuED5i9N3ROyavVG7ve3LiaNCBCuyidWsErNT7NiJStGfLHbxT6Vhzcdtg7Jji9GDJZbv8mxWKRWXr7CxKJixO0AGuF/4XTUBoQZxUZAcXOnaP0uemiDaunq1dZR1lfnA0GeouDA4+A7NRaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAODQwj7M="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
  "id": -576460752303422675,
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBHTSyi7fg/CmwQ7Furb5hFgszjXcwpRdhR1U6+9tU4n0PYDLeAaXrenl+OpKD7m7VoNnHYyzqf5fXXceTRDN8DuED5i9N3ROyavVG7ve3LiaNCBCuyidWsErNT7NiJStGfLHbxT6Vhzcdtg7Jji9GDJZbv8mxWKRWXr7CxKJixO0AGuF/4XTUBoQZxUZAcXOnaP0uemiDaunq1dZR1lfnA0GeouDA4+A7NRaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAODQwj7M=",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBHTSyi7fg/CmwQ7Furb5hFgszjXcwpRdhR1U6+9tU4n0PYDLeAaXrenl+OpKD7m7VoNnHYyzqf5fXXceTRDN8DuED5i9N3ROyavVG7ve3LiaNCBCuyidWsErNT7NiJStGfLHbxT6Vhzcdtg7Jji9GDJZbv8mxWKRWXr7CxKJixO0AGuF/4XTUBoQZxUZAcXOnaP0uemiDaunq1dZR1lfnA0GeouDA4+A7NRaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAODQwj7M=",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBHTSyi7fg/CmwQ7Furb5hFgszjXcwpRdhR1U6+9tU4n0PYDLeAaXrenl+OpKD7m7VoNnHYyzqf5fXXceTRDN8DuED5i9N3ROyavVG7ve3LiaNCBCuyidWsErNT7NiJStGfLHbxT6Vhzcdtg7Jji9GDJZbv8mxWKRWXr7CxKJixO0AGuF/4XTUBoQZxUZAcXOnaP0uemiDaunq1dZR1lfnA0GeouDA4+A7NRaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAODQwj7M=",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBHTSyi7fg/CmwQ7Furb5hFgszjXcwpRdhR1U6+9tU4n0PYDLeAaXrenl+OpKD7m7VoNnHYyzqf5fXXceTRDN8DuED5i9N3ROyavVG7ve3LiaNCBCuyidWsErNT7NiJStGfLHbxT6Vhzcdtg7Jji9GDJZbv8mxWKRWXr7CxKJixO0AGuF/4XTUBoQZxUZAcXOnaP0uemiDaunq1dZR1lfnA0GeouDA4+A7NRaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAODQwj7M=",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
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
    "channel_id": "ch_ruaA8hG9HfRxefWes1aVrQacfLb232qr6QeTcmFan8qjVHo8Q",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
