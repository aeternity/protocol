
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
      "fsm_id": "ba_yMf62AkMZea8/lRS1wFNWyxFEAxZ0k4EbPZqF6KyAnxFa0PU"
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
      "fsm_id": "ba_zadzu+00iXRaXKjQs5coS/XLbCwqS+MRLUdhOmn9JBOr/fek"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs8hfiULg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422665,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDCdubq2UTQCILgvYQwRGokuwT1dzPA+vZHshO9tz34bUdHvVhGAvkZ1LYqZIxvlyMpaeb4KMMbD9S1reyRpIIJuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LPFLzfbg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422665,
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "fsm_id": "ba_zadzu+00iXRaXKjQs5coS/XLbCwqS+MRLUdhOmn9JBOr/fek",
      "signed_tx": "tx_+MsLAfhCuEDCdubq2UTQCILgvYQwRGokuwT1dzPA+vZHshO9tz34bUdHvVhGAvkZ1LYqZIxvlyMpaeb4KMMbD9S1reyRpIIJuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LPFLzfbg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422664,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAwnbm6tlE0AiC4L2EMERqJLsE9XczwPr2R7ITvbc9+G1HR71YRgL5GdS2KmSMb5cjKWnm+CjDGw/Uta3skaSCCbhAz3z/dFfTW3w+kCtq26wDXXH2wcaU03ez42bAa5aUrgxntZcg5qH7es+b3oAwI334zFd6tFZHQrP1vYi/d9BYBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzxYaBDg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
  "id": -576460752303422664,
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAwnbm6tlE0AiC4L2EMERqJLsE9XczwPr2R7ITvbc9+G1HR71YRgL5GdS2KmSMb5cjKWnm+CjDGw/Uta3skaSCCbhAz3z/dFfTW3w+kCtq26wDXXH2wcaU03ez42bAa5aUrgxntZcg5qH7es+b3oAwI334zFd6tFZHQrP1vYi/d9BYBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzxYaBDg",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_yMf62AkMZea8/lRS1wFNWyxFEAxZ0k4EbPZqF6KyAnxFa0PU"
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAwnbm6tlE0AiC4L2EMERqJLsE9XczwPr2R7ITvbc9+G1HR71YRgL5GdS2KmSMb5cjKWnm+CjDGw/Uta3skaSCCbhAz3z/dFfTW3w+kCtq26wDXXH2wcaU03ez42bAa5aUrgxntZcg5qH7es+b3oAwI334zFd6tFZHQrP1vYi/d9BYBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzxYaBDg",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAwnbm6tlE0AiC4L2EMERqJLsE9XczwPr2R7ITvbc9+G1HR71YRgL5GdS2KmSMb5cjKWnm+CjDGw/Uta3skaSCCbhAz3z/dFfTW3w+kCtq26wDXXH2wcaU03ez42bAa5aUrgxntZcg5qH7es+b3oAwI334zFd6tFZHQrP1vYi/d9BYBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzxYaBDg",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAwnbm6tlE0AiC4L2EMERqJLsE9XczwPr2R7ITvbc9+G1HR71YRgL5GdS2KmSMb5cjKWnm+CjDGw/Uta3skaSCCbhAz3z/dFfTW3w+kCtq26wDXXH2wcaU03ez42bAa5aUrgxntZcg5qH7es+b3oAwI334zFd6tFZHQrP1vYi/d9BYBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzxYaBDg",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
  "id": -576460752303422663,
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
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
  "id": -576460752303422663,
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "state": "tx_+QENCwH4hLhAwnbm6tlE0AiC4L2EMERqJLsE9XczwPr2R7ITvbc9+G1HR71YRgL5GdS2KmSMb5cjKWnm+CjDGw/Uta3skaSCCbhAz3z/dFfTW3w+kCtq26wDXXH2wcaU03ez42bAa5aUrgxntZcg5qH7es+b3oAwI334zFd6tFZHQrP1vYi/d9BYBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzxYaBDg"
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "state": "tx_+QENCwH4hLhAwnbm6tlE0AiC4L2EMERqJLsE9XczwPr2R7ITvbc9+G1HR71YRgL5GdS2KmSMb5cjKWnm+CjDGw/Uta3skaSCCbhAz3z/dFfTW3w+kCtq26wDXXH2wcaU03ez42bAa5aUrgxntZcg5qH7es+b3oAwI334zFd6tFZHQrP1vYi/d9BYBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzxYaBDg"
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBriVuHWz0MstvKGaaIGnJBuLgPoe1RrbAti0OkqBCLFvoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhnBIhhsPP6D6aIyRp0q4njYpKUN7EoE8dGS1wKGxithIYn6oqM3YIgI9VmrMKA==",
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
  "id": -576460752303422662,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDeSKXiIH4faGol0oOZOxCKtjN8pWp4WVtXSxTBh1Fb4OVaCYl9eKB1Tx85Ysv9Z6R2vIGe+I5p1T+yFSRp2W0AuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICPaQWZqE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
  "id": -576460752303422662,
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDeSKXiIH4faGol0oOZOxCKtjN8pWp4WVtXSxTBh1Fb4OVaCYl9eKB1Tx85Ysv9Z6R2vIGe+I5p1T+yFSRp2W0AuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICPaQWZqE=",
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
  "id": -576460752303422661,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECNHYDFULwCOV6LGnVphsUOqrzFpdFraCudZJWAQ9++M6+En75/Cks5aTvyawJ/WI/LnWNbR/jxavJug129qMIDuEDeSKXiIH4faGol0oOZOxCKtjN8pWp4WVtXSxTBh1Fb4OVaCYl9eKB1Tx85Ysv9Z6R2vIGe+I5p1T+yFSRp2W0AuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICPc3pVE0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
  "id": -576460752303422661,
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECNHYDFULwCOV6LGnVphsUOqrzFpdFraCudZJWAQ9++M6+En75/Cks5aTvyawJ/WI/LnWNbR/jxavJug129qMIDuEDeSKXiIH4faGol0oOZOxCKtjN8pWp4WVtXSxTBh1Fb4OVaCYl9eKB1Tx85Ysv9Z6R2vIGe+I5p1T+yFSRp2W0AuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICPc3pVE0=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECNHYDFULwCOV6LGnVphsUOqrzFpdFraCudZJWAQ9++M6+En75/Cks5aTvyawJ/WI/LnWNbR/jxavJug129qMIDuEDeSKXiIH4faGol0oOZOxCKtjN8pWp4WVtXSxTBh1Fb4OVaCYl9eKB1Tx85Ysv9Z6R2vIGe+I5p1T+yFSRp2W0AuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICPc3pVE0=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECNHYDFULwCOV6LGnVphsUOqrzFpdFraCudZJWAQ9++M6+En75/Cks5aTvyawJ/WI/LnWNbR/jxavJug129qMIDuEDeSKXiIH4faGol0oOZOxCKtjN8pWp4WVtXSxTBh1Fb4OVaCYl9eKB1Tx85Ysv9Z6R2vIGe+I5p1T+yFSRp2W0AuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICPc3pVE0=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECNHYDFULwCOV6LGnVphsUOqrzFpdFraCudZJWAQ9++M6+En75/Cks5aTvyawJ/WI/LnWNbR/jxavJug129qMIDuEDeSKXiIH4faGol0oOZOxCKtjN8pWp4WVtXSxTBh1Fb4OVaCYl9eKB1Tx85Ysv9Z6R2vIGe+I5p1T+yFSRp2W0AuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICPc3pVE0=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "state": "tx_+P4LAfiEuECNHYDFULwCOV6LGnVphsUOqrzFpdFraCudZJWAQ9++M6+En75/Cks5aTvyawJ/WI/LnWNbR/jxavJug129qMIDuEDeSKXiIH4faGol0oOZOxCKtjN8pWp4WVtXSxTBh1Fb4OVaCYl9eKB1Tx85Ysv9Z6R2vIGe+I5p1T+yFSRp2W0AuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICPc3pVE0="
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "state": "tx_+P4LAfiEuECNHYDFULwCOV6LGnVphsUOqrzFpdFraCudZJWAQ9++M6+En75/Cks5aTvyawJ/WI/LnWNbR/jxavJug129qMIDuEDeSKXiIH4faGol0oOZOxCKtjN8pWp4WVtXSxTBh1Fb4OVaCYl9eKB1Tx85Ysv9Z6R2vIGe+I5p1T+yFSRp2W0AuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIZwSIYbDz+g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICPc3pVE0="
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBriVuHWz0MstvKGaaIGnJBuLgPoe1RrbAti0OkqBCLFvoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhnBIhhsPP6BIWkDp9eRQQRyHm8U+8URorUUQQNdonwOQZqEaw6yolgMYxIV7jA==",
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
  "id": -576460752303422660,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECyB72RTzeEDJFTlBbUlY0wl9yh+het0VFpviT0iEukXWXH+fo+pCNKQIfJkFcAIfsEHBvxsBjWxgGTs7xAO1MIuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDGC0agg4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
  "id": -576460752303422660,
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECyB72RTzeEDJFTlBbUlY0wl9yh+het0VFpviT0iEukXWXH+fo+pCNKQIfJkFcAIfsEHBvxsBjWxgGTs7xAO1MIuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDGC0agg4=",
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
  "id": -576460752303422659,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAod/ri/dTM0+lEghglAl+8z+S+wN3TVY0dEdn03OrWi6uqWgJIUuaLbvdxF0LNeY3uTR6YXvK8ys0oniwRZeIDuECyB72RTzeEDJFTlBbUlY0wl9yh+het0VFpviT0iEukXWXH+fo+pCNKQIfJkFcAIfsEHBvxsBjWxgGTs7xAO1MIuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDGMXwAZc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
  "id": -576460752303422659,
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAod/ri/dTM0+lEghglAl+8z+S+wN3TVY0dEdn03OrWi6uqWgJIUuaLbvdxF0LNeY3uTR6YXvK8ys0oniwRZeIDuECyB72RTzeEDJFTlBbUlY0wl9yh+het0VFpviT0iEukXWXH+fo+pCNKQIfJkFcAIfsEHBvxsBjWxgGTs7xAO1MIuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDGMXwAZc=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAod/ri/dTM0+lEghglAl+8z+S+wN3TVY0dEdn03OrWi6uqWgJIUuaLbvdxF0LNeY3uTR6YXvK8ys0oniwRZeIDuECyB72RTzeEDJFTlBbUlY0wl9yh+het0VFpviT0iEukXWXH+fo+pCNKQIfJkFcAIfsEHBvxsBjWxgGTs7xAO1MIuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDGMXwAZc=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "message": {
        "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAod/ri/dTM0+lEghglAl+8z+S+wN3TVY0dEdn03OrWi6uqWgJIUuaLbvdxF0LNeY3uTR6YXvK8ys0oniwRZeIDuECyB72RTzeEDJFTlBbUlY0wl9yh+het0VFpviT0iEukXWXH+fo+pCNKQIfJkFcAIfsEHBvxsBjWxgGTs7xAO1MIuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDGMXwAZc=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAod/ri/dTM0+lEghglAl+8z+S+wN3TVY0dEdn03OrWi6uqWgJIUuaLbvdxF0LNeY3uTR6YXvK8ys0oniwRZeIDuECyB72RTzeEDJFTlBbUlY0wl9yh+het0VFpviT0iEukXWXH+fo+pCNKQIfJkFcAIfsEHBvxsBjWxgGTs7xAO1MIuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDGMXwAZc=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "state": "tx_+P4LAfiEuEAod/ri/dTM0+lEghglAl+8z+S+wN3TVY0dEdn03OrWi6uqWgJIUuaLbvdxF0LNeY3uTR6YXvK8ys0oniwRZeIDuECyB72RTzeEDJFTlBbUlY0wl9yh+het0VFpviT0iEukXWXH+fo+pCNKQIfJkFcAIfsEHBvxsBjWxgGTs7xAO1MIuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDGMXwAZc="
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "state": "tx_+P4LAfiEuEAod/ri/dTM0+lEghglAl+8z+S+wN3TVY0dEdn03OrWi6uqWgJIUuaLbvdxF0LNeY3uTR6YXvK8ys0oniwRZeIDuECyB72RTzeEDJFTlBbUlY0wl9yh+het0VFpviT0iEukXWXH+fo+pCNKQIfJkFcAIfsEHBvxsBjWxgGTs7xAO1MIuHT4cjQBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIZwSIYbDz+gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDGMXwAZc="
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBriVuHWz0MstvKGaaIGnJBuLgPoe1RrbAti0OkqBCLFvoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/2GHLHOiuv/AIYPXtZ/KAA+qQvIUw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422658,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAhVG8sbBYJ4TR8wz72waK/aFJxdF59gPzncRsl6mJVi0VgkNoEqPsBhkpaj/4CMxSx0cdcCqFrtqlFGonhALEFuF/4XTUBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAPrgRlNY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
  "id": -576460752303422658,
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAhVG8sbBYJ4TR8wz72waK/aFJxdF59gPzncRsl6mJVi0VgkNoEqPsBhkpaj/4CMxSx0cdcCqFrtqlFGonhALEFuF/4XTUBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAPrgRlNY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422657,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAhVG8sbBYJ4TR8wz72waK/aFJxdF59gPzncRsl6mJVi0VgkNoEqPsBhkpaj/4CMxSx0cdcCqFrtqlFGonhALEFuEBqLbKWV48oB1uoc3h58B4GiH7JT+kEja07wV8tor3ABfIbfg4gxQyaO1yb8K0KFAatzVsnjbBaMYgpTxEmo1IBuF/4XTUBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAPi7vA8A="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
  "id": -576460752303422657,
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAhVG8sbBYJ4TR8wz72waK/aFJxdF59gPzncRsl6mJVi0VgkNoEqPsBhkpaj/4CMxSx0cdcCqFrtqlFGonhALEFuEBqLbKWV48oB1uoc3h58B4GiH7JT+kEja07wV8tor3ABfIbfg4gxQyaO1yb8K0KFAatzVsnjbBaMYgpTxEmo1IBuF/4XTUBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAPi7vA8A=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAhVG8sbBYJ4TR8wz72waK/aFJxdF59gPzncRsl6mJVi0VgkNoEqPsBhkpaj/4CMxSx0cdcCqFrtqlFGonhALEFuEBqLbKWV48oB1uoc3h58B4GiH7JT+kEja07wV8tor3ABfIbfg4gxQyaO1yb8K0KFAatzVsnjbBaMYgpTxEmo1IBuF/4XTUBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAPi7vA8A=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAhVG8sbBYJ4TR8wz72waK/aFJxdF59gPzncRsl6mJVi0VgkNoEqPsBhkpaj/4CMxSx0cdcCqFrtqlFGonhALEFuEBqLbKWV48oB1uoc3h58B4GiH7JT+kEja07wV8tor3ABfIbfg4gxQyaO1yb8K0KFAatzVsnjbBaMYgpTxEmo1IBuF/4XTUBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAPi7vA8A=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAhVG8sbBYJ4TR8wz72waK/aFJxdF59gPzncRsl6mJVi0VgkNoEqPsBhkpaj/4CMxSx0cdcCqFrtqlFGonhALEFuEBqLbKWV48oB1uoc3h58B4GiH7JT+kEja07wV8tor3ABfIbfg4gxQyaO1yb8K0KFAatzVsnjbBaMYgpTxEmo1IBuF/4XTUBoQa4lbh1s9DLLbyhmmiBpyQbi4D6HtUa2wLYtDpKgQixb6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAPi7vA8A=",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
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
    "channel_id": "ch_2QHyPJwPrP3cjg2iuXfPgRynzmXEmTyPVGkwsXrvstPyfWPcW7",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
