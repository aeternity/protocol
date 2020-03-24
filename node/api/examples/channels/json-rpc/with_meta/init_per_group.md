
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
      "fsm_id": "ba_oLCg/RSB2svUS5VrWCdB/tI9sjFYGUxS1gS7AWcbW9rY6f76"
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
      "fsm_id": "ba_B2GsnQoJOOEoJG5/W5kkss64SY83HR7mdQmDiLU3Qep1+z1q"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs0Ca3eIg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422828,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBsj7bekbtuTpUh0LZK/1lsWWvGWXgjzS81eOrIM1VkAzBSIQaB0SC1ae82dM/GnKw8u/vt5QIzbCsR8yCw/ncKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LNIAoTKg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422828,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "fsm_id": "ba_B2GsnQoJOOEoJG5/W5kkss64SY83HR7mdQmDiLU3Qep1+z1q",
      "signed_tx": "tx_+MsLAfhCuEBsj7bekbtuTpUh0LZK/1lsWWvGWXgjzS81eOrIM1VkAzBSIQaB0SC1ae82dM/GnKw8u/vt5QIzbCsR8yCw/ncKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LNIAoTKg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422827,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAbI+23pG7bk6VIdC2Sv9ZbFlrxll4I80vNXjqyDNVZAMwUiEGgdEgtWnvNnTPxpysPLv77eUCM2wrEfMgsP53CrhAzyZ1+I3kBREfowRgY3Lel4OHveP859wUVlqOfeaGQYkUojKQy0EfJ16N8Gj5GyWJi9CjgdLrUSrvr+BOxEPSB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzTYG7Ns"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422827,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAbI+23pG7bk6VIdC2Sv9ZbFlrxll4I80vNXjqyDNVZAMwUiEGgdEgtWnvNnTPxpysPLv77eUCM2wrEfMgsP53CrhAzyZ1+I3kBREfowRgY3Lel4OHveP859wUVlqOfeaGQYkUojKQy0EfJ16N8Gj5GyWJi9CjgdLrUSrvr+BOxEPSB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzTYG7Ns",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_oLCg/RSB2svUS5VrWCdB/tI9sjFYGUxS1gS7AWcbW9rY6f76"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAbI+23pG7bk6VIdC2Sv9ZbFlrxll4I80vNXjqyDNVZAMwUiEGgdEgtWnvNnTPxpysPLv77eUCM2wrEfMgsP53CrhAzyZ1+I3kBREfowRgY3Lel4OHveP859wUVlqOfeaGQYkUojKQy0EfJ16N8Gj5GyWJi9CjgdLrUSrvr+BOxEPSB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzTYG7Ns",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbI+23pG7bk6VIdC2Sv9ZbFlrxll4I80vNXjqyDNVZAMwUiEGgdEgtWnvNnTPxpysPLv77eUCM2wrEfMgsP53CrhAzyZ1+I3kBREfowRgY3Lel4OHveP859wUVlqOfeaGQYkUojKQy0EfJ16N8Gj5GyWJi9CjgdLrUSrvr+BOxEPSB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzTYG7Ns",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbI+23pG7bk6VIdC2Sv9ZbFlrxll4I80vNXjqyDNVZAMwUiEGgdEgtWnvNnTPxpysPLv77eUCM2wrEfMgsP53CrhAzyZ1+I3kBREfowRgY3Lel4OHveP859wUVlqOfeaGQYkUojKQy0EfJ16N8Gj5GyWJi9CjgdLrUSrvr+BOxEPSB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzTYG7Ns",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
  "id": -576460752303422826,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422826,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+QENCwH4hLhAbI+23pG7bk6VIdC2Sv9ZbFlrxll4I80vNXjqyDNVZAMwUiEGgdEgtWnvNnTPxpysPLv77eUCM2wrEfMgsP53CrhAzyZ1+I3kBREfowRgY3Lel4OHveP859wUVlqOfeaGQYkUojKQy0EfJ16N8Gj5GyWJi9CjgdLrUSrvr+BOxEPSB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzTYG7Ns"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+QENCwH4hLhAbI+23pG7bk6VIdC2Sv9ZbFlrxll4I80vNXjqyDNVZAMwUiEGgdEgtWnvNnTPxpysPLv77eUCM2wrEfMgsP53CrhAzyZ1+I3kBREfowRgY3Lel4OHveP859wUVlqOfeaGQYkUojKQy0EfJ16N8Gj5GyWJi9CjgdLrUSrvr+BOxEPSB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzTYG7Ns"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422825,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422825,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsbBWu/xVpTJkxB+RilACEVlef3ALvNKFwUfDi3K/R8eAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAshbzPc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422824,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECBoACMHFc/lINcJMVDdnHbeB8LkDPN36DLGE3v6yGR/+xBLR/cgJfrqUOMCWdH9AfNEokGCvDC8t0SJoI8beYHuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLpbOIu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422824,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+JALAfhCuECBoACMHFc/lINcJMVDdnHbeB8LkDPN36DLGE3v6yGR/+xBLR/cgJfrqUOMCWdH9AfNEokGCvDC8t0SJoI8beYHuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLpbOIu",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422823,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA/aQhHTajNA4tac/g7ZQ54a9+4CVa7GGPf9wKRDeNCsVOc0VMYMc+076+Tkj7mCzk4LKyh5dMHA5umZv51qKwHuECBoACMHFc/lINcJMVDdnHbeB8LkDPN36DLGE3v6yGR/+xBLR/cgJfrqUOMCWdH9AfNEokGCvDC8t0SJoI8beYHuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJf92Hj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422823,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuEA/aQhHTajNA4tac/g7ZQ54a9+4CVa7GGPf9wKRDeNCsVOc0VMYMc+076+Tkj7mCzk4LKyh5dMHA5umZv51qKwHuECBoACMHFc/lINcJMVDdnHbeB8LkDPN36DLGE3v6yGR/+xBLR/cgJfrqUOMCWdH9AfNEokGCvDC8t0SJoI8beYHuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJf92Hj"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuEA/aQhHTajNA4tac/g7ZQ54a9+4CVa7GGPf9wKRDeNCsVOc0VMYMc+076+Tkj7mCzk4LKyh5dMHA5umZv51qKwHuECBoACMHFc/lINcJMVDdnHbeB8LkDPN36DLGE3v6yGR/+xBLR/cgJfrqUOMCWdH9AfNEokGCvDC8t0SJoI8beYHuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJf92Hj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422822,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422822,
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
  "id": -576460752303422821,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422821,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA/aQhHTajNA4tac/g7ZQ54a9+4CVa7GGPf9wKRDeNCsVOc0VMYMc+076+Tkj7mCzk4LKyh5dMHA5umZv51qKwHuECBoACMHFc/lINcJMVDdnHbeB8LkDPN36DLGE3v6yGR/+xBLR/cgJfrqUOMCWdH9AfNEokGCvDC8t0SJoI8beYHuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJf92Hj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422820,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422820,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsbBWu/xVpTJkxB+RilACEVlef3ALvNKFwUfDi3K/R8eA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC9Xr6Ik=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422819,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA+dHN8biejsn7jBavzGBBaZv8ZNBqM1C+pl1DZOS75WrJsqG1kd93WeCUVYjWmnL3LpnMTYUqJ+44L8eemTeINuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsMN+9j"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422819,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA+dHN8biejsn7jBavzGBBaZv8ZNBqM1C+pl1DZOS75WrJsqG1kd93WeCUVYjWmnL3LpnMTYUqJ+44L8eemTeINuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsMN+9j",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422818,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA+dHN8biejsn7jBavzGBBaZv8ZNBqM1C+pl1DZOS75WrJsqG1kd93WeCUVYjWmnL3LpnMTYUqJ+44L8eemTeINuEDYKUzJFohl78bWnIlFxCVrz3dVGU4MFfYvW2O6MuKSkI8hXxh0lg0USXXByUGX5Y/UefB8CiBCDcPvQgRCfcsDuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt1rKWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422818,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuEA+dHN8biejsn7jBavzGBBaZv8ZNBqM1C+pl1DZOS75WrJsqG1kd93WeCUVYjWmnL3LpnMTYUqJ+44L8eemTeINuEDYKUzJFohl78bWnIlFxCVrz3dVGU4MFfYvW2O6MuKSkI8hXxh0lg0USXXByUGX5Y/UefB8CiBCDcPvQgRCfcsDuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt1rKWA"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuEA+dHN8biejsn7jBavzGBBaZv8ZNBqM1C+pl1DZOS75WrJsqG1kd93WeCUVYjWmnL3LpnMTYUqJ+44L8eemTeINuEDYKUzJFohl78bWnIlFxCVrz3dVGU4MFfYvW2O6MuKSkI8hXxh0lg0USXXByUGX5Y/UefB8CiBCDcPvQgRCfcsDuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt1rKWA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422817,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422817,
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
  "id": -576460752303422816,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422816,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA+dHN8biejsn7jBavzGBBaZv8ZNBqM1C+pl1DZOS75WrJsqG1kd93WeCUVYjWmnL3LpnMTYUqJ+44L8eemTeINuEDYKUzJFohl78bWnIlFxCVrz3dVGU4MFfYvW2O6MuKSkI8hXxh0lg0USXXByUGX5Y/UefB8CiBCDcPvQgRCfcsDuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt1rKWA",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422815,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422815,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsbBWu/xVpTJkxB+RilACEVlef3ALvNKFwUfDi3K/R8eBKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMUa3F8o=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422814,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED34dNbzBj1/Csu9/o3KOJrbH82ss8CrkEmUuykFzuh1hLIhcp6w2O3fnsXuwV5/XBbKne5xlJbdu12jK75L7QFuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHlkRuq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422814,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+JALAfhCuED34dNbzBj1/Csu9/o3KOJrbH82ss8CrkEmUuykFzuh1hLIhcp6w2O3fnsXuwV5/XBbKne5xlJbdu12jK75L7QFuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHlkRuq",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422813,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAORXISEDGQ+QawynoqpGBnlIphqAH/DaRaInPrQv9c1QrwZ5WqbLCw6C+TabIuX+489BdgOQEZwE3DcmL5UZcNuED34dNbzBj1/Csu9/o3KOJrbH82ss8CrkEmUuykFzuh1hLIhcp6w2O3fnsXuwV5/XBbKne5xlJbdu12jK75L7QFuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE774NZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422813,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuEAORXISEDGQ+QawynoqpGBnlIphqAH/DaRaInPrQv9c1QrwZ5WqbLCw6C+TabIuX+489BdgOQEZwE3DcmL5UZcNuED34dNbzBj1/Csu9/o3KOJrbH82ss8CrkEmUuykFzuh1hLIhcp6w2O3fnsXuwV5/XBbKne5xlJbdu12jK75L7QFuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE774NZ"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuEAORXISEDGQ+QawynoqpGBnlIphqAH/DaRaInPrQv9c1QrwZ5WqbLCw6C+TabIuX+489BdgOQEZwE3DcmL5UZcNuED34dNbzBj1/Csu9/o3KOJrbH82ss8CrkEmUuykFzuh1hLIhcp6w2O3fnsXuwV5/XBbKne5xlJbdu12jK75L7QFuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE774NZ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422812,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422812,
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
  "id": -576460752303422811,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422811,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAORXISEDGQ+QawynoqpGBnlIphqAH/DaRaInPrQv9c1QrwZ5WqbLCw6C+TabIuX+489BdgOQEZwE3DcmL5UZcNuED34dNbzBj1/Csu9/o3KOJrbH82ss8CrkEmUuykFzuh1hLIhcp6w2O3fnsXuwV5/XBbKne5xlJbdu12jK75L7QFuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE774NZ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422810,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422810,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsbBWu/xVpTJkxB+RilACEVlef3ALvNKFwUfDi3K/R8eBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC6oxl5E=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422809,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDjFZafVZmWdofVDTYe0yMgvDMl/VrZ3S4sj1fqFeB8oHaW2vlU+UH5e4TbzjLMZD0PjagoDLOgX5IDqy6dxP0AuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguW2sZe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422809,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDjFZafVZmWdofVDTYe0yMgvDMl/VrZ3S4sj1fqFeB8oHaW2vlU+UH5e4TbzjLMZD0PjagoDLOgX5IDqy6dxP0AuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguW2sZe",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422808,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECFuTeaCPNSIJuVhDJybG/HAYcElbhl/Tf2UXfxqapqxuqo3N47iqYMV+ks2Xp6mD8G7kMI3S9X9jGpOeT9XNUNuEDjFZafVZmWdofVDTYe0yMgvDMl/VrZ3S4sj1fqFeB8oHaW2vlU+UH5e4TbzjLMZD0PjagoDLOgX5IDqy6dxP0AuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgueF3Is"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422808,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuECFuTeaCPNSIJuVhDJybG/HAYcElbhl/Tf2UXfxqapqxuqo3N47iqYMV+ks2Xp6mD8G7kMI3S9X9jGpOeT9XNUNuEDjFZafVZmWdofVDTYe0yMgvDMl/VrZ3S4sj1fqFeB8oHaW2vlU+UH5e4TbzjLMZD0PjagoDLOgX5IDqy6dxP0AuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgueF3Is"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuECFuTeaCPNSIJuVhDJybG/HAYcElbhl/Tf2UXfxqapqxuqo3N47iqYMV+ks2Xp6mD8G7kMI3S9X9jGpOeT9XNUNuEDjFZafVZmWdofVDTYe0yMgvDMl/VrZ3S4sj1fqFeB8oHaW2vlU+UH5e4TbzjLMZD0PjagoDLOgX5IDqy6dxP0AuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgueF3Is"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422807,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422807,
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
  "id": -576460752303422806,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422806,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECFuTeaCPNSIJuVhDJybG/HAYcElbhl/Tf2UXfxqapqxuqo3N47iqYMV+ks2Xp6mD8G7kMI3S9X9jGpOeT9XNUNuEDjFZafVZmWdofVDTYe0yMgvDMl/VrZ3S4sj1fqFeB8oHaW2vlU+UH5e4TbzjLMZD0PjagoDLOgX5IDqy6dxP0AuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgueF3Is",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422805,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422805,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsbBWu/xVpTJkxB+RilACEVlef3ALvNKFwUfDi3K/R8eBqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMcA4Hig=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422804,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA7DO1HvijrDFEo/PLhhzDCYST7FKWTlCpHZOq0+mRofi+4xaSuEwh9nYurXAKH8iujXZoI3t6pD7/V8tr0yz8OuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGim9Rs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422804,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA7DO1HvijrDFEo/PLhhzDCYST7FKWTlCpHZOq0+mRofi+4xaSuEwh9nYurXAKH8iujXZoI3t6pD7/V8tr0yz8OuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGim9Rs",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303422803,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAlzUdNpqPObm7+1rsy8jogFCSLt2pJTkuMpWdjcETN56bBM5CbpBWVu7kCnv+GAYrqr0qURjDbkOoMAREzMlsNuEA7DO1HvijrDFEo/PLhhzDCYST7FKWTlCpHZOq0+mRofi+4xaSuEwh9nYurXAKH8iujXZoI3t6pD7/V8tr0yz8OuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jF9Qchz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422803,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuEAlzUdNpqPObm7+1rsy8jogFCSLt2pJTkuMpWdjcETN56bBM5CbpBWVu7kCnv+GAYrqr0qURjDbkOoMAREzMlsNuEA7DO1HvijrDFEo/PLhhzDCYST7FKWTlCpHZOq0+mRofi+4xaSuEwh9nYurXAKH8iujXZoI3t6pD7/V8tr0yz8OuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jF9Qchz"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+NILAfiEuEAlzUdNpqPObm7+1rsy8jogFCSLt2pJTkuMpWdjcETN56bBM5CbpBWVu7kCnv+GAYrqr0qURjDbkOoMAREzMlsNuEA7DO1HvijrDFEo/PLhhzDCYST7FKWTlCpHZOq0+mRofi+4xaSuEwh9nYurXAKH8iujXZoI3t6pD7/V8tr0yz8OuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jF9Qchz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422802,
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422802,
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
  "id": -576460752303422801,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422801,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAlzUdNpqPObm7+1rsy8jogFCSLt2pJTkuMpWdjcETN56bBM5CbpBWVu7kCnv+GAYrqr0qURjDbkOoMAREzMlsNuEA7DO1HvijrDFEo/PLhhzDCYST7FKWTlCpHZOq0+mRofi+4xaSuEwh9nYurXAKH8iujXZoI3t6pD7/V8tr0yz8OuEj4RjkCoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHgagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jF9Qchz",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```
