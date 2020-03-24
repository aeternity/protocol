
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish%2F3734
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
      "fsm_id": "ba_wy7AnwqJ/dVxWVvMjwJUViRLldpTWmwMv779PLyW49dThf8W"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish%2F3734
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
      "fsm_id": "ba_qyxNbjFqO7vYIog7ebkuwoe863CVdA6l7Q/HFLEn57OPISa3"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsVvIpu/Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423277,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA/loPqdUG00bGic+SAUZAcjh3zHzoRjKmUOoldb+nVciay1fQg16Ke7Nvs1smlycLxY6cR7mjgrl4cykIAP44AuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LFRccWnE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423277,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "fsm_id": "ba_qyxNbjFqO7vYIog7ebkuwoe863CVdA6l7Q/HFLEn57OPISa3",
      "signed_tx": "tx_+MsLAfhCuEA/loPqdUG00bGic+SAUZAcjh3zHzoRjKmUOoldb+nVciay1fQg16Ke7Nvs1smlycLxY6cR7mjgrl4cykIAP44AuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LFRccWnE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423276,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423276,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_wy7AnwqJ/dVxWVvMjwJUViRLldpTWmwMv779PLyW49dThf8W"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "message": {
        "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "message": {
        "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
  "id": -576460752303423275,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423275,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE&existing_fsm_id=ba_qyxNbjFqO7vYIog7ebkuwoe863CVdA6l7Q%2FHFLEn57OPISa3&offchain_tx=tx_%2BQENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW%2Fp1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD%2BOALhA5QgUO0l3PUQOPompU5kD15I4JR%2B%2BA4Ws%2FFhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5%2FEnTREjRIDC7iD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz&port=13180&protocol=json-rpc&role=responder
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
      "fsm_id": "ba_k5mj4chX7lTis1oQ7Q6lDhraa6UaORzRuleE+nr0ANmx4xYV"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE&existing_fsm_id=ba_wy7AnwqJ%2FdVxWVvMjwJUViRLldpTWmwMv779PLyW49dThf8W&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW%2Fp1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD%2BOALhA5QgUO0l3PUQOPompU5kD15I4JR%2B%2BA4Ws%2FFhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5%2FEnTREjRIDC7iD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz&port=13180&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_zlzb3pNzoO8jxn8tQXlnairkuOoB5PtqygLx874erN47y1ES"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+QENCwH4hLhAP5aD6nVBtNGxonPkgFGQHI4d8x86EYyplDqJXW/p1XImstX0INeinuzb7NbJpcnC8WOnEe5o4K5eHMpCAD+OALhA5QgUO0l3PUQOPompU5kD15I4JR++A4Ws/FhiLKZLZuhkr4N8uDWKR9lh1dfqwI1Ktv1V5jMaJ5/EnTREjRIDC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxXneXqz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423274,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423274,
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpGWnOh0uh2voeNjJIGYqyH5RTl7kyjFnmCstpHRF7M/AqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAsNK8WI=",
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
  "id": -576460752303423273,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBcRO6HpyfbvCxcyJ4UFJzBGCS2Zg5Vt3UMz/GsJd8RHjICsiblOP9kagxr+omkw3v6A8bzDRjcfab43Wzhp5cDuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJNpy3q"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423273,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBcRO6HpyfbvCxcyJ4UFJzBGCS2Zg5Vt3UMz/GsJd8RHjICsiblOP9kagxr+omkw3v6A8bzDRjcfab43Wzhp5cDuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJNpy3q",
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
  "id": -576460752303423272,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAQDJmwCpyh3vaa5Nuu2KbfScOevgn1uAQlvYhJGeewLIyVIUvn0sGp4xQv9CemfF6iebWWlbXf+xMav54Bar0GuEBcRO6HpyfbvCxcyJ4UFJzBGCS2Zg5Vt3UMz/GsJd8RHjICsiblOP9kagxr+omkw3v6A8bzDRjcfab43Wzhp5cDuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgILAiwF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423272,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEAQDJmwCpyh3vaa5Nuu2KbfScOevgn1uAQlvYhJGeewLIyVIUvn0sGp4xQv9CemfF6iebWWlbXf+xMav54Bar0GuEBcRO6HpyfbvCxcyJ4UFJzBGCS2Zg5Vt3UMz/GsJd8RHjICsiblOP9kagxr+omkw3v6A8bzDRjcfab43Wzhp5cDuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgILAiwF"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEAQDJmwCpyh3vaa5Nuu2KbfScOevgn1uAQlvYhJGeewLIyVIUvn0sGp4xQv9CemfF6iebWWlbXf+xMav54Bar0GuEBcRO6HpyfbvCxcyJ4UFJzBGCS2Zg5Vt3UMz/GsJd8RHjICsiblOP9kagxr+omkw3v6A8bzDRjcfab43Wzhp5cDuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgILAiwF"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423271,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423271,
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
  "id": -576460752303423270,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423270,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAQDJmwCpyh3vaa5Nuu2KbfScOevgn1uAQlvYhJGeewLIyVIUvn0sGp4xQv9CemfF6iebWWlbXf+xMav54Bar0GuEBcRO6HpyfbvCxcyJ4UFJzBGCS2Zg5Vt3UMz/GsJd8RHjICsiblOP9kagxr+omkw3v6A8bzDRjcfab43Wzhp5cDuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgILAiwF",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423269,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423269,
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpGWnOh0uh2voeNjJIGYqyH5RTl7kyjFnmCstpHRF7M/A6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3j3OKk=",
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
  "id": -576460752303423268,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB4w5NA4R/n76GfbfrbxMdAbWNmi8Xosm0rEMBgzRhz7B4WJUgc130/IlnScWMYSrjwPVR+4kdX1lH+GW+je4gGuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvFmQ4R"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423268,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB4w5NA4R/n76GfbfrbxMdAbWNmi8Xosm0rEMBgzRhz7B4WJUgc130/IlnScWMYSrjwPVR+4kdX1lH+GW+je4gGuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvFmQ4R",
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
  "id": -576460752303423267,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBCpr2luifXWgKEyJhIHJxDrluYixrvk5xdPaAUftO7Y1rQ6Cpoh5Y0QZXnEgGXOBV3BHZBOjwdZtO13gRx3QwAuEB4w5NA4R/n76GfbfrbxMdAbWNmi8Xosm0rEMBgzRhz7B4WJUgc130/IlnScWMYSrjwPVR+4kdX1lH+GW+je4gGuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu2EVDQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423267,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEBCpr2luifXWgKEyJhIHJxDrluYixrvk5xdPaAUftO7Y1rQ6Cpoh5Y0QZXnEgGXOBV3BHZBOjwdZtO13gRx3QwAuEB4w5NA4R/n76GfbfrbxMdAbWNmi8Xosm0rEMBgzRhz7B4WJUgc130/IlnScWMYSrjwPVR+4kdX1lH+GW+je4gGuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu2EVDQ"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEBCpr2luifXWgKEyJhIHJxDrluYixrvk5xdPaAUftO7Y1rQ6Cpoh5Y0QZXnEgGXOBV3BHZBOjwdZtO13gRx3QwAuEB4w5NA4R/n76GfbfrbxMdAbWNmi8Xosm0rEMBgzRhz7B4WJUgc130/IlnScWMYSrjwPVR+4kdX1lH+GW+je4gGuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu2EVDQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423266,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423266,
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
  "id": -576460752303423265,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423265,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBCpr2luifXWgKEyJhIHJxDrluYixrvk5xdPaAUftO7Y1rQ6Cpoh5Y0QZXnEgGXOBV3BHZBOjwdZtO13gRx3QwAuEB4w5NA4R/n76GfbfrbxMdAbWNmi8Xosm0rEMBgzRhz7B4WJUgc130/IlnScWMYSrjwPVR+4kdX1lH+GW+je4gGuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu2EVDQ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423264,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423264,
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpGWnOh0uh2voeNjJIGYqyH5RTl7kyjFnmCstpHRF7M/BKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMSugJDE=",
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
  "id": -576460752303423263,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDVTG2WfJFIcFfMoG6uZjfD/V+BlTXb2aFOR+lK+gNvGnMtSYjP28t9kFLksnh2uqStchT27/QFijsXgYEMC8sAuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHurFqr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423263,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDVTG2WfJFIcFfMoG6uZjfD/V+BlTXb2aFOR+lK+gNvGnMtSYjP28t9kFLksnh2uqStchT27/QFijsXgYEMC8sAuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHurFqr",
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
  "id": -576460752303423262,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDCcDbsA4S8557Q0Jq2XnZo39BpA1qAY2vLe7KAg4sdzT4ElzFrNCHs7FWus7eQX85vAL5YcM4yDDLB+q7cOHMDuEDVTG2WfJFIcFfMoG6uZjfD/V+BlTXb2aFOR+lK+gNvGnMtSYjP28t9kFLksnh2uqStchT27/QFijsXgYEMC8sAuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGNoD7i"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423262,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEDCcDbsA4S8557Q0Jq2XnZo39BpA1qAY2vLe7KAg4sdzT4ElzFrNCHs7FWus7eQX85vAL5YcM4yDDLB+q7cOHMDuEDVTG2WfJFIcFfMoG6uZjfD/V+BlTXb2aFOR+lK+gNvGnMtSYjP28t9kFLksnh2uqStchT27/QFijsXgYEMC8sAuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGNoD7i"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEDCcDbsA4S8557Q0Jq2XnZo39BpA1qAY2vLe7KAg4sdzT4ElzFrNCHs7FWus7eQX85vAL5YcM4yDDLB+q7cOHMDuEDVTG2WfJFIcFfMoG6uZjfD/V+BlTXb2aFOR+lK+gNvGnMtSYjP28t9kFLksnh2uqStchT27/QFijsXgYEMC8sAuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGNoD7i"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423261,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423261,
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
  "id": -576460752303423260,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423260,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDCcDbsA4S8557Q0Jq2XnZo39BpA1qAY2vLe7KAg4sdzT4ElzFrNCHs7FWus7eQX85vAL5YcM4yDDLB+q7cOHMDuEDVTG2WfJFIcFfMoG6uZjfD/V+BlTXb2aFOR+lK+gNvGnMtSYjP28t9kFLksnh2uqStchT27/QFijsXgYEMC8sAuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGNoD7i",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423259,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423259,
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpGWnOh0uh2voeNjJIGYqyH5RTl7kyjFnmCstpHRF7M/BaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0gyJfI=",
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
  "id": -576460752303423258,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB7cp/blwin0bDbT/j7jGG2pPzk2wRYmOsviYmnZvWfefA7pK6QBwIISxF24c5eGG55Q8qkKWpUsGVWKp/YLT4NuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvUosB+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423258,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB7cp/blwin0bDbT/j7jGG2pPzk2wRYmOsviYmnZvWfefA7pK6QBwIISxF24c5eGG55Q8qkKWpUsGVWKp/YLT4NuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvUosB+",
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
  "id": -576460752303423257,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB7cp/blwin0bDbT/j7jGG2pPzk2wRYmOsviYmnZvWfefA7pK6QBwIISxF24c5eGG55Q8qkKWpUsGVWKp/YLT4NuECsS62Ho0y6ZI6BNrFQt7znOQ6e3PREJKfgE5B/trdY6t+vg9Ef5a8keTLegE0rX3tuQ20cHgcdxeiRRF/ZKckCuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguYU3U5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423257,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEB7cp/blwin0bDbT/j7jGG2pPzk2wRYmOsviYmnZvWfefA7pK6QBwIISxF24c5eGG55Q8qkKWpUsGVWKp/YLT4NuECsS62Ho0y6ZI6BNrFQt7znOQ6e3PREJKfgE5B/trdY6t+vg9Ef5a8keTLegE0rX3tuQ20cHgcdxeiRRF/ZKckCuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguYU3U5"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEB7cp/blwin0bDbT/j7jGG2pPzk2wRYmOsviYmnZvWfefA7pK6QBwIISxF24c5eGG55Q8qkKWpUsGVWKp/YLT4NuECsS62Ho0y6ZI6BNrFQt7znOQ6e3PREJKfgE5B/trdY6t+vg9Ef5a8keTLegE0rX3tuQ20cHgcdxeiRRF/ZKckCuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguYU3U5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423256,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423256,
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
  "id": -576460752303423255,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423255,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB7cp/blwin0bDbT/j7jGG2pPzk2wRYmOsviYmnZvWfefA7pK6QBwIISxF24c5eGG55Q8qkKWpUsGVWKp/YLT4NuECsS62Ho0y6ZI6BNrFQt7znOQ6e3PREJKfgE5B/trdY6t+vg9Ef5a8keTLegE0rX3tuQ20cHgcdxeiRRF/ZKckCuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguYU3U5",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423254,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423254,
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpGWnOh0uh2voeNjJIGYqyH5RTl7kyjFnmCstpHRF7M/BqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMdBZkKA=",
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
  "id": -576460752303423253,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED+cPK1RC7xIQPK0YAgt1xsbq5Abl/zMimgocLlgVU95Q/BvGTzi80reExcCd2E6pizMWKZNJrqlUliVeiKbzsBuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFbnCjS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423253,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "signed_tx": "tx_+JALAfhCuED+cPK1RC7xIQPK0YAgt1xsbq5Abl/zMimgocLlgVU95Q/BvGTzi80reExcCd2E6pizMWKZNJrqlUliVeiKbzsBuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFbnCjS",
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
  "id": -576460752303423252,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAPxNPX3g65N1r5Cx+JGa6Nt2HMT5sosfl7ibiG82ZDm16keIWpYb2aTXCHi+4bs1wznjmUziA6rHW2xZkl2QANuED+cPK1RC7xIQPK0YAgt1xsbq5Abl/zMimgocLlgVU95Q/BvGTzi80reExcCd2E6pizMWKZNJrqlUliVeiKbzsBuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHCiXnL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423252,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEAPxNPX3g65N1r5Cx+JGa6Nt2HMT5sosfl7ibiG82ZDm16keIWpYb2aTXCHi+4bs1wznjmUziA6rHW2xZkl2QANuED+cPK1RC7xIQPK0YAgt1xsbq5Abl/zMimgocLlgVU95Q/BvGTzi80reExcCd2E6pizMWKZNJrqlUliVeiKbzsBuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHCiXnL"
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
    "data": {
      "state": "tx_+NILAfiEuEAPxNPX3g65N1r5Cx+JGa6Nt2HMT5sosfl7ibiG82ZDm16keIWpYb2aTXCHi+4bs1wznjmUziA6rHW2xZkl2QANuED+cPK1RC7xIQPK0YAgt1xsbq5Abl/zMimgocLlgVU95Q/BvGTzi80reExcCd2E6pizMWKZNJrqlUliVeiKbzsBuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHCiXnL"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423251,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423251,
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
  "id": -576460752303423250,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423250,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAPxNPX3g65N1r5Cx+JGa6Nt2HMT5sosfl7ibiG82ZDm16keIWpYb2aTXCHi+4bs1wznjmUziA6rHW2xZkl2QANuED+cPK1RC7xIQPK0YAgt1xsbq5Abl/zMimgocLlgVU95Q/BvGTzi80reExcCd2E6pizMWKZNJrqlUliVeiKbzsBuEj4RjkCoQaRlpzodLodr6HjYySBmKsh+UU5e5MoxZ5grLaR0RezPwagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHCiXnL",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423249,
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423249,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423248,
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
    "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
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
  "channel_id": "ch_277ro7EiWgW4YPwfXhpEwcnmjvuBUQqhXAXfSKYoJy3C2Wr6sE",
  "id": -576460752303423248,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
