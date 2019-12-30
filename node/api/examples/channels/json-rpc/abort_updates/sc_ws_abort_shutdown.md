
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
      "fsm_id": "ba_WCeR03UEfOYP2AwUC3QNR7zp3Xux5zHIGM6NgR8VgkXfjcZP"
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
      "fsm_id": "ba_jZHUYMzzu6hrXVPFBXCDsjrsGiKwwJqoyIlFdwsfVRRCldVB"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4908nh7w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422862,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEC2RXPKYpPX8vtV6k0pVy1DOTYhF9Jm6Y36Rx1PuJZJV4FzVP50lDXdHr3KZ3jGyFIg69Rl79XQ1I/UohM+opcNuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uPZSgu0I="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422862,
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
      "signed_tx": "tx_+MsLAfhCuEC2RXPKYpPX8vtV6k0pVy1DOTYhF9Jm6Y36Rx1PuJZJV4FzVP50lDXdHr3KZ3jGyFIg69Rl79XQ1I/UohM+opcNuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uPZSgu0I=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422861,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAUSd/dV+6aSFNO5nzNEtgnNV3yKD4kF6aDAwWxVNUMiW9jrlCXTfmU/IGmSgntrwKXFPi4J1Mz9XMUtKmnSSlC7hAtkVzymKT1/L7VepNKVctQzk2IRfSZumN+kcdT7iWSVeBc1T+dJQ13R69ymd4xshSIOvUZe/V0NSP1KITPqKXDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j1w8a8A"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422861,
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAUSd/dV+6aSFNO5nzNEtgnNV3yKD4kF6aDAwWxVNUMiW9jrlCXTfmU/IGmSgntrwKXFPi4J1Mz9XMUtKmnSSlC7hAtkVzymKT1/L7VepNKVctQzk2IRfSZumN+kcdT7iWSVeBc1T+dJQ13R69ymd4xshSIOvUZe/V0NSP1KITPqKXDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j1w8a8A",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAUSd/dV+6aSFNO5nzNEtgnNV3yKD4kF6aDAwWxVNUMiW9jrlCXTfmU/IGmSgntrwKXFPi4J1Mz9XMUtKmnSSlC7hAtkVzymKT1/L7VepNKVctQzk2IRfSZumN+kcdT7iWSVeBc1T+dJQ13R69ymd4xshSIOvUZe/V0NSP1KITPqKXDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j1w8a8A",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAUSd/dV+6aSFNO5nzNEtgnNV3yKD4kF6aDAwWxVNUMiW9jrlCXTfmU/IGmSgntrwKXFPi4J1Mz9XMUtKmnSSlC7hAtkVzymKT1/L7VepNKVctQzk2IRfSZumN+kcdT7iWSVeBc1T+dJQ13R69ymd4xshSIOvUZe/V0NSP1KITPqKXDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j1w8a8A",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAUSd/dV+6aSFNO5nzNEtgnNV3yKD4kF6aDAwWxVNUMiW9jrlCXTfmU/IGmSgntrwKXFPi4J1Mz9XMUtKmnSSlC7hAtkVzymKT1/L7VepNKVctQzk2IRfSZumN+kcdT7iWSVeBc1T+dJQ13R69ymd4xshSIOvUZe/V0NSP1KITPqKXDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j1w8a8A",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "message": {
        "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "message": {
        "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
  "id": -576460752303422860,
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
  "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
  "id": -576460752303422860,
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "state": "tx_+QENCwH4hLhAUSd/dV+6aSFNO5nzNEtgnNV3yKD4kF6aDAwWxVNUMiW9jrlCXTfmU/IGmSgntrwKXFPi4J1Mz9XMUtKmnSSlC7hAtkVzymKT1/L7VepNKVctQzk2IRfSZumN+kcdT7iWSVeBc1T+dJQ13R69ymd4xshSIOvUZe/V0NSP1KITPqKXDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j1w8a8A"
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "state": "tx_+QENCwH4hLhAUSd/dV+6aSFNO5nzNEtgnNV3yKD4kF6aDAwWxVNUMiW9jrlCXTfmU/IGmSgntrwKXFPi4J1Mz9XMUtKmnSSlC7hAtkVzymKT1/L7VepNKVctQzk2IRfSZumN+kcdT7iWSVeBc1T+dJQ13R69ymd4xshSIOvUZe/V0NSP1KITPqKXDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j1w8a8A"
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBsgfIiUnuHH3f7Fx3yy/GhAJ9WbW/UT8DpCuJUxCWgwwoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY2kdavv/+GG0jrV+ABAIYSMJzlQAA+8S0Tcg==",
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
  "method": "channels.shutdown_sign",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBsgfIiUnuHH3f7Fx3yy/GhAJ9WbW/UT8DpCuJUxCWgwwoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY2kdavv/+GG0jrV+ABAIYSMJzlQAAXQXqmyw==",
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
  "method": "channels.shutdown_sign",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBsgfIiUnuHH3f7Fx3yy/GhAJ9WbW/UT8DpCuJUxCWgwwoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY2kdavv/+GG0jrV+ABAIYSMJzlQAA+8S0Tcg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422859,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEB1CH+NIXZ5/xNK8eKT0kuHipdbBm808Utw54FHE8cS01Tc8MU+NbqVTP46V8LGUebTAD+lj4nvcNFoXDBL/ggFuF/4XTUBoQbIHyIlJ7hx93+xcd8svxoQCfVm1v1E/A6QriVMQloMMKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAPvHAcQs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
  "id": -576460752303422859,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
      "method": "channels.shutdown_sign",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEB1CH+NIXZ5/xNK8eKT0kuHipdbBm808Utw54FHE8cS01Tc8MU+NbqVTP46V8LGUebTAD+lj4nvcNFoXDBL/ggFuF/4XTUBoQbIHyIlJ7hx93+xcd8svxoQCfVm1v1E/A6QriVMQloMMKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAPvHAcQs=",
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
  "method": "channels.shutdown_sign_ack",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
    "data": {
      "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
  "id": -576460752303422858,
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
  "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
  "id": -576460752303422858,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422857,
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
    "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
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
  "channel_id": "ch_2X8qcE5YqtXdLmvx2cnFvSUUe5LYoJnAxA5iu1qhSEyZsb26f5",
  "id": -576460752303422857,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
