
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
      "fsm_id": "ba_19jPCeFjx5s2X0OvQuzTO3ewIWE1NMhLK3XUozDiWYCDRA23"
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
      "fsm_id": "ba_pdmdTdVMKnrvENeLbiMgvMOo8fwN6ryvwKWeR39/4xI6cqKn"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtCe93lXw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422617,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECqRpAHKm2Kh4U1YIHIaTbLdI7pfIEEUiU+ucsbvLuCSjAGrd4PPW8cJeVmvcKhYgDmyvS9sFPPg1HZAFzrS9MKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LQvp1CeY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422617,
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "fsm_id": "ba_pdmdTdVMKnrvENeLbiMgvMOo8fwN6ryvwKWeR39/4xI6cqKn",
      "signed_tx": "tx_+MsLAfhCuECqRpAHKm2Kh4U1YIHIaTbLdI7pfIEEUiU+ucsbvLuCSjAGrd4PPW8cJeVmvcKhYgDmyvS9sFPPg1HZAFzrS9MKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LQvp1CeY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422616,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAlOsjJukg53W2a4ObK1374kNmQ8zg/Ryd7b7bX0BGD0E4WWLQMyh+g260LrE12az+mPvuKE77PJPArTT8IuWhD7hAqkaQByptioeFNWCByGk2y3SO6XyBBFIlPrnLG7y7gkowBq3eDz1vHCXlZr3CoWIA5sr0vbBTz4NR2QBc60vTCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0Lwc9v2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
  "id": -576460752303422616,
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAlOsjJukg53W2a4ObK1374kNmQ8zg/Ryd7b7bX0BGD0E4WWLQMyh+g260LrE12az+mPvuKE77PJPArTT8IuWhD7hAqkaQByptioeFNWCByGk2y3SO6XyBBFIlPrnLG7y7gkowBq3eDz1vHCXlZr3CoWIA5sr0vbBTz4NR2QBc60vTCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0Lwc9v2",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_19jPCeFjx5s2X0OvQuzTO3ewIWE1NMhLK3XUozDiWYCDRA23"
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAlOsjJukg53W2a4ObK1374kNmQ8zg/Ryd7b7bX0BGD0E4WWLQMyh+g260LrE12az+mPvuKE77PJPArTT8IuWhD7hAqkaQByptioeFNWCByGk2y3SO6XyBBFIlPrnLG7y7gkowBq3eDz1vHCXlZr3CoWIA5sr0vbBTz4NR2QBc60vTCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0Lwc9v2",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAlOsjJukg53W2a4ObK1374kNmQ8zg/Ryd7b7bX0BGD0E4WWLQMyh+g260LrE12az+mPvuKE77PJPArTT8IuWhD7hAqkaQByptioeFNWCByGk2y3SO6XyBBFIlPrnLG7y7gkowBq3eDz1vHCXlZr3CoWIA5sr0vbBTz4NR2QBc60vTCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0Lwc9v2",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAlOsjJukg53W2a4ObK1374kNmQ8zg/Ryd7b7bX0BGD0E4WWLQMyh+g260LrE12az+mPvuKE77PJPArTT8IuWhD7hAqkaQByptioeFNWCByGk2y3SO6XyBBFIlPrnLG7y7gkowBq3eDz1vHCXlZr3CoWIA5sr0vbBTz4NR2QBc60vTCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0Lwc9v2",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "message": {
        "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "message": {
        "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
  "id": -576460752303422615,
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
  "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
  "id": -576460752303422615,
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "state": "tx_+QENCwH4hLhAlOsjJukg53W2a4ObK1374kNmQ8zg/Ryd7b7bX0BGD0E4WWLQMyh+g260LrE12az+mPvuKE77PJPArTT8IuWhD7hAqkaQByptioeFNWCByGk2y3SO6XyBBFIlPrnLG7y7gkowBq3eDz1vHCXlZr3CoWIA5sr0vbBTz4NR2QBc60vTCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0Lwc9v2"
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "state": "tx_+QENCwH4hLhAlOsjJukg53W2a4ObK1374kNmQ8zg/Ryd7b7bX0BGD0E4WWLQMyh+g260LrE12az+mPvuKE77PJPArTT8IuWhD7hAqkaQByptioeFNWCByGk2y3SO6XyBBFIlPrnLG7y7gkowBq3eDz1vHCXlZr3CoWIA5sr0vbBTz4NR2QBc60vTCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0Lwc9v2"
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
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBkMgAeGdEOvtRKC377n92tfPwqaHtC0wuVmUJ0eaFFzzoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGcEiGGw8/Q66Bb/0=",
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
    "signed_tx": "tx_+QHrCwH4QrhA+hKpH+QmnTq2u8hSKaTqo2tvVxlNBhOEctr504w4hy8HrisSYKBBsZgl+gjO003l5jr4nU7W8/UzQdQeBETbA7kBovkBnzYBoQZDIAHhnRDr7USgt++5/drXz8Kmh7QtMLlZlCdHmhRc86EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhnBIhhsPP0O4AkwT"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA+hKpH+QmnTq2u8hSKaTqo2tvVxlNBhOEctr504w4hy8HrisSYKBBsZgl+gjO003l5jr4nU7W8/UzQdQeBETbA7kBovkBnzYBoQZDIAHhnRDr7USgt++5/drXz8Kmh7QtMLlZlCdHmhRc86EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhnBIhhsPP0O4AkwT",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA+hKpH+QmnTq2u8hSKaTqo2tvVxlNBhOEctr504w4hy8HrisSYKBBsZgl+gjO003l5jr4nU7W8/UzQdQeBETbA7kBovkBnzYBoQZDIAHhnRDr7USgt++5/drXz8Kmh7QtMLlZlCdHmhRc86EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhnBIhhsPP0O4AkwT",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBkMgAeGdEOvtRKC377n92tfPwqaHtC0wuVmUJ0eaFFzzoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAAaoP2cKg==",
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
    "signed_tx": "tx_+KcLAfhCuEBabtDWmCoh6GX7qhfbNKyD/RE7JczAGgQ0MQP4K5w9/gJoGX2ZvVvJ/o3Mq5HuLH67A9Z/vRLwW5K99+Kiu+wLuF/4XTgBoQZDIAHhnRDr7USgt++5/drXz8Kmh7QtMLlZlCdHmhRc86EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAGuv83lo="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBabtDWmCoh6GX7qhfbNKyD/RE7JczAGgQ0MQP4K5w9/gJoGX2ZvVvJ/o3Mq5HuLH67A9Z/vRLwW5K99+Kiu+wLuF/4XTgBoQZDIAHhnRDr7USgt++5/drXz8Kmh7QtMLlZlCdHmhRc86EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAGuv83lo=",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBabtDWmCoh6GX7qhfbNKyD/RE7JczAGgQ0MQP4K5w9/gJoGX2ZvVvJ/o3Mq5HuLH67A9Z/vRLwW5K99+Kiu+wLuF/4XTgBoQZDIAHhnRDr7USgt++5/drXz8Kmh7QtMLlZlCdHmhRc86EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAGuv83lo=",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
    "channel_id": "ch_WZctXs9UTWnvgdcQqACcSWkgqVEFPJxMs8bNMuJQCihn6JW4B",
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
      "fsm_id": "ba_0y7R0HebBQVDfT+ZCLOIKH5q9H62DSyZXezwexhOlAEFixVe"
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
      "fsm_id": "ba_43dMp35ikVdF15sF8QCpBy/LuA5Q/QVqRHonIS9N9sqDuyDg"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtEs2Z1cA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422614,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBVp9XbimHrMpAgmeOOYyR6rWr72U7vMoiVSTz0qB39b6spZSLClpLOSI0xLYTlC8OOX3fLr/5fiy4xRcY4JlwLuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LRHnqa60="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422614,
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "fsm_id": "ba_43dMp35ikVdF15sF8QCpBy/LuA5Q/QVqRHonIS9N9sqDuyDg",
      "signed_tx": "tx_+MsLAfhCuEBVp9XbimHrMpAgmeOOYyR6rWr72U7vMoiVSTz0qB39b6spZSLClpLOSI0xLYTlC8OOX3fLr/5fiy4xRcY4JlwLuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LRHnqa60=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422613,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAVafV24ph6zKQIJnjjmMkeq1q+9lO7zKIlUk89Kgd/W+rKWUiwpaSzkiNMS2E5QvDjl93y6/+X4suMUXGOCZcC7hAxIlU2ym3AXlCueGuAA7nnAX9U2DtT7EDiYC2bbNq+YUqk9T4WwYLPE5ji4/s6XMAxPeoC16eZvWMr0/4kmlOCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0TNVfNK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
  "id": -576460752303422613,
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAVafV24ph6zKQIJnjjmMkeq1q+9lO7zKIlUk89Kgd/W+rKWUiwpaSzkiNMS2E5QvDjl93y6/+X4suMUXGOCZcC7hAxIlU2ym3AXlCueGuAA7nnAX9U2DtT7EDiYC2bbNq+YUqk9T4WwYLPE5ji4/s6XMAxPeoC16eZvWMr0/4kmlOCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0TNVfNK",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_0y7R0HebBQVDfT+ZCLOIKH5q9H62DSyZXezwexhOlAEFixVe"
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAVafV24ph6zKQIJnjjmMkeq1q+9lO7zKIlUk89Kgd/W+rKWUiwpaSzkiNMS2E5QvDjl93y6/+X4suMUXGOCZcC7hAxIlU2ym3AXlCueGuAA7nnAX9U2DtT7EDiYC2bbNq+YUqk9T4WwYLPE5ji4/s6XMAxPeoC16eZvWMr0/4kmlOCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0TNVfNK",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAVafV24ph6zKQIJnjjmMkeq1q+9lO7zKIlUk89Kgd/W+rKWUiwpaSzkiNMS2E5QvDjl93y6/+X4suMUXGOCZcC7hAxIlU2ym3AXlCueGuAA7nnAX9U2DtT7EDiYC2bbNq+YUqk9T4WwYLPE5ji4/s6XMAxPeoC16eZvWMr0/4kmlOCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0TNVfNK",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAVafV24ph6zKQIJnjjmMkeq1q+9lO7zKIlUk89Kgd/W+rKWUiwpaSzkiNMS2E5QvDjl93y6/+X4suMUXGOCZcC7hAxIlU2ym3AXlCueGuAA7nnAX9U2DtT7EDiYC2bbNq+YUqk9T4WwYLPE5ji4/s6XMAxPeoC16eZvWMr0/4kmlOCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0TNVfNK",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "message": {
        "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "message": {
        "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
  "id": -576460752303422612,
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
  "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
  "id": -576460752303422612,
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "state": "tx_+QENCwH4hLhAVafV24ph6zKQIJnjjmMkeq1q+9lO7zKIlUk89Kgd/W+rKWUiwpaSzkiNMS2E5QvDjl93y6/+X4suMUXGOCZcC7hAxIlU2ym3AXlCueGuAA7nnAX9U2DtT7EDiYC2bbNq+YUqk9T4WwYLPE5ji4/s6XMAxPeoC16eZvWMr0/4kmlOCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0TNVfNK"
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "state": "tx_+QENCwH4hLhAVafV24ph6zKQIJnjjmMkeq1q+9lO7zKIlUk89Kgd/W+rKWUiwpaSzkiNMS2E5QvDjl93y6/+X4suMUXGOCZcC7hAxIlU2ym3AXlCueGuAA7nnAX9U2DtT7EDiYC2bbNq+YUqk9T4WwYLPE5ji4/s6XMAxPeoC16eZvWMr0/4kmlOCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0TNVfNK"
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
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBj5oNAzaXvfjj1VXXlWP6tuwZknD/MNyQ+3ypDN22L/EoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGcEiGGw8/G8GCBe8=",
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
    "signed_tx": "tx_+QHrCwH4QrhAyMkS5gG2qDK0UYX+4pYtoJ3Aucbg681Hf7heV7Iu7EzGyPXObbsgFqMuAEHz/oil0uLDufiYsmAUlNwYTBujD7kBovkBnzYBoQY+aDQM2l73449VV15Vj+rbsGZJw/zDckPt8qQzdti/xKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhnBIhhsPPxuIy5qQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAyMkS5gG2qDK0UYX+4pYtoJ3Aucbg681Hf7heV7Iu7EzGyPXObbsgFqMuAEHz/oil0uLDufiYsmAUlNwYTBujD7kBovkBnzYBoQY+aDQM2l73449VV15Vj+rbsGZJw/zDckPt8qQzdti/xKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhnBIhhsPPxuIy5qQ",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAyMkS5gG2qDK0UYX+4pYtoJ3Aucbg681Hf7heV7Iu7EzGyPXObbsgFqMuAEHz/oil0uLDufiYsmAUlNwYTBujD7kBovkBnzYBoQY+aDQM2l73449VV15Vj+rbsGZJw/zDckPt8qQzdti/xKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhnBIhhsPPxuIy5qQ",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBj5oNAzaXvfjj1VXXlWP6tuwZknD/MNyQ+3ypDN22L/EoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KAAc+WAyWQ==",
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
    "signed_tx": "tx_+KcLAfhCuEC9zJx10IYWOrV68knJTtY8WqbGcuPrJkMZyAEPQVr0rZxRlBPXzKTmRlLZNrCYj+aXim1JRw2mv9y0knw3DD4CuF/4XTgBoQY+aDQM2l73449VV15Vj+rbsGZJw/zDckPt8qQzdti/xKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAHLtpoOQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC9zJx10IYWOrV68knJTtY8WqbGcuPrJkMZyAEPQVr0rZxRlBPXzKTmRlLZNrCYj+aXim1JRw2mv9y0knw3DD4CuF/4XTgBoQY+aDQM2l73449VV15Vj+rbsGZJw/zDckPt8qQzdti/xKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAHLtpoOQ=",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC9zJx10IYWOrV68knJTtY8WqbGcuPrJkMZyAEPQVr0rZxRlBPXzKTmRlLZNrCYj+aXim1JRw2mv9y0knw3DD4CuF/4XTgBoQY+aDQM2l73449VV15Vj+rbsGZJw/zDckPt8qQzdti/xKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17WfygAHLtpoOQ=",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
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
    "channel_id": "ch_UV73UrZZGsEQQ9c1J1cYi1YJLsf4VRJHg4mv7h1obEhCuqUUY",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
