
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
      "fsm_id": "ba_5+eUWfEc+0tI4AiCdaO7SUcc5ZbZQadT5x3rNRhDpF8zYdg1"
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
      "fsm_id": "ba_py5gMr9QkARz+SR4KBqjrpGN63LSVxoVaLlbdfiAjnLVvizA"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBt5YXBps=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422119,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBbJefzRleSpzi3w8E1NxccbsdvaqQXUS8TX+OhHFRpfndBhb/xjkjatMpiGCkrwV5Hp/pLgpgH+GwSMgnNB9IBuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbcKq2C4"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422119,
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "fsm_id": "ba_py5gMr9QkARz+SR4KBqjrpGN63LSVxoVaLlbdfiAjnLVvizA",
      "signed_tx": "tx_+MwLAfhCuEBbJefzRleSpzi3w8E1NxccbsdvaqQXUS8TX+OhHFRpfndBhb/xjkjatMpiGCkrwV5Hp/pLgpgH+GwSMgnNB9IBuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbcKq2C4",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422118,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAG4gXbV+3uu9JjOSTXDpdmlU4+ermL/IFWpb5iEdHeAIOqzAI47to7d8SGF+YnJcEflvmPGMlo+cAXPXhADF9D7hAWyXn80ZXkqc4t8PBNTcXHG7Hb2qkF1EvE1/joRxUaX53QYW/8Y5I2rTKYhgpK8FeR6f6S4KYB/hsEjIJzQfSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G3+AkYcw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
  "id": -576460752303422118,
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAG4gXbV+3uu9JjOSTXDpdmlU4+ermL/IFWpb5iEdHeAIOqzAI47to7d8SGF+YnJcEflvmPGMlo+cAXPXhADF9D7hAWyXn80ZXkqc4t8PBNTcXHG7Hb2qkF1EvE1/joRxUaX53QYW/8Y5I2rTKYhgpK8FeR6f6S4KYB/hsEjIJzQfSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G3+AkYcw==",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_5+eUWfEc+0tI4AiCdaO7SUcc5ZbZQadT5x3rNRhDpF8zYdg1"
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAG4gXbV+3uu9JjOSTXDpdmlU4+ermL/IFWpb5iEdHeAIOqzAI47to7d8SGF+YnJcEflvmPGMlo+cAXPXhADF9D7hAWyXn80ZXkqc4t8PBNTcXHG7Hb2qkF1EvE1/joRxUaX53QYW/8Y5I2rTKYhgpK8FeR6f6S4KYB/hsEjIJzQfSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G3+AkYcw==",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAG4gXbV+3uu9JjOSTXDpdmlU4+ermL/IFWpb5iEdHeAIOqzAI47to7d8SGF+YnJcEflvmPGMlo+cAXPXhADF9D7hAWyXn80ZXkqc4t8PBNTcXHG7Hb2qkF1EvE1/joRxUaX53QYW/8Y5I2rTKYhgpK8FeR6f6S4KYB/hsEjIJzQfSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G3+AkYcw==",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAG4gXbV+3uu9JjOSTXDpdmlU4+ermL/IFWpb5iEdHeAIOqzAI47to7d8SGF+YnJcEflvmPGMlo+cAXPXhADF9D7hAWyXn80ZXkqc4t8PBNTcXHG7Hb2qkF1EvE1/joRxUaX53QYW/8Y5I2rTKYhgpK8FeR6f6S4KYB/hsEjIJzQfSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G3+AkYcw==",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "message": {
        "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "message": {
        "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
  "id": -576460752303422117,
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
  "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
  "id": -576460752303422117,
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "state": "tx_+QEOCwH4hLhAG4gXbV+3uu9JjOSTXDpdmlU4+ermL/IFWpb5iEdHeAIOqzAI47to7d8SGF+YnJcEflvmPGMlo+cAXPXhADF9D7hAWyXn80ZXkqc4t8PBNTcXHG7Hb2qkF1EvE1/joRxUaX53QYW/8Y5I2rTKYhgpK8FeR6f6S4KYB/hsEjIJzQfSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G3+AkYcw=="
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "state": "tx_+QEOCwH4hLhAG4gXbV+3uu9JjOSTXDpdmlU4+ermL/IFWpb5iEdHeAIOqzAI47to7d8SGF+YnJcEflvmPGMlo+cAXPXhADF9D7hAWyXn80ZXkqc4t8PBNTcXHG7Hb2qkF1EvE1/joRxUaX53QYW/8Y5I2rTKYhgpK8FeR6f6S4KYB/hsEjIJzQfSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G3+AkYcw=="
    }
  },
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmUrxOI2xiCyu37u4Ne6B8+KAIJnembPa4K4K45T87eAAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeApYGJnU=",
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
  "jsonrpc": "2.0",
  "method": "channels.update",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmUrxOI2xiCyu37u4Ne6B8+KAIJnembPa4K4K45T87eAAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeApYGJnU=",
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
  "jsonrpc": "2.0",
  "method": "channels.update",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmUrxOI2xiCyu37u4Ne6B8+KAIJnembPa4K4K45T87eAAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeApYGJnU=",
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
  "id": -576460752303422116,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDVnlo1vX7NHO25u7+xcHCD5koYgRlFVgi6Y94HGNyfxBfW34P2x13WIFtb/w8YU5byW/r7go6RZdvmxbNdrnUBuEj4RjkCoQZlK8TiNsYgsrt+7uDXugfPigCCZ3pmz2uCuCuOU/O3gAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIE2KFC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
  "id": -576460752303422116,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
      "method": "channels.update",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDVnlo1vX7NHO25u7+xcHCD5koYgRlFVgi6Y94HGNyfxBfW34P2x13WIFtb/w8YU5byW/r7go6RZdvmxbNdrnUBuEj4RjkCoQZlK8TiNsYgsrt+7uDXugfPigCCZ3pmz2uCuCuOU/O3gAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIE2KFC",
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
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
    "data": {
      "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
  "id": -576460752303422115,
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
  "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
  "id": -576460752303422115,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422114,
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
    "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
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
  "channel_id": "ch_mZH3t5AVV8YRpsmgeV4jK6zXYHd4PCjiKbjMsGzkSZKWihWux",
  "id": -576460752303422114,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
