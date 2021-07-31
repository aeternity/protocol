
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr&keep_running=false&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa&role=initiator
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
      "fsm_id": "ba_S4ekM75B1eUmnyn+Dxv0DhSmNJacoP1wiuJSXv4tHa8EXjUk"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr&keep_running=false&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa&role=responder
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
      "fsm_id": "ba_7bf2+5Nu89uNvScHSp9u6lMrtFxPuuhUpPogfNZJO6zhZ8Pj"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAS5uFzQXd5z0T87/Xckj/UZm9gV6LmQzMPCNcES31lwmhj+qJSJgAKEBAlj/ARiNN15HwVq6gkiNSBe7ic3+3AaoAhvWc8PZl22GJGE5yoAAAgoAhhAGeddIAMCgxbK3vfaSbcmVp+tyPBBuoH487fftPSUvC7qlKcKw6VcBzW4uhg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421219,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECZUhx+cUjXrkVK5EUTOqrpPVZMs4W+jBaWiYehIuu7h6P9XGPObgdgrzimtOPipEH1xq7Q8iFpw0tXC/yX0NkGuIP4gTIBoQEubhc0F3ec9E/O/13JI/1GZvYFei5kMzDwjXBEt9ZcJoY/qiUiYAChAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdthiRhOcqAAAIKAIYQBnnXSADAoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXAVKT+KU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421219,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_7bf2+5Nu89uNvScHSp9u6lMrtFxPuuhUpPogfNZJO6zhZ8Pj"
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECZUhx+cUjXrkVK5EUTOqrpPVZMs4W+jBaWiYehIuu7h6P9XGPObgdgrzimtOPipEH1xq7Q8iFpw0tXC/yX0NkGuIP4gTIBoQEubhc0F3ec9E/O/13JI/1GZvYFei5kMzDwjXBEt9ZcJoY/qiUiYAChAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdthiRhOcqAAAIKAIYQBnnXSADAoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXAVKT+KU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421218,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAmVIcfnFI165FSuRFEzqq6T1WTLOFvowWlomHoSLru4ej/Vxjzm4HYK84prTj4qRB9cau0PIhacNLVwv8l9DZBriD+IEyAaEBLm4XNBd3nPRPzv9dySP9Rmb2BXouZDMw8I1wRLfWXCaGP6olImAAoQECWP8BGI03XkfBWrqCSI1IF7uJzf7cBqgCG9Zzw9mXbYYkYTnKgAACCgCGEAZ510gAwKDFsre99pJtyZWn63I8EG6gfjzt9+09JS8LuqUpwrDpVwFTWM+1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421218,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAmVIcfnFI165FSuRFEzqq6T1WTLOFvowWlomHoSLru4ej/Vxjzm4HYK84prTj4qRB9cau0PIhacNLVwv8l9DZBriD+IEyAaEBLm4XNBd3nPRPzv9dySP9Rmb2BXouZDMw8I1wRLfWXCaGP6olImAAoQECWP8BGI03XkfBWrqCSI1IF7uJzf7cBqgCG9Zzw9mXbYYkYTnKgAACCgCGEAZ510gAwKDFsre99pJtyZWn63I8EG6gfjzt9+09JS8LuqUpwrDpVwFTWM+1",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_S4ekM75B1eUmnyn+Dxv0DhSmNJacoP1wiuJSXv4tHa8EXjUk"
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAmVIcfnFI165FSuRFEzqq6T1WTLOFvowWlomHoSLru4ej/Vxjzm4HYK84prTj4qRB9cau0PIhacNLVwv8l9DZBriD+IEyAaEBLm4XNBd3nPRPzv9dySP9Rmb2BXouZDMw8I1wRLfWXCaGP6olImAAoQECWP8BGI03XkfBWrqCSI1IF7uJzf7cBqgCG9Zzw9mXbYYkYTnKgAACCgCGEAZ510gAwKDFsre99pJtyZWn63I8EG6gfjzt9+09JS8LuqUpwrDpVwFTWM+1",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAmVIcfnFI165FSuRFEzqq6T1WTLOFvowWlomHoSLru4ej/Vxjzm4HYK84prTj4qRB9cau0PIhacNLVwv8l9DZBriD+IEyAaEBLm4XNBd3nPRPzv9dySP9Rmb2BXouZDMw8I1wRLfWXCaGP6olImAAoQECWP8BGI03XkfBWrqCSI1IF7uJzf7cBqgCG9Zzw9mXbYYkYTnKgAACCgCGEAZ510gAwKDFsre99pJtyZWn63I8EG6gfjzt9+09JS8LuqUpwrDpVwFTWM+1",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAmVIcfnFI165FSuRFEzqq6T1WTLOFvowWlomHoSLru4ej/Vxjzm4HYK84prTj4qRB9cau0PIhacNLVwv8l9DZBriD+IEyAaEBLm4XNBd3nPRPzv9dySP9Rmb2BXouZDMw8I1wRLfWXCaGP6olImAAoQECWP8BGI03XkfBWrqCSI1IF7uJzf7cBqgCG9Zzw9mXbYYkYTnKgAACCgCGEAZ510gAwKDFsre99pJtyZWn63I8EG6gfjzt9+09JS8LuqUpwrDpVwFTWM+1",
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
    "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "message": {
        "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
        "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
        "info": "Hello",
        "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "message": {
        "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
        "info": "Hello back",
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421217,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421217,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "balance": 69999999999999
    },
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAmVIcfnFI165FSuRFEzqq6T1WTLOFvowWlomHoSLru4ej/Vxjzm4HYK84prTj4qRB9cau0PIhacNLVwv8l9DZBriD+IEyAaEBLm4XNBd3nPRPzv9dySP9Rmb2BXouZDMw8I1wRLfWXCaGP6olImAAoQECWP8BGI03XkfBWrqCSI1IF7uJzf7cBqgCG9Zzw9mXbYYkYTnKgAACCgCGEAZ510gAwKDFsre99pJtyZWn63I8EG6gfjzt9+09JS8LuqUpwrDpVwFTWM+1"
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAmVIcfnFI165FSuRFEzqq6T1WTLOFvowWlomHoSLru4ej/Vxjzm4HYK84prTj4qRB9cau0PIhacNLVwv8l9DZBriD+IEyAaEBLm4XNBd3nPRPzv9dySP9Rmb2BXouZDMw8I1wRLfWXCaGP6olImAAoQECWP8BGI03XkfBWrqCSI1IF7uJzf7cBqgCG9Zzw9mXbYYkYTnKgAACCgCGEAZ510gAwKDFsre99pJtyZWn63I8EG6gfjzt9+09JS8LuqUpwrDpVwFTWM+1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421216,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421216,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "balance": 69999999999999
    },
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
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
    "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
    "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
        "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
    "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
    "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
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
    "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
    "meta": 17,
    "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
        "meta": 17,
        "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
    "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
    "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkpMappFcFqyoyfmI9jFEodNGAQQCcbmk9yonGBze8cnAqCkjNGrprT7r29YBhyy0ds1hk+r3y/Z4hyv7SSjLRadgzh72qs=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
          "op": "OffChainTransfer",
          "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
  "id": -576460752303421215,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB70O0G0hsBZGusJn21pHAwdNwJu6NQuMBov/N+s/T1e5QtR/5JO5qLQ9v9Pf9/10+4M4GhHfD0rFLmXp8TzrAOuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwKgpIzRq6a0+69vWAYcstHbNYZPq98v2eIcr+0koy0WnYM2bzzq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421215,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB70O0G0hsBZGusJn21pHAwdNwJu6NQuMBov/N+s/T1e5QtR/5JO5qLQ9v9Pf9/10+4M4GhHfD0rFLmXp8TzrAOuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwKgpIzRq6a0+69vWAYcstHbNYZPq98v2eIcr+0koy0WnYM2bzzq",
      "updates": [
        {
          "amount": 1,
          "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
          "op": "OffChainTransfer",
          "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
  "id": -576460752303421214,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAe9DtBtIbAWRrrCZ9taRwMHTcCbujULjAaL/zfrP09XuULUf+STuai0Pb/T3/f9dPuDOBoR3w9KxS5l6fE86wDrhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycCoKSM0aumtPuvb1gGHLLR2zWGT6vfL9niHK/tJKMtFp2DlCdQeA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421214,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAe9DtBtIbAWRrrCZ9taRwMHTcCbujULjAaL/zfrP09XuULUf+STuai0Pb/T3/f9dPuDOBoR3w9KxS5l6fE86wDrhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycCoKSM0aumtPuvb1gGHLLR2zWGT6vfL9niHK/tJKMtFp2DlCdQeA=="
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAe9DtBtIbAWRrrCZ9taRwMHTcCbujULjAaL/zfrP09XuULUf+STuai0Pb/T3/f9dPuDOBoR3w9KxS5l6fE86wDrhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycCoKSM0aumtPuvb1gGHLLR2zWGT6vfL9niHK/tJKMtFp2DlCdQeA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421213,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421213,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "balance": 69999999999998
    },
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421212,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421212,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAe9DtBtIbAWRrrCZ9taRwMHTcCbujULjAaL/zfrP09XuULUf+STuai0Pb/T3/f9dPuDOBoR3w9KxS5l6fE86wDrhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycCoKSM0aumtPuvb1gGHLLR2zWGT6vfL9niHK/tJKMtFp2DlCdQeA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAubhc0F3ec9E/O/13JI/1GZvYFei5kMzDwjXBEt9ZcJovKCgEAhj+qJSJf/rDvQAGgAlj/ARiNN15HwVq6gkiNSBe7ic3+3AaoAhvWc8PZl22LygoBAIYkYTnKgAIFgPnq"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421211,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421211,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "balance": 40000000000002
    },
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "meta": 17,
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
        "meta": 17,
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkpMappFcFqyoyfmI9jFEodNGAQQCcbmk9yonGBze8cnA6DFsre99pJtyZWn63I8EG6gfjzt9+09JS8LuqUpwrDpV5cFF3E=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
          "op": "OffChainTransfer",
          "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
  "id": -576460752303421210,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwOgxbK3vfaSbcmVp+tyPBBuoH487fftPSUvC7qlKcKw6Vd6c0xw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421210,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwOgxbK3vfaSbcmVp+tyPBBuoH487fftPSUvC7qlKcKw6Vd6c0xw",
      "updates": [
        {
          "amount": 1,
          "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
          "op": "OffChainTransfer",
          "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
  "id": -576460752303421209,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA5t+UhBiSgUgE17L4ZRGqbmk1ZDimgPAVPxBOW0lpE9YlIZVCZK8PUcEsk++/33Ld5zA1qMwcGctq9QRhYXK0B7hI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycDoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXm1T0kg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421209,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA5t+UhBiSgUgE17L4ZRGqbmk1ZDimgPAVPxBOW0lpE9YlIZVCZK8PUcEsk++/33Ld5zA1qMwcGctq9QRhYXK0B7hI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycDoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXm1T0kg=="
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA5t+UhBiSgUgE17L4ZRGqbmk1ZDimgPAVPxBOW0lpE9YlIZVCZK8PUcEsk++/33Ld5zA1qMwcGctq9QRhYXK0B7hI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycDoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXm1T0kg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421208,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421208,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "balance": 40000000000001
    },
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421207,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421207,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA5t+UhBiSgUgE17L4ZRGqbmk1ZDimgPAVPxBOW0lpE9YlIZVCZK8PUcEsk++/33Ld5zA1qMwcGctq9QRhYXK0B7hI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycDoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXm1T0kg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAubhc0F3ec9E/O/13JI/1GZvYFei5kMzDwjXBEt9ZcJovKCgEAhj+qJSJf/7DvQAGgAlj/ARiNN15HwVq6gkiNSBe7ic3+3AaoAhvWc8PZl22LygoBAIYkYTnKgAGAhCZI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421206,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421206,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "balance": 40000000000001
    },
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "meta": 17,
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
        "meta": 17,
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkpMappFcFqyoyfmI9jFEodNGAQQCcbmk9yonGBze8cnBKCyXTTPK0tQT0sz593PyqQ41mwImM4E+rqxrWj2Tht1oCVAJvc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
          "op": "OffChainTransfer",
          "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
  "id": -576460752303421205,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwSgsl00zytLUE9LM+fdz8qkONZsCJjOBPq6sa1o9k4bdaAMWGa0"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421205,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwSgsl00zytLUE9LM+fdz8qkONZsCJjOBPq6sa1o9k4bdaAMWGa0",
      "updates": [
        {
          "amount": 1,
          "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
          "op": "OffChainTransfer",
          "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
  "id": -576460752303421204,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhApslhqC9I+4bsj92Yjz7mGpo6UYB9UgxN7ZCoaChNd/d9DakBA4R7EqIL8aC/iCBXxUc94MiEUV95O3eaoprdDbhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycEoLJdNM8rS1BPSzPn3c/KpDjWbAiYzgT6urGtaPZOG3WgsCVEsg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421204,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhApslhqC9I+4bsj92Yjz7mGpo6UYB9UgxN7ZCoaChNd/d9DakBA4R7EqIL8aC/iCBXxUc94MiEUV95O3eaoprdDbhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycEoLJdNM8rS1BPSzPn3c/KpDjWbAiYzgT6urGtaPZOG3WgsCVEsg=="
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhApslhqC9I+4bsj92Yjz7mGpo6UYB9UgxN7ZCoaChNd/d9DakBA4R7EqIL8aC/iCBXxUc94MiEUV95O3eaoprdDbhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycEoLJdNM8rS1BPSzPn3c/KpDjWbAiYzgT6urGtaPZOG3WgsCVEsg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421203,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421203,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "balance": 40000000000000
    },
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421202,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421202,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhApslhqC9I+4bsj92Yjz7mGpo6UYB9UgxN7ZCoaChNd/d9DakBA4R7EqIL8aC/iCBXxUc94MiEUV95O3eaoprdDbhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycEoLJdNM8rS1BPSzPn3c/KpDjWbAiYzgT6urGtaPZOG3WgsCVEsg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAubhc0F3ec9E/O/13JI/1GZvYFei5kMzDwjXBEt9ZcJovKCgEAhj+qJSJgALDvQAGgAlj/ARiNN15HwVq6gkiNSBe7ic3+3AaoAhvWc8PZl22LygoBAIYkYTnKgAAVyZJ4"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421201,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421201,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "balance": 70000000000000
    },
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
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
    "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
    "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
        "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
    "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
    "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
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
    "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
    "meta": 17,
    "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
        "meta": 17,
        "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
    "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
    "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkpMappFcFqyoyfmI9jFEodNGAQQCcbmk9yonGBze8cnBaDFsre99pJtyZWn63I8EG6gfjzt9+09JS8LuqUpwrDpVzGKSSQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
          "op": "OffChainTransfer",
          "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
  "id": -576460752303421200,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECpWrF5lGuVD/Cq9uQLISqI0lTUmB6Rk0qI8j7n1N5Ojt8jJnoKYDe13YVOWdXVuQsHku8SbPIbqkeDUksBMI8NuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwWgxbK3vfaSbcmVp+tyPBBuoH487fftPSUvC7qlKcKw6Vd8eQSd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421200,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+JALAfhCuECpWrF5lGuVD/Cq9uQLISqI0lTUmB6Rk0qI8j7n1N5Ojt8jJnoKYDe13YVOWdXVuQsHku8SbPIbqkeDUksBMI8NuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwWgxbK3vfaSbcmVp+tyPBBuoH487fftPSUvC7qlKcKw6Vd8eQSd",
      "updates": [
        {
          "amount": 1,
          "from": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
          "op": "OffChainTransfer",
          "to": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
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
  "id": -576460752303421199,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAqVqxeZRrlQ/wqvbkCyEqiNJU1JgekZNKiPI+59TeTo7fIyZ6CmA3td2FTlnV1bkLB5LvEmzyG6pHg1JLATCPDbhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycFoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXY2GvFQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421199,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAqVqxeZRrlQ/wqvbkCyEqiNJU1JgekZNKiPI+59TeTo7fIyZ6CmA3td2FTlnV1bkLB5LvEmzyG6pHg1JLATCPDbhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycFoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXY2GvFQ=="
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAqVqxeZRrlQ/wqvbkCyEqiNJU1JgekZNKiPI+59TeTo7fIyZ6CmA3td2FTlnV1bkLB5LvEmzyG6pHg1JLATCPDbhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycFoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXY2GvFQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421198,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421198,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "balance": 69999999999999
    },
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421197,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421197,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAqVqxeZRrlQ/wqvbkCyEqiNJU1JgekZNKiPI+59TeTo7fIyZ6CmA3td2FTlnV1bkLB5LvEmzyG6pHg1JLATCPDbhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycFoMWyt732km3JlafrcjwQbqB+PO337T0lLwu6pSnCsOlXY2GvFQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAubhc0F3ec9E/O/13JI/1GZvYFei5kMzDwjXBEt9ZcJovKCgEAhj+qJSJf/7DvQAGgAlj/ARiNN15HwVq6gkiNSBe7ic3+3AaoAhvWc8PZl22LygoBAIYkYTnKgAGAhCZI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421196,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421196,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "balance": 40000000000001
    },
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "meta": 17,
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
        "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
        "meta": 17,
        "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
    "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
    "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkpMappFcFqyoyfmI9jFEodNGAQQCcbmk9yonGBze8cnBqCyXTTPK0tQT0sz593PyqQ41mwImM4E+rqxrWj2Tht1oGU671s=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
          "op": "OffChainTransfer",
          "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
  "id": -576460752303421195,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwagsl00zytLUE9LM+fdz8qkONZsCJjOBPq6sa1o9k4bdaC1lxbV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421195,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZKTGqaRXBasqMn5iPYxRKHTRgEEAnG5pPcqJxgc3vHJwagsl00zytLUE9LM+fdz8qkONZsCJjOBPq6sa1o9k4bdaC1lxbV",
      "updates": [
        {
          "amount": 1,
          "from": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
          "op": "OffChainTransfer",
          "to": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
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
  "id": -576460752303421194,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAeS2BwYJFX6cuTFxOG42+sQXhkJKluf7eAZBOQJyb6JWoHx28xDUf0RmZsi+6V6jCkvXpkbfoj7rnz8W332LqBLhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycGoLJdNM8rS1BPSzPn3c/KpDjWbAiYzgT6urGtaPZOG3WgcnztHw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421194,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAeS2BwYJFX6cuTFxOG42+sQXhkJKluf7eAZBOQJyb6JWoHx28xDUf0RmZsi+6V6jCkvXpkbfoj7rnz8W332LqBLhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycGoLJdNM8rS1BPSzPn3c/KpDjWbAiYzgT6urGtaPZOG3WgcnztHw=="
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAeS2BwYJFX6cuTFxOG42+sQXhkJKluf7eAZBOQJyb6JWoHx28xDUf0RmZsi+6V6jCkvXpkbfoj7rnz8W332LqBLhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycGoLJdNM8rS1BPSzPn3c/KpDjWbAiYzgT6urGtaPZOG3WgcnztHw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421193,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421193,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_22y78dMUUgcXZ1HkdtSsLYQexTpci7verjcdcUCsoZzt89cEa",
      "balance": 40000000000000
    },
    {
      "account": "ak_MSzbmvRVrxhF6fS2KMuqg8qgSYcr84qoVy6pe7Zi6i7ey8cDr",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421192,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421192,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAQJY/wEYjTdeR8FauoJIjUgXu4nN/twGqAIb1nPD2ZdtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAeS2BwYJFX6cuTFxOG42+sQXhkJKluf7eAZBOQJyb6JWoHx28xDUf0RmZsi+6V6jCkvXpkbfoj7rnz8W332LqBLhI+EY5AqEGSkxqmkVwWrKjJ+Yj2MUSh00YBBAJxuaT3KicYHN7xycGoLJdNM8rS1BPSzPn3c/KpDjWbAiYzgT6urGtaPZOG3WgcnztHw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAubhc0F3ec9E/O/13JI/1GZvYFei5kMzDwjXBEt9ZcJovKCgEAhj+qJSJgALDvQAGgAlj/ARiNN15HwVq6gkiNSBe7ic3+3AaoAhvWc8PZl22LygoBAIYkYTnKgAAVyZJ4"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421191,
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
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421191,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421190,
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
    "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
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
  "channel_id": "ch_ZircvH3qMQSTTv4LdykRdRAnK94ecjobYPF1ZgPeA3kxWv2dv",
  "id": -576460752303421190,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
