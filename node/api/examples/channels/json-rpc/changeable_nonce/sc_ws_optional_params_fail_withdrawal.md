
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
      "fsm_id": "ba_swguNzeWqXq77IpLYicSs7eSlEA3RX8L3Y1FynO+NKmW6mc7"
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
      "fsm_id": "ba_JAAMA77bXyd1TJmWwBt/4+sj85xKOdwy9stjD7u4bG6GQviC"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBnZiQh0M=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422257,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEDECpIxMbdSbfPxjMHGOPpeS+BmpMIP8PUHiRJmur98QGDiFQfnGBVVWbfWfDVMXhzJjaIq7F5ke/voqQFHz/UIuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZ0VNEyu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422257,
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "fsm_id": "ba_JAAMA77bXyd1TJmWwBt/4+sj85xKOdwy9stjD7u4bG6GQviC",
      "signed_tx": "tx_+MwLAfhCuEDECpIxMbdSbfPxjMHGOPpeS+BmpMIP8PUHiRJmur98QGDiFQfnGBVVWbfWfDVMXhzJjaIq7F5ke/voqQFHz/UIuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZ0VNEyu",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422256,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhArC1vjlfykqvW4v8yxlZcciPm6uWjjHGer1sOHY++UrLB5oDwrCeifi5EkUhUVxJZk8Xon9w0NVJ/fWfsUKEqBLhAxAqSMTG3Um3z8YzBxjj6XkvgZqTCD/D1B4kSZrq/fEBg4hUH5xgVVVm31nw1TF4cyY2iKuxeZHv76KkBR8/1CLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gd+nz3jw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
  "id": -576460752303422256,
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhArC1vjlfykqvW4v8yxlZcciPm6uWjjHGer1sOHY++UrLB5oDwrCeifi5EkUhUVxJZk8Xon9w0NVJ/fWfsUKEqBLhAxAqSMTG3Um3z8YzBxjj6XkvgZqTCD/D1B4kSZrq/fEBg4hUH5xgVVVm31nw1TF4cyY2iKuxeZHv76KkBR8/1CLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gd+nz3jw==",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_swguNzeWqXq77IpLYicSs7eSlEA3RX8L3Y1FynO+NKmW6mc7"
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhArC1vjlfykqvW4v8yxlZcciPm6uWjjHGer1sOHY++UrLB5oDwrCeifi5EkUhUVxJZk8Xon9w0NVJ/fWfsUKEqBLhAxAqSMTG3Um3z8YzBxjj6XkvgZqTCD/D1B4kSZrq/fEBg4hUH5xgVVVm31nw1TF4cyY2iKuxeZHv76KkBR8/1CLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gd+nz3jw==",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhArC1vjlfykqvW4v8yxlZcciPm6uWjjHGer1sOHY++UrLB5oDwrCeifi5EkUhUVxJZk8Xon9w0NVJ/fWfsUKEqBLhAxAqSMTG3Um3z8YzBxjj6XkvgZqTCD/D1B4kSZrq/fEBg4hUH5xgVVVm31nw1TF4cyY2iKuxeZHv76KkBR8/1CLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gd+nz3jw==",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhArC1vjlfykqvW4v8yxlZcciPm6uWjjHGer1sOHY++UrLB5oDwrCeifi5EkUhUVxJZk8Xon9w0NVJ/fWfsUKEqBLhAxAqSMTG3Um3z8YzBxjj6XkvgZqTCD/D1B4kSZrq/fEBg4hUH5xgVVVm31nw1TF4cyY2iKuxeZHv76KkBR8/1CLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gd+nz3jw==",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "message": {
        "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "message": {
        "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
  "id": -576460752303422255,
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
  "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
  "id": -576460752303422255,
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "state": "tx_+QEOCwH4hLhArC1vjlfykqvW4v8yxlZcciPm6uWjjHGer1sOHY++UrLB5oDwrCeifi5EkUhUVxJZk8Xon9w0NVJ/fWfsUKEqBLhAxAqSMTG3Um3z8YzBxjj6XkvgZqTCD/D1B4kSZrq/fEBg4hUH5xgVVVm31nw1TF4cyY2iKuxeZHv76KkBR8/1CLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gd+nz3jw=="
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "state": "tx_+QEOCwH4hLhArC1vjlfykqvW4v8yxlZcciPm6uWjjHGer1sOHY++UrLB5oDwrCeifi5EkUhUVxJZk8Xon9w0NVJ/fWfsUKEqBLhAxAqSMTG3Um3z8YzBxjj6XkvgZqTCD/D1B4kSZrq/fEBg4hUH5xgVVVm31nw1TF4cyY2iKuxeZHv76KkBR8/1CLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gd+nz3jw=="
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
    "amount": 2,
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "signed_tx": "tx_+HwLAcC4d/h1NAGhBuVRUIoqHFS+zcEwQkM7752K7Bqn9ZTxQqvK12mt2ka+oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/OmLnoAKD6aIyRp0q4njYpKUN7EoE8dGS1wKGxithIYn6oqM3YIgKDEtaHCEaG4w==",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBuVRUIoqHFS+zcEwQkM7752K7Bqn9ZTxQqvK12mt2ka+oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBnoto1qc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422254,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEAZzuM7M6Oc+SKyUxDptbp8OR0bFNhI5Wt6YszgpH7nKRpGLbSN+W/ujAGEarclZ6e54Qr7kU+UxySXQtowICQBuGD4XjUBoQblUVCKKhxUvs3BMEJDO++diuwap/WU8UKrytdprdpGvqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ6OWlQm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
  "id": -576460752303422254,
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEAZzuM7M6Oc+SKyUxDptbp8OR0bFNhI5Wt6YszgpH7nKRpGLbSN+W/ujAGEarclZ6e54Qr7kU+UxySXQtowICQBuGD4XjUBoQblUVCKKhxUvs3BMEJDO++diuwap/WU8UKrytdprdpGvqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ6OWlQm",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422253,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAZzuM7M6Oc+SKyUxDptbp8OR0bFNhI5Wt6YszgpH7nKRpGLbSN+W/ujAGEarclZ6e54Qr7kU+UxySXQtowICQBuEBdgwYRM2EKL140xZ4hAyVKdjipNX8okOU0ku7jCkMjuuGpkx2GOaD4+puKhckqAMsMjfC0IstIWx61K8qnHM0AuGD4XjUBoQblUVCKKhxUvs3BMEJDO++diuwap/WU8UKrytdprdpGvqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ5lbIsb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
  "id": -576460752303422253,
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAZzuM7M6Oc+SKyUxDptbp8OR0bFNhI5Wt6YszgpH7nKRpGLbSN+W/ujAGEarclZ6e54Qr7kU+UxySXQtowICQBuEBdgwYRM2EKL140xZ4hAyVKdjipNX8okOU0ku7jCkMjuuGpkx2GOaD4+puKhckqAMsMjfC0IstIWx61K8qnHM0AuGD4XjUBoQblUVCKKhxUvs3BMEJDO++diuwap/WU8UKrytdprdpGvqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ5lbIsb",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAZzuM7M6Oc+SKyUxDptbp8OR0bFNhI5Wt6YszgpH7nKRpGLbSN+W/ujAGEarclZ6e54Qr7kU+UxySXQtowICQBuEBdgwYRM2EKL140xZ4hAyVKdjipNX8okOU0ku7jCkMjuuGpkx2GOaD4+puKhckqAMsMjfC0IstIWx61K8qnHM0AuGD4XjUBoQblUVCKKhxUvs3BMEJDO++diuwap/WU8UKrytdprdpGvqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ5lbIsb",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAZzuM7M6Oc+SKyUxDptbp8OR0bFNhI5Wt6YszgpH7nKRpGLbSN+W/ujAGEarclZ6e54Qr7kU+UxySXQtowICQBuEBdgwYRM2EKL140xZ4hAyVKdjipNX8okOU0ku7jCkMjuuGpkx2GOaD4+puKhckqAMsMjfC0IstIWx61K8qnHM0AuGD4XjUBoQblUVCKKhxUvs3BMEJDO++diuwap/WU8UKrytdprdpGvqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ5lbIsb",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAZzuM7M6Oc+SKyUxDptbp8OR0bFNhI5Wt6YszgpH7nKRpGLbSN+W/ujAGEarclZ6e54Qr7kU+UxySXQtowICQBuEBdgwYRM2EKL140xZ4hAyVKdjipNX8okOU0ku7jCkMjuuGpkx2GOaD4+puKhckqAMsMjfC0IstIWx61K8qnHM0AuGD4XjUBoQblUVCKKhxUvs3BMEJDO++diuwap/WU8UKrytdprdpGvqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZ5lbIsb",
      "type": "channel_close_mutual_tx"
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
      "fsm_id": "ba_sb+QBD5LaHWfRifU6C0Q9tURKcwPv4p0t2BPYlFj/g3UrtHJ"
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
      "fsm_id": "ba_P/EHaFsUitbgquKslJfHNctZRV8JCG10Y3ICICiJFscPrzE1"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBn+u4L8s=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422252,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEB6ulL/jriGy39bo+xLDiSZQqDE42R7VoAVUSvYrqUxFqEe4RYQAHaF2D2heEMkryxC2ZzhFjpDxvIqzvFEu5MGuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZ8UniUU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422252,
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "fsm_id": "ba_P/EHaFsUitbgquKslJfHNctZRV8JCG10Y3ICICiJFscPrzE1",
      "signed_tx": "tx_+MwLAfhCuEB6ulL/jriGy39bo+xLDiSZQqDE42R7VoAVUSvYrqUxFqEe4RYQAHaF2D2heEMkryxC2ZzhFjpDxvIqzvFEu5MGuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZ8UniUU",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422251,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAerpS/464hst/W6PsSw4kmUKgxONke1aAFVEr2K6lMRahHuEWEAB2hdg9oXhDJK8sQtmc4RY6Q8byKs7xRLuTBrhAh+xhPSZSAhPAxFOaCNgjiPf2bAh/2SWP3M5pW2UJM1DXiL0SGKjzNXHCa9FYiG4VXjHUiFsLLUtBAISWxfaGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gfmr8JOg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
  "id": -576460752303422251,
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAerpS/464hst/W6PsSw4kmUKgxONke1aAFVEr2K6lMRahHuEWEAB2hdg9oXhDJK8sQtmc4RY6Q8byKs7xRLuTBrhAh+xhPSZSAhPAxFOaCNgjiPf2bAh/2SWP3M5pW2UJM1DXiL0SGKjzNXHCa9FYiG4VXjHUiFsLLUtBAISWxfaGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gfmr8JOg==",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_sb+QBD5LaHWfRifU6C0Q9tURKcwPv4p0t2BPYlFj/g3UrtHJ"
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAerpS/464hst/W6PsSw4kmUKgxONke1aAFVEr2K6lMRahHuEWEAB2hdg9oXhDJK8sQtmc4RY6Q8byKs7xRLuTBrhAh+xhPSZSAhPAxFOaCNgjiPf2bAh/2SWP3M5pW2UJM1DXiL0SGKjzNXHCa9FYiG4VXjHUiFsLLUtBAISWxfaGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gfmr8JOg==",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAerpS/464hst/W6PsSw4kmUKgxONke1aAFVEr2K6lMRahHuEWEAB2hdg9oXhDJK8sQtmc4RY6Q8byKs7xRLuTBrhAh+xhPSZSAhPAxFOaCNgjiPf2bAh/2SWP3M5pW2UJM1DXiL0SGKjzNXHCa9FYiG4VXjHUiFsLLUtBAISWxfaGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gfmr8JOg==",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAerpS/464hst/W6PsSw4kmUKgxONke1aAFVEr2K6lMRahHuEWEAB2hdg9oXhDJK8sQtmc4RY6Q8byKs7xRLuTBrhAh+xhPSZSAhPAxFOaCNgjiPf2bAh/2SWP3M5pW2UJM1DXiL0SGKjzNXHCa9FYiG4VXjHUiFsLLUtBAISWxfaGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gfmr8JOg==",
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
    "channel_id": "ch_2jzcT8CZiLEE5kiYwMSUr9QfrwZTBjEr5dw8FAX39Y2FcZsXCd",
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
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "message": {
        "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "message": {
        "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
  "id": -576460752303422250,
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
  "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
  "id": -576460752303422250,
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "state": "tx_+QEOCwH4hLhAerpS/464hst/W6PsSw4kmUKgxONke1aAFVEr2K6lMRahHuEWEAB2hdg9oXhDJK8sQtmc4RY6Q8byKs7xRLuTBrhAh+xhPSZSAhPAxFOaCNgjiPf2bAh/2SWP3M5pW2UJM1DXiL0SGKjzNXHCa9FYiG4VXjHUiFsLLUtBAISWxfaGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gfmr8JOg=="
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "state": "tx_+QEOCwH4hLhAerpS/464hst/W6PsSw4kmUKgxONke1aAFVEr2K6lMRahHuEWEAB2hdg9oXhDJK8sQtmc4RY6Q8byKs7xRLuTBrhAh+xhPSZSAhPAxFOaCNgjiPf2bAh/2SWP3M5pW2UJM1DXiL0SGKjzNXHCa9FYiG4VXjHUiFsLLUtBAISWxfaGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gfmr8JOg=="
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
    "amount": 2,
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "signed_tx": "tx_+HwLAcC4d/h1NAGhBpvP4aSUC6nk4MFLJz9JhbJ+52J81RVZ6aAdqjiG0iG1oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/OmLnoAKCLRArAVcRpHJDJSClg9OVacmLqGJRqqnqJGZLd8dhkrwKDEtaHrqjl/A==",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBpvP4aSUC6nk4MFLJz9JhbJ+52J81RVZ6aAdqjiG0iG1oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBoJbvksc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422249,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEDS9ccqY0vkzf+EWwqkIbD7+qsVloRE00PMyww/tOfYAUahBKHuQcrzCAqPjcOTGfLR8K42/CRJxOWP16mvsLcNuGD4XjUBoQabz+GklAup5ODBSyc/SYWyfudifNUVWemgHao4htIhtaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaB5/WMe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
  "id": -576460752303422249,
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEDS9ccqY0vkzf+EWwqkIbD7+qsVloRE00PMyww/tOfYAUahBKHuQcrzCAqPjcOTGfLR8K42/CRJxOWP16mvsLcNuGD4XjUBoQabz+GklAup5ODBSyc/SYWyfudifNUVWemgHao4htIhtaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaB5/WMe",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422248,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuECOgOR7fiEeYt+ron0/fZGmUFBJRZUGDQYapsho3wRsHVFTyYPR/iwiMC5uUCFlAnypfD4ueNGLLt8gipJ5l14HuEDS9ccqY0vkzf+EWwqkIbD7+qsVloRE00PMyww/tOfYAUahBKHuQcrzCAqPjcOTGfLR8K42/CRJxOWP16mvsLcNuGD4XjUBoQabz+GklAup5ODBSyc/SYWyfudifNUVWemgHao4htIhtaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaA55Ee5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
  "id": -576460752303422248,
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuECOgOR7fiEeYt+ron0/fZGmUFBJRZUGDQYapsho3wRsHVFTyYPR/iwiMC5uUCFlAnypfD4ueNGLLt8gipJ5l14HuEDS9ccqY0vkzf+EWwqkIbD7+qsVloRE00PMyww/tOfYAUahBKHuQcrzCAqPjcOTGfLR8K42/CRJxOWP16mvsLcNuGD4XjUBoQabz+GklAup5ODBSyc/SYWyfudifNUVWemgHao4htIhtaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaA55Ee5",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuECOgOR7fiEeYt+ron0/fZGmUFBJRZUGDQYapsho3wRsHVFTyYPR/iwiMC5uUCFlAnypfD4ueNGLLt8gipJ5l14HuEDS9ccqY0vkzf+EWwqkIbD7+qsVloRE00PMyww/tOfYAUahBKHuQcrzCAqPjcOTGfLR8K42/CRJxOWP16mvsLcNuGD4XjUBoQabz+GklAup5ODBSyc/SYWyfudifNUVWemgHao4htIhtaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaA55Ee5",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuECOgOR7fiEeYt+ron0/fZGmUFBJRZUGDQYapsho3wRsHVFTyYPR/iwiMC5uUCFlAnypfD4ueNGLLt8gipJ5l14HuEDS9ccqY0vkzf+EWwqkIbD7+qsVloRE00PMyww/tOfYAUahBKHuQcrzCAqPjcOTGfLR8K42/CRJxOWP16mvsLcNuGD4XjUBoQabz+GklAup5ODBSyc/SYWyfudifNUVWemgHao4htIhtaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaA55Ee5",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuECOgOR7fiEeYt+ron0/fZGmUFBJRZUGDQYapsho3wRsHVFTyYPR/iwiMC5uUCFlAnypfD4ueNGLLt8gipJ5l14HuEDS9ccqY0vkzf+EWwqkIbD7+qsVloRE00PMyww/tOfYAUahBKHuQcrzCAqPjcOTGfLR8K42/CRJxOWP16mvsLcNuGD4XjUBoQabz+GklAup5ODBSyc/SYWyfudifNUVWemgHao4htIhtaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaA55Ee5",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
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
    "channel_id": "ch_2Bd1YUq9y7HcSXr9FMvMAjQg6bNhLAWxKwNmg1qh2JMbFTHySa",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
