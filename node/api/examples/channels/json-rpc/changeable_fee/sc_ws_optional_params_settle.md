
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
      "fsm_id": "ba_BvBZhElXySjI3hK36HOtqDUJkL+PlYE3mbyPSrhTgPtNoVqc"
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
      "fsm_id": "ba_d5EsAxcqwGBb4bH8aOwVpagGgfbPfjYyM3PN4O+l9vtyRVT6"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtKGhhfHg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422593,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuED06st9rrXpf6o6jWwU/w2RWGozcy5SQCrOJe6nn4FyYd/6RWSY39NlsEB+aOnOyUEI8pZ6mQymiB6768ie1jQBuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LStDLfO8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422593,
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "fsm_id": "ba_d5EsAxcqwGBb4bH8aOwVpagGgfbPfjYyM3PN4O+l9vtyRVT6",
      "signed_tx": "tx_+MsLAfhCuED06st9rrXpf6o6jWwU/w2RWGozcy5SQCrOJe6nn4FyYd/6RWSY39NlsEB+aOnOyUEI8pZ6mQymiB6768ie1jQBuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LStDLfO8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422592,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAslMxlCNCl5ogPA5PVw6+qNbZDj6KR42KQb966cmEYbNtcWGZjpaAsbB4Bb1Ek9LbTB0ScMat9KpxUP2Mv1fXDrhA9OrLfa616X+qOo1sFP8NkVhqM3MuUkAqziXup5+BcmHf+kVkmN/TZbBAfmjpzslBCPKWepkMpogeu+vIntY0AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0pfL4UC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
  "id": -576460752303422592,
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAslMxlCNCl5ogPA5PVw6+qNbZDj6KR42KQb966cmEYbNtcWGZjpaAsbB4Bb1Ek9LbTB0ScMat9KpxUP2Mv1fXDrhA9OrLfa616X+qOo1sFP8NkVhqM3MuUkAqziXup5+BcmHf+kVkmN/TZbBAfmjpzslBCPKWepkMpogeu+vIntY0AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0pfL4UC",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_BvBZhElXySjI3hK36HOtqDUJkL+PlYE3mbyPSrhTgPtNoVqc"
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAslMxlCNCl5ogPA5PVw6+qNbZDj6KR42KQb966cmEYbNtcWGZjpaAsbB4Bb1Ek9LbTB0ScMat9KpxUP2Mv1fXDrhA9OrLfa616X+qOo1sFP8NkVhqM3MuUkAqziXup5+BcmHf+kVkmN/TZbBAfmjpzslBCPKWepkMpogeu+vIntY0AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0pfL4UC",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAslMxlCNCl5ogPA5PVw6+qNbZDj6KR42KQb966cmEYbNtcWGZjpaAsbB4Bb1Ek9LbTB0ScMat9KpxUP2Mv1fXDrhA9OrLfa616X+qOo1sFP8NkVhqM3MuUkAqziXup5+BcmHf+kVkmN/TZbBAfmjpzslBCPKWepkMpogeu+vIntY0AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0pfL4UC",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAslMxlCNCl5ogPA5PVw6+qNbZDj6KR42KQb966cmEYbNtcWGZjpaAsbB4Bb1Ek9LbTB0ScMat9KpxUP2Mv1fXDrhA9OrLfa616X+qOo1sFP8NkVhqM3MuUkAqziXup5+BcmHf+kVkmN/TZbBAfmjpzslBCPKWepkMpogeu+vIntY0AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0pfL4UC",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "message": {
        "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "message": {
        "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
  "id": -576460752303422591,
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
  "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
  "id": -576460752303422591,
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "state": "tx_+QENCwH4hLhAslMxlCNCl5ogPA5PVw6+qNbZDj6KR42KQb966cmEYbNtcWGZjpaAsbB4Bb1Ek9LbTB0ScMat9KpxUP2Mv1fXDrhA9OrLfa616X+qOo1sFP8NkVhqM3MuUkAqziXup5+BcmHf+kVkmN/TZbBAfmjpzslBCPKWepkMpogeu+vIntY0AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0pfL4UC"
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "state": "tx_+QENCwH4hLhAslMxlCNCl5ogPA5PVw6+qNbZDj6KR42KQb966cmEYbNtcWGZjpaAsbB4Bb1Ek9LbTB0ScMat9KpxUP2Mv1fXDrhA9OrLfa616X+qOo1sFP8NkVhqM3MuUkAqziXup5+BcmHf+kVkmN/TZbBAfmjpzslBCPKWepkMpogeu+vIntY0AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0pfL4UC"
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
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBvC9HHS3e4tK4gT5dISkAs0c7GDBr8/rQu+jy0TeDSzRoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7sgIAAS/QdoAI=",
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
    "signed_tx": "tx_+QHrCwH4QrhAKYmODTn9QAD9iJeeqWT16jx/VEnDHl8Q1sLLh3CGb+lp6N5HTnzR3vo0+TMdmrQI+xECr2X8I9yzzUIdKZK5CrkBovkBnzYBoQbwvRx0t3uLSuIE+XSEpALNHOxgwa/P60Lvo8tE3g0s0aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAEu+F1Tj"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAKYmODTn9QAD9iJeeqWT16jx/VEnDHl8Q1sLLh3CGb+lp6N5HTnzR3vo0+TMdmrQI+xECr2X8I9yzzUIdKZK5CrkBovkBnzYBoQbwvRx0t3uLSuIE+XSEpALNHOxgwa/P60Lvo8tE3g0s0aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAEu+F1Tj",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAKYmODTn9QAD9iJeeqWT16jx/VEnDHl8Q1sLLh3CGb+lp6N5HTnzR3vo0+TMdmrQI+xECr2X8I9yzzUIdKZK5CrkBovkBnzYBoQbwvRx0t3uLSuIE+XSEpALNHOxgwa/P60Lvo8tE3g0s0aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAEu+F1Tj",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBvC9HHS3e4tK4gT5dISkAs0c7GDBr8/rQu+jy0TeDSzRoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIZwSIYbDz8gDXhQ5Q==",
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
    "signed_tx": "tx_+KcLAfhCuEB/9J7V2ygx8UZj/6usNUgw7Duem2uep0dfmzaUlV5CoRpGrk44Orsy1SkfJ3PHvIGz1IxIfubbG6YYxPDXdYUMuF/4XTgBoQbwvRx0t3uLSuIE+XSEpALNHOxgwa/P60Lvo8tE3g0s0aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGcEiGGw8/IG+XcsY="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB/9J7V2ygx8UZj/6usNUgw7Duem2uep0dfmzaUlV5CoRpGrk44Orsy1SkfJ3PHvIGz1IxIfubbG6YYxPDXdYUMuF/4XTgBoQbwvRx0t3uLSuIE+XSEpALNHOxgwa/P60Lvo8tE3g0s0aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGcEiGGw8/IG+XcsY=",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB/9J7V2ygx8UZj/6usNUgw7Duem2uep0dfmzaUlV5CoRpGrk44Orsy1SkfJ3PHvIGz1IxIfubbG6YYxPDXdYUMuF/4XTgBoQbwvRx0t3uLSuIE+XSEpALNHOxgwa/P60Lvo8tE3g0s0aEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGcEiGGw8/IG+XcsY=",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
    "channel_id": "ch_2q2M9b9VNyhi2pCUZ9Z4dUfmAkhvSh9wZPFribHCdxyXpNF8dN",
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
      "fsm_id": "ba_EXDcMU4bc+pDySCbZxBClr7ldrkdR0Byc10yrp9fcjasxr2p"
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
      "fsm_id": "ba_awNKAccfXo7UexYN/C0iJWojYNsggcYpGAp9fhrQ2iILJaEG"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtMPqveHQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422590,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBE/IqHtZAYTTLuFQnzaxpSskI/8oIJxM6LYsg09g8RiuBcGno1hJDApx2nPAS0jUePnbKl6YLg1A6OT0HxaxIKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LTFDXGKU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422590,
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "fsm_id": "ba_awNKAccfXo7UexYN/C0iJWojYNsggcYpGAp9fhrQ2iILJaEG",
      "signed_tx": "tx_+MsLAfhCuEBE/IqHtZAYTTLuFQnzaxpSskI/8oIJxM6LYsg09g8RiuBcGno1hJDApx2nPAS0jUePnbKl6YLg1A6OT0HxaxIKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LTFDXGKU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422589,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhARPyKh7WQGE0y7hUJ82saUrJCP/KCCcTOi2LINPYPEYrgXBp6NYSQwKcdpzwEtI1Hj52ypemC4NQOjk9B8WsSCrhAzLDxUJsZLtlXSCtUIhZo0weHtOB1HiCRB0JvIh9jwf6z/sVnIjWIzf2X6OadDeDgTPNd3kj/HpSAMcres9axDriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0x6GwRT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
  "id": -576460752303422589,
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhARPyKh7WQGE0y7hUJ82saUrJCP/KCCcTOi2LINPYPEYrgXBp6NYSQwKcdpzwEtI1Hj52ypemC4NQOjk9B8WsSCrhAzLDxUJsZLtlXSCtUIhZo0weHtOB1HiCRB0JvIh9jwf6z/sVnIjWIzf2X6OadDeDgTPNd3kj/HpSAMcres9axDriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0x6GwRT",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_EXDcMU4bc+pDySCbZxBClr7ldrkdR0Byc10yrp9fcjasxr2p"
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhARPyKh7WQGE0y7hUJ82saUrJCP/KCCcTOi2LINPYPEYrgXBp6NYSQwKcdpzwEtI1Hj52ypemC4NQOjk9B8WsSCrhAzLDxUJsZLtlXSCtUIhZo0weHtOB1HiCRB0JvIh9jwf6z/sVnIjWIzf2X6OadDeDgTPNd3kj/HpSAMcres9axDriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0x6GwRT",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARPyKh7WQGE0y7hUJ82saUrJCP/KCCcTOi2LINPYPEYrgXBp6NYSQwKcdpzwEtI1Hj52ypemC4NQOjk9B8WsSCrhAzLDxUJsZLtlXSCtUIhZo0weHtOB1HiCRB0JvIh9jwf6z/sVnIjWIzf2X6OadDeDgTPNd3kj/HpSAMcres9axDriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0x6GwRT",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARPyKh7WQGE0y7hUJ82saUrJCP/KCCcTOi2LINPYPEYrgXBp6NYSQwKcdpzwEtI1Hj52ypemC4NQOjk9B8WsSCrhAzLDxUJsZLtlXSCtUIhZo0weHtOB1HiCRB0JvIh9jwf6z/sVnIjWIzf2X6OadDeDgTPNd3kj/HpSAMcres9axDriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0x6GwRT",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "message": {
        "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "message": {
        "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
  "id": -576460752303422588,
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
  "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
  "id": -576460752303422588,
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "state": "tx_+QENCwH4hLhARPyKh7WQGE0y7hUJ82saUrJCP/KCCcTOi2LINPYPEYrgXBp6NYSQwKcdpzwEtI1Hj52ypemC4NQOjk9B8WsSCrhAzLDxUJsZLtlXSCtUIhZo0weHtOB1HiCRB0JvIh9jwf6z/sVnIjWIzf2X6OadDeDgTPNd3kj/HpSAMcres9axDriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0x6GwRT"
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "state": "tx_+QENCwH4hLhARPyKh7WQGE0y7hUJ82saUrJCP/KCCcTOi2LINPYPEYrgXBp6NYSQwKcdpzwEtI1Hj52ypemC4NQOjk9B8WsSCrhAzLDxUJsZLtlXSCtUIhZo0weHtOB1HiCRB0JvIh9jwf6z/sVnIjWIzf2X6OadDeDgTPNd3kj/HpSAMcres9axDriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0x6GwRT"
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
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBvHvV+xRcFUrf6c4+7hgK4RKkY/0FFCYICAW6thG2+znoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFT7sgIAATVctDg8=",
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
    "signed_tx": "tx_+QHrCwH4QrhAei4iGoz1hJ6pNv/l3jzEE4GypSsz6HX6XfJ4+GhC2uNYSMBwvj3khRbkPwr8JlvTC5NuuP+fwozcTBG2bAaTA7kBovkBnzYBoQbx71fsUXBVK3+nOPu4YCuESpGP9BRQmCAgFurYRtvs56EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAE1EA/k0"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAei4iGoz1hJ6pNv/l3jzEE4GypSsz6HX6XfJ4+GhC2uNYSMBwvj3khRbkPwr8JlvTC5NuuP+fwozcTBG2bAaTA7kBovkBnzYBoQbx71fsUXBVK3+nOPu4YCuESpGP9BRQmCAgFurYRtvs56EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAE1EA/k0",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAei4iGoz1hJ6pNv/l3jzEE4GypSsz6HX6XfJ4+GhC2uNYSMBwvj3khRbkPwr8JlvTC5NuuP+fwozcTBG2bAaTA7kBovkBnzYBoQbx71fsUXBVK3+nOPu4YCuESpGP9BRQmCAgFurYRtvs56EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhU+7ICAAE1EA/k0",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBvHvV+xRcFUrf6c4+7hgK4RKkY/0FFCYICAW6thG2+znoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiX/+GJGE5yoABAIZwSIYbDz9OFMlRvQ==",
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
    "signed_tx": "tx_+KcLAfhCuEBHcbn9dPTYpLGmoQbDDOoktBAOiY4qCFhOV+6rioOmV3ZmJkohf4iNvrEcF4qEDFBJQNvsWXqoXdFzG/sqhnwBuF/4XTgBoQbx71fsUXBVK3+nOPu4YCuESpGP9BRQmCAgFurYRtvs56EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGcEiGGw8/TmSnjGo="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBHcbn9dPTYpLGmoQbDDOoktBAOiY4qCFhOV+6rioOmV3ZmJkohf4iNvrEcF4qEDFBJQNvsWXqoXdFzG/sqhnwBuF/4XTgBoQbx71fsUXBVK3+nOPu4YCuESpGP9BRQmCAgFurYRtvs56EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGcEiGGw8/TmSnjGo=",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBHcbn9dPTYpLGmoQbDDOoktBAOiY4qCFhOV+6rioOmV3ZmJkohf4iNvrEcF4qEDFBJQNvsWXqoXdFzG/sqhnwBuF/4XTgBoQbx71fsUXBVK3+nOPu4YCuESpGP9BRQmCAgFurYRtvs56EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGcEiGGw8/TmSnjGo=",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
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
    "channel_id": "ch_2qYuPQbchGqjp335TNqaAXRxJrkrta69Gw614XwwvHmNvpUP4e",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
