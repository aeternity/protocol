
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
      "fsm_id": "ba_XnonqZdbSfVk9U8YyZ00xw/l4iev/v4JY1PGztv3sbwxd7CV"
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
      "fsm_id": "ba_QYk9aLW5O0N7v89u/2eDz4n0sff3aliKrCs76q7JnWONNJxN"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBxEWU2RE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421971,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEDkw/nOBHX2QB6n8vuV2Ny2JqXNiYMr/6ztnfctSrr8Yb5A9jtkfTcO7eFTJMkK7Gdlb/L7EBS0wHtI+5fL4/4OuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgcQinAeY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421971,
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "fsm_id": "ba_QYk9aLW5O0N7v89u/2eDz4n0sff3aliKrCs76q7JnWONNJxN",
      "signed_tx": "tx_+MwLAfhCuEDkw/nOBHX2QB6n8vuV2Ny2JqXNiYMr/6ztnfctSrr8Yb5A9jtkfTcO7eFTJMkK7Gdlb/L7EBS0wHtI+5fL4/4OuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgcQinAeY",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421970,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAr9L7px41MMCw7h9BqnUOGaQWjGZVeZq53sAp7mBIh+D8sK4XWB4WfHS7zSjbz1SpkrsN1dR3vQJDycc5dGkAA7hA5MP5zgR19kAep/L7ldjctialzYmDK/+s7Z33LUq6/GG+QPY7ZH03Du3hUyTJCuxnZW/y+xAUtMB7SPuXy+P+DriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HER2ff5w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
  "id": -576460752303421970,
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAr9L7px41MMCw7h9BqnUOGaQWjGZVeZq53sAp7mBIh+D8sK4XWB4WfHS7zSjbz1SpkrsN1dR3vQJDycc5dGkAA7hA5MP5zgR19kAep/L7ldjctialzYmDK/+s7Z33LUq6/GG+QPY7ZH03Du3hUyTJCuxnZW/y+xAUtMB7SPuXy+P+DriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HER2ff5w==",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_XnonqZdbSfVk9U8YyZ00xw/l4iev/v4JY1PGztv3sbwxd7CV"
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAr9L7px41MMCw7h9BqnUOGaQWjGZVeZq53sAp7mBIh+D8sK4XWB4WfHS7zSjbz1SpkrsN1dR3vQJDycc5dGkAA7hA5MP5zgR19kAep/L7ldjctialzYmDK/+s7Z33LUq6/GG+QPY7ZH03Du3hUyTJCuxnZW/y+xAUtMB7SPuXy+P+DriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HER2ff5w==",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAr9L7px41MMCw7h9BqnUOGaQWjGZVeZq53sAp7mBIh+D8sK4XWB4WfHS7zSjbz1SpkrsN1dR3vQJDycc5dGkAA7hA5MP5zgR19kAep/L7ldjctialzYmDK/+s7Z33LUq6/GG+QPY7ZH03Du3hUyTJCuxnZW/y+xAUtMB7SPuXy+P+DriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HER2ff5w==",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAr9L7px41MMCw7h9BqnUOGaQWjGZVeZq53sAp7mBIh+D8sK4XWB4WfHS7zSjbz1SpkrsN1dR3vQJDycc5dGkAA7hA5MP5zgR19kAep/L7ldjctialzYmDK/+s7Z33LUq6/GG+QPY7ZH03Du3hUyTJCuxnZW/y+xAUtMB7SPuXy+P+DriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HER2ff5w==",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "message": {
        "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "message": {
        "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
  "id": -576460752303421969,
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
  "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
  "id": -576460752303421969,
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "state": "tx_+QEOCwH4hLhAr9L7px41MMCw7h9BqnUOGaQWjGZVeZq53sAp7mBIh+D8sK4XWB4WfHS7zSjbz1SpkrsN1dR3vQJDycc5dGkAA7hA5MP5zgR19kAep/L7ldjctialzYmDK/+s7Z33LUq6/GG+QPY7ZH03Du3hUyTJCuxnZW/y+xAUtMB7SPuXy+P+DriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HER2ff5w=="
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
    "data": {
      "state": "tx_+QEOCwH4hLhAr9L7px41MMCw7h9BqnUOGaQWjGZVeZq53sAp7mBIh+D8sK4XWB4WfHS7zSjbz1SpkrsN1dR3vQJDycc5dGkAA7hA5MP5zgR19kAep/L7ldjctialzYmDK/+s7Z33LUq6/GG+QPY7ZH03Du3hUyTJCuxnZW/y+xAUtMB7SPuXy+P+DriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HER2ff5w=="
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
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1018,
        "message": "Not allowed at current channel state"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update",
      "params": {
        "error": 42
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
  "method": "channels.update",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1018,
        "message": "Not allowed at current channel state"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update",
      "params": {
        "error": 42
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
  "id": -576460752303421968,
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
  "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
  "id": -576460752303421968,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421967,
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
    "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
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
  "channel_id": "ch_2Ci7Twr7bBQA8tiwmx2VygqYKjw12b8zqJzKryuVhXMbp2RSsp",
  "id": -576460752303421967,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
