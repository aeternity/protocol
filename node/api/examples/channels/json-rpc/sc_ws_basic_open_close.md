
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
      "fsm_id": "ba_hIKlbkEAxpPG6iJ1o3wFP1LheKafzs7aqEtRmtGGECC2PVxM"
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
      "fsm_id": "ba_MNLZzslYLQaraS6E3PuEfVNRNQbITbf43pXKdY45gKRHmwqY"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsDvsywiA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423456,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECeItZ7Z/XSnQe9SLHy6SC9dcrva7U2F4NRlqPRex4tuvNRW2XcV3/ujKMfEXbh8/1L+RDRo4ZNq/2TtaOlgTQPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LA3Wo8c4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423456,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "fsm_id": "ba_MNLZzslYLQaraS6E3PuEfVNRNQbITbf43pXKdY45gKRHmwqY",
      "signed_tx": "tx_+MsLAfhCuECeItZ7Z/XSnQe9SLHy6SC9dcrva7U2F4NRlqPRex4tuvNRW2XcV3/ujKMfEXbh8/1L+RDRo4ZNq/2TtaOlgTQPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LA3Wo8c4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423455,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAniLWe2f10p0HvUix8ukgvXXK72u1NheDUZaj0XseLbrzUVtl3Fd/7oyjHxF24fP9S/kQ0aOGTav9k7WjpYE0D7hA2jYU1yBAHGKWIPbwm87YR+xwXr5gJOfknZb5d1TEewAqo7yAIPdJwul9XdEK7ou8zTZd6Cs4r8KygdXjyF9OAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwMCPIk4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423455,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAniLWe2f10p0HvUix8ukgvXXK72u1NheDUZaj0XseLbrzUVtl3Fd/7oyjHxF24fP9S/kQ0aOGTav9k7WjpYE0D7hA2jYU1yBAHGKWIPbwm87YR+xwXr5gJOfknZb5d1TEewAqo7yAIPdJwul9XdEK7ou8zTZd6Cs4r8KygdXjyF9OAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwMCPIk4",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_hIKlbkEAxpPG6iJ1o3wFP1LheKafzs7aqEtRmtGGECC2PVxM"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAniLWe2f10p0HvUix8ukgvXXK72u1NheDUZaj0XseLbrzUVtl3Fd/7oyjHxF24fP9S/kQ0aOGTav9k7WjpYE0D7hA2jYU1yBAHGKWIPbwm87YR+xwXr5gJOfknZb5d1TEewAqo7yAIPdJwul9XdEK7ou8zTZd6Cs4r8KygdXjyF9OAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwMCPIk4",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAniLWe2f10p0HvUix8ukgvXXK72u1NheDUZaj0XseLbrzUVtl3Fd/7oyjHxF24fP9S/kQ0aOGTav9k7WjpYE0D7hA2jYU1yBAHGKWIPbwm87YR+xwXr5gJOfknZb5d1TEewAqo7yAIPdJwul9XdEK7ou8zTZd6Cs4r8KygdXjyF9OAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwMCPIk4",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAniLWe2f10p0HvUix8ukgvXXK72u1NheDUZaj0XseLbrzUVtl3Fd/7oyjHxF24fP9S/kQ0aOGTav9k7WjpYE0D7hA2jYU1yBAHGKWIPbwm87YR+xwXr5gJOfknZb5d1TEewAqo7yAIPdJwul9XdEK7ou8zTZd6Cs4r8KygdXjyF9OAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwMCPIk4",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "message": {
        "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "message": {
        "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
  "id": -576460752303423454,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423454,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+QENCwH4hLhAniLWe2f10p0HvUix8ukgvXXK72u1NheDUZaj0XseLbrzUVtl3Fd/7oyjHxF24fP9S/kQ0aOGTav9k7WjpYE0D7hA2jYU1yBAHGKWIPbwm87YR+xwXr5gJOfknZb5d1TEewAqo7yAIPdJwul9XdEK7ou8zTZd6Cs4r8KygdXjyF9OAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwMCPIk4"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+QENCwH4hLhAniLWe2f10p0HvUix8ukgvXXK72u1NheDUZaj0XseLbrzUVtl3Fd/7oyjHxF24fP9S/kQ0aOGTav9k7WjpYE0D7hA2jYU1yBAHGKWIPbwm87YR+xwXr5gJOfknZb5d1TEewAqo7yAIPdJwul9XdEK7ou8zTZd6Cs4r8KygdXjyF9OAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwMCPIk4"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423453,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423453,
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
    "amount": "1",
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": 17,
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": 17,
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr117Jd1653QsOjDwA+227NsNf4+Li1gZD2ZbltdnSDUAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeArQLu1M=",
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
  "id": -576460752303423452,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA6iGehTm7jxU8XQi5zNE7yuSXy0LWgq0XfB5bV2tnPvCDhEZplBg6cW1DLA4m/1ICT6+I0yvl21qrd9ZLq8xoIuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKohXZg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423452,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA6iGehTm7jxU8XQi5zNE7yuSXy0LWgq0XfB5bV2tnPvCDhEZplBg6cW1DLA4m/1ICT6+I0yvl21qrd9ZLq8xoIuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKohXZg",
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
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA6iGehTm7jxU8XQi5zNE7yuSXy0LWgq0XfB5bV2tnPvCDhEZplBg6cW1DLA4m/1ICT6+I0yvl21qrd9ZLq8xoIuECkzlvAVOS6AFHCMr9aX0I00wSoRc8UmSyYZF5tMqgF7wEtqM4ZyamtrS1h3uFH7fJMnItnLOhUGv5fbl9QlV8PuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLlVvLc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423451,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEA6iGehTm7jxU8XQi5zNE7yuSXy0LWgq0XfB5bV2tnPvCDhEZplBg6cW1DLA4m/1ICT6+I0yvl21qrd9ZLq8xoIuECkzlvAVOS6AFHCMr9aX0I00wSoRc8UmSyYZF5tMqgF7wEtqM4ZyamtrS1h3uFH7fJMnItnLOhUGv5fbl9QlV8PuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLlVvLc"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEA6iGehTm7jxU8XQi5zNE7yuSXy0LWgq0XfB5bV2tnPvCDhEZplBg6cW1DLA4m/1ICT6+I0yvl21qrd9ZLq8xoIuECkzlvAVOS6AFHCMr9aX0I00wSoRc8UmSyYZF5tMqgF7wEtqM4ZyamtrS1h3uFH7fJMnItnLOhUGv5fbl9QlV8PuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLlVvLc"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423450,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423450,
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
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA6iGehTm7jxU8XQi5zNE7yuSXy0LWgq0XfB5bV2tnPvCDhEZplBg6cW1DLA4m/1ICT6+I0yvl21qrd9ZLq8xoIuECkzlvAVOS6AFHCMr9aX0I00wSoRc8UmSyYZF5tMqgF7wEtqM4ZyamtrS1h3uFH7fJMnItnLOhUGv5fbl9QlV8PuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLlVvLc",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423448,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423448,
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
    "amount": "1",
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr117Jd1653QsOjDwA+227NsNf4+Li1gZD2ZbltdnSDUA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzTMA20=",
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
  "id": -576460752303423447,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB+7+0N6MnR7lvGseSNsVzLK9e/3g7IUe0wl5BCVb0IL2fGrxTq7TobaL5/yeqj9MkXgEhwFcB5IgWl+8PAUhMDuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtiCQfg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423447,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB+7+0N6MnR7lvGseSNsVzLK9e/3g7IUe0wl5BCVb0IL2fGrxTq7TobaL5/yeqj9MkXgEhwFcB5IgWl+8PAUhMDuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtiCQfg",
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
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBl3qTNHY0lQXMax5IQkCpgMejnPHbqiq3LDG4inlQTDdLquettBGhLSQQ2IRD3XcdMOeiwkUfoOUmXJOXhTS8MuEB+7+0N6MnR7lvGseSNsVzLK9e/3g7IUe0wl5BCVb0IL2fGrxTq7TobaL5/yeqj9MkXgEhwFcB5IgWl+8PAUhMDuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguLtJDK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423446,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEBl3qTNHY0lQXMax5IQkCpgMejnPHbqiq3LDG4inlQTDdLquettBGhLSQQ2IRD3XcdMOeiwkUfoOUmXJOXhTS8MuEB+7+0N6MnR7lvGseSNsVzLK9e/3g7IUe0wl5BCVb0IL2fGrxTq7TobaL5/yeqj9MkXgEhwFcB5IgWl+8PAUhMDuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguLtJDK"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEBl3qTNHY0lQXMax5IQkCpgMejnPHbqiq3LDG4inlQTDdLquettBGhLSQQ2IRD3XcdMOeiwkUfoOUmXJOXhTS8MuEB+7+0N6MnR7lvGseSNsVzLK9e/3g7IUe0wl5BCVb0IL2fGrxTq7TobaL5/yeqj9MkXgEhwFcB5IgWl+8PAUhMDuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguLtJDK"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423445,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423445,
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
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBl3qTNHY0lQXMax5IQkCpgMejnPHbqiq3LDG4inlQTDdLquettBGhLSQQ2IRD3XcdMOeiwkUfoOUmXJOXhTS8MuEB+7+0N6MnR7lvGseSNsVzLK9e/3g7IUe0wl5BCVb0IL2fGrxTq7TobaL5/yeqj9MkXgEhwFcB5IgWl+8PAUhMDuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguLtJDK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423443,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423443,
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr117Jd1653QsOjDwA+227NsNf4+Li1gZD2ZbltdnSDUBKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMR9QmBY=",
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
  "id": -576460752303423442,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAI1RA/NY2XR8BJ3m+84O+YjzMFc1iVEnWvdZdiGY38ta3E0n67ezk8teiGSsvdMT0JXsHqbpo8dP+0aQ7KhuUDuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1ASgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jH0QMiO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423442,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAI1RA/NY2XR8BJ3m+84O+YjzMFc1iVEnWvdZdiGY38ta3E0n67ezk8teiGSsvdMT0JXsHqbpo8dP+0aQ7KhuUDuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1ASgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jH0QMiO",
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
  "id": -576460752303423441,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAI1RA/NY2XR8BJ3m+84O+YjzMFc1iVEnWvdZdiGY38ta3E0n67ezk8teiGSsvdMT0JXsHqbpo8dP+0aQ7KhuUDuEDnINIeSTCqrPoaGwmGuiDih6XkvI5Cieck3l7jVCMilbQQU8A+rTT6h7D5qWR7d9wJf39ZQNsD7UyjXkfsyFADuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1ASgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGPVlwB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423441,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEAI1RA/NY2XR8BJ3m+84O+YjzMFc1iVEnWvdZdiGY38ta3E0n67ezk8teiGSsvdMT0JXsHqbpo8dP+0aQ7KhuUDuEDnINIeSTCqrPoaGwmGuiDih6XkvI5Cieck3l7jVCMilbQQU8A+rTT6h7D5qWR7d9wJf39ZQNsD7UyjXkfsyFADuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1ASgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGPVlwB"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEAI1RA/NY2XR8BJ3m+84O+YjzMFc1iVEnWvdZdiGY38ta3E0n67ezk8teiGSsvdMT0JXsHqbpo8dP+0aQ7KhuUDuEDnINIeSTCqrPoaGwmGuiDih6XkvI5Cieck3l7jVCMilbQQU8A+rTT6h7D5qWR7d9wJf39ZQNsD7UyjXkfsyFADuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1ASgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGPVlwB"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423440,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423440,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAI1RA/NY2XR8BJ3m+84O+YjzMFc1iVEnWvdZdiGY38ta3E0n67ezk8teiGSsvdMT0JXsHqbpo8dP+0aQ7KhuUDuEDnINIeSTCqrPoaGwmGuiDih6XkvI5Cieck3l7jVCMilbQQU8A+rTT6h7D5qWR7d9wJf39ZQNsD7UyjXkfsyFADuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1ASgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGPVlwB",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423438,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423438,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
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
    "amount": "1",
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": 17,
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": 17,
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr117Jd1653QsOjDwA+227NsNf4+Li1gZD2ZbltdnSDUBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC90SslE=",
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
  "id": -576460752303423437,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBYbzumzoh2SzPsNPNilBpGvivEHTdMms0EE8VvXO4HUIt8SE7GkUk9htnDtIk2srk/95os3FT/wGAtVtO8CcEHuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgstLPHL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423437,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBYbzumzoh2SzPsNPNilBpGvivEHTdMms0EE8VvXO4HUIt8SE7GkUk9htnDtIk2srk/95os3FT/wGAtVtO8CcEHuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgstLPHL",
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
  "id": -576460752303423436,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBYbzumzoh2SzPsNPNilBpGvivEHTdMms0EE8VvXO4HUIt8SE7GkUk9htnDtIk2srk/95os3FT/wGAtVtO8CcEHuEDTxCGa3M4TpVqyaY+MGfXqzgsbddmkDLIB4KGj62VJ4UNkHvkuHjL8prghDznHjDIvq7BL8QQ7JIioGqSifQEHuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtCXgXL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423436,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEBYbzumzoh2SzPsNPNilBpGvivEHTdMms0EE8VvXO4HUIt8SE7GkUk9htnDtIk2srk/95os3FT/wGAtVtO8CcEHuEDTxCGa3M4TpVqyaY+MGfXqzgsbddmkDLIB4KGj62VJ4UNkHvkuHjL8prghDznHjDIvq7BL8QQ7JIioGqSifQEHuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtCXgXL"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEBYbzumzoh2SzPsNPNilBpGvivEHTdMms0EE8VvXO4HUIt8SE7GkUk9htnDtIk2srk/95os3FT/wGAtVtO8CcEHuEDTxCGa3M4TpVqyaY+MGfXqzgsbddmkDLIB4KGj62VJ4UNkHvkuHjL8prghDznHjDIvq7BL8QQ7JIioGqSifQEHuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtCXgXL"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423435,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423435,
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
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBYbzumzoh2SzPsNPNilBpGvivEHTdMms0EE8VvXO4HUIt8SE7GkUk9htnDtIk2srk/95os3FT/wGAtVtO8CcEHuEDTxCGa3M4TpVqyaY+MGfXqzgsbddmkDLIB4KGj62VJ4UNkHvkuHjL8prghDznHjDIvq7BL8QQ7JIioGqSifQEHuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtCXgXL",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423433,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423433,
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr117Jd1653QsOjDwA+227NsNf4+Li1gZD2ZbltdnSDUBqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMV70Gfc=",
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
  "id": -576460752303423432,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAzzniAnkhX086C81vY3gxd1IQVXZQ4EV5oFwg1YgvX7MYQzwiBcoFkcHC6FJkC2rGnR8X4V1D92a1Dz5rCw1cMuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1Aagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHeXHy2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423432,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAzzniAnkhX086C81vY3gxd1IQVXZQ4EV5oFwg1YgvX7MYQzwiBcoFkcHC6FJkC2rGnR8X4V1D92a1Dz5rCw1cMuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1Aagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHeXHy2",
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
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAzzniAnkhX086C81vY3gxd1IQVXZQ4EV5oFwg1YgvX7MYQzwiBcoFkcHC6FJkC2rGnR8X4V1D92a1Dz5rCw1cMuEDGfEHI4Uj1RlW4gWUHExy0jZ/a+R2wgUZ2XYgMzFYe2TWegH7zcUxcUoFini6mLeU7fNXk5QkDTrVxtHKHpFsOuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1Aagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGTo/Di"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423431,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEAzzniAnkhX086C81vY3gxd1IQVXZQ4EV5oFwg1YgvX7MYQzwiBcoFkcHC6FJkC2rGnR8X4V1D92a1Dz5rCw1cMuEDGfEHI4Uj1RlW4gWUHExy0jZ/a+R2wgUZ2XYgMzFYe2TWegH7zcUxcUoFini6mLeU7fNXk5QkDTrVxtHKHpFsOuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1Aagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGTo/Di"
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
    "data": {
      "state": "tx_+NILAfiEuEAzzniAnkhX086C81vY3gxd1IQVXZQ4EV5oFwg1YgvX7MYQzwiBcoFkcHC6FJkC2rGnR8X4V1D92a1Dz5rCw1cMuEDGfEHI4Uj1RlW4gWUHExy0jZ/a+R2wgUZ2XYgMzFYe2TWegH7zcUxcUoFini6mLeU7fNXk5QkDTrVxtHKHpFsOuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1Aagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGTo/Di"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423430,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423430,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423429,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423429,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAzzniAnkhX086C81vY3gxd1IQVXZQ4EV5oFwg1YgvX7MYQzwiBcoFkcHC6FJkC2rGnR8X4V1D92a1Dz5rCw1cMuEDGfEHI4Uj1RlW4gWUHExy0jZ/a+R2wgUZ2XYgMzFYe2TWegH7zcUxcUoFini6mLeU7fNXk5QkDTrVxtHKHpFsOuEj4RjkCoQa9deyXdeud0LDow8APttuzbDX+Pi4tYGQ9mW5bXZ0g1Aagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGTo/Di",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423428,
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423428,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423427,
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
    "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
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
  "channel_id": "ch_2SSX2t3b6NuBQdvoCj8LMAXdykWS8pstg4nRYp9CB3uQmjL8Q8",
  "id": -576460752303423427,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
