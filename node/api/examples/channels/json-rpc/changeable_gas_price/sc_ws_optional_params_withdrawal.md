
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
      "fsm_id": "ba_4EkQf6rlx3qiSNh/rQjmLBYUkmvYN0TooojUUErIbf/9p9oT"
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
      "fsm_id": "ba_4DQXpBh20KzihUmZxkihSq1cXC5UYLFdgCEBZwAGzSrDAdVp"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtUj54WQQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422573,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBe0J2H/0EqAWpQeAHEdjAUhg807Bbpnc9ITtu366hjxx2NrVhM6I5fMlM1QtZEFOYIVTBHDVPnI1Gx6/6y6RQNuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LVLGBr3Y="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422573,
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "fsm_id": "ba_4DQXpBh20KzihUmZxkihSq1cXC5UYLFdgCEBZwAGzSrDAdVp",
      "signed_tx": "tx_+MsLAfhCuEBe0J2H/0EqAWpQeAHEdjAUhg807Bbpnc9ITtu366hjxx2NrVhM6I5fMlM1QtZEFOYIVTBHDVPnI1Gx6/6y6RQNuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LVLGBr3Y=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422572,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAXtCdh/9BKgFqUHgBxHYwFIYPNOwW6Z3PSE7bt+uoY8cdja1YTOiOXzJTNULWRBTmCFUwRw1T5yNRsev+sukUDbhAfdipyO6ozrO1CrSVpbwU1nolYUIPad3fB5gCr8RHXh33C5c0/j7GrJqrXny8a7DLRVavNy1w2l5LwsfmwucHALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1T7I9TH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
  "id": -576460752303422572,
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAXtCdh/9BKgFqUHgBxHYwFIYPNOwW6Z3PSE7bt+uoY8cdja1YTOiOXzJTNULWRBTmCFUwRw1T5yNRsev+sukUDbhAfdipyO6ozrO1CrSVpbwU1nolYUIPad3fB5gCr8RHXh33C5c0/j7GrJqrXny8a7DLRVavNy1w2l5LwsfmwucHALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1T7I9TH",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_4EkQf6rlx3qiSNh/rQjmLBYUkmvYN0TooojUUErIbf/9p9oT"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAXtCdh/9BKgFqUHgBxHYwFIYPNOwW6Z3PSE7bt+uoY8cdja1YTOiOXzJTNULWRBTmCFUwRw1T5yNRsev+sukUDbhAfdipyO6ozrO1CrSVpbwU1nolYUIPad3fB5gCr8RHXh33C5c0/j7GrJqrXny8a7DLRVavNy1w2l5LwsfmwucHALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1T7I9TH",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAXtCdh/9BKgFqUHgBxHYwFIYPNOwW6Z3PSE7bt+uoY8cdja1YTOiOXzJTNULWRBTmCFUwRw1T5yNRsev+sukUDbhAfdipyO6ozrO1CrSVpbwU1nolYUIPad3fB5gCr8RHXh33C5c0/j7GrJqrXny8a7DLRVavNy1w2l5LwsfmwucHALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1T7I9TH",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAXtCdh/9BKgFqUHgBxHYwFIYPNOwW6Z3PSE7bt+uoY8cdja1YTOiOXzJTNULWRBTmCFUwRw1T5yNRsev+sukUDbhAfdipyO6ozrO1CrSVpbwU1nolYUIPad3fB5gCr8RHXh33C5c0/j7GrJqrXny8a7DLRVavNy1w2l5LwsfmwucHALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1T7I9TH",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
  "id": -576460752303422571,
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
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
  "id": -576460752303422571,
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "state": "tx_+QENCwH4hLhAXtCdh/9BKgFqUHgBxHYwFIYPNOwW6Z3PSE7bt+uoY8cdja1YTOiOXzJTNULWRBTmCFUwRw1T5yNRsev+sukUDbhAfdipyO6ozrO1CrSVpbwU1nolYUIPad3fB5gCr8RHXh33C5c0/j7GrJqrXny8a7DLRVavNy1w2l5LwsfmwucHALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1T7I9TH"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "state": "tx_+QENCwH4hLhAXtCdh/9BKgFqUHgBxHYwFIYPNOwW6Z3PSE7bt+uoY8cdja1YTOiOXzJTNULWRBTmCFUwRw1T5yNRsev+sukUDbhAfdipyO6ozrO1CrSVpbwU1nolYUIPad3fB5gCr8RHXh33C5c0/j7GrJqrXny8a7DLRVavNy1w2l5LwsfmwucHALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1T7I9TH"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
      "method": "channels.withdraw",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBlCV5jVX5QcjenTA8A5S4rrqRRSK0sd6HAsMKSI35wztoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/Aobiv0KD6aIyRp0q4njYpKUN7EoE8dGS1wKGxithIYn6oqM3YIgJVl2jr3Q==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422570,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBbcrps1QKg8lNRb3rDyp3JFf2M8FuKHid1Twvfy+XmzKwOSb7BWdye9HXbgS3UDcNMWxyFv8GxLvyZXkAv8bkBuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9Cg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICVaJWusQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
  "id": -576460752303422570,
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBbcrps1QKg8lNRb3rDyp3JFf2M8FuKHid1Twvfy+XmzKwOSb7BWdye9HXbgS3UDcNMWxyFv8GxLvyZXkAv8bkBuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9Cg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICVaJWusQ=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422569,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBbcrps1QKg8lNRb3rDyp3JFf2M8FuKHid1Twvfy+XmzKwOSb7BWdye9HXbgS3UDcNMWxyFv8GxLvyZXkAv8bkBuECoobWTz0Ng/kp8WfZRQBcytZxLgnJ7ZyAl5xcW/e6VSj+8gf3ZpdvYGRBNWhW2EJepgcnR8YgTQW/8bt5RorEFuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9Cg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICVezCBiA="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
  "id": -576460752303422569,
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEBbcrps1QKg8lNRb3rDyp3JFf2M8FuKHid1Twvfy+XmzKwOSb7BWdye9HXbgS3UDcNMWxyFv8GxLvyZXkAv8bkBuECoobWTz0Ng/kp8WfZRQBcytZxLgnJ7ZyAl5xcW/e6VSj+8gf3ZpdvYGRBNWhW2EJepgcnR8YgTQW/8bt5RorEFuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9Cg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICVezCBiA=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEBbcrps1QKg8lNRb3rDyp3JFf2M8FuKHid1Twvfy+XmzKwOSb7BWdye9HXbgS3UDcNMWxyFv8GxLvyZXkAv8bkBuECoobWTz0Ng/kp8WfZRQBcytZxLgnJ7ZyAl5xcW/e6VSj+8gf3ZpdvYGRBNWhW2EJepgcnR8YgTQW/8bt5RorEFuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9Cg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICVezCBiA=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBbcrps1QKg8lNRb3rDyp3JFf2M8FuKHid1Twvfy+XmzKwOSb7BWdye9HXbgS3UDcNMWxyFv8GxLvyZXkAv8bkBuECoobWTz0Ng/kp8WfZRQBcytZxLgnJ7ZyAl5xcW/e6VSj+8gf3ZpdvYGRBNWhW2EJepgcnR8YgTQW/8bt5RorEFuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9Cg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICVezCBiA=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBbcrps1QKg8lNRb3rDyp3JFf2M8FuKHid1Twvfy+XmzKwOSb7BWdye9HXbgS3UDcNMWxyFv8GxLvyZXkAv8bkBuECoobWTz0Ng/kp8WfZRQBcytZxLgnJ7ZyAl5xcW/e6VSj+8gf3ZpdvYGRBNWhW2EJepgcnR8YgTQW/8bt5RorEFuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9Cg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICVezCBiA=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "state": "tx_+P4LAfiEuEBbcrps1QKg8lNRb3rDyp3JFf2M8FuKHid1Twvfy+XmzKwOSb7BWdye9HXbgS3UDcNMWxyFv8GxLvyZXkAv8bkBuECoobWTz0Ng/kp8WfZRQBcytZxLgnJ7ZyAl5xcW/e6VSj+8gf3ZpdvYGRBNWhW2EJepgcnR8YgTQW/8bt5RorEFuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9Cg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICVezCBiA="
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "state": "tx_+P4LAfiEuEBbcrps1QKg8lNRb3rDyp3JFf2M8FuKHid1Twvfy+XmzKwOSb7BWdye9HXbgS3UDcNMWxyFv8GxLvyZXkAv8bkBuECoobWTz0Ng/kp8WfZRQBcytZxLgnJ7ZyAl5xcW/e6VSj+8gf3ZpdvYGRBNWhW2EJepgcnR8YgTQW/8bt5RorEFuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9Cg+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICVezCBiA="
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
      "method": "channels.withdraw",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBlCV5jVX5QcjenTA8A5S4rrqRRSK0sd6HAsMKSI35wztoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/Aobiv0KBIWkDp9eRQQRyHm8U+8URorUUQQNdonwOQZqEaw6yolgMi8n05ig==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422568,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEC0TZ8zO+eQWWyNeB8QDg3L4pSIYt10G32J4dKF4+8oNtXFMEeETugFOkxgKixWNevgQiYb8m33JKA5P6Z/R14FuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDIlUrwkw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
  "id": -576460752303422568,
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEC0TZ8zO+eQWWyNeB8QDg3L4pSIYt10G32J4dKF4+8oNtXFMEeETugFOkxgKixWNevgQiYb8m33JKA5P6Z/R14FuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDIlUrwkw=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422567,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEChqvcX+LTn970+xP7yaY8kq8n6ysAZ1OZWDZWJY6kBYd/3MAwfk9GpavdAZ7CKwsZVXowSe0cjqIH7kb1j44wPuEC0TZ8zO+eQWWyNeB8QDg3L4pSIYt10G32J4dKF4+8oNtXFMEeETugFOkxgKixWNevgQiYb8m33JKA5P6Z/R14FuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDImJQe0g="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
  "id": -576460752303422567,
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEChqvcX+LTn970+xP7yaY8kq8n6ysAZ1OZWDZWJY6kBYd/3MAwfk9GpavdAZ7CKwsZVXowSe0cjqIH7kb1j44wPuEC0TZ8zO+eQWWyNeB8QDg3L4pSIYt10G32J4dKF4+8oNtXFMEeETugFOkxgKixWNevgQiYb8m33JKA5P6Z/R14FuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDImJQe0g=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEChqvcX+LTn970+xP7yaY8kq8n6ysAZ1OZWDZWJY6kBYd/3MAwfk9GpavdAZ7CKwsZVXowSe0cjqIH7kb1j44wPuEC0TZ8zO+eQWWyNeB8QDg3L4pSIYt10G32J4dKF4+8oNtXFMEeETugFOkxgKixWNevgQiYb8m33JKA5P6Z/R14FuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDImJQe0g=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "message": {
        "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEChqvcX+LTn970+xP7yaY8kq8n6ysAZ1OZWDZWJY6kBYd/3MAwfk9GpavdAZ7CKwsZVXowSe0cjqIH7kb1j44wPuEC0TZ8zO+eQWWyNeB8QDg3L4pSIYt10G32J4dKF4+8oNtXFMEeETugFOkxgKixWNevgQiYb8m33JKA5P6Z/R14FuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDImJQe0g=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEChqvcX+LTn970+xP7yaY8kq8n6ysAZ1OZWDZWJY6kBYd/3MAwfk9GpavdAZ7CKwsZVXowSe0cjqIH7kb1j44wPuEC0TZ8zO+eQWWyNeB8QDg3L4pSIYt10G32J4dKF4+8oNtXFMEeETugFOkxgKixWNevgQiYb8m33JKA5P6Z/R14FuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDImJQe0g=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "state": "tx_+P4LAfiEuEChqvcX+LTn970+xP7yaY8kq8n6ysAZ1OZWDZWJY6kBYd/3MAwfk9GpavdAZ7CKwsZVXowSe0cjqIH7kb1j44wPuEC0TZ8zO+eQWWyNeB8QDg3L4pSIYt10G32J4dKF4+8oNtXFMEeETugFOkxgKixWNevgQiYb8m33JKA5P6Z/R14FuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDImJQe0g="
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "state": "tx_+P4LAfiEuEChqvcX+LTn970+xP7yaY8kq8n6ysAZ1OZWDZWJY6kBYd/3MAwfk9GpavdAZ7CKwsZVXowSe0cjqIH7kb1j44wPuEC0TZ8zO+eQWWyNeB8QDg3L4pSIYt10G32J4dKF4+8oNtXFMEeETugFOkxgKixWNevgQiYb8m33JKA5P6Z/R14FuHT4cjQBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDImJQe0g="
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBlCV5jVX5QcjenTA8A5S4rrqRRSK0sd6HAsMKSI35wztoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/2GHLHOiuv/AIYPXtZ/KABW1lfbcw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422566,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDCPQ2xgBCUiV8+VaKupdAvbDkdNfnPvGBz37Dv+fByixwiq+y/qqUxkELzgdMuL2rPvSTRBgSyjsf+j6F6MnwIuF/4XTUBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAVtWudvs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
  "id": -576460752303422566,
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDCPQ2xgBCUiV8+VaKupdAvbDkdNfnPvGBz37Dv+fByixwiq+y/qqUxkELzgdMuL2rPvSTRBgSyjsf+j6F6MnwIuF/4XTUBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAVtWudvs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422565,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEDCPQ2xgBCUiV8+VaKupdAvbDkdNfnPvGBz37Dv+fByixwiq+y/qqUxkELzgdMuL2rPvSTRBgSyjsf+j6F6MnwIuEDYmGfQBL2z59P+k2EJYOp18o0lgwrAplaSZDW/ENVryyx+dDSE2P3ciuMm1b1rtRjANazTPfYJzxfOjCA7SQAJuF/4XTUBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAVtUHUek="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
  "id": -576460752303422565,
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEDCPQ2xgBCUiV8+VaKupdAvbDkdNfnPvGBz37Dv+fByixwiq+y/qqUxkELzgdMuL2rPvSTRBgSyjsf+j6F6MnwIuEDYmGfQBL2z59P+k2EJYOp18o0lgwrAplaSZDW/ENVryyx+dDSE2P3ciuMm1b1rtRjANazTPfYJzxfOjCA7SQAJuF/4XTUBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAVtUHUek=",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEDCPQ2xgBCUiV8+VaKupdAvbDkdNfnPvGBz37Dv+fByixwiq+y/qqUxkELzgdMuL2rPvSTRBgSyjsf+j6F6MnwIuEDYmGfQBL2z59P+k2EJYOp18o0lgwrAplaSZDW/ENVryyx+dDSE2P3ciuMm1b1rtRjANazTPfYJzxfOjCA7SQAJuF/4XTUBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAVtUHUek=",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEDCPQ2xgBCUiV8+VaKupdAvbDkdNfnPvGBz37Dv+fByixwiq+y/qqUxkELzgdMuL2rPvSTRBgSyjsf+j6F6MnwIuEDYmGfQBL2z59P+k2EJYOp18o0lgwrAplaSZDW/ENVryyx+dDSE2P3ciuMm1b1rtRjANazTPfYJzxfOjCA7SQAJuF/4XTUBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAVtUHUek=",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEDCPQ2xgBCUiV8+VaKupdAvbDkdNfnPvGBz37Dv+fByixwiq+y/qqUxkELzgdMuL2rPvSTRBgSyjsf+j6F6MnwIuEDYmGfQBL2z59P+k2EJYOp18o0lgwrAplaSZDW/ENVryyx+dDSE2P3ciuMm1b1rtRjANazTPfYJzxfOjCA7SQAJuF/4XTUBoQZQleY1V+UHI3p0wPAOUuK66kUUitLHehwLDCkiN+cM7aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAVtUHUek=",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
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
    "channel_id": "ch_cVT5L8mVLYKubEPUnhKE73e4VSiJ9w6NL17AASsj6FLmtQLCB",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
