
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
      "fsm_id": "ba_n6YEqRE9iUtt6gCwewqOh7BVBA47cHhPIIlD+O0CgXU+getl"
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
      "fsm_id": "ba_JRr61MA/PPUyHu2+9zDJFPMpj12ymh4+qEfn4BdKl0XAhIPq"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcEPn9wYW2WeUioPc0aitoAUhn4Ax/9xBaFbAsrOdjjMhj+qJSJgAKEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGJGE5yoAAAgoAhhAGeddIAMCg1L8DGd++jlpUYTNXUSswpxHX8sdCYQqWeBe+ygX0qb8ErxD9uw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422997,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECU8Gq7Vxef8p8aLgVBA3gbcqb+f3TgAAT6qkh4TSL7GrO4rQ1SzgaEz0QU80ZC9xbIForWjkM46kiA9MQnDcsAuIP4gTIBoQHBD5/cGFtlnlIqD3NGoraAFIZ+AMf/cQWhWwLKznY4zIY/qiUiYAChAfpVYf9STroOfVZtXPrwIm0A4/wUDym95HhoReMybiQRhiRhOcqAAAIKAIYQBnnXSADAoNS/Axnfvo5aVGEzV1ErMKcR1/LHQmEKlngXvsoF9Km/BDmxUSA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422997,
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
      "signed_tx": "tx_+MsLAfhCuECU8Gq7Vxef8p8aLgVBA3gbcqb+f3TgAAT6qkh4TSL7GrO4rQ1SzgaEz0QU80ZC9xbIForWjkM46kiA9MQnDcsAuIP4gTIBoQHBD5/cGFtlnlIqD3NGoraAFIZ+AMf/cQWhWwLKznY4zIY/qiUiYAChAfpVYf9STroOfVZtXPrwIm0A4/wUDym95HhoReMybiQRhiRhOcqAAAIKAIYQBnnXSADAoNS/Axnfvo5aVGEzV1ErMKcR1/LHQmEKlngXvsoF9Km/BDmxUSA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422996,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAlPBqu1cXn/KfGi4FQQN4G3Km/n904AAE+qpIeE0i+xqzuK0NUs4GhM9EFPNGQvcWyBaK1o5DOOpIgPTEJw3LALhAtQTfZqX2FkF1cCcNjPZ95kCQG7UrZfg+Krz7/sO/bx8R3XHqCQpU33YggFhTZqbNN0bfFV4NHOehLjGgwOeuBriD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwQ2JjIK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422996,
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAlPBqu1cXn/KfGi4FQQN4G3Km/n904AAE+qpIeE0i+xqzuK0NUs4GhM9EFPNGQvcWyBaK1o5DOOpIgPTEJw3LALhAtQTfZqX2FkF1cCcNjPZ95kCQG7UrZfg+Krz7/sO/bx8R3XHqCQpU33YggFhTZqbNN0bfFV4NHOehLjGgwOeuBriD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwQ2JjIK",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAlPBqu1cXn/KfGi4FQQN4G3Km/n904AAE+qpIeE0i+xqzuK0NUs4GhM9EFPNGQvcWyBaK1o5DOOpIgPTEJw3LALhAtQTfZqX2FkF1cCcNjPZ95kCQG7UrZfg+Krz7/sO/bx8R3XHqCQpU33YggFhTZqbNN0bfFV4NHOehLjGgwOeuBriD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwQ2JjIK",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAlPBqu1cXn/KfGi4FQQN4G3Km/n904AAE+qpIeE0i+xqzuK0NUs4GhM9EFPNGQvcWyBaK1o5DOOpIgPTEJw3LALhAtQTfZqX2FkF1cCcNjPZ95kCQG7UrZfg+Krz7/sO/bx8R3XHqCQpU33YggFhTZqbNN0bfFV4NHOehLjGgwOeuBriD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwQ2JjIK",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAlPBqu1cXn/KfGi4FQQN4G3Km/n904AAE+qpIeE0i+xqzuK0NUs4GhM9EFPNGQvcWyBaK1o5DOOpIgPTEJw3LALhAtQTfZqX2FkF1cCcNjPZ95kCQG7UrZfg+Krz7/sO/bx8R3XHqCQpU33YggFhTZqbNN0bfFV4NHOehLjGgwOeuBriD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwQ2JjIK",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "message": {
        "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "message": {
        "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
  "id": -576460752303422995,
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
  "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
  "id": -576460752303422995,
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "state": "tx_+QENCwH4hLhAlPBqu1cXn/KfGi4FQQN4G3Km/n904AAE+qpIeE0i+xqzuK0NUs4GhM9EFPNGQvcWyBaK1o5DOOpIgPTEJw3LALhAtQTfZqX2FkF1cCcNjPZ95kCQG7UrZfg+Krz7/sO/bx8R3XHqCQpU33YggFhTZqbNN0bfFV4NHOehLjGgwOeuBriD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwQ2JjIK"
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "state": "tx_+QENCwH4hLhAlPBqu1cXn/KfGi4FQQN4G3Km/n904AAE+qpIeE0i+xqzuK0NUs4GhM9EFPNGQvcWyBaK1o5DOOpIgPTEJw3LALhAtQTfZqX2FkF1cCcNjPZ95kCQG7UrZfg+Krz7/sO/bx8R3XHqCQpU33YggFhTZqbNN0bfFV4NHOehLjGgwOeuBriD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwQ2JjIK"
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBogFWHYd7q7nfmsmNrNDjSNLIiYFosR8Ms0+gQmn4TIQAqBHh4mvUSj9aFbIafOber7OBvUvDH5jm2YfIGLuwwQhWJ+IPVM=",
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
    "signed_tx": "tx_+JALAfhCuEDvYW1LiVKDYiGC+LR1RG6yu4v5lfjH7n8vIo2JiZLy4H9wC4o1YmelzmZdlTDZHam0QKx64Zs0vmgzUsNyadEPuEj4RjkCoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEAKgR4eJr1Eo/WhWyGnzm3q+zgb1Lwx+Y5tmHyBi7sMEIVh9rwHT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBogFWHYd7q7nfmsmNrNDjSNLIiYFosR8Ms0+gQmn4TIQAqBHh4mvUSj9aFbIafOber7OBvUvDH5jm2YfIGLuwwQhWJ+IPVM=",
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
    "signed_tx": "tx_+NILAfiEuEAEtju0XkuleWZXDkKod9xRlUlEviuSxDGRFUfFki993xabNX9+4KqWTbV1ghthDF4XdFTR7MfaUMTKWABuk98CuEDvYW1LiVKDYiGC+LR1RG6yu4v5lfjH7n8vIo2JiZLy4H9wC4o1YmelzmZdlTDZHam0QKx64Zs0vmgzUsNyadEPuEj4RjkCoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEAKgR4eJr1Eo/WhWyGnzm3q+zgb1Lwx+Y5tmHyBi7sMEIVhYcOF+"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "state": "tx_+NILAfiEuEAEtju0XkuleWZXDkKod9xRlUlEviuSxDGRFUfFki993xabNX9+4KqWTbV1ghthDF4XdFTR7MfaUMTKWABuk98CuEDvYW1LiVKDYiGC+LR1RG6yu4v5lfjH7n8vIo2JiZLy4H9wC4o1YmelzmZdlTDZHam0QKx64Zs0vmgzUsNyadEPuEj4RjkCoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEAKgR4eJr1Eo/WhWyGnzm3q+zgb1Lwx+Y5tmHyBi7sMEIVhYcOF+"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw&host=localhost&offchain_tx=tx_%2BNILAfiEuEAEtju0XkuleWZXDkKod9xRlUlEviuSxDGRFUfFki993xabNX9%2B4KqWTbV1ghthDF4XdFTR7MfaUMTKWABuk98CuEDvYW1LiVKDYiGC%2BLR1RG6yu4v5lfjH7n8vIo2JiZLy4H9wC4o1YmelzmZdlTDZHam0QKx64Zs0vmgzUsNyadEPuEj4RjkCoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp%2BEyEAKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVhYcOF%2B&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuEAEtju0XkuleWZXDkKod9xRlUlEviuSxDGRFUfFki993xabNX9%2B4KqWTbV1ghthDF4XdFTR7MfaUMTKWABuk98CuEDvYW1LiVKDYiGC%2BLR1RG6yu4v5lfjH7n8vIo2JiZLy4H9wC4o1YmelzmZdlTDZHam0QKx64Zs0vmgzUsNyadEPuEj4RjkCoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp%2BEyEAKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVhYcOF%2B&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw&existing_fsm_id=ba_EIJ2v7Sp2kVBQ9zw&host=localhost&offchain_tx=tx_%2BNILAfiEuEAEtju0XkuleWZXDkKod9xRlUlEviuSxDGRFUfFki993xabNX9%2B4KqWTbV1ghthDF4XdFTR7MfaUMTKWABuk98CuEDvYW1LiVKDYiGC%2BLR1RG6yu4v5lfjH7n8vIo2JiZLy4H9wC4o1YmelzmZdlTDZHam0QKx64Zs0vmgzUsNyadEPuEj4RjkCoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp%2BEyEAKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVhYcOF%2B&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw&existing_fsm_id=ba_Yfyxldr2BfJKgBO%2BCbmKhgM%2Fo4bRgtP8fRbUiMSHzBiCof2x&host=localhost&offchain_tx=tx_%2BNILAfiEuEAEtju0XkuleWZXDkKod9xRlUlEviuSxDGRFUfFki993xabNX9%2B4KqWTbV1ghthDF4XdFTR7MfaUMTKWABuk98CuEDvYW1LiVKDYiGC%2BLR1RG6yu4v5lfjH7n8vIo2JiZLy4H9wC4o1YmelzmZdlTDZHam0QKx64Zs0vmgzUsNyadEPuEj4RjkCoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp%2BEyEAKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVhYcOF%2B&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw&existing_fsm_id=ba_n6YEqRE9iUtt6gCwewqOh7BVBA47cHhPIIlD%2BO0CgXU%2Bgetl&host=localhost&offchain_tx=tx_%2BNILAfiEuEAEtju0XkuleWZXDkKod9xRlUlEviuSxDGRFUfFki993xabNX9%2B4KqWTbV1ghthDF4XdFTR7MfaUMTKWABuk98CuEDvYW1LiVKDYiGC%2BLR1RG6yu4v5lfjH7n8vIo2JiZLy4H9wC4o1YmelzmZdlTDZHam0QKx64Zs0vmgzUsNyadEPuEj4RjkCoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp%2BEyEAKgR4eJr1Eo%2FWhWyGnzm3q%2Bzgb1Lwx%2BY5tmHyBi7sMEIVhYcOF%2B&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_n6YEqRE9iUtt6gCwewqOh7BVBA47cHhPIIlD+O0CgXU+getl"
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBogFWHYd7q7nfmsmNrNDjSNLIiYFosR8Ms0+gQmn4TIQoQHBD5/cGFtlnlIqD3NGoraAFIZ+AMf/cQWhWwLKznY4zIY2kdavwACGG0jrV+AAAIYSMJzlQAAFx3+PdA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422994,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAq2ANmFi+odCsFZ2+2FnEbyvUyNfeKtqzfQTfAN1IQmEnftLr+2fpGLeVDVbgJlDlOimH5+b04RAKFMT3DcCQEuF/4XTUBoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEKEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAABS5gF44="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
  "id": -576460752303422994,
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAq2ANmFi+odCsFZ2+2FnEbyvUyNfeKtqzfQTfAN1IQmEnftLr+2fpGLeVDVbgJlDlOimH5+b04RAKFMT3DcCQEuF/4XTUBoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEKEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAABS5gF44=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422993,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAMSCNkPq5lOFD2SuWP+Xbhci8f5ARci3+JrkvlEWm51BohvXm2RwBrIYcygc9X6Tc1yJPm4b3zbkuz52O0LqEBuEAq2ANmFi+odCsFZ2+2FnEbyvUyNfeKtqzfQTfAN1IQmEnftLr+2fpGLeVDVbgJlDlOimH5+b04RAKFMT3DcCQEuF/4XTUBoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEKEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAABUa4iPE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
  "id": -576460752303422993,
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAMSCNkPq5lOFD2SuWP+Xbhci8f5ARci3+JrkvlEWm51BohvXm2RwBrIYcygc9X6Tc1yJPm4b3zbkuz52O0LqEBuEAq2ANmFi+odCsFZ2+2FnEbyvUyNfeKtqzfQTfAN1IQmEnftLr+2fpGLeVDVbgJlDlOimH5+b04RAKFMT3DcCQEuF/4XTUBoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEKEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAABUa4iPE=",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAMSCNkPq5lOFD2SuWP+Xbhci8f5ARci3+JrkvlEWm51BohvXm2RwBrIYcygc9X6Tc1yJPm4b3zbkuz52O0LqEBuEAq2ANmFi+odCsFZ2+2FnEbyvUyNfeKtqzfQTfAN1IQmEnftLr+2fpGLeVDVbgJlDlOimH5+b04RAKFMT3DcCQEuF/4XTUBoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEKEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAABUa4iPE=",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAMSCNkPq5lOFD2SuWP+Xbhci8f5ARci3+JrkvlEWm51BohvXm2RwBrIYcygc9X6Tc1yJPm4b3zbkuz52O0LqEBuEAq2ANmFi+odCsFZ2+2FnEbyvUyNfeKtqzfQTfAN1IQmEnftLr+2fpGLeVDVbgJlDlOimH5+b04RAKFMT3DcCQEuF/4XTUBoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEKEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAABUa4iPE=",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAMSCNkPq5lOFD2SuWP+Xbhci8f5ARci3+JrkvlEWm51BohvXm2RwBrIYcygc9X6Tc1yJPm4b3zbkuz52O0LqEBuEAq2ANmFi+odCsFZ2+2FnEbyvUyNfeKtqzfQTfAN1IQmEnftLr+2fpGLeVDVbgJlDlOimH5+b04RAKFMT3DcCQEuF/4XTUBoQaIBVh2He6u535rJjazQ40jSyImBaLEfDLNPoEJp+EyEKEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGNpHWr8AAhhtI61fgAACGEjCc5UAABUa4iPE=",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
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
    "channel_id": "ch_22uUJvzCuCJb4FnN9aRQeYDHUNSMqwJ69S6eANZLtPxJzhiqaw",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
