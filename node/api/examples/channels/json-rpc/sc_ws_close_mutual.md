
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
      "fsm_id": "ba_nRo1PVJGv2uTvI1AAIjbEA4yEMg2ZjF6toOv8oN/+zfHF+qO"
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
      "fsm_id": "ba_x4JPjDAlJwSv6FLJ5ugsTxqm6ZIxd0NyY4SbTrTtoI7DBSRn"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4JDImxtQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423311,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBPsKgBl5v9R7vzMbMc4aePS3xTCLEWlhFrIwCV0O8WBVZzfZZ2dqsSd2lGY9td2Oc6qluoHumGoX/UzXMvOpgHuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uCZZ7XVs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423311,
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
      "signed_tx": "tx_+MsLAfhCuEBPsKgBl5v9R7vzMbMc4aePS3xTCLEWlhFrIwCV0O8WBVZzfZZ2dqsSd2lGY9td2Oc6qluoHumGoX/UzXMvOpgHuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uCZZ7XVs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423310,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAB+OY6IAdv+QoDM/X+f+sGxHKPTAwwOp6vO1Oqp27UQBojOyzSCkGFNlHIdRiVQZjFDsH+6GJloeO0MJCfpQdBLhAT7CoAZeb/Ue78zGzHOGnj0t8UwixFpYRayMAldDvFgVWc32WdnarEndpRmPbXdjnOqpbqB7phqF/1M1zLzqYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gn7wOHr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423310,
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAB+OY6IAdv+QoDM/X+f+sGxHKPTAwwOp6vO1Oqp27UQBojOyzSCkGFNlHIdRiVQZjFDsH+6GJloeO0MJCfpQdBLhAT7CoAZeb/Ue78zGzHOGnj0t8UwixFpYRayMAldDvFgVWc32WdnarEndpRmPbXdjnOqpbqB7phqF/1M1zLzqYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gn7wOHr",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAB+OY6IAdv+QoDM/X+f+sGxHKPTAwwOp6vO1Oqp27UQBojOyzSCkGFNlHIdRiVQZjFDsH+6GJloeO0MJCfpQdBLhAT7CoAZeb/Ue78zGzHOGnj0t8UwixFpYRayMAldDvFgVWc32WdnarEndpRmPbXdjnOqpbqB7phqF/1M1zLzqYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gn7wOHr",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAB+OY6IAdv+QoDM/X+f+sGxHKPTAwwOp6vO1Oqp27UQBojOyzSCkGFNlHIdRiVQZjFDsH+6GJloeO0MJCfpQdBLhAT7CoAZeb/Ue78zGzHOGnj0t8UwixFpYRayMAldDvFgVWc32WdnarEndpRmPbXdjnOqpbqB7phqF/1M1zLzqYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gn7wOHr",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAB+OY6IAdv+QoDM/X+f+sGxHKPTAwwOp6vO1Oqp27UQBojOyzSCkGFNlHIdRiVQZjFDsH+6GJloeO0MJCfpQdBLhAT7CoAZeb/Ue78zGzHOGnj0t8UwixFpYRayMAldDvFgVWc32WdnarEndpRmPbXdjnOqpbqB7phqF/1M1zLzqYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gn7wOHr",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "message": {
        "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "message": {
        "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
  "id": -576460752303423309,
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
  "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
  "id": -576460752303423309,
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "state": "tx_+QENCwH4hLhAB+OY6IAdv+QoDM/X+f+sGxHKPTAwwOp6vO1Oqp27UQBojOyzSCkGFNlHIdRiVQZjFDsH+6GJloeO0MJCfpQdBLhAT7CoAZeb/Ue78zGzHOGnj0t8UwixFpYRayMAldDvFgVWc32WdnarEndpRmPbXdjnOqpbqB7phqF/1M1zLzqYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gn7wOHr"
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "state": "tx_+QENCwH4hLhAB+OY6IAdv+QoDM/X+f+sGxHKPTAwwOp6vO1Oqp27UQBojOyzSCkGFNlHIdRiVQZjFDsH+6GJloeO0MJCfpQdBLhAT7CoAZeb/Ue78zGzHOGnj0t8UwixFpYRayMAldDvFgVWc32WdnarEndpRmPbXdjnOqpbqB7phqF/1M1zLzqYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gn7wOHr"
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBmDaosCpa0xkPMKSlsgXD4U/Ce3mhKds9ICfFF7IYpcKoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY2kdavv/+GG0jrV+ABAIYSMJzlQAAKc4vL7A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423308,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECjciwt1VZljOGgwVjEGW11OHmq9eg4uXUAtm1qOpSnDuqRm4GA0nYQBwqwPm2x3BjHuD84ERhq0iVEnS9vgkwJuF/4XTUBoQZg2qLAqWtMZDzCkpbIFw+FPwnt5oSnbPSAnxReyGKXCqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAACgaMCng="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
  "id": -576460752303423308,
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECjciwt1VZljOGgwVjEGW11OHmq9eg4uXUAtm1qOpSnDuqRm4GA0nYQBwqwPm2x3BjHuD84ERhq0iVEnS9vgkwJuF/4XTUBoQZg2qLAqWtMZDzCkpbIFw+FPwnt5oSnbPSAnxReyGKXCqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAACgaMCng=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423307,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAuJHNVUdGEEDg48JCpOacWsxthAUxK1RAFtqWoREYm6cLxvgMlJ9veGjNtTnuQ607hjq8QQaerjig5OdS0DfwCuECjciwt1VZljOGgwVjEGW11OHmq9eg4uXUAtm1qOpSnDuqRm4GA0nYQBwqwPm2x3BjHuD84ERhq0iVEnS9vgkwJuF/4XTUBoQZg2qLAqWtMZDzCkpbIFw+FPwnt5oSnbPSAnxReyGKXCqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAACtvLI1Q="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
  "id": -576460752303423307,
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAuJHNVUdGEEDg48JCpOacWsxthAUxK1RAFtqWoREYm6cLxvgMlJ9veGjNtTnuQ607hjq8QQaerjig5OdS0DfwCuECjciwt1VZljOGgwVjEGW11OHmq9eg4uXUAtm1qOpSnDuqRm4GA0nYQBwqwPm2x3BjHuD84ERhq0iVEnS9vgkwJuF/4XTUBoQZg2qLAqWtMZDzCkpbIFw+FPwnt5oSnbPSAnxReyGKXCqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAACtvLI1Q=",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAuJHNVUdGEEDg48JCpOacWsxthAUxK1RAFtqWoREYm6cLxvgMlJ9veGjNtTnuQ607hjq8QQaerjig5OdS0DfwCuECjciwt1VZljOGgwVjEGW11OHmq9eg4uXUAtm1qOpSnDuqRm4GA0nYQBwqwPm2x3BjHuD84ERhq0iVEnS9vgkwJuF/4XTUBoQZg2qLAqWtMZDzCkpbIFw+FPwnt5oSnbPSAnxReyGKXCqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAACtvLI1Q=",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAuJHNVUdGEEDg48JCpOacWsxthAUxK1RAFtqWoREYm6cLxvgMlJ9veGjNtTnuQ607hjq8QQaerjig5OdS0DfwCuECjciwt1VZljOGgwVjEGW11OHmq9eg4uXUAtm1qOpSnDuqRm4GA0nYQBwqwPm2x3BjHuD84ERhq0iVEnS9vgkwJuF/4XTUBoQZg2qLAqWtMZDzCkpbIFw+FPwnt5oSnbPSAnxReyGKXCqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAACtvLI1Q=",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAuJHNVUdGEEDg48JCpOacWsxthAUxK1RAFtqWoREYm6cLxvgMlJ9veGjNtTnuQ607hjq8QQaerjig5OdS0DfwCuECjciwt1VZljOGgwVjEGW11OHmq9eg4uXUAtm1qOpSnDuqRm4GA0nYQBwqwPm2x3BjHuD84ERhq0iVEnS9vgkwJuF/4XTUBoQZg2qLAqWtMZDzCkpbIFw+FPwnt5oSnbPSAnxReyGKXCqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAACtvLI1Q=",
      "type": "channel_close_mutual_tx"
    }
  },
  "version": 1
}
```

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
      "fsm_id": "ba_/Pbqcz5hwc7btD+OH9TQzlM+nNISlF6Zp+ny89cB7pC0TJBW"
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
      "fsm_id": "ba_Lq+tQcrq2ykjmAUv2wDOXALknw7AEZfGK4lVnOgqASv4qzdp"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4L6Ud6iQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423306,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAYTO6iSfvpeh1h5Esshiy4DUkWlNJvt6OQ7Yv5VtYX1hhl0ig2vCfykQ39OGaJ528K8AJZFLYrsD54DKpR7REHuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uC5xvZ8A="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423306,
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
      "signed_tx": "tx_+MsLAfhCuEAYTO6iSfvpeh1h5Esshiy4DUkWlNJvt6OQ7Yv5VtYX1hhl0ig2vCfykQ39OGaJ528K8AJZFLYrsD54DKpR7REHuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uC5xvZ8A=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423305,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAGEzuokn76XodYeRLLIYsuA1JFpTSb7ejkO2L+VbWF9YYZdIoNrwn8pEN/ThmiedvCvACWRS2K7A+eAyqUe0RB7hA4pJaiiCw2VR2UPZCQuZH9uDJH20gLJ4Tvlcp4H1e/95qZA5uJdIuAMS5Pn/HSFalJusj3erlDr3FD7B+EqBKCriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gsdAHHo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423305,
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAGEzuokn76XodYeRLLIYsuA1JFpTSb7ejkO2L+VbWF9YYZdIoNrwn8pEN/ThmiedvCvACWRS2K7A+eAyqUe0RB7hA4pJaiiCw2VR2UPZCQuZH9uDJH20gLJ4Tvlcp4H1e/95qZA5uJdIuAMS5Pn/HSFalJusj3erlDr3FD7B+EqBKCriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gsdAHHo",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAGEzuokn76XodYeRLLIYsuA1JFpTSb7ejkO2L+VbWF9YYZdIoNrwn8pEN/ThmiedvCvACWRS2K7A+eAyqUe0RB7hA4pJaiiCw2VR2UPZCQuZH9uDJH20gLJ4Tvlcp4H1e/95qZA5uJdIuAMS5Pn/HSFalJusj3erlDr3FD7B+EqBKCriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gsdAHHo",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGEzuokn76XodYeRLLIYsuA1JFpTSb7ejkO2L+VbWF9YYZdIoNrwn8pEN/ThmiedvCvACWRS2K7A+eAyqUe0RB7hA4pJaiiCw2VR2UPZCQuZH9uDJH20gLJ4Tvlcp4H1e/95qZA5uJdIuAMS5Pn/HSFalJusj3erlDr3FD7B+EqBKCriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gsdAHHo",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGEzuokn76XodYeRLLIYsuA1JFpTSb7ejkO2L+VbWF9YYZdIoNrwn8pEN/ThmiedvCvACWRS2K7A+eAyqUe0RB7hA4pJaiiCw2VR2UPZCQuZH9uDJH20gLJ4Tvlcp4H1e/95qZA5uJdIuAMS5Pn/HSFalJusj3erlDr3FD7B+EqBKCriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gsdAHHo",
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
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
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "message": {
        "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jf1PErP6zUSovsdbqtXdTDVFLrhiaDcGxthBtSWrvRNtgFGDg",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "message": {
        "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
  "id": -576460752303423304,
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
  "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
  "id": -576460752303423304,
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "state": "tx_+QENCwH4hLhAGEzuokn76XodYeRLLIYsuA1JFpTSb7ejkO2L+VbWF9YYZdIoNrwn8pEN/ThmiedvCvACWRS2K7A+eAyqUe0RB7hA4pJaiiCw2VR2UPZCQuZH9uDJH20gLJ4Tvlcp4H1e/95qZA5uJdIuAMS5Pn/HSFalJusj3erlDr3FD7B+EqBKCriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gsdAHHo"
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "state": "tx_+QENCwH4hLhAGEzuokn76XodYeRLLIYsuA1JFpTSb7ejkO2L+VbWF9YYZdIoNrwn8pEN/ThmiedvCvACWRS2K7A+eAyqUe0RB7hA4pJaiiCw2VR2UPZCQuZH9uDJH20gLJ4Tvlcp4H1e/95qZA5uJdIuAMS5Pn/HSFalJusj3erlDr3FD7B+EqBKCriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gsdAHHo"
    }
  },
  "version": 1
}
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBkk/qY4HDTElo/cQe4kaX7Z466kS6QzrZGVcT7+9mL/uoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY2kdavv/+GG0jrV+ABAIYSMJzlQAADC9Jj0A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423303,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECzfDmP5wB1EHfHcMEupB5y+RNKaEgZurXQKOdFk69U1itJFj+GaMt3R2iaqTiJuGYFnWLn58wiFsHnxgUb4j8OuF/4XTUBoQZJP6mOBw0xJaP3EHuJGl+2eOupEukM62RlXE+/vZi/7qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGNpHWr7//hhtI61fgAQCGEjCc5UAAA4HodmM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
  "id": -576460752303423303,
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECzfDmP5wB1EHfHcMEupB5y+RNKaEgZurXQKOdFk69U1itJFj+GaMt3R2iaqTiJuGYFnWLn58wiFsHnxgUb4j8OuF/4XTUBoQZJP6mOBw0xJaP3EHuJGl+2eOupEukM62RlXE+/vZi/7qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGNpHWr7//hhtI61fgAQCGEjCc5UAAA4HodmM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423302,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuECgAzU8+VTMBhvMX5thoNyAa/ZO0Mmr/os+r2cNBQOuufZX/VtAzlMiZYyRiuMig8O/cU2oF8gql+JkPqsxyq0CuECzfDmP5wB1EHfHcMEupB5y+RNKaEgZurXQKOdFk69U1itJFj+GaMt3R2iaqTiJuGYFnWLn58wiFsHnxgUb4j8OuF/4XTUBoQZJP6mOBw0xJaP3EHuJGl+2eOupEukM62RlXE+/vZi/7qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGNpHWr7//hhtI61fgAQCGEjCc5UAAA4jZ0SA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
  "id": -576460752303423302,
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECgAzU8+VTMBhvMX5thoNyAa/ZO0Mmr/os+r2cNBQOuufZX/VtAzlMiZYyRiuMig8O/cU2oF8gql+JkPqsxyq0CuECzfDmP5wB1EHfHcMEupB5y+RNKaEgZurXQKOdFk69U1itJFj+GaMt3R2iaqTiJuGYFnWLn58wiFsHnxgUb4j8OuF/4XTUBoQZJP6mOBw0xJaP3EHuJGl+2eOupEukM62RlXE+/vZi/7qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGNpHWr7//hhtI61fgAQCGEjCc5UAAA4jZ0SA=",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECgAzU8+VTMBhvMX5thoNyAa/ZO0Mmr/os+r2cNBQOuufZX/VtAzlMiZYyRiuMig8O/cU2oF8gql+JkPqsxyq0CuECzfDmP5wB1EHfHcMEupB5y+RNKaEgZurXQKOdFk69U1itJFj+GaMt3R2iaqTiJuGYFnWLn58wiFsHnxgUb4j8OuF/4XTUBoQZJP6mOBw0xJaP3EHuJGl+2eOupEukM62RlXE+/vZi/7qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGNpHWr7//hhtI61fgAQCGEjCc5UAAA4jZ0SA=",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECgAzU8+VTMBhvMX5thoNyAa/ZO0Mmr/os+r2cNBQOuufZX/VtAzlMiZYyRiuMig8O/cU2oF8gql+JkPqsxyq0CuECzfDmP5wB1EHfHcMEupB5y+RNKaEgZurXQKOdFk69U1itJFj+GaMt3R2iaqTiJuGYFnWLn58wiFsHnxgUb4j8OuF/4XTUBoQZJP6mOBw0xJaP3EHuJGl+2eOupEukM62RlXE+/vZi/7qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGNpHWr7//hhtI61fgAQCGEjCc5UAAA4jZ0SA=",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECgAzU8+VTMBhvMX5thoNyAa/ZO0Mmr/os+r2cNBQOuufZX/VtAzlMiZYyRiuMig8O/cU2oF8gql+JkPqsxyq0CuECzfDmP5wB1EHfHcMEupB5y+RNKaEgZurXQKOdFk69U1itJFj+GaMt3R2iaqTiJuGYFnWLn58wiFsHnxgUb4j8OuF/4XTUBoQZJP6mOBw0xJaP3EHuJGl+2eOupEukM62RlXE+/vZi/7qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGNpHWr7//hhtI61fgAQCGEjCc5UAAA4jZ0SA=",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
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
    "channel_id": "ch_ZG3H28C9wgXKD2MNHxtgSy2uqRgoysNaY2StJwpYK8qJUu2fh",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
