
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
      "fsm_id": "ba_tyQcFG2ev0hFsBSg97vmN/ubOKdAQ21G46pIzEPxHcZx2Sb8"
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
      "fsm_id": "ba_hKRnm4yH/IlhEzVj8UDcJQJbGztnrr4ewSDdlnYUyyaFU4CD"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBikBle0E=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422341,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECeBWRZrmuaViXC8AVKF1xT3fswhq5bTmrHa6acsnLGWS0XXluVfXrJA0nJaVeCl/HeJ60LSGwPH5kg4CzxZPwPuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYqVcZmN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422341,
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "fsm_id": "ba_hKRnm4yH/IlhEzVj8UDcJQJbGztnrr4ewSDdlnYUyyaFU4CD",
      "signed_tx": "tx_+MwLAfhCuECeBWRZrmuaViXC8AVKF1xT3fswhq5bTmrHa6acsnLGWS0XXluVfXrJA0nJaVeCl/HeJ60LSGwPH5kg4CzxZPwPuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYqVcZmN",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422340,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAAsE3s1O4V4EomrqdbANRJEmrMsgRpf7qzR+xUxLN5EuYRrrRLief8+eMd+g1SVgC3HPQTuG6kWCl6IL39o7+BLhAngVkWa5rmlYlwvAFShdcU937MIauW05qx2umnLJyxlktF15blX16yQNJyWlXgpfx3ietC0hsDx+ZIOAs8WT8D7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GK/WrSDQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
  "id": -576460752303422340,
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAAsE3s1O4V4EomrqdbANRJEmrMsgRpf7qzR+xUxLN5EuYRrrRLief8+eMd+g1SVgC3HPQTuG6kWCl6IL39o7+BLhAngVkWa5rmlYlwvAFShdcU937MIauW05qx2umnLJyxlktF15blX16yQNJyWlXgpfx3ietC0hsDx+ZIOAs8WT8D7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GK/WrSDQ==",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_tyQcFG2ev0hFsBSg97vmN/ubOKdAQ21G46pIzEPxHcZx2Sb8"
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAAsE3s1O4V4EomrqdbANRJEmrMsgRpf7qzR+xUxLN5EuYRrrRLief8+eMd+g1SVgC3HPQTuG6kWCl6IL39o7+BLhAngVkWa5rmlYlwvAFShdcU937MIauW05qx2umnLJyxlktF15blX16yQNJyWlXgpfx3ietC0hsDx+ZIOAs8WT8D7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GK/WrSDQ==",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAAsE3s1O4V4EomrqdbANRJEmrMsgRpf7qzR+xUxLN5EuYRrrRLief8+eMd+g1SVgC3HPQTuG6kWCl6IL39o7+BLhAngVkWa5rmlYlwvAFShdcU937MIauW05qx2umnLJyxlktF15blX16yQNJyWlXgpfx3ietC0hsDx+ZIOAs8WT8D7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GK/WrSDQ==",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAAsE3s1O4V4EomrqdbANRJEmrMsgRpf7qzR+xUxLN5EuYRrrRLief8+eMd+g1SVgC3HPQTuG6kWCl6IL39o7+BLhAngVkWa5rmlYlwvAFShdcU937MIauW05qx2umnLJyxlktF15blX16yQNJyWlXgpfx3ietC0hsDx+ZIOAs8WT8D7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GK/WrSDQ==",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "message": {
        "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "message": {
        "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
  "id": -576460752303422339,
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
  "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
  "id": -576460752303422339,
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "state": "tx_+QEOCwH4hLhAAsE3s1O4V4EomrqdbANRJEmrMsgRpf7qzR+xUxLN5EuYRrrRLief8+eMd+g1SVgC3HPQTuG6kWCl6IL39o7+BLhAngVkWa5rmlYlwvAFShdcU937MIauW05qx2umnLJyxlktF15blX16yQNJyWlXgpfx3ietC0hsDx+ZIOAs8WT8D7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GK/WrSDQ=="
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "state": "tx_+QEOCwH4hLhAAsE3s1O4V4EomrqdbANRJEmrMsgRpf7qzR+xUxLN5EuYRrrRLief8+eMd+g1SVgC3HPQTuG6kWCl6IL39o7+BLhAngVkWa5rmlYlwvAFShdcU937MIauW05qx2umnLJyxlktF15blX16yQNJyWlXgpfx3ietC0hsDx+ZIOAs8WT8D7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GK/WrSDQ=="
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
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "signed_tx": "tx_+QGpCwHAuQGj+QGgNgGhBhFkP84Sv4rVXTjSkWy6SSI/bzTMNl3WC9Nrbh0uqrYOoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFUOWUILogYsACuNR",
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
    "signed_tx": "tx_+QHsCwH4QrhAetY4zk8p8EKUJBYEC49foHzA3YGWGCwpPHmZPLQTBoyPXvtEVE0WzUpWTuc+yWBXcvIf9pPAh0qK0r/ZJEdOCrkBo/kBoDYBoQYRZD/OEr+K1V040pFsukkiP280zDZd1gvTa24dLqq2DqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDllCC6IGLmCSLTQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAetY4zk8p8EKUJBYEC49foHzA3YGWGCwpPHmZPLQTBoyPXvtEVE0WzUpWTuc+yWBXcvIf9pPAh0qK0r/ZJEdOCrkBo/kBoDYBoQYRZD/OEr+K1V040pFsukkiP280zDZd1gvTa24dLqq2DqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDllCC6IGLmCSLTQ==",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAetY4zk8p8EKUJBYEC49foHzA3YGWGCwpPHmZPLQTBoyPXvtEVE0WzUpWTuc+yWBXcvIf9pPAh0qK0r/ZJEdOCrkBo/kBoDYBoQYRZD/OEr+K1V040pFsukkiP280zDZd1gvTa24dLqq2DqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDllCC6IGLmCSLTQ==",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBhFkP84Sv4rVXTjSkWy6SSI/bzTMNl3WC9Nrbh0uqrYOoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAA4NwRe2g==",
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
    "signed_tx": "tx_+KcLAfhCuEA454pvCcPFPcrzclemaLZG3/lBgGqiaITuX655qI0xreQQpQEHYDwG1kjRVmzwv4gpCchvNNfrbH1/HH5AFQABuF/4XTgBoQYRZD/OEr+K1V040pFsukkiP280zDZd1gvTa24dLqq2DqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAODC0V4Y="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA454pvCcPFPcrzclemaLZG3/lBgGqiaITuX655qI0xreQQpQEHYDwG1kjRVmzwv4gpCchvNNfrbH1/HH5AFQABuF/4XTgBoQYRZD/OEr+K1V040pFsukkiP280zDZd1gvTa24dLqq2DqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAODC0V4Y=",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA454pvCcPFPcrzclemaLZG3/lBgGqiaITuX655qI0xreQQpQEHYDwG1kjRVmzwv4gpCchvNNfrbH1/HH5AFQABuF/4XTgBoQYRZD/OEr+K1V040pFsukkiP280zDZd1gvTa24dLqq2DqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAODC0V4Y=",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
    "channel_id": "ch_8fFDL1LCWSmnF2tnbBcJrcRGS5Bx4oMXeV5fcXB215uLEt4fS",
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
      "fsm_id": "ba_RFckE6opxNdq52pW12gJEEcJnbBLC5+4k/TdrN/JNxXiGpRw"
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
      "fsm_id": "ba_ExzNuiODE9lTp80VxwXmsEsrqI3VNuLql7YlT0wHgMPRiqh5"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBjBAegL8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422338,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAAvPcJkOK0tRLnG0FkfFC0O/xF05pAInm+v6SDN6XQ8SiDPt0vNhS04GBDosOkW9Kqj4iWJIJjQI0Ekvoaj6sMuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYz5qmC7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422338,
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "fsm_id": "ba_ExzNuiODE9lTp80VxwXmsEsrqI3VNuLql7YlT0wHgMPRiqh5",
      "signed_tx": "tx_+MwLAfhCuEAAvPcJkOK0tRLnG0FkfFC0O/xF05pAInm+v6SDN6XQ8SiDPt0vNhS04GBDosOkW9Kqj4iWJIJjQI0Ekvoaj6sMuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYz5qmC7",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422337,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAALz3CZDitLUS5xtBZHxQtDv8RdOaQCJ5vr+kgzel0PEogz7dLzYUtOBgQ6LDpFvSqo+IliSCY0CNBJL6Go+rDLhABEnRoTlDTord32I4dinbI/BfqzoeWTJQxM2S6nHWfInyr84KVN/qHDEP5qLPCIAo6wTFpdALyoWzGHoB+nvUDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GMkE61Qg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
  "id": -576460752303422337,
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAALz3CZDitLUS5xtBZHxQtDv8RdOaQCJ5vr+kgzel0PEogz7dLzYUtOBgQ6LDpFvSqo+IliSCY0CNBJL6Go+rDLhABEnRoTlDTord32I4dinbI/BfqzoeWTJQxM2S6nHWfInyr84KVN/qHDEP5qLPCIAo6wTFpdALyoWzGHoB+nvUDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GMkE61Qg==",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_RFckE6opxNdq52pW12gJEEcJnbBLC5+4k/TdrN/JNxXiGpRw"
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAALz3CZDitLUS5xtBZHxQtDv8RdOaQCJ5vr+kgzel0PEogz7dLzYUtOBgQ6LDpFvSqo+IliSCY0CNBJL6Go+rDLhABEnRoTlDTord32I4dinbI/BfqzoeWTJQxM2S6nHWfInyr84KVN/qHDEP5qLPCIAo6wTFpdALyoWzGHoB+nvUDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GMkE61Qg==",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAALz3CZDitLUS5xtBZHxQtDv8RdOaQCJ5vr+kgzel0PEogz7dLzYUtOBgQ6LDpFvSqo+IliSCY0CNBJL6Go+rDLhABEnRoTlDTord32I4dinbI/BfqzoeWTJQxM2S6nHWfInyr84KVN/qHDEP5qLPCIAo6wTFpdALyoWzGHoB+nvUDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GMkE61Qg==",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAALz3CZDitLUS5xtBZHxQtDv8RdOaQCJ5vr+kgzel0PEogz7dLzYUtOBgQ6LDpFvSqo+IliSCY0CNBJL6Go+rDLhABEnRoTlDTord32I4dinbI/BfqzoeWTJQxM2S6nHWfInyr84KVN/qHDEP5qLPCIAo6wTFpdALyoWzGHoB+nvUDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GMkE61Qg==",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "message": {
        "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "message": {
        "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
  "id": -576460752303422336,
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
  "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
  "id": -576460752303422336,
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "state": "tx_+QEOCwH4hLhAALz3CZDitLUS5xtBZHxQtDv8RdOaQCJ5vr+kgzel0PEogz7dLzYUtOBgQ6LDpFvSqo+IliSCY0CNBJL6Go+rDLhABEnRoTlDTord32I4dinbI/BfqzoeWTJQxM2S6nHWfInyr84KVN/qHDEP5qLPCIAo6wTFpdALyoWzGHoB+nvUDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GMkE61Qg=="
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "state": "tx_+QEOCwH4hLhAALz3CZDitLUS5xtBZHxQtDv8RdOaQCJ5vr+kgzel0PEogz7dLzYUtOBgQ6LDpFvSqo+IliSCY0CNBJL6Go+rDLhABEnRoTlDTord32I4dinbI/BfqzoeWTJQxM2S6nHWfInyr84KVN/qHDEP5qLPCIAo6wTFpdALyoWzGHoB+nvUDbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GMkE61Qg=="
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
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBt+Tc/3y2AvqOTVRSH91620PQhGQMzefJ3vLT8/ZMTPUoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7uOFqAOSzd3FE=",
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
    "signed_tx": "tx_+QHrCwH4QrhARmE+AZg+Zci9jFHzqB71nw1PE92g6/k7mSTZkScDNSV9sN2ELH6d8QXV2XuJnIkahnPuJlSS26QWNcRzQUx8C7kBovkBnzYBoQbfk3P98tgL6jk1UUh/dettD0IRkDM3nyd7y0/P2TEz1KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7jhagDm5jAq7"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhARmE+AZg+Zci9jFHzqB71nw1PE92g6/k7mSTZkScDNSV9sN2ELH6d8QXV2XuJnIkahnPuJlSS26QWNcRzQUx8C7kBovkBnzYBoQbfk3P98tgL6jk1UUh/dettD0IRkDM3nyd7y0/P2TEz1KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7jhagDm5jAq7",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhARmE+AZg+Zci9jFHzqB71nw1PE92g6/k7mSTZkScDNSV9sN2ELH6d8QXV2XuJnIkahnPuJlSS26QWNcRzQUx8C7kBovkBnzYBoQbfk3P98tgL6jk1UUh/dettD0IRkDM3nyd7y0/P2TEz1KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7jhagDm5jAq7",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBt+Tc/3y2AvqOTVRSH91620PQhGQMzefJ3vLT8/ZMTPUoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAA69WF0Hw==",
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
    "signed_tx": "tx_+KcLAfhCuED6gHY7DUorgth6+irAxrMG8PmNYdAbcQN9ja3WdMXumKaPRk+PYkmZdDe+YCgI2r742tnbaE7iVGhmwG87pfkPuF/4XTgBoQbfk3P98tgL6jk1UUh/dettD0IRkDM3nyd7y0/P2TEz1KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAOgPGSCw="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuED6gHY7DUorgth6+irAxrMG8PmNYdAbcQN9ja3WdMXumKaPRk+PYkmZdDe+YCgI2r742tnbaE7iVGhmwG87pfkPuF/4XTgBoQbfk3P98tgL6jk1UUh/dettD0IRkDM3nyd7y0/P2TEz1KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAOgPGSCw=",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuED6gHY7DUorgth6+irAxrMG8PmNYdAbcQN9ja3WdMXumKaPRk+PYkmZdDe+YCgI2r742tnbaE7iVGhmwG87pfkPuF/4XTgBoQbfk3P98tgL6jk1UUh/dettD0IRkDM3nyd7y0/P2TEz1KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAOgPGSCw=",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
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
    "channel_id": "ch_2hTx1xJJkeypci7FysJUuBNgRTF1JPMZeNNkgmesqgT2een9Qa",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
