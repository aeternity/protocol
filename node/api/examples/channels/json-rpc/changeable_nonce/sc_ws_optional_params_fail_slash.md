
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
      "fsm_id": "ba_7kGS+fvvZTj6/xxyKAu7/B6744n1TdZoVxZ1XBg4KyYtxP9/"
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
      "fsm_id": "ba_cVazatb28cxd2lv3YfMnPIl+JlYq1ilt8MhiZkT6eD3Jq4oU"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBrfjAahs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422195,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEB/q2TfSFkB/8Xfi0YyZh/7mYxp3yTQVNW5wu8A0kyY+9VfltOpf84airmmsKHDw7rtsxpG0yV0JdsWoe88KqAFuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lga1FFbFw"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422195,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "fsm_id": "ba_cVazatb28cxd2lv3YfMnPIl+JlYq1ilt8MhiZkT6eD3Jq4oU",
      "signed_tx": "tx_+MwLAfhCuEB/q2TfSFkB/8Xfi0YyZh/7mYxp3yTQVNW5wu8A0kyY+9VfltOpf84airmmsKHDw7rtsxpG0yV0JdsWoe88KqAFuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lga1FFbFw",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422194,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAWXNVvRPqDTPN1NRHFmWeyYdXNBbZpUaok8sbwyQCb7STjZeVD1PvkN8k8UG8QhimROdkQbA2cULNUXJgqvm7DbhAf6tk30hZAf/F34tGMmYf+5mMad8k0FTVucLvANJMmPvVX5bTqX/OGoq5prChw8O67bMaRtMldCXbFqHvPCqgBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gt/DxOQg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422194,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAWXNVvRPqDTPN1NRHFmWeyYdXNBbZpUaok8sbwyQCb7STjZeVD1PvkN8k8UG8QhimROdkQbA2cULNUXJgqvm7DbhAf6tk30hZAf/F34tGMmYf+5mMad8k0FTVucLvANJMmPvVX5bTqX/OGoq5prChw8O67bMaRtMldCXbFqHvPCqgBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gt/DxOQg==",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_7kGS+fvvZTj6/xxyKAu7/B6744n1TdZoVxZ1XBg4KyYtxP9/"
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAWXNVvRPqDTPN1NRHFmWeyYdXNBbZpUaok8sbwyQCb7STjZeVD1PvkN8k8UG8QhimROdkQbA2cULNUXJgqvm7DbhAf6tk30hZAf/F34tGMmYf+5mMad8k0FTVucLvANJMmPvVX5bTqX/OGoq5prChw8O67bMaRtMldCXbFqHvPCqgBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gt/DxOQg==",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAWXNVvRPqDTPN1NRHFmWeyYdXNBbZpUaok8sbwyQCb7STjZeVD1PvkN8k8UG8QhimROdkQbA2cULNUXJgqvm7DbhAf6tk30hZAf/F34tGMmYf+5mMad8k0FTVucLvANJMmPvVX5bTqX/OGoq5prChw8O67bMaRtMldCXbFqHvPCqgBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gt/DxOQg==",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAWXNVvRPqDTPN1NRHFmWeyYdXNBbZpUaok8sbwyQCb7STjZeVD1PvkN8k8UG8QhimROdkQbA2cULNUXJgqvm7DbhAf6tk30hZAf/F34tGMmYf+5mMad8k0FTVucLvANJMmPvVX5bTqX/OGoq5prChw8O67bMaRtMldCXbFqHvPCqgBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gt/DxOQg==",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "message": {
        "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "message": {
        "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
  "id": -576460752303422193,
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
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422193,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+QEOCwH4hLhAWXNVvRPqDTPN1NRHFmWeyYdXNBbZpUaok8sbwyQCb7STjZeVD1PvkN8k8UG8QhimROdkQbA2cULNUXJgqvm7DbhAf6tk30hZAf/F34tGMmYf+5mMad8k0FTVucLvANJMmPvVX5bTqX/OGoq5prChw8O67bMaRtMldCXbFqHvPCqgBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gt/DxOQg=="
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+QEOCwH4hLhAWXNVvRPqDTPN1NRHFmWeyYdXNBbZpUaok8sbwyQCb7STjZeVD1PvkN8k8UG8QhimROdkQbA2cULNUXJgqvm7DbhAf6tk30hZAf/F34tGMmYf+5mMad8k0FTVucLvANJMmPvVX5bTqX/OGoq5prChw8O67bMaRtMldCXbFqHvPCqgBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gt/DxOQg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422192,
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
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422192,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtKw4xwsBQoHtCa68wgD3rfVj0dmZS2Jq9pKolVksz27AqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAuGJPow=",
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
  "id": -576460752303422191,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBV80opwVgrdO9R2+iGN27Wrl/MTc9nZRF2ff0SUiH526Phrrd/cIip8MVTvFljhYBZSMKHCcGcpd7tOyK8IzwNuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJng1Nn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422191,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBV80opwVgrdO9R2+iGN27Wrl/MTc9nZRF2ff0SUiH526Phrrd/cIip8MVTvFljhYBZSMKHCcGcpd7tOyK8IzwNuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJng1Nn",
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
  "id": -576460752303422190,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBV80opwVgrdO9R2+iGN27Wrl/MTc9nZRF2ff0SUiH526Phrrd/cIip8MVTvFljhYBZSMKHCcGcpd7tOyK8IzwNuEDYHd2yB9E1CAWNe9gsKICfnJuQQvUEMkRQZACyo7kq6QNoXCUf/y8u9Gy25CZVXw9CH8X0/S8DsDbVFLJbEcwFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIGUw+X"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422190,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+NILAfiEuEBV80opwVgrdO9R2+iGN27Wrl/MTc9nZRF2ff0SUiH526Phrrd/cIip8MVTvFljhYBZSMKHCcGcpd7tOyK8IzwNuEDYHd2yB9E1CAWNe9gsKICfnJuQQvUEMkRQZACyo7kq6QNoXCUf/y8u9Gy25CZVXw9CH8X0/S8DsDbVFLJbEcwFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIGUw+X"
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+NILAfiEuEBV80opwVgrdO9R2+iGN27Wrl/MTc9nZRF2ff0SUiH526Phrrd/cIip8MVTvFljhYBZSMKHCcGcpd7tOyK8IzwNuEDYHd2yB9E1CAWNe9gsKICfnJuQQvUEMkRQZACyo7kq6QNoXCUf/y8u9Gy25CZVXw9CH8X0/S8DsDbVFLJbEcwFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIGUw+X"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422189,
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
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422189,
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
  "id": -576460752303422188,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422188,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBV80opwVgrdO9R2+iGN27Wrl/MTc9nZRF2ff0SUiH526Phrrd/cIip8MVTvFljhYBZSMKHCcGcpd7tOyK8IzwNuEDYHd2yB9E1CAWNe9gsKICfnJuQQvUEMkRQZACyo7kq6QNoXCUf/y8u9Gy25CZVXw9CH8X0/S8DsDbVFLJbEcwFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIGUw+X",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422187,
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
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422187,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtKw4xwsBQoHtCa68wgD3rfVj0dmZS2Jq9pKolVksz27A6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2fmxqU=",
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
  "id": -576460752303422186,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC15GiBLZd8mY6WfNpG7JbFsmGLANX+EboRrgib54yX4ctfYDi+GcezLEVf9So1Q9Fhwi9DYj6L62EMjQDdQ2wFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguMiRUo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422186,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC15GiBLZd8mY6WfNpG7JbFsmGLANX+EboRrgib54yX4ctfYDi+GcezLEVf9So1Q9Fhwi9DYj6L62EMjQDdQ2wFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguMiRUo",
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
  "id": -576460752303422185,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECZ982FK4irjQ497uwMZnw6wwKFsuZVOYca0p60KT02h11SYZLpGQ9snYUMCtRQSgEV3x/qMEFI9wgeAkQTvo8PuEC15GiBLZd8mY6WfNpG7JbFsmGLANX+EboRrgib54yX4ctfYDi+GcezLEVf9So1Q9Fhwi9DYj6L62EMjQDdQ2wFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguxRNO0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422185,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+NILAfiEuECZ982FK4irjQ497uwMZnw6wwKFsuZVOYca0p60KT02h11SYZLpGQ9snYUMCtRQSgEV3x/qMEFI9wgeAkQTvo8PuEC15GiBLZd8mY6WfNpG7JbFsmGLANX+EboRrgib54yX4ctfYDi+GcezLEVf9So1Q9Fhwi9DYj6L62EMjQDdQ2wFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguxRNO0"
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+NILAfiEuECZ982FK4irjQ497uwMZnw6wwKFsuZVOYca0p60KT02h11SYZLpGQ9snYUMCtRQSgEV3x/qMEFI9wgeAkQTvo8PuEC15GiBLZd8mY6WfNpG7JbFsmGLANX+EboRrgib54yX4ctfYDi+GcezLEVf9So1Q9Fhwi9DYj6L62EMjQDdQ2wFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguxRNO0"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422184,
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
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422184,
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
  "id": -576460752303422183,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422183,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECZ982FK4irjQ497uwMZnw6wwKFsuZVOYca0p60KT02h11SYZLpGQ9snYUMCtRQSgEV3x/qMEFI9wgeAkQTvo8PuEC15GiBLZd8mY6WfNpG7JbFsmGLANX+EboRrgib54yX4ctfYDi+GcezLEVf9So1Q9Fhwi9DYj6L62EMjQDdQ2wFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguxRNO0",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422182,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422182,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECZ982FK4irjQ497uwMZnw6wwKFsuZVOYca0p60KT02h11SYZLpGQ9snYUMCtRQSgEV3x/qMEFI9wgeAkQTvo8PuEC15GiBLZd8mY6WfNpG7JbFsmGLANX+EboRrgib54yX4ctfYDi+GcezLEVf9So1Q9Fhwi9DYj6L62EMjQDdQ2wFuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguxRNO0",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422181,
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
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422181,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtKw4xwsBQoHtCa68wgD3rfVj0dmZS2Jq9pKolVksz27BKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeApSaZR4=",
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
  "id": -576460752303422180,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDRkW/XCNh63a185a8E5lXcOjwblSeTxrTJsowXKY0/DN5OZp7psJIxsU8/Ts3kaUBqXUsFYFloiA6YhC1qB7wHuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKmKszL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422180,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDRkW/XCNh63a185a8E5lXcOjwblSeTxrTJsowXKY0/DN5OZp7psJIxsU8/Ts3kaUBqXUsFYFloiA6YhC1qB7wHuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKmKszL",
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
  "id": -576460752303422179,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAzMbch1F/99ba4K9caRHLy9Cg1mzMqrjvi5KkOKQw94SbVnfiv5BQqmfSizQGVkIZ5+ExciFeIZrFCdfrm8uQNuEDRkW/XCNh63a185a8E5lXcOjwblSeTxrTJsowXKY0/DN5OZp7psJIxsU8/Ts3kaUBqXUsFYFloiA6YhC1qB7wHuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJL0dIN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422179,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+NILAfiEuEAzMbch1F/99ba4K9caRHLy9Cg1mzMqrjvi5KkOKQw94SbVnfiv5BQqmfSizQGVkIZ5+ExciFeIZrFCdfrm8uQNuEDRkW/XCNh63a185a8E5lXcOjwblSeTxrTJsowXKY0/DN5OZp7psJIxsU8/Ts3kaUBqXUsFYFloiA6YhC1qB7wHuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJL0dIN"
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+NILAfiEuEAzMbch1F/99ba4K9caRHLy9Cg1mzMqrjvi5KkOKQw94SbVnfiv5BQqmfSizQGVkIZ5+ExciFeIZrFCdfrm8uQNuEDRkW/XCNh63a185a8E5lXcOjwblSeTxrTJsowXKY0/DN5OZp7psJIxsU8/Ts3kaUBqXUsFYFloiA6YhC1qB7wHuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJL0dIN"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422178,
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
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422178,
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
  "id": -576460752303422177,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422177,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAzMbch1F/99ba4K9caRHLy9Cg1mzMqrjvi5KkOKQw94SbVnfiv5BQqmfSizQGVkIZ5+ExciFeIZrFCdfrm8uQNuEDRkW/XCNh63a185a8E5lXcOjwblSeTxrTJsowXKY0/DN5OZp7psJIxsU8/Ts3kaUBqXUsFYFloiA6YhC1qB7wHuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJL0dIN",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422176,
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
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422176,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtKw4xwsBQoHtCa68wgD3rfVj0dmZS2Jq9pKolVksz27BaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCw7q0DA=",
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
  "id": -576460752303422175,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsMdagd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422175,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+JALAfhCuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsMdagd",
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
  "id": -576460752303422174,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEDkhZOZiaCdL8L7+pqEfC6yc1fV9ljQlmkNJYHe0UdrR3q/Bymrh8aKfN1kuZVHoDA2A0/D9PXkp2jCIeBwdvEGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvBRRo6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422174,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+NILAfiEuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEDkhZOZiaCdL8L7+pqEfC6yc1fV9ljQlmkNJYHe0UdrR3q/Bymrh8aKfN1kuZVHoDA2A0/D9PXkp2jCIeBwdvEGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvBRRo6"
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "state": "tx_+NILAfiEuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEDkhZOZiaCdL8L7+pqEfC6yc1fV9ljQlmkNJYHe0UdrR3q/Bymrh8aKfN1kuZVHoDA2A0/D9PXkp2jCIeBwdvEGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvBRRo6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422173,
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
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422173,
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
  "id": -576460752303422172,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422172,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEDkhZOZiaCdL8L7+pqEfC6yc1fV9ljQlmkNJYHe0UdrR3q/Bymrh8aKfN1kuZVHoDA2A0/D9PXkp2jCIeBwdvEGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvBRRo6",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEDkhZOZiaCdL8L7+pqEfC6yc1fV9ljQlmkNJYHe0UdrR3q/Bymrh8aKfN1kuZVHoDA2A0/D9PXkp2jCIeBwdvEGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvBRRo6",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEDkhZOZiaCdL8L7+pqEfC6yc1fV9ljQlmkNJYHe0UdrR3q/Bymrh8aKfN1kuZVHoDA2A0/D9PXkp2jCIeBwdvEGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvBRRo6",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
  "method": "channels.slash",
  "params": {
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+QKACwHAuQJ6+QJ3NwGhBtKw4xwsBQoHtCa68wgD3rfVj0dmZS2Jq9pKolVksz27oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEDkhZOZiaCdL8L7+pqEfC6yc1fV9ljQlmkNJYHe0UdrR3q/Bymrh8aKfN1kuZVHoDA2A0/D9PXkp2jCIeBwdvEGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGSzAkUAAgxLWh7x+Wfk=",
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
  "method": "channels.slash_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422171,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
  "id": -576460752303422171,
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBtKw4xwsBQoHtCa68wgD3rfVj0dmZS2Jq9pKolVksz27oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuECYGoPv816y24HmSWRaDo+lohb7FAV1wr36oMhFYpChfHyqDmIJebYE9Yp/3+KTW0x5QWPbNqRVg68IOkwEWToGuEDkhZOZiaCdL8L7+pqEfC6yc1fV9ljQlmkNJYHe0UdrR3q/Bymrh8aKfN1kuZVHoDA2A0/D9PXkp2jCIeBwdvEGuEj4RjkCoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9uwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGSNwYbAAga/Gh2uh",
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
    "signed_tx": "tx_+QLBCwH4QrhALUIQ+MiYQm5hOKloT38wB2b8I5yj/iXGlZtQG11zwDiVu4XGUbhcEBXsRPFYw1UcTReilaxfWO+H8m/oroFOA7kCePkCdTcBoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9u6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAmBqD7/NestuB5klkWg6PpaIW+xQFdcK9+qDIRWKQoXx8qg5iCXm2BPWKf9/ik1tMeUFj2zakVYOvCDpMBFk6BrhA5IWTmYmgnS/C+/qahHwusnNX1fZY0JZpDSWB3tFHa0d6vwcpq4fGinzdZLmVR6AwNgNPw/T15KdowiHgcHbxBrhI+EY5AqEG0rDjHCwFCge0JrrzCAPet9WPR2ZlLYmr2kqiVWSzPbsFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIGv0xhERA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhALUIQ+MiYQm5hOKloT38wB2b8I5yj/iXGlZtQG11zwDiVu4XGUbhcEBXsRPFYw1UcTReilaxfWO+H8m/oroFOA7kCePkCdTcBoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9u6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAmBqD7/NestuB5klkWg6PpaIW+xQFdcK9+qDIRWKQoXx8qg5iCXm2BPWKf9/ik1tMeUFj2zakVYOvCDpMBFk6BrhA5IWTmYmgnS/C+/qahHwusnNX1fZY0JZpDSWB3tFHa0d6vwcpq4fGinzdZLmVR6AwNgNPw/T15KdowiHgcHbxBrhI+EY5AqEG0rDjHCwFCge0JrrzCAPet9WPR2ZlLYmr2kqiVWSzPbsFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIGv0xhERA==",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhALUIQ+MiYQm5hOKloT38wB2b8I5yj/iXGlZtQG11zwDiVu4XGUbhcEBXsRPFYw1UcTReilaxfWO+H8m/oroFOA7kCePkCdTcBoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9u6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAmBqD7/NestuB5klkWg6PpaIW+xQFdcK9+qDIRWKQoXx8qg5iCXm2BPWKf9/ik1tMeUFj2zakVYOvCDpMBFk6BrhA5IWTmYmgnS/C+/qahHwusnNX1fZY0JZpDSWB3tFHa0d6vwcpq4fGinzdZLmVR6AwNgNPw/T15KdowiHgcHbxBrhI+EY5AqEG0rDjHCwFCge0JrrzCAPet9WPR2ZlLYmr2kqiVWSzPbsFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIGv0xhERA==",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBtKw4xwsBQoHtCa68wgD3rfVj0dmZS2Jq9pKolVksz27oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAA/eBVxXw==",
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
    "signed_tx": "tx_+KcLAfhCuEAY7jxy1gRWnf9Zidkt1fQQJhMXW1pX9n3AkkhXFEn20y4F6S8tHi1d7z7KL1z/v7rzRJDxfVSSkIZM35W1+v4LuF/4XTgBoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9u6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAP9bYaac="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAY7jxy1gRWnf9Zidkt1fQQJhMXW1pX9n3AkkhXFEn20y4F6S8tHi1d7z7KL1z/v7rzRJDxfVSSkIZM35W1+v4LuF/4XTgBoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9u6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAP9bYaac=",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAY7jxy1gRWnf9Zidkt1fQQJhMXW1pX9n3AkkhXFEn20y4F6S8tHi1d7z7KL1z/v7rzRJDxfVSSkIZM35W1+v4LuF/4XTgBoQbSsOMcLAUKB7QmuvMIA9631Y9HZmUtiavaSqJVZLM9u6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAP9bYaac=",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
    "channel_id": "ch_2bnpSXrQbTHRZQDJBeXmikrZjSNJamnrofH8z3NutmtLAFr4bp",
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
      "fsm_id": "ba_qw3/YMFhMrEIc/lNRJUxVtg8fTgow7TKXRZLMv0IUYAPj70U"
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
      "fsm_id": "ba_bTcNu/mbkODv+K4JgW/X8fspT5pZa8E4catOl0nOyLnVrx1u"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBsKY679U=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422170,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuED2xKhYZGFrJ9gahzAZUI+CVJMAgmpj4zg0TK0qyua0gRafwP37Om5spryy9m+TPGBZh4Z/klqlABXVKFpqDGINuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbDG3yWn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422170,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "fsm_id": "ba_bTcNu/mbkODv+K4JgW/X8fspT5pZa8E4catOl0nOyLnVrx1u",
      "signed_tx": "tx_+MwLAfhCuED2xKhYZGFrJ9gahzAZUI+CVJMAgmpj4zg0TK0qyua0gRafwP37Om5spryy9m+TPGBZh4Z/klqlABXVKFpqDGINuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbDG3yWn",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422169,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhARI1IBYF+PtqjZ41shDOnh4PsLRuveIOE4j/oX6R5Rvo5Vw8MnzbtLM5ZR28M664j4P71sYsHM+0alwJwbHH8DbhA9sSoWGRhayfYGocwGVCPglSTAIJqY+M4NEytKsrmtIEWn8D9+zpubKa8svZvkzxgWYeGf5JapQAV1ShaagxiDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GwfZG0zA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422169,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhARI1IBYF+PtqjZ41shDOnh4PsLRuveIOE4j/oX6R5Rvo5Vw8MnzbtLM5ZR28M664j4P71sYsHM+0alwJwbHH8DbhA9sSoWGRhayfYGocwGVCPglSTAIJqY+M4NEytKsrmtIEWn8D9+zpubKa8svZvkzxgWYeGf5JapQAV1ShaagxiDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GwfZG0zA==",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_qw3/YMFhMrEIc/lNRJUxVtg8fTgow7TKXRZLMv0IUYAPj70U"
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhARI1IBYF+PtqjZ41shDOnh4PsLRuveIOE4j/oX6R5Rvo5Vw8MnzbtLM5ZR28M664j4P71sYsHM+0alwJwbHH8DbhA9sSoWGRhayfYGocwGVCPglSTAIJqY+M4NEytKsrmtIEWn8D9+zpubKa8svZvkzxgWYeGf5JapQAV1ShaagxiDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GwfZG0zA==",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhARI1IBYF+PtqjZ41shDOnh4PsLRuveIOE4j/oX6R5Rvo5Vw8MnzbtLM5ZR28M664j4P71sYsHM+0alwJwbHH8DbhA9sSoWGRhayfYGocwGVCPglSTAIJqY+M4NEytKsrmtIEWn8D9+zpubKa8svZvkzxgWYeGf5JapQAV1ShaagxiDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GwfZG0zA==",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhARI1IBYF+PtqjZ41shDOnh4PsLRuveIOE4j/oX6R5Rvo5Vw8MnzbtLM5ZR28M664j4P71sYsHM+0alwJwbHH8DbhA9sSoWGRhayfYGocwGVCPglSTAIJqY+M4NEytKsrmtIEWn8D9+zpubKa8svZvkzxgWYeGf5JapQAV1ShaagxiDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GwfZG0zA==",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "message": {
        "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "message": {
        "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
  "id": -576460752303422168,
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
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422168,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+QEOCwH4hLhARI1IBYF+PtqjZ41shDOnh4PsLRuveIOE4j/oX6R5Rvo5Vw8MnzbtLM5ZR28M664j4P71sYsHM+0alwJwbHH8DbhA9sSoWGRhayfYGocwGVCPglSTAIJqY+M4NEytKsrmtIEWn8D9+zpubKa8svZvkzxgWYeGf5JapQAV1ShaagxiDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GwfZG0zA=="
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+QEOCwH4hLhARI1IBYF+PtqjZ41shDOnh4PsLRuveIOE4j/oX6R5Rvo5Vw8MnzbtLM5ZR28M664j4P71sYsHM+0alwJwbHH8DbhA9sSoWGRhayfYGocwGVCPglSTAIJqY+M4NEytKsrmtIEWn8D9+zpubKa8svZvkzxgWYeGf5JapQAV1ShaagxiDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GwfZG0zA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422167,
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
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422167,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt1qUAR8eIJ7VTcKjT2y59wXwN7g5Yb9WHjlQyaaqaPjAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAm1lw0U=",
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
  "id": -576460752303422166,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED/AVeDItVe8SNi7RyCxqr11zkJWL6GXjJLIaV+jNjCDhDR2L9ztsYvdBVrHU/ocE8hq/sbLWZJwGzGFw7+T4IHuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJKEyVr"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422166,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+JALAfhCuED/AVeDItVe8SNi7RyCxqr11zkJWL6GXjJLIaV+jNjCDhDR2L9ztsYvdBVrHU/ocE8hq/sbLWZJwGzGFw7+T4IHuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJKEyVr",
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
  "id": -576460752303422165,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBRXmhC1J/lgUSrkTUnsb/UIaMNOqYeSFFEJjesoaB5tDwfHo2KZbc3eC4SHZRAyhfhQotq3G3rONA00Xf5VvkPuED/AVeDItVe8SNi7RyCxqr11zkJWL6GXjJLIaV+jNjCDhDR2L9ztsYvdBVrHU/ocE8hq/sbLWZJwGzGFw7+T4IHuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLeoIt/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422165,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+NILAfiEuEBRXmhC1J/lgUSrkTUnsb/UIaMNOqYeSFFEJjesoaB5tDwfHo2KZbc3eC4SHZRAyhfhQotq3G3rONA00Xf5VvkPuED/AVeDItVe8SNi7RyCxqr11zkJWL6GXjJLIaV+jNjCDhDR2L9ztsYvdBVrHU/ocE8hq/sbLWZJwGzGFw7+T4IHuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLeoIt/"
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+NILAfiEuEBRXmhC1J/lgUSrkTUnsb/UIaMNOqYeSFFEJjesoaB5tDwfHo2KZbc3eC4SHZRAyhfhQotq3G3rONA00Xf5VvkPuED/AVeDItVe8SNi7RyCxqr11zkJWL6GXjJLIaV+jNjCDhDR2L9ztsYvdBVrHU/ocE8hq/sbLWZJwGzGFw7+T4IHuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLeoIt/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422164,
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
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422164,
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
  "id": -576460752303422163,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422163,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBRXmhC1J/lgUSrkTUnsb/UIaMNOqYeSFFEJjesoaB5tDwfHo2KZbc3eC4SHZRAyhfhQotq3G3rONA00Xf5VvkPuED/AVeDItVe8SNi7RyCxqr11zkJWL6GXjJLIaV+jNjCDhDR2L9ztsYvdBVrHU/ocE8hq/sbLWZJwGzGFw7+T4IHuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLeoIt/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422162,
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
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422162,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt1qUAR8eIJ7VTcKjT2y59wXwN7g5Yb9WHjlQyaaqaPjA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3Dm5eg=",
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
  "id": -576460752303422161,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDo7ss020pLvlvArUfy6qTu6VSS8D3zaqB8J/Ywv2ItPUOakGUjj08HHJZzAULqIXGQXv35j68zH7IKRBxJclwLuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsPt0bO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422161,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDo7ss020pLvlvArUfy6qTu6VSS8D3zaqB8J/Ywv2ItPUOakGUjj08HHJZzAULqIXGQXv35j68zH7IKRBxJclwLuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsPt0bO",
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
  "id": -576460752303422160,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBUUK7LFTYsu/l3ET8fea0HhvIlfWvTd5vB9ZyQLhSa+h2l8ZQCFS9R+kr0qmAT2+QcNnU7vla1E3gSB1GpF48PuEDo7ss020pLvlvArUfy6qTu6VSS8D3zaqB8J/Ywv2ItPUOakGUjj08HHJZzAULqIXGQXv35j68zH7IKRBxJclwLuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvxkYpD"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422160,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+NILAfiEuEBUUK7LFTYsu/l3ET8fea0HhvIlfWvTd5vB9ZyQLhSa+h2l8ZQCFS9R+kr0qmAT2+QcNnU7vla1E3gSB1GpF48PuEDo7ss020pLvlvArUfy6qTu6VSS8D3zaqB8J/Ywv2ItPUOakGUjj08HHJZzAULqIXGQXv35j68zH7IKRBxJclwLuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvxkYpD"
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+NILAfiEuEBUUK7LFTYsu/l3ET8fea0HhvIlfWvTd5vB9ZyQLhSa+h2l8ZQCFS9R+kr0qmAT2+QcNnU7vla1E3gSB1GpF48PuEDo7ss020pLvlvArUfy6qTu6VSS8D3zaqB8J/Ywv2ItPUOakGUjj08HHJZzAULqIXGQXv35j68zH7IKRBxJclwLuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvxkYpD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422159,
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
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422159,
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
  "id": -576460752303422158,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422158,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBUUK7LFTYsu/l3ET8fea0HhvIlfWvTd5vB9ZyQLhSa+h2l8ZQCFS9R+kr0qmAT2+QcNnU7vla1E3gSB1GpF48PuEDo7ss020pLvlvArUfy6qTu6VSS8D3zaqB8J/Ywv2ItPUOakGUjj08HHJZzAULqIXGQXv35j68zH7IKRBxJclwLuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvxkYpD",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422157,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422157,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBUUK7LFTYsu/l3ET8fea0HhvIlfWvTd5vB9ZyQLhSa+h2l8ZQCFS9R+kr0qmAT2+QcNnU7vla1E3gSB1GpF48PuEDo7ss020pLvlvArUfy6qTu6VSS8D3zaqB8J/Ywv2ItPUOakGUjj08HHJZzAULqIXGQXv35j68zH7IKRBxJclwLuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvxkYpD",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422156,
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
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422156,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt1qUAR8eIJ7VTcKjT2y59wXwN7g5Yb9WHjlQyaaqaPjBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeArwPXkU=",
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
  "id": -576460752303422155,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDrt55RfAUl6rAclAZWc/yLyu13rdEAP5iygJsDdrxd8U1r++wFwzy99XdQQGmDoE9Fmg4NEuwQ9VIElToabywGuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKiGrEf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422155,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDrt55RfAUl6rAclAZWc/yLyu13rdEAP5iygJsDdrxd8U1r++wFwzy99XdQQGmDoE9Fmg4NEuwQ9VIElToabywGuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKiGrEf",
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
  "id": -576460752303422154,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBHWTx2Wl6tL7uUMsbsSE9+GLz0WuQLLx8SBVUVBXY++9itYXH7FdAbf+S4m/TKWMx8HzXDbdNwWsmZ+5BP57wHuEDrt55RfAUl6rAclAZWc/yLyu13rdEAP5iygJsDdrxd8U1r++wFwzy99XdQQGmDoE9Fmg4NEuwQ9VIElToabywGuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIYA3EM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422154,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+NILAfiEuEBHWTx2Wl6tL7uUMsbsSE9+GLz0WuQLLx8SBVUVBXY++9itYXH7FdAbf+S4m/TKWMx8HzXDbdNwWsmZ+5BP57wHuEDrt55RfAUl6rAclAZWc/yLyu13rdEAP5iygJsDdrxd8U1r++wFwzy99XdQQGmDoE9Fmg4NEuwQ9VIElToabywGuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIYA3EM"
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+NILAfiEuEBHWTx2Wl6tL7uUMsbsSE9+GLz0WuQLLx8SBVUVBXY++9itYXH7FdAbf+S4m/TKWMx8HzXDbdNwWsmZ+5BP57wHuEDrt55RfAUl6rAclAZWc/yLyu13rdEAP5iygJsDdrxd8U1r++wFwzy99XdQQGmDoE9Fmg4NEuwQ9VIElToabywGuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIYA3EM"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422153,
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
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422153,
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
  "id": -576460752303422152,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422152,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBHWTx2Wl6tL7uUMsbsSE9+GLz0WuQLLx8SBVUVBXY++9itYXH7FdAbf+S4m/TKWMx8HzXDbdNwWsmZ+5BP57wHuEDrt55RfAUl6rAclAZWc/yLyu13rdEAP5iygJsDdrxd8U1r++wFwzy99XdQQGmDoE9Fmg4NEuwQ9VIElToabywGuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIYA3EM",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422151,
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
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422151,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBt1qUAR8eIJ7VTcKjT2y59wXwN7g5Yb9WHjlQyaaqaPjBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC64nX+c=",
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
  "id": -576460752303422150,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvIgVCV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422150,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvIgVCV",
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
  "id": -576460752303422149,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBezTqXp09RoRrlEn6HZ3qpskeOI9WpxJckX3/lx15YlHUJN/u8m+V1yF11kWRROqS9iXXQaZqMZcURQGjbHIIKuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtIBM6D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422149,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+NILAfiEuEBezTqXp09RoRrlEn6HZ3qpskeOI9WpxJckX3/lx15YlHUJN/u8m+V1yF11kWRROqS9iXXQaZqMZcURQGjbHIIKuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtIBM6D"
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "state": "tx_+NILAfiEuEBezTqXp09RoRrlEn6HZ3qpskeOI9WpxJckX3/lx15YlHUJN/u8m+V1yF11kWRROqS9iXXQaZqMZcURQGjbHIIKuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtIBM6D"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422148,
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
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422148,
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
  "id": -576460752303422147,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422147,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBezTqXp09RoRrlEn6HZ3qpskeOI9WpxJckX3/lx15YlHUJN/u8m+V1yF11kWRROqS9iXXQaZqMZcURQGjbHIIKuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtIBM6D",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBezTqXp09RoRrlEn6HZ3qpskeOI9WpxJckX3/lx15YlHUJN/u8m+V1yF11kWRROqS9iXXQaZqMZcURQGjbHIIKuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtIBM6D",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBezTqXp09RoRrlEn6HZ3qpskeOI9WpxJckX3/lx15YlHUJN/u8m+V1yF11kWRROqS9iXXQaZqMZcURQGjbHIIKuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtIBM6D",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
  "method": "channels.slash",
  "params": {
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+QKACwHAuQJ6+QJ3NwGhBt1qUAR8eIJ7VTcKjT2y59wXwN7g5Yb9WHjlQyaaqaPjoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEBezTqXp09RoRrlEn6HZ3qpskeOI9WpxJckX3/lx15YlHUJN/u8m+V1yF11kWRROqS9iXXQaZqMZcURQGjbHIIKuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGSzAkUAAgxLWh+iQH0c=",
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
  "method": "channels.slash_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422146,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
  "id": -576460752303422146,
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBt1qUAR8eIJ7VTcKjT2y59wXwN7g5Yb9WHjlQyaaqaPjoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEBezTqXp09RoRrlEn6HZ3qpskeOI9WpxJckX3/lx15YlHUJN/u8m+V1yF11kWRROqS9iXXQaZqMZcURQGjbHIIKuEDMOk+ipBo6Eq3h6UOqeU+1Ke1ErfuRp2J2s2oH3vHhjTXcWs3OUUO7+jMFtAvt2ozzrwC1/oDfkbnmnvpPGC4KuEj4RjkCoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj4wWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGSNwYbAAgbLyP+pq",
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
    "signed_tx": "tx_+QLBCwH4QrhAr/J2XZeRViUAcLmF5bXarEYkLHbpfKUlA39jC9JywMtainORwrBo5sf61uoqVVbh/RRwEK0nj3McSzBosxQZBLkCePkCdTcBoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj46EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAXs06l6dPUaEa5RJ+h2d6qbJHjiPVqcSXJF9/5cdeWJR1CTf7vJvldchddZFkUTqkvYl10GmajGXFEUBo2xyCCrhAzDpPoqQaOhKt4elDqnlPtSntRK37kadidrNqB97x4Y013FrNzlFDu/ozBbQL7dqM868Atf6A35G55p76TxguCrhI+EY5AqEG3WpQBHx4gntVNwqNPbLn3BfA3uDlhv1YeOVDJpqpo+MFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIGyRdFORA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAr/J2XZeRViUAcLmF5bXarEYkLHbpfKUlA39jC9JywMtainORwrBo5sf61uoqVVbh/RRwEK0nj3McSzBosxQZBLkCePkCdTcBoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj46EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAXs06l6dPUaEa5RJ+h2d6qbJHjiPVqcSXJF9/5cdeWJR1CTf7vJvldchddZFkUTqkvYl10GmajGXFEUBo2xyCCrhAzDpPoqQaOhKt4elDqnlPtSntRK37kadidrNqB97x4Y013FrNzlFDu/ozBbQL7dqM868Atf6A35G55p76TxguCrhI+EY5AqEG3WpQBHx4gntVNwqNPbLn3BfA3uDlhv1YeOVDJpqpo+MFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIGyRdFORA==",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAr/J2XZeRViUAcLmF5bXarEYkLHbpfKUlA39jC9JywMtainORwrBo5sf61uoqVVbh/RRwEK0nj3McSzBosxQZBLkCePkCdTcBoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj46EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAXs06l6dPUaEa5RJ+h2d6qbJHjiPVqcSXJF9/5cdeWJR1CTf7vJvldchddZFkUTqkvYl10GmajGXFEUBo2xyCCrhAzDpPoqQaOhKt4elDqnlPtSntRK37kadidrNqB97x4Y013FrNzlFDu/ozBbQL7dqM868Atf6A35G55p76TxguCrhI+EY5AqEG3WpQBHx4gntVNwqNPbLn3BfA3uDlhv1YeOVDJpqpo+MFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIGyRdFORA==",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBt1qUAR8eIJ7VTcKjT2y59wXwN7g5Yb9WHjlQyaaqaPjoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KABAbqJl4A==",
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
    "signed_tx": "tx_+KcLAfhCuEDWd44pVfzDGbf1OYHytOlTU3Ernik683nzT1NHnclVonJ2rxLuXaNq/Nw1OyGV+4wIZOUDDjPzzZgc+5cQYh0IuF/4XTgBoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj46EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAQMDvx8A="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDWd44pVfzDGbf1OYHytOlTU3Ernik683nzT1NHnclVonJ2rxLuXaNq/Nw1OyGV+4wIZOUDDjPzzZgc+5cQYh0IuF/4XTgBoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj46EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAQMDvx8A=",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDWd44pVfzDGbf1OYHytOlTU3Ernik683nzT1NHnclVonJ2rxLuXaNq/Nw1OyGV+4wIZOUDDjPzzZgc+5cQYh0IuF/4XTgBoQbdalAEfHiCe1U3Co09sufcF8De4OWG/Vh45UMmmqmj46EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAQMDvx8A=",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
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
    "channel_id": "ch_2gWks1aLSzarFxrWcBajts7HLp4C6qdMemv6WJt8nR6aLmhw31",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
