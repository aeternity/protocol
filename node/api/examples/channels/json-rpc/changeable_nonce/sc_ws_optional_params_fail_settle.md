
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
      "fsm_id": "ba_ac8bLlH3ezZ0xWNJ9GNLbuWIoF7vFtZF6/F7J2S/YE8zQnRo"
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
      "fsm_id": "ba_acMDGAJhF/Dot1LdBzFWeD/wA2ataszJYW+NV6zh528ME3Q2"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBs9MLeu8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422145,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEC3K1uSMGAHDGJouVB0OY4WmSUlZn7w+HQ0j60R5OIH70cmd4NCJJ/RU3qBLSn29EQgQXHhpp/1yRCnNcYuwaIAuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbOQ+Wds"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422145,
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "fsm_id": "ba_acMDGAJhF/Dot1LdBzFWeD/wA2ataszJYW+NV6zh528ME3Q2",
      "signed_tx": "tx_+MwLAfhCuEC3K1uSMGAHDGJouVB0OY4WmSUlZn7w+HQ0j60R5OIH70cmd4NCJJ/RU3qBLSn29EQgQXHhpp/1yRCnNcYuwaIAuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbOQ+Wds",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422144,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAQ5kZjy/XfJHSU+GMwXpgIilD4tSJTYXMLfiNaK0lynLYlCSgc8hivO7NTvV/rT8LXxZnD+qUsX9W0Ya59eXkBbhAtytbkjBgBwxiaLlQdDmOFpklJWZ+8Ph0NI+tEeTiB+9HJneDQiSf0VN6gS0p9vREIEFx4aaf9ckQpzXGLsGiALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gz+9Dazg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422144,
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAQ5kZjy/XfJHSU+GMwXpgIilD4tSJTYXMLfiNaK0lynLYlCSgc8hivO7NTvV/rT8LXxZnD+qUsX9W0Ya59eXkBbhAtytbkjBgBwxiaLlQdDmOFpklJWZ+8Ph0NI+tEeTiB+9HJneDQiSf0VN6gS0p9vREIEFx4aaf9ckQpzXGLsGiALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gz+9Dazg==",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_ac8bLlH3ezZ0xWNJ9GNLbuWIoF7vFtZF6/F7J2S/YE8zQnRo"
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAQ5kZjy/XfJHSU+GMwXpgIilD4tSJTYXMLfiNaK0lynLYlCSgc8hivO7NTvV/rT8LXxZnD+qUsX9W0Ya59eXkBbhAtytbkjBgBwxiaLlQdDmOFpklJWZ+8Ph0NI+tEeTiB+9HJneDQiSf0VN6gS0p9vREIEFx4aaf9ckQpzXGLsGiALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gz+9Dazg==",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAQ5kZjy/XfJHSU+GMwXpgIilD4tSJTYXMLfiNaK0lynLYlCSgc8hivO7NTvV/rT8LXxZnD+qUsX9W0Ya59eXkBbhAtytbkjBgBwxiaLlQdDmOFpklJWZ+8Ph0NI+tEeTiB+9HJneDQiSf0VN6gS0p9vREIEFx4aaf9ckQpzXGLsGiALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gz+9Dazg==",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAQ5kZjy/XfJHSU+GMwXpgIilD4tSJTYXMLfiNaK0lynLYlCSgc8hivO7NTvV/rT8LXxZnD+qUsX9W0Ya59eXkBbhAtytbkjBgBwxiaLlQdDmOFpklJWZ+8Ph0NI+tEeTiB+9HJneDQiSf0VN6gS0p9vREIEFx4aaf9ckQpzXGLsGiALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gz+9Dazg==",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "message": {
        "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "message": {
        "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
  "id": -576460752303422143,
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
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422143,
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "state": "tx_+QEOCwH4hLhAQ5kZjy/XfJHSU+GMwXpgIilD4tSJTYXMLfiNaK0lynLYlCSgc8hivO7NTvV/rT8LXxZnD+qUsX9W0Ya59eXkBbhAtytbkjBgBwxiaLlQdDmOFpklJWZ+8Ph0NI+tEeTiB+9HJneDQiSf0VN6gS0p9vREIEFx4aaf9ckQpzXGLsGiALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gz+9Dazg=="
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "state": "tx_+QEOCwH4hLhAQ5kZjy/XfJHSU+GMwXpgIilD4tSJTYXMLfiNaK0lynLYlCSgc8hivO7NTvV/rT8LXxZnD+qUsX9W0Ya59eXkBbhAtytbkjBgBwxiaLlQdDmOFpklJWZ+8Ph0NI+tEeTiB+9HJneDQiSf0VN6gS0p9vREIEFx4aaf9ckQpzXGLsGiALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4Gz+9Dazg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422142,
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
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422142,
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpJaVXZVF+l7BJWQsvpCcyZqvZXMYskfVK12ZjR0x/VpAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAjJK4lA=",
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
  "id": -576460752303422141,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECb6EADHdXWwjhDbjR/ys3Nh4LSLADsuwRHUTspo/YcbO6XCHiPVV//xGC/iJpswutI38IilxvcAeipPpZwGHIOuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKE3Y3N"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422141,
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "signed_tx": "tx_+JALAfhCuECb6EADHdXWwjhDbjR/ys3Nh4LSLADsuwRHUTspo/YcbO6XCHiPVV//xGC/iJpswutI38IilxvcAeipPpZwGHIOuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKE3Y3N",
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
  "id": -576460752303422140,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECb6EADHdXWwjhDbjR/ys3Nh4LSLADsuwRHUTspo/YcbO6XCHiPVV//xGC/iJpswutI38IilxvcAeipPpZwGHIOuEDpvGJ8ym3qFVoZwsYOM089IFrUy54th6fI5Tq822oEfeB2lXBN78QxLOFFL3QjZ98vnAkoan5fB4X0m7TyVa0PuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKFkBqU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422140,
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "state": "tx_+NILAfiEuECb6EADHdXWwjhDbjR/ys3Nh4LSLADsuwRHUTspo/YcbO6XCHiPVV//xGC/iJpswutI38IilxvcAeipPpZwGHIOuEDpvGJ8ym3qFVoZwsYOM089IFrUy54th6fI5Tq822oEfeB2lXBN78QxLOFFL3QjZ98vnAkoan5fB4X0m7TyVa0PuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKFkBqU"
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "state": "tx_+NILAfiEuECb6EADHdXWwjhDbjR/ys3Nh4LSLADsuwRHUTspo/YcbO6XCHiPVV//xGC/iJpswutI38IilxvcAeipPpZwGHIOuEDpvGJ8ym3qFVoZwsYOM089IFrUy54th6fI5Tq822oEfeB2lXBN78QxLOFFL3QjZ98vnAkoan5fB4X0m7TyVa0PuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKFkBqU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422139,
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
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422139,
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
  "id": -576460752303422138,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422138,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECb6EADHdXWwjhDbjR/ys3Nh4LSLADsuwRHUTspo/YcbO6XCHiPVV//xGC/iJpswutI38IilxvcAeipPpZwGHIOuEDpvGJ8ym3qFVoZwsYOM089IFrUy54th6fI5Tq822oEfeB2lXBN78QxLOFFL3QjZ98vnAkoan5fB4X0m7TyVa0PuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKFkBqU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422137,
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
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422137,
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpJaVXZVF+l7BJWQsvpCcyZqvZXMYskfVK12ZjR0x/VpA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC7GNKOg=",
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
  "id": -576460752303422136,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAd//17Ldyc7sGyWqdncTYBZ+sSmGGxkGuAzLlrWiB1VietGNEXi8XTkfnuMs0M6FwNElJG7SLJr7N/4x0fWl0KuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsr0+zH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422136,
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAd//17Ldyc7sGyWqdncTYBZ+sSmGGxkGuAzLlrWiB1VietGNEXi8XTkfnuMs0M6FwNElJG7SLJr7N/4x0fWl0KuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsr0+zH",
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
  "id": -576460752303422135,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAFKYes1mJvz3CFVRGY7d92tTbG83fl6R+EtPcamToYnMGOkPlg1J4EyezGjI2JM6Fp0CIc9aMJhNmN9AxigD8EuEAd//17Ldyc7sGyWqdncTYBZ+sSmGGxkGuAzLlrWiB1VietGNEXi8XTkfnuMs0M6FwNElJG7SLJr7N/4x0fWl0KuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv4Wubw"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422135,
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "state": "tx_+NILAfiEuEAFKYes1mJvz3CFVRGY7d92tTbG83fl6R+EtPcamToYnMGOkPlg1J4EyezGjI2JM6Fp0CIc9aMJhNmN9AxigD8EuEAd//17Ldyc7sGyWqdncTYBZ+sSmGGxkGuAzLlrWiB1VietGNEXi8XTkfnuMs0M6FwNElJG7SLJr7N/4x0fWl0KuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv4Wubw"
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "state": "tx_+NILAfiEuEAFKYes1mJvz3CFVRGY7d92tTbG83fl6R+EtPcamToYnMGOkPlg1J4EyezGjI2JM6Fp0CIc9aMJhNmN9AxigD8EuEAd//17Ldyc7sGyWqdncTYBZ+sSmGGxkGuAzLlrWiB1VietGNEXi8XTkfnuMs0M6FwNElJG7SLJr7N/4x0fWl0KuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv4Wubw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422134,
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
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422134,
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
  "id": -576460752303422133,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
  "id": -576460752303422133,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAFKYes1mJvz3CFVRGY7d92tTbG83fl6R+EtPcamToYnMGOkPlg1J4EyezGjI2JM6Fp0CIc9aMJhNmN9AxigD8EuEAd//17Ldyc7sGyWqdncTYBZ+sSmGGxkGuAzLlrWiB1VietGNEXi8XTkfnuMs0M6FwNElJG7SLJr7N/4x0fWl0KuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgv4Wubw",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NgGhBpJaVXZVF+l7BJWQsvpCcyZqvZXMYskfVK12ZjR0x/VpoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAFKYes1mJvz3CFVRGY7d92tTbG83fl6R+EtPcamToYnMGOkPlg1J4EyezGjI2JM6Fp0CIc9aMJhNmN9AxigD8EuEAd//17Ldyc7sGyWqdncTYBZ+sSmGGxkGuAzLlrWiB1VietGNEXi8XTkfnuMs0M6FwNElJG7SLJr7N/4x0fWl0KuEj4RjkCoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aQOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGSNwYbAAgbQDcJ3o",
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
    "signed_tx": "tx_+QLBCwH4QrhAkeHwC5YnYvJ0MIX4ufjZOxmLhfeFZ+Lu/AkFQDcXvT0HNanmIvj+Q7n0X1MmmVJtW08894gQeA69lsdgubeBArkCePkCdTYBoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhABSmHrNZib89whVURmO3fdrU2xvN35ekfhLT3Gpk6GJzBjpD5YNSeBMnsxoyNiTOhadAiHPWjCYTZjfQMYoA/BLhAHf/9ey3cnO7BslqnZ3E2AWfrEphhsZBrgMy5a1ogdVYnrRjRF4vF05H57jLNDOhcDRJSRu0iya+zf+MdH1pdCrhI+EY5AqEGklpVdlUX6XsElZCy+kJzJmq9lcxiyR9UrXZmNHTH9WkDoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIG05R0/+Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAkeHwC5YnYvJ0MIX4ufjZOxmLhfeFZ+Lu/AkFQDcXvT0HNanmIvj+Q7n0X1MmmVJtW08894gQeA69lsdgubeBArkCePkCdTYBoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhABSmHrNZib89whVURmO3fdrU2xvN35ekfhLT3Gpk6GJzBjpD5YNSeBMnsxoyNiTOhadAiHPWjCYTZjfQMYoA/BLhAHf/9ey3cnO7BslqnZ3E2AWfrEphhsZBrgMy5a1ogdVYnrRjRF4vF05H57jLNDOhcDRJSRu0iya+zf+MdH1pdCrhI+EY5AqEGklpVdlUX6XsElZCy+kJzJmq9lcxiyR9UrXZmNHTH9WkDoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIG05R0/+Q==",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAkeHwC5YnYvJ0MIX4ufjZOxmLhfeFZ+Lu/AkFQDcXvT0HNanmIvj+Q7n0X1MmmVJtW08894gQeA69lsdgubeBArkCePkCdTYBoQaSWlV2VRfpewSVkLL6QnMmar2VzGLJH1StdmY0dMf1aaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhABSmHrNZib89whVURmO3fdrU2xvN35ekfhLT3Gpk6GJzBjpD5YNSeBMnsxoyNiTOhadAiHPWjCYTZjfQMYoA/BLhAHf/9ey3cnO7BslqnZ3E2AWfrEphhsZBrgMy5a1ogdVYnrRjRF4vF05H57jLNDOhcDRJSRu0iya+zf+MdH1pdCrhI+EY5AqEGklpVdlUX6XsElZCy+kJzJmq9lcxiyR9UrXZmNHTH9WkDoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIG05R0/+Q==",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
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
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "signed_tx": "tx_+GcLAcC4YvhgOAGhBpJaVXZVF+l7BJWQsvpCcyZqvZXMYskfVK12ZjR0x/VpoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiX/+GJGE5yoABAIYPbM7GgACDEtaHKA5dng==",
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
    "channel_id": "ch_27TPUibg4r3zJ1tzEe9ugUCQYsxZ8j6Y96WLpLCgEBtr8Xahrk",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

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
      "fsm_id": "ba_cighcGq/d0g5s7SPzWFuZsBGHqnHwzhGAWcWdOM4A1e/zobI"
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
      "fsm_id": "ba_f5lgksFcIgGK/Hr1UagqFjIGCrLAyCUrT0YoJvPdqkKpA4Jp"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBtWoTokU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422132,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEC3RovNaMElYnSG88vaCGVw8rQo6uKCUGxRNm3qyPVYO5PL6u9dfUaE81Jap0eZOqqkqQtsKBHu3IsobPOtZv8AuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbW5HFFJ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422132,
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "fsm_id": "ba_f5lgksFcIgGK/Hr1UagqFjIGCrLAyCUrT0YoJvPdqkKpA4Jp",
      "signed_tx": "tx_+MwLAfhCuEC3RovNaMElYnSG88vaCGVw8rQo6uKCUGxRNm3qyPVYO5PL6u9dfUaE81Jap0eZOqqkqQtsKBHu3IsobPOtZv8AuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgbW5HFFJ",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422131,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAMUk87MgIbVpcPl2uVOtyYYcv8wIM/midgMnqaSCNFNXZKZdStHne9JS1VYjEXCfTABPLTAPW9tMeTOG0TmegBrhAt0aLzWjBJWJ0hvPL2ghlcPK0KOriglBsUTZt6sj1WDuTy+rvXX1GhPNSWqdHmTqqpKkLbCgR7tyLKGzzrWb/ALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G1pgUYPA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422131,
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAMUk87MgIbVpcPl2uVOtyYYcv8wIM/midgMnqaSCNFNXZKZdStHne9JS1VYjEXCfTABPLTAPW9tMeTOG0TmegBrhAt0aLzWjBJWJ0hvPL2ghlcPK0KOriglBsUTZt6sj1WDuTy+rvXX1GhPNSWqdHmTqqpKkLbCgR7tyLKGzzrWb/ALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G1pgUYPA==",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_cighcGq/d0g5s7SPzWFuZsBGHqnHwzhGAWcWdOM4A1e/zobI"
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAMUk87MgIbVpcPl2uVOtyYYcv8wIM/midgMnqaSCNFNXZKZdStHne9JS1VYjEXCfTABPLTAPW9tMeTOG0TmegBrhAt0aLzWjBJWJ0hvPL2ghlcPK0KOriglBsUTZt6sj1WDuTy+rvXX1GhPNSWqdHmTqqpKkLbCgR7tyLKGzzrWb/ALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G1pgUYPA==",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAMUk87MgIbVpcPl2uVOtyYYcv8wIM/midgMnqaSCNFNXZKZdStHne9JS1VYjEXCfTABPLTAPW9tMeTOG0TmegBrhAt0aLzWjBJWJ0hvPL2ghlcPK0KOriglBsUTZt6sj1WDuTy+rvXX1GhPNSWqdHmTqqpKkLbCgR7tyLKGzzrWb/ALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G1pgUYPA==",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAMUk87MgIbVpcPl2uVOtyYYcv8wIM/midgMnqaSCNFNXZKZdStHne9JS1VYjEXCfTABPLTAPW9tMeTOG0TmegBrhAt0aLzWjBJWJ0hvPL2ghlcPK0KOriglBsUTZt6sj1WDuTy+rvXX1GhPNSWqdHmTqqpKkLbCgR7tyLKGzzrWb/ALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G1pgUYPA==",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "message": {
        "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "message": {
        "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
  "id": -576460752303422130,
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
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422130,
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "state": "tx_+QEOCwH4hLhAMUk87MgIbVpcPl2uVOtyYYcv8wIM/midgMnqaSCNFNXZKZdStHne9JS1VYjEXCfTABPLTAPW9tMeTOG0TmegBrhAt0aLzWjBJWJ0hvPL2ghlcPK0KOriglBsUTZt6sj1WDuTy+rvXX1GhPNSWqdHmTqqpKkLbCgR7tyLKGzzrWb/ALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G1pgUYPA=="
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "state": "tx_+QEOCwH4hLhAMUk87MgIbVpcPl2uVOtyYYcv8wIM/midgMnqaSCNFNXZKZdStHne9JS1VYjEXCfTABPLTAPW9tMeTOG0TmegBrhAt0aLzWjBJWJ0hvPL2ghlcPK0KOriglBsUTZt6sj1WDuTy+rvXX1GhPNSWqdHmTqqpKkLbCgR7tyLKGzzrWb/ALiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4G1pgUYPA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422129,
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
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422129,
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBra217V3xEFLSG39GC+UCJDt7e0bzxn2W2ZCsNLl1NPvAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAieizCU=",
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
  "id": -576460752303422128,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA3NUiM0ZVQaCQ80oOG5BN24AhsN8SN/eKJHaQkJS4QRpycOvrcT5uoPJrp8IG88Wqtcj19thaLP39q9/cVoMsDuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1s6Ri"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422128,
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA3NUiM0ZVQaCQ80oOG5BN24AhsN8SN/eKJHaQkJS4QRpycOvrcT5uoPJrp8IG88Wqtcj19thaLP39q9/cVoMsDuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ1s6Ri",
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
  "id": -576460752303422127,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA3NUiM0ZVQaCQ80oOG5BN24AhsN8SN/eKJHaQkJS4QRpycOvrcT5uoPJrp8IG88Wqtcj19thaLP39q9/cVoMsDuEDHSvOAd613hj/ZmeCu/WuTLpHq9yu+9i9qJ4/CV1uPEDeJeP4ABwRwTAIJy2J8h9vFqCniCNFy+lhEbni2N3EAuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLuiTaA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422127,
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "state": "tx_+NILAfiEuEA3NUiM0ZVQaCQ80oOG5BN24AhsN8SN/eKJHaQkJS4QRpycOvrcT5uoPJrp8IG88Wqtcj19thaLP39q9/cVoMsDuEDHSvOAd613hj/ZmeCu/WuTLpHq9yu+9i9qJ4/CV1uPEDeJeP4ABwRwTAIJy2J8h9vFqCniCNFy+lhEbni2N3EAuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLuiTaA"
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "state": "tx_+NILAfiEuEA3NUiM0ZVQaCQ80oOG5BN24AhsN8SN/eKJHaQkJS4QRpycOvrcT5uoPJrp8IG88Wqtcj19thaLP39q9/cVoMsDuEDHSvOAd613hj/ZmeCu/WuTLpHq9yu+9i9qJ4/CV1uPEDeJeP4ABwRwTAIJy2J8h9vFqCniCNFy+lhEbni2N3EAuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLuiTaA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422126,
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
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422126,
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
  "id": -576460752303422125,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422125,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA3NUiM0ZVQaCQ80oOG5BN24AhsN8SN/eKJHaQkJS4QRpycOvrcT5uoPJrp8IG88Wqtcj19thaLP39q9/cVoMsDuEDHSvOAd613hj/ZmeCu/WuTLpHq9yu+9i9qJ4/CV1uPEDeJeP4ABwRwTAIJy2J8h9vFqCniCNFy+lhEbni2N3EAuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLuiTaA",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422124,
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
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422124,
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBra217V3xEFLSG39GC+UCJDt7e0bzxn2W2ZCsNLl1NPvA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3mHf/g=",
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
  "id": -576460752303422123,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC9CN1phSgwl6g03fh6UuK9vX2bMfLlqQ/wgF3wz5UKbX+Ah3cKfd9+YQRuAMckwC1s0hXSNZYY8ilBAe5lJ/cEuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvoW2d5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422123,
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC9CN1phSgwl6g03fh6UuK9vX2bMfLlqQ/wgF3wz5UKbX+Ah3cKfd9+YQRuAMckwC1s0hXSNZYY8ilBAe5lJ/cEuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvoW2d5",
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
  "id": -576460752303422122,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAJqrekQOPDlQvIQF8AjjOwxDm/mmxsT4BLM6RQwHW5sBAe/JHGjWvhYAfWfKxCpY3VGsj6evMvbXqdNsly94MKuEC9CN1phSgwl6g03fh6UuK9vX2bMfLlqQ/wgF3wz5UKbX+Ah3cKfd9+YQRuAMckwC1s0hXSNZYY8ilBAe5lJ/cEuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvdjHgF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422122,
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "state": "tx_+NILAfiEuEAJqrekQOPDlQvIQF8AjjOwxDm/mmxsT4BLM6RQwHW5sBAe/JHGjWvhYAfWfKxCpY3VGsj6evMvbXqdNsly94MKuEC9CN1phSgwl6g03fh6UuK9vX2bMfLlqQ/wgF3wz5UKbX+Ah3cKfd9+YQRuAMckwC1s0hXSNZYY8ilBAe5lJ/cEuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvdjHgF"
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "state": "tx_+NILAfiEuEAJqrekQOPDlQvIQF8AjjOwxDm/mmxsT4BLM6RQwHW5sBAe/JHGjWvhYAfWfKxCpY3VGsj6evMvbXqdNsly94MKuEC9CN1phSgwl6g03fh6UuK9vX2bMfLlqQ/wgF3wz5UKbX+Ah3cKfd9+YQRuAMckwC1s0hXSNZYY8ilBAe5lJ/cEuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvdjHgF"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422121,
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
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422121,
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
  "id": -576460752303422120,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
  "id": -576460752303422120,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAJqrekQOPDlQvIQF8AjjOwxDm/mmxsT4BLM6RQwHW5sBAe/JHGjWvhYAfWfKxCpY3VGsj6evMvbXqdNsly94MKuEC9CN1phSgwl6g03fh6UuK9vX2bMfLlqQ/wgF3wz5UKbX+Ah3cKfd9+YQRuAMckwC1s0hXSNZYY8ilBAe5lJ/cEuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvdjHgF",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NgGhBra217V3xEFLSG39GC+UCJDt7e0bzxn2W2ZCsNLl1NPvoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAJqrekQOPDlQvIQF8AjjOwxDm/mmxsT4BLM6RQwHW5sBAe/JHGjWvhYAfWfKxCpY3VGsj6evMvbXqdNsly94MKuEC9CN1phSgwl6g03fh6UuK9vX2bMfLlqQ/wgF3wz5UKbX+Ah3cKfd9+YQRuAMckwC1s0hXSNZYY8ilBAe5lJ/cEuEj4RjkCoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT7wOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGGSNwYbAAgbZQ1kwE",
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
    "signed_tx": "tx_+QLBCwH4QrhAlENgPMXDKYKY8tmC5GuEM/5rUxMwWSvju1JEXnvE61GygVxT+i4mO7cMpPWwTCCFx+iZgIzaIn+UB03rhRMOBrkCePkCdTYBoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT76EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhACaq3pEDjw5ULyEBfAI4zsMQ5v5psbE+ASzOkUMB1ubAQHvyRxo1r4WAH1nysQqWN1RrI+nrzL216nTbJcveDCrhAvQjdaYUoMJeoNN34elLivb19mzHy5akP8IBd8M+VCm1/gId3Cn3ffmEEbgDHJMAtbNIV0jWWGPIpQQHuZSf3BLhI+EY5AqEGtrbXtXfEQUtIbf0YL5QIkO3t7RvPGfZbZkKw0uXU0+8DoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIG2nDIdAQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAlENgPMXDKYKY8tmC5GuEM/5rUxMwWSvju1JEXnvE61GygVxT+i4mO7cMpPWwTCCFx+iZgIzaIn+UB03rhRMOBrkCePkCdTYBoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT76EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhACaq3pEDjw5ULyEBfAI4zsMQ5v5psbE+ASzOkUMB1ubAQHvyRxo1r4WAH1nysQqWN1RrI+nrzL216nTbJcveDCrhAvQjdaYUoMJeoNN34elLivb19mzHy5akP8IBd8M+VCm1/gId3Cn3ffmEEbgDHJMAtbNIV0jWWGPIpQQHuZSf3BLhI+EY5AqEGtrbXtXfEQUtIbf0YL5QIkO3t7RvPGfZbZkKw0uXU0+8DoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIG2nDIdAQ==",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAlENgPMXDKYKY8tmC5GuEM/5rUxMwWSvju1JEXnvE61GygVxT+i4mO7cMpPWwTCCFx+iZgIzaIn+UB03rhRMOBrkCePkCdTYBoQa2tte1d8RBS0ht/RgvlAiQ7e3tG88Z9ltmQrDS5dTT76EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhACaq3pEDjw5ULyEBfAI4zsMQ5v5psbE+ASzOkUMB1ubAQHvyRxo1r4WAH1nysQqWN1RrI+nrzL216nTbJcveDCrhAvQjdaYUoMJeoNN34elLivb19mzHy5akP8IBd8M+VCm1/gId3Cn3ffmEEbgDHJMAtbNIV0jWWGPIpQQHuZSf3BLhI+EY5AqEGtrbXtXfEQUtIbf0YL5QIkO3t7RvPGfZbZkKw0uXU0+8DoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhkjcGGwAIG2nDIdAQ==",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
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
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "signed_tx": "tx_+GcLAcC4YvhgOAGhBra217V3xEFLSG39GC+UCJDt7e0bzxn2W2ZCsNLl1NPvoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPbM7GgACDEtaH3HXj+Q==",
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
    "channel_id": "ch_2PUC1KYvyis1maWJ9A1XC3JMv9kiBoJX2QjM7tADepRspjhJqB",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
