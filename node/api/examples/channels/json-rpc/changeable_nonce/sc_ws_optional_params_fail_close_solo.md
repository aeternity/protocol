
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
      "fsm_id": "ba_0w5M7O4WZyHIULTTa8HkY88YrNeVxRcfVFumQQxntiberYi5"
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
      "fsm_id": "ba_foHRNNoAZDgX5+JgWgIcSj3eA9iSIrMuJBT/P/9IHv2j/+Se"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBqROpk7I=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422205,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBQhRnn5QAyJz9p2RS7olOjM83lpCplAx83SBt4nfXYPHhlBqE/U4p1CJI2d168AW21tvf+7SV3KXG02e/mYu0PuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgamWiqGe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422205,
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "fsm_id": "ba_foHRNNoAZDgX5+JgWgIcSj3eA9iSIrMuJBT/P/9IHv2j/+Se",
      "signed_tx": "tx_+MwLAfhCuEBQhRnn5QAyJz9p2RS7olOjM83lpCplAx83SBt4nfXYPHhlBqE/U4p1CJI2d168AW21tvf+7SV3KXG02e/mYu0PuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgamWiqGe",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422204,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAUIUZ5+UAMic/adkUu6JTozPN5aQqZQMfN0gbeJ312Dx4ZQahP1OKdQiSNndevAFttbb3/u0ldylxtNnv5mLtD7hAeP25XmgQnT++X/3Yue4R0ovuMAieWr0PPQbN8Z8TKhM3MstEqYJe71g2jTm52ZXlGIKWul+Ss7iQhFYMWdq+DbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gp419FiA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
  "id": -576460752303422204,
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAUIUZ5+UAMic/adkUu6JTozPN5aQqZQMfN0gbeJ312Dx4ZQahP1OKdQiSNndevAFttbb3/u0ldylxtNnv5mLtD7hAeP25XmgQnT++X/3Yue4R0ovuMAieWr0PPQbN8Z8TKhM3MstEqYJe71g2jTm52ZXlGIKWul+Ss7iQhFYMWdq+DbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gp419FiA==",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_0w5M7O4WZyHIULTTa8HkY88YrNeVxRcfVFumQQxntiberYi5"
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAUIUZ5+UAMic/adkUu6JTozPN5aQqZQMfN0gbeJ312Dx4ZQahP1OKdQiSNndevAFttbb3/u0ldylxtNnv5mLtD7hAeP25XmgQnT++X/3Yue4R0ovuMAieWr0PPQbN8Z8TKhM3MstEqYJe71g2jTm52ZXlGIKWul+Ss7iQhFYMWdq+DbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gp419FiA==",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAUIUZ5+UAMic/adkUu6JTozPN5aQqZQMfN0gbeJ312Dx4ZQahP1OKdQiSNndevAFttbb3/u0ldylxtNnv5mLtD7hAeP25XmgQnT++X/3Yue4R0ovuMAieWr0PPQbN8Z8TKhM3MstEqYJe71g2jTm52ZXlGIKWul+Ss7iQhFYMWdq+DbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gp419FiA==",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAUIUZ5+UAMic/adkUu6JTozPN5aQqZQMfN0gbeJ312Dx4ZQahP1OKdQiSNndevAFttbb3/u0ldylxtNnv5mLtD7hAeP25XmgQnT++X/3Yue4R0ovuMAieWr0PPQbN8Z8TKhM3MstEqYJe71g2jTm52ZXlGIKWul+Ss7iQhFYMWdq+DbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gp419FiA==",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "message": {
        "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "message": {
        "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
  "id": -576460752303422203,
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
  "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
  "id": -576460752303422203,
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "state": "tx_+QEOCwH4hLhAUIUZ5+UAMic/adkUu6JTozPN5aQqZQMfN0gbeJ312Dx4ZQahP1OKdQiSNndevAFttbb3/u0ldylxtNnv5mLtD7hAeP25XmgQnT++X/3Yue4R0ovuMAieWr0PPQbN8Z8TKhM3MstEqYJe71g2jTm52ZXlGIKWul+Ss7iQhFYMWdq+DbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gp419FiA=="
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "state": "tx_+QEOCwH4hLhAUIUZ5+UAMic/adkUu6JTozPN5aQqZQMfN0gbeJ312Dx4ZQahP1OKdQiSNndevAFttbb3/u0ldylxtNnv5mLtD7hAeP25XmgQnT++X/3Yue4R0ovuMAieWr0PPQbN8Z8TKhM3MstEqYJe71g2jTm52ZXlGIKWul+Ss7iQhFYMWdq+DbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gp419FiA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "signed_tx": "tx_+QGrCwHAuQGl+QGiNgGhBuXzcEMUIjkbDb60WtUHJGAslBzOrPy6lxJmF5sCXQWxoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFUzkx9gAgxLWh7d+94Y=",
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
  "method": "channels.close_solo_sign",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBuXzcEMUIjkbDb60WtUHJGAslBzOrPy6lxJmF5sCXQWxoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBqqU0LuE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422202,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEAsN9q09wxzI5FpchAlrBqQ7ilCIJVyC3gzUA01YO+b3a11uUag5iKVExFHVytHyvOStJLA5wWis98xGsnWvdEPuGD4XjUBoQbl83BDFCI5Gw2+tFrVByRgLJQczqz8upcSZhebAl0FsaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaoT3lDx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
  "id": -576460752303422202,
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEAsN9q09wxzI5FpchAlrBqQ7ilCIJVyC3gzUA01YO+b3a11uUag5iKVExFHVytHyvOStJLA5wWis98xGsnWvdEPuGD4XjUBoQbl83BDFCI5Gw2+tFrVByRgLJQczqz8upcSZhebAl0FsaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaoT3lDx",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422201,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAsN9q09wxzI5FpchAlrBqQ7ilCIJVyC3gzUA01YO+b3a11uUag5iKVExFHVytHyvOStJLA5wWis98xGsnWvdEPuEBuME33QqGv89VfD6OZR/1q0Ykz5Pi+Kba3st16RhAePxag0Qq0rKEKiD0OBFHlwFpn6r262AMvGOqnjA36eZgIuGD4XjUBoQbl83BDFCI5Gw2+tFrVByRgLJQczqz8upcSZhebAl0FsaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgapCFyYR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
  "id": -576460752303422201,
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAsN9q09wxzI5FpchAlrBqQ7ilCIJVyC3gzUA01YO+b3a11uUag5iKVExFHVytHyvOStJLA5wWis98xGsnWvdEPuEBuME33QqGv89VfD6OZR/1q0Ykz5Pi+Kba3st16RhAePxag0Qq0rKEKiD0OBFHlwFpn6r262AMvGOqnjA36eZgIuGD4XjUBoQbl83BDFCI5Gw2+tFrVByRgLJQczqz8upcSZhebAl0FsaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgapCFyYR",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAsN9q09wxzI5FpchAlrBqQ7ilCIJVyC3gzUA01YO+b3a11uUag5iKVExFHVytHyvOStJLA5wWis98xGsnWvdEPuEBuME33QqGv89VfD6OZR/1q0Ykz5Pi+Kba3st16RhAePxag0Qq0rKEKiD0OBFHlwFpn6r262AMvGOqnjA36eZgIuGD4XjUBoQbl83BDFCI5Gw2+tFrVByRgLJQczqz8upcSZhebAl0FsaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgapCFyYR",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAsN9q09wxzI5FpchAlrBqQ7ilCIJVyC3gzUA01YO+b3a11uUag5iKVExFHVytHyvOStJLA5wWis98xGsnWvdEPuEBuME33QqGv89VfD6OZR/1q0Ykz5Pi+Kba3st16RhAePxag0Qq0rKEKiD0OBFHlwFpn6r262AMvGOqnjA36eZgIuGD4XjUBoQbl83BDFCI5Gw2+tFrVByRgLJQczqz8upcSZhebAl0FsaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgapCFyYR",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAsN9q09wxzI5FpchAlrBqQ7ilCIJVyC3gzUA01YO+b3a11uUag5iKVExFHVytHyvOStJLA5wWis98xGsnWvdEPuEBuME33QqGv89VfD6OZR/1q0Ykz5Pi+Kba3st16RhAePxag0Qq0rKEKiD0OBFHlwFpn6r262AMvGOqnjA36eZgIuGD4XjUBoQbl83BDFCI5Gw2+tFrVByRgLJQczqz8upcSZhebAl0FsaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgapCFyYR",
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
      "fsm_id": "ba_4XumtAzyzOFfr40R46L9Y2JvCZmq/6acU5WJyao51q7V2ui2"
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
      "fsm_id": "ba_jQdUT8Fsx2y5gvS7913VhYXwDmWwjAygCmGmUHq6m4PuIkv+"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBq5KX5bo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422200,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBVikOfICmFLKXpk7XhmaJoImRucv4PfRbbjlLz+fXO+3dWNPN//dy3yq+gmV3wxtUWAq1xfzyLo1JLD1n42G0PuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgatoqZRe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422200,
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "fsm_id": "ba_jQdUT8Fsx2y5gvS7913VhYXwDmWwjAygCmGmUHq6m4PuIkv+",
      "signed_tx": "tx_+MwLAfhCuEBVikOfICmFLKXpk7XhmaJoImRucv4PfRbbjlLz+fXO+3dWNPN//dy3yq+gmV3wxtUWAq1xfzyLo1JLD1n42G0PuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgatoqZRe",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422199,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAVYpDnyAphSyl6ZO14ZmiaCJkbnL+D30W245S8/n1zvt3VjTzf/3ct8qvoJld8MbVFgKtcX88i6NSSw9Z+NhtD7hAlMvdvK07/T/4x4+uBQ/zA+hhEs0MBwRZVuZWnkb+su4TmyArR/bqsUGtxpMtIEeJICXURiVtvnTzCD6tmhxNCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GrXhO2AQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
  "id": -576460752303422199,
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAVYpDnyAphSyl6ZO14ZmiaCJkbnL+D30W245S8/n1zvt3VjTzf/3ct8qvoJld8MbVFgKtcX88i6NSSw9Z+NhtD7hAlMvdvK07/T/4x4+uBQ/zA+hhEs0MBwRZVuZWnkb+su4TmyArR/bqsUGtxpMtIEeJICXURiVtvnTzCD6tmhxNCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GrXhO2AQ==",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_4XumtAzyzOFfr40R46L9Y2JvCZmq/6acU5WJyao51q7V2ui2"
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAVYpDnyAphSyl6ZO14ZmiaCJkbnL+D30W245S8/n1zvt3VjTzf/3ct8qvoJld8MbVFgKtcX88i6NSSw9Z+NhtD7hAlMvdvK07/T/4x4+uBQ/zA+hhEs0MBwRZVuZWnkb+su4TmyArR/bqsUGtxpMtIEeJICXURiVtvnTzCD6tmhxNCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GrXhO2AQ==",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAVYpDnyAphSyl6ZO14ZmiaCJkbnL+D30W245S8/n1zvt3VjTzf/3ct8qvoJld8MbVFgKtcX88i6NSSw9Z+NhtD7hAlMvdvK07/T/4x4+uBQ/zA+hhEs0MBwRZVuZWnkb+su4TmyArR/bqsUGtxpMtIEeJICXURiVtvnTzCD6tmhxNCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GrXhO2AQ==",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAVYpDnyAphSyl6ZO14ZmiaCJkbnL+D30W245S8/n1zvt3VjTzf/3ct8qvoJld8MbVFgKtcX88i6NSSw9Z+NhtD7hAlMvdvK07/T/4x4+uBQ/zA+hhEs0MBwRZVuZWnkb+su4TmyArR/bqsUGtxpMtIEeJICXURiVtvnTzCD6tmhxNCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GrXhO2AQ==",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
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
    "channel_id": "ch_2kGnhaVNqkS79u6CXNtTiWV4JkKGtouZaoFgF6gfUsmoAknVUG",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "message": {
        "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "message": {
        "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
  "id": -576460752303422198,
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
  "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
  "id": -576460752303422198,
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

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "state": "tx_+QEOCwH4hLhAVYpDnyAphSyl6ZO14ZmiaCJkbnL+D30W245S8/n1zvt3VjTzf/3ct8qvoJld8MbVFgKtcX88i6NSSw9Z+NhtD7hAlMvdvK07/T/4x4+uBQ/zA+hhEs0MBwRZVuZWnkb+su4TmyArR/bqsUGtxpMtIEeJICXURiVtvnTzCD6tmhxNCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GrXhO2AQ=="
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "state": "tx_+QEOCwH4hLhAVYpDnyAphSyl6ZO14ZmiaCJkbnL+D30W245S8/n1zvt3VjTzf/3ct8qvoJld8MbVFgKtcX88i6NSSw9Z+NhtD7hAlMvdvK07/T/4x4+uBQ/zA+hhEs0MBwRZVuZWnkb+su4TmyArR/bqsUGtxpMtIEeJICXURiVtvnTzCD6tmhxNCriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GrXhO2AQ=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "signed_tx": "tx_+QGrCwHAuQGl+QGiNgGhBrB3CX8ldo4N3STZD9TTLZG7KBwmGBKM7glNBvqWwLxgoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFUzkx9gAgxLWhwO1tC0=",
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
  "method": "channels.close_solo_sign",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBrB3CX8ldo4N3STZD9TTLZG7KBwmGBKM7glNBvqWwLxgoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBrEXrbD8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422197,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEAFXcXpD7PP9CnydrL8ct3dOF1sw9FZ4zBQeboFvH3rBCzoSscPQmIcMc7CNiXo3flbnS1fBsFWXid/YBHgKlkGuGD4XjUBoQawdwl/JXaODd0k2Q/U0y2RuygcJhgSjO4JTQb6lsC8YKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaztkg6C"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
  "id": -576460752303422197,
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEAFXcXpD7PP9CnydrL8ct3dOF1sw9FZ4zBQeboFvH3rBCzoSscPQmIcMc7CNiXo3flbnS1fBsFWXid/YBHgKlkGuGD4XjUBoQawdwl/JXaODd0k2Q/U0y2RuygcJhgSjO4JTQb6lsC8YKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaztkg6C",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422196,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAFXcXpD7PP9CnydrL8ct3dOF1sw9FZ4zBQeboFvH3rBCzoSscPQmIcMc7CNiXo3flbnS1fBsFWXid/YBHgKlkGuECVJwP/F/2GRXf/DsXfLDmBMOKOKITWmg/910r4OF6PcznbBH001Is1OvrYhCRaIOQtCRd5h2DiBj2miV/qGVwJuGD4XjUBoQawdwl/JXaODd0k2Q/U0y2RuygcJhgSjO4JTQb6lsC8YKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgazdUObK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
  "id": -576460752303422196,
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAFXcXpD7PP9CnydrL8ct3dOF1sw9FZ4zBQeboFvH3rBCzoSscPQmIcMc7CNiXo3flbnS1fBsFWXid/YBHgKlkGuECVJwP/F/2GRXf/DsXfLDmBMOKOKITWmg/910r4OF6PcznbBH001Is1OvrYhCRaIOQtCRd5h2DiBj2miV/qGVwJuGD4XjUBoQawdwl/JXaODd0k2Q/U0y2RuygcJhgSjO4JTQb6lsC8YKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgazdUObK",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAFXcXpD7PP9CnydrL8ct3dOF1sw9FZ4zBQeboFvH3rBCzoSscPQmIcMc7CNiXo3flbnS1fBsFWXid/YBHgKlkGuECVJwP/F/2GRXf/DsXfLDmBMOKOKITWmg/910r4OF6PcznbBH001Is1OvrYhCRaIOQtCRd5h2DiBj2miV/qGVwJuGD4XjUBoQawdwl/JXaODd0k2Q/U0y2RuygcJhgSjO4JTQb6lsC8YKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgazdUObK",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAFXcXpD7PP9CnydrL8ct3dOF1sw9FZ4zBQeboFvH3rBCzoSscPQmIcMc7CNiXo3flbnS1fBsFWXid/YBHgKlkGuECVJwP/F/2GRXf/DsXfLDmBMOKOKITWmg/910r4OF6PcznbBH001Is1OvrYhCRaIOQtCRd5h2DiBj2miV/qGVwJuGD4XjUBoQawdwl/JXaODd0k2Q/U0y2RuygcJhgSjO4JTQb6lsC8YKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgazdUObK",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAFXcXpD7PP9CnydrL8ct3dOF1sw9FZ4zBQeboFvH3rBCzoSscPQmIcMc7CNiXo3flbnS1fBsFWXid/YBHgKlkGuECVJwP/F/2GRXf/DsXfLDmBMOKOKITWmg/910r4OF6PcznbBH001Is1OvrYhCRaIOQtCRd5h2DiBj2miV/qGVwJuGD4XjUBoQawdwl/JXaODd0k2Q/U0y2RuygcJhgSjO4JTQb6lsC8YKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgazdUObK",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
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
    "channel_id": "ch_2LiZZCEWWVrVbmWnNNeGp5AsyX2ov9qm1v9HVevFEhD5wPim7u",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
