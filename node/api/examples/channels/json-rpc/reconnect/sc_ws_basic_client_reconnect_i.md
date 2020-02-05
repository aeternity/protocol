
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t&role=initiator
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
      "fsm_id": "ba_6WPWxC79+wzukdei+37JExnPFbNP51m3SCatp1aURqbD0jbv"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t&role=responder
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
      "fsm_id": "ba_WyVkEV8jBBDNKuebYXxF6fVSTL7LcWhA6l72zZRzb29tUyVT"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcEPn9wYW2WeUioPc0aitoAUhn4Ax/9xBaFbAsrOdjjMhj+qJSJgAKEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGJGE5yoAAAgoAhhAGeddIAMCg1L8DGd++jlpUYTNXUSswpxHX8sdCYQqWeBe+ygX0qb8BCmF+Nw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423007,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECKKayq39VubuiJp27zIJA2qbiF13ETSwgQWa1lP7PDOIJpTrboqH9k39t7qm9uAOKDw1/KWgJjyeKBxn4FpI8DuIP4gTIBoQHBD5/cGFtlnlIqD3NGoraAFIZ+AMf/cQWhWwLKznY4zIY/qiUiYAChAfpVYf9STroOfVZtXPrwIm0A4/wUDym95HhoReMybiQRhiRhOcqAAAIKAIYQBnnXSADAoNS/Axnfvo5aVGEzV1ErMKcR1/LHQmEKlngXvsoF9Km/AQ66OQs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423007,
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
      "signed_tx": "tx_+MsLAfhCuECKKayq39VubuiJp27zIJA2qbiF13ETSwgQWa1lP7PDOIJpTrboqH9k39t7qm9uAOKDw1/KWgJjyeKBxn4FpI8DuIP4gTIBoQHBD5/cGFtlnlIqD3NGoraAFIZ+AMf/cQWhWwLKznY4zIY/qiUiYAChAfpVYf9STroOfVZtXPrwIm0A4/wUDym95HhoReMybiQRhiRhOcqAAAIKAIYQBnnXSADAoNS/Axnfvo5aVGEzV1ErMKcR1/LHQmEKlngXvsoF9Km/AQ66OQs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423006,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAiimsqt/Vbm7oiadu8yCQNqm4hddxE0sIEFmtZT+zwziCaU626Kh/ZN/be6pvbgDig8NfyloCY8nigcZ+BaSPA7hAlq8gAZEuYWLyr1eAHlH4m7pkOl2Z9OnOKtkn8I48HmdyRhKixdmUnFY8TDfCZuDk1MTZAL5VSmezLoRInJSsC7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwH7QWF/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423006,
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAiimsqt/Vbm7oiadu8yCQNqm4hddxE0sIEFmtZT+zwziCaU626Kh/ZN/be6pvbgDig8NfyloCY8nigcZ+BaSPA7hAlq8gAZEuYWLyr1eAHlH4m7pkOl2Z9OnOKtkn8I48HmdyRhKixdmUnFY8TDfCZuDk1MTZAL5VSmezLoRInJSsC7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwH7QWF/",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAiimsqt/Vbm7oiadu8yCQNqm4hddxE0sIEFmtZT+zwziCaU626Kh/ZN/be6pvbgDig8NfyloCY8nigcZ+BaSPA7hAlq8gAZEuYWLyr1eAHlH4m7pkOl2Z9OnOKtkn8I48HmdyRhKixdmUnFY8TDfCZuDk1MTZAL5VSmezLoRInJSsC7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwH7QWF/",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAiimsqt/Vbm7oiadu8yCQNqm4hddxE0sIEFmtZT+zwziCaU626Kh/ZN/be6pvbgDig8NfyloCY8nigcZ+BaSPA7hAlq8gAZEuYWLyr1eAHlH4m7pkOl2Z9OnOKtkn8I48HmdyRhKixdmUnFY8TDfCZuDk1MTZAL5VSmezLoRInJSsC7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwH7QWF/",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAiimsqt/Vbm7oiadu8yCQNqm4hddxE0sIEFmtZT+zwziCaU626Kh/ZN/be6pvbgDig8NfyloCY8nigcZ+BaSPA7hAlq8gAZEuYWLyr1eAHlH4m7pkOl2Z9OnOKtkn8I48HmdyRhKixdmUnFY8TDfCZuDk1MTZAL5VSmezLoRInJSsC7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwH7QWF/",
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
    "to": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "message": {
        "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
        "from": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
        "info": "Hello",
        "to": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
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
    "to": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "message": {
        "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
        "from": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t",
        "info": "Hello back",
        "to": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423005,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
      "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
  "id": -576460752303423005,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
      "balance": 69999999999999
    },
    {
      "account": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "state": "tx_+QENCwH4hLhAiimsqt/Vbm7oiadu8yCQNqm4hddxE0sIEFmtZT+zwziCaU626Kh/ZN/be6pvbgDig8NfyloCY8nigcZ+BaSPA7hAlq8gAZEuYWLyr1eAHlH4m7pkOl2Z9OnOKtkn8I48HmdyRhKixdmUnFY8TDfCZuDk1MTZAL5VSmezLoRInJSsC7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwH7QWF/"
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "state": "tx_+QENCwH4hLhAiimsqt/Vbm7oiadu8yCQNqm4hddxE0sIEFmtZT+zwziCaU626Kh/ZN/be6pvbgDig8NfyloCY8nigcZ+BaSPA7hAlq8gAZEuYWLyr1eAHlH4m7pkOl2Z9OnOKtkn8I48HmdyRhKixdmUnFY8TDfCZuDk1MTZAL5VSmezLoRInJSsC7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwH7QWF/"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t",
    "to": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpRVyYG/NxSqJYjJqAXuBAjtiZlX4DRnBymAYzdsoe5TAqBHh4mvUSj9aFbIafOber7OBvUvDH5jm2YfIGLuwwQhWAwEOTg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t",
          "op": "OffChainTransfer",
          "to": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAULm01A7ja5qClRwkSIz1uGlSQ6J9/88QfCnJ4KUIS6AJrxM9+Vc66BtnYa8Tx1FyOeW7QmeHdFr8HlbthCUoBuEj4RjkCoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuUwKgR4eJr1Eo/WhWyGnzm3q+zgb1Lwx+Y5tmHyBi7sMEIVhtZYvE"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
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
    "from": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t",
    "to": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpRVyYG/NxSqJYjJqAXuBAjtiZlX4DRnBymAYzdsoe5TAqBHh4mvUSj9aFbIafOber7OBvUvDH5jm2YfIGLuwwQhWAwEOTg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t",
          "op": "OffChainTransfer",
          "to": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAULm01A7ja5qClRwkSIz1uGlSQ6J9/88QfCnJ4KUIS6AJrxM9+Vc66BtnYa8Tx1FyOeW7QmeHdFr8HlbthCUoBuEAj3QzTWKV2QKvQIx5G6lDVx3SLWMOrKAvFaCuLMXcHjT0rY5BOa+4nhmdekkw6AQLWwWt8Z73V17NjGq7dmHIEuEj4RjkCoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuUwKgR4eJr1Eo/WhWyGnzm3q+zgb1Lwx+Y5tmHyBi7sMEIVi4t9XD"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "state": "tx_+NILAfiEuEAULm01A7ja5qClRwkSIz1uGlSQ6J9/88QfCnJ4KUIS6AJrxM9+Vc66BtnYa8Tx1FyOeW7QmeHdFr8HlbthCUoBuEAj3QzTWKV2QKvQIx5G6lDVx3SLWMOrKAvFaCuLMXcHjT0rY5BOa+4nhmdekkw6AQLWwWt8Z73V17NjGq7dmHIEuEj4RjkCoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuUwKgR4eJr1Eo/WhWyGnzm3q+zgb1Lwx+Y5tmHyBi7sMEIVi4t9XD"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ&host=localhost&offchain_tx=tx_%2BNILAfiEuEAULm01A7ja5qClRwkSIz1uGlSQ6J9%2F88QfCnJ4KUIS6AJrxM9%2BVc66BtnYa8Tx1FyOeW7QmeHdFr8HlbthCUoBuEAj3QzTWKV2QKvQIx5G6lDVx3SLWMOrKAvFaCuLMXcHjT0rY5BOa%2B4nhmdekkw6AQLWwWt8Z73V17NjGq7dmHIEuEj4RjkCoQaUVcmBvzcUqiWIyagF7gQI7YmZV%2BA0ZwcpgGM3bKHuUwKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVi4t9XD&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuEAULm01A7ja5qClRwkSIz1uGlSQ6J9%2F88QfCnJ4KUIS6AJrxM9%2BVc66BtnYa8Tx1FyOeW7QmeHdFr8HlbthCUoBuEAj3QzTWKV2QKvQIx5G6lDVx3SLWMOrKAvFaCuLMXcHjT0rY5BOa%2B4nhmdekkw6AQLWwWt8Z73V17NjGq7dmHIEuEj4RjkCoQaUVcmBvzcUqiWIyagF7gQI7YmZV%2BA0ZwcpgGM3bKHuUwKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVi4t9XD&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ&existing_fsm_id=ba_7L5gYLLn5WqRnnNm&host=localhost&offchain_tx=tx_%2BNILAfiEuEAULm01A7ja5qClRwkSIz1uGlSQ6J9%2F88QfCnJ4KUIS6AJrxM9%2BVc66BtnYa8Tx1FyOeW7QmeHdFr8HlbthCUoBuEAj3QzTWKV2QKvQIx5G6lDVx3SLWMOrKAvFaCuLMXcHjT0rY5BOa%2B4nhmdekkw6AQLWwWt8Z73V17NjGq7dmHIEuEj4RjkCoQaUVcmBvzcUqiWIyagF7gQI7YmZV%2BA0ZwcpgGM3bKHuUwKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVi4t9XD&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ&existing_fsm_id=ba_JJVV0VIcP6T5iWDc%2FpAA5AYzNFVbQ66RfMKC38eH3qd%2F3fVU&host=localhost&offchain_tx=tx_%2BNILAfiEuEAULm01A7ja5qClRwkSIz1uGlSQ6J9%2F88QfCnJ4KUIS6AJrxM9%2BVc66BtnYa8Tx1FyOeW7QmeHdFr8HlbthCUoBuEAj3QzTWKV2QKvQIx5G6lDVx3SLWMOrKAvFaCuLMXcHjT0rY5BOa%2B4nhmdekkw6AQLWwWt8Z73V17NjGq7dmHIEuEj4RjkCoQaUVcmBvzcUqiWIyagF7gQI7YmZV%2BA0ZwcpgGM3bKHuUwKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVi4t9XD&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ&existing_fsm_id=ba_6WPWxC79%2Bwzukdei%2B37JExnPFbNP51m3SCatp1aURqbD0jbv&host=localhost&offchain_tx=tx_%2BNILAfiEuEAULm01A7ja5qClRwkSIz1uGlSQ6J9%2F88QfCnJ4KUIS6AJrxM9%2BVc66BtnYa8Tx1FyOeW7QmeHdFr8HlbthCUoBuEAj3QzTWKV2QKvQIx5G6lDVx3SLWMOrKAvFaCuLMXcHjT0rY5BOa%2B4nhmdekkw6AQLWwWt8Z73V17NjGq7dmHIEuEj4RjkCoQaUVcmBvzcUqiWIyagF7gQI7YmZV%2BA0ZwcpgGM3bKHuUwKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVi4t9XD&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_6WPWxC79+wzukdei+37JExnPFbNP51m3SCatp1aURqbD0jbv"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBpRVyYG/NxSqJYjJqAXuBAjtiZlX4DRnBymAYzdsoe5ToQHBD5/cGFtlnlIqD3NGoraAFIZ+AMf/cQWhWwLKznY4zIY2kdavwACGG0jrV+AAAIYSMJzlQAACNF8fkQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423004,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECAF9ZRNQqqnaeEBljKmAdqbpVG0gOh0zHnRSAhIEIWrukETGB56lhEgf6vFMT0pzVKY6JVIeRG5oJ+NE/zADQGuF/4XTUBoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuU6EBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAAAjjQmqs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
  "id": -576460752303423004,
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECAF9ZRNQqqnaeEBljKmAdqbpVG0gOh0zHnRSAhIEIWrukETGB56lhEgf6vFMT0pzVKY6JVIeRG5oJ+NE/zADQGuF/4XTUBoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuU6EBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAAAjjQmqs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423003,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuECAF9ZRNQqqnaeEBljKmAdqbpVG0gOh0zHnRSAhIEIWrukETGB56lhEgf6vFMT0pzVKY6JVIeRG5oJ+NE/zADQGuECVvx3E9AzYvqA+peV+LFz2VV8DAYOfpMLiQMQBY2SnNzK1Jeu03d1OSxcn0IcwFk1VGb8XnboEyFwIv/JBo18IuF/4XTUBoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuU6EBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAAAqInV+E="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
  "id": -576460752303423003,
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECAF9ZRNQqqnaeEBljKmAdqbpVG0gOh0zHnRSAhIEIWrukETGB56lhEgf6vFMT0pzVKY6JVIeRG5oJ+NE/zADQGuECVvx3E9AzYvqA+peV+LFz2VV8DAYOfpMLiQMQBY2SnNzK1Jeu03d1OSxcn0IcwFk1VGb8XnboEyFwIv/JBo18IuF/4XTUBoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuU6EBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAAAqInV+E=",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECAF9ZRNQqqnaeEBljKmAdqbpVG0gOh0zHnRSAhIEIWrukETGB56lhEgf6vFMT0pzVKY6JVIeRG5oJ+NE/zADQGuECVvx3E9AzYvqA+peV+LFz2VV8DAYOfpMLiQMQBY2SnNzK1Jeu03d1OSxcn0IcwFk1VGb8XnboEyFwIv/JBo18IuF/4XTUBoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuU6EBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAAAqInV+E=",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECAF9ZRNQqqnaeEBljKmAdqbpVG0gOh0zHnRSAhIEIWrukETGB56lhEgf6vFMT0pzVKY6JVIeRG5oJ+NE/zADQGuECVvx3E9AzYvqA+peV+LFz2VV8DAYOfpMLiQMQBY2SnNzK1Jeu03d1OSxcn0IcwFk1VGb8XnboEyFwIv/JBo18IuF/4XTUBoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuU6EBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAAAqInV+E=",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECAF9ZRNQqqnaeEBljKmAdqbpVG0gOh0zHnRSAhIEIWrukETGB56lhEgf6vFMT0pzVKY6JVIeRG5oJ+NE/zADQGuECVvx3E9AzYvqA+peV+LFz2VV8DAYOfpMLiQMQBY2SnNzK1Jeu03d1OSxcn0IcwFk1VGb8XnboEyFwIv/JBo18IuF/4XTUBoQaUVcmBvzcUqiWIyagF7gQI7YmZV+A0ZwcpgGM3bKHuU6EBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAAAqInV+E=",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
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
    "channel_id": "ch_28L2EJbW5FainxsWbidVZzwMvtXz6TFhRTeKdw99LmS8tEyrGZ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
