
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
      "fsm_id": "ba_O1QKd8+w/YJR8oDuLqwvptNYVsypnqwQp8VW+F1q+iVv3Dlj"
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
      "fsm_id": "ba_1U0HpdIXTU1R/4jFrnYOXf6oWYPag1ohjqC7JYhpCfKff82v"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsGREHs3g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423391,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDxpwBVUzrAOM4ngixskrw6peGFcHgtdFYWK+JAaVUKwnEnZn5y1SMeWaPh5Jv5WhdlFgd+51G/hRjEpudWQE4EuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LBjAogN8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423391,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "fsm_id": "ba_1U0HpdIXTU1R/4jFrnYOXf6oWYPag1ohjqC7JYhpCfKff82v",
      "signed_tx": "tx_+MsLAfhCuEDxpwBVUzrAOM4ngixskrw6peGFcHgtdFYWK+JAaVUKwnEnZn5y1SMeWaPh5Jv5WhdlFgd+51G/hRjEpudWQE4EuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LBjAogN8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423390,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAouzUPw6tcevs7tjWPzma4coGOaaBL2ZHqC9/RGwQ3Lv/FpFA65m00mz5h0ixmHlhRybl2TELR5rsXYXGQ4v8BbhA8acAVVM6wDjOJ4IsbJK8OqXhhXB4LXRWFiviQGlVCsJxJ2Z+ctUjHlmj4eSb+VoXZRYHfudRv4UYxKbnVkBOBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwaXyYtW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423390,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAouzUPw6tcevs7tjWPzma4coGOaaBL2ZHqC9/RGwQ3Lv/FpFA65m00mz5h0ixmHlhRybl2TELR5rsXYXGQ4v8BbhA8acAVVM6wDjOJ4IsbJK8OqXhhXB4LXRWFiviQGlVCsJxJ2Z+ctUjHlmj4eSb+VoXZRYHfudRv4UYxKbnVkBOBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwaXyYtW",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_O1QKd8+w/YJR8oDuLqwvptNYVsypnqwQp8VW+F1q+iVv3Dlj"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAouzUPw6tcevs7tjWPzma4coGOaaBL2ZHqC9/RGwQ3Lv/FpFA65m00mz5h0ixmHlhRybl2TELR5rsXYXGQ4v8BbhA8acAVVM6wDjOJ4IsbJK8OqXhhXB4LXRWFiviQGlVCsJxJ2Z+ctUjHlmj4eSb+VoXZRYHfudRv4UYxKbnVkBOBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwaXyYtW",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAouzUPw6tcevs7tjWPzma4coGOaaBL2ZHqC9/RGwQ3Lv/FpFA65m00mz5h0ixmHlhRybl2TELR5rsXYXGQ4v8BbhA8acAVVM6wDjOJ4IsbJK8OqXhhXB4LXRWFiviQGlVCsJxJ2Z+ctUjHlmj4eSb+VoXZRYHfudRv4UYxKbnVkBOBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwaXyYtW",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAouzUPw6tcevs7tjWPzma4coGOaaBL2ZHqC9/RGwQ3Lv/FpFA65m00mz5h0ixmHlhRybl2TELR5rsXYXGQ4v8BbhA8acAVVM6wDjOJ4IsbJK8OqXhhXB4LXRWFiviQGlVCsJxJ2Z+ctUjHlmj4eSb+VoXZRYHfudRv4UYxKbnVkBOBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwaXyYtW",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "message": {
        "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "message": {
        "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
  "id": -576460752303423389,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423389,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+QENCwH4hLhAouzUPw6tcevs7tjWPzma4coGOaaBL2ZHqC9/RGwQ3Lv/FpFA65m00mz5h0ixmHlhRybl2TELR5rsXYXGQ4v8BbhA8acAVVM6wDjOJ4IsbJK8OqXhhXB4LXRWFiviQGlVCsJxJ2Z+ctUjHlmj4eSb+VoXZRYHfudRv4UYxKbnVkBOBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwaXyYtW"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+QENCwH4hLhAouzUPw6tcevs7tjWPzma4coGOaaBL2ZHqC9/RGwQ3Lv/FpFA65m00mz5h0ixmHlhRybl2TELR5rsXYXGQ4v8BbhA8acAVVM6wDjOJ4IsbJK8OqXhhXB4LXRWFiviQGlVCsJxJ2Z+ctUjHlmj4eSb+VoXZRYHfudRv4UYxKbnVkBOBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwaXyYtW"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423388,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "error": {
    "code": 2,
    "data": [
      {
        "code": 1012,
        "message": "Offchain tx expected"
      }
    ],
    "message": "Action not allowed",
    "request": {
      "id": -576460752303423388,
      "jsonrpc": "2.0",
      "method": "channels.snapshot_solo",
      "params": {}
    }
  },
  "id": -576460752303423388,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423387,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423387,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAh94wP8=",
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
  "id": -576460752303423386,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB9NAVAssRUY9g/fJ5fbOiM2yW1OKr8Av5UdM/LnD7P8OfYxzO6vCBcCKCiBfRiolaNf5wcD52VB1aCtVkjiT8PuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJxl6TK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423386,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB9NAVAssRUY9g/fJ5fbOiM2yW1OKr8Av5UdM/LnD7P8OfYxzO6vCBcCKCiBfRiolaNf5wcD52VB1aCtVkjiT8PuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJxl6TK",
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
  "id": -576460752303423385,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB9NAVAssRUY9g/fJ5fbOiM2yW1OKr8Av5UdM/LnD7P8OfYxzO6vCBcCKCiBfRiolaNf5wcD52VB1aCtVkjiT8PuEDhPn/qdwcotSx4UmiIEC/kASFOtaucSahHPV5W72IlhlAJuSUfbTN5HAybvd83PXRkTIzB7d0/WOJKR+11dYILuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLB6nvS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423385,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEB9NAVAssRUY9g/fJ5fbOiM2yW1OKr8Av5UdM/LnD7P8OfYxzO6vCBcCKCiBfRiolaNf5wcD52VB1aCtVkjiT8PuEDhPn/qdwcotSx4UmiIEC/kASFOtaucSahHPV5W72IlhlAJuSUfbTN5HAybvd83PXRkTIzB7d0/WOJKR+11dYILuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLB6nvS"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEB9NAVAssRUY9g/fJ5fbOiM2yW1OKr8Av5UdM/LnD7P8OfYxzO6vCBcCKCiBfRiolaNf5wcD52VB1aCtVkjiT8PuEDhPn/qdwcotSx4UmiIEC/kASFOtaucSahHPV5W72IlhlAJuSUfbTN5HAybvd83PXRkTIzB7d0/WOJKR+11dYILuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLB6nvS"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423384,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423384,
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
  "id": -576460752303423383,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423383,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB9NAVAssRUY9g/fJ5fbOiM2yW1OKr8Av5UdM/LnD7P8OfYxzO6vCBcCKCiBfRiolaNf5wcD52VB1aCtVkjiT8PuEDhPn/qdwcotSx4UmiIEC/kASFOtaucSahHPV5W72IlhlAJuSUfbTN5HAybvd83PXRkTIzB7d0/WOJKR+11dYILuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLB6nvS",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423382,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423382,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC+y3Nq4=",
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
  "id": -576460752303423381,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBGmNyZnu1nVVUlYFJUNBNFbHRp2tOb3ysoSGRj0eXlQxOePoQ+tLCI0/KpWGaOYimXzoxJt8U/qaq7hdpsgCgAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtb59Tl"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423381,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBGmNyZnu1nVVUlYFJUNBNFbHRp2tOb3ysoSGRj0eXlQxOePoQ+tLCI0/KpWGaOYimXzoxJt8U/qaq7hdpsgCgAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtb59Tl",
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
  "id": -576460752303423380,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAIT9hAXf7+2pRd2XfGb4J64hr+MAoe8xvmluBFlT0NFmpqMKAjQUhlfPBiaQ+dbMsQI8zp7pVuqpTcqnuyxO0GuEBGmNyZnu1nVVUlYFJUNBNFbHRp2tOb3ysoSGRj0eXlQxOePoQ+tLCI0/KpWGaOYimXzoxJt8U/qaq7hdpsgCgAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs3JIEG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423380,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEAIT9hAXf7+2pRd2XfGb4J64hr+MAoe8xvmluBFlT0NFmpqMKAjQUhlfPBiaQ+dbMsQI8zp7pVuqpTcqnuyxO0GuEBGmNyZnu1nVVUlYFJUNBNFbHRp2tOb3ysoSGRj0eXlQxOePoQ+tLCI0/KpWGaOYimXzoxJt8U/qaq7hdpsgCgAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs3JIEG"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEAIT9hAXf7+2pRd2XfGb4J64hr+MAoe8xvmluBFlT0NFmpqMKAjQUhlfPBiaQ+dbMsQI8zp7pVuqpTcqnuyxO0GuEBGmNyZnu1nVVUlYFJUNBNFbHRp2tOb3ysoSGRj0eXlQxOePoQ+tLCI0/KpWGaOYimXzoxJt8U/qaq7hdpsgCgAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs3JIEG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423379,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423379,
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
  "id": -576460752303423378,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423378,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAIT9hAXf7+2pRd2XfGb4J64hr+MAoe8xvmluBFlT0NFmpqMKAjQUhlfPBiaQ+dbMsQI8zp7pVuqpTcqnuyxO0GuEBGmNyZnu1nVVUlYFJUNBNFbHRp2tOb3ysoSGRj0eXlQxOePoQ+tLCI0/KpWGaOYimXzoxJt8U/qaq7hdpsgCgAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs3JIEG",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423377,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423377,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAIT9hAXf7+2pRd2XfGb4J64hr+MAoe8xvmluBFlT0NFmpqMKAjQUhlfPBiaQ+dbMsQI8zp7pVuqpTcqnuyxO0GuEBGmNyZnu1nVVUlYFJUNBNFbHRp2tOb3ysoSGRj0eXlQxOePoQ+tLCI0/KpWGaOYimXzoxJt8U/qaq7hdpsgCgAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMG0SswAAdEyzJB",
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
    "signed_tx": "tx_+QFxCwH4QrhAlovoVxSkd9dQ6/n3QGjKv6hEGFOdz9TaqiF7hZweZRkTG/L8cnoRmR8Fp2uNe0Vd9qhLfi8ONIak+SBPn9ulDLkBKPkBJTsBoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhACE/YQF3+/tqUXdl3xm+CeuIa/jAKHvMb5pbgRZU9DRZqajCgI0FIZXzwYmkPnWzLECPM6e6VbqqU3Kp7ssTtBrhARpjcmZ7tZ1VVJWBSVDQTRWx0adrTm98rKEhkY9Hl5UMTnj6EPrSwiNPyqVhmjmIpl86MSbfFP6mqu4XabIAoALhI+EY5AqEGDHvsF0dfgpSxJ2XzOfcrhtuKWBCedRbbkWJF6whRCFIDoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtErMAAHuhVB3w=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423376,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423376,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAlPKqwg=",
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
  "id": -576460752303423375,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAQbez8boifvB7pkVjRdGwMcMehdBVk3oAPiUv7wI/o65td2bOz+1tuVDs/DJAgzzrLU+T5e4Jxdr0CK9SkZYILuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLIpw/9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423375,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAQbez8boifvB7pkVjRdGwMcMehdBVk3oAPiUv7wI/o65td2bOz+1tuVDs/DJAgzzrLU+T5e4Jxdr0CK9SkZYILuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLIpw/9",
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
  "id": -576460752303423374,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAQbez8boifvB7pkVjRdGwMcMehdBVk3oAPiUv7wI/o65td2bOz+1tuVDs/DJAgzzrLU+T5e4Jxdr0CK9SkZYILuECqjtYt0vdrkYgIEze2EJvPAfJlnKhW6mZIzHVqvAphbyjz5aIwY2Q/5OKALWeQ8R9CqBqm6PTnfup8TqPO8Y0HuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKtWir6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423374,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEAQbez8boifvB7pkVjRdGwMcMehdBVk3oAPiUv7wI/o65td2bOz+1tuVDs/DJAgzzrLU+T5e4Jxdr0CK9SkZYILuECqjtYt0vdrkYgIEze2EJvPAfJlnKhW6mZIzHVqvAphbyjz5aIwY2Q/5OKALWeQ8R9CqBqm6PTnfup8TqPO8Y0HuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKtWir6"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEAQbez8boifvB7pkVjRdGwMcMehdBVk3oAPiUv7wI/o65td2bOz+1tuVDs/DJAgzzrLU+T5e4Jxdr0CK9SkZYILuECqjtYt0vdrkYgIEze2EJvPAfJlnKhW6mZIzHVqvAphbyjz5aIwY2Q/5OKALWeQ8R9CqBqm6PTnfup8TqPO8Y0HuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKtWir6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423373,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423373,
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
  "id": -576460752303423372,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423372,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAQbez8boifvB7pkVjRdGwMcMehdBVk3oAPiUv7wI/o65td2bOz+1tuVDs/DJAgzzrLU+T5e4Jxdr0CK9SkZYILuECqjtYt0vdrkYgIEze2EJvPAfJlnKhW6mZIzHVqvAphbyjz5aIwY2Q/5OKALWeQ8R9CqBqm6PTnfup8TqPO8Y0HuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKtWir6",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423371,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423371,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC8wNAt8=",
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
  "id": -576460752303423370,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECuhf28Eg1jER65iDf3bEZK2gvCTt6Cha20Juol2vBpJdhRjbGY1tkvRfoUV4er3VfjDpMpW0v6fPukeeUJdIYOuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsLddfe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423370,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+JALAfhCuECuhf28Eg1jER65iDf3bEZK2gvCTt6Cha20Juol2vBpJdhRjbGY1tkvRfoUV4er3VfjDpMpW0v6fPukeeUJdIYOuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsLddfe",
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
  "id": -576460752303423369,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECc5XmPP3ib8FL4MGLD18PpIRckbOlBEUWvsmCC6IJi0Xb4eMoHg4UN1yT8RshGg7+xOSizlYcCFKPGBdR2yWQJuECuhf28Eg1jER65iDf3bEZK2gvCTt6Cha20Juol2vBpJdhRjbGY1tkvRfoUV4er3VfjDpMpW0v6fPukeeUJdIYOuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsHEnl6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423369,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuECc5XmPP3ib8FL4MGLD18PpIRckbOlBEUWvsmCC6IJi0Xb4eMoHg4UN1yT8RshGg7+xOSizlYcCFKPGBdR2yWQJuECuhf28Eg1jER65iDf3bEZK2gvCTt6Cha20Juol2vBpJdhRjbGY1tkvRfoUV4er3VfjDpMpW0v6fPukeeUJdIYOuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsHEnl6"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuECc5XmPP3ib8FL4MGLD18PpIRckbOlBEUWvsmCC6IJi0Xb4eMoHg4UN1yT8RshGg7+xOSizlYcCFKPGBdR2yWQJuECuhf28Eg1jER65iDf3bEZK2gvCTt6Cha20Juol2vBpJdhRjbGY1tkvRfoUV4er3VfjDpMpW0v6fPukeeUJdIYOuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsHEnl6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423368,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423368,
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
  "id": -576460752303423367,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423367,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECc5XmPP3ib8FL4MGLD18PpIRckbOlBEUWvsmCC6IJi0Xb4eMoHg4UN1yT8RshGg7+xOSizlYcCFKPGBdR2yWQJuECuhf28Eg1jER65iDf3bEZK2gvCTt6Cha20Juol2vBpJdhRjbGY1tkvRfoUV4er3VfjDpMpW0v6fPukeeUJdIYOuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsHEnl6",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAlovoVxSkd9dQ6/n3QGjKv6hEGFOdz9TaqiF7hZweZRkTG/L8cnoRmR8Fp2uNe0Vd9qhLfi8ONIak+SBPn9ulDLkBKPkBJTsBoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhACE/YQF3+/tqUXdl3xm+CeuIa/jAKHvMb5pbgRZU9DRZqajCgI0FIZXzwYmkPnWzLECPM6e6VbqqU3Kp7ssTtBrhARpjcmZ7tZ1VVJWBSVDQTRWx0adrTm98rKEhkY9Hl5UMTnj6EPrSwiNPyqVhmjmIpl86MSbfFP6mqu4XabIAoALhI+EY5AqEGDHvsF0dfgpSxJ2XzOfcrhtuKWBCedRbbkWJF6whRCFIDoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtErMAAHuhVB3w==",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAlovoVxSkd9dQ6/n3QGjKv6hEGFOdz9TaqiF7hZweZRkTG/L8cnoRmR8Fp2uNe0Vd9qhLfi8ONIak+SBPn9ulDLkBKPkBJTsBoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhACE/YQF3+/tqUXdl3xm+CeuIa/jAKHvMb5pbgRZU9DRZqajCgI0FIZXzwYmkPnWzLECPM6e6VbqqU3Kp7ssTtBrhARpjcmZ7tZ1VVJWBSVDQTRWx0adrTm98rKEhkY9Hl5UMTnj6EPrSwiNPyqVhmjmIpl86MSbfFP6mqu4XabIAoALhI+EY5AqEGDHvsF0dfgpSxJ2XzOfcrhtuKWBCedRbbkWJF6whRCFIDoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtErMAAHuhVB3w==",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "{߾�KC��C]��?���\\�\n5-�\u000b�?�y,�\u0001",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423366,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423366,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuECc5XmPP3ib8FL4MGLD18PpIRckbOlBEUWvsmCC6IJi0Xb4eMoHg4UN1yT8RshGg7+xOSizlYcCFKPGBdR2yWQJuECuhf28Eg1jER65iDf3bEZK2gvCTt6Cha20Juol2vBpJdhRjbGY1tkvRfoUV4er3VfjDpMpW0v6fPukeeUJdIYOuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMG0SswAAG8gU6J",
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
    "signed_tx": "tx_+QFxCwH4QrhA3lr3XqnNJngOscsZ6cBhoXsRktGShu3uKfIVVCXK8gLahXR1cmQ7Cs2ZXwCBoLW+fMIJSt6GsLfHyFd2mfqyCbkBKPkBJTsBoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAnOV5jz94m/BS+DBiw9fD6SEXJGzpQRFFr7JgguiCYtF2+HjKB4OFDdck/EbIRoO/sTkos5WHAhSjxgXUdslkCbhAroX9vBINYxEeuYg392xGStoLwk7egoWttCbqJdrwaSXYUY2xmNbZL0X6FFeHq91X4w6TKVtL+nz7pHnlCXSGDrhI+EY5AqEGDHvsF0dfgpSxJ2XzOfcrhtuKWBCedRbbkWJF6whRCFIFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtErMAABksSOTA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA3lr3XqnNJngOscsZ6cBhoXsRktGShu3uKfIVVCXK8gLahXR1cmQ7Cs2ZXwCBoLW+fMIJSt6GsLfHyFd2mfqyCbkBKPkBJTsBoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAnOV5jz94m/BS+DBiw9fD6SEXJGzpQRFFr7JgguiCYtF2+HjKB4OFDdck/EbIRoO/sTkos5WHAhSjxgXUdslkCbhAroX9vBINYxEeuYg392xGStoLwk7egoWttCbqJdrwaSXYUY2xmNbZL0X6FFeHq91X4w6TKVtL+nz7pHnlCXSGDrhI+EY5AqEGDHvsF0dfgpSxJ2XzOfcrhtuKWBCedRbbkWJF6whRCFIFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtErMAABksSOTA==",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA3lr3XqnNJngOscsZ6cBhoXsRktGShu3uKfIVVCXK8gLahXR1cmQ7Cs2ZXwCBoLW+fMIJSt6GsLfHyFd2mfqyCbkBKPkBJTsBoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAnOV5jz94m/BS+DBiw9fD6SEXJGzpQRFFr7JgguiCYtF2+HjKB4OFDdck/EbIRoO/sTkos5WHAhSjxgXUdslkCbhAroX9vBINYxEeuYg392xGStoLwk7egoWttCbqJdrwaSXYUY2xmNbZL0X6FFeHq91X4w6TKVtL+nz7pHnlCXSGDrhI+EY5AqEGDHvsF0dfgpSxJ2XzOfcrhtuKWBCedRbbkWJF6whRCFIFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtErMAABksSOTA==",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "�v����$wW�\u00040��eLC�䘣�7y�\u0001<\u001cȋ",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1013,
        "message": "Tx already on-chain"
      }
    ],
    "message": "Rejected",
    "request": {
      "id": -576460752303423365,
      "jsonrpc": "2.0",
      "method": "channels.snapshot_solo",
      "params": {}
    }
  },
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423364,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423364,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSBqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAmbBbMQ=",
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
  "id": -576460752303423363,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED9BfEvXsrwNprY/SXv3IyGi7KdyJVEy3wfujBOjVIRqQFlb5e5lRjSWLNVSbdXKsUX91t1cCcUmYx+LR+yN+4CuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1xgUZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423363,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+JALAfhCuED9BfEvXsrwNprY/SXv3IyGi7KdyJVEy3wfujBOjVIRqQFlb5e5lRjSWLNVSbdXKsUX91t1cCcUmYx+LR+yN+4CuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1xgUZ",
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
  "id": -576460752303423362,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC/SaSWsZWmTsLS2tWfZE2ufh3xIu0Fg7yx+yHfaq6+HYX9EcJCaHZQIZj7Q5YqFK8hIflM7PC6v3mOX5begvkLuED9BfEvXsrwNprY/SXv3IyGi7KdyJVEy3wfujBOjVIRqQFlb5e5lRjSWLNVSbdXKsUX91t1cCcUmYx+LR+yN+4CuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJm0n+e"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423362,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEC/SaSWsZWmTsLS2tWfZE2ufh3xIu0Fg7yx+yHfaq6+HYX9EcJCaHZQIZj7Q5YqFK8hIflM7PC6v3mOX5begvkLuED9BfEvXsrwNprY/SXv3IyGi7KdyJVEy3wfujBOjVIRqQFlb5e5lRjSWLNVSbdXKsUX91t1cCcUmYx+LR+yN+4CuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJm0n+e"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEC/SaSWsZWmTsLS2tWfZE2ufh3xIu0Fg7yx+yHfaq6+HYX9EcJCaHZQIZj7Q5YqFK8hIflM7PC6v3mOX5begvkLuED9BfEvXsrwNprY/SXv3IyGi7KdyJVEy3wfujBOjVIRqQFlb5e5lRjSWLNVSbdXKsUX91t1cCcUmYx+LR+yN+4CuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJm0n+e"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423361,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423361,
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
  "id": -576460752303423360,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423360,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC/SaSWsZWmTsLS2tWfZE2ufh3xIu0Fg7yx+yHfaq6+HYX9EcJCaHZQIZj7Q5YqFK8hIflM7PC6v3mOX5begvkLuED9BfEvXsrwNprY/SXv3IyGi7KdyJVEy3wfujBOjVIRqQFlb5e5lRjSWLNVSbdXKsUX91t1cCcUmYx+LR+yN+4CuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJm0n+e",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423359,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423359,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSB6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC8FFGkg=",
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
  "id": -576460752303423358,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED9Oka9bKM/3s+0Z7E5Lwd1wtjRzvPhqjIjce3eYBAHlk2mvK7OoZfTavvp941cVRqsD9ctgRS9hjBPnftUvkQBuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtjT4GB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423358,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+JALAfhCuED9Oka9bKM/3s+0Z7E5Lwd1wtjRzvPhqjIjce3eYBAHlk2mvK7OoZfTavvp941cVRqsD9ctgRS9hjBPnftUvkQBuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtjT4GB",
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
  "id": -576460752303423357,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAjv48UJqaXBJPhB3YlZLyE6R/VXwaJwv3GCWiU+H6AEzpqNmR77+G39L9pOm8u+dXsjxc4TD4zV3f4127Xbf4HuED9Oka9bKM/3s+0Z7E5Lwd1wtjRzvPhqjIjce3eYBAHlk2mvK7OoZfTavvp941cVRqsD9ctgRS9hjBPnftUvkQBuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtzHfps"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423357,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEAjv48UJqaXBJPhB3YlZLyE6R/VXwaJwv3GCWiU+H6AEzpqNmR77+G39L9pOm8u+dXsjxc4TD4zV3f4127Xbf4HuED9Oka9bKM/3s+0Z7E5Lwd1wtjRzvPhqjIjce3eYBAHlk2mvK7OoZfTavvp941cVRqsD9ctgRS9hjBPnftUvkQBuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtzHfps"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEAjv48UJqaXBJPhB3YlZLyE6R/VXwaJwv3GCWiU+H6AEzpqNmR77+G39L9pOm8u+dXsjxc4TD4zV3f4127Xbf4HuED9Oka9bKM/3s+0Z7E5Lwd1wtjRzvPhqjIjce3eYBAHlk2mvK7OoZfTavvp941cVRqsD9ctgRS9hjBPnftUvkQBuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtzHfps"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423356,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423356,
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
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAjv48UJqaXBJPhB3YlZLyE6R/VXwaJwv3GCWiU+H6AEzpqNmR77+G39L9pOm8u+dXsjxc4TD4zV3f4127Xbf4HuED9Oka9bKM/3s+0Z7E5Lwd1wtjRzvPhqjIjce3eYBAHlk2mvK7OoZfTavvp941cVRqsD9ctgRS9hjBPnftUvkQBuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtzHfps",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423354,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423354,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEAjv48UJqaXBJPhB3YlZLyE6R/VXwaJwv3GCWiU+H6AEzpqNmR77+G39L9pOm8u+dXsjxc4TD4zV3f4127Xbf4HuED9Oka9bKM/3s+0Z7E5Lwd1wtjRzvPhqjIjce3eYBAHlk2mvK7OoZfTavvp941cVRqsD9ctgRS9hjBPnftUvkQBuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMG0SswAAJ8UoSw",
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
    "signed_tx": "tx_+QFxCwH4QrhAqKrHV/G8JyoAoG7ygHCoNLsJ5zcQlS8UuPh4OwIdIPP4Czk9oLSlTIdBY4opoHL66wBa1QS2O2T8kgJqHOJIBrkBKPkBJTsBoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAI7+PFCamlwST4Qd2JWS8hOkf1V8GicL9xglolPh+gBM6ajZke+/ht/S/aTpvLvnV7I8XOEw+M1d3+Ndu123+B7hA/TpGvWyjP97PtGexOS8HdcLY0c7z4aoyI3Ht3mAQB5ZNpryuzqGX02r76feNXFUarA/XLYEUvYYwT537VL5EAbhI+EY5AqEGDHvsF0dfgpSxJ2XzOfcrhtuKWBCedRbbkWJF6whRCFIHoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtErMAACHa+MUw=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423353,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423353,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSCKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeApKT5RA=",
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
  "id": -576460752303423352,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECOhDpAzzsEoToi0RmIaNQ0t6NrRVhb8NSUjSGwuSxwwRL1DAbKfa9RbQBB9LbWtMGIxLuASXImzdLMIh7ziJAAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgigjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK0ByfB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423352,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+JALAfhCuECOhDpAzzsEoToi0RmIaNQ0t6NrRVhb8NSUjSGwuSxwwRL1DAbKfa9RbQBB9LbWtMGIxLuASXImzdLMIh7ziJAAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgigjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK0ByfB",
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
  "id": -576460752303423351,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAsnsa3mYRjwzr/j8I99rSmuUQIju+T9D5MIDhrG0ceR3tT/jyg4Q+P7lcxT195D4pcINzmijlNpR3e2aZevosDuECOhDpAzzsEoToi0RmIaNQ0t6NrRVhb8NSUjSGwuSxwwRL1DAbKfa9RbQBB9LbWtMGIxLuASXImzdLMIh7ziJAAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgigjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLBPdbM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423351,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEAsnsa3mYRjwzr/j8I99rSmuUQIju+T9D5MIDhrG0ceR3tT/jyg4Q+P7lcxT195D4pcINzmijlNpR3e2aZevosDuECOhDpAzzsEoToi0RmIaNQ0t6NrRVhb8NSUjSGwuSxwwRL1DAbKfa9RbQBB9LbWtMGIxLuASXImzdLMIh7ziJAAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgigjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLBPdbM"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEAsnsa3mYRjwzr/j8I99rSmuUQIju+T9D5MIDhrG0ceR3tT/jyg4Q+P7lcxT195D4pcINzmijlNpR3e2aZevosDuECOhDpAzzsEoToi0RmIaNQ0t6NrRVhb8NSUjSGwuSxwwRL1DAbKfa9RbQBB9LbWtMGIxLuASXImzdLMIh7ziJAAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgigjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLBPdbM"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423350,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423350,
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
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAsnsa3mYRjwzr/j8I99rSmuUQIju+T9D5MIDhrG0ceR3tT/jyg4Q+P7lcxT195D4pcINzmijlNpR3e2aZevosDuECOhDpAzzsEoToi0RmIaNQ0t6NrRVhb8NSUjSGwuSxwwRL1DAbKfa9RbQBB9LbWtMGIxLuASXImzdLMIh7ziJAAuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgigjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLBPdbM",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423348,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423348,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgx77BdHX4KUsSdl8zn3K4bbilgQnnUW25FiResIUQhSCaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzDmPkk=",
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
  "id": -576460752303423347,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED6xEKa3Pb0sonputGS91AiPyC0uth5ou+XWZ9KZjMPYdEvXZ8mcpdNmenZk106dYWDPdgqzBHlB0k24iczD3UDuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgmgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtmiCtX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423347,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "signed_tx": "tx_+JALAfhCuED6xEKa3Pb0sonputGS91AiPyC0uth5ou+XWZ9KZjMPYdEvXZ8mcpdNmenZk106dYWDPdgqzBHlB0k24iczD3UDuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgmgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtmiCtX",
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
  "id": -576460752303423346,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB2TGvmdMZ1mMCe5A1dBAK95+liXWWDPhZU55WRRN4+Rxdl2i6N2FXjRCQSMU/d70OH4lK75Vmfq1WLuyfRpc8FuED6xEKa3Pb0sonputGS91AiPyC0uth5ou+XWZ9KZjMPYdEvXZ8mcpdNmenZk106dYWDPdgqzBHlB0k24iczD3UDuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgmgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs/Va2e"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423346,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEB2TGvmdMZ1mMCe5A1dBAK95+liXWWDPhZU55WRRN4+Rxdl2i6N2FXjRCQSMU/d70OH4lK75Vmfq1WLuyfRpc8FuED6xEKa3Pb0sonputGS91AiPyC0uth5ou+XWZ9KZjMPYdEvXZ8mcpdNmenZk106dYWDPdgqzBHlB0k24iczD3UDuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgmgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs/Va2e"
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "state": "tx_+NILAfiEuEB2TGvmdMZ1mMCe5A1dBAK95+liXWWDPhZU55WRRN4+Rxdl2i6N2FXjRCQSMU/d70OH4lK75Vmfq1WLuyfRpc8FuED6xEKa3Pb0sonputGS91AiPyC0uth5ou+XWZ9KZjMPYdEvXZ8mcpdNmenZk106dYWDPdgqzBHlB0k24iczD3UDuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgmgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs/Va2e"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423345,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423345,
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
  "id": -576460752303423344,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423344,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB2TGvmdMZ1mMCe5A1dBAK95+liXWWDPhZU55WRRN4+Rxdl2i6N2FXjRCQSMU/d70OH4lK75Vmfq1WLuyfRpc8FuED6xEKa3Pb0sonputGS91AiPyC0uth5ou+XWZ9KZjMPYdEvXZ8mcpdNmenZk106dYWDPdgqzBHlB0k24iczD3UDuEj4RjkCoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUgmgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs/Va2e",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAqKrHV/G8JyoAoG7ygHCoNLsJ5zcQlS8UuPh4OwIdIPP4Czk9oLSlTIdBY4opoHL66wBa1QS2O2T8kgJqHOJIBrkBKPkBJTsBoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAI7+PFCamlwST4Qd2JWS8hOkf1V8GicL9xglolPh+gBM6ajZke+/ht/S/aTpvLvnV7I8XOEw+M1d3+Ndu123+B7hA/TpGvWyjP97PtGexOS8HdcLY0c7z4aoyI3Ht3mAQB5ZNpryuzqGX02r76feNXFUarA/XLYEUvYYwT537VL5EAbhI+EY5AqEGDHvsF0dfgpSxJ2XzOfcrhtuKWBCedRbbkWJF6whRCFIHoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtErMAACHa+MUw==",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAqKrHV/G8JyoAoG7ygHCoNLsJ5zcQlS8UuPh4OwIdIPP4Czk9oLSlTIdBY4opoHL66wBa1QS2O2T8kgJqHOJIBrkBKPkBJTsBoQYMe+wXR1+ClLEnZfM59yuG24pYEJ51FtuRYkXrCFEIUqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAI7+PFCamlwST4Qd2JWS8hOkf1V8GicL9xglolPh+gBM6ajZke+/ht/S/aTpvLvnV7I8XOEw+M1d3+Ndu123+B7hA/TpGvWyjP97PtGexOS8HdcLY0c7z4aoyI3Ht3mAQB5ZNpryuzqGX02r76feNXFUarA/XLYEUvYYwT537VL5EAbhI+EY5AqEGDHvsF0dfgpSxJ2XzOfcrhtuKWBCedRbbkWJF6whRCFIHoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtErMAACHa+MUw==",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "�LO�Gxϒ\u0017\u0015�F^�\u0015=�\n��:S�i��.�ǂ$",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423343,
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423343,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423342,
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
    "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
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
  "channel_id": "ch_6VtZ55GdtW7qHgisddMAkk8kWFQkZZAygrFU4q9tDS35hXqXe",
  "id": -576460752303423342,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
