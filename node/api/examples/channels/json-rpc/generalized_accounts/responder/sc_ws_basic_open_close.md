
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4&keep_running=false&lock_period=10&port=13079&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c&role=initiator
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
      "fsm_id": "ba_4Ja7sr88eB7AhwnuJiQecSGvxseVF/1CXjgi+C0Y6NZoPXvU"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4&keep_running=false&lock_period=10&port=13079&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c&role=responder
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
      "fsm_id": "ba_5TNrxaABMwvauQ6hjlvVystt4qKWjG9BxzPWLaar86R40Z29"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAZChMuwVtlbTrOcYFs5yd9Hf4GtFC1IAetiGYzEJ6/dohj+qJSJgAKEBWMH5l8Uq7Y/JgAu9kI7Z3+PsLO/LkRI8oQl6CDI+GxSGJGE5yoAAAgoAhhAGeddIAMCgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xQBEvHHqw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422155,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB7rJvBD0ziaagC0DdQOdyYnWUYiXFqvIjDHGXzBhxRqPl/oNYSpcqjIr6cH4Mt05i2z85WfQ38rE5KTJi/ZUAIuIP4gTIBoQGQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIY/qiUiYAChAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUhiRhOcqAAAIKAIYQBnnXSADAoFLbU7BcXb4IP6lQl8w8pITyWWqmwZJimnu4VObIKO8UAQcpbEE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422155,
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
    "channel_id": null,
    "data": {
      "event": "funding_created"
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
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuEB7rJvBD0ziaagC0DdQOdyYnWUYiXFqvIjDHGXzBhxRqPl/oNYSpcqjIr6cH4Mt05i2z85WfQ38rE5KTJi/ZUAIuIP4gTIBoQGQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIY/qiUiYAChAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUhiRhOcqAAAIKAIYQBnnXSADAoFLbU7BcXb4IP6lQl8w8pITyWWqmwZJimnu4VObIKO8UAQcpbEE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422154,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QGxCwHAuQGr+QGoUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEB7rJvBD0ziaagC0DdQOdyYnWUYiXFqvIjDHGXzBhxRqPl/oNYSpcqjIr6cH4Mt05i2z85WfQ38rE5KTJi/ZUAIuIP4gTIBoQGQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIY/qiUiYAChAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUhiRhOcqAAAIKAIYQBnnXSADAoFLbU7BcXb4IP6lQl8w8pITyWWqmwZJimnu4VObIKO8UARuiX1A="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422154,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEB7rJvBD0ziaagC0DdQOdyYnWUYiXFqvIjDHGXzBhxRqPl/oNYSpcqjIr6cH4Mt05i2z85WfQ38rE5KTJi/ZUAIuIP4gTIBoQGQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIY/qiUiYAChAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUhiRhOcqAAAIKAIYQBnnXSADAoFLbU7BcXb4IP6lQl8w8pITyWWqmwZJimnu4VObIKO8UARuiX1A=",
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEB7rJvBD0ziaagC0DdQOdyYnWUYiXFqvIjDHGXzBhxRqPl/oNYSpcqjIr6cH4Mt05i2z85WfQ38rE5KTJi/ZUAIuIP4gTIBoQGQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIY/qiUiYAChAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUhiRhOcqAAAIKAIYQBnnXSADAoFLbU7BcXb4IP6lQl8w8pITyWWqmwZJimnu4VObIKO8UARuiX1A=",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEB7rJvBD0ziaagC0DdQOdyYnWUYiXFqvIjDHGXzBhxRqPl/oNYSpcqjIr6cH4Mt05i2z85WfQ38rE5KTJi/ZUAIuIP4gTIBoQGQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIY/qiUiYAChAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUhiRhOcqAAAIKAIYQBnnXSADAoFLbU7BcXb4IP6lQl8w8pITyWWqmwZJimnu4VObIKO8UARuiX1A=",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEB7rJvBD0ziaagC0DdQOdyYnWUYiXFqvIjDHGXzBhxRqPl/oNYSpcqjIr6cH4Mt05i2z85WfQ38rE5KTJi/ZUAIuIP4gTIBoQGQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIY/qiUiYAChAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUhiRhOcqAAAIKAIYQBnnXSADAoFLbU7BcXb4IP6lQl8w8pITyWWqmwZJimnu4VObIKO8UARuiX1A=",
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
    "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "message": {
        "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
        "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
        "info": "Hello",
        "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "message": {
        "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
        "info": "Hello back",
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422153,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422153,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "balance": 69999999999999
    },
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "event": "own_funding_locked"
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEB7rJvBD0ziaagC0DdQOdyYnWUYiXFqvIjDHGXzBhxRqPl/oNYSpcqjIr6cH4Mt05i2z85WfQ38rE5KTJi/ZUAIuIP4gTIBoQGQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIY/qiUiYAChAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUhiRhOcqAAAIKAIYQBnnXSADAoFLbU7BcXb4IP6lQl8w8pITyWWqmwZJimnu4VObIKO8UARuiX1A="
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEB7rJvBD0ziaagC0DdQOdyYnWUYiXFqvIjDHGXzBhxRqPl/oNYSpcqjIr6cH4Mt05i2z85WfQ38rE5KTJi/ZUAIuIP4gTIBoQGQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIY/qiUiYAChAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUhiRhOcqAAAIKAIYQBnnXSADAoFLbU7BcXb4IP6lQl8w8pITyWWqmwZJimnu4VObIKO8UARuiX1A="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422152,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422152,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "balance": 69999999999999
    },
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
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
    "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
    "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
        "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
    "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
    "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
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
    "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
    "meta": 17,
    "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
        "meta": 17,
        "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
    "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
    "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgAqDh9wlC3xi+bYwAuI6f3xIZMit7kRhrBfpsevA6VTUAEImyvDI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
          "op": "OffChainTransfer",
          "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
  "id": -576460752303422151,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED1Umv6lrFjqvUhTy4eR6n0ylpYniwLCHNq+WzF2iWWFibnSxeRmu+D1Cor1iVKsusOy3OPAesK8isvbV0Ar9ADuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AKg4fcJQt8Yvm2MALiOn98SGTIre5EYawX6bHrwOlU1ABAPqXEt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422151,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+JALAfhCuED1Umv6lrFjqvUhTy4eR6n0ylpYniwLCHNq+WzF2iWWFibnSxeRmu+D1Cor1iVKsusOy3OPAesK8isvbV0Ar9ADuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AKg4fcJQt8Yvm2MALiOn98SGTIre5EYawX6bHrwOlU1ABAPqXEt",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
          "op": "OffChainTransfer",
          "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
  "id": -576460752303422150,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED1Umv6lrFjqvUhTy4eR6n0ylpYniwLCHNq+WzF2iWWFibnSxeRmu+D1Cor1iVKsusOy3OPAesK8isvbV0Ar9ADuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AKg4fcJQt8Yvm2MALiOn98SGTIre5EYawX6bHrwOlU1ABCv3Xce"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422150,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED1Umv6lrFjqvUhTy4eR6n0ylpYniwLCHNq+WzF2iWWFibnSxeRmu+D1Cor1iVKsusOy3OPAesK8isvbV0Ar9ADuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AKg4fcJQt8Yvm2MALiOn98SGTIre5EYawX6bHrwOlU1ABCv3Xce"
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED1Umv6lrFjqvUhTy4eR6n0ylpYniwLCHNq+WzF2iWWFibnSxeRmu+D1Cor1iVKsusOy3OPAesK8isvbV0Ar9ADuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AKg4fcJQt8Yvm2MALiOn98SGTIre5EYawX6bHrwOlU1ABCv3Xce"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422149,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422149,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "balance": 69999999999998
    },
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422148,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422148,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED1Umv6lrFjqvUhTy4eR6n0ylpYniwLCHNq+WzF2iWWFibnSxeRmu+D1Cor1iVKsusOy3OPAesK8isvbV0Ar9ADuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AKg4fcJQt8Yvm2MALiOn98SGTIre5EYawX6bHrwOlU1ABCv3Xce",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIvKCgEAhj+qJSJf/rDvQAGgWMH5l8Uq7Y/JgAu9kI7Z3+PsLO/LkRI8oQl6CDI+GxSLygoBAIYkYTnKgAIHaGWj"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422147,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422147,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "balance": 40000000000002
    },
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "meta": 17,
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
        "meta": 17,
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgA6BS21OwXF2+CD+pUJfMPKSE8llqpsGSYpp7uFTmyCjvFO57mDk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
          "op": "OffChainTransfer",
          "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
  "id": -576460752303422146,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgA6BS21OwXF2+CD+pUJfMPKSE8llqpsGSYpp7uFTmyCjvFGZGK7s="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422146,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgA6BS21OwXF2+CD+pUJfMPKSE8llqpsGSYpp7uFTmyCjvFGZGK7s=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
          "op": "OffChainTransfer",
          "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
  "id": -576460752303422145,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECn+sGMSliTnaD//UK0bYaKr9qGnOjjTewDKfGAO5jyx5g0csht24CNbOzYZmKXPYq4cAa0xE5LWE6J/UCPacQOuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AOgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xQSE366"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422145,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECn+sGMSliTnaD//UK0bYaKr9qGnOjjTewDKfGAO5jyx5g0csht24CNbOzYZmKXPYq4cAa0xE5LWE6J/UCPacQOuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AOgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xQSE366"
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECn+sGMSliTnaD//UK0bYaKr9qGnOjjTewDKfGAO5jyx5g0csht24CNbOzYZmKXPYq4cAa0xE5LWE6J/UCPacQOuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AOgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xQSE366"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422144,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422144,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "balance": 40000000000001
    },
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422143,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422143,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECn+sGMSliTnaD//UK0bYaKr9qGnOjjTewDKfGAO5jyx5g0csht24CNbOzYZmKXPYq4cAa0xE5LWE6J/UCPacQOuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AOgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xQSE366",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIvKCgEAhj+qJSJf/7DvQAGgWMH5l8Uq7Y/JgAu9kI7Z3+PsLO/LkRI8oQl6CDI+GxSLygoBAIYkYTnKgAH2PZtl"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422142,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422142,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "balance": 40000000000001
    },
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "meta": 17,
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
        "meta": 17,
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgBKCv5SjFM1bx1vTtNFKrNxVYu8pN+68e8QW9VhrY4RxMNBf8NSg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
          "op": "OffChainTransfer",
          "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
  "id": -576460752303422141,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgBKCv5SjFM1bx1vTtNFKrNxVYu8pN+68e8QW9VhrY4RxMNAEw6bM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422141,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgBKCv5SjFM1bx1vTtNFKrNxVYu8pN+68e8QW9VhrY4RxMNAEw6bM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
          "op": "OffChainTransfer",
          "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
  "id": -576460752303422140,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDZ1h/eYUJlCDWjU0Pe/MwgR7WxDGpYdYOkBT4NeY4XvtEdWvibZNeiFtXbOpgDhq3eZ3t7rGCqZWNzzTQyuvMEuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4ASgr+UoxTNW8db07TRSqzcVWLvKTfuvHvEFvVYa2OEcTDRsKGNq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422140,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDZ1h/eYUJlCDWjU0Pe/MwgR7WxDGpYdYOkBT4NeY4XvtEdWvibZNeiFtXbOpgDhq3eZ3t7rGCqZWNzzTQyuvMEuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4ASgr+UoxTNW8db07TRSqzcVWLvKTfuvHvEFvVYa2OEcTDRsKGNq"
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDZ1h/eYUJlCDWjU0Pe/MwgR7WxDGpYdYOkBT4NeY4XvtEdWvibZNeiFtXbOpgDhq3eZ3t7rGCqZWNzzTQyuvMEuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4ASgr+UoxTNW8db07TRSqzcVWLvKTfuvHvEFvVYa2OEcTDRsKGNq"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422139,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422139,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "balance": 40000000000000
    },
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422138,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422138,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDZ1h/eYUJlCDWjU0Pe/MwgR7WxDGpYdYOkBT4NeY4XvtEdWvibZNeiFtXbOpgDhq3eZ3t7rGCqZWNzzTQyuvMEuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4ASgr+UoxTNW8db07TRSqzcVWLvKTfuvHvEFvVYa2OEcTDRsKGNq",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIvKCgEAhj+qJSJgALDvQAGgWMH5l8Uq7Y/JgAu9kI7Z3+PsLO/LkRI8oQl6CDI+GxSLygoBAIYkYTnKgAAWFHsX"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422137,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422137,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "balance": 70000000000000
    },
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
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
    "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
    "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
        "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
    "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
    "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
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
    "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
    "meta": 17,
    "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
        "meta": 17,
        "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
    "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
    "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgBaBS21OwXF2+CD+pUJfMPKSE8llqpsGSYpp7uFTmyCjvFDR6C/w=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
          "op": "OffChainTransfer",
          "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
  "id": -576460752303422136,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDXoIpWZ0/+Wxi00JoBzn+cfKaVgO04mOPdF7eyOdW83hgBbeujVREdEtce2rxrj6w6qOkM/KLFrQsddDlOdR4KuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AWgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xSoAyHq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422136,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDXoIpWZ0/+Wxi00JoBzn+cfKaVgO04mOPdF7eyOdW83hgBbeujVREdEtce2rxrj6w6qOkM/KLFrQsddDlOdR4KuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AWgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xSoAyHq",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
          "op": "OffChainTransfer",
          "to": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
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
  "id": -576460752303422135,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDXoIpWZ0/+Wxi00JoBzn+cfKaVgO04mOPdF7eyOdW83hgBbeujVREdEtce2rxrj6w6qOkM/KLFrQsddDlOdR4KuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AWgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xTBqUfX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422135,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDXoIpWZ0/+Wxi00JoBzn+cfKaVgO04mOPdF7eyOdW83hgBbeujVREdEtce2rxrj6w6qOkM/KLFrQsddDlOdR4KuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AWgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xTBqUfX"
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDXoIpWZ0/+Wxi00JoBzn+cfKaVgO04mOPdF7eyOdW83hgBbeujVREdEtce2rxrj6w6qOkM/KLFrQsddDlOdR4KuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AWgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xTBqUfX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422134,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422134,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "balance": 69999999999999
    },
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422133,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422133,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDXoIpWZ0/+Wxi00JoBzn+cfKaVgO04mOPdF7eyOdW83hgBbeujVREdEtce2rxrj6w6qOkM/KLFrQsddDlOdR4KuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4AWgUttTsFxdvgg/qVCXzDykhPJZaqbBkmKae7hU5sgo7xTBqUfX",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIvKCgEAhj+qJSJf/7DvQAGgWMH5l8Uq7Y/JgAu9kI7Z3+PsLO/LkRI8oQl6CDI+GxSLygoBAIYkYTnKgAH2PZtl"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422132,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422132,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "balance": 40000000000001
    },
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "meta": 17,
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
        "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
        "meta": 17,
        "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
    "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
    "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgBqCv5SjFM1bx1vTtNFKrNxVYu8pN+68e8QW9VhrY4RxMNHxIAlc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
          "op": "OffChainTransfer",
          "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
  "id": -576460752303422131,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgBqCv5SjFM1bx1vTtNFKrNxVYu8pN+68e8QW9VhrY4RxMNCQuOBM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422131,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlFm6cv0L3dlMeqdSI2j57sTITCgov3sBlSZUpTOErDgBqCv5SjFM1bx1vTtNFKrNxVYu8pN+68e8QW9VhrY4RxMNCQuOBM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
          "op": "OffChainTransfer",
          "to": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
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
  "id": -576460752303422130,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED2Htc8ovIovELrgYExKxkF+tMsAXpfmDC9ulTNYqLZ4R4lbHaIgYtZ41CvTyVlAZkM06I9e2LG1HXv1QV3ohoAuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4Aagr+UoxTNW8db07TRSqzcVWLvKTfuvHvEFvVYa2OEcTDR8geYc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422130,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED2Htc8ovIovELrgYExKxkF+tMsAXpfmDC9ulTNYqLZ4R4lbHaIgYtZ41CvTyVlAZkM06I9e2LG1HXv1QV3ohoAuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4Aagr+UoxTNW8db07TRSqzcVWLvKTfuvHvEFvVYa2OEcTDR8geYc"
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED2Htc8ovIovELrgYExKxkF+tMsAXpfmDC9ulTNYqLZ4R4lbHaIgYtZ41CvTyVlAZkM06I9e2LG1HXv1QV3ohoAuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4Aagr+UoxTNW8db07TRSqzcVWLvKTfuvHvEFvVYa2OEcTDR8geYc"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422129,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422129,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_g6CQh2rN6WZPpHW99egBcLJE59xHPbUHuKyd5qnRgfTk3T14c",
      "balance": 40000000000000
    },
    {
      "account": "ak_26hNXXunJyyuTuDfkAbKDVgqe1ifXm4ZJG71Wt3DkevQ7YMwK4",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422128,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422128,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAVjB+ZfFKu2PyYALvZCO2d/j7Czvy5ESPKEJeggyPhsUuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED2Htc8ovIovELrgYExKxkF+tMsAXpfmDC9ulTNYqLZ4R4lbHaIgYtZ41CvTyVlAZkM06I9e2LG1HXv1QV3ohoAuEj4RjkCoQZRZunL9C93ZTHqnUiNo+e7EyEwoKL97AZUmVKUzhKw4Aagr+UoxTNW8db07TRSqzcVWLvKTfuvHvEFvVYa2OEcTDR8geYc",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQoTLsFbZW06znGBbOcnfR3+BrRQtSAHrYhmMxCev3aIvKCgEAhj+qJSJgALDvQAGgWMH5l8Uq7Y/JgAu9kI7Z3+PsLO/LkRI8oQl6CDI+GxSLygoBAIYkYTnKgAAWFHsX"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422127,
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
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422127,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422126,
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
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
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
  "channel_id": "ch_crJgu3QWGjQFTCRST92g9wrHtVw1maBQMpNrwcMqRXY5QsuNH",
  "id": -576460752303422126,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK&keep_running=false&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s&role=initiator
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
      "fsm_id": "ba_cYWXMoMHGCw1Ui1u/95GPZYjRA6KTWcDXrNwlE1bY4htXSRy"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK&keep_running=false&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s&role=responder
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
      "fsm_id": "ba_8bs0RQ4riVJBCsc6BYwoGKTAd2z0XKVjBL68XL8lVDDVjgcD"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAS7jsZyhSrssy2nvLJnGIl0SZV+uvqZP3AJpRTwVjF4Vhj+qJSJgAKEBYgT/WqFMQlgkqfbgp0etqgN8VxdlQ30xAyqLCtOt8RyGJGE5yoAAAgoAhhAGeddIAMCgoRbIB1VFrBVRw1exUbfREt9DqrMnruLkF9JVd8/WXIABCOLNHA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421508,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECdc6S+XI3TIMyD9M3kw0+8FzafZiHfxTnvwsAp2tkQEk70uJz74ymVvEAT19W8t5xdtQBzsOp43fl/t7qFKf8NuIP4gTIBoQEu47GcoUq7LMtp7yyZxiJdEmVfrr6mT9wCaUU8FYxeFYY/qiUiYAChAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEchiRhOcqAAAIKAIYQBnnXSADAoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAAVjrJ7M="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421508,
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
    "channel_id": null,
    "data": {
      "event": "funding_created"
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
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuECdc6S+XI3TIMyD9M3kw0+8FzafZiHfxTnvwsAp2tkQEk70uJz74ymVvEAT19W8t5xdtQBzsOp43fl/t7qFKf8NuIP4gTIBoQEu47GcoUq7LMtp7yyZxiJdEmVfrr6mT9wCaUU8FYxeFYY/qiUiYAChAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEchiRhOcqAAAIKAIYQBnnXSADAoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAAVjrJ7M=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421507,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAnXOkvlyN0yDMg/TN5MNPvBc2n2Yh38U578LAKdrZEBJO9Lic++MplbxAE9fVvLecXbUAc7DqeN35f7e6hSn/DbiD+IEyAaEBLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWGP6olImAAoQFiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIYkYTnKgAACCgCGEAZ510gAwKChFsgHVUWsFVHDV7FRt9ES30Oqsyeu4uQX0lV3z9ZcgAE6OO0P"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421507,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAnXOkvlyN0yDMg/TN5MNPvBc2n2Yh38U578LAKdrZEBJO9Lic++MplbxAE9fVvLecXbUAc7DqeN35f7e6hSn/DbiD+IEyAaEBLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWGP6olImAAoQFiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIYkYTnKgAACCgCGEAZ510gAwKChFsgHVUWsFVHDV7FRt9ES30Oqsyeu4uQX0lV3z9ZcgAE6OO0P",
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAnXOkvlyN0yDMg/TN5MNPvBc2n2Yh38U578LAKdrZEBJO9Lic++MplbxAE9fVvLecXbUAc7DqeN35f7e6hSn/DbiD+IEyAaEBLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWGP6olImAAoQFiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIYkYTnKgAACCgCGEAZ510gAwKChFsgHVUWsFVHDV7FRt9ES30Oqsyeu4uQX0lV3z9ZcgAE6OO0P",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAnXOkvlyN0yDMg/TN5MNPvBc2n2Yh38U578LAKdrZEBJO9Lic++MplbxAE9fVvLecXbUAc7DqeN35f7e6hSn/DbiD+IEyAaEBLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWGP6olImAAoQFiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIYkYTnKgAACCgCGEAZ510gAwKChFsgHVUWsFVHDV7FRt9ES30Oqsyeu4uQX0lV3z9ZcgAE6OO0P",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAnXOkvlyN0yDMg/TN5MNPvBc2n2Yh38U578LAKdrZEBJO9Lic++MplbxAE9fVvLecXbUAc7DqeN35f7e6hSn/DbiD+IEyAaEBLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWGP6olImAAoQFiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIYkYTnKgAACCgCGEAZ510gAwKChFsgHVUWsFVHDV7FRt9ES30Oqsyeu4uQX0lV3z9ZcgAE6OO0P",
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
    "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "message": {
        "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
        "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
        "info": "Hello",
        "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "message": {
        "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
        "info": "Hello back",
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421506,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421506,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "balance": 69999999999999
    },
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAnXOkvlyN0yDMg/TN5MNPvBc2n2Yh38U578LAKdrZEBJO9Lic++MplbxAE9fVvLecXbUAc7DqeN35f7e6hSn/DbiD+IEyAaEBLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWGP6olImAAoQFiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIYkYTnKgAACCgCGEAZ510gAwKChFsgHVUWsFVHDV7FRt9ES30Oqsyeu4uQX0lV3z9ZcgAE6OO0P"
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAnXOkvlyN0yDMg/TN5MNPvBc2n2Yh38U578LAKdrZEBJO9Lic++MplbxAE9fVvLecXbUAc7DqeN35f7e6hSn/DbiD+IEyAaEBLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWGP6olImAAoQFiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIYkYTnKgAACCgCGEAZ510gAwKChFsgHVUWsFVHDV7FRt9ES30Oqsyeu4uQX0lV3z9ZcgAE6OO0P"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421505,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421505,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "balance": 69999999999999
    },
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
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
    "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
    "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
        "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
    "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
    "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
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
    "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
    "meta": 17,
    "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
        "meta": 17,
        "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
    "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
    "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlbdYB5ex+4ZiyLQVJ68kHgjkH1JP1wouGFAndTluA9/AqDD7VpK7qFzSBYFlhgWM69UMqmrGVdNFYEhjO5D9hxEWCJzRrg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
          "op": "OffChainTransfer",
          "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
  "id": -576460752303421504,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDYQ38ca+gpdhnOq9DWqGldB+g0KxFqcpTjHqMkF5m5MoB5n0O3WFHvu1yixJUaWmI6/mHkDYVq6+4Y48t/Z8UMuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwKgw+1aSu6hc0gWBZYYFjOvVDKpqxlXTRWBIYzuQ/YcRFjhJ6TQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421504,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDYQ38ca+gpdhnOq9DWqGldB+g0KxFqcpTjHqMkF5m5MoB5n0O3WFHvu1yixJUaWmI6/mHkDYVq6+4Y48t/Z8UMuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwKgw+1aSu6hc0gWBZYYFjOvVDKpqxlXTRWBIYzuQ/YcRFjhJ6TQ",
      "updates": [
        {
          "amount": 1,
          "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
          "op": "OffChainTransfer",
          "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
  "id": -576460752303421503,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2EN/HGvoKXYZzqvQ1qhpXQfoNCsRanKU4x6jJBeZuTKAeZ9Dt1hR77tcosSVGlpiOv5h5A2FauvuGOPLf2fFDLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38CoMPtWkruoXNIFgWWGBYzr1QyqasZV00VgSGM7kP2HERYqTNqKg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421503,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2EN/HGvoKXYZzqvQ1qhpXQfoNCsRanKU4x6jJBeZuTKAeZ9Dt1hR77tcosSVGlpiOv5h5A2FauvuGOPLf2fFDLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38CoMPtWkruoXNIFgWWGBYzr1QyqasZV00VgSGM7kP2HERYqTNqKg=="
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2EN/HGvoKXYZzqvQ1qhpXQfoNCsRanKU4x6jJBeZuTKAeZ9Dt1hR77tcosSVGlpiOv5h5A2FauvuGOPLf2fFDLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38CoMPtWkruoXNIFgWWGBYzr1QyqasZV00VgSGM7kP2HERYqTNqKg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421502,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421502,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "balance": 69999999999998
    },
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421501,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421501,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2EN/HGvoKXYZzqvQ1qhpXQfoNCsRanKU4x6jJBeZuTKAeZ9Dt1hR77tcosSVGlpiOv5h5A2FauvuGOPLf2fFDLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38CoMPtWkruoXNIFgWWGBYzr1QyqasZV00VgSGM7kP2HERYqTNqKg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIvKCgEAhiRhOcqAArDvQAGgLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWLygoBAIY/qiUiX/6gmcaK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421500,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421500,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "balance": 40000000000002
    },
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "meta": 17,
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
        "meta": 17,
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlbdYB5ex+4ZiyLQVJ68kHgjkH1JP1wouGFAndTluA9/A6ChFsgHVUWsFVHDV7FRt9ES30Oqsyeu4uQX0lV3z9ZcgDIRFxg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
          "op": "OffChainTransfer",
          "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
  "id": -576460752303421499,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwOgoRbIB1VFrBVRw1exUbfREt9DqrMnruLkF9JVd8/WXICqGZXD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421499,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwOgoRbIB1VFrBVRw1exUbfREt9DqrMnruLkF9JVd8/WXICqGZXD",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
          "op": "OffChainTransfer",
          "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
  "id": -576460752303421498,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAsHpd/md3z2VCF98ADXJOr4y2u0k2g8VawsyeB+FzWRLay6AD35Vgp9xoCEL9aJOGaLX1Qg9uucohwZQxKTuvCLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38DoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAphruvg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421498,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAsHpd/md3z2VCF98ADXJOr4y2u0k2g8VawsyeB+FzWRLay6AD35Vgp9xoCEL9aJOGaLX1Qg9uucohwZQxKTuvCLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38DoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAphruvg=="
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAsHpd/md3z2VCF98ADXJOr4y2u0k2g8VawsyeB+FzWRLay6AD35Vgp9xoCEL9aJOGaLX1Qg9uucohwZQxKTuvCLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38DoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAphruvg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421497,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421497,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "balance": 40000000000001
    },
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421496,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421496,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAsHpd/md3z2VCF98ADXJOr4y2u0k2g8VawsyeB+FzWRLay6AD35Vgp9xoCEL9aJOGaLX1Qg9uucohwZQxKTuvCLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38DoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAphruvg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIvKCgEAhiRhOcqAAbDvQAGgLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWLygoBAIY/qiUiX/90EaA0"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421495,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421495,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "balance": 40000000000001
    },
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "meta": 17,
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
        "meta": 17,
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlbdYB5ex+4ZiyLQVJ68kHgjkH1JP1wouGFAndTluA9/BKC//JH/Q/OQjwn7wiLUbXrCipcihyKroL0hinSM1KAodCUaulI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
          "op": "OffChainTransfer",
          "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
  "id": -576460752303421494,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwSgv/yR/0PzkI8J+8Ii1G16woqXIociq6C9IYp0jNSgKHTokQW7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421494,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwSgv/yR/0PzkI8J+8Ii1G16woqXIociq6C9IYp0jNSgKHTokQW7",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
          "op": "OffChainTransfer",
          "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
  "id": -576460752303421493,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA0O0EWlP6f9HWkdULCt+0E4G7K14VZGknT27wOMPXawY+A3wA8EcV74tvdfPPwnZLqAqCaf6jUj8ow+/gQzUPCLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38EoL/8kf9D85CPCfvCItRtesKKlyKHIqugvSGKdIzUoCh0ExosYg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421493,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA0O0EWlP6f9HWkdULCt+0E4G7K14VZGknT27wOMPXawY+A3wA8EcV74tvdfPPwnZLqAqCaf6jUj8ow+/gQzUPCLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38EoL/8kf9D85CPCfvCItRtesKKlyKHIqugvSGKdIzUoCh0ExosYg=="
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA0O0EWlP6f9HWkdULCt+0E4G7K14VZGknT27wOMPXawY+A3wA8EcV74tvdfPPwnZLqAqCaf6jUj8ow+/gQzUPCLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38EoL/8kf9D85CPCfvCItRtesKKlyKHIqugvSGKdIzUoCh0ExosYg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421492,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421492,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "balance": 40000000000000
    },
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421491,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421491,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA0O0EWlP6f9HWkdULCt+0E4G7K14VZGknT27wOMPXawY+A3wA8EcV74tvdfPPwnZLqAqCaf6jUj8ow+/gQzUPCLhI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38EoL/8kf9D85CPCfvCItRtesKKlyKHIqugvSGKdIzUoCh0ExosYg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIvKCgEAhiRhOcqAALDvQAGgLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWLygoBAIY/qiUiYAD8fMaj"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421490,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421490,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "balance": 70000000000000
    },
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
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
    "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
    "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
        "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
    "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
    "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
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
    "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
    "meta": 17,
    "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
        "meta": 17,
        "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
    "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
    "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlbdYB5ex+4ZiyLQVJ68kHgjkH1JP1wouGFAndTluA9/BaChFsgHVUWsFVHDV7FRt9ES30Oqsyeu4uQX0lV3z9ZcgFthNGY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
          "op": "OffChainTransfer",
          "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
  "id": -576460752303421489,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAxxxrE6tSK5CeaCGN7QbO7BeGjiiH7dhNUcM4QBxstaQovohy2c0CqngSENBBA2Hw9o9ZNNHnXUdVsmBYj15sLuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwWgoRbIB1VFrBVRw1exUbfREt9DqrMnruLkF9JVd8/WXICkqVAx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421489,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAxxxrE6tSK5CeaCGN7QbO7BeGjiiH7dhNUcM4QBxstaQovohy2c0CqngSENBBA2Hw9o9ZNNHnXUdVsmBYj15sLuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwWgoRbIB1VFrBVRw1exUbfREt9DqrMnruLkF9JVd8/WXICkqVAx",
      "updates": [
        {
          "amount": 1,
          "from": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
          "op": "OffChainTransfer",
          "to": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
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
  "id": -576460752303421488,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAMccaxOrUiuQnmghje0GzuwXho4oh+3YTVHDOEAcbLWkKL6IctnNAqp4EhDQQQNh8PaPWTTR511HVbJgWI9ebC7hI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38FoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAXSGowA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421488,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAMccaxOrUiuQnmghje0GzuwXho4oh+3YTVHDOEAcbLWkKL6IctnNAqp4EhDQQQNh8PaPWTTR511HVbJgWI9ebC7hI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38FoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAXSGowA=="
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAMccaxOrUiuQnmghje0GzuwXho4oh+3YTVHDOEAcbLWkKL6IctnNAqp4EhDQQQNh8PaPWTTR511HVbJgWI9ebC7hI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38FoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAXSGowA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421487,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421487,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "balance": 69999999999999
    },
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421486,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421486,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAMccaxOrUiuQnmghje0GzuwXho4oh+3YTVHDOEAcbLWkKL6IctnNAqp4EhDQQQNh8PaPWTTR511HVbJgWI9ebC7hI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38FoKEWyAdVRawVUcNXsVG30RLfQ6qzJ67i5BfSVXfP1lyAXSGowA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIvKCgEAhiRhOcqAAbDvQAGgLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWLygoBAIY/qiUiX/90EaA0"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421485,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421485,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "balance": 40000000000001
    },
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "meta": 17,
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
        "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
        "meta": 17,
        "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
    "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
    "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlbdYB5ex+4ZiyLQVJ68kHgjkH1JP1wouGFAndTluA9/BqC//JH/Q/OQjwn7wiLUbXrCipcihyKroL0hinSM1KAodBfkUBY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
          "op": "OffChainTransfer",
          "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
  "id": -576460752303421484,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwagv/yR/0PzkI8J+8Ii1G16woqXIociq6C9IYp0jNSgKHQkLYQx"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421484,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZW3WAeXsfuGYsi0FSevJB4I5B9ST9cKLhhQJ3U5bgPfwagv/yR/0PzkI8J+8Ii1G16woqXIociq6C9IYp0jNSgKHQkLYQx",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
          "op": "OffChainTransfer",
          "to": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
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
  "id": -576460752303421483,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAxJm36D3Y2HFngrY5CfEQSBlh4XESb+5ytlCdfHRbwj5FfZkIFD7BwDx58o8qmcYWJbAGvkpATjDqqrKxDYKOA7hI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38GoL/8kf9D85CPCfvCItRtesKKlyKHIqugvSGKdIzUoCh0fl2ibQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421483,
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAxJm36D3Y2HFngrY5CfEQSBlh4XESb+5ytlCdfHRbwj5FfZkIFD7BwDx58o8qmcYWJbAGvkpATjDqqrKxDYKOA7hI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38GoL/8kf9D85CPCfvCItRtesKKlyKHIqugvSGKdIzUoCh0fl2ibQ=="
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAxJm36D3Y2HFngrY5CfEQSBlh4XESb+5ytlCdfHRbwj5FfZkIFD7BwDx58o8qmcYWJbAGvkpATjDqqrKxDYKOA7hI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38GoL/8kf9D85CPCfvCItRtesKKlyKHIqugvSGKdIzUoCh0fl2ibQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421482,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421482,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kAn5E2MGWLxGrmC7SHXtryAtBoLKCKS5kmxAQXVysMwhjmy8s",
      "balance": 40000000000000
    },
    {
      "account": "ak_MejCQbMkjyeGLGfLNiacmTKAJaNkMeiwDXtWzjWRQcmUJBYpK",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421481,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421481,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAWIE/1qhTEJYJKn24KdHraoDfFcXZUN9MQMqiwrTrfEciSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAxJm36D3Y2HFngrY5CfEQSBlh4XESb+5ytlCdfHRbwj5FfZkIFD7BwDx58o8qmcYWJbAGvkpATjDqqrKxDYKOA7hI+EY5AqEGVt1gHl7H7hmLItBUnryQeCOQfUk/XCi4YUCd1OW4D38GoL/8kf9D85CPCfvCItRtesKKlyKHIqugvSGKdIzUoCh0fl2ibQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBiBP9aoUxCWCSp9uCnR62qA3xXF2VDfTEDKosK063xHIvKCgEAhiRhOcqAALDvQAGgLuOxnKFKuyzLae8smcYiXRJlX66+pk/cAmlFPBWMXhWLygoBAIY/qiUiYAD8fMaj"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421480,
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
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421480,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421479,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
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
    "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fFqvCY5SFxhE7fWVckhjwR1cpgJ7dDYRexANZLhpK51x1DZ5M",
  "id": -576460752303421479,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
