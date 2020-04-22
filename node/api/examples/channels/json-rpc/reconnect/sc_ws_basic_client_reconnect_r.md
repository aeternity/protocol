
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
      "fsm_id": "ba_MsyEJ+HzxuXMBs6/Dk9DC12WlRdLbXYpMlQ0OCVajDAhE6Fb"
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
      "fsm_id": "ba_cQiEQGZ/G5WoXg5o0uLYscwXGrxa+WPteqFwxZ7xsmEctG4/"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhATqYQ8+Cp4ie+LkalvZGF7tP6RNZa6xgqEYh5ntBXdojhj+qJSJgAKEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGJGE5yoAAAgoAhhAGeddIAMCgREYAn9gt2fSx6P2d51pzkXMksF9cpLYZ/pl2oteKAW8DiTrXxw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422689,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB+R5siZdD7yxbfN7HFhp6fo2poDy4+liheIdGr8DC0ni7MB76/SEqVIIjHGGPnt5g+bN/AJUUD/lpBIhgbsL8EuIP4gTIBoQE6mEPPgqeInvi5Gpb2Rhe7T+kTWWusYKhGIeZ7QV3aI4Y/qiUiYAChAYOpDt3EU/y+hQJt+QjFEoxM7RDeN41NWLsSM7ymIQhYhiRhOcqAAAIKAIYQBnnXSADAoERGAJ/YLdn0sej9nedac5FzJLBfXKS2Gf6ZdqLXigFvA/NohKo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422689,
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_cQiEQGZ/G5WoXg5o0uLYscwXGrxa+WPteqFwxZ7xsmEctG4/"
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEB+R5siZdD7yxbfN7HFhp6fo2poDy4+liheIdGr8DC0ni7MB76/SEqVIIjHGGPnt5g+bN/AJUUD/lpBIhgbsL8EuIP4gTIBoQE6mEPPgqeInvi5Gpb2Rhe7T+kTWWusYKhGIeZ7QV3aI4Y/qiUiYAChAYOpDt3EU/y+hQJt+QjFEoxM7RDeN41NWLsSM7ymIQhYhiRhOcqAAAIKAIYQBnnXSADAoERGAJ/YLdn0sej9nedac5FzJLBfXKS2Gf6ZdqLXigFvA/NohKo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422688,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAfkebImXQ+8sW3zexxYaen6NqaA8uPpYoXiHRq/AwtJ4uzAe+v0hKlSCIxxhj57eYPmzfwCVFA/5aQSIYG7C/BLhAy8gRoLS5Zr50wFZlbq7oS17SgYg51Gxp6XiC/zDpH4fOl8tMBSu2NPV5V0adQaaF8W+0wZOCy3OhvXdv74WBCbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwMda4R9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
  "id": -576460752303422688,
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAfkebImXQ+8sW3zexxYaen6NqaA8uPpYoXiHRq/AwtJ4uzAe+v0hKlSCIxxhj57eYPmzfwCVFA/5aQSIYG7C/BLhAy8gRoLS5Zr50wFZlbq7oS17SgYg51Gxp6XiC/zDpH4fOl8tMBSu2NPV5V0adQaaF8W+0wZOCy3OhvXdv74WBCbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwMda4R9",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_MsyEJ+HzxuXMBs6/Dk9DC12WlRdLbXYpMlQ0OCVajDAhE6Fb"
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAfkebImXQ+8sW3zexxYaen6NqaA8uPpYoXiHRq/AwtJ4uzAe+v0hKlSCIxxhj57eYPmzfwCVFA/5aQSIYG7C/BLhAy8gRoLS5Zr50wFZlbq7oS17SgYg51Gxp6XiC/zDpH4fOl8tMBSu2NPV5V0adQaaF8W+0wZOCy3OhvXdv74WBCbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwMda4R9",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAfkebImXQ+8sW3zexxYaen6NqaA8uPpYoXiHRq/AwtJ4uzAe+v0hKlSCIxxhj57eYPmzfwCVFA/5aQSIYG7C/BLhAy8gRoLS5Zr50wFZlbq7oS17SgYg51Gxp6XiC/zDpH4fOl8tMBSu2NPV5V0adQaaF8W+0wZOCy3OhvXdv74WBCbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwMda4R9",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAfkebImXQ+8sW3zexxYaen6NqaA8uPpYoXiHRq/AwtJ4uzAe+v0hKlSCIxxhj57eYPmzfwCVFA/5aQSIYG7C/BLhAy8gRoLS5Zr50wFZlbq7oS17SgYg51Gxp6XiC/zDpH4fOl8tMBSu2NPV5V0adQaaF8W+0wZOCy3OhvXdv74WBCbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwMda4R9",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "message": {
        "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "message": {
        "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
  "id": -576460752303422687,
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
  "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
  "id": -576460752303422687,
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "state": "tx_+QENCwH4hLhAfkebImXQ+8sW3zexxYaen6NqaA8uPpYoXiHRq/AwtJ4uzAe+v0hKlSCIxxhj57eYPmzfwCVFA/5aQSIYG7C/BLhAy8gRoLS5Zr50wFZlbq7oS17SgYg51Gxp6XiC/zDpH4fOl8tMBSu2NPV5V0adQaaF8W+0wZOCy3OhvXdv74WBCbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwMda4R9"
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "state": "tx_+QENCwH4hLhAfkebImXQ+8sW3zexxYaen6NqaA8uPpYoXiHRq/AwtJ4uzAe+v0hKlSCIxxhj57eYPmzfwCVFA/5aQSIYG7C/BLhAy8gRoLS5Zr50wFZlbq7oS17SgYg51Gxp6XiC/zDpH4fOl8tMBSu2NPV5V0adQaaF8W+0wZOCy3OhvXdv74WBCbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwMda4R9"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2",
    "to": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpfPOQt9EMQhETZKwfkfwwc8onSwLPif55+tA8ABbg0tAqCqgPsDPo8+16WFY9cSElD1/Lhya0V2JJ+06z9Yp+GUwsnOFBc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2",
          "op": "OffChainTransfer",
          "to": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC3rzPNkRpXr+WVz70fnPYGjgtSPL4ViYxZexQYeoCzdJXOYuNQltY8zrH78du76JQ8UWV9nTjFAz2hyKm/M5oLuEj4RjkCoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLQKgqoD7Az6PPtelhWPXEhJQ9fy4cmtFdiSftOs/WKfhlMKTQM48"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
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
    "from": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2",
    "to": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpfPOQt9EMQhETZKwfkfwwc8onSwLPif55+tA8ABbg0tAqCqgPsDPo8+16WFY9cSElD1/Lhya0V2JJ+06z9Yp+GUwsnOFBc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Soj4M7ojYxbWvNf8vNYSZZ9TnMWL7r4sF2wUmktKdc8qqC1w2",
          "op": "OffChainTransfer",
          "to": "ak_zz66HmMbYFXsfeo6f576yHyCk39sMKSFtbaxP9SyebwfczbYR"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuECpv0vIQrLVfHcYgq7sHVcq+CDmHBPFIzKkpKbD1jQucC8GBt+bEnRXfpHby860c01F8Yr90jYgSdLIhkxZYGYEuEC3rzPNkRpXr+WVz70fnPYGjgtSPL4ViYxZexQYeoCzdJXOYuNQltY8zrH78du76JQ8UWV9nTjFAz2hyKm/M5oLuEj4RjkCoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLQKgqoD7Az6PPtelhWPXEhJQ9fy4cmtFdiSftOs/WKfhlMLcwEpr"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "state": "tx_+NILAfiEuECpv0vIQrLVfHcYgq7sHVcq+CDmHBPFIzKkpKbD1jQucC8GBt+bEnRXfpHby860c01F8Yr90jYgSdLIhkxZYGYEuEC3rzPNkRpXr+WVz70fnPYGjgtSPL4ViYxZexQYeoCzdJXOYuNQltY8zrH78du76JQ8UWV9nTjFAz2hyKm/M5oLuEj4RjkCoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLQKgqoD7Az6PPtelhWPXEhJQ9fy4cmtFdiSftOs/WKfhlMLcwEpr"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC&host=localhost&offchain_tx=tx_%2BNILAfiEuECpv0vIQrLVfHcYgq7sHVcq%2BCDmHBPFIzKkpKbD1jQucC8GBt%2BbEnRXfpHby860c01F8Yr90jYgSdLIhkxZYGYEuEC3rzPNkRpXr%2BWVz70fnPYGjgtSPL4ViYxZexQYeoCzdJXOYuNQltY8zrH78du76JQ8UWV9nTjFAz2hyKm%2FM5oLuEj4RjkCoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n%2BefrQPAAW4NLQKgqoD7Az6PPtelhWPXEhJQ9fy4cmtFdiSftOs%2FWKfhlMLcwEpr&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuECpv0vIQrLVfHcYgq7sHVcq%2BCDmHBPFIzKkpKbD1jQucC8GBt%2BbEnRXfpHby860c01F8Yr90jYgSdLIhkxZYGYEuEC3rzPNkRpXr%2BWVz70fnPYGjgtSPL4ViYxZexQYeoCzdJXOYuNQltY8zrH78du76JQ8UWV9nTjFAz2hyKm%2FM5oLuEj4RjkCoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n%2BefrQPAAW4NLQKgqoD7Az6PPtelhWPXEhJQ9fy4cmtFdiSftOs%2FWKfhlMLcwEpr&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC&existing_fsm_id=ba_0l8E77UMjdvRtTsx&host=localhost&offchain_tx=tx_%2BNILAfiEuECpv0vIQrLVfHcYgq7sHVcq%2BCDmHBPFIzKkpKbD1jQucC8GBt%2BbEnRXfpHby860c01F8Yr90jYgSdLIhkxZYGYEuEC3rzPNkRpXr%2BWVz70fnPYGjgtSPL4ViYxZexQYeoCzdJXOYuNQltY8zrH78du76JQ8UWV9nTjFAz2hyKm%2FM5oLuEj4RjkCoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n%2BefrQPAAW4NLQKgqoD7Az6PPtelhWPXEhJQ9fy4cmtFdiSftOs%2FWKfhlMLcwEpr&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC&existing_fsm_id=ba_KhTOHOVl3M8xvXcfbJWs4t5asEPIrJcDgsw9t9PyiFJ%2FZPT6&host=localhost&offchain_tx=tx_%2BNILAfiEuECpv0vIQrLVfHcYgq7sHVcq%2BCDmHBPFIzKkpKbD1jQucC8GBt%2BbEnRXfpHby860c01F8Yr90jYgSdLIhkxZYGYEuEC3rzPNkRpXr%2BWVz70fnPYGjgtSPL4ViYxZexQYeoCzdJXOYuNQltY8zrH78du76JQ8UWV9nTjFAz2hyKm%2FM5oLuEj4RjkCoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n%2BefrQPAAW4NLQKgqoD7Az6PPtelhWPXEhJQ9fy4cmtFdiSftOs%2FWKfhlMLcwEpr&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC&existing_fsm_id=ba_cQiEQGZ%2FG5WoXg5o0uLYscwXGrxa%2BWPteqFwxZ7xsmEctG4%2F&offchain_tx=tx_%2BNILAfiEuECpv0vIQrLVfHcYgq7sHVcq%2BCDmHBPFIzKkpKbD1jQucC8GBt%2BbEnRXfpHby860c01F8Yr90jYgSdLIhkxZYGYEuEC3rzPNkRpXr%2BWVz70fnPYGjgtSPL4ViYxZexQYeoCzdJXOYuNQltY8zrH78du76JQ8UWV9nTjFAz2hyKm%2FM5oLuEj4RjkCoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n%2BefrQPAAW4NLQKgqoD7Az6PPtelhWPXEhJQ9fy4cmtFdiSftOs%2FWKfhlMLcwEpr&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_cQiEQGZ/G5WoXg5o0uLYscwXGrxa+WPteqFwxZ7xsmEctG4/"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBpfPOQt9EMQhETZKwfkfwwc8onSwLPif55+tA8ABbg0toQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIY3+rniy/6GHLHOiuwCAIYPXtZ/KAABajAfpQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422686,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDmJGV4IgldfVk/ufTgZ1tTLUwjedbToRFzMgGPE9wIUrfb5o2SPZ8a/8cKS+HgXN8ViSFC+BKOCQjlaXc9HHsFuF/4XTUBoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLaEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGN/q54sv+hhyxzorsAgCGD17WfygAAZXoobc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
  "id": -576460752303422686,
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDmJGV4IgldfVk/ufTgZ1tTLUwjedbToRFzMgGPE9wIUrfb5o2SPZ8a/8cKS+HgXN8ViSFC+BKOCQjlaXc9HHsFuF/4XTUBoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLaEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGN/q54sv+hhyxzorsAgCGD17WfygAAZXoobc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422685,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEDWEcgcV5ufboZvZd0nCdBeFpNkjgWm5OxcJCHLcCS2vGxcMX3tQH2ywcLGBCMOhTr9XoWmOkhb1DSUwjh3P6YCuEDmJGV4IgldfVk/ufTgZ1tTLUwjedbToRFzMgGPE9wIUrfb5o2SPZ8a/8cKS+HgXN8ViSFC+BKOCQjlaXc9HHsFuF/4XTUBoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLaEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGN/q54sv+hhyxzorsAgCGD17WfygAAU8EWLI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
  "id": -576460752303422685,
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEDWEcgcV5ufboZvZd0nCdBeFpNkjgWm5OxcJCHLcCS2vGxcMX3tQH2ywcLGBCMOhTr9XoWmOkhb1DSUwjh3P6YCuEDmJGV4IgldfVk/ufTgZ1tTLUwjedbToRFzMgGPE9wIUrfb5o2SPZ8a/8cKS+HgXN8ViSFC+BKOCQjlaXc9HHsFuF/4XTUBoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLaEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGN/q54sv+hhyxzorsAgCGD17WfygAAU8EWLI=",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEDWEcgcV5ufboZvZd0nCdBeFpNkjgWm5OxcJCHLcCS2vGxcMX3tQH2ywcLGBCMOhTr9XoWmOkhb1DSUwjh3P6YCuEDmJGV4IgldfVk/ufTgZ1tTLUwjedbToRFzMgGPE9wIUrfb5o2SPZ8a/8cKS+HgXN8ViSFC+BKOCQjlaXc9HHsFuF/4XTUBoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLaEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGN/q54sv+hhyxzorsAgCGD17WfygAAU8EWLI=",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEDWEcgcV5ufboZvZd0nCdBeFpNkjgWm5OxcJCHLcCS2vGxcMX3tQH2ywcLGBCMOhTr9XoWmOkhb1DSUwjh3P6YCuEDmJGV4IgldfVk/ufTgZ1tTLUwjedbToRFzMgGPE9wIUrfb5o2SPZ8a/8cKS+HgXN8ViSFC+BKOCQjlaXc9HHsFuF/4XTUBoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLaEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGN/q54sv+hhyxzorsAgCGD17WfygAAU8EWLI=",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEDWEcgcV5ufboZvZd0nCdBeFpNkjgWm5OxcJCHLcCS2vGxcMX3tQH2ywcLGBCMOhTr9XoWmOkhb1DSUwjh3P6YCuEDmJGV4IgldfVk/ufTgZ1tTLUwjedbToRFzMgGPE9wIUrfb5o2SPZ8a/8cKS+HgXN8ViSFC+BKOCQjlaXc9HHsFuF/4XTUBoQaXzzkLfRDEIRE2SsH5H8MHPKJ0sCz4n+efrQPAAW4NLaEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGN/q54sv+hhyxzorsAgCGD17WfygAAU8EWLI=",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
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
    "channel_id": "ch_29rmbxczEmFWBx2JFjD2S8YkhPULNwdUFe6NoZuM3HSA1fEKPC",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
