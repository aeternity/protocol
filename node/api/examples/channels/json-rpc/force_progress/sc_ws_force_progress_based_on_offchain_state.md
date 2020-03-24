
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
      "fsm_id": "ba_niBZPIzg4WygDUOM3VZX2ta2gbdH5ParktZ12Ticisb/WkFi"
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
      "fsm_id": "ba_krudkGk3RF1Vjo512HI+F5I1MUOue3VECSF18LkNAjiEx7g2"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsb7Rr1qw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423152,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDDsHpHeDKRjDMxAkzmKOdaNKeDXjgPpmuvdplcYQlfXerMzrZBiE/i/OmmApTcTEVxYAejYqeJ/qKkAu0j8cgKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LG177KZA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423152,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "fsm_id": "ba_krudkGk3RF1Vjo512HI+F5I1MUOue3VECSF18LkNAjiEx7g2",
      "signed_tx": "tx_+MsLAfhCuEDDsHpHeDKRjDMxAkzmKOdaNKeDXjgPpmuvdplcYQlfXerMzrZBiE/i/OmmApTcTEVxYAejYqeJ/qKkAu0j8cgKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LG177KZA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423151,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhALBrJul3dS7kP2t5Nxd8KVTflwnOAa2GK9PO8YXiaLMF5rFsJmWMqCMt083MnoxHjeYD+3CkBxwTu2+bCly3NDLhAw7B6R3gykYwzMQJM5ijnWjSng144D6Zrr3aZXGEJX13qzM62QYhP4vzppgKU3ExFcWAHo2Knif6ipALtI/HICriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxsHntF0"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423151,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhALBrJul3dS7kP2t5Nxd8KVTflwnOAa2GK9PO8YXiaLMF5rFsJmWMqCMt083MnoxHjeYD+3CkBxwTu2+bCly3NDLhAw7B6R3gykYwzMQJM5ijnWjSng144D6Zrr3aZXGEJX13qzM62QYhP4vzppgKU3ExFcWAHo2Knif6ipALtI/HICriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxsHntF0",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_niBZPIzg4WygDUOM3VZX2ta2gbdH5ParktZ12Ticisb/WkFi"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhALBrJul3dS7kP2t5Nxd8KVTflwnOAa2GK9PO8YXiaLMF5rFsJmWMqCMt083MnoxHjeYD+3CkBxwTu2+bCly3NDLhAw7B6R3gykYwzMQJM5ijnWjSng144D6Zrr3aZXGEJX13qzM62QYhP4vzppgKU3ExFcWAHo2Knif6ipALtI/HICriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxsHntF0",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALBrJul3dS7kP2t5Nxd8KVTflwnOAa2GK9PO8YXiaLMF5rFsJmWMqCMt083MnoxHjeYD+3CkBxwTu2+bCly3NDLhAw7B6R3gykYwzMQJM5ijnWjSng144D6Zrr3aZXGEJX13qzM62QYhP4vzppgKU3ExFcWAHo2Knif6ipALtI/HICriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxsHntF0",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALBrJul3dS7kP2t5Nxd8KVTflwnOAa2GK9PO8YXiaLMF5rFsJmWMqCMt083MnoxHjeYD+3CkBxwTu2+bCly3NDLhAw7B6R3gykYwzMQJM5ijnWjSng144D6Zrr3aZXGEJX13qzM62QYhP4vzppgKU3ExFcWAHo2Knif6ipALtI/HICriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxsHntF0",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "message": {
        "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "message": {
        "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
  "id": -576460752303423150,
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
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423150,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+QENCwH4hLhALBrJul3dS7kP2t5Nxd8KVTflwnOAa2GK9PO8YXiaLMF5rFsJmWMqCMt083MnoxHjeYD+3CkBxwTu2+bCly3NDLhAw7B6R3gykYwzMQJM5ijnWjSng144D6Zrr3aZXGEJX13qzM62QYhP4vzppgKU3ExFcWAHo2Knif6ipALtI/HICriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxsHntF0"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+QENCwH4hLhALBrJul3dS7kP2t5Nxd8KVTflwnOAa2GK9PO8YXiaLMF5rFsJmWMqCMt083MnoxHjeYD+3CkBxwTu2+bCly3NDLhAw7B6R3gykYwzMQJM5ijnWjSng144D6Zrr3aZXGEJX13qzM62QYhP4vzppgKU3ExFcWAHo2Knif6ipALtI/HICriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxsHntF0"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRAqAouRWKhPGHVEJAUE52PjsnjMUr34XqgzAUlFDPz+A7/vYFN1g=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "vm_version": 6
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
  "id": -576460752303423149,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEARzFrMMUqg3kLOsMWe4ERRhEzTRgnq+L7+uKHBQ9sUJT68tdwuoxLsNb8PGPQ1Bp0DkLFjy6SqyUyz1FSWDNsAuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/4j6JAA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423149,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEARzFrMMUqg3kLOsMWe4ERRhEzTRgnq+L7+uKHBQ9sUJT68tdwuoxLsNb8PGPQ1Bp0DkLFjy6SqyUyz1FSWDNsAuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/4j6JAA",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "vm_version": 6
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
  "id": -576460752303423148,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEARzFrMMUqg3kLOsMWe4ERRhEzTRgnq+L7+uKHBQ9sUJT68tdwuoxLsNb8PGPQ1Bp0DkLFjy6SqyUyz1FSWDNsAuEDuNDCBlHUBx63GLD1ewbupdGpq+4xrNrlTssOrNwGsh/MZPey+1n6Pt5VXtwJp5te4Qcw3YzRD96qmGmqcR8INuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/5aFItw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423148,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEARzFrMMUqg3kLOsMWe4ERRhEzTRgnq+L7+uKHBQ9sUJT68tdwuoxLsNb8PGPQ1Bp0DkLFjy6SqyUyz1FSWDNsAuEDuNDCBlHUBx63GLD1ewbupdGpq+4xrNrlTssOrNwGsh/MZPey+1n6Pt5VXtwJp5te4Qcw3YzRD96qmGmqcR8INuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/5aFItw"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEARzFrMMUqg3kLOsMWe4ERRhEzTRgnq+L7+uKHBQ9sUJT68tdwuoxLsNb8PGPQ1Bp0DkLFjy6SqyUyz1FSWDNsAuEDuNDCBlHUBx63GLD1ewbupdGpq+4xrNrlTssOrNwGsh/MZPey+1n6Pt5VXtwJp5te4Qcw3YzRD96qmGmqcR8INuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/5aFItw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRA6AlppMnxQtjAbIpqc5olcFylVD5N2YrzRsUGhqmlS2ceUqulT0=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423147,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA8PGsTjg1DEJ9jkjrWIEkgzBkUVkbL5sbYhOvrG9TKyxZLXKNSUWQxmM8EAIZp4Qi5kRqyL6zrmeQSOqGCOA8BuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHkDj7Ij"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423147,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA8PGsTjg1DEJ9jkjrWIEkgzBkUVkbL5sbYhOvrG9TKyxZLXKNSUWQxmM8EAIZp4Qi5kRqyL6zrmeQSOqGCOA8BuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHkDj7Ij",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423146,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA8PGsTjg1DEJ9jkjrWIEkgzBkUVkbL5sbYhOvrG9TKyxZLXKNSUWQxmM8EAIZp4Qi5kRqyL6zrmeQSOqGCOA8BuEB9RR7gh1+D9J0GoxYwkuVSMBsoHqUFUK2QQwAkNW9+K7E5tisnTCyDdMS2r5PhlWEZ6bxXQiRcUr9G3Eg3vOcNuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHm9DnEJ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423146,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEA8PGsTjg1DEJ9jkjrWIEkgzBkUVkbL5sbYhOvrG9TKyxZLXKNSUWQxmM8EAIZp4Qi5kRqyL6zrmeQSOqGCOA8BuEB9RR7gh1+D9J0GoxYwkuVSMBsoHqUFUK2QQwAkNW9+K7E5tisnTCyDdMS2r5PhlWEZ6bxXQiRcUr9G3Eg3vOcNuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHm9DnEJ"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEA8PGsTjg1DEJ9jkjrWIEkgzBkUVkbL5sbYhOvrG9TKyxZLXKNSUWQxmM8EAIZp4Qi5kRqyL6zrmeQSOqGCOA8BuEB9RR7gh1+D9J0GoxYwkuVSMBsoHqUFUK2QQwAkNW9+K7E5tisnTCyDdMS2r5PhlWEZ6bxXQiRcUr9G3Eg3vOcNuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHm9DnEJ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 4,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRBKBb4pc9PDpQOTSad04plvbM7fDomSyF+U2kEzNYQ9yGYiZB+9U=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423145,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDs/s8ID5IPg4hx0e2pheTTsZeOrxAGkI6YLaB0k65GsbfSX5GLVbt9uzeEA5dP/SQiBisKDUdss1oM42TqCXkCuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmKP85Ph"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423145,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDs/s8ID5IPg4hx0e2pheTTsZeOrxAGkI6YLaB0k65GsbfSX5GLVbt9uzeEA5dP/SQiBisKDUdss1oM42TqCXkCuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmKP85Ph",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423144,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA8akkxJNawYZWIxKAmFW8Fwrylbk6iHuXwhFAM/LIRks/ps01/P5B24YlwSjjU33ugYhh2brMIh0anJM2FWdAEuEDs/s8ID5IPg4hx0e2pheTTsZeOrxAGkI6YLaB0k65GsbfSX5GLVbt9uzeEA5dP/SQiBisKDUdss1oM42TqCXkCuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmIHjRJD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423144,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEA8akkxJNawYZWIxKAmFW8Fwrylbk6iHuXwhFAM/LIRks/ps01/P5B24YlwSjjU33ugYhh2brMIh0anJM2FWdAEuEDs/s8ID5IPg4hx0e2pheTTsZeOrxAGkI6YLaB0k65GsbfSX5GLVbt9uzeEA5dP/SQiBisKDUdss1oM42TqCXkCuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmIHjRJD"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEA8akkxJNawYZWIxKAmFW8Fwrylbk6iHuXwhFAM/LIRks/ps01/P5B24YlwSjjU33ugYhh2brMIh0anJM2FWdAEuEDs/s8ID5IPg4hx0e2pheTTsZeOrxAGkI6YLaB0k65GsbfSX5GLVbt9uzeEA5dP/SQiBisKDUdss1oM42TqCXkCuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QSgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmIHjRJD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRBaBYGi82dykqQsolpZCFXhY2WNDzDD8kPVKD6lp1jdngAEGsaG4=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423143,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEARINv+u172RsQQHm47mFnnBdoWnVzXUbmc4X9yrnOa8Gh3TNe6QQwitjTO4lkxkDnT8HAgLc+zduuYlorlxEELuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4AB/nT3h"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423143,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEARINv+u172RsQQHm47mFnnBdoWnVzXUbmc4X9yrnOa8Gh3TNe6QQwitjTO4lkxkDnT8HAgLc+zduuYlorlxEELuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4AB/nT3h",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423142,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEARINv+u172RsQQHm47mFnnBdoWnVzXUbmc4X9yrnOa8Gh3TNe6QQwitjTO4lkxkDnT8HAgLc+zduuYlorlxEELuEDIrsbjZFG0UziZcQwefsMsKX7Gtvy0+kYzYmUkAdESrigndk3kxKTvZrIt6q+chEDT6598IZ9ikrVs/BklrtYDuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABlWhSp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423142,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEARINv+u172RsQQHm47mFnnBdoWnVzXUbmc4X9yrnOa8Gh3TNe6QQwitjTO4lkxkDnT8HAgLc+zduuYlorlxEELuEDIrsbjZFG0UziZcQwefsMsKX7Gtvy0+kYzYmUkAdESrigndk3kxKTvZrIt6q+chEDT6598IZ9ikrVs/BklrtYDuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABlWhSp"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEARINv+u172RsQQHm47mFnnBdoWnVzXUbmc4X9yrnOa8Gh3TNe6QQwitjTO4lkxkDnT8HAgLc+zduuYlorlxEELuEDIrsbjZFG0UziZcQwefsMsKX7Gtvy0+kYzYmUkAdESrigndk3kxKTvZrIt6q+chEDT6598IZ9ikrVs/BklrtYDuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABlWhSp"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRBqCRsup10nGpF4gNB8+vwlp3ceGKO/l7VIBv15EabTEe1uJ/Wx4=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423141,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBuVoxcYa+INvjbnU4OmoD2T4gTHhXuxP0aFx1wX9iBpyDefOlyGwCHcJS3IbMGWhQr2Nbr9SvkWInHhDWY8OgBuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtYkQ4Gu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423141,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBuVoxcYa+INvjbnU4OmoD2T4gTHhXuxP0aFx1wX9iBpyDefOlyGwCHcJS3IbMGWhQr2Nbr9SvkWInHhDWY8OgBuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtYkQ4Gu",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423140,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBuVoxcYa+INvjbnU4OmoD2T4gTHhXuxP0aFx1wX9iBpyDefOlyGwCHcJS3IbMGWhQr2Nbr9SvkWInHhDWY8OgBuEBy4Qyt+gM4FWUMg2A/9BXe6T8sOU06XBSRoxFzTeLk29sHXoqdxYw6ZtYwTHLz6bHkLl/gCjvwgsRe5M6GJO8PuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtYwVVYO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423140,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEBuVoxcYa+INvjbnU4OmoD2T4gTHhXuxP0aFx1wX9iBpyDefOlyGwCHcJS3IbMGWhQr2Nbr9SvkWInHhDWY8OgBuEBy4Qyt+gM4FWUMg2A/9BXe6T8sOU06XBSRoxFzTeLk29sHXoqdxYw6ZtYwTHLz6bHkLl/gCjvwgsRe5M6GJO8PuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtYwVVYO"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEBuVoxcYa+INvjbnU4OmoD2T4gTHhXuxP0aFx1wX9iBpyDefOlyGwCHcJS3IbMGWhQr2Nbr9SvkWInHhDWY8OgBuEBy4Qyt+gM4FWUMg2A/9BXe6T8sOU06XBSRoxFzTeLk29sHXoqdxYw6ZtYwTHLz6bHkLl/gCjvwgsRe5M6GJO8PuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtYwVVYO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 5,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 5,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 6,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 6,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRB6DiGExj+Vck8sLRqQDcVePkSMwsZhoYdAwpruPJkpQCefLgro0=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423139,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB+oEYiHimv4ppyTxSFmMHAuxCMsT2J/15yLW1EqZT5btgh/nAjGmJyVAWnHVBksKcSVpTcUo970kgX/kFvZaYGuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnl3AQ1a"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423139,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB+oEYiHimv4ppyTxSFmMHAuxCMsT2J/15yLW1EqZT5btgh/nAjGmJyVAWnHVBksKcSVpTcUo970kgX/kFvZaYGuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnl3AQ1a",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423138,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB+oEYiHimv4ppyTxSFmMHAuxCMsT2J/15yLW1EqZT5btgh/nAjGmJyVAWnHVBksKcSVpTcUo970kgX/kFvZaYGuEDmTddrOmkNaGep8Twe0c+KqnZY7bX9YTM7DZ5tqeNVTPgZ/lXF+KGwTZUWePyT6kTFBBpXkumKPTivyOvQbqcIuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnnpxEe9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423138,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEB+oEYiHimv4ppyTxSFmMHAuxCMsT2J/15yLW1EqZT5btgh/nAjGmJyVAWnHVBksKcSVpTcUo970kgX/kFvZaYGuEDmTddrOmkNaGep8Twe0c+KqnZY7bX9YTM7DZ5tqeNVTPgZ/lXF+KGwTZUWePyT6kTFBBpXkumKPTivyOvQbqcIuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnnpxEe9"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEB+oEYiHimv4ppyTxSFmMHAuxCMsT2J/15yLW1EqZT5btgh/nAjGmJyVAWnHVBksKcSVpTcUo970kgX/kFvZaYGuEDmTddrOmkNaGep8Twe0c+KqnZY7bX9YTM7DZ5tqeNVTPgZ/lXF+KGwTZUWePyT6kTFBBpXkumKPTivyOvQbqcIuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnnpxEe9"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 8,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 7,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 7,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRCKDNERM0ttXr3D3t0V8ND0XwmXDpPdFClBK7Gzed22LwePNv54U=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423137,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA1GB62DbloCVl+nbNGAG0VU4amxtq2ZZozmOdU7AQVYpAyCqRiIZwi2EiMboQSYce0TX3otS2bEzFcjDJz6MQGuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8Hid3QIN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423137,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA1GB62DbloCVl+nbNGAG0VU4amxtq2ZZozmOdU7AQVYpAyCqRiIZwi2EiMboQSYce0TX3otS2bEzFcjDJz6MQGuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8Hid3QIN",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423136,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA1GB62DbloCVl+nbNGAG0VU4amxtq2ZZozmOdU7AQVYpAyCqRiIZwi2EiMboQSYce0TX3otS2bEzFcjDJz6MQGuEBk8XS16LgGZgEuzXssWe21iULdez2Dm7jSc7YvWS8kLzOtPyJgFSPSZzpTPVHjNIbQfQbbrJdOtPDaxh24I/IFuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8Hg5qnuL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423136,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEA1GB62DbloCVl+nbNGAG0VU4amxtq2ZZozmOdU7AQVYpAyCqRiIZwi2EiMboQSYce0TX3otS2bEzFcjDJz6MQGuEBk8XS16LgGZgEuzXssWe21iULdez2Dm7jSc7YvWS8kLzOtPyJgFSPSZzpTPVHjNIbQfQbbrJdOtPDaxh24I/IFuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8Hg5qnuL"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEA1GB62DbloCVl+nbNGAG0VU4amxtq2ZZozmOdU7AQVYpAyCqRiIZwi2EiMboQSYce0TX3otS2bEzFcjDJz6MQGuEBk8XS16LgGZgEuzXssWe21iULdez2Dm7jSc7YvWS8kLzOtPyJgFSPSZzpTPVHjNIbQfQbbrJdOtPDaxh24I/IFuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0QigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8Hg5qnuL"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRCaCWHjfN80qMk25WVfiaUOCE/EcFocpmZScduuyWKweWQWlp3kc=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423135,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBJ4Pw+vos7oBxqIJWIdt7Svv1TfduXaZmOYIZ4JHi2XwBwKRmdazaJdRgUY32Y2xW4I+uz7TURnG69RXj9A0QKuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkFom2GG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423135,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBJ4Pw+vos7oBxqIJWIdt7Svv1TfduXaZmOYIZ4JHi2XwBwKRmdazaJdRgUY32Y2xW4I+uz7TURnG69RXj9A0QKuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkFom2GG",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423134,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAD1uz0cE/ulUIeMkORCHSLops5CAoAaLs8BX97lbzsYL83vetzPEj/buh3/uek0J3beNwAWu89rCCe6lSjjFkOuEBJ4Pw+vos7oBxqIJWIdt7Svv1TfduXaZmOYIZ4JHi2XwBwKRmdazaJdRgUY32Y2xW4I+uz7TURnG69RXj9A0QKuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkHrjFH2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423134,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEAD1uz0cE/ulUIeMkORCHSLops5CAoAaLs8BX97lbzsYL83vetzPEj/buh3/uek0J3beNwAWu89rCCe6lSjjFkOuEBJ4Pw+vos7oBxqIJWIdt7Svv1TfduXaZmOYIZ4JHi2XwBwKRmdazaJdRgUY32Y2xW4I+uz7TURnG69RXj9A0QKuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkHrjFH2"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuEAD1uz0cE/ulUIeMkORCHSLops5CAoAaLs8BX97lbzsYL83vetzPEj/buh3/uek0J3beNwAWu89rCCe6lSjjFkOuEBJ4Pw+vos7oBxqIJWIdt7Svv1TfduXaZmOYIZ4JHi2XwBwKRmdazaJdRgUY32Y2xW4I+uz7TURnG69RXj9A0QKuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkHrjFH2"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRCqDtOc3Amcplq0xSbaR585IcTo5Yw0MEz4WRUsC9u8JRPxVvM2k=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423133,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECsLDL2MIsQXzw5PIrNbjADVA07VdrOU1pzTwDXf6zXPCL5kMIq+5aeAwYzZYjScNdkf/CKPdebMlKLo6bsjVAFuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8YPXQd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423133,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+JALAfhCuECsLDL2MIsQXzw5PIrNbjADVA07VdrOU1pzTwDXf6zXPCL5kMIq+5aeAwYzZYjScNdkf/CKPdebMlKLo6bsjVAFuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8YPXQd",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423132,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECsLDL2MIsQXzw5PIrNbjADVA07VdrOU1pzTwDXf6zXPCL5kMIq+5aeAwYzZYjScNdkf/CKPdebMlKLo6bsjVAFuEDAXO0ah2/ewMGoqvW2pn9C+KRqkQZr355Mj28GeO6gPkC5zDpFU5bKuA0DHexSnDVXfE5/Icj2gqzNAAnh3RIPuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9fgMZ8"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423132,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuECsLDL2MIsQXzw5PIrNbjADVA07VdrOU1pzTwDXf6zXPCL5kMIq+5aeAwYzZYjScNdkf/CKPdebMlKLo6bsjVAFuEDAXO0ah2/ewMGoqvW2pn9C+KRqkQZr355Mj28GeO6gPkC5zDpFU5bKuA0DHexSnDVXfE5/Icj2gqzNAAnh3RIPuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9fgMZ8"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "state": "tx_+NILAfiEuECsLDL2MIsQXzw5PIrNbjADVA07VdrOU1pzTwDXf6zXPCL5kMIq+5aeAwYzZYjScNdkf/CKPdebMlKLo6bsjVAFuEDAXO0ah2/ewMGoqvW2pn9C+KRqkQZr355Mj28GeO6gPkC5zDpFU5bKuA0DHexSnDVXfE5/Icj2gqzNAAnh3RIPuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9fgMZ8"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 9,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 9,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 10,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 10,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
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
    ],
    "contracts": [
      "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg3RjYwp6lL7XajvEvm7iNq5KLyfXpybbmKQXb+iOzt6/5AYP4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4lKDdGNjCnqUvtdqO8S+buI2rkovJ9enJtuYpBdv6I7O3r/hxgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatig/OJdc7quICtQ5NDRs4AnNC4CAml1Rk+yukDNxgsfRl2AgICAoOE3SJ7NFgWikf5Diz5ODDyxSzAvj+fsIYI10YhYpvfagICAgID4T6DhN0iezRYFopH+Q4s+Tgw8sUswL4/n7CGCNdGIWKb32u2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/X4SaD84l1zuq4gK1Dk0NGzgCc0LgICaXVGT7K6QM3GCx9GXeegMoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAArj4qCRnDmiIQXoObi9BsqN64Iwy/saIfO5/lEZSSZpgSp538DA+Qap+QamoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+EOhAGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkoGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QO2oGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMLcUPQ=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ],
    "contracts": [
      "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg3RjYwp6lL7XajvEvm7iNq5KLyfXpybbmKQXb+iOzt6/5AYP4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4lKDdGNjCnqUvtdqO8S+buI2rkovJ9enJtuYpBdv6I7O3r/hxgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatig/OJdc7quICtQ5NDRs4AnNC4CAml1Rk+yukDNxgsfRl2AgICAoOE3SJ7NFgWikf5Diz5ODDyxSzAvj+fsIYI10YhYpvfagICAgID4T6DhN0iezRYFopH+Q4s+Tgw8sUswL4/n7CGCNdGIWKb32u2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/X4SaD84l1zuq4gK1Dk0NGzgCc0LgICaXVGT7K6QM3GCx9GXeegMoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAArj4qCRnDmiIQXoObi9BsqN64Iwy/saIfO5/lEZSSZpgSp538DA+Qap+QamoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+EOhAGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkoGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QO2oGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMLcUPQ=="
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
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303423131,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423131,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QL7ggJuAbkC9PkC8T8B+QLsuLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5P9BLORlFnNWP46Iw23Suc9M0u1MToYNRjGwe0xrNZbVuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AgIoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAc6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwLi5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMC4ufi3QAG4QGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkHklzMgEiJuGa1TSZkIu3K+YdJ9z2A0ZmrndttUxpu9m4cfhvKQKhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwBwehBWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5Ae4yCOvwLRy2pdytmVuW6e0b4NzEVlVrJMD+RlTwM5LuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AkJoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwHq9rHM=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECsLDL2MIsQXzw5PIrNbjADVA07VdrOU1pzTwDXf6zXPCL5kMIq+5aeAwYzZYjScNdkf/CKPdebMlKLo6bsjVAFuEDAXO0ah2/ewMGoqvW2pn9C+KRqkQZr355Mj28GeO6gPkC5zDpFU5bKuA0DHexSnDVXfE5/Icj2gqzNAAnh3RIPuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT9fgMZ8",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABrDrddQ=="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423130,
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "gas_price": 1000009612
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423130,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "signed_tx": "tx_+Qi7CwHAuQi1+QiyggIJAaEGVTl35b3Ya2fk9O21yrr6RJ087bQxUg+iy9YcYrLA5NGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WuNT40gsB+IS4QKwsMvYwixBfPDk8is1uMANUDTtV2s5TWnNPANd/rNc8IvmQwir7lp4DBjNliNJw12R/8Io915syUoujpuyNUAW4QMBc7RqHb97Awaiq9bamf0L4pGqRBmvfnkyPbwZ47qA+QLnMOkVTlsq4DQMd7FKcNVd8Tn8hyPaCrM0ACeHdEg+4SPhGOQKhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRCqDtOc3Amcplq0xSbaR585IcTo5Yw0MEz4WRUsC9u8JRPwu4uPi2ggI+AaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9ahBWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkAQqDD0JAhDua74y4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgsLnd8c6DXYWg6hhHdGzLNnHtXmkbdLuhR1rW6JxSh4y5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaJigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5BABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQALkDiPkDhUABoGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5DqJ1/GRi5uSlXBXF7zuPMeGEyeQXkwdotSRIiuTGrJAuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AoKoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2w70ABoLHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Wi8oKAQCGP6olIl/1qulAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5IXECgEACrDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAEAhwHB0nyRVXAcfqhXYA==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1000009612,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+Qj+CwH4QrhAWSwcxoWu1xZOeDpnL11nm2MJ9vIbH0mBAnl5eKhkkhXLhwSS/ZljhBNInYXixufaHwZw+AVE+szPX5yWpSlhDLkItfkIsoICCQGhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuECsLDL2MIsQXzw5PIrNbjADVA07VdrOU1pzTwDXf6zXPCL5kMIq+5aeAwYzZYjScNdkf/CKPdebMlKLo6bsjVAFuEDAXO0ah2/ewMGoqvW2pn9C+KRqkQZr355Mj28GeO6gPkC5zDpFU5bKuA0DHexSnDVXfE5/Icj2gqzNAAnh3RIPuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8LuLj4toICPgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AEKgw9CQIQ7mu+MuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoLC53fHOg12FoOoYR3RsyzZx7V5pG3S7oUda1uicUoeMuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABAIcBwdJ8kVVwHHGswDU="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAWSwcxoWu1xZOeDpnL11nm2MJ9vIbH0mBAnl5eKhkkhXLhwSS/ZljhBNInYXixufaHwZw+AVE+szPX5yWpSlhDLkItfkIsoICCQGhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuECsLDL2MIsQXzw5PIrNbjADVA07VdrOU1pzTwDXf6zXPCL5kMIq+5aeAwYzZYjScNdkf/CKPdebMlKLo6bsjVAFuEDAXO0ah2/ewMGoqvW2pn9C+KRqkQZr355Mj28GeO6gPkC5zDpFU5bKuA0DHexSnDVXfE5/Icj2gqzNAAnh3RIPuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8LuLj4toICPgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AEKgw9CQIQ7mu+MuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoLC53fHOg12FoOoYR3RsyzZx7V5pG3S7oUda1uicUoeMuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABAIcBwdJ8kVVwHHGswDU=",
      "type": "channel_force_progress_tx"
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAWSwcxoWu1xZOeDpnL11nm2MJ9vIbH0mBAnl5eKhkkhXLhwSS/ZljhBNInYXixufaHwZw+AVE+szPX5yWpSlhDLkItfkIsoICCQGhBlU5d+W92Gtn5PTttcq6+kSdPO20MVIPosvWHGKywOTRoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuECsLDL2MIsQXzw5PIrNbjADVA07VdrOU1pzTwDXf6zXPCL5kMIq+5aeAwYzZYjScNdkf/CKPdebMlKLo6bsjVAFuEDAXO0ah2/ewMGoqvW2pn9C+KRqkQZr355Mj28GeO6gPkC5zDpFU5bKuA0DHexSnDVXfE5/Icj2gqzNAAnh3RIPuEj4RjkCoQZVOXflvdhrZ+T07bXKuvpEnTzttDFSD6LL1hxissDk0Qqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8LuLj4toICPgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AEKgw9CQIQ7mu+MuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoLC53fHOg12FoOoYR3RsyzZx7V5pG3S7oUda1uicUoeMuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABAIcBwdJ8kVVwHHGswDU=",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423129,
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
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423129,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423128,
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
    "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
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
  "channel_id": "ch_eXwpLJN6F8bPNSE9mBZrkUvdKpR6uaHXpzm4cvoDJjxu9ebNt",
  "id": -576460752303423128,
  "jsonrpc": "2.0",
  "result": "ok",
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
      "fsm_id": "ba_Dr8kurXMeVMIcM3HipVDhr19h24R75QRaHtg16/+8H9eS9Vo"
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
      "fsm_id": "ba_bSw+oM9Qf5Hdp4v8UvwdAaz5i+6W7mdpA8t5SpjidSqpYVb4"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsdF3Z2Pw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423127,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECddWfIp6acDn146aTfQ59v+luPn/mmT8y3Tt79oNTb1hFnvcUntX9pZsMe3gxqpNtl3nBM6SB1i0A6ymFyXZIBuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LHTsdNZY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423127,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "fsm_id": "ba_bSw+oM9Qf5Hdp4v8UvwdAaz5i+6W7mdpA8t5SpjidSqpYVb4",
      "signed_tx": "tx_+MsLAfhCuECddWfIp6acDn146aTfQ59v+luPn/mmT8y3Tt79oNTb1hFnvcUntX9pZsMe3gxqpNtl3nBM6SB1i0A6ymFyXZIBuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LHTsdNZY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423126,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAjirtjj9VW4blhrX+HWnqXJ0gA6yJSPyU39QG9+naEiKv3iK9HsbnZJ4p/CoP+1csA02ccAsU3pdsQqwtPfXZDbhAnXVnyKemnA59eOmk30Ofb/pbj5/5pk/Mt07e/aDU29YRZ73FJ7V/aWbDHt4MaqTbZd5wTOkgdYtAOsphcl2SAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx0dULU/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423126,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAjirtjj9VW4blhrX+HWnqXJ0gA6yJSPyU39QG9+naEiKv3iK9HsbnZJ4p/CoP+1csA02ccAsU3pdsQqwtPfXZDbhAnXVnyKemnA59eOmk30Ofb/pbj5/5pk/Mt07e/aDU29YRZ73FJ7V/aWbDHt4MaqTbZd5wTOkgdYtAOsphcl2SAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx0dULU/",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Dr8kurXMeVMIcM3HipVDhr19h24R75QRaHtg16/+8H9eS9Vo"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAjirtjj9VW4blhrX+HWnqXJ0gA6yJSPyU39QG9+naEiKv3iK9HsbnZJ4p/CoP+1csA02ccAsU3pdsQqwtPfXZDbhAnXVnyKemnA59eOmk30Ofb/pbj5/5pk/Mt07e/aDU29YRZ73FJ7V/aWbDHt4MaqTbZd5wTOkgdYtAOsphcl2SAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx0dULU/",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAjirtjj9VW4blhrX+HWnqXJ0gA6yJSPyU39QG9+naEiKv3iK9HsbnZJ4p/CoP+1csA02ccAsU3pdsQqwtPfXZDbhAnXVnyKemnA59eOmk30Ofb/pbj5/5pk/Mt07e/aDU29YRZ73FJ7V/aWbDHt4MaqTbZd5wTOkgdYtAOsphcl2SAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx0dULU/",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAjirtjj9VW4blhrX+HWnqXJ0gA6yJSPyU39QG9+naEiKv3iK9HsbnZJ4p/CoP+1csA02ccAsU3pdsQqwtPfXZDbhAnXVnyKemnA59eOmk30Ofb/pbj5/5pk/Mt07e/aDU29YRZ73FJ7V/aWbDHt4MaqTbZd5wTOkgdYtAOsphcl2SAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx0dULU/",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "message": {
        "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "message": {
        "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
  "id": -576460752303423125,
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
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423125,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+QENCwH4hLhAjirtjj9VW4blhrX+HWnqXJ0gA6yJSPyU39QG9+naEiKv3iK9HsbnZJ4p/CoP+1csA02ccAsU3pdsQqwtPfXZDbhAnXVnyKemnA59eOmk30Ofb/pbj5/5pk/Mt07e/aDU29YRZ73FJ7V/aWbDHt4MaqTbZd5wTOkgdYtAOsphcl2SAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx0dULU/"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+QENCwH4hLhAjirtjj9VW4blhrX+HWnqXJ0gA6yJSPyU39QG9+naEiKv3iK9HsbnZJ4p/CoP+1csA02ccAsU3pdsQqwtPfXZDbhAnXVnyKemnA59eOmk30Ofb/pbj5/5pk/Mt07e/aDU29YRZ73FJ7V/aWbDHt4MaqTbZd5wTOkgdYtAOsphcl2SAbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx0dULU/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwAqAouRWKhPGHVEJAUE52PjsnjMUr34XqgzAUlFDPz+A7/ihtsLs=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "vm_version": 6
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
  "id": -576460752303423124,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBTqTZeqyYFe6JKGba7o0oGiKr9oBuNpq5sAkNzagMS/12x476RyDnvobCN7L9tmrbEUE76qMTSKfA7YfK1FisJuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/54ZdDg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423124,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBTqTZeqyYFe6JKGba7o0oGiKr9oBuNpq5sAkNzagMS/12x476RyDnvobCN7L9tmrbEUE76qMTSKfA7YfK1FisJuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/54ZdDg",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "vm_version": 6
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
  "id": -576460752303423123,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBTqTZeqyYFe6JKGba7o0oGiKr9oBuNpq5sAkNzagMS/12x476RyDnvobCN7L9tmrbEUE76qMTSKfA7YfK1FisJuEBbsm3kxf7Rf5KNnXaEl+M6MPSaZY23f0qsA46oGKv0AutBQvbTUw1UpzOzxYf5EdxEQ0wNe7NyzUUMgGgHKdUDuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/7WR6ul"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423123,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEBTqTZeqyYFe6JKGba7o0oGiKr9oBuNpq5sAkNzagMS/12x476RyDnvobCN7L9tmrbEUE76qMTSKfA7YfK1FisJuEBbsm3kxf7Rf5KNnXaEl+M6MPSaZY23f0qsA46oGKv0AutBQvbTUw1UpzOzxYf5EdxEQ0wNe7NyzUUMgGgHKdUDuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/7WR6ul"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEBTqTZeqyYFe6JKGba7o0oGiKr9oBuNpq5sAkNzagMS/12x476RyDnvobCN7L9tmrbEUE76qMTSKfA7YfK1FisJuEBbsm3kxf7Rf5KNnXaEl+M6MPSaZY23f0qsA46oGKv0AutBQvbTUw1UpzOzxYf5EdxEQ0wNe7NyzUUMgGgHKdUDuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAKgKLkVioTxh1RCQFBOdj47J4zFK9+F6oMwFJRQz8/gO/7WR6ul"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwA6AlppMnxQtjAbIpqc5olcFylVD5N2YrzRsUGhqmlS2ceQYvm4U=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423122,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECwvWGINXE/f++Hv4RZUXOIIMVjgOZtWQ7NZrIIETt6DzfUR+LVlb1Bsw8bJwxCxkpzM4m+JbDM7bqCbaTASm8EuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHnEqyda"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423122,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+JALAfhCuECwvWGINXE/f++Hv4RZUXOIIMVjgOZtWQ7NZrIIETt6DzfUR+LVlb1Bsw8bJwxCxkpzM4m+JbDM7bqCbaTASm8EuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHnEqyda",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423121,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECgyzs9/SIf0/pfDUUEQo0GA+6Za+ow8C87c7Y0bxp+IQH8mI0+JqFQHNlynyekO2o0LxGNKjQDymVcVcQBWk0IuECwvWGINXE/f++Hv4RZUXOIIMVjgOZtWQ7NZrIIETt6DzfUR+LVlb1Bsw8bJwxCxkpzM4m+JbDM7bqCbaTASm8EuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHlZ5AlI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423121,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuECgyzs9/SIf0/pfDUUEQo0GA+6Za+ow8C87c7Y0bxp+IQH8mI0+JqFQHNlynyekO2o0LxGNKjQDymVcVcQBWk0IuECwvWGINXE/f++Hv4RZUXOIIMVjgOZtWQ7NZrIIETt6DzfUR+LVlb1Bsw8bJwxCxkpzM4m+JbDM7bqCbaTASm8EuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHlZ5AlI"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuECgyzs9/SIf0/pfDUUEQo0GA+6Za+ow8C87c7Y0bxp+IQH8mI0+JqFQHNlynyekO2o0LxGNKjQDymVcVcQBWk0IuECwvWGINXE/f++Hv4RZUXOIIMVjgOZtWQ7NZrIIETt6DzfUR+LVlb1Bsw8bJwxCxkpzM4m+JbDM7bqCbaTASm8EuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAOgJaaTJ8ULYwGyKanOaJXBcpVQ+TdmK80bFBoappUtnHlZ5AlI"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 4,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwBKBb4pc9PDpQOTSad04plvbM7fDomSyF+U2kEzNYQ9yGYg67tHc=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423120,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAPJUc5sMpRF+f2aybY80TWSqKiEIsxe3mtUmuL8YY0pJ++Ykt+4hCkSLt/gp72TM89uq5cUTvW8BM+PrUj9MsEuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cASgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmIBpa8F"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423120,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAPJUc5sMpRF+f2aybY80TWSqKiEIsxe3mtUmuL8YY0pJ++Ykt+4hCkSLt/gp72TM89uq5cUTvW8BM+PrUj9MsEuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cASgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmIBpa8F",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423119,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAPJUc5sMpRF+f2aybY80TWSqKiEIsxe3mtUmuL8YY0pJ++Ykt+4hCkSLt/gp72TM89uq5cUTvW8BM+PrUj9MsEuEDq95awCvEpOQxyTe3A9dYsh9EFlrggjTWpXmyrDn4zF3W83fzN+5CA3yZ2YRgamlOXSr0T8bvDrctrDKSL1bcJuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cASgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmLz0XfA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423119,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEAPJUc5sMpRF+f2aybY80TWSqKiEIsxe3mtUmuL8YY0pJ++Ykt+4hCkSLt/gp72TM89uq5cUTvW8BM+PrUj9MsEuEDq95awCvEpOQxyTe3A9dYsh9EFlrggjTWpXmyrDn4zF3W83fzN+5CA3yZ2YRgamlOXSr0T8bvDrctrDKSL1bcJuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cASgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmLz0XfA"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEAPJUc5sMpRF+f2aybY80TWSqKiEIsxe3mtUmuL8YY0pJ++Ykt+4hCkSLt/gp72TM89uq5cUTvW8BM+PrUj9MsEuEDq95awCvEpOQxyTe3A9dYsh9EFlrggjTWpXmyrDn4zF3W83fzN+5CA3yZ2YRgamlOXSr0T8bvDrctrDKSL1bcJuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cASgW+KXPTw6UDk0mndOKZb2zO3w6JkshflNpBMzWEPchmLz0XfA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwBaBYGi82dykqQsolpZCFXhY2WNDzDD8kPVKD6lp1jdngABbdyOs=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423118,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED3XdAwkQtDtoHzsedlnfAmr9Ohmej9y/eEU1izaubRTEnEGcgLbxwA4vaf6fS44ymn3pzgiluIyFt6rZwTK3gAuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ADKwOIj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423118,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+JALAfhCuED3XdAwkQtDtoHzsedlnfAmr9Ohmej9y/eEU1izaubRTEnEGcgLbxwA4vaf6fS44ymn3pzgiluIyFt6rZwTK3gAuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ADKwOIj",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423117,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEApYryf+UqUjDTqw1AlhB1L6MMaHFLirkr5/401h6TZL1cIQ/O+oyBATB+u9mMHGJU9uvrZtG8F4tj5wUCq0RAKuED3XdAwkQtDtoHzsedlnfAmr9Ohmej9y/eEU1izaubRTEnEGcgLbxwA4vaf6fS44ymn3pzgiluIyFt6rZwTK3gAuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABddXBq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423117,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEApYryf+UqUjDTqw1AlhB1L6MMaHFLirkr5/401h6TZL1cIQ/O+oyBATB+u9mMHGJU9uvrZtG8F4tj5wUCq0RAKuED3XdAwkQtDtoHzsedlnfAmr9Ohmej9y/eEU1izaubRTEnEGcgLbxwA4vaf6fS44ymn3pzgiluIyFt6rZwTK3gAuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABddXBq"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEApYryf+UqUjDTqw1AlhB1L6MMaHFLirkr5/401h6TZL1cIQ/O+oyBATB+u9mMHGJU9uvrZtG8F4tj5wUCq0RAKuED3XdAwkQtDtoHzsedlnfAmr9Ohmej9y/eEU1izaubRTEnEGcgLbxwA4vaf6fS44ymn3pzgiluIyFt6rZwTK3gAuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAWgWBovNncpKkLKJaWQhV4WNljQ8ww/JD1Sg+padY3Z4ABddXBq"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwBqCRsup10nGpF4gNB8+vwlp3ceGKO/l7VIBv15EabTEe1nLjQ0U=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423116,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBNfod1K3+CA59t+O+t1Df0n+ecKrfg2PdjDppxZTIBYhVEOlNkDGtUQRwEOvcYSopehj4ScwQFjgqjE+fwBcYIuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtaNc+Wv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423116,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBNfod1K3+CA59t+O+t1Df0n+ecKrfg2PdjDppxZTIBYhVEOlNkDGtUQRwEOvcYSopehj4ScwQFjgqjE+fwBcYIuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtaNc+Wv",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423115,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBNfod1K3+CA59t+O+t1Df0n+ecKrfg2PdjDppxZTIBYhVEOlNkDGtUQRwEOvcYSopehj4ScwQFjgqjE+fwBcYIuECyx4nWVbnQe3rDY3a5wxf5dRmGxBvQcDeKWA0w+gKgnCY/cfYy3CuebpdX0jcPkSrs4GIIN3MEM4fC40u+l1cLuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtZ8gRz+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423115,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEBNfod1K3+CA59t+O+t1Df0n+ecKrfg2PdjDppxZTIBYhVEOlNkDGtUQRwEOvcYSopehj4ScwQFjgqjE+fwBcYIuECyx4nWVbnQe3rDY3a5wxf5dRmGxBvQcDeKWA0w+gKgnCY/cfYy3CuebpdX0jcPkSrs4GIIN3MEM4fC40u+l1cLuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtZ8gRz+"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEBNfod1K3+CA59t+O+t1Df0n+ecKrfg2PdjDppxZTIBYhVEOlNkDGtUQRwEOvcYSopehj4ScwQFjgqjE+fwBcYIuECyx4nWVbnQe3rDY3a5wxf5dRmGxBvQcDeKWA0w+gKgnCY/cfYy3CuebpdX0jcPkSrs4GIIN3MEM4fC40u+l1cLuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAagkbLqddJxqReIDQfPr8Jad3Hhijv5e1SAb9eRGm0xHtZ8gRz+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 5,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 5,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 6,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 6,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 3,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwB6DiGExj+Vck8sLRqQDcVePkSMwsZhoYdAwpruPJkpQCeeVq/wQ=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423114,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDgc5eNIEC7ngOesBULsJkSlfG4SYoR9k44+ELqxQiy+HBp9182lh9rLCQFl7ISxDzIo5XkwVFlj5Ns+XkqzU8LuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnlMWCXc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423114,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDgc5eNIEC7ngOesBULsJkSlfG4SYoR9k44+ELqxQiy+HBp9182lh9rLCQFl7ISxDzIo5XkwVFlj5Ns+XkqzU8LuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnlMWCXc",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423113,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAecSrr5qXtTebUPsqASK6m9yF71ExEa7VyprW0mGNKjBaWyW9L9e1zfFdTZqhUXi+qoQXkzg/t0SlTQDml9PoMuEDgc5eNIEC7ngOesBULsJkSlfG4SYoR9k44+ELqxQiy+HBp9182lh9rLCQFl7ISxDzIo5XkwVFlj5Ns+XkqzU8LuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnnprPy3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423113,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEAecSrr5qXtTebUPsqASK6m9yF71ExEa7VyprW0mGNKjBaWyW9L9e1zfFdTZqhUXi+qoQXkzg/t0SlTQDml9PoMuEDgc5eNIEC7ngOesBULsJkSlfG4SYoR9k44+ELqxQiy+HBp9182lh9rLCQFl7ISxDzIo5XkwVFlj5Ns+XkqzU8LuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnnprPy3"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEAecSrr5qXtTebUPsqASK6m9yF71ExEa7VyprW0mGNKjBaWyW9L9e1zfFdTZqhUXi+qoQXkzg/t0SlTQDml9PoMuEDgc5eNIEC7ngOesBULsJkSlfG4SYoR9k44+ELqxQiy+HBp9182lh9rLCQFl7ISxDzIo5XkwVFlj5Ns+XkqzU8LuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAeg4hhMY/lXJPLC0akA3FXj5EjMLGYaGHQMKa7jyZKUAnnprPy3"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 8,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 7,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 7,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwCKDNERM0ttXr3D3t0V8ND0XwmXDpPdFClBK7Gzed22LwePQUXMo=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423112,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBAgjpnYyXJnUyoO68i5ROfChJr9vhi4mC0JWHDYabvxz59vHM5R1fpra8LJhOef4tS0aSiVRddz76Lc4hYzUYAuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgMmOCc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423112,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBAgjpnYyXJnUyoO68i5ROfChJr9vhi4mC0JWHDYabvxz59vHM5R1fpra8LJhOef4tS0aSiVRddz76Lc4hYzUYAuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgMmOCc",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423111,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBAgjpnYyXJnUyoO68i5ROfChJr9vhi4mC0JWHDYabvxz59vHM5R1fpra8LJhOef4tS0aSiVRddz76Lc4hYzUYAuEDquo1eVNoZeDB/5W5Qpb/UlqekRQ2bxv9A6qNfecAKGvfYmmp7PIWRMNEQf69R8J6PVjYA7bkclvuDAAedjVkHuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgYFyVG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423111,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEBAgjpnYyXJnUyoO68i5ROfChJr9vhi4mC0JWHDYabvxz59vHM5R1fpra8LJhOef4tS0aSiVRddz76Lc4hYzUYAuEDquo1eVNoZeDB/5W5Qpb/UlqekRQ2bxv9A6qNfecAKGvfYmmp7PIWRMNEQf69R8J6PVjYA7bkclvuDAAedjVkHuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgYFyVG"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEBAgjpnYyXJnUyoO68i5ROfChJr9vhi4mC0JWHDYabvxz59vHM5R1fpra8LJhOef4tS0aSiVRddz76Lc4hYzUYAuEDquo1eVNoZeDB/5W5Qpb/UlqekRQ2bxv9A6qNfecAKGvfYmmp7PIWRMNEQf69R8J6PVjYA7bkclvuDAAedjVkHuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAigzRETNLbV69w97dFfDQ9F8Jlw6T3RQpQSuxs3ndti8HgYFyVG"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwCaCWHjfN80qMk25WVfiaUOCE/EcFocpmZScduuyWKweWQSsRsSY=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423110,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA9Ll65si7CrgWnEB7X3I8QpHTtAzUGBWhjPjoq4pIxIMpHy4FfqSzWinikq1+bLzfdtDDGW7nMyyHgX5bJf04FuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkHtqJiF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423110,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA9Ll65si7CrgWnEB7X3I8QpHTtAzUGBWhjPjoq4pIxIMpHy4FfqSzWinikq1+bLzfdtDDGW7nMyyHgX5bJf04FuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkHtqJiF",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423109,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAH4kMers29RNhoHmvHiX9iEQ+9MlfRFW1a0fd7eunTsyjgHglI5EL4mfXLxuA4vEvqIZq4eUy2qrtLUNiAzmANuEA9Ll65si7CrgWnEB7X3I8QpHTtAzUGBWhjPjoq4pIxIMpHy4FfqSzWinikq1+bLzfdtDDGW7nMyyHgX5bJf04FuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkEgJVXL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423109,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEAH4kMers29RNhoHmvHiX9iEQ+9MlfRFW1a0fd7eunTsyjgHglI5EL4mfXLxuA4vEvqIZq4eUy2qrtLUNiAzmANuEA9Ll65si7CrgWnEB7X3I8QpHTtAzUGBWhjPjoq4pIxIMpHy4FfqSzWinikq1+bLzfdtDDGW7nMyyHgX5bJf04FuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkEgJVXL"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEAH4kMers29RNhoHmvHiX9iEQ+9MlfRFW1a0fd7eunTsyjgHglI5EL4mfXLxuA4vEvqIZq4eUy2qrtLUNiAzmANuEA9Ll65si7CrgWnEB7X3I8QpHTtAzUGBWhjPjoq4pIxIMpHy4FfqSzWinikq1+bLzfdtDDGW7nMyyHgX5bJf04FuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAmglh43zfNKjJNuVlX4mlDghPxHBaHKZmUnHbrslisHlkEgJVXL"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwCqDtOc3Amcplq0xSbaR585IcTo5Yw0MEz4WRUsC9u8JRP0SiaUk=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423108,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDHmLjZLphtjiFx+Evr+RXQQCsZhuC97LGS5ODAWqOU73TL7lIIQDgrf3wR4Psh0uAU73rVvRZePuk1qhVeFxgIuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT/T1EW5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423108,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDHmLjZLphtjiFx+Evr+RXQQCsZhuC97LGS5ODAWqOU73TL7lIIQDgrf3wR4Psh0uAU73rVvRZePuk1qhVeFxgIuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT/T1EW5",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423107,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDHmLjZLphtjiFx+Evr+RXQQCsZhuC97LGS5ODAWqOU73TL7lIIQDgrf3wR4Psh0uAU73rVvRZePuk1qhVeFxgIuEDVGxb5q98KbMaPtDTcz/Y7dwxg4wvefPCmLm0V5poqyQR6B93bnUSIQjooXReW9yOTEAPQid1ZFB+MbGxpeKELuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT/KZU7f"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423107,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEDHmLjZLphtjiFx+Evr+RXQQCsZhuC97LGS5ODAWqOU73TL7lIIQDgrf3wR4Psh0uAU73rVvRZePuk1qhVeFxgIuEDVGxb5q98KbMaPtDTcz/Y7dwxg4wvefPCmLm0V5poqyQR6B93bnUSIQjooXReW9yOTEAPQid1ZFB+MbGxpeKELuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT/KZU7f"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "state": "tx_+NILAfiEuEDHmLjZLphtjiFx+Evr+RXQQCsZhuC97LGS5ODAWqOU73TL7lIIQDgrf3wR4Psh0uAU73rVvRZePuk1qhVeFxgIuEDVGxb5q98KbMaPtDTcz/Y7dwxg4wvefPCmLm0V5poqyQR6B93bnUSIQjooXReW9yOTEAPQid1ZFB+MbGxpeKELuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT/KZU7f"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 9,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 9,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 10,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 10,
      "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
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
    ],
    "contracts": [
      "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg3RjYwp6lL7XajvEvm7iNq5KLyfXpybbmKQXb+iOzt6/5AYP4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4lKDdGNjCnqUvtdqO8S+buI2rkovJ9enJtuYpBdv6I7O3r/hxgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatig/OJdc7quICtQ5NDRs4AnNC4CAml1Rk+yukDNxgsfRl2AgICAoOE3SJ7NFgWikf5Diz5ODDyxSzAvj+fsIYI10YhYpvfagICAgID4T6DhN0iezRYFopH+Q4s+Tgw8sUswL4/n7CGCNdGIWKb32u2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/X4SaD84l1zuq4gK1Dk0NGzgCc0LgICaXVGT7K6QM3GCx9GXeegMoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAArj4qCRnDmiIQXoObi9BsqN64Iwy/saIfO5/lEZSSZpgSp538DA+Qap+QamoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+EOhAGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkoGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QO2oGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMLcUPQ=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ],
    "contracts": [
      "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaeg3RjYwp6lL7XajvEvm7iNq5KLyfXpybbmKQXb+iOzt6/5AYP4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4lKDdGNjCnqUvtdqO8S+buI2rkovJ9enJtuYpBdv6I7O3r/hxgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatig/OJdc7quICtQ5NDRs4AnNC4CAml1Rk+yukDNxgsfRl2AgICAoOE3SJ7NFgWikf5Diz5ODDyxSzAvj+fsIYI10YhYpvfagICAgID4T6DhN0iezRYFopH+Q4s+Tgw8sUswL4/n7CGCNdGIWKb32u2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/X4SaD84l1zuq4gK1Dk0NGzgCc0LgICaXVGT7K6QM3GCx9GXeegMoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAArj4qCRnDmiIQXoObi9BsqN64Iwy/saIfO5/lEZSSZpgSp538DA+Qap+QamoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhmoGMpBufQ7B6erpxok8dVQHiy4nhEx1V4pqP198nPlyLj+EOhAGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkoGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QO2oGR0KZ94ScjAEeD3CS92qy842WOMY9Vpxkf61voIMZZ6+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMLcUPQ=="
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
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303423106,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423106,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QL7ggJuAbkC9PkC8T8B+QLsuLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5P9BLORlFnNWP46Iw23Suc9M0u1MToYNRjGwe0xrNZbVuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AgIoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAc6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwLi5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMC4ufi3QAG4QGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkHklzMgEiJuGa1TSZkIu3K+YdJ9z2A0ZmrndttUxpu9m4cfhvKQKhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwBwehBWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5Ae4yCOvwLRy2pdytmVuW6e0b4NzEVlVrJMD+RlTwM5LuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AkJoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwHq9rHM=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDHmLjZLphtjiFx+Evr+RXQQCsZhuC97LGS5ODAWqOU73TL7lIIQDgrf3wR4Psh0uAU73rVvRZePuk1qhVeFxgIuEDVGxb5q98KbMaPtDTcz/Y7dwxg4wvefPCmLm0V5poqyQR6B93bnUSIQjooXReW9yOTEAPQid1ZFB+MbGxpeKELuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT/KZU7f",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABrDrddQ=="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423105,
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
    "gas_price": 1000008346
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423105,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "signed_tx": "tx_+Qi7CwHAuQi1+QiyggIJAaEGBQVu0pg7MPlup+nO9UDlkvFq81Ip1rRonz/eWbkEt3ChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwuNT40gsB+IS4QMeYuNkumG2OIXH4S+v5FdBAKxmG4L3ssZLk4MBao5TvdMvuUghAOCt/fBHg+yHS4BTvetW9Fl4+6TWqFV4XGAi4QNUbFvmr3wpsxo+0NNzP9jt3DGDjC9588KYubRXmmirJBHoH3dudRIhCOihdF5b3I5MQA9CJ3VkUH4xsbGl4oQu4SPhGOQKhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwCqDtOc3Amcplq0xSbaR585IcTo5Yw0MEz4WRUsC9u8JRPwu4uPi2ggI+AaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvChBWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkAQqDD0JAhDua6pq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgIPwItZLPdQEuQHtWOLm5lnCHzeWPC391fUoMzHqraP25Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaJigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5BABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQALkDiPkDhUABoGKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkuQNf+QNcKAGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuEBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5DqJ1/GRi5uSlXBXF7zuPMeGEyeQXkwdotSRIiuTGrJAuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AoKoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2w70ABoLHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Wi8oKAQCGP6olIl/1qulAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5IXECgEACrDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAEAhwHB0lc/OMgJ2SH5Wg==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_kPFqzEAutEbJ1fQDMQYhGBRFqrCeAPwm9e3ohHfVH6S7PwRtf",
          "gas": 1000000,
          "gas_price": 1000008346,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+Qj+CwH4QrhAiLrXgIo3IhrF92XYzsbhhII+Q/wC2w2X5kUXQQWiOF6SU9iQFwO+3j7u8nu8zhZ1iN89c1OENV/PyVio8tL1BbkItfkIsoICCQGhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEDHmLjZLphtjiFx+Evr+RXQQCsZhuC97LGS5ODAWqOU73TL7lIIQDgrf3wR4Psh0uAU73rVvRZePuk1qhVeFxgIuEDVGxb5q98KbMaPtDTcz/Y7dwxg4wvefPCmLm0V5poqyQR6B93bnUSIQjooXReW9yOTEAPQid1ZFB+MbGxpeKELuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8LuLj4toICPgGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AEKgw9CQIQ7muqauGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoCD8CLWSz3UBLkB7Vji5uZZwh83ljwt/dX1KDMx6q2j9uQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABAIcBwdJXPzjICUBk1Y4="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAiLrXgIo3IhrF92XYzsbhhII+Q/wC2w2X5kUXQQWiOF6SU9iQFwO+3j7u8nu8zhZ1iN89c1OENV/PyVio8tL1BbkItfkIsoICCQGhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEDHmLjZLphtjiFx+Evr+RXQQCsZhuC97LGS5ODAWqOU73TL7lIIQDgrf3wR4Psh0uAU73rVvRZePuk1qhVeFxgIuEDVGxb5q98KbMaPtDTcz/Y7dwxg4wvefPCmLm0V5poqyQR6B93bnUSIQjooXReW9yOTEAPQid1ZFB+MbGxpeKELuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8LuLj4toICPgGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AEKgw9CQIQ7muqauGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoCD8CLWSz3UBLkB7Vji5uZZwh83ljwt/dX1KDMx6q2j9uQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABAIcBwdJXPzjICUBk1Y4=",
      "type": "channel_force_progress_tx"
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAiLrXgIo3IhrF92XYzsbhhII+Q/wC2w2X5kUXQQWiOF6SU9iQFwO+3j7u8nu8zhZ1iN89c1OENV/PyVio8tL1BbkItfkIsoICCQGhBgUFbtKYOzD5bqfpzvVA5ZLxavNSKda0aJ8/3lm5BLdwoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEDHmLjZLphtjiFx+Evr+RXQQCsZhuC97LGS5ODAWqOU73TL7lIIQDgrf3wR4Psh0uAU73rVvRZePuk1qhVeFxgIuEDVGxb5q98KbMaPtDTcz/Y7dwxg4wvefPCmLm0V5poqyQR6B93bnUSIQjooXReW9yOTEAPQid1ZFB+MbGxpeKELuEj4RjkCoQYFBW7SmDsw+W6n6c71QOWS8WrzUinWtGifP95ZuQS3cAqg7TnNwJnKZatMUm2kefOSHE6OWMNDBM+FkVLAvbvCUT8LuLj4toICPgGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwoQVigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5AEKgw9CQIQ7muqauGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoCD8CLWSz3UBLkB7Vji5uZZwh83ljwt/dX1KDMx6q2j9uQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABomKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoWKCD5sEhtdZsqcEi1vhzEcLplyF8qQoTRneQHQ+gVTkEAC5A4j5A4VAAaBigg+bBIbXWbKnBItb4cxHC6ZchfKkKE0Z3kB0PoFU5LkDX/kDXCgBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQ6idfxkYubkpVwVxe87jzHhhMnkF5MHaLUkSIrkxqyQLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAKCqEFYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf9arpQAGgYoIPmwSG11mypwSLW+HMRwumXIXypChNGd5AdD6BVOSFxAoBAAqw70ABoFCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8Lwi8oKAQCGJGE5yoABAIcBwdJXPzjICUBk1Y4=",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423104,
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
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423104,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423103,
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
    "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
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
  "channel_id": "ch_3DG6vyom65PP65QZsUBnGhcLKcvDe4ZK5WBgBNMS9BB8bkWXM",
  "id": -576460752303423103,
  "jsonrpc": "2.0",
  "result": "ok",
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
      "fsm_id": "ba_EQxyS9CX7It78sfjCKh1jPKzlkjj58vsQNU8fyA6C0+MdmxW"
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
      "fsm_id": "ba_gDZ28eBjlmJztH+vKRVXm0AehO9XGyeKjP1OA/dlq/PsodQp"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgseHWlllQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423102,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAyrfmazTNDltynt2tC447AN58Ie6KoWUekKXjnE0IFcuSFyasOWAackqVwq71Q8Le6A4j2aIFk0kpB+PVC2GwAuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LHpFlYu4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423102,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "fsm_id": "ba_gDZ28eBjlmJztH+vKRVXm0AehO9XGyeKjP1OA/dlq/PsodQp",
      "signed_tx": "tx_+MsLAfhCuEAyrfmazTNDltynt2tC447AN58Ie6KoWUekKXjnE0IFcuSFyasOWAackqVwq71Q8Le6A4j2aIFk0kpB+PVC2GwAuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LHpFlYu4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423101,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAHhMYfTmqnhQneDfE6tv6ntqUwzRc2zxkh2dw9xp+RsGW1nSAD7R3fOw8GtdeZG61CKg4DYFOoyPK0mol7ZYVDbhAMq35ms0zQ5bcp7drQuOOwDefCHuiqFlHpCl45xNCBXLkhcmrDlgGnJKlcKu9UPC3ugOI9miBZNJKQfj1QthsALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx5oknIO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423101,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAHhMYfTmqnhQneDfE6tv6ntqUwzRc2zxkh2dw9xp+RsGW1nSAD7R3fOw8GtdeZG61CKg4DYFOoyPK0mol7ZYVDbhAMq35ms0zQ5bcp7drQuOOwDefCHuiqFlHpCl45xNCBXLkhcmrDlgGnJKlcKu9UPC3ugOI9miBZNJKQfj1QthsALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx5oknIO",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_EQxyS9CX7It78sfjCKh1jPKzlkjj58vsQNU8fyA6C0+MdmxW"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAHhMYfTmqnhQneDfE6tv6ntqUwzRc2zxkh2dw9xp+RsGW1nSAD7R3fOw8GtdeZG61CKg4DYFOoyPK0mol7ZYVDbhAMq35ms0zQ5bcp7drQuOOwDefCHuiqFlHpCl45xNCBXLkhcmrDlgGnJKlcKu9UPC3ugOI9miBZNJKQfj1QthsALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx5oknIO",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHhMYfTmqnhQneDfE6tv6ntqUwzRc2zxkh2dw9xp+RsGW1nSAD7R3fOw8GtdeZG61CKg4DYFOoyPK0mol7ZYVDbhAMq35ms0zQ5bcp7drQuOOwDefCHuiqFlHpCl45xNCBXLkhcmrDlgGnJKlcKu9UPC3ugOI9miBZNJKQfj1QthsALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx5oknIO",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHhMYfTmqnhQneDfE6tv6ntqUwzRc2zxkh2dw9xp+RsGW1nSAD7R3fOw8GtdeZG61CKg4DYFOoyPK0mol7ZYVDbhAMq35ms0zQ5bcp7drQuOOwDefCHuiqFlHpCl45xNCBXLkhcmrDlgGnJKlcKu9UPC3ugOI9miBZNJKQfj1QthsALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx5oknIO",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "message": {
        "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "message": {
        "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
  "id": -576460752303423100,
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
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423100,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+QENCwH4hLhAHhMYfTmqnhQneDfE6tv6ntqUwzRc2zxkh2dw9xp+RsGW1nSAD7R3fOw8GtdeZG61CKg4DYFOoyPK0mol7ZYVDbhAMq35ms0zQ5bcp7drQuOOwDefCHuiqFlHpCl45xNCBXLkhcmrDlgGnJKlcKu9UPC3ugOI9miBZNJKQfj1QthsALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx5oknIO"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+QENCwH4hLhAHhMYfTmqnhQneDfE6tv6ntqUwzRc2zxkh2dw9xp+RsGW1nSAD7R3fOw8GtdeZG61CKg4DYFOoyPK0mol7ZYVDbhAMq35ms0zQ5bcp7drQuOOwDefCHuiqFlHpCl45xNCBXLkhcmrDlgGnJKlcKu9UPC3ugOI9miBZNJKQfj1QthsALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx5oknIO"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjAqAIWu5MinH5T2hUs5XtWN3/av4FQRcLcBcK6qB+LG/r+JzkUqM=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "vm_version": 6
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
  "id": -576460752303423099,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA1vOEGOABCUV+WyAdrwSC7sbONlcppVWKVCjkuTGl1I2v7VH2mqRaJANQsEW7nCgAG6OzdS0GMWZE13QA7SBcEuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/jPTbXT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423099,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA1vOEGOABCUV+WyAdrwSC7sbONlcppVWKVCjkuTGl1I2v7VH2mqRaJANQsEW7nCgAG6OzdS0GMWZE13QA7SBcEuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/jPTbXT",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "vm_version": 6
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
  "id": -576460752303423098,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAd/5Mi6ZWVrEBJALVPggnSHyiizvWXb+S+pBVUKYDMglKoEI7LZZdCrjD4y//xYS2ZWRmRf4PSmRtElJn/dAEOuEA1vOEGOABCUV+WyAdrwSC7sbONlcppVWKVCjkuTGl1I2v7VH2mqRaJANQsEW7nCgAG6OzdS0GMWZE13QA7SBcEuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/gZ9KKD"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423098,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAd/5Mi6ZWVrEBJALVPggnSHyiizvWXb+S+pBVUKYDMglKoEI7LZZdCrjD4y//xYS2ZWRmRf4PSmRtElJn/dAEOuEA1vOEGOABCUV+WyAdrwSC7sbONlcppVWKVCjkuTGl1I2v7VH2mqRaJANQsEW7nCgAG6OzdS0GMWZE13QA7SBcEuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/gZ9KKD"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAd/5Mi6ZWVrEBJALVPggnSHyiizvWXb+S+pBVUKYDMglKoEI7LZZdCrjD4y//xYS2ZWRmRf4PSmRtElJn/dAEOuEA1vOEGOABCUV+WyAdrwSC7sbONlcppVWKVCjkuTGl1I2v7VH2mqRaJANQsEW7nCgAG6OzdS0GMWZE13QA7SBcEuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/gZ9KKD"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjA6AUpHMUud/1j7wHTBkJ0c/qfMEfZlEzIcuuUxe25zHMMY44zOI=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423097,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDSID348J6LR/JQDTpN7bh2cOmtNOYqFTreLhrfA7kskwuoMAL7RAjqzNREsOTajOuADXtxT5vPPHM2sQf1AvgMuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDE9OAEu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423097,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDSID348J6LR/JQDTpN7bh2cOmtNOYqFTreLhrfA7kskwuoMAL7RAjqzNREsOTajOuADXtxT5vPPHM2sQf1AvgMuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDE9OAEu",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423096,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECnZdA3qNk9lj7Opm0FaUqXT4QyeU8qhU+rf7eeI+yiU9u7HkXruhNTX6cIHDprlTwwMlOjhaZaAx7MVJtia+MPuEDSID348J6LR/JQDTpN7bh2cOmtNOYqFTreLhrfA7kskwuoMAL7RAjqzNREsOTajOuADXtxT5vPPHM2sQf1AvgMuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDFHRTn1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423096,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuECnZdA3qNk9lj7Opm0FaUqXT4QyeU8qhU+rf7eeI+yiU9u7HkXruhNTX6cIHDprlTwwMlOjhaZaAx7MVJtia+MPuEDSID348J6LR/JQDTpN7bh2cOmtNOYqFTreLhrfA7kskwuoMAL7RAjqzNREsOTajOuADXtxT5vPPHM2sQf1AvgMuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDFHRTn1"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuECnZdA3qNk9lj7Opm0FaUqXT4QyeU8qhU+rf7eeI+yiU9u7HkXruhNTX6cIHDprlTwwMlOjhaZaAx7MVJtia+MPuEDSID348J6LR/JQDTpN7bh2cOmtNOYqFTreLhrfA7kskwuoMAL7RAjqzNREsOTajOuADXtxT5vPPHM2sQf1AvgMuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDFHRTn1"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 4,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 3,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 3,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjBKBRiLe6ieGM0YoPUiSFj6wPGyXcSCzl5HxMOBrtVh7I4O1kdUs=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423095,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECcFFvqDfdI6XeKQmeK2MULwzyNpQ1eqwZPeDmfFiPtHWyKyHmAqBVZqKL+WByTX67GWSjeQ8NuTzP9WswDCnQAuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyOB+ghIR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423095,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+JALAfhCuECcFFvqDfdI6XeKQmeK2MULwzyNpQ1eqwZPeDmfFiPtHWyKyHmAqBVZqKL+WByTX67GWSjeQ8NuTzP9WswDCnQAuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyOB+ghIR",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423094,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAg/3Y+VimWB6EQ8nOg+LN42F9/BCDDjNeiQE+dTOjf7Rpja7fZrCygBjG1a7fCUIEiqS08MXU5OS4IEP8k8XcBuECcFFvqDfdI6XeKQmeK2MULwzyNpQ1eqwZPeDmfFiPtHWyKyHmAqBVZqKL+WByTX67GWSjeQ8NuTzP9WswDCnQAuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyOCSQK1+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423094,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAg/3Y+VimWB6EQ8nOg+LN42F9/BCDDjNeiQE+dTOjf7Rpja7fZrCygBjG1a7fCUIEiqS08MXU5OS4IEP8k8XcBuECcFFvqDfdI6XeKQmeK2MULwzyNpQ1eqwZPeDmfFiPtHWyKyHmAqBVZqKL+WByTX67GWSjeQ8NuTzP9WswDCnQAuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyOCSQK1+"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAg/3Y+VimWB6EQ8nOg+LN42F9/BCDDjNeiQE+dTOjf7Rpja7fZrCygBjG1a7fCUIEiqS08MXU5OS4IEP8k8XcBuECcFFvqDfdI6XeKQmeK2MULwzyNpQ1eqwZPeDmfFiPtHWyKyHmAqBVZqKL+WByTX67GWSjeQ8NuTzP9WswDCnQAuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyOCSQK1+"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjBaAIkDQISw6F7owgvj10Z3DMAc71UKcDHSJJBS3HMp/Hc0IlHfk=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423093,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDlmqWoHdjgdFvsS7332YcDKRK1c3krj5hHvfvqzbYZnbLbZzPt/hc/Yjc9R34qab5kmT9GTqih7omheSTevf0BuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3PW4GNk"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423093,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDlmqWoHdjgdFvsS7332YcDKRK1c3krj5hHvfvqzbYZnbLbZzPt/hc/Yjc9R34qab5kmT9GTqih7omheSTevf0BuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3PW4GNk",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423092,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECZRlv3Is+5nBj7gopZOWpBCP5vCc2KA9BuspOQiax7pRQyB+g9ayMQrnHVjUFBZrry9AeX1hOuIrWLaFf1SrsKuEDlmqWoHdjgdFvsS7332YcDKRK1c3krj5hHvfvqzbYZnbLbZzPt/hc/Yjc9R34qab5kmT9GTqih7omheSTevf0BuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3MDdijK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423092,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuECZRlv3Is+5nBj7gopZOWpBCP5vCc2KA9BuspOQiax7pRQyB+g9ayMQrnHVjUFBZrry9AeX1hOuIrWLaFf1SrsKuEDlmqWoHdjgdFvsS7332YcDKRK1c3krj5hHvfvqzbYZnbLbZzPt/hc/Yjc9R34qab5kmT9GTqih7omheSTevf0BuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3MDdijK"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuECZRlv3Is+5nBj7gopZOWpBCP5vCc2KA9BuspOQiax7pRQyB+g9ayMQrnHVjUFBZrry9AeX1hOuIrWLaFf1SrsKuEDlmqWoHdjgdFvsS7332YcDKRK1c3krj5hHvfvqzbYZnbLbZzPt/hc/Yjc9R34qab5kmT9GTqih7omheSTevf0BuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3MDdijK"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjBqCorP0XGr2ciKksOWED8YlfkYS9HacAuEW5Qy2wC97GVO8G0gg=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423091,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC4TmwoE0gZ2j6qll03R/iAoxN6xhz0LudyzqYSOSy999gq+X4xAR4N6u3/vNU93EV5IfhUeRciuXFw7ryaipcBuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlS8fsSF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423091,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC4TmwoE0gZ2j6qll03R/iAoxN6xhz0LudyzqYSOSy999gq+X4xAR4N6u3/vNU93EV5IfhUeRciuXFw7ryaipcBuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlS8fsSF",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423090,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAh4JJ8l33oxP0gkEk8Qpzt+TVqNxqwUbsB4q7EJQbGlAbAgmYnM1VxxPBzuROhTArPT6JBtAFTnWOi58/PNa8BuEC4TmwoE0gZ2j6qll03R/iAoxN6xhz0LudyzqYSOSy999gq+X4xAR4N6u3/vNU93EV5IfhUeRciuXFw7ryaipcBuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlRzw6O0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423090,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAh4JJ8l33oxP0gkEk8Qpzt+TVqNxqwUbsB4q7EJQbGlAbAgmYnM1VxxPBzuROhTArPT6JBtAFTnWOi58/PNa8BuEC4TmwoE0gZ2j6qll03R/iAoxN6xhz0LudyzqYSOSy999gq+X4xAR4N6u3/vNU93EV5IfhUeRciuXFw7ryaipcBuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlRzw6O0"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAh4JJ8l33oxP0gkEk8Qpzt+TVqNxqwUbsB4q7EJQbGlAbAgmYnM1VxxPBzuROhTArPT6JBtAFTnWOi58/PNa8BuEC4TmwoE0gZ2j6qll03R/iAoxN6xhz0LudyzqYSOSy999gq+X4xAR4N6u3/vNU93EV5IfhUeRciuXFw7ryaipcBuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlRzw6O0"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 5,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 5,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 6,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 6,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 3,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 3,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjB6BDrzxhf3PQBW5DBzBVDzZpdEXWQahfr195nGdVCBrefY3954Q=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423089,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC8T6IgGeJ1MoCOSI0uQzrfCMG9dtH79Kn0DycZhb8C710IO78HHqghVyNJU7nVOIVfeE1K1kYyeijn5JLW2AYGuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n20Gz8r"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423089,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC8T6IgGeJ1MoCOSI0uQzrfCMG9dtH79Kn0DycZhb8C710IO78HHqghVyNJU7nVOIVfeE1K1kYyeijn5JLW2AYGuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n20Gz8r",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423088,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEALy7MlIcmy3mpQIO1Xa9BUCvoCcisoV/qmwhn62sUpOd7zlsq8MC1QEPc8hBzb3SARoOwXpD2BX6KAfRdwmc8JuEC8T6IgGeJ1MoCOSI0uQzrfCMG9dtH79Kn0DycZhb8C710IO78HHqghVyNJU7nVOIVfeE1K1kYyeijn5JLW2AYGuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n1Xr9Lr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423088,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEALy7MlIcmy3mpQIO1Xa9BUCvoCcisoV/qmwhn62sUpOd7zlsq8MC1QEPc8hBzb3SARoOwXpD2BX6KAfRdwmc8JuEC8T6IgGeJ1MoCOSI0uQzrfCMG9dtH79Kn0DycZhb8C710IO78HHqghVyNJU7nVOIVfeE1K1kYyeijn5JLW2AYGuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n1Xr9Lr"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEALy7MlIcmy3mpQIO1Xa9BUCvoCcisoV/qmwhn62sUpOd7zlsq8MC1QEPc8hBzb3SARoOwXpD2BX6KAfRdwmc8JuEC8T6IgGeJ1MoCOSI0uQzrfCMG9dtH79Kn0DycZhb8C710IO78HHqghVyNJU7nVOIVfeE1K1kYyeijn5JLW2AYGuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n1Xr9Lr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 8,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 7,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 7,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjCKBeN8SRXeZrW6awTv1d98AmPBx1GrjbEg8v45BpJOoTy90O0FE=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423087,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBXA94G7WJo+OytmpOIf2VOlKkCJ4t+MQaoUaseLOZL/VUpdLbBpIx6dRMWUns6+u5Nichc8oiBtAeZuetYSJgPuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8uGgoRv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423087,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBXA94G7WJo+OytmpOIf2VOlKkCJ4t+MQaoUaseLOZL/VUpdLbBpIx6dRMWUns6+u5Nichc8oiBtAeZuetYSJgPuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8uGgoRv",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423086,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBD7+W0wWQ5QpgNHDwE04XLQonM4jWPiuFAr2O2FvjCYBo2FMi9F/TDJa3nxzRzn+VgyjV5iABYQOn46YtexsUBuEBXA94G7WJo+OytmpOIf2VOlKkCJ4t+MQaoUaseLOZL/VUpdLbBpIx6dRMWUns6+u5Nichc8oiBtAeZuetYSJgPuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8u7maZz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423086,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEBD7+W0wWQ5QpgNHDwE04XLQonM4jWPiuFAr2O2FvjCYBo2FMi9F/TDJa3nxzRzn+VgyjV5iABYQOn46YtexsUBuEBXA94G7WJo+OytmpOIf2VOlKkCJ4t+MQaoUaseLOZL/VUpdLbBpIx6dRMWUns6+u5Nichc8oiBtAeZuetYSJgPuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8u7maZz"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEBD7+W0wWQ5QpgNHDwE04XLQonM4jWPiuFAr2O2FvjCYBo2FMi9F/TDJa3nxzRzn+VgyjV5iABYQOn46YtexsUBuEBXA94G7WJo+OytmpOIf2VOlKkCJ4t+MQaoUaseLOZL/VUpdLbBpIx6dRMWUns6+u5Nichc8oiBtAeZuetYSJgPuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8u7maZz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjCaCJPRoEoUA9eJQfV7KhvjA4FYszagJTS++DGJSwbVvZU8N+VWI=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423085,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECkZxh7YdFuEovSn1kHPsFj1UnaCcodYwaK7Cp9z/aA0PorQPRAeqMxXBpygxrbpkKpti6b/fT7qUh90wqYShMLuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VOMD+/r"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423085,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+JALAfhCuECkZxh7YdFuEovSn1kHPsFj1UnaCcodYwaK7Cp9z/aA0PorQPRAeqMxXBpygxrbpkKpti6b/fT7qUh90wqYShMLuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VOMD+/r",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423084,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAzLFkNcYjs/d7DJTq28u+h3mLISr48XPXgws/AWqVWpxXAlO0FAFkOdgDPfh18J5RU7CMfwMaGQYacEoXkvIQDuECkZxh7YdFuEovSn1kHPsFj1UnaCcodYwaK7Cp9z/aA0PorQPRAeqMxXBpygxrbpkKpti6b/fT7qUh90wqYShMLuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VOjRhqs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423084,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAzLFkNcYjs/d7DJTq28u+h3mLISr48XPXgws/AWqVWpxXAlO0FAFkOdgDPfh18J5RU7CMfwMaGQYacEoXkvIQDuECkZxh7YdFuEovSn1kHPsFj1UnaCcodYwaK7Cp9z/aA0PorQPRAeqMxXBpygxrbpkKpti6b/fT7qUh90wqYShMLuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VOjRhqs"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAzLFkNcYjs/d7DJTq28u+h3mLISr48XPXgws/AWqVWpxXAlO0FAFkOdgDPfh18J5RU7CMfwMaGQYacEoXkvIQDuECkZxh7YdFuEovSn1kHPsFj1UnaCcodYwaK7Cp9z/aA0PorQPRAeqMxXBpygxrbpkKpti6b/fT7qUh90wqYShMLuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VOjRhqs"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjCqCbpTUGPjYK8W9Hbq08zfsMGe3sdz1U8ypN57sF/+l8Jsf3Xxo=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423083,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA3pFHLgbfDCewz19AIb3gsAhXlLiR8QyH4bTMBiBmSWEDV2Cq8cyUUGUvlPUjKxJq9EDfKCcgxMq9crZov3bgNuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCYJTS5M"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423083,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA3pFHLgbfDCewz19AIb3gsAhXlLiR8QyH4bTMBiBmSWEDV2Cq8cyUUGUvlPUjKxJq9EDfKCcgxMq9crZov3bgNuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCYJTS5M",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423082,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAb01Ox49ee/RLBCfdzx9T7xE3tP/V8rSIMGf7XPeNsmejw7PpFZgGeqHtLQqv3Pxl4oxbG3qe6A2RP1Hk2JKwAuEA3pFHLgbfDCewz19AIb3gsAhXlLiR8QyH4bTMBiBmSWEDV2Cq8cyUUGUvlPUjKxJq9EDfKCcgxMq9crZov3bgNuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCZy4H5l"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423082,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAb01Ox49ee/RLBCfdzx9T7xE3tP/V8rSIMGf7XPeNsmejw7PpFZgGeqHtLQqv3Pxl4oxbG3qe6A2RP1Hk2JKwAuEA3pFHLgbfDCewz19AIb3gsAhXlLiR8QyH4bTMBiBmSWEDV2Cq8cyUUGUvlPUjKxJq9EDfKCcgxMq9crZov3bgNuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCZy4H5l"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "state": "tx_+NILAfiEuEAb01Ox49ee/RLBCfdzx9T7xE3tP/V8rSIMGf7XPeNsmejw7PpFZgGeqHtLQqv3Pxl4oxbG3qe6A2RP1Hk2JKwAuEA3pFHLgbfDCewz19AIb3gsAhXlLiR8QyH4bTMBiBmSWEDV2Cq8cyUUGUvlPUjKxJq9EDfKCcgxMq9crZov3bgNuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCZy4H5l"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 9,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 9,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 10,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 10,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ],
    "contracts": [
      "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+Mdj4gioEYHV7uWYqzLlPuu/XRDajGbC3I7HdTE1RX5AYP4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4SaB6t8a6kE6M48iOxU7hBaDUl+z5WHzF6JLatsvxgJMDGuegNPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OFxAoBAAr4lKCT4x2PiCKgRgdXu5ZirMuU+679dENqMZsLcjsd1MTVFfhxgKB6t8a6kE6M48iOxU7hBaDUl+z5WHzF6JLatsvxgJMDGoCAgKDRdKEaoffGcn4cP7JvVpPoukzl9YawGvMdYjrlH/qgooCAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgID4T6DRdKEaoffGcn4cP7JvVpPoukzl9YawGvMdYjrlH/qgou2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/fj4qA19Bz7NeyhIKCs38MFwBVsz68BMko84tymGS666tIKqMDA+Qap+QamoDnTnL+cEufMb+bOniQkxAOQGj/Sv1lbgTl4puy9GwBt+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+GagOdOcv5wS58xv5s6eJCTEA5AaP9K/WVuBOXim7L0bAG34Q6EAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OgcqwZ+7hASIIrq9ppKxV/3vuJGfYXgwZLsEpkkIIAe8/4dKBIER5XC7xxbur+BQq0j0FPtJBdjUer3LAh9f2Bgo7xRfhRoBVqI09vFvWdE58TQLrptCdtmByUCsuEkhUhLVLTF8FfoMMN5omVEejhhfhAqs9cOijYD5ArIrSxrLGPPIGxA0Z3gICAgICAgICAgICAgICA+QO2oHKsGfu4QEiCK6vaaSsVf977iRn2F4MGS7BKZJCCAHvP+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAkNix/w=="
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
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ],
    "contracts": [
      "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+Mdj4gioEYHV7uWYqzLlPuu/XRDajGbC3I7HdTE1RX5AYP4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4SaB6t8a6kE6M48iOxU7hBaDUl+z5WHzF6JLatsvxgJMDGuegNPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OFxAoBAAr4lKCT4x2PiCKgRgdXu5ZirMuU+679dENqMZsLcjsd1MTVFfhxgKB6t8a6kE6M48iOxU7hBaDUl+z5WHzF6JLatsvxgJMDGoCAgKDRdKEaoffGcn4cP7JvVpPoukzl9YawGvMdYjrlH/qgooCAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgID4T6DRdKEaoffGcn4cP7JvVpPoukzl9YawGvMdYjrlH/qgou2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/fj4qA19Bz7NeyhIKCs38MFwBVsz68BMko84tymGS666tIKqMDA+Qap+QamoDnTnL+cEufMb+bOniQkxAOQGj/Sv1lbgTl4puy9GwBt+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+GagOdOcv5wS58xv5s6eJCTEA5AaP9K/WVuBOXim7L0bAG34Q6EAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OgcqwZ+7hASIIrq9ppKxV/3vuJGfYXgwZLsEpkkIIAe8/4dKBIER5XC7xxbur+BQq0j0FPtJBdjUer3LAh9f2Bgo7xRfhRoBVqI09vFvWdE58TQLrptCdtmByUCsuEkhUhLVLTF8FfoMMN5omVEejhhfhAqs9cOijYD5ArIrSxrLGPPIGxA0Z3gICAgICAgICAgICAgICA+QO2oHKsGfu4QEiCK6vaaSsVf977iRn2F4MGS7BKZJCCAHvP+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAkNix/w=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303423081,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423081,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QeoggJuAbkHofkHnj8B+QeZuLn4t0ABuEAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw/ufvjimPkppe+Dgl5/lWBWFz3108sOOJ8t1z1VIDJFXuHH4bykCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gcHoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYAwLi5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8PXK/Iyce6OqTzXHY9BdvEkp7Uvc7nFnXriL6WIazA6WLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAFBaEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAMC4ufi3QAG4QBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDyxgOKMOWaeM3vPsmcctm3cm7pIYPkmbyPCRA1RtRWkS4cfhvKQKhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwAwOhBRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFQDAuLn4t0ABuEAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw5zeXYvCmX+dH/5SvLqrB8Lv8Zp18i+/pmUuKzqp2+0uuHH4bykCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1goKoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Nv/umPuzYoFvZ2NkRSvjGllt27gqJftiuxie47j23M3Lhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YJCaEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMC4ufi3QAG4QBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDWV8rInHJz1MXFFPDS0wf0pNxm8PVX2MeoexYs+tPwo+4cfhvKQKhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WCAihBRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDAYIBzqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAuLn4t0ABuEAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw0vUs/yNgnhRCopO30t+ZcRIYdc2l34GMNaHDSoJZu2kuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AQEoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwGCAc6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwLi5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MUf0v0q9Y5fIV5MPZEd/a4Pjgkv7k240em2pF3lNEiCrhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAGBqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAMC5Ab75AbtAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MCcJD+dT8/fZHPCpoRUInIuHshRxuIoI5MO8Vv4cIzXrkBdPkBcSkCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AICoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwCCAT+5ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABUAwFu5zA0=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAb01Ox49ee/RLBCfdzx9T7xE3tP/V8rSIMGf7XPeNsmejw7PpFZgGeqHtLQqv3Pxl4oxbG3qe6A2RP1Hk2JKwAuEA3pFHLgbfDCewz19AIb3gsAhXlLiR8QyH4bTMBiBmSWEDV2Cq8cyUUGUvlPUjKxJq9EDfKCcgxMq9crZov3bgNuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCZy4H5l",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABohT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC5A4j5A4VAAaAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw7kDX/kDXCgBoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Oc3l2Lwpl/nR/+Ury6qwfC7/GadfIvv6ZlLis6qdvtLrhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YKCqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/eq6UABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDhcQKAQAKYD7MFg=="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423080,
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "gas_price": 1000006096
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423080,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "signed_tx": "tx_+Qi7CwHAuQi1+QiyggIJAaEGXrFHMr1j/iUf0KwS6kmie6b/iGMc6mGmDUbZtEaRu+OhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WuNT40gsB+IS4QBvTU7Hj1579EsEJ93PH1PvETe0/9XytIgwZ/tc942yZ6PDs+kVmAZ6oe0tCq/c/GXijFsbep7oDZE/UeTYkrAC4QDekUcuBt8MJ7DPX0AhveCwCFeUuJHxDIfhtMwGIGZJYQNXYKrxzJRQZS+U9SMrEmr0QN8oJyDEyr1ytmi/duA24SPhGOQKhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjCqCbpTUGPjYK8W9Hbq08zfsMGe3sdz1U8ypN57sF/+l8Jgu4uPi2ggI+AaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9ahBRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDAQqDD0JAhDua4dC4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCguIl74ok0Vi3DhY9gMtm2IZec3uWatajdauyM51GHXku5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaIU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwxABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQALkDiPkDhUABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDuQNf+QNcKAGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuEAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw5zeXYvCmX+dH/5SvLqrB8Lv8Zp18i+/pmUuKzqp2+0uuHH4bykCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1goKoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2w70ABoLHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Wi8oKAQCGP6olIl//sO9AAaBQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcp/96rpQAGgFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OFxAoBAAoAhwHB0hTrKkAfCOyCDA==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1000006096,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+Qj+CwH4QrhAkfAoe/K3DvaQ/bAOWLCf5hN+p5BVPe4xCB5otwGNdJYW//UtSvs7mlaSZe8iSah53XYIdNSNo4R/yvKQgxepCrkItfkIsoICCQGhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAb01Ox49ee/RLBCfdzx9T7xE3tP/V8rSIMGf7XPeNsmejw7PpFZgGeqHtLQqv3Pxl4oxbG3qe6A2RP1Hk2JKwAuEA3pFHLgbfDCewz19AIb3gsAhXlLiR8QyH4bTMBiBmSWEDV2Cq8cyUUGUvlPUjKxJq9EDfKCcgxMq9crZov3bgNuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCYLuLj4toICPgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwEKgw9CQIQ7muHQuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoLiJe+KJNFYtw4WPYDLZtiGXnN7lmrWo3WrsjOdRh15LuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABohT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC5A4j5A4VAAaAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw7kDX/kDXCgBoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Oc3l2Lwpl/nR/+Ury6qwfC7/GadfIvv6ZlLis6qdvtLrhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YKCqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/eq6UABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDhcQKAQAKAIcBwdIU6ypAH/eDL+c="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAkfAoe/K3DvaQ/bAOWLCf5hN+p5BVPe4xCB5otwGNdJYW//UtSvs7mlaSZe8iSah53XYIdNSNo4R/yvKQgxepCrkItfkIsoICCQGhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAb01Ox49ee/RLBCfdzx9T7xE3tP/V8rSIMGf7XPeNsmejw7PpFZgGeqHtLQqv3Pxl4oxbG3qe6A2RP1Hk2JKwAuEA3pFHLgbfDCewz19AIb3gsAhXlLiR8QyH4bTMBiBmSWEDV2Cq8cyUUGUvlPUjKxJq9EDfKCcgxMq9crZov3bgNuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCYLuLj4toICPgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwEKgw9CQIQ7muHQuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoLiJe+KJNFYtw4WPYDLZtiGXnN7lmrWo3WrsjOdRh15LuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABohT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC5A4j5A4VAAaAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw7kDX/kDXCgBoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Oc3l2Lwpl/nR/+Ury6qwfC7/GadfIvv6ZlLis6qdvtLrhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YKCqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/eq6UABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDhcQKAQAKAIcBwdIU6ypAH/eDL+c=",
      "type": "channel_force_progress_tx"
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAkfAoe/K3DvaQ/bAOWLCf5hN+p5BVPe4xCB5otwGNdJYW//UtSvs7mlaSZe8iSah53XYIdNSNo4R/yvKQgxepCrkItfkIsoICCQGhBl6xRzK9Y/4lH9CsEupJonum/4hjHOphpg1G2bRGkbvjoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAb01Ox49ee/RLBCfdzx9T7xE3tP/V8rSIMGf7XPeNsmejw7PpFZgGeqHtLQqv3Pxl4oxbG3qe6A2RP1Hk2JKwAuEA3pFHLgbfDCewz19AIb3gsAhXlLiR8QyH4bTMBiBmSWEDV2Cq8cyUUGUvlPUjKxJq9EDfKCcgxMq9crZov3bgNuEj4RjkCoQZesUcyvWP+JR/QrBLqSaJ7pv+IYxzqYaYNRtm0RpG74wqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCYLuLj4toICPgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwEKgw9CQIQ7muHQuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoLiJe+KJNFYtw4WPYDLZtiGXnN7lmrWo3WrsjOdRh15LuQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABohT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC5A4j5A4VAAaAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw7kDX/kDXCgBoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Oc3l2Lwpl/nR/+Ury6qwfC7/GadfIvv6ZlLis6qdvtLrhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YKCqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/eq6UABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDhcQKAQAKAIcBwdIU6ypAH/eDL+c=",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423079,
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
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423079,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423078,
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
    "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
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
  "channel_id": "ch_ihnyRPm1yTi3qLuRVk4pTzjVWaw9AeANUs31E6FAQtaHVaDQp",
  "id": -576460752303423078,
  "jsonrpc": "2.0",
  "result": "ok",
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
      "fsm_id": "ba_RC4Dds/5DQk7MAqwJ+R0rtB0yc1yyHhCE1Va0zW9/CZnHtZZ"
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
      "fsm_id": "ba_H9ZhBCex2d7TYEb0V13k2tyGS5xc2Df02/uO6gzXlUt7Wmq+"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsg7NSLlg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423077,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBoZQzbH7L2hB7chhKJIzffMv5KAYYr4F79U/mYQVMfnayea6puAJ7XSzvRn8kf6wQnZ6WQrlHTOj5hjZtJUvICuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LIE5Tf3k="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423077,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "fsm_id": "ba_H9ZhBCex2d7TYEb0V13k2tyGS5xc2Df02/uO6gzXlUt7Wmq+",
      "signed_tx": "tx_+MsLAfhCuEBoZQzbH7L2hB7chhKJIzffMv5KAYYr4F79U/mYQVMfnayea6puAJ7XSzvRn8kf6wQnZ6WQrlHTOj5hjZtJUvICuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LIE5Tf3k=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423076,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAaGUM2x+y9oQe3IYSiSM33zL+SgGGK+Be/VP5mEFTH52snmuqbgCe10s70Z/JH+sEJ2elkK5R0zo+YY2bSVLyArhAgwS5j9PX8zl583vsor4s+KTA34yOsoRje7sw6xESBIjEeufdRvTwrlcFrirLbeltU93jY9APSFRITDVx4aVaA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCyBQoaXC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423076,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAaGUM2x+y9oQe3IYSiSM33zL+SgGGK+Be/VP5mEFTH52snmuqbgCe10s70Z/JH+sEJ2elkK5R0zo+YY2bSVLyArhAgwS5j9PX8zl583vsor4s+KTA34yOsoRje7sw6xESBIjEeufdRvTwrlcFrirLbeltU93jY9APSFRITDVx4aVaA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCyBQoaXC",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_RC4Dds/5DQk7MAqwJ+R0rtB0yc1yyHhCE1Va0zW9/CZnHtZZ"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAaGUM2x+y9oQe3IYSiSM33zL+SgGGK+Be/VP5mEFTH52snmuqbgCe10s70Z/JH+sEJ2elkK5R0zo+YY2bSVLyArhAgwS5j9PX8zl583vsor4s+KTA34yOsoRje7sw6xESBIjEeufdRvTwrlcFrirLbeltU93jY9APSFRITDVx4aVaA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCyBQoaXC",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAaGUM2x+y9oQe3IYSiSM33zL+SgGGK+Be/VP5mEFTH52snmuqbgCe10s70Z/JH+sEJ2elkK5R0zo+YY2bSVLyArhAgwS5j9PX8zl583vsor4s+KTA34yOsoRje7sw6xESBIjEeufdRvTwrlcFrirLbeltU93jY9APSFRITDVx4aVaA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCyBQoaXC",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAaGUM2x+y9oQe3IYSiSM33zL+SgGGK+Be/VP5mEFTH52snmuqbgCe10s70Z/JH+sEJ2elkK5R0zo+YY2bSVLyArhAgwS5j9PX8zl583vsor4s+KTA34yOsoRje7sw6xESBIjEeufdRvTwrlcFrirLbeltU93jY9APSFRITDVx4aVaA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCyBQoaXC",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "message": {
        "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "message": {
        "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
  "id": -576460752303423075,
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
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423075,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+QENCwH4hLhAaGUM2x+y9oQe3IYSiSM33zL+SgGGK+Be/VP5mEFTH52snmuqbgCe10s70Z/JH+sEJ2elkK5R0zo+YY2bSVLyArhAgwS5j9PX8zl583vsor4s+KTA34yOsoRje7sw6xESBIjEeufdRvTwrlcFrirLbeltU93jY9APSFRITDVx4aVaA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCyBQoaXC"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+QENCwH4hLhAaGUM2x+y9oQe3IYSiSM33zL+SgGGK+Be/VP5mEFTH52snmuqbgCe10s70Z/JH+sEJ2elkK5R0zo+YY2bSVLyArhAgwS5j9PX8zl583vsor4s+KTA34yOsoRje7sw6xESBIjEeufdRvTwrlcFrirLbeltU93jY9APSFRITDVx4aVaA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCyBQoaXC"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2AqAIWu5MinH5T2hUs5XtWN3/av4FQRcLcBcK6qB+LG/r+PQ+ckc=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "vm_version": 6
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
  "id": -576460752303423074,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA2uTIZTGUOaXpOSsJxY0ZOFCHzkd5JRTfkx9DcbItJ1hbqr5wrH6+UM+vDP4ahbIsVYe8yhgkS1rvgn1019WsPuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/hNlGAM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423074,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA2uTIZTGUOaXpOSsJxY0ZOFCHzkd5JRTfkx9DcbItJ1hbqr5wrH6+UM+vDP4ahbIsVYe8yhgkS1rvgn1019WsPuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/hNlGAM",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "vm_version": 6
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
  "id": -576460752303423073,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA2uTIZTGUOaXpOSsJxY0ZOFCHzkd5JRTfkx9DcbItJ1hbqr5wrH6+UM+vDP4ahbIsVYe8yhgkS1rvgn1019WsPuEBCC9+LmNs01f62r07y1uBscinh9jo1oHb7Xch9I1UnJZIrKbNfJtzH9YclY+ntSg/mK4PzknIY+O1VUw3sdwYKuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/hw6dOA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423073,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEA2uTIZTGUOaXpOSsJxY0ZOFCHzkd5JRTfkx9DcbItJ1hbqr5wrH6+UM+vDP4ahbIsVYe8yhgkS1rvgn1019WsPuEBCC9+LmNs01f62r07y1uBscinh9jo1oHb7Xch9I1UnJZIrKbNfJtzH9YclY+ntSg/mK4PzknIY+O1VUw3sdwYKuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/hw6dOA"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEA2uTIZTGUOaXpOSsJxY0ZOFCHzkd5JRTfkx9DcbItJ1hbqr5wrH6+UM+vDP4ahbIsVYe8yhgkS1rvgn1019WsPuEBCC9+LmNs01f62r07y1uBscinh9jo1oHb7Xch9I1UnJZIrKbNfJtzH9YclY+ntSg/mK4PzknIY+O1VUw3sdwYKuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgKgCFruTIpx+U9oVLOV7Vjd/2r+BUEXC3AXCuqgfixv6/hw6dOA"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2A6AUpHMUud/1j7wHTBkJ0c/qfMEfZlEzIcuuUxe25zHMMSdvEJM=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423072,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDju6zBWLNEm7CNQVLf2GmN/JECwvGSGvD/B5lsBbiizwagDUu3x1ttJFnCqXXsguduCF8fR1JUsO7s8WD+cIcLuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDH6FLWl"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423072,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDju6zBWLNEm7CNQVLf2GmN/JECwvGSGvD/B5lsBbiizwagDUu3x1ttJFnCqXXsguduCF8fR1JUsO7s8WD+cIcLuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDH6FLWl",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423071,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBpsMEj9RPuvXr+tXuo5Z8pJvesCfIAuH8hcmW1DbX79CtcKmfBpXguNEmrY3Kn9x/NIhzZlF5MrXjyZSeHlnYAuEDju6zBWLNEm7CNQVLf2GmN/JECwvGSGvD/B5lsBbiizwagDUu3x1ttJFnCqXXsguduCF8fR1JUsO7s8WD+cIcLuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDH2jG0G"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423071,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEBpsMEj9RPuvXr+tXuo5Z8pJvesCfIAuH8hcmW1DbX79CtcKmfBpXguNEmrY3Kn9x/NIhzZlF5MrXjyZSeHlnYAuEDju6zBWLNEm7CNQVLf2GmN/JECwvGSGvD/B5lsBbiizwagDUu3x1ttJFnCqXXsguduCF8fR1JUsO7s8WD+cIcLuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDH2jG0G"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEBpsMEj9RPuvXr+tXuo5Z8pJvesCfIAuH8hcmW1DbX79CtcKmfBpXguNEmrY3Kn9x/NIhzZlF5MrXjyZSeHlnYAuEDju6zBWLNEm7CNQVLf2GmN/JECwvGSGvD/B5lsBbiizwagDUu3x1ttJFnCqXXsguduCF8fR1JUsO7s8WD+cIcLuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgOgFKRzFLnf9Y+8B0wZCdHP6nzBH2ZRMyHLrlMXtucxzDH2jG0G"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 4,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 3,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 3,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2BKBRiLe6ieGM0YoPUiSFj6wPGyXcSCzl5HxMOBrtVh7I4H7ad5k=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423070,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBv11MX0Nw8wppkMNo0x1IT3kmP+sj9Gi7U+tFO18RwcivhS7c//P1FwzPYK72jm4i/6IPuh0X4ETrP3K0Hz8ANuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyODQxqya"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423070,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBv11MX0Nw8wppkMNo0x1IT3kmP+sj9Gi7U+tFO18RwcivhS7c//P1FwzPYK72jm4i/6IPuh0X4ETrP3K0Hz8ANuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyODQxqya",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423069,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAMwwtnLQb9fuQCxkYoDimEpDoBvMyXo5TEqbhSuUDnAhl1tzpBWEJGkongn+pEJzvb1E6Xan1qr1E37TC3CQUNuEBv11MX0Nw8wppkMNo0x1IT3kmP+sj9Gi7U+tFO18RwcivhS7c//P1FwzPYK72jm4i/6IPuh0X4ETrP3K0Hz8ANuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyOC9er4Z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423069,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEAMwwtnLQb9fuQCxkYoDimEpDoBvMyXo5TEqbhSuUDnAhl1tzpBWEJGkongn+pEJzvb1E6Xan1qr1E37TC3CQUNuEBv11MX0Nw8wppkMNo0x1IT3kmP+sj9Gi7U+tFO18RwcivhS7c//P1FwzPYK72jm4i/6IPuh0X4ETrP3K0Hz8ANuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyOC9er4Z"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEAMwwtnLQb9fuQCxkYoDimEpDoBvMyXo5TEqbhSuUDnAhl1tzpBWEJGkongn+pEJzvb1E6Xan1qr1E37TC3CQUNuEBv11MX0Nw8wppkMNo0x1IT3kmP+sj9Gi7U+tFO18RwcivhS7c//P1FwzPYK72jm4i/6IPuh0X4ETrP3K0Hz8ANuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgSgUYi3uonhjNGKD1IkhY+sDxsl3Egs5eR8TDga7VYeyOC9er4Z"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2BaAIkDQISw6F7owgvj10Z3DMAc71UKcDHSJJBS3HMp/Hcy4IGcQ=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423068,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECpI0sFokJHRmXsUjnWZ41Ff2WP+k3NfMH8/DJlfOs32dbclvQXk3zgLq1Q9pKLmXnjY4VGuVkOYCHJdrPEAKUOuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3NEvJCU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423068,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+JALAfhCuECpI0sFokJHRmXsUjnWZ41Ff2WP+k3NfMH8/DJlfOs32dbclvQXk3zgLq1Q9pKLmXnjY4VGuVkOYCHJdrPEAKUOuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3NEvJCU",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423067,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBwE1eX5ppGKYs/oT4vpg2MqySAVe6Xm4oz8XlzN4AnK0XMiQcyWfW6ihMLlVFBlgHuASRcUiIdnts23vHsWGACuECpI0sFokJHRmXsUjnWZ41Ff2WP+k3NfMH8/DJlfOs32dbclvQXk3zgLq1Q9pKLmXnjY4VGuVkOYCHJdrPEAKUOuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3Oz2F7k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423067,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEBwE1eX5ppGKYs/oT4vpg2MqySAVe6Xm4oz8XlzN4AnK0XMiQcyWfW6ihMLlVFBlgHuASRcUiIdnts23vHsWGACuECpI0sFokJHRmXsUjnWZ41Ff2WP+k3NfMH8/DJlfOs32dbclvQXk3zgLq1Q9pKLmXnjY4VGuVkOYCHJdrPEAKUOuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3Oz2F7k"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEBwE1eX5ppGKYs/oT4vpg2MqySAVe6Xm4oz8XlzN4AnK0XMiQcyWfW6ihMLlVFBlgHuASRcUiIdnts23vHsWGACuECpI0sFokJHRmXsUjnWZ41Ff2WP+k3NfMH8/DJlfOs32dbclvQXk3zgLq1Q9pKLmXnjY4VGuVkOYCHJdrPEAKUOuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgWgCJA0CEsOhe6MIL49dGdwzAHO9VCnAx0iSQUtxzKfx3Oz2F7k"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2BqCorP0XGr2ciKksOWED8YlfkYS9HacAuEW5Qy2wC97GVLwAX9g=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423066,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECZCv6hVGmmaHxB96jcYPb+4t1y/B0BQVrIa2tLnp6dJVG+rEOIbndjPTDCf0d0J9cPFiaRivuFcjZ/E9bdx8wHuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlTUd8TT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423066,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+JALAfhCuECZCv6hVGmmaHxB96jcYPb+4t1y/B0BQVrIa2tLnp6dJVG+rEOIbndjPTDCf0d0J9cPFiaRivuFcjZ/E9bdx8wHuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlTUd8TT",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423065,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEARb0DRS9UlLvVHZBY4E7+By6UII87XH2drSJu6fU72NeRzPbaHWT7j5AO4iKnC+3A6ZWcLbmoFMg0KYKVkt9sKuECZCv6hVGmmaHxB96jcYPb+4t1y/B0BQVrIa2tLnp6dJVG+rEOIbndjPTDCf0d0J9cPFiaRivuFcjZ/E9bdx8wHuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlRN2ASl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423065,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEARb0DRS9UlLvVHZBY4E7+By6UII87XH2drSJu6fU72NeRzPbaHWT7j5AO4iKnC+3A6ZWcLbmoFMg0KYKVkt9sKuECZCv6hVGmmaHxB96jcYPb+4t1y/B0BQVrIa2tLnp6dJVG+rEOIbndjPTDCf0d0J9cPFiaRivuFcjZ/E9bdx8wHuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlRN2ASl"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEARb0DRS9UlLvVHZBY4E7+By6UII87XH2drSJu6fU72NeRzPbaHWT7j5AO4iKnC+3A6ZWcLbmoFMg0KYKVkt9sKuECZCv6hVGmmaHxB96jcYPb+4t1y/B0BQVrIa2tLnp6dJVG+rEOIbndjPTDCf0d0J9cPFiaRivuFcjZ/E9bdx8wHuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgagqKz9Fxq9nIipLDlhA/GJX5GEvR2nALhFuUMtsAvexlRN2ASl"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 5,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 5,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 6,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 6,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 3,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "caller_nonce": 3,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2B6BDrzxhf3PQBW5DBzBVDzZpdEXWQahfr195nGdVCBrefQg5hZI=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423064,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBcrmSck6LhwFPesVK8iXlYxo1/BZavyeD/F+d2hrUlAginBO0IY15I/0tvdk7z7uqP/iivpZcN4cVd/V+ix+IEuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n18cWwa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423064,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBcrmSck6LhwFPesVK8iXlYxo1/BZavyeD/F+d2hrUlAginBO0IY15I/0tvdk7z7uqP/iivpZcN4cVd/V+ix+IEuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n18cWwa",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423063,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBWNn0BeiDx0MJiD8dDtTNyuOZdcRHYXXYFNLIEMi7d+M4QKJSsiQpM5WuQkNZVSIxbrj8SqVG4tjSny5V6oxIBuEBcrmSck6LhwFPesVK8iXlYxo1/BZavyeD/F+d2hrUlAginBO0IY15I/0tvdk7z7uqP/iivpZcN4cVd/V+ix+IEuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n0SKBw6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423063,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEBWNn0BeiDx0MJiD8dDtTNyuOZdcRHYXXYFNLIEMi7d+M4QKJSsiQpM5WuQkNZVSIxbrj8SqVG4tjSny5V6oxIBuEBcrmSck6LhwFPesVK8iXlYxo1/BZavyeD/F+d2hrUlAginBO0IY15I/0tvdk7z7uqP/iivpZcN4cVd/V+ix+IEuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n0SKBw6"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEBWNn0BeiDx0MJiD8dDtTNyuOZdcRHYXXYFNLIEMi7d+M4QKJSsiQpM5WuQkNZVSIxbrj8SqVG4tjSny5V6oxIBuEBcrmSck6LhwFPesVK8iXlYxo1/BZavyeD/F+d2hrUlAginBO0IY15I/0tvdk7z7uqP/iivpZcN4cVd/V+ix+IEuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgegQ688YX9z0AVuQwcwVQ82aXRF1kGoX69feZxnVQga3n0SKBw6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 8,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 7,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 7,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2CKBeN8SRXeZrW6awTv1d98AmPBx1GrjbEg8v45BpJOoTy6Ar0gI=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423062,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA10qsZUgkkDyTfdxFdxriB0WEC0Vw6RPlaym6v7sbpNje0xzzVwajxnNdNjWYbQD8FJXveB6Wjq0xXFwOAcrgLuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8ujwpSG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423062,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA10qsZUgkkDyTfdxFdxriB0WEC0Vw6RPlaym6v7sbpNje0xzzVwajxnNdNjWYbQD8FJXveB6Wjq0xXFwOAcrgLuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8ujwpSG",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423061,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA10qsZUgkkDyTfdxFdxriB0WEC0Vw6RPlaym6v7sbpNje0xzzVwajxnNdNjWYbQD8FJXveB6Wjq0xXFwOAcrgLuEBjLpbK8823Xpwe4C6RM8CAo0XBoHn3dktW7W47ziqtxMNiaHlSIxsu/h1msa3DOPTboDM4aHb1AqZo1WQAitgJuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8uZsk+S"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423061,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEA10qsZUgkkDyTfdxFdxriB0WEC0Vw6RPlaym6v7sbpNje0xzzVwajxnNdNjWYbQD8FJXveB6Wjq0xXFwOAcrgLuEBjLpbK8823Xpwe4C6RM8CAo0XBoHn3dktW7W47ziqtxMNiaHlSIxsu/h1msa3DOPTboDM4aHb1AqZo1WQAitgJuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8uZsk+S"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEA10qsZUgkkDyTfdxFdxriB0WEC0Vw6RPlaym6v7sbpNje0xzzVwajxnNdNjWYbQD8FJXveB6Wjq0xXFwOAcrgLuEBjLpbK8823Xpwe4C6RM8CAo0XBoHn3dktW7W47ziqtxMNiaHlSIxsu/h1msa3DOPTboDM4aHb1AqZo1WQAitgJuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgigXjfEkV3ma1umsE79XffAJjwcdRq42xIPL+OQaSTqE8uZsk+S"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2CaCJPRoEoUA9eJQfV7KhvjA4FYszagJTS++DGJSwbVvZU0ZWf2g=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423060,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAXQWAcyqy/KjnyCNN/7AR00D0x3K1/hgHA0gylFPCHE92hhzFZjgoDIHKFEvDNcOCZxagM6ugKUVhkBMbKyQMNuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VMefTFK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423060,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAXQWAcyqy/KjnyCNN/7AR00D0x3K1/hgHA0gylFPCHE92hhzFZjgoDIHKFEvDNcOCZxagM6ugKUVhkBMbKyQMNuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VMefTFK",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423059,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAXQWAcyqy/KjnyCNN/7AR00D0x3K1/hgHA0gylFPCHE92hhzFZjgoDIHKFEvDNcOCZxagM6ugKUVhkBMbKyQMNuEClapfmuL1lp7ZWp+5X0xqk/WVGiCcSsXDXGKZgLmu7EhizS5oeBdDgtVVACpRx8uebX26HolXuJFE5GTKZPgACuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VNj64aI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423059,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEAXQWAcyqy/KjnyCNN/7AR00D0x3K1/hgHA0gylFPCHE92hhzFZjgoDIHKFEvDNcOCZxagM6ugKUVhkBMbKyQMNuEClapfmuL1lp7ZWp+5X0xqk/WVGiCcSsXDXGKZgLmu7EhizS5oeBdDgtVVACpRx8uebX26HolXuJFE5GTKZPgACuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VNj64aI"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEAXQWAcyqy/KjnyCNN/7AR00D0x3K1/hgHA0gylFPCHE92hhzFZjgoDIHKFEvDNcOCZxagM6ugKUVhkBMbKyQMNuEClapfmuL1lp7ZWp+5X0xqk/WVGiCcSsXDXGKZgLmu7EhizS5oeBdDgtVVACpRx8uebX26HolXuJFE5GTKZPgACuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgmgiT0aBKFAPXiUH1eyob4wOBWLM2oCU0vvgxiUsG1b2VNj64aI"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2CqCbpTUGPjYK8W9Hbq08zfsMGe3sdz1U8ypN57sF/+l8Jrd8Qxw=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423058,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAxM/7AXb2CMyd9xojcfNFeM2loWJiy5uGzidN70Ouawz6xGkhHPqY9w6AxRrRpAlhLPO4MvmIxXENyBETgoB4EuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCZwlZP5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423058,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAxM/7AXb2CMyd9xojcfNFeM2loWJiy5uGzidN70Ouawz6xGkhHPqY9w6AxRrRpAlhLPO4MvmIxXENyBETgoB4EuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCZwlZP5",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303423057,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAxM/7AXb2CMyd9xojcfNFeM2loWJiy5uGzidN70Ouawz6xGkhHPqY9w6AxRrRpAlhLPO4MvmIxXENyBETgoB4EuECfKMlB/s+nycoEWEEijzI24RSnkf0/ALUiQzaET9cGVi4KkH65auZjXlJ6k5JiteELY6qAQGhhgfTOVJ+Iz5sBuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCbMYxc+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423057,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEAxM/7AXb2CMyd9xojcfNFeM2loWJiy5uGzidN70Ouawz6xGkhHPqY9w6AxRrRpAlhLPO4MvmIxXENyBETgoB4EuECfKMlB/s+nycoEWEEijzI24RSnkf0/ALUiQzaET9cGVi4KkH65auZjXlJ6k5JiteELY6qAQGhhgfTOVJ+Iz5sBuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCbMYxc+"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "state": "tx_+NILAfiEuEAxM/7AXb2CMyd9xojcfNFeM2loWJiy5uGzidN70Ouawz6xGkhHPqY9w6AxRrRpAlhLPO4MvmIxXENyBETgoB4EuECfKMlB/s+nycoEWEEijzI24RSnkf0/ALUiQzaET9cGVi4KkH65auZjXlJ6k5JiteELY6qAQGhhgfTOVJ+Iz5sBuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCbMYxc+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 9,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 9,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 10,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "caller_id": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "caller_nonce": 10,
      "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ],
    "contracts": [
      "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+Mdj4gioEYHV7uWYqzLlPuu/XRDajGbC3I7HdTE1RX5AYP4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4SaB6t8a6kE6M48iOxU7hBaDUl+z5WHzF6JLatsvxgJMDGuegNPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OFxAoBAAr4lKCT4x2PiCKgRgdXu5ZirMuU+679dENqMZsLcjsd1MTVFfhxgKB6t8a6kE6M48iOxU7hBaDUl+z5WHzF6JLatsvxgJMDGoCAgKDRdKEaoffGcn4cP7JvVpPoukzl9YawGvMdYjrlH/qgooCAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgID4T6DRdKEaoffGcn4cP7JvVpPoukzl9YawGvMdYjrlH/qgou2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/fj4qA19Bz7NeyhIKCs38MFwBVsz68BMko84tymGS666tIKqMDA+Qap+QamoDnTnL+cEufMb+bOniQkxAOQGj/Sv1lbgTl4puy9GwBt+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+GagOdOcv5wS58xv5s6eJCTEA5AaP9K/WVuBOXim7L0bAG34Q6EAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OgcqwZ+7hASIIrq9ppKxV/3vuJGfYXgwZLsEpkkIIAe8/4dKBIER5XC7xxbur+BQq0j0FPtJBdjUer3LAh9f2Bgo7xRfhRoBVqI09vFvWdE58TQLrptCdtmByUCsuEkhUhLVLTF8FfoMMN5omVEejhhfhAqs9cOijYD5ArIrSxrLGPPIGxA0Z3gICAgICAgICAgICAgICA+QO2oHKsGfu4QEiCK6vaaSsVf977iRn2F4MGS7BKZJCCAHvP+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAkNix/w=="
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
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ],
    "contracts": [
      "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+Mdj4gioEYHV7uWYqzLlPuu/XRDajGbC3I7HdTE1RX5AYP4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4SaB6t8a6kE6M48iOxU7hBaDUl+z5WHzF6JLatsvxgJMDGuegNPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OFxAoBAAr4lKCT4x2PiCKgRgdXu5ZirMuU+679dENqMZsLcjsd1MTVFfhxgKB6t8a6kE6M48iOxU7hBaDUl+z5WHzF6JLatsvxgJMDGoCAgKDRdKEaoffGcn4cP7JvVpPoukzl9YawGvMdYjrlH/qgooCAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgID4T6DRdKEaoffGcn4cP7JvVpPoukzl9YawGvMdYjrlH/qgou2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/fj4qA19Bz7NeyhIKCs38MFwBVsz68BMko84tymGS666tIKqMDA+Qap+QamoDnTnL+cEufMb+bOniQkxAOQGj/Sv1lbgTl4puy9GwBt+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+GagOdOcv5wS58xv5s6eJCTEA5AaP9K/WVuBOXim7L0bAG34Q6EAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OgcqwZ+7hASIIrq9ppKxV/3vuJGfYXgwZLsEpkkIIAe8/4dKBIER5XC7xxbur+BQq0j0FPtJBdjUer3LAh9f2Bgo7xRfhRoBVqI09vFvWdE58TQLrptCdtmByUCsuEkhUhLVLTF8FfoMMN5omVEejhhfhAqs9cOijYD5ArIrSxrLGPPIGxA0Z3gICAgICAgICAgICAgICA+QO2oHKsGfu4QEiCK6vaaSsVf977iRn2F4MGS7BKZJCCAHvP+QOSgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQNf+QNcKAGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAr45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAkNix/w=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303423056,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423056,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QeoggJuAbkHofkHnj8B+QeZuLn4t0ABuEAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw/ufvjimPkppe+Dgl5/lWBWFz3108sOOJ8t1z1VIDJFXuHH4bykCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gcHoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYAwLi5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8PXK/Iyce6OqTzXHY9BdvEkp7Uvc7nFnXriL6WIazA6WLhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAFBaEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAMC4ufi3QAG4QBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDyxgOKMOWaeM3vPsmcctm3cm7pIYPkmbyPCRA1RtRWkS4cfhvKQKhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwAwOhBRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDAYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFQDAuLn4t0ABuEAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw5zeXYvCmX+dH/5SvLqrB8Lv8Zp18i+/pmUuKzqp2+0uuHH4bykCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1goKoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Nv/umPuzYoFvZ2NkRSvjGllt27gqJftiuxie47j23M3Lhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YJCaEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMC4ufi3QAG4QBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDWV8rInHJz1MXFFPDS0wf0pNxm8PVX2MeoexYs+tPwo+4cfhvKQKhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WCAihBRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDAYIBzqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAuLn4t0ABuEAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw0vUs/yNgnhRCopO30t+ZcRIYdc2l34GMNaHDSoJZu2kuHH4bykCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AQEoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwGCAc6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwLi5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MUf0v0q9Y5fIV5MPZEd/a4Pjgkv7k240em2pF3lNEiCrhx+G8pAqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvAGBqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAMC5Ab75AbtAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MCcJD+dT8/fZHPCpoRUInIuHshRxuIoI5MO8Vv4cIzXrkBdPkBcSkCoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AICoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwCCAT+5ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABUAwFu5zA0=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAxM/7AXb2CMyd9xojcfNFeM2loWJiy5uGzidN70Ouawz6xGkhHPqY9w6AxRrRpAlhLPO4MvmIxXENyBETgoB4EuECfKMlB/s+nycoEWEEijzI24RSnkf0/ALUiQzaET9cGVi4KkH65auZjXlJ6k5JiteELY6qAQGhhgfTOVJ+Iz5sBuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCbMYxc+",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABohT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC5A4j5A4VAAaAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw7kDX/kDXCgBoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Oc3l2Lwpl/nR/+Ury6qwfC7/GadfIvv6ZlLis6qdvtLrhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YKCqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/eq6UABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDhcQKAQAKYD7MFg=="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423055,
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
    "gas_price": 1000001315
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423055,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "signed_tx": "tx_+Qi7CwHAuQi1+QiyggIJAaEGEj1nJ26rub7fuhfzbMsMQ3g12M6CdQIG+2NA8NF057ahAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwuNT40gsB+IS4QDEz/sBdvYIzJ33GiNx80V4zaWhYmLLm4bOJ03vQ65rDPrEaSEc+pj3DoDFGtGkCWEs87gy+YjFcQ3IEROCgHgS4QJ8oyUH+z6fJygRYQSKPMjbhFKeR/T8AtSJDNoRP1wZWLgqQfrlq5mNeUnqTkmK14QtjqoBAaGGB9M5Un4jPmwG4SPhGOQKhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2CqCbpTUGPjYK8W9Hbq08zfsMGe3sdz1U8ypN57sF/+l8Jgu4uPi2ggI+AaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvChBRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDAQqDD0JAhDuazyO4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgc2uRKxROcQf6tjkuEW2gCavj30+KXjuvSmRQGsVZovy5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaIU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwxABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQALkDiPkDhUABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDuQNf+QNcKAGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuEAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw5zeXYvCmX+dH/5SvLqrB8Lv8Zp18i+/pmUuKzqp2+0uuHH4bykCoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1goKoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2w70ABoLHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Wi8oKAQCGP6olIl//sO9AAaBQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcp/96rpQAGgFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8OFxAoBAAoAhwHB0Yf6blwK42GMpQ==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "contract_id": "ct_AESYcHoPtdMqqp35Fsp4vU1UDTVooSzan6b1JYeqNNAd4vo4D",
          "gas": 1000000,
          "gas_price": 1000001315,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+Qj+CwH4QrhAevTiACYYcjrmzIXJznfWbaDnEJaJwD7fEL5gYJ38Wn3yY9Bs+0D2I2JV1OrTx4s21LPa4goKCBEbxA9XHEB2ALkItfkIsoICCQGhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEAxM/7AXb2CMyd9xojcfNFeM2loWJiy5uGzidN70Ouawz6xGkhHPqY9w6AxRrRpAlhLPO4MvmIxXENyBETgoB4EuECfKMlB/s+nycoEWEEijzI24RSnkf0/ALUiQzaET9cGVi4KkH65auZjXlJ6k5JiteELY6qAQGhhgfTOVJ+Iz5sBuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCYLuLj4toICPgGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwEKgw9CQIQ7ms8juGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoHNrkSsUTnEH+rY5LhFtoAmr499Pil47r0pkUBrFWaL8uQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABohT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC5A4j5A4VAAaAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw7kDX/kDXCgBoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Oc3l2Lwpl/nR/+Ury6qwfC7/GadfIvv6ZlLis6qdvtLrhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YKCqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/eq6UABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDhcQKAQAKAIcBwdGH+m5cCpmWndQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAevTiACYYcjrmzIXJznfWbaDnEJaJwD7fEL5gYJ38Wn3yY9Bs+0D2I2JV1OrTx4s21LPa4goKCBEbxA9XHEB2ALkItfkIsoICCQGhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEAxM/7AXb2CMyd9xojcfNFeM2loWJiy5uGzidN70Ouawz6xGkhHPqY9w6AxRrRpAlhLPO4MvmIxXENyBETgoB4EuECfKMlB/s+nycoEWEEijzI24RSnkf0/ALUiQzaET9cGVi4KkH65auZjXlJ6k5JiteELY6qAQGhhgfTOVJ+Iz5sBuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCYLuLj4toICPgGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwEKgw9CQIQ7ms8juGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoHNrkSsUTnEH+rY5LhFtoAmr499Pil47r0pkUBrFWaL8uQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABohT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC5A4j5A4VAAaAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw7kDX/kDXCgBoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Oc3l2Lwpl/nR/+Ury6qwfC7/GadfIvv6ZlLis6qdvtLrhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YKCqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/eq6UABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDhcQKAQAKAIcBwdGH+m5cCpmWndQ=",
      "type": "channel_force_progress_tx"
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+Qj+CwH4QrhAevTiACYYcjrmzIXJznfWbaDnEJaJwD7fEL5gYJ38Wn3yY9Bs+0D2I2JV1OrTx4s21LPa4goKCBEbxA9XHEB2ALkItfkIsoICCQGhBhI9Zyduq7m+37oX82zLDEN4NdjOgnUCBvtjQPDRdOe2oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEAxM/7AXb2CMyd9xojcfNFeM2loWJiy5uGzidN70Ouawz6xGkhHPqY9w6AxRrRpAlhLPO4MvmIxXENyBETgoB4EuECfKMlB/s+nycoEWEEijzI24RSnkf0/ALUiQzaET9cGVi4KkH65auZjXlJ6k5JiteELY6qAQGhhgfTOVJ+Iz5sBuEj4RjkCoQYSPWcnbqu5vt+6F/NsywxDeDXYzoJ1Agb7Y0Dw0XTntgqgm6U1Bj42CvFvR26tPM37DBnt7Hc9VPMqTee7Bf/pfCYLuLj4toICPgGhAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwoQUU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLwwEKgw9CQIQ7ms8juGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAoHNrkSsUTnEH+rY5LhFtoAmr499Pil47r0pkUBrFWaL8uQar+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGiFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABohT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoRT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDEAC5A4j5A4VAAaAU9jbxSQ57VBu9ooUz5GYnMsbGwmfngOJf5eVfAjxLw7kDX/kDXCgBoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8Oc3l2Lwpl/nR/+Ury6qwfC7/GadfIvv6ZlLis6qdvtLrhx+G8pAqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YKCqEFFPY28UkOe1QbvaKFM+RmJzLGxsJn54DiX+XlXwI8S8MBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNsO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKf/eq6UABoBT2NvFJDntUG72ihTPkZicyxsbCZ+eA4l/l5V8CPEvDhcQKAQAKAIcBwdGH+m5cCpmWndQ=",
      "type": "channel_force_progress_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423054,
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
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423054,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423053,
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
    "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
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
  "channel_id": "ch_92uw4WYzJdhwnjnfoeuXLaQeXetei7Xkkjmjnomr5dxnM5vjE",
  "id": -576460752303423053,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
