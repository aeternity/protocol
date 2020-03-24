
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
      "fsm_id": "ba_plf0I0rsRV+byxwKJPGokWTTZ2ZzyXu87dgIZ7KuyjCWi1dL"
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
      "fsm_id": "ba_kfbavucnQMN1I0pxT7ADR8ZHbM1994WG+CLgUZLSYRKyNnDU"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtppYpb3w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422490,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDOtQlDlM3rvU3AERQHyjHcuB+ImVDKsvlqf7pUSGCtAN2LNvPZg/ROKN+6sNgqxMAMzbaT5admhyMTd6yo4g4CuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LaQSgDcw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422490,
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "fsm_id": "ba_kfbavucnQMN1I0pxT7ADR8ZHbM1994WG+CLgUZLSYRKyNnDU",
      "signed_tx": "tx_+MsLAfhCuEDOtQlDlM3rvU3AERQHyjHcuB+ImVDKsvlqf7pUSGCtAN2LNvPZg/ROKN+6sNgqxMAMzbaT5admhyMTd6yo4g4CuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LaQSgDcw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422489,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAViyyduK88U6DbWjcSLEoyp8SmgvBJ3LadALlivlbDvV1EFtL6urVzQc/w6dA31d5IF04GWbvZFEbTv6606clArhAzrUJQ5TN671NwBEUB8ox3LgfiJlQyrL5an+6VEhgrQDdizbz2YP0TijfurDYKsTADM22k+WnZocjE3esqOIOAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2kWcxx/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
  "id": -576460752303422489,
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAViyyduK88U6DbWjcSLEoyp8SmgvBJ3LadALlivlbDvV1EFtL6urVzQc/w6dA31d5IF04GWbvZFEbTv6606clArhAzrUJQ5TN671NwBEUB8ox3LgfiJlQyrL5an+6VEhgrQDdizbz2YP0TijfurDYKsTADM22k+WnZocjE3esqOIOAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2kWcxx/",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_plf0I0rsRV+byxwKJPGokWTTZ2ZzyXu87dgIZ7KuyjCWi1dL"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAViyyduK88U6DbWjcSLEoyp8SmgvBJ3LadALlivlbDvV1EFtL6urVzQc/w6dA31d5IF04GWbvZFEbTv6606clArhAzrUJQ5TN671NwBEUB8ox3LgfiJlQyrL5an+6VEhgrQDdizbz2YP0TijfurDYKsTADM22k+WnZocjE3esqOIOAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2kWcxx/",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAViyyduK88U6DbWjcSLEoyp8SmgvBJ3LadALlivlbDvV1EFtL6urVzQc/w6dA31d5IF04GWbvZFEbTv6606clArhAzrUJQ5TN671NwBEUB8ox3LgfiJlQyrL5an+6VEhgrQDdizbz2YP0TijfurDYKsTADM22k+WnZocjE3esqOIOAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2kWcxx/",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAViyyduK88U6DbWjcSLEoyp8SmgvBJ3LadALlivlbDvV1EFtL6urVzQc/w6dA31d5IF04GWbvZFEbTv6606clArhAzrUJQ5TN671NwBEUB8ox3LgfiJlQyrL5an+6VEhgrQDdizbz2YP0TijfurDYKsTADM22k+WnZocjE3esqOIOAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2kWcxx/",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
  "id": -576460752303422488,
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
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
  "id": -576460752303422488,
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "state": "tx_+QENCwH4hLhAViyyduK88U6DbWjcSLEoyp8SmgvBJ3LadALlivlbDvV1EFtL6urVzQc/w6dA31d5IF04GWbvZFEbTv6606clArhAzrUJQ5TN671NwBEUB8ox3LgfiJlQyrL5an+6VEhgrQDdizbz2YP0TijfurDYKsTADM22k+WnZocjE3esqOIOAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2kWcxx/"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "state": "tx_+QENCwH4hLhAViyyduK88U6DbWjcSLEoyp8SmgvBJ3LadALlivlbDvV1EFtL6urVzQc/w6dA31d5IF04GWbvZFEbTv6606clArhAzrUJQ5TN671NwBEUB8ox3LgfiJlQyrL5an+6VEhgrQDdizbz2YP0TijfurDYKsTADM22k+WnZocjE3esqOIOAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2kWcxx/"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
      "method": "channels.deposit",
      "params": {
        "amount": "2"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBvJK1MrLc0farr2yV6RsNMwy070gF+E/e/TJHwPGw59aoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhuCRDDYefqAJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQJqxr2BdA==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainDeposit"
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
  "id": -576460752303422487,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEB+UltXiEGV3SQ3hEgvmllohlwmaehbIjGd1YCi0US4Y4lqIF+FkqPUP1j3A4PU2WDpXG7eAqca1nQ/Edaf46ACuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCakwHDX0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
  "id": -576460752303422487,
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEB+UltXiEGV3SQ3hEgvmllohlwmaehbIjGd1YCi0US4Y4lqIF+FkqPUP1j3A4PU2WDpXG7eAqca1nQ/Edaf46ACuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCakwHDX0=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainDeposit"
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
  "id": -576460752303422486,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEB+UltXiEGV3SQ3hEgvmllohlwmaehbIjGd1YCi0US4Y4lqIF+FkqPUP1j3A4PU2WDpXG7eAqca1nQ/Edaf46ACuEC1C6p8XrF93RRNj1da0mdbQQgLEpuK/02PosdcAOseyAvDmNibStJgfD1b5AZjSP8PaiC6LNcDVJ4AJc/xwFIKuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCak7lonQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
  "id": -576460752303422486,
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEB+UltXiEGV3SQ3hEgvmllohlwmaehbIjGd1YCi0US4Y4lqIF+FkqPUP1j3A4PU2WDpXG7eAqca1nQ/Edaf46ACuEC1C6p8XrF93RRNj1da0mdbQQgLEpuK/02PosdcAOseyAvDmNibStJgfD1b5AZjSP8PaiC6LNcDVJ4AJc/xwFIKuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCak7lonQ=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEB+UltXiEGV3SQ3hEgvmllohlwmaehbIjGd1YCi0US4Y4lqIF+FkqPUP1j3A4PU2WDpXG7eAqca1nQ/Edaf46ACuEC1C6p8XrF93RRNj1da0mdbQQgLEpuK/02PosdcAOseyAvDmNibStJgfD1b5AZjSP8PaiC6LNcDVJ4AJc/xwFIKuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCak7lonQ=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEB+UltXiEGV3SQ3hEgvmllohlwmaehbIjGd1YCi0US4Y4lqIF+FkqPUP1j3A4PU2WDpXG7eAqca1nQ/Edaf46ACuEC1C6p8XrF93RRNj1da0mdbQQgLEpuK/02PosdcAOseyAvDmNibStJgfD1b5AZjSP8PaiC6LNcDVJ4AJc/xwFIKuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCak7lonQ=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEB+UltXiEGV3SQ3hEgvmllohlwmaehbIjGd1YCi0US4Y4lqIF+FkqPUP1j3A4PU2WDpXG7eAqca1nQ/Edaf46ACuEC1C6p8XrF93RRNj1da0mdbQQgLEpuK/02PosdcAOseyAvDmNibStJgfD1b5AZjSP8PaiC6LNcDVJ4AJc/xwFIKuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCak7lonQ=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "state": "tx_+P4LAfiEuEB+UltXiEGV3SQ3hEgvmllohlwmaehbIjGd1YCi0US4Y4lqIF+FkqPUP1j3A4PU2WDpXG7eAqca1nQ/Edaf46ACuEC1C6p8XrF93RRNj1da0mdbQQgLEpuK/02PosdcAOseyAvDmNibStJgfD1b5AZjSP8PaiC6LNcDVJ4AJc/xwFIKuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCak7lonQ="
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "state": "tx_+P4LAfiEuEB+UltXiEGV3SQ3hEgvmllohlwmaehbIjGd1YCi0US4Y4lqIF+FkqPUP1j3A4PU2WDpXG7eAqca1nQ/Edaf46ACuEC1C6p8XrF93RRNj1da0mdbQQgLEpuK/02PosdcAOseyAvDmNibStJgfD1b5AZjSP8PaiC6LNcDVJ4AJc/xwFIKuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCak7lonQ="
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
    "info": "Hello",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
      "method": "channels.deposit",
      "params": {
        "amount": "2"
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
  "method": "channels.message",
  "params": {
    "info": "Hello",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBvJK1MrLc0farr2yV6RsNMwy070gF+E/e/TJHwPGw59aoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhuCRDDYefqBdYyosJiEVkIv3UfhREtMPbLmXGvLesTSuRCc8B8rvQgMrWEkTXw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainDeposit"
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
  "id": -576460752303422485,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDjGkdQQYFQZ22lE7mHkVGLAi0I0UhnmsI96Pz4W39KVIDiNXFdZZ6MdZNf9VfOFQ1hH9Ml7p/Y/ebyJd2VeaECuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDK2AJgM4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
  "id": -576460752303422485,
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDjGkdQQYFQZ22lE7mHkVGLAi0I0UhnmsI96Pz4W39KVIDiNXFdZZ6MdZNf9VfOFQ1hH9Ml7p/Y/ebyJd2VeaECuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDK2AJgM4=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainDeposit"
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
  "id": -576460752303422484,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEA9t+0x4UWV5JYkCbDUo55ztbitRxkQZ164LkFAcoNDh3+VackDYWdKfJ7Qh+vnyidhNIt5HZKtygaFvsfoAkANuEDjGkdQQYFQZ22lE7mHkVGLAi0I0UhnmsI96Pz4W39KVIDiNXFdZZ6MdZNf9VfOFQ1hH9Ml7p/Y/ebyJd2VeaECuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDKyZblIU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
  "id": -576460752303422484,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEA9t+0x4UWV5JYkCbDUo55ztbitRxkQZ164LkFAcoNDh3+VackDYWdKfJ7Qh+vnyidhNIt5HZKtygaFvsfoAkANuEDjGkdQQYFQZ22lE7mHkVGLAi0I0UhnmsI96Pz4W39KVIDiNXFdZZ6MdZNf9VfOFQ1hH9Ml7p/Y/ebyJd2VeaECuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDKyZblIU=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEA9t+0x4UWV5JYkCbDUo55ztbitRxkQZ164LkFAcoNDh3+VackDYWdKfJ7Qh+vnyidhNIt5HZKtygaFvsfoAkANuEDjGkdQQYFQZ22lE7mHkVGLAi0I0UhnmsI96Pz4W39KVIDiNXFdZZ6MdZNf9VfOFQ1hH9Ml7p/Y/ebyJd2VeaECuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDKyZblIU=",
      "type": "channel_deposit_tx"
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
    "info": "Hello",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "message": {
        "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
      }
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEA9t+0x4UWV5JYkCbDUo55ztbitRxkQZ164LkFAcoNDh3+VackDYWdKfJ7Qh+vnyidhNIt5HZKtygaFvsfoAkANuEDjGkdQQYFQZ22lE7mHkVGLAi0I0UhnmsI96Pz4W39KVIDiNXFdZZ6MdZNf9VfOFQ1hH9Ml7p/Y/ebyJd2VeaECuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDKyZblIU=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEA9t+0x4UWV5JYkCbDUo55ztbitRxkQZ164LkFAcoNDh3+VackDYWdKfJ7Qh+vnyidhNIt5HZKtygaFvsfoAkANuEDjGkdQQYFQZ22lE7mHkVGLAi0I0UhnmsI96Pz4W39KVIDiNXFdZZ6MdZNf9VfOFQ1hH9Ml7p/Y/ebyJd2VeaECuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDKyZblIU=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "state": "tx_+P4LAfiEuEA9t+0x4UWV5JYkCbDUo55ztbitRxkQZ164LkFAcoNDh3+VackDYWdKfJ7Qh+vnyidhNIt5HZKtygaFvsfoAkANuEDjGkdQQYFQZ22lE7mHkVGLAi0I0UhnmsI96Pz4W39KVIDiNXFdZZ6MdZNf9VfOFQ1hH9Ml7p/Y/ebyJd2VeaECuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDKyZblIU="
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "state": "tx_+P4LAfiEuEA9t+0x4UWV5JYkCbDUo55ztbitRxkQZ164LkFAcoNDh3+VackDYWdKfJ7Qh+vnyidhNIt5HZKtygaFvsfoAkANuEDjGkdQQYFQZ22lE7mHkVGLAi0I0UhnmsI96Pz4W39KVIDiNXFdZZ6MdZNf9VfOFQ1hH9Ml7p/Y/ebyJd2VeaECuHT4cjMBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDKyZblIU="
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBvJK1MrLc0farr2yV6RsNMwy070gF+E/e/TJHwPGw59aoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rnizAGGHLHOiuwDAIYPXtZ/KABrA6ef8A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422483,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBL+oE9gvsKLTGCj5YJ5relxMn5eB9MIOapQvzJghtQJQ4HQ8qGPo0db0LnKu2iyChMCV6tTVob3BTLNBtO9c8BuF/4XTUBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAa5zcr+w="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
  "id": -576460752303422483,
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBL+oE9gvsKLTGCj5YJ5relxMn5eB9MIOapQvzJghtQJQ4HQ8qGPo0db0LnKu2iyChMCV6tTVob3BTLNBtO9c8BuF/4XTUBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAa5zcr+w=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422482,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBL+oE9gvsKLTGCj5YJ5relxMn5eB9MIOapQvzJghtQJQ4HQ8qGPo0db0LnKu2iyChMCV6tTVob3BTLNBtO9c8BuEC0lZVkbFjLbhmWUtKjrbFsIgf4GwsD9ym9QAQZChsQJTgP+X+204c+vlk5ebp/s6bDzoqagFh1DfK3LHs/wl4OuF/4XTUBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAa18ptjI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
  "id": -576460752303422482,
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBL+oE9gvsKLTGCj5YJ5relxMn5eB9MIOapQvzJghtQJQ4HQ8qGPo0db0LnKu2iyChMCV6tTVob3BTLNBtO9c8BuEC0lZVkbFjLbhmWUtKjrbFsIgf4GwsD9ym9QAQZChsQJTgP+X+204c+vlk5ebp/s6bDzoqagFh1DfK3LHs/wl4OuF/4XTUBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAa18ptjI=",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBL+oE9gvsKLTGCj5YJ5relxMn5eB9MIOapQvzJghtQJQ4HQ8qGPo0db0LnKu2iyChMCV6tTVob3BTLNBtO9c8BuEC0lZVkbFjLbhmWUtKjrbFsIgf4GwsD9ym9QAQZChsQJTgP+X+204c+vlk5ebp/s6bDzoqagFh1DfK3LHs/wl4OuF/4XTUBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAa18ptjI=",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBL+oE9gvsKLTGCj5YJ5relxMn5eB9MIOapQvzJghtQJQ4HQ8qGPo0db0LnKu2iyChMCV6tTVob3BTLNBtO9c8BuEC0lZVkbFjLbhmWUtKjrbFsIgf4GwsD9ym9QAQZChsQJTgP+X+204c+vlk5ebp/s6bDzoqagFh1DfK3LHs/wl4OuF/4XTUBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAa18ptjI=",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBL+oE9gvsKLTGCj5YJ5relxMn5eB9MIOapQvzJghtQJQ4HQ8qGPo0db0LnKu2iyChMCV6tTVob3BTLNBtO9c8BuEC0lZVkbFjLbhmWUtKjrbFsIgf4GwsD9ym9QAQZChsQJTgP+X+204c+vlk5ebp/s6bDzoqagFh1DfK3LHs/wl4OuF/4XTUBoQbyStTKy3NH2q69slekbDTMMtO9IBfhP3v0yR8DxsOfWqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAa18ptjI=",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
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
    "channel_id": "ch_2qi2rA9TzmWp6nGV2gfoGpLT9UrNAQFdXZZ4fGbU3Nd9aW6N7C",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
