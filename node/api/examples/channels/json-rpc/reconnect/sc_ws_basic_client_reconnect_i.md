
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
      "fsm_id": "ba_YAUVSBPgiAJf3E3bcHCIrTcvZ+LRcVTfs4ysj5ILNpM1KFtF"
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
      "fsm_id": "ba_CkCo46IJQIWE9aXERwx/NtNKEBv6r0AcXd1QJVuAYelF4QC3"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhATqYQ8+Cp4ie+LkalvZGF7tP6RNZa6xgqEYh5ntBXdojhj+qJSJgAKEBg6kO3cRT/L6FAm35CMUSjEztEN43jU1YuxIzvKYhCFiGJGE5yoAAAgoAhhAGeddIAMCgREYAn9gt2fSx6P2d51pzkXMksF9cpLYZ/pl2oteKAW8BhypXAg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422694,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDn+KaTHwcTP9+9iyvAUh+ekzG7uAwtAIcjs2XPca1zZNWccvOrzypXaV6uiwtYoensUCbe6jvKdTYL04CLi4MFuIP4gTIBoQE6mEPPgqeInvi5Gpb2Rhe7T+kTWWusYKhGIeZ7QV3aI4Y/qiUiYAChAYOpDt3EU/y+hQJt+QjFEoxM7RDeN41NWLsSM7ymIQhYhiRhOcqAAAIKAIYQBnnXSADAoERGAJ/YLdn0sej9nedac5FzJLBfXKS2Gf6ZdqLXigFvAQY8GoY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422694,
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_CkCo46IJQIWE9aXERwx/NtNKEBv6r0AcXd1QJVuAYelF4QC3"
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDn+KaTHwcTP9+9iyvAUh+ekzG7uAwtAIcjs2XPca1zZNWccvOrzypXaV6uiwtYoensUCbe6jvKdTYL04CLi4MFuIP4gTIBoQE6mEPPgqeInvi5Gpb2Rhe7T+kTWWusYKhGIeZ7QV3aI4Y/qiUiYAChAYOpDt3EU/y+hQJt+QjFEoxM7RDeN41NWLsSM7ymIQhYhiRhOcqAAAIKAIYQBnnXSADAoERGAJ/YLdn0sej9nedac5FzJLBfXKS2Gf6ZdqLXigFvAQY8GoY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422693,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhADC4z9F34Pi95uk/YqsY7m75HQyFKB6pGxcZSZjqGwg4STkoO1jsqsfMVJDipcaWzoWWZ9/G3emfsawjSwRwbALhA5/imkx8HEz/fvYsrwFIfnpMxu7gMLQCHI7Nlz3Gtc2TVnHLzq88qV2lerosLWKHp7FAm3uo7ynU2C9OAi4uDBbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwGxjl2u"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
  "id": -576460752303422693,
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhADC4z9F34Pi95uk/YqsY7m75HQyFKB6pGxcZSZjqGwg4STkoO1jsqsfMVJDipcaWzoWWZ9/G3emfsawjSwRwbALhA5/imkx8HEz/fvYsrwFIfnpMxu7gMLQCHI7Nlz3Gtc2TVnHLzq88qV2lerosLWKHp7FAm3uo7ynU2C9OAi4uDBbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwGxjl2u",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_YAUVSBPgiAJf3E3bcHCIrTcvZ+LRcVTfs4ysj5ILNpM1KFtF"
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhADC4z9F34Pi95uk/YqsY7m75HQyFKB6pGxcZSZjqGwg4STkoO1jsqsfMVJDipcaWzoWWZ9/G3emfsawjSwRwbALhA5/imkx8HEz/fvYsrwFIfnpMxu7gMLQCHI7Nlz3Gtc2TVnHLzq88qV2lerosLWKHp7FAm3uo7ynU2C9OAi4uDBbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwGxjl2u",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhADC4z9F34Pi95uk/YqsY7m75HQyFKB6pGxcZSZjqGwg4STkoO1jsqsfMVJDipcaWzoWWZ9/G3emfsawjSwRwbALhA5/imkx8HEz/fvYsrwFIfnpMxu7gMLQCHI7Nlz3Gtc2TVnHLzq88qV2lerosLWKHp7FAm3uo7ynU2C9OAi4uDBbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwGxjl2u",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhADC4z9F34Pi95uk/YqsY7m75HQyFKB6pGxcZSZjqGwg4STkoO1jsqsfMVJDipcaWzoWWZ9/G3emfsawjSwRwbALhA5/imkx8HEz/fvYsrwFIfnpMxu7gMLQCHI7Nlz3Gtc2TVnHLzq88qV2lerosLWKHp7FAm3uo7ynU2C9OAi4uDBbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwGxjl2u",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "message": {
        "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "message": {
        "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
  "id": -576460752303422692,
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
  "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
  "id": -576460752303422692,
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "state": "tx_+QENCwH4hLhADC4z9F34Pi95uk/YqsY7m75HQyFKB6pGxcZSZjqGwg4STkoO1jsqsfMVJDipcaWzoWWZ9/G3emfsawjSwRwbALhA5/imkx8HEz/fvYsrwFIfnpMxu7gMLQCHI7Nlz3Gtc2TVnHLzq88qV2lerosLWKHp7FAm3uo7ynU2C9OAi4uDBbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwGxjl2u"
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "state": "tx_+QENCwH4hLhADC4z9F34Pi95uk/YqsY7m75HQyFKB6pGxcZSZjqGwg4STkoO1jsqsfMVJDipcaWzoWWZ9/G3emfsawjSwRwbALhA5/imkx8HEz/fvYsrwFIfnpMxu7gMLQCHI7Nlz3Gtc2TVnHLzq88qV2lerosLWKHp7FAm3uo7ynU2C9OAi4uDBbiD+IEyAaEBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGP6olImAAoQGDqQ7dxFP8voUCbfkIxRKMTO0Q3jeNTVi7EjO8piEIWIYkYTnKgAACCgCGEAZ510gAwKBERgCf2C3Z9LHo/Z3nWnORcySwX1ykthn+mXai14oBbwGxjl2u"
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr15LrykRBcZV99mEGianI5coLRYYyvLCBEmkP+2p80bAqDR3cmi3w18lIQILNh13fJV4Rcs7IMEtoknxCDt9O0vk6dfRLc=",
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
    "signed_tx": "tx_+JALAfhCuEC8MFi7A2jq35dCdHoVrzWmEsN3nYF82rP9p485IpX2PNQqX5DZNKacRJuMuLUKpoLo/NLMYgdFbVHYGb+koKEDuEj4RjkCoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNGwKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5P//VO9"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr15LrykRBcZV99mEGianI5coLRYYyvLCBEmkP+2p80bAqDR3cmi3w18lIQILNh13fJV4Rcs7IMEtoknxCDt9O0vk6dfRLc=",
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
    "signed_tx": "tx_+NILAfiEuEC8MFi7A2jq35dCdHoVrzWmEsN3nYF82rP9p485IpX2PNQqX5DZNKacRJuMuLUKpoLo/NLMYgdFbVHYGb+koKEDuEDbseJIukyqkTO1CyqyKbCLrsbnDJXPGYAFesplf+w/ZFCGoI7PJ9UkO/Mi7EmXS/ka67i60qtKKh1f9heT0zADuEj4RjkCoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNGwKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5Mat5YD"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "state": "tx_+NILAfiEuEC8MFi7A2jq35dCdHoVrzWmEsN3nYF82rP9p485IpX2PNQqX5DZNKacRJuMuLUKpoLo/NLMYgdFbVHYGb+koKEDuEDbseJIukyqkTO1CyqyKbCLrsbnDJXPGYAFesplf+w/ZFCGoI7PJ9UkO/Mi7EmXS/ka67i60qtKKh1f9heT0zADuEj4RjkCoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNGwKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5Mat5YD"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4&host=localhost&offchain_tx=tx_%2BNILAfiEuEC8MFi7A2jq35dCdHoVrzWmEsN3nYF82rP9p485IpX2PNQqX5DZNKacRJuMuLUKpoLo%2FNLMYgdFbVHYGb%2BkoKEDuEDbseJIukyqkTO1CyqyKbCLrsbnDJXPGYAFesplf%2Bw%2FZFCGoI7PJ9UkO%2FMi7EmXS%2Fka67i60qtKKh1f9heT0zADuEj4RjkCoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD%2FtqfNGwKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5Mat5YD&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuEC8MFi7A2jq35dCdHoVrzWmEsN3nYF82rP9p485IpX2PNQqX5DZNKacRJuMuLUKpoLo%2FNLMYgdFbVHYGb%2BkoKEDuEDbseJIukyqkTO1CyqyKbCLrsbnDJXPGYAFesplf%2Bw%2FZFCGoI7PJ9UkO%2FMi7EmXS%2Fka67i60qtKKh1f9heT0zADuEj4RjkCoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD%2FtqfNGwKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5Mat5YD&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4&existing_fsm_id=ba_VdRl%2BzAMvYVDGr3f&host=localhost&offchain_tx=tx_%2BNILAfiEuEC8MFi7A2jq35dCdHoVrzWmEsN3nYF82rP9p485IpX2PNQqX5DZNKacRJuMuLUKpoLo%2FNLMYgdFbVHYGb%2BkoKEDuEDbseJIukyqkTO1CyqyKbCLrsbnDJXPGYAFesplf%2Bw%2FZFCGoI7PJ9UkO%2FMi7EmXS%2Fka67i60qtKKh1f9heT0zADuEj4RjkCoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD%2FtqfNGwKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5Mat5YD&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4&existing_fsm_id=ba_MzT88xN0%2F86r5mcdZ3eGgrfLAn2h5V6cg37PxVb8SBu3%2BOmP&host=localhost&offchain_tx=tx_%2BNILAfiEuEC8MFi7A2jq35dCdHoVrzWmEsN3nYF82rP9p485IpX2PNQqX5DZNKacRJuMuLUKpoLo%2FNLMYgdFbVHYGb%2BkoKEDuEDbseJIukyqkTO1CyqyKbCLrsbnDJXPGYAFesplf%2Bw%2FZFCGoI7PJ9UkO%2FMi7EmXS%2Fka67i60qtKKh1f9heT0zADuEj4RjkCoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD%2FtqfNGwKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5Mat5YD&port=14035&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4&existing_fsm_id=ba_YAUVSBPgiAJf3E3bcHCIrTcvZ%2BLRcVTfs4ysj5ILNpM1KFtF&host=localhost&offchain_tx=tx_%2BNILAfiEuEC8MFi7A2jq35dCdHoVrzWmEsN3nYF82rP9p485IpX2PNQqX5DZNKacRJuMuLUKpoLo%2FNLMYgdFbVHYGb%2BkoKEDuEDbseJIukyqkTO1CyqyKbCLrsbnDJXPGYAFesplf%2Bw%2FZFCGoI7PJ9UkO%2FMi7EmXS%2Fka67i60qtKKh1f9heT0zADuEj4RjkCoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD%2FtqfNGwKg0d3Jot8NfJSECCzYdd3yVeEXLOyDBLaJJ8Qg7fTtL5Mat5YD&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_YAUVSBPgiAJf3E3bcHCIrTcvZ+LRcVTfs4ysj5ILNpM1KFtF"
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBr15LrykRBcZV99mEGianI5coLRYYyvLCBEmkP+2p80boQE6mEPPgqeInvi5Gpb2Rhe7T+kTWWusYKhGIeZ7QV3aI4Y3+rnizACGHLHOiuwAAIYPXtZ/KAACq5JVlA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422691,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBlgfSrQQBdht7RRXPy3wdwV+tFmISb1uGQ0NvRldli9bfPkYHSp6Hm5zlLn7Fopxg1LQXfHr2DyG094zv/RIwEuF/4XTUBoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNG6EBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygAAueTpy8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
  "id": -576460752303422691,
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBlgfSrQQBdht7RRXPy3wdwV+tFmISb1uGQ0NvRldli9bfPkYHSp6Hm5zlLn7Fopxg1LQXfHr2DyG094zv/RIwEuF/4XTUBoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNG6EBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygAAueTpy8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422690,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBlgfSrQQBdht7RRXPy3wdwV+tFmISb1uGQ0NvRldli9bfPkYHSp6Hm5zlLn7Fopxg1LQXfHr2DyG094zv/RIwEuECoLGVQPxDJBHUR67QXcvxp/K7QJsywlC5JfHrWQScM6lPWSrv7lE8P66hrWVmAAy3z7XlLWon5o2NMDQYfqgoEuF/4XTUBoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNG6EBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygAAkuKazU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
  "id": -576460752303422690,
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBlgfSrQQBdht7RRXPy3wdwV+tFmISb1uGQ0NvRldli9bfPkYHSp6Hm5zlLn7Fopxg1LQXfHr2DyG094zv/RIwEuECoLGVQPxDJBHUR67QXcvxp/K7QJsywlC5JfHrWQScM6lPWSrv7lE8P66hrWVmAAy3z7XlLWon5o2NMDQYfqgoEuF/4XTUBoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNG6EBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygAAkuKazU=",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBlgfSrQQBdht7RRXPy3wdwV+tFmISb1uGQ0NvRldli9bfPkYHSp6Hm5zlLn7Fopxg1LQXfHr2DyG094zv/RIwEuECoLGVQPxDJBHUR67QXcvxp/K7QJsywlC5JfHrWQScM6lPWSrv7lE8P66hrWVmAAy3z7XlLWon5o2NMDQYfqgoEuF/4XTUBoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNG6EBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygAAkuKazU=",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBlgfSrQQBdht7RRXPy3wdwV+tFmISb1uGQ0NvRldli9bfPkYHSp6Hm5zlLn7Fopxg1LQXfHr2DyG094zv/RIwEuECoLGVQPxDJBHUR67QXcvxp/K7QJsywlC5JfHrWQScM6lPWSrv7lE8P66hrWVmAAy3z7XlLWon5o2NMDQYfqgoEuF/4XTUBoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNG6EBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygAAkuKazU=",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBlgfSrQQBdht7RRXPy3wdwV+tFmISb1uGQ0NvRldli9bfPkYHSp6Hm5zlLn7Fopxg1LQXfHr2DyG094zv/RIwEuECoLGVQPxDJBHUR67QXcvxp/K7QJsywlC5JfHrWQScM6lPWSrv7lE8P66hrWVmAAy3z7XlLWon5o2NMDQYfqgoEuF/4XTUBoQa9eS68pEQXGVffZhBompyOXKC0WGMrywgRJpD/tqfNG6EBOphDz4KniJ74uRqW9kYXu0/pE1lrrGCoRiHme0Fd2iOGN/q54swAhhyxzorsAACGD17WfygAAkuKazU=",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
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
    "channel_id": "ch_2SSqtb2UuQwgwdZptsQLU7ZCrATBA3BZLYJDE8K6wTj89nt6F4",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
