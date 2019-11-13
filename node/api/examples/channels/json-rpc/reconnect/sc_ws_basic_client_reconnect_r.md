
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH&role=initiator
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
      "fsm_id": "ba_InjTf+WoiC/egAVSUa4eFY8Xbnqo1hsp1HcdKpqzmoSoL1D7"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH&role=responder
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
      "fsm_id": "ba_q7iC/fId3vqQOxzNba/V6XYN7xKqYGI6TYMAv11HPIBAYLdw"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAZxDM9BiTzFpS5hy+lom7XXexvNUoE4C7mSKujTfKLPLhj+qJSJgAKEBS/jO5UGWg32L0vdFXoVxcYcJUTd0aWCtT79BCq7KqZqGJGE5yoAAAgoAhhAGeddIAMCgGLhuErzxBZ2xsoxOkYB+IYb24CHBcl28KSToXkG/rEsDVccfGg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423002,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA1WR7BpdhTK3fWFGwsoLhDAudQ/IA7Zh+eH61M+Fe7xbHQpgg0I0324rFm/dbM7aH+cgnCLaU8EFPOUVffQ9gKuIP4gTIBoQGcQzPQYk8xaUuYcvpaJu113sbzVKBOAu5kiro03yizy4Y/qiUiYAChAUv4zuVBloN9i9L3RV6FcXGHCVE3dGlgrU+/QQquyqmahiRhOcqAAAIKAIYQBnnXSADAoBi4bhK88QWdsbKMTpGAfiGG9uAhwXJdvCkk6F5Bv6xLA2R6YTA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423002,
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
      "signed_tx": "tx_+MsLAfhCuEA1WR7BpdhTK3fWFGwsoLhDAudQ/IA7Zh+eH61M+Fe7xbHQpgg0I0324rFm/dbM7aH+cgnCLaU8EFPOUVffQ9gKuIP4gTIBoQGcQzPQYk8xaUuYcvpaJu113sbzVKBOAu5kiro03yizy4Y/qiUiYAChAUv4zuVBloN9i9L3RV6FcXGHCVE3dGlgrU+/QQquyqmahiRhOcqAAAIKAIYQBnnXSADAoBi4bhK88QWdsbKMTpGAfiGG9uAhwXJdvCkk6F5Bv6xLA2R6YTA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423001,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAJNqZKuQJAvovo3rK4spw2YDiKJEjbLYa9QjY0xBLTjxYl27o5Ok6UCjhzwYDJb6xU2u9FfQMcLAeTh9VMrUaCLhANVkewaXYUyt31hRsLKC4QwLnUPyAO2Yfnh+tTPhXu8Wx0KYINCNN9uKxZv3WzO2h/nIJwi2lPBBTzlFX30PYCriD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwMAmVyD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423001,
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAJNqZKuQJAvovo3rK4spw2YDiKJEjbLYa9QjY0xBLTjxYl27o5Ok6UCjhzwYDJb6xU2u9FfQMcLAeTh9VMrUaCLhANVkewaXYUyt31hRsLKC4QwLnUPyAO2Yfnh+tTPhXu8Wx0KYINCNN9uKxZv3WzO2h/nIJwi2lPBBTzlFX30PYCriD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwMAmVyD",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAJNqZKuQJAvovo3rK4spw2YDiKJEjbLYa9QjY0xBLTjxYl27o5Ok6UCjhzwYDJb6xU2u9FfQMcLAeTh9VMrUaCLhANVkewaXYUyt31hRsLKC4QwLnUPyAO2Yfnh+tTPhXu8Wx0KYINCNN9uKxZv3WzO2h/nIJwi2lPBBTzlFX30PYCriD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwMAmVyD",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJNqZKuQJAvovo3rK4spw2YDiKJEjbLYa9QjY0xBLTjxYl27o5Ok6UCjhzwYDJb6xU2u9FfQMcLAeTh9VMrUaCLhANVkewaXYUyt31hRsLKC4QwLnUPyAO2Yfnh+tTPhXu8Wx0KYINCNN9uKxZv3WzO2h/nIJwi2lPBBTzlFX30PYCriD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwMAmVyD",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJNqZKuQJAvovo3rK4spw2YDiKJEjbLYa9QjY0xBLTjxYl27o5Ok6UCjhzwYDJb6xU2u9FfQMcLAeTh9VMrUaCLhANVkewaXYUyt31hRsLKC4QwLnUPyAO2Yfnh+tTPhXu8Wx0KYINCNN9uKxZv3WzO2h/nIJwi2lPBBTzlFX30PYCriD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwMAmVyD",
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
    "to": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "message": {
        "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
        "from": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR",
        "info": "Hello",
        "to": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH"
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
    "to": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "message": {
        "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
        "from": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH",
        "info": "Hello back",
        "to": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423000,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR",
      "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
  "id": -576460752303423000,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR",
      "balance": 69999999999999
    },
    {
      "account": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "state": "tx_+QENCwH4hLhAJNqZKuQJAvovo3rK4spw2YDiKJEjbLYa9QjY0xBLTjxYl27o5Ok6UCjhzwYDJb6xU2u9FfQMcLAeTh9VMrUaCLhANVkewaXYUyt31hRsLKC4QwLnUPyAO2Yfnh+tTPhXu8Wx0KYINCNN9uKxZv3WzO2h/nIJwi2lPBBTzlFX30PYCriD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwMAmVyD"
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "state": "tx_+QENCwH4hLhAJNqZKuQJAvovo3rK4spw2YDiKJEjbLYa9QjY0xBLTjxYl27o5Ok6UCjhzwYDJb6xU2u9FfQMcLAeTh9VMrUaCLhANVkewaXYUyt31hRsLKC4QwLnUPyAO2Yfnh+tTPhXu8Wx0KYINCNN9uKxZv3WzO2h/nIJwi2lPBBTzlFX30PYCriD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwMAmVyD"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR",
    "to": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvjlgkVveTCs/ir8viL6PAhC/zbW2m/YMYq5/pe/d45LAqA2HXLHDiVyT6N60Sf/91tc7tETfe9SAKdT2i4YrrI2i9tlLH4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR",
          "op": "OffChainTransfer",
          "to": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH"
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
    "signed_tx": "tx_+JALAfhCuECrwsKnhMEQvvyWkgO8UAZWd9nN0pj6pgNUIwFaLksEnQG691gJ4VpoduSSk1ttotK2lrk1EhNdUTXQL2FuxrgMuEj4RjkCoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOSwKgNh1yxw4lck+jetEn//dbXO7RE33vUgCnU9ouGK6yNouKtcpr"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
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
    "from": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR",
    "to": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvjlgkVveTCs/ir8viL6PAhC/zbW2m/YMYq5/pe/d45LAqA2HXLHDiVyT6N60Sf/91tc7tETfe9SAKdT2i4YrrI2i9tlLH4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR",
          "op": "OffChainTransfer",
          "to": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH"
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
    "signed_tx": "tx_+NILAfiEuEAL3Qv10MwO19w7v9JOpwSKyweNdb8b0Kgekb5KoE/Dqvzx1ZnAENeDkSmKm98XKj5qtZ8t2XtsXgrC2OJWVJwLuECrwsKnhMEQvvyWkgO8UAZWd9nN0pj6pgNUIwFaLksEnQG691gJ4VpoduSSk1ttotK2lrk1EhNdUTXQL2FuxrgMuEj4RjkCoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOSwKgNh1yxw4lck+jetEn//dbXO7RE33vUgCnU9ouGK6yNovMXlrj"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "state": "tx_+NILAfiEuEAL3Qv10MwO19w7v9JOpwSKyweNdb8b0Kgekb5KoE/Dqvzx1ZnAENeDkSmKm98XKj5qtZ8t2XtsXgrC2OJWVJwLuECrwsKnhMEQvvyWkgO8UAZWd9nN0pj6pgNUIwFaLksEnQG691gJ4VpoduSSk1ttotK2lrk1EhNdUTXQL2FuxrgMuEj4RjkCoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOSwKgNh1yxw4lck+jetEn//dbXO7RE33vUgCnU9ouGK6yNovMXlrj"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV&host=localhost&offchain_tx=tx_%2BNILAfiEuEAL3Qv10MwO19w7v9JOpwSKyweNdb8b0Kgekb5KoE%2FDqvzx1ZnAENeDkSmKm98XKj5qtZ8t2XtsXgrC2OJWVJwLuECrwsKnhMEQvvyWkgO8UAZWd9nN0pj6pgNUIwFaLksEnQG691gJ4VpoduSSk1ttotK2lrk1EhNdUTXQL2FuxrgMuEj4RjkCoQb45YJFb3kwrP4q%2FL4i%2BjwIQv821tpv2DGKuf6Xv3eOSwKgNh1yxw4lck%2BjetEn%2F%2FdbXO7RE33vUgCnU9ouGK6yNovMXlrj&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuEAL3Qv10MwO19w7v9JOpwSKyweNdb8b0Kgekb5KoE%2FDqvzx1ZnAENeDkSmKm98XKj5qtZ8t2XtsXgrC2OJWVJwLuECrwsKnhMEQvvyWkgO8UAZWd9nN0pj6pgNUIwFaLksEnQG691gJ4VpoduSSk1ttotK2lrk1EhNdUTXQL2FuxrgMuEj4RjkCoQb45YJFb3kwrP4q%2FL4i%2BjwIQv821tpv2DGKuf6Xv3eOSwKgNh1yxw4lck%2BjetEn%2F%2FdbXO7RE33vUgCnU9ouGK6yNovMXlrj&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV&existing_fsm_id=ba_iomcUkLXJu6vz0cX&host=localhost&offchain_tx=tx_%2BNILAfiEuEAL3Qv10MwO19w7v9JOpwSKyweNdb8b0Kgekb5KoE%2FDqvzx1ZnAENeDkSmKm98XKj5qtZ8t2XtsXgrC2OJWVJwLuECrwsKnhMEQvvyWkgO8UAZWd9nN0pj6pgNUIwFaLksEnQG691gJ4VpoduSSk1ttotK2lrk1EhNdUTXQL2FuxrgMuEj4RjkCoQb45YJFb3kwrP4q%2FL4i%2BjwIQv821tpv2DGKuf6Xv3eOSwKgNh1yxw4lck%2BjetEn%2F%2FdbXO7RE33vUgCnU9ouGK6yNovMXlrj&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV&existing_fsm_id=ba_tDMfdPjC9KUJrugJL58lPZ9eJnJ7seQvUXRTcuwVLK0w%2FbaD&host=localhost&offchain_tx=tx_%2BNILAfiEuEAL3Qv10MwO19w7v9JOpwSKyweNdb8b0Kgekb5KoE%2FDqvzx1ZnAENeDkSmKm98XKj5qtZ8t2XtsXgrC2OJWVJwLuECrwsKnhMEQvvyWkgO8UAZWd9nN0pj6pgNUIwFaLksEnQG691gJ4VpoduSSk1ttotK2lrk1EhNdUTXQL2FuxrgMuEj4RjkCoQb45YJFb3kwrP4q%2FL4i%2BjwIQv821tpv2DGKuf6Xv3eOSwKgNh1yxw4lck%2BjetEn%2F%2FdbXO7RE33vUgCnU9ouGK6yNovMXlrj&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV&existing_fsm_id=ba_q7iC%2FfId3vqQOxzNba%2FV6XYN7xKqYGI6TYMAv11HPIBAYLdw&offchain_tx=tx_%2BNILAfiEuEAL3Qv10MwO19w7v9JOpwSKyweNdb8b0Kgekb5KoE%2FDqvzx1ZnAENeDkSmKm98XKj5qtZ8t2XtsXgrC2OJWVJwLuECrwsKnhMEQvvyWkgO8UAZWd9nN0pj6pgNUIwFaLksEnQG691gJ4VpoduSSk1ttotK2lrk1EhNdUTXQL2FuxrgMuEj4RjkCoQb45YJFb3kwrP4q%2FL4i%2BjwIQv821tpv2DGKuf6Xv3eOSwKgNh1yxw4lck%2BjetEn%2F%2FdbXO7RE33vUgCnU9ouGK6yNovMXlrj&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_q7iC/fId3vqQOxzNba/V6XYN7xKqYGI6TYMAv11HPIBAYLdw"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBvjlgkVveTCs/ir8viL6PAhC/zbW2m/YMYq5/pe/d45LoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoY2kdavv/6GG0jrV+ACAIYSMJzlQAAB7tWPDQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422999,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEB44LaWbzjDpsZWtM/2dFaOY4kHTLmUiPMwDUM2e9ko6SG1wyxjyGm0m45ms+8PNaUORpCidSO0LHSyehQNS7AKuF/4XTUBoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOS6EBS/jO5UGWg32L0vdFXoVxcYcJUTd0aWCtT79BCq7KqZqGNpHWr7/+hhtI61fgAgCGEjCc5UAAAUWMx2o="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
  "id": -576460752303422999,
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEB44LaWbzjDpsZWtM/2dFaOY4kHTLmUiPMwDUM2e9ko6SG1wyxjyGm0m45ms+8PNaUORpCidSO0LHSyehQNS7AKuF/4XTUBoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOS6EBS/jO5UGWg32L0vdFXoVxcYcJUTd0aWCtT79BCq7KqZqGNpHWr7/+hhtI61fgAgCGEjCc5UAAAUWMx2o=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422998,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBCxECnTRKR3fo2S4KNnpBVe8kxVgfQnbYtini3kYtF75VoNqeF4hFhq4+IneSkSoP8Xx0MNppuLDJ+6NgsSCQJuEB44LaWbzjDpsZWtM/2dFaOY4kHTLmUiPMwDUM2e9ko6SG1wyxjyGm0m45ms+8PNaUORpCidSO0LHSyehQNS7AKuF/4XTUBoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOS6EBS/jO5UGWg32L0vdFXoVxcYcJUTd0aWCtT79BCq7KqZqGNpHWr7/+hhtI61fgAgCGEjCc5UAAAVlJ/7Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
  "id": -576460752303422998,
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBCxECnTRKR3fo2S4KNnpBVe8kxVgfQnbYtini3kYtF75VoNqeF4hFhq4+IneSkSoP8Xx0MNppuLDJ+6NgsSCQJuEB44LaWbzjDpsZWtM/2dFaOY4kHTLmUiPMwDUM2e9ko6SG1wyxjyGm0m45ms+8PNaUORpCidSO0LHSyehQNS7AKuF/4XTUBoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOS6EBS/jO5UGWg32L0vdFXoVxcYcJUTd0aWCtT79BCq7KqZqGNpHWr7/+hhtI61fgAgCGEjCc5UAAAVlJ/7Q=",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBCxECnTRKR3fo2S4KNnpBVe8kxVgfQnbYtini3kYtF75VoNqeF4hFhq4+IneSkSoP8Xx0MNppuLDJ+6NgsSCQJuEB44LaWbzjDpsZWtM/2dFaOY4kHTLmUiPMwDUM2e9ko6SG1wyxjyGm0m45ms+8PNaUORpCidSO0LHSyehQNS7AKuF/4XTUBoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOS6EBS/jO5UGWg32L0vdFXoVxcYcJUTd0aWCtT79BCq7KqZqGNpHWr7/+hhtI61fgAgCGEjCc5UAAAVlJ/7Q=",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBCxECnTRKR3fo2S4KNnpBVe8kxVgfQnbYtini3kYtF75VoNqeF4hFhq4+IneSkSoP8Xx0MNppuLDJ+6NgsSCQJuEB44LaWbzjDpsZWtM/2dFaOY4kHTLmUiPMwDUM2e9ko6SG1wyxjyGm0m45ms+8PNaUORpCidSO0LHSyehQNS7AKuF/4XTUBoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOS6EBS/jO5UGWg32L0vdFXoVxcYcJUTd0aWCtT79BCq7KqZqGNpHWr7/+hhtI61fgAgCGEjCc5UAAAVlJ/7Q=",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBCxECnTRKR3fo2S4KNnpBVe8kxVgfQnbYtini3kYtF75VoNqeF4hFhq4+IneSkSoP8Xx0MNppuLDJ+6NgsSCQJuEB44LaWbzjDpsZWtM/2dFaOY4kHTLmUiPMwDUM2e9ko6SG1wyxjyGm0m45ms+8PNaUORpCidSO0LHSyehQNS7AKuF/4XTUBoQb45YJFb3kwrP4q/L4i+jwIQv821tpv2DGKuf6Xv3eOS6EBS/jO5UGWg32L0vdFXoVxcYcJUTd0aWCtT79BCq7KqZqGNpHWr7/+hhtI61fgAgCGEjCc5UAAAVlJ/7Q=",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
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
    "channel_id": "ch_2tcjCPhdVmUorBQH34SF3BuXY14v3t7YZMGnMckoqdSRc1GqYV",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator closes WebSocket connection
```

```
