
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
      "fsm_id": "ba_aR5aEQKob3TGNzk+oCW764SGwFZFCrrMNEPOkrISk73glFXR"
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
      "fsm_id": "ba_TVbQZLuZ+Xxd7zJBPSJhJ/oUSLJgov48W96uzu28he4wymnL"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsIRiJsCw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423341,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDeJxMFIKSOSv1rgRR8BJQjIHneiX/mOu9CB/UPSK4Fo5As1//Cx55oK3v58bNCuu1h/Hb3Aj98HPGuFJH2iq0LuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LCLnHkSY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423341,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "fsm_id": "ba_TVbQZLuZ+Xxd7zJBPSJhJ/oUSLJgov48W96uzu28he4wymnL",
      "signed_tx": "tx_+MsLAfhCuEDeJxMFIKSOSv1rgRR8BJQjIHneiX/mOu9CB/UPSK4Fo5As1//Cx55oK3v58bNCuu1h/Hb3Aj98HPGuFJH2iq0LuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LCLnHkSY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423340,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAPGqMYm1xSi2JAzFD3tOrisAD82t1jEAQUi86yVWn9RHDUMS3XUiN2+CQ890dYAyekRe+mz7s/5IaLtO54EQqD7hA3icTBSCkjkr9a4EUfASUIyB53ol/5jrvQgf1D0iuBaOQLNf/wseeaCt7+fGzQrrtYfx29wI/fBzxrhSR9oqtC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwhGOtz7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423340,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAPGqMYm1xSi2JAzFD3tOrisAD82t1jEAQUi86yVWn9RHDUMS3XUiN2+CQ890dYAyekRe+mz7s/5IaLtO54EQqD7hA3icTBSCkjkr9a4EUfASUIyB53ol/5jrvQgf1D0iuBaOQLNf/wseeaCt7+fGzQrrtYfx29wI/fBzxrhSR9oqtC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwhGOtz7",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_aR5aEQKob3TGNzk+oCW764SGwFZFCrrMNEPOkrISk73glFXR"
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAPGqMYm1xSi2JAzFD3tOrisAD82t1jEAQUi86yVWn9RHDUMS3XUiN2+CQ890dYAyekRe+mz7s/5IaLtO54EQqD7hA3icTBSCkjkr9a4EUfASUIyB53ol/5jrvQgf1D0iuBaOQLNf/wseeaCt7+fGzQrrtYfx29wI/fBzxrhSR9oqtC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwhGOtz7",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPGqMYm1xSi2JAzFD3tOrisAD82t1jEAQUi86yVWn9RHDUMS3XUiN2+CQ890dYAyekRe+mz7s/5IaLtO54EQqD7hA3icTBSCkjkr9a4EUfASUIyB53ol/5jrvQgf1D0iuBaOQLNf/wseeaCt7+fGzQrrtYfx29wI/fBzxrhSR9oqtC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwhGOtz7",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPGqMYm1xSi2JAzFD3tOrisAD82t1jEAQUi86yVWn9RHDUMS3XUiN2+CQ890dYAyekRe+mz7s/5IaLtO54EQqD7hA3icTBSCkjkr9a4EUfASUIyB53ol/5jrvQgf1D0iuBaOQLNf/wseeaCt7+fGzQrrtYfx29wI/fBzxrhSR9oqtC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwhGOtz7",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "message": {
        "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "message": {
        "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
  "id": -576460752303423339,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423339,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+QENCwH4hLhAPGqMYm1xSi2JAzFD3tOrisAD82t1jEAQUi86yVWn9RHDUMS3XUiN2+CQ890dYAyekRe+mz7s/5IaLtO54EQqD7hA3icTBSCkjkr9a4EUfASUIyB53ol/5jrvQgf1D0iuBaOQLNf/wseeaCt7+fGzQrrtYfx29wI/fBzxrhSR9oqtC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwhGOtz7"
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+QENCwH4hLhAPGqMYm1xSi2JAzFD3tOrisAD82t1jEAQUi86yVWn9RHDUMS3XUiN2+CQ890dYAyekRe+mz7s/5IaLtO54EQqD7hA3icTBSCkjkr9a4EUfASUIyB53ol/5jrvQgf1D0iuBaOQLNf/wseeaCt7+fGzQrrtYfx29wI/fBzxrhSR9oqtC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwhGOtz7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423338,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423338,
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
    "amount": "1",
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": [
      "meta 1"
    ],
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": [
          "meta 1"
        ],
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "meta": [
      "meta 1"
    ],
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "meta": [
          "meta 1"
        ],
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": [
          "meta 1"
        ],
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": 17,
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": 17,
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+NhyNtNuf6bblBOGtZXPKqa+1errX9OlINJI013cM1AqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAoeT3tQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423337,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC9kIJPkEdgsrF2PaCmkP5b8uRj04lnZSRDcTo2tKJVNCcdi/NmKBYsMDh8tjHjB7JPEjHV/ft8EjRvfP18W7EMuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJGoO0J"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423337,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC9kIJPkEdgsrF2PaCmkP5b8uRj04lnZSRDcTo2tKJVNCcdi/NmKBYsMDh8tjHjB7JPEjHV/ft8EjRvfP18W7EMuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJGoO0J",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423336,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC61Xz6nXjZLY+wLVWYOIyI2di44ot/xgPaNwrPVvFrgxDtMrcujLtwadfTwGXFwhi+7ig2IRON1AvlVSrT51ECuEC9kIJPkEdgsrF2PaCmkP5b8uRj04lnZSRDcTo2tKJVNCcdi/NmKBYsMDh8tjHjB7JPEjHV/ft8EjRvfP18W7EMuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLZAy0m"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423336,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEC61Xz6nXjZLY+wLVWYOIyI2di44ot/xgPaNwrPVvFrgxDtMrcujLtwadfTwGXFwhi+7ig2IRON1AvlVSrT51ECuEC9kIJPkEdgsrF2PaCmkP5b8uRj04lnZSRDcTo2tKJVNCcdi/NmKBYsMDh8tjHjB7JPEjHV/ft8EjRvfP18W7EMuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLZAy0m"
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEC61Xz6nXjZLY+wLVWYOIyI2di44ot/xgPaNwrPVvFrgxDtMrcujLtwadfTwGXFwhi+7ig2IRON1AvlVSrT51ECuEC9kIJPkEdgsrF2PaCmkP5b8uRj04lnZSRDcTo2tKJVNCcdi/NmKBYsMDh8tjHjB7JPEjHV/ft8EjRvfP18W7EMuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLZAy0m"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423335,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423335,
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
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC61Xz6nXjZLY+wLVWYOIyI2di44ot/xgPaNwrPVvFrgxDtMrcujLtwadfTwGXFwhi+7ig2IRON1AvlVSrT51ECuEC9kIJPkEdgsrF2PaCmkP5b8uRj04lnZSRDcTo2tKJVNCcdi/NmKBYsMDh8tjHjB7JPEjHV/ft8EjRvfP18W7EMuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLZAy0m",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423333,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423333,
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
    "amount": "1",
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": [
          "meta 1"
        ],
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "meta": [
          "meta 1"
        ],
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": [
          "meta 1"
        ],
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+NhyNtNuf6bblBOGtZXPKqa+1errX9OlINJI013cM1A6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC/F61S0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423332,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBSiZKj2E0vEqXbRbIF/vlYDSUA/wmebXqK5rDRhrHupfBVV5aNJidfPdD4RqlxCFZ9c5mALrVYlGbkIeV+xq0NuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt4xjK4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423332,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBSiZKj2E0vEqXbRbIF/vlYDSUA/wmebXqK5rDRhrHupfBVV5aNJidfPdD4RqlxCFZ9c5mALrVYlGbkIeV+xq0NuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt4xjK4",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423331,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBSiZKj2E0vEqXbRbIF/vlYDSUA/wmebXqK5rDRhrHupfBVV5aNJidfPdD4RqlxCFZ9c5mALrVYlGbkIeV+xq0NuECc9HwA822HpTDoBYzYesF7DIok86C4C2syFf416aKkjDikXK+A6DHe9wFwhXxhBwJ1vb6C1WwcW9fHH/3gR24HuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv2SED1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423331,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEBSiZKj2E0vEqXbRbIF/vlYDSUA/wmebXqK5rDRhrHupfBVV5aNJidfPdD4RqlxCFZ9c5mALrVYlGbkIeV+xq0NuECc9HwA822HpTDoBYzYesF7DIok86C4C2syFf416aKkjDikXK+A6DHe9wFwhXxhBwJ1vb6C1WwcW9fHH/3gR24HuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv2SED1"
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEBSiZKj2E0vEqXbRbIF/vlYDSUA/wmebXqK5rDRhrHupfBVV5aNJidfPdD4RqlxCFZ9c5mALrVYlGbkIeV+xq0NuECc9HwA822HpTDoBYzYesF7DIok86C4C2syFf416aKkjDikXK+A6DHe9wFwhXxhBwJ1vb6C1WwcW9fHH/3gR24HuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv2SED1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423330,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423330,
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
  "id": -576460752303423329,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423329,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBSiZKj2E0vEqXbRbIF/vlYDSUA/wmebXqK5rDRhrHupfBVV5aNJidfPdD4RqlxCFZ9c5mALrVYlGbkIeV+xq0NuECc9HwA822HpTDoBYzYesF7DIok86C4C2syFf416aKkjDikXK+A6DHe9wFwhXxhBwJ1vb6C1WwcW9fHH/3gR24HuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv2SED1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423328,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423328,
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": [
          "meta 1"
        ],
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "meta": [
          "meta 1"
        ],
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": [
          "meta 1"
        ],
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+NhyNtNuf6bblBOGtZXPKqa+1errX9OlINJI013cM1BKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMctAI58=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423327,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAmTahs1bIffZvUYvdik7qIXGDEKCNavI/nRwr0isjQZuvbTcnqUzwOfTq3GwO6VcoOz9Vtd0Brbm2gNHZD8uABuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEoCdkP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423327,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAmTahs1bIffZvUYvdik7qIXGDEKCNavI/nRwr0isjQZuvbTcnqUzwOfTq3GwO6VcoOz9Vtd0Brbm2gNHZD8uABuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEoCdkP",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423326,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAmTahs1bIffZvUYvdik7qIXGDEKCNavI/nRwr0isjQZuvbTcnqUzwOfTq3GwO6VcoOz9Vtd0Brbm2gNHZD8uABuEDSdLbU3AZOn6HT1SRSRYuZM7jf0+d1JvA2M08eVGAS9C6QBgAA7C6bIBFID9y+DcsCeyaSrt+P+23s57XlTJsKuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHeJ39B"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423326,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEAmTahs1bIffZvUYvdik7qIXGDEKCNavI/nRwr0isjQZuvbTcnqUzwOfTq3GwO6VcoOz9Vtd0Brbm2gNHZD8uABuEDSdLbU3AZOn6HT1SRSRYuZM7jf0+d1JvA2M08eVGAS9C6QBgAA7C6bIBFID9y+DcsCeyaSrt+P+23s57XlTJsKuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHeJ39B"
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEAmTahs1bIffZvUYvdik7qIXGDEKCNavI/nRwr0isjQZuvbTcnqUzwOfTq3GwO6VcoOz9Vtd0Brbm2gNHZD8uABuEDSdLbU3AZOn6HT1SRSRYuZM7jf0+d1JvA2M08eVGAS9C6QBgAA7C6bIBFID9y+DcsCeyaSrt+P+23s57XlTJsKuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHeJ39B"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423325,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423325,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423324,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423324,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAmTahs1bIffZvUYvdik7qIXGDEKCNavI/nRwr0isjQZuvbTcnqUzwOfTq3GwO6VcoOz9Vtd0Brbm2gNHZD8uABuEDSdLbU3AZOn6HT1SRSRYuZM7jf0+d1JvA2M08eVGAS9C6QBgAA7C6bIBFID9y+DcsCeyaSrt+P+23s57XlTJsKuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHeJ39B",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423323,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423323,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
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
    "amount": "1",
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": [
      "meta 1"
    ],
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": [
          "meta 1"
        ],
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "meta": [
      "meta 1"
    ],
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "meta": [
          "meta 1"
        ],
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": [
          "meta 1"
        ],
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": 17,
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": 17,
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+NhyNtNuf6bblBOGtZXPKqa+1errX9OlINJI013cM1BaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwhByDE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423322,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBhBKQmbLZuD1ZlYVmtVIqZalH6K8wF3assm5VrVI36tlx6rVUsHX49l1NGjWDh2KZsQgAiXyIRLGoY5n/EQjsPuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgucA2dd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423322,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBhBKQmbLZuD1ZlYVmtVIqZalH6K8wF3assm5VrVI36tlx6rVUsHX49l1NGjWDh2KZsQgAiXyIRLGoY5n/EQjsPuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgucA2dd",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423321,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBhBKQmbLZuD1ZlYVmtVIqZalH6K8wF3assm5VrVI36tlx6rVUsHX49l1NGjWDh2KZsQgAiXyIRLGoY5n/EQjsPuECO/l5R1dTNJ26Y+vr+8h9nR5HFEhgauWLAOS4kYibODK1PS18w0qbfkE7l0uMVCTWfZT7mwiANKdT26mSy9AIJuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsV7k5Y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423321,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEBhBKQmbLZuD1ZlYVmtVIqZalH6K8wF3assm5VrVI36tlx6rVUsHX49l1NGjWDh2KZsQgAiXyIRLGoY5n/EQjsPuECO/l5R1dTNJ26Y+vr+8h9nR5HFEhgauWLAOS4kYibODK1PS18w0qbfkE7l0uMVCTWfZT7mwiANKdT26mSy9AIJuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsV7k5Y"
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEBhBKQmbLZuD1ZlYVmtVIqZalH6K8wF3assm5VrVI36tlx6rVUsHX49l1NGjWDh2KZsQgAiXyIRLGoY5n/EQjsPuECO/l5R1dTNJ26Y+vr+8h9nR5HFEhgauWLAOS4kYibODK1PS18w0qbfkE7l0uMVCTWfZT7mwiANKdT26mSy9AIJuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsV7k5Y"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423320,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423320,
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
  "id": -576460752303423319,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423319,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBhBKQmbLZuD1ZlYVmtVIqZalH6K8wF3assm5VrVI36tlx6rVUsHX49l1NGjWDh2KZsQgAiXyIRLGoY5n/EQjsPuECO/l5R1dTNJ26Y+vr+8h9nR5HFEhgauWLAOS4kYibODK1PS18w0qbfkE7l0uMVCTWfZT7mwiANKdT26mSy9AIJuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsV7k5Y",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423318,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423318,
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": [
          "meta 1"
        ],
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "meta": [
          "meta 1"
        ],
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": [
          "meta 1"
        ],
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+NhyNtNuf6bblBOGtZXPKqa+1errX9OlINJI013cM1BqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMUxTj50=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423317,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEApgDrkyXxeG6K4A03gac0JqQ4cMd6Gqt6gNJoLbomwXi9+rWc60G8PAt51CPeiGozpEfOGeppbkphoaOOu8/4KuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKlv6Y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423317,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "signed_tx": "tx_+JALAfhCuEApgDrkyXxeG6K4A03gac0JqQ4cMd6Gqt6gNJoLbomwXi9+rWc60G8PAt51CPeiGozpEfOGeppbkphoaOOu8/4KuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKlv6Y",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423316,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEApgDrkyXxeG6K4A03gac0JqQ4cMd6Gqt6gNJoLbomwXi9+rWc60G8PAt51CPeiGozpEfOGeppbkphoaOOu8/4KuEC5R/mLczp2fCOfApoFWNDOFB+qxe8sIxt+aY51iGveQ//Q35UYYZWyGoFSFawAAw42tVLzw6jcmqEATiIF7k4CuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHSVu0r"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423316,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEApgDrkyXxeG6K4A03gac0JqQ4cMd6Gqt6gNJoLbomwXi9+rWc60G8PAt51CPeiGozpEfOGeppbkphoaOOu8/4KuEC5R/mLczp2fCOfApoFWNDOFB+qxe8sIxt+aY51iGveQ//Q35UYYZWyGoFSFawAAw42tVLzw6jcmqEATiIF7k4CuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHSVu0r"
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
    "data": {
      "state": "tx_+NILAfiEuEApgDrkyXxeG6K4A03gac0JqQ4cMd6Gqt6gNJoLbomwXi9+rWc60G8PAt51CPeiGozpEfOGeppbkphoaOOu8/4KuEC5R/mLczp2fCOfApoFWNDOFB+qxe8sIxt+aY51iGveQ//Q35UYYZWyGoFSFawAAw42tVLzw6jcmqEATiIF7k4CuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHSVu0r"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423315,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423315,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423314,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423314,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEApgDrkyXxeG6K4A03gac0JqQ4cMd6Gqt6gNJoLbomwXi9+rWc60G8PAt51CPeiGozpEfOGeppbkphoaOOu8/4KuEC5R/mLczp2fCOfApoFWNDOFB+qxe8sIxt+aY51iGveQ//Q35UYYZWyGoFSFawAAw42tVLzw6jcmqEATiIF7k4CuEj4RjkCoQZvjYcjbTbn+m25QThrWVzyqmvtXq61/TpSDSSNNd3DNQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHSVu0r",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423313,
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423313,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423312,
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
    "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
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
  "channel_id": "ch_r8U8DXYWPfBD8pLtKprNGK9G6T5SNqKKaj6qoZywnXYYdnjiU",
  "id": -576460752303423312,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
