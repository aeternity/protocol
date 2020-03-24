
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_EhsNt6OH/O2dMALvD2qsrz0Et88gPIXHgize4F1f8dGWHo9Y"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_sVejwYlZ0hRg8fbDWj9P0KmjzTmPcBLViFb09JCfhwzJei1e"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsCpM2u4g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423486,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBsPydZNg+goELeON5BcK2p3Lhw2to7MjBnPV6kL5pArGdgt3W+0r0pvdq8hZLUZDNvKmm6qHoZ3cG/rNj6tYIEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAimvhcc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423486,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "fsm_id": "ba_sVejwYlZ0hRg8fbDWj9P0KmjzTmPcBLViFb09JCfhwzJei1e",
      "signed_tx": "tx_+MsLAfhCuEBsPydZNg+goELeON5BcK2p3Lhw2to7MjBnPV6kL5pArGdgt3W+0r0pvdq8hZLUZDNvKmm6qHoZ3cG/rNj6tYIEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAimvhcc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAbD8nWTYPoKBC3jjeQXCtqdy4cNraOzIwZz1epC+aQKxnYLd1vtK9Kb3avIWS1GQzbyppuqh6Gd3Bv6zY+rWCBLhAftoWnacHBi5iQA0Jh9GeYmPMVrAzxMgOyciwQebpr6OX0jLfrrs8jnbgg9aZsUn6S6fL+lBrTsui5GMVeuoFC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwJlc+sY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423485,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAbD8nWTYPoKBC3jjeQXCtqdy4cNraOzIwZz1epC+aQKxnYLd1vtK9Kb3avIWS1GQzbyppuqh6Gd3Bv6zY+rWCBLhAftoWnacHBi5iQA0Jh9GeYmPMVrAzxMgOyciwQebpr6OX0jLfrrs8jnbgg9aZsUn6S6fL+lBrTsui5GMVeuoFC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwJlc+sY",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_EhsNt6OH/O2dMALvD2qsrz0Et88gPIXHgize4F1f8dGWHo9Y"
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAbD8nWTYPoKBC3jjeQXCtqdy4cNraOzIwZz1epC+aQKxnYLd1vtK9Kb3avIWS1GQzbyppuqh6Gd3Bv6zY+rWCBLhAftoWnacHBi5iQA0Jh9GeYmPMVrAzxMgOyciwQebpr6OX0jLfrrs8jnbgg9aZsUn6S6fL+lBrTsui5GMVeuoFC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwJlc+sY",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbD8nWTYPoKBC3jjeQXCtqdy4cNraOzIwZz1epC+aQKxnYLd1vtK9Kb3avIWS1GQzbyppuqh6Gd3Bv6zY+rWCBLhAftoWnacHBi5iQA0Jh9GeYmPMVrAzxMgOyciwQebpr6OX0jLfrrs8jnbgg9aZsUn6S6fL+lBrTsui5GMVeuoFC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwJlc+sY",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbD8nWTYPoKBC3jjeQXCtqdy4cNraOzIwZz1epC+aQKxnYLd1vtK9Kb3avIWS1GQzbyppuqh6Gd3Bv6zY+rWCBLhAftoWnacHBi5iQA0Jh9GeYmPMVrAzxMgOyciwQebpr6OX0jLfrrs8jnbgg9aZsUn6S6fL+lBrTsui5GMVeuoFC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwJlc+sY",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+QENCwH4hLhAbD8nWTYPoKBC3jjeQXCtqdy4cNraOzIwZz1epC+aQKxnYLd1vtK9Kb3avIWS1GQzbyppuqh6Gd3Bv6zY+rWCBLhAftoWnacHBi5iQA0Jh9GeYmPMVrAzxMgOyciwQebpr6OX0jLfrrs8jnbgg9aZsUn6S6fL+lBrTsui5GMVeuoFC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwJlc+sY"
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+QENCwH4hLhAbD8nWTYPoKBC3jjeQXCtqdy4cNraOzIwZz1epC+aQKxnYLd1vtK9Kb3avIWS1GQzbyppuqh6Gd3Bv6zY+rWCBLhAftoWnacHBi5iQA0Jh9GeYmPMVrAzxMgOyciwQebpr6OX0jLfrrs8jnbgg9aZsUn6S6fL+lBrTsui5GMVeuoFC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwJlc+sY"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "message": {
        "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "message": {
        "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "id": -576460752303423484,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423484,
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
  "id": -576460752303423483,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423483,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtd0ak8OigTxdidMooT7LVVYvy+0Sznv74QF7gxOxdOqAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAvL1ZAE=",
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
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAye9gcv5pLw/BtPZfvmiSF1m7AW+dDK8B34ndc8ZNVnybSmGbKPdtfB9y0dBpg/o5wHo2o1q9kPBN0o9HJkTsMuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5VUGV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423482,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAye9gcv5pLw/BtPZfvmiSF1m7AW+dDK8B34ndc8ZNVnybSmGbKPdtfB9y0dBpg/o5wHo2o1q9kPBN0o9HJkTsMuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5VUGV",
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
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAye9gcv5pLw/BtPZfvmiSF1m7AW+dDK8B34ndc8ZNVnybSmGbKPdtfB9y0dBpg/o5wHo2o1q9kPBN0o9HJkTsMuEAy6nOzd2qbUYAFxhXED2TzOXw+AtEw0oX2SgcPdrBxeOJtJqCu5vf01+YllurhRpEBVXA7WIk3giQ+EEqPhJwGuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ7Mw8/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423481,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEAye9gcv5pLw/BtPZfvmiSF1m7AW+dDK8B34ndc8ZNVnybSmGbKPdtfB9y0dBpg/o5wHo2o1q9kPBN0o9HJkTsMuEAy6nOzd2qbUYAFxhXED2TzOXw+AtEw0oX2SgcPdrBxeOJtJqCu5vf01+YllurhRpEBVXA7WIk3giQ+EEqPhJwGuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ7Mw8/"
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEAye9gcv5pLw/BtPZfvmiSF1m7AW+dDK8B34ndc8ZNVnybSmGbKPdtfB9y0dBpg/o5wHo2o1q9kPBN0o9HJkTsMuEAy6nOzd2qbUYAFxhXED2TzOXw+AtEw0oX2SgcPdrBxeOJtJqCu5vf01+YllurhRpEBVXA7WIk3giQ+EEqPhJwGuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ7Mw8/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423480,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423480,
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
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAye9gcv5pLw/BtPZfvmiSF1m7AW+dDK8B34ndc8ZNVnybSmGbKPdtfB9y0dBpg/o5wHo2o1q9kPBN0o9HJkTsMuEAy6nOzd2qbUYAFxhXED2TzOXw+AtEw0oX2SgcPdrBxeOJtJqCu5vf01+YllurhRpEBVXA7WIk3giQ+EEqPhJwGuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ7Mw8/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423478,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423478,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtd0ak8OigTxdidMooT7LVVYvy+0Sznv74QF7gxOxdOqA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC9W8zSg=",
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
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDm0X8xUWFLogwxqvL+NEFIDhpoSBfjn8aQJID4QfIBOHAySTpt44hACsXUPB8lEFE3kFXFc5sWYgoTe1qm5BAIuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtZcXjE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423477,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDm0X8xUWFLogwxqvL+NEFIDhpoSBfjn8aQJID4QfIBOHAySTpt44hACsXUPB8lEFE3kFXFc5sWYgoTe1qm5BAIuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtZcXjE",
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
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAHRI+BT3r0uzWqcFqUXUmHsjK393YkJeYsrucsaYFX8bunVwghkoxgl2uE07+8rOSWMPzlb8+Oj4TxyeKadWUEuEDm0X8xUWFLogwxqvL+NEFIDhpoSBfjn8aQJID4QfIBOHAySTpt44hACsXUPB8lEFE3kFXFc5sWYgoTe1qm5BAIuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguadb8w"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423476,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEAHRI+BT3r0uzWqcFqUXUmHsjK393YkJeYsrucsaYFX8bunVwghkoxgl2uE07+8rOSWMPzlb8+Oj4TxyeKadWUEuEDm0X8xUWFLogwxqvL+NEFIDhpoSBfjn8aQJID4QfIBOHAySTpt44hACsXUPB8lEFE3kFXFc5sWYgoTe1qm5BAIuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguadb8w"
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEAHRI+BT3r0uzWqcFqUXUmHsjK393YkJeYsrucsaYFX8bunVwghkoxgl2uE07+8rOSWMPzlb8+Oj4TxyeKadWUEuEDm0X8xUWFLogwxqvL+NEFIDhpoSBfjn8aQJID4QfIBOHAySTpt44hACsXUPB8lEFE3kFXFc5sWYgoTe1qm5BAIuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguadb8w"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423475,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423475,
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
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAHRI+BT3r0uzWqcFqUXUmHsjK393YkJeYsrucsaYFX8bunVwghkoxgl2uE07+8rOSWMPzlb8+Oj4TxyeKadWUEuEDm0X8xUWFLogwxqvL+NEFIDhpoSBfjn8aQJID4QfIBOHAySTpt44hACsXUPB8lEFE3kFXFc5sWYgoTe1qm5BAIuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguadb8w",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423473,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423473,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtd0ak8OigTxdidMooT7LVVYvy+0Sznv74QF7gxOxdOqBKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMe5exCo=",
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
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAzo4ovnMexMvA1yxM7XKyI5GNy4rMLfgjiZo7fc4p/7ePD7uEkLSXZbX7HaQgKKnvpdSIlu+/TxrchR34Q6rEPuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGxK/99"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423472,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAzo4ovnMexMvA1yxM7XKyI5GNy4rMLfgjiZo7fc4p/7ePD7uEkLSXZbX7HaQgKKnvpdSIlu+/TxrchR34Q6rEPuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGxK/99",
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
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAv+ifKwL0lUJDgpxaiaVOg61a1WVJB6xdCYOpsjFJ/8rmrHXT+SLX/g86UkbA/hzpd6ictdHEtQdrGETIeN5ELuEAzo4ovnMexMvA1yxM7XKyI5GNy4rMLfgjiZo7fc4p/7ePD7uEkLSXZbX7HaQgKKnvpdSIlu+/TxrchR34Q6rEPuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGNGkuG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423471,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEAv+ifKwL0lUJDgpxaiaVOg61a1WVJB6xdCYOpsjFJ/8rmrHXT+SLX/g86UkbA/hzpd6ictdHEtQdrGETIeN5ELuEAzo4ovnMexMvA1yxM7XKyI5GNy4rMLfgjiZo7fc4p/7ePD7uEkLSXZbX7HaQgKKnvpdSIlu+/TxrchR34Q6rEPuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGNGkuG"
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEAv+ifKwL0lUJDgpxaiaVOg61a1WVJB6xdCYOpsjFJ/8rmrHXT+SLX/g86UkbA/hzpd6ictdHEtQdrGETIeN5ELuEAzo4ovnMexMvA1yxM7XKyI5GNy4rMLfgjiZo7fc4p/7ePD7uEkLSXZbX7HaQgKKnvpdSIlu+/TxrchR34Q6rEPuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGNGkuG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423470,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423470,
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
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAv+ifKwL0lUJDgpxaiaVOg61a1WVJB6xdCYOpsjFJ/8rmrHXT+SLX/g86UkbA/hzpd6ictdHEtQdrGETIeN5ELuEAzo4ovnMexMvA1yxM7XKyI5GNy4rMLfgjiZo7fc4p/7ePD7uEkLSXZbX7HaQgKKnvpdSIlu+/TxrchR34Q6rEPuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGNGkuG",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423468,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423468,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtd0ak8OigTxdidMooT7LVVYvy+0Sznv74QF7gxOxdOqBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC8ZJyh0=",
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
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA5f20NVGqTEdDUBZyQ7Af+EKoBe7hiwDvliJAPMju7VWEJ3xAcUP6y/Y3OBv9/GOHMqFVFY6PYHi1WiYvHeo0HuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguxlLVe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423467,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA5f20NVGqTEdDUBZyQ7Af+EKoBe7hiwDvliJAPMju7VWEJ3xAcUP6y/Y3OBv9/GOHMqFVFY6PYHi1WiYvHeo0HuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguxlLVe",
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
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA5f20NVGqTEdDUBZyQ7Af+EKoBe7hiwDvliJAPMju7VWEJ3xAcUP6y/Y3OBv9/GOHMqFVFY6PYHi1WiYvHeo0HuECQZaLoXazhBCIkTPxr8BloS7TxuBPZ0x3KJzvq3uklXzI+jm8nCCko7sQgwQYiDwqMoR7jv4CpdVHuwe/7K0sHuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgugPF9a"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423466,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEA5f20NVGqTEdDUBZyQ7Af+EKoBe7hiwDvliJAPMju7VWEJ3xAcUP6y/Y3OBv9/GOHMqFVFY6PYHi1WiYvHeo0HuECQZaLoXazhBCIkTPxr8BloS7TxuBPZ0x3KJzvq3uklXzI+jm8nCCko7sQgwQYiDwqMoR7jv4CpdVHuwe/7K0sHuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgugPF9a"
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEA5f20NVGqTEdDUBZyQ7Af+EKoBe7hiwDvliJAPMju7VWEJ3xAcUP6y/Y3OBv9/GOHMqFVFY6PYHi1WiYvHeo0HuECQZaLoXazhBCIkTPxr8BloS7TxuBPZ0x3KJzvq3uklXzI+jm8nCCko7sQgwQYiDwqMoR7jv4CpdVHuwe/7K0sHuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgugPF9a"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423465,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423465,
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
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA5f20NVGqTEdDUBZyQ7Af+EKoBe7hiwDvliJAPMju7VWEJ3xAcUP6y/Y3OBv9/GOHMqFVFY6PYHi1WiYvHeo0HuECQZaLoXazhBCIkTPxr8BloS7TxuBPZ0x3KJzvq3uklXzI+jm8nCCko7sQgwQYiDwqMoR7jv4CpdVHuwe/7K0sHuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgugPF9a",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423463,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423463,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtd0ak8OigTxdidMooT7LVVYvy+0Sznv74QF7gxOxdOqBqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMat2Xwk=",
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
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDUaY6vithLFWu5F9ERwCB8taWSN0RdHAL8gfnT6MJ3v1UJ8U/mfoxt/ilMzSprCdcXGNjO8AL1MXUt0oWNkZAMuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFjIbAu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423462,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDUaY6vithLFWu5F9ERwCB8taWSN0RdHAL8gfnT6MJ3v1UJ8U/mfoxt/ilMzSprCdcXGNjO8AL1MXUt0oWNkZAMuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFjIbAu",
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
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAun6JKRf0+nwCIDR/9Vh3jms/GUz6WMW8xVXfgXp0F8Ok6CVeijHzKHKcgm55SkGq+s5tPlIxkCANfRJoD6fsJuEDUaY6vithLFWu5F9ERwCB8taWSN0RdHAL8gfnT6MJ3v1UJ8U/mfoxt/ilMzSprCdcXGNjO8AL1MXUt0oWNkZAMuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFKb85O"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423461,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEAun6JKRf0+nwCIDR/9Vh3jms/GUz6WMW8xVXfgXp0F8Ok6CVeijHzKHKcgm55SkGq+s5tPlIxkCANfRJoD6fsJuEDUaY6vithLFWu5F9ERwCB8taWSN0RdHAL8gfnT6MJ3v1UJ8U/mfoxt/ilMzSprCdcXGNjO8AL1MXUt0oWNkZAMuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFKb85O"
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
    "data": {
      "state": "tx_+NILAfiEuEAun6JKRf0+nwCIDR/9Vh3jms/GUz6WMW8xVXfgXp0F8Ok6CVeijHzKHKcgm55SkGq+s5tPlIxkCANfRJoD6fsJuEDUaY6vithLFWu5F9ERwCB8taWSN0RdHAL8gfnT6MJ3v1UJ8U/mfoxt/ilMzSprCdcXGNjO8AL1MXUt0oWNkZAMuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFKb85O"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423460,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423460,
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
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAun6JKRf0+nwCIDR/9Vh3jms/GUz6WMW8xVXfgXp0F8Ok6CVeijHzKHKcgm55SkGq+s5tPlIxkCANfRJoD6fsJuEDUaY6vithLFWu5F9ERwCB8taWSN0RdHAL8gfnT6MJ3v1UJ8U/mfoxt/ilMzSprCdcXGNjO8AL1MXUt0oWNkZAMuEj4RjkCoQbXdGpPDooE8XYnTKKE+y1VWL8vtEs57++EBe4MTsXTqgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFKb85O",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423458,
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423457,
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
    "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
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
  "channel_id": "ch_2dtW8tXS359VXQU8u23zZdaYJg1Ma8tEQ8uRChYzduwAApPqjG",
  "id": -576460752303423457,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
