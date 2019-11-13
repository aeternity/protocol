
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW&keep_running=false&lock_period=10&port=13454&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL&role=initiator
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
      "fsm_id": "ba_qoWqeU7YyMUXA3b1Jp5fk5CUJBvZ6swvTqveIFQSJyVny2vl"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW&keep_running=false&lock_period=10&port=13454&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL&role=responder
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
      "fsm_id": "ba_QxNg43+P930ru8k+DVmSuHRlmgGJijEFoZoNbOYptZBUS1oi"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztrhj+qJSJgAKEBKUv/PrybLyyFYNVkZgU15UFyqfEvpJ58TduBWvdBATiGJGE5yoAAAgoAhhAGeddIAMCgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPYARXk5lw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422185,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztrhj+qJSJgAKEBKUv/PrybLyyFYNVkZgU15UFyqfEvpJ58TduBWvdBATiGJGE5yoAAAgoAhhAGeddIAMCgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPYAvtlHkg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422185,
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
      "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztrhj+qJSJgAKEBKUv/PrybLyyFYNVkZgU15UFyqfEvpJ58TduBWvdBATiGJGE5yoAAAgoAhhAGeddIAMCgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPYAvtlHkg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422184,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QGxCwHAuQGr+QGoUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDk2GUwC6JNY9FiC7/wicHcb11Jd/uCfIMoonucGNb2q9VlT77gNLgZwAshAVLfkPvaqvqilrYbKLhdKm/PEPUGuIP4gTIBoQEqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4Y/qiUiYAChASlL/z68my8shWDVZGYFNeVBcqnxL6SefE3bgVr3QQE4hiRhOcqAAAIKAIYQBnnXSADAoBOgXx/x1Itxmu2GA5lZMDmIrcJmB2G91u4TEdd5M6D2ABNWMWQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422184,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDk2GUwC6JNY9FiC7/wicHcb11Jd/uCfIMoonucGNb2q9VlT77gNLgZwAshAVLfkPvaqvqilrYbKLhdKm/PEPUGuIP4gTIBoQEqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4Y/qiUiYAChASlL/z68my8shWDVZGYFNeVBcqnxL6SefE3bgVr3QQE4hiRhOcqAAAIKAIYQBnnXSADAoBOgXx/x1Itxmu2GA5lZMDmIrcJmB2G91u4TEdd5M6D2ABNWMWQ=",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDk2GUwC6JNY9FiC7/wicHcb11Jd/uCfIMoonucGNb2q9VlT77gNLgZwAshAVLfkPvaqvqilrYbKLhdKm/PEPUGuIP4gTIBoQEqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4Y/qiUiYAChASlL/z68my8shWDVZGYFNeVBcqnxL6SefE3bgVr3QQE4hiRhOcqAAAIKAIYQBnnXSADAoBOgXx/x1Itxmu2GA5lZMDmIrcJmB2G91u4TEdd5M6D2ABNWMWQ=",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDk2GUwC6JNY9FiC7/wicHcb11Jd/uCfIMoonucGNb2q9VlT77gNLgZwAshAVLfkPvaqvqilrYbKLhdKm/PEPUGuIP4gTIBoQEqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4Y/qiUiYAChASlL/z68my8shWDVZGYFNeVBcqnxL6SefE3bgVr3QQE4hiRhOcqAAAIKAIYQBnnXSADAoBOgXx/x1Itxmu2GA5lZMDmIrcJmB2G91u4TEdd5M6D2ABNWMWQ=",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDk2GUwC6JNY9FiC7/wicHcb11Jd/uCfIMoonucGNb2q9VlT77gNLgZwAshAVLfkPvaqvqilrYbKLhdKm/PEPUGuIP4gTIBoQEqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4Y/qiUiYAChASlL/z68my8shWDVZGYFNeVBcqnxL6SefE3bgVr3QQE4hiRhOcqAAAIKAIYQBnnXSADAoBOgXx/x1Itxmu2GA5lZMDmIrcJmB2G91u4TEdd5M6D2ABNWMWQ=",
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
    "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "message": {
        "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
        "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
        "info": "Hello",
        "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "message": {
        "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
        "info": "Hello back",
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422183,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422183,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "balance": 69999999999999
    },
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDk2GUwC6JNY9FiC7/wicHcb11Jd/uCfIMoonucGNb2q9VlT77gNLgZwAshAVLfkPvaqvqilrYbKLhdKm/PEPUGuIP4gTIBoQEqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4Y/qiUiYAChASlL/z68my8shWDVZGYFNeVBcqnxL6SefE3bgVr3QQE4hiRhOcqAAAIKAIYQBnnXSADAoBOgXx/x1Itxmu2GA5lZMDmIrcJmB2G91u4TEdd5M6D2ABNWMWQ="
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDk2GUwC6JNY9FiC7/wicHcb11Jd/uCfIMoonucGNb2q9VlT77gNLgZwAshAVLfkPvaqvqilrYbKLhdKm/PEPUGuIP4gTIBoQEqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4Y/qiUiYAChASlL/z68my8shWDVZGYFNeVBcqnxL6SefE3bgVr3QQE4hiRhOcqAAAIKAIYQBnnXSADAoBOgXx/x1Itxmu2GA5lZMDmIrcJmB2G91u4TEdd5M6D2ABNWMWQ="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422182,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422182,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "balance": 69999999999999
    },
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
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
    "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
    "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
        "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
    "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
    "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
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
    "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
    "meta": 17,
    "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
        "meta": 17,
        "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
    "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
    "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhUYqfmjZXf7wgXEMnGCKu/eeQLGw+w40xDMm6UmbVYBAqCsUpQqDVDT27tcWnXE0+JFk4aZlN3H7dQQyrp8LbPCMTjTfS0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
          "op": "OffChainTransfer",
          "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
  "id": -576460752303422181,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhUYqfmjZXf7wgXEMnGCKu/eeQLGw+w40xDMm6UmbVYBAqCsUpQqDVDT27tcWnXE0+JFk4aZlN3H7dQQyrp8LbPCMdU2MEA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422181,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhUYqfmjZXf7wgXEMnGCKu/eeQLGw+w40xDMm6UmbVYBAqCsUpQqDVDT27tcWnXE0+JFk4aZlN3H7dQQyrp8LbPCMdU2MEA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
          "op": "OffChainTransfer",
          "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
  "id": -576460752303422180,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED0icqks2DLZaDeELytVN3qHGq2PtGiji+8e+FvB3pdMiJrBSRLMdsPUVE1I4KdMxFgURyQ4e6uBnDso1n103wPuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQKgrFKUKg1Q09u7XFp1xNPiRZOGmZTdx+3UEMq6fC2zwjGkO3La"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422180,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED0icqks2DLZaDeELytVN3qHGq2PtGiji+8e+FvB3pdMiJrBSRLMdsPUVE1I4KdMxFgURyQ4e6uBnDso1n103wPuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQKgrFKUKg1Q09u7XFp1xNPiRZOGmZTdx+3UEMq6fC2zwjGkO3La"
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED0icqks2DLZaDeELytVN3qHGq2PtGiji+8e+FvB3pdMiJrBSRLMdsPUVE1I4KdMxFgURyQ4e6uBnDso1n103wPuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQKgrFKUKg1Q09u7XFp1xNPiRZOGmZTdx+3UEMq6fC2zwjGkO3La"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422179,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422179,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "balance": 69999999999998
    },
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422178,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422178,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuED0icqks2DLZaDeELytVN3qHGq2PtGiji+8e+FvB3pdMiJrBSRLMdsPUVE1I4KdMxFgURyQ4e6uBnDso1n103wPuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQKgrFKUKg1Q09u7XFp1xNPiRZOGmZTdx+3UEMq6fC2zwjGkO3La",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4vKCgEAhj+qJSJf/rDvQAGgKUv/PrybLyyFYNVkZgU15UFyqfEvpJ58TduBWvdBATiLygoBAIYkYTnKgAKHY2au"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422177,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422177,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "balance": 40000000000002
    },
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "meta": 17,
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
        "meta": 17,
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhUYqfmjZXf7wgXEMnGCKu/eeQLGw+w40xDMm6UmbVYBA6AToF8f8dSLcZrthgOZWTA5iK3CZgdhvdbuExHXeTOg9o7GJes=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
          "op": "OffChainTransfer",
          "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
  "id": -576460752303422176,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECVZkyU2s4WHWPXH+nkZre8RnsFymUXspAehgbij+s4Pa/PP/PvILTJGEH1a7KBKy77/yKv/fvCC4bTMP1HQNIKuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQOgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPbyXw2F"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422176,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+JALAfhCuECVZkyU2s4WHWPXH+nkZre8RnsFymUXspAehgbij+s4Pa/PP/PvILTJGEH1a7KBKy77/yKv/fvCC4bTMP1HQNIKuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQOgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPbyXw2F",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
          "op": "OffChainTransfer",
          "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
  "id": -576460752303422175,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECVZkyU2s4WHWPXH+nkZre8RnsFymUXspAehgbij+s4Pa/PP/PvILTJGEH1a7KBKy77/yKv/fvCC4bTMP1HQNIKuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQOgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPbZKGaS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422175,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECVZkyU2s4WHWPXH+nkZre8RnsFymUXspAehgbij+s4Pa/PP/PvILTJGEH1a7KBKy77/yKv/fvCC4bTMP1HQNIKuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQOgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPbZKGaS"
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECVZkyU2s4WHWPXH+nkZre8RnsFymUXspAehgbij+s4Pa/PP/PvILTJGEH1a7KBKy77/yKv/fvCC4bTMP1HQNIKuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQOgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPbZKGaS"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422174,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422174,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "balance": 40000000000001
    },
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422173,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422173,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECVZkyU2s4WHWPXH+nkZre8RnsFymUXspAehgbij+s4Pa/PP/PvILTJGEH1a7KBKy77/yKv/fvCC4bTMP1HQNIKuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQOgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPbZKGaS",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4vKCgEAhj+qJSJf/7DvQAGgKUv/PrybLyyFYNVkZgU15UFyqfEvpJ58TduBWvdBATiLygoBAIYkYTnKgAEDxRWX"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422172,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422172,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "balance": 40000000000001
    },
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "meta": 17,
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
        "meta": 17,
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhUYqfmjZXf7wgXEMnGCKu/eeQLGw+w40xDMm6UmbVYBBKApnJ3+NixLSkBAK7a7DaE9An2nBLysFOf6qX4R0bq9xfBbyFc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
          "op": "OffChainTransfer",
          "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
  "id": -576460752303422171,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBMjTKjN/Q7RjElxBVv2hM6lrBHnN56oW6hh/N4kj4d2xIPdJ9bPQA+97HaO51KzSL+j9XKXJvs6tIxMQKN+ugOuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQSgKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcV2Hsn6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422171,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBMjTKjN/Q7RjElxBVv2hM6lrBHnN56oW6hh/N4kj4d2xIPdJ9bPQA+97HaO51KzSL+j9XKXJvs6tIxMQKN+ugOuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQSgKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcV2Hsn6",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
          "op": "OffChainTransfer",
          "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
  "id": -576460752303422170,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBMjTKjN/Q7RjElxBVv2hM6lrBHnN56oW6hh/N4kj4d2xIPdJ9bPQA+97HaO51KzSL+j9XKXJvs6tIxMQKN+ugOuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQSgKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcWfrGjt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422170,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBMjTKjN/Q7RjElxBVv2hM6lrBHnN56oW6hh/N4kj4d2xIPdJ9bPQA+97HaO51KzSL+j9XKXJvs6tIxMQKN+ugOuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQSgKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcWfrGjt"
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBMjTKjN/Q7RjElxBVv2hM6lrBHnN56oW6hh/N4kj4d2xIPdJ9bPQA+97HaO51KzSL+j9XKXJvs6tIxMQKN+ugOuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQSgKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcWfrGjt"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422169,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422169,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "balance": 40000000000000
    },
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422168,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422168,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBMjTKjN/Q7RjElxBVv2hM6lrBHnN56oW6hh/N4kj4d2xIPdJ9bPQA+97HaO51KzSL+j9XKXJvs6tIxMQKN+ugOuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQSgKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcWfrGjt",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4vKCgEAhj+qJSJgALDvQAGgKUv/PrybLyyFYNVkZgU15UFyqfEvpJ58TduBWvdBATiLygoBAIYkYTnKgADqPdbf"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422167,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422167,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "balance": 70000000000000
    },
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
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
    "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
    "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
        "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
    "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
    "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
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
    "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
    "meta": 17,
    "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
        "meta": 17,
        "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
    "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
    "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhUYqfmjZXf7wgXEMnGCKu/eeQLGw+w40xDMm6UmbVYBBaAToF8f8dSLcZrthgOZWTA5iK3CZgdhvdbuExHXeTOg9iL4SgU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
          "op": "OffChainTransfer",
          "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
  "id": -576460752303422166,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhUYqfmjZXf7wgXEMnGCKu/eeQLGw+w40xDMm6UmbVYBBaAToF8f8dSLcZrthgOZWTA5iK3CZgdhvdbuExHXeTOg9sNT2is="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422166,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhUYqfmjZXf7wgXEMnGCKu/eeQLGw+w40xDMm6UmbVYBBaAToF8f8dSLcZrthgOZWTA5iK3CZgdhvdbuExHXeTOg9sNT2is=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
          "op": "OffChainTransfer",
          "to": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
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
  "id": -576460752303422165,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAbUmbp5drhnpehFgvkajk9k4JXonpfgSZSqUbY+DALdXSk1mSOO3vidUjAhOwNpcViFLM+RNoTq3YtWSDKkYAIuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQWgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPZT9oII"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422165,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAbUmbp5drhnpehFgvkajk9k4JXonpfgSZSqUbY+DALdXSk1mSOO3vidUjAhOwNpcViFLM+RNoTq3YtWSDKkYAIuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQWgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPZT9oII"
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAbUmbp5drhnpehFgvkajk9k4JXonpfgSZSqUbY+DALdXSk1mSOO3vidUjAhOwNpcViFLM+RNoTq3YtWSDKkYAIuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQWgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPZT9oII"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422164,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422164,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "balance": 69999999999999
    },
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422163,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422163,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAbUmbp5drhnpehFgvkajk9k4JXonpfgSZSqUbY+DALdXSk1mSOO3vidUjAhOwNpcViFLM+RNoTq3YtWSDKkYAIuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQWgE6BfH/HUi3Ga7YYDmVkwOYitwmYHYb3W7hMR13kzoPZT9oII",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4vKCgEAhj+qJSJf/7DvQAGgKUv/PrybLyyFYNVkZgU15UFyqfEvpJ58TduBWvdBATiLygoBAIYkYTnKgAEDxRWX"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422162,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422162,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "balance": 40000000000001
    },
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "meta": 17,
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
        "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
        "meta": 17,
        "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
    "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
    "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhUYqfmjZXf7wgXEMnGCKu/eeQLGw+w40xDMm6UmbVYBBqApnJ3+NixLSkBAK7a7DaE9An2nBLysFOf6qX4R0bq9xTBV7l4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
          "op": "OffChainTransfer",
          "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
  "id": -576460752303422161,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECmNAAfBI+pOQ7um0QgXPuNCOtaYZghRQf0yE0L0dMAgLbbuC/ntTVY78sJbLeuZLh9rNUQlUMRdZxjuoUVrnEJuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQagKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcWEYUl6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422161,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "signed_tx": "tx_+JALAfhCuECmNAAfBI+pOQ7um0QgXPuNCOtaYZghRQf0yE0L0dMAgLbbuC/ntTVY78sJbLeuZLh9rNUQlUMRdZxjuoUVrnEJuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQagKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcWEYUl6",
      "updates": [
        {
          "amount": 1,
          "from": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
          "op": "OffChainTransfer",
          "to": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
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
  "id": -576460752303422160,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECmNAAfBI+pOQ7um0QgXPuNCOtaYZghRQf0yE0L0dMAgLbbuC/ntTVY78sJbLeuZLh9rNUQlUMRdZxjuoUVrnEJuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQagKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcUb6nxH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422160,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECmNAAfBI+pOQ7um0QgXPuNCOtaYZghRQf0yE0L0dMAgLbbuC/ntTVY78sJbLeuZLh9rNUQlUMRdZxjuoUVrnEJuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQagKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcUb6nxH"
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECmNAAfBI+pOQ7um0QgXPuNCOtaYZghRQf0yE0L0dMAgLbbuC/ntTVY78sJbLeuZLh9rNUQlUMRdZxjuoUVrnEJuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQagKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcUb6nxH"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422159,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422159,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KBsdcHZqPbe9mNRkFfcBzojDGRbN298GRXKFZyEXhyAZ3JrzL",
      "balance": 40000000000000
    },
    {
      "account": "ak_KehgXRpZnGnD4hrh8LcNf6epRGzdhamWm6K7tM7X3nJGqNZJW",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422158,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422158,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhASpY35Nfk9yla1Pxys1yKZ1PIMiU6cstzwJZTeYfuztruKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECmNAAfBI+pOQ7um0QgXPuNCOtaYZghRQf0yE0L0dMAgLbbuC/ntTVY78sJbLeuZLh9rNUQlUMRdZxjuoUVrnEJuEj4RjkCoQYVGKn5o2V3+8IFxDJxgirv3nkCxsPsONMQzJulJm1WAQagKZyd/jYsS0pAQCu2uw2hPQJ9pwS8rBTn+ql+EdG6vcUb6nxH",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAqWN+TX5PcpWtT8crNcimdTyDIlOnLLc8CWU3mH7s7a4vKCgEAhj+qJSJgALDvQAGgKUv/PrybLyyFYNVkZgU15UFyqfEvpJ58TduBWvdBATiLygoBAIYkYTnKgADqPdbf"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422157,
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
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422157,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422156,
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
    "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
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
  "channel_id": "ch_AHsus4qfShGTEk5uCxFoSQiqZbbop3kKRiGJmxPsqC5XDqk65",
  "id": -576460752303422156,
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
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH&keep_running=false&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG&role=initiator
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
      "fsm_id": "ba_nHJyJXsadXweoOuz45KVI1lSL3GqgSaSYmNi1NuoZITPKHH5"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH&keep_running=false&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG&role=responder
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
      "fsm_id": "ba_1wCM4nX/9jSoMG/m8tGB32We9OVlAvKhptMdjVe2vQQ80qqQ"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaChj+qJSJgAKEBpao6Rdn5uqn3UvVCqDBI0ttHBGdKU8/f3l1DaD4JXxCGJGE5yoAAAgoAhhAGeddIAMCgJgBmv/qcC3IAUbsli5I9l0xn9IVODTcoabE8f6zvKJoApjlOHw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421538,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+NQLAcC4z/jNUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQE2kca/fsJ+hwPk7BOgSAG5L1u6W9tlTPAoEaAjvyC2goY/qiUiYAChAaWqOkXZ+bqp91L1QqgwSNLbRwRnSlPP395dQ2g+CV8QhiRhOcqAAAIKAIYQBnnXSADAoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaAKsUBvY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421538,
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
      "signed_tx": "tx_+NQLAcC4z/jNUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQE2kca/fsJ+hwPk7BOgSAG5L1u6W9tlTPAoEaAjvyC2goY/qiUiYAChAaWqOkXZ+bqp91L1QqgwSNLbRwRnSlPP395dQ2g+CV8QhiRhOcqAAAIKAIYQBnnXSADAoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaAKsUBvY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421537,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAS8iI8EDiMYlt8YHE2mBPn3Ed/K+BOanXSDnaHeM73EacLuMBdMTwZsA3T13kXrn7TqpY70c7sN82blBSSR3vALiD+IEyAaEBNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKGP6olImAAoQGlqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIYkYTnKgAACCgCGEAZ510gAwKAmAGa/+pwLcgBRuyWLkj2XTGf0hU4NNyhpsTx/rO8omgCLqqAJ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421537,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAS8iI8EDiMYlt8YHE2mBPn3Ed/K+BOanXSDnaHeM73EacLuMBdMTwZsA3T13kXrn7TqpY70c7sN82blBSSR3vALiD+IEyAaEBNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKGP6olImAAoQGlqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIYkYTnKgAACCgCGEAZ510gAwKAmAGa/+pwLcgBRuyWLkj2XTGf0hU4NNyhpsTx/rO8omgCLqqAJ",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAS8iI8EDiMYlt8YHE2mBPn3Ed/K+BOanXSDnaHeM73EacLuMBdMTwZsA3T13kXrn7TqpY70c7sN82blBSSR3vALiD+IEyAaEBNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKGP6olImAAoQGlqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIYkYTnKgAACCgCGEAZ510gAwKAmAGa/+pwLcgBRuyWLkj2XTGf0hU4NNyhpsTx/rO8omgCLqqAJ",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAS8iI8EDiMYlt8YHE2mBPn3Ed/K+BOanXSDnaHeM73EacLuMBdMTwZsA3T13kXrn7TqpY70c7sN82blBSSR3vALiD+IEyAaEBNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKGP6olImAAoQGlqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIYkYTnKgAACCgCGEAZ510gAwKAmAGa/+pwLcgBRuyWLkj2XTGf0hU4NNyhpsTx/rO8omgCLqqAJ",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAS8iI8EDiMYlt8YHE2mBPn3Ed/K+BOanXSDnaHeM73EacLuMBdMTwZsA3T13kXrn7TqpY70c7sN82blBSSR3vALiD+IEyAaEBNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKGP6olImAAoQGlqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIYkYTnKgAACCgCGEAZ510gAwKAmAGa/+pwLcgBRuyWLkj2XTGf0hU4NNyhpsTx/rO8omgCLqqAJ",
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
    "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "message": {
        "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
        "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
        "info": "Hello",
        "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "message": {
        "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
        "info": "Hello back",
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421536,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421536,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "balance": 69999999999999
    },
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAS8iI8EDiMYlt8YHE2mBPn3Ed/K+BOanXSDnaHeM73EacLuMBdMTwZsA3T13kXrn7TqpY70c7sN82blBSSR3vALiD+IEyAaEBNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKGP6olImAAoQGlqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIYkYTnKgAACCgCGEAZ510gAwKAmAGa/+pwLcgBRuyWLkj2XTGf0hU4NNyhpsTx/rO8omgCLqqAJ"
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAS8iI8EDiMYlt8YHE2mBPn3Ed/K+BOanXSDnaHeM73EacLuMBdMTwZsA3T13kXrn7TqpY70c7sN82blBSSR3vALiD+IEyAaEBNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKGP6olImAAoQGlqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIYkYTnKgAACCgCGEAZ510gAwKAmAGa/+pwLcgBRuyWLkj2XTGf0hU4NNyhpsTx/rO8omgCLqqAJ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421535,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421535,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "balance": 69999999999999
    },
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
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
    "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
    "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
        "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
    "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
    "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
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
    "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
    "meta": 17,
    "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
        "meta": 17,
        "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
    "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
    "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBndZQ9R3dKMLuWcXaWOySmowD9VqWTOiYvPxtjbODRR9AqD6ANMB05l3fqjPMhVeE5ok3/us1RzQM1DVSFO9Li2fNSZ+HtE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
          "op": "OffChainTransfer",
          "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
  "id": -576460752303421534,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQKg+gDTAdOZd36ozzIVXhOaJN/7rNUc0DNQ1UhTvS4tnzVw31AE"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421534,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQKg+gDTAdOZd36ozzIVXhOaJN/7rNUc0DNQ1UhTvS4tnzVw31AE",
      "updates": [
        {
          "amount": 1,
          "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
          "op": "OffChainTransfer",
          "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
  "id": -576460752303421533,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAKaRTJ2B2IWxOO9draoUsTbKphsmlX8v5Fy0KWjKWPiaajcJBXqHMO/i38ad5ttUU7G0dRkazSflFDb1dJRJwCrhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0CoPoA0wHTmXd+qM8yFV4TmiTf+6zVHNAzUNVIU70uLZ8192VjGw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421533,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAKaRTJ2B2IWxOO9draoUsTbKphsmlX8v5Fy0KWjKWPiaajcJBXqHMO/i38ad5ttUU7G0dRkazSflFDb1dJRJwCrhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0CoPoA0wHTmXd+qM8yFV4TmiTf+6zVHNAzUNVIU70uLZ8192VjGw=="
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAKaRTJ2B2IWxOO9draoUsTbKphsmlX8v5Fy0KWjKWPiaajcJBXqHMO/i38ad5ttUU7G0dRkazSflFDb1dJRJwCrhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0CoPoA0wHTmXd+qM8yFV4TmiTf+6zVHNAzUNVIU70uLZ8192VjGw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421532,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421532,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "balance": 69999999999998
    },
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421531,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421531,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAKaRTJ2B2IWxOO9draoUsTbKphsmlX8v5Fy0KWjKWPiaajcJBXqHMO/i38ad5ttUU7G0dRkazSflFDb1dJRJwCrhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0CoPoA0wHTmXd+qM8yFV4TmiTf+6zVHNAzUNVIU70uLZ8192VjGw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIvKCgEAhiRhOcqAArDvQAGgNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKLygoBAIY/qiUiX/7i/96f"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421530,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421530,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "balance": 40000000000002
    },
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "meta": 17,
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
        "meta": 17,
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBndZQ9R3dKMLuWcXaWOySmowD9VqWTOiYvPxtjbODRR9A6AmAGa/+pwLcgBRuyWLkj2XTGf0hU4NNyhpsTx/rO8omt6z4lo=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
          "op": "OffChainTransfer",
          "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
  "id": -576460752303421529,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAt2gcwL0XOeIIiTK8yMVTv3ZqNi8dOidS32LFtZRA2/K/pvKSmr7vAfORzeNPSzF/zYUAk9IZVgnyudtDEplIJuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQOgJgBmv/qcC3IAUbsli5I9l0xn9IVODTcoabE8f6zvKJpNGBlc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421529,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAt2gcwL0XOeIIiTK8yMVTv3ZqNi8dOidS32LFtZRA2/K/pvKSmr7vAfORzeNPSzF/zYUAk9IZVgnyudtDEplIJuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQOgJgBmv/qcC3IAUbsli5I9l0xn9IVODTcoabE8f6zvKJpNGBlc",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
          "op": "OffChainTransfer",
          "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
  "id": -576460752303421528,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhALdoHMC9FzniCIkyvMjFU792ajYvHTonUt9ixbWUQNvyv6bykpq+7wHzkc3jT0sxf82FAJPSGVYJ8rnbQxKZSCbhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0DoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaNss1Lw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421528,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhALdoHMC9FzniCIkyvMjFU792ajYvHTonUt9ixbWUQNvyv6bykpq+7wHzkc3jT0sxf82FAJPSGVYJ8rnbQxKZSCbhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0DoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaNss1Lw=="
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhALdoHMC9FzniCIkyvMjFU792ajYvHTonUt9ixbWUQNvyv6bykpq+7wHzkc3jT0sxf82FAJPSGVYJ8rnbQxKZSCbhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0DoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaNss1Lw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421527,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421527,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "balance": 40000000000001
    },
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421526,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421526,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhALdoHMC9FzniCIkyvMjFU792ajYvHTonUt9ixbWUQNvyv6bykpq+7wHzkc3jT0sxf82FAJPSGVYJ8rnbQxKZSCbhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0DoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaNss1Lw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIvKCgEAhiRhOcqAAbDvQAGgNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKLygoBAIY/qiUiX/8fkadJ"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421525,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421525,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "balance": 40000000000001
    },
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "meta": 17,
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
        "meta": 17,
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBndZQ9R3dKMLuWcXaWOySmowD9VqWTOiYvPxtjbODRR9BKAwDxGjAmI9N3AMDDNJtpb+679FVDUpsgXccmiIS4CbKS3bTSU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
          "op": "OffChainTransfer",
          "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
  "id": -576460752303421524,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDfTINE+gSYfjmvgSmMQw3JgSpZpGgx5jBkxswLwmoXd8cTA6m5goE4JLEuJ7q1ThfaAZT0YndA6h3jHCuJVfYHuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQSgMA8RowJiPTdwDAwzSbaW/uu/RVQ1KbIF3HJoiEuAmykBWBxy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421524,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDfTINE+gSYfjmvgSmMQw3JgSpZpGgx5jBkxswLwmoXd8cTA6m5goE4JLEuJ7q1ThfaAZT0YndA6h3jHCuJVfYHuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQSgMA8RowJiPTdwDAwzSbaW/uu/RVQ1KbIF3HJoiEuAmykBWBxy",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
          "op": "OffChainTransfer",
          "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
  "id": -576460752303421523,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA30yDRPoEmH45r4EpjEMNyYEqWaRoMeYwZMbMC8JqF3fHEwOpuYKBOCSxLie6tU4X2gGU9GJ3QOod4xwriVX2B7hI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0EoDAPEaMCYj03cAwMM0m2lv7rv0VUNSmyBdxyaIhLgJspKWmBYQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421523,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA30yDRPoEmH45r4EpjEMNyYEqWaRoMeYwZMbMC8JqF3fHEwOpuYKBOCSxLie6tU4X2gGU9GJ3QOod4xwriVX2B7hI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0EoDAPEaMCYj03cAwMM0m2lv7rv0VUNSmyBdxyaIhLgJspKWmBYQ=="
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA30yDRPoEmH45r4EpjEMNyYEqWaRoMeYwZMbMC8JqF3fHEwOpuYKBOCSxLie6tU4X2gGU9GJ3QOod4xwriVX2B7hI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0EoDAPEaMCYj03cAwMM0m2lv7rv0VUNSmyBdxyaIhLgJspKWmBYQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421522,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421522,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "balance": 40000000000000
    },
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421521,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421521,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA30yDRPoEmH45r4EpjEMNyYEqWaRoMeYwZMbMC8JqF3fHEwOpuYKBOCSxLie6tU4X2gGU9GJ3QOod4xwriVX2B7hI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0EoDAPEaMCYj03cAwMM0m2lv7rv0VUNSmyBdxyaIhLgJspKWmBYQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIvKCgEAhiRhOcqAALDvQAGgNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKLygoBAIY/qiUiYABSd7Yv"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421520,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421520,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "balance": 70000000000000
    },
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
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
    "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
    "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
        "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
    "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
    "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
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
    "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
    "meta": 17,
    "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
        "meta": 17,
        "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
    "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
    "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBndZQ9R3dKMLuWcXaWOySmowD9VqWTOiYvPxtjbODRR9BaAmAGa/+pwLcgBRuyWLkj2XTGf0hU4NNyhpsTx/rO8ompClLiA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
          "op": "OffChainTransfer",
          "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
  "id": -576460752303421519,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQWgJgBmv/qcC3IAUbsli5I9l0xn9IVODTcoabE8f6zvKJpC69Ml"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421519,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQWgJgBmv/qcC3IAUbsli5I9l0xn9IVODTcoabE8f6zvKJpC69Ml",
      "updates": [
        {
          "amount": 1,
          "from": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
          "op": "OffChainTransfer",
          "to": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
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
  "id": -576460752303421518,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAhsbzpy3Bqo9n/uq7qRcRJ5mdsrWF1pHbwOQgQV7HlKACmIvORwwVkui7VQrIpY8NXViDD/6MPjcI8PGsEevtDLhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0FoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaav38eg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421518,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAhsbzpy3Bqo9n/uq7qRcRJ5mdsrWF1pHbwOQgQV7HlKACmIvORwwVkui7VQrIpY8NXViDD/6MPjcI8PGsEevtDLhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0FoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaav38eg=="
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAhsbzpy3Bqo9n/uq7qRcRJ5mdsrWF1pHbwOQgQV7HlKACmIvORwwVkui7VQrIpY8NXViDD/6MPjcI8PGsEevtDLhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0FoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaav38eg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421517,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421517,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "balance": 69999999999999
    },
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421516,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421516,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAhsbzpy3Bqo9n/uq7qRcRJ5mdsrWF1pHbwOQgQV7HlKACmIvORwwVkui7VQrIpY8NXViDD/6MPjcI8PGsEevtDLhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0FoCYAZr/6nAtyAFG7JYuSPZdMZ/SFTg03KGmxPH+s7yiaav38eg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIvKCgEAhiRhOcqAAbDvQAGgNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKLygoBAIY/qiUiX/8fkadJ"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421515,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421515,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "balance": 40000000000001
    },
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "meta": 17,
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
        "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
        "meta": 17,
        "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
    "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
    "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBndZQ9R3dKMLuWcXaWOySmowD9VqWTOiYvPxtjbODRR9BqAwDxGjAmI9N3AMDDNJtpb+679FVDUpsgXccmiIS4CbKahnIzI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
          "op": "OffChainTransfer",
          "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
  "id": -576460752303421514,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDDjyyBd8tsgG5xF4gWuCObcSrr9VJM1saCl+fMkn5sPK/WV+gqRhOUddfuhGHHxABH10sNJijd1XWk4rMbsmMBuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQagMA8RowJiPTdwDAwzSbaW/uu/RVQ1KbIF3HJoiEuAmynlcSiD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421514,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDDjyyBd8tsgG5xF4gWuCObcSrr9VJM1saCl+fMkn5sPK/WV+gqRhOUddfuhGHHxABH10sNJijd1XWk4rMbsmMBuEj4RjkCoQZ3WUPUd3SjC7lnF2ljskpqMA/ValkzomLz8bY2zg0UfQagMA8RowJiPTdwDAwzSbaW/uu/RVQ1KbIF3HJoiEuAmynlcSiD",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
          "op": "OffChainTransfer",
          "to": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
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
  "id": -576460752303421513,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAw48sgXfLbIBucReIFrgjm3Eq6/VSTNbGgpfnzJJ+bDyv1lfoKkYTlHXX7oRhx8QAR9dLDSYo3dV1pOKzG7JjAbhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0GoDAPEaMCYj03cAwMM0m2lv7rv0VUNSmyBdxyaIhLgJspoeBNbg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421513,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAw48sgXfLbIBucReIFrgjm3Eq6/VSTNbGgpfnzJJ+bDyv1lfoKkYTlHXX7oRhx8QAR9dLDSYo3dV1pOKzG7JjAbhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0GoDAPEaMCYj03cAwMM0m2lv7rv0VUNSmyBdxyaIhLgJspoeBNbg=="
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAw48sgXfLbIBucReIFrgjm3Eq6/VSTNbGgpfnzJJ+bDyv1lfoKkYTlHXX7oRhx8QAR9dLDSYo3dV1pOKzG7JjAbhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0GoDAPEaMCYj03cAwMM0m2lv7rv0VUNSmyBdxyaIhLgJspoeBNbg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421512,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421512,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2FxgxGrHqkk2s7eDPwpaWWaNdhmwAj1aUdoj5qiAy6qGCjuAGG",
      "balance": 40000000000000
    },
    {
      "account": "ak_R2uNx8rGW3S8zZSGcnji8cEmrMVuDpXuE6DjsT4TTCHMMTQxH",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421511,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421511,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhATaRxr9+wn6HA+TsE6BIAbkvW7pb22VM8CgRoCO/ILaCiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAw48sgXfLbIBucReIFrgjm3Eq6/VSTNbGgpfnzJJ+bDyv1lfoKkYTlHXX7oRhx8QAR9dLDSYo3dV1pOKzG7JjAbhI+EY5AqEGd1lD1Hd0owu5ZxdpY7JKajAP1WpZM6Ji8/G2Ns4NFH0GoDAPEaMCYj03cAwMM0m2lv7rv0VUNSmyBdxyaIhLgJspoeBNbg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClqjpF2fm6qfdS9UKoMEjS20cEZ0pTz9/eXUNoPglfEIvKCgEAhiRhOcqAALDvQAGgNpHGv37CfocD5OwToEgBuS9bulvbZUzwKBGgI78gtoKLygoBAIY/qiUiYABSd7Yv"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421510,
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
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421510,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421509,
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
    "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
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
  "channel_id": "ch_uZbvaoEXXz8bQ2EAYm3ZCqbhSAKZGGUXwXRDDUtT37ggYWbHu",
  "id": -576460752303421509,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
