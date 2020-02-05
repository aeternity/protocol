
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator
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
      "fsm_id": "ba_YHjoTxz2pn7zk2A3tbZiA55LhqGopOwEKu3/w8iP65Rp24ir"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder
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
      "fsm_id": "ba_7y8r6s66XWlE9dhokpvIrp7HuRdNkyy5sYoyKAjgh/ipFj2I"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+47I0LiWQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422883,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDaEOA3tcXJzKB6kuYTz95voQAW7dqMmxGfeg7c3YvfuHao0Ere1vV+Q5z8XYhZBp1xpD4idnsupNfW0zQMkTADuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uO2rMQXI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422883,
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
      "signed_tx": "tx_+MsLAfhCuEDaEOA3tcXJzKB6kuYTz95voQAW7dqMmxGfeg7c3YvfuHao0Ere1vV+Q5z8XYhZBp1xpD4idnsupNfW0zQMkTADuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uO2rMQXI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422882,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhABNFLMGLkDOrFimA9N5BckQ4EIwNOEQv3pGafmxh6GEuLXm9G2zenowirWyNw0kxtnthZmyAL2V+p4nj4ruIpAbhA2hDgN7XFycygepLmE8/eb6EAFu3ajJsRn3oO3N2L37h2qNBK3tb1fkOc/F2IWQadcaQ+InZ7LqTX1tM0DJEwA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jvmIZrn"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422882,
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhABNFLMGLkDOrFimA9N5BckQ4EIwNOEQv3pGafmxh6GEuLXm9G2zenowirWyNw0kxtnthZmyAL2V+p4nj4ruIpAbhA2hDgN7XFycygepLmE8/eb6EAFu3ajJsRn3oO3N2L37h2qNBK3tb1fkOc/F2IWQadcaQ+InZ7LqTX1tM0DJEwA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jvmIZrn",
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhABNFLMGLkDOrFimA9N5BckQ4EIwNOEQv3pGafmxh6GEuLXm9G2zenowirWyNw0kxtnthZmyAL2V+p4nj4ruIpAbhA2hDgN7XFycygepLmE8/eb6EAFu3ajJsRn3oO3N2L37h2qNBK3tb1fkOc/F2IWQadcaQ+InZ7LqTX1tM0DJEwA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jvmIZrn",
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABNFLMGLkDOrFimA9N5BckQ4EIwNOEQv3pGafmxh6GEuLXm9G2zenowirWyNw0kxtnthZmyAL2V+p4nj4ruIpAbhA2hDgN7XFycygepLmE8/eb6EAFu3ajJsRn3oO3N2L37h2qNBK3tb1fkOc/F2IWQadcaQ+InZ7LqTX1tM0DJEwA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jvmIZrn",
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABNFLMGLkDOrFimA9N5BckQ4EIwNOEQv3pGafmxh6GEuLXm9G2zenowirWyNw0kxtnthZmyAL2V+p4nj4ruIpAbhA2hDgN7XFycygepLmE8/eb6EAFu3ajJsRn3oO3N2L37h2qNBK3tb1fkOc/F2IWQadcaQ+InZ7LqTX1tM0DJEwA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jvmIZrn",
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
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "message": {
        "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "message": {
        "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422881,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
  "id": -576460752303422881,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "event": "open"
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "state": "tx_+QENCwH4hLhABNFLMGLkDOrFimA9N5BckQ4EIwNOEQv3pGafmxh6GEuLXm9G2zenowirWyNw0kxtnthZmyAL2V+p4nj4ruIpAbhA2hDgN7XFycygepLmE8/eb6EAFu3ajJsRn3oO3N2L37h2qNBK3tb1fkOc/F2IWQadcaQ+InZ7LqTX1tM0DJEwA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jvmIZrn"
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "state": "tx_+QENCwH4hLhABNFLMGLkDOrFimA9N5BckQ4EIwNOEQv3pGafmxh6GEuLXm9G2zenowirWyNw0kxtnthZmyAL2V+p4nj4ruIpAbhA2hDgN7XFycygepLmE8/eb6EAFu3ajJsRn3oO3N2L37h2qNBK3tb1fkOc/F2IWQadcaQ+InZ7LqTX1tM0DJEwA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jvmIZrn"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBmmlF4WZ9KOya5xsealsB3Og3WL08Qp2mC/BPBiRizSdoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhg/AoHKQAKDzbRVCr+DdkhskLcCBV1D3dvqUhQ5X1avffdiIqRPtFwI88AvelA==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.withdraw_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBmmlF4WZ9KOya5xsealsB3Og3WL08Qp2mC/BPBiRizSdoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEAIAhg/AoHKQAKDlzwAxiXLRRweSA8y8C+7SpRvQR8MYCvXqf+y6juh93QIXfq8CVg==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "method": "channels.withdraw_tx",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBmmlF4WZ9KOya5xsealsB3Og3WL08Qp2mC/BPBiRizSdoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhg/AoHKQAKDzbRVCr+DdkhskLcCBV1D3dvqUhQ5X1avffdiIqRPtFwI88AvelA==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422880,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEC3gZ9ZnKFY3knOYLNeJTJNwfSbCgut9YUBszuDrxxBWJN6VlGdY63RoWHmLfKyZ4H9lq7wwV9p3gyNhXlVDCUMuHT4cjQBoQZppReFmfSjsmucbHmpbAdzoN1i9PEKdpgvwTwYkYs0naEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACg820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCPPi6gTg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
  "id": -576460752303422880,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1018,
        "message": "Not allowed at current channel state"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.withdraw_tx",
      "params": {
        "error": 42
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEC3gZ9ZnKFY3knOYLNeJTJNwfSbCgut9YUBszuDrxxBWJN6VlGdY63RoWHmLfKyZ4H9lq7wwV9p3gyNhXlVDCUMuHT4cjQBoQZppReFmfSjsmucbHmpbAdzoN1i9PEKdpgvwTwYkYs0naEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACg820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCPPi6gTg=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.withdraw_ack",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
      "error_code": 42,
      "error_msg": "unknown",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422879,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
  "id": -576460752303422879,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422878,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "event": "died"
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
    "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oXZJWVx8EW3f4qMoXQfgaFN4Dorj8fbyZoCuZNXmgYZd2MV4b",
  "id": -576460752303422878,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
