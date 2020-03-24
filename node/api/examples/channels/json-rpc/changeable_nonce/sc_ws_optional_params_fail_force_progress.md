
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
      "fsm_id": "ba_Q4b+0ogVqVRwlc/U+ufVd8D1vTnZnjH7TlqpaHjqHBKr9Moi"
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
      "fsm_id": "ba_OyNFdaRqPSAvnIlTziP7+3/SwnV+5s1iVAI8caxlfHRMvdvz"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBl5tAqXA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422311,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECaCM2aPA9Ja3OSLDGnRNueVpGRWXjpUZNsNf/dmakLL6hm0gy+73daHnIDi2cKeXhzQosRakP/6oFjWCXfrYEHuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZfXR0Ud"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422311,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "fsm_id": "ba_OyNFdaRqPSAvnIlTziP7+3/SwnV+5s1iVAI8caxlfHRMvdvz",
      "signed_tx": "tx_+MwLAfhCuECaCM2aPA9Ja3OSLDGnRNueVpGRWXjpUZNsNf/dmakLL6hm0gy+73daHnIDi2cKeXhzQosRakP/6oFjWCXfrYEHuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZfXR0Ud",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422310,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAHipekwCvAizhE+7rT2ZKCcdozWGPTz1nuIVDz96Rf5HIzdNSBZWKplQgPrFkAaImfbeL7xrG5+cZj6MS0a6dArhAmgjNmjwPSWtzkiwxp0TbnlaRkVl46VGTbDX/3ZmpCy+oZtIMvu93Wh5yA4tnCnl4c0KLEWpD/+qBY1gl362BB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GXOglXyw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422310,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAHipekwCvAizhE+7rT2ZKCcdozWGPTz1nuIVDz96Rf5HIzdNSBZWKplQgPrFkAaImfbeL7xrG5+cZj6MS0a6dArhAmgjNmjwPSWtzkiwxp0TbnlaRkVl46VGTbDX/3ZmpCy+oZtIMvu93Wh5yA4tnCnl4c0KLEWpD/+qBY1gl362BB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GXOglXyw==",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Q4b+0ogVqVRwlc/U+ufVd8D1vTnZnjH7TlqpaHjqHBKr9Moi"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAHipekwCvAizhE+7rT2ZKCcdozWGPTz1nuIVDz96Rf5HIzdNSBZWKplQgPrFkAaImfbeL7xrG5+cZj6MS0a6dArhAmgjNmjwPSWtzkiwxp0TbnlaRkVl46VGTbDX/3ZmpCy+oZtIMvu93Wh5yA4tnCnl4c0KLEWpD/+qBY1gl362BB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GXOglXyw==",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAHipekwCvAizhE+7rT2ZKCcdozWGPTz1nuIVDz96Rf5HIzdNSBZWKplQgPrFkAaImfbeL7xrG5+cZj6MS0a6dArhAmgjNmjwPSWtzkiwxp0TbnlaRkVl46VGTbDX/3ZmpCy+oZtIMvu93Wh5yA4tnCnl4c0KLEWpD/+qBY1gl362BB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GXOglXyw==",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAHipekwCvAizhE+7rT2ZKCcdozWGPTz1nuIVDz96Rf5HIzdNSBZWKplQgPrFkAaImfbeL7xrG5+cZj6MS0a6dArhAmgjNmjwPSWtzkiwxp0TbnlaRkVl46VGTbDX/3ZmpCy+oZtIMvu93Wh5yA4tnCnl4c0KLEWpD/+qBY1gl362BB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GXOglXyw==",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "message": {
        "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "message": {
        "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
  "id": -576460752303422309,
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
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422309,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+QEOCwH4hLhAHipekwCvAizhE+7rT2ZKCcdozWGPTz1nuIVDz96Rf5HIzdNSBZWKplQgPrFkAaImfbeL7xrG5+cZj6MS0a6dArhAmgjNmjwPSWtzkiwxp0TbnlaRkVl46VGTbDX/3ZmpCy+oZtIMvu93Wh5yA4tnCnl4c0KLEWpD/+qBY1gl362BB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GXOglXyw=="
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+QEOCwH4hLhAHipekwCvAizhE+7rT2ZKCcdozWGPTz1nuIVDz96Rf5HIzdNSBZWKplQgPrFkAaImfbeL7xrG5+cZj6MS0a6dArhAmgjNmjwPSWtzkiwxp0TbnlaRkVl46VGTbDX/3ZmpCy+oZtIMvu93Wh5yA4tnCnl4c0KLEWpD/+qBY1gl362BB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GXOglXyw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiAqAouRWKhPGHVEJAUE52PjsnjMUr34XqgzAUlFDPz+A7/jumb8k=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "vm_version": 6
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
  "id": -576460752303422308,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDjUfMqeuTkoytHGCqPwmLf+Jxml7/1phT1Eo7RoV2D7T1y648Xr58PHPbxy9UxUZyjRgn0PsvLniO0eobm0QoOuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/7RvgAG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422308,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDjUfMqeuTkoytHGCqPwmLf+Jxml7/1phT1Eo7RoV2D7T1y648Xr58PHPbxy9UxUZyjRgn0PsvLniO0eobm0QoOuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/7RvgAG",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "vm_version": 6
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
  "id": -576460752303422307,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEANaGdRmli4/gBwQ7ynUNpDRP5ZCMn+laSaekBuT+YydXOTFE0MIombIa/848QUlo/hUTcYhmUwjetbXmqkoxMFuEDjUfMqeuTkoytHGCqPwmLf+Jxml7/1phT1Eo7RoV2D7T1y648Xr58PHPbxy9UxUZyjRgn0PsvLniO0eobm0QoOuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/5Ru7Jp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422307,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEANaGdRmli4/gBwQ7ynUNpDRP5ZCMn+laSaekBuT+YydXOTFE0MIombIa/848QUlo/hUTcYhmUwjetbXmqkoxMFuEDjUfMqeuTkoytHGCqPwmLf+Jxml7/1phT1Eo7RoV2D7T1y648Xr58PHPbxy9UxUZyjRgn0PsvLniO0eobm0QoOuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/5Ru7Jp"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEANaGdRmli4/gBwQ7ynUNpDRP5ZCMn+laSaekBuT+YydXOTFE0MIombIa/848QUlo/hUTcYhmUwjetbXmqkoxMFuEDjUfMqeuTkoytHGCqPwmLf+Jxml7/1phT1Eo7RoV2D7T1y648Xr58PHPbxy9UxUZyjRgn0PsvLniO0eobm0QoOuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/5Ru7Jp"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiA6AlppMnxQtjAbIpqc5olcFylVD5N2YrzRsUGhqmlS2ceSMIBvw=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422306,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB7jyDc44rg89vus/yDelp35Jpv+d9PF4VJOWnFJHxI3cqamOEiZZ2ss5CeM/ClqO4/iiR9ul0PX96efoTI90cEuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHl5lU0a"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422306,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB7jyDc44rg89vus/yDelp35Jpv+d9PF4VJOWnFJHxI3cqamOEiZZ2ss5CeM/ClqO4/iiR9ul0PX96efoTI90cEuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHl5lU0a",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422305,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB7jyDc44rg89vus/yDelp35Jpv+d9PF4VJOWnFJHxI3cqamOEiZZ2ss5CeM/ClqO4/iiR9ul0PX96efoTI90cEuED6WfDVuVht0B3pV1IrSVDx9lpcfHAY5IFWV/8eObquln89SexyNWdIjurgdm0SQwfu3sP0xj+QZ0oFpSVmL+IAuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHmevCB9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422305,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEB7jyDc44rg89vus/yDelp35Jpv+d9PF4VJOWnFJHxI3cqamOEiZZ2ss5CeM/ClqO4/iiR9ul0PX96efoTI90cEuED6WfDVuVht0B3pV1IrSVDx9lpcfHAY5IFWV/8eObquln89SexyNWdIjurgdm0SQwfu3sP0xj+QZ0oFpSVmL+IAuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHmevCB9"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEB7jyDc44rg89vus/yDelp35Jpv+d9PF4VJOWnFJHxI3cqamOEiZZ2ss5CeM/ClqO4/iiR9ul0PX96efoTI90cEuED6WfDVuVht0B3pV1IrSVDx9lpcfHAY5IFWV/8eObquln89SexyNWdIjurgdm0SQwfu3sP0xj+QZ0oFpSVmL+IAuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHmevCB9"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 4,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiBKBb4pc9PDpQOTSad04plvbM7fDomSyF+U2kEzNYQ9yGYuPJXxc=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422304,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC/cSxFOtK7Fz2Wl8U6tL+Z6FSjbVnOqmmG3fiSiuz1u0PN4KujksV39iXz+S2b33/Gbbo+nBgAcHRgrUkpQwUAuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmJJYaIl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422304,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC/cSxFOtK7Fz2Wl8U6tL+Z6FSjbVnOqmmG3fiSiuz1u0PN4KujksV39iXz+S2b33/Gbbo+nBgAcHRgrUkpQwUAuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmJJYaIl",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422303,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECrxkkh9S6PaY+SAOxa6SmScyWOyv2yNjYC486t4rhNB+n1EW6FzC+EuPDCWsHQvl40RIYHkwexBqiSEbaiEgAJuEC/cSxFOtK7Fz2Wl8U6tL+Z6FSjbVnOqmmG3fiSiuz1u0PN4KujksV39iXz+S2b33/Gbbo+nBgAcHRgrUkpQwUAuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmItJbA9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422303,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuECrxkkh9S6PaY+SAOxa6SmScyWOyv2yNjYC486t4rhNB+n1EW6FzC+EuPDCWsHQvl40RIYHkwexBqiSEbaiEgAJuEC/cSxFOtK7Fz2Wl8U6tL+Z6FSjbVnOqmmG3fiSiuz1u0PN4KujksV39iXz+S2b33/Gbbo+nBgAcHRgrUkpQwUAuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmItJbA9"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuECrxkkh9S6PaY+SAOxa6SmScyWOyv2yNjYC486t4rhNB+n1EW6FzC+EuPDCWsHQvl40RIYHkwexBqiSEbaiEgAJuEC/cSxFOtK7Fz2Wl8U6tL+Z6FSjbVnOqmmG3fiSiuz1u0PN4KujksV39iXz+S2b33/Gbbo+nBgAcHRgrUkpQwUAuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmItJbA9"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiBaBYGi82dykqQsolpZCFXhY2WNDzDD8kPVKD6lp1jdngAG8UT4s=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422302,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBDxWxbhHs4fhOqH15hFpfRs4X6Ji2MAQuIjVE4T2F8jnibfMhyB1vuqkkNcFC66reXfLAcps+OE41Wgdw5Tv4IuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABWxAp7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422302,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBDxWxbhHs4fhOqH15hFpfRs4X6Ji2MAQuIjVE4T2F8jnibfMhyB1vuqkkNcFC66reXfLAcps+OE41Wgdw5Tv4IuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABWxAp7",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422301,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA9DjXgRzEmSN3wQciLdzLsO4tBfDz1f4IxBqbqvDbn6LEQfh2Ozvq1nGW2arifL2brsD+T0j73bW6+3uFK8fADuEBDxWxbhHs4fhOqH15hFpfRs4X6Ji2MAQuIjVE4T2F8jnibfMhyB1vuqkkNcFC66reXfLAcps+OE41Wgdw5Tv4IuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4AAQeKDW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422301,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEA9DjXgRzEmSN3wQciLdzLsO4tBfDz1f4IxBqbqvDbn6LEQfh2Ozvq1nGW2arifL2brsD+T0j73bW6+3uFK8fADuEBDxWxbhHs4fhOqH15hFpfRs4X6Ji2MAQuIjVE4T2F8jnibfMhyB1vuqkkNcFC66reXfLAcps+OE41Wgdw5Tv4IuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4AAQeKDW"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEA9DjXgRzEmSN3wQciLdzLsO4tBfDz1f4IxBqbqvDbn6LEQfh2Ozvq1nGW2arifL2brsD+T0j73bW6+3uFK8fADuEBDxWxbhHs4fhOqH15hFpfRs4X6Ji2MAQuIjVE4T2F8jnibfMhyB1vuqkkNcFC66reXfLAcps+OE41Wgdw5Tv4IuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4AAQeKDW"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiBqCRsup10nGpF4gNB8+vwlp3ceGKO/l7VIBv15EabTEe1mHwatE=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422300,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAkekixQ/i6FZSzj3P5BtlIfAImQWQX1z0spf4drglt9Yf2Pmd2q/hhqP9kEfJMdP+epZkeIac/coef45SwWO8HuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtZCSk/+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422300,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAkekixQ/i6FZSzj3P5BtlIfAImQWQX1z0spf4drglt9Yf2Pmd2q/hhqP9kEfJMdP+epZkeIac/coef45SwWO8HuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtZCSk/+",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422299,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAkekixQ/i6FZSzj3P5BtlIfAImQWQX1z0spf4drglt9Yf2Pmd2q/hhqP9kEfJMdP+epZkeIac/coef45SwWO8HuECNO12a/H3YPRFdL7CxXcJA6fXwEBfvE1os6fpQo8nfS4tdqeCa4Zvxw699tVFpUvB8ut4Ve7OIpXGYV/3Q9K4EuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtbhlFtM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422299,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEAkekixQ/i6FZSzj3P5BtlIfAImQWQX1z0spf4drglt9Yf2Pmd2q/hhqP9kEfJMdP+epZkeIac/coef45SwWO8HuECNO12a/H3YPRFdL7CxXcJA6fXwEBfvE1os6fpQo8nfS4tdqeCa4Zvxw699tVFpUvB8ut4Ve7OIpXGYV/3Q9K4EuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtbhlFtM"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEAkekixQ/i6FZSzj3P5BtlIfAImQWQX1z0spf4drglt9Yf2Pmd2q/hhqP9kEfJMdP+epZkeIac/coef45SwWO8HuECNO12a/H3YPRFdL7CxXcJA6fXwEBfvE1os6fpQo8nfS4tdqeCa4Zvxw699tVFpUvB8ut4Ve7OIpXGYV/3Q9K4EuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtbhlFtM"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 5,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 5,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 6,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 6,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiB6DiGExj+Vck8sLRqQDcVePkSMwsZhoYdAwpruPJkpQCeTuIhh0=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422298,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBACSsR7Sr3ejW2VNWO0ifhwPzDZ+wcruzNlshQQYhF9VECzA9/8zaT0Dw9L0b+knnTrmDHFbZm3gPG7Abnpk8HuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404geg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnkP1+2r"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422298,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBACSsR7Sr3ejW2VNWO0ifhwPzDZ+wcruzNlshQQYhF9VECzA9/8zaT0Dw9L0b+knnTrmDHFbZm3gPG7Abnpk8HuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404geg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnkP1+2r",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422297,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBACSsR7Sr3ejW2VNWO0ifhwPzDZ+wcruzNlshQQYhF9VECzA9/8zaT0Dw9L0b+knnTrmDHFbZm3gPG7Abnpk8HuEBZniozJvVPDkwDLxLIC6VgFMBuZW5rV9y2g2jGj9Y536AIb4WirrcqN89QQGDWUdmOOp2vvmW6Yvn2FDZIn8AMuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404geg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnl7Bl7w"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422297,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEBACSsR7Sr3ejW2VNWO0ifhwPzDZ+wcruzNlshQQYhF9VECzA9/8zaT0Dw9L0b+knnTrmDHFbZm3gPG7Abnpk8HuEBZniozJvVPDkwDLxLIC6VgFMBuZW5rV9y2g2jGj9Y536AIb4WirrcqN89QQGDWUdmOOp2vvmW6Yvn2FDZIn8AMuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404geg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnl7Bl7w"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEBACSsR7Sr3ejW2VNWO0ifhwPzDZ+wcruzNlshQQYhF9VECzA9/8zaT0Dw9L0b+knnTrmDHFbZm3gPG7Abnpk8HuEBZniozJvVPDkwDLxLIC6VgFMBuZW5rV9y2g2jGj9Y536AIb4WirrcqN89QQGDWUdmOOp2vvmW6Yvn2FDZIn8AMuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404geg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnl7Bl7w"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 8,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 7,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 7,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiCKDNERM0ttXr3D3t0V8ND0XwmXDpPdFClBK7Gzed22LweJRGs9I=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422296,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECOMyPEHkMU5qbhUnalhgetAOasTWzk6s4O4rpiZyF14+B+S63ir2t8eO71iE2lkWZNkw1hilCxItIs+oznGuYHuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HjGcEmO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422296,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+JALAfhCuECOMyPEHkMU5qbhUnalhgetAOasTWzk6s4O4rpiZyF14+B+S63ir2t8eO71iE2lkWZNkw1hilCxItIs+oznGuYHuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HjGcEmO",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422295,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECOMyPEHkMU5qbhUnalhgetAOasTWzk6s4O4rpiZyF14+B+S63ir2t8eO71iE2lkWZNkw1hilCxItIs+oznGuYHuEDZMlVl/rP3fzzWFtb1uQhRfZyUl+yCtdqlDUL4+L5s9sKStZrAD7D0AdH8mBqgDNbTvPzyHbhvV2llWNCfm6gPuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgkAJWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422295,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuECOMyPEHkMU5qbhUnalhgetAOasTWzk6s4O4rpiZyF14+B+S63ir2t8eO71iE2lkWZNkw1hilCxItIs+oznGuYHuEDZMlVl/rP3fzzWFtb1uQhRfZyUl+yCtdqlDUL4+L5s9sKStZrAD7D0AdH8mBqgDNbTvPzyHbhvV2llWNCfm6gPuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgkAJWA"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuECOMyPEHkMU5qbhUnalhgetAOasTWzk6s4O4rpiZyF14+B+S63ir2t8eO71iE2lkWZNkw1hilCxItIs+oznGuYHuEDZMlVl/rP3fzzWFtb1uQhRfZyUl+yCtdqlDUL4+L5s9sKStZrAD7D0AdH8mBqgDNbTvPzyHbhvV2llWNCfm6gPuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgkAJWA"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiCaCWHjfN80qMk25WVfiaUOCE/EcFocpmZScduuyWKweWQde88yE=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422294,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBrBF72CGTVI36ugMXz/Sm6eC1mSUrJ3iW2MVKtTTjw2+GXf9TuiLMXbltm5+8LlCTZ1MzexEq3zNnqyvqQFJYDuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkHYXqWs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422294,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBrBF72CGTVI36ugMXz/Sm6eC1mSUrJ3iW2MVKtTTjw2+GXf9TuiLMXbltm5+8LlCTZ1MzexEq3zNnqyvqQFJYDuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkHYXqWs",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422293,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBrBF72CGTVI36ugMXz/Sm6eC1mSUrJ3iW2MVKtTTjw2+GXf9TuiLMXbltm5+8LlCTZ1MzexEq3zNnqyvqQFJYDuEDKZFJfUaD5pSSshOKes73roPVd/54fOJZnKEKgcZCNYq+tXZNFoU7YyIW7dKmH7nRPruSkmN2DawHXZ/9IlpgGuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkE651ay"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422293,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEBrBF72CGTVI36ugMXz/Sm6eC1mSUrJ3iW2MVKtTTjw2+GXf9TuiLMXbltm5+8LlCTZ1MzexEq3zNnqyvqQFJYDuEDKZFJfUaD5pSSshOKes73roPVd/54fOJZnKEKgcZCNYq+tXZNFoU7YyIW7dKmH7nRPruSkmN2DawHXZ/9IlpgGuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkE651ay"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuEBrBF72CGTVI36ugMXz/Sm6eC1mSUrJ3iW2MVKtTTjw2+GXf9TuiLMXbltm5+8LlCTZ1MzexEq3zNnqyvqQFJYDuEDKZFJfUaD5pSSshOKes73roPVd/54fOJZnKEKgcZCNYq+tXZNFoU7YyIW7dKmH7nRPruSkmN2DawHXZ/9IlpgGuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkE651ay"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiCqDtOc3Amcplq0xSbaR585IcTo5Yw0MEz4WRUsC9u8JRP+7M3j0=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422292,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECgvG2MsqdX1Bkvj5jX7H1M/U3iSD1izDic9s005s+Wiu34EuBXNJ65/xuLgbqEDyPxsgp/ILKk8JbJ8yI845MJuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT/kty7f"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422292,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+JALAfhCuECgvG2MsqdX1Bkvj5jX7H1M/U3iSD1izDic9s005s+Wiu34EuBXNJ65/xuLgbqEDyPxsgp/ILKk8JbJ8yI845MJuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT/kty7f",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422291,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECgvG2MsqdX1Bkvj5jX7H1M/U3iSD1izDic9s005s+Wiu34EuBXNJ65/xuLgbqEDyPxsgp/ILKk8JbJ8yI845MJuEDUbQkfDof5S/3Lo+czv3Ut0ASoZP6BSohf4pevWDuFepDcbU0ury7HP0AO/K85j+Yyk9him+JraFQCUuxy/ToNuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9WSBDt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422291,
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuECgvG2MsqdX1Bkvj5jX7H1M/U3iSD1izDic9s005s+Wiu34EuBXNJ65/xuLgbqEDyPxsgp/ILKk8JbJ8yI845MJuEDUbQkfDof5S/3Lo+czv3Ut0ASoZP6BSohf4pevWDuFepDcbU0ury7HP0AO/K85j+Yyk9him+JraFQCUuxy/ToNuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9WSBDt"
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "state": "tx_+NILAfiEuECgvG2MsqdX1Bkvj5jX7H1M/U3iSD1izDic9s005s+Wiu34EuBXNJ65/xuLgbqEDyPxsgp/ILKk8JbJ8yI845MJuEDUbQkfDof5S/3Lo+czv3Ut0ASoZP6BSohf4pevWDuFepDcbU0ury7HP0AO/K85j+Yyk9him+JraFQCUuxy/ToNuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9WSBDt"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 9,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 9,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 10,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 10,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ],
    "contracts": [
      "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg3RjYwp6lL7XajvEvm7iNq5KLyfXpybbmKQXb+iOzt6/5AYP4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4lKDdGNjCnqUvtdqO8S+buI2rkovJ9enJtuYpBdv6I7O3r/hxgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatig/OJdc7quICtQ5NDRs4AnNC4CAml1Rk+yukDNxgsfRl2AgICAoOE3SJ7NFgWikf5Diz5ODDyxSzAvj+fsIYI10YhYpvfagICAgID4T6DhN0iezRYFopH+Q4s+Tgw8sUswL4/n7CGCNdGIWKb32u2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/X4SaD84l1zuq4gK1Dk0NGzgCc0LgICaXVGT7K6QM3GCx9GXeegMoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAArj4qCRnDmiIQXoObi9BsqN64Iwy/saIfO5/lEZSSZpgSp538DA+Qap+QamoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+EOhAGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkoGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QO2oGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMLcUPQ=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ],
    "contracts": [
      "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg3RjYwp6lL7XajvEvm7iNq5KLyfXpybbmKQXb+iOzt6/5AYP4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4lKDdGNjCnqUvtdqO8S+buI2rkovJ9enJtuYpBdv6I7O3r/hxgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatig/OJdc7quICtQ5NDRs4AnNC4CAml1Rk+yukDNxgsfRl2AgICAoOE3SJ7NFgWikf5Diz5ODDyxSzAvj+fsIYI10YhYpvfagICAgID4T6DhN0iezRYFopH+Q4s+Tgw8sUswL4/n7CGCNdGIWKb32u2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/X4SaD84l1zuq4gK1Dk0NGzgCc0LgICaXVGT7K6QM3GCx9GXeegMoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAArj4qCRnDmiIQXoObi9BsqN64Iwy/saIfO5/lEZSSZpgSp538DA+Qap+QamoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+EOhAGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkoGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QO2oGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMLcUPQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303422290,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
  "id": -576460752303422290,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QL7ggJuAbkC9PkC8T8B+QLsuLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5P9BLORlFnNWP46Iw23Suc9M0u1MToYNRjGwe0xrNZbVuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AgIoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAc6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwLi5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMC4ufi3QAG4QGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkHklzMgEiJuGa1TSZkIu3K+YdJ9z2A0ZmrndttUxpu9m4cfhvKQKhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwBwehBWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5Ae4yCOvwLRy2pdytmVuW6e0b4NzEVlVrJMD+RlTwM5LuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AkJoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwHq9rHM=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECgvG2MsqdX1Bkvj5jX7H1M/U3iSD1izDic9s005s+Wiu34EuBXNJ65/xuLgbqEDyPxsgp/ILKk8JbJ8yI845MJuEDUbQkfDof5S/3Lo+czv3Ut0ASoZP6BSohf4pevWDuFepDcbU0ury7HP0AO/K85j+Yyk9him+JraFQCUuxy/ToNuEj4RjkCoQa6+TISBUR2bhGmGaRPT8UuZYEz2nZjfzDexF9y8u404gqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9WSBDt",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABrDrddQ=="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "gas_price": 1000005656,
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "signed_tx": "tx_+Qi+CwHAuQi4+Qi1ggIJAaEGuvkyEgVEdm4RphmkT0/FLmWBM9p2Y38w3sRfcvLuNOKhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WuNT40gsB+IS4QKC8bYyyp1fUGS+PmNfsfUz9TeJIPWLMOJz2zTTmz5aK7fgS4Fc0nrn/G4uBuoQPI/GyCn8gsqTwlsnzIjzjkwm4QNRtCR8Oh/lL/cuj5zO/dS3QBKhk/oFKiF/il69YO4V6kNxtTS6vLsc/QA78rzmP5jKT2GKb4mtoVAJS7HL9Og24SPhGOQKhBrr5MhIFRHZuEaYZpE9PxS5lgTPadmN/MN7EX3Ly7jTiCqDtOc3Amcplq0xSbaR585IcTo5Yw0MEz4WRUsC9u8JRPwu4uPi2ggI+AaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9ahBWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkAQqDD0JAhDua4Bi4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgzooJzY7ukmDnZ/ggj61KRPtYPgSs3oL0EPfIJRI5Sn+5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaJigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5BABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQALkDiPkDhUABoGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5DqJ1/GRi5uSlXBXF7zuPMeGEyeQXkwdotSRIiuTGrJAuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AoKoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2w70ABoLHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Wi8oKAQCGP6olIl/1qulAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5IXECgEACrDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAEAhwHB4AA/JICDEtaH5HI9QQ==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1000005656,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_tx",
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
    "channel_id": "ch_2RLz8o6vDQBJ6WoMuB83ygqP79EuApBuxUjErY1izVFRvMzMvE",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

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
      "fsm_id": "ba_E7rX4h9uoq+kBoxbyUGsWMrP3o0hs8kAW/9yLqq6lLfU131R"
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
      "fsm_id": "ba_OSdC2FEXQBlFOL78PABoEUP2ggWyc4fwrmPpWuCf0O1BxGFa"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBmH7Y+Ic=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422289,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBgw86G/xvV77f2vvh7RKcBTsZj/ZJCcfFAfaAVyk4o/+E0S12l97OyhERe6BSxXzW96OhG2mN+gu2Wdb7FK9cIuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZjj3nJ+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422289,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "fsm_id": "ba_OSdC2FEXQBlFOL78PABoEUP2ggWyc4fwrmPpWuCf0O1BxGFa",
      "signed_tx": "tx_+MwLAfhCuEBgw86G/xvV77f2vvh7RKcBTsZj/ZJCcfFAfaAVyk4o/+E0S12l97OyhERe6BSxXzW96OhG2mN+gu2Wdb7FK9cIuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZjj3nJ+",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422288,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhANXl70Iqo9c7KDLSjAj5pFc6inJ/ch2NeULFJBCs9HtcBcxpn5upUeh/CTayHfFfo5Tp4AuU0Hyq8PxIG0Q83BrhAYMPOhv8b1e+39r74e0SnAU7GY/2SQnHxQH2gFcpOKP/hNEtdpfezsoREXugUsV81vejoRtpjfoLtlnW+xSvXCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GY+syTdA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422288,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhANXl70Iqo9c7KDLSjAj5pFc6inJ/ch2NeULFJBCs9HtcBcxpn5upUeh/CTayHfFfo5Tp4AuU0Hyq8PxIG0Q83BrhAYMPOhv8b1e+39r74e0SnAU7GY/2SQnHxQH2gFcpOKP/hNEtdpfezsoREXugUsV81vejoRtpjfoLtlnW+xSvXCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GY+syTdA==",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_E7rX4h9uoq+kBoxbyUGsWMrP3o0hs8kAW/9yLqq6lLfU131R"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhANXl70Iqo9c7KDLSjAj5pFc6inJ/ch2NeULFJBCs9HtcBcxpn5upUeh/CTayHfFfo5Tp4AuU0Hyq8PxIG0Q83BrhAYMPOhv8b1e+39r74e0SnAU7GY/2SQnHxQH2gFcpOKP/hNEtdpfezsoREXugUsV81vejoRtpjfoLtlnW+xSvXCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GY+syTdA==",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhANXl70Iqo9c7KDLSjAj5pFc6inJ/ch2NeULFJBCs9HtcBcxpn5upUeh/CTayHfFfo5Tp4AuU0Hyq8PxIG0Q83BrhAYMPOhv8b1e+39r74e0SnAU7GY/2SQnHxQH2gFcpOKP/hNEtdpfezsoREXugUsV81vejoRtpjfoLtlnW+xSvXCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GY+syTdA==",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhANXl70Iqo9c7KDLSjAj5pFc6inJ/ch2NeULFJBCs9HtcBcxpn5upUeh/CTayHfFfo5Tp4AuU0Hyq8PxIG0Q83BrhAYMPOhv8b1e+39r74e0SnAU7GY/2SQnHxQH2gFcpOKP/hNEtdpfezsoREXugUsV81vejoRtpjfoLtlnW+xSvXCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GY+syTdA==",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "message": {
        "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "message": {
        "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
  "id": -576460752303422287,
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
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422287,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+QEOCwH4hLhANXl70Iqo9c7KDLSjAj5pFc6inJ/ch2NeULFJBCs9HtcBcxpn5upUeh/CTayHfFfo5Tp4AuU0Hyq8PxIG0Q83BrhAYMPOhv8b1e+39r74e0SnAU7GY/2SQnHxQH2gFcpOKP/hNEtdpfezsoREXugUsV81vejoRtpjfoLtlnW+xSvXCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GY+syTdA=="
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+QEOCwH4hLhANXl70Iqo9c7KDLSjAj5pFc6inJ/ch2NeULFJBCs9HtcBcxpn5upUeh/CTayHfFfo5Tp4AuU0Hyq8PxIG0Q83BrhAYMPOhv8b1e+39r74e0SnAU7GY/2SQnHxQH2gFcpOKP/hNEtdpfezsoREXugUsV81vejoRtpjfoLtlnW+xSvXCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GY+syTdA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTAqAouRWKhPGHVEJAUE52PjsnjMUr34XqgzAUlFDPz+A7/muO2/A=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "vm_version": 6
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
  "id": -576460752303422286,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECIqzDUqa1nd6WD40UrhxiR98iG6k9cJ5stVk6ukeata0ZmxQ7NbkgE79jJ2XZ9nRc4B8Lm5l6KKsI8ysF0Z0kFuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/6GSUzN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422286,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+JALAfhCuECIqzDUqa1nd6WD40UrhxiR98iG6k9cJ5stVk6ukeata0ZmxQ7NbkgE79jJ2XZ9nRc4B8Lm5l6KKsI8ysF0Z0kFuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/6GSUzN",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "vm_version": 6
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
  "id": -576460752303422285,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECIqzDUqa1nd6WD40UrhxiR98iG6k9cJ5stVk6ukeata0ZmxQ7NbkgE79jJ2XZ9nRc4B8Lm5l6KKsI8ysF0Z0kFuEDVaoykI9dFCa8Ic2MGwbfZ+L2fHCERw+y6DYoOP4QpAquFoJ3DN5xL4tpJ2lmoqXRXa3FTVqMIIIvhcayK9F0JuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/5bKSGn"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422285,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuECIqzDUqa1nd6WD40UrhxiR98iG6k9cJ5stVk6ukeata0ZmxQ7NbkgE79jJ2XZ9nRc4B8Lm5l6KKsI8ysF0Z0kFuEDVaoykI9dFCa8Ic2MGwbfZ+L2fHCERw+y6DYoOP4QpAquFoJ3DN5xL4tpJ2lmoqXRXa3FTVqMIIIvhcayK9F0JuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/5bKSGn"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuECIqzDUqa1nd6WD40UrhxiR98iG6k9cJ5stVk6ukeata0ZmxQ7NbkgE79jJ2XZ9nRc4B8Lm5l6KKsI8ysF0Z0kFuEDVaoykI9dFCa8Ic2MGwbfZ+L2fHCERw+y6DYoOP4QpAquFoJ3DN5xL4tpJ2lmoqXRXa3FTVqMIIIvhcayK9F0JuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/5bKSGn"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTA6AlppMnxQtjAbIpqc5olcFylVD5N2YrzRsUGhqmlS2ceWa7eFU=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422284,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC5HeUmqz1EUJI6hLCd/pr9cyWTYBpseK+puabDt7fx0dHfsK7dUPFwH2uv/jnNAQEQyUThAOJS24DJHpOcxmgJuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHnF2KPv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422284,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC5HeUmqz1EUJI6hLCd/pr9cyWTYBpseK+puabDt7fx0dHfsK7dUPFwH2uv/jnNAQEQyUThAOJS24DJHpOcxmgJuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHnF2KPv",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422283,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC5HeUmqz1EUJI6hLCd/pr9cyWTYBpseK+puabDt7fx0dHfsK7dUPFwH2uv/jnNAQEQyUThAOJS24DJHpOcxmgJuEDFiNX3rBfofNrp4HNaUvOxtTJpAXjGWuA9i8QsRcUxxmrxM94gPhGmGg0yA5RsTN0iSNperl+KdmOIAsE1FzQHuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHnreM8E"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422283,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEC5HeUmqz1EUJI6hLCd/pr9cyWTYBpseK+puabDt7fx0dHfsK7dUPFwH2uv/jnNAQEQyUThAOJS24DJHpOcxmgJuEDFiNX3rBfofNrp4HNaUvOxtTJpAXjGWuA9i8QsRcUxxmrxM94gPhGmGg0yA5RsTN0iSNperl+KdmOIAsE1FzQHuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHnreM8E"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEC5HeUmqz1EUJI6hLCd/pr9cyWTYBpseK+puabDt7fx0dHfsK7dUPFwH2uv/jnNAQEQyUThAOJS24DJHpOcxmgJuEDFiNX3rBfofNrp4HNaUvOxtTJpAXjGWuA9i8QsRcUxxmrxM94gPhGmGg0yA5RsTN0iSNperl+KdmOIAsE1FzQHuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHnreM8E"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 4,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTBKBb4pc9PDpQOTSad04plvbM7fDomSyF+U2kEzNYQ9yGYsyZlxM=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422282,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAOFnZUYi6ONqohfwY3hETOwqKgMffDeFMwpqHmczxZIHLSz2hVNS1OwqZMw5D81owCIHzwpMZ6vBMXPukIwIgIuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmLVXQoE"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422282,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAOFnZUYi6ONqohfwY3hETOwqKgMffDeFMwpqHmczxZIHLSz2hVNS1OwqZMw5D81owCIHzwpMZ6vBMXPukIwIgIuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmLVXQoE",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422281,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAOFnZUYi6ONqohfwY3hETOwqKgMffDeFMwpqHmczxZIHLSz2hVNS1OwqZMw5D81owCIHzwpMZ6vBMXPukIwIgIuED94xxPVN4vnqR3CXIdBYbHz6llqMIoJQTymJ9gxPa2Cq94zi5+AIpE9NH3piMoFU0bGEhurpyYKmcFNPkAq78IuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmIlsJPR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422281,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEAOFnZUYi6ONqohfwY3hETOwqKgMffDeFMwpqHmczxZIHLSz2hVNS1OwqZMw5D81owCIHzwpMZ6vBMXPukIwIgIuED94xxPVN4vnqR3CXIdBYbHz6llqMIoJQTymJ9gxPa2Cq94zi5+AIpE9NH3piMoFU0bGEhurpyYKmcFNPkAq78IuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmIlsJPR"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEAOFnZUYi6ONqohfwY3hETOwqKgMffDeFMwpqHmczxZIHLSz2hVNS1OwqZMw5D81owCIHzwpMZ6vBMXPukIwIgIuED94xxPVN4vnqR3CXIdBYbHz6llqMIoJQTymJ9gxPa2Cq94zi5+AIpE9NH3piMoFU0bGEhurpyYKmcFNPkAq78IuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmIlsJPR"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTBaBYGi82dykqQsolpZCFXhY2WNDzDD8kPVKD6lp1jdngALl9Pq8=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422280,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC5iNX59SiFN9CEmsoPmDI43SgFRM8KwDuFfapeT/zXGoUcSB7yESQ4I5BdC0+hJEqlC/ipYoHuhpStqZClbugJuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABXkx5s"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422280,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC5iNX59SiFN9CEmsoPmDI43SgFRM8KwDuFfapeT/zXGoUcSB7yESQ4I5BdC0+hJEqlC/ipYoHuhpStqZClbugJuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABXkx5s",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422279,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC5iNX59SiFN9CEmsoPmDI43SgFRM8KwDuFfapeT/zXGoUcSB7yESQ4I5BdC0+hJEqlC/ipYoHuhpStqZClbugJuEDfPWMLi2E2I5dF9TkjuBt5s5HkGvmtzKToDixwghoTnJREnClLj5eHreNcmUS/7+IVB8iQC5SiWTGQaCYIYksNuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABK726g"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422279,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEC5iNX59SiFN9CEmsoPmDI43SgFRM8KwDuFfapeT/zXGoUcSB7yESQ4I5BdC0+hJEqlC/ipYoHuhpStqZClbugJuEDfPWMLi2E2I5dF9TkjuBt5s5HkGvmtzKToDixwghoTnJREnClLj5eHreNcmUS/7+IVB8iQC5SiWTGQaCYIYksNuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABK726g"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEC5iNX59SiFN9CEmsoPmDI43SgFRM8KwDuFfapeT/zXGoUcSB7yESQ4I5BdC0+hJEqlC/ipYoHuhpStqZClbugJuEDfPWMLi2E2I5dF9TkjuBt5s5HkGvmtzKToDixwghoTnJREnClLj5eHreNcmUS/7+IVB8iQC5SiWTGQaCYIYksNuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABK726g"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTBqCRsup10nGpF4gNB8+vwlp3ceGKO/l7VIBv15EabTEe1m+33zM=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422278,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECckcMtTnKwBSMyHbwOgvfJEYmQISLhE2sZiunhgMDQpkmJUF/dyiKH4oHrq/ph0b4L3rZGd36Eyst026uoN0UIuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtarDB/1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422278,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+JALAfhCuECckcMtTnKwBSMyHbwOgvfJEYmQISLhE2sZiunhgMDQpkmJUF/dyiKH4oHrq/ph0b4L3rZGd36Eyst026uoN0UIuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtarDB/1",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422277,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECckcMtTnKwBSMyHbwOgvfJEYmQISLhE2sZiunhgMDQpkmJUF/dyiKH4oHrq/ph0b4L3rZGd36Eyst026uoN0UIuEClahDfGR7f9Ggw+RA9NxLVn1oM5plz53EqW5CRJDjuVElqDOOpgxZVsEY+XCx7N9KRO3Cv/cTTcI+nwTYHcAUAuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtb/E2UT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422277,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuECckcMtTnKwBSMyHbwOgvfJEYmQISLhE2sZiunhgMDQpkmJUF/dyiKH4oHrq/ph0b4L3rZGd36Eyst026uoN0UIuEClahDfGR7f9Ggw+RA9NxLVn1oM5plz53EqW5CRJDjuVElqDOOpgxZVsEY+XCx7N9KRO3Cv/cTTcI+nwTYHcAUAuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtb/E2UT"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuECckcMtTnKwBSMyHbwOgvfJEYmQISLhE2sZiunhgMDQpkmJUF/dyiKH4oHrq/ph0b4L3rZGd36Eyst026uoN0UIuEClahDfGR7f9Ggw+RA9NxLVn1oM5plz53EqW5CRJDjuVElqDOOpgxZVsEY+XCx7N9KRO3Cv/cTTcI+nwTYHcAUAuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtb/E2UT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 5,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 5,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 6,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 6,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTB6DiGExj+Vck8sLRqQDcVePkSMwsZhoYdAwpruPJkpQCeSWjqJM=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422276,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBoLjPjIrppzEDWnQ52L90iqY8hvfO2SNH1dcQpuGiqYaKttn8S7YmX8nMF2uzOqxeIN86keYpCFQXqCTnOAu4KuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkweg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnlbzwMi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422276,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBoLjPjIrppzEDWnQ52L90iqY8hvfO2SNH1dcQpuGiqYaKttn8S7YmX8nMF2uzOqxeIN86keYpCFQXqCTnOAu4KuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkweg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnlbzwMi",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422275,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA6xZscWSrhPV2M300c/F44uEFITbv1RrYLm9nMijiErsdRvseIATxuedz88MtF4hcT8kt/uyJkr33oOmwCc/UCuEBoLjPjIrppzEDWnQ52L90iqY8hvfO2SNH1dcQpuGiqYaKttn8S7YmX8nMF2uzOqxeIN86keYpCFQXqCTnOAu4KuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkweg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnnrbA8I"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422275,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEA6xZscWSrhPV2M300c/F44uEFITbv1RrYLm9nMijiErsdRvseIATxuedz88MtF4hcT8kt/uyJkr33oOmwCc/UCuEBoLjPjIrppzEDWnQ52L90iqY8hvfO2SNH1dcQpuGiqYaKttn8S7YmX8nMF2uzOqxeIN86keYpCFQXqCTnOAu4KuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkweg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnnrbA8I"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEA6xZscWSrhPV2M300c/F44uEFITbv1RrYLm9nMijiErsdRvseIATxuedz88MtF4hcT8kt/uyJkr33oOmwCc/UCuEBoLjPjIrppzEDWnQ52L90iqY8hvfO2SNH1dcQpuGiqYaKttn8S7YmX8nMF2uzOqxeIN86keYpCFQXqCTnOAu4KuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkweg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnnrbA8I"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 8,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 7,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 7,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTCKDNERM0ttXr3D3t0V8ND0XwmXDpPdFClBK7Gzed22LweG8GFD8=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422274,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECa1dHQPi8sRU8vMosWw8gMinWVXD9jNZKg/YpXydJXJ62YffSOTR3uvOsCZRSPUgf0khizyuPDGB63NkwtZ10AuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgpjzWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422274,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+JALAfhCuECa1dHQPi8sRU8vMosWw8gMinWVXD9jNZKg/YpXydJXJ62YffSOTR3uvOsCZRSPUgf0khizyuPDGB63NkwtZ10AuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgpjzWA",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422273,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBSWTyaLDWck1E8/fS3hsMbpkaj4n9MAIUfR6p1eDAn58XlhR4iNswhUAfdxKJUuPAhSy1Bn3sk/ltqO5vDN6sFuECa1dHQPi8sRU8vMosWw8gMinWVXD9jNZKg/YpXydJXJ62YffSOTR3uvOsCZRSPUgf0khizyuPDGB63NkwtZ10AuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HhRe5Oq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422273,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEBSWTyaLDWck1E8/fS3hsMbpkaj4n9MAIUfR6p1eDAn58XlhR4iNswhUAfdxKJUuPAhSy1Bn3sk/ltqO5vDN6sFuECa1dHQPi8sRU8vMosWw8gMinWVXD9jNZKg/YpXydJXJ62YffSOTR3uvOsCZRSPUgf0khizyuPDGB63NkwtZ10AuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HhRe5Oq"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEBSWTyaLDWck1E8/fS3hsMbpkaj4n9MAIUfR6p1eDAn58XlhR4iNswhUAfdxKJUuPAhSy1Bn3sk/ltqO5vDN6sFuECa1dHQPi8sRU8vMosWw8gMinWVXD9jNZKg/YpXydJXJ62YffSOTR3uvOsCZRSPUgf0khizyuPDGB63NkwtZ10AuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HhRe5Oq"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTCaCWHjfN80qMk25WVfiaUOCE/EcFocpmZScduuyWKweWQYsmiBE=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422272,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED92aW/1G151EndgAtBmPYPNAfC4JyixQGjJ4Q/mv+4rByZp4OGHcToGyqtrqEyRJEKltHgPsn6ZpA6ZwWNGIINuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkGxEj4b"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422272,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+JALAfhCuED92aW/1G151EndgAtBmPYPNAfC4JyixQGjJ4Q/mv+4rByZp4OGHcToGyqtrqEyRJEKltHgPsn6ZpA6ZwWNGIINuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkGxEj4b",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422271,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDDjdqOQEHlMacuQmdujqRf+gCt9jyjXV5gkBdNbrF1QZfHeWqtfJzLoDyMnXATrGGtO0OfxVHQyv9tzpUS0jAAuED92aW/1G151EndgAtBmPYPNAfC4JyixQGjJ4Q/mv+4rByZp4OGHcToGyqtrqEyRJEKltHgPsn6ZpA6ZwWNGIINuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkFh/Tl9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422271,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEDDjdqOQEHlMacuQmdujqRf+gCt9jyjXV5gkBdNbrF1QZfHeWqtfJzLoDyMnXATrGGtO0OfxVHQyv9tzpUS0jAAuED92aW/1G151EndgAtBmPYPNAfC4JyixQGjJ4Q/mv+4rByZp4OGHcToGyqtrqEyRJEKltHgPsn6ZpA6ZwWNGIINuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkFh/Tl9"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEDDjdqOQEHlMacuQmdujqRf+gCt9jyjXV5gkBdNbrF1QZfHeWqtfJzLoDyMnXATrGGtO0OfxVHQyv9tzpUS0jAAuED92aW/1G151EndgAtBmPYPNAfC4JyixQGjJ4Q/mv+4rByZp4OGHcToGyqtrqEyRJEKltHgPsn6ZpA6ZwWNGIINuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkFh/Tl9"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTCqDtOc3Amcplq0xSbaR585IcTo5Yw0MEz4WRUsC9u8JRP2g9Mdk=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422270,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBZhDporS1K6MjovyRt53btKGuahrwMB59sXQOYAYKvcXZUxU43h/hY4D0PsuSCruHyFssc9ukQrr0SoZZhTWsKuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8Sen5C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422270,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBZhDporS1K6MjovyRt53btKGuahrwMB59sXQOYAYKvcXZUxU43h/hY4D0PsuSCruHyFssc9ukQrr0SoZZhTWsKuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8Sen5C",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422269,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBZhDporS1K6MjovyRt53btKGuahrwMB59sXQOYAYKvcXZUxU43h/hY4D0PsuSCruHyFssc9ukQrr0SoZZhTWsKuECpkgTfYVM2JNy4wmNKAu1pGZVZ7T4QLzhvM/B2Vb5G9RYivpeab6+44Hu7Ne3LL90/5noYSkMcAHx054IGVtwCuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9X8O/3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422269,
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEBZhDporS1K6MjovyRt53btKGuahrwMB59sXQOYAYKvcXZUxU43h/hY4D0PsuSCruHyFssc9ukQrr0SoZZhTWsKuECpkgTfYVM2JNy4wmNKAu1pGZVZ7T4QLzhvM/B2Vb5G9RYivpeab6+44Hu7Ne3LL90/5noYSkMcAHx054IGVtwCuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9X8O/3"
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "state": "tx_+NILAfiEuEBZhDporS1K6MjovyRt53btKGuahrwMB59sXQOYAYKvcXZUxU43h/hY4D0PsuSCruHyFssc9ukQrr0SoZZhTWsKuECpkgTfYVM2JNy4wmNKAu1pGZVZ7T4QLzhvM/B2Vb5G9RYivpeab6+44Hu7Ne3LL90/5noYSkMcAHx054IGVtwCuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9X8O/3"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 9,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 9,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 10,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 10,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ],
    "contracts": [
      "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg3RjYwp6lL7XajvEvm7iNq5KLyfXpybbmKQXb+iOzt6/5AYP4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4lKDdGNjCnqUvtdqO8S+buI2rkovJ9enJtuYpBdv6I7O3r/hxgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatig/OJdc7quICtQ5NDRs4AnNC4CAml1Rk+yukDNxgsfRl2AgICAoOE3SJ7NFgWikf5Diz5ODDyxSzAvj+fsIYI10YhYpvfagICAgID4T6DhN0iezRYFopH+Q4s+Tgw8sUswL4/n7CGCNdGIWKb32u2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/X4SaD84l1zuq4gK1Dk0NGzgCc0LgICaXVGT7K6QM3GCx9GXeegMoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAArj4qCRnDmiIQXoObi9BsqN64Iwy/saIfO5/lEZSSZpgSp538DA+Qap+QamoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+EOhAGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkoGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QO2oGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMLcUPQ=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ],
    "contracts": [
      "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg3RjYwp6lL7XajvEvm7iNq5KLyfXpybbmKQXb+iOzt6/5AYP4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4lKDdGNjCnqUvtdqO8S+buI2rkovJ9enJtuYpBdv6I7O3r/hxgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatig/OJdc7quICtQ5NDRs4AnNC4CAml1Rk+yukDNxgsfRl2AgICAoOE3SJ7NFgWikf5Diz5ODDyxSzAvj+fsIYI10YhYpvfagICAgID4T6DhN0iezRYFopH+Q4s+Tgw8sUswL4/n7CGCNdGIWKb32u2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/X4SaD84l1zuq4gK1Dk0NGzgCc0LgICaXVGT7K6QM3GCx9GXeegMoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAArj4qCRnDmiIQXoObi9BsqN64Iwy/saIfO5/lEZSSZpgSp538DA+Qap+QamoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+EOhAGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkoGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QO2oGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMLcUPQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303422268,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
  "id": -576460752303422268,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QL7ggJuAbkC9PkC8T8B+QLsuLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5P9BLORlFnNWP46Iw23Suc9M0u1MToYNRjGwe0xrNZbVuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AgIoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAc6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwLi5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMC4ufi3QAG4QGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkHklzMgEiJuGa1TSZkIu3K+YdJ9z2A0ZmrndttUxpu9m4cfhvKQKhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwBwehBWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5Ae4yCOvwLRy2pdytmVuW6e0b4NzEVlVrJMD+RlTwM5LuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AkJoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwHq9rHM=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBZhDporS1K6MjovyRt53btKGuahrwMB59sXQOYAYKvcXZUxU43h/hY4D0PsuSCruHyFssc9ukQrr0SoZZhTWsKuECpkgTfYVM2JNy4wmNKAu1pGZVZ7T4QLzhvM/B2Vb5G9RYivpeab6+44Hu7Ne3LL90/5noYSkMcAHx054IGVtwCuEj4RjkCoQYkNwR2ZqC3eagdGXTxJojMkYM0knXub/hWPM4+R27pkwqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9X8O/3",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABrDrddQ=="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "gas_price": 1000000515,
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "signed_tx": "tx_+Qi+CwHAuQi4+Qi1ggIJAaEGJDcEdmagt3moHRl08SaIzJGDNJJ17m/4VjzOPkdu6ZOhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwuNT40gsB+IS4QFmEOmitLUroyOi/JG3ndu0oa5qGvAwHn2xdA5gBgq9xdlTFTjeH+FjgPQ+y5IKu4fIWyxz26RCuvRKhlmFNawq4QKmSBN9hUzYk3LjCY0oC7WkZlVntPhAvOG8z8HZVvkb1FiK+l5pvr7jge7s17csv3T/mehhKQxwAfHTnggZW3AK4SPhGOQKhBiQ3BHZmoLd5qB0ZdPEmiMyRgzSSde5v+FY8zj5HbumTCqDtOc3Amcplq0xSbaR585IcTo5Yw0MEz4WRUsC9u8JRPwu4uPi2ggI+AaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvChBWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkAQqDD0JAhDuazAO4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgsE8m0wzuzlNFHYIGJ4cqtfha8BMAbdvQY9jzSLbbEWy5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaJigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5BABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQALkDiPkDhUABoGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5DqJ1/GRi5uSlXBXF7zuPMeGEyeQXkwdotSRIiuTGrJAuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AoKoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2w70ABoLHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Wi8oKAQCGP6olIl/1qulAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5IXECgEACrDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAEAhwHB32is5JCDEtaH+NpB3w==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1000000515,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_tx",
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
    "channel_id": "ch_Gx4ZGmoxqv8xzoezDT2YKPEvv2UahBkXdtnEXjvNcsqhwMu7H",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
