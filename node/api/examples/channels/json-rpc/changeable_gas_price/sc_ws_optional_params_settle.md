
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
      "fsm_id": "ba_vaRsLTNrb5nXUsHue91ORjVqRrS3b7WpXxPmU9dm1QSUU2vM"
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
      "fsm_id": "ba_UcgqXU9at95P2j9terDe/bZrbj+RZfUvifcsfIsjyylTbo4h"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtiTRvTUA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422501,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBLCP3YkIzw1Lwp+v1F5CC/lTmlU3OvadimlI92neaONJHmwR6vXEQc1+81G8pnFeQ+37IwQyafmGaAnddSCi4PuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LYkLSN88="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422501,
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "fsm_id": "ba_UcgqXU9at95P2j9terDe/bZrbj+RZfUvifcsfIsjyylTbo4h",
      "signed_tx": "tx_+MsLAfhCuEBLCP3YkIzw1Lwp+v1F5CC/lTmlU3OvadimlI92neaONJHmwR6vXEQc1+81G8pnFeQ+37IwQyafmGaAnddSCi4PuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LYkLSN88=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422500,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhASwj92JCM8NS8Kfr9ReQgv5U5pVNzr2nYppSPdp3mjjSR5sEer1xEHNfvNRvKZxXkPt+yMEMmn5hmgJ3XUgouD7hAcJLLx5OIt9rCoyo54i0kHiGYOR8GX5up1lF5meyRet9cFsTjGlN7eWfswOpPkIgH61tcJB9qL6rINGfqLxWwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2K+VAVm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
  "id": -576460752303422500,
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhASwj92JCM8NS8Kfr9ReQgv5U5pVNzr2nYppSPdp3mjjSR5sEer1xEHNfvNRvKZxXkPt+yMEMmn5hmgJ3XUgouD7hAcJLLx5OIt9rCoyo54i0kHiGYOR8GX5up1lF5meyRet9cFsTjGlN7eWfswOpPkIgH61tcJB9qL6rINGfqLxWwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2K+VAVm",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_vaRsLTNrb5nXUsHue91ORjVqRrS3b7WpXxPmU9dm1QSUU2vM"
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhASwj92JCM8NS8Kfr9ReQgv5U5pVNzr2nYppSPdp3mjjSR5sEer1xEHNfvNRvKZxXkPt+yMEMmn5hmgJ3XUgouD7hAcJLLx5OIt9rCoyo54i0kHiGYOR8GX5up1lF5meyRet9cFsTjGlN7eWfswOpPkIgH61tcJB9qL6rINGfqLxWwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2K+VAVm",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhASwj92JCM8NS8Kfr9ReQgv5U5pVNzr2nYppSPdp3mjjSR5sEer1xEHNfvNRvKZxXkPt+yMEMmn5hmgJ3XUgouD7hAcJLLx5OIt9rCoyo54i0kHiGYOR8GX5up1lF5meyRet9cFsTjGlN7eWfswOpPkIgH61tcJB9qL6rINGfqLxWwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2K+VAVm",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhASwj92JCM8NS8Kfr9ReQgv5U5pVNzr2nYppSPdp3mjjSR5sEer1xEHNfvNRvKZxXkPt+yMEMmn5hmgJ3XUgouD7hAcJLLx5OIt9rCoyo54i0kHiGYOR8GX5up1lF5meyRet9cFsTjGlN7eWfswOpPkIgH61tcJB9qL6rINGfqLxWwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2K+VAVm",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "message": {
        "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "message": {
        "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
  "id": -576460752303422499,
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
  "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
  "id": -576460752303422499,
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "state": "tx_+QENCwH4hLhASwj92JCM8NS8Kfr9ReQgv5U5pVNzr2nYppSPdp3mjjSR5sEer1xEHNfvNRvKZxXkPt+yMEMmn5hmgJ3XUgouD7hAcJLLx5OIt9rCoyo54i0kHiGYOR8GX5up1lF5meyRet9cFsTjGlN7eWfswOpPkIgH61tcJB9qL6rINGfqLxWwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2K+VAVm"
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "state": "tx_+QENCwH4hLhASwj92JCM8NS8Kfr9ReQgv5U5pVNzr2nYppSPdp3mjjSR5sEer1xEHNfvNRvKZxXkPt+yMEMmn5hmgJ3XUgouD7hAcJLLx5OIt9rCoyo54i0kHiGYOR8GX5up1lF5meyRet9cFsTjGlN7eWfswOpPkIgH61tcJB9qL6rINGfqLxWwBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2K+VAVm"
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBrhFGfTBzLw2G7Hry+KehZlgrQ5PkdfzEStZlGdr2t7JoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7sgIAAY1OwgH0=",
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
    "signed_tx": "tx_+QHrCwH4QrhAJCB8cbA2xgcO1GCGXj1lRXtIJHQmOGYjy5m7CJe2RStBqxibp1YPlbgqyjgSDQM2Cow5HtnEmdgKn2hI3E1NA7kBovkBnzYBoQa4RRn0wcy8Nhux68vinoWZYK0OT5HX8xErWZRna9reyaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAGNVXfzo"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAJCB8cbA2xgcO1GCGXj1lRXtIJHQmOGYjy5m7CJe2RStBqxibp1YPlbgqyjgSDQM2Cow5HtnEmdgKn2hI3E1NA7kBovkBnzYBoQa4RRn0wcy8Nhux68vinoWZYK0OT5HX8xErWZRna9reyaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAGNVXfzo",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAJCB8cbA2xgcO1GCGXj1lRXtIJHQmOGYjy5m7CJe2RStBqxibp1YPlbgqyjgSDQM2Cow5HtnEmdgKn2hI3E1NA7kBovkBnzYBoQa4RRn0wcy8Nhux68vinoWZYK0OT5HX8xErWZRna9reyaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAGNVXfzo",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
  "params": {
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBrhFGfTBzLw2G7Hry+KehZlgrQ5PkdfzEStZlGdr2t7JoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXte9X0gqHaXUCg==",
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
    "signed_tx": "tx_+KcLAfhCuEDzxFPaUxifme6ixVfOjfvatfdsy3pIEE6jWlAludNaDP3swTP8vZ1VvX4DMBuY3WYd7mLXfgQ52MG/l4ZtY5gFuF/4XTgBoQa4RRn0wcy8Nhux68vinoWZYK0OT5HX8xErWZRna9reyaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17XvV9IKumdOOU="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDzxFPaUxifme6ixVfOjfvatfdsy3pIEE6jWlAludNaDP3swTP8vZ1VvX4DMBuY3WYd7mLXfgQ52MG/l4ZtY5gFuF/4XTgBoQa4RRn0wcy8Nhux68vinoWZYK0OT5HX8xErWZRna9reyaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17XvV9IKumdOOU=",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDzxFPaUxifme6ixVfOjfvatfdsy3pIEE6jWlAludNaDP3swTP8vZ1VvX4DMBuY3WYd7mLXfgQ52MG/l4ZtY5gFuF/4XTgBoQa4RRn0wcy8Nhux68vinoWZYK0OT5HX8xErWZRna9reyaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17XvV9IKumdOOU=",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
    "channel_id": "ch_2Q9vpiPXyKQiLkuJ2XCvp22XsU5WgdgBW3mSWzDTtxAY2iegqq",
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
      "fsm_id": "ba_qN7dIN8HDwaV0nJHeoSQxbYYM9arvNFtwJxsAcfV2wRHCOC8"
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
      "fsm_id": "ba_quZ2mU8FVPax61I2qJEjbNb08bDukZA19yR6nwDIYSISAtbm"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtk0mNiFg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422498,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBa6BQSnZ2TW9+Eu/JwPKQelCw8NAnJobqPtUZL5bo6ICOKF56brIfHplzm3EjQFQ13lckim8DZBu/b2/UDjEkIuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LZFG18Tg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422498,
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "fsm_id": "ba_quZ2mU8FVPax61I2qJEjbNb08bDukZA19yR6nwDIYSISAtbm",
      "signed_tx": "tx_+MsLAfhCuEBa6BQSnZ2TW9+Eu/JwPKQelCw8NAnJobqPtUZL5bo6ICOKF56brIfHplzm3EjQFQ13lckim8DZBu/b2/UDjEkIuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LZFG18Tg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422497,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAWugUEp2dk1vfhLvycDykHpQsPDQJyaG6j7VGS+W6OiAjiheem6yHx6Zc5txI0BUNd5XJIpvA2Qbv29v1A4xJCLhAaP5DtzPdpmdO0dYjs795qh0pZNKKy7nTeXASMDHZfsYbRCWkEyC9uIOFxVHIX+sGV2FgLyzgr1Aqwvjfqbs0CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2RrCfmZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
  "id": -576460752303422497,
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAWugUEp2dk1vfhLvycDykHpQsPDQJyaG6j7VGS+W6OiAjiheem6yHx6Zc5txI0BUNd5XJIpvA2Qbv29v1A4xJCLhAaP5DtzPdpmdO0dYjs795qh0pZNKKy7nTeXASMDHZfsYbRCWkEyC9uIOFxVHIX+sGV2FgLyzgr1Aqwvjfqbs0CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2RrCfmZ",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_qN7dIN8HDwaV0nJHeoSQxbYYM9arvNFtwJxsAcfV2wRHCOC8"
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAWugUEp2dk1vfhLvycDykHpQsPDQJyaG6j7VGS+W6OiAjiheem6yHx6Zc5txI0BUNd5XJIpvA2Qbv29v1A4xJCLhAaP5DtzPdpmdO0dYjs795qh0pZNKKy7nTeXASMDHZfsYbRCWkEyC9uIOFxVHIX+sGV2FgLyzgr1Aqwvjfqbs0CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2RrCfmZ",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAWugUEp2dk1vfhLvycDykHpQsPDQJyaG6j7VGS+W6OiAjiheem6yHx6Zc5txI0BUNd5XJIpvA2Qbv29v1A4xJCLhAaP5DtzPdpmdO0dYjs795qh0pZNKKy7nTeXASMDHZfsYbRCWkEyC9uIOFxVHIX+sGV2FgLyzgr1Aqwvjfqbs0CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2RrCfmZ",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAWugUEp2dk1vfhLvycDykHpQsPDQJyaG6j7VGS+W6OiAjiheem6yHx6Zc5txI0BUNd5XJIpvA2Qbv29v1A4xJCLhAaP5DtzPdpmdO0dYjs795qh0pZNKKy7nTeXASMDHZfsYbRCWkEyC9uIOFxVHIX+sGV2FgLyzgr1Aqwvjfqbs0CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2RrCfmZ",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "message": {
        "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "message": {
        "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
  "id": -576460752303422496,
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
  "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
  "id": -576460752303422496,
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "state": "tx_+QENCwH4hLhAWugUEp2dk1vfhLvycDykHpQsPDQJyaG6j7VGS+W6OiAjiheem6yHx6Zc5txI0BUNd5XJIpvA2Qbv29v1A4xJCLhAaP5DtzPdpmdO0dYjs795qh0pZNKKy7nTeXASMDHZfsYbRCWkEyC9uIOFxVHIX+sGV2FgLyzgr1Aqwvjfqbs0CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2RrCfmZ"
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "state": "tx_+QENCwH4hLhAWugUEp2dk1vfhLvycDykHpQsPDQJyaG6j7VGS+W6OiAjiheem6yHx6Zc5txI0BUNd5XJIpvA2Qbv29v1A4xJCLhAaP5DtzPdpmdO0dYjs795qh0pZNKKy7nTeXASMDHZfsYbRCWkEyC9uIOFxVHIX+sGV2FgLyzgr1Aqwvjfqbs0CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2RrCfmZ"
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBljXvrfON91D7ZJQV9aMZQalK02ZUkwXwbPgnA0eAro4oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7sgIAAZT8GYaE=",
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
    "signed_tx": "tx_+QHrCwH4QrhAY7jIdoCKXGsBgSLushGLjZE6KyPsCJ3yqvGwWdwgALhukw/UVQt2KmiSONk4Q4Pk8Rq2xHCcbmq+XCmKYNVvAbkBovkBnzYBoQZY1763zjfdQ+2SUFfWjGUGpStNmVJMF8Gz4JwNHgK6OKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAGX5Iynl"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAY7jIdoCKXGsBgSLushGLjZE6KyPsCJ3yqvGwWdwgALhukw/UVQt2KmiSONk4Q4Pk8Rq2xHCcbmq+XCmKYNVvAbkBovkBnzYBoQZY1763zjfdQ+2SUFfWjGUGpStNmVJMF8Gz4JwNHgK6OKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAGX5Iynl",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAY7jIdoCKXGsBgSLushGLjZE6KyPsCJ3yqvGwWdwgALhukw/UVQt2KmiSONk4Q4Pk8Rq2xHCcbmq+XCmKYNVvAbkBovkBnzYBoQZY1763zjfdQ+2SUFfWjGUGpStNmVJMF8Gz4JwNHgK6OKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAGX5Iynl",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
  "params": {
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBljXvrfON91D7ZJQV9aMZQalK02ZUkwXwbPgnA0eAro4oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiX/+GJGE5yoABAIYPXte9X0hmsCjFAA==",
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
    "signed_tx": "tx_+KcLAfhCuECL5GNeuBaEeZu+JEXnnQ8z+L7T6qkX1b0hgMfER2siUm469kHzNjifth/OqvH9p8BtRh0hqvfslv2Dpbg7ESkPuF/4XTgBoQZY1763zjfdQ+2SUFfWjGUGpStNmVJMF8Gz4JwNHgK6OKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGD17XvV9IZi0gQ5A="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECL5GNeuBaEeZu+JEXnnQ8z+L7T6qkX1b0hgMfER2siUm469kHzNjifth/OqvH9p8BtRh0hqvfslv2Dpbg7ESkPuF/4XTgBoQZY1763zjfdQ+2SUFfWjGUGpStNmVJMF8Gz4JwNHgK6OKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGD17XvV9IZi0gQ5A=",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECL5GNeuBaEeZu+JEXnnQ8z+L7T6qkX1b0hgMfER2siUm469kHzNjifth/OqvH9p8BtRh0hqvfslv2Dpbg7ESkPuF/4XTgBoQZY1763zjfdQ+2SUFfWjGUGpStNmVJMF8Gz4JwNHgK6OKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGD17XvV9IZi0gQ5A=",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
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
    "channel_id": "ch_g8NQ1QmmzEh8mfqLpJowW8KwfcNa9KwMVHXLS4WvymSoZNN8o",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
