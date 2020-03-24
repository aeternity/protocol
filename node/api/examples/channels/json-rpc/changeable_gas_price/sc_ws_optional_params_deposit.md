
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
      "fsm_id": "ba_3vdmcUD7AwEQH0Ir+flqYV8jxBshD/8NLjtbL3EWEd1ks80q"
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
      "fsm_id": "ba_mZVeFGvJLhykUOamcHYUG5waumhecHC9YY/yCy6vBbadF7df"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtRtqzawA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422582,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAPxy1u3RJLrdKVvsCvQBcZbr0t1A19k61+8+FQbUL++xcQbJOWBRlDq4XfjQDQEU7tFjYsg9HeoXl3kUmLzrAAuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LUdlBoYI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422582,
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "fsm_id": "ba_mZVeFGvJLhykUOamcHYUG5waumhecHC9YY/yCy6vBbadF7df",
      "signed_tx": "tx_+MsLAfhCuEAPxy1u3RJLrdKVvsCvQBcZbr0t1A19k61+8+FQbUL++xcQbJOWBRlDq4XfjQDQEU7tFjYsg9HeoXl3kUmLzrAAuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LUdlBoYI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422581,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAD8ctbt0SS63Slb7Ar0AXGW69LdQNfZOtfvPhUG1C/vsXEGyTlgUZQ6uF340A0BFO7RY2LIPR3qF5d5FJi86wALhA6rMACIjq0UOqLl33iaFYtMHbHPTYWNc2iOBKnSa4etv/y2vXa7hpJW7pUbLjNRKzRnyvSxnSf2oNMkRJo+AWD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1GS90hc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
  "id": -576460752303422581,
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAD8ctbt0SS63Slb7Ar0AXGW69LdQNfZOtfvPhUG1C/vsXEGyTlgUZQ6uF340A0BFO7RY2LIPR3qF5d5FJi86wALhA6rMACIjq0UOqLl33iaFYtMHbHPTYWNc2iOBKnSa4etv/y2vXa7hpJW7pUbLjNRKzRnyvSxnSf2oNMkRJo+AWD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1GS90hc",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_3vdmcUD7AwEQH0Ir+flqYV8jxBshD/8NLjtbL3EWEd1ks80q"
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAD8ctbt0SS63Slb7Ar0AXGW69LdQNfZOtfvPhUG1C/vsXEGyTlgUZQ6uF340A0BFO7RY2LIPR3qF5d5FJi86wALhA6rMACIjq0UOqLl33iaFYtMHbHPTYWNc2iOBKnSa4etv/y2vXa7hpJW7pUbLjNRKzRnyvSxnSf2oNMkRJo+AWD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1GS90hc",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAD8ctbt0SS63Slb7Ar0AXGW69LdQNfZOtfvPhUG1C/vsXEGyTlgUZQ6uF340A0BFO7RY2LIPR3qF5d5FJi86wALhA6rMACIjq0UOqLl33iaFYtMHbHPTYWNc2iOBKnSa4etv/y2vXa7hpJW7pUbLjNRKzRnyvSxnSf2oNMkRJo+AWD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1GS90hc",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAD8ctbt0SS63Slb7Ar0AXGW69LdQNfZOtfvPhUG1C/vsXEGyTlgUZQ6uF340A0BFO7RY2LIPR3qF5d5FJi86wALhA6rMACIjq0UOqLl33iaFYtMHbHPTYWNc2iOBKnSa4etv/y2vXa7hpJW7pUbLjNRKzRnyvSxnSf2oNMkRJo+AWD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1GS90hc",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
  "id": -576460752303422580,
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
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
  "id": -576460752303422580,
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "state": "tx_+QENCwH4hLhAD8ctbt0SS63Slb7Ar0AXGW69LdQNfZOtfvPhUG1C/vsXEGyTlgUZQ6uF340A0BFO7RY2LIPR3qF5d5FJi86wALhA6rMACIjq0UOqLl33iaFYtMHbHPTYWNc2iOBKnSa4etv/y2vXa7hpJW7pUbLjNRKzRnyvSxnSf2oNMkRJo+AWD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1GS90hc"
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "state": "tx_+QENCwH4hLhAD8ctbt0SS63Slb7Ar0AXGW69LdQNfZOtfvPhUG1C/vsXEGyTlgUZQ6uF340A0BFO7RY2LIPR3qF5d5FJi86wALhA6rMACIjq0UOqLl33iaFYtMHbHPTYWNc2iOBKnSa4etv/y2vXa7hpJW7pUbLjNRKzRnyvSxnSf2oNMkRJo+AWD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1GS90hc"
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBmJQDTSt8vpE3zui3FjsKM4TlPHP5qqKQandrse+qD9AoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/Aobiv0KAJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQJS3CawJA==",
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
  "id": -576460752303422579,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAPDwt1LhxFHxNcGiQsYxPJUt7PFb5dQLV3HIS0MS6dWu7Ae+efudJ159xv0BcaxxEEgdBhocoGxQSYM8X/6NsLuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9CgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCUmWgmBw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
  "id": -576460752303422579,
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAPDwt1LhxFHxNcGiQsYxPJUt7PFb5dQLV3HIS0MS6dWu7Ae+efudJ159xv0BcaxxEEgdBhocoGxQSYM8X/6NsLuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9CgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCUmWgmBw=",
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
  "id": -576460752303422578,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAPDwt1LhxFHxNcGiQsYxPJUt7PFb5dQLV3HIS0MS6dWu7Ae+efudJ159xv0BcaxxEEgdBhocoGxQSYM8X/6NsLuEASCugaEQtkss5wE0i9DWuIY6tgMGPemZ2yw3IEATS291Gib8YIy/Nq7SlXi30mI1pg8l8Pscqd7jhA+bcI36cIuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9CgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCUtOGOTU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
  "id": -576460752303422578,
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEAPDwt1LhxFHxNcGiQsYxPJUt7PFb5dQLV3HIS0MS6dWu7Ae+efudJ159xv0BcaxxEEgdBhocoGxQSYM8X/6NsLuEASCugaEQtkss5wE0i9DWuIY6tgMGPemZ2yw3IEATS291Gib8YIy/Nq7SlXi30mI1pg8l8Pscqd7jhA+bcI36cIuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9CgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCUtOGOTU=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEAPDwt1LhxFHxNcGiQsYxPJUt7PFb5dQLV3HIS0MS6dWu7Ae+efudJ159xv0BcaxxEEgdBhocoGxQSYM8X/6NsLuEASCugaEQtkss5wE0i9DWuIY6tgMGPemZ2yw3IEATS291Gib8YIy/Nq7SlXi30mI1pg8l8Pscqd7jhA+bcI36cIuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9CgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCUtOGOTU=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAPDwt1LhxFHxNcGiQsYxPJUt7PFb5dQLV3HIS0MS6dWu7Ae+efudJ159xv0BcaxxEEgdBhocoGxQSYM8X/6NsLuEASCugaEQtkss5wE0i9DWuIY6tgMGPemZ2yw3IEATS291Gib8YIy/Nq7SlXi30mI1pg8l8Pscqd7jhA+bcI36cIuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9CgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCUtOGOTU=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAPDwt1LhxFHxNcGiQsYxPJUt7PFb5dQLV3HIS0MS6dWu7Ae+efudJ159xv0BcaxxEEgdBhocoGxQSYM8X/6NsLuEASCugaEQtkss5wE0i9DWuIY6tgMGPemZ2yw3IEATS291Gib8YIy/Nq7SlXi30mI1pg8l8Pscqd7jhA+bcI36cIuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9CgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCUtOGOTU=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "state": "tx_+P4LAfiEuEAPDwt1LhxFHxNcGiQsYxPJUt7PFb5dQLV3HIS0MS6dWu7Ae+efudJ159xv0BcaxxEEgdBhocoGxQSYM8X/6NsLuEASCugaEQtkss5wE0i9DWuIY6tgMGPemZ2yw3IEATS291Gib8YIy/Nq7SlXi30mI1pg8l8Pscqd7jhA+bcI36cIuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9CgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCUtOGOTU="
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "state": "tx_+P4LAfiEuEAPDwt1LhxFHxNcGiQsYxPJUt7PFb5dQLV3HIS0MS6dWu7Ae+efudJ159xv0BcaxxEEgdBhocoGxQSYM8X/6NsLuEASCugaEQtkss5wE0i9DWuIY6tgMGPemZ2yw3IEATS291Gib8YIy/Nq7SlXi30mI1pg8l8Pscqd7jhA+bcI36cIuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKG4r9CgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCUtOGOTU="
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBmJQDTSt8vpE3zui3FjsKM4TlPHP5qqKQandrse+qD9AoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/Aobiv0KBdYyosJiEVkIv3UfhREtMPbLmXGvLesTSuRCc8B8rvQgMhIpTq2g==",
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
  "id": -576460752303422577,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECiQQ5IglC/Xjuxo4NRTT93ADAJ2kVvPpXix4QkI9/E67Kr9A8JS5cGDuQqVimaIVUA44EbaTLjuDtq3oTt9PIPuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDIZ8oNtM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
  "id": -576460752303422577,
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECiQQ5IglC/Xjuxo4NRTT93ADAJ2kVvPpXix4QkI9/E67Kr9A8JS5cGDuQqVimaIVUA44EbaTLjuDtq3oTt9PIPuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDIZ8oNtM=",
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
  "id": -576460752303422576,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBN4kFqd5MQ12Shcuod01xGTDoGl2CPj5HnDMcncfzoJf1cTiheKhhDOIPzuK7w9pgp0xpCTWM3B6ImNMXHODYNuECiQQ5IglC/Xjuxo4NRTT93ADAJ2kVvPpXix4QkI9/E67Kr9A8JS5cGDuQqVimaIVUA44EbaTLjuDtq3oTt9PIPuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDITTPfe8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
  "id": -576460752303422576,
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBN4kFqd5MQ12Shcuod01xGTDoGl2CPj5HnDMcncfzoJf1cTiheKhhDOIPzuK7w9pgp0xpCTWM3B6ImNMXHODYNuECiQQ5IglC/Xjuxo4NRTT93ADAJ2kVvPpXix4QkI9/E67Kr9A8JS5cGDuQqVimaIVUA44EbaTLjuDtq3oTt9PIPuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDITTPfe8=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBN4kFqd5MQ12Shcuod01xGTDoGl2CPj5HnDMcncfzoJf1cTiheKhhDOIPzuK7w9pgp0xpCTWM3B6ImNMXHODYNuECiQQ5IglC/Xjuxo4NRTT93ADAJ2kVvPpXix4QkI9/E67Kr9A8JS5cGDuQqVimaIVUA44EbaTLjuDtq3oTt9PIPuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDITTPfe8=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "message": {
        "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBN4kFqd5MQ12Shcuod01xGTDoGl2CPj5HnDMcncfzoJf1cTiheKhhDOIPzuK7w9pgp0xpCTWM3B6ImNMXHODYNuECiQQ5IglC/Xjuxo4NRTT93ADAJ2kVvPpXix4QkI9/E67Kr9A8JS5cGDuQqVimaIVUA44EbaTLjuDtq3oTt9PIPuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDITTPfe8=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBN4kFqd5MQ12Shcuod01xGTDoGl2CPj5HnDMcncfzoJf1cTiheKhhDOIPzuK7w9pgp0xpCTWM3B6ImNMXHODYNuECiQQ5IglC/Xjuxo4NRTT93ADAJ2kVvPpXix4QkI9/E67Kr9A8JS5cGDuQqVimaIVUA44EbaTLjuDtq3oTt9PIPuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDITTPfe8=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "state": "tx_+P4LAfiEuEBN4kFqd5MQ12Shcuod01xGTDoGl2CPj5HnDMcncfzoJf1cTiheKhhDOIPzuK7w9pgp0xpCTWM3B6ImNMXHODYNuECiQQ5IglC/Xjuxo4NRTT93ADAJ2kVvPpXix4QkI9/E67Kr9A8JS5cGDuQqVimaIVUA44EbaTLjuDtq3oTt9PIPuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDITTPfe8="
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "state": "tx_+P4LAfiEuEBN4kFqd5MQ12Shcuod01xGTDoGl2CPj5HnDMcncfzoJf1cTiheKhhDOIPzuK7w9pgp0xpCTWM3B6ImNMXHODYNuECiQQ5IglC/Xjuxo4NRTT93ADAJ2kVvPpXix4QkI9/E67Kr9A8JS5cGDuQqVimaIVUA44EbaTLjuDtq3oTt9PIPuHT4cjMBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDITTPfe8="
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBmJQDTSt8vpE3zui3FjsKM4TlPHP5qqKQandrse+qD9AoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rnizAGGHLHOiuwDAIYPXtZ/KABTNLRjEg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422575,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDDfV/SZeLJ1IahYhTRTAhIi99UF28vaahYydodZ5chO1iJsfKfnJ3IGEDew8jVXLw7ICzAshn34YX0kFzUSVwIuF/4XTUBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAU+vrMWw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
  "id": -576460752303422575,
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDDfV/SZeLJ1IahYhTRTAhIi99UF28vaahYydodZ5chO1iJsfKfnJ3IGEDew8jVXLw7ICzAshn34YX0kFzUSVwIuF/4XTUBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAU+vrMWw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422574,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEDDfV/SZeLJ1IahYhTRTAhIi99UF28vaahYydodZ5chO1iJsfKfnJ3IGEDew8jVXLw7ICzAshn34YX0kFzUSVwIuEDuA8apWY0Sy6HRPkesw+LjBMtrfWyblnXQ3rlizRCXZBFwZ7cPXBwU0LlJmLx6XxKUgyYUyX4UaahIC6EcwzcFuF/4XTUBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAU9O0fEA="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
  "id": -576460752303422574,
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEDDfV/SZeLJ1IahYhTRTAhIi99UF28vaahYydodZ5chO1iJsfKfnJ3IGEDew8jVXLw7ICzAshn34YX0kFzUSVwIuEDuA8apWY0Sy6HRPkesw+LjBMtrfWyblnXQ3rlizRCXZBFwZ7cPXBwU0LlJmLx6XxKUgyYUyX4UaahIC6EcwzcFuF/4XTUBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAU9O0fEA=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEDDfV/SZeLJ1IahYhTRTAhIi99UF28vaahYydodZ5chO1iJsfKfnJ3IGEDew8jVXLw7ICzAshn34YX0kFzUSVwIuEDuA8apWY0Sy6HRPkesw+LjBMtrfWyblnXQ3rlizRCXZBFwZ7cPXBwU0LlJmLx6XxKUgyYUyX4UaahIC6EcwzcFuF/4XTUBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAU9O0fEA=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEDDfV/SZeLJ1IahYhTRTAhIi99UF28vaahYydodZ5chO1iJsfKfnJ3IGEDew8jVXLw7ICzAshn34YX0kFzUSVwIuEDuA8apWY0Sy6HRPkesw+LjBMtrfWyblnXQ3rlizRCXZBFwZ7cPXBwU0LlJmLx6XxKUgyYUyX4UaahIC6EcwzcFuF/4XTUBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAU9O0fEA=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEDDfV/SZeLJ1IahYhTRTAhIi99UF28vaahYydodZ5chO1iJsfKfnJ3IGEDew8jVXLw7ICzAshn34YX0kFzUSVwIuEDuA8apWY0Sy6HRPkesw+LjBMtrfWyblnXQ3rlizRCXZBFwZ7cPXBwU0LlJmLx6XxKUgyYUyX4UaahIC6EcwzcFuF/4XTUBoQZiUA00rfL6RN87otxY7CjOE5Txz+aqikGp3a7Hvqg/QKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54swBhhyxzorsAwCGD17WfygAU9O0fEA=",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
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
    "channel_id": "ch_kJGRromQKvQVMN4b13wKph7gSMyUXjuWG4pUMeWMCYF7D6Hcq",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
