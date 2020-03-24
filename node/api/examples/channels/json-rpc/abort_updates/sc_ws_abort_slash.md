
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
      "fsm_id": "ba_JboFJ2ueF3CcT2gIJxRbYQFscZv7kE4GzX5JwE5vj6+Ft80j"
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
      "fsm_id": "ba_bi42q0x/75a65T/+bH0dMczlte4T/DjUzTr+pe7elbySVnRV"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBvMBJY0o=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422080,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEDGx7emAGavVo6BG1iQALQ4O4HFFwXxfpeBnrOUHDmVJGw2G4FexVJ5/omCBISPFT6Pud221I/moGsUqacut2AAuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbyhT9tW"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422080,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "fsm_id": "ba_bi42q0x/75a65T/+bH0dMczlte4T/DjUzTr+pe7elbySVnRV",
      "signed_tx": "tx_+MwLAfhCuEDGx7emAGavVo6BG1iQALQ4O4HFFwXxfpeBnrOUHDmVJGw2G4FexVJ5/omCBISPFT6Pud221I/moGsUqacut2AAuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbyhT9tW",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422079,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAvuM4iPwAbkR9W+dL6VdN5CXzaLDPn6m9BoNPWBv35l4G5384YNoZuoWvgp3kUc3xJ8YJUqXJmfEDO4zViZL2BbhAxse3pgBmr1aOgRtYkAC0ODuBxRcF8X6XgZ6zlBw5lSRsNhuBXsVSef6JggSEjxU+j7ndttSP5qBrFKmnLrdgALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G8YaYd3w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422079,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAvuM4iPwAbkR9W+dL6VdN5CXzaLDPn6m9BoNPWBv35l4G5384YNoZuoWvgp3kUc3xJ8YJUqXJmfEDO4zViZL2BbhAxse3pgBmr1aOgRtYkAC0ODuBxRcF8X6XgZ6zlBw5lSRsNhuBXsVSef6JggSEjxU+j7ndttSP5qBrFKmnLrdgALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G8YaYd3w==",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_JboFJ2ueF3CcT2gIJxRbYQFscZv7kE4GzX5JwE5vj6+Ft80j"
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAvuM4iPwAbkR9W+dL6VdN5CXzaLDPn6m9BoNPWBv35l4G5384YNoZuoWvgp3kUc3xJ8YJUqXJmfEDO4zViZL2BbhAxse3pgBmr1aOgRtYkAC0ODuBxRcF8X6XgZ6zlBw5lSRsNhuBXsVSef6JggSEjxU+j7ndttSP5qBrFKmnLrdgALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G8YaYd3w==",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAvuM4iPwAbkR9W+dL6VdN5CXzaLDPn6m9BoNPWBv35l4G5384YNoZuoWvgp3kUc3xJ8YJUqXJmfEDO4zViZL2BbhAxse3pgBmr1aOgRtYkAC0ODuBxRcF8X6XgZ6zlBw5lSRsNhuBXsVSef6JggSEjxU+j7ndttSP5qBrFKmnLrdgALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G8YaYd3w==",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAvuM4iPwAbkR9W+dL6VdN5CXzaLDPn6m9BoNPWBv35l4G5384YNoZuoWvgp3kUc3xJ8YJUqXJmfEDO4zViZL2BbhAxse3pgBmr1aOgRtYkAC0ODuBxRcF8X6XgZ6zlBw5lSRsNhuBXsVSef6JggSEjxU+j7ndttSP5qBrFKmnLrdgALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G8YaYd3w==",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "message": {
        "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "message": {
        "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
  "id": -576460752303422078,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422078,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+QEOCwH4hLhAvuM4iPwAbkR9W+dL6VdN5CXzaLDPn6m9BoNPWBv35l4G5384YNoZuoWvgp3kUc3xJ8YJUqXJmfEDO4zViZL2BbhAxse3pgBmr1aOgRtYkAC0ODuBxRcF8X6XgZ6zlBw5lSRsNhuBXsVSef6JggSEjxU+j7ndttSP5qBrFKmnLrdgALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G8YaYd3w=="
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+QEOCwH4hLhAvuM4iPwAbkR9W+dL6VdN5CXzaLDPn6m9BoNPWBv35l4G5384YNoZuoWvgp3kUc3xJ8YJUqXJmfEDO4zViZL2BbhAxse3pgBmr1aOgRtYkAC0ODuBxRcF8X6XgZ6zlBw5lSRsNhuBXsVSef6JggSEjxU+j7ndttSP5qBrFKmnLrdgALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G8YaYd3w=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422077,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422077,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoxuzzQsxmvj92xmJEGSUCsfwwAmjZtNRFKAdjv7Q+yZAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAtI1Tmg=",
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
  "id": -576460752303422076,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDou9er9MXctESRYydTWVkub/IbGvtiRlvIR3DZHaugawhOZjzYktnQ9KiOTK4pv+z7dvR6s8FSYYEr8K510yMPuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKZ4KJB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422076,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDou9er9MXctESRYydTWVkub/IbGvtiRlvIR3DZHaugawhOZjzYktnQ9KiOTK4pv+z7dvR6s8FSYYEr8K510yMPuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKZ4KJB",
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
  "id": -576460752303422075,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDBh2N2yD/lLEdCYFLhFu4BBIiaeS+uGFiYSpj+LnXNjj4mz2RrzfqB/va21CnCUusaadBoNnAFNE2HmR80ggkCuEDou9er9MXctESRYydTWVkub/IbGvtiRlvIR3DZHaugawhOZjzYktnQ9KiOTK4pv+z7dvR6s8FSYYEr8K510yMPuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI5JMh3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422075,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+NILAfiEuEDBh2N2yD/lLEdCYFLhFu4BBIiaeS+uGFiYSpj+LnXNjj4mz2RrzfqB/va21CnCUusaadBoNnAFNE2HmR80ggkCuEDou9er9MXctESRYydTWVkub/IbGvtiRlvIR3DZHaugawhOZjzYktnQ9KiOTK4pv+z7dvR6s8FSYYEr8K510yMPuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI5JMh3"
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+NILAfiEuEDBh2N2yD/lLEdCYFLhFu4BBIiaeS+uGFiYSpj+LnXNjj4mz2RrzfqB/va21CnCUusaadBoNnAFNE2HmR80ggkCuEDou9er9MXctESRYydTWVkub/IbGvtiRlvIR3DZHaugawhOZjzYktnQ9KiOTK4pv+z7dvR6s8FSYYEr8K510yMPuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI5JMh3"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422074,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422074,
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
  "id": -576460752303422073,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422073,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDBh2N2yD/lLEdCYFLhFu4BBIiaeS+uGFiYSpj+LnXNjj4mz2RrzfqB/va21CnCUusaadBoNnAFNE2HmR80ggkCuEDou9er9MXctESRYydTWVkub/IbGvtiRlvIR3DZHaugawhOZjzYktnQ9KiOTK4pv+z7dvR6s8FSYYEr8K510yMPuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI5JMh3",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422072,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422072,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoxuzzQsxmvj92xmJEGSUCsfwwAmjZtNRFKAdjv7Q+yZA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC6qmU0E=",
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
  "id": -576460752303422071,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC5ERJARd4UIFSRq23sQXr85ogaf8KJkKDyqH8ab3z6TDuD2FpTGBphOHuMmHgMKo+A0EJZ9mYvHIY6eMFH/AABuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguHl8wT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422071,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC5ERJARd4UIFSRq23sQXr85ogaf8KJkKDyqH8ab3z6TDuD2FpTGBphOHuMmHgMKo+A0EJZ9mYvHIY6eMFH/AABuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguHl8wT",
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
  "id": -576460752303422070,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA/xJwYzrXm9m8aA7EsUUuKrbFmkubbgOHKTOJhsEnkrgRMJ8mT8F7QfJIrzu1EgaPuz6FQJBptZJyQyASLofcOuEC5ERJARd4UIFSRq23sQXr85ogaf8KJkKDyqH8ab3z6TDuD2FpTGBphOHuMmHgMKo+A0EJZ9mYvHIY6eMFH/AABuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtLoTXY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422070,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+NILAfiEuEA/xJwYzrXm9m8aA7EsUUuKrbFmkubbgOHKTOJhsEnkrgRMJ8mT8F7QfJIrzu1EgaPuz6FQJBptZJyQyASLofcOuEC5ERJARd4UIFSRq23sQXr85ogaf8KJkKDyqH8ab3z6TDuD2FpTGBphOHuMmHgMKo+A0EJZ9mYvHIY6eMFH/AABuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtLoTXY"
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+NILAfiEuEA/xJwYzrXm9m8aA7EsUUuKrbFmkubbgOHKTOJhsEnkrgRMJ8mT8F7QfJIrzu1EgaPuz6FQJBptZJyQyASLofcOuEC5ERJARd4UIFSRq23sQXr85ogaf8KJkKDyqH8ab3z6TDuD2FpTGBphOHuMmHgMKo+A0EJZ9mYvHIY6eMFH/AABuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtLoTXY"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422069,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422069,
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
  "id": -576460752303422068,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422068,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA/xJwYzrXm9m8aA7EsUUuKrbFmkubbgOHKTOJhsEnkrgRMJ8mT8F7QfJIrzu1EgaPuz6FQJBptZJyQyASLofcOuEC5ERJARd4UIFSRq23sQXr85ogaf8KJkKDyqH8ab3z6TDuD2FpTGBphOHuMmHgMKo+A0EJZ9mYvHIY6eMFH/AABuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtLoTXY",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422067,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422067,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA/xJwYzrXm9m8aA7EsUUuKrbFmkubbgOHKTOJhsEnkrgRMJ8mT8F7QfJIrzu1EgaPuz6FQJBptZJyQyASLofcOuEC5ERJARd4UIFSRq23sQXr85ogaf8KJkKDyqH8ab3z6TDuD2FpTGBphOHuMmHgMKo+A0EJZ9mYvHIY6eMFH/AABuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtLoTXY",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422066,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422066,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoxuzzQsxmvj92xmJEGSUCsfwwAmjZtNRFKAdjv7Q+yZBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAmklY6o=",
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
  "id": -576460752303422065,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBhtjtvY+moNt56JBpjIl893OZCpdzrZ/MBzkJWP8sATZkYdbZM8Ho2J7a8XQretSddUj/1mKDmvfFawP4od6YGuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLFHaR+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422065,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBhtjtvY+moNt56JBpjIl893OZCpdzrZ/MBzkJWP8sATZkYdbZM8Ho2J7a8XQretSddUj/1mKDmvfFawP4od6YGuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLFHaR+",
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
  "id": -576460752303422064,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBhtjtvY+moNt56JBpjIl893OZCpdzrZ/MBzkJWP8sATZkYdbZM8Ho2J7a8XQretSddUj/1mKDmvfFawP4od6YGuECu2RusVr6WILO5Y9FvGafzQjnEKDqh+h7AAN+y9P8UG40xFaHwCc8lpK354QxnSvcqwCLeTaHDZvKamQt+GYwKuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIrS2Py"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422064,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+NILAfiEuEBhtjtvY+moNt56JBpjIl893OZCpdzrZ/MBzkJWP8sATZkYdbZM8Ho2J7a8XQretSddUj/1mKDmvfFawP4od6YGuECu2RusVr6WILO5Y9FvGafzQjnEKDqh+h7AAN+y9P8UG40xFaHwCc8lpK354QxnSvcqwCLeTaHDZvKamQt+GYwKuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIrS2Py"
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+NILAfiEuEBhtjtvY+moNt56JBpjIl893OZCpdzrZ/MBzkJWP8sATZkYdbZM8Ho2J7a8XQretSddUj/1mKDmvfFawP4od6YGuECu2RusVr6WILO5Y9FvGafzQjnEKDqh+h7AAN+y9P8UG40xFaHwCc8lpK354QxnSvcqwCLeTaHDZvKamQt+GYwKuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIrS2Py"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422063,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422063,
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
  "id": -576460752303422062,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422062,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBhtjtvY+moNt56JBpjIl893OZCpdzrZ/MBzkJWP8sATZkYdbZM8Ho2J7a8XQretSddUj/1mKDmvfFawP4od6YGuECu2RusVr6WILO5Y9FvGafzQjnEKDqh+h7AAN+y9P8UG40xFaHwCc8lpK354QxnSvcqwCLeTaHDZvKamQt+GYwKuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIrS2Py",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422061,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422061,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoxuzzQsxmvj92xmJEGSUCsfwwAmjZtNRFKAdjv7Q+yZBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC48euX8=",
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
  "id": -576460752303422060,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECrDE7YUJ/d4R+qLG3yWsCNwYoeSU6jpBHUyalZG+Hzd/aMQqC5vanWnLD+/6xvxjHBm0HHRLSBBUrKwgdLrZIOuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvf/Eid"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422060,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "signed_tx": "tx_+JALAfhCuECrDE7YUJ/d4R+qLG3yWsCNwYoeSU6jpBHUyalZG+Hzd/aMQqC5vanWnLD+/6xvxjHBm0HHRLSBBUrKwgdLrZIOuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvf/Eid",
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
  "id": -576460752303422059,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECrDE7YUJ/d4R+qLG3yWsCNwYoeSU6jpBHUyalZG+Hzd/aMQqC5vanWnLD+/6xvxjHBm0HHRLSBBUrKwgdLrZIOuEDq1tWFL5iWjktMqeP4LDUWJxgjZi5686IrAP6cxccBiqO/1+ep18op1otMTQ/+G1KRQEMaLrMJAKfi3vbsJ10IuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtFu+BX"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422059,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+NILAfiEuECrDE7YUJ/d4R+qLG3yWsCNwYoeSU6jpBHUyalZG+Hzd/aMQqC5vanWnLD+/6xvxjHBm0HHRLSBBUrKwgdLrZIOuEDq1tWFL5iWjktMqeP4LDUWJxgjZi5686IrAP6cxccBiqO/1+ep18op1otMTQ/+G1KRQEMaLrMJAKfi3vbsJ10IuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtFu+BX"
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "state": "tx_+NILAfiEuECrDE7YUJ/d4R+qLG3yWsCNwYoeSU6jpBHUyalZG+Hzd/aMQqC5vanWnLD+/6xvxjHBm0HHRLSBBUrKwgdLrZIOuEDq1tWFL5iWjktMqeP4LDUWJxgjZi5686IrAP6cxccBiqO/1+ep18op1otMTQ/+G1KRQEMaLrMJAKfi3vbsJ10IuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtFu+BX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422058,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422058,
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
  "id": -576460752303422057,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422057,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECrDE7YUJ/d4R+qLG3yWsCNwYoeSU6jpBHUyalZG+Hzd/aMQqC5vanWnLD+/6xvxjHBm0HHRLSBBUrKwgdLrZIOuEDq1tWFL5iWjktMqeP4LDUWJxgjZi5686IrAP6cxccBiqO/1+ep18op1otMTQ/+G1KRQEMaLrMJAKfi3vbsJ10IuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtFu+BX",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECrDE7YUJ/d4R+qLG3yWsCNwYoeSU6jpBHUyalZG+Hzd/aMQqC5vanWnLD+/6xvxjHBm0HHRLSBBUrKwgdLrZIOuEDq1tWFL5iWjktMqeP4LDUWJxgjZi5686IrAP6cxccBiqO/1+ep18op1otMTQ/+G1KRQEMaLrMJAKfi3vbsJ10IuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtFu+BX",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECrDE7YUJ/d4R+qLG3yWsCNwYoeSU6jpBHUyalZG+Hzd/aMQqC5vanWnLD+/6xvxjHBm0HHRLSBBUrKwgdLrZIOuEDq1tWFL5iWjktMqeP4LDUWJxgjZi5686IrAP6cxccBiqO/1+ep18op1otMTQ/+G1KRQEMaLrMJAKfi3vbsJ10IuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtFu+BX",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBoxuzzQsxmvj92xmJEGSUCsfwwAmjZtNRFKAdjv7Q+yZoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuECrDE7YUJ/d4R+qLG3yWsCNwYoeSU6jpBHUyalZG+Hzd/aMQqC5vanWnLD+/6xvxjHBm0HHRLSBBUrKwgdLrZIOuEDq1tWFL5iWjktMqeP4LDUWJxgjZi5686IrAP6cxccBiqO/1+ep18op1otMTQ/+G1KRQEMaLrMJAKfi3vbsJ10IuEj4RjkCoQaMbs80LMZr4/dsZiRBklArH8MAJo2bTURSgHY7+0PsmQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGSNwYbAAgb57Cpa0",
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
  "method": "channels.slash_sign",
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
  "id": -576460752303422056,
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422056,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422055,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
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
  "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
  "id": -576460752303422055,
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
    "channel_id": "ch_24rAnLvdECymahJC1Zk6jWBrd5Fv2r4UKQz797gkewiSGvQ8xw",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

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
      "fsm_id": "ba_YPt0PSfucyt5uFXpsHemFm7XM4feSeDGA0DRDEgMs+diajc/"
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
      "fsm_id": "ba_Jp6SbwU7ipLNaHDzPkXfHhE49okQYE2gPuQA3hITjMItPSJ5"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBvhxFdqo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422054,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBSj1yoJ0YwEs4GXrIBtyJupPXsT5vCCAO16XIFl4Z44qQpyv66eun3Mq40MV2aJvW0sRQqQXA2EQl4KfNH/V0LuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lgb4Z/9Ql"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422054,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "fsm_id": "ba_Jp6SbwU7ipLNaHDzPkXfHhE49okQYE2gPuQA3hITjMItPSJ5",
      "signed_tx": "tx_+MwLAfhCuEBSj1yoJ0YwEs4GXrIBtyJupPXsT5vCCAO16XIFl4Z44qQpyv66eun3Mq40MV2aJvW0sRQqQXA2EQl4KfNH/V0LuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lgb4Z/9Ql",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422053,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAUo9cqCdGMBLOBl6yAbcibqT17E+bwggDtelyBZeGeOKkKcr+unrp9zKuNDFdmib1tLEUKkFwNhEJeCnzR/1dC7hAygkdBlTproNA8Na8IV94jyT/CWZYx5zpCTXJc1i5wCnXgckcJp9oOoCjLO+kNfZR6M2QNYYmIfcFYrtIwreCCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G+yzwPxA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422053,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAUo9cqCdGMBLOBl6yAbcibqT17E+bwggDtelyBZeGeOKkKcr+unrp9zKuNDFdmib1tLEUKkFwNhEJeCnzR/1dC7hAygkdBlTproNA8Na8IV94jyT/CWZYx5zpCTXJc1i5wCnXgckcJp9oOoCjLO+kNfZR6M2QNYYmIfcFYrtIwreCCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G+yzwPxA==",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_YPt0PSfucyt5uFXpsHemFm7XM4feSeDGA0DRDEgMs+diajc/"
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAUo9cqCdGMBLOBl6yAbcibqT17E+bwggDtelyBZeGeOKkKcr+unrp9zKuNDFdmib1tLEUKkFwNhEJeCnzR/1dC7hAygkdBlTproNA8Na8IV94jyT/CWZYx5zpCTXJc1i5wCnXgckcJp9oOoCjLO+kNfZR6M2QNYYmIfcFYrtIwreCCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G+yzwPxA==",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAUo9cqCdGMBLOBl6yAbcibqT17E+bwggDtelyBZeGeOKkKcr+unrp9zKuNDFdmib1tLEUKkFwNhEJeCnzR/1dC7hAygkdBlTproNA8Na8IV94jyT/CWZYx5zpCTXJc1i5wCnXgckcJp9oOoCjLO+kNfZR6M2QNYYmIfcFYrtIwreCCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G+yzwPxA==",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAUo9cqCdGMBLOBl6yAbcibqT17E+bwggDtelyBZeGeOKkKcr+unrp9zKuNDFdmib1tLEUKkFwNhEJeCnzR/1dC7hAygkdBlTproNA8Na8IV94jyT/CWZYx5zpCTXJc1i5wCnXgckcJp9oOoCjLO+kNfZR6M2QNYYmIfcFYrtIwreCCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G+yzwPxA==",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "message": {
        "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "message": {
        "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
  "id": -576460752303422052,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422052,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+QEOCwH4hLhAUo9cqCdGMBLOBl6yAbcibqT17E+bwggDtelyBZeGeOKkKcr+unrp9zKuNDFdmib1tLEUKkFwNhEJeCnzR/1dC7hAygkdBlTproNA8Na8IV94jyT/CWZYx5zpCTXJc1i5wCnXgckcJp9oOoCjLO+kNfZR6M2QNYYmIfcFYrtIwreCCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G+yzwPxA=="
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+QEOCwH4hLhAUo9cqCdGMBLOBl6yAbcibqT17E+bwggDtelyBZeGeOKkKcr+unrp9zKuNDFdmib1tLEUKkFwNhEJeCnzR/1dC7hAygkdBlTproNA8Na8IV94jyT/CWZYx5zpCTXJc1i5wCnXgckcJp9oOoCjLO+kNfZR6M2QNYYmIfcFYrtIwreCCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G+yzwPxA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422051,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422051,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoM749ObLQCqk+WB3s9SbW8J4h3wpY8YjsfQZIC45wXgAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAu4dN1k=",
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
  "id": -576460752303422050,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECPqBvzuDYV9qLrd1wuw1OUt/AGcM+hL4ygnKqosEaL5qz2QtKAoaaISJ/YG/yNuqIXyd4tz265gTx4h8VewqoJuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLEDR+z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422050,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "signed_tx": "tx_+JALAfhCuECPqBvzuDYV9qLrd1wuw1OUt/AGcM+hL4ygnKqosEaL5qz2QtKAoaaISJ/YG/yNuqIXyd4tz265gTx4h8VewqoJuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLEDR+z",
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
  "id": -576460752303422049,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECPqBvzuDYV9qLrd1wuw1OUt/AGcM+hL4ygnKqosEaL5qz2QtKAoaaISJ/YG/yNuqIXyd4tz265gTx4h8VewqoJuEDy9OSMohd9KzuGxtsrKcFgSteoW3KvyZMaHJ++KHmxrwpupXy+onzJfM/DiMxeXznc7jsMCKGwqdBrBDUxLS4DuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJdY343"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422049,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+NILAfiEuECPqBvzuDYV9qLrd1wuw1OUt/AGcM+hL4ygnKqosEaL5qz2QtKAoaaISJ/YG/yNuqIXyd4tz265gTx4h8VewqoJuEDy9OSMohd9KzuGxtsrKcFgSteoW3KvyZMaHJ++KHmxrwpupXy+onzJfM/DiMxeXznc7jsMCKGwqdBrBDUxLS4DuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJdY343"
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+NILAfiEuECPqBvzuDYV9qLrd1wuw1OUt/AGcM+hL4ygnKqosEaL5qz2QtKAoaaISJ/YG/yNuqIXyd4tz265gTx4h8VewqoJuEDy9OSMohd9KzuGxtsrKcFgSteoW3KvyZMaHJ++KHmxrwpupXy+onzJfM/DiMxeXznc7jsMCKGwqdBrBDUxLS4DuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJdY343"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422048,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422048,
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
  "id": -576460752303422047,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422047,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECPqBvzuDYV9qLrd1wuw1OUt/AGcM+hL4ygnKqosEaL5qz2QtKAoaaISJ/YG/yNuqIXyd4tz265gTx4h8VewqoJuEDy9OSMohd9KzuGxtsrKcFgSteoW3KvyZMaHJ++KHmxrwpupXy+onzJfM/DiMxeXznc7jsMCKGwqdBrBDUxLS4DuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJdY343",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422046,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422046,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoM749ObLQCqk+WB3s9SbW8J4h3wpY8YjsfQZIC45wXgA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzgMFjA=",
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
  "id": -576460752303422045,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDvw/QRAok3oFwrNMLNlQ/XvRHTjzOhU2rVPVkkWgnucpkjBZb9Samu6ioFdLLSd/kxgd8qTUv3FchfBEtsUT0AuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgugIWdX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422045,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDvw/QRAok3oFwrNMLNlQ/XvRHTjzOhU2rVPVkkWgnucpkjBZb9Samu6ioFdLLSd/kxgd8qTUv3FchfBEtsUT0AuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgugIWdX",
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
  "id": -576460752303422044,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDK2ZxI0z8NEosoHEUZ/1wj8YigqYGBjEeFAVg+YrDR4pucNpuPQwoFBBRt2bWjaJ3VP1OxW+NKpa2s9N1vulsKuEDvw/QRAok3oFwrNMLNlQ/XvRHTjzOhU2rVPVkkWgnucpkjBZb9Samu6ioFdLLSd/kxgd8qTUv3FchfBEtsUT0AuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu7Mgs2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422044,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+NILAfiEuEDK2ZxI0z8NEosoHEUZ/1wj8YigqYGBjEeFAVg+YrDR4pucNpuPQwoFBBRt2bWjaJ3VP1OxW+NKpa2s9N1vulsKuEDvw/QRAok3oFwrNMLNlQ/XvRHTjzOhU2rVPVkkWgnucpkjBZb9Samu6ioFdLLSd/kxgd8qTUv3FchfBEtsUT0AuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu7Mgs2"
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+NILAfiEuEDK2ZxI0z8NEosoHEUZ/1wj8YigqYGBjEeFAVg+YrDR4pucNpuPQwoFBBRt2bWjaJ3VP1OxW+NKpa2s9N1vulsKuEDvw/QRAok3oFwrNMLNlQ/XvRHTjzOhU2rVPVkkWgnucpkjBZb9Samu6ioFdLLSd/kxgd8qTUv3FchfBEtsUT0AuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu7Mgs2"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422043,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422043,
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
  "id": -576460752303422042,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422042,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDK2ZxI0z8NEosoHEUZ/1wj8YigqYGBjEeFAVg+YrDR4pucNpuPQwoFBBRt2bWjaJ3VP1OxW+NKpa2s9N1vulsKuEDvw/QRAok3oFwrNMLNlQ/XvRHTjzOhU2rVPVkkWgnucpkjBZb9Samu6ioFdLLSd/kxgd8qTUv3FchfBEtsUT0AuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu7Mgs2",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422041,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422041,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDK2ZxI0z8NEosoHEUZ/1wj8YigqYGBjEeFAVg+YrDR4pucNpuPQwoFBBRt2bWjaJ3VP1OxW+NKpa2s9N1vulsKuEDvw/QRAok3oFwrNMLNlQ/XvRHTjzOhU2rVPVkkWgnucpkjBZb9Samu6ioFdLLSd/kxgd8qTUv3FchfBEtsUT0AuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu7Mgs2",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422040,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422040,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoM749ObLQCqk+WB3s9SbW8J4h3wpY8YjsfQZIC45wXgBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAtTMa6s=",
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
  "id": -576460752303422039,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED4nsNwW3kYCRMmDDi9CRMXZlq5XPKFc+hJtIIdUN8P7bOvfgl3ydtguwT8nS04UnNBsByiGv0QXX1Hkwow4B8BuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4ASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJmDjov"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422039,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "signed_tx": "tx_+JALAfhCuED4nsNwW3kYCRMmDDi9CRMXZlq5XPKFc+hJtIIdUN8P7bOvfgl3ydtguwT8nS04UnNBsByiGv0QXX1Hkwow4B8BuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4ASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJmDjov",
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
  "id": -576460752303422038,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEArCmhg558XS+e4tnuAN/PuqyolilrOCmo7MQGSKB5Oxw3qNslJSRNnXuaZP0SfrJjOFV65Cjp6WW9nbf/GNQ8NuED4nsNwW3kYCRMmDDi9CRMXZlq5XPKFc+hJtIIdUN8P7bOvfgl3ydtguwT8nS04UnNBsByiGv0QXX1Hkwow4B8BuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4ASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgInS+vW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422038,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+NILAfiEuEArCmhg558XS+e4tnuAN/PuqyolilrOCmo7MQGSKB5Oxw3qNslJSRNnXuaZP0SfrJjOFV65Cjp6WW9nbf/GNQ8NuED4nsNwW3kYCRMmDDi9CRMXZlq5XPKFc+hJtIIdUN8P7bOvfgl3ydtguwT8nS04UnNBsByiGv0QXX1Hkwow4B8BuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4ASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgInS+vW"
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+NILAfiEuEArCmhg558XS+e4tnuAN/PuqyolilrOCmo7MQGSKB5Oxw3qNslJSRNnXuaZP0SfrJjOFV65Cjp6WW9nbf/GNQ8NuED4nsNwW3kYCRMmDDi9CRMXZlq5XPKFc+hJtIIdUN8P7bOvfgl3ydtguwT8nS04UnNBsByiGv0QXX1Hkwow4B8BuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4ASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgInS+vW"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422037,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422037,
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
  "id": -576460752303422036,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422036,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEArCmhg558XS+e4tnuAN/PuqyolilrOCmo7MQGSKB5Oxw3qNslJSRNnXuaZP0SfrJjOFV65Cjp6WW9nbf/GNQ8NuED4nsNwW3kYCRMmDDi9CRMXZlq5XPKFc+hJtIIdUN8P7bOvfgl3ydtguwT8nS04UnNBsByiGv0QXX1Hkwow4B8BuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4ASgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgInS+vW",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422035,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422035,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoM749ObLQCqk+WB3s9SbW8J4h3wpY8YjsfQZIC45wXgBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0yVyA8=",
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
  "id": -576460752303422034,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECjRJ4o2yYx4Rj95iF61KK+gsnzwTyRWe0zwzNMvsdI9gDyLpEBlTFvE8/WwQ7Vf3rkCPizkK4F5iqijumsKA4GuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu+yg+y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422034,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "signed_tx": "tx_+JALAfhCuECjRJ4o2yYx4Rj95iF61KK+gsnzwTyRWe0zwzNMvsdI9gDyLpEBlTFvE8/WwQ7Vf3rkCPizkK4F5iqijumsKA4GuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu+yg+y",
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
  "id": -576460752303422033,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECb0Q2/whcR8y03pGgUy8EtVobQ6RqfbJsy6g/dN1vLC8yDS4ayo/V5Qg2Gu4eKaOBRD4/khmg9+hZT1ktWBFwPuECjRJ4o2yYx4Rj95iF61KK+gsnzwTyRWe0zwzNMvsdI9gDyLpEBlTFvE8/WwQ7Vf3rkCPizkK4F5iqijumsKA4GuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvJEoD4"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422033,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+NILAfiEuECb0Q2/whcR8y03pGgUy8EtVobQ6RqfbJsy6g/dN1vLC8yDS4ayo/V5Qg2Gu4eKaOBRD4/khmg9+hZT1ktWBFwPuECjRJ4o2yYx4Rj95iF61KK+gsnzwTyRWe0zwzNMvsdI9gDyLpEBlTFvE8/WwQ7Vf3rkCPizkK4F5iqijumsKA4GuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvJEoD4"
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "state": "tx_+NILAfiEuECb0Q2/whcR8y03pGgUy8EtVobQ6RqfbJsy6g/dN1vLC8yDS4ayo/V5Qg2Gu4eKaOBRD4/khmg9+hZT1ktWBFwPuECjRJ4o2yYx4Rj95iF61KK+gsnzwTyRWe0zwzNMvsdI9gDyLpEBlTFvE8/WwQ7Vf3rkCPizkK4F5iqijumsKA4GuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvJEoD4"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422032,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422032,
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
  "id": -576460752303422031,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422031,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECb0Q2/whcR8y03pGgUy8EtVobQ6RqfbJsy6g/dN1vLC8yDS4ayo/V5Qg2Gu4eKaOBRD4/khmg9+hZT1ktWBFwPuECjRJ4o2yYx4Rj95iF61KK+gsnzwTyRWe0zwzNMvsdI9gDyLpEBlTFvE8/WwQ7Vf3rkCPizkK4F5iqijumsKA4GuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvJEoD4",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECb0Q2/whcR8y03pGgUy8EtVobQ6RqfbJsy6g/dN1vLC8yDS4ayo/V5Qg2Gu4eKaOBRD4/khmg9+hZT1ktWBFwPuECjRJ4o2yYx4Rj95iF61KK+gsnzwTyRWe0zwzNMvsdI9gDyLpEBlTFvE8/WwQ7Vf3rkCPizkK4F5iqijumsKA4GuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvJEoD4",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECb0Q2/whcR8y03pGgUy8EtVobQ6RqfbJsy6g/dN1vLC8yDS4ayo/V5Qg2Gu4eKaOBRD4/khmg9+hZT1ktWBFwPuECjRJ4o2yYx4Rj95iF61KK+gsnzwTyRWe0zwzNMvsdI9gDyLpEBlTFvE8/WwQ7Vf3rkCPizkK4F5iqijumsKA4GuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvJEoD4",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBoM749ObLQCqk+WB3s9SbW8J4h3wpY8YjsfQZIC45wXgoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuECb0Q2/whcR8y03pGgUy8EtVobQ6RqfbJsy6g/dN1vLC8yDS4ayo/V5Qg2Gu4eKaOBRD4/khmg9+hZT1ktWBFwPuECjRJ4o2yYx4Rj95iF61KK+gsnzwTyRWe0zwzNMvsdI9gDyLpEBlTFvE8/WwQ7Vf3rkCPizkK4F5iqijumsKA4GuEj4RjkCoQaDO+PTmy0AqpPlgd7PUm1vCeId8KWPGI7H0GSAuOcF4AWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGR7ISegAQeLKR1U=",
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
  "method": "channels.slash_sign",
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
  "id": -576460752303422030,
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422030,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422029,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
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
  "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
  "id": -576460752303422029,
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
    "channel_id": "ch_zoCJxWj9qESPs2f1CzWRcXYw3TKXxYE2ZY2nVagKQEHUFM9Lu",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

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
      "fsm_id": "ba_O0bbzuOFl/z1bvWBkOgps8hEfXxk+oE9sN+EmWvdzjb98sTH"
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
      "fsm_id": "ba_aEa+stbStNTo4I78OTXQgRYLTp4TgDxBhQtSpQ8Rn9abjttk"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBwBNCE6o=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422028,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBMhBshjFhTBdLdz6sYfz5gVBTsyZOceUZAdQTpS81Lg7pgJL1XTIaps9JhWfcPlwg/V/wXuWvaKjsTtU2hyQQOuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgcD08e2V"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422028,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "fsm_id": "ba_aEa+stbStNTo4I78OTXQgRYLTp4TgDxBhQtSpQ8Rn9abjttk",
      "signed_tx": "tx_+MwLAfhCuEBMhBshjFhTBdLdz6sYfz5gVBTsyZOceUZAdQTpS81Lg7pgJL1XTIaps9JhWfcPlwg/V/wXuWvaKjsTtU2hyQQOuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgcD08e2V",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422027,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhATIQbIYxYUwXS3c+rGH8+YFQU7MmTnHlGQHUE6UvNS4O6YCS9V0yGqbPSYVn3D5cIP1f8F7lr2io7E7VNockEDrhAVKHaVteWtisVfq88viKq2UvCmaPRD3sT5+80CSuhRFyt8YhBHzJ5OjppQatbJHwJrWPRziFCUv+s2Txi/oRwDriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HAcxJcxw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422027,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhATIQbIYxYUwXS3c+rGH8+YFQU7MmTnHlGQHUE6UvNS4O6YCS9V0yGqbPSYVn3D5cIP1f8F7lr2io7E7VNockEDrhAVKHaVteWtisVfq88viKq2UvCmaPRD3sT5+80CSuhRFyt8YhBHzJ5OjppQatbJHwJrWPRziFCUv+s2Txi/oRwDriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HAcxJcxw==",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_O0bbzuOFl/z1bvWBkOgps8hEfXxk+oE9sN+EmWvdzjb98sTH"
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhATIQbIYxYUwXS3c+rGH8+YFQU7MmTnHlGQHUE6UvNS4O6YCS9V0yGqbPSYVn3D5cIP1f8F7lr2io7E7VNockEDrhAVKHaVteWtisVfq88viKq2UvCmaPRD3sT5+80CSuhRFyt8YhBHzJ5OjppQatbJHwJrWPRziFCUv+s2Txi/oRwDriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HAcxJcxw==",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhATIQbIYxYUwXS3c+rGH8+YFQU7MmTnHlGQHUE6UvNS4O6YCS9V0yGqbPSYVn3D5cIP1f8F7lr2io7E7VNockEDrhAVKHaVteWtisVfq88viKq2UvCmaPRD3sT5+80CSuhRFyt8YhBHzJ5OjppQatbJHwJrWPRziFCUv+s2Txi/oRwDriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HAcxJcxw==",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhATIQbIYxYUwXS3c+rGH8+YFQU7MmTnHlGQHUE6UvNS4O6YCS9V0yGqbPSYVn3D5cIP1f8F7lr2io7E7VNockEDrhAVKHaVteWtisVfq88viKq2UvCmaPRD3sT5+80CSuhRFyt8YhBHzJ5OjppQatbJHwJrWPRziFCUv+s2Txi/oRwDriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HAcxJcxw==",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "message": {
        "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "message": {
        "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
  "id": -576460752303422026,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422026,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+QEOCwH4hLhATIQbIYxYUwXS3c+rGH8+YFQU7MmTnHlGQHUE6UvNS4O6YCS9V0yGqbPSYVn3D5cIP1f8F7lr2io7E7VNockEDrhAVKHaVteWtisVfq88viKq2UvCmaPRD3sT5+80CSuhRFyt8YhBHzJ5OjppQatbJHwJrWPRziFCUv+s2Txi/oRwDriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HAcxJcxw=="
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+QEOCwH4hLhATIQbIYxYUwXS3c+rGH8+YFQU7MmTnHlGQHUE6UvNS4O6YCS9V0yGqbPSYVn3D5cIP1f8F7lr2io7E7VNockEDrhAVKHaVteWtisVfq88viKq2UvCmaPRD3sT5+80CSuhRFyt8YhBHzJ5OjppQatbJHwJrWPRziFCUv+s2Txi/oRwDriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HAcxJcxw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422025,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422025,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkxnSZEQtzo+67cmpM9pqdwPtV5FLBFNG1Qke3KjdXiyAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAgCr5sA=",
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
  "id": -576460752303422024,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAVq61KGtROFLjsgwhuVUtYDoYowdHBvIdM32YJId8uPrPTxNXoHVSOgF241J0lUXxqPW2bbxBEA8cxkegLc9wLuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLxnrYL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422024,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAVq61KGtROFLjsgwhuVUtYDoYowdHBvIdM32YJId8uPrPTxNXoHVSOgF241J0lUXxqPW2bbxBEA8cxkegLc9wLuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLxnrYL",
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
  "id": -576460752303422023,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAVq61KGtROFLjsgwhuVUtYDoYowdHBvIdM32YJId8uPrPTxNXoHVSOgF241J0lUXxqPW2bbxBEA8cxkegLc9wLuECLITIh1NTQFa3gfClcXkyw7KtSQ23nvd7OC2AxWU/ZFZk/kHpe4arn0QY7j50YqotCF1mHrE8fR2V/q7InekYKuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLii7k+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422023,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+NILAfiEuEAVq61KGtROFLjsgwhuVUtYDoYowdHBvIdM32YJId8uPrPTxNXoHVSOgF241J0lUXxqPW2bbxBEA8cxkegLc9wLuECLITIh1NTQFa3gfClcXkyw7KtSQ23nvd7OC2AxWU/ZFZk/kHpe4arn0QY7j50YqotCF1mHrE8fR2V/q7InekYKuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLii7k+"
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+NILAfiEuEAVq61KGtROFLjsgwhuVUtYDoYowdHBvIdM32YJId8uPrPTxNXoHVSOgF241J0lUXxqPW2bbxBEA8cxkegLc9wLuECLITIh1NTQFa3gfClcXkyw7KtSQ23nvd7OC2AxWU/ZFZk/kHpe4arn0QY7j50YqotCF1mHrE8fR2V/q7InekYKuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLii7k+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422022,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422022,
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
  "id": -576460752303422021,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422021,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAVq61KGtROFLjsgwhuVUtYDoYowdHBvIdM32YJId8uPrPTxNXoHVSOgF241J0lUXxqPW2bbxBEA8cxkegLc9wLuECLITIh1NTQFa3gfClcXkyw7KtSQ23nvd7OC2AxWU/ZFZk/kHpe4arn0QY7j50YqotCF1mHrE8fR2V/q7InekYKuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLii7k+",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422020,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422020,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkxnSZEQtzo+67cmpM9pqdwPtV5FLBFNG1Qke3KjdXiyA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzcVTUY=",
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
  "id": -576460752303422019,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDh8SUCh/MBB1BmFylPKMOF+DicXqwzeqya0G82RFIyBH9lNo3PnmqPSzTcdkAc5cKMSev6sKpFRTiljjdB6UgOuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsCYM/X"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422019,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDh8SUCh/MBB1BmFylPKMOF+DicXqwzeqya0G82RFIyBH9lNo3PnmqPSzTcdkAc5cKMSev6sKpFRTiljjdB6UgOuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsCYM/X",
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
  "id": -576460752303422018,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDh8SUCh/MBB1BmFylPKMOF+DicXqwzeqya0G82RFIyBH9lNo3PnmqPSzTcdkAc5cKMSev6sKpFRTiljjdB6UgOuED4QNRWUpFwMrQd3wK4zl2TImk2+MQBqehBfgr3HKXYMgN2XD/XwmMw/97kxSngZfIcRp82qSDrFfZqK6p7bLwHuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgucPse1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422018,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+NILAfiEuEDh8SUCh/MBB1BmFylPKMOF+DicXqwzeqya0G82RFIyBH9lNo3PnmqPSzTcdkAc5cKMSev6sKpFRTiljjdB6UgOuED4QNRWUpFwMrQd3wK4zl2TImk2+MQBqehBfgr3HKXYMgN2XD/XwmMw/97kxSngZfIcRp82qSDrFfZqK6p7bLwHuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgucPse1"
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+NILAfiEuEDh8SUCh/MBB1BmFylPKMOF+DicXqwzeqya0G82RFIyBH9lNo3PnmqPSzTcdkAc5cKMSev6sKpFRTiljjdB6UgOuED4QNRWUpFwMrQd3wK4zl2TImk2+MQBqehBfgr3HKXYMgN2XD/XwmMw/97kxSngZfIcRp82qSDrFfZqK6p7bLwHuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgucPse1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422017,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422017,
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
  "id": -576460752303422016,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422016,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDh8SUCh/MBB1BmFylPKMOF+DicXqwzeqya0G82RFIyBH9lNo3PnmqPSzTcdkAc5cKMSev6sKpFRTiljjdB6UgOuED4QNRWUpFwMrQd3wK4zl2TImk2+MQBqehBfgr3HKXYMgN2XD/XwmMw/97kxSngZfIcRp82qSDrFfZqK6p7bLwHuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgucPse1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422015,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422015,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDh8SUCh/MBB1BmFylPKMOF+DicXqwzeqya0G82RFIyBH9lNo3PnmqPSzTcdkAc5cKMSev6sKpFRTiljjdB6UgOuED4QNRWUpFwMrQd3wK4zl2TImk2+MQBqehBfgr3HKXYMgN2XD/XwmMw/97kxSngZfIcRp82qSDrFfZqK6p7bLwHuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgucPse1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422014,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422014,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkxnSZEQtzo+67cmpM9pqdwPtV5FLBFNG1Qke3KjdXiyBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAkKePzQ=",
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
  "id": -576460752303422013,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECzHo4I8DEyPNWSeuU9RSBaSpNu+KogafPBwk26vwhCCIQcdrXyPjwb1+71hkIyKALKNx7EbYZxSMfwHTzueb8MuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJxxT/6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422013,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "signed_tx": "tx_+JALAfhCuECzHo4I8DEyPNWSeuU9RSBaSpNu+KogafPBwk26vwhCCIQcdrXyPjwb1+71hkIyKALKNx7EbYZxSMfwHTzueb8MuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJxxT/6",
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
  "id": -576460752303422012,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBhFKrhvR6EWP75f0Ps/w4MGM5RtnABm984PTJjFJ+dxi5kAH8eczdsmpQb+FHg8MjrRxKZrqwYCaJxecYIb1MMuECzHo4I8DEyPNWSeuU9RSBaSpNu+KogafPBwk26vwhCCIQcdrXyPjwb1+71hkIyKALKNx7EbYZxSMfwHTzueb8MuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIjQBol"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422012,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+NILAfiEuEBhFKrhvR6EWP75f0Ps/w4MGM5RtnABm984PTJjFJ+dxi5kAH8eczdsmpQb+FHg8MjrRxKZrqwYCaJxecYIb1MMuECzHo4I8DEyPNWSeuU9RSBaSpNu+KogafPBwk26vwhCCIQcdrXyPjwb1+71hkIyKALKNx7EbYZxSMfwHTzueb8MuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIjQBol"
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+NILAfiEuEBhFKrhvR6EWP75f0Ps/w4MGM5RtnABm984PTJjFJ+dxi5kAH8eczdsmpQb+FHg8MjrRxKZrqwYCaJxecYIb1MMuECzHo4I8DEyPNWSeuU9RSBaSpNu+KogafPBwk26vwhCCIQcdrXyPjwb1+71hkIyKALKNx7EbYZxSMfwHTzueb8MuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIjQBol"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422011,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422011,
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
  "id": -576460752303422010,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422010,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBhFKrhvR6EWP75f0Ps/w4MGM5RtnABm984PTJjFJ+dxi5kAH8eczdsmpQb+FHg8MjrRxKZrqwYCaJxecYIb1MMuECzHo4I8DEyPNWSeuU9RSBaSpNu+KogafPBwk26vwhCCIQcdrXyPjwb1+71hkIyKALKNx7EbYZxSMfwHTzueb8MuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIjQBol",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422009,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422009,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkxnSZEQtzo+67cmpM9pqdwPtV5FLBFNG1Qke3KjdXiyBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwbpPkg=",
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
  "id": -576460752303422008,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDiVZjU3Gb6yUJ3V3uAu/g/VDN2lfibtX6cHZcTWtXTUSx50C82jJu90tYAsuxlaNkYd4UHHaqs+Y9N88lu6CsFuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvWDTan"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422008,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDiVZjU3Gb6yUJ3V3uAu/g/VDN2lfibtX6cHZcTWtXTUSx50C82jJu90tYAsuxlaNkYd4UHHaqs+Y9N88lu6CsFuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvWDTan",
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
  "id": -576460752303422007,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECySQ1BQbVoNgVpPtA0cO7pES7rwLAcTHv4OVBoBYQMxWLtEIxZ4HsmI8gvX1wOBQt7BBwlOf9orVTOzhuEoqIEuEDiVZjU3Gb6yUJ3V3uAu/g/VDN2lfibtX6cHZcTWtXTUSx50C82jJu90tYAsuxlaNkYd4UHHaqs+Y9N88lu6CsFuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguCp3Nw"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422007,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+NILAfiEuECySQ1BQbVoNgVpPtA0cO7pES7rwLAcTHv4OVBoBYQMxWLtEIxZ4HsmI8gvX1wOBQt7BBwlOf9orVTOzhuEoqIEuEDiVZjU3Gb6yUJ3V3uAu/g/VDN2lfibtX6cHZcTWtXTUSx50C82jJu90tYAsuxlaNkYd4UHHaqs+Y9N88lu6CsFuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguCp3Nw"
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "state": "tx_+NILAfiEuECySQ1BQbVoNgVpPtA0cO7pES7rwLAcTHv4OVBoBYQMxWLtEIxZ4HsmI8gvX1wOBQt7BBwlOf9orVTOzhuEoqIEuEDiVZjU3Gb6yUJ3V3uAu/g/VDN2lfibtX6cHZcTWtXTUSx50C82jJu90tYAsuxlaNkYd4UHHaqs+Y9N88lu6CsFuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguCp3Nw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422006,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422006,
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
  "id": -576460752303422005,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422005,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECySQ1BQbVoNgVpPtA0cO7pES7rwLAcTHv4OVBoBYQMxWLtEIxZ4HsmI8gvX1wOBQt7BBwlOf9orVTOzhuEoqIEuEDiVZjU3Gb6yUJ3V3uAu/g/VDN2lfibtX6cHZcTWtXTUSx50C82jJu90tYAsuxlaNkYd4UHHaqs+Y9N88lu6CsFuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguCp3Nw",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECySQ1BQbVoNgVpPtA0cO7pES7rwLAcTHv4OVBoBYQMxWLtEIxZ4HsmI8gvX1wOBQt7BBwlOf9orVTOzhuEoqIEuEDiVZjU3Gb6yUJ3V3uAu/g/VDN2lfibtX6cHZcTWtXTUSx50C82jJu90tYAsuxlaNkYd4UHHaqs+Y9N88lu6CsFuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguCp3Nw",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECySQ1BQbVoNgVpPtA0cO7pES7rwLAcTHv4OVBoBYQMxWLtEIxZ4HsmI8gvX1wOBQt7BBwlOf9orVTOzhuEoqIEuEDiVZjU3Gb6yUJ3V3uAu/g/VDN2lfibtX6cHZcTWtXTUSx50C82jJu90tYAsuxlaNkYd4UHHaqs+Y9N88lu6CsFuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguCp3Nw",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBkxnSZEQtzo+67cmpM9pqdwPtV5FLBFNG1Qke3KjdXiyoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuECySQ1BQbVoNgVpPtA0cO7pES7rwLAcTHv4OVBoBYQMxWLtEIxZ4HsmI8gvX1wOBQt7BBwlOf9orVTOzhuEoqIEuEDiVZjU3Gb6yUJ3V3uAu/g/VDN2lfibtX6cHZcTWtXTUSx50C82jJu90tYAsuxlaNkYd4UHHaqs+Y9N88lu6CsFuEj4RjkCoQZMZ0mRELc6Puu3JqTPaancD7VeRSwRTRtUJHtyo3V4sgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGSNwYbAAgcEnJ3oO",
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
  "method": "channels.slash_sign",
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
  "id": -576460752303422004,
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422004,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422003,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
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
  "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
  "id": -576460752303422003,
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
    "channel_id": "ch_aedC9HXEM4ddT4j2B4j1c5nyzJ9HrzNiupaZ1YQpQZ3ZocZtG",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

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
      "fsm_id": "ba_vW9ubmXswSUdXbC+HCoCEAjcdeGaM8rI9TGCNqM4wUxkyxuJ"
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
      "fsm_id": "ba_tKzAXKnPTR/DdK6QZJhMt3/8syVmmI1JFg/Vtga0lHqmjfEZ"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBwTnxyeM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422002,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAJGrtpG3ADRDUVbXVV3VI4zSyzmNjBehlATdpV6a3GCvnAeXl5qTvkuCF+zX44HzgIw0TLs0g1UZY8o6vkRwoNuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgcG+R8rY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422002,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "fsm_id": "ba_tKzAXKnPTR/DdK6QZJhMt3/8syVmmI1JFg/Vtga0lHqmjfEZ",
      "signed_tx": "tx_+MwLAfhCuEAJGrtpG3ADRDUVbXVV3VI4zSyzmNjBehlATdpV6a3GCvnAeXl5qTvkuCF+zX44HzgIw0TLs0g1UZY8o6vkRwoNuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgcG+R8rY",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422001,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhACRq7aRtwA0Q1FW11Vd1SOM0ss5jYwXoZQE3aVemtxgr5wHl5eak75Lghfs1+OB84CMNEy7NINVGWPKOr5EcKDbhACovoC244t+k8w6lqKMVlhS55xFwiuJaxQWdmaMN50ronq/KI4IlR+g2MYeJgKN8bwPxvo+ji/H+YcWTA6XrGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HBvmDBeQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303422001,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhACRq7aRtwA0Q1FW11Vd1SOM0ss5jYwXoZQE3aVemtxgr5wHl5eak75Lghfs1+OB84CMNEy7NINVGWPKOr5EcKDbhACovoC244t+k8w6lqKMVlhS55xFwiuJaxQWdmaMN50ronq/KI4IlR+g2MYeJgKN8bwPxvo+ji/H+YcWTA6XrGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HBvmDBeQ==",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_vW9ubmXswSUdXbC+HCoCEAjcdeGaM8rI9TGCNqM4wUxkyxuJ"
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhACRq7aRtwA0Q1FW11Vd1SOM0ss5jYwXoZQE3aVemtxgr5wHl5eak75Lghfs1+OB84CMNEy7NINVGWPKOr5EcKDbhACovoC244t+k8w6lqKMVlhS55xFwiuJaxQWdmaMN50ronq/KI4IlR+g2MYeJgKN8bwPxvo+ji/H+YcWTA6XrGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HBvmDBeQ==",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhACRq7aRtwA0Q1FW11Vd1SOM0ss5jYwXoZQE3aVemtxgr5wHl5eak75Lghfs1+OB84CMNEy7NINVGWPKOr5EcKDbhACovoC244t+k8w6lqKMVlhS55xFwiuJaxQWdmaMN50ronq/KI4IlR+g2MYeJgKN8bwPxvo+ji/H+YcWTA6XrGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HBvmDBeQ==",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhACRq7aRtwA0Q1FW11Vd1SOM0ss5jYwXoZQE3aVemtxgr5wHl5eak75Lghfs1+OB84CMNEy7NINVGWPKOr5EcKDbhACovoC244t+k8w6lqKMVlhS55xFwiuJaxQWdmaMN50ronq/KI4IlR+g2MYeJgKN8bwPxvo+ji/H+YcWTA6XrGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HBvmDBeQ==",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "message": {
        "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "message": {
        "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
  "id": -576460752303422000,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303422000,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+QEOCwH4hLhACRq7aRtwA0Q1FW11Vd1SOM0ss5jYwXoZQE3aVemtxgr5wHl5eak75Lghfs1+OB84CMNEy7NINVGWPKOr5EcKDbhACovoC244t+k8w6lqKMVlhS55xFwiuJaxQWdmaMN50ronq/KI4IlR+g2MYeJgKN8bwPxvo+ji/H+YcWTA6XrGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HBvmDBeQ=="
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+QEOCwH4hLhACRq7aRtwA0Q1FW11Vd1SOM0ss5jYwXoZQE3aVemtxgr5wHl5eak75Lghfs1+OB84CMNEy7NINVGWPKOr5EcKDbhACovoC244t+k8w6lqKMVlhS55xFwiuJaxQWdmaMN50ronq/KI4IlR+g2MYeJgKN8bwPxvo+ji/H+YcWTA6XrGBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HBvmDBeQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421999,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421999,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqPkiVsbzhVz7myNIRDG31xIDzvqpfY+62gJrGZQmBSdAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeApZAoQk=",
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
  "id": -576460752303421998,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAIXIFLmRif61t8sfrEHShNEqUbYJftt7spjU6n4/p0oNvjFMaHj86UWY74cqF/gpcFwlWB5e8QWpddYXufUG8LuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL59C8i"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421998,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAIXIFLmRif61t8sfrEHShNEqUbYJftt7spjU6n4/p0oNvjFMaHj86UWY74cqF/gpcFwlWB5e8QWpddYXufUG8LuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL59C8i",
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
  "id": -576460752303421997,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAIXIFLmRif61t8sfrEHShNEqUbYJftt7spjU6n4/p0oNvjFMaHj86UWY74cqF/gpcFwlWB5e8QWpddYXufUG8LuECb5o+MPCU1hSy/QNBjbly+H6p6ba8iQbq3tT/yQrS1rlJdKba237nnj6UwGeKbm1XtEx88AgjOMZJaVe3mN8UCuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKnKw5X"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421997,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+NILAfiEuEAIXIFLmRif61t8sfrEHShNEqUbYJftt7spjU6n4/p0oNvjFMaHj86UWY74cqF/gpcFwlWB5e8QWpddYXufUG8LuECb5o+MPCU1hSy/QNBjbly+H6p6ba8iQbq3tT/yQrS1rlJdKba237nnj6UwGeKbm1XtEx88AgjOMZJaVe3mN8UCuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKnKw5X"
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+NILAfiEuEAIXIFLmRif61t8sfrEHShNEqUbYJftt7spjU6n4/p0oNvjFMaHj86UWY74cqF/gpcFwlWB5e8QWpddYXufUG8LuECb5o+MPCU1hSy/QNBjbly+H6p6ba8iQbq3tT/yQrS1rlJdKba237nnj6UwGeKbm1XtEx88AgjOMZJaVe3mN8UCuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKnKw5X"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421996,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421996,
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
  "id": -576460752303421995,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421995,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAIXIFLmRif61t8sfrEHShNEqUbYJftt7spjU6n4/p0oNvjFMaHj86UWY74cqF/gpcFwlWB5e8QWpddYXufUG8LuECb5o+MPCU1hSy/QNBjbly+H6p6ba8iQbq3tT/yQrS1rlJdKba237nnj6UwGeKbm1XtEx88AgjOMZJaVe3mN8UCuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKnKw5X",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421994,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421994,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqPkiVsbzhVz7myNIRDG31xIDzvqpfY+62gJrGZQmBSdA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC5YYJ8c=",
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
  "id": -576460752303421993,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBrqd+92g5+1j/d9uG0dCr6rQvB9+3BQslINHOxiaM9VnRdC6iAIAHiMKOoekKM3WtI2CXAnbEWawZTZWn+kkIKuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvKhdcM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421993,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBrqd+92g5+1j/d9uG0dCr6rQvB9+3BQslINHOxiaM9VnRdC6iAIAHiMKOoekKM3WtI2CXAnbEWawZTZWn+kkIKuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvKhdcM",
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
  "id": -576460752303421992,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBLu6cJbA1DBAm5b5sxxMZC0T97DJFxHpm4OrlOHBmVU7iBbfRrEUAZDsqxM0SfEmqrwUVq26Xh5e1X5fkKeOQBuEBrqd+92g5+1j/d9uG0dCr6rQvB9+3BQslINHOxiaM9VnRdC6iAIAHiMKOoekKM3WtI2CXAnbEWawZTZWn+kkIKuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguVW42B"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421992,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+NILAfiEuEBLu6cJbA1DBAm5b5sxxMZC0T97DJFxHpm4OrlOHBmVU7iBbfRrEUAZDsqxM0SfEmqrwUVq26Xh5e1X5fkKeOQBuEBrqd+92g5+1j/d9uG0dCr6rQvB9+3BQslINHOxiaM9VnRdC6iAIAHiMKOoekKM3WtI2CXAnbEWawZTZWn+kkIKuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguVW42B"
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+NILAfiEuEBLu6cJbA1DBAm5b5sxxMZC0T97DJFxHpm4OrlOHBmVU7iBbfRrEUAZDsqxM0SfEmqrwUVq26Xh5e1X5fkKeOQBuEBrqd+92g5+1j/d9uG0dCr6rQvB9+3BQslINHOxiaM9VnRdC6iAIAHiMKOoekKM3WtI2CXAnbEWawZTZWn+kkIKuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguVW42B"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421991,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421991,
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
  "id": -576460752303421990,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421990,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBLu6cJbA1DBAm5b5sxxMZC0T97DJFxHpm4OrlOHBmVU7iBbfRrEUAZDsqxM0SfEmqrwUVq26Xh5e1X5fkKeOQBuEBrqd+92g5+1j/d9uG0dCr6rQvB9+3BQslINHOxiaM9VnRdC6iAIAHiMKOoekKM3WtI2CXAnbEWawZTZWn+kkIKuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguVW42B",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421989,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421989,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBLu6cJbA1DBAm5b5sxxMZC0T97DJFxHpm4OrlOHBmVU7iBbfRrEUAZDsqxM0SfEmqrwUVq26Xh5e1X5fkKeOQBuEBrqd+92g5+1j/d9uG0dCr6rQvB9+3BQslINHOxiaM9VnRdC6iAIAHiMKOoekKM3WtI2CXAnbEWawZTZWn+kkIKuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguVW42B",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421988,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421988,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqPkiVsbzhVz7myNIRDG31xIDzvqpfY+62gJrGZQmBSdBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAq/0Ykc=",
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
  "id": -576460752303421987,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECCts5T5lac3NCb8R0f5TC9Gm14KYCaFRfRAlLQRhcvTYjsS+QEjbQAktlWkGaW94DAGuDzitnQTm+R7zBkS4wHuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLOa50I"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421987,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "signed_tx": "tx_+JALAfhCuECCts5T5lac3NCb8R0f5TC9Gm14KYCaFRfRAlLQRhcvTYjsS+QEjbQAktlWkGaW94DAGuDzitnQTm+R7zBkS4wHuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLOa50I",
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
  "id": -576460752303421986,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAcAcbXqeTzVnZvDNNVexLRqAoCC6TeCPGDG/T4QUIh2NYTFxcefSjx//f7KNFgrtj8vfZg179/5MJnflA/QjgAuECCts5T5lac3NCb8R0f5TC9Gm14KYCaFRfRAlLQRhcvTYjsS+QEjbQAktlWkGaW94DAGuDzitnQTm+R7zBkS4wHuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJBAfRz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421986,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+NILAfiEuEAcAcbXqeTzVnZvDNNVexLRqAoCC6TeCPGDG/T4QUIh2NYTFxcefSjx//f7KNFgrtj8vfZg179/5MJnflA/QjgAuECCts5T5lac3NCb8R0f5TC9Gm14KYCaFRfRAlLQRhcvTYjsS+QEjbQAktlWkGaW94DAGuDzitnQTm+R7zBkS4wHuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJBAfRz"
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+NILAfiEuEAcAcbXqeTzVnZvDNNVexLRqAoCC6TeCPGDG/T4QUIh2NYTFxcefSjx//f7KNFgrtj8vfZg179/5MJnflA/QjgAuECCts5T5lac3NCb8R0f5TC9Gm14KYCaFRfRAlLQRhcvTYjsS+QEjbQAktlWkGaW94DAGuDzitnQTm+R7zBkS4wHuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJBAfRz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421985,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421985,
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
  "id": -576460752303421984,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421984,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAcAcbXqeTzVnZvDNNVexLRqAoCC6TeCPGDG/T4QUIh2NYTFxcefSjx//f7KNFgrtj8vfZg179/5MJnflA/QjgAuECCts5T5lac3NCb8R0f5TC9Gm14KYCaFRfRAlLQRhcvTYjsS+QEjbQAktlWkGaW94DAGuDzitnQTm+R7zBkS4wHuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJBAfRz",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421983,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421983,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqPkiVsbzhVz7myNIRDG31xIDzvqpfY+62gJrGZQmBSdBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC52NuGw=",
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
  "id": -576460752303421982,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAdxh+59z9s+rCcYxFalPQEx9bYDK7fimTBH/F/p2gm5HwQDbZT4x/RrNLWPkBcMgMxRladImlZP/oSEWATVjUNuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguknE9T"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421982,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAdxh+59z9s+rCcYxFalPQEx9bYDK7fimTBH/F/p2gm5HwQDbZT4x/RrNLWPkBcMgMxRladImlZP/oSEWATVjUNuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguknE9T",
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
  "id": -576460752303421981,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAdxh+59z9s+rCcYxFalPQEx9bYDK7fimTBH/F/p2gm5HwQDbZT4x/RrNLWPkBcMgMxRladImlZP/oSEWATVjUNuEC+ViHQXgt80fzUPYzO8hid3TsjqMqtFn3O2Hu+2vqusf/GhLSSjl02jtg/Ew75u0T2J1ow2Vxn8PKJeY2WXr4KuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsy+RxA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421981,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+NILAfiEuEAdxh+59z9s+rCcYxFalPQEx9bYDK7fimTBH/F/p2gm5HwQDbZT4x/RrNLWPkBcMgMxRladImlZP/oSEWATVjUNuEC+ViHQXgt80fzUPYzO8hid3TsjqMqtFn3O2Hu+2vqusf/GhLSSjl02jtg/Ew75u0T2J1ow2Vxn8PKJeY2WXr4KuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsy+RxA"
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "state": "tx_+NILAfiEuEAdxh+59z9s+rCcYxFalPQEx9bYDK7fimTBH/F/p2gm5HwQDbZT4x/RrNLWPkBcMgMxRladImlZP/oSEWATVjUNuEC+ViHQXgt80fzUPYzO8hid3TsjqMqtFn3O2Hu+2vqusf/GhLSSjl02jtg/Ew75u0T2J1ow2Vxn8PKJeY2WXr4KuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsy+RxA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421980,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421980,
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
  "id": -576460752303421979,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421979,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAdxh+59z9s+rCcYxFalPQEx9bYDK7fimTBH/F/p2gm5HwQDbZT4x/RrNLWPkBcMgMxRladImlZP/oSEWATVjUNuEC+ViHQXgt80fzUPYzO8hid3TsjqMqtFn3O2Hu+2vqusf/GhLSSjl02jtg/Ew75u0T2J1ow2Vxn8PKJeY2WXr4KuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsy+RxA",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAdxh+59z9s+rCcYxFalPQEx9bYDK7fimTBH/F/p2gm5HwQDbZT4x/RrNLWPkBcMgMxRladImlZP/oSEWATVjUNuEC+ViHQXgt80fzUPYzO8hid3TsjqMqtFn3O2Hu+2vqusf/GhLSSjl02jtg/Ew75u0T2J1ow2Vxn8PKJeY2WXr4KuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsy+RxA",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAdxh+59z9s+rCcYxFalPQEx9bYDK7fimTBH/F/p2gm5HwQDbZT4x/RrNLWPkBcMgMxRladImlZP/oSEWATVjUNuEC+ViHQXgt80fzUPYzO8hid3TsjqMqtFn3O2Hu+2vqusf/GhLSSjl02jtg/Ew75u0T2J1ow2Vxn8PKJeY2WXr4KuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsy+RxA",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBqPkiVsbzhVz7myNIRDG31xIDzvqpfY+62gJrGZQmBSdoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEAdxh+59z9s+rCcYxFalPQEx9bYDK7fimTBH/F/p2gm5HwQDbZT4x/RrNLWPkBcMgMxRladImlZP/oSEWATVjUNuEC+ViHQXgt80fzUPYzO8hid3TsjqMqtFn3O2Hu+2vqusf/GhLSSjl02jtg/Ew75u0T2J1ow2Vxn8PKJeY2WXr4KuEj4RjkCoQaj5IlbG84Vc+5sjSEQxt9cSA876qX2PutoCaxmUJgUnQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGR7ISegAQz8ryh4=",
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
  "method": "channels.slash_sign",
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
  "id": -576460752303421978,
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421978,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421977,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
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
  "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
  "id": -576460752303421977,
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
    "channel_id": "ch_2FBRLVbYJMuNBDNyDfwoxohNALKaFXfVQE9w2GBonThiDUcLNC",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
