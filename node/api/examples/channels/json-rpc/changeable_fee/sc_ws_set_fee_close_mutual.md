
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
      "fsm_id": "ba_rHFFjBTTFP4xLK5fzWYY0Z4kJJzuusZUVj7mVBn+bXylo3SA"
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
      "fsm_id": "ba_blnC64vbDiJOmgQGPW9Tf8Fi/YmhGA1GLjZu58eqx+wLanmF"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4qNfsnXQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422930,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECxw+QNPHdw4lRWglNEDDlg8cfWXbA3VnUe/9/32lKb5z9XGUKHznDMCekYqMmIlEpICL23eGEIbUh08roTKNgHuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uKiwwhIU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422930,
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
      "signed_tx": "tx_+MsLAfhCuECxw+QNPHdw4lRWglNEDDlg8cfWXbA3VnUe/9/32lKb5z9XGUKHznDMCekYqMmIlEpICL23eGEIbUh08roTKNgHuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uKiwwhIU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422929,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAc+HPP5ntFLzSO5qvd/M04DS/n2Gxb0Pj4vff2iLLgqu/PslPwA0ZRM6AazjY50SkBxJLenq/++HWa/+3SSI9CLhAscPkDTx3cOJUVoJTRAw5YPHH1l2wN1Z1Hv/f99pSm+c/VxlCh85wzAnpGKjJiJRKSAi9t3hhCG1IdPK6EyjYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ir+sCsw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422929,
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAc+HPP5ntFLzSO5qvd/M04DS/n2Gxb0Pj4vff2iLLgqu/PslPwA0ZRM6AazjY50SkBxJLenq/++HWa/+3SSI9CLhAscPkDTx3cOJUVoJTRAw5YPHH1l2wN1Z1Hv/f99pSm+c/VxlCh85wzAnpGKjJiJRKSAi9t3hhCG1IdPK6EyjYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ir+sCsw",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAc+HPP5ntFLzSO5qvd/M04DS/n2Gxb0Pj4vff2iLLgqu/PslPwA0ZRM6AazjY50SkBxJLenq/++HWa/+3SSI9CLhAscPkDTx3cOJUVoJTRAw5YPHH1l2wN1Z1Hv/f99pSm+c/VxlCh85wzAnpGKjJiJRKSAi9t3hhCG1IdPK6EyjYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ir+sCsw",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAc+HPP5ntFLzSO5qvd/M04DS/n2Gxb0Pj4vff2iLLgqu/PslPwA0ZRM6AazjY50SkBxJLenq/++HWa/+3SSI9CLhAscPkDTx3cOJUVoJTRAw5YPHH1l2wN1Z1Hv/f99pSm+c/VxlCh85wzAnpGKjJiJRKSAi9t3hhCG1IdPK6EyjYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ir+sCsw",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAc+HPP5ntFLzSO5qvd/M04DS/n2Gxb0Pj4vff2iLLgqu/PslPwA0ZRM6AazjY50SkBxJLenq/++HWa/+3SSI9CLhAscPkDTx3cOJUVoJTRAw5YPHH1l2wN1Z1Hv/f99pSm+c/VxlCh85wzAnpGKjJiJRKSAi9t3hhCG1IdPK6EyjYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ir+sCsw",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "message": {
        "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "message": {
        "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
  "id": -576460752303422928,
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
  "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
  "id": -576460752303422928,
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "state": "tx_+QENCwH4hLhAc+HPP5ntFLzSO5qvd/M04DS/n2Gxb0Pj4vff2iLLgqu/PslPwA0ZRM6AazjY50SkBxJLenq/++HWa/+3SSI9CLhAscPkDTx3cOJUVoJTRAw5YPHH1l2wN1Z1Hv/f99pSm+c/VxlCh85wzAnpGKjJiJRKSAi9t3hhCG1IdPK6EyjYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ir+sCsw"
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "state": "tx_+QENCwH4hLhAc+HPP5ntFLzSO5qvd/M04DS/n2Gxb0Pj4vff2iLLgqu/PslPwA0ZRM6AazjY50SkBxJLenq/++HWa/+3SSI9CLhAscPkDTx3cOJUVoJTRAw5YPHH1l2wN1Z1Hv/f99pSm+c/VxlCh85wzAnpGKjJiJRKSAi9t3hhCG1IdPK6EyjYB7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ir+sCsw"
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
  "params": {
    "fee": 20000000000001
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBuGYoyOh7OERzmlLkotTmVJdtuxtmpGE2dM3OngNSFEmoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY2kdavv/6GG0jrV+ABAIYSMJzlQAErXps8AA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422927,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDECLytjlFk2ZI8oq5Zb10xaUJt20snU9J6xFh2NqkUcWQIB3I0JthJQQNmRkC06oBkHlNi6+6NL1Xx3VeVhvMFuF/4XTUBoQbhmKMjoezhEc5pS5KLU5lSXbbsbZqRhNnTNzp4DUhRJqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/+hhtI61fgAQCGEjCc5UABK6qx1jc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
  "id": -576460752303422927,
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDECLytjlFk2ZI8oq5Zb10xaUJt20snU9J6xFh2NqkUcWQIB3I0JthJQQNmRkC06oBkHlNi6+6NL1Xx3VeVhvMFuF/4XTUBoQbhmKMjoezhEc5pS5KLU5lSXbbsbZqRhNnTNzp4DUhRJqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/+hhtI61fgAQCGEjCc5UABK6qx1jc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422926,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEC2DTICGYbyxaIvZ5E7VqM8EM+LDgNEDWmvaqB6tH8yAq+Nyj8jTb+96kLjnYUfX74c011iJRd1oaNXZ+aN354KuEDECLytjlFk2ZI8oq5Zb10xaUJt20snU9J6xFh2NqkUcWQIB3I0JthJQQNmRkC06oBkHlNi6+6NL1Xx3VeVhvMFuF/4XTUBoQbhmKMjoezhEc5pS5KLU5lSXbbsbZqRhNnTNzp4DUhRJqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/+hhtI61fgAQCGEjCc5UABKydnOGY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
  "id": -576460752303422926,
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEC2DTICGYbyxaIvZ5E7VqM8EM+LDgNEDWmvaqB6tH8yAq+Nyj8jTb+96kLjnYUfX74c011iJRd1oaNXZ+aN354KuEDECLytjlFk2ZI8oq5Zb10xaUJt20snU9J6xFh2NqkUcWQIB3I0JthJQQNmRkC06oBkHlNi6+6NL1Xx3VeVhvMFuF/4XTUBoQbhmKMjoezhEc5pS5KLU5lSXbbsbZqRhNnTNzp4DUhRJqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/+hhtI61fgAQCGEjCc5UABKydnOGY=",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEC2DTICGYbyxaIvZ5E7VqM8EM+LDgNEDWmvaqB6tH8yAq+Nyj8jTb+96kLjnYUfX74c011iJRd1oaNXZ+aN354KuEDECLytjlFk2ZI8oq5Zb10xaUJt20snU9J6xFh2NqkUcWQIB3I0JthJQQNmRkC06oBkHlNi6+6NL1Xx3VeVhvMFuF/4XTUBoQbhmKMjoezhEc5pS5KLU5lSXbbsbZqRhNnTNzp4DUhRJqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/+hhtI61fgAQCGEjCc5UABKydnOGY=",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEC2DTICGYbyxaIvZ5E7VqM8EM+LDgNEDWmvaqB6tH8yAq+Nyj8jTb+96kLjnYUfX74c011iJRd1oaNXZ+aN354KuEDECLytjlFk2ZI8oq5Zb10xaUJt20snU9J6xFh2NqkUcWQIB3I0JthJQQNmRkC06oBkHlNi6+6NL1Xx3VeVhvMFuF/4XTUBoQbhmKMjoezhEc5pS5KLU5lSXbbsbZqRhNnTNzp4DUhRJqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/+hhtI61fgAQCGEjCc5UABKydnOGY=",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEC2DTICGYbyxaIvZ5E7VqM8EM+LDgNEDWmvaqB6tH8yAq+Nyj8jTb+96kLjnYUfX74c011iJRd1oaNXZ+aN354KuEDECLytjlFk2ZI8oq5Zb10xaUJt20snU9J6xFh2NqkUcWQIB3I0JthJQQNmRkC06oBkHlNi6+6NL1Xx3VeVhvMFuF/4XTUBoQbhmKMjoezhEc5pS5KLU5lSXbbsbZqRhNnTNzp4DUhRJqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/+hhtI61fgAQCGEjCc5UABKydnOGY=",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
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
    "channel_id": "ch_2iMZ5oP2nxzC3XRTu8DihS9Mmbcv4eHbN89YKFYjZ3pTRyXmyx",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
