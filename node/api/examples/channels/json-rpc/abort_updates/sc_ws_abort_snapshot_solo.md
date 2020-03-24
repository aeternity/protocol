
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
      "fsm_id": "ba_w9VMqh101qUfTAXtaiMB4PlrV4RfsD+rQ1SQRY8xgHv9O/Zj"
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
      "fsm_id": "ba_vQM3vw7OjLIrxfWta5wTDV8Rxzywdk60In+qZE9c+44feUBM"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBugdR7dE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422101,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEDawE33BN1ZBlC8BIM8aKvIz50DlP5nRsKisOTQxCFo87Bu6bfKDGU2CyYONtw7gmeFpSsLz1rgyYDs6WeaIo0MuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgborFIDZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422101,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "fsm_id": "ba_vQM3vw7OjLIrxfWta5wTDV8Rxzywdk60In+qZE9c+44feUBM",
      "signed_tx": "tx_+MwLAfhCuEDawE33BN1ZBlC8BIM8aKvIz50DlP5nRsKisOTQxCFo87Bu6bfKDGU2CyYONtw7gmeFpSsLz1rgyYDs6WeaIo0MuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgborFIDZ",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422100,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhApl1Uwo5oiGKlvIvdy7YktZHERvgw7Jb6zKIHLlu89VIwbPLRhSwTINKNLJmVP7utSzgtRmIpcenCH7XnaNyOB7hA2sBN9wTdWQZQvASDPGiryM+dA5T+Z0bCorDk0MQhaPOwbum3ygxlNgsmDjbcO4JnhaUrC89a4MmA7OlnmiKNDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G6o/ynKQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422100,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhApl1Uwo5oiGKlvIvdy7YktZHERvgw7Jb6zKIHLlu89VIwbPLRhSwTINKNLJmVP7utSzgtRmIpcenCH7XnaNyOB7hA2sBN9wTdWQZQvASDPGiryM+dA5T+Z0bCorDk0MQhaPOwbum3ygxlNgsmDjbcO4JnhaUrC89a4MmA7OlnmiKNDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G6o/ynKQ==",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_w9VMqh101qUfTAXtaiMB4PlrV4RfsD+rQ1SQRY8xgHv9O/Zj"
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhApl1Uwo5oiGKlvIvdy7YktZHERvgw7Jb6zKIHLlu89VIwbPLRhSwTINKNLJmVP7utSzgtRmIpcenCH7XnaNyOB7hA2sBN9wTdWQZQvASDPGiryM+dA5T+Z0bCorDk0MQhaPOwbum3ygxlNgsmDjbcO4JnhaUrC89a4MmA7OlnmiKNDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G6o/ynKQ==",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhApl1Uwo5oiGKlvIvdy7YktZHERvgw7Jb6zKIHLlu89VIwbPLRhSwTINKNLJmVP7utSzgtRmIpcenCH7XnaNyOB7hA2sBN9wTdWQZQvASDPGiryM+dA5T+Z0bCorDk0MQhaPOwbum3ygxlNgsmDjbcO4JnhaUrC89a4MmA7OlnmiKNDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G6o/ynKQ==",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhApl1Uwo5oiGKlvIvdy7YktZHERvgw7Jb6zKIHLlu89VIwbPLRhSwTINKNLJmVP7utSzgtRmIpcenCH7XnaNyOB7hA2sBN9wTdWQZQvASDPGiryM+dA5T+Z0bCorDk0MQhaPOwbum3ygxlNgsmDjbcO4JnhaUrC89a4MmA7OlnmiKNDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G6o/ynKQ==",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "message": {
        "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "message": {
        "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
  "id": -576460752303422099,
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
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422099,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "state": "tx_+QEOCwH4hLhApl1Uwo5oiGKlvIvdy7YktZHERvgw7Jb6zKIHLlu89VIwbPLRhSwTINKNLJmVP7utSzgtRmIpcenCH7XnaNyOB7hA2sBN9wTdWQZQvASDPGiryM+dA5T+Z0bCorDk0MQhaPOwbum3ygxlNgsmDjbcO4JnhaUrC89a4MmA7OlnmiKNDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G6o/ynKQ=="
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "state": "tx_+QEOCwH4hLhApl1Uwo5oiGKlvIvdy7YktZHERvgw7Jb6zKIHLlu89VIwbPLRhSwTINKNLJmVP7utSzgtRmIpcenCH7XnaNyOB7hA2sBN9wTdWQZQvASDPGiryM+dA5T+Z0bCorDk0MQhaPOwbum3ygxlNgsmDjbcO4JnhaUrC89a4MmA7OlnmiKNDLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G6o/ynKQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422098,
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
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422098,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgLlrDPrfOJCV9AW41VSutrIHPQzEHaDCVUba8TlJHeoAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAv9+CLo=",
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
  "id": -576460752303422097,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBjnZbNLJ+n965x+wZkCk1Zpf0rhIBrFmemnVhiNdum4lmwGm+zvnOytBodED0ANQD1o5NaS+LJ/S6fhHEOCY4OuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKaMpwc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422097,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBjnZbNLJ+n965x+wZkCk1Zpf0rhIBrFmemnVhiNdum4lmwGm+zvnOytBodED0ANQD1o5NaS+LJ/S6fhHEOCY4OuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKaMpwc",
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
  "id": -576460752303422096,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBjnZbNLJ+n965x+wZkCk1Zpf0rhIBrFmemnVhiNdum4lmwGm+zvnOytBodED0ANQD1o5NaS+LJ/S6fhHEOCY4OuEB5vTex55cHKZoiA53Cu73n7tLXynYdzKYOr1NjRKIDjceOH+W+D23vS04SbBHPbPpYV0k11R3xzW+H2nqwhSAFuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLSPoAV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422096,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "state": "tx_+NILAfiEuEBjnZbNLJ+n965x+wZkCk1Zpf0rhIBrFmemnVhiNdum4lmwGm+zvnOytBodED0ANQD1o5NaS+LJ/S6fhHEOCY4OuEB5vTex55cHKZoiA53Cu73n7tLXynYdzKYOr1NjRKIDjceOH+W+D23vS04SbBHPbPpYV0k11R3xzW+H2nqwhSAFuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLSPoAV"
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "state": "tx_+NILAfiEuEBjnZbNLJ+n965x+wZkCk1Zpf0rhIBrFmemnVhiNdum4lmwGm+zvnOytBodED0ANQD1o5NaS+LJ/S6fhHEOCY4OuEB5vTex55cHKZoiA53Cu73n7tLXynYdzKYOr1NjRKIDjceOH+W+D23vS04SbBHPbPpYV0k11R3xzW+H2nqwhSAFuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLSPoAV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422095,
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
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422095,
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
  "id": -576460752303422094,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422094,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBjnZbNLJ+n965x+wZkCk1Zpf0rhIBrFmemnVhiNdum4lmwGm+zvnOytBodED0ANQD1o5NaS+LJ/S6fhHEOCY4OuEB5vTex55cHKZoiA53Cu73n7tLXynYdzKYOr1NjRKIDjceOH+W+D23vS04SbBHPbPpYV0k11R3xzW+H2nqwhSAFuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLSPoAV",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422093,
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
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422093,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgLlrDPrfOJCV9AW41VSutrIHPQzEHaDCVUba8TlJHeoA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCx49HQw=",
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
  "id": -576460752303422092,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC+fzFBh0EleXQ1g4F+qSnh56KYQ325y+ait2vV2bAagkYtyezICgCpXH77dDHAp7aZcpgZ7+RNtvl2mz5Y4hoLuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvhsqa1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422092,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC+fzFBh0EleXQ1g4F+qSnh56KYQ325y+ait2vV2bAagkYtyezICgCpXH77dDHAp7aZcpgZ7+RNtvl2mz5Y4hoLuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvhsqa1",
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
  "id": -576460752303422091,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECY7QKoQtYHjUyhKEMng8p6F9YqlOO0mIchusSek/+sLngJEhdbKQDrImXkpq9TCpBGHvOexpZcrNwltc7TvC0GuEC+fzFBh0EleXQ1g4F+qSnh56KYQ325y+ait2vV2bAagkYtyezICgCpXH77dDHAp7aZcpgZ7+RNtvl2mz5Y4hoLuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvuINty"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422091,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "state": "tx_+NILAfiEuECY7QKoQtYHjUyhKEMng8p6F9YqlOO0mIchusSek/+sLngJEhdbKQDrImXkpq9TCpBGHvOexpZcrNwltc7TvC0GuEC+fzFBh0EleXQ1g4F+qSnh56KYQ325y+ait2vV2bAagkYtyezICgCpXH77dDHAp7aZcpgZ7+RNtvl2mz5Y4hoLuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvuINty"
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "state": "tx_+NILAfiEuECY7QKoQtYHjUyhKEMng8p6F9YqlOO0mIchusSek/+sLngJEhdbKQDrImXkpq9TCpBGHvOexpZcrNwltc7TvC0GuEC+fzFBh0EleXQ1g4F+qSnh56KYQ325y+ait2vV2bAagkYtyezICgCpXH77dDHAp7aZcpgZ7+RNtvl2mz5Y4hoLuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvuINty"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422090,
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
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422090,
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
  "id": -576460752303422089,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422089,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECY7QKoQtYHjUyhKEMng8p6F9YqlOO0mIchusSek/+sLngJEhdbKQDrImXkpq9TCpBGHvOexpZcrNwltc7TvC0GuEC+fzFBh0EleXQ1g4F+qSnh56KYQ325y+ait2vV2bAagkYtyezICgCpXH77dDHAp7aZcpgZ7+RNtvl2mz5Y4hoLuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvuINty",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "signed_tx": "tx_+QEvCwHAuQEp+QEmOwGhBgLlrDPrfOJCV9AW41VSutrIHPQzEHaDCVUba8TlJHeooQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuECY7QKoQtYHjUyhKEMng8p6F9YqlOO0mIchusSek/+sLngJEhdbKQDrImXkpq9TCpBGHvOexpZcrNwltc7TvC0GuEC+fzFBh0EleXQ1g4F+qSnh56KYQ325y+ait2vV2bAagkYtyezICgCpXH77dDHAp7aZcpgZ7+RNtvl2mz5Y4hoLuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMLeUL4AIG7b3uaqg==",
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
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBgLlrDPrfOJCV9AW41VSutrIHPQzEHaDCVUba8TlJHeooQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuECY7QKoQtYHjUyhKEMng8p6F9YqlOO0mIchusSek/+sLngJEhdbKQDrImXkpq9TCpBGHvOexpZcrNwltc7TvC0GuEC+fzFBh0EleXQ1g4F+qSnh56KYQ325y+ait2vV2bAagkYtyezICgCpXH77dDHAp7aZcpgZ7+RNtvl2mz5Y4hoLuEj4RjkCoQYC5awz63ziQlfQFuNVUrrayBz0MxB2gwlVG2vE5SR3qAOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMG0SswAEGYK0cA",
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
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422088,
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
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422088,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422087,
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
    "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
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
  "channel_id": "ch_2H1EaCQ5MgM3WUnWm7uCZzLng2DL8a4Ey55EiuAjLLhqPt9VW",
  "id": -576460752303422087,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
