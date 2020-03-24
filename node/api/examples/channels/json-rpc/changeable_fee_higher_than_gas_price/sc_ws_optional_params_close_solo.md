
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
      "fsm_id": "ba_Pap2GJXaXsa7FfhZhFuqIJGFFah/ojrGq1xiqafLTMwe1Dr4"
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
      "fsm_id": "ba_KITsq14zamZUi2NKGKTQaXKyq1neflmRuWqzUa1ubPwimWaJ"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtyo1AzTg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422433,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDY3dkV8u47JfAO/XZlfy1wvnm/CKQ2YbzD9f8RW5KgGWWHyiNLuTp1inC3lVZzUKgDNu2naz75we6+hY/0CbEPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LcunAfsI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422433,
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "fsm_id": "ba_KITsq14zamZUi2NKGKTQaXKyq1neflmRuWqzUa1ubPwimWaJ",
      "signed_tx": "tx_+MsLAfhCuEDY3dkV8u47JfAO/XZlfy1wvnm/CKQ2YbzD9f8RW5KgGWWHyiNLuTp1inC3lVZzUKgDNu2naz75we6+hY/0CbEPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LcunAfsI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422432,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAdngd6bQFHDHIU2pIibmtFOdxtLGzMsEUyG0U38Ow6QVJjAufjKpQFRqnKgY2X/LDOcW4lcd/lwV5wm8ZSD6wA7hA2N3ZFfLuOyXwDv12ZX8tcL55vwikNmG8w/X/EVuSoBllh8ojS7k6dYpwt5VWc1CoAzbtp2s++cHuvoWP9AmxD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3L8SceO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
  "id": -576460752303422432,
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAdngd6bQFHDHIU2pIibmtFOdxtLGzMsEUyG0U38Ow6QVJjAufjKpQFRqnKgY2X/LDOcW4lcd/lwV5wm8ZSD6wA7hA2N3ZFfLuOyXwDv12ZX8tcL55vwikNmG8w/X/EVuSoBllh8ojS7k6dYpwt5VWc1CoAzbtp2s++cHuvoWP9AmxD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3L8SceO",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Pap2GJXaXsa7FfhZhFuqIJGFFah/ojrGq1xiqafLTMwe1Dr4"
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAdngd6bQFHDHIU2pIibmtFOdxtLGzMsEUyG0U38Ow6QVJjAufjKpQFRqnKgY2X/LDOcW4lcd/lwV5wm8ZSD6wA7hA2N3ZFfLuOyXwDv12ZX8tcL55vwikNmG8w/X/EVuSoBllh8ojS7k6dYpwt5VWc1CoAzbtp2s++cHuvoWP9AmxD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3L8SceO",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAdngd6bQFHDHIU2pIibmtFOdxtLGzMsEUyG0U38Ow6QVJjAufjKpQFRqnKgY2X/LDOcW4lcd/lwV5wm8ZSD6wA7hA2N3ZFfLuOyXwDv12ZX8tcL55vwikNmG8w/X/EVuSoBllh8ojS7k6dYpwt5VWc1CoAzbtp2s++cHuvoWP9AmxD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3L8SceO",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAdngd6bQFHDHIU2pIibmtFOdxtLGzMsEUyG0U38Ow6QVJjAufjKpQFRqnKgY2X/LDOcW4lcd/lwV5wm8ZSD6wA7hA2N3ZFfLuOyXwDv12ZX8tcL55vwikNmG8w/X/EVuSoBllh8ojS7k6dYpwt5VWc1CoAzbtp2s++cHuvoWP9AmxD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3L8SceO",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "message": {
        "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "message": {
        "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
  "id": -576460752303422431,
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
  "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
  "id": -576460752303422431,
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "event": "open"
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "state": "tx_+QENCwH4hLhAdngd6bQFHDHIU2pIibmtFOdxtLGzMsEUyG0U38Ow6QVJjAufjKpQFRqnKgY2X/LDOcW4lcd/lwV5wm8ZSD6wA7hA2N3ZFfLuOyXwDv12ZX8tcL55vwikNmG8w/X/EVuSoBllh8ojS7k6dYpwt5VWc1CoAzbtp2s++cHuvoWP9AmxD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3L8SceO"
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "state": "tx_+QENCwH4hLhAdngd6bQFHDHIU2pIibmtFOdxtLGzMsEUyG0U38Ow6QVJjAufjKpQFRqnKgY2X/LDOcW4lcd/lwV5wm8ZSD6wA7hA2N3ZFfLuOyXwDv12ZX8tcL55vwikNmG8w/X/EVuSoBllh8ojS7k6dYpwt5VWc1CoAzbtp2s++cHuvoWP9AmxD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3L8SceO"
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
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBjTOsr3Vs9e749iSxjmP3JdQbAAvziq6jq8/gVafMXzcoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACG4JEMNh5+c7VordM=",
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
    "signed_tx": "tx_+QHrCwH4QrhAPr/+BdthX93auF8TYQktUhwaJmIDF1reyP9DB8h9XHP2sXHVZkNAxyvqiYQ0/xtcpaD7jrjxiRdv9A+ckeJIDrkBovkBnzYBoQY0zrK91bPXu+PYksY5j9yXUGwAL84quo6vP4FWnzF83KEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhuCRDDYefnMWj2lR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAPr/+BdthX93auF8TYQktUhwaJmIDF1reyP9DB8h9XHP2sXHVZkNAxyvqiYQ0/xtcpaD7jrjxiRdv9A+ckeJIDrkBovkBnzYBoQY0zrK91bPXu+PYksY5j9yXUGwAL84quo6vP4FWnzF83KEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhuCRDDYefnMWj2lR",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAPr/+BdthX93auF8TYQktUhwaJmIDF1reyP9DB8h9XHP2sXHVZkNAxyvqiYQ0/xtcpaD7jrjxiRdv9A+ckeJIDrkBovkBnzYBoQY0zrK91bPXu+PYksY5j9yXUGwAL84quo6vP4FWnzF83KEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhuCRDDYefnMWj2lR",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBjTOsr3Vs9e749iSxjmP3JdQbAAvziq6jq8/gVafMXzcoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAAu/vRCBw==",
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
    "signed_tx": "tx_+KcLAfhCuEAuB4zIqcZao7+rkDp8i4g5QXxty6qapF3Os0XQawSAnYr5EFYxG4fiMjPgA3gkqdA1cmOCtoLj4Kxqp6lGLkIOuF/4XTgBoQY0zrK91bPXu+PYksY5j9yXUGwAL84quo6vP4FWnzF83KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygALjcUP7I="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAuB4zIqcZao7+rkDp8i4g5QXxty6qapF3Os0XQawSAnYr5EFYxG4fiMjPgA3gkqdA1cmOCtoLj4Kxqp6lGLkIOuF/4XTgBoQY0zrK91bPXu+PYksY5j9yXUGwAL84quo6vP4FWnzF83KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygALjcUP7I=",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAuB4zIqcZao7+rkDp8i4g5QXxty6qapF3Os0XQawSAnYr5EFYxG4fiMjPgA3gkqdA1cmOCtoLj4Kxqp6lGLkIOuF/4XTgBoQY0zrK91bPXu+PYksY5j9yXUGwAL84quo6vP4FWnzF83KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygALjcUP7I=",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
    "channel_id": "ch_QFttE7G9q3byNHUgXqTDyCPTeCYXsMqtSdUBSoweQiSoYNuRq",
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
      "fsm_id": "ba_d+ZaQHKHaMP2fZzP1FX/q/MA0sOIzBIFw/VuEPn5/Qaefz2r"
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
      "fsm_id": "ba_hdFjlEQDq6PGUxY1n1uXsdMCSTJeEtbEwCvb4Os1cjV5FiRG"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt04QQ5OQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422430,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDvWAF+ltPe7bk5Kdzi2i9gwPJShfoGhj4N2JBQxU+CnQTCOope2khwgTn1UZAP+omubJ/ydIaklqY2t3iJX4ALuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LdJENllg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422430,
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "fsm_id": "ba_hdFjlEQDq6PGUxY1n1uXsdMCSTJeEtbEwCvb4Os1cjV5FiRG",
      "signed_tx": "tx_+MsLAfhCuEDvWAF+ltPe7bk5Kdzi2i9gwPJShfoGhj4N2JBQxU+CnQTCOope2khwgTn1UZAP+omubJ/ydIaklqY2t3iJX4ALuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LdJENllg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422429,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhATxMFd4xz03hkf5Y1nAW6WHp9OFRTzNhGqiwHTC7qRETbdRVEBdtR695cbJ28k8+GlP8KQF+16ABkHydIfcoLALhA71gBfpbT3u25OSnc4tovYMDyUoX6BoY+DdiQUMVPgp0EwjqKXtpIcIE59VGQD/qJrmyf8nSGpJamNrd4iV+AC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3QH4vaf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
  "id": -576460752303422429,
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhATxMFd4xz03hkf5Y1nAW6WHp9OFRTzNhGqiwHTC7qRETbdRVEBdtR695cbJ28k8+GlP8KQF+16ABkHydIfcoLALhA71gBfpbT3u25OSnc4tovYMDyUoX6BoY+DdiQUMVPgp0EwjqKXtpIcIE59VGQD/qJrmyf8nSGpJamNrd4iV+AC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3QH4vaf",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_d+ZaQHKHaMP2fZzP1FX/q/MA0sOIzBIFw/VuEPn5/Qaefz2r"
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhATxMFd4xz03hkf5Y1nAW6WHp9OFRTzNhGqiwHTC7qRETbdRVEBdtR695cbJ28k8+GlP8KQF+16ABkHydIfcoLALhA71gBfpbT3u25OSnc4tovYMDyUoX6BoY+DdiQUMVPgp0EwjqKXtpIcIE59VGQD/qJrmyf8nSGpJamNrd4iV+AC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3QH4vaf",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhATxMFd4xz03hkf5Y1nAW6WHp9OFRTzNhGqiwHTC7qRETbdRVEBdtR695cbJ28k8+GlP8KQF+16ABkHydIfcoLALhA71gBfpbT3u25OSnc4tovYMDyUoX6BoY+DdiQUMVPgp0EwjqKXtpIcIE59VGQD/qJrmyf8nSGpJamNrd4iV+AC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3QH4vaf",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhATxMFd4xz03hkf5Y1nAW6WHp9OFRTzNhGqiwHTC7qRETbdRVEBdtR695cbJ28k8+GlP8KQF+16ABkHydIfcoLALhA71gBfpbT3u25OSnc4tovYMDyUoX6BoY+DdiQUMVPgp0EwjqKXtpIcIE59VGQD/qJrmyf8nSGpJamNrd4iV+AC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3QH4vaf",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "message": {
        "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "message": {
        "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
  "id": -576460752303422428,
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
  "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
  "id": -576460752303422428,
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "state": "tx_+QENCwH4hLhATxMFd4xz03hkf5Y1nAW6WHp9OFRTzNhGqiwHTC7qRETbdRVEBdtR695cbJ28k8+GlP8KQF+16ABkHydIfcoLALhA71gBfpbT3u25OSnc4tovYMDyUoX6BoY+DdiQUMVPgp0EwjqKXtpIcIE59VGQD/qJrmyf8nSGpJamNrd4iV+AC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3QH4vaf"
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "state": "tx_+QENCwH4hLhATxMFd4xz03hkf5Y1nAW6WHp9OFRTzNhGqiwHTC7qRETbdRVEBdtR695cbJ28k8+GlP8KQF+16ABkHydIfcoLALhA71gBfpbT3u25OSnc4tovYMDyUoX6BoY+DdiQUMVPgp0EwjqKXtpIcIE59VGQD/qJrmyf8nSGpJamNrd4iV+AC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3QH4vaf"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBkMvMx8P+NLAJqfwj+Sbhgj7K8UYF1M4apzze7t6X3v6oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACG4JEMNh5+Ly84TNM=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAmS916XQsUIAHQXC82FpVU9Rxz93I/K2ps+e8pLGq7HkER+i0YFXGpFWY5i+/y/ydiYtTuvsWkXjyXe3SDAppDbkBovkBnzYBoQZDLzMfD/jSwCan8I/km4YI+yvFGBdTOGqc83u7el97+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhuCRDDYefi/tdRT4"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAmS916XQsUIAHQXC82FpVU9Rxz93I/K2ps+e8pLGq7HkER+i0YFXGpFWY5i+/y/ydiYtTuvsWkXjyXe3SDAppDbkBovkBnzYBoQZDLzMfD/jSwCan8I/km4YI+yvFGBdTOGqc83u7el97+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhuCRDDYefi/tdRT4",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAmS916XQsUIAHQXC82FpVU9Rxz93I/K2ps+e8pLGq7HkER+i0YFXGpFWY5i+/y/ydiYtTuvsWkXjyXe3SDAppDbkBovkBnzYBoQZDLzMfD/jSwCan8I/km4YI+yvFGBdTOGqc83u7el97+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhuCRDDYefi/tdRT4",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBkMvMx8P+NLAJqfwj+Sbhgj7K8UYF1M4apzze7t6X3v6oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAAwzabdQA==",
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
    "signed_tx": "tx_+KcLAfhCuEDnMaFDPnS3PnX9pvoXfA+Jb9kOb8Aurnu02QYjOg0jXRY5YmRSOOhdmOHJvAacsfUUQjjVoQMfYoQU3284vQ0GuF/4XTgBoQZDLzMfD/jSwCan8I/km4YI+yvFGBdTOGqc83u7el97+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAMHGTc/Y="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDnMaFDPnS3PnX9pvoXfA+Jb9kOb8Aurnu02QYjOg0jXRY5YmRSOOhdmOHJvAacsfUUQjjVoQMfYoQU3284vQ0GuF/4XTgBoQZDLzMfD/jSwCan8I/km4YI+yvFGBdTOGqc83u7el97+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAMHGTc/Y=",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDnMaFDPnS3PnX9pvoXfA+Jb9kOb8Aurnu02QYjOg0jXRY5YmRSOOhdmOHJvAacsfUUQjjVoQMfYoQU3284vQ0GuF/4XTgBoQZDLzMfD/jSwCan8I/km4YI+yvFGBdTOGqc83u7el97+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAMHGTc/Y=",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
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
    "channel_id": "ch_Wb8ozLraq6Jn2ugs3AMbjNVi5622xjzsGcKEAFiKPNzfkZVSR",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
