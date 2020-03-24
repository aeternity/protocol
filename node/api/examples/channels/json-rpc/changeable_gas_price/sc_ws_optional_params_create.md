
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&gas_price=1000001234&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_zNuOuOVlV76+jk9rbMPMPv8x7R2lSLP1P4yDhXtvVWNSm7JN"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&gas_price=1000001234&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_9zgaN4CnbYin5n9idAfCagdJouAn3mGdQy/oJXRKlvAidGe5"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeyMN6MCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtPBz9FoA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422587,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECUiSGyjbatDOkVGf6t2AsOHnQduRcbQkGCauUdhIhYJ0ro3/+PPRBGYOsIAqREFLL1xK+wJbwCye4T4NzYujcKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnsjDejAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LTx7hCBI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422587,
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "fsm_id": "ba_9zgaN4CnbYin5n9idAfCagdJouAn3mGdQy/oJXRKlvAidGe5",
      "signed_tx": "tx_+MsLAfhCuECUiSGyjbatDOkVGf6t2AsOHnQduRcbQkGCauUdhIhYJ0ro3/+PPRBGYOsIAqREFLL1xK+wJbwCye4T4NzYujcKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnsjDejAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LTx7hCBI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422586,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAVvtvSwr8oz/Ge/0N4oCIk93GWYONLn4x1Nz0/DM5qqeB5+mRl/eAxVAYy6QvBMxTCUl+Hw6WkD0pN+ZSaCkSDrhAlIkhso22rQzpFRn+rdgLDh50HbkXG0JBgmrlHYSIWCdK6N//jz0QRmDrCAKkRBSy9cSvsCW8AsnuE+Dc2Lo3CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0+gfYlz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
  "id": -576460752303422586,
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAVvtvSwr8oz/Ge/0N4oCIk93GWYONLn4x1Nz0/DM5qqeB5+mRl/eAxVAYy6QvBMxTCUl+Hw6WkD0pN+ZSaCkSDrhAlIkhso22rQzpFRn+rdgLDh50HbkXG0JBgmrlHYSIWCdK6N//jz0QRmDrCAKkRBSy9cSvsCW8AsnuE+Dc2Lo3CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0+gfYlz",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_zNuOuOVlV76+jk9rbMPMPv8x7R2lSLP1P4yDhXtvVWNSm7JN"
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAVvtvSwr8oz/Ge/0N4oCIk93GWYONLn4x1Nz0/DM5qqeB5+mRl/eAxVAYy6QvBMxTCUl+Hw6WkD0pN+ZSaCkSDrhAlIkhso22rQzpFRn+rdgLDh50HbkXG0JBgmrlHYSIWCdK6N//jz0QRmDrCAKkRBSy9cSvsCW8AsnuE+Dc2Lo3CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0+gfYlz",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAVvtvSwr8oz/Ge/0N4oCIk93GWYONLn4x1Nz0/DM5qqeB5+mRl/eAxVAYy6QvBMxTCUl+Hw6WkD0pN+ZSaCkSDrhAlIkhso22rQzpFRn+rdgLDh50HbkXG0JBgmrlHYSIWCdK6N//jz0QRmDrCAKkRBSy9cSvsCW8AsnuE+Dc2Lo3CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0+gfYlz",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAVvtvSwr8oz/Ge/0N4oCIk93GWYONLn4x1Nz0/DM5qqeB5+mRl/eAxVAYy6QvBMxTCUl+Hw6WkD0pN+ZSaCkSDrhAlIkhso22rQzpFRn+rdgLDh50HbkXG0JBgmrlHYSIWCdK6N//jz0QRmDrCAKkRBSy9cSvsCW8AsnuE+Dc2Lo3CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0+gfYlz",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "message": {
        "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "message": {
        "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
  "id": -576460752303422585,
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
  "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
  "id": -576460752303422585,
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "state": "tx_+QENCwH4hLhAVvtvSwr8oz/Ge/0N4oCIk93GWYONLn4x1Nz0/DM5qqeB5+mRl/eAxVAYy6QvBMxTCUl+Hw6WkD0pN+ZSaCkSDrhAlIkhso22rQzpFRn+rdgLDh50HbkXG0JBgmrlHYSIWCdK6N//jz0QRmDrCAKkRBSy9cSvsCW8AsnuE+Dc2Lo3CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0+gfYlz"
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "state": "tx_+QENCwH4hLhAVvtvSwr8oz/Ge/0N4oCIk93GWYONLn4x1Nz0/DM5qqeB5+mRl/eAxVAYy6QvBMxTCUl+Hw6WkD0pN+ZSaCkSDrhAlIkhso22rQzpFRn+rdgLDh50HbkXG0JBgmrlHYSIWCdK6N//jz0QRmDrCAKkRBSy9cSvsCW8AsnuE+Dc2Lo3CriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0+gfYlz"
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBhZ88OUDP/HNB736/CESXW2V7eirN9l2ovxTaeBzz1F5oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/+GHLHOiuwBAIYPXtZ/KABQHe8oJA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422584,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECzDjEsDrtK5Tfk4KRmHQm0f6+X0zE2QImWQwQVtsJqvLvVJ/z6G7HUQt5zF+D45+v7oK38gAI1XbGes4XlN88NuF/4XTUBoQYWfPDlAz/xzQe9+vwhEl1tle3oqzfZdqL8U2ngc89ReaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAUAl9ZlU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
  "id": -576460752303422584,
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECzDjEsDrtK5Tfk4KRmHQm0f6+X0zE2QImWQwQVtsJqvLvVJ/z6G7HUQt5zF+D45+v7oK38gAI1XbGes4XlN88NuF/4XTUBoQYWfPDlAz/xzQe9+vwhEl1tle3oqzfZdqL8U2ngc89ReaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAUAl9ZlU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422583,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEANXOjOYLPH/VlgRG5e0G1dXfgUQ7bkKe2fNaXCH5LwgYfwnGAUaVel0ngJP4PkCZJXUplvO6xU+r6GhcmWEkcIuECzDjEsDrtK5Tfk4KRmHQm0f6+X0zE2QImWQwQVtsJqvLvVJ/z6G7HUQt5zF+D45+v7oK38gAI1XbGes4XlN88NuF/4XTUBoQYWfPDlAz/xzQe9+vwhEl1tle3oqzfZdqL8U2ngc89ReaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAUFxcIQE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
  "id": -576460752303422583,
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEANXOjOYLPH/VlgRG5e0G1dXfgUQ7bkKe2fNaXCH5LwgYfwnGAUaVel0ngJP4PkCZJXUplvO6xU+r6GhcmWEkcIuECzDjEsDrtK5Tfk4KRmHQm0f6+X0zE2QImWQwQVtsJqvLvVJ/z6G7HUQt5zF+D45+v7oK38gAI1XbGes4XlN88NuF/4XTUBoQYWfPDlAz/xzQe9+vwhEl1tle3oqzfZdqL8U2ngc89ReaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAUFxcIQE=",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEANXOjOYLPH/VlgRG5e0G1dXfgUQ7bkKe2fNaXCH5LwgYfwnGAUaVel0ngJP4PkCZJXUplvO6xU+r6GhcmWEkcIuECzDjEsDrtK5Tfk4KRmHQm0f6+X0zE2QImWQwQVtsJqvLvVJ/z6G7HUQt5zF+D45+v7oK38gAI1XbGes4XlN88NuF/4XTUBoQYWfPDlAz/xzQe9+vwhEl1tle3oqzfZdqL8U2ngc89ReaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAUFxcIQE=",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEANXOjOYLPH/VlgRG5e0G1dXfgUQ7bkKe2fNaXCH5LwgYfwnGAUaVel0ngJP4PkCZJXUplvO6xU+r6GhcmWEkcIuECzDjEsDrtK5Tfk4KRmHQm0f6+X0zE2QImWQwQVtsJqvLvVJ/z6G7HUQt5zF+D45+v7oK38gAI1XbGes4XlN88NuF/4XTUBoQYWfPDlAz/xzQe9+vwhEl1tle3oqzfZdqL8U2ngc89ReaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAUFxcIQE=",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEANXOjOYLPH/VlgRG5e0G1dXfgUQ7bkKe2fNaXCH5LwgYfwnGAUaVel0ngJP4PkCZJXUplvO6xU+r6GhcmWEkcIuECzDjEsDrtK5Tfk4KRmHQm0f6+X0zE2QImWQwQVtsJqvLvVJ/z6G7HUQt5zF+D45+v7oK38gAI1XbGes4XlN88NuF/4XTUBoQYWfPDlAz/xzQe9+vwhEl1tle3oqzfZdqL8U2ngc89ReaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAUFxcIQE=",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
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
    "channel_id": "ch_AuRmgMquf9v3vyv1hqvUJHRYBYMZnCd2ZC4vsQiLhx6KHK2tm",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
