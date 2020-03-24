
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3566%5Binitiator%5D
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
      "fsm_id": "ba_cHed70TRcy6a/vKW0C8nA0/z0catoeKKRq7JyVPZYzPs6u6a"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3566%5Binitiator%5D
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
      "fsm_id": "ba_QEHKwyGUbcIpHzddpMA/cgIVgp+GxqwL1LVs2MsJIImptm/c"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsMStI6QQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423301,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECxEsBjX+vMKnw0I/UDbuiegbD1eU+YZgTfch9HQOzMswn/S3+QamHX5nYsD3b4Qrg5XxcdJc98yy2m/uZ9u5IDuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LDAti/0M="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423301,
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "fsm_id": "ba_QEHKwyGUbcIpHzddpMA/cgIVgp+GxqwL1LVs2MsJIImptm/c",
      "signed_tx": "tx_+MsLAfhCuECxEsBjX+vMKnw0I/UDbuiegbD1eU+YZgTfch9HQOzMswn/S3+QamHX5nYsD3b4Qrg5XxcdJc98yy2m/uZ9u5IDuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LDAti/0M=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423300,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAkcGfSKdKErazrDl/IQ5p28VM7+gA5SrZVuZ6RimJQ2OBkWTKI3epxMQ8Pe5EtiOqv4Krr5rz2ek9xff9BnocBbhAsRLAY1/rzCp8NCP1A27onoGw9XlPmGYE33IfR0DszLMJ/0t/kGph1+Z2LA92+EK4OV8XHSXPfMstpv7mfbuSA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwxzPIpu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
  "id": -576460752303423300,
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAkcGfSKdKErazrDl/IQ5p28VM7+gA5SrZVuZ6RimJQ2OBkWTKI3epxMQ8Pe5EtiOqv4Krr5rz2ek9xff9BnocBbhAsRLAY1/rzCp8NCP1A27onoGw9XlPmGYE33IfR0DszLMJ/0t/kGph1+Z2LA92+EK4OV8XHSXPfMstpv7mfbuSA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwxzPIpu",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_cHed70TRcy6a/vKW0C8nA0/z0catoeKKRq7JyVPZYzPs6u6a"
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAkcGfSKdKErazrDl/IQ5p28VM7+gA5SrZVuZ6RimJQ2OBkWTKI3epxMQ8Pe5EtiOqv4Krr5rz2ek9xff9BnocBbhAsRLAY1/rzCp8NCP1A27onoGw9XlPmGYE33IfR0DszLMJ/0t/kGph1+Z2LA92+EK4OV8XHSXPfMstpv7mfbuSA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwxzPIpu",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAkcGfSKdKErazrDl/IQ5p28VM7+gA5SrZVuZ6RimJQ2OBkWTKI3epxMQ8Pe5EtiOqv4Krr5rz2ek9xff9BnocBbhAsRLAY1/rzCp8NCP1A27onoGw9XlPmGYE33IfR0DszLMJ/0t/kGph1+Z2LA92+EK4OV8XHSXPfMstpv7mfbuSA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwxzPIpu",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAkcGfSKdKErazrDl/IQ5p28VM7+gA5SrZVuZ6RimJQ2OBkWTKI3epxMQ8Pe5EtiOqv4Krr5rz2ek9xff9BnocBbhAsRLAY1/rzCp8NCP1A27onoGw9XlPmGYE33IfR0DszLMJ/0t/kGph1+Z2LA92+EK4OV8XHSXPfMstpv7mfbuSA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwxzPIpu",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "message": {
        "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "message": {
        "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
  "id": -576460752303423299,
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
  "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
  "id": -576460752303423299,
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "state": "tx_+QENCwH4hLhAkcGfSKdKErazrDl/IQ5p28VM7+gA5SrZVuZ6RimJQ2OBkWTKI3epxMQ8Pe5EtiOqv4Krr5rz2ek9xff9BnocBbhAsRLAY1/rzCp8NCP1A27onoGw9XlPmGYE33IfR0DszLMJ/0t/kGph1+Z2LA92+EK4OV8XHSXPfMstpv7mfbuSA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwxzPIpu"
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "state": "tx_+QENCwH4hLhAkcGfSKdKErazrDl/IQ5p28VM7+gA5SrZVuZ6RimJQ2OBkWTKI3epxMQ8Pe5EtiOqv4Krr5rz2ek9xff9BnocBbhAsRLAY1/rzCp8NCP1A27onoGw9XlPmGYE33IfR0DszLMJ/0t/kGph1+Z2LA92+EK4OV8XHSXPfMstpv7mfbuSA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwxzPIpu"
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
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBvAnllw9QKBhJDqRgI6KSpGaJgNp+d3lWEnTULwxr+KWoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7sgIAADXKeB2g=",
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
    "signed_tx": "tx_+QHrCwH4QrhAi8QXKMC+NK8366P9avpE/hkZacyPUKebSFU/46tfBpy+cj0hEpddRmmmof7SzpmZVdoBIi1T+0rDa6X6LmkOCrkBovkBnzYBoQbwJ5ZcPUCgYSQ6kYCOikqRmiYDafnd5VhJ01C8Ma/ilqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAA0Yt3zr"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAi8QXKMC+NK8366P9avpE/hkZacyPUKebSFU/46tfBpy+cj0hEpddRmmmof7SzpmZVdoBIi1T+0rDa6X6LmkOCrkBovkBnzYBoQbwJ5ZcPUCgYSQ6kYCOikqRmiYDafnd5VhJ01C8Ma/ilqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAA0Yt3zr",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAi8QXKMC+NK8366P9avpE/hkZacyPUKebSFU/46tfBpy+cj0hEpddRmmmof7SzpmZVdoBIi1T+0rDa6X6LmkOCrkBovkBnzYBoQbwJ5ZcPUCgYSQ6kYCOikqRmiYDafnd5VhJ01C8Ma/ilqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAA0Yt3zr",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBvAnllw9QKBhJDqRgI6KSpGaJgNp+d3lWEnTULwxr+KWoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAAEDRv/Hw==",
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
    "signed_tx": "tx_+KcLAfhCuEDEUwI0/XqO25HaC8iNYpI1/VEQ5NLZ8VyPbSUaZwhnofdcdvnyhvKA/wWXfMULpOUTjM+uheiK8cHWexxUoV4OuF/4XTgBoQbwJ5ZcPUCgYSQ6kYCOikqRmiYDafnd5VhJ01C8Ma/ilqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygABC3o9Bc="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDEUwI0/XqO25HaC8iNYpI1/VEQ5NLZ8VyPbSUaZwhnofdcdvnyhvKA/wWXfMULpOUTjM+uheiK8cHWexxUoV4OuF/4XTgBoQbwJ5ZcPUCgYSQ6kYCOikqRmiYDafnd5VhJ01C8Ma/ilqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygABC3o9Bc=",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDEUwI0/XqO25HaC8iNYpI1/VEQ5NLZ8VyPbSUaZwhnofdcdvnyhvKA/wWXfMULpOUTjM+uheiK8cHWexxUoV4OuF/4XTgBoQbwJ5ZcPUCgYSQ6kYCOikqRmiYDafnd5VhJ01C8Ma/ilqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygABC3o9Bc=",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
    "channel_id": "ch_2pmRpUwmhBM7MhZ3niXSCQj1SZxVp3d1YcR7tkP83cKJMPMHwc",
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
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3566%5Bresponder%5D
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
      "fsm_id": "ba_fBAPmB/fGKYKxSd5+3EfLrJ7egZDHfh1gPbKYALqjS6xvSkv"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3566%5Bresponder%5D
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
      "fsm_id": "ba_BTrkiFiVCrZDgh74MjxuCiYiTEKalyuJ5W5wk1fvkneA/L/O"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsOgtTqWg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423298,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuED/RFkaI0RuCp0tLZOUcZG44UfHa7j/0cpc4aivKZppk1Ahs2qYvb9oeKtC48JiIzyde3SFKrhDhD7K9PhYLfICuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LDrTopUc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423298,
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "fsm_id": "ba_BTrkiFiVCrZDgh74MjxuCiYiTEKalyuJ5W5wk1fvkneA/L/O",
      "signed_tx": "tx_+MsLAfhCuED/RFkaI0RuCp0tLZOUcZG44UfHa7j/0cpc4aivKZppk1Ahs2qYvb9oeKtC48JiIzyde3SFKrhDhD7K9PhYLfICuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LDrTopUc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423297,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhA+TWsc7macb4a+PK7PaAy5rJ2BZG9aUFR402yvmtBfOH3Wpc7dFHeg6+0HO4VocddxrQOt6G38RII6csqHHK3ArhA/0RZGiNEbgqdLS2TlHGRuOFHx2u4/9HKXOGorymaaZNQIbNqmL2/aHirQuPCYiM8nXt0hSq4Q4Q+yvT4WC3yAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCw6P6CU1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
  "id": -576460752303423297,
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhA+TWsc7macb4a+PK7PaAy5rJ2BZG9aUFR402yvmtBfOH3Wpc7dFHeg6+0HO4VocddxrQOt6G38RII6csqHHK3ArhA/0RZGiNEbgqdLS2TlHGRuOFHx2u4/9HKXOGorymaaZNQIbNqmL2/aHirQuPCYiM8nXt0hSq4Q4Q+yvT4WC3yAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCw6P6CU1",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_fBAPmB/fGKYKxSd5+3EfLrJ7egZDHfh1gPbKYALqjS6xvSkv"
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhA+TWsc7macb4a+PK7PaAy5rJ2BZG9aUFR402yvmtBfOH3Wpc7dFHeg6+0HO4VocddxrQOt6G38RII6csqHHK3ArhA/0RZGiNEbgqdLS2TlHGRuOFHx2u4/9HKXOGorymaaZNQIbNqmL2/aHirQuPCYiM8nXt0hSq4Q4Q+yvT4WC3yAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCw6P6CU1",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA+TWsc7macb4a+PK7PaAy5rJ2BZG9aUFR402yvmtBfOH3Wpc7dFHeg6+0HO4VocddxrQOt6G38RII6csqHHK3ArhA/0RZGiNEbgqdLS2TlHGRuOFHx2u4/9HKXOGorymaaZNQIbNqmL2/aHirQuPCYiM8nXt0hSq4Q4Q+yvT4WC3yAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCw6P6CU1",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA+TWsc7macb4a+PK7PaAy5rJ2BZG9aUFR402yvmtBfOH3Wpc7dFHeg6+0HO4VocddxrQOt6G38RII6csqHHK3ArhA/0RZGiNEbgqdLS2TlHGRuOFHx2u4/9HKXOGorymaaZNQIbNqmL2/aHirQuPCYiM8nXt0hSq4Q4Q+yvT4WC3yAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCw6P6CU1",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "message": {
        "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "message": {
        "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
  "id": -576460752303423296,
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
  "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
  "id": -576460752303423296,
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "state": "tx_+QENCwH4hLhA+TWsc7macb4a+PK7PaAy5rJ2BZG9aUFR402yvmtBfOH3Wpc7dFHeg6+0HO4VocddxrQOt6G38RII6csqHHK3ArhA/0RZGiNEbgqdLS2TlHGRuOFHx2u4/9HKXOGorymaaZNQIbNqmL2/aHirQuPCYiM8nXt0hSq4Q4Q+yvT4WC3yAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCw6P6CU1"
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "state": "tx_+QENCwH4hLhA+TWsc7macb4a+PK7PaAy5rJ2BZG9aUFR402yvmtBfOH3Wpc7dFHeg6+0HO4VocddxrQOt6G38RII6csqHHK3ArhA/0RZGiNEbgqdLS2TlHGRuOFHx2u4/9HKXOGorymaaZNQIbNqmL2/aHirQuPCYiM8nXt0hSq4Q4Q+yvT4WC3yAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCw6P6CU1"
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBtonIaEeJqGHs32fnoKvqwzSdCkN8jaLxiTc9vBf808zoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7sgIAABRUnkb8=",
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
    "signed_tx": "tx_+QHrCwH4QrhA7oYFLSS08tZSsIaYOZD0VxW1Qa6/z6CoQn+W0/fnwKbd/Ms4RZh/8itK31waaK4jD5IxpjbE0nNZPBOI7ti9ALkBovkBnzYBoQbaJyGhHiahh7N9n56Cr6sM0nQpDfI2i8Yk3PbwX/NPM6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAAUDAFAO"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA7oYFLSS08tZSsIaYOZD0VxW1Qa6/z6CoQn+W0/fnwKbd/Ms4RZh/8itK31waaK4jD5IxpjbE0nNZPBOI7ti9ALkBovkBnzYBoQbaJyGhHiahh7N9n56Cr6sM0nQpDfI2i8Yk3PbwX/NPM6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAAUDAFAO",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA7oYFLSS08tZSsIaYOZD0VxW1Qa6/z6CoQn+W0/fnwKbd/Ms4RZh/8itK31waaK4jD5IxpjbE0nNZPBOI7ti9ALkBovkBnzYBoQbaJyGhHiahh7N9n56Cr6sM0nQpDfI2i8Yk3PbwX/NPM6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAAUDAFAO",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
  "method": "channels.settle",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBtonIaEeJqGHs32fnoKvqwzSdCkN8jaLxiTc9vBf808zoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiX/+GJGE5yoABAIYPXtZ/KAAPIeLF6A==",
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
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECQetnGvZuOqXS6icrW9tXPOsUiNtvNdoK8kc+x1gJAPak49jQ616Ph3IZcpr7vaxzeoAkP0nDHzPibSUn5v+8IuF/4XTgBoQbaJyGhHiahh7N9n56Cr6sM0nQpDfI2i8Yk3PbwX/NPM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGD17WfygAD9NysaE="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECQetnGvZuOqXS6icrW9tXPOsUiNtvNdoK8kc+x1gJAPak49jQ616Ph3IZcpr7vaxzeoAkP0nDHzPibSUn5v+8IuF/4XTgBoQbaJyGhHiahh7N9n56Cr6sM0nQpDfI2i8Yk3PbwX/NPM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGD17WfygAD9NysaE=",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECQetnGvZuOqXS6icrW9tXPOsUiNtvNdoK8kc+x1gJAPak49jQ616Ph3IZcpr7vaxzeoAkP0nDHzPibSUn5v+8IuF/4XTgBoQbaJyGhHiahh7N9n56Cr6sM0nQpDfI2i8Yk3PbwX/NPM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGD17WfygAD9NysaE=",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
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
    "channel_id": "ch_2f5RUQ26wQdYtZXcVwUpmSH3q4LHdHgbhBDxswadnYcjej3q2N",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
