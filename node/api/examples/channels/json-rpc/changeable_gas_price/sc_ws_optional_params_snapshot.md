
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
      "fsm_id": "ba_UV11GGA2IlW1IqlCr3EIus7HnYnoGoizmfCOQvj6nnD4zoiT"
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
      "fsm_id": "ba_kW4t2sbqayGjeWQ5NDTfjw5r6WXeEE8xiJ+ppQeC9/zDkXBa"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtX35/H3w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422564,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAMkj94OsNPJqsnznO/BApB1kBK4hbTDM2flpZeKUltcTaAdse3vAL44o8GbkAhpb2RCr0CKg4xem2+5bfs55EIuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LV/3GnxU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422564,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "fsm_id": "ba_kW4t2sbqayGjeWQ5NDTfjw5r6WXeEE8xiJ+ppQeC9/zDkXBa",
      "signed_tx": "tx_+MsLAfhCuEAMkj94OsNPJqsnznO/BApB1kBK4hbTDM2flpZeKUltcTaAdse3vAL44o8GbkAhpb2RCr0CKg4xem2+5bfs55EIuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LV/3GnxU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422563,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhADJI/eDrDTyarJ85zvwQKQdZASuIW0wzNn5aWXilJbXE2gHbHt7wC+OKPBm5AIaW9kQq9AioOMXptvuW37OeRCLhAkQHrIWn8LarWCTGRDMX/vtzLZsS2wvujvBvIp+Bt3H/TfkdLqlKMsGZlnf1UWRaB9OX7jTrBZZu3e5BYBTInD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1fQo8Sh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422563,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhADJI/eDrDTyarJ85zvwQKQdZASuIW0wzNn5aWXilJbXE2gHbHt7wC+OKPBm5AIaW9kQq9AioOMXptvuW37OeRCLhAkQHrIWn8LarWCTGRDMX/vtzLZsS2wvujvBvIp+Bt3H/TfkdLqlKMsGZlnf1UWRaB9OX7jTrBZZu3e5BYBTInD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1fQo8Sh",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_UV11GGA2IlW1IqlCr3EIus7HnYnoGoizmfCOQvj6nnD4zoiT"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhADJI/eDrDTyarJ85zvwQKQdZASuIW0wzNn5aWXilJbXE2gHbHt7wC+OKPBm5AIaW9kQq9AioOMXptvuW37OeRCLhAkQHrIWn8LarWCTGRDMX/vtzLZsS2wvujvBvIp+Bt3H/TfkdLqlKMsGZlnf1UWRaB9OX7jTrBZZu3e5BYBTInD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1fQo8Sh",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhADJI/eDrDTyarJ85zvwQKQdZASuIW0wzNn5aWXilJbXE2gHbHt7wC+OKPBm5AIaW9kQq9AioOMXptvuW37OeRCLhAkQHrIWn8LarWCTGRDMX/vtzLZsS2wvujvBvIp+Bt3H/TfkdLqlKMsGZlnf1UWRaB9OX7jTrBZZu3e5BYBTInD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1fQo8Sh",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhADJI/eDrDTyarJ85zvwQKQdZASuIW0wzNn5aWXilJbXE2gHbHt7wC+OKPBm5AIaW9kQq9AioOMXptvuW37OeRCLhAkQHrIWn8LarWCTGRDMX/vtzLZsS2wvujvBvIp+Bt3H/TfkdLqlKMsGZlnf1UWRaB9OX7jTrBZZu3e5BYBTInD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1fQo8Sh",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "message": {
        "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "message": {
        "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
  "id": -576460752303422562,
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
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422562,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+QENCwH4hLhADJI/eDrDTyarJ85zvwQKQdZASuIW0wzNn5aWXilJbXE2gHbHt7wC+OKPBm5AIaW9kQq9AioOMXptvuW37OeRCLhAkQHrIWn8LarWCTGRDMX/vtzLZsS2wvujvBvIp+Bt3H/TfkdLqlKMsGZlnf1UWRaB9OX7jTrBZZu3e5BYBTInD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1fQo8Sh"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+QENCwH4hLhADJI/eDrDTyarJ85zvwQKQdZASuIW0wzNn5aWXilJbXE2gHbHt7wC+OKPBm5AIaW9kQq9AioOMXptvuW37OeRCLhAkQHrIWn8LarWCTGRDMX/vtzLZsS2wvujvBvIp+Bt3H/TfkdLqlKMsGZlnf1UWRaB9OX7jTrBZZu3e5BYBTInD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1fQo8Sh"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422561,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422561,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QENCwH4hLhADJI/eDrDTyarJ85zvwQKQdZASuIW0wzNn5aWXilJbXE2gHbHt7wC+OKPBm5AIaW9kQq9AioOMXptvuW37OeRCLhAkQHrIWn8LarWCTGRDMX/vtzLZsS2wvujvBvIp+Bt3H/TfkdLqlKMsGZlnf1UWRaB9OX7jTrBZZu3e5BYBTInD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1fQo8Sh",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422560,
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
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422560,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrV28tuLgXBDpa2Zg22xF5n4NFyR2Iy2EbtixsOTdMx4AqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAsyLzug=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422559,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBetM3nyxrY7WMEupVnKaMXeVUkJiMQsRkTNe8ZY6epi1gjF2uK9ohRqTz85oRnRsNdRQniC1rtd7pgL0tS1ZUEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI47T07"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422559,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBetM3nyxrY7WMEupVnKaMXeVUkJiMQsRkTNe8ZY6epi1gjF2uK9ohRqTz85oRnRsNdRQniC1rtd7pgL0tS1ZUEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI47T07",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422558,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBJkTcILMae+FUu+3hg06GkUdG1dWbiUTWcfiDWLkocjZVBcp00SmLgDK7IQPn8EEk/mNM51qAv7Co6JfjwBlMDuEBetM3nyxrY7WMEupVnKaMXeVUkJiMQsRkTNe8ZY6epi1gjF2uK9ohRqTz85oRnRsNdRQniC1rtd7pgL0tS1ZUEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKRWTRb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422558,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEBJkTcILMae+FUu+3hg06GkUdG1dWbiUTWcfiDWLkocjZVBcp00SmLgDK7IQPn8EEk/mNM51qAv7Co6JfjwBlMDuEBetM3nyxrY7WMEupVnKaMXeVUkJiMQsRkTNe8ZY6epi1gjF2uK9ohRqTz85oRnRsNdRQniC1rtd7pgL0tS1ZUEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKRWTRb"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEBJkTcILMae+FUu+3hg06GkUdG1dWbiUTWcfiDWLkocjZVBcp00SmLgDK7IQPn8EEk/mNM51qAv7Co6JfjwBlMDuEBetM3nyxrY7WMEupVnKaMXeVUkJiMQsRkTNe8ZY6epi1gjF2uK9ohRqTz85oRnRsNdRQniC1rtd7pgL0tS1ZUEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKRWTRb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422557,
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
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422557,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422556,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422556,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBJkTcILMae+FUu+3hg06GkUdG1dWbiUTWcfiDWLkocjZVBcp00SmLgDK7IQPn8EEk/mNM51qAv7Co6JfjwBlMDuEBetM3nyxrY7WMEupVnKaMXeVUkJiMQsRkTNe8ZY6epi1gjF2uK9ohRqTz85oRnRsNdRQniC1rtd7pgL0tS1ZUEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKRWTRb",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422555,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422555,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBrV28tuLgXBDpa2Zg22xF5n4NFyR2Iy2EbtixsOTdMx4oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEBJkTcILMae+FUu+3hg06GkUdG1dWbiUTWcfiDWLkocjZVBcp00SmLgDK7IQPn8EEk/mNM51qAv7Co6JfjwBlMDuEBetM3nyxrY7WMEupVnKaMXeVUkJiMQsRkTNe8ZY6epi1gjF2uK9ohRqTz85oRnRsNdRQniC1rtd7pgL0tS1ZUEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIAhhMG0rUY8FhCOvGh",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhA+250+EdjTqNH8J0mKTJRDxY4QG3VTjnEoy497HLX+P810QvfdGcD2fqpmYaPN6wWXidWGwrRVWxXdZWweYrcD7kBKPkBJTsBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhASZE3CCzGnvhVLvt4YNOhpFHRtXVm4lE1nH4g1i5KHI2VQXKdNEpi4AyuyED5/BBJP5jTOdagL+wqOiX48AZTA7hAXrTN58sa2O1jBLqVZymjF3lVJCYjELEZEzXvGWOnqYtYIxdrivaIUak8/OaEZ0bDXUUJ4gta7Xe6YC9LUtWVBLhI+EY5AqEGtXby24uBcEOlrZmDbbEXmfg0XJHYjLYRu2LGw5N0zHgCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIYTBtK1GPBYPiaqDQ=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422554,
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
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422554,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
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
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrV28tuLgXBDpa2Zg22xF5n4NFyR2Iy2EbtixsOTdMx4A6Ah5YXSCzjC3C5f2KaHrz5Qp6zPFnxOBCDOm/SZojmZpY49zzE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422553,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBZQ4jFsc0GZzwtL1gHojs82cpo1tOMmetTxKXT+e44uSB7Xw09rZ9U46bqEUkdohdh1fRaRaBcKsxIwhFkSfgGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maUin9Uy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422553,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBZQ4jFsc0GZzwtL1gHojs82cpo1tOMmetTxKXT+e44uSB7Xw09rZ9U46bqEUkdohdh1fRaRaBcKsxIwhFkSfgGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maUin9Uy",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422552,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBZQ4jFsc0GZzwtL1gHojs82cpo1tOMmetTxKXT+e44uSB7Xw09rZ9U46bqEUkdohdh1fRaRaBcKsxIwhFkSfgGuEDMz4v2NJ4+O9VKGQE3OaNBGBuhXwMjOJsFiFQUJraBWEFOPy2CvqSEqGxHGRXacHx610GPAz9VVsN7EyE5tgkEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maX4hzuE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422552,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEBZQ4jFsc0GZzwtL1gHojs82cpo1tOMmetTxKXT+e44uSB7Xw09rZ9U46bqEUkdohdh1fRaRaBcKsxIwhFkSfgGuEDMz4v2NJ4+O9VKGQE3OaNBGBuhXwMjOJsFiFQUJraBWEFOPy2CvqSEqGxHGRXacHx610GPAz9VVsN7EyE5tgkEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maX4hzuE"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEBZQ4jFsc0GZzwtL1gHojs82cpo1tOMmetTxKXT+e44uSB7Xw09rZ9U46bqEUkdohdh1fRaRaBcKsxIwhFkSfgGuEDMz4v2NJ4+O9VKGQE3OaNBGBuhXwMjOJsFiFQUJraBWEFOPy2CvqSEqGxHGRXacHx610GPAz9VVsN7EyE5tgkEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maX4hzuE"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422551,
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
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422551,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999997
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000003
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422550,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422550,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBZQ4jFsc0GZzwtL1gHojs82cpo1tOMmetTxKXT+e44uSB7Xw09rZ9U46bqEUkdohdh1fRaRaBcKsxIwhFkSfgGuEDMz4v2NJ4+O9VKGQE3OaNBGBuhXwMjOJsFiFQUJraBWEFOPy2CvqSEqGxHGRXacHx610GPAz9VVsN7EyE5tgkEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maX4hzuE",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/bDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAP0OPKg"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422549,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422549,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000003
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999997
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
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrV28tuLgXBDpa2Zg22xF5n4NFyR2Iy2EbtixsOTdMx4BKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAlCAHBM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422548,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBlf6R7aaO+yONBYyfouSdRvnppIrE1xCqKatmCRvxLyETPNmJaRuR0lrsvCzB/Ap0DTE3ne0PFRDJNbsewKOQDuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJE9bUb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422548,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBlf6R7aaO+yONBYyfouSdRvnppIrE1xCqKatmCRvxLyETPNmJaRuR0lrsvCzB/Ap0DTE3ne0PFRDJNbsewKOQDuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJE9bUb",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422547,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBlf6R7aaO+yONBYyfouSdRvnppIrE1xCqKatmCRvxLyETPNmJaRuR0lrsvCzB/Ap0DTE3ne0PFRDJNbsewKOQDuEDmCfEF/hQGFBP8XdqZV7THwNvjPrsSnJ1RHHgowNasx+uu/qHnoQ89oEdBjsR+2mdhEuGShZPUA25i/kpMniQGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLGmQDI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422547,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEBlf6R7aaO+yONBYyfouSdRvnppIrE1xCqKatmCRvxLyETPNmJaRuR0lrsvCzB/Ap0DTE3ne0PFRDJNbsewKOQDuEDmCfEF/hQGFBP8XdqZV7THwNvjPrsSnJ1RHHgowNasx+uu/qHnoQ89oEdBjsR+2mdhEuGShZPUA25i/kpMniQGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLGmQDI"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEBlf6R7aaO+yONBYyfouSdRvnppIrE1xCqKatmCRvxLyETPNmJaRuR0lrsvCzB/Ap0DTE3ne0PFRDJNbsewKOQDuEDmCfEF/hQGFBP8XdqZV7THwNvjPrsSnJ1RHHgowNasx+uu/qHnoQ89oEdBjsR+2mdhEuGShZPUA25i/kpMniQGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLGmQDI"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422546,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422546,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422545,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422545,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBlf6R7aaO+yONBYyfouSdRvnppIrE1xCqKatmCRvxLyETPNmJaRuR0lrsvCzB/Ap0DTE3ne0PFRDJNbsewKOQDuEDmCfEF/hQGFBP8XdqZV7THwNvjPrsSnJ1RHHgowNasx+uu/qHnoQ89oEdBjsR+2mdhEuGShZPUA25i/kpMniQGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLGmQDI",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA+250+EdjTqNH8J0mKTJRDxY4QG3VTjnEoy497HLX+P810QvfdGcD2fqpmYaPN6wWXidWGwrRVWxXdZWweYrcD7kBKPkBJTsBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhASZE3CCzGnvhVLvt4YNOhpFHRtXVm4lE1nH4g1i5KHI2VQXKdNEpi4AyuyED5/BBJP5jTOdagL+wqOiX48AZTA7hAXrTN58sa2O1jBLqVZymjF3lVJCYjELEZEzXvGWOnqYtYIxdrivaIUak8/OaEZ0bDXUUJ4gta7Xe6YC9LUtWVBLhI+EY5AqEGtXby24uBcEOlrZmDbbEXmfg0XJHYjLYRu2LGw5N0zHgCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIYTBtK1GPBYPiaqDQ==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA+250+EdjTqNH8J0mKTJRDxY4QG3VTjnEoy497HLX+P810QvfdGcD2fqpmYaPN6wWXidWGwrRVWxXdZWweYrcD7kBKPkBJTsBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhASZE3CCzGnvhVLvt4YNOhpFHRtXVm4lE1nH4g1i5KHI2VQXKdNEpi4AyuyED5/BBJP5jTOdagL+wqOiX48AZTA7hAXrTN58sa2O1jBLqVZymjF3lVJCYjELEZEzXvGWOnqYtYIxdrivaIUak8/OaEZ0bDXUUJ4gta7Xe6YC9LUtWVBLhI+EY5AqEGtXby24uBcEOlrZmDbbEXmfg0XJHYjLYRu2LGw5N0zHgCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIYTBtK1GPBYPiaqDQ==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "�&\u0016�>�ca��TK搐X�\u000b�\u001dک*���d��\f�",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422544,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422544,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBlf6R7aaO+yONBYyfouSdRvnppIrE1xCqKatmCRvxLyETPNmJaRuR0lrsvCzB/Ap0DTE3ne0PFRDJNbsewKOQDuEDmCfEF/hQGFBP8XdqZV7THwNvjPrsSnJ1RHHgowNasx+uu/qHnoQ89oEdBjsR+2mdhEuGShZPUA25i/kpMniQGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLGmQDI",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422543,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422543,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrV28tuLgXBDpa2Zg22xF5n4NFyR2Iy2EbtixsOTdMx4BaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC88AezQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422542,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDQ4/wXYgx8xHmeKfubLGbmLmFXAmjWz+t31Vz4AvC1gg6swYqf3C99Zt1oM1r3cDaLjwNBtomREz7RW/YIz+AGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt7lnYN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422542,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDQ4/wXYgx8xHmeKfubLGbmLmFXAmjWz+t31Vz4AvC1gg6swYqf3C99Zt1oM1r3cDaLjwNBtomREz7RW/YIz+AGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt7lnYN",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422541,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBL9M3pJ/UOUVbY6q3xbelv37jHSIzdK8SSv6ibvyAmJfb/NHlUDVEDUKR6OHlKg7n4TzD7ixx4M6VH23l4S+cBuEDQ4/wXYgx8xHmeKfubLGbmLmFXAmjWz+t31Vz4AvC1gg6swYqf3C99Zt1oM1r3cDaLjwNBtomREz7RW/YIz+AGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsil4IA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422541,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEBL9M3pJ/UOUVbY6q3xbelv37jHSIzdK8SSv6ibvyAmJfb/NHlUDVEDUKR6OHlKg7n4TzD7ixx4M6VH23l4S+cBuEDQ4/wXYgx8xHmeKfubLGbmLmFXAmjWz+t31Vz4AvC1gg6swYqf3C99Zt1oM1r3cDaLjwNBtomREz7RW/YIz+AGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsil4IA"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEBL9M3pJ/UOUVbY6q3xbelv37jHSIzdK8SSv6ibvyAmJfb/NHlUDVEDUKR6OHlKg7n4TzD7ixx4M6VH23l4S+cBuEDQ4/wXYgx8xHmeKfubLGbmLmFXAmjWz+t31Vz4AvC1gg6swYqf3C99Zt1oM1r3cDaLjwNBtomREz7RW/YIz+AGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsil4IA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422540,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422540,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422539,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422539,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBL9M3pJ/UOUVbY6q3xbelv37jHSIzdK8SSv6ibvyAmJfb/NHlUDVEDUKR6OHlKg7n4TzD7ixx4M6VH23l4S+cBuEDQ4/wXYgx8xHmeKfubLGbmLmFXAmjWz+t31Vz4AvC1gg6swYqf3C99Zt1oM1r3cDaLjwNBtomREz7RW/YIz+AGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsil4IA",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422538,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422538,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBrV28tuLgXBDpa2Zg22xF5n4NFyR2Iy2EbtixsOTdMx4oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEBL9M3pJ/UOUVbY6q3xbelv37jHSIzdK8SSv6ibvyAmJfb/NHlUDVEDUKR6OHlKg7n4TzD7ixx4M6VH23l4S+cBuEDQ4/wXYgx8xHmeKfubLGbmLmFXAmjWz+t31Vz4AvC1gg6swYqf3C99Zt1oM1r3cDaLjwNBtomREz7RW/YIz+AGuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMG0rUY8CPrc/y5",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAuRpBVVPZs2/yp421UxI+pYeJtX4h84gfybqfRAWkCM9ZCL5DQeI7Dft7oxxmRx26pwPsVgeZ46o6bgKB07zfArkBKPkBJTsBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAS/TN6Sf1DlFW2Oqt8W3pb9+4x0iM3SvEkr+om78gJiX2/zR5VA1RA1Ckejh5SoO5+E8w+4sceDOlR9t5eEvnAbhA0OP8F2IMfMR5nin7myxm5i5hVwJo1s/rd9Vc+ALwtYIOrMGKn9wvfWbdaDNa93A2i48DQbaJkRM+0Vv2CM/gBrhI+EY5AqEGtXby24uBcEOlrZmDbbEXmfg0XJHYjLYRu2LGw5N0zHgFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtK1GPAjZPtJOw=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422537,
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
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422537,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrV28tuLgXBDpa2Zg22xF5n4NFyR2Iy2EbtixsOTdMx4BqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeApNDv9A=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422536,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECLgUuR9T96eYFgoePfY/+V60EKv5kbrkzZ434i50bf5mu5Dq93pHqou6l+CqL3sMguDcGE+locrRtegi1DE/ADuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1B17N"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422536,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+JALAfhCuECLgUuR9T96eYFgoePfY/+V60EKv5kbrkzZ434i50bf5mu5Dq93pHqou6l+CqL3sMguDcGE+locrRtegi1DE/ADuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1B17N",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422535,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECLgUuR9T96eYFgoePfY/+V60EKv5kbrkzZ434i50bf5mu5Dq93pHqou6l+CqL3sMguDcGE+locrRtegi1DE/ADuECS0jPENDorT+Sw3vKJcXXsVQXm44f9PHZSOLnjo/bZZW1JEOCD4B+rNk2gASamgs6Z5H8HVC/h9gA7MNB+X3sHuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI0E1hj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422535,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuECLgUuR9T96eYFgoePfY/+V60EKv5kbrkzZ434i50bf5mu5Dq93pHqou6l+CqL3sMguDcGE+locrRtegi1DE/ADuECS0jPENDorT+Sw3vKJcXXsVQXm44f9PHZSOLnjo/bZZW1JEOCD4B+rNk2gASamgs6Z5H8HVC/h9gA7MNB+X3sHuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI0E1hj"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuECLgUuR9T96eYFgoePfY/+V60EKv5kbrkzZ434i50bf5mu5Dq93pHqou6l+CqL3sMguDcGE+locrRtegi1DE/ADuECS0jPENDorT+Sw3vKJcXXsVQXm44f9PHZSOLnjo/bZZW1JEOCD4B+rNk2gASamgs6Z5H8HVC/h9gA7MNB+X3sHuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI0E1hj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422534,
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
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422534,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422533,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422533,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECLgUuR9T96eYFgoePfY/+V60EKv5kbrkzZ434i50bf5mu5Dq93pHqou6l+CqL3sMguDcGE+locrRtegi1DE/ADuECS0jPENDorT+Sw3vKJcXXsVQXm44f9PHZSOLnjo/bZZW1JEOCD4B+rNk2gASamgs6Z5H8HVC/h9gA7MNB+X3sHuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI0E1hj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422532,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422532,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrV28tuLgXBDpa2Zg22xF5n4NFyR2Iy2EbtixsOTdMx4B6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCy32NqU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422531,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAYewzCcAtenAgl2VMla9rWLdM8ngPZwHoxRzh87opJP5+oVfjrmZWYa6aOwPrapy7oQiqrrPNUIcmVoNERi5EEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgskzAcX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422531,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAYewzCcAtenAgl2VMla9rWLdM8ngPZwHoxRzh87opJP5+oVfjrmZWYa6aOwPrapy7oQiqrrPNUIcmVoNERi5EEuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgskzAcX",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422530,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAYewzCcAtenAgl2VMla9rWLdM8ngPZwHoxRzh87opJP5+oVfjrmZWYa6aOwPrapy7oQiqrrPNUIcmVoNERi5EEuEAZAMGIzGrW89uHhg8Eb/+wWrU81vWFHAI5EHNqZ9JLeiHbJg/aQDgRVoVKZgSz+idAiBlgkIZpBvLfR6apm4oOuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgur+g+P"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422530,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEAYewzCcAtenAgl2VMla9rWLdM8ngPZwHoxRzh87opJP5+oVfjrmZWYa6aOwPrapy7oQiqrrPNUIcmVoNERi5EEuEAZAMGIzGrW89uHhg8Eb/+wWrU81vWFHAI5EHNqZ9JLeiHbJg/aQDgRVoVKZgSz+idAiBlgkIZpBvLfR6apm4oOuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgur+g+P"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "state": "tx_+NILAfiEuEAYewzCcAtenAgl2VMla9rWLdM8ngPZwHoxRzh87opJP5+oVfjrmZWYa6aOwPrapy7oQiqrrPNUIcmVoNERi5EEuEAZAMGIzGrW89uHhg8Eb/+wWrU81vWFHAI5EHNqZ9JLeiHbJg/aQDgRVoVKZgSz+idAiBlgkIZpBvLfR6apm4oOuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgur+g+P"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422529,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422529,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422528,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422528,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAYewzCcAtenAgl2VMla9rWLdM8ngPZwHoxRzh87opJP5+oVfjrmZWYa6aOwPrapy7oQiqrrPNUIcmVoNERi5EEuEAZAMGIzGrW89uHhg8Eb/+wWrU81vWFHAI5EHNqZ9JLeiHbJg/aQDgRVoVKZgSz+idAiBlgkIZpBvLfR6apm4oOuEj4RjkCoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeAegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgur+g+P",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAuRpBVVPZs2/yp421UxI+pYeJtX4h84gfybqfRAWkCM9ZCL5DQeI7Dft7oxxmRx26pwPsVgeZ46o6bgKB07zfArkBKPkBJTsBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAS/TN6Sf1DlFW2Oqt8W3pb9+4x0iM3SvEkr+om78gJiX2/zR5VA1RA1Ckejh5SoO5+E8w+4sceDOlR9t5eEvnAbhA0OP8F2IMfMR5nin7myxm5i5hVwJo1s/rd9Vc+ALwtYIOrMGKn9wvfWbdaDNa93A2i48DQbaJkRM+0Vv2CM/gBrhI+EY5AqEGtXby24uBcEOlrZmDbbEXmfg0XJHYjLYRu2LGw5N0zHgFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtK1GPAjZPtJOw==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAuRpBVVPZs2/yp421UxI+pYeJtX4h84gfybqfRAWkCM9ZCL5DQeI7Dft7oxxmRx26pwPsVgeZ46o6bgKB07zfArkBKPkBJTsBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAS/TN6Sf1DlFW2Oqt8W3pb9+4x0iM3SvEkr+om78gJiX2/zR5VA1RA1Ckejh5SoO5+E8w+4sceDOlR9t5eEvnAbhA0OP8F2IMfMR5nin7myxm5i5hVwJo1s/rd9Vc+ALwtYIOrMGKn9wvfWbdaDNa93A2i48DQbaJkRM+0Vv2CM/gBrhI+EY5AqEGtXby24uBcEOlrZmDbbEXmfg0XJHYjLYRu2LGw5N0zHgFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtK1GPAjZPtJOw==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "Ú��7\u001fr`��\u0017xZ^�P��\u0001�ɕk���@J<\u0015",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBrV28tuLgXBDpa2Zg22xF5n4NFyR2Iy2EbtixsOTdMx4oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/+GHLHOiuwBAIYPXtZ/KABZENwDTQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422527,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBdE/LxlQRYKbpX6ynCgV/eDixA4xCf+bExpsRFZIxy1uyPzH0CsNUK5rmMoZY6LMvXiyBF6cvieSktSq/Ff2gCuF/4XTUBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAWbppEP8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422527,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBdE/LxlQRYKbpX6ynCgV/eDixA4xCf+bExpsRFZIxy1uyPzH0CsNUK5rmMoZY6LMvXiyBF6cvieSktSq/Ff2gCuF/4XTUBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAWbppEP8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422526,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBdE/LxlQRYKbpX6ynCgV/eDixA4xCf+bExpsRFZIxy1uyPzH0CsNUK5rmMoZY6LMvXiyBF6cvieSktSq/Ff2gCuED/m0VEKb9Tgkld8eHQYonnKKyk5BvY1AlmOXWCoNNoL68ScIiuNMe2mjjf88cIh2yjcUs+RQieUV3HDU84xH4GuF/4XTUBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAWY70OcY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
  "id": -576460752303422526,
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBdE/LxlQRYKbpX6ynCgV/eDixA4xCf+bExpsRFZIxy1uyPzH0CsNUK5rmMoZY6LMvXiyBF6cvieSktSq/Ff2gCuED/m0VEKb9Tgkld8eHQYonnKKyk5BvY1AlmOXWCoNNoL68ScIiuNMe2mjjf88cIh2yjcUs+RQieUV3HDU84xH4GuF/4XTUBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAWY70OcY=",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBdE/LxlQRYKbpX6ynCgV/eDixA4xCf+bExpsRFZIxy1uyPzH0CsNUK5rmMoZY6LMvXiyBF6cvieSktSq/Ff2gCuED/m0VEKb9Tgkld8eHQYonnKKyk5BvY1AlmOXWCoNNoL68ScIiuNMe2mjjf88cIh2yjcUs+RQieUV3HDU84xH4GuF/4XTUBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAWY70OcY=",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBdE/LxlQRYKbpX6ynCgV/eDixA4xCf+bExpsRFZIxy1uyPzH0CsNUK5rmMoZY6LMvXiyBF6cvieSktSq/Ff2gCuED/m0VEKb9Tgkld8eHQYonnKKyk5BvY1AlmOXWCoNNoL68ScIiuNMe2mjjf88cIh2yjcUs+RQieUV3HDU84xH4GuF/4XTUBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAWY70OcY=",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBdE/LxlQRYKbpX6ynCgV/eDixA4xCf+bExpsRFZIxy1uyPzH0CsNUK5rmMoZY6LMvXiyBF6cvieSktSq/Ff2gCuED/m0VEKb9Tgkld8eHQYonnKKyk5BvY1AlmOXWCoNNoL68ScIiuNMe2mjjf88cIh2yjcUs+RQieUV3HDU84xH4GuF/4XTUBoQa1dvLbi4FwQ6WtmYNtsReZ+DRckdiMthG7YsbDk3TMeKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAWY70OcY=",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
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
    "channel_id": "ch_2NvGhqSW5d7iYZqDDwWjrWFjgoq2s1P1jHDpdKaYCokCJ2zFGY",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
