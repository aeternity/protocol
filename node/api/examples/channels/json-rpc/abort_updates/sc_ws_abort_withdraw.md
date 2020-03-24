
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
      "fsm_id": "ba_eSQrbB0Z7MCUR/cK5LHmbFQxF4WhsOFciA0gT1o90V5EkQRy"
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
      "fsm_id": "ba_0vB975RwScDTfiAy3ysqweNjANMlPTyKbGbyugm1b6keX9iA"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBuSJcaR4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422107,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuED7EGU2yp0X/NQlmIStfLzaG2TeUYvCjIKRe+1VKiSqBeLK2KajtIbLHunF9KG0CwhKF4vtHFsPaPPCKks/EmcMuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lgbn3NR+v"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422107,
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "fsm_id": "ba_0vB975RwScDTfiAy3ysqweNjANMlPTyKbGbyugm1b6keX9iA",
      "signed_tx": "tx_+MwLAfhCuED7EGU2yp0X/NQlmIStfLzaG2TeUYvCjIKRe+1VKiSqBeLK2KajtIbLHunF9KG0CwhKF4vtHFsPaPPCKks/EmcMuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lgbn3NR+v",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422106,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAySalx3XE/v6bqIESDgBUT4F9u73uuBIIF0pFQ+YootnUMBmmdwit5IfzU1ge4j3muEYlfx/hxk/0GiHrJWPYBLhA+xBlNsqdF/zUJZiErXy82htk3lGLwoyCkXvtVSokqgXiytimo7SGyx7pxfShtAsISheL7RxbD2jzwipLPxJnDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G57bbTzQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
  "id": -576460752303422106,
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAySalx3XE/v6bqIESDgBUT4F9u73uuBIIF0pFQ+YootnUMBmmdwit5IfzU1ge4j3muEYlfx/hxk/0GiHrJWPYBLhA+xBlNsqdF/zUJZiErXy82htk3lGLwoyCkXvtVSokqgXiytimo7SGyx7pxfShtAsISheL7RxbD2jzwipLPxJnDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G57bbTzQ==",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_eSQrbB0Z7MCUR/cK5LHmbFQxF4WhsOFciA0gT1o90V5EkQRy"
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAySalx3XE/v6bqIESDgBUT4F9u73uuBIIF0pFQ+YootnUMBmmdwit5IfzU1ge4j3muEYlfx/hxk/0GiHrJWPYBLhA+xBlNsqdF/zUJZiErXy82htk3lGLwoyCkXvtVSokqgXiytimo7SGyx7pxfShtAsISheL7RxbD2jzwipLPxJnDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G57bbTzQ==",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAySalx3XE/v6bqIESDgBUT4F9u73uuBIIF0pFQ+YootnUMBmmdwit5IfzU1ge4j3muEYlfx/hxk/0GiHrJWPYBLhA+xBlNsqdF/zUJZiErXy82htk3lGLwoyCkXvtVSokqgXiytimo7SGyx7pxfShtAsISheL7RxbD2jzwipLPxJnDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G57bbTzQ==",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAySalx3XE/v6bqIESDgBUT4F9u73uuBIIF0pFQ+YootnUMBmmdwit5IfzU1ge4j3muEYlfx/hxk/0GiHrJWPYBLhA+xBlNsqdF/zUJZiErXy82htk3lGLwoyCkXvtVSokqgXiytimo7SGyx7pxfShtAsISheL7RxbD2jzwipLPxJnDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G57bbTzQ==",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "message": {
        "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "message": {
        "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
  "id": -576460752303422105,
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
  "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
  "id": -576460752303422105,
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "state": "tx_+QEOCwH4hLhAySalx3XE/v6bqIESDgBUT4F9u73uuBIIF0pFQ+YootnUMBmmdwit5IfzU1ge4j3muEYlfx/hxk/0GiHrJWPYBLhA+xBlNsqdF/zUJZiErXy82htk3lGLwoyCkXvtVSokqgXiytimo7SGyx7pxfShtAsISheL7RxbD2jzwipLPxJnDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G57bbTzQ=="
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "state": "tx_+QEOCwH4hLhAySalx3XE/v6bqIESDgBUT4F9u73uuBIIF0pFQ+YootnUMBmmdwit5IfzU1ge4j3muEYlfx/hxk/0GiHrJWPYBLhA+xBlNsqdF/zUJZiErXy82htk3lGLwoyCkXvtVSokqgXiytimo7SGyx7pxfShtAsISheL7RxbD2jzwipLPxJnDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G57bbTzQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBg84mQ1WHGsFVdkXOPeMwrM1VMjlZJLFI0n+vtzcxJiXoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/FSIpYAKD6aIyRp0q4njYpKUN7EoE8dGS1wKGxithIYn6oqM3YIgKBuu9I9xc=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBg84mQ1WHGsFVdkXOPeMwrM1VMjlZJLFI0n+vtzcxJiXoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/AoHKQAKCLRArAVcRpHJDJSClg9OVacmLqGJRqqnqJGZLd8dhkrwJBcjJdqQ==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBg84mQ1WHGsFVdkXOPeMwrM1VMjlZJLFI0n+vtzcxJiXoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/FSIpYAKD6aIyRp0q4njYpKUN7EoE8dGS1wKGxithIYn6oqM3YIgKBuu9I9xc=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422104,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEB5UzGVXCadOrzAXjk5cR0cKtd0tAj/tcBYh8/Qjf/roiiaMBll/Fvpo7pSvlnHkJvuLvXPV0fAK1jIFEj3aEIBuHX4czQBoQYPOJkNVhxrBVXZFzj3jMKzNVTI5WSSxSNJ/r7c3MSYl6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUiKWACg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgbqiTeAf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
  "id": -576460752303422104,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
      "method": "channels.withdraw_tx",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "signed_tx": "tx_+L0LAfhCuEB5UzGVXCadOrzAXjk5cR0cKtd0tAj/tcBYh8/Qjf/roiiaMBll/Fvpo7pSvlnHkJvuLvXPV0fAK1jIFEj3aEIBuHX4czQBoQYPOJkNVhxrBVXZFzj3jMKzNVTI5WSSxSNJ/r7c3MSYl6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUiKWACg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgbqiTeAf",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
    "data": {
      "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
  "id": -576460752303422103,
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
  "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
  "id": -576460752303422103,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422102,
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
    "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
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
  "channel_id": "ch_7hoXbLuZWVcAiZDeohufNVNnnbGK6SMcVdoZY7XcWTf4kP5m1",
  "id": -576460752303422102,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
