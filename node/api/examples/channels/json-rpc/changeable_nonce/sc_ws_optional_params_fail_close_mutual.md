
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
      "fsm_id": "ba_3Qf8l6pdjE6n+P/5x0NqLzX/w0PxD/whT9KqT7ElCsZuitW6"
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
      "fsm_id": "ba_gUNfiZrfu4vbO6ozR7UGp7ILeDjHjqdbYusuI8dG6mi0w5Qw"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBpY7jl7s=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422215,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECS9otuw6OKdHXOlWlCU8MZzFwWfRhhAKpnGFoCrsYeWO0orNsbqK/rLE8qY2Z4ovtLLfb375XJa7zk3K2TRv0LuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgaVk8P2/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422215,
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "fsm_id": "ba_gUNfiZrfu4vbO6ozR7UGp7ILeDjHjqdbYusuI8dG6mi0w5Qw",
      "signed_tx": "tx_+MwLAfhCuECS9otuw6OKdHXOlWlCU8MZzFwWfRhhAKpnGFoCrsYeWO0orNsbqK/rLE8qY2Z4ovtLLfb375XJa7zk3K2TRv0LuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgaVk8P2/",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422214,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAkvaLbsOjinR1zpVpQlPDGcxcFn0YYQCqZxhaAq7GHljtKKzbG6iv6yxPKmNmeKL7Sy329++VyWu85Nytk0b9C7hAueX1wL4l6ofMNQX1rl9yqPjXeySl+NYWkPsstkIiSDNOFYci5G9iPoDbVu9DECn62n/Lz4g8E+BR28IKocInALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gl5hJwng=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
  "id": -576460752303422214,
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAkvaLbsOjinR1zpVpQlPDGcxcFn0YYQCqZxhaAq7GHljtKKzbG6iv6yxPKmNmeKL7Sy329++VyWu85Nytk0b9C7hAueX1wL4l6ofMNQX1rl9yqPjXeySl+NYWkPsstkIiSDNOFYci5G9iPoDbVu9DECn62n/Lz4g8E+BR28IKocInALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gl5hJwng==",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_3Qf8l6pdjE6n+P/5x0NqLzX/w0PxD/whT9KqT7ElCsZuitW6"
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAkvaLbsOjinR1zpVpQlPDGcxcFn0YYQCqZxhaAq7GHljtKKzbG6iv6yxPKmNmeKL7Sy329++VyWu85Nytk0b9C7hAueX1wL4l6ofMNQX1rl9yqPjXeySl+NYWkPsstkIiSDNOFYci5G9iPoDbVu9DECn62n/Lz4g8E+BR28IKocInALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gl5hJwng==",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAkvaLbsOjinR1zpVpQlPDGcxcFn0YYQCqZxhaAq7GHljtKKzbG6iv6yxPKmNmeKL7Sy329++VyWu85Nytk0b9C7hAueX1wL4l6ofMNQX1rl9yqPjXeySl+NYWkPsstkIiSDNOFYci5G9iPoDbVu9DECn62n/Lz4g8E+BR28IKocInALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gl5hJwng==",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAkvaLbsOjinR1zpVpQlPDGcxcFn0YYQCqZxhaAq7GHljtKKzbG6iv6yxPKmNmeKL7Sy329++VyWu85Nytk0b9C7hAueX1wL4l6ofMNQX1rl9yqPjXeySl+NYWkPsstkIiSDNOFYci5G9iPoDbVu9DECn62n/Lz4g8E+BR28IKocInALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gl5hJwng==",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "message": {
        "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "message": {
        "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
  "id": -576460752303422213,
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
  "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
  "id": -576460752303422213,
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "state": "tx_+QEOCwH4hLhAkvaLbsOjinR1zpVpQlPDGcxcFn0YYQCqZxhaAq7GHljtKKzbG6iv6yxPKmNmeKL7Sy329++VyWu85Nytk0b9C7hAueX1wL4l6ofMNQX1rl9yqPjXeySl+NYWkPsstkIiSDNOFYci5G9iPoDbVu9DECn62n/Lz4g8E+BR28IKocInALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gl5hJwng=="
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "state": "tx_+QEOCwH4hLhAkvaLbsOjinR1zpVpQlPDGcxcFn0YYQCqZxhaAq7GHljtKKzbG6iv6yxPKmNmeKL7Sy329++VyWu85Nytk0b9C7hAueX1wL4l6ofMNQX1rl9yqPjXeySl+NYWkPsstkIiSDNOFYci5G9iPoDbVu9DECn62n/Lz4g8E+BR28IKocInALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gl5hJwng=="
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
  "params": {
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "signed_tx": "tx_+GcLAcC4YvhgNQGhBhjP1rWNfMbs/fcU9ayGBHhDDlF2EfKSo+3JqbiyBr9eoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3872/H/+GHKrSZ0ABAIYPbM7GgACDEtaHToOIhQ==",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBhjP1rWNfMbs/fcU9ayGBHhDDlF2EfKSo+3JqbiyBr9eoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBphZVTVY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422212,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuED8HcEwQyS2QdkWe97398jmF9sD08n00C4oDMSc0ktZ9W2jdvy6AmWIOUvHRmU+wnnqSa4uMSK8icS+gOWBtGcNuGD4XjUBoQYYz9a1jXzG7P33FPWshgR4Qw5RdhHykqPtyam4sga/XqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaaP0iH0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
  "id": -576460752303422212,
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "signed_tx": "tx_+KgLAfhCuED8HcEwQyS2QdkWe97398jmF9sD08n00C4oDMSc0ktZ9W2jdvy6AmWIOUvHRmU+wnnqSa4uMSK8icS+gOWBtGcNuGD4XjUBoQYYz9a1jXzG7P33FPWshgR4Qw5RdhHykqPtyam4sga/XqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaaP0iH0",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422211,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuED74yJTRVghO/cPRDBHxYUDgdml3bqCqL2b9+ctxTi+sKNrPF8D5uYM2C08BwrV9zIgHPT3ZpionpWgg1Ea/igAuED8HcEwQyS2QdkWe97398jmF9sD08n00C4oDMSc0ktZ9W2jdvy6AmWIOUvHRmU+wnnqSa4uMSK8icS+gOWBtGcNuGD4XjUBoQYYz9a1jXzG7P33FPWshgR4Qw5RdhHykqPtyam4sga/XqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgab4zX6i"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
  "id": -576460752303422211,
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuED74yJTRVghO/cPRDBHxYUDgdml3bqCqL2b9+ctxTi+sKNrPF8D5uYM2C08BwrV9zIgHPT3ZpionpWgg1Ea/igAuED8HcEwQyS2QdkWe97398jmF9sD08n00C4oDMSc0ktZ9W2jdvy6AmWIOUvHRmU+wnnqSa4uMSK8icS+gOWBtGcNuGD4XjUBoQYYz9a1jXzG7P33FPWshgR4Qw5RdhHykqPtyam4sga/XqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgab4zX6i",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuED74yJTRVghO/cPRDBHxYUDgdml3bqCqL2b9+ctxTi+sKNrPF8D5uYM2C08BwrV9zIgHPT3ZpionpWgg1Ea/igAuED8HcEwQyS2QdkWe97398jmF9sD08n00C4oDMSc0ktZ9W2jdvy6AmWIOUvHRmU+wnnqSa4uMSK8icS+gOWBtGcNuGD4XjUBoQYYz9a1jXzG7P33FPWshgR4Qw5RdhHykqPtyam4sga/XqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgab4zX6i",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuED74yJTRVghO/cPRDBHxYUDgdml3bqCqL2b9+ctxTi+sKNrPF8D5uYM2C08BwrV9zIgHPT3ZpionpWgg1Ea/igAuED8HcEwQyS2QdkWe97398jmF9sD08n00C4oDMSc0ktZ9W2jdvy6AmWIOUvHRmU+wnnqSa4uMSK8icS+gOWBtGcNuGD4XjUBoQYYz9a1jXzG7P33FPWshgR4Qw5RdhHykqPtyam4sga/XqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgab4zX6i",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuED74yJTRVghO/cPRDBHxYUDgdml3bqCqL2b9+ctxTi+sKNrPF8D5uYM2C08BwrV9zIgHPT3ZpionpWgg1Ea/igAuED8HcEwQyS2QdkWe97398jmF9sD08n00C4oDMSc0ktZ9W2jdvy6AmWIOUvHRmU+wnnqSa4uMSK8icS+gOWBtGcNuGD4XjUBoQYYz9a1jXzG7P33FPWshgR4Qw5RdhHykqPtyam4sga/XqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgab4zX6i",
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
      "fsm_id": "ba_jyy3EVLFKkDIr52Ucs+QFDWdj0WZoHh8nUaLs/LNioBYM6C+"
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
      "fsm_id": "ba_lPK9Fxx42pVAQOejB3524tVQ1lWVZMGBiO+hDc2q/GBPubZf"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBp82U+yo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422210,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEDLtBC8eXxeecFL83YnLOFNUg6ozw5ve83m/2Ek9ld7w2kn3PjVbVZF/00/IaJUEdoIGKUb8S9epvwZtmWeB3IHuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgadPwOpL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422210,
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "fsm_id": "ba_lPK9Fxx42pVAQOejB3524tVQ1lWVZMGBiO+hDc2q/GBPubZf",
      "signed_tx": "tx_+MwLAfhCuEDLtBC8eXxeecFL83YnLOFNUg6ozw5ve83m/2Ek9ld7w2kn3PjVbVZF/00/IaJUEdoIGKUb8S9epvwZtmWeB3IHuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgadPwOpL",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422209,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAec4Q0RhVS4aWB/MPbzX4wbJmVUoCutaOhIw4IW2+Z8COwNQeJCBFcQaL4h+hpraqYTB0oD25NabCJmXlMso0CbhAy7QQvHl8XnnBS/N2JyzhTVIOqM8Ob3vN5v9hJPZXe8NpJ9z41W1WRf9NPyGiVBHaCBilG/EvXqb8GbZlngdyB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GnLG3q3Q=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
  "id": -576460752303422209,
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAec4Q0RhVS4aWB/MPbzX4wbJmVUoCutaOhIw4IW2+Z8COwNQeJCBFcQaL4h+hpraqYTB0oD25NabCJmXlMso0CbhAy7QQvHl8XnnBS/N2JyzhTVIOqM8Ob3vN5v9hJPZXe8NpJ9z41W1WRf9NPyGiVBHaCBilG/EvXqb8GbZlngdyB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GnLG3q3Q==",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_jyy3EVLFKkDIr52Ucs+QFDWdj0WZoHh8nUaLs/LNioBYM6C+"
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAec4Q0RhVS4aWB/MPbzX4wbJmVUoCutaOhIw4IW2+Z8COwNQeJCBFcQaL4h+hpraqYTB0oD25NabCJmXlMso0CbhAy7QQvHl8XnnBS/N2JyzhTVIOqM8Ob3vN5v9hJPZXe8NpJ9z41W1WRf9NPyGiVBHaCBilG/EvXqb8GbZlngdyB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GnLG3q3Q==",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAec4Q0RhVS4aWB/MPbzX4wbJmVUoCutaOhIw4IW2+Z8COwNQeJCBFcQaL4h+hpraqYTB0oD25NabCJmXlMso0CbhAy7QQvHl8XnnBS/N2JyzhTVIOqM8Ob3vN5v9hJPZXe8NpJ9z41W1WRf9NPyGiVBHaCBilG/EvXqb8GbZlngdyB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GnLG3q3Q==",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAec4Q0RhVS4aWB/MPbzX4wbJmVUoCutaOhIw4IW2+Z8COwNQeJCBFcQaL4h+hpraqYTB0oD25NabCJmXlMso0CbhAy7QQvHl8XnnBS/N2JyzhTVIOqM8Ob3vN5v9hJPZXe8NpJ9z41W1WRf9NPyGiVBHaCBilG/EvXqb8GbZlngdyB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GnLG3q3Q==",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
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
    "channel_id": "ch_BvnappDHvtHNqgWsW2enUk5zkWjxwUDtb37bLGn9s4DnkM8Pd",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "message": {
        "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "message": {
        "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
  "id": -576460752303422208,
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
  "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
  "id": -576460752303422208,
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "state": "tx_+QEOCwH4hLhAec4Q0RhVS4aWB/MPbzX4wbJmVUoCutaOhIw4IW2+Z8COwNQeJCBFcQaL4h+hpraqYTB0oD25NabCJmXlMso0CbhAy7QQvHl8XnnBS/N2JyzhTVIOqM8Ob3vN5v9hJPZXe8NpJ9z41W1WRf9NPyGiVBHaCBilG/EvXqb8GbZlngdyB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GnLG3q3Q=="
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "state": "tx_+QEOCwH4hLhAec4Q0RhVS4aWB/MPbzX4wbJmVUoCutaOhIw4IW2+Z8COwNQeJCBFcQaL4h+hpraqYTB0oD25NabCJmXlMso0CbhAy7QQvHl8XnnBS/N2JyzhTVIOqM8Ob3vN5v9hJPZXe8NpJ9z41W1WRf9NPyGiVBHaCBilG/EvXqb8GbZlngdyB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GnLG3q3Q=="
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
  "params": {
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "signed_tx": "tx_+GcLAcC4YvhgNQGhBq8j77VwLa13whncU0SIPPxyeym6kXtyDO6L+VJ1OtiqoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY3872/H/+GHKrSZ0ABAIYPbM7GgACDEtaHDKtEug==",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBq8j77VwLa13whncU0SIPPxyeym6kXtyDO6L+VJ1OtiqoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBqNFl6Gg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422207,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEBd5REPt3Th0Ok3BgyHbPu8SGaaPtJ+Snxsdse6utKDuFmEge9N228U//jZ+bPtADevNEgU6cZJgqLwsnaaWl0LuGD4XjUBoQavI++1cC2td8IZ3FNEiDz8cnspupF7cgzui/lSdTrYqqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgahjw8/e"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
  "id": -576460752303422207,
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEBd5REPt3Th0Ok3BgyHbPu8SGaaPtJ+Snxsdse6utKDuFmEge9N228U//jZ+bPtADevNEgU6cZJgqLwsnaaWl0LuGD4XjUBoQavI++1cC2td8IZ3FNEiDz8cnspupF7cgzui/lSdTrYqqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgahjw8/e",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422206,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEBd5REPt3Th0Ok3BgyHbPu8SGaaPtJ+Snxsdse6utKDuFmEge9N228U//jZ+bPtADevNEgU6cZJgqLwsnaaWl0LuEB7d3ZK2I7RBm4FgErau3SzlmkSeqieMfc3PU5ufDsNpamdCkphbWCdqgaFDBgnRTxOVSB8r+c83a6z89efA+MJuGD4XjUBoQavI++1cC2td8IZ3FNEiDz8cnspupF7cgzui/lSdTrYqqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgag0HMFT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
  "id": -576460752303422206,
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEBd5REPt3Th0Ok3BgyHbPu8SGaaPtJ+Snxsdse6utKDuFmEge9N228U//jZ+bPtADevNEgU6cZJgqLwsnaaWl0LuEB7d3ZK2I7RBm4FgErau3SzlmkSeqieMfc3PU5ufDsNpamdCkphbWCdqgaFDBgnRTxOVSB8r+c83a6z89efA+MJuGD4XjUBoQavI++1cC2td8IZ3FNEiDz8cnspupF7cgzui/lSdTrYqqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgag0HMFT",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEBd5REPt3Th0Ok3BgyHbPu8SGaaPtJ+Snxsdse6utKDuFmEge9N228U//jZ+bPtADevNEgU6cZJgqLwsnaaWl0LuEB7d3ZK2I7RBm4FgErau3SzlmkSeqieMfc3PU5ufDsNpamdCkphbWCdqgaFDBgnRTxOVSB8r+c83a6z89efA+MJuGD4XjUBoQavI++1cC2td8IZ3FNEiDz8cnspupF7cgzui/lSdTrYqqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgag0HMFT",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEBd5REPt3Th0Ok3BgyHbPu8SGaaPtJ+Snxsdse6utKDuFmEge9N228U//jZ+bPtADevNEgU6cZJgqLwsnaaWl0LuEB7d3ZK2I7RBm4FgErau3SzlmkSeqieMfc3PU5ufDsNpamdCkphbWCdqgaFDBgnRTxOVSB8r+c83a6z89efA+MJuGD4XjUBoQavI++1cC2td8IZ3FNEiDz8cnspupF7cgzui/lSdTrYqqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgag0HMFT",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEBd5REPt3Th0Ok3BgyHbPu8SGaaPtJ+Snxsdse6utKDuFmEge9N228U//jZ+bPtADevNEgU6cZJgqLwsnaaWl0LuEB7d3ZK2I7RBm4FgErau3SzlmkSeqieMfc3PU5ufDsNpamdCkphbWCdqgaFDBgnRTxOVSB8r+c83a6z89efA+MJuGD4XjUBoQavI++1cC2td8IZ3FNEiDz8cnspupF7cgzui/lSdTrYqqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgag0HMFT",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
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
    "channel_id": "ch_2L8j6mVQY4pA896teBDTMzPWmntvMLGt9qUg8KAXqhaiiWyLmD",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
