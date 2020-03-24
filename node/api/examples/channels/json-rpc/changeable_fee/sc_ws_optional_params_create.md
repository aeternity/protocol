
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=123456789876543&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_Jz+VCFL7cFF7x3sv2uNS43wSwOrWRkQowtq45e00QseCkFbn"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=123456789876543&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_2avrNRuR/RPVph0/dw9kkHGnK76+j1t1UxNuzDJLHi2/rdO9"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhnBIhhsPP8CgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs3FrZrNA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422679,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAk3PK418Q5LEW1iPOdMWsu7S35Uu5RRYpSChdHEAYgidPu+Q3dxZZLdSwxtB5pcSwwPXrup95r3H9yu04YnMgNuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIZwSIYbDz/AoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LNxs/QZ4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422679,
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "fsm_id": "ba_2avrNRuR/RPVph0/dw9kkHGnK76+j1t1UxNuzDJLHi2/rdO9",
      "signed_tx": "tx_+MsLAfhCuEAk3PK418Q5LEW1iPOdMWsu7S35Uu5RRYpSChdHEAYgidPu+Q3dxZZLdSwxtB5pcSwwPXrup95r3H9yu04YnMgNuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIZwSIYbDz/AoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LNxs/QZ4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422678,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAJNzyuNfEOSxFtYjznTFrLu0t+VLuUUWKUgoXRxAGIInT7vkN3cWWS3UsMbQeaXEsMD167qfea9x/crtOGJzIDbhA/kxUHg60dxRbkCtc0q7EcseoITd6fHUrJGtWd460dAOG32+Uk47dBUfI6ZugBVuGzAW0xqTZ8k0pY3lgwPUeDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGcEiGGw8/wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzdEVbBd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
  "id": -576460752303422678,
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAJNzyuNfEOSxFtYjznTFrLu0t+VLuUUWKUgoXRxAGIInT7vkN3cWWS3UsMbQeaXEsMD167qfea9x/crtOGJzIDbhA/kxUHg60dxRbkCtc0q7EcseoITd6fHUrJGtWd460dAOG32+Uk47dBUfI6ZugBVuGzAW0xqTZ8k0pY3lgwPUeDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGcEiGGw8/wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzdEVbBd",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Jz+VCFL7cFF7x3sv2uNS43wSwOrWRkQowtq45e00QseCkFbn"
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAJNzyuNfEOSxFtYjznTFrLu0t+VLuUUWKUgoXRxAGIInT7vkN3cWWS3UsMbQeaXEsMD167qfea9x/crtOGJzIDbhA/kxUHg60dxRbkCtc0q7EcseoITd6fHUrJGtWd460dAOG32+Uk47dBUfI6ZugBVuGzAW0xqTZ8k0pY3lgwPUeDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGcEiGGw8/wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzdEVbBd",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJNzyuNfEOSxFtYjznTFrLu0t+VLuUUWKUgoXRxAGIInT7vkN3cWWS3UsMbQeaXEsMD167qfea9x/crtOGJzIDbhA/kxUHg60dxRbkCtc0q7EcseoITd6fHUrJGtWd460dAOG32+Uk47dBUfI6ZugBVuGzAW0xqTZ8k0pY3lgwPUeDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGcEiGGw8/wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzdEVbBd",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJNzyuNfEOSxFtYjznTFrLu0t+VLuUUWKUgoXRxAGIInT7vkN3cWWS3UsMbQeaXEsMD167qfea9x/crtOGJzIDbhA/kxUHg60dxRbkCtc0q7EcseoITd6fHUrJGtWd460dAOG32+Uk47dBUfI6ZugBVuGzAW0xqTZ8k0pY3lgwPUeDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGcEiGGw8/wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzdEVbBd",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "message": {
        "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "message": {
        "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
  "id": -576460752303422677,
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
  "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
  "id": -576460752303422677,
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "state": "tx_+QENCwH4hLhAJNzyuNfEOSxFtYjznTFrLu0t+VLuUUWKUgoXRxAGIInT7vkN3cWWS3UsMbQeaXEsMD167qfea9x/crtOGJzIDbhA/kxUHg60dxRbkCtc0q7EcseoITd6fHUrJGtWd460dAOG32+Uk47dBUfI6ZugBVuGzAW0xqTZ8k0pY3lgwPUeDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGcEiGGw8/wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzdEVbBd"
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "state": "tx_+QENCwH4hLhAJNzyuNfEOSxFtYjznTFrLu0t+VLuUUWKUgoXRxAGIInT7vkN3cWWS3UsMbQeaXEsMD167qfea9x/crtOGJzIDbhA/kxUHg60dxRbkCtc0q7EcseoITd6fHUrJGtWd460dAOG32+Uk47dBUfI6ZugBVuGzAW0xqTZ8k0pY3lgwPUeDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGcEiGGw8/wKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzdEVbBd"
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBqxFKjUfmgUwbmcvC3i8u6jzyGZzsWpRYQMqmJE3OetJoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/+GHLHOiuwBAIYPXtZ/KAA48KTq+w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422676,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEC9B3VSkOzqv+9OifRlQlsBhUTkzbZpuaAFCGg+2ReQZ8mm3uYr37yp5fsXMGDb3oQ4D1UjxvJeJyWkhGCVn/ACuF/4XTUBoQasRSo1H5oFMG5nLwt4vLuo88hmc7FqUWEDKpiRNznrSaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAOD0mpc4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
  "id": -576460752303422676,
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEC9B3VSkOzqv+9OifRlQlsBhUTkzbZpuaAFCGg+2ReQZ8mm3uYr37yp5fsXMGDb3oQ4D1UjxvJeJyWkhGCVn/ACuF/4XTUBoQasRSo1H5oFMG5nLwt4vLuo88hmc7FqUWEDKpiRNznrSaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAOD0mpc4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422675,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAG80RdaamUM7B87cYUdivTwtJ4+mZ5w6gbZ3wMkS3Pqp767mMETE9GleuC3RD+n0BSMbm4CkMhh33zcZmewa0FuEC9B3VSkOzqv+9OifRlQlsBhUTkzbZpuaAFCGg+2ReQZ8mm3uYr37yp5fsXMGDb3oQ4D1UjxvJeJyWkhGCVn/ACuF/4XTUBoQasRSo1H5oFMG5nLwt4vLuo88hmc7FqUWEDKpiRNznrSaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAOP37wfs="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
  "id": -576460752303422675,
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAG80RdaamUM7B87cYUdivTwtJ4+mZ5w6gbZ3wMkS3Pqp767mMETE9GleuC3RD+n0BSMbm4CkMhh33zcZmewa0FuEC9B3VSkOzqv+9OifRlQlsBhUTkzbZpuaAFCGg+2ReQZ8mm3uYr37yp5fsXMGDb3oQ4D1UjxvJeJyWkhGCVn/ACuF/4XTUBoQasRSo1H5oFMG5nLwt4vLuo88hmc7FqUWEDKpiRNznrSaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAOP37wfs=",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAG80RdaamUM7B87cYUdivTwtJ4+mZ5w6gbZ3wMkS3Pqp767mMETE9GleuC3RD+n0BSMbm4CkMhh33zcZmewa0FuEC9B3VSkOzqv+9OifRlQlsBhUTkzbZpuaAFCGg+2ReQZ8mm3uYr37yp5fsXMGDb3oQ4D1UjxvJeJyWkhGCVn/ACuF/4XTUBoQasRSo1H5oFMG5nLwt4vLuo88hmc7FqUWEDKpiRNznrSaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAOP37wfs=",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAG80RdaamUM7B87cYUdivTwtJ4+mZ5w6gbZ3wMkS3Pqp767mMETE9GleuC3RD+n0BSMbm4CkMhh33zcZmewa0FuEC9B3VSkOzqv+9OifRlQlsBhUTkzbZpuaAFCGg+2ReQZ8mm3uYr37yp5fsXMGDb3oQ4D1UjxvJeJyWkhGCVn/ACuF/4XTUBoQasRSo1H5oFMG5nLwt4vLuo88hmc7FqUWEDKpiRNznrSaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAOP37wfs=",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAG80RdaamUM7B87cYUdivTwtJ4+mZ5w6gbZ3wMkS3Pqp767mMETE9GleuC3RD+n0BSMbm4CkMhh33zcZmewa0FuEC9B3VSkOzqv+9OifRlQlsBhUTkzbZpuaAFCGg+2ReQZ8mm3uYr37yp5fsXMGDb3oQ4D1UjxvJeJyWkhGCVn/ACuF/4XTUBoQasRSo1H5oFMG5nLwt4vLuo88hmc7FqUWEDKpiRNznrSaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAOP37wfs=",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
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
    "channel_id": "ch_2JsQoeDGU2w3rnPA8YNKXRjbSkPGjNjqfoSwKcM8saVNCJjTfy",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
