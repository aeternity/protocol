
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
      "fsm_id": "ba_S6Vcgs1iHBIjm69E8ghEQV0F/cWWxVb3MTnqE5Ceb/uUj3Hi"
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
      "fsm_id": "ba_IaK9fcR0TB3RavbADoELQi4L0zyBBzDLzqBcOx64Vyrfi1An"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgs/5EXb+A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422656,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDNwPg2EpIYVU8Iqf3z0bWzIjOi9KXCssiI0EFcgw2xx1T0HaqwREpY7QCbl/S/luC8hVDebv52TXBBLjcc8GUPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LP1V38l8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422656,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "fsm_id": "ba_IaK9fcR0TB3RavbADoELQi4L0zyBBzDLzqBcOx64Vyrfi1An",
      "signed_tx": "tx_+MsLAfhCuEDNwPg2EpIYVU8Iqf3z0bWzIjOi9KXCssiI0EFcgw2xx1T0HaqwREpY7QCbl/S/luC8hVDebv52TXBBLjcc8GUPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LP1V38l8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422655,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAjgmjzAehjM/ULFqWcaywbne7tp0+BU1UeP1e2Oa2hnFw1HyKwRHv8M9UaiEpCAI4l44ibVF6eUhD8yK0NodpCLhAzcD4NhKSGFVPCKn989G1syIzovSlwrLIiNBBXIMNscdU9B2qsERKWO0Am5f0v5bgvIVQ3m7+dk1wQS43HPBlD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCz+WrxG7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422655,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAjgmjzAehjM/ULFqWcaywbne7tp0+BU1UeP1e2Oa2hnFw1HyKwRHv8M9UaiEpCAI4l44ibVF6eUhD8yK0NodpCLhAzcD4NhKSGFVPCKn989G1syIzovSlwrLIiNBBXIMNscdU9B2qsERKWO0Am5f0v5bgvIVQ3m7+dk1wQS43HPBlD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCz+WrxG7",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_S6Vcgs1iHBIjm69E8ghEQV0F/cWWxVb3MTnqE5Ceb/uUj3Hi"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAjgmjzAehjM/ULFqWcaywbne7tp0+BU1UeP1e2Oa2hnFw1HyKwRHv8M9UaiEpCAI4l44ibVF6eUhD8yK0NodpCLhAzcD4NhKSGFVPCKn989G1syIzovSlwrLIiNBBXIMNscdU9B2qsERKWO0Am5f0v5bgvIVQ3m7+dk1wQS43HPBlD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCz+WrxG7",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAjgmjzAehjM/ULFqWcaywbne7tp0+BU1UeP1e2Oa2hnFw1HyKwRHv8M9UaiEpCAI4l44ibVF6eUhD8yK0NodpCLhAzcD4NhKSGFVPCKn989G1syIzovSlwrLIiNBBXIMNscdU9B2qsERKWO0Am5f0v5bgvIVQ3m7+dk1wQS43HPBlD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCz+WrxG7",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAjgmjzAehjM/ULFqWcaywbne7tp0+BU1UeP1e2Oa2hnFw1HyKwRHv8M9UaiEpCAI4l44ibVF6eUhD8yK0NodpCLhAzcD4NhKSGFVPCKn989G1syIzovSlwrLIiNBBXIMNscdU9B2qsERKWO0Am5f0v5bgvIVQ3m7+dk1wQS43HPBlD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCz+WrxG7",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "message": {
        "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "message": {
        "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
  "id": -576460752303422654,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422654,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+QENCwH4hLhAjgmjzAehjM/ULFqWcaywbne7tp0+BU1UeP1e2Oa2hnFw1HyKwRHv8M9UaiEpCAI4l44ibVF6eUhD8yK0NodpCLhAzcD4NhKSGFVPCKn989G1syIzovSlwrLIiNBBXIMNscdU9B2qsERKWO0Am5f0v5bgvIVQ3m7+dk1wQS43HPBlD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCz+WrxG7"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+QENCwH4hLhAjgmjzAehjM/ULFqWcaywbne7tp0+BU1UeP1e2Oa2hnFw1HyKwRHv8M9UaiEpCAI4l44ibVF6eUhD8yK0NodpCLhAzcD4NhKSGFVPCKn989G1syIzovSlwrLIiNBBXIMNscdU9B2qsERKWO0Am5f0v5bgvIVQ3m7+dk1wQS43HPBlD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCz+WrxG7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422653,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422653,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QENCwH4hLhAjgmjzAehjM/ULFqWcaywbne7tp0+BU1UeP1e2Oa2hnFw1HyKwRHv8M9UaiEpCAI4l44ibVF6eUhD8yK0NodpCLhAzcD4NhKSGFVPCKn989G1syIzovSlwrLIiNBBXIMNscdU9B2qsERKWO0Am5f0v5bgvIVQ3m7+dk1wQS43HPBlD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCz+WrxG7",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422652,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422652,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwbskMm+MC+GX/ajg6fuikM4mlio6OCLDdQKql0TvwRAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAlU/zBo=",
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
  "id": -576460752303422651,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA9CyX7FoIQ99ROrs1vC1UbO3bIFEX4Vn9duvSdZI9aZ2cBml+yodc3j7rxLVVZBU7j6B9mZQOiXwAjIDksOr0EuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ9rzob"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422651,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA9CyX7FoIQ99ROrs1vC1UbO3bIFEX4Vn9duvSdZI9aZ2cBml+yodc3j7rxLVVZBU7j6B9mZQOiXwAjIDksOr0EuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJ9rzob",
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
  "id": -576460752303422650,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA9CyX7FoIQ99ROrs1vC1UbO3bIFEX4Vn9duvSdZI9aZ2cBml+yodc3j7rxLVVZBU7j6B9mZQOiXwAjIDksOr0EuECPvNb4rgVCYvNALCfhWfDmKG8OT4A4D6BRnnQdyGSEbNpE9U5nDAmLngaZfDoqjM7qg6lzyF9nyRkGHanug1AGuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK++Lor"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422650,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuEA9CyX7FoIQ99ROrs1vC1UbO3bIFEX4Vn9duvSdZI9aZ2cBml+yodc3j7rxLVVZBU7j6B9mZQOiXwAjIDksOr0EuECPvNb4rgVCYvNALCfhWfDmKG8OT4A4D6BRnnQdyGSEbNpE9U5nDAmLngaZfDoqjM7qg6lzyF9nyRkGHanug1AGuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK++Lor"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuEA9CyX7FoIQ99ROrs1vC1UbO3bIFEX4Vn9duvSdZI9aZ2cBml+yodc3j7rxLVVZBU7j6B9mZQOiXwAjIDksOr0EuECPvNb4rgVCYvNALCfhWfDmKG8OT4A4D6BRnnQdyGSEbNpE9U5nDAmLngaZfDoqjM7qg6lzyF9nyRkGHanug1AGuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK++Lor"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422649,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422649,
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
  "id": -576460752303422648,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422648,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA9CyX7FoIQ99ROrs1vC1UbO3bIFEX4Vn9duvSdZI9aZ2cBml+yodc3j7rxLVVZBU7j6B9mZQOiXwAjIDksOr0EuECPvNb4rgVCYvNALCfhWfDmKG8OT4A4D6BRnnQdyGSEbNpE9U5nDAmLngaZfDoqjM7qg6lzyF9nyRkGHanug1AGuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK++Lor",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422647,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422647,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBvwbskMm+MC+GX/ajg6fuikM4mlio6OCLDdQKql0TvwRoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEA9CyX7FoIQ99ROrs1vC1UbO3bIFEX4Vn9duvSdZI9aZ2cBml+yodc3j7rxLVVZBU7j6B9mZQOiXwAjIDksOr0EuECPvNb4rgVCYvNALCfhWfDmKG8OT4A4D6BRnnQdyGSEbNpE9U5nDAmLngaZfDoqjM7qg6lzyF9nyRkGHanug1AGuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIAhnBIhhsPP0DJglyf",
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
    "signed_tx": "tx_+QFxCwH4QrhA0OL4/71nXGpbCsWNITJhc1t8FP2oMEbDjzccShlYhTcLGcsAGag9CegN8XP9xPDcfxY/Z8JQ1AEDKs5PJeszBrkBKPkBJTsBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAPQsl+xaCEPfUTq7NbwtVGzt2yBRF+FZ/Xbr0nWSPWmdnAZpfsqHXN4+68S1VWQVO4+gfZmUDol8AIyA5LDq9BLhAj7zW+K4FQmLzQCwn4Vnw5ihvDk+AOA+gUZ50HchkhGzaRPVOZwwJi54GmXw6KozO6oOpc8hfZ8kZBh2p7oNQBrhI+EY5AqEG/BuyQyb4wL4Zf9qODp+6KQziaWKjo4IsN1AqqXRO/BECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIZwSIYbDz9AdKtv1w=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422646,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422646,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwbskMm+MC+GX/ajg6fuikM4mlio6OCLDdQKql0TvwRA6Ah5YXSCzjC3C5f2KaHrz5Qp6zPFnxOBCDOm/SZojmZpc5bAP4=",
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
  "id": -576460752303422645,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDYBIGOBZpBTKDhWStEoV2/XMVaPSeK1pOqkh6hWckCQvPKTtjPlHIypY983Rp/guAYMec1xOCmtfdIZzjUqysMuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maVO9sdO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422645,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDYBIGOBZpBTKDhWStEoV2/XMVaPSeK1pOqkh6hWckCQvPKTtjPlHIypY983Rp/guAYMec1xOCmtfdIZzjUqysMuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maVO9sdO",
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
  "id": -576460752303422644,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECZ+MdxXlbd8sZ6xdWudz/JjoKn8kvwZkOYc0f6uFWIavc62lD+oBRt/JJ+7wYLIhQItmbE45qFxLXBqi0IzRcEuEDYBIGOBZpBTKDhWStEoV2/XMVaPSeK1pOqkh6hWckCQvPKTtjPlHIypY983Rp/guAYMec1xOCmtfdIZzjUqysMuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maV5SXH1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422644,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuECZ+MdxXlbd8sZ6xdWudz/JjoKn8kvwZkOYc0f6uFWIavc62lD+oBRt/JJ+7wYLIhQItmbE45qFxLXBqi0IzRcEuEDYBIGOBZpBTKDhWStEoV2/XMVaPSeK1pOqkh6hWckCQvPKTtjPlHIypY983Rp/guAYMec1xOCmtfdIZzjUqysMuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maV5SXH1"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuECZ+MdxXlbd8sZ6xdWudz/JjoKn8kvwZkOYc0f6uFWIavc62lD+oBRt/JJ+7wYLIhQItmbE45qFxLXBqi0IzRcEuEDYBIGOBZpBTKDhWStEoV2/XMVaPSeK1pOqkh6hWckCQvPKTtjPlHIypY983Rp/guAYMec1xOCmtfdIZzjUqysMuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maV5SXH1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422643,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422643,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999997
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000003
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422642,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422642,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECZ+MdxXlbd8sZ6xdWudz/JjoKn8kvwZkOYc0f6uFWIavc62lD+oBRt/JJ+7wYLIhQItmbE45qFxLXBqi0IzRcEuEDYBIGOBZpBTKDhWStEoV2/XMVaPSeK1pOqkh6hWckCQvPKTtjPlHIypY983Rp/guAYMec1xOCmtfdIZzjUqysMuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQOgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maV5SXH1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/bDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAP0OPKg"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422641,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422641,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000003
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999997
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwbskMm+MC+GX/ajg6fuikM4mlio6OCLDdQKql0TvwRBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAq66aDQ=",
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
  "id": -576460752303422640,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAYFLp++WmCPjPmvTTB5JqqiL5GA/iS8shdGQYNe15FglYrKqOX+W+LIzgYlmGAZ1vu/SdJnlBALBMQE9DOOzIKuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL8AK9z"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422640,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAYFLp++WmCPjPmvTTB5JqqiL5GA/iS8shdGQYNe15FglYrKqOX+W+LIzgYlmGAZ1vu/SdJnlBALBMQE9DOOzIKuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL8AK9z",
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
  "id": -576460752303422639,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAYFLp++WmCPjPmvTTB5JqqiL5GA/iS8shdGQYNe15FglYrKqOX+W+LIzgYlmGAZ1vu/SdJnlBALBMQE9DOOzIKuEDu9OG67FUYeH0Dh1taJ9+9IhYIZawfYv5XLapalzuVJcTsM8Gf7Jv9171YNoOT4BPs5R33LLiS6Y37c3LDR1IAuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKoElki"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422639,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuEAYFLp++WmCPjPmvTTB5JqqiL5GA/iS8shdGQYNe15FglYrKqOX+W+LIzgYlmGAZ1vu/SdJnlBALBMQE9DOOzIKuEDu9OG67FUYeH0Dh1taJ9+9IhYIZawfYv5XLapalzuVJcTsM8Gf7Jv9171YNoOT4BPs5R33LLiS6Y37c3LDR1IAuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKoElki"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuEAYFLp++WmCPjPmvTTB5JqqiL5GA/iS8shdGQYNe15FglYrKqOX+W+LIzgYlmGAZ1vu/SdJnlBALBMQE9DOOzIKuEDu9OG67FUYeH0Dh1taJ9+9IhYIZawfYv5XLapalzuVJcTsM8Gf7Jv9171YNoOT4BPs5R33LLiS6Y37c3LDR1IAuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKoElki"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422638,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422638,
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

#### initiator ---> node
```javascript
{
  "id": -576460752303422637,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422637,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAYFLp++WmCPjPmvTTB5JqqiL5GA/iS8shdGQYNe15FglYrKqOX+W+LIzgYlmGAZ1vu/SdJnlBALBMQE9DOOzIKuEDu9OG67FUYeH0Dh1taJ9+9IhYIZawfYv5XLapalzuVJcTsM8Gf7Jv9171YNoOT4BPs5R33LLiS6Y37c3LDR1IAuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKoElki",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA0OL4/71nXGpbCsWNITJhc1t8FP2oMEbDjzccShlYhTcLGcsAGag9CegN8XP9xPDcfxY/Z8JQ1AEDKs5PJeszBrkBKPkBJTsBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAPQsl+xaCEPfUTq7NbwtVGzt2yBRF+FZ/Xbr0nWSPWmdnAZpfsqHXN4+68S1VWQVO4+gfZmUDol8AIyA5LDq9BLhAj7zW+K4FQmLzQCwn4Vnw5ihvDk+AOA+gUZ50HchkhGzaRPVOZwwJi54GmXw6KozO6oOpc8hfZ8kZBh2p7oNQBrhI+EY5AqEG/BuyQyb4wL4Zf9qODp+6KQziaWKjo4IsN1AqqXRO/BECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIZwSIYbDz9AdKtv1w==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA0OL4/71nXGpbCsWNITJhc1t8FP2oMEbDjzccShlYhTcLGcsAGag9CegN8XP9xPDcfxY/Z8JQ1AEDKs5PJeszBrkBKPkBJTsBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAPQsl+xaCEPfUTq7NbwtVGzt2yBRF+FZ/Xbr0nWSPWmdnAZpfsqHXN4+68S1VWQVO4+gfZmUDol8AIyA5LDq9BLhAj7zW+K4FQmLzQCwn4Vnw5ihvDk+AOA+gUZ50HchkhGzaRPVOZwwJi54GmXw6KozO6oOpc8hfZ8kZBh2p7oNQBrhI+EY5AqEG/BuyQyb4wL4Zf9qODp+6KQziaWKjo4IsN1AqqXRO/BECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CAIZwSIYbDz9AdKtv1w==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "횎���\u0016���Jl��'>i�5�S@I�o��B��",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422636,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422636,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAYFLp++WmCPjPmvTTB5JqqiL5GA/iS8shdGQYNe15FglYrKqOX+W+LIzgYlmGAZ1vu/SdJnlBALBMQE9DOOzIKuEDu9OG67FUYeH0Dh1taJ9+9IhYIZawfYv5XLapalzuVJcTsM8Gf7Jv9171YNoOT4BPs5R33LLiS6Y37c3LDR1IAuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKoElki",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422635,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422635,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwbskMm+MC+GX/ajg6fuikM4mlio6OCLDdQKql0TvwRBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC1LyzzU=",
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
  "id": -576460752303422634,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBopCceORrevfhC/nEtPoLrwUV/MY/ALaiTfuNr5aXPaM9UFg100TS9+sdq4FP6rSWGtfdWE4FBkNUHHC5ddKcFuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsViH+s"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422634,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBopCceORrevfhC/nEtPoLrwUV/MY/ALaiTfuNr5aXPaM9UFg100TS9+sdq4FP6rSWGtfdWE4FBkNUHHC5ddKcFuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsViH+s",
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
  "id": -576460752303422633,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBopCceORrevfhC/nEtPoLrwUV/MY/ALaiTfuNr5aXPaM9UFg100TS9+sdq4FP6rSWGtfdWE4FBkNUHHC5ddKcFuECrU7Q8Nd/FAeKeZAtAXyJPccLdcExt3AoU6TdKtzUOYthVq3I+u75Ijy2PIi0Ugdkrek6MglSvBNPxAgYRzGIEuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu/k4UA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422633,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuEBopCceORrevfhC/nEtPoLrwUV/MY/ALaiTfuNr5aXPaM9UFg100TS9+sdq4FP6rSWGtfdWE4FBkNUHHC5ddKcFuECrU7Q8Nd/FAeKeZAtAXyJPccLdcExt3AoU6TdKtzUOYthVq3I+u75Ijy2PIi0Ugdkrek6MglSvBNPxAgYRzGIEuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu/k4UA"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuEBopCceORrevfhC/nEtPoLrwUV/MY/ALaiTfuNr5aXPaM9UFg100TS9+sdq4FP6rSWGtfdWE4FBkNUHHC5ddKcFuECrU7Q8Nd/FAeKeZAtAXyJPccLdcExt3AoU6TdKtzUOYthVq3I+u75Ijy2PIi0Ugdkrek6MglSvBNPxAgYRzGIEuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu/k4UA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422632,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422632,
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
  "id": -576460752303422631,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422631,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBopCceORrevfhC/nEtPoLrwUV/MY/ALaiTfuNr5aXPaM9UFg100TS9+sdq4FP6rSWGtfdWE4FBkNUHHC5ddKcFuECrU7Q8Nd/FAeKeZAtAXyJPccLdcExt3AoU6TdKtzUOYthVq3I+u75Ijy2PIi0Ugdkrek6MglSvBNPxAgYRzGIEuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgu/k4UA",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422630,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422630,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBvwbskMm+MC+GX/ajg6fuikM4mlio6OCLDdQKql0TvwRoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEBopCceORrevfhC/nEtPoLrwUV/MY/ALaiTfuNr5aXPaM9UFg100TS9+sdq4FP6rSWGtfdWE4FBkNUHHC5ddKcFuECrU7Q8Nd/FAeKeZAtAXyJPccLdcExt3AoU6TdKtzUOYthVq3I+u75Ijy2PIi0Ugdkrek6MglSvBNPxAgYRzGIEuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhnBIhhsPPxlZzbV3",
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
    "signed_tx": "tx_+QFxCwH4QrhAOBc2aqN7SxoiYZ37n5y61+0aO02dK92+BFGOHCM7QFmpdgBNEMiqSL8W6OszjN2QDTAJuBZggMjCL8e+ZVrEA7kBKPkBJTsBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAaKQnHjka3r34Qv5xLT6C68FFfzGPwC2ok37ja+Wlz2jPVBYNdNE0vfrHauBT+q0lhrX3VhOBQZDVBxwuXXSnBbhAq1O0PDXfxQHinmQLQF8iT3HC3XBMbdwKFOk3Src1DmLYVatyPru+SI8tjyItFIHZK3pOjIJUrwTT8QIGEcxiBLhI+EY5AqEG/BuyQyb4wL4Zf9qODp+6KQziaWKjo4IsN1AqqXRO/BEFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIZwSIYbDz8ZdMGROg=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422629,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422629,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwbskMm+MC+GX/ajg6fuikM4mlio6OCLDdQKql0TvwRBqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAiG+j88=",
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
  "id": -576460752303422628,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDTafo2kLrP8R49jMXLJK2UQS+1S10WJMkZITvqD9tIY4EX++K/BoSuNFcbIVUq5xXQJJbFrsM5pdkvzoZsnhEKuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL/W8NA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422628,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDTafo2kLrP8R49jMXLJK2UQS+1S10WJMkZITvqD9tIY4EX++K/BoSuNFcbIVUq5xXQJJbFrsM5pdkvzoZsnhEKuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL/W8NA",
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
  "id": -576460752303422627,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC7zUo7gdMbBNsNn+DcbaeKJv/OEVLjb+6Ry8WmyBliVyvFPy8wrI2VZX789YwykJYaD+IXUYqEf3n3q6GQxdQLuEDTafo2kLrP8R49jMXLJK2UQS+1S10WJMkZITvqD9tIY4EX++K/BoSuNFcbIVUq5xXQJJbFrsM5pdkvzoZsnhEKuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIPMkE+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422627,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuEC7zUo7gdMbBNsNn+DcbaeKJv/OEVLjb+6Ry8WmyBliVyvFPy8wrI2VZX789YwykJYaD+IXUYqEf3n3q6GQxdQLuEDTafo2kLrP8R49jMXLJK2UQS+1S10WJMkZITvqD9tIY4EX++K/BoSuNFcbIVUq5xXQJJbFrsM5pdkvzoZsnhEKuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIPMkE+"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuEC7zUo7gdMbBNsNn+DcbaeKJv/OEVLjb+6Ry8WmyBliVyvFPy8wrI2VZX789YwykJYaD+IXUYqEf3n3q6GQxdQLuEDTafo2kLrP8R49jMXLJK2UQS+1S10WJMkZITvqD9tIY4EX++K/BoSuNFcbIVUq5xXQJJbFrsM5pdkvzoZsnhEKuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIPMkE+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422626,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422626,
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
  "id": -576460752303422625,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422625,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC7zUo7gdMbBNsNn+DcbaeKJv/OEVLjb+6Ry8WmyBliVyvFPy8wrI2VZX789YwykJYaD+IXUYqEf3n3q6GQxdQLuEDTafo2kLrP8R49jMXLJK2UQS+1S10WJMkZITvqD9tIY4EX++K/BoSuNFcbIVUq5xXQJJbFrsM5pdkvzoZsnhEKuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQagjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIPMkE+",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422624,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422624,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwbskMm+MC+GX/ajg6fuikM4mlio6OCLDdQKql0TvwRB6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC85KFl8=",
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
  "id": -576460752303422623,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDTOakodjP4fYQx8j3i5gBsgeJg6BUsXFpwn2NKtj/uMGIoNBpHk+5dvf2i+dt+2/S3CPYF5yAiy4L92iE821oDuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguCgN+0"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422623,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDTOakodjP4fYQx8j3i5gBsgeJg6BUsXFpwn2NKtj/uMGIoNBpHk+5dvf2i+dt+2/S3CPYF5yAiy4L92iE821oDuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguCgN+0",
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
  "id": -576460752303422622,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECEybeBbh0xXUELhrJd5lWhDmyR/B/q1H/z+aockI8nTQm4QZn+QNHA0Yt9C6WArZpqOxWDWgeT5LgS2G09a4kKuEDTOakodjP4fYQx8j3i5gBsgeJg6BUsXFpwn2NKtj/uMGIoNBpHk+5dvf2i+dt+2/S3CPYF5yAiy4L92iE821oDuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsln7eS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422622,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuECEybeBbh0xXUELhrJd5lWhDmyR/B/q1H/z+aockI8nTQm4QZn+QNHA0Yt9C6WArZpqOxWDWgeT5LgS2G09a4kKuEDTOakodjP4fYQx8j3i5gBsgeJg6BUsXFpwn2NKtj/uMGIoNBpHk+5dvf2i+dt+2/S3CPYF5yAiy4L92iE821oDuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsln7eS"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "state": "tx_+NILAfiEuECEybeBbh0xXUELhrJd5lWhDmyR/B/q1H/z+aockI8nTQm4QZn+QNHA0Yt9C6WArZpqOxWDWgeT5LgS2G09a4kKuEDTOakodjP4fYQx8j3i5gBsgeJg6BUsXFpwn2NKtj/uMGIoNBpHk+5dvf2i+dt+2/S3CPYF5yAiy4L92iE821oDuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsln7eS"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422621,
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
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422621,
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
  "id": -576460752303422620,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422620,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECEybeBbh0xXUELhrJd5lWhDmyR/B/q1H/z+aockI8nTQm4QZn+QNHA0Yt9C6WArZpqOxWDWgeT5LgS2G09a4kKuEDTOakodjP4fYQx8j3i5gBsgeJg6BUsXFpwn2NKtj/uMGIoNBpHk+5dvf2i+dt+2/S3CPYF5yAiy4L92iE821oDuEj4RjkCoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EQegJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsln7eS",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAOBc2aqN7SxoiYZ37n5y61+0aO02dK92+BFGOHCM7QFmpdgBNEMiqSL8W6OszjN2QDTAJuBZggMjCL8e+ZVrEA7kBKPkBJTsBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAaKQnHjka3r34Qv5xLT6C68FFfzGPwC2ok37ja+Wlz2jPVBYNdNE0vfrHauBT+q0lhrX3VhOBQZDVBxwuXXSnBbhAq1O0PDXfxQHinmQLQF8iT3HC3XBMbdwKFOk3Src1DmLYVatyPru+SI8tjyItFIHZK3pOjIJUrwTT8QIGEcxiBLhI+EY5AqEG/BuyQyb4wL4Zf9qODp+6KQziaWKjo4IsN1AqqXRO/BEFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIZwSIYbDz8ZdMGROg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAOBc2aqN7SxoiYZ37n5y61+0aO02dK92+BFGOHCM7QFmpdgBNEMiqSL8W6OszjN2QDTAJuBZggMjCL8e+ZVrEA7kBKPkBJTsBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAaKQnHjka3r34Qv5xLT6C68FFfzGPwC2ok37ja+Wlz2jPVBYNdNE0vfrHauBT+q0lhrX3VhOBQZDVBxwuXXSnBbhAq1O0PDXfxQHinmQLQF8iT3HC3XBMbdwKFOk3Src1DmLYVatyPru+SI8tjyItFIHZK3pOjIJUrwTT8QIGEcxiBLhI+EY5AqEG/BuyQyb4wL4Zf9qODp+6KQziaWKjo4IsN1AqqXRO/BEFoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAIZwSIYbDz8ZdMGROg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "�\u0012\u001e��o\nQ��W��\u0017�\u001e׋����7��sP�νo�",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBvwbskMm+MC+GX/ajg6fuikM4mlio6OCLDdQKql0TvwRoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/+GHLHOiuwBAIYPXtZ/KABBgiGdIA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422619,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECp4nX0+C2boWzjXwKNiExeDKXl/wqwmxtDUCTwb4h8lB3zf7n88IQfnkN/Vk+OyZM5hAJmG2/ke2Yn4fN+2dgKuF/4XTUBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAQQBzja0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422619,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECp4nX0+C2boWzjXwKNiExeDKXl/wqwmxtDUCTwb4h8lB3zf7n88IQfnkN/Vk+OyZM5hAJmG2/ke2Yn4fN+2dgKuF/4XTUBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAQQBzja0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422618,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBgbizpy8hR1ycUt9DjRntq2b16WZC+3yLR7PTKr3U+4kUdVo9GV3a02Jes8ALtvKMZaG6HWYF9lOilX5S+3lAIuECp4nX0+C2boWzjXwKNiExeDKXl/wqwmxtDUCTwb4h8lB3zf7n88IQfnkN/Vk+OyZM5hAJmG2/ke2Yn4fN+2dgKuF/4XTUBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAQT+4jyg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
  "id": -576460752303422618,
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBgbizpy8hR1ycUt9DjRntq2b16WZC+3yLR7PTKr3U+4kUdVo9GV3a02Jes8ALtvKMZaG6HWYF9lOilX5S+3lAIuECp4nX0+C2boWzjXwKNiExeDKXl/wqwmxtDUCTwb4h8lB3zf7n88IQfnkN/Vk+OyZM5hAJmG2/ke2Yn4fN+2dgKuF/4XTUBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAQT+4jyg=",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBgbizpy8hR1ycUt9DjRntq2b16WZC+3yLR7PTKr3U+4kUdVo9GV3a02Jes8ALtvKMZaG6HWYF9lOilX5S+3lAIuECp4nX0+C2boWzjXwKNiExeDKXl/wqwmxtDUCTwb4h8lB3zf7n88IQfnkN/Vk+OyZM5hAJmG2/ke2Yn4fN+2dgKuF/4XTUBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAQT+4jyg=",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBgbizpy8hR1ycUt9DjRntq2b16WZC+3yLR7PTKr3U+4kUdVo9GV3a02Jes8ALtvKMZaG6HWYF9lOilX5S+3lAIuECp4nX0+C2boWzjXwKNiExeDKXl/wqwmxtDUCTwb4h8lB3zf7n88IQfnkN/Vk+OyZM5hAJmG2/ke2Yn4fN+2dgKuF/4XTUBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAQT+4jyg=",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBgbizpy8hR1ycUt9DjRntq2b16WZC+3yLR7PTKr3U+4kUdVo9GV3a02Jes8ALtvKMZaG6HWYF9lOilX5S+3lAIuECp4nX0+C2boWzjXwKNiExeDKXl/wqwmxtDUCTwb4h8lB3zf7n88IQfnkN/Vk+OyZM5hAJmG2/ke2Yn4fN+2dgKuF/4XTUBoQb8G7JDJvjAvhl/2o4On7opDOJpYqOjgiw3UCqpdE78EaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAQT+4jyg=",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
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
    "channel_id": "ch_2v2mPXo6wksBiz69oFV87UUobcYCjqNNS8wHkt3EEjWKUBmxdV",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
