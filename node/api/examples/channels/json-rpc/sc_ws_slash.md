
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3578%5Binitiator44initiator%5D
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
      "fsm_id": "ba_NbtLj/WybNc0qug1en2fx2pYQbkZMFYfQ8hyWGl7wdFidlWP"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3578%5Binitiator44initiator%5D
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
      "fsm_id": "ba_Ay9cPpsFwjcL1f6hvwu0guA7eZcalkYfmKQBm+CyGHk1RElY"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsQN+I2xw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423295,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDN5Y107dTEJw5L1D1sgJbzP+28yIaHLWdNe069eaTl2andsEjedPUucrA4DDJeHH74KUZkxVTt38FVSOH539MGuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LEENbCIM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423295,
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "fsm_id": "ba_Ay9cPpsFwjcL1f6hvwu0guA7eZcalkYfmKQBm+CyGHk1RElY",
      "signed_tx": "tx_+MsLAfhCuEDN5Y107dTEJw5L1D1sgJbzP+28yIaHLWdNe069eaTl2andsEjedPUucrA4DDJeHH74KUZkxVTt38FVSOH539MGuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LEENbCIM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423294,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAzeWNdO3UxCcOS9Q9bICW8z/tvMiGhy1nTXtOvXmk5dmp3bBI3nT1LnKwOAwyXhx++ClGZMVU7d/BVUjh+d/TBrhA/QuQDQErkgX5CehrikbXeks+k9GRI1KA6coYVJDTTImmN04+E8/5FdMfmI7PPRNmE0/j4GtfOQy/lCpvhghRC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxBFgLzf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
  "id": -576460752303423294,
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAzeWNdO3UxCcOS9Q9bICW8z/tvMiGhy1nTXtOvXmk5dmp3bBI3nT1LnKwOAwyXhx++ClGZMVU7d/BVUjh+d/TBrhA/QuQDQErkgX5CehrikbXeks+k9GRI1KA6coYVJDTTImmN04+E8/5FdMfmI7PPRNmE0/j4GtfOQy/lCpvhghRC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxBFgLzf",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_NbtLj/WybNc0qug1en2fx2pYQbkZMFYfQ8hyWGl7wdFidlWP"
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAzeWNdO3UxCcOS9Q9bICW8z/tvMiGhy1nTXtOvXmk5dmp3bBI3nT1LnKwOAwyXhx++ClGZMVU7d/BVUjh+d/TBrhA/QuQDQErkgX5CehrikbXeks+k9GRI1KA6coYVJDTTImmN04+E8/5FdMfmI7PPRNmE0/j4GtfOQy/lCpvhghRC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxBFgLzf",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAzeWNdO3UxCcOS9Q9bICW8z/tvMiGhy1nTXtOvXmk5dmp3bBI3nT1LnKwOAwyXhx++ClGZMVU7d/BVUjh+d/TBrhA/QuQDQErkgX5CehrikbXeks+k9GRI1KA6coYVJDTTImmN04+E8/5FdMfmI7PPRNmE0/j4GtfOQy/lCpvhghRC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxBFgLzf",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAzeWNdO3UxCcOS9Q9bICW8z/tvMiGhy1nTXtOvXmk5dmp3bBI3nT1LnKwOAwyXhx++ClGZMVU7d/BVUjh+d/TBrhA/QuQDQErkgX5CehrikbXeks+k9GRI1KA6coYVJDTTImmN04+E8/5FdMfmI7PPRNmE0/j4GtfOQy/lCpvhghRC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxBFgLzf",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "message": {
        "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "message": {
        "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
  "id": -576460752303423293,
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
  "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
  "id": -576460752303423293,
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "state": "tx_+QENCwH4hLhAzeWNdO3UxCcOS9Q9bICW8z/tvMiGhy1nTXtOvXmk5dmp3bBI3nT1LnKwOAwyXhx++ClGZMVU7d/BVUjh+d/TBrhA/QuQDQErkgX5CehrikbXeks+k9GRI1KA6coYVJDTTImmN04+E8/5FdMfmI7PPRNmE0/j4GtfOQy/lCpvhghRC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxBFgLzf"
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "state": "tx_+QENCwH4hLhAzeWNdO3UxCcOS9Q9bICW8z/tvMiGhy1nTXtOvXmk5dmp3bBI3nT1LnKwOAwyXhx++ClGZMVU7d/BVUjh+d/TBrhA/QuQDQErkgX5CehrikbXeks+k9GRI1KA6coYVJDTTImmN04+E8/5FdMfmI7PPRNmE0/j4GtfOQy/lCpvhghRC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxBFgLzf"
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMBXVz9I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423292,
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
  "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
  "id": -576460752303423292,
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvEAfHsQFMexrqjqnSe5AV2uC5HrLPVRVcS9HbHJnsuBAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAtbCdRY=",
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
  "id": -576460752303423291,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAREy1eNzQoS2nbL0qhcWjFzzpNaGhxmcIZiUskBLh29YYU2nZ6TS1Gb6eBCLUrmQoJjokjFoBosfP2AtFe1poPuEj4RjkCoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIYY+h0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
  "id": -576460752303423291,
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAREy1eNzQoS2nbL0qhcWjFzzpNaGhxmcIZiUskBLh29YYU2nZ6TS1Gb6eBCLUrmQoJjokjFoBosfP2AtFe1poPuEj4RjkCoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIYY+h0",
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
  "id": -576460752303423290,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAREy1eNzQoS2nbL0qhcWjFzzpNaGhxmcIZiUskBLh29YYU2nZ6TS1Gb6eBCLUrmQoJjokjFoBosfP2AtFe1poPuECjie1zH340w7cO6ZwAreu2er+qnnq9zISXgvOUnwyvGJKMbHLqO56c7bBWpvbh3xqgXcLS9ejxCnqaRfKbcyEKuEj4RjkCoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLg0TZU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
  "id": -576460752303423290,
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "state": "tx_+NILAfiEuEAREy1eNzQoS2nbL0qhcWjFzzpNaGhxmcIZiUskBLh29YYU2nZ6TS1Gb6eBCLUrmQoJjokjFoBosfP2AtFe1poPuECjie1zH340w7cO6ZwAreu2er+qnnq9zISXgvOUnwyvGJKMbHLqO56c7bBWpvbh3xqgXcLS9ejxCnqaRfKbcyEKuEj4RjkCoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLg0TZU"
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "state": "tx_+NILAfiEuEAREy1eNzQoS2nbL0qhcWjFzzpNaGhxmcIZiUskBLh29YYU2nZ6TS1Gb6eBCLUrmQoJjokjFoBosfP2AtFe1poPuECjie1zH340w7cO6ZwAreu2er+qnnq9zISXgvOUnwyvGJKMbHLqO56c7bBWpvbh3xqgXcLS9ejxCnqaRfKbcyEKuEj4RjkCoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLg0TZU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423289,
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
  "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
  "id": -576460752303423289,
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
  "id": -576460752303423288,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
  "id": -576460752303423288,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAREy1eNzQoS2nbL0qhcWjFzzpNaGhxmcIZiUskBLh29YYU2nZ6TS1Gb6eBCLUrmQoJjokjFoBosfP2AtFe1poPuECjie1zH340w7cO6ZwAreu2er+qnnq9zISXgvOUnwyvGJKMbHLqO56c7bBWpvbh3xqgXcLS9ejxCnqaRfKbcyEKuEj4RjkCoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLg0TZU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAREy1eNzQoS2nbL0qhcWjFzzpNaGhxmcIZiUskBLh29YYU2nZ6TS1Gb6eBCLUrmQoJjokjFoBosfP2AtFe1poPuECjie1zH340w7cO6ZwAreu2er+qnnq9zISXgvOUnwyvGJKMbHLqO56c7bBWpvbh3xqgXcLS9ejxCnqaRfKbcyEKuEj4RjkCoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLg0TZU",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAREy1eNzQoS2nbL0qhcWjFzzpNaGhxmcIZiUskBLh29YYU2nZ6TS1Gb6eBCLUrmQoJjokjFoBosfP2AtFe1poPuECjie1zH340w7cO6ZwAreu2er+qnnq9zISXgvOUnwyvGJKMbHLqO56c7bBWpvbh3xqgXcLS9ejxCnqaRfKbcyEKuEj4RjkCoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLg0TZU",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
  "id": -576460752303423287,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
  "id": -576460752303423287,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBvEAfHsQFMexrqjqnSe5AV2uC5HrLPVRVcS9HbHJnsuBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAREy1eNzQoS2nbL0qhcWjFzzpNaGhxmcIZiUskBLh29YYU2nZ6TS1Gb6eBCLUrmQoJjokjFoBosfP2AtFe1poPuECjie1zH340w7cO6ZwAreu2er+qnnq9zISXgvOUnwyvGJKMbHLqO56c7bBWpvbh3xqgXcLS9ejxCnqaRfKbcyEKuEj4RjkCoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACGGR7ISegAEjSVG8Q=",
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
    "signed_tx": "tx_+QLACwH4QrhA1oJqeI1REeRQHzZ+eC9g+lsYgPpK9lfvEdpASnYRdSareqeWtAFKCmtPfMVF0m3PTbrOYCEB+LnuhG5p1RI6ALkCd/kCdDcBoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAERMtXjc0KEtp2y9KoXFoxc86TWhocZnCGYlLJAS4dvWGFNp2ek0tRm+ngQi1K5kKCY6JIxaAaLHz9gLRXtaaD7hAo4ntcx9+NMO3DumcAK3rtnq/qp56vcyEl4LzlJ8MrxiSjGxy6juenO2wVqb24d8aoF3C0vXo8Qp6mkXym3MhCrhI+EY5AqEG8QB8exAUx7GuqOqdJ7kBXa4Lkess9VFVxL0dscmey4ECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeyEnoABKTccBD"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA1oJqeI1REeRQHzZ+eC9g+lsYgPpK9lfvEdpASnYRdSareqeWtAFKCmtPfMVF0m3PTbrOYCEB+LnuhG5p1RI6ALkCd/kCdDcBoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAERMtXjc0KEtp2y9KoXFoxc86TWhocZnCGYlLJAS4dvWGFNp2ek0tRm+ngQi1K5kKCY6JIxaAaLHz9gLRXtaaD7hAo4ntcx9+NMO3DumcAK3rtnq/qp56vcyEl4LzlJ8MrxiSjGxy6juenO2wVqb24d8aoF3C0vXo8Qp6mkXym3MhCrhI+EY5AqEG8QB8exAUx7GuqOqdJ7kBXa4Lkess9VFVxL0dscmey4ECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeyEnoABKTccBD",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA1oJqeI1REeRQHzZ+eC9g+lsYgPpK9lfvEdpASnYRdSareqeWtAFKCmtPfMVF0m3PTbrOYCEB+LnuhG5p1RI6ALkCd/kCdDcBoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAERMtXjc0KEtp2y9KoXFoxc86TWhocZnCGYlLJAS4dvWGFNp2ek0tRm+ngQi1K5kKCY6JIxaAaLHz9gLRXtaaD7hAo4ntcx9+NMO3DumcAK3rtnq/qp56vcyEl4LzlJ8MrxiSjGxy6juenO2wVqb24d8aoF3C0vXo8Qp6mkXym3MhCrhI+EY5AqEG8QB8exAUx7GuqOqdJ7kBXa4Lkess9VFVxL0dscmey4ECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeyEnoABKTccBD",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBvEAfHsQFMexrqjqnSe5AV2uC5HrLPVRVcS9HbHJnsuBoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAAG8rawqA==",
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
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECLqpKbpthLMsoUP1ceqd/c1gxZbB3w7vxDDZdlR/gZYPKMD0Vrtn4vZ73e1vkdcRUGI+Bm+dGZjcbjbSyUzn4MuF/4XTgBoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygABqfjOoU="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECLqpKbpthLMsoUP1ceqd/c1gxZbB3w7vxDDZdlR/gZYPKMD0Vrtn4vZ73e1vkdcRUGI+Bm+dGZjcbjbSyUzn4MuF/4XTgBoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygABqfjOoU=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECLqpKbpthLMsoUP1ceqd/c1gxZbB3w7vxDDZdlR/gZYPKMD0Vrtn4vZ73e1vkdcRUGI+Bm+dGZjcbjbSyUzn4MuF/4XTgBoQbxAHx7EBTHsa6o6p0nuQFdrguR6yz1UVXEvR2xyZ7LgaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygABqfjOoU=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
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
    "channel_id": "ch_2q954gwvV99ohJCVvuMyHbpNVM5oE89wiAMB31HFECS4oWYHDm",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3578%5Binitiator44responder%5D
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
      "fsm_id": "ba_GYNCGWmIkTt99iVdJSKLn7ZlYf8+dGExzRyJ6s2WkGbrzicq"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3578%5Binitiator44responder%5D
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
      "fsm_id": "ba_aBpHErelp7yYHLBMoaSAjearx4/I2sFOr4oyZ4AoMlWrtXpn"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsT+14Qww==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423286,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAn+Q0nhsU8YOy2rIsE6E/QpNUBdj5x98eSEnsft4G5W2yT2HMDCAugilB4K1KBPw/WMoW6UNcuyhg+inLzICwLuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LE+KSRvo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423286,
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "fsm_id": "ba_aBpHErelp7yYHLBMoaSAjearx4/I2sFOr4oyZ4AoMlWrtXpn",
      "signed_tx": "tx_+MsLAfhCuEAn+Q0nhsU8YOy2rIsE6E/QpNUBdj5x98eSEnsft4G5W2yT2HMDCAugilB4K1KBPw/WMoW6UNcuyhg+inLzICwLuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LE+KSRvo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423285,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAJ/kNJ4bFPGDstqyLBOhP0KTVAXY+cffHkhJ7H7eBuVtsk9hzAwgLoIpQeCtSgT8P1jKFulDXLsoYPopy8yAsC7hAMZo7bWcqvZi3DB+SdFsc8OgyzA2/+A8C5Uh+98+CJG9kD+O4qGTd8FIaIxm7pCfWcrNyI91mE/afnF3ivcyXBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxOafgaa"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
  "id": -576460752303423285,
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAJ/kNJ4bFPGDstqyLBOhP0KTVAXY+cffHkhJ7H7eBuVtsk9hzAwgLoIpQeCtSgT8P1jKFulDXLsoYPopy8yAsC7hAMZo7bWcqvZi3DB+SdFsc8OgyzA2/+A8C5Uh+98+CJG9kD+O4qGTd8FIaIxm7pCfWcrNyI91mE/afnF3ivcyXBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxOafgaa",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_GYNCGWmIkTt99iVdJSKLn7ZlYf8+dGExzRyJ6s2WkGbrzicq"
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAJ/kNJ4bFPGDstqyLBOhP0KTVAXY+cffHkhJ7H7eBuVtsk9hzAwgLoIpQeCtSgT8P1jKFulDXLsoYPopy8yAsC7hAMZo7bWcqvZi3DB+SdFsc8OgyzA2/+A8C5Uh+98+CJG9kD+O4qGTd8FIaIxm7pCfWcrNyI91mE/afnF3ivcyXBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxOafgaa",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJ/kNJ4bFPGDstqyLBOhP0KTVAXY+cffHkhJ7H7eBuVtsk9hzAwgLoIpQeCtSgT8P1jKFulDXLsoYPopy8yAsC7hAMZo7bWcqvZi3DB+SdFsc8OgyzA2/+A8C5Uh+98+CJG9kD+O4qGTd8FIaIxm7pCfWcrNyI91mE/afnF3ivcyXBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxOafgaa",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJ/kNJ4bFPGDstqyLBOhP0KTVAXY+cffHkhJ7H7eBuVtsk9hzAwgLoIpQeCtSgT8P1jKFulDXLsoYPopy8yAsC7hAMZo7bWcqvZi3DB+SdFsc8OgyzA2/+A8C5Uh+98+CJG9kD+O4qGTd8FIaIxm7pCfWcrNyI91mE/afnF3ivcyXBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxOafgaa",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "message": {
        "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "message": {
        "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
  "id": -576460752303423284,
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
  "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
  "id": -576460752303423284,
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "state": "tx_+QENCwH4hLhAJ/kNJ4bFPGDstqyLBOhP0KTVAXY+cffHkhJ7H7eBuVtsk9hzAwgLoIpQeCtSgT8P1jKFulDXLsoYPopy8yAsC7hAMZo7bWcqvZi3DB+SdFsc8OgyzA2/+A8C5Uh+98+CJG9kD+O4qGTd8FIaIxm7pCfWcrNyI91mE/afnF3ivcyXBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxOafgaa"
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "state": "tx_+QENCwH4hLhAJ/kNJ4bFPGDstqyLBOhP0KTVAXY+cffHkhJ7H7eBuVtsk9hzAwgLoIpQeCtSgT8P1jKFulDXLsoYPopy8yAsC7hAMZo7bWcqvZi3DB+SdFsc8OgyzA2/+A8C5Uh+98+CJG9kD+O4qGTd8FIaIxm7pCfWcrNyI91mE/afnF3ivcyXBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxOafgaa"
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMBXVz9I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423283,
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
  "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
  "id": -576460752303423283,
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBh/R7toEYjlYMnUg672CMuj8ks3+uPr9/9vAe+BQ9ibTAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAq2MHXY=",
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
  "id": -576460752303423282,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAU194SrUj3IgwtwJGMqAoltROEDbsKWVUiwgZP8Znxiepu82gqvcaH3f6/tu8PpdFVrcIRlrPrippvTaBJJcELuEj4RjkCoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm0wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKxk7pY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
  "id": -576460752303423282,
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAU194SrUj3IgwtwJGMqAoltROEDbsKWVUiwgZP8Znxiepu82gqvcaH3f6/tu8PpdFVrcIRlrPrippvTaBJJcELuEj4RjkCoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm0wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKxk7pY",
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
  "id": -576460752303423281,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAU194SrUj3IgwtwJGMqAoltROEDbsKWVUiwgZP8Znxiepu82gqvcaH3f6/tu8PpdFVrcIRlrPrippvTaBJJcELuECpv1aH6ZwQm9r0Tr9RA4Fa+vXQ0yVjMTkdGiK9sAihiNeLKjb1tcHYvX64rF+C5/2uWf2IsRBnW/Q+8be+KGIBuEj4RjkCoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm0wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIaQ6aX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
  "id": -576460752303423281,
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "state": "tx_+NILAfiEuEAU194SrUj3IgwtwJGMqAoltROEDbsKWVUiwgZP8Znxiepu82gqvcaH3f6/tu8PpdFVrcIRlrPrippvTaBJJcELuECpv1aH6ZwQm9r0Tr9RA4Fa+vXQ0yVjMTkdGiK9sAihiNeLKjb1tcHYvX64rF+C5/2uWf2IsRBnW/Q+8be+KGIBuEj4RjkCoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm0wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIaQ6aX"
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "state": "tx_+NILAfiEuEAU194SrUj3IgwtwJGMqAoltROEDbsKWVUiwgZP8Znxiepu82gqvcaH3f6/tu8PpdFVrcIRlrPrippvTaBJJcELuECpv1aH6ZwQm9r0Tr9RA4Fa+vXQ0yVjMTkdGiK9sAihiNeLKjb1tcHYvX64rF+C5/2uWf2IsRBnW/Q+8be+KGIBuEj4RjkCoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm0wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIaQ6aX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423280,
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
  "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
  "id": -576460752303423280,
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
  "id": -576460752303423279,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
  "id": -576460752303423279,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAU194SrUj3IgwtwJGMqAoltROEDbsKWVUiwgZP8Znxiepu82gqvcaH3f6/tu8PpdFVrcIRlrPrippvTaBJJcELuECpv1aH6ZwQm9r0Tr9RA4Fa+vXQ0yVjMTkdGiK9sAihiNeLKjb1tcHYvX64rF+C5/2uWf2IsRBnW/Q+8be+KGIBuEj4RjkCoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm0wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIaQ6aX",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAU194SrUj3IgwtwJGMqAoltROEDbsKWVUiwgZP8Znxiepu82gqvcaH3f6/tu8PpdFVrcIRlrPrippvTaBJJcELuECpv1aH6ZwQm9r0Tr9RA4Fa+vXQ0yVjMTkdGiK9sAihiNeLKjb1tcHYvX64rF+C5/2uWf2IsRBnW/Q+8be+KGIBuEj4RjkCoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm0wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIaQ6aX",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAU194SrUj3IgwtwJGMqAoltROEDbsKWVUiwgZP8Znxiepu82gqvcaH3f6/tu8PpdFVrcIRlrPrippvTaBJJcELuECpv1aH6ZwQm9r0Tr9RA4Fa+vXQ0yVjMTkdGiK9sAihiNeLKjb1tcHYvX64rF+C5/2uWf2IsRBnW/Q+8be+KGIBuEj4RjkCoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm0wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIaQ6aX",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
  "id": -576460752303423278,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
  "id": -576460752303423278,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBh/R7toEYjlYMnUg672CMuj8ks3+uPr9/9vAe+BQ9ibToQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEAU194SrUj3IgwtwJGMqAoltROEDbsKWVUiwgZP8Znxiepu82gqvcaH3f6/tu8PpdFVrcIRlrPrippvTaBJJcELuECpv1aH6ZwQm9r0Tr9RA4Fa+vXQ0yVjMTkdGiK9sAihiNeLKjb1tcHYvX64rF+C5/2uWf2IsRBnW/Q+8be+KGIBuEj4RjkCoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm0wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACGGR7ISegAB+pXdm0=",
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
    "signed_tx": "tx_+QLACwH4QrhABaitXO1iLLfEVOFeQkr+hsgxByDNyx7Ln1TdGQX1vM22dO3fwrssXqrvxABXjgT4vo6WnwNgm+/fCj/mufBcCbkCd/kCdDcBoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm06EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAFNfeEq1I9yIMLcCRjKgKJbUThA27CllVIsIGT/GZ8YnqbvNoKr3Gh93+v7bvD6XRVa3CEZaz64qab02gSSXBC7hAqb9Wh+mcEJva9E6/UQOBWvr10NMlYzE5HRoivbAIoYjXiyo29bXB2L1+uKxfguf9rln9iLEQZ1v0PvG3vihiAbhI+EY5AqEGH9Hu2gRiOVgydSDrvYIy6PySzf64+v3/28B74FD2JtMCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeyEnoAAcdfF8e"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhABaitXO1iLLfEVOFeQkr+hsgxByDNyx7Ln1TdGQX1vM22dO3fwrssXqrvxABXjgT4vo6WnwNgm+/fCj/mufBcCbkCd/kCdDcBoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm06EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAFNfeEq1I9yIMLcCRjKgKJbUThA27CllVIsIGT/GZ8YnqbvNoKr3Gh93+v7bvD6XRVa3CEZaz64qab02gSSXBC7hAqb9Wh+mcEJva9E6/UQOBWvr10NMlYzE5HRoivbAIoYjXiyo29bXB2L1+uKxfguf9rln9iLEQZ1v0PvG3vihiAbhI+EY5AqEGH9Hu2gRiOVgydSDrvYIy6PySzf64+v3/28B74FD2JtMCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeyEnoAAcdfF8e",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhABaitXO1iLLfEVOFeQkr+hsgxByDNyx7Ln1TdGQX1vM22dO3fwrssXqrvxABXjgT4vo6WnwNgm+/fCj/mufBcCbkCd/kCdDcBoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm06EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAFNfeEq1I9yIMLcCRjKgKJbUThA27CllVIsIGT/GZ8YnqbvNoKr3Gh93+v7bvD6XRVa3CEZaz64qab02gSSXBC7hAqb9Wh+mcEJva9E6/UQOBWvr10NMlYzE5HRoivbAIoYjXiyo29bXB2L1+uKxfguf9rln9iLEQZ1v0PvG3vihiAbhI+EY5AqEGH9Hu2gRiOVgydSDrvYIy6PySzf64+v3/28B74FD2JtMCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeyEnoAAcdfF8e",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBh/R7toEYjlYMnUg672CMuj8ks3+uPr9/9vAe+BQ9ibToQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAAIq1tkIA==",
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
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEA6ULkI1Ijv5l2sb16kplk6M8Vqk9OBYCACpNNcWLI7WqyS/S3zBbot+148U2W+i+ur4itAtdnpkyZMhvU/LDYOuF/4XTgBoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm06EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygACO9AeBw="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA6ULkI1Ijv5l2sb16kplk6M8Vqk9OBYCACpNNcWLI7WqyS/S3zBbot+148U2W+i+ur4itAtdnpkyZMhvU/LDYOuF/4XTgBoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm06EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygACO9AeBw=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA6ULkI1Ijv5l2sb16kplk6M8Vqk9OBYCACpNNcWLI7WqyS/S3zBbot+148U2W+i+ur4itAtdnpkyZMhvU/LDYOuF/4XTgBoQYf0e7aBGI5WDJ1IOu9gjLo/JLN/rj6/f/bwHvgUPYm06EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygACO9AeBw=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
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
    "channel_id": "ch_F1oRrWxAjk5o7N8WeS5b4gtMt9UKrMkxssob15XSyF4fX2vBJ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
