
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
      "fsm_id": "ba_6oJ3dvml0emd6WNj9O0BU4BN7iiAnJmhif8U8sUrTAgCTG4C"
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
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

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
      "fsm_id": "ba_AfiUmH2nC0K2ahoD7YfRe+zZerIpEh8RdySIJGKEoMzNini1"
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
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFrquE0Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423396,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECHJGs1RtWJ44fujtem+UAEHFhJjWGZHZWmDFMcYLFlLoa5aCjMZtFRMZV45je0RODTcq+VxxRk3q3ughYdjDYHuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LBST19t0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423396,
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "fsm_id": "ba_AfiUmH2nC0K2ahoD7YfRe+zZerIpEh8RdySIJGKEoMzNini1",
      "signed_tx": "tx_+MsLAfhCuECHJGs1RtWJ44fujtem+UAEHFhJjWGZHZWmDFMcYLFlLoa5aCjMZtFRMZV45je0RODTcq+VxxRk3q3ughYdjDYHuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LBST19t0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423395,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAWLRoHJse73PTdpa553U0mW77tYc1vLTW0DxT8IKBfp1BhTdkNxpZsDE8nAwv9k75cOS9CXVSfIEyisOJyUmvAbhAhyRrNUbVieOH7o7XpvlABBxYSY1hmR2VpgxTHGCxZS6GuWgozGbRUTGVeOY3tETg03KvlccUZN6t7oIWHYw2B7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwVE85L0"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
  "id": -576460752303423395,
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAWLRoHJse73PTdpa553U0mW77tYc1vLTW0DxT8IKBfp1BhTdkNxpZsDE8nAwv9k75cOS9CXVSfIEyisOJyUmvAbhAhyRrNUbVieOH7o7XpvlABBxYSY1hmR2VpgxTHGCxZS6GuWgozGbRUTGVeOY3tETg03KvlccUZN6t7oIWHYw2B7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwVE85L0",
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_6oJ3dvml0emd6WNj9O0BU4BN7iiAnJmhif8U8sUrTAgCTG4C"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "action": "system",
      "tag": "pong"
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAWLRoHJse73PTdpa553U0mW77tYc1vLTW0DxT8IKBfp1BhTdkNxpZsDE8nAwv9k75cOS9CXVSfIEyisOJyUmvAbhAhyRrNUbVieOH7o7XpvlABBxYSY1hmR2VpgxTHGCxZS6GuWgozGbRUTGVeOY3tETg03KvlccUZN6t7oIWHYw2B7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwVE85L0",
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
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "action": "system",
      "tag": "pong"
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAWLRoHJse73PTdpa553U0mW77tYc1vLTW0DxT8IKBfp1BhTdkNxpZsDE8nAwv9k75cOS9CXVSfIEyisOJyUmvAbhAhyRrNUbVieOH7o7XpvlABBxYSY1hmR2VpgxTHGCxZS6GuWgozGbRUTGVeOY3tETg03KvlccUZN6t7oIWHYw2B7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwVE85L0",
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAWLRoHJse73PTdpa553U0mW77tYc1vLTW0DxT8IKBfp1BhTdkNxpZsDE8nAwv9k75cOS9CXVSfIEyisOJyUmvAbhAhyRrNUbVieOH7o7XpvlABBxYSY1hmR2VpgxTHGCxZS6GuWgozGbRUTGVeOY3tETg03KvlccUZN6t7oIWHYw2B7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwVE85L0",
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
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "action": "system",
      "tag": "pong"
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "message": {
        "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "message": {
        "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
  "id": -576460752303423394,
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
  "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
  "id": -576460752303423394,
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "state": "tx_+QENCwH4hLhAWLRoHJse73PTdpa553U0mW77tYc1vLTW0DxT8IKBfp1BhTdkNxpZsDE8nAwv9k75cOS9CXVSfIEyisOJyUmvAbhAhyRrNUbVieOH7o7XpvlABBxYSY1hmR2VpgxTHGCxZS6GuWgozGbRUTGVeOY3tETg03KvlccUZN6t7oIWHYw2B7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwVE85L0"
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
    "data": {
      "state": "tx_+QENCwH4hLhAWLRoHJse73PTdpa553U0mW77tYc1vLTW0DxT8IKBfp1BhTdkNxpZsDE8nAwv9k75cOS9CXVSfIEyisOJyUmvAbhAhyRrNUbVieOH7o7XpvlABBxYSY1hmR2VpgxTHGCxZS6GuWgozGbRUTGVeOY3tETg03KvlccUZN6t7oIWHYw2B7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwVE85L0"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423393,
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
  "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
  "id": -576460752303423393,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423392,
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
    "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
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
  "channel_id": "ch_xnogBD7wejyVG9ojqifeUGhMsJ7zHXiUcyBYPv4q65ysFYn7Z",
  "id": -576460752303423392,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
