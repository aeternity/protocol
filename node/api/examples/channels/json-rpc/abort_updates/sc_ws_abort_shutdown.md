
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
      "fsm_id": "ba_aDFatG8zhRpTMp48AzLmD3ejzgJ5yi4Shc1EDtFjqsl7Nr9j"
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
      "fsm_id": "ba_fKVzO+4OkLDbTQ3DH1+MSF7NbpSubv5nLc5ymIrNtYstI+4M"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBu/HKpVE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422086,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEC8JLMXJiMD241RsQco+txo83nV+3wAAfsLsvJCQWA5t8AW3str9MGOeQKP2/BjV4e64gGVyQvzD5BGEFZrB+sFuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lgbvl87Dg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422086,
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "fsm_id": "ba_fKVzO+4OkLDbTQ3DH1+MSF7NbpSubv5nLc5ymIrNtYstI+4M",
      "signed_tx": "tx_+MwLAfhCuEC8JLMXJiMD241RsQco+txo83nV+3wAAfsLsvJCQWA5t8AW3str9MGOeQKP2/BjV4e64gGVyQvzD5BGEFZrB+sFuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lgbvl87Dg",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422085,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAMDauZxRwTIWmacT9fbtG0psqKzc3xatv14UlfylDw6hdzA0CRLXmeQogkxY6lvy9mzSk7EyHcIoeQoaJmRUkBLhAvCSzFyYjA9uNUbEHKPrcaPN51ft8AAH7C7LyQkFgObfAFt7La/TBjnkCj9vwY1eHuuIBlckL8w+QRhBWawfrBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G7pK3VNQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
  "id": -576460752303422085,
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAMDauZxRwTIWmacT9fbtG0psqKzc3xatv14UlfylDw6hdzA0CRLXmeQogkxY6lvy9mzSk7EyHcIoeQoaJmRUkBLhAvCSzFyYjA9uNUbEHKPrcaPN51ft8AAH7C7LyQkFgObfAFt7La/TBjnkCj9vwY1eHuuIBlckL8w+QRhBWawfrBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G7pK3VNQ==",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_aDFatG8zhRpTMp48AzLmD3ejzgJ5yi4Shc1EDtFjqsl7Nr9j"
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAMDauZxRwTIWmacT9fbtG0psqKzc3xatv14UlfylDw6hdzA0CRLXmeQogkxY6lvy9mzSk7EyHcIoeQoaJmRUkBLhAvCSzFyYjA9uNUbEHKPrcaPN51ft8AAH7C7LyQkFgObfAFt7La/TBjnkCj9vwY1eHuuIBlckL8w+QRhBWawfrBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G7pK3VNQ==",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAMDauZxRwTIWmacT9fbtG0psqKzc3xatv14UlfylDw6hdzA0CRLXmeQogkxY6lvy9mzSk7EyHcIoeQoaJmRUkBLhAvCSzFyYjA9uNUbEHKPrcaPN51ft8AAH7C7LyQkFgObfAFt7La/TBjnkCj9vwY1eHuuIBlckL8w+QRhBWawfrBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G7pK3VNQ==",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAMDauZxRwTIWmacT9fbtG0psqKzc3xatv14UlfylDw6hdzA0CRLXmeQogkxY6lvy9mzSk7EyHcIoeQoaJmRUkBLhAvCSzFyYjA9uNUbEHKPrcaPN51ft8AAH7C7LyQkFgObfAFt7La/TBjnkCj9vwY1eHuuIBlckL8w+QRhBWawfrBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G7pK3VNQ==",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "message": {
        "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "message": {
        "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
  "id": -576460752303422084,
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
  "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
  "id": -576460752303422084,
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "state": "tx_+QEOCwH4hLhAMDauZxRwTIWmacT9fbtG0psqKzc3xatv14UlfylDw6hdzA0CRLXmeQogkxY6lvy9mzSk7EyHcIoeQoaJmRUkBLhAvCSzFyYjA9uNUbEHKPrcaPN51ft8AAH7C7LyQkFgObfAFt7La/TBjnkCj9vwY1eHuuIBlckL8w+QRhBWawfrBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G7pK3VNQ=="
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "state": "tx_+QEOCwH4hLhAMDauZxRwTIWmacT9fbtG0psqKzc3xatv14UlfylDw6hdzA0CRLXmeQogkxY6lvy9mzSk7EyHcIoeQoaJmRUkBLhAvCSzFyYjA9uNUbEHKPrcaPN51ft8AAH7C7LyQkFgObfAFt7La/TBjnkCj9vwY1eHuuIBlckL8w+QRhBWawfrBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G7pK3VNQ=="
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBvywGhxcSjKrYMatYm3wQBS39V5uGyA/tQ4VZ4bZENpCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBvAFWtnA=",
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
  "method": "channels.shutdown_sign",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBvywGhxcSjKrYMatYm3wQBS39V5uGyA/tQ4VZ4bZENpCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY3+rniy/+GHLHOiuwBAIYPXtZ/KABB5iBgLg==",
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
  "method": "channels.shutdown_sign",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBvywGhxcSjKrYMatYm3wQBS39V5uGyA/tQ4VZ4bZENpCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBvAFWtnA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422083,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEBNdh1YEDtV516zE5fJcd/hwhV3pj4rY1myMGsOlwHi/IFelPcGPz70BWGckfsp4GlxHgZBiAoIq8ya74RXUbcFuGD4XjUBoQb8sBocXEoyq2DGrWJt8EAUt/VebhsgP7UOFWeG2RDaQqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgbyJ9hJb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
  "id": -576460752303422083,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
      "method": "channels.shutdown_sign",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEBNdh1YEDtV516zE5fJcd/hwhV3pj4rY1myMGsOlwHi/IFelPcGPz70BWGckfsp4GlxHgZBiAoIq8ya74RXUbcFuGD4XjUBoQb8sBocXEoyq2DGrWJt8EAUt/VebhsgP7UOFWeG2RDaQqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgbyJ9hJb",
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
  "method": "channels.shutdown_sign_ack",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
    "data": {
      "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
      "error_code": 42,
      "error_msg": "unknown",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422082,
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
  "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
  "id": -576460752303422082,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422081,
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
    "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
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
  "channel_id": "ch_2vHaFKWQcBUbWftS9auMaZpMqWroJBnLiCexcYKACWSsbq3F8c",
  "id": -576460752303422081,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
