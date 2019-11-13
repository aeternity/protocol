
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
      "fsm_id": "ba_MShI5xsbV3B5/QdhZDScP7Zo0FLjFRFQL35nBwDXNqkZxC+h"
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
      "fsm_id": "ba_Oa289vb2cNGzEMZ8EjvhP7JbOShOuAI027ySbfKiMAh+ug1r"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAZxDM9BiTzFpS5hy+lom7XXexvNUoE4C7mSKujTfKLPLhj+qJSJgAKEBS/jO5UGWg32L0vdFXoVxcYcJUTd0aWCtT79BCq7KqZqGJGE5yoAAAgoAhhAGeddIAMCgGLhuErzxBZ2xsoxOkYB+IYb24CHBcl28KSToXkG/rEsEJSlZ5g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422997,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAuu0CkraMGoVH2Y8sF+fv6KCNgLkXWo/m9GrtXf0PCh3X3ysSxRkFVqPnsJPswyWdJ3mc4NSqnCE/N2lVK4SQPuIP4gTIBoQGcQzPQYk8xaUuYcvpaJu113sbzVKBOAu5kiro03yizy4Y/qiUiYAChAUv4zuVBloN9i9L3RV6FcXGHCVE3dGlgrU+/QQquyqmahiRhOcqAAAIKAIYQBnnXSADAoBi4bhK88QWdsbKMTpGAfiGG9uAhwXJdvCkk6F5Bv6xLBBRQF7Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422997,
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
      "signed_tx": "tx_+MsLAfhCuEAuu0CkraMGoVH2Y8sF+fv6KCNgLkXWo/m9GrtXf0PCh3X3ysSxRkFVqPnsJPswyWdJ3mc4NSqnCE/N2lVK4SQPuIP4gTIBoQGcQzPQYk8xaUuYcvpaJu113sbzVKBOAu5kiro03yizy4Y/qiUiYAChAUv4zuVBloN9i9L3RV6FcXGHCVE3dGlgrU+/QQquyqmahiRhOcqAAAIKAIYQBnnXSADAoBi4bhK88QWdsbKMTpGAfiGG9uAhwXJdvCkk6F5Bv6xLBBRQF7Q=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422996,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhALrtApK2jBqFR9mPLBfn7+igjYC5F1qP5vRq7V39Dwod198rEsUZBVaj57CT7MMlnSd5nODUqpwhPzdpVSuEkD7hA74BMrFZ3IMFdHmL7rIFDYsjUnayIOzYaz4uL0Xri3Ec4MyxBaheyEZIfS/5SZFd3qoylS7AQyLQ2c56e2U+3BLiD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwQNOr3f"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422996,
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhALrtApK2jBqFR9mPLBfn7+igjYC5F1qP5vRq7V39Dwod198rEsUZBVaj57CT7MMlnSd5nODUqpwhPzdpVSuEkD7hA74BMrFZ3IMFdHmL7rIFDYsjUnayIOzYaz4uL0Xri3Ec4MyxBaheyEZIfS/5SZFd3qoylS7AQyLQ2c56e2U+3BLiD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwQNOr3f",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhALrtApK2jBqFR9mPLBfn7+igjYC5F1qP5vRq7V39Dwod198rEsUZBVaj57CT7MMlnSd5nODUqpwhPzdpVSuEkD7hA74BMrFZ3IMFdHmL7rIFDYsjUnayIOzYaz4uL0Xri3Ec4MyxBaheyEZIfS/5SZFd3qoylS7AQyLQ2c56e2U+3BLiD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwQNOr3f",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALrtApK2jBqFR9mPLBfn7+igjYC5F1qP5vRq7V39Dwod198rEsUZBVaj57CT7MMlnSd5nODUqpwhPzdpVSuEkD7hA74BMrFZ3IMFdHmL7rIFDYsjUnayIOzYaz4uL0Xri3Ec4MyxBaheyEZIfS/5SZFd3qoylS7AQyLQ2c56e2U+3BLiD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwQNOr3f",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALrtApK2jBqFR9mPLBfn7+igjYC5F1qP5vRq7V39Dwod198rEsUZBVaj57CT7MMlnSd5nODUqpwhPzdpVSuEkD7hA74BMrFZ3IMFdHmL7rIFDYsjUnayIOzYaz4uL0Xri3Ec4MyxBaheyEZIfS/5SZFd3qoylS7AQyLQ2c56e2U+3BLiD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwQNOr3f",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "message": {
        "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "message": {
        "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
  "id": -576460752303422995,
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
  "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
  "id": -576460752303422995,
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "state": "tx_+QENCwH4hLhALrtApK2jBqFR9mPLBfn7+igjYC5F1qP5vRq7V39Dwod198rEsUZBVaj57CT7MMlnSd5nODUqpwhPzdpVSuEkD7hA74BMrFZ3IMFdHmL7rIFDYsjUnayIOzYaz4uL0Xri3Ec4MyxBaheyEZIfS/5SZFd3qoylS7AQyLQ2c56e2U+3BLiD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwQNOr3f"
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "state": "tx_+QENCwH4hLhALrtApK2jBqFR9mPLBfn7+igjYC5F1qP5vRq7V39Dwod198rEsUZBVaj57CT7MMlnSd5nODUqpwhPzdpVSuEkD7hA74BMrFZ3IMFdHmL7rIFDYsjUnayIOzYaz4uL0Xri3Ec4MyxBaheyEZIfS/5SZFd3qoylS7AQyLQ2c56e2U+3BLiD+IEyAaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGP6olImAAoQFL+M7lQZaDfYvS90VehXFxhwlRN3RpYK1Pv0EKrsqpmoYkYTnKgAACCgCGEAZ510gAwKAYuG4SvPEFnbGyjE6RgH4hhvbgIcFyXbwpJOheQb+sSwQNOr3f"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH",
    "to": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpc7xV2jC/0yamDfE+jj7O9nYGJmdvOCGbK768YGFCaBAqD9zzYUR6Hz6z6ha9fe3/DVyfSWU54QCc//PaXpwEIJf++04GE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH",
          "op": "OffChainTransfer",
          "to": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR"
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBwYokLNEulidrRNxcj3LzFgAg4X35UNenDEmPJv0ZXUZ4EDKxbAOKQeWH9PohPF69Ifc+kJkbaaQZmsvCJLyIFuEj4RjkCoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgQKg/c82FEeh8+s+oWvX3t/w1cn0llOeEAnP/z2l6cBCCX+37/dJ"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
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
    "from": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH",
    "to": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpc7xV2jC/0yamDfE+jj7O9nYGJmdvOCGbK768YGFCaBAqD9zzYUR6Hz6z6ha9fe3/DVyfSWU54QCc//PaXpwEIJf++04GE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_aTbpjyMhsjMQTBXkUTVUkEQQavxRi1nJsKfyKt51a55wLQJcH",
          "op": "OffChainTransfer",
          "to": "ak_2BpWw5VjvKXCqn2JVaUcxm8oWHKBn3PUupzxpKXHSrECrzRWNR"
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBky8hF61oNboNS18CaA/zX1ZtglwhnsZJRDonHQeG3SARzkeiATfTbTbabXhYj7cdDUkOevCRrcW9c2tj4HuMJuEBwYokLNEulidrRNxcj3LzFgAg4X35UNenDEmPJv0ZXUZ4EDKxbAOKQeWH9PohPF69Ifc+kJkbaaQZmsvCJLyIFuEj4RjkCoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgQKg/c82FEeh8+s+oWvX3t/w1cn0llOeEAnP/z2l6cBCCX/qyy6Y"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "state": "tx_+NILAfiEuEBky8hF61oNboNS18CaA/zX1ZtglwhnsZJRDonHQeG3SARzkeiATfTbTbabXhYj7cdDUkOevCRrcW9c2tj4HuMJuEBwYokLNEulidrRNxcj3LzFgAg4X35UNenDEmPJv0ZXUZ4EDKxbAOKQeWH9PohPF69Ifc+kJkbaaQZmsvCJLyIFuEj4RjkCoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgQKg/c82FEeh8+s+oWvX3t/w1cn0llOeEAnP/z2l6cBCCX/qyy6Y"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2&host=localhost&offchain_tx=tx_%2BNILAfiEuEBky8hF61oNboNS18CaA%2FzX1ZtglwhnsZJRDonHQeG3SARzkeiATfTbTbabXhYj7cdDUkOevCRrcW9c2tj4HuMJuEBwYokLNEulidrRNxcj3LzFgAg4X35UNenDEmPJv0ZXUZ4EDKxbAOKQeWH9PohPF69Ifc%2BkJkbaaQZmsvCJLyIFuEj4RjkCoQaXO8Vdowv9Mmpg3xPo4%2BzvZ2BiZnbzghmyu%2BvGBhQmgQKg%2Fc82FEeh8%2Bs%2BoWvX3t%2Fw1cn0llOeEAnP%2Fz2l6cBCCX%2Fqyy6Y&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
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

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuEBky8hF61oNboNS18CaA%2FzX1ZtglwhnsZJRDonHQeG3SARzkeiATfTbTbabXhYj7cdDUkOevCRrcW9c2tj4HuMJuEBwYokLNEulidrRNxcj3LzFgAg4X35UNenDEmPJv0ZXUZ4EDKxbAOKQeWH9PohPF69Ifc%2BkJkbaaQZmsvCJLyIFuEj4RjkCoQaXO8Vdowv9Mmpg3xPo4%2BzvZ2BiZnbzghmyu%2BvGBhQmgQKg%2Fc82FEeh8%2Bs%2BoWvX3t%2Fw1cn0llOeEAnP%2Fz2l6cBCCX%2Fqyy6Y&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
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

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2&existing_fsm_id=ba_6QeHE7BAb1fL8tx4&host=localhost&offchain_tx=tx_%2BNILAfiEuEBky8hF61oNboNS18CaA%2FzX1ZtglwhnsZJRDonHQeG3SARzkeiATfTbTbabXhYj7cdDUkOevCRrcW9c2tj4HuMJuEBwYokLNEulidrRNxcj3LzFgAg4X35UNenDEmPJv0ZXUZ4EDKxbAOKQeWH9PohPF69Ifc%2BkJkbaaQZmsvCJLyIFuEj4RjkCoQaXO8Vdowv9Mmpg3xPo4%2BzvZ2BiZnbzghmyu%2BvGBhQmgQKg%2Fc82FEeh8%2Bs%2BoWvX3t%2Fw1cn0llOeEAnP%2Fz2l6cBCCX%2Fqyy6Y&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
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

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2&existing_fsm_id=ba_Qqp%2BoQafP00MWxWqDzNeGOUPLcjRzB3%2BSWCGXkVPwNqmROIO&host=localhost&offchain_tx=tx_%2BNILAfiEuEBky8hF61oNboNS18CaA%2FzX1ZtglwhnsZJRDonHQeG3SARzkeiATfTbTbabXhYj7cdDUkOevCRrcW9c2tj4HuMJuEBwYokLNEulidrRNxcj3LzFgAg4X35UNenDEmPJv0ZXUZ4EDKxbAOKQeWH9PohPF69Ifc%2BkJkbaaQZmsvCJLyIFuEj4RjkCoQaXO8Vdowv9Mmpg3xPo4%2BzvZ2BiZnbzghmyu%2BvGBhQmgQKg%2Fc82FEeh8%2Bs%2BoWvX3t%2Fw1cn0llOeEAnP%2Fz2l6cBCCX%2Fqyy6Y&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
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

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2&existing_fsm_id=ba_MShI5xsbV3B5%2FQdhZDScP7Zo0FLjFRFQL35nBwDXNqkZxC%2Bh&host=localhost&offchain_tx=tx_%2BNILAfiEuEBky8hF61oNboNS18CaA%2FzX1ZtglwhnsZJRDonHQeG3SARzkeiATfTbTbabXhYj7cdDUkOevCRrcW9c2tj4HuMJuEBwYokLNEulidrRNxcj3LzFgAg4X35UNenDEmPJv0ZXUZ4EDKxbAOKQeWH9PohPF69Ifc%2BkJkbaaQZmsvCJLyIFuEj4RjkCoQaXO8Vdowv9Mmpg3xPo4%2BzvZ2BiZnbzghmyu%2BvGBhQmgQKg%2Fc82FEeh8%2Bs%2BoWvX3t%2Fw1cn0llOeEAnP%2Fz2l6cBCCX%2Fqyy6Y&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_MShI5xsbV3B5/QdhZDScP7Zo0FLjFRFQL35nBwDXNqkZxC+h"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBpc7xV2jC/0yamDfE+jj7O9nYGJmdvOCGbK768YGFCaBoQGcQzPQYk8xaUuYcvpaJu113sbzVKBOAu5kiro03yizy4Y2kdavwACGG0jrV+AAAIYSMJzlQAAFrO8Pig==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422994,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBo+o7rHk8S1+iunDu5okz5OqiO72xPa0CQfPx9f9xVILXq0P47KQmBJ+Rf4tzZb2RE6r/bGLzUhoFatv6C7CIOuF/4XTUBoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGNpHWr8AAhhtI61fgAACGEjCc5UAABY25Lzw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
  "id": -576460752303422994,
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBo+o7rHk8S1+iunDu5okz5OqiO72xPa0CQfPx9f9xVILXq0P47KQmBJ+Rf4tzZb2RE6r/bGLzUhoFatv6C7CIOuF/4XTUBoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGNpHWr8AAhhtI61fgAACGEjCc5UAABY25Lzw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422993,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBo+o7rHk8S1+iunDu5okz5OqiO72xPa0CQfPx9f9xVILXq0P47KQmBJ+Rf4tzZb2RE6r/bGLzUhoFatv6C7CIOuEDwePBEMShsLZmbsIDUZ3rLKc7Rtkk3d/fAe+ij5hpF+5qtorM0gy/l30B0bKHaNLIv+ImzqyNCfJs1vSw9gEUCuF/4XTUBoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGNpHWr8AAhhtI61fgAACGEjCc5UAABSuWPyE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
  "id": -576460752303422993,
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBo+o7rHk8S1+iunDu5okz5OqiO72xPa0CQfPx9f9xVILXq0P47KQmBJ+Rf4tzZb2RE6r/bGLzUhoFatv6C7CIOuEDwePBEMShsLZmbsIDUZ3rLKc7Rtkk3d/fAe+ij5hpF+5qtorM0gy/l30B0bKHaNLIv+ImzqyNCfJs1vSw9gEUCuF/4XTUBoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGNpHWr8AAhhtI61fgAACGEjCc5UAABSuWPyE=",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBo+o7rHk8S1+iunDu5okz5OqiO72xPa0CQfPx9f9xVILXq0P47KQmBJ+Rf4tzZb2RE6r/bGLzUhoFatv6C7CIOuEDwePBEMShsLZmbsIDUZ3rLKc7Rtkk3d/fAe+ij5hpF+5qtorM0gy/l30B0bKHaNLIv+ImzqyNCfJs1vSw9gEUCuF/4XTUBoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGNpHWr8AAhhtI61fgAACGEjCc5UAABSuWPyE=",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBo+o7rHk8S1+iunDu5okz5OqiO72xPa0CQfPx9f9xVILXq0P47KQmBJ+Rf4tzZb2RE6r/bGLzUhoFatv6C7CIOuEDwePBEMShsLZmbsIDUZ3rLKc7Rtkk3d/fAe+ij5hpF+5qtorM0gy/l30B0bKHaNLIv+ImzqyNCfJs1vSw9gEUCuF/4XTUBoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGNpHWr8AAhhtI61fgAACGEjCc5UAABSuWPyE=",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBo+o7rHk8S1+iunDu5okz5OqiO72xPa0CQfPx9f9xVILXq0P47KQmBJ+Rf4tzZb2RE6r/bGLzUhoFatv6C7CIOuEDwePBEMShsLZmbsIDUZ3rLKc7Rtkk3d/fAe+ij5hpF+5qtorM0gy/l30B0bKHaNLIv+ImzqyNCfJs1vSw9gEUCuF/4XTUBoQaXO8Vdowv9Mmpg3xPo4+zvZ2BiZnbzghmyu+vGBhQmgaEBnEMz0GJPMWlLmHL6Wibtdd7G81SgTgLuZIq6NN8os8uGNpHWr8AAhhtI61fgAACGEjCc5UAABSuWPyE=",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
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
    "channel_id": "ch_29c4GKUN826tHZWhDVHNei5agHK8fP4DHsvXtjTWEqV2dkjaJ2",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder closes WebSocket connection
```

```
