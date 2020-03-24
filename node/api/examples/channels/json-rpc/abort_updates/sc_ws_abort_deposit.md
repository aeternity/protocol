
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
      "fsm_id": "ba_MhfHbUlHZUK5tmIc9G0ZNiCk/pasNQlWWB36VNmMuMm6/9LC"
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
      "fsm_id": "ba_v0LT1Zdxl8gETghbluZUM72p1Yj13gqfKcbRysa6BocsiVMX"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBuMxepLg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422113,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBaDhOHL00AvzLvEbHdKGMlUh2QYBj3dA6G+CHv0yLb9Ao9ngNJgXNRPNFV5nmZWkN4s/Y76FJhe7J73UyKLBQPuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lgbhlvtcc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422113,
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "fsm_id": "ba_v0LT1Zdxl8gETghbluZUM72p1Yj13gqfKcbRysa6BocsiVMX",
      "signed_tx": "tx_+MwLAfhCuEBaDhOHL00AvzLvEbHdKGMlUh2QYBj3dA6G+CHv0yLb9Ao9ngNJgXNRPNFV5nmZWkN4s/Y76FJhe7J73UyKLBQPuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lgbhlvtcc",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422112,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAWg4Thy9NAL8y7xGx3ShjJVIdkGAY93QOhvgh79Mi2/QKPZ4DSYFzUTzRVeZ5mVpDeLP2O+hSYXuye91MiiwUD7hA9BiMTulZnLy+e151tNxdPu7CsMPxTsZG/F/iZp9bMefzOv5cibjEFUyROHT8I/fIqNBOShuJlESn3eNIHzmKCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G4N5o2DA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
  "id": -576460752303422112,
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAWg4Thy9NAL8y7xGx3ShjJVIdkGAY93QOhvgh79Mi2/QKPZ4DSYFzUTzRVeZ5mVpDeLP2O+hSYXuye91MiiwUD7hA9BiMTulZnLy+e151tNxdPu7CsMPxTsZG/F/iZp9bMefzOv5cibjEFUyROHT8I/fIqNBOShuJlESn3eNIHzmKCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G4N5o2DA==",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_MhfHbUlHZUK5tmIc9G0ZNiCk/pasNQlWWB36VNmMuMm6/9LC"
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAWg4Thy9NAL8y7xGx3ShjJVIdkGAY93QOhvgh79Mi2/QKPZ4DSYFzUTzRVeZ5mVpDeLP2O+hSYXuye91MiiwUD7hA9BiMTulZnLy+e151tNxdPu7CsMPxTsZG/F/iZp9bMefzOv5cibjEFUyROHT8I/fIqNBOShuJlESn3eNIHzmKCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G4N5o2DA==",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAWg4Thy9NAL8y7xGx3ShjJVIdkGAY93QOhvgh79Mi2/QKPZ4DSYFzUTzRVeZ5mVpDeLP2O+hSYXuye91MiiwUD7hA9BiMTulZnLy+e151tNxdPu7CsMPxTsZG/F/iZp9bMefzOv5cibjEFUyROHT8I/fIqNBOShuJlESn3eNIHzmKCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G4N5o2DA==",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAWg4Thy9NAL8y7xGx3ShjJVIdkGAY93QOhvgh79Mi2/QKPZ4DSYFzUTzRVeZ5mVpDeLP2O+hSYXuye91MiiwUD7hA9BiMTulZnLy+e151tNxdPu7CsMPxTsZG/F/iZp9bMefzOv5cibjEFUyROHT8I/fIqNBOShuJlESn3eNIHzmKCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G4N5o2DA==",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "message": {
        "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "message": {
        "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
  "id": -576460752303422111,
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
  "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
  "id": -576460752303422111,
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "state": "tx_+QEOCwH4hLhAWg4Thy9NAL8y7xGx3ShjJVIdkGAY93QOhvgh79Mi2/QKPZ4DSYFzUTzRVeZ5mVpDeLP2O+hSYXuye91MiiwUD7hA9BiMTulZnLy+e151tNxdPu7CsMPxTsZG/F/iZp9bMefzOv5cibjEFUyROHT8I/fIqNBOShuJlESn3eNIHzmKCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G4N5o2DA=="
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "state": "tx_+QEOCwH4hLhAWg4Thy9NAL8y7xGx3ShjJVIdkGAY93QOhvgh79Mi2/QKPZ4DSYFzUTzRVeZ5mVpDeLP2O+hSYXuye91MiiwUD7hA9BiMTulZnLy+e151tNxdPu7CsMPxTsZG/F/iZp9bMefzOv5cibjEFUyROHT8I/fIqNBOShuJlESn3eNIHzmKCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G4N5o2DA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBmrEbUqoia+9uS6UBxIX0ryR995GhefH98p2nJGGbAo/oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/FSIpYAKAJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQKBuVU+67o=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainDeposit"
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
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBmrEbUqoia+9uS6UBxIX0ryR995GhefH98p2nJGGbAo/oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/AoHKQAKDqgdNkuhddveVDE/es1N/fevZuJ9NTBtOGxk/KimI/YwJBVA7NqA==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainDeposit"
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
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBmrEbUqoia+9uS6UBxIX0ryR995GhefH98p2nJGGbAo/oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/FSIpYAKAJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQKBuVU+67o=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainDeposit"
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
  "id": -576460752303422110,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuECKxOzFIMcJ0YeXKrAgHt4qI7br1LHKFIuPeBXgYq7JyqHubv+GZPhbmr2hauxbnbdx92IMfSuVSqqTadh6PccMuHX4czMBoQZqxG1KqImvvbkulAcSF9K8kffeRoXnx/fKdpyRhmwKP6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUiKWACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgbmjr4dQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
  "id": -576460752303422110,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
      "method": "channels.deposit_tx",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "signed_tx": "tx_+L0LAfhCuECKxOzFIMcJ0YeXKrAgHt4qI7br1LHKFIuPeBXgYq7JyqHubv+GZPhbmr2hauxbnbdx92IMfSuVSqqTadh6PccMuHX4czMBoQZqxG1KqImvvbkulAcSF9K8kffeRoXnx/fKdpyRhmwKP6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUiKWACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgbmjr4dQ",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainDeposit"
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
  "method": "channels.deposit_ack",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
    "data": {
      "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
  "id": -576460752303422109,
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
  "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
  "id": -576460752303422109,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422108,
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
    "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
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
  "channel_id": "ch_p2EBHHxzKrJ496ZqCbFvgsKUXdnT3ayqc8jwkA4ZP2mPeJffM",
  "id": -576460752303422108,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
