
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU&role=responder
```

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhATYCBrI2BNuE6IvbTxvKKCBHiukJKReG/sl/95YnHm7zhj+qJSJgAKEBgjC/LrZ1mGltIX68J5ML2qxkm4r6rSDZKH/ih6dhz12GJGE5yoAAAgoAhhAGeddIAMCgec6VB+9/6Y9a5tYzaqU5ibParER/CtIESsVAUssbVx8DpPeyrw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423318,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuED8jEJxaIw6djWDLtpiEZ/a6+LgrJbEAWrjQvolomASDw/70LjGaIJNkmIw7fTyD+Z5rRig2Eu/1KGwbiGbKrYNuIP4gTIBoQE2AgayNgTbhOiL208byiggR4rpCSkXhv7Jf/eWJx5u84Y/qiUiYAChAYIwvy62dZhpbSF+vCeTC9qsZJuK+q0g2Sh/4oenYc9dhiRhOcqAAAIKAIYQBnnXSADAoHnOlQfvf+mPWubWM2qlOYmz2qxEfwrSBErFQFLLG1cfAwLcbJk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423318,
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
    "channel_id": null,
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
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuED8jEJxaIw6djWDLtpiEZ/a6+LgrJbEAWrjQvolomASDw/70LjGaIJNkmIw7fTyD+Z5rRig2Eu/1KGwbiGbKrYNuIP4gTIBoQE2AgayNgTbhOiL208byiggR4rpCSkXhv7Jf/eWJx5u84Y/qiUiYAChAYIwvy62dZhpbSF+vCeTC9qsZJuK+q0g2Sh/4oenYc9dhiRhOcqAAAIKAIYQBnnXSADAoHnOlQfvf+mPWubWM2qlOYmz2qxEfwrSBErFQFLLG1cfAwLcbJk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423317,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAa4msOglzoVeEFb0xDhH+1AMSQIKLa5knTAMAabt1ulpOwnTGzEjo5TIPT7RuSgIUhe+IdYmIykyUbwQkgcWhALhA/IxCcWiMOnY1gy7aYhGf2uvi4KyWxAFq40L6JaJgEg8P+9C4xmiCTZJiMO308g/mea0YoNhLv9ShsG4hmyq2DbiD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwOUGt0a"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423317,
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
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAa4msOglzoVeEFb0xDhH+1AMSQIKLa5knTAMAabt1ulpOwnTGzEjo5TIPT7RuSgIUhe+IdYmIykyUbwQkgcWhALhA/IxCcWiMOnY1gy7aYhGf2uvi4KyWxAFq40L6JaJgEg8P+9C4xmiCTZJiMO308g/mea0YoNhLv9ShsG4hmyq2DbiD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwOUGt0a",
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAa4msOglzoVeEFb0xDhH+1AMSQIKLa5knTAMAabt1ulpOwnTGzEjo5TIPT7RuSgIUhe+IdYmIykyUbwQkgcWhALhA/IxCcWiMOnY1gy7aYhGf2uvi4KyWxAFq40L6JaJgEg8P+9C4xmiCTZJiMO308g/mea0YoNhLv9ShsG4hmyq2DbiD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwOUGt0a",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAa4msOglzoVeEFb0xDhH+1AMSQIKLa5knTAMAabt1ulpOwnTGzEjo5TIPT7RuSgIUhe+IdYmIykyUbwQkgcWhALhA/IxCcWiMOnY1gy7aYhGf2uvi4KyWxAFq40L6JaJgEg8P+9C4xmiCTZJiMO308g/mea0YoNhLv9ShsG4hmyq2DbiD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwOUGt0a",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAa4msOglzoVeEFb0xDhH+1AMSQIKLa5knTAMAabt1ulpOwnTGzEjo5TIPT7RuSgIUhe+IdYmIykyUbwQkgcWhALhA/IxCcWiMOnY1gy7aYhGf2uvi4KyWxAFq40L6JaJgEg8P+9C4xmiCTZJiMO308g/mea0YoNhLv9ShsG4hmyq2DbiD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwOUGt0a",
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
    "to": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "message": {
        "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
        "from": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP",
        "info": "Hello",
        "to": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU"
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
    "to": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "message": {
        "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
        "from": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU",
        "info": "Hello back",
        "to": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423316,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP",
      "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
  "id": -576460752303423316,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP",
      "balance": 69999999999999
    },
    {
      "account": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU",
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "event": "own_funding_locked"
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "state": "tx_+QENCwH4hLhAa4msOglzoVeEFb0xDhH+1AMSQIKLa5knTAMAabt1ulpOwnTGzEjo5TIPT7RuSgIUhe+IdYmIykyUbwQkgcWhALhA/IxCcWiMOnY1gy7aYhGf2uvi4KyWxAFq40L6JaJgEg8P+9C4xmiCTZJiMO308g/mea0YoNhLv9ShsG4hmyq2DbiD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwOUGt0a"
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "state": "tx_+QENCwH4hLhAa4msOglzoVeEFb0xDhH+1AMSQIKLa5knTAMAabt1ulpOwnTGzEjo5TIPT7RuSgIUhe+IdYmIykyUbwQkgcWhALhA/IxCcWiMOnY1gy7aYhGf2uvi4KyWxAFq40L6JaJgEg8P+9C4xmiCTZJiMO308g/mea0YoNhLv9ShsG4hmyq2DbiD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwOUGt0a"
    }
  },
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
    "from": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP",
    "to": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkOichjerfEojsda5DK+C6cO3aMyW+M8f0HZtKGAEiasAqCw9yxFdYbLwuw9GaY7Vk8/TTxqpPJsWcv+SwFMfZyN/Cvw9Vw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP",
          "op": "OffChainTransfer",
          "to": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU"
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBbe/8gW00gSS8jdX3Gm9vEJ/Hr9vkQvmneIIzONOJtqJNvidbSrE8vqnSefhbDpikX4dwjU18ueFWbUfvFr8wKuEj4RjkCoQZDonIY3q3xKI7HWuQyvgunDt2jMlvjPH9B2bShgBImrAKgsPcsRXWGy8LsPRmmO1ZPP008aqTybFnL/ksBTH2cjfw9usl2"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?port=14035&protocol=json-rpc&reconnect_tx=tx_%2BJ0LAfhCuED5i01pqh3CjS%2Bp5xY8P6clCsYWtCwuSsxzHyEeO6PN5E7r5WjIk0dAy2PL%2Fdiiq3LbXGmgldfxvd0Jk%2FxRM3wDuFX4U4ICPwGhBkOichjerfEojsda5DK%2BC6cO3aMyW%2BM8f0HZtKGAEiasAYlyZXNwb25kZXKhAYIwvy62dZhpbSF%2BvCeTC9qsZJuK%2Bq0g2Sh%2F4oenYc9daQ8HEw%3D%3D&role=responder
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBkOichjerfEojsda5DK+C6cO3aMyW+M8f0HZtKGAEiasoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYY2kdavv/+GG0jrV+ABAIYSMJzlQAABzdOr/g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423315,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBEwnGRqwn62eyEG9k5De0iL5tpaCRx2URJGe91x9hrQuUpTKCQzvkzz7e/G1Y87XGx9Umr6o4IsKDRUwhH3BALuF/4XTUBoQZDonIY3q3xKI7HWuQyvgunDt2jMlvjPH9B2bShgBImrKEBgjC/LrZ1mGltIX68J5ML2qxkm4r6rSDZKH/ih6dhz12GNpHWr7//hhtI61fgAQCGEjCc5UAAAYOII1w="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
  "id": -576460752303423315,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBEwnGRqwn62eyEG9k5De0iL5tpaCRx2URJGe91x9hrQuUpTKCQzvkzz7e/G1Y87XGx9Umr6o4IsKDRUwhH3BALuF/4XTUBoQZDonIY3q3xKI7HWuQyvgunDt2jMlvjPH9B2bShgBImrKEBgjC/LrZ1mGltIX68J5ML2qxkm4r6rSDZKH/ih6dhz12GNpHWr7//hhtI61fgAQCGEjCc5UAAAYOII1w=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423314,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBEwnGRqwn62eyEG9k5De0iL5tpaCRx2URJGe91x9hrQuUpTKCQzvkzz7e/G1Y87XGx9Umr6o4IsKDRUwhH3BALuEBFhLT2/adfPR7dmZhdTDK5yHL5xPj28+L5bPIm8KwC/e6ZFXXRbv2RDKidfr8q5w7/cwMfdTP9yjS0VKpIwncNuF/4XTUBoQZDonIY3q3xKI7HWuQyvgunDt2jMlvjPH9B2bShgBImrKEBgjC/LrZ1mGltIX68J5ML2qxkm4r6rSDZKH/ih6dhz12GNpHWr7//hhtI61fgAQCGEjCc5UAAAarvAYM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
  "id": -576460752303423314,
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBEwnGRqwn62eyEG9k5De0iL5tpaCRx2URJGe91x9hrQuUpTKCQzvkzz7e/G1Y87XGx9Umr6o4IsKDRUwhH3BALuEBFhLT2/adfPR7dmZhdTDK5yHL5xPj28+L5bPIm8KwC/e6ZFXXRbv2RDKidfr8q5w7/cwMfdTP9yjS0VKpIwncNuF/4XTUBoQZDonIY3q3xKI7HWuQyvgunDt2jMlvjPH9B2bShgBImrKEBgjC/LrZ1mGltIX68J5ML2qxkm4r6rSDZKH/ih6dhz12GNpHWr7//hhtI61fgAQCGEjCc5UAAAarvAYM=",
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "event": "close_mutual"
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBEwnGRqwn62eyEG9k5De0iL5tpaCRx2URJGe91x9hrQuUpTKCQzvkzz7e/G1Y87XGx9Umr6o4IsKDRUwhH3BALuEBFhLT2/adfPR7dmZhdTDK5yHL5xPj28+L5bPIm8KwC/e6ZFXXRbv2RDKidfr8q5w7/cwMfdTP9yjS0VKpIwncNuF/4XTUBoQZDonIY3q3xKI7HWuQyvgunDt2jMlvjPH9B2bShgBImrKEBgjC/LrZ1mGltIX68J5ML2qxkm4r6rSDZKH/ih6dhz12GNpHWr7//hhtI61fgAQCGEjCc5UAAAarvAYM=",
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "event": "close_mutual"
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
    "channel_id": "ch_WndmRFDqEqtUiS2n1CkExWrE3dUrUJdpmAn3sU7WSVAK7RXVg",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```
