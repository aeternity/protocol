
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_z8ylrIF7LG1/FMVTTXqIfVh/PSuJ16hfNN/PW65y2kosQ3ly"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_phBz1ht6fEU/aMntCdHhi/01d/b5JILB5ScypiIUiO/H25W7"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt6XRQ/YQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422409,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAINBARbUyUo8Q0rP4QOECgwn089T8wsBw8sigXFGsZJ2IGybHmwAkX89wZQxMwuKLDg3Jpi+LyPn8ko8Y4fuEHuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Leoq4iVg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422409,
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "fsm_id": "ba_phBz1ht6fEU/aMntCdHhi/01d/b5JILB5ScypiIUiO/H25W7",
      "signed_tx": "tx_+MsLAfhCuEAINBARbUyUo8Q0rP4QOECgwn089T8wsBw8sigXFGsZJ2IGybHmwAkX89wZQxMwuKLDg3Jpi+LyPn8ko8Y4fuEHuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Leoq4iVg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422408,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhACDQQEW1MlKPENKz+EDhAoMJ9PPU/MLAcPLIoFxRrGSdiBsmx5sAJF/PcGUMTMLiiw4NyaYvi8j5/JKPGOH7hB7hA3tXzeLezqS9f3MEgn2TkD4jE20flsHCQ3fpPh+4YtDXJTp8bGwfE6+Cd7qaIGwrrchK6ofQlIT3VUFulnllOBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3rqCcyQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
  "id": -576460752303422408,
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhACDQQEW1MlKPENKz+EDhAoMJ9PPU/MLAcPLIoFxRrGSdiBsmx5sAJF/PcGUMTMLiiw4NyaYvi8j5/JKPGOH7hB7hA3tXzeLezqS9f3MEgn2TkD4jE20flsHCQ3fpPh+4YtDXJTp8bGwfE6+Cd7qaIGwrrchK6ofQlIT3VUFulnllOBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3rqCcyQ",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_z8ylrIF7LG1/FMVTTXqIfVh/PSuJ16hfNN/PW65y2kosQ3ly"
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhACDQQEW1MlKPENKz+EDhAoMJ9PPU/MLAcPLIoFxRrGSdiBsmx5sAJF/PcGUMTMLiiw4NyaYvi8j5/JKPGOH7hB7hA3tXzeLezqS9f3MEgn2TkD4jE20flsHCQ3fpPh+4YtDXJTp8bGwfE6+Cd7qaIGwrrchK6ofQlIT3VUFulnllOBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3rqCcyQ",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhACDQQEW1MlKPENKz+EDhAoMJ9PPU/MLAcPLIoFxRrGSdiBsmx5sAJF/PcGUMTMLiiw4NyaYvi8j5/JKPGOH7hB7hA3tXzeLezqS9f3MEgn2TkD4jE20flsHCQ3fpPh+4YtDXJTp8bGwfE6+Cd7qaIGwrrchK6ofQlIT3VUFulnllOBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3rqCcyQ",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhACDQQEW1MlKPENKz+EDhAoMJ9PPU/MLAcPLIoFxRrGSdiBsmx5sAJF/PcGUMTMLiiw4NyaYvi8j5/JKPGOH7hB7hA3tXzeLezqS9f3MEgn2TkD4jE20flsHCQ3fpPh+4YtDXJTp8bGwfE6+Cd7qaIGwrrchK6ofQlIT3VUFulnllOBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3rqCcyQ",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "message": {
        "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "message": {
        "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422407,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
  "id": -576460752303422407,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "state": "tx_+QENCwH4hLhACDQQEW1MlKPENKz+EDhAoMJ9PPU/MLAcPLIoFxRrGSdiBsmx5sAJF/PcGUMTMLiiw4NyaYvi8j5/JKPGOH7hB7hA3tXzeLezqS9f3MEgn2TkD4jE20flsHCQ3fpPh+4YtDXJTp8bGwfE6+Cd7qaIGwrrchK6ofQlIT3VUFulnllOBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3rqCcyQ"
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "state": "tx_+QENCwH4hLhACDQQEW1MlKPENKz+EDhAoMJ9PPU/MLAcPLIoFxRrGSdiBsmx5sAJF/PcGUMTMLiiw4NyaYvi8j5/JKPGOH7hB7hA3tXzeLezqS9f3MEgn2TkD4jE20flsHCQ3fpPh+4YtDXJTp8bGwfE6+Cd7qaIGwrrchK6ofQlIT3VUFulnllOBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3rqCcyQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBhpA80sRx7aFsakCGDTCq9qi85tilZsmjcc/S7irSEzGoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7sgIAAe8opEqo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhA55w9kUVGfJWkj7lMYjJcgM/e98upf52taJwxwli+CsiapMfC51S5bglwrpegV+2ceYYgL/w7+qHKcSsU9OKNCLkBovkBnzYBoQYaQPNLEce2hbGpAhg0wqvaovObYpWbJo3HP0u4q0hMxqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAHulStTI"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA55w9kUVGfJWkj7lMYjJcgM/e98upf52taJwxwli+CsiapMfC51S5bglwrpegV+2ceYYgL/w7+qHKcSsU9OKNCLkBovkBnzYBoQYaQPNLEce2hbGpAhg0wqvaovObYpWbJo3HP0u4q0hMxqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAHulStTI",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA55w9kUVGfJWkj7lMYjJcgM/e98upf52taJwxwli+CsiapMfC51S5bglwrpegV+2ceYYgL/w7+qHKcSsU9OKNCLkBovkBnzYBoQYaQPNLEce2hbGpAhg0wqvaovObYpWbJo3HP0u4q0hMxqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAHulStTI",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBhpA80sRx7aFsakCGDTCq9qi85tilZsmjcc/S7irSEzGoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIbgkQw2Hn406Avk2A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDy3kAUJMqdRHCfB8g1j0IdS6sGjmxKY/qW8io5YW+GG8A8xTP5ZgZXFZa2vLg5VZbv6DQITm9NKoJIWnrrv2APuF/4XTgBoQYaQPNLEce2hbGpAhg0wqvaovObYpWbJo3HP0u4q0hMxqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCG4JEMNh5+NDJcQ4U="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDy3kAUJMqdRHCfB8g1j0IdS6sGjmxKY/qW8io5YW+GG8A8xTP5ZgZXFZa2vLg5VZbv6DQITm9NKoJIWnrrv2APuF/4XTgBoQYaQPNLEce2hbGpAhg0wqvaovObYpWbJo3HP0u4q0hMxqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCG4JEMNh5+NDJcQ4U=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDy3kAUJMqdRHCfB8g1j0IdS6sGjmxKY/qW8io5YW+GG8A8xTP5ZgZXFZa2vLg5VZbv6DQITm9NKoJIWnrrv2APuF/4XTgBoQYaQPNLEce2hbGpAhg0wqvaovObYpWbJo3HP0u4q0hMxqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCG4JEMNh5+NDJcQ4U=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
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
    "channel_id": "ch_CZcihxB3fmbWjp2itj1VE4AUWN5FYznAkTdp9SzqveW983Lon",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_w/aQisDabppjDZHObCvQv+faHQaMLsh1rPsK/dIimYeviie4"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_s+G/zEsMvwT8WJ3UidoLUtwXBm6720SOxeMyrqGArlHyY7kI"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt8ZQ7EYA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422406,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECeVZgPkVTrdcHpjtz0VdkevT0R0rt7TyDEJKHJCa7OwMJju57XCPNNMzwt2nQ3OGpLGT68+pSvyyXwyeMDdc8PuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LfIPDI6E="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422406,
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "fsm_id": "ba_s+G/zEsMvwT8WJ3UidoLUtwXBm6720SOxeMyrqGArlHyY7kI",
      "signed_tx": "tx_+MsLAfhCuECeVZgPkVTrdcHpjtz0VdkevT0R0rt7TyDEJKHJCa7OwMJju57XCPNNMzwt2nQ3OGpLGT68+pSvyyXwyeMDdc8PuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LfIPDI6E=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422405,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAUfzdj2Bd1uaRwwPgarDpmVBEprThhU67gpJioxHhZtphD3Yg53iZJ6TzWZ++LJZ7FekCoMZsur1Nyb8AzQFRDbhAnlWYD5FU63XB6Y7c9FXZHr09EdK7e08gxCShyQmuzsDCY7ue1wjzTTM8Ldp0NzhqSxk+vPqUr8sl8MnjA3XPD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3xnspYY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
  "id": -576460752303422405,
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAUfzdj2Bd1uaRwwPgarDpmVBEprThhU67gpJioxHhZtphD3Yg53iZJ6TzWZ++LJZ7FekCoMZsur1Nyb8AzQFRDbhAnlWYD5FU63XB6Y7c9FXZHr09EdK7e08gxCShyQmuzsDCY7ue1wjzTTM8Ldp0NzhqSxk+vPqUr8sl8MnjA3XPD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3xnspYY",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_w/aQisDabppjDZHObCvQv+faHQaMLsh1rPsK/dIimYeviie4"
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAUfzdj2Bd1uaRwwPgarDpmVBEprThhU67gpJioxHhZtphD3Yg53iZJ6TzWZ++LJZ7FekCoMZsur1Nyb8AzQFRDbhAnlWYD5FU63XB6Y7c9FXZHr09EdK7e08gxCShyQmuzsDCY7ue1wjzTTM8Ldp0NzhqSxk+vPqUr8sl8MnjA3XPD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3xnspYY",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAUfzdj2Bd1uaRwwPgarDpmVBEprThhU67gpJioxHhZtphD3Yg53iZJ6TzWZ++LJZ7FekCoMZsur1Nyb8AzQFRDbhAnlWYD5FU63XB6Y7c9FXZHr09EdK7e08gxCShyQmuzsDCY7ue1wjzTTM8Ldp0NzhqSxk+vPqUr8sl8MnjA3XPD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3xnspYY",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAUfzdj2Bd1uaRwwPgarDpmVBEprThhU67gpJioxHhZtphD3Yg53iZJ6TzWZ++LJZ7FekCoMZsur1Nyb8AzQFRDbhAnlWYD5FU63XB6Y7c9FXZHr09EdK7e08gxCShyQmuzsDCY7ue1wjzTTM8Ldp0NzhqSxk+vPqUr8sl8MnjA3XPD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3xnspYY",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "message": {
        "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "message": {
        "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422404,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
  "id": -576460752303422404,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "state": "tx_+QENCwH4hLhAUfzdj2Bd1uaRwwPgarDpmVBEprThhU67gpJioxHhZtphD3Yg53iZJ6TzWZ++LJZ7FekCoMZsur1Nyb8AzQFRDbhAnlWYD5FU63XB6Y7c9FXZHr09EdK7e08gxCShyQmuzsDCY7ue1wjzTTM8Ldp0NzhqSxk+vPqUr8sl8MnjA3XPD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3xnspYY"
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "state": "tx_+QENCwH4hLhAUfzdj2Bd1uaRwwPgarDpmVBEprThhU67gpJioxHhZtphD3Yg53iZJ6TzWZ++LJZ7FekCoMZsur1Nyb8AzQFRDbhAnlWYD5FU63XB6Y7c9FXZHr09EdK7e08gxCShyQmuzsDCY7ue1wjzTTM8Ldp0NzhqSxk+vPqUr8sl8MnjA3XPD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3xnspYY"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBrf/0KqDNNoWgAmwDyvy0gOqRw3JUBzJiaIFB8DEqLD6oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7sgIAAffB7TEg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAqjGKZ99YVlsfPr79OhluUHGXd75iOVurGOaBEV3/PCCZhXby69aUjcJRCukq5AnuPzrfud9my2/dU5RV5Q0SALkBovkBnzYBoQa3/9CqgzTaFoAJsA8r8tIDqkcNyVAcyYmiBQfAxKiw+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAH3mthUq"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAqjGKZ99YVlsfPr79OhluUHGXd75iOVurGOaBEV3/PCCZhXby69aUjcJRCukq5AnuPzrfud9my2/dU5RV5Q0SALkBovkBnzYBoQa3/9CqgzTaFoAJsA8r8tIDqkcNyVAcyYmiBQfAxKiw+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAH3mthUq",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAqjGKZ99YVlsfPr79OhluUHGXd75iOVurGOaBEV3/PCCZhXby69aUjcJRCukq5AnuPzrfud9my2/dU5RV5Q0SALkBovkBnzYBoQa3/9CqgzTaFoAJsA8r8tIDqkcNyVAcyYmiBQfAxKiw+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAH3mthUq",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBrf/0KqDNNoWgAmwDyvy0gOqRw3JUBzJiaIFB8DEqLD6oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiX/+GJGE5yoABAIbgkQw2Hn5+sYv8sw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDqqapybpN0HcQi+7JHkldb2rumiCr9DFnksYoa6UtaO8934yb/98GMdIiudoNz5XFuu7a6huVSPXdFYDohKZkBuF/4XTgBoQa3/9CqgzTaFoAJsA8r8tIDqkcNyVAcyYmiBQfAxKiw+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCG4JEMNh5+ftaI4Xs="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDqqapybpN0HcQi+7JHkldb2rumiCr9DFnksYoa6UtaO8934yb/98GMdIiudoNz5XFuu7a6huVSPXdFYDohKZkBuF/4XTgBoQa3/9CqgzTaFoAJsA8r8tIDqkcNyVAcyYmiBQfAxKiw+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCG4JEMNh5+ftaI4Xs=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDqqapybpN0HcQi+7JHkldb2rumiCr9DFnksYoa6UtaO8934yb/98GMdIiudoNz5XFuu7a6huVSPXdFYDohKZkBuF/4XTgBoQa3/9CqgzTaFoAJsA8r8tIDqkcNyVAcyYmiBQfAxKiw+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCG4JEMNh5+ftaI4Xs=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
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
    "channel_id": "ch_2Q31r718hCCBFBYjDa7vAZ86CQAufBMrbmSouZ5LN7o7QWjkm5",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
