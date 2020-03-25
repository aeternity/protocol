
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR&role=initiator
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
      "fsm_id": "ba_bj/TtKh8m7fG956Heuw+67xOZAXmZmiBd+uM8JqoRsQ1ZvlG"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR&role=responder
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
      "fsm_id": "ba_waZ0h5l/zIVpOoZ+YyZ3r7grIaVGGPj+6k4ZtGND3bpDvdSY"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhATqYQ8+Cp4ie+LkalvZGF7tP6RNZa6xgqEYh5ntBXdojhj+qJSJgAKEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGJGE5yoAAAgoAhhAGeddIAMCgREYAn9gt2fSx6P2d51pzkXMksF9cpLYZ/pl2oteKAW8EMxAXrw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422684,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEC/WAvm8afYjVrDmAucrbdxD2hWHv2UTqM8RC94nKFZpQDAdLm0NPzgJK4alG+TIcsATJ1kxWKZVzYUXTMpZfoPuIP4gTIBoQE6mEPPgqeInvi5Gpb2Rhe7T+kTWWusYKhGIeZ7QV3aI4Y/qiUiYAChAYOpDt3EU/y+hQJt+QjFEoxM7RDeN41NWLsSM7ymIQhYhiRhOcqAAAIKAIYQBnnXSADAoERGAJ/YLdn0sej9nedac5FzJLBfXKS2Gf6ZdqLXigFvBALJWuM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422684,
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_waZ0h5l/zIVpOoZ+YyZ3r7grIaVGGPj+6k4ZtGND3bpDvdSY"
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEC/WAvm8afYjVrDmAucrbdxD2hWHv2UTqM8RC94nKFZpQDAdLm0NPzgJK4alG+TIcsATJ1kxWKZVzYUXTMpZfoPuIP4gTIBoQE6mEPPgqeInvi5Gpb2Rhe7T+kTWWusYKhGIeZ7QV3aI4Y/qiUiYAChAYOpDt3EU/y+hQJt+QjFEoxM7RDeN41NWLsSM7ymIQhYhiRhOcqAAAIKAIYQBnnXSADAoERGAJ/YLdn0sej9nedac5FzJLBfXKS2Gf6ZdqLXigFvBALJWuM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422683,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAv1gL5vGn2I1aw5gLnK23cQ9oVh79lE6jPEQveJyhWaUAwHS5tDT84CSuGpRvkyHLAEydZMVimVc2FF0zKWX6D7hA9VShoER5wThEjeS480PCTgD0VdOTtUyvioPXwZ1rZIgicQGGe8B9r8eN4Rxke25cEzKpqxhg26ieV805VpaAC7iD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwS9oHRo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
  "id": -576460752303422683,
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAv1gL5vGn2I1aw5gLnK23cQ9oVh79lE6jPEQveJyhWaUAwHS5tDT84CSuGpRvkyHLAEydZMVimVc2FF0zKWX6D7hA9VShoER5wThEjeS480PCTgD0VdOTtUyvioPXwZ1rZIgicQGGe8B9r8eN4Rxke25cEzKpqxhg26ieV805VpaAC7iD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwS9oHRo",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_bj/TtKh8m7fG956Heuw+67xOZAXmZmiBd+uM8JqoRsQ1ZvlG"
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAv1gL5vGn2I1aw5gLnK23cQ9oVh79lE6jPEQveJyhWaUAwHS5tDT84CSuGpRvkyHLAEydZMVimVc2FF0zKWX6D7hA9VShoER5wThEjeS480PCTgD0VdOTtUyvioPXwZ1rZIgicQGGe8B9r8eN4Rxke25cEzKpqxhg26ieV805VpaAC7iD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwS9oHRo",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAv1gL5vGn2I1aw5gLnK23cQ9oVh79lE6jPEQveJyhWaUAwHS5tDT84CSuGpRvkyHLAEydZMVimVc2FF0zKWX6D7hA9VShoER5wThEjeS480PCTgD0VdOTtUyvioPXwZ1rZIgicQGGe8B9r8eN4Rxke25cEzKpqxhg26ieV805VpaAC7iD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwS9oHRo",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAv1gL5vGn2I1aw5gLnK23cQ9oVh79lE6jPEQveJyhWaUAwHS5tDT84CSuGpRvkyHLAEydZMVimVc2FF0zKWX6D7hA9VShoER5wThEjeS480PCTgD0VdOTtUyvioPXwZ1rZIgicQGGe8B9r8eN4Rxke25cEzKpqxhg26ieV805VpaAC7iD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwS9oHRo",
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
    "to": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "message": {
        "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
        "from": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2",
        "info": "Hello",
        "to": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR"
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
    "to": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "message": {
        "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
        "from": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR",
        "info": "Hello back",
        "to": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422682,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2",
      "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
  "id": -576460752303422682,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2",
      "balance": 69999999999999
    },
    {
      "account": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "state": "tx_+QENCwH4hLhAv1gL5vGn2I1aw5gLnK23cQ9oVh79lE6jPEQveJyhWaUAwHS5tDT84CSuGpRvkyHLAEydZMVimVc2FF0zKWX6D7hA9VShoER5wThEjeS480PCTgD0VdOTtUyvioPXwZ1rZIgicQGGe8B9r8eN4Rxke25cEzKpqxhg26ieV805VpaAC7iD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwS9oHRo"
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "state": "tx_+QENCwH4hLhAv1gL5vGn2I1aw5gLnK23cQ9oVh79lE6jPEQveJyhWaUAwHS5tDT84CSuGpRvkyHLAEydZMVimVc2FF0zKWX6D7hA9VShoER5wThEjeS480PCTgD0VdOTtUyvioPXwZ1rZIgicQGGe8B9r8eN4Rxke25cEzKpqxhg26ieV805VpaAC7iD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwS9oHRo"
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
    "from": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR",
    "to": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjll28aZRDf7pqykk+2AzhRAdV9zWB66AqDNuerx/4LJAqDR3cmi3w18lIQILNh13fJV4Rcs7IMEtoknxCDt9O0vkzrDNHA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR",
          "op": "OffChainTransfer",
          "to": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2"
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
    "signed_tx": "tx_+JALAfhCuEC9ahRqSO0QinMGRQg8ea8Nqqp5TYVBdc9jzxH3WXz6mNas3QAtJR500IHTV+U8N9ZGhTkkkcpnEaXK+pK2WwkDuEj4RjkCoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyQKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5Nj+YVv"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "from": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR",
    "to": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjll28aZRDf7pqykk+2AzhRAdV9zWB66AqDNuerx/4LJAqDR3cmi3w18lIQILNh13fJV4Rcs7IMEtoknxCDt9O0vkzrDNHA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR",
          "op": "OffChainTransfer",
          "to": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2"
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
    "signed_tx": "tx_+NILAfiEuEAiEQ8qqRJNvUV9G3xWTzjJ0N2KrgVZ1BQGMjWw3pmPZpeNnvHhhy2yvZ70Cn2AdjspmvVDnAJBg80Qu1kIc6MOuEC9ahRqSO0QinMGRQg8ea8Nqqp5TYVBdc9jzxH3WXz6mNas3QAtJR500IHTV+U8N9ZGhTkkkcpnEaXK+pK2WwkDuEj4RjkCoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyQKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5OobhL7"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "state": "tx_+NILAfiEuEAiEQ8qqRJNvUV9G3xWTzjJ0N2KrgVZ1BQGMjWw3pmPZpeNnvHhhy2yvZ70Cn2AdjspmvVDnAJBg80Qu1kIc6MOuEC9ahRqSO0QinMGRQg8ea8Nqqp5TYVBdc9jzxH3WXz6mNas3QAtJR500IHTV+U8N9ZGhTkkkcpnEaXK+pK2WwkDuEj4RjkCoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyQKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5OobhL7"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1&host=localhost&offchain_tx=tx_%2BNILAfiEuEAiEQ8qqRJNvUV9G3xWTzjJ0N2KrgVZ1BQGMjWw3pmPZpeNnvHhhy2yvZ70Cn2AdjspmvVDnAJBg80Qu1kIc6MOuEC9ahRqSO0QinMGRQg8ea8Nqqp5TYVBdc9jzxH3WXz6mNas3QAtJR500IHTV%2BU8N9ZGhTkkkcpnEaXK%2BpK2WwkDuEj4RjkCoQY5ZdvGmUQ3%2B6aspJPtgM4UQHVfc1geugKgzbnq8f%2BCyQKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5OobhL7&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuEAiEQ8qqRJNvUV9G3xWTzjJ0N2KrgVZ1BQGMjWw3pmPZpeNnvHhhy2yvZ70Cn2AdjspmvVDnAJBg80Qu1kIc6MOuEC9ahRqSO0QinMGRQg8ea8Nqqp5TYVBdc9jzxH3WXz6mNas3QAtJR500IHTV%2BU8N9ZGhTkkkcpnEaXK%2BpK2WwkDuEj4RjkCoQY5ZdvGmUQ3%2B6aspJPtgM4UQHVfc1geugKgzbnq8f%2BCyQKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5OobhL7&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1&existing_fsm_id=ba_q3azvTmBt%2BLJreNW&host=localhost&offchain_tx=tx_%2BNILAfiEuEAiEQ8qqRJNvUV9G3xWTzjJ0N2KrgVZ1BQGMjWw3pmPZpeNnvHhhy2yvZ70Cn2AdjspmvVDnAJBg80Qu1kIc6MOuEC9ahRqSO0QinMGRQg8ea8Nqqp5TYVBdc9jzxH3WXz6mNas3QAtJR500IHTV%2BU8N9ZGhTkkkcpnEaXK%2BpK2WwkDuEj4RjkCoQY5ZdvGmUQ3%2B6aspJPtgM4UQHVfc1geugKgzbnq8f%2BCyQKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5OobhL7&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1&existing_fsm_id=ba_pJm%2FqAz6e6REzw%2FAupFFK0%2FL0BWMc17PzmKPCYc2Vg1zgy3j&host=localhost&offchain_tx=tx_%2BNILAfiEuEAiEQ8qqRJNvUV9G3xWTzjJ0N2KrgVZ1BQGMjWw3pmPZpeNnvHhhy2yvZ70Cn2AdjspmvVDnAJBg80Qu1kIc6MOuEC9ahRqSO0QinMGRQg8ea8Nqqp5TYVBdc9jzxH3WXz6mNas3QAtJR500IHTV%2BU8N9ZGhTkkkcpnEaXK%2BpK2WwkDuEj4RjkCoQY5ZdvGmUQ3%2B6aspJPtgM4UQHVfc1geugKgzbnq8f%2BCyQKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5OobhL7&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1&existing_fsm_id=ba_bj%2FTtKh8m7fG956Heuw%2B67xOZAXmZmiBd%2BuM8JqoRsQ1ZvlG&host=localhost&offchain_tx=tx_%2BNILAfiEuEAiEQ8qqRJNvUV9G3xWTzjJ0N2KrgVZ1BQGMjWw3pmPZpeNnvHhhy2yvZ70Cn2AdjspmvVDnAJBg80Qu1kIc6MOuEC9ahRqSO0QinMGRQg8ea8Nqqp5TYVBdc9jzxH3WXz6mNas3QAtJR500IHTV%2BU8N9ZGhTkkkcpnEaXK%2BpK2WwkDuEj4RjkCoQY5ZdvGmUQ3%2B6aspJPtgM4UQHVfc1geugKgzbnq8f%2BCyQKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5OobhL7&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_bj/TtKh8m7fG956Heuw+67xOZAXmZmiBd+uM8JqoRsQ1ZvlG"
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBjll28aZRDf7pqykk+2AzhRAdV9zWB66AqDNuerx/4LJoQE6mEPPgqeInvi5Gpb2Rhe7T+kTWWusYKhGIeZ7QV3aI4Y3+rnizACGHLHOiuwAAIYPXtZ/KAAFEwjv0Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422681,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDwPH3/PlmdPcqGO8U20NR3XPSsmefJ5OiWWkr4RLRA6LSnK6CskLb7bMdeAb+rHpW8TZ2biOkXvHaK349FSpQJuF/4XTUBoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygABWV6sN4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
  "id": -576460752303422681,
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDwPH3/PlmdPcqGO8U20NR3XPSsmefJ5OiWWkr4RLRA6LSnK6CskLb7bMdeAb+rHpW8TZ2biOkXvHaK349FSpQJuF/4XTUBoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygABWV6sN4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422680,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBL0XYdWr0sK4yQEUtTBaDcG9R55st+ZjsYX+SdDoZMG476AeYwk9cR4osZ1VVaJKLHslv9/+R0mY5bdBIlj4AEuEDwPH3/PlmdPcqGO8U20NR3XPSsmefJ5OiWWkr4RLRA6LSnK6CskLb7bMdeAb+rHpW8TZ2biOkXvHaK349FSpQJuF/4XTUBoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygABV/JO4U="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
  "id": -576460752303422680,
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBL0XYdWr0sK4yQEUtTBaDcG9R55st+ZjsYX+SdDoZMG476AeYwk9cR4osZ1VVaJKLHslv9/+R0mY5bdBIlj4AEuEDwPH3/PlmdPcqGO8U20NR3XPSsmefJ5OiWWkr4RLRA6LSnK6CskLb7bMdeAb+rHpW8TZ2biOkXvHaK349FSpQJuF/4XTUBoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygABV/JO4U=",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBL0XYdWr0sK4yQEUtTBaDcG9R55st+ZjsYX+SdDoZMG476AeYwk9cR4osZ1VVaJKLHslv9/+R0mY5bdBIlj4AEuEDwPH3/PlmdPcqGO8U20NR3XPSsmefJ5OiWWkr4RLRA6LSnK6CskLb7bMdeAb+rHpW8TZ2biOkXvHaK349FSpQJuF/4XTUBoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygABV/JO4U=",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBL0XYdWr0sK4yQEUtTBaDcG9R55st+ZjsYX+SdDoZMG476AeYwk9cR4osZ1VVaJKLHslv9/+R0mY5bdBIlj4AEuEDwPH3/PlmdPcqGO8U20NR3XPSsmefJ5OiWWkr4RLRA6LSnK6CskLb7bMdeAb+rHpW8TZ2biOkXvHaK349FSpQJuF/4XTUBoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygABV/JO4U=",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBL0XYdWr0sK4yQEUtTBaDcG9R55st+ZjsYX+SdDoZMG476AeYwk9cR4osZ1VVaJKLHslv9/+R0mY5bdBIlj4AEuEDwPH3/PlmdPcqGO8U20NR3XPSsmefJ5OiWWkr4RLRA6LSnK6CskLb7bMdeAb+rHpW8TZ2biOkXvHaK349FSpQJuF/4XTUBoQY5ZdvGmUQ3+6aspJPtgM4UQHVfc1geugKgzbnq8f+CyaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygABV/JO4U=",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
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
    "channel_id": "ch_SH9p6PqipHNPnMaiFauo9k5w9EyqviG5qdpNkwRieaFZ1YHs1",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
