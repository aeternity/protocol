
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=246913579753086&gas_price=1000000000&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_a5273ZIA7e37WbeRHlHfoZ7zZso3NQ0Ms+4bRSBpgCH9mdEs"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=246913579753086&gas_price=1000000000&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_MpLuPu4kt/NJCdiH/lAy5BzlpwEV/B+DCt1bmihxFEkLQHgk"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhuCRDDYefsCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtnqyNhzw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422495,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB1V+5moJwnTOmQ59exlvTVKqgSMInddEybHPw2tW/nscL0rZCNy+mp+O5BvLDIiol4zdsh60e3qGuGvia7xwoFuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIbgkQw2Hn7AoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LZ8AcbPY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422495,
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "fsm_id": "ba_MpLuPu4kt/NJCdiH/lAy5BzlpwEV/B+DCt1bmihxFEkLQHgk",
      "signed_tx": "tx_+MsLAfhCuEB1V+5moJwnTOmQ59exlvTVKqgSMInddEybHPw2tW/nscL0rZCNy+mp+O5BvLDIiol4zdsh60e3qGuGvia7xwoFuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIbgkQw2Hn7AoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LZ8AcbPY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422494,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAG3qluJPbSClZJ+9SU9mICmYFNEo8hNXYlFf0HRoU3TWn0I3QBTig4NyNUTx0Eu2WhZxJKI+RTYt6LXIwcA6jArhAdVfuZqCcJ0zpkOfXsZb01SqoEjCJ3XRMmxz8NrVv57HC9K2QjcvpqfjuQbywyIqJeM3bIetHt6hrhr4mu8cKBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCG4JEMNh5+wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2ehzPRS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
  "id": -576460752303422494,
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAG3qluJPbSClZJ+9SU9mICmYFNEo8hNXYlFf0HRoU3TWn0I3QBTig4NyNUTx0Eu2WhZxJKI+RTYt6LXIwcA6jArhAdVfuZqCcJ0zpkOfXsZb01SqoEjCJ3XRMmxz8NrVv57HC9K2QjcvpqfjuQbywyIqJeM3bIetHt6hrhr4mu8cKBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCG4JEMNh5+wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2ehzPRS",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_a5273ZIA7e37WbeRHlHfoZ7zZso3NQ0Ms+4bRSBpgCH9mdEs"
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAG3qluJPbSClZJ+9SU9mICmYFNEo8hNXYlFf0HRoU3TWn0I3QBTig4NyNUTx0Eu2WhZxJKI+RTYt6LXIwcA6jArhAdVfuZqCcJ0zpkOfXsZb01SqoEjCJ3XRMmxz8NrVv57HC9K2QjcvpqfjuQbywyIqJeM3bIetHt6hrhr4mu8cKBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCG4JEMNh5+wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2ehzPRS",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAG3qluJPbSClZJ+9SU9mICmYFNEo8hNXYlFf0HRoU3TWn0I3QBTig4NyNUTx0Eu2WhZxJKI+RTYt6LXIwcA6jArhAdVfuZqCcJ0zpkOfXsZb01SqoEjCJ3XRMmxz8NrVv57HC9K2QjcvpqfjuQbywyIqJeM3bIetHt6hrhr4mu8cKBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCG4JEMNh5+wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2ehzPRS",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAG3qluJPbSClZJ+9SU9mICmYFNEo8hNXYlFf0HRoU3TWn0I3QBTig4NyNUTx0Eu2WhZxJKI+RTYt6LXIwcA6jArhAdVfuZqCcJ0zpkOfXsZb01SqoEjCJ3XRMmxz8NrVv57HC9K2QjcvpqfjuQbywyIqJeM3bIetHt6hrhr4mu8cKBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCG4JEMNh5+wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2ehzPRS",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "message": {
        "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "message": {
        "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
  "id": -576460752303422493,
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
  "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
  "id": -576460752303422493,
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "state": "tx_+QENCwH4hLhAG3qluJPbSClZJ+9SU9mICmYFNEo8hNXYlFf0HRoU3TWn0I3QBTig4NyNUTx0Eu2WhZxJKI+RTYt6LXIwcA6jArhAdVfuZqCcJ0zpkOfXsZb01SqoEjCJ3XRMmxz8NrVv57HC9K2QjcvpqfjuQbywyIqJeM3bIetHt6hrhr4mu8cKBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCG4JEMNh5+wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2ehzPRS"
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "state": "tx_+QENCwH4hLhAG3qluJPbSClZJ+9SU9mICmYFNEo8hNXYlFf0HRoU3TWn0I3QBTig4NyNUTx0Eu2WhZxJKI+RTYt6LXIwcA6jArhAdVfuZqCcJ0zpkOfXsZb01SqoEjCJ3XRMmxz8NrVv57HC9K2QjcvpqfjuQbywyIqJeM3bIetHt6hrhr4mu8cKBbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCG4JEMNh5+wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2ehzPRS"
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBuR2whXGFg5GPxYVF2qCDwppokreRmptPSh7Fh+8BUqLoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/+GHLHOiuwBAIYPXtZ/KABo9g3pfg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422492,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBmurh/DCXIvmqdfNvanTtQT/lVtkdxep2nSI69DlN6KYdXhwEV0ItVZa38JS7T5+1v1FY1dzyj9DWwhpi1hzEMuF/4XTUBoQbkdsIVxhYORj8WFRdqgg8KaaJK3kZqbT0oexYfvAVKi6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAaAphalY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
  "id": -576460752303422492,
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBmurh/DCXIvmqdfNvanTtQT/lVtkdxep2nSI69DlN6KYdXhwEV0ItVZa38JS7T5+1v1FY1dzyj9DWwhpi1hzEMuF/4XTUBoQbkdsIVxhYORj8WFRdqgg8KaaJK3kZqbT0oexYfvAVKi6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAaAphalY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422491,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAk+kpYjfX2hZfHgyaYTrhOa/UhkQwUJW+HbD44wR4x9WdpKlrJP0H0IeMXzhfaNCf3J24WxlnxGK5o9vvqIFkKuEBmurh/DCXIvmqdfNvanTtQT/lVtkdxep2nSI69DlN6KYdXhwEV0ItVZa38JS7T5+1v1FY1dzyj9DWwhpi1hzEMuF/4XTUBoQbkdsIVxhYORj8WFRdqgg8KaaJK3kZqbT0oexYfvAVKi6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAaFw8E6A="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
  "id": -576460752303422491,
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAk+kpYjfX2hZfHgyaYTrhOa/UhkQwUJW+HbD44wR4x9WdpKlrJP0H0IeMXzhfaNCf3J24WxlnxGK5o9vvqIFkKuEBmurh/DCXIvmqdfNvanTtQT/lVtkdxep2nSI69DlN6KYdXhwEV0ItVZa38JS7T5+1v1FY1dzyj9DWwhpi1hzEMuF/4XTUBoQbkdsIVxhYORj8WFRdqgg8KaaJK3kZqbT0oexYfvAVKi6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAaFw8E6A=",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAk+kpYjfX2hZfHgyaYTrhOa/UhkQwUJW+HbD44wR4x9WdpKlrJP0H0IeMXzhfaNCf3J24WxlnxGK5o9vvqIFkKuEBmurh/DCXIvmqdfNvanTtQT/lVtkdxep2nSI69DlN6KYdXhwEV0ItVZa38JS7T5+1v1FY1dzyj9DWwhpi1hzEMuF/4XTUBoQbkdsIVxhYORj8WFRdqgg8KaaJK3kZqbT0oexYfvAVKi6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAaFw8E6A=",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAk+kpYjfX2hZfHgyaYTrhOa/UhkQwUJW+HbD44wR4x9WdpKlrJP0H0IeMXzhfaNCf3J24WxlnxGK5o9vvqIFkKuEBmurh/DCXIvmqdfNvanTtQT/lVtkdxep2nSI69DlN6KYdXhwEV0ItVZa38JS7T5+1v1FY1dzyj9DWwhpi1hzEMuF/4XTUBoQbkdsIVxhYORj8WFRdqgg8KaaJK3kZqbT0oexYfvAVKi6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAaFw8E6A=",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAk+kpYjfX2hZfHgyaYTrhOa/UhkQwUJW+HbD44wR4x9WdpKlrJP0H0IeMXzhfaNCf3J24WxlnxGK5o9vvqIFkKuEBmurh/DCXIvmqdfNvanTtQT/lVtkdxep2nSI69DlN6KYdXhwEV0ItVZa38JS7T5+1v1FY1dzyj9DWwhpi1hzEMuF/4XTUBoQbkdsIVxhYORj8WFRdqgg8KaaJK3kZqbT0oexYfvAVKi6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAaFw8E6A=",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
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
    "channel_id": "ch_2jcocYUYY6gfXeDJEAC6vZKZ6P2sBDfoCawMhN5MJwWBRhYYuG",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
