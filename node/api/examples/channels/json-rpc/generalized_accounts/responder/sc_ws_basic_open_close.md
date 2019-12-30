
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve&keep_running=false&lock_period=10&port=13079&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u&role=initiator
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
      "fsm_id": "ba_kMVveOOH9mXXHVrOMQM2GjP55mrPCSdnSeGT3u1wSHtw4CQ9"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve&keep_running=false&lock_period=10&port=13079&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u&role=responder
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
      "fsm_id": "ba_fcPc4yMcJUBqCuk7yvaBr+aYV6np+qH8ZYrOuVCv5zfYnET7"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAQMCjb8okBePkq6Cb1gLMA7CVdgncpTPFw43611YM4mhhj+qJSJgAKEBLYGadt4XJO0Ezmmi0VEd5t61oyZZXd7l1WhoPLd1aaKGJGE5yoAAAgoAhhAGeddIAMCg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBEB6FiNqg==",
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
    "signed_tx": "tx_+MsLAfhCuEBpJgMr0PfE9N900DK+H8+qB+jtfyr0TcG6r3MMHYGm/SM1mk/FFc3ECPdjQ65a4s9O/T4JTc2G5ZdprvX7TsgJuIP4gTIBoQEDAo2/KJAXj5Kugm9YCzAOwlXYJ3KUzxcON+tdWDOJoYY/qiUiYAChAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmihiRhOcqAAAIKAIYQBnnXSADAoPWWlo9LlF3I/ovM6GYlW1sWTVNEbvFn2TWdKvvkMqARATdupmg="
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
      "signed_tx": "tx_+MsLAfhCuEBpJgMr0PfE9N900DK+H8+qB+jtfyr0TcG6r3MMHYGm/SM1mk/FFc3ECPdjQ65a4s9O/T4JTc2G5ZdprvX7TsgJuIP4gTIBoQEDAo2/KJAXj5Kugm9YCzAOwlXYJ3KUzxcON+tdWDOJoYY/qiUiYAChAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmihiRhOcqAAAIKAIYQBnnXSADAoPWWlo9LlF3I/ovM6GYlW1sWTVNEbvFn2TWdKvvkMqARATdupmg=",
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
    "signed_tx": "tx_+QGxCwHAuQGr+QGoUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBpJgMr0PfE9N900DK+H8+qB+jtfyr0TcG6r3MMHYGm/SM1mk/FFc3ECPdjQ65a4s9O/T4JTc2G5ZdprvX7TsgJuIP4gTIBoQEDAo2/KJAXj5Kugm9YCzAOwlXYJ3KUzxcON+tdWDOJoYY/qiUiYAChAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmihiRhOcqAAAIKAIYQBnnXSADAoPWWlo9LlF3I/ovM6GYlW1sWTVNEbvFn2TWdKvvkMqARAap4lXg="
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBpJgMr0PfE9N900DK+H8+qB+jtfyr0TcG6r3MMHYGm/SM1mk/FFc3ECPdjQ65a4s9O/T4JTc2G5ZdprvX7TsgJuIP4gTIBoQEDAo2/KJAXj5Kugm9YCzAOwlXYJ3KUzxcON+tdWDOJoYY/qiUiYAChAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmihiRhOcqAAAIKAIYQBnnXSADAoPWWlo9LlF3I/ovM6GYlW1sWTVNEbvFn2TWdKvvkMqARAap4lXg=",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBpJgMr0PfE9N900DK+H8+qB+jtfyr0TcG6r3MMHYGm/SM1mk/FFc3ECPdjQ65a4s9O/T4JTc2G5ZdprvX7TsgJuIP4gTIBoQEDAo2/KJAXj5Kugm9YCzAOwlXYJ3KUzxcON+tdWDOJoYY/qiUiYAChAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmihiRhOcqAAAIKAIYQBnnXSADAoPWWlo9LlF3I/ovM6GYlW1sWTVNEbvFn2TWdKvvkMqARAap4lXg=",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBpJgMr0PfE9N900DK+H8+qB+jtfyr0TcG6r3MMHYGm/SM1mk/FFc3ECPdjQ65a4s9O/T4JTc2G5ZdprvX7TsgJuIP4gTIBoQEDAo2/KJAXj5Kugm9YCzAOwlXYJ3KUzxcON+tdWDOJoYY/qiUiYAChAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmihiRhOcqAAAIKAIYQBnnXSADAoPWWlo9LlF3I/ovM6GYlW1sWTVNEbvFn2TWdKvvkMqARAap4lXg=",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBpJgMr0PfE9N900DK+H8+qB+jtfyr0TcG6r3MMHYGm/SM1mk/FFc3ECPdjQ65a4s9O/T4JTc2G5ZdprvX7TsgJuIP4gTIBoQEDAo2/KJAXj5Kugm9YCzAOwlXYJ3KUzxcON+tdWDOJoYY/qiUiYAChAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmihiRhOcqAAAIKAIYQBnnXSADAoPWWlo9LlF3I/ovM6GYlW1sWTVNEbvFn2TWdKvvkMqARAap4lXg=",
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
    "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "message": {
        "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
        "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
        "info": "Hello",
        "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "message": {
        "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
        "info": "Hello back",
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422153,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "balance": 69999999999999
    },
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBpJgMr0PfE9N900DK+H8+qB+jtfyr0TcG6r3MMHYGm/SM1mk/FFc3ECPdjQ65a4s9O/T4JTc2G5ZdprvX7TsgJuIP4gTIBoQEDAo2/KJAXj5Kugm9YCzAOwlXYJ3KUzxcON+tdWDOJoYY/qiUiYAChAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmihiRhOcqAAAIKAIYQBnnXSADAoPWWlo9LlF3I/ovM6GYlW1sWTVNEbvFn2TWdKvvkMqARAap4lXg="
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBpJgMr0PfE9N900DK+H8+qB+jtfyr0TcG6r3MMHYGm/SM1mk/FFc3ECPdjQ65a4s9O/T4JTc2G5ZdprvX7TsgJuIP4gTIBoQEDAo2/KJAXj5Kugm9YCzAOwlXYJ3KUzxcON+tdWDOJoYY/qiUiYAChAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmihiRhOcqAAAIKAIYQBnnXSADAoPWWlo9LlF3I/ovM6GYlW1sWTVNEbvFn2TWdKvvkMqARAap4lXg="
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
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422152,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "balance": 69999999999999
    },
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
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
    "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
    "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
        "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
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
    "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
    "meta": 17,
    "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
        "meta": 17,
        "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
    "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oAqAr3bWvG9+DYg/T08Fdig/eThN6Kb3ynXPSiVQdqbeXaohdOPI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
          "op": "OffChainTransfer",
          "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "signed_tx": "tx_+JALAfhCuEDFz4uSFLERcuJ/IQBg+AH1erK+M8P+6jewYYPN9PFzUWeURxWJM1hfpuS13fRklfML9OHbEASMKFoIWEyCiL0KuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAKgK921rxvfg2IP09PBXYoP3k4Teim98p1z0olUHam3l2paq4NL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDFz4uSFLERcuJ/IQBg+AH1erK+M8P+6jewYYPN9PFzUWeURxWJM1hfpuS13fRklfML9OHbEASMKFoIWEyCiL0KuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAKgK921rxvfg2IP09PBXYoP3k4Teim98p1z0olUHam3l2paq4NL",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
          "op": "OffChainTransfer",
          "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDFz4uSFLERcuJ/IQBg+AH1erK+M8P+6jewYYPN9PFzUWeURxWJM1hfpuS13fRklfML9OHbEASMKFoIWEyCiL0KuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAKgK921rxvfg2IP09PBXYoP3k4Teim98p1z0olUHam3l2r7Qdo/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDFz4uSFLERcuJ/IQBg+AH1erK+M8P+6jewYYPN9PFzUWeURxWJM1hfpuS13fRklfML9OHbEASMKFoIWEyCiL0KuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAKgK921rxvfg2IP09PBXYoP3k4Teim98p1z0olUHam3l2r7Qdo/"
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDFz4uSFLERcuJ/IQBg+AH1erK+M8P+6jewYYPN9PFzUWeURxWJM1hfpuS13fRklfML9OHbEASMKFoIWEyCiL0KuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAKgK921rxvfg2IP09PBXYoP3k4Teim98p1z0olUHam3l2r7Qdo/"
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
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422149,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "balance": 69999999999998
    },
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
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
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422148,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDFz4uSFLERcuJ/IQBg+AH1erK+M8P+6jewYYPN9PFzUWeURxWJM1hfpuS13fRklfML9OHbEASMKFoIWEyCiL0KuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAKgK921rxvfg2IP09PBXYoP3k4Teim98p1z0olUHam3l2r7Qdo/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAtgZp23hck7QTOaaLRUR3m3rWjJlld3uXVaGg8t3VpoovKCgEAhiRhOcqAArDvQAGgAwKNvyiQF4+SroJvWAswDsJV2CdylM8XDjfrXVgziaGLygoBAIY/qiUiX/6LYF69"
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
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422147,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "balance": 40000000000002
    },
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "meta": 17,
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
        "meta": 17,
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oA6D1lpaPS5RdyP6LzOhmJVtbFk1TRG7xZ9k1nSr75DKgEarDwXM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
          "op": "OffChainTransfer",
          "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oA6D1lpaPS5RdyP6LzOhmJVtbFk1TRG7xZ9k1nSr75DKgEbaagqA="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oA6D1lpaPS5RdyP6LzOhmJVtbFk1TRG7xZ9k1nSr75DKgEbaagqA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
          "op": "OffChainTransfer",
          "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECPXnsnSt9Y/Uw66KXVMo8uXGKhhPHi+oJWv2mhuROQLo0h+X29D2vV1B60Em/ZXE30fzVtmm3ImawYclf+wQUIuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAOg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBFNFjJP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECPXnsnSt9Y/Uw66KXVMo8uXGKhhPHi+oJWv2mhuROQLo0h+X29D2vV1B60Em/ZXE30fzVtmm3ImawYclf+wQUIuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAOg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBFNFjJP"
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECPXnsnSt9Y/Uw66KXVMo8uXGKhhPHi+oJWv2mhuROQLo0h+X29D2vV1B60Em/ZXE30fzVtmm3ImawYclf+wQUIuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAOg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBFNFjJP"
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
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422144,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "balance": 40000000000001
    },
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
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
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422143,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECPXnsnSt9Y/Uw66KXVMo8uXGKhhPHi+oJWv2mhuROQLo0h+X29D2vV1B60Em/ZXE30fzVtmm3ImawYclf+wQUIuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAOg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBFNFjJP",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAtgZp23hck7QTOaaLRUR3m3rWjJlld3uXVaGg8t3VpoovKCgEAhiRhOcqAAbDvQAGgAwKNvyiQF4+SroJvWAswDsJV2CdylM8XDjfrXVgziaGLygoBAIY/qiUiX/9e8HGQ"
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
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422142,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "balance": 40000000000001
    },
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "meta": 17,
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
        "meta": 17,
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oBKBlO0D+GU+DLJv01mt7IqVZ591gdUJvP7xxeQh6hw3EFdoSvSg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
          "op": "OffChainTransfer",
          "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oBKBlO0D+GU+DLJv01mt7IqVZ591gdUJvP7xxeQh6hw3EFWa/+Q0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oBKBlO0D+GU+DLJv01mt7IqVZ591gdUJvP7xxeQh6hw3EFWa/+Q0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
          "op": "OffChainTransfer",
          "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAmFPmEsnewkhDZKI69WV0lDQzvMZphrBeX8OqgVvx2Yf4kuPb1Z0lHsMDENBlXtOtZRV30+DQdQzoAnhICqIsAuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqASgZTtA/hlPgyyb9NZreyKlWefdYHVCbz+8cXkIeocNxBVw0vmg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAmFPmEsnewkhDZKI69WV0lDQzvMZphrBeX8OqgVvx2Yf4kuPb1Z0lHsMDENBlXtOtZRV30+DQdQzoAnhICqIsAuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqASgZTtA/hlPgyyb9NZreyKlWefdYHVCbz+8cXkIeocNxBVw0vmg"
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAmFPmEsnewkhDZKI69WV0lDQzvMZphrBeX8OqgVvx2Yf4kuPb1Z0lHsMDENBlXtOtZRV30+DQdQzoAnhICqIsAuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqASgZTtA/hlPgyyb9NZreyKlWefdYHVCbz+8cXkIeocNxBVw0vmg"
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
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422139,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "balance": 40000000000000
    },
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
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
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422138,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAmFPmEsnewkhDZKI69WV0lDQzvMZphrBeX8OqgVvx2Yf4kuPb1Z0lHsMDENBlXtOtZRV30+DQdQzoAnhICqIsAuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqASgZTtA/hlPgyyb9NZreyKlWefdYHVCbz+8cXkIeocNxBVw0vmg",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAtgZp23hck7QTOaaLRUR3m3rWjJlld3uXVaGg8t3VpoovKCgEAhiRhOcqAALDvQAGgAwKNvyiQF4+SroJvWAswDsJV2CdylM8XDjfrXVgziaGLygoBAIY/qiUiYAA1wHgo"
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
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422137,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "balance": 70000000000000
    },
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
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
    "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
    "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
        "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
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
    "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
    "meta": 17,
    "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
        "meta": 17,
        "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
    "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oBaD1lpaPS5RdyP6LzOhmJVtbFk1TRG7xZ9k1nSr75DKgEc+K1vE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
          "op": "OffChainTransfer",
          "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "signed_tx": "tx_+JALAfhCuEAdDzFmI8qKohj2oT1Emjq0X1uCPRxwsnuAbU70+xkYgAMnOJ00lvczihQiM7r5TjKBF731Mf4FrwhTkzzloYIPuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAWg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBFPYqAh"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAdDzFmI8qKohj2oT1Emjq0X1uCPRxwsnuAbU70+xkYgAMnOJ00lvczihQiM7r5TjKBF731Mf4FrwhTkzzloYIPuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAWg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBFPYqAh",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
          "op": "OffChainTransfer",
          "to": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
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
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAdDzFmI8qKohj2oT1Emjq0X1uCPRxwsnuAbU70+xkYgAMnOJ00lvczihQiM7r5TjKBF731Mf4FrwhTkzzloYIPuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAWg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBGakCf3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAdDzFmI8qKohj2oT1Emjq0X1uCPRxwsnuAbU70+xkYgAMnOJ00lvczihQiM7r5TjKBF731Mf4FrwhTkzzloYIPuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAWg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBGakCf3"
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAdDzFmI8qKohj2oT1Emjq0X1uCPRxwsnuAbU70+xkYgAMnOJ00lvczihQiM7r5TjKBF731Mf4FrwhTkzzloYIPuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAWg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBGakCf3"
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
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422134,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
      "balance": 69999999999999
    },
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
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
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422133,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAdDzFmI8qKohj2oT1Emjq0X1uCPRxwsnuAbU70+xkYgAMnOJ00lvczihQiM7r5TjKBF731Mf4FrwhTkzzloYIPuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAWg9ZaWj0uUXcj+i8zoZiVbWxZNU0Ru8WfZNZ0q++QyoBGakCf3",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAtgZp23hck7QTOaaLRUR3m3rWjJlld3uXVaGg8t3VpoovKCgEAhiRhOcqAAbDvQAGgAwKNvyiQF4+SroJvWAswDsJV2CdylM8XDjfrXVgziaGLygoBAIY/qiUiX/9e8HGQ"
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
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422132,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "balance": 40000000000001
    },
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "meta": 17,
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
        "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
        "meta": 17,
        "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
    "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oBqBlO0D+GU+DLJv01mt7IqVZ591gdUJvP7xxeQh6hw3EFTbzr2c=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
          "op": "OffChainTransfer",
          "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oBqBlO0D+GU+DLJv01mt7IqVZ591gdUJvP7xxeQh6hw3EFbQ+jVY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBhnCO1YLLb6fqvRXWYRESHZVIUQxwSkM7pcEy6TuQa+oBqBlO0D+GU+DLJv01mt7IqVZ591gdUJvP7xxeQh6hw3EFbQ+jVY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
          "op": "OffChainTransfer",
          "to": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
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
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECGiSALnxWl44CR1u3RMK8a36Pym5F0aO00pUufL4VYit+ovvtW7AtVSYfNC7p+mSSVNIRlVVZOBvjME7SLep0IuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAagZTtA/hlPgyyb9NZreyKlWefdYHVCbz+8cXkIeocNxBVYX9U6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECGiSALnxWl44CR1u3RMK8a36Pym5F0aO00pUufL4VYit+ovvtW7AtVSYfNC7p+mSSVNIRlVVZOBvjME7SLep0IuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAagZTtA/hlPgyyb9NZreyKlWefdYHVCbz+8cXkIeocNxBVYX9U6"
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECGiSALnxWl44CR1u3RMK8a36Pym5F0aO00pUufL4VYit+ovvtW7AtVSYfNC7p+mSSVNIRlVVZOBvjME7SLep0IuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAagZTtA/hlPgyyb9NZreyKlWefdYHVCbz+8cXkIeocNxBVYX9U6"
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
      "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422129,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_M3PzYmeSvm5vWVHT465PJwDv7c1FLHxFcNxJWqtMVfNSR7F8u",
      "balance": 40000000000000
    },
    {
      "account": "ak_2KtNma6c8SdYMFXE2pGB8QtNSGPmftMoLCVjEvY4x8oq6dKve",
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
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422128,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAS2BmnbeFyTtBM5potFRHebetaMmWV3e5dVoaDy3dWmiuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECGiSALnxWl44CR1u3RMK8a36Pym5F0aO00pUufL4VYit+ovvtW7AtVSYfNC7p+mSSVNIRlVVZOBvjME7SLep0IuEj4RjkCoQYZwjtWCy2+n6r0V1mEREh2VSFEMcEpDO6XBMuk7kGvqAagZTtA/hlPgyyb9NZreyKlWefdYHVCbz+8cXkIeocNxBVYX9U6",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAtgZp23hck7QTOaaLRUR3m3rWjJlld3uXVaGg8t3VpoovKCgEAhiRhOcqAALDvQAGgAwKNvyiQF4+SroJvWAswDsJV2CdylM8XDjfrXVgziaGLygoBAIY/qiUiYAA1wHgo"
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
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
  "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
  "id": -576460752303422127,
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
    "channel_id": "ch_CLyNPqE4KYjUd7AvhXsTLGcYnNgJEstmrWSbFgrxLE2bE7UwP",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St&keep_running=false&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH&role=initiator
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
      "fsm_id": "ba_iv9/b3rC28J/sEuXO0pV81Ei6JQNFt8OWmwsnLejp/VkAWHg"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St&keep_running=false&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH&role=responder
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
      "fsm_id": "ba_Xu7MAMQ1RkAdMIKzjIIt5IrHpd2jbIR0JHAu+CXA+XKwJ4JB"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAezfB4HNCF9cwpKxrnGF6zVaucxOXUxoQr1Q8VGp3UAwhj+qJSJgAKEBCvf5zkXZyWe1EuEcyLIqi+gHe4YVcUYNasFfLONIVO2GJGE5yoAAAgoAhhAGeddIAMCgf1/purJvXj8TjWYI9+SVQ/A1z5CFPPdD56V1P2d1OPkByjPOnQ==",
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
    "signed_tx": "tx_+MsLAfhCuEDiSWGYyDZKH1FXLd6CJF/GUCDvM0JmsJ7e3KI9BPjU3F9z2zb7Xi/Drx+XwvsYUz5KfCD8s7IcKuMKyyrAjDYMuIP4gTIBoQHs3weBzQhfXMKSsa5xhes1WrnMTl1MaEK9UPFRqd1AMIY/qiUiYAChAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTthiRhOcqAAAIKAIYQBnnXSADAoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5AVmd1jE="
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
      "signed_tx": "tx_+MsLAfhCuEDiSWGYyDZKH1FXLd6CJF/GUCDvM0JmsJ7e3KI9BPjU3F9z2zb7Xi/Drx+XwvsYUz5KfCD8s7IcKuMKyyrAjDYMuIP4gTIBoQHs3weBzQhfXMKSsa5xhes1WrnMTl1MaEK9UPFRqd1AMIY/qiUiYAChAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTthiRhOcqAAAIKAIYQBnnXSADAoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5AVmd1jE=",
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
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA4klhmMg2Sh9RVy3egiRfxlAg7zNCZrCe3tyiPQT41Nxfc9s2+14vw68fl8L7GFM+Snwg/LOyHCrjCssqwIw2DLiD+IEyAaEB7N8Hgc0IX1zCkrGucYXrNVq5zE5dTGhCvVDxUandQDCGP6olImAAoQEK9/nORdnJZ7US4RzIsiqL6Ad7hhVxRg1qwV8s40hU7YYkYTnKgAACCgCGEAZ510gAwKB/X+m6sm9ePxONZgj35JVD8DXPkIU890PnpXU/Z3U4+QFHM/uL"
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA4klhmMg2Sh9RVy3egiRfxlAg7zNCZrCe3tyiPQT41Nxfc9s2+14vw68fl8L7GFM+Snwg/LOyHCrjCssqwIw2DLiD+IEyAaEB7N8Hgc0IX1zCkrGucYXrNVq5zE5dTGhCvVDxUandQDCGP6olImAAoQEK9/nORdnJZ7US4RzIsiqL6Ad7hhVxRg1qwV8s40hU7YYkYTnKgAACCgCGEAZ510gAwKB/X+m6sm9ePxONZgj35JVD8DXPkIU890PnpXU/Z3U4+QFHM/uL",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA4klhmMg2Sh9RVy3egiRfxlAg7zNCZrCe3tyiPQT41Nxfc9s2+14vw68fl8L7GFM+Snwg/LOyHCrjCssqwIw2DLiD+IEyAaEB7N8Hgc0IX1zCkrGucYXrNVq5zE5dTGhCvVDxUandQDCGP6olImAAoQEK9/nORdnJZ7US4RzIsiqL6Ad7hhVxRg1qwV8s40hU7YYkYTnKgAACCgCGEAZ510gAwKB/X+m6sm9ePxONZgj35JVD8DXPkIU890PnpXU/Z3U4+QFHM/uL",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA4klhmMg2Sh9RVy3egiRfxlAg7zNCZrCe3tyiPQT41Nxfc9s2+14vw68fl8L7GFM+Snwg/LOyHCrjCssqwIw2DLiD+IEyAaEB7N8Hgc0IX1zCkrGucYXrNVq5zE5dTGhCvVDxUandQDCGP6olImAAoQEK9/nORdnJZ7US4RzIsiqL6Ad7hhVxRg1qwV8s40hU7YYkYTnKgAACCgCGEAZ510gAwKB/X+m6sm9ePxONZgj35JVD8DXPkIU890PnpXU/Z3U4+QFHM/uL",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA4klhmMg2Sh9RVy3egiRfxlAg7zNCZrCe3tyiPQT41Nxfc9s2+14vw68fl8L7GFM+Snwg/LOyHCrjCssqwIw2DLiD+IEyAaEB7N8Hgc0IX1zCkrGucYXrNVq5zE5dTGhCvVDxUandQDCGP6olImAAoQEK9/nORdnJZ7US4RzIsiqL6Ad7hhVxRg1qwV8s40hU7YYkYTnKgAACCgCGEAZ510gAwKB/X+m6sm9ePxONZgj35JVD8DXPkIU890PnpXU/Z3U4+QFHM/uL",
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
    "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "message": {
        "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
        "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
        "info": "Hello",
        "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "message": {
        "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
        "info": "Hello back",
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421506,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "balance": 69999999999999
    },
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA4klhmMg2Sh9RVy3egiRfxlAg7zNCZrCe3tyiPQT41Nxfc9s2+14vw68fl8L7GFM+Snwg/LOyHCrjCssqwIw2DLiD+IEyAaEB7N8Hgc0IX1zCkrGucYXrNVq5zE5dTGhCvVDxUandQDCGP6olImAAoQEK9/nORdnJZ7US4RzIsiqL6Ad7hhVxRg1qwV8s40hU7YYkYTnKgAACCgCGEAZ510gAwKB/X+m6sm9ePxONZgj35JVD8DXPkIU890PnpXU/Z3U4+QFHM/uL"
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA4klhmMg2Sh9RVy3egiRfxlAg7zNCZrCe3tyiPQT41Nxfc9s2+14vw68fl8L7GFM+Snwg/LOyHCrjCssqwIw2DLiD+IEyAaEB7N8Hgc0IX1zCkrGucYXrNVq5zE5dTGhCvVDxUandQDCGP6olImAAoQEK9/nORdnJZ7US4RzIsiqL6Ad7hhVxRg1qwV8s40hU7YYkYTnKgAACCgCGEAZ510gAwKB/X+m6sm9ePxONZgj35JVD8DXPkIU890PnpXU/Z3U4+QFHM/uL"
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
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421505,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "balance": 69999999999999
    },
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
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
    "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
    "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
        "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
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
    "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
    "meta": 17,
    "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
        "meta": 17,
        "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
    "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqdrWPsYlsAyKWBYZT76P/vncDpdwbKdcbJT7p1aLkEBAqCaJjkIv0DUfB+tPNM8ZDnV78J9XtVaSCz7eRGFdyKKlepcsU0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
          "op": "OffChainTransfer",
          "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "signed_tx": "tx_+JALAfhCuEBkF5xjmGw4ASMXiBNNrol3ADyVDb64Of0A6nqYJSF0dG6yyY/J2IdAlyQ+vjp8SYIZHILq/yPrN6a+WtGkzo4DuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQKgmiY5CL9A1HwfrTzTPGQ51e/CfV7VWkgs+3kRhXciipXxqlvT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBkF5xjmGw4ASMXiBNNrol3ADyVDb64Of0A6nqYJSF0dG6yyY/J2IdAlyQ+vjp8SYIZHILq/yPrN6a+WtGkzo4DuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQKgmiY5CL9A1HwfrTzTPGQ51e/CfV7VWkgs+3kRhXciipXxqlvT",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
          "op": "OffChainTransfer",
          "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAZBecY5hsOAEjF4gTTa6JdwA8lQ2+uDn9AOp6mCUhdHRussmPydiHQJckPr46fEmCGRyC6v8j6zemvlrRpM6OA7hI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQECoJomOQi/QNR8H6080zxkOdXvwn1e1VpILPt5EYV3IoqVJZeFMw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAZBecY5hsOAEjF4gTTa6JdwA8lQ2+uDn9AOp6mCUhdHRussmPydiHQJckPr46fEmCGRyC6v8j6zemvlrRpM6OA7hI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQECoJomOQi/QNR8H6080zxkOdXvwn1e1VpILPt5EYV3IoqVJZeFMw=="
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAZBecY5hsOAEjF4gTTa6JdwA8lQ2+uDn9AOp6mCUhdHRussmPydiHQJckPr46fEmCGRyC6v8j6zemvlrRpM6OA7hI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQECoJomOQi/QNR8H6080zxkOdXvwn1e1VpILPt5EYV3IoqVJZeFMw=="
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
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421502,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "balance": 69999999999998
    },
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
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
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421501,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAZBecY5hsOAEjF4gTTa6JdwA8lQ2+uDn9AOp6mCUhdHRussmPydiHQJckPr46fEmCGRyC6v8j6zemvlrRpM6OA7hI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQECoJomOQi/QNR8H6080zxkOdXvwn1e1VpILPt5EYV3IoqVJZeFMw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDs3weBzQhfXMKSsa5xhes1WrnMTl1MaEK9UPFRqd1AMIvKCgEAhj+qJSJf/rDvQAGgCvf5zkXZyWe1EuEcyLIqi+gHe4YVcUYNasFfLONIVO2LygoBAIYkYTnKgAKRUwdP"
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
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421500,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "balance": 40000000000002
    },
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "meta": 17,
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
        "meta": 17,
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqdrWPsYlsAyKWBYZT76P/vncDpdwbKdcbJT7p1aLkEBA6B/X+m6sm9ePxONZgj35JVD8DXPkIU890PnpXU/Z3U4+Wj1qNM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
          "op": "OffChainTransfer",
          "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQOgf1/purJvXj8TjWYI9+SVQ/A1z5CFPPdD56V1P2d1OPkpcIqy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQOgf1/purJvXj8TjWYI9+SVQ/A1z5CFPPdD56V1P2d1OPkpcIqy",
      "updates": [
        {
          "amount": 1,
          "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
          "op": "OffChainTransfer",
          "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAZA6Xt+haS5yPMa7xCJwIsTUJRPRmyEw2ubM2oadgQgytXIt4hM5K8Bvhjw4vqNoXUV5ThC/7ufCzsuYZ5AgNBbhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEDoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5JQkCYA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAZA6Xt+haS5yPMa7xCJwIsTUJRPRmyEw2ubM2oadgQgytXIt4hM5K8Bvhjw4vqNoXUV5ThC/7ufCzsuYZ5AgNBbhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEDoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5JQkCYA=="
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAZA6Xt+haS5yPMa7xCJwIsTUJRPRmyEw2ubM2oadgQgytXIt4hM5K8Bvhjw4vqNoXUV5ThC/7ufCzsuYZ5AgNBbhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEDoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5JQkCYA=="
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
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421497,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "balance": 40000000000001
    },
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
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
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421496,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAZA6Xt+haS5yPMa7xCJwIsTUJRPRmyEw2ubM2oadgQgytXIt4hM5K8Bvhjw4vqNoXUV5ThC/7ufCzsuYZ5AgNBbhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEDoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5JQkCYA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDs3weBzQhfXMKSsa5xhes1WrnMTl1MaEK9UPFRqd1AMIvKCgEAhj+qJSJf/7DvQAGgCvf5zkXZyWe1EuEcyLIqi+gHe4YVcUYNasFfLONIVO2LygoBAIYkYTnKgAFDJVu6"
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
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421495,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "balance": 40000000000001
    },
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "meta": 17,
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
        "meta": 17,
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqdrWPsYlsAyKWBYZT76P/vncDpdwbKdcbJT7p1aLkEBBKC5CakP3O9zcP5UUJnTYZtRlOzQPRVySEQh2v1Plq8saJCCrUc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
          "op": "OffChainTransfer",
          "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQSguQmpD9zvc3D+VFCZ02GbUZTs0D0VckhEIdr9T5avLGh1VumF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQSguQmpD9zvc3D+VFCZ02GbUZTs0D0VckhEIdr9T5avLGh1VumF",
      "updates": [
        {
          "amount": 1,
          "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
          "op": "OffChainTransfer",
          "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAb7LYfvw76ATKqeUyBAw3rITvB8pBdGF/up/OAboTwCpIlw6tSWV3nmvJls10AftaXzfaUvWwbEm4lpH7xSoEALhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEEoLkJqQ/c73Nw/lRQmdNhm1GU7NA9FXJIRCHa/U+WryxoxbJvNg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAb7LYfvw76ATKqeUyBAw3rITvB8pBdGF/up/OAboTwCpIlw6tSWV3nmvJls10AftaXzfaUvWwbEm4lpH7xSoEALhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEEoLkJqQ/c73Nw/lRQmdNhm1GU7NA9FXJIRCHa/U+WryxoxbJvNg=="
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAb7LYfvw76ATKqeUyBAw3rITvB8pBdGF/up/OAboTwCpIlw6tSWV3nmvJls10AftaXzfaUvWwbEm4lpH7xSoEALhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEEoLkJqQ/c73Nw/lRQmdNhm1GU7NA9FXJIRCHa/U+WryxoxbJvNg=="
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
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421492,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "balance": 40000000000000
    },
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
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
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421491,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAb7LYfvw76ATKqeUyBAw3rITvB8pBdGF/up/OAboTwCpIlw6tSWV3nmvJls10AftaXzfaUvWwbEm4lpH7xSoEALhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEEoLkJqQ/c73Nw/lRQmdNhm1GU7NA9FXJIRCHa/U+WryxoxbJvNg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDs3weBzQhfXMKSsa5xhes1WrnMTl1MaEK9UPFRqd1AMIvKCgEAhj+qJSJgALDvQAGgCvf5zkXZyWe1EuEcyLIqi+gHe4YVcUYNasFfLONIVO2LygoBAIYkYTnKgADhOi00"
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
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421490,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "balance": 70000000000000
    },
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
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
    "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
    "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
        "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
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
    "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
    "meta": 17,
    "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
        "meta": 17,
        "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
    "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqdrWPsYlsAyKWBYZT76P/vncDpdwbKdcbJT7p1aLkEBBaB/X+m6sm9ePxONZgj35JVD8DXPkIU890PnpXU/Z3U4+XDa29g=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
          "op": "OffChainTransfer",
          "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "signed_tx": "tx_+JALAfhCuEB/QMWYJKLXzapHktXstz/b1U69t8IttOsIepYxtanTn3hroorErIFhNplvqnud6auwOMEmzulwSSPOqKlzrqMNuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQWgf1/purJvXj8TjWYI9+SVQ/A1z5CFPPdD56V1P2d1OPnwlDr+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB/QMWYJKLXzapHktXstz/b1U69t8IttOsIepYxtanTn3hroorErIFhNplvqnud6auwOMEmzulwSSPOqKlzrqMNuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQWgf1/purJvXj8TjWYI9+SVQ/A1z5CFPPdD56V1P2d1OPnwlDr+",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
          "op": "OffChainTransfer",
          "to": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAf0DFmCSi182qR5LV7Lc/29VOvbfCLbTrCHqWMbWp0594a6KKxKyBYTaZb6p7nemrsDjBJs7pcEkjzqipc66jDbhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEFoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5SoIaGg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAf0DFmCSi182qR5LV7Lc/29VOvbfCLbTrCHqWMbWp0594a6KKxKyBYTaZb6p7nemrsDjBJs7pcEkjzqipc66jDbhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEFoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5SoIaGg=="
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAf0DFmCSi182qR5LV7Lc/29VOvbfCLbTrCHqWMbWp0594a6KKxKyBYTaZb6p7nemrsDjBJs7pcEkjzqipc66jDbhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEFoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5SoIaGg=="
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
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421487,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
      "balance": 69999999999999
    },
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
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
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421486,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAf0DFmCSi182qR5LV7Lc/29VOvbfCLbTrCHqWMbWp0594a6KKxKyBYTaZb6p7nemrsDjBJs7pcEkjzqipc66jDbhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEFoH9f6bqyb14/E41mCPfklUPwNc+QhTz3Q+eldT9ndTj5SoIaGg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDs3weBzQhfXMKSsa5xhes1WrnMTl1MaEK9UPFRqd1AMIvKCgEAhj+qJSJf/7DvQAGgCvf5zkXZyWe1EuEcyLIqi+gHe4YVcUYNasFfLONIVO2LygoBAIYkYTnKgAFDJVu6"
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
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421485,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "balance": 40000000000001
    },
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "meta": 17,
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
        "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
        "meta": 17,
        "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
    "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqdrWPsYlsAyKWBYZT76P/vncDpdwbKdcbJT7p1aLkEBBqC5CakP3O9zcP5UUJnTYZtRlOzQPRVySEQh2v1Plq8saNJ67O8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
          "op": "OffChainTransfer",
          "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQaguQmpD9zvc3D+VFCZ02GbUZTs0D0VckhEIdr9T5avLGjwD6cB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQana1j7GJbAMilgWGU++j/753A6XcGynXGyU+6dWi5BAQaguQmpD9zvc3D+VFCZ02GbUZTs0D0VckhEIdr9T5avLGjwD6cB",
      "updates": [
        {
          "amount": 1,
          "from": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
          "op": "OffChainTransfer",
          "to": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA15pzpwA21av3ugdjipyOHow137igCJXfEKGrFiNTSn79dVGLe9cLN1nVZtZEGVri3kJXDnbEGanf7+zvoPNJDLhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEGoLkJqQ/c73Nw/lRQmdNhm1GU7NA9FXJIRCHa/U+WryxocOHOiQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA15pzpwA21av3ugdjipyOHow137igCJXfEKGrFiNTSn79dVGLe9cLN1nVZtZEGVri3kJXDnbEGanf7+zvoPNJDLhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEGoLkJqQ/c73Nw/lRQmdNhm1GU7NA9FXJIRCHa/U+WryxocOHOiQ=="
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
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA15pzpwA21av3ugdjipyOHow137igCJXfEKGrFiNTSn79dVGLe9cLN1nVZtZEGVri3kJXDnbEGanf7+zvoPNJDLhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEGoLkJqQ/c73Nw/lRQmdNhm1GU7NA9FXJIRCHa/U+WryxocOHOiQ=="
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
      "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421482,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_5qBR7mMg43otpStGrUHdDakRvaG85Tn5fxUn9B1AP3ZftzhWH",
      "balance": 40000000000000
    },
    {
      "account": "ak_2oKZK68RqGgdVZQ9FcQWkD1WvV5WkXGW4WK5YvyzgRgcTh15St",
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
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421481,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQr3+c5F2clntRLhHMiyKovoB3uGFXFGDWrBXyzjSFTtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA15pzpwA21av3ugdjipyOHow137igCJXfEKGrFiNTSn79dVGLe9cLN1nVZtZEGVri3kJXDnbEGanf7+zvoPNJDLhI+EY5AqEGp2tY+xiWwDIpYFhlPvo/++dwOl3Bsp1xslPunVouQQEGoLkJqQ/c73Nw/lRQmdNhm1GU7NA9FXJIRCHa/U+WryxocOHOiQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDs3weBzQhfXMKSsa5xhes1WrnMTl1MaEK9UPFRqd1AMIvKCgEAhj+qJSJgALDvQAGgCvf5zkXZyWe1EuEcyLIqi+gHe4YVcUYNasFfLONIVO2LygoBAIYkYTnKgADhOi00"
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
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
  "channel_id": "ch_2GjW7iBqDRmNJ4ZWtThgQrPC9KtMFJgNBDJp1zoLn71eUwcqTV",
  "id": -576460752303421479,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
