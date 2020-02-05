
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
      "fsm_id": "ba_WZEqMXUQATbBJg99XChdH75SHE4ImY8r27vm2HHUkM+vX6s5"
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
      "fsm_id": "ba_VWH5jkEW9YRMTHCC26kl3kbOMwbHks6wIThqn2HsHXm3PIhg"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5GEfCicw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422747,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBoUmlhqjJLyfzAxvVlwdmHrPsHVCeSx8Bl6xFkmg/aZjdasvrxkUbNx3SpYNQi/7vyd9vlb0RcWrTknQFR/UUDuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uRpZa8Ew="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422747,
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
      "signed_tx": "tx_+MsLAfhCuEBoUmlhqjJLyfzAxvVlwdmHrPsHVCeSx8Bl6xFkmg/aZjdasvrxkUbNx3SpYNQi/7vyd9vlb0RcWrTknQFR/UUDuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uRpZa8Ew=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422746,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAMyPdOyKj44B2BIumHdk0Uh03UuzQyMKiSIhIN+QvhqHZ/PeOzMqD3MNQcGRfjiwgcXfq/QL5kzQ7dj711KpMA7hAaFJpYaoyS8n8wMb1ZcHZh6z7B1QnksfAZesRZJoP2mY3WrL68ZFGzcd0qWDUIv+78nfb5W9EXFq05J0BUf1FA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kbOiyw1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422746,
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAMyPdOyKj44B2BIumHdk0Uh03UuzQyMKiSIhIN+QvhqHZ/PeOzMqD3MNQcGRfjiwgcXfq/QL5kzQ7dj711KpMA7hAaFJpYaoyS8n8wMb1ZcHZh6z7B1QnksfAZesRZJoP2mY3WrL68ZFGzcd0qWDUIv+78nfb5W9EXFq05J0BUf1FA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kbOiyw1",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAMyPdOyKj44B2BIumHdk0Uh03UuzQyMKiSIhIN+QvhqHZ/PeOzMqD3MNQcGRfjiwgcXfq/QL5kzQ7dj711KpMA7hAaFJpYaoyS8n8wMb1ZcHZh6z7B1QnksfAZesRZJoP2mY3WrL68ZFGzcd0qWDUIv+78nfb5W9EXFq05J0BUf1FA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kbOiyw1",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAMyPdOyKj44B2BIumHdk0Uh03UuzQyMKiSIhIN+QvhqHZ/PeOzMqD3MNQcGRfjiwgcXfq/QL5kzQ7dj711KpMA7hAaFJpYaoyS8n8wMb1ZcHZh6z7B1QnksfAZesRZJoP2mY3WrL68ZFGzcd0qWDUIv+78nfb5W9EXFq05J0BUf1FA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kbOiyw1",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAMyPdOyKj44B2BIumHdk0Uh03UuzQyMKiSIhIN+QvhqHZ/PeOzMqD3MNQcGRfjiwgcXfq/QL5kzQ7dj711KpMA7hAaFJpYaoyS8n8wMb1ZcHZh6z7B1QnksfAZesRZJoP2mY3WrL68ZFGzcd0qWDUIv+78nfb5W9EXFq05J0BUf1FA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kbOiyw1",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
    "data": {
      "message": {
        "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
    "data": {
      "message": {
        "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
  "id": -576460752303422745,
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
  "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
  "id": -576460752303422745,
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
    "data": {
      "state": "tx_+QENCwH4hLhAMyPdOyKj44B2BIumHdk0Uh03UuzQyMKiSIhIN+QvhqHZ/PeOzMqD3MNQcGRfjiwgcXfq/QL5kzQ7dj711KpMA7hAaFJpYaoyS8n8wMb1ZcHZh6z7B1QnksfAZesRZJoP2mY3WrL68ZFGzcd0qWDUIv+78nfb5W9EXFq05J0BUf1FA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kbOiyw1"
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
    "data": {
      "state": "tx_+QENCwH4hLhAMyPdOyKj44B2BIumHdk0Uh03UuzQyMKiSIhIN+QvhqHZ/PeOzMqD3MNQcGRfjiwgcXfq/QL5kzQ7dj711KpMA7hAaFJpYaoyS8n8wMb1ZcHZh6z7B1QnksfAZesRZJoP2mY3WrL68ZFGzcd0qWDUIv+78nfb5W9EXFq05J0BUf1FA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kbOiyw1"
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
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
      "method": "channels.update",
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
      "method": "channels.update",
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

#### responder ---> node
```javascript
{
  "id": -576460752303422744,
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
  "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
  "id": -576460752303422744,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422743,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
    "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
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
  "channel_id": "ch_tE7dYwesxQLQ6DMiaFo7Kbxfn19zGN9LFPQV8nBmB8XZZEFdF",
  "id": -576460752303422743,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
