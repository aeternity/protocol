
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
      "fsm_id": "ba_2mqudfcHFtSJOt7rci91U6WCk7nGMVM69FRbOU3eG4nOtQUW"
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
      "fsm_id": "ba_VNUql9DRT2isH2o5SF+HhRS7GdOQEF1KrfRS7CCsMUUng4pR"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtawEz+aA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422525,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAO/gWIduuzdMGqNxBeWgaPiYQ7Wi3kNzF2enIC8SOFcnLFP46w6m+ssp9sBX8EF/kiQrprxO2ecYhfM1Rj1QUEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LWn8rPMA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422525,
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "fsm_id": "ba_VNUql9DRT2isH2o5SF+HhRS7GdOQEF1KrfRS7CCsMUUng4pR",
      "signed_tx": "tx_+MsLAfhCuEAO/gWIduuzdMGqNxBeWgaPiYQ7Wi3kNzF2enIC8SOFcnLFP46w6m+ssp9sBX8EF/kiQrprxO2ecYhfM1Rj1QUEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LWn8rPMA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422524,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhADv4FiHbrs3TBqjcQXloGj4mEO1ot5DcxdnpyAvEjhXJyxT+OsOpvrLKfbAV/BBf5IkK6a8TtnnGIXzNUY9UFBLhA1NEcrPs0LfhGUl19IV4bU7hdmaYv8UoiULdi/j1fz8uzBuG+xx8Wa8S0AW1QSYOOVDGmwhMyMYj0/ZOj4gXAD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1pGkNWZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
  "id": -576460752303422524,
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhADv4FiHbrs3TBqjcQXloGj4mEO1ot5DcxdnpyAvEjhXJyxT+OsOpvrLKfbAV/BBf5IkK6a8TtnnGIXzNUY9UFBLhA1NEcrPs0LfhGUl19IV4bU7hdmaYv8UoiULdi/j1fz8uzBuG+xx8Wa8S0AW1QSYOOVDGmwhMyMYj0/ZOj4gXAD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1pGkNWZ",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_2mqudfcHFtSJOt7rci91U6WCk7nGMVM69FRbOU3eG4nOtQUW"
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhADv4FiHbrs3TBqjcQXloGj4mEO1ot5DcxdnpyAvEjhXJyxT+OsOpvrLKfbAV/BBf5IkK6a8TtnnGIXzNUY9UFBLhA1NEcrPs0LfhGUl19IV4bU7hdmaYv8UoiULdi/j1fz8uzBuG+xx8Wa8S0AW1QSYOOVDGmwhMyMYj0/ZOj4gXAD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1pGkNWZ",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhADv4FiHbrs3TBqjcQXloGj4mEO1ot5DcxdnpyAvEjhXJyxT+OsOpvrLKfbAV/BBf5IkK6a8TtnnGIXzNUY9UFBLhA1NEcrPs0LfhGUl19IV4bU7hdmaYv8UoiULdi/j1fz8uzBuG+xx8Wa8S0AW1QSYOOVDGmwhMyMYj0/ZOj4gXAD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1pGkNWZ",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhADv4FiHbrs3TBqjcQXloGj4mEO1ot5DcxdnpyAvEjhXJyxT+OsOpvrLKfbAV/BBf5IkK6a8TtnnGIXzNUY9UFBLhA1NEcrPs0LfhGUl19IV4bU7hdmaYv8UoiULdi/j1fz8uzBuG+xx8Wa8S0AW1QSYOOVDGmwhMyMYj0/ZOj4gXAD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1pGkNWZ",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "message": {
        "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "message": {
        "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
  "id": -576460752303422523,
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
  "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
  "id": -576460752303422523,
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "state": "tx_+QENCwH4hLhADv4FiHbrs3TBqjcQXloGj4mEO1ot5DcxdnpyAvEjhXJyxT+OsOpvrLKfbAV/BBf5IkK6a8TtnnGIXzNUY9UFBLhA1NEcrPs0LfhGUl19IV4bU7hdmaYv8UoiULdi/j1fz8uzBuG+xx8Wa8S0AW1QSYOOVDGmwhMyMYj0/ZOj4gXAD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1pGkNWZ"
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "state": "tx_+QENCwH4hLhADv4FiHbrs3TBqjcQXloGj4mEO1ot5DcxdnpyAvEjhXJyxT+OsOpvrLKfbAV/BBf5IkK6a8TtnnGIXzNUY9UFBLhA1NEcrPs0LfhGUl19IV4bU7hdmaYv8UoiULdi/j1fz8uzBuG+xx8Wa8S0AW1QSYOOVDGmwhMyMYj0/ZOj4gXAD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1pGkNWZ"
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
  "params": {
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBjbNCMXDobLY61a45p4C78tX6CzvvVNk5R+1VwHxs0zEoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7uOFqAWzmnwb4=",
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
    "signed_tx": "tx_+QHrCwH4QrhAk/MlyppW4cbTVFiHD3oOwtfgweqjlcc3+mft/IdqRkimU3z9f5zlSWj9i4DHGw8kiJFPgOxlerpHaZTfz5qbCrkBovkBnzYBoQY2zQjFw6Gy2OtWuOaeAu/LV+gs771TZOUftVcB8bNMxKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7jhagFusgEvM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAk/MlyppW4cbTVFiHD3oOwtfgweqjlcc3+mft/IdqRkimU3z9f5zlSWj9i4DHGw8kiJFPgOxlerpHaZTfz5qbCrkBovkBnzYBoQY2zQjFw6Gy2OtWuOaeAu/LV+gs771TZOUftVcB8bNMxKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7jhagFusgEvM",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAk/MlyppW4cbTVFiHD3oOwtfgweqjlcc3+mft/IdqRkimU3z9f5zlSWj9i4DHGw8kiJFPgOxlerpHaZTfz5qbCrkBovkBnzYBoQY2zQjFw6Gy2OtWuOaeAu/LV+gs771TZOUftVcB8bNMxKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7jhagFusgEvM",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBjbNCMXDobLY61a45p4C78tX6CzvvVNk5R+1VwHxs0zEoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAAkOx+0pA==",
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
    "signed_tx": "tx_+KcLAfhCuECQZu5wBy8Sis8OFmAuXEiDN0PT5QEKBrgPbK+ScMk0BlPUwgpSOKJnBuhlxAEIFdYLVhWz14QxnY5CHlmizn8LuF/4XTgBoQY2zQjFw6Gy2OtWuOaeAu/LV+gs771TZOUftVcB8bNMxKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAJI81qNo="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECQZu5wBy8Sis8OFmAuXEiDN0PT5QEKBrgPbK+ScMk0BlPUwgpSOKJnBuhlxAEIFdYLVhWz14QxnY5CHlmizn8LuF/4XTgBoQY2zQjFw6Gy2OtWuOaeAu/LV+gs771TZOUftVcB8bNMxKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAJI81qNo=",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECQZu5wBy8Sis8OFmAuXEiDN0PT5QEKBrgPbK+ScMk0BlPUwgpSOKJnBuhlxAEIFdYLVhWz14QxnY5CHlmizn8LuF/4XTgBoQY2zQjFw6Gy2OtWuOaeAu/LV+gs771TZOUftVcB8bNMxKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAJI81qNo=",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
    "channel_id": "ch_R8pKSQhWkWvYPjjiaH3rLt1JeqtJ8WAAKmJxUFVCST9xRG6eC",
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
      "fsm_id": "ba_Mfwzd6So9EaYnAFjyVwkfntTt0By+16QfywmJYGxuIqWFQps"
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
      "fsm_id": "ba_l+ZleOgdvMf6cVYUfSZIw6UBQSoqumP/CnMS693YsYyH3bjG"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtcKfJgfQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422522,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB//qIX8RyIrW3tkCGkkT1h+FxaE5BSWJ6DStdVyOhrXEttKp7lbEmQMllUpW8MvZDCT9bek0u4dVFxto84QHAEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LXNViX/M="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422522,
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "fsm_id": "ba_l+ZleOgdvMf6cVYUfSZIw6UBQSoqumP/CnMS693YsYyH3bjG",
      "signed_tx": "tx_+MsLAfhCuEB//qIX8RyIrW3tkCGkkT1h+FxaE5BSWJ6DStdVyOhrXEttKp7lbEmQMllUpW8MvZDCT9bek0u4dVFxto84QHAEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LXNViX/M=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422521,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAFMDyzbMvgm/R1CQElm9vRo/gBk49TM10rfOjuaj2fE/c4m5A5ZAZCAHB7kM6hyJcTdisOT84ATGhCpuda0A5A7hAf/6iF/EciK1t7ZAhpJE9YfhcWhOQUlieg0rXVcjoa1xLbSqe5WxJkDJZVKVvDL2Qwk/W3pNLuHVRcbaPOEBwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1zKiOlN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
  "id": -576460752303422521,
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAFMDyzbMvgm/R1CQElm9vRo/gBk49TM10rfOjuaj2fE/c4m5A5ZAZCAHB7kM6hyJcTdisOT84ATGhCpuda0A5A7hAf/6iF/EciK1t7ZAhpJE9YfhcWhOQUlieg0rXVcjoa1xLbSqe5WxJkDJZVKVvDL2Qwk/W3pNLuHVRcbaPOEBwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1zKiOlN",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Mfwzd6So9EaYnAFjyVwkfntTt0By+16QfywmJYGxuIqWFQps"
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAFMDyzbMvgm/R1CQElm9vRo/gBk49TM10rfOjuaj2fE/c4m5A5ZAZCAHB7kM6hyJcTdisOT84ATGhCpuda0A5A7hAf/6iF/EciK1t7ZAhpJE9YfhcWhOQUlieg0rXVcjoa1xLbSqe5WxJkDJZVKVvDL2Qwk/W3pNLuHVRcbaPOEBwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1zKiOlN",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFMDyzbMvgm/R1CQElm9vRo/gBk49TM10rfOjuaj2fE/c4m5A5ZAZCAHB7kM6hyJcTdisOT84ATGhCpuda0A5A7hAf/6iF/EciK1t7ZAhpJE9YfhcWhOQUlieg0rXVcjoa1xLbSqe5WxJkDJZVKVvDL2Qwk/W3pNLuHVRcbaPOEBwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1zKiOlN",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFMDyzbMvgm/R1CQElm9vRo/gBk49TM10rfOjuaj2fE/c4m5A5ZAZCAHB7kM6hyJcTdisOT84ATGhCpuda0A5A7hAf/6iF/EciK1t7ZAhpJE9YfhcWhOQUlieg0rXVcjoa1xLbSqe5WxJkDJZVKVvDL2Qwk/W3pNLuHVRcbaPOEBwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1zKiOlN",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "message": {
        "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "message": {
        "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
  "id": -576460752303422520,
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
  "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
  "id": -576460752303422520,
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "state": "tx_+QENCwH4hLhAFMDyzbMvgm/R1CQElm9vRo/gBk49TM10rfOjuaj2fE/c4m5A5ZAZCAHB7kM6hyJcTdisOT84ATGhCpuda0A5A7hAf/6iF/EciK1t7ZAhpJE9YfhcWhOQUlieg0rXVcjoa1xLbSqe5WxJkDJZVKVvDL2Qwk/W3pNLuHVRcbaPOEBwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1zKiOlN"
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "state": "tx_+QENCwH4hLhAFMDyzbMvgm/R1CQElm9vRo/gBk49TM10rfOjuaj2fE/c4m5A5ZAZCAHB7kM6hyJcTdisOT84ATGhCpuda0A5A7hAf/6iF/EciK1t7ZAhpJE9YfhcWhOQUlieg0rXVcjoa1xLbSqe5WxJkDJZVKVvDL2Qwk/W3pNLuHVRcbaPOEBwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1zKiOlN"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBlDObtSJqtSc6jHS0003xJdQyzOtLGtYQ2OnSB9ddC0UoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7uOFqAJR4u1Lo=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAy+szNosshMZJEsOtHcxfhyzjBOdXkG48af7lvaZEHtQI+btPid2Rd94EfBDsXQLAbZ1nV/lYtxYqw+H0HllfCbkBovkBnzYBoQZQzm7UiarUnOox0tNNN8SXUMszrSxrWENjp0gfXXQtFKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7jhagCUpAAFJ"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAy+szNosshMZJEsOtHcxfhyzjBOdXkG48af7lvaZEHtQI+btPid2Rd94EfBDsXQLAbZ1nV/lYtxYqw+H0HllfCbkBovkBnzYBoQZQzm7UiarUnOox0tNNN8SXUMszrSxrWENjp0gfXXQtFKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7jhagCUpAAFJ",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAy+szNosshMZJEsOtHcxfhyzjBOdXkG48af7lvaZEHtQI+btPid2Rd94EfBDsXQLAbZ1nV/lYtxYqw+H0HllfCbkBovkBnzYBoQZQzm7UiarUnOox0tNNN8SXUMszrSxrWENjp0gfXXQtFKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7jhagCUpAAFJ",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBlDObtSJqtSc6jHS0003xJdQyzOtLGtYQ2OnSB9ddC0UoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAAmu6vj3A==",
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
    "signed_tx": "tx_+KcLAfhCuEDx2khlhi6xoTFlKQbUrXhc4BU3S/A5QSxpB6YKCwn6WDhVUcgdIV+rb5GPExLDSqwXRENPSa0Oxuvyy9NhSMAEuF/4XTgBoQZQzm7UiarUnOox0tNNN8SXUMszrSxrWENjp0gfXXQtFKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAJuHIIWk="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDx2khlhi6xoTFlKQbUrXhc4BU3S/A5QSxpB6YKCwn6WDhVUcgdIV+rb5GPExLDSqwXRENPSa0Oxuvyy9NhSMAEuF/4XTgBoQZQzm7UiarUnOox0tNNN8SXUMszrSxrWENjp0gfXXQtFKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAJuHIIWk=",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDx2khlhi6xoTFlKQbUrXhc4BU3S/A5QSxpB6YKCwn6WDhVUcgdIV+rb5GPExLDSqwXRENPSa0Oxuvyy9NhSMAEuF/4XTgBoQZQzm7UiarUnOox0tNNN8SXUMszrSxrWENjp0gfXXQtFKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAJuHIIWk=",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
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
    "channel_id": "ch_cb6FQQtuWHEAtiGr6BTMn5VTGY5cKeDYnaFwD4NZZbxaQ6u4f",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
