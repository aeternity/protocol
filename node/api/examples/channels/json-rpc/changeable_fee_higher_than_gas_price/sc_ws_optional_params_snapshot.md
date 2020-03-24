
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
      "fsm_id": "ba_yGhBs0MUNKf3P7/fxp4ysQMHfyAjrzKHZGaBku0exsJN2ApZ"
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
      "fsm_id": "ba_4cHgqoolxL0UGbTUx5UFiCqK+3IZEibzXLkRhZs+Gg5EjyGg"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtvx+4/7g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422472,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBnHEnfxr9lN33yIakVO48rXEkSiIVMcvESoFfCXr6bZJRKohzAV+PG/xR6fUv/osUdG1dkQoIGINLkWLHwGvgJuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lb/sCewI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422472,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "fsm_id": "ba_4cHgqoolxL0UGbTUx5UFiCqK+3IZEibzXLkRhZs+Gg5EjyGg",
      "signed_tx": "tx_+MsLAfhCuEBnHEnfxr9lN33yIakVO48rXEkSiIVMcvESoFfCXr6bZJRKohzAV+PG/xR6fUv/osUdG1dkQoIGINLkWLHwGvgJuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lb/sCewI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422471,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhASRQW0HK533smmB4UoCsXidqTuq6rTQTSCrVfwC9H1Ve2+BnzlXUMqenSi5aoIJdQ+QGIxVxggpnNKYnZ4tCoA7hAZxxJ38a/ZTd98iGpFTuPK1xJEoiFTHLxEqBXwl6+m2SUSqIcwFfjxv8Uen1L/6LFHRtXZEKCBiDS5Fix8Br4CbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC294pKuE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422471,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhASRQW0HK533smmB4UoCsXidqTuq6rTQTSCrVfwC9H1Ve2+BnzlXUMqenSi5aoIJdQ+QGIxVxggpnNKYnZ4tCoA7hAZxxJ38a/ZTd98iGpFTuPK1xJEoiFTHLxEqBXwl6+m2SUSqIcwFfjxv8Uen1L/6LFHRtXZEKCBiDS5Fix8Br4CbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC294pKuE",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_yGhBs0MUNKf3P7/fxp4ysQMHfyAjrzKHZGaBku0exsJN2ApZ"
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhASRQW0HK533smmB4UoCsXidqTuq6rTQTSCrVfwC9H1Ve2+BnzlXUMqenSi5aoIJdQ+QGIxVxggpnNKYnZ4tCoA7hAZxxJ38a/ZTd98iGpFTuPK1xJEoiFTHLxEqBXwl6+m2SUSqIcwFfjxv8Uen1L/6LFHRtXZEKCBiDS5Fix8Br4CbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC294pKuE",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhASRQW0HK533smmB4UoCsXidqTuq6rTQTSCrVfwC9H1Ve2+BnzlXUMqenSi5aoIJdQ+QGIxVxggpnNKYnZ4tCoA7hAZxxJ38a/ZTd98iGpFTuPK1xJEoiFTHLxEqBXwl6+m2SUSqIcwFfjxv8Uen1L/6LFHRtXZEKCBiDS5Fix8Br4CbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC294pKuE",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhASRQW0HK533smmB4UoCsXidqTuq6rTQTSCrVfwC9H1Ve2+BnzlXUMqenSi5aoIJdQ+QGIxVxggpnNKYnZ4tCoA7hAZxxJ38a/ZTd98iGpFTuPK1xJEoiFTHLxEqBXwl6+m2SUSqIcwFfjxv8Uen1L/6LFHRtXZEKCBiDS5Fix8Br4CbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC294pKuE",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "message": {
        "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "message": {
        "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
  "id": -576460752303422470,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422470,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+QENCwH4hLhASRQW0HK533smmB4UoCsXidqTuq6rTQTSCrVfwC9H1Ve2+BnzlXUMqenSi5aoIJdQ+QGIxVxggpnNKYnZ4tCoA7hAZxxJ38a/ZTd98iGpFTuPK1xJEoiFTHLxEqBXwl6+m2SUSqIcwFfjxv8Uen1L/6LFHRtXZEKCBiDS5Fix8Br4CbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC294pKuE"
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+QENCwH4hLhASRQW0HK533smmB4UoCsXidqTuq6rTQTSCrVfwC9H1Ve2+BnzlXUMqenSi5aoIJdQ+QGIxVxggpnNKYnZ4tCoA7hAZxxJ38a/ZTd98iGpFTuPK1xJEoiFTHLxEqBXwl6+m2SUSqIcwFfjxv8Uen1L/6LFHRtXZEKCBiDS5Fix8Br4CbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC294pKuE"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422469,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422469,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QENCwH4hLhASRQW0HK533smmB4UoCsXidqTuq6rTQTSCrVfwC9H1Ve2+BnzlXUMqenSi5aoIJdQ+QGIxVxggpnNKYnZ4tCoA7hAZxxJ38a/ZTd98iGpFTuPK1xJEoiFTHLxEqBXwl6+m2SUSqIcwFfjxv8Uen1L/6LFHRtXZEKCBiDS5Fix8Br4CbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC294pKuE",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422468,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422468,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvjuR+FgyrnwSPg93+NRhwOgkbAKHhT/a+YxX7w7l8gzAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAr3SVno=",
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
  "id": -576460752303422467,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAeo+1nF4+3kvyJOhT3OlFZlm/cgXDx8HzsdJZ1PmpwCvnZepN/s+qS6UuxPBEf2PkvmHONpZCe4A9ylZH/KWQFuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLLvaFa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422467,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAeo+1nF4+3kvyJOhT3OlFZlm/cgXDx8HzsdJZ1PmpwCvnZepN/s+qS6UuxPBEf2PkvmHONpZCe4A9ylZH/KWQFuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLLvaFa",
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
  "id": -576460752303422466,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAeo+1nF4+3kvyJOhT3OlFZlm/cgXDx8HzsdJZ1PmpwCvnZepN/s+qS6UuxPBEf2PkvmHONpZCe4A9ylZH/KWQFuEAn0Odhu5/Beh1+XcxQcsHr8glcFNbgu713AHIlL2KW+yzsHgA0g1VIKZuBb6WcDRa0LOYJf4ECzd2pPswQhosCuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL1xoCV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422466,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEAeo+1nF4+3kvyJOhT3OlFZlm/cgXDx8HzsdJZ1PmpwCvnZepN/s+qS6UuxPBEf2PkvmHONpZCe4A9ylZH/KWQFuEAn0Odhu5/Beh1+XcxQcsHr8glcFNbgu713AHIlL2KW+yzsHgA0g1VIKZuBb6WcDRa0LOYJf4ECzd2pPswQhosCuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL1xoCV"
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEAeo+1nF4+3kvyJOhT3OlFZlm/cgXDx8HzsdJZ1PmpwCvnZepN/s+qS6UuxPBEf2PkvmHONpZCe4A9ylZH/KWQFuEAn0Odhu5/Beh1+XcxQcsHr8glcFNbgu713AHIlL2KW+yzsHgA0g1VIKZuBb6WcDRa0LOYJf4ECzd2pPswQhosCuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL1xoCV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422465,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422465,
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
  "id": -576460752303422464,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422464,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAeo+1nF4+3kvyJOhT3OlFZlm/cgXDx8HzsdJZ1PmpwCvnZepN/s+qS6UuxPBEf2PkvmHONpZCe4A9ylZH/KWQFuEAn0Odhu5/Beh1+XcxQcsHr8glcFNbgu713AHIlL2KW+yzsHgA0g1VIKZuBb6WcDRa0LOYJf4ECzd2pPswQhosCuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL1xoCV",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422463,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422463,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBvjuR+FgyrnwSPg93+NRhwOgkbAKHhT/a+YxX7w7l8gzoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAeo+1nF4+3kvyJOhT3OlFZlm/cgXDx8HzsdJZ1PmpwCvnZepN/s+qS6UuxPBEf2PkvmHONpZCe4A9ylZH/KWQFuEAn0Odhu5/Beh1+XcxQcsHr8glcFNbgu713AHIlL2KW+yzsHgA0g1VIKZuBb6WcDRa0LOYJf4ECzd2pPswQhosCuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIAhuCRDDYefnDfGX5L",
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
    "signed_tx": "tx_+QFxCwH4QrhADYVrPxyQgnuEVdednMxR/K27YoU/qklqRVfIEEuQ0dLiqM2lrtPj+I3R9wHucLAHH/nezCc1Adhu70WrFUyXALkBKPkBJTsBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAHqPtZxePt5L8iToU9zpRWZZv3IFw8fB87HSWdT5qcAr52XqTf7PqkulLsTwRH9j5L5hzjaWQnuAPcpWR/ylkBbhAJ9DnYbufwXodfl3MUHLB6/IJXBTW4Lu9dwByJS9ilvss7B4ANINVSCmbgW+lnA0WtCzmCX+BAs3dqT7MEIaLArhI+EY5AqEG+O5H4WDKufBI+D3f41GHA6CRsAoeFP9r5jFfvDuXyDMCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIbgkQw2Hn5wno9Mhw=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422462,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422462,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvjuR+FgyrnwSPg93+NRhwOgkbAKHhT/a+YxX7w7l8gzA6Ah5YXSCzjC3C5f2KaHrz5Qp6zPFnxOBCDOm/SZojmZpU0z6G8=",
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
  "id": -576460752303422461,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBc7OrO9Nv3eSxmxFH2SzkqE+7PkjDxSKjZKKszH1RfE4tw3cXhwfKqq66VxJuy2pF86rHrrtSxPkUbBDP9EnYOuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maV4lgGt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422461,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBc7OrO9Nv3eSxmxFH2SzkqE+7PkjDxSKjZKKszH1RfE4tw3cXhwfKqq66VxJuy2pF86rHrrtSxPkUbBDP9EnYOuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maV4lgGt",
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
  "id": -576460752303422460,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAWWpxNT21GCarIKyC+UoHYlL9rvnZRdyhSPOx223EwPpjhujOh/9YwbdS/oqB2hEWr+LTqhj/blpLF/zNw4CsGuEBc7OrO9Nv3eSxmxFH2SzkqE+7PkjDxSKjZKKszH1RfE4tw3cXhwfKqq66VxJuy2pF86rHrrtSxPkUbBDP9EnYOuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maWY/PpD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422460,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEAWWpxNT21GCarIKyC+UoHYlL9rvnZRdyhSPOx223EwPpjhujOh/9YwbdS/oqB2hEWr+LTqhj/blpLF/zNw4CsGuEBc7OrO9Nv3eSxmxFH2SzkqE+7PkjDxSKjZKKszH1RfE4tw3cXhwfKqq66VxJuy2pF86rHrrtSxPkUbBDP9EnYOuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maWY/PpD"
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEAWWpxNT21GCarIKyC+UoHYlL9rvnZRdyhSPOx223EwPpjhujOh/9YwbdS/oqB2hEWr+LTqhj/blpLF/zNw4CsGuEBc7OrO9Nv3eSxmxFH2SzkqE+7PkjDxSKjZKKszH1RfE4tw3cXhwfKqq66VxJuy2pF86rHrrtSxPkUbBDP9EnYOuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maWY/PpD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422459,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422459,
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
  "id": -576460752303422458,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422458,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAWWpxNT21GCarIKyC+UoHYlL9rvnZRdyhSPOx223EwPpjhujOh/9YwbdS/oqB2hEWr+LTqhj/blpLF/zNw4CsGuEBc7OrO9Nv3eSxmxFH2SzkqE+7PkjDxSKjZKKszH1RfE4tw3cXhwfKqq66VxJuy2pF86rHrrtSxPkUbBDP9EnYOuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maWY/PpD",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/bDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAP0OPKg"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422457,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422457,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvjuR+FgyrnwSPg93+NRhwOgkbAKHhT/a+YxX7w7l8gzBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAkT4XHs=",
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
  "id": -576460752303422456,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDwdEitNy+m9H/dM9TOVUI47MP/P0y8+BydCdkM2W1JP/8fI1t+14Lb/7KspzzOMWVftT+ra7gdbqP+pYbb+EYNuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLmaiwZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422456,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDwdEitNy+m9H/dM9TOVUI47MP/P0y8+BydCdkM2W1JP/8fI1t+14Lb/7KspzzOMWVftT+ra7gdbqP+pYbb+EYNuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLmaiwZ",
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
  "id": -576460752303422455,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECTDd3XDCl004Kx+zFso/MYkrMk6E7e2GUTGTSe7f9ok8nh0yAidznDEzW0VXJ8y6bwTFqsdxxvzEMQB6l/LOoDuEDwdEitNy+m9H/dM9TOVUI47MP/P0y8+BydCdkM2W1JP/8fI1t+14Lb/7KspzzOMWVftT+ra7gdbqP+pYbb+EYNuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK09o7c"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422455,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuECTDd3XDCl004Kx+zFso/MYkrMk6E7e2GUTGTSe7f9ok8nh0yAidznDEzW0VXJ8y6bwTFqsdxxvzEMQB6l/LOoDuEDwdEitNy+m9H/dM9TOVUI47MP/P0y8+BydCdkM2W1JP/8fI1t+14Lb/7KspzzOMWVftT+ra7gdbqP+pYbb+EYNuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK09o7c"
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuECTDd3XDCl004Kx+zFso/MYkrMk6E7e2GUTGTSe7f9ok8nh0yAidznDEzW0VXJ8y6bwTFqsdxxvzEMQB6l/LOoDuEDwdEitNy+m9H/dM9TOVUI47MP/P0y8+BydCdkM2W1JP/8fI1t+14Lb/7KspzzOMWVftT+ra7gdbqP+pYbb+EYNuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK09o7c"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422454,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422454,
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
  "id": -576460752303422453,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422453,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECTDd3XDCl004Kx+zFso/MYkrMk6E7e2GUTGTSe7f9ok8nh0yAidznDEzW0VXJ8y6bwTFqsdxxvzEMQB6l/LOoDuEDwdEitNy+m9H/dM9TOVUI47MP/P0y8+BydCdkM2W1JP/8fI1t+14Lb/7KspzzOMWVftT+ra7gdbqP+pYbb+EYNuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK09o7c",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhADYVrPxyQgnuEVdednMxR/K27YoU/qklqRVfIEEuQ0dLiqM2lrtPj+I3R9wHucLAHH/nezCc1Adhu70WrFUyXALkBKPkBJTsBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAHqPtZxePt5L8iToU9zpRWZZv3IFw8fB87HSWdT5qcAr52XqTf7PqkulLsTwRH9j5L5hzjaWQnuAPcpWR/ylkBbhAJ9DnYbufwXodfl3MUHLB6/IJXBTW4Lu9dwByJS9ilvss7B4ANINVSCmbgW+lnA0WtCzmCX+BAs3dqT7MEIaLArhI+EY5AqEG+O5H4WDKufBI+D3f41GHA6CRsAoeFP9r5jFfvDuXyDMCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIbgkQw2Hn5wno9Mhw==",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhADYVrPxyQgnuEVdednMxR/K27YoU/qklqRVfIEEuQ0dLiqM2lrtPj+I3R9wHucLAHH/nezCc1Adhu70WrFUyXALkBKPkBJTsBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAHqPtZxePt5L8iToU9zpRWZZv3IFw8fB87HSWdT5qcAr52XqTf7PqkulLsTwRH9j5L5hzjaWQnuAPcpWR/ylkBbhAJ9DnYbufwXodfl3MUHLB6/IJXBTW4Lu9dwByJS9ilvss7B4ANINVSCmbgW+lnA0WtCzmCX+BAs3dqT7MEIaLArhI+EY5AqEG+O5H4WDKufBI+D3f41GHA6CRsAoeFP9r5jFfvDuXyDMCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIbgkQw2Hn5wno9Mhw==",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "A\u000f߱����+���I��L\bE��9�%�\u001aC�x",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422452,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422452,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECTDd3XDCl004Kx+zFso/MYkrMk6E7e2GUTGTSe7f9ok8nh0yAidznDEzW0VXJ8y6bwTFqsdxxvzEMQB6l/LOoDuEDwdEitNy+m9H/dM9TOVUI47MP/P0y8+BydCdkM2W1JP/8fI1t+14Lb/7KspzzOMWVftT+ra7gdbqP+pYbb+EYNuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK09o7c",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422451,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422451,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvjuR+FgyrnwSPg93+NRhwOgkbAKHhT/a+YxX7w7l8gzBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC20Ni+U=",
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
  "id": -576460752303422450,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECoRJDbozjpk+eWoCOkZRgWGPwYHN71FMn7wkRalhlP0jmzcOdM/PeSJtwvQfZxiItBg0OXJ0YKNR9I9EGLb2EPuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtONzYV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422450,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+JALAfhCuECoRJDbozjpk+eWoCOkZRgWGPwYHN71FMn7wkRalhlP0jmzcOdM/PeSJtwvQfZxiItBg0OXJ0YKNR9I9EGLb2EPuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtONzYV",
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
  "id": -576460752303422449,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA9BXuBqioTdNhgDP+V2kTmdHJw012bKNv665ZWJsHunlgO4hL8+mqhy92TUOQFpFl7Y7Irc7C0Y+P8EIwkBPMKuECoRJDbozjpk+eWoCOkZRgWGPwYHN71FMn7wkRalhlP0jmzcOdM/PeSJtwvQfZxiItBg0OXJ0YKNR9I9EGLb2EPuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvpxAVV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422449,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEA9BXuBqioTdNhgDP+V2kTmdHJw012bKNv665ZWJsHunlgO4hL8+mqhy92TUOQFpFl7Y7Irc7C0Y+P8EIwkBPMKuECoRJDbozjpk+eWoCOkZRgWGPwYHN71FMn7wkRalhlP0jmzcOdM/PeSJtwvQfZxiItBg0OXJ0YKNR9I9EGLb2EPuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvpxAVV"
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEA9BXuBqioTdNhgDP+V2kTmdHJw012bKNv665ZWJsHunlgO4hL8+mqhy92TUOQFpFl7Y7Irc7C0Y+P8EIwkBPMKuECoRJDbozjpk+eWoCOkZRgWGPwYHN71FMn7wkRalhlP0jmzcOdM/PeSJtwvQfZxiItBg0OXJ0YKNR9I9EGLb2EPuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvpxAVV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422448,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422448,
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
  "id": -576460752303422447,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422447,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA9BXuBqioTdNhgDP+V2kTmdHJw012bKNv665ZWJsHunlgO4hL8+mqhy92TUOQFpFl7Y7Irc7C0Y+P8EIwkBPMKuECoRJDbozjpk+eWoCOkZRgWGPwYHN71FMn7wkRalhlP0jmzcOdM/PeSJtwvQfZxiItBg0OXJ0YKNR9I9EGLb2EPuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvpxAVV",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422446,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422446,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBvjuR+FgyrnwSPg93+NRhwOgkbAKHhT/a+YxX7w7l8gzoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEA9BXuBqioTdNhgDP+V2kTmdHJw012bKNv665ZWJsHunlgO4hL8+mqhy92TUOQFpFl7Y7Irc7C0Y+P8EIwkBPMKuECoRJDbozjpk+eWoCOkZRgWGPwYHN71FMn7wkRalhlP0jmzcOdM/PeSJtwvQfZxiItBg0OXJ0YKNR9I9EGLb2EPuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhuCRDDYefi3PXF/R",
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
    "signed_tx": "tx_+QFxCwH4QrhAGsHZMGM7zeWAa3CZxuTyyuPNothbDqQL/9P7tM4bZ4Da3nKtAhcyv0PKRSOVVV0a7SGbG9/OMXkooPrJJGkhA7kBKPkBJTsBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAPQV7gaoqE3TYYAz/ldpE5nRycNNdmyjb+uuWVibB7p5YDuIS/Ppqocvdk1DkBaRZe2OyK3OwtGPj/BCMJATzCrhAqESQ26M46ZPnlqAjpGUYFhj8GBze9RTJ+8JEWpYZT9I5s3DnTPz3kibcL0H2cYiLQYNDlydGCjUfSPRBi29hD7hI+EY5AqEG+O5H4WDKufBI+D3f41GHA6CRsAoeFP9r5jFfvDuXyDMFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIbgkQw2Hn4tbtWcnQ=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422445,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422445,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvjuR+FgyrnwSPg93+NRhwOgkbAKHhT/a+YxX7w7l8gzBqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAuGeyBQ=",
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
  "id": -576460752303422444,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECjj25j1KW4iPbksSrgKO2yQCw9cA+gNdpHAbGIAWabIV2Dg6oHPXZc+kaj6aTiTpqBlwIo2fWjGpiDNQpdqwEEuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKWUWr/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422444,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+JALAfhCuECjj25j1KW4iPbksSrgKO2yQCw9cA+gNdpHAbGIAWabIV2Dg6oHPXZc+kaj6aTiTpqBlwIo2fWjGpiDNQpdqwEEuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKWUWr/",
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
  "id": -576460752303422443,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEChOr0WDcWKponMET7O3rxHhUvMThYUYvECA4Fg6shD7zHTS0dxhsCoiGC17Q+96uLv25E7drVzo6qBDOq6KHoMuECjj25j1KW4iPbksSrgKO2yQCw9cA+gNdpHAbGIAWabIV2Dg6oHPXZc+kaj6aTiTpqBlwIo2fWjGpiDNQpdqwEEuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLpSnW1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422443,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEChOr0WDcWKponMET7O3rxHhUvMThYUYvECA4Fg6shD7zHTS0dxhsCoiGC17Q+96uLv25E7drVzo6qBDOq6KHoMuECjj25j1KW4iPbksSrgKO2yQCw9cA+gNdpHAbGIAWabIV2Dg6oHPXZc+kaj6aTiTpqBlwIo2fWjGpiDNQpdqwEEuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLpSnW1"
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEChOr0WDcWKponMET7O3rxHhUvMThYUYvECA4Fg6shD7zHTS0dxhsCoiGC17Q+96uLv25E7drVzo6qBDOq6KHoMuECjj25j1KW4iPbksSrgKO2yQCw9cA+gNdpHAbGIAWabIV2Dg6oHPXZc+kaj6aTiTpqBlwIo2fWjGpiDNQpdqwEEuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLpSnW1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422442,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422442,
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
  "id": -576460752303422441,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422441,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEChOr0WDcWKponMET7O3rxHhUvMThYUYvECA4Fg6shD7zHTS0dxhsCoiGC17Q+96uLv25E7drVzo6qBDOq6KHoMuECjj25j1KW4iPbksSrgKO2yQCw9cA+gNdpHAbGIAWabIV2Dg6oHPXZc+kaj6aTiTpqBlwIo2fWjGpiDNQpdqwEEuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLpSnW1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422440,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422440,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvjuR+FgyrnwSPg93+NRhwOgkbAKHhT/a+YxX7w7l8gzB6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1lpTqM=",
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
  "id": -576460752303422439,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAa+4oFAtDDi9EDCx2Xkw4ir2M4nrFzhMaLhcoBD2imbizzOv+kq3IaUa3oRWp0nt93gAoCsvE22sXcxanE5hsDuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsQLCEC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422439,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAa+4oFAtDDi9EDCx2Xkw4ir2M4nrFzhMaLhcoBD2imbizzOv+kq3IaUa3oRWp0nt93gAoCsvE22sXcxanE5hsDuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsQLCEC",
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
  "id": -576460752303422438,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAa+4oFAtDDi9EDCx2Xkw4ir2M4nrFzhMaLhcoBD2imbizzOv+kq3IaUa3oRWp0nt93gAoCsvE22sXcxanE5hsDuEAyQwHV0A/axDhCdmGm36JRljRSlE7CG8cIkgSN6A2IIZ67Q616VuIlgh/ag7V/u/yKP7kHHkD8NmHF10oGVjQHuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgutJcu9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422438,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEAa+4oFAtDDi9EDCx2Xkw4ir2M4nrFzhMaLhcoBD2imbizzOv+kq3IaUa3oRWp0nt93gAoCsvE22sXcxanE5hsDuEAyQwHV0A/axDhCdmGm36JRljRSlE7CG8cIkgSN6A2IIZ67Q616VuIlgh/ag7V/u/yKP7kHHkD8NmHF10oGVjQHuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgutJcu9"
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "state": "tx_+NILAfiEuEAa+4oFAtDDi9EDCx2Xkw4ir2M4nrFzhMaLhcoBD2imbizzOv+kq3IaUa3oRWp0nt93gAoCsvE22sXcxanE5hsDuEAyQwHV0A/axDhCdmGm36JRljRSlE7CG8cIkgSN6A2IIZ67Q616VuIlgh/ag7V/u/yKP7kHHkD8NmHF10oGVjQHuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgutJcu9"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422437,
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
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422437,
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
  "id": -576460752303422436,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422436,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAa+4oFAtDDi9EDCx2Xkw4ir2M4nrFzhMaLhcoBD2imbizzOv+kq3IaUa3oRWp0nt93gAoCsvE22sXcxanE5hsDuEAyQwHV0A/axDhCdmGm36JRljRSlE7CG8cIkgSN6A2IIZ67Q616VuIlgh/ag7V/u/yKP7kHHkD8NmHF10oGVjQHuEj4RjkCoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIMwegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgutJcu9",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAGsHZMGM7zeWAa3CZxuTyyuPNothbDqQL/9P7tM4bZ4Da3nKtAhcyv0PKRSOVVV0a7SGbG9/OMXkooPrJJGkhA7kBKPkBJTsBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAPQV7gaoqE3TYYAz/ldpE5nRycNNdmyjb+uuWVibB7p5YDuIS/Ppqocvdk1DkBaRZe2OyK3OwtGPj/BCMJATzCrhAqESQ26M46ZPnlqAjpGUYFhj8GBze9RTJ+8JEWpYZT9I5s3DnTPz3kibcL0H2cYiLQYNDlydGCjUfSPRBi29hD7hI+EY5AqEG+O5H4WDKufBI+D3f41GHA6CRsAoeFP9r5jFfvDuXyDMFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIbgkQw2Hn4tbtWcnQ==",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAGsHZMGM7zeWAa3CZxuTyyuPNothbDqQL/9P7tM4bZ4Da3nKtAhcyv0PKRSOVVV0a7SGbG9/OMXkooPrJJGkhA7kBKPkBJTsBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAPQV7gaoqE3TYYAz/ldpE5nRycNNdmyjb+uuWVibB7p5YDuIS/Ppqocvdk1DkBaRZe2OyK3OwtGPj/BCMJATzCrhAqESQ26M46ZPnlqAjpGUYFhj8GBze9RTJ+8JEWpYZT9I5s3DnTPz3kibcL0H2cYiLQYNDlydGCjUfSPRBi29hD7hI+EY5AqEG+O5H4WDKufBI+D3f41GHA6CRsAoeFP9r5jFfvDuXyDMFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIbgkQw2Hn4tbtWcnQ==",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "��\u0015�\u0013A~�s_��\u0015T2�:@�\u0002��\u0019�\r�\u001b��\rh",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBvjuR+FgyrnwSPg93+NRhwOgkbAKHhT/a+YxX7w7l8gzoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/+GHLHOiuwBAIYPXtZ/KABxvCW8PA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422435,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECPgpxByhA0sbn6gF+cb5d+bguWUsUOa91rW3Lsc+kZ1qN1gfufn6WktcW4vy6NP6QPP46hB2Jw4m9A5GO4Hd0KuF/4XTUBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAcTayccI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422435,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECPgpxByhA0sbn6gF+cb5d+bguWUsUOa91rW3Lsc+kZ1qN1gfufn6WktcW4vy6NP6QPP46hB2Jw4m9A5GO4Hd0KuF/4XTUBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAcTayccI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422434,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBFcYd6aArvRcUOgbYlH9MlpnSfG81gMpoovhQR3oHdYVcf8kXjIrMjAN4cTi7BkifBnh7/1V6y+GqOHQLQ3mQGuECPgpxByhA0sbn6gF+cb5d+bguWUsUOa91rW3Lsc+kZ1qN1gfufn6WktcW4vy6NP6QPP46hB2Jw4m9A5GO4Hd0KuF/4XTUBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAcQzt1mE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
  "id": -576460752303422434,
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBFcYd6aArvRcUOgbYlH9MlpnSfG81gMpoovhQR3oHdYVcf8kXjIrMjAN4cTi7BkifBnh7/1V6y+GqOHQLQ3mQGuECPgpxByhA0sbn6gF+cb5d+bguWUsUOa91rW3Lsc+kZ1qN1gfufn6WktcW4vy6NP6QPP46hB2Jw4m9A5GO4Hd0KuF/4XTUBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAcQzt1mE=",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBFcYd6aArvRcUOgbYlH9MlpnSfG81gMpoovhQR3oHdYVcf8kXjIrMjAN4cTi7BkifBnh7/1V6y+GqOHQLQ3mQGuECPgpxByhA0sbn6gF+cb5d+bguWUsUOa91rW3Lsc+kZ1qN1gfufn6WktcW4vy6NP6QPP46hB2Jw4m9A5GO4Hd0KuF/4XTUBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAcQzt1mE=",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBFcYd6aArvRcUOgbYlH9MlpnSfG81gMpoovhQR3oHdYVcf8kXjIrMjAN4cTi7BkifBnh7/1V6y+GqOHQLQ3mQGuECPgpxByhA0sbn6gF+cb5d+bguWUsUOa91rW3Lsc+kZ1qN1gfufn6WktcW4vy6NP6QPP46hB2Jw4m9A5GO4Hd0KuF/4XTUBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAcQzt1mE=",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBFcYd6aArvRcUOgbYlH9MlpnSfG81gMpoovhQR3oHdYVcf8kXjIrMjAN4cTi7BkifBnh7/1V6y+GqOHQLQ3mQGuECPgpxByhA0sbn6gF+cb5d+bguWUsUOa91rW3Lsc+kZ1qN1gfufn6WktcW4vy6NP6QPP46hB2Jw4m9A5GO4Hd0KuF/4XTUBoQb47kfhYMq58Ej4Pd/jUYcDoJGwCh4U/2vmMV+8O5fIM6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAcQzt1mE=",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
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
    "channel_id": "ch_2tdbxmXXWG78BU3LYMxaGMT5VYWYVxVtQS2d9CMHJ8Yi8jpESV",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
