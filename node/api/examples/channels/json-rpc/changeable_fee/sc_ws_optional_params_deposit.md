
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
      "fsm_id": "ba_QLVYRVCA5KkrqIzbZgN5cPgUijRx1rybR87xUcvsq3TnDqpE"
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
      "fsm_id": "ba_SphIpgrXBagfGl4Jc9xunxal+7c4PNlA4dAh2gF3jLP6TslW"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs5WT52rA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422674,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECvSI8Q1aba/nD5T2LV36U44mGqGFc1LULaYgTzVZui7MbcOQxCdJ/ktJwDoyeYbNSuFx0IOBDS4DCbWWfA4ZAKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LOcPnvco="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422674,
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "fsm_id": "ba_SphIpgrXBagfGl4Jc9xunxal+7c4PNlA4dAh2gF3jLP6TslW",
      "signed_tx": "tx_+MsLAfhCuECvSI8Q1aba/nD5T2LV36U44mGqGFc1LULaYgTzVZui7MbcOQxCdJ/ktJwDoyeYbNSuFx0IOBDS4DCbWWfA4ZAKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LOcPnvco=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422673,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAf4lbqwqD/DhsyVlRqBtRiLr2nP0H8bl+QVbm3eTJEZH0hCKdJPe9H/lIXsXK/9xGIKsadrzZYlXvLtYNK2hgCLhAr0iPENWm2v5w+U9i1d+lOOJhqhhXNS1C2mIE81WbouzG3DkMQnSf5LScA6MnmGzUrhcdCDgQ0uAwm1lnwOGQCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzlFNZxu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
  "id": -576460752303422673,
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAf4lbqwqD/DhsyVlRqBtRiLr2nP0H8bl+QVbm3eTJEZH0hCKdJPe9H/lIXsXK/9xGIKsadrzZYlXvLtYNK2hgCLhAr0iPENWm2v5w+U9i1d+lOOJhqhhXNS1C2mIE81WbouzG3DkMQnSf5LScA6MnmGzUrhcdCDgQ0uAwm1lnwOGQCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzlFNZxu",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_QLVYRVCA5KkrqIzbZgN5cPgUijRx1rybR87xUcvsq3TnDqpE"
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAf4lbqwqD/DhsyVlRqBtRiLr2nP0H8bl+QVbm3eTJEZH0hCKdJPe9H/lIXsXK/9xGIKsadrzZYlXvLtYNK2hgCLhAr0iPENWm2v5w+U9i1d+lOOJhqhhXNS1C2mIE81WbouzG3DkMQnSf5LScA6MnmGzUrhcdCDgQ0uAwm1lnwOGQCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzlFNZxu",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAf4lbqwqD/DhsyVlRqBtRiLr2nP0H8bl+QVbm3eTJEZH0hCKdJPe9H/lIXsXK/9xGIKsadrzZYlXvLtYNK2hgCLhAr0iPENWm2v5w+U9i1d+lOOJhqhhXNS1C2mIE81WbouzG3DkMQnSf5LScA6MnmGzUrhcdCDgQ0uAwm1lnwOGQCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzlFNZxu",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAf4lbqwqD/DhsyVlRqBtRiLr2nP0H8bl+QVbm3eTJEZH0hCKdJPe9H/lIXsXK/9xGIKsadrzZYlXvLtYNK2hgCLhAr0iPENWm2v5w+U9i1d+lOOJhqhhXNS1C2mIE81WbouzG3DkMQnSf5LScA6MnmGzUrhcdCDgQ0uAwm1lnwOGQCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzlFNZxu",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
  "id": -576460752303422672,
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
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
  "id": -576460752303422672,
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "state": "tx_+QENCwH4hLhAf4lbqwqD/DhsyVlRqBtRiLr2nP0H8bl+QVbm3eTJEZH0hCKdJPe9H/lIXsXK/9xGIKsadrzZYlXvLtYNK2hgCLhAr0iPENWm2v5w+U9i1d+lOOJhqhhXNS1C2mIE81WbouzG3DkMQnSf5LScA6MnmGzUrhcdCDgQ0uAwm1lnwOGQCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzlFNZxu"
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "state": "tx_+QENCwH4hLhAf4lbqwqD/DhsyVlRqBtRiLr2nP0H8bl+QVbm3eTJEZH0hCKdJPe9H/lIXsXK/9xGIKsadrzZYlXvLtYNK2hgCLhAr0iPENWm2v5w+U9i1d+lOOJhqhhXNS1C2mIE81WbouzG3DkMQnSf5LScA6MnmGzUrhcdCDgQ0uAwm1lnwOGQCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzlFNZxu"
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBlg90MVu2H3c9adH8zY3rkhZrYagukzwSRccva9TtABgoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhnBIhhsPP6AJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQI6txIgJg==",
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
  "id": -576460752303422671,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDV723MGER9izTXDSTtRI3gvPLnAhIe8pfE3xn9DW3nOMzaIps76EwHZKgY9SCiKbnC4o3oCq75X6EDoBOJ0vgMuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCOi8CrXg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
  "id": -576460752303422671,
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDV723MGER9izTXDSTtRI3gvPLnAhIe8pfE3xn9DW3nOMzaIps76EwHZKgY9SCiKbnC4o3oCq75X6EDoBOJ0vgMuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCOi8CrXg=",
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
  "id": -576460752303422670,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAboDEzXGoJMC+gGRPp/7o0/hXKi+MfkYHEjg34zZXkAjyBhq3AITjnVrE6KKGN9fwshv0b0W6oc5d/8tRjeisAuEDV723MGER9izTXDSTtRI3gvPLnAhIe8pfE3xn9DW3nOMzaIps76EwHZKgY9SCiKbnC4o3oCq75X6EDoBOJ0vgMuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCOkp8WxY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
  "id": -576460752303422670,
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEAboDEzXGoJMC+gGRPp/7o0/hXKi+MfkYHEjg34zZXkAjyBhq3AITjnVrE6KKGN9fwshv0b0W6oc5d/8tRjeisAuEDV723MGER9izTXDSTtRI3gvPLnAhIe8pfE3xn9DW3nOMzaIps76EwHZKgY9SCiKbnC4o3oCq75X6EDoBOJ0vgMuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCOkp8WxY=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEAboDEzXGoJMC+gGRPp/7o0/hXKi+MfkYHEjg34zZXkAjyBhq3AITjnVrE6KKGN9fwshv0b0W6oc5d/8tRjeisAuEDV723MGER9izTXDSTtRI3gvPLnAhIe8pfE3xn9DW3nOMzaIps76EwHZKgY9SCiKbnC4o3oCq75X6EDoBOJ0vgMuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCOkp8WxY=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAboDEzXGoJMC+gGRPp/7o0/hXKi+MfkYHEjg34zZXkAjyBhq3AITjnVrE6KKGN9fwshv0b0W6oc5d/8tRjeisAuEDV723MGER9izTXDSTtRI3gvPLnAhIe8pfE3xn9DW3nOMzaIps76EwHZKgY9SCiKbnC4o3oCq75X6EDoBOJ0vgMuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCOkp8WxY=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAboDEzXGoJMC+gGRPp/7o0/hXKi+MfkYHEjg34zZXkAjyBhq3AITjnVrE6KKGN9fwshv0b0W6oc5d/8tRjeisAuEDV723MGER9izTXDSTtRI3gvPLnAhIe8pfE3xn9DW3nOMzaIps76EwHZKgY9SCiKbnC4o3oCq75X6EDoBOJ0vgMuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCOkp8WxY=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "state": "tx_+P4LAfiEuEAboDEzXGoJMC+gGRPp/7o0/hXKi+MfkYHEjg34zZXkAjyBhq3AITjnVrE6KKGN9fwshv0b0W6oc5d/8tRjeisAuEDV723MGER9izTXDSTtRI3gvPLnAhIe8pfE3xn9DW3nOMzaIps76EwHZKgY9SCiKbnC4o3oCq75X6EDoBOJ0vgMuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCOkp8WxY="
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "state": "tx_+P4LAfiEuEAboDEzXGoJMC+gGRPp/7o0/hXKi+MfkYHEjg34zZXkAjyBhq3AITjnVrE6KKGN9fwshv0b0W6oc5d/8tRjeisAuEDV723MGER9izTXDSTtRI3gvPLnAhIe8pfE3xn9DW3nOMzaIps76EwHZKgY9SCiKbnC4o3oCq75X6EDoBOJ0vgMuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+gCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCOkp8WxY="
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBlg90MVu2H3c9adH8zY3rkhZrYagukzwSRccva9TtABgoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhnBIhhsPP6BdYyosJiEVkIv3UfhREtMPbLmXGvLesTSuRCc8B8rvQgMXoEqidw==",
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
  "id": -576460752303422669,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBBTMiLvhwRYjvbJBXNwmD4VTCL37Iq4+9xRGaqpAcOyL1p9btmQ0m9spTrSIRAw2wyAisjfM7tv1gXuvw66hUGuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDFw7Mszw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
  "id": -576460752303422669,
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBBTMiLvhwRYjvbJBXNwmD4VTCL37Iq4+9xRGaqpAcOyL1p9btmQ0m9spTrSIRAw2wyAisjfM7tv1gXuvw66hUGuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDFw7Mszw=",
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
  "id": -576460752303422668,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBBTMiLvhwRYjvbJBXNwmD4VTCL37Iq4+9xRGaqpAcOyL1p9btmQ0m9spTrSIRAw2wyAisjfM7tv1gXuvw66hUGuECXjug/1ih0B4wWoxcS2QiQD1fN49GwHTCF5TaeOSADHP1iG6nydqU8uWZjG2yWbjPOAeS7mBqLTrPdu0I/g5kOuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDF4yWDgs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
  "id": -576460752303422668,
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBBTMiLvhwRYjvbJBXNwmD4VTCL37Iq4+9xRGaqpAcOyL1p9btmQ0m9spTrSIRAw2wyAisjfM7tv1gXuvw66hUGuECXjug/1ih0B4wWoxcS2QiQD1fN49GwHTCF5TaeOSADHP1iG6nydqU8uWZjG2yWbjPOAeS7mBqLTrPdu0I/g5kOuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDF4yWDgs=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBBTMiLvhwRYjvbJBXNwmD4VTCL37Iq4+9xRGaqpAcOyL1p9btmQ0m9spTrSIRAw2wyAisjfM7tv1gXuvw66hUGuECXjug/1ih0B4wWoxcS2QiQD1fN49GwHTCF5TaeOSADHP1iG6nydqU8uWZjG2yWbjPOAeS7mBqLTrPdu0I/g5kOuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDF4yWDgs=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "message": {
        "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBBTMiLvhwRYjvbJBXNwmD4VTCL37Iq4+9xRGaqpAcOyL1p9btmQ0m9spTrSIRAw2wyAisjfM7tv1gXuvw66hUGuECXjug/1ih0B4wWoxcS2QiQD1fN49GwHTCF5TaeOSADHP1iG6nydqU8uWZjG2yWbjPOAeS7mBqLTrPdu0I/g5kOuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDF4yWDgs=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBBTMiLvhwRYjvbJBXNwmD4VTCL37Iq4+9xRGaqpAcOyL1p9btmQ0m9spTrSIRAw2wyAisjfM7tv1gXuvw66hUGuECXjug/1ih0B4wWoxcS2QiQD1fN49GwHTCF5TaeOSADHP1iG6nydqU8uWZjG2yWbjPOAeS7mBqLTrPdu0I/g5kOuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDF4yWDgs=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "state": "tx_+P4LAfiEuEBBTMiLvhwRYjvbJBXNwmD4VTCL37Iq4+9xRGaqpAcOyL1p9btmQ0m9spTrSIRAw2wyAisjfM7tv1gXuvw66hUGuECXjug/1ih0B4wWoxcS2QiQD1fN49GwHTCF5TaeOSADHP1iG6nydqU8uWZjG2yWbjPOAeS7mBqLTrPdu0I/g5kOuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDF4yWDgs="
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "state": "tx_+P4LAfiEuEBBTMiLvhwRYjvbJBXNwmD4VTCL37Iq4+9xRGaqpAcOyL1p9btmQ0m9spTrSIRAw2wyAisjfM7tv1gXuvw66hUGuECXjug/1ih0B4wWoxcS2QiQD1fN49GwHTCF5TaeOSADHP1iG6nydqU8uWZjG2yWbjPOAeS7mBqLTrPdu0I/g5kOuHT4cjMBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDF4yWDgs="
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBlg90MVu2H3c9adH8zY3rkhZrYagukzwSRccva9TtABgoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rnizAGGHLHOiuwDAIYPXtZ/KAA79VfRvA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422667,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBXTtUt9Xr5UyjAUbKGJixsCN5GPW+hQPlAnxzBZCCovVuEg8TYtseEIshGl7OowDfKbiBGm8GMZ84KDsl90PcBuF/4XTUBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAO2hMVgA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
  "id": -576460752303422667,
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBXTtUt9Xr5UyjAUbKGJixsCN5GPW+hQPlAnxzBZCCovVuEg8TYtseEIshGl7OowDfKbiBGm8GMZ84KDsl90PcBuF/4XTUBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAO2hMVgA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422666,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBXTtUt9Xr5UyjAUbKGJixsCN5GPW+hQPlAnxzBZCCovVuEg8TYtseEIshGl7OowDfKbiBGm8GMZ84KDsl90PcBuEDO4+JxHUMXRuhn2yH0yQGj6W5jgpGZrNa39NFAWk+dzIPaFG07eZ9yAC5W+SY4IbtTezuNXYtzMCOdM86ouvwDuF/4XTUBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAOw5mha4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
  "id": -576460752303422666,
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBXTtUt9Xr5UyjAUbKGJixsCN5GPW+hQPlAnxzBZCCovVuEg8TYtseEIshGl7OowDfKbiBGm8GMZ84KDsl90PcBuEDO4+JxHUMXRuhn2yH0yQGj6W5jgpGZrNa39NFAWk+dzIPaFG07eZ9yAC5W+SY4IbtTezuNXYtzMCOdM86ouvwDuF/4XTUBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAOw5mha4=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBXTtUt9Xr5UyjAUbKGJixsCN5GPW+hQPlAnxzBZCCovVuEg8TYtseEIshGl7OowDfKbiBGm8GMZ84KDsl90PcBuEDO4+JxHUMXRuhn2yH0yQGj6W5jgpGZrNa39NFAWk+dzIPaFG07eZ9yAC5W+SY4IbtTezuNXYtzMCOdM86ouvwDuF/4XTUBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAOw5mha4=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBXTtUt9Xr5UyjAUbKGJixsCN5GPW+hQPlAnxzBZCCovVuEg8TYtseEIshGl7OowDfKbiBGm8GMZ84KDsl90PcBuEDO4+JxHUMXRuhn2yH0yQGj6W5jgpGZrNa39NFAWk+dzIPaFG07eZ9yAC5W+SY4IbtTezuNXYtzMCOdM86ouvwDuF/4XTUBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAOw5mha4=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBXTtUt9Xr5UyjAUbKGJixsCN5GPW+hQPlAnxzBZCCovVuEg8TYtseEIshGl7OowDfKbiBGm8GMZ84KDsl90PcBuEDO4+JxHUMXRuhn2yH0yQGj6W5jgpGZrNa39NFAWk+dzIPaFG07eZ9yAC5W+SY4IbtTezuNXYtzMCOdM86ouvwDuF/4XTUBoQZYPdDFbth93PWnR/M2N65IWa2GoLpM8EkXHL2vU7QAYKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAOw5mha4=",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
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
    "channel_id": "ch_fs1a6Wn3rcsfaPm99KthXaEr82X8Sco6GjejMGsZEbCHh4zS8",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
