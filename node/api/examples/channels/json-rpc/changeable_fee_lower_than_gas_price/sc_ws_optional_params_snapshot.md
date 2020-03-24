
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
      "fsm_id": "ba_odRLnKsAd3TA8BeQcGTEHrRIMMBkl2SS5AQF1FSFQA8lDd8G"
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
      "fsm_id": "ba_5F2uYMab14HIHEMKJJpezPLfwgP/kMy71OUBx8c6kEwQwtC+"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBhyWP4/Q=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422380,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECOEqhudW0k+JF6QHh0ok9IdgJ6ZSsbHtVj/052pSlazPxGYI0g23VsS4gkK+xV5kz7xVLDOkAGeO5xQSkolpIEuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYeAlpmR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422380,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "fsm_id": "ba_5F2uYMab14HIHEMKJJpezPLfwgP/kMy71OUBx8c6kEwQwtC+",
      "signed_tx": "tx_+MwLAfhCuECOEqhudW0k+JF6QHh0ok9IdgJ6ZSsbHtVj/052pSlazPxGYI0g23VsS4gkK+xV5kz7xVLDOkAGeO5xQSkolpIEuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYeAlpmR",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422379,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAjhKobnVtJPiRekB4dKJPSHYCemUrGx7VY/9OdqUpWsz8RmCNINt1bEuIJCvsVeZM+8VSwzpABnjucUEpKJaSBLhAqxTPWEaDwU16PiZOxKOH+QoRAdkbD6bxsML6iUADqndzhXp/F143J9wxWfvFnZnjAykA7AljIjOmnxMTOY5HC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GH8F+MpA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422379,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAjhKobnVtJPiRekB4dKJPSHYCemUrGx7VY/9OdqUpWsz8RmCNINt1bEuIJCvsVeZM+8VSwzpABnjucUEpKJaSBLhAqxTPWEaDwU16PiZOxKOH+QoRAdkbD6bxsML6iUADqndzhXp/F143J9wxWfvFnZnjAykA7AljIjOmnxMTOY5HC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GH8F+MpA==",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_odRLnKsAd3TA8BeQcGTEHrRIMMBkl2SS5AQF1FSFQA8lDd8G"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAjhKobnVtJPiRekB4dKJPSHYCemUrGx7VY/9OdqUpWsz8RmCNINt1bEuIJCvsVeZM+8VSwzpABnjucUEpKJaSBLhAqxTPWEaDwU16PiZOxKOH+QoRAdkbD6bxsML6iUADqndzhXp/F143J9wxWfvFnZnjAykA7AljIjOmnxMTOY5HC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GH8F+MpA==",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAjhKobnVtJPiRekB4dKJPSHYCemUrGx7VY/9OdqUpWsz8RmCNINt1bEuIJCvsVeZM+8VSwzpABnjucUEpKJaSBLhAqxTPWEaDwU16PiZOxKOH+QoRAdkbD6bxsML6iUADqndzhXp/F143J9wxWfvFnZnjAykA7AljIjOmnxMTOY5HC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GH8F+MpA==",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAjhKobnVtJPiRekB4dKJPSHYCemUrGx7VY/9OdqUpWsz8RmCNINt1bEuIJCvsVeZM+8VSwzpABnjucUEpKJaSBLhAqxTPWEaDwU16PiZOxKOH+QoRAdkbD6bxsML6iUADqndzhXp/F143J9wxWfvFnZnjAykA7AljIjOmnxMTOY5HC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GH8F+MpA==",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "message": {
        "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "message": {
        "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
  "id": -576460752303422378,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422378,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+QEOCwH4hLhAjhKobnVtJPiRekB4dKJPSHYCemUrGx7VY/9OdqUpWsz8RmCNINt1bEuIJCvsVeZM+8VSwzpABnjucUEpKJaSBLhAqxTPWEaDwU16PiZOxKOH+QoRAdkbD6bxsML6iUADqndzhXp/F143J9wxWfvFnZnjAykA7AljIjOmnxMTOY5HC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GH8F+MpA=="
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+QEOCwH4hLhAjhKobnVtJPiRekB4dKJPSHYCemUrGx7VY/9OdqUpWsz8RmCNINt1bEuIJCvsVeZM+8VSwzpABnjucUEpKJaSBLhAqxTPWEaDwU16PiZOxKOH+QoRAdkbD6bxsML6iUADqndzhXp/F143J9wxWfvFnZnjAykA7AljIjOmnxMTOY5HC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GH8F+MpA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422377,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422377,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEOCwH4hLhAjhKobnVtJPiRekB4dKJPSHYCemUrGx7VY/9OdqUpWsz8RmCNINt1bEuIJCvsVeZM+8VSwzpABnjucUEpKJaSBLhAqxTPWEaDwU16PiZOxKOH+QoRAdkbD6bxsML6iUADqndzhXp/F143J9wxWfvFnZnjAykA7AljIjOmnxMTOY5HC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GH8F+MpA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422376,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422376,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBorCm1bjSNoP7P6YRZohTxMtWmlUQKCtRKMu2YodJrBqAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeApCeqj0=",
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
  "id": -576460752303422375,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECy7oZFnEkIXGm+DWhxqhQrZ0NNr4W4OAcL+vcwQrs3LX1G9yJc92qzGTWNjAifLkW9q4GhquWLlW3o/1cpgjALuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIEMl14"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422375,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+JALAfhCuECy7oZFnEkIXGm+DWhxqhQrZ0NNr4W4OAcL+vcwQrs3LX1G9yJc92qzGTWNjAifLkW9q4GhquWLlW3o/1cpgjALuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIEMl14",
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
  "id": -576460752303422374,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECM+Aypoj6hY2VOG0tPYs3sPDxtNPFPBjQ1mDgMHGGCbhsbKfIJGMzW2fMnSwuToFC7Sf5jQlvZs8prIjt4rNsBuECy7oZFnEkIXGm+DWhxqhQrZ0NNr4W4OAcL+vcwQrs3LX1G9yJc92qzGTWNjAifLkW9q4GhquWLlW3o/1cpgjALuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIg6k8w"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422374,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuECM+Aypoj6hY2VOG0tPYs3sPDxtNPFPBjQ1mDgMHGGCbhsbKfIJGMzW2fMnSwuToFC7Sf5jQlvZs8prIjt4rNsBuECy7oZFnEkIXGm+DWhxqhQrZ0NNr4W4OAcL+vcwQrs3LX1G9yJc92qzGTWNjAifLkW9q4GhquWLlW3o/1cpgjALuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIg6k8w"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuECM+Aypoj6hY2VOG0tPYs3sPDxtNPFPBjQ1mDgMHGGCbhsbKfIJGMzW2fMnSwuToFC7Sf5jQlvZs8prIjt4rNsBuECy7oZFnEkIXGm+DWhxqhQrZ0NNr4W4OAcL+vcwQrs3LX1G9yJc92qzGTWNjAifLkW9q4GhquWLlW3o/1cpgjALuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIg6k8w"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422373,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422373,
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
  "id": -576460752303422372,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422372,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECM+Aypoj6hY2VOG0tPYs3sPDxtNPFPBjQ1mDgMHGGCbhsbKfIJGMzW2fMnSwuToFC7Sf5jQlvZs8prIjt4rNsBuECy7oZFnEkIXGm+DWhxqhQrZ0NNr4W4OAcL+vcwQrs3LX1G9yJc92qzGTWNjAifLkW9q4GhquWLlW3o/1cpgjALuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIg6k8w",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422371,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422371,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+QEvCwHAuQEp+QEmOwGhBorCm1bjSNoP7P6YRZohTxMtWmlUQKCtRKMu2YodJrBqoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuECM+Aypoj6hY2VOG0tPYs3sPDxtNPFPBjQ1mDgMHGGCbhsbKfIJGMzW2fMnSwuToFC7Sf5jQlvZs8prIjt4rNsBuECy7oZFnEkIXGm+DWhxqhQrZ0NNr4W4OAcL+vcwQrs3LX1G9yJc92qzGTWNjAifLkW9q4GhquWLlW3o/1cpgjALuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIAhhMLes1BWIGItRFRXA==",
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
    "signed_tx": "tx_+QFyCwH4QrhA8DQnGZ7stZts87TKA7c52v1zauyNjAhq+DrZiZgzJBNbZj8Muzn/ge/kB6PG0bbo+/gU2pZaRU+IUG0ZII6ICbkBKfkBJjsBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAjPgMqaI+oWNlThtLT2LN7Dw8bTTxTwY0NZg4DBxhgm4bGynyCRjM1tnzJ0sLk6BQu0n+Y0Jb2bPKayI7eKzbAbhAsu6GRZxJCFxpvg1ocaoUK2dDTa+FuDgHC/r3MEK7Ny19RvciXPdqsxk1jYwIny5FvauBoarli5Vt6P9XKYIwC7hI+EY5AqEGisKbVuNI2g/s/phFmiFPEy1aaVRAoK1Eoy7Zih0msGoCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIYTC3rNQViBiHzUACk="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422370,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422370,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBorCm1bjSNoP7P6YRZohTxMtWmlUQKCtRKMu2YodJrBqA6Ah5YXSCzjC3C5f2KaHrz5Qp6zPFnxOBCDOm/SZojmZpURLSHY=",
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
  "id": -576460752303422369,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECrV5b/WWW4KhFL/LrmEqNTQvLV+YMj4nta0kmPk/Lypfi6vd0PdGYy9zbZvKOpUPZRZc10rZ6Es0rjTh8N8M4MuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maUhEFup"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422369,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+JALAfhCuECrV5b/WWW4KhFL/LrmEqNTQvLV+YMj4nta0kmPk/Lypfi6vd0PdGYy9zbZvKOpUPZRZc10rZ6Es0rjTh8N8M4MuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maUhEFup",
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
  "id": -576460752303422368,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECrV5b/WWW4KhFL/LrmEqNTQvLV+YMj4nta0kmPk/Lypfi6vd0PdGYy9zbZvKOpUPZRZc10rZ6Es0rjTh8N8M4MuEDO5AvEEVyKr+wmUbHsRh3ra6PZGc1nx99YMkNd66EQ1zDj+JwG2bJVlHkrx3b9Ss6MgNfOjDG0Jy7x0hsMhdwPuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maUf2FEV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422368,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuECrV5b/WWW4KhFL/LrmEqNTQvLV+YMj4nta0kmPk/Lypfi6vd0PdGYy9zbZvKOpUPZRZc10rZ6Es0rjTh8N8M4MuEDO5AvEEVyKr+wmUbHsRh3ra6PZGc1nx99YMkNd66EQ1zDj+JwG2bJVlHkrx3b9Ss6MgNfOjDG0Jy7x0hsMhdwPuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maUf2FEV"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuECrV5b/WWW4KhFL/LrmEqNTQvLV+YMj4nta0kmPk/Lypfi6vd0PdGYy9zbZvKOpUPZRZc10rZ6Es0rjTh8N8M4MuEDO5AvEEVyKr+wmUbHsRh3ra6PZGc1nx99YMkNd66EQ1zDj+JwG2bJVlHkrx3b9Ss6MgNfOjDG0Jy7x0hsMhdwPuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maUf2FEV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422367,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422367,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999997
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000003
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422366,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422366,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECrV5b/WWW4KhFL/LrmEqNTQvLV+YMj4nta0kmPk/Lypfi6vd0PdGYy9zbZvKOpUPZRZc10rZ6Es0rjTh8N8M4MuEDO5AvEEVyKr+wmUbHsRh3ra6PZGc1nx99YMkNd66EQ1zDj+JwG2bJVlHkrx3b9Ss6MgNfOjDG0Jy7x0hsMhdwPuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maUf2FEV",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/bDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAP0OPKg"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422365,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422365,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000003
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999997
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBorCm1bjSNoP7P6YRZohTxMtWmlUQKCtRKMu2YodJrBqBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAh8DgL4=",
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
  "id": -576460752303422364,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECC1SHT8PipoWV1yxkLAJZfi4gd+uC9b/VaRfuSPiGI/gkvQDB+TwZ44oVMmBB1lcYyDafiLIbeq1jP8XjGSrMOuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLKlaTn"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422364,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+JALAfhCuECC1SHT8PipoWV1yxkLAJZfi4gd+uC9b/VaRfuSPiGI/gkvQDB+TwZ44oVMmBB1lcYyDafiLIbeq1jP8XjGSrMOuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLKlaTn",
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
  "id": -576460752303422363,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECC1SHT8PipoWV1yxkLAJZfi4gd+uC9b/VaRfuSPiGI/gkvQDB+TwZ44oVMmBB1lcYyDafiLIbeq1jP8XjGSrMOuEC2hj6AfLBFosj2YOqK1twLiIRx7BaFYz4yjd7PFse98VmkusY6rT4M9NvFa7XbOn87WrB3k8JTYDUaShvjOIcKuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJM9yhI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422363,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuECC1SHT8PipoWV1yxkLAJZfi4gd+uC9b/VaRfuSPiGI/gkvQDB+TwZ44oVMmBB1lcYyDafiLIbeq1jP8XjGSrMOuEC2hj6AfLBFosj2YOqK1twLiIRx7BaFYz4yjd7PFse98VmkusY6rT4M9NvFa7XbOn87WrB3k8JTYDUaShvjOIcKuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJM9yhI"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuECC1SHT8PipoWV1yxkLAJZfi4gd+uC9b/VaRfuSPiGI/gkvQDB+TwZ44oVMmBB1lcYyDafiLIbeq1jP8XjGSrMOuEC2hj6AfLBFosj2YOqK1twLiIRx7BaFYz4yjd7PFse98VmkusY6rT4M9NvFa7XbOn87WrB3k8JTYDUaShvjOIcKuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJM9yhI"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422362,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422362,
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

#### initiator ---> node
```javascript
{
  "id": -576460752303422361,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422361,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECC1SHT8PipoWV1yxkLAJZfi4gd+uC9b/VaRfuSPiGI/gkvQDB+TwZ44oVMmBB1lcYyDafiLIbeq1jP8XjGSrMOuEC2hj6AfLBFosj2YOqK1twLiIRx7BaFYz4yjd7PFse98VmkusY6rT4M9NvFa7XbOn87WrB3k8JTYDUaShvjOIcKuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJM9yhI",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFyCwH4QrhA8DQnGZ7stZts87TKA7c52v1zauyNjAhq+DrZiZgzJBNbZj8Muzn/ge/kB6PG0bbo+/gU2pZaRU+IUG0ZII6ICbkBKfkBJjsBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAjPgMqaI+oWNlThtLT2LN7Dw8bTTxTwY0NZg4DBxhgm4bGynyCRjM1tnzJ0sLk6BQu0n+Y0Jb2bPKayI7eKzbAbhAsu6GRZxJCFxpvg1ocaoUK2dDTa+FuDgHC/r3MEK7Ny19RvciXPdqsxk1jYwIny5FvauBoarli5Vt6P9XKYIwC7hI+EY5AqEGisKbVuNI2g/s/phFmiFPEy1aaVRAoK1Eoy7Zih0msGoCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIYTC3rNQViBiHzUACk=",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFyCwH4QrhA8DQnGZ7stZts87TKA7c52v1zauyNjAhq+DrZiZgzJBNbZj8Muzn/ge/kB6PG0bbo+/gU2pZaRU+IUG0ZII6ICbkBKfkBJjsBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAjPgMqaI+oWNlThtLT2LN7Dw8bTTxTwY0NZg4DBxhgm4bGynyCRjM1tnzJ0sLk6BQu0n+Y0Jb2bPKayI7eKzbAbhAsu6GRZxJCFxpvg1ocaoUK2dDTa+FuDgHC/r3MEK7Ny19RvciXPdqsxk1jYwIny5FvauBoarli5Vt6P9XKYIwC7hI+EY5AqEGisKbVuNI2g/s/phFmiFPEy1aaVRAoK1Eoy7Zih0msGoCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIYTC3rNQViBiHzUACk=",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "딅��֛��\u0019$\b\u00031���h\u0010�\u001d\u0015#;\u0003eR��<�",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422360,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422360,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECC1SHT8PipoWV1yxkLAJZfi4gd+uC9b/VaRfuSPiGI/gkvQDB+TwZ44oVMmBB1lcYyDafiLIbeq1jP8XjGSrMOuEC2hj6AfLBFosj2YOqK1twLiIRx7BaFYz4yjd7PFse98VmkusY6rT4M9NvFa7XbOn87WrB3k8JTYDUaShvjOIcKuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJM9yhI",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422359,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422359,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBorCm1bjSNoP7P6YRZohTxMtWmlUQKCtRKMu2YodJrBqBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC+Frf08=",
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
  "id": -576460752303422358,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECGHdNjGMS5pNcPlT9dYyFYxgcPn3GWNn1JVnvgg2sKA/3sVO5UC6wE+PXzMpZY4TUVvgNzIDbsTwNzB/+I+/cOuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv2pw7n"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422358,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+JALAfhCuECGHdNjGMS5pNcPlT9dYyFYxgcPn3GWNn1JVnvgg2sKA/3sVO5UC6wE+PXzMpZY4TUVvgNzIDbsTwNzB/+I+/cOuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv2pw7n",
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
  "id": -576460752303422357,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECGHdNjGMS5pNcPlT9dYyFYxgcPn3GWNn1JVnvgg2sKA/3sVO5UC6wE+PXzMpZY4TUVvgNzIDbsTwNzB/+I+/cOuECi0WGO7Ty0feDDv/INakOcSn9VPWz8E0OeeQDa5B7JGsVBGpDjRAJ9onql4zXEoz9CQtmgIwkqDtwZ5x3kxs0NuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv9rS5h"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422357,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuECGHdNjGMS5pNcPlT9dYyFYxgcPn3GWNn1JVnvgg2sKA/3sVO5UC6wE+PXzMpZY4TUVvgNzIDbsTwNzB/+I+/cOuECi0WGO7Ty0feDDv/INakOcSn9VPWz8E0OeeQDa5B7JGsVBGpDjRAJ9onql4zXEoz9CQtmgIwkqDtwZ5x3kxs0NuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv9rS5h"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuECGHdNjGMS5pNcPlT9dYyFYxgcPn3GWNn1JVnvgg2sKA/3sVO5UC6wE+PXzMpZY4TUVvgNzIDbsTwNzB/+I+/cOuECi0WGO7Ty0feDDv/INakOcSn9VPWz8E0OeeQDa5B7JGsVBGpDjRAJ9onql4zXEoz9CQtmgIwkqDtwZ5x3kxs0NuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv9rS5h"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422356,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422356,
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
  "id": -576460752303422355,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422355,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECGHdNjGMS5pNcPlT9dYyFYxgcPn3GWNn1JVnvgg2sKA/3sVO5UC6wE+PXzMpZY4TUVvgNzIDbsTwNzB/+I+/cOuECi0WGO7Ty0feDDv/INakOcSn9VPWz8E0OeeQDa5B7JGsVBGpDjRAJ9onql4zXEoz9CQtmgIwkqDtwZ5x3kxs0NuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv9rS5h",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422354,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422354,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBorCm1bjSNoP7P6YRZohTxMtWmlUQKCtRKMu2YodJrBqoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuECGHdNjGMS5pNcPlT9dYyFYxgcPn3GWNn1JVnvgg2sKA/3sVO5UC6wE+PXzMpZY4TUVvgNzIDbsTwNzB/+I+/cOuECi0WGO7Ty0feDDv/INakOcSn9VPWz8E0OeeQDa5B7JGsVBGpDjRAJ9onql4zXEoz9CQtmgIwkqDtwZ5x3kxs0NuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMG0rUY8DdQGCvK",
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
    "signed_tx": "tx_+QFxCwH4QrhAYNj3df+0hCjxbBRroZo35tnKupU96mClQFdUb9WuIrOffDv6rxroCfNqPBL97zzs5+L/P7nPh4Z/lzlQ+vd8BrkBKPkBJTsBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAhh3TYxjEuaTXD5U/XWMhWMYHD59xljZ9SVZ74INrCgP97FTuVAusBPj18zKWWOE1Fb4DcyA27E8Dcwf/iPv3DrhAotFhju08tH3gw7/yDWpDnEp/VT1s/BNDnnkA2uQeyRrFQRqQ40QCfaJ6peM1xKM/QkLZoCMJKg7cGecd5MbNDbhI+EY5AqEGisKbVuNI2g/s/phFmiFPEy1aaVRAoK1Eoy7Zih0msGoFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtK1GPA3kfzbDg=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422353,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422353,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBorCm1bjSNoP7P6YRZohTxMtWmlUQKCtRKMu2YodJrBqBqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAgIlffo=",
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
  "id": -576460752303422352,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBJY4YnyB1W1Hmwt1J/HLOZo3qrleQv9XfAHfuWMwVnueTAC6Cx/QhG15GTb/4YjCJiHY9XAlOc3NJyDkfpx/ILuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIPg0T1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422352,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBJY4YnyB1W1Hmwt1J/HLOZo3qrleQv9XfAHfuWMwVnueTAC6Cx/QhG15GTb/4YjCJiHY9XAlOc3NJyDkfpx/ILuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIPg0T1",
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
  "id": -576460752303422351,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAK0dudM8njKGtwwNjMmF38J6knuMEiN0fmdgF69T42xvhMty1XJ7uACvsKoqcydmiBGfrHec9r7BmloIn5mvcPuEBJY4YnyB1W1Hmwt1J/HLOZo3qrleQv9XfAHfuWMwVnueTAC6Cx/QhG15GTb/4YjCJiHY9XAlOc3NJyDkfpx/ILuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKC05Zu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422351,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuEAK0dudM8njKGtwwNjMmF38J6knuMEiN0fmdgF69T42xvhMty1XJ7uACvsKoqcydmiBGfrHec9r7BmloIn5mvcPuEBJY4YnyB1W1Hmwt1J/HLOZo3qrleQv9XfAHfuWMwVnueTAC6Cx/QhG15GTb/4YjCJiHY9XAlOc3NJyDkfpx/ILuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKC05Zu"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuEAK0dudM8njKGtwwNjMmF38J6knuMEiN0fmdgF69T42xvhMty1XJ7uACvsKoqcydmiBGfrHec9r7BmloIn5mvcPuEBJY4YnyB1W1Hmwt1J/HLOZo3qrleQv9XfAHfuWMwVnueTAC6Cx/QhG15GTb/4YjCJiHY9XAlOc3NJyDkfpx/ILuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKC05Zu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422350,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422350,
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
  "id": -576460752303422349,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422349,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAK0dudM8njKGtwwNjMmF38J6knuMEiN0fmdgF69T42xvhMty1XJ7uACvsKoqcydmiBGfrHec9r7BmloIn5mvcPuEBJY4YnyB1W1Hmwt1J/HLOZo3qrleQv9XfAHfuWMwVnueTAC6Cx/QhG15GTb/4YjCJiHY9XAlOc3NJyDkfpx/ILuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKC05Zu",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422348,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422348,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBorCm1bjSNoP7P6YRZohTxMtWmlUQKCtRKMu2YodJrBqB6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC15w8f8=",
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
  "id": -576460752303422347,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDOGfDOYvXGpDb2IVT/Te6A/3/45y7H5RONhH0Z/q1QOJkwoyZ5VzjBFNXOKt7lr3soGOdR4je6Gw3ladAv0BcIuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvv+A1B"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422347,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDOGfDOYvXGpDb2IVT/Te6A/3/45y7H5RONhH0Z/q1QOJkwoyZ5VzjBFNXOKt7lr3soGOdR4je6Gw3ladAv0BcIuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvv+A1B",
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
  "id": -576460752303422346,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEACBdcuINxoLJFlX03vHliTkscDnLAntvZoWFqhTyTv/mrtHPcy5Tv1AL+Xcoa8yDKWTG7aSyfynA1YM9SxgSgFuEDOGfDOYvXGpDb2IVT/Te6A/3/45y7H5RONhH0Z/q1QOJkwoyZ5VzjBFNXOKt7lr3soGOdR4je6Gw3ladAv0BcIuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgse8RiX"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422346,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuEACBdcuINxoLJFlX03vHliTkscDnLAntvZoWFqhTyTv/mrtHPcy5Tv1AL+Xcoa8yDKWTG7aSyfynA1YM9SxgSgFuEDOGfDOYvXGpDb2IVT/Te6A/3/45y7H5RONhH0Z/q1QOJkwoyZ5VzjBFNXOKt7lr3soGOdR4je6Gw3ladAv0BcIuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgse8RiX"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "state": "tx_+NILAfiEuEACBdcuINxoLJFlX03vHliTkscDnLAntvZoWFqhTyTv/mrtHPcy5Tv1AL+Xcoa8yDKWTG7aSyfynA1YM9SxgSgFuEDOGfDOYvXGpDb2IVT/Te6A/3/45y7H5RONhH0Z/q1QOJkwoyZ5VzjBFNXOKt7lr3soGOdR4je6Gw3ladAv0BcIuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgse8RiX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422345,
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
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422345,
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
  "id": -576460752303422344,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422344,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEACBdcuINxoLJFlX03vHliTkscDnLAntvZoWFqhTyTv/mrtHPcy5Tv1AL+Xcoa8yDKWTG7aSyfynA1YM9SxgSgFuEDOGfDOYvXGpDb2IVT/Te6A/3/45y7H5RONhH0Z/q1QOJkwoyZ5VzjBFNXOKt7lr3soGOdR4je6Gw3ladAv0BcIuEj4RjkCoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawagegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgse8RiX",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAYNj3df+0hCjxbBRroZo35tnKupU96mClQFdUb9WuIrOffDv6rxroCfNqPBL97zzs5+L/P7nPh4Z/lzlQ+vd8BrkBKPkBJTsBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAhh3TYxjEuaTXD5U/XWMhWMYHD59xljZ9SVZ74INrCgP97FTuVAusBPj18zKWWOE1Fb4DcyA27E8Dcwf/iPv3DrhAotFhju08tH3gw7/yDWpDnEp/VT1s/BNDnnkA2uQeyRrFQRqQ40QCfaJ6peM1xKM/QkLZoCMJKg7cGecd5MbNDbhI+EY5AqEGisKbVuNI2g/s/phFmiFPEy1aaVRAoK1Eoy7Zih0msGoFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtK1GPA3kfzbDg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAYNj3df+0hCjxbBRroZo35tnKupU96mClQFdUb9WuIrOffDv6rxroCfNqPBL97zzs5+L/P7nPh4Z/lzlQ+vd8BrkBKPkBJTsBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAhh3TYxjEuaTXD5U/XWMhWMYHD59xljZ9SVZ74INrCgP97FTuVAusBPj18zKWWOE1Fb4DcyA27E8Dcwf/iPv3DrhAotFhju08tH3gw7/yDWpDnEp/VT1s/BNDnnkA2uQeyRrFQRqQ40QCfaJ6peM1xKM/QkLZoCMJKg7cGecd5MbNDbhI+EY5AqEGisKbVuNI2g/s/phFmiFPEy1aaVRAoK1Eoy7Zih0msGoFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIYTBtK1GPA3kfzbDg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "|�\"�|��\u0011ħO&�be�Jϓ���\b�؞�rŞ�",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBorCm1bjSNoP7P6YRZohTxMtWmlUQKCtRKMu2YodJrBqoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBiRmgTUA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422343,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuECHrVtMQ2DhEhAhM/+aKTh0rMEpjKd6lZjsfL6RZrJ420b3GwrPjzY7T4suj0QJEnyFXWQU9YBWgfkjCQAiUhwCuGD4XjUBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYnT1FKM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422343,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "signed_tx": "tx_+KgLAfhCuECHrVtMQ2DhEhAhM/+aKTh0rMEpjKd6lZjsfL6RZrJ420b3GwrPjzY7T4suj0QJEnyFXWQU9YBWgfkjCQAiUhwCuGD4XjUBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYnT1FKM",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422342,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuECHrVtMQ2DhEhAhM/+aKTh0rMEpjKd6lZjsfL6RZrJ420b3GwrPjzY7T4suj0QJEnyFXWQU9YBWgfkjCQAiUhwCuECUglAQNN7CMpExpFYe5+pTdBtifd09Cg5SPaqXVCzbK/FZGhIsKqBsMsDmrsKhuaeIXOVIZ7riIuikgfxBCbUHuGD4XjUBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYl3UOFI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
  "id": -576460752303422342,
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuECHrVtMQ2DhEhAhM/+aKTh0rMEpjKd6lZjsfL6RZrJ420b3GwrPjzY7T4suj0QJEnyFXWQU9YBWgfkjCQAiUhwCuECUglAQNN7CMpExpFYe5+pTdBtifd09Cg5SPaqXVCzbK/FZGhIsKqBsMsDmrsKhuaeIXOVIZ7riIuikgfxBCbUHuGD4XjUBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYl3UOFI",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuECHrVtMQ2DhEhAhM/+aKTh0rMEpjKd6lZjsfL6RZrJ420b3GwrPjzY7T4suj0QJEnyFXWQU9YBWgfkjCQAiUhwCuECUglAQNN7CMpExpFYe5+pTdBtifd09Cg5SPaqXVCzbK/FZGhIsKqBsMsDmrsKhuaeIXOVIZ7riIuikgfxBCbUHuGD4XjUBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYl3UOFI",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuECHrVtMQ2DhEhAhM/+aKTh0rMEpjKd6lZjsfL6RZrJ420b3GwrPjzY7T4suj0QJEnyFXWQU9YBWgfkjCQAiUhwCuECUglAQNN7CMpExpFYe5+pTdBtifd09Cg5SPaqXVCzbK/FZGhIsKqBsMsDmrsKhuaeIXOVIZ7riIuikgfxBCbUHuGD4XjUBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYl3UOFI",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuECHrVtMQ2DhEhAhM/+aKTh0rMEpjKd6lZjsfL6RZrJ420b3GwrPjzY7T4suj0QJEnyFXWQU9YBWgfkjCQAiUhwCuECUglAQNN7CMpExpFYe5+pTdBtifd09Cg5SPaqXVCzbK/FZGhIsKqBsMsDmrsKhuaeIXOVIZ7riIuikgfxBCbUHuGD4XjUBoQaKwptW40jaD+z+mEWaIU8TLVppVECgrUSjLtmKHSawaqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYl3UOFI",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
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
    "channel_id": "ch_247Sg27gL1yoAgBRiXusZ5ixw752cMrvYSG8dTZ1JszdW1BFvA",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
