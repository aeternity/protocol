
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
      "fsm_id": "ba_AdOJfu0h2gX8U7vJHQDiUXfolrFqkWK0v0TbQuVi9Ue+kAcb"
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
      "fsm_id": "ba_EWtC/ZCp4duohjyhI4gNyKNUzyOrsX7X38o5zWPI5yxbQtz8"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBofLrulo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422247,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBnhEtB1qwo3aKwr61DAZ4ABAL+XkBgwLw0ewzZH9Obx5yLpVWyD7YBT9oGZWhwEDpYDBkOgtKQ/mwGUOCN2FgBuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgaEj7n+Z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422247,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "fsm_id": "ba_EWtC/ZCp4duohjyhI4gNyKNUzyOrsX7X38o5zWPI5yxbQtz8",
      "signed_tx": "tx_+MwLAfhCuEBnhEtB1qwo3aKwr61DAZ4ABAL+XkBgwLw0ewzZH9Obx5yLpVWyD7YBT9oGZWhwEDpYDBkOgtKQ/mwGUOCN2FgBuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgaEj7n+Z",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422246,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhALKaW5MM0HwzMziK/qQ2FoQ/sqnHql9s6sEjObSJrA2jaRSjPFcvmHbiNO/E02eJWoVz0bpGLoPjBRKAtQ53jArhAZ4RLQdasKN2isK+tQwGeAAQC/l5AYMC8NHsM2R/Tm8eci6VVsg+2AU/aBmVocBA6WAwZDoLSkP5sBlDgjdhYAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GhV4ehdQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422246,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhALKaW5MM0HwzMziK/qQ2FoQ/sqnHql9s6sEjObSJrA2jaRSjPFcvmHbiNO/E02eJWoVz0bpGLoPjBRKAtQ53jArhAZ4RLQdasKN2isK+tQwGeAAQC/l5AYMC8NHsM2R/Tm8eci6VVsg+2AU/aBmVocBA6WAwZDoLSkP5sBlDgjdhYAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GhV4ehdQ==",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_AdOJfu0h2gX8U7vJHQDiUXfolrFqkWK0v0TbQuVi9Ue+kAcb"
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhALKaW5MM0HwzMziK/qQ2FoQ/sqnHql9s6sEjObSJrA2jaRSjPFcvmHbiNO/E02eJWoVz0bpGLoPjBRKAtQ53jArhAZ4RLQdasKN2isK+tQwGeAAQC/l5AYMC8NHsM2R/Tm8eci6VVsg+2AU/aBmVocBA6WAwZDoLSkP5sBlDgjdhYAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GhV4ehdQ==",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhALKaW5MM0HwzMziK/qQ2FoQ/sqnHql9s6sEjObSJrA2jaRSjPFcvmHbiNO/E02eJWoVz0bpGLoPjBRKAtQ53jArhAZ4RLQdasKN2isK+tQwGeAAQC/l5AYMC8NHsM2R/Tm8eci6VVsg+2AU/aBmVocBA6WAwZDoLSkP5sBlDgjdhYAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GhV4ehdQ==",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhALKaW5MM0HwzMziK/qQ2FoQ/sqnHql9s6sEjObSJrA2jaRSjPFcvmHbiNO/E02eJWoVz0bpGLoPjBRKAtQ53jArhAZ4RLQdasKN2isK+tQwGeAAQC/l5AYMC8NHsM2R/Tm8eci6VVsg+2AU/aBmVocBA6WAwZDoLSkP5sBlDgjdhYAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GhV4ehdQ==",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "message": {
        "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "message": {
        "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
  "id": -576460752303422245,
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
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422245,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "state": "tx_+QEOCwH4hLhALKaW5MM0HwzMziK/qQ2FoQ/sqnHql9s6sEjObSJrA2jaRSjPFcvmHbiNO/E02eJWoVz0bpGLoPjBRKAtQ53jArhAZ4RLQdasKN2isK+tQwGeAAQC/l5AYMC8NHsM2R/Tm8eci6VVsg+2AU/aBmVocBA6WAwZDoLSkP5sBlDgjdhYAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GhV4ehdQ=="
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "state": "tx_+QEOCwH4hLhALKaW5MM0HwzMziK/qQ2FoQ/sqnHql9s6sEjObSJrA2jaRSjPFcvmHbiNO/E02eJWoVz0bpGLoPjBRKAtQ53jArhAZ4RLQdasKN2isK+tQwGeAAQC/l5AYMC8NHsM2R/Tm8eci6VVsg+2AU/aBmVocBA6WAwZDoLSkP5sBlDgjdhYAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GhV4ehdQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422244,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422244,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEOCwH4hLhALKaW5MM0HwzMziK/qQ2FoQ/sqnHql9s6sEjObSJrA2jaRSjPFcvmHbiNO/E02eJWoVz0bpGLoPjBRKAtQ53jArhAZ4RLQdasKN2isK+tQwGeAAQC/l5AYMC8NHsM2R/Tm8eci6VVsg+2AU/aBmVocBA6WAwZDoLSkP5sBlDgjdhYAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GhV4ehdQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422243,
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
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422243,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBq0Wq77CFZ3DzaDCfs9DFYqa9l/TpH4t+n69CJ8AafKCAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAi5LR/4=",
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
  "id": -576460752303422242,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAdT0wMXLZ4RTZN0uJvKqf18yvq6LRJQfUzHjcv2VaWA6d0sAnfYjQ/pKbof9050Uz0RwxalXzXpO/ceRljbfIFuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLURrCv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422242,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAdT0wMXLZ4RTZN0uJvKqf18yvq6LRJQfUzHjcv2VaWA6d0sAnfYjQ/pKbof9050Uz0RwxalXzXpO/ceRljbfIFuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLURrCv",
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
  "id": -576460752303422241,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAHm26QS5C6sDEWLncx43U0XoqSgZ2d2hE348b2Cdm9WCYkgOwOfEjZuzJcA45qB9mtrIKj8mDyNuKMT6p/GWIIuEAdT0wMXLZ4RTZN0uJvKqf18yvq6LRJQfUzHjcv2VaWA6d0sAnfYjQ/pKbof9050Uz0RwxalXzXpO/ceRljbfIFuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKDVMrt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422241,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "state": "tx_+NILAfiEuEAHm26QS5C6sDEWLncx43U0XoqSgZ2d2hE348b2Cdm9WCYkgOwOfEjZuzJcA45qB9mtrIKj8mDyNuKMT6p/GWIIuEAdT0wMXLZ4RTZN0uJvKqf18yvq6LRJQfUzHjcv2VaWA6d0sAnfYjQ/pKbof9050Uz0RwxalXzXpO/ceRljbfIFuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKDVMrt"
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "state": "tx_+NILAfiEuEAHm26QS5C6sDEWLncx43U0XoqSgZ2d2hE348b2Cdm9WCYkgOwOfEjZuzJcA45qB9mtrIKj8mDyNuKMT6p/GWIIuEAdT0wMXLZ4RTZN0uJvKqf18yvq6LRJQfUzHjcv2VaWA6d0sAnfYjQ/pKbof9050Uz0RwxalXzXpO/ceRljbfIFuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKDVMrt"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422240,
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
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422240,
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
  "id": -576460752303422239,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422239,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAHm26QS5C6sDEWLncx43U0XoqSgZ2d2hE348b2Cdm9WCYkgOwOfEjZuzJcA45qB9mtrIKj8mDyNuKMT6p/GWIIuEAdT0wMXLZ4RTZN0uJvKqf18yvq6LRJQfUzHjcv2VaWA6d0sAnfYjQ/pKbof9050Uz0RwxalXzXpO/ceRljbfIFuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKDVMrt",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422238,
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
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422238,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBq0Wq77CFZ3DzaDCfs9DFYqa9l/TpH4t+n69CJ8AafKCA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCyN/iNk=",
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
  "id": -576460752303422237,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAiRG2CFJI4RrP9RVRp39fH6lgO6oefAZhttqvJGpEg4/2n19oXnQJlotLrg7E3RYX4RvkfXwASwgQU+GXXUTsBuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguIqDkF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422237,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAiRG2CFJI4RrP9RVRp39fH6lgO6oefAZhttqvJGpEg4/2n19oXnQJlotLrg7E3RYX4RvkfXwASwgQU+GXXUTsBuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguIqDkF",
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
  "id": -576460752303422236,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAiRG2CFJI4RrP9RVRp39fH6lgO6oefAZhttqvJGpEg4/2n19oXnQJlotLrg7E3RYX4RvkfXwASwgQU+GXXUTsBuECuvtpwJIEmFMFKDzbrZTPKXDohi7k13uzMqfetgdoZlcccIyfLGQU5hcYBW3+b38MTptUd3kcKHNLC3G8jH4wBuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs7MoS1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422236,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "state": "tx_+NILAfiEuEAiRG2CFJI4RrP9RVRp39fH6lgO6oefAZhttqvJGpEg4/2n19oXnQJlotLrg7E3RYX4RvkfXwASwgQU+GXXUTsBuECuvtpwJIEmFMFKDzbrZTPKXDohi7k13uzMqfetgdoZlcccIyfLGQU5hcYBW3+b38MTptUd3kcKHNLC3G8jH4wBuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs7MoS1"
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "state": "tx_+NILAfiEuEAiRG2CFJI4RrP9RVRp39fH6lgO6oefAZhttqvJGpEg4/2n19oXnQJlotLrg7E3RYX4RvkfXwASwgQU+GXXUTsBuECuvtpwJIEmFMFKDzbrZTPKXDohi7k13uzMqfetgdoZlcccIyfLGQU5hcYBW3+b38MTptUd3kcKHNLC3G8jH4wBuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs7MoS1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422235,
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
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422235,
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
  "id": -576460752303422234,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422234,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAiRG2CFJI4RrP9RVRp39fH6lgO6oefAZhttqvJGpEg4/2n19oXnQJlotLrg7E3RYX4RvkfXwASwgQU+GXXUTsBuECuvtpwJIEmFMFKDzbrZTPKXDohi7k13uzMqfetgdoZlcccIyfLGQU5hcYBW3+b38MTptUd3kcKHNLC3G8jH4wBuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs7MoS1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "signed_tx": "tx_+QExCwHAuQEr+QEoOwGhBq0Wq77CFZ3DzaDCfs9DFYqa9l/TpH4t+n69CJ8AafKCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAiRG2CFJI4RrP9RVRp39fH6lgO6oefAZhttqvJGpEg4/2n19oXnQJlotLrg7E3RYX4RvkfXwASwgQU+GXXUTsBuECuvtpwJIEmFMFKDzbrZTPKXDohi7k13uzMqfetgdoZlcccIyfLGQU5hcYBW3+b38MTptUd3kcKHNLC3G8jH4wBuEj4RjkCoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnyggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMUyXKIAIMS1oe+uCiE",
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
  "method": "channels.snapshot_solo_sign",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBq0Wq77CFZ3DzaDCfs9DFYqa9l/TpH4t+n69CJ8AafKCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBohoDdIk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422233,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEAxuLC8WioBcFxOJNxaeacBHKttOaAKUQxXfJLeah87Cr42Gm+gmEIDcwru4szfp6krz3xu/IM+XtM6ngDKRVwHuGD4XjUBoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnygqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaKJovDD"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422233,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEAxuLC8WioBcFxOJNxaeacBHKttOaAKUQxXfJLeah87Cr42Gm+gmEIDcwru4szfp6krz3xu/IM+XtM6ngDKRVwHuGD4XjUBoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnygqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaKJovDD",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422232,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAxuLC8WioBcFxOJNxaeacBHKttOaAKUQxXfJLeah87Cr42Gm+gmEIDcwru4szfp6krz3xu/IM+XtM6ngDKRVwHuEDiB4f6nDnE3Wr41IxaMhag3iCqUiMzBtG5z6tTWdhFtpJegAVt6oR2djcHj7GxBa9tV8dRCC5K9gH/8UcRaq8DuGD4XjUBoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnygqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaIfCy1J"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
  "id": -576460752303422232,
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAxuLC8WioBcFxOJNxaeacBHKttOaAKUQxXfJLeah87Cr42Gm+gmEIDcwru4szfp6krz3xu/IM+XtM6ngDKRVwHuEDiB4f6nDnE3Wr41IxaMhag3iCqUiMzBtG5z6tTWdhFtpJegAVt6oR2djcHj7GxBa9tV8dRCC5K9gH/8UcRaq8DuGD4XjUBoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnygqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaIfCy1J",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAxuLC8WioBcFxOJNxaeacBHKttOaAKUQxXfJLeah87Cr42Gm+gmEIDcwru4szfp6krz3xu/IM+XtM6ngDKRVwHuEDiB4f6nDnE3Wr41IxaMhag3iCqUiMzBtG5z6tTWdhFtpJegAVt6oR2djcHj7GxBa9tV8dRCC5K9gH/8UcRaq8DuGD4XjUBoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnygqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaIfCy1J",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAxuLC8WioBcFxOJNxaeacBHKttOaAKUQxXfJLeah87Cr42Gm+gmEIDcwru4szfp6krz3xu/IM+XtM6ngDKRVwHuEDiB4f6nDnE3Wr41IxaMhag3iCqUiMzBtG5z6tTWdhFtpJegAVt6oR2djcHj7GxBa9tV8dRCC5K9gH/8UcRaq8DuGD4XjUBoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnygqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaIfCy1J",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAxuLC8WioBcFxOJNxaeacBHKttOaAKUQxXfJLeah87Cr42Gm+gmEIDcwru4szfp6krz3xu/IM+XtM6ngDKRVwHuEDiB4f6nDnE3Wr41IxaMhag3iCqUiMzBtG5z6tTWdhFtpJegAVt6oR2djcHj7GxBa9tV8dRCC5K9gH/8UcRaq8DuGD4XjUBoQatFqu+whWdw82gwn7PQxWKmvZf06R+Lfp+vQifAGnygqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaIfCy1J",
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
      "fsm_id": "ba_slfC8iNljoTg82BENstm6GE/+eKfZRoT/aLnOPdrBIQYoNQe"
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
      "fsm_id": "ba_uwfZO1rLvTG4N8vXeONpaElu1EKf2R8G7wpiKSoBeHxTs+JG"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBo6wKwi4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422231,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBKtNvmUTLfz8jnY8ciLQtPIM1EGf4J6svO9odyR1Y/A2Fng3mvqbuFTbPwsdELqw56evCMoHlczCzqZnrr9tAAuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgaOWTkva"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422231,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "fsm_id": "ba_uwfZO1rLvTG4N8vXeONpaElu1EKf2R8G7wpiKSoBeHxTs+JG",
      "signed_tx": "tx_+MwLAfhCuEBKtNvmUTLfz8jnY8ciLQtPIM1EGf4J6svO9odyR1Y/A2Fng3mvqbuFTbPwsdELqw56evCMoHlczCzqZnrr9tAAuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgaOWTkva",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422230,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhASrTb5lEy38/I52PHIi0LTyDNRBn+CerLzvaHckdWPwNhZ4N5r6m7hU2z8LHRC6sOenrwjKB5XMws6mZ66/bQALhAWsv9toPhajL6qx6TJjdNF80NKSwS2NzsjKHVLS4gFPDGQnjNIxsYS/fNHEQX4u4Hq0WWr/a0f3QOTUvz+PGkBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GjiaODCw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422230,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhASrTb5lEy38/I52PHIi0LTyDNRBn+CerLzvaHckdWPwNhZ4N5r6m7hU2z8LHRC6sOenrwjKB5XMws6mZ66/bQALhAWsv9toPhajL6qx6TJjdNF80NKSwS2NzsjKHVLS4gFPDGQnjNIxsYS/fNHEQX4u4Hq0WWr/a0f3QOTUvz+PGkBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GjiaODCw==",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_slfC8iNljoTg82BENstm6GE/+eKfZRoT/aLnOPdrBIQYoNQe"
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhASrTb5lEy38/I52PHIi0LTyDNRBn+CerLzvaHckdWPwNhZ4N5r6m7hU2z8LHRC6sOenrwjKB5XMws6mZ66/bQALhAWsv9toPhajL6qx6TJjdNF80NKSwS2NzsjKHVLS4gFPDGQnjNIxsYS/fNHEQX4u4Hq0WWr/a0f3QOTUvz+PGkBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GjiaODCw==",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhASrTb5lEy38/I52PHIi0LTyDNRBn+CerLzvaHckdWPwNhZ4N5r6m7hU2z8LHRC6sOenrwjKB5XMws6mZ66/bQALhAWsv9toPhajL6qx6TJjdNF80NKSwS2NzsjKHVLS4gFPDGQnjNIxsYS/fNHEQX4u4Hq0WWr/a0f3QOTUvz+PGkBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GjiaODCw==",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhASrTb5lEy38/I52PHIi0LTyDNRBn+CerLzvaHckdWPwNhZ4N5r6m7hU2z8LHRC6sOenrwjKB5XMws6mZ66/bQALhAWsv9toPhajL6qx6TJjdNF80NKSwS2NzsjKHVLS4gFPDGQnjNIxsYS/fNHEQX4u4Hq0WWr/a0f3QOTUvz+PGkBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GjiaODCw==",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
    "data": {
      "event": "died"
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2KEKGMJH91fUaw7fWbSAdVzibVXT2gF1MZe2CdMU1fhTnSNSbX",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "message": {
        "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "message": {
        "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
  "id": -576460752303422229,
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
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422229,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "state": "tx_+QEOCwH4hLhASrTb5lEy38/I52PHIi0LTyDNRBn+CerLzvaHckdWPwNhZ4N5r6m7hU2z8LHRC6sOenrwjKB5XMws6mZ66/bQALhAWsv9toPhajL6qx6TJjdNF80NKSwS2NzsjKHVLS4gFPDGQnjNIxsYS/fNHEQX4u4Hq0WWr/a0f3QOTUvz+PGkBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GjiaODCw=="
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "state": "tx_+QEOCwH4hLhASrTb5lEy38/I52PHIi0LTyDNRBn+CerLzvaHckdWPwNhZ4N5r6m7hU2z8LHRC6sOenrwjKB5XMws6mZ66/bQALhAWsv9toPhajL6qx6TJjdNF80NKSwS2NzsjKHVLS4gFPDGQnjNIxsYS/fNHEQX4u4Hq0WWr/a0f3QOTUvz+PGkBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GjiaODCw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422228,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422228,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEOCwH4hLhASrTb5lEy38/I52PHIi0LTyDNRBn+CerLzvaHckdWPwNhZ4N5r6m7hU2z8LHRC6sOenrwjKB5XMws6mZ66/bQALhAWsv9toPhajL6qx6TJjdNF80NKSwS2NzsjKHVLS4gFPDGQnjNIxsYS/fNHEQX4u4Hq0WWr/a0f3QOTUvz+PGkBLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GjiaODCw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422227,
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
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422227,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvTONM2RgtBXLlICQDzeLgu0I7qC+/2/Nlm0UQ44c45AAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAjkNNbI=",
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
  "id": -576460752303422226,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBeyruVIlmw4bSrVd0+K9jwQJuLRNunsLCXtddSRUfFUK76u1qCVlO3ntrmwPvi+XgGSMsPsNYUP+qZ4S4A+jsBuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLQP4HF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422226,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBeyruVIlmw4bSrVd0+K9jwQJuLRNunsLCXtddSRUfFUK76u1qCVlO3ntrmwPvi+XgGSMsPsNYUP+qZ4S4A+jsBuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLQP4HF",
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
  "id": -576460752303422225,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBeyruVIlmw4bSrVd0+K9jwQJuLRNunsLCXtddSRUfFUK76u1qCVlO3ntrmwPvi+XgGSMsPsNYUP+qZ4S4A+jsBuEDEV1ZWsOZydvHkP3HAmNKNZn+TB0OnWqHM8bdYNbbVITUHJLoDCLZ5OP3+YRC6LJ6JdtqXhJayeHRSEu1iveUFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1NCsH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422225,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "state": "tx_+NILAfiEuEBeyruVIlmw4bSrVd0+K9jwQJuLRNunsLCXtddSRUfFUK76u1qCVlO3ntrmwPvi+XgGSMsPsNYUP+qZ4S4A+jsBuEDEV1ZWsOZydvHkP3HAmNKNZn+TB0OnWqHM8bdYNbbVITUHJLoDCLZ5OP3+YRC6LJ6JdtqXhJayeHRSEu1iveUFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1NCsH"
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "state": "tx_+NILAfiEuEBeyruVIlmw4bSrVd0+K9jwQJuLRNunsLCXtddSRUfFUK76u1qCVlO3ntrmwPvi+XgGSMsPsNYUP+qZ4S4A+jsBuEDEV1ZWsOZydvHkP3HAmNKNZn+TB0OnWqHM8bdYNbbVITUHJLoDCLZ5OP3+YRC6LJ6JdtqXhJayeHRSEu1iveUFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1NCsH"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422224,
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
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422224,
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
  "id": -576460752303422223,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422223,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBeyruVIlmw4bSrVd0+K9jwQJuLRNunsLCXtddSRUfFUK76u1qCVlO3ntrmwPvi+XgGSMsPsNYUP+qZ4S4A+jsBuEDEV1ZWsOZydvHkP3HAmNKNZn+TB0OnWqHM8bdYNbbVITUHJLoDCLZ5OP3+YRC6LJ6JdtqXhJayeHRSEu1iveUFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1NCsH",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422222,
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
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422222,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvTONM2RgtBXLlICQDzeLgu0I7qC+/2/Nlm0UQ44c45AA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC8g9z1s=",
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
  "id": -576460752303422221,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECu17hfVh3Lsxm0ah2rFX5N3+ZQgcw4fXYEUBAikCfsVBW7FB/mLMndHPq73272P+bFxSw1LUx0/77bZ7wpEYkFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvMVdy6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422221,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "signed_tx": "tx_+JALAfhCuECu17hfVh3Lsxm0ah2rFX5N3+ZQgcw4fXYEUBAikCfsVBW7FB/mLMndHPq73272P+bFxSw1LUx0/77bZ7wpEYkFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvMVdy6",
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
  "id": -576460752303422220,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBGKECTTj4iHgHyB7paxdIjZNghZOSHWAIWyexbIxasTwW7xIYq7+axW9pTMOIQqCV6U2zNgCu16VANrzvQ9+YLuECu17hfVh3Lsxm0ah2rFX5N3+ZQgcw4fXYEUBAikCfsVBW7FB/mLMndHPq73272P+bFxSw1LUx0/77bZ7wpEYkFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt4yVL1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422220,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "state": "tx_+NILAfiEuEBGKECTTj4iHgHyB7paxdIjZNghZOSHWAIWyexbIxasTwW7xIYq7+axW9pTMOIQqCV6U2zNgCu16VANrzvQ9+YLuECu17hfVh3Lsxm0ah2rFX5N3+ZQgcw4fXYEUBAikCfsVBW7FB/mLMndHPq73272P+bFxSw1LUx0/77bZ7wpEYkFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt4yVL1"
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "state": "tx_+NILAfiEuEBGKECTTj4iHgHyB7paxdIjZNghZOSHWAIWyexbIxasTwW7xIYq7+axW9pTMOIQqCV6U2zNgCu16VANrzvQ9+YLuECu17hfVh3Lsxm0ah2rFX5N3+ZQgcw4fXYEUBAikCfsVBW7FB/mLMndHPq73272P+bFxSw1LUx0/77bZ7wpEYkFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt4yVL1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422219,
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
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422219,
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
  "id": -576460752303422218,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422218,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBGKECTTj4iHgHyB7paxdIjZNghZOSHWAIWyexbIxasTwW7xIYq7+axW9pTMOIQqCV6U2zNgCu16VANrzvQ9+YLuECu17hfVh3Lsxm0ah2rFX5N3+ZQgcw4fXYEUBAikCfsVBW7FB/mLMndHPq73272P+bFxSw1LUx0/77bZ7wpEYkFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt4yVL1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "signed_tx": "tx_+QExCwHAuQEr+QEoOwGhBvTONM2RgtBXLlICQDzeLgu0I7qC+/2/Nlm0UQ44c45AoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEBGKECTTj4iHgHyB7paxdIjZNghZOSHWAIWyexbIxasTwW7xIYq7+axW9pTMOIQqCV6U2zNgCu16VANrzvQ9+YLuECu17hfVh3Lsxm0ah2rFX5N3+ZQgcw4fXYEUBAikCfsVBW7FB/mLMndHPq73272P+bFxSw1LUx0/77bZ7wpEYkFuEj4RjkCoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMUyXKIAIMS1odroEV7",
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
  "method": "channels.snapshot_solo_sign",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBvTONM2RgtBXLlICQDzeLgu0I7qC+/2/Nlm0UQ44c45AoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBpNyk/GI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422217,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEDx2m1BDhb7QTuAZQCx6ubluXbMUDDOCjOqc/mCK+hygdppLzoSvMJjtQgzb0VnQf0IKbb0+cvhUDn5yfCC31UOuGD4XjUBoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaR3tRFp"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422217,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEDx2m1BDhb7QTuAZQCx6ubluXbMUDDOCjOqc/mCK+hygdppLzoSvMJjtQgzb0VnQf0IKbb0+cvhUDn5yfCC31UOuGD4XjUBoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaR3tRFp",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422216,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAdvuCvi1YXRskIEHymsijFrDSa37ZUkfkv/ldV7Xmx5bak2n9y3ITxytP5rEszpCQSJuDYfSDJGIby9WC9OWcMuEDx2m1BDhb7QTuAZQCx6ubluXbMUDDOCjOqc/mCK+hygdppLzoSvMJjtQgzb0VnQf0IKbb0+cvhUDn5yfCC31UOuGD4XjUBoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaRDQ+YD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
  "id": -576460752303422216,
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAdvuCvi1YXRskIEHymsijFrDSa37ZUkfkv/ldV7Xmx5bak2n9y3ITxytP5rEszpCQSJuDYfSDJGIby9WC9OWcMuEDx2m1BDhb7QTuAZQCx6ubluXbMUDDOCjOqc/mCK+hygdppLzoSvMJjtQgzb0VnQf0IKbb0+cvhUDn5yfCC31UOuGD4XjUBoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaRDQ+YD",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAdvuCvi1YXRskIEHymsijFrDSa37ZUkfkv/ldV7Xmx5bak2n9y3ITxytP5rEszpCQSJuDYfSDJGIby9WC9OWcMuEDx2m1BDhb7QTuAZQCx6ubluXbMUDDOCjOqc/mCK+hygdppLzoSvMJjtQgzb0VnQf0IKbb0+cvhUDn5yfCC31UOuGD4XjUBoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaRDQ+YD",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAdvuCvi1YXRskIEHymsijFrDSa37ZUkfkv/ldV7Xmx5bak2n9y3ITxytP5rEszpCQSJuDYfSDJGIby9WC9OWcMuEDx2m1BDhb7QTuAZQCx6ubluXbMUDDOCjOqc/mCK+hygdppLzoSvMJjtQgzb0VnQf0IKbb0+cvhUDn5yfCC31UOuGD4XjUBoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaRDQ+YD",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAdvuCvi1YXRskIEHymsijFrDSa37ZUkfkv/ldV7Xmx5bak2n9y3ITxytP5rEszpCQSJuDYfSDJGIby9WC9OWcMuEDx2m1BDhb7QTuAZQCx6ubluXbMUDDOCjOqc/mCK+hygdppLzoSvMJjtQgzb0VnQf0IKbb0+cvhUDn5yfCC31UOuGD4XjUBoQb0zjTNkYLQVy5SAkA83i4LtCO6gvv9vzZZtFEOOHOOQKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgaRDQ+YD",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
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
    "channel_id": "ch_2rpEDBmnzjvus1jfR4brmLokjqMhaFFcDZgoQXR63iUMpG8Yxe",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
