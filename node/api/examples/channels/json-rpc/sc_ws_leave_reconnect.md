
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reconnect%2F3760
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
      "fsm_id": "ba_xPMf4vwu/OqDnX8CLdeIMOhrnoDmstbkEzUciK+GGZwjyp4n"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=true&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reconnect%2F3760
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
      "fsm_id": "ba_YKGJTh8jLCeRgYNqauzkkk3bfhIk3GkYaKKb55IyTlFkgoMd"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsYRiptuQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423187,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuED1StdhUKOD8u4l3xxbx/7yPgkVxQ3QVmoh5stYANM9hhykiCIJX7yct/WIbucwokcDKGS0/2eclSOiK8WFzqcEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LGCFEJa0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423187,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "fsm_id": "ba_YKGJTh8jLCeRgYNqauzkkk3bfhIk3GkYaKKb55IyTlFkgoMd",
      "signed_tx": "tx_+MsLAfhCuED1StdhUKOD8u4l3xxbx/7yPgkVxQ3QVmoh5stYANM9hhykiCIJX7yct/WIbucwokcDKGS0/2eclSOiK8WFzqcEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LGCFEJa0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423186,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423186,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_xPMf4vwu/OqDnX8CLdeIMOhrnoDmstbkEzUciK+GGZwjyp4n"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "message": {
        "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "message": {
        "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "id": -576460752303423185,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423185,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "event": "peer_disconnected"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAw%2BFykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn%2BRJaFY%2FYaXnPs31%2BheXTDPGoBrhA9UrXYVCjg%2FLuJd8cW8f%2B8j4JFcUN0FZqIebLWADTPYYcpIgiCV%2B8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAw%2BFykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn%2BRJaFY%2FYaXnPs31%2BheXTDPGoBrhA9UrXYVCjg%2FLuJd8cW8f%2B8j4JFcUN0FZqIebLWADTPYYcpIgiCV%2B8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ&existing_fsm_id=ba_w2v7iTWFmK%2BnyaZI&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAw%2BFykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn%2BRJaFY%2FYaXnPs31%2BheXTDPGoBrhA9UrXYVCjg%2FLuJd8cW8f%2B8j4JFcUN0FZqIebLWADTPYYcpIgiCV%2B8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ&existing_fsm_id=ba_Xw4zY05qFTmDnGvKuCfOvZG0S9cN4%2Fd4%2BfiuEUry3GTdikDs&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAw%2BFykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn%2BRJaFY%2FYaXnPs31%2BheXTDPGoBrhA9UrXYVCjg%2FLuJd8cW8f%2B8j4JFcUN0FZqIebLWADTPYYcpIgiCV%2B8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ&existing_fsm_id=ba_xPMf4vwu%2FOqDnX8CLdeIMOhrnoDmstbkEzUciK%2BGGZwjyp4n&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAw%2BFykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn%2BRJaFY%2FYaXnPs31%2BheXTDPGoBrhA9UrXYVCjg%2FLuJd8cW8f%2B8j4JFcUN0FZqIebLWADTPYYcpIgiCV%2B8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW&port=13179&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_9UuhYg7sFdoqNeL9f1AdYXsDRCW9Mr6f72LLBo0tNiunNDQv"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+QENCwH4hLhAw+FykirSLY6Df6S5yUaVoje9Od72BOMVrZALLYqF8lw6kg1jAc4bcgEm5bgn+RJaFY/YaXnPs31+heXTDPGoBrhA9UrXYVCjg/LuJd8cW8f+8j4JFcUN0FZqIebLWADTPYYcpIgiCV+8nLf1iG7nMKJHAyhktP9nnJUjoivFhc6nBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxjQnniW"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423184,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423184,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiDiFsWmRFjv+opYyPgRwXxhwv24m+JBHujjves+/+0NAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAlwptfI=",
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
  "id": -576460752303423183,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBPOoN9UYX/kMOwXuSWBd44deLEZ3fqCukLF1HNRG2/e0EXkRApbS8QF+3a7hAOiB2tqnKHUeOeFCVWa8xBYDoMuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIS9n3o"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423183,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBPOoN9UYX/kMOwXuSWBd44deLEZ3fqCukLF1HNRG2/e0EXkRApbS8QF+3a7hAOiB2tqnKHUeOeFCVWa8xBYDoMuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIS9n3o",
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
  "id": -576460752303423182,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBPOoN9UYX/kMOwXuSWBd44deLEZ3fqCukLF1HNRG2/e0EXkRApbS8QF+3a7hAOiB2tqnKHUeOeFCVWa8xBYDoMuEDFepX+XRx4AIJk5p9IZuM95g4A3AsbJ6KLZZ755ONT9ddDTPbtXMSFdvX896gFMp6+g/b7S5cTSRoFY5eOhvIOuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKrOkOZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423182,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuEBPOoN9UYX/kMOwXuSWBd44deLEZ3fqCukLF1HNRG2/e0EXkRApbS8QF+3a7hAOiB2tqnKHUeOeFCVWa8xBYDoMuEDFepX+XRx4AIJk5p9IZuM95g4A3AsbJ6KLZZ755ONT9ddDTPbtXMSFdvX896gFMp6+g/b7S5cTSRoFY5eOhvIOuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKrOkOZ"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuEBPOoN9UYX/kMOwXuSWBd44deLEZ3fqCukLF1HNRG2/e0EXkRApbS8QF+3a7hAOiB2tqnKHUeOeFCVWa8xBYDoMuEDFepX+XRx4AIJk5p9IZuM95g4A3AsbJ6KLZZ755ONT9ddDTPbtXMSFdvX896gFMp6+g/b7S5cTSRoFY5eOhvIOuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKrOkOZ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423181,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423181,
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
  "id": -576460752303423180,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423180,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBPOoN9UYX/kMOwXuSWBd44deLEZ3fqCukLF1HNRG2/e0EXkRApbS8QF+3a7hAOiB2tqnKHUeOeFCVWa8xBYDoMuEDFepX+XRx4AIJk5p9IZuM95g4A3AsbJ6KLZZ755ONT9ddDTPbtXMSFdvX896gFMp6+g/b7S5cTSRoFY5eOhvIOuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKrOkOZ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423179,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423179,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiDiFsWmRFjv+opYyPgRwXxhwv24m+JBHujjves+/+0NA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzUk7rE=",
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
  "id": -576460752303423178,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECpVlwcKjAq2uN+Z5RTJcvyVZ/u6z4bzw26PdcXJ4B5lznmXnTPn88ipZ8bn++2d0TvbKjOtrhORudIWL0GZMUGuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsfOAec"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423178,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuECpVlwcKjAq2uN+Z5RTJcvyVZ/u6z4bzw26PdcXJ4B5lznmXnTPn88ipZ8bn++2d0TvbKjOtrhORudIWL0GZMUGuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsfOAec",
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
  "id": -576460752303423177,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECpVlwcKjAq2uN+Z5RTJcvyVZ/u6z4bzw26PdcXJ4B5lznmXnTPn88ipZ8bn++2d0TvbKjOtrhORudIWL0GZMUGuEDOh2F8IbfBml6y6dpZFIL4IonyxHtYWsVWCjXYvGc2Mi2vBzHfi0HdY8sE8/uSQcgEpONckL/sLbNDGO24krsGuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsbg3sx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423177,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuECpVlwcKjAq2uN+Z5RTJcvyVZ/u6z4bzw26PdcXJ4B5lznmXnTPn88ipZ8bn++2d0TvbKjOtrhORudIWL0GZMUGuEDOh2F8IbfBml6y6dpZFIL4IonyxHtYWsVWCjXYvGc2Mi2vBzHfi0HdY8sE8/uSQcgEpONckL/sLbNDGO24krsGuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsbg3sx"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuECpVlwcKjAq2uN+Z5RTJcvyVZ/u6z4bzw26PdcXJ4B5lznmXnTPn88ipZ8bn++2d0TvbKjOtrhORudIWL0GZMUGuEDOh2F8IbfBml6y6dpZFIL4IonyxHtYWsVWCjXYvGc2Mi2vBzHfi0HdY8sE8/uSQcgEpONckL/sLbNDGO24krsGuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsbg3sx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423176,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423176,
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
  "id": -576460752303423175,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423175,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECpVlwcKjAq2uN+Z5RTJcvyVZ/u6z4bzw26PdcXJ4B5lznmXnTPn88ipZ8bn++2d0TvbKjOtrhORudIWL0GZMUGuEDOh2F8IbfBml6y6dpZFIL4IonyxHtYWsVWCjXYvGc2Mi2vBzHfi0HdY8sE8/uSQcgEpONckL/sLbNDGO24krsGuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsbg3sx",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423174,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423174,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiDiFsWmRFjv+opYyPgRwXxhwv24m+JBHujjves+/+0NBKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMS0+65I=",
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
  "id": -576460752303423173,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECqVbNnkO5SGfGQ0ovMwqOu8zHfdW2VmCfMA926kn5S7mDofnm9s2brUYsZVx5i9olrCO6g4V3AhZ5URGukEc4BuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jH3MVi4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423173,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuECqVbNnkO5SGfGQ0ovMwqOu8zHfdW2VmCfMA926kn5S7mDofnm9s2brUYsZVx5i9olrCO6g4V3AhZ5URGukEc4BuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jH3MVi4",
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
  "id": -576460752303423172,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECqVbNnkO5SGfGQ0ovMwqOu8zHfdW2VmCfMA926kn5S7mDofnm9s2brUYsZVx5i9olrCO6g4V3AhZ5URGukEc4BuEDuFl9VaunxuuuI/UUwVLvMdUR/WA3ZSzZ3TYuviRKVnSgod/m5Ot+cLYs+YfiybPQ/Pc2fOxc7rj5n/q/+hecPuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEDdVEY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423172,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuECqVbNnkO5SGfGQ0ovMwqOu8zHfdW2VmCfMA926kn5S7mDofnm9s2brUYsZVx5i9olrCO6g4V3AhZ5URGukEc4BuEDuFl9VaunxuuuI/UUwVLvMdUR/WA3ZSzZ3TYuviRKVnSgod/m5Ot+cLYs+YfiybPQ/Pc2fOxc7rj5n/q/+hecPuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEDdVEY"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuECqVbNnkO5SGfGQ0ovMwqOu8zHfdW2VmCfMA926kn5S7mDofnm9s2brUYsZVx5i9olrCO6g4V3AhZ5URGukEc4BuEDuFl9VaunxuuuI/UUwVLvMdUR/WA3ZSzZ3TYuviRKVnSgod/m5Ot+cLYs+YfiybPQ/Pc2fOxc7rj5n/q/+hecPuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEDdVEY"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423171,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423171,
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
  "id": -576460752303423170,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423170,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECqVbNnkO5SGfGQ0ovMwqOu8zHfdW2VmCfMA926kn5S7mDofnm9s2brUYsZVx5i9olrCO6g4V3AhZ5URGukEc4BuEDuFl9VaunxuuuI/UUwVLvMdUR/WA3ZSzZ3TYuviRKVnSgod/m5Ot+cLYs+YfiybPQ/Pc2fOxc7rj5n/q/+hecPuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEDdVEY",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423169,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423169,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiDiFsWmRFjv+opYyPgRwXxhwv24m+JBHujjves+/+0NBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC8uN/wE=",
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
  "id": -576460752303423168,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB/dCRv9SCkxy8zNfO+1ML0NE9dYQOm0iomxx0QwPRIdHMKM1Y0mkXzkvxiHBjwbpkTcUGPw6MvE4Y4vhEKkqUPuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguTl9Q1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423168,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB/dCRv9SCkxy8zNfO+1ML0NE9dYQOm0iomxx0QwPRIdHMKM1Y0mkXzkvxiHBjwbpkTcUGPw6MvE4Y4vhEKkqUPuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguTl9Q1",
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
  "id": -576460752303423167,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB/dCRv9SCkxy8zNfO+1ML0NE9dYQOm0iomxx0QwPRIdHMKM1Y0mkXzkvxiHBjwbpkTcUGPw6MvE4Y4vhEKkqUPuEC1+IT0CQyidUPNdqlcuc6D2PzDCXcMso2I2q6Pe8ZFXtxvLR4apLML4yU8Pg1vMa0BlSU0F+EiYkuWpw9kzWwNuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvae9/d"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423167,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuEB/dCRv9SCkxy8zNfO+1ML0NE9dYQOm0iomxx0QwPRIdHMKM1Y0mkXzkvxiHBjwbpkTcUGPw6MvE4Y4vhEKkqUPuEC1+IT0CQyidUPNdqlcuc6D2PzDCXcMso2I2q6Pe8ZFXtxvLR4apLML4yU8Pg1vMa0BlSU0F+EiYkuWpw9kzWwNuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvae9/d"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuEB/dCRv9SCkxy8zNfO+1ML0NE9dYQOm0iomxx0QwPRIdHMKM1Y0mkXzkvxiHBjwbpkTcUGPw6MvE4Y4vhEKkqUPuEC1+IT0CQyidUPNdqlcuc6D2PzDCXcMso2I2q6Pe8ZFXtxvLR4apLML4yU8Pg1vMa0BlSU0F+EiYkuWpw9kzWwNuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvae9/d"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423166,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423166,
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
  "id": -576460752303423165,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423165,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB/dCRv9SCkxy8zNfO+1ML0NE9dYQOm0iomxx0QwPRIdHMKM1Y0mkXzkvxiHBjwbpkTcUGPw6MvE4Y4vhEKkqUPuEC1+IT0CQyidUPNdqlcuc6D2PzDCXcMso2I2q6Pe8ZFXtxvLR4apLML4yU8Pg1vMa0BlSU0F+EiYkuWpw9kzWwNuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvae9/d",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423164,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423164,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiDiFsWmRFjv+opYyPgRwXxhwv24m+JBHujjves+/+0NBqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMT8ewhk=",
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
  "id": -576460752303423163,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDIpN48kRB6D25Qqd4emXlhg5GgW2N314qVACah2qX3ZCv92/EKz8eO1S1wwwjKl+t4FEOAb75jrSa1XQ196AgMuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHAaySi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423163,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDIpN48kRB6D25Qqd4emXlhg5GgW2N314qVACah2qX3ZCv92/EKz8eO1S1wwwjKl+t4FEOAb75jrSa1XQ196AgMuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHAaySi",
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
  "id": -576460752303423162,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDIpN48kRB6D25Qqd4emXlhg5GgW2N314qVACah2qX3ZCv92/EKz8eO1S1wwwjKl+t4FEOAb75jrSa1XQ196AgMuED/eMxHq5A70Qfx1wlgf8jwjdMbObrH0cDUt6Da541EXp2jrvjzbDW/fRLc8zHenk5EY+dd36tr5DtXRLMFWqACuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHc0ilW"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423162,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuEDIpN48kRB6D25Qqd4emXlhg5GgW2N314qVACah2qX3ZCv92/EKz8eO1S1wwwjKl+t4FEOAb75jrSa1XQ196AgMuED/eMxHq5A70Qfx1wlgf8jwjdMbObrH0cDUt6Da541EXp2jrvjzbDW/fRLc8zHenk5EY+dd36tr5DtXRLMFWqACuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHc0ilW"
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
    "data": {
      "state": "tx_+NILAfiEuEDIpN48kRB6D25Qqd4emXlhg5GgW2N314qVACah2qX3ZCv92/EKz8eO1S1wwwjKl+t4FEOAb75jrSa1XQ196AgMuED/eMxHq5A70Qfx1wlgf8jwjdMbObrH0cDUt6Da541EXp2jrvjzbDW/fRLc8zHenk5EY+dd36tr5DtXRLMFWqACuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHc0ilW"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423161,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423161,
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
  "id": -576460752303423160,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423160,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDIpN48kRB6D25Qqd4emXlhg5GgW2N314qVACah2qX3ZCv92/EKz8eO1S1wwwjKl+t4FEOAb75jrSa1XQ196AgMuED/eMxHq5A70Qfx1wlgf8jwjdMbObrH0cDUt6Da541EXp2jrvjzbDW/fRLc8zHenk5EY+dd36tr5DtXRLMFWqACuEj4RjkCoQYg4hbFpkRY7/qKWMj4EcF8YcL9uJviQR7o473rPv/tDQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHc0ilW",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423159,
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423159,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423158,
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
    "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
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
  "channel_id": "ch_FUxTcgy5TmSAw8t4pRva7DKkp6ovgtyGcaxxisAFYHzPEwKnJ",
  "id": -576460752303423158,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
