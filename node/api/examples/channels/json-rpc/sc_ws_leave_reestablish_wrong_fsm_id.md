
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_wrong_fsm_id%2F3741
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
      "fsm_id": "ba_aLS03axF7nvewicyJvAJ5dPH/1pZq4y/b4+mUtfzQ9XHq7tH"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_wrong_fsm_id%2F3741
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
      "fsm_id": "ba_IwVn5JTrOQ/AU9LyCcdihDtKmxKObUiIaDSYmUum9LL1rfXd"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsWbDPHIw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423247,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBqiL33HHOMMJaKt9Y5mEGzrgeyH3yi+FZEBKOOi5Tsb4szP1GWd9WBVQEaUiVLoTvLfNdmsGQeJr0ftkk5p8sDuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LFkSNpHM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423247,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "fsm_id": "ba_IwVn5JTrOQ/AU9LyCcdihDtKmxKObUiIaDSYmUum9LL1rfXd",
      "signed_tx": "tx_+MsLAfhCuEBqiL33HHOMMJaKt9Y5mEGzrgeyH3yi+FZEBKOOi5Tsb4szP1GWd9WBVQEaUiVLoTvLfNdmsGQeJr0ftkk5p8sDuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LFkSNpHM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423246,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423246,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_aLS03axF7nvewicyJvAJ5dPH/1pZq4y/b4+mUtfzQ9XHq7tH"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "message": {
        "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "message": {
        "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "id": -576460752303423245,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423245,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&existing_fsm_id=ba_xX5EcZsIYrpbY9KN&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&existing_fsm_id=ba_xX5EcZsIYrpbY9KN&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&existing_fsm_id=ba_bwnDW8ktO71IgfMEbsYau8ELhuqNWPOEHUdjkkg%2BTaglIzkF&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&existing_fsm_id=ba_bwnDW8ktO71IgfMEbsYau8ELhuqNWPOEHUdjkkg%2BTaglIzkF&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&existing_fsm_id=ba_IwVn5JTrOQ%2FAU9LyCcdihDtKmxKObUiIaDSYmUum9LL1rfXd&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=responder
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
      "fsm_id": "ba_0xH3ariagN7WcZwzovtEeCIhaViKcrKo1fYTNMl+zr7oertL"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq&existing_fsm_id=ba_aLS03axF7nvewicyJvAJ5dPH%2F1pZq4y%2Fb4%2BmUtfzQ9XHq7tH&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G%2BLMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy&port=13180&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_e4ib2JIZC2WIKkKGJXzdBEu1GyXxBGRohyFWlJc4qWqwHjP2"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+QENCwH4hLhAaoi99xxzjDCWirfWOZhBs64Hsh98ovhWRASjjouU7G+LMz9RlnfVgVUBGlIlS6E7y3zXZrBkHia9H7ZJOafLA7hA1Zn8j2FgoIGIy4KNJwZZJUx8yoLpd9s2GmnQeoEzN5GHr3VKi5iBARWtkKCEao0JrGaFHjh9zuNLCIhjVIdAAriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxbsLECy"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423244,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423244,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBilLsKuhMnuZ9JjeO8lwj9ffQeIyA1Fa2Y+1CDmIO6sJAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAnTZ6sc=",
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
  "id": -576460752303423243,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECjmL6tjV8lTxLan4yXP0X+Lj+1thaBmgJjByIo0yxaTBOHeBUzJsUP78TyDWysKC9Bgl2GS7gWi092a+W8mPoDuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJCLcdA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423243,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+JALAfhCuECjmL6tjV8lTxLan4yXP0X+Lj+1thaBmgJjByIo0yxaTBOHeBUzJsUP78TyDWysKC9Bgl2GS7gWi092a+W8mPoDuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJCLcdA",
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
  "id": -576460752303423242,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECjmL6tjV8lTxLan4yXP0X+Lj+1thaBmgJjByIo0yxaTBOHeBUzJsUP78TyDWysKC9Bgl2GS7gWi092a+W8mPoDuED+Zhel2a1CxADgajfhK7CqxfmLC7b0UkNwku8tZWKv1pwPhGxt3fJqmExe6DQItyi0ehT+H+LHl74q3kmFNWsEuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIo0jeO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423242,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuECjmL6tjV8lTxLan4yXP0X+Lj+1thaBmgJjByIo0yxaTBOHeBUzJsUP78TyDWysKC9Bgl2GS7gWi092a+W8mPoDuED+Zhel2a1CxADgajfhK7CqxfmLC7b0UkNwku8tZWKv1pwPhGxt3fJqmExe6DQItyi0ehT+H+LHl74q3kmFNWsEuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIo0jeO"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuECjmL6tjV8lTxLan4yXP0X+Lj+1thaBmgJjByIo0yxaTBOHeBUzJsUP78TyDWysKC9Bgl2GS7gWi092a+W8mPoDuED+Zhel2a1CxADgajfhK7CqxfmLC7b0UkNwku8tZWKv1pwPhGxt3fJqmExe6DQItyi0ehT+H+LHl74q3kmFNWsEuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIo0jeO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423241,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423241,
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
  "id": -576460752303423240,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423240,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECjmL6tjV8lTxLan4yXP0X+Lj+1thaBmgJjByIo0yxaTBOHeBUzJsUP78TyDWysKC9Bgl2GS7gWi092a+W8mPoDuED+Zhel2a1CxADgajfhK7CqxfmLC7b0UkNwku8tZWKv1pwPhGxt3fJqmExe6DQItyi0ehT+H+LHl74q3kmFNWsEuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIo0jeO",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423239,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423239,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBilLsKuhMnuZ9JjeO8lwj9ffQeIyA1Fa2Y+1CDmIO6sJA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCyJtfq4=",
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
  "id": -576460752303423238,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBwCWZ5lbY6msdaq0t0hJvA++7+4sCRl4qlEKVQZhsb70Z8rvzDWLHDMw+jbWS3SoycxOOyR2BTrCeWI2AfywoEuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv2+4pm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423238,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBwCWZ5lbY6msdaq0t0hJvA++7+4sCRl4qlEKVQZhsb70Z8rvzDWLHDMw+jbWS3SoycxOOyR2BTrCeWI2AfywoEuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv2+4pm",
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
  "id": -576460752303423237,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBwCWZ5lbY6msdaq0t0hJvA++7+4sCRl4qlEKVQZhsb70Z8rvzDWLHDMw+jbWS3SoycxOOyR2BTrCeWI2AfywoEuEDENKprSnUNj5kd5EAduqtfRiRQtcYI4YiMFo6izC2RwsHkW4jGx2xAmK5eZKabTQg2/2vbKhSjATwBpx3KppcAuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvYewLa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423237,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuEBwCWZ5lbY6msdaq0t0hJvA++7+4sCRl4qlEKVQZhsb70Z8rvzDWLHDMw+jbWS3SoycxOOyR2BTrCeWI2AfywoEuEDENKprSnUNj5kd5EAduqtfRiRQtcYI4YiMFo6izC2RwsHkW4jGx2xAmK5eZKabTQg2/2vbKhSjATwBpx3KppcAuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvYewLa"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuEBwCWZ5lbY6msdaq0t0hJvA++7+4sCRl4qlEKVQZhsb70Z8rvzDWLHDMw+jbWS3SoycxOOyR2BTrCeWI2AfywoEuEDENKprSnUNj5kd5EAduqtfRiRQtcYI4YiMFo6izC2RwsHkW4jGx2xAmK5eZKabTQg2/2vbKhSjATwBpx3KppcAuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvYewLa"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423236,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423236,
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
  "id": -576460752303423235,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423235,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBwCWZ5lbY6msdaq0t0hJvA++7+4sCRl4qlEKVQZhsb70Z8rvzDWLHDMw+jbWS3SoycxOOyR2BTrCeWI2AfywoEuEDENKprSnUNj5kd5EAduqtfRiRQtcYI4YiMFo6izC2RwsHkW4jGx2xAmK5eZKabTQg2/2vbKhSjATwBpx3KppcAuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvYewLa",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423234,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423234,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBilLsKuhMnuZ9JjeO8lwj9ffQeIyA1Fa2Y+1CDmIO6sJBKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMbOaFTI=",
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
  "id": -576460752303423233,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBkgdkh/xKoHyZFu61ewRpylCxJQVZ9kqv7ePQdh1x5b/pomIN0XVcIdVqWqesdeRYeUM3ctwyvQtm7fHTvBJEJuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFmGIRH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423233,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBkgdkh/xKoHyZFu61ewRpylCxJQVZ9kqv7ePQdh1x5b/pomIN0XVcIdVqWqesdeRYeUM3ctwyvQtm7fHTvBJEJuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFmGIRH",
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
  "id": -576460752303423232,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBkgdkh/xKoHyZFu61ewRpylCxJQVZ9kqv7ePQdh1x5b/pomIN0XVcIdVqWqesdeRYeUM3ctwyvQtm7fHTvBJEJuEDNNolLTQEXJHsibSAu+pyJlzgOFL+YCYRU+UvlYdjM3TxshFlQInQN0U0Kz07rh6zM369iWhRV71gzfVr9MqgLuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGt67ro"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423232,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuEBkgdkh/xKoHyZFu61ewRpylCxJQVZ9kqv7ePQdh1x5b/pomIN0XVcIdVqWqesdeRYeUM3ctwyvQtm7fHTvBJEJuEDNNolLTQEXJHsibSAu+pyJlzgOFL+YCYRU+UvlYdjM3TxshFlQInQN0U0Kz07rh6zM369iWhRV71gzfVr9MqgLuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGt67ro"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuEBkgdkh/xKoHyZFu61ewRpylCxJQVZ9kqv7ePQdh1x5b/pomIN0XVcIdVqWqesdeRYeUM3ctwyvQtm7fHTvBJEJuEDNNolLTQEXJHsibSAu+pyJlzgOFL+YCYRU+UvlYdjM3TxshFlQInQN0U0Kz07rh6zM369iWhRV71gzfVr9MqgLuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGt67ro"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423231,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423231,
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
  "id": -576460752303423230,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423230,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBkgdkh/xKoHyZFu61ewRpylCxJQVZ9kqv7ePQdh1x5b/pomIN0XVcIdVqWqesdeRYeUM3ctwyvQtm7fHTvBJEJuEDNNolLTQEXJHsibSAu+pyJlzgOFL+YCYRU+UvlYdjM3TxshFlQInQN0U0Kz07rh6zM369iWhRV71gzfVr9MqgLuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGt67ro",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423229,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423229,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBilLsKuhMnuZ9JjeO8lwj9ffQeIyA1Fa2Y+1CDmIO6sJBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzYy2Bw=",
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
  "id": -576460752303423228,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECx0EjqSGzowgug61qMza5GQhwaEQOJ1FRfwAVTY2198bvRZFCD8k6TE0Efam1oZvRMONEkY1Re8twznRmqDVkGuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtidfvr"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423228,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+JALAfhCuECx0EjqSGzowgug61qMza5GQhwaEQOJ1FRfwAVTY2198bvRZFCD8k6TE0Efam1oZvRMONEkY1Re8twznRmqDVkGuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtidfvr",
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
  "id": -576460752303423227,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBg4kq6juWreK4hFJC3YLGJowqQk+B7ly4Fg05kYLI/WqGys4RtDmDnbD4HGZqyh4vjvFsjGIJ68P4JjGCn9+ADuECx0EjqSGzowgug61qMza5GQhwaEQOJ1FRfwAVTY2198bvRZFCD8k6TE0Efam1oZvRMONEkY1Re8twznRmqDVkGuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsicS5d"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423227,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuEBg4kq6juWreK4hFJC3YLGJowqQk+B7ly4Fg05kYLI/WqGys4RtDmDnbD4HGZqyh4vjvFsjGIJ68P4JjGCn9+ADuECx0EjqSGzowgug61qMza5GQhwaEQOJ1FRfwAVTY2198bvRZFCD8k6TE0Efam1oZvRMONEkY1Re8twznRmqDVkGuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsicS5d"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuEBg4kq6juWreK4hFJC3YLGJowqQk+B7ly4Fg05kYLI/WqGys4RtDmDnbD4HGZqyh4vjvFsjGIJ68P4JjGCn9+ADuECx0EjqSGzowgug61qMza5GQhwaEQOJ1FRfwAVTY2198bvRZFCD8k6TE0Efam1oZvRMONEkY1Re8twznRmqDVkGuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsicS5d"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423226,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423226,
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
  "id": -576460752303423225,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423225,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBg4kq6juWreK4hFJC3YLGJowqQk+B7ly4Fg05kYLI/WqGys4RtDmDnbD4HGZqyh4vjvFsjGIJ68P4JjGCn9+ADuECx0EjqSGzowgug61qMza5GQhwaEQOJ1FRfwAVTY2198bvRZFCD8k6TE0Efam1oZvRMONEkY1Re8twznRmqDVkGuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsicS5d",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423224,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423224,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBilLsKuhMnuZ9JjeO8lwj9ffQeIyA1Fa2Y+1CDmIO6sJBqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMSDNn9g=",
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
  "id": -576460752303423223,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECV9HQaonl9wsuJgotupQxpEHJxJGfKk3AC5a1ofMqbuLPqToZd4VQfpIvB+s7q2CYk2HfSs1tpwHuCD3sYtMYHuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jF5CGTp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423223,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "signed_tx": "tx_+JALAfhCuECV9HQaonl9wsuJgotupQxpEHJxJGfKk3AC5a1ofMqbuLPqToZd4VQfpIvB+s7q2CYk2HfSs1tpwHuCD3sYtMYHuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jF5CGTp",
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
  "id": -576460752303423222,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECV9HQaonl9wsuJgotupQxpEHJxJGfKk3AC5a1ofMqbuLPqToZd4VQfpIvB+s7q2CYk2HfSs1tpwHuCD3sYtMYHuEDRIHvOQFxW/idIxtagn7vb9rxD4H1nq6TyuqkLWrZae7WZ1jnJJckruLRR6Q7S2pFq009FIeTRmV9n9MMA+y0AuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jG//zlp"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423222,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuECV9HQaonl9wsuJgotupQxpEHJxJGfKk3AC5a1ofMqbuLPqToZd4VQfpIvB+s7q2CYk2HfSs1tpwHuCD3sYtMYHuEDRIHvOQFxW/idIxtagn7vb9rxD4H1nq6TyuqkLWrZae7WZ1jnJJckruLRR6Q7S2pFq009FIeTRmV9n9MMA+y0AuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jG//zlp"
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "state": "tx_+NILAfiEuECV9HQaonl9wsuJgotupQxpEHJxJGfKk3AC5a1ofMqbuLPqToZd4VQfpIvB+s7q2CYk2HfSs1tpwHuCD3sYtMYHuEDRIHvOQFxW/idIxtagn7vb9rxD4H1nq6TyuqkLWrZae7WZ1jnJJckruLRR6Q7S2pFq009FIeTRmV9n9MMA+y0AuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jG//zlp"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423221,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423221,
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
  "id": -576460752303423220,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423220,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECV9HQaonl9wsuJgotupQxpEHJxJGfKk3AC5a1ofMqbuLPqToZd4VQfpIvB+s7q2CYk2HfSs1tpwHuCD3sYtMYHuEDRIHvOQFxW/idIxtagn7vb9rxD4H1nq6TyuqkLWrZae7WZ1jnJJckruLRR6Q7S2pFq009FIeTRmV9n9MMA+y0AuEj4RjkCoQYpS7CroTJ7mfSY3jvJcI/X30HiMgNRWtmPtQg5iDurCQagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jG//zlp",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423219,
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423219,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423218,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
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
  "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
  "id": -576460752303423218,
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
    "channel_id": "ch_KBqrarLidAkaa7MTpNYjyT56kSSjmXJfEaArWUSdJT3cfrJZq",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
