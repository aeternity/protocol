
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
      "fsm_id": "ba_YxyA8jWr6Bl4D0iCv6yAooJtEGGoEPhBfwk2M7Q7iwa2f4eJ"
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
      "fsm_id": "ba_ZybPRJhtASDvAoHL+cju0qRSiDKDcZAbGISX7Y1AB+qGvQGd"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt1OGPwFQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422427,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDYoPFnIcGocvegW5uaD2J/2bTGjL1d/Y68tUbeoKFk25RaUV83JiMb2UA+LUEem05XfVIsGPzT3LM0NNXOMggPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LdWAHZNs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422427,
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "fsm_id": "ba_ZybPRJhtASDvAoHL+cju0qRSiDKDcZAbGISX7Y1AB+qGvQGd",
      "signed_tx": "tx_+MsLAfhCuEDYoPFnIcGocvegW5uaD2J/2bTGjL1d/Y68tUbeoKFk25RaUV83JiMb2UA+LUEem05XfVIsGPzT3LM0NNXOMggPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LdWAHZNs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422426,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAQr40vVqt0g4P5sz/vL3uh4ilV2copx+349GWQ8LLLuOeuvaMOAYuHoVYRA/2jZjeBGbILnEuOAMr7T4K0SLcD7hA2KDxZyHBqHL3oFubmg9if9m0xoy9Xf2OvLVG3qChZNuUWlFfNyYjG9lAPi1BHptOV31SLBj809yzNDTVzjIID7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3Vf3Des"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
  "id": -576460752303422426,
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAQr40vVqt0g4P5sz/vL3uh4ilV2copx+349GWQ8LLLuOeuvaMOAYuHoVYRA/2jZjeBGbILnEuOAMr7T4K0SLcD7hA2KDxZyHBqHL3oFubmg9if9m0xoy9Xf2OvLVG3qChZNuUWlFfNyYjG9lAPi1BHptOV31SLBj809yzNDTVzjIID7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3Vf3Des",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_YxyA8jWr6Bl4D0iCv6yAooJtEGGoEPhBfwk2M7Q7iwa2f4eJ"
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAQr40vVqt0g4P5sz/vL3uh4ilV2copx+349GWQ8LLLuOeuvaMOAYuHoVYRA/2jZjeBGbILnEuOAMr7T4K0SLcD7hA2KDxZyHBqHL3oFubmg9if9m0xoy9Xf2OvLVG3qChZNuUWlFfNyYjG9lAPi1BHptOV31SLBj809yzNDTVzjIID7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3Vf3Des",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAQr40vVqt0g4P5sz/vL3uh4ilV2copx+349GWQ8LLLuOeuvaMOAYuHoVYRA/2jZjeBGbILnEuOAMr7T4K0SLcD7hA2KDxZyHBqHL3oFubmg9if9m0xoy9Xf2OvLVG3qChZNuUWlFfNyYjG9lAPi1BHptOV31SLBj809yzNDTVzjIID7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3Vf3Des",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAQr40vVqt0g4P5sz/vL3uh4ilV2copx+349GWQ8LLLuOeuvaMOAYuHoVYRA/2jZjeBGbILnEuOAMr7T4K0SLcD7hA2KDxZyHBqHL3oFubmg9if9m0xoy9Xf2OvLVG3qChZNuUWlFfNyYjG9lAPi1BHptOV31SLBj809yzNDTVzjIID7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3Vf3Des",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "message": {
        "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "message": {
        "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
  "id": -576460752303422425,
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
  "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
  "id": -576460752303422425,
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "state": "tx_+QENCwH4hLhAQr40vVqt0g4P5sz/vL3uh4ilV2copx+349GWQ8LLLuOeuvaMOAYuHoVYRA/2jZjeBGbILnEuOAMr7T4K0SLcD7hA2KDxZyHBqHL3oFubmg9if9m0xoy9Xf2OvLVG3qChZNuUWlFfNyYjG9lAPi1BHptOV31SLBj809yzNDTVzjIID7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3Vf3Des"
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "state": "tx_+QENCwH4hLhAQr40vVqt0g4P5sz/vL3uh4ilV2copx+349GWQ8LLLuOeuvaMOAYuHoVYRA/2jZjeBGbILnEuOAMr7T4K0SLcD7hA2KDxZyHBqHL3oFubmg9if9m0xoy9Xf2OvLVG3qChZNuUWlFfNyYjG9lAPi1BHptOV31SLBj809yzNDTVzjIID7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3Vf3Des"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMBXVz9I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422424,
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
  "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
  "id": -576460752303422424,
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBn4QVMWbEm1WYyDsyrELQuuehSPMA/qo5phi7A1OrmK9AqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAti4Kv8=",
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
  "id": -576460752303422423,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA0ei9X1KKlMW3tLGsP2hkgkTlFS5mPgZE8hvVrhxfr8d3a+/wWMThr4xS7F7e2lWxO+vTPQYbIwY82p4rpA3sCuEj4RjkCoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKUPvtF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
  "id": -576460752303422423,
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA0ei9X1KKlMW3tLGsP2hkgkTlFS5mPgZE8hvVrhxfr8d3a+/wWMThr4xS7F7e2lWxO+vTPQYbIwY82p4rpA3sCuEj4RjkCoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKUPvtF",
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
  "id": -576460752303422422,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA0ei9X1KKlMW3tLGsP2hkgkTlFS5mPgZE8hvVrhxfr8d3a+/wWMThr4xS7F7e2lWxO+vTPQYbIwY82p4rpA3sCuEDigN/IZbox0cvVF8OGVcfnOlwzDvq75c7CbftlboTDz4wA8bid9LqGYhGFCxyDk9Zbho3u/4xT5yApS5ocPakDuEj4RjkCoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLF580y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
  "id": -576460752303422422,
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "state": "tx_+NILAfiEuEA0ei9X1KKlMW3tLGsP2hkgkTlFS5mPgZE8hvVrhxfr8d3a+/wWMThr4xS7F7e2lWxO+vTPQYbIwY82p4rpA3sCuEDigN/IZbox0cvVF8OGVcfnOlwzDvq75c7CbftlboTDz4wA8bid9LqGYhGFCxyDk9Zbho3u/4xT5yApS5ocPakDuEj4RjkCoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLF580y"
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "state": "tx_+NILAfiEuEA0ei9X1KKlMW3tLGsP2hkgkTlFS5mPgZE8hvVrhxfr8d3a+/wWMThr4xS7F7e2lWxO+vTPQYbIwY82p4rpA3sCuEDigN/IZbox0cvVF8OGVcfnOlwzDvq75c7CbftlboTDz4wA8bid9LqGYhGFCxyDk9Zbho3u/4xT5yApS5ocPakDuEj4RjkCoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLF580y"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422421,
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
  "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
  "id": -576460752303422421,
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
  "id": -576460752303422420,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
  "id": -576460752303422420,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA0ei9X1KKlMW3tLGsP2hkgkTlFS5mPgZE8hvVrhxfr8d3a+/wWMThr4xS7F7e2lWxO+vTPQYbIwY82p4rpA3sCuEDigN/IZbox0cvVF8OGVcfnOlwzDvq75c7CbftlboTDz4wA8bid9LqGYhGFCxyDk9Zbho3u/4xT5yApS5ocPakDuEj4RjkCoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLF580y",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEA0ei9X1KKlMW3tLGsP2hkgkTlFS5mPgZE8hvVrhxfr8d3a+/wWMThr4xS7F7e2lWxO+vTPQYbIwY82p4rpA3sCuEDigN/IZbox0cvVF8OGVcfnOlwzDvq75c7CbftlboTDz4wA8bid9LqGYhGFCxyDk9Zbho3u/4xT5yApS5ocPakDuEj4RjkCoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLF580y",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEA0ei9X1KKlMW3tLGsP2hkgkTlFS5mPgZE8hvVrhxfr8d3a+/wWMThr4xS7F7e2lWxO+vTPQYbIwY82p4rpA3sCuEDigN/IZbox0cvVF8OGVcfnOlwzDvq75c7CbftlboTDz4wA8bid9LqGYhGFCxyDk9Zbho3u/4xT5yApS5ocPakDuEj4RjkCoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLF580y",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
  "id": -576460752303422419,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
  "id": -576460752303422419,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBn4QVMWbEm1WYyDsyrELQuuehSPMA/qo5phi7A1OrmK9oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEA0ei9X1KKlMW3tLGsP2hkgkTlFS5mPgZE8hvVrhxfr8d3a+/wWMThr4xS7F7e2lWxO+vTPQYbIwY82p4rpA3sCuEDigN/IZbox0cvVF8OGVcfnOlwzDvq75c7CbftlboTDz4wA8bid9LqGYhGFCxyDk9Zbho3u/4xT5yApS5ocPakDuEj4RjkCoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACG4JEMNh5+d74AaXI=",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhA12S+0Jhec+1GK2XNyUElxZIC9igRMUvr6vg9Hil35Lc51e3xB9pz1inSv8uq0/+Nl9g8WfPj2aJUgW24SXleD7kCd/kCdDcBoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhANHovV9SipTFt7SxrD9oZIJE5RUuZj4GRPIb1a4cX6/Hd2vv8FjE4a+MUuxe3tpVsTvr0z0GGyMGPNqeK6QN7ArhA4oDfyGW6MdHL1RfDhlXH5zpcMw76u+XOwm37ZW6Ew8+MAPG4nfS6hmIRhQscg5PWW4aN7v+MU+cgKUuaHD2pA7hI+EY5AqEGfhBUxZsSbVZjIOzKsQtC656FI8wD+qjmmGLsDU6uYr0CoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhuCRDDYefnf2M9vB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA12S+0Jhec+1GK2XNyUElxZIC9igRMUvr6vg9Hil35Lc51e3xB9pz1inSv8uq0/+Nl9g8WfPj2aJUgW24SXleD7kCd/kCdDcBoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhANHovV9SipTFt7SxrD9oZIJE5RUuZj4GRPIb1a4cX6/Hd2vv8FjE4a+MUuxe3tpVsTvr0z0GGyMGPNqeK6QN7ArhA4oDfyGW6MdHL1RfDhlXH5zpcMw76u+XOwm37ZW6Ew8+MAPG4nfS6hmIRhQscg5PWW4aN7v+MU+cgKUuaHD2pA7hI+EY5AqEGfhBUxZsSbVZjIOzKsQtC656FI8wD+qjmmGLsDU6uYr0CoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhuCRDDYefnf2M9vB",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA12S+0Jhec+1GK2XNyUElxZIC9igRMUvr6vg9Hil35Lc51e3xB9pz1inSv8uq0/+Nl9g8WfPj2aJUgW24SXleD7kCd/kCdDcBoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhANHovV9SipTFt7SxrD9oZIJE5RUuZj4GRPIb1a4cX6/Hd2vv8FjE4a+MUuxe3tpVsTvr0z0GGyMGPNqeK6QN7ArhA4oDfyGW6MdHL1RfDhlXH5zpcMw76u+XOwm37ZW6Ew8+MAPG4nfS6hmIRhQscg5PWW4aN7v+MU+cgKUuaHD2pA7hI+EY5AqEGfhBUxZsSbVZjIOzKsQtC656FI8wD+qjmmGLsDU6uYr0CoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhuCRDDYefnf2M9vB",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBn4QVMWbEm1WYyDsyrELQuuehSPMA/qo5phi7A1OrmK9oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAAxurho7g==",
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
    "signed_tx": "tx_+KcLAfhCuEAeMgTXImGpLUZi4zvUkSmfx7i2cyqrBJSvOmlbtOPF1zasgiAacYSH1VVp1XZOATp6jLPunOzzTTsgsKYY+oEFuF/4XTgBoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAMWPlUr8="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAeMgTXImGpLUZi4zvUkSmfx7i2cyqrBJSvOmlbtOPF1zasgiAacYSH1VVp1XZOATp6jLPunOzzTTsgsKYY+oEFuF/4XTgBoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAMWPlUr8=",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAeMgTXImGpLUZi4zvUkSmfx7i2cyqrBJSvOmlbtOPF1zasgiAacYSH1VVp1XZOATp6jLPunOzzTTsgsKYY+oEFuF/4XTgBoQZ+EFTFmxJtVmMg7MqxC0LrnoUjzAP6qOaYYuwNTq5ivaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAMWPlUr8=",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
    "channel_id": "ch_xX8ZhXoxpuStsEn7YPSR5SwmfKDrpcZ9rvZtRVACkNzfC1yXJ",
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
      "fsm_id": "ba_iP6B93meRGEEt/vZ/dc6Woa9goVHJ4bl+fV1XBfWtF6gkDyr"
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
      "fsm_id": "ba_QggD/Ql1mI0hucYXO8mYhhFHcVZqnOFwvWqDVhQZxtEmn66N"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt4q00HGw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422418,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECvQUR5MB8Rm3FHOVqmrIPOE4IwXJvUSAiG57AXEqdRxsNl/Exy/o9F0QSNPkSu/SjcY4TmMKjR1WFbtZiEQ+APuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LeOAurN0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422418,
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "fsm_id": "ba_QggD/Ql1mI0hucYXO8mYhhFHcVZqnOFwvWqDVhQZxtEmn66N",
      "signed_tx": "tx_+MsLAfhCuECvQUR5MB8Rm3FHOVqmrIPOE4IwXJvUSAiG57AXEqdRxsNl/Exy/o9F0QSNPkSu/SjcY4TmMKjR1WFbtZiEQ+APuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LeOAurN0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422417,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAODummKAyhgSBlOHItW5mi8D8yzsis4F3lgsUxjpFEHqaIFt6Fhj/+HdgwZgsArmN5LekzZ1qTPz42LZtEeLbC7hAr0FEeTAfEZtxRzlapqyDzhOCMFyb1EgIhuewFxKnUcbDZfxMcv6PRdEEjT5Erv0o3GOE5jCo0dVhW7WYhEPgD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3gazBN5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
  "id": -576460752303422417,
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAODummKAyhgSBlOHItW5mi8D8yzsis4F3lgsUxjpFEHqaIFt6Fhj/+HdgwZgsArmN5LekzZ1qTPz42LZtEeLbC7hAr0FEeTAfEZtxRzlapqyDzhOCMFyb1EgIhuewFxKnUcbDZfxMcv6PRdEEjT5Erv0o3GOE5jCo0dVhW7WYhEPgD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3gazBN5",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_iP6B93meRGEEt/vZ/dc6Woa9goVHJ4bl+fV1XBfWtF6gkDyr"
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAODummKAyhgSBlOHItW5mi8D8yzsis4F3lgsUxjpFEHqaIFt6Fhj/+HdgwZgsArmN5LekzZ1qTPz42LZtEeLbC7hAr0FEeTAfEZtxRzlapqyDzhOCMFyb1EgIhuewFxKnUcbDZfxMcv6PRdEEjT5Erv0o3GOE5jCo0dVhW7WYhEPgD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3gazBN5",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAODummKAyhgSBlOHItW5mi8D8yzsis4F3lgsUxjpFEHqaIFt6Fhj/+HdgwZgsArmN5LekzZ1qTPz42LZtEeLbC7hAr0FEeTAfEZtxRzlapqyDzhOCMFyb1EgIhuewFxKnUcbDZfxMcv6PRdEEjT5Erv0o3GOE5jCo0dVhW7WYhEPgD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3gazBN5",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAODummKAyhgSBlOHItW5mi8D8yzsis4F3lgsUxjpFEHqaIFt6Fhj/+HdgwZgsArmN5LekzZ1qTPz42LZtEeLbC7hAr0FEeTAfEZtxRzlapqyDzhOCMFyb1EgIhuewFxKnUcbDZfxMcv6PRdEEjT5Erv0o3GOE5jCo0dVhW7WYhEPgD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3gazBN5",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "message": {
        "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "message": {
        "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
  "id": -576460752303422416,
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
  "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
  "id": -576460752303422416,
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "state": "tx_+QENCwH4hLhAODummKAyhgSBlOHItW5mi8D8yzsis4F3lgsUxjpFEHqaIFt6Fhj/+HdgwZgsArmN5LekzZ1qTPz42LZtEeLbC7hAr0FEeTAfEZtxRzlapqyDzhOCMFyb1EgIhuewFxKnUcbDZfxMcv6PRdEEjT5Erv0o3GOE5jCo0dVhW7WYhEPgD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3gazBN5"
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "state": "tx_+QENCwH4hLhAODummKAyhgSBlOHItW5mi8D8yzsis4F3lgsUxjpFEHqaIFt6Fhj/+HdgwZgsArmN5LekzZ1qTPz42LZtEeLbC7hAr0FEeTAfEZtxRzlapqyDzhOCMFyb1EgIhuewFxKnUcbDZfxMcv6PRdEEjT5Erv0o3GOE5jCo0dVhW7WYhEPgD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3gazBN5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMBXVz9I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422415,
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
  "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
  "id": -576460752303422415,
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqoNHjiTThdrCCDjdWsLkUxoWv34cmPSMZoZ27xwVXAxAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAiH0zyU=",
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
  "id": -576460752303422414,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAhtFQDPZgZhPRIVe73jz6y+/qCNPmdjdhp2zYtNlLPA7959Vr1Kn/W01Vq8H3lwUTZ1u/8waM+NTZsI9Cdz+UPuEj4RjkCoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJReL1h"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
  "id": -576460752303422414,
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAhtFQDPZgZhPRIVe73jz6y+/qCNPmdjdhp2zYtNlLPA7959Vr1Kn/W01Vq8H3lwUTZ1u/8waM+NTZsI9Cdz+UPuEj4RjkCoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJReL1h",
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
  "id": -576460752303422413,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAhtFQDPZgZhPRIVe73jz6y+/qCNPmdjdhp2zYtNlLPA7959Vr1Kn/W01Vq8H3lwUTZ1u/8waM+NTZsI9Cdz+UPuEDfLhyNpGaJoZGxPuGjEwiMYdct3K74PNHxxEofMaGUVhQXNtWkveka1GhDiSUSpZBL6pkbblSAjT9l9c3H+5EDuEj4RjkCoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKAa69k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
  "id": -576460752303422413,
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "state": "tx_+NILAfiEuEAhtFQDPZgZhPRIVe73jz6y+/qCNPmdjdhp2zYtNlLPA7959Vr1Kn/W01Vq8H3lwUTZ1u/8waM+NTZsI9Cdz+UPuEDfLhyNpGaJoZGxPuGjEwiMYdct3K74PNHxxEofMaGUVhQXNtWkveka1GhDiSUSpZBL6pkbblSAjT9l9c3H+5EDuEj4RjkCoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKAa69k"
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "state": "tx_+NILAfiEuEAhtFQDPZgZhPRIVe73jz6y+/qCNPmdjdhp2zYtNlLPA7959Vr1Kn/W01Vq8H3lwUTZ1u/8waM+NTZsI9Cdz+UPuEDfLhyNpGaJoZGxPuGjEwiMYdct3K74PNHxxEofMaGUVhQXNtWkveka1GhDiSUSpZBL6pkbblSAjT9l9c3H+5EDuEj4RjkCoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKAa69k"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422412,
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
  "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
  "id": -576460752303422412,
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
  "id": -576460752303422411,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
  "id": -576460752303422411,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAhtFQDPZgZhPRIVe73jz6y+/qCNPmdjdhp2zYtNlLPA7959Vr1Kn/W01Vq8H3lwUTZ1u/8waM+NTZsI9Cdz+UPuEDfLhyNpGaJoZGxPuGjEwiMYdct3K74PNHxxEofMaGUVhQXNtWkveka1GhDiSUSpZBL6pkbblSAjT9l9c3H+5EDuEj4RjkCoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKAa69k",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAhtFQDPZgZhPRIVe73jz6y+/qCNPmdjdhp2zYtNlLPA7959Vr1Kn/W01Vq8H3lwUTZ1u/8waM+NTZsI9Cdz+UPuEDfLhyNpGaJoZGxPuGjEwiMYdct3K74PNHxxEofMaGUVhQXNtWkveka1GhDiSUSpZBL6pkbblSAjT9l9c3H+5EDuEj4RjkCoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKAa69k",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAhtFQDPZgZhPRIVe73jz6y+/qCNPmdjdhp2zYtNlLPA7959Vr1Kn/W01Vq8H3lwUTZ1u/8waM+NTZsI9Cdz+UPuEDfLhyNpGaJoZGxPuGjEwiMYdct3K74PNHxxEofMaGUVhQXNtWkveka1GhDiSUSpZBL6pkbblSAjT9l9c3H+5EDuEj4RjkCoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKAa69k",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
  "id": -576460752303422410,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
  "id": -576460752303422410,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBqoNHjiTThdrCCDjdWsLkUxoWv34cmPSMZoZ27xwVXAxoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEAhtFQDPZgZhPRIVe73jz6y+/qCNPmdjdhp2zYtNlLPA7959Vr1Kn/W01Vq8H3lwUTZ1u/8waM+NTZsI9Cdz+UPuEDfLhyNpGaJoZGxPuGjEwiMYdct3K74PNHxxEofMaGUVhQXNtWkveka1GhDiSUSpZBL6pkbblSAjT9l9c3H+5EDuEj4RjkCoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACG4JEMNh5+MtW24Ko=",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhA4QcS3pbHhYhIQQlqPRhYRIbMiPy61W+opRVIhrybcycknCWJnuilxeqXvcIAxA2AHoJsz/2JX520rNSgZwrPCrkCd/kCdDcBoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAIbRUAz2YGYT0SFXu948+svv6gjT5nY3Yads2LTZSzwO/efVa9Sp/1tNVavB95cFE2dbv/MGjPjU2bCPQnc/lD7hA3y4cjaRmiaGRsT7hoxMIjGHXLdyu+DzR8cRKHzGhlFYUFzbVpL3pGtRoQ4klEqWQS+qZG25UgI0/ZfXNx/uRA7hI+EY5AqEGqg0eOJNOF2sIION1awuRTGha/fhyY9IxmhnbvHBVcDECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhuCRDDYefjKBeL9y"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA4QcS3pbHhYhIQQlqPRhYRIbMiPy61W+opRVIhrybcycknCWJnuilxeqXvcIAxA2AHoJsz/2JX520rNSgZwrPCrkCd/kCdDcBoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAIbRUAz2YGYT0SFXu948+svv6gjT5nY3Yads2LTZSzwO/efVa9Sp/1tNVavB95cFE2dbv/MGjPjU2bCPQnc/lD7hA3y4cjaRmiaGRsT7hoxMIjGHXLdyu+DzR8cRKHzGhlFYUFzbVpL3pGtRoQ4klEqWQS+qZG25UgI0/ZfXNx/uRA7hI+EY5AqEGqg0eOJNOF2sIION1awuRTGha/fhyY9IxmhnbvHBVcDECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhuCRDDYefjKBeL9y",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA4QcS3pbHhYhIQQlqPRhYRIbMiPy61W+opRVIhrybcycknCWJnuilxeqXvcIAxA2AHoJsz/2JX520rNSgZwrPCrkCd/kCdDcBoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAIbRUAz2YGYT0SFXu948+svv6gjT5nY3Yads2LTZSzwO/efVa9Sp/1tNVavB95cFE2dbv/MGjPjU2bCPQnc/lD7hA3y4cjaRmiaGRsT7hoxMIjGHXLdyu+DzR8cRKHzGhlFYUFzbVpL3pGtRoQ4klEqWQS+qZG25UgI0/ZfXNx/uRA7hI+EY5AqEGqg0eOJNOF2sIION1awuRTGha/fhyY9IxmhnbvHBVcDECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhuCRDDYefjKBeL9y",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBqoNHjiTThdrCCDjdWsLkUxoWv34cmPSMZoZ27xwVXAxoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAAzhkHMHw==",
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
    "signed_tx": "tx_+KcLAfhCuEC+BRjHA/Gus9qPuMbLkoron21tH1jsEr/7sMP7HZFNkJsOywQNrtqx8S9NaMxsIRnvMZyLGOOSDUz6lPoLzBsBuF/4XTgBoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAM6bwgL4="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC+BRjHA/Gus9qPuMbLkoron21tH1jsEr/7sMP7HZFNkJsOywQNrtqx8S9NaMxsIRnvMZyLGOOSDUz6lPoLzBsBuF/4XTgBoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAM6bwgL4=",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC+BRjHA/Gus9qPuMbLkoron21tH1jsEr/7sMP7HZFNkJsOywQNrtqx8S9NaMxsIRnvMZyLGOOSDUz6lPoLzBsBuF/4XTgBoQaqDR44k04Xawgg43VrC5FMaFr9+HJj0jGaGdu8cFVwMaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAM6bwgL4=",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
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
    "channel_id": "ch_2HtjPFquXiVfKSbnXFh1SK1oZSB2oedwNPuWp9tm7W1PA2fFVt",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
