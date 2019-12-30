
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
      "fsm_id": "ba_CtGuwjAvHdxT+IRdSR8P/Ww1tjSfMxnaoIihQYxZt8VJ2RnE"
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
      "fsm_id": "ba_2dFj1lPpbmvUqlNXN8XPw6Ahiu7atwSjv+lOSyVz+tbFpJZH"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4El76Ebg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423426,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBCaDHOi0OHnVfopDrSWoyBRKjkTlzbQi4+3jSqJrpwEiuGFdyZVb0LPut0lgJHpy0VTm1U3yp6ZQHbvfvarXEEuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uBJT+HKk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423426,
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
      "signed_tx": "tx_+MsLAfhCuEBCaDHOi0OHnVfopDrSWoyBRKjkTlzbQi4+3jSqJrpwEiuGFdyZVb0LPut0lgJHpy0VTm1U3yp6ZQHbvfvarXEEuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uBJT+HKk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423425,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAQmgxzotDh51X6KQ60lqMgUSo5E5c20IuPt40qia6cBIrhhXcmVW9Cz7rdJYCR6ctFU5tVN8qemUB27372q1xBLhArH4zb6ESHqFdGTvZnhuMMZe0dHB066h30xtjbPvgR0SFIqrmZ3MfchWv1xvy3mQGPePQFxgzbpO2OEQVRV54A7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gQnPqOz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423425,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAQmgxzotDh51X6KQ60lqMgUSo5E5c20IuPt40qia6cBIrhhXcmVW9Cz7rdJYCR6ctFU5tVN8qemUB27372q1xBLhArH4zb6ESHqFdGTvZnhuMMZe0dHB066h30xtjbPvgR0SFIqrmZ3MfchWv1xvy3mQGPePQFxgzbpO2OEQVRV54A7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gQnPqOz",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAQmgxzotDh51X6KQ60lqMgUSo5E5c20IuPt40qia6cBIrhhXcmVW9Cz7rdJYCR6ctFU5tVN8qemUB27372q1xBLhArH4zb6ESHqFdGTvZnhuMMZe0dHB066h30xtjbPvgR0SFIqrmZ3MfchWv1xvy3mQGPePQFxgzbpO2OEQVRV54A7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gQnPqOz",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAQmgxzotDh51X6KQ60lqMgUSo5E5c20IuPt40qia6cBIrhhXcmVW9Cz7rdJYCR6ctFU5tVN8qemUB27372q1xBLhArH4zb6ESHqFdGTvZnhuMMZe0dHB066h30xtjbPvgR0SFIqrmZ3MfchWv1xvy3mQGPePQFxgzbpO2OEQVRV54A7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gQnPqOz",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAQmgxzotDh51X6KQ60lqMgUSo5E5c20IuPt40qia6cBIrhhXcmVW9Cz7rdJYCR6ctFU5tVN8qemUB27372q1xBLhArH4zb6ESHqFdGTvZnhuMMZe0dHB066h30xtjbPvgR0SFIqrmZ3MfchWv1xvy3mQGPePQFxgzbpO2OEQVRV54A7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gQnPqOz",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "message": {
        "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "message": {
        "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
  "id": -576460752303423424,
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
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423424,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+QENCwH4hLhAQmgxzotDh51X6KQ60lqMgUSo5E5c20IuPt40qia6cBIrhhXcmVW9Cz7rdJYCR6ctFU5tVN8qemUB27372q1xBLhArH4zb6ESHqFdGTvZnhuMMZe0dHB066h30xtjbPvgR0SFIqrmZ3MfchWv1xvy3mQGPePQFxgzbpO2OEQVRV54A7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gQnPqOz"
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+QENCwH4hLhAQmgxzotDh51X6KQ60lqMgUSo5E5c20IuPt40qia6cBIrhhXcmVW9Cz7rdJYCR6ctFU5tVN8qemUB27372q1xBLhArH4zb6ESHqFdGTvZnhuMMZe0dHB066h30xtjbPvgR0SFIqrmZ3MfchWv1xvy3mQGPePQFxgzbpO2OEQVRV54A7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gQnPqOz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423423,
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
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423423,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ABCDEF",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "meta": 17,
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "meta": 17,
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnRyany4amgt+ICVyh9FILT6L9ttgLdaxgwzN907IpStAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B8t1j5I=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423422,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAMIj0qTBekT+eM3ikTCot94O2j4ay1b3zNl5IAhtt/1nDnNNoNlvff3LFP9vfHDtudJWqlo8/XSoKOys/8nKoNuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeG3t3u"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423422,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAMIj0qTBekT+eM3ikTCot94O2j4ay1b3zNl5IAhtt/1nDnNNoNlvff3LFP9vfHDtudJWqlo8/XSoKOys/8nKoNuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeG3t3u",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
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
  "id": -576460752303423421,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAMIj0qTBekT+eM3ikTCot94O2j4ay1b3zNl5IAhtt/1nDnNNoNlvff3LFP9vfHDtudJWqlo8/XSoKOys/8nKoNuEAuN6jCW1jdWgz6SH8tqzTRiWbAPUdylQdJaFY7vJq/uan4OzRebmn+OXCkIyMwAB7Jwxw0CjdPHTxQZTSRi+gMuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeogMeT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423421,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEAMIj0qTBekT+eM3ikTCot94O2j4ay1b3zNl5IAhtt/1nDnNNoNlvff3LFP9vfHDtudJWqlo8/XSoKOys/8nKoNuEAuN6jCW1jdWgz6SH8tqzTRiWbAPUdylQdJaFY7vJq/uan4OzRebmn+OXCkIyMwAB7Jwxw0CjdPHTxQZTSRi+gMuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeogMeT"
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEAMIj0qTBekT+eM3ikTCot94O2j4ay1b3zNl5IAhtt/1nDnNNoNlvff3LFP9vfHDtudJWqlo8/XSoKOys/8nKoNuEAuN6jCW1jdWgz6SH8tqzTRiWbAPUdylQdJaFY7vJq/uan4OzRebmn+OXCkIyMwAB7Jwxw0CjdPHTxQZTSRi+gMuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeogMeT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423420,
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
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423420,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999998
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423419,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423419,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAMIj0qTBekT+eM3ikTCot94O2j4ay1b3zNl5IAhtt/1nDnNNoNlvff3LFP9vfHDtudJWqlo8/XSoKOys/8nKoNuEAuN6jCW1jdWgz6SH8tqzTRiWbAPUdylQdJaFY7vJq/uan4OzRebmn+OXCkIyMwAB7Jwxw0CjdPHTxQZTSRi+gMuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeogMeT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423418,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423418,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "amount": "1",
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "meta": 17,
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "meta": 17,
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnRyany4amgt+ICVyh9FILT6L9ttgLdaxgwzN907IpStA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7g8/0ds=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
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
  "id": -576460752303423417,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECtGSGdf08ueqW0lcQpe3IsMvNVzg9dDj7Nn0StSQ56xdQjbEiNpQdazwipe5ZU9XYD6VHcnnl3eVFLbx9SKz0DuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+50F7yy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423417,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+JALAfhCuECtGSGdf08ueqW0lcQpe3IsMvNVzg9dDj7Nn0StSQ56xdQjbEiNpQdazwipe5ZU9XYD6VHcnnl3eVFLbx9SKz0DuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+50F7yy",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
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
  "id": -576460752303423416,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAn+saariloiEbGuPnIHrJCFtxk2CYOp2YFyTOZ+V0Vdqoy2oO4pxsz3zzVpDolHGb5/VD91/JsjDvJU0fmLqEJuECtGSGdf08ueqW0lcQpe3IsMvNVzg9dDj7Nn0StSQ56xdQjbEiNpQdazwipe5ZU9XYD6VHcnnl3eVFLbx9SKz0DuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62L5/+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423416,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEAn+saariloiEbGuPnIHrJCFtxk2CYOp2YFyTOZ+V0Vdqoy2oO4pxsz3zzVpDolHGb5/VD91/JsjDvJU0fmLqEJuECtGSGdf08ueqW0lcQpe3IsMvNVzg9dDj7Nn0StSQ56xdQjbEiNpQdazwipe5ZU9XYD6VHcnnl3eVFLbx9SKz0DuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62L5/+"
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEAn+saariloiEbGuPnIHrJCFtxk2CYOp2YFyTOZ+V0Vdqoy2oO4pxsz3zzVpDolHGb5/VD91/JsjDvJU0fmLqEJuECtGSGdf08ueqW0lcQpe3IsMvNVzg9dDj7Nn0StSQ56xdQjbEiNpQdazwipe5ZU9XYD6VHcnnl3eVFLbx9SKz0DuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62L5/+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423415,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423415,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423414,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423414,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAn+saariloiEbGuPnIHrJCFtxk2CYOp2YFyTOZ+V0Vdqoy2oO4pxsz3zzVpDolHGb5/VD91/JsjDvJU0fmLqEJuECtGSGdf08ueqW0lcQpe3IsMvNVzg9dDj7Nn0StSQ56xdQjbEiNpQdazwipe5ZU9XYD6VHcnnl3eVFLbx9SKz0DuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62L5/+",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423413,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423413,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
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
    "amount": "1",
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "meta": 17,
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "meta": 17,
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnRyany4amgt+ICVyh9FILT6L9ttgLdaxgwzN907IpStBKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tvNZs6Q=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
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
  "id": -576460752303423412,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBoIwTLAzxr3y2Z+i5vAo4phU28VxuUgf0wkt7QYGItjR8gesSL5mnQDSrchsv99sudF8JG+n9/I78Nen6hQPMGuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bqksjD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423412,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBoIwTLAzxr3y2Z+i5vAo4phU28VxuUgf0wkt7QYGItjR8gesSL5mnQDSrchsv99sudF8JG+n9/I78Nen6hQPMGuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bqksjD",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
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
  "id": -576460752303423411,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAdi+mO28+G1RG3iz5IfsbVK/GaGKvd8ORGqT5VRnMRTQVfweeqyrHYRodSUOvhFy0e591Cpd1DW4cc1Ps4tzcNuEBoIwTLAzxr3y2Z+i5vAo4phU28VxuUgf0wkt7QYGItjR8gesSL5mnQDSrchsv99sudF8JG+n9/I78Nen6hQPMGuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bTA2s6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423411,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEAdi+mO28+G1RG3iz5IfsbVK/GaGKvd8ORGqT5VRnMRTQVfweeqyrHYRodSUOvhFy0e591Cpd1DW4cc1Ps4tzcNuEBoIwTLAzxr3y2Z+i5vAo4phU28VxuUgf0wkt7QYGItjR8gesSL5mnQDSrchsv99sudF8JG+n9/I78Nen6hQPMGuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bTA2s6"
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEAdi+mO28+G1RG3iz5IfsbVK/GaGKvd8ORGqT5VRnMRTQVfweeqyrHYRodSUOvhFy0e591Cpd1DW4cc1Ps4tzcNuEBoIwTLAzxr3y2Z+i5vAo4phU28VxuUgf0wkt7QYGItjR8gesSL5mnQDSrchsv99sudF8JG+n9/I78Nen6hQPMGuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bTA2s6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423410,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423410,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000000
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423409,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423409,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAdi+mO28+G1RG3iz5IfsbVK/GaGKvd8ORGqT5VRnMRTQVfweeqyrHYRodSUOvhFy0e591Cpd1DW4cc1Ps4tzcNuEBoIwTLAzxr3y2Z+i5vAo4phU28VxuUgf0wkt7QYGItjR8gesSL5mnQDSrchsv99sudF8JG+n9/I78Nen6hQPMGuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bTA2s6",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423408,
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
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423408,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 70000000000000
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000000
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
    "amount": "1",
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ABCDEF",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "meta": 17,
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "meta": 17,
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnRyany4amgt+ICVyh9FILT6L9ttgLdaxgwzN907IpStBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7tEkdzg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423407,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAVT65Z2VNMhaOoEcggd0NG6qvexva7uVAnt0FL2nYaEP/YYGDMf92E1XvXGiJcrbwm7Frvu2tvpA+LxLDCdj4DuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7UiM6m"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423407,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAVT65Z2VNMhaOoEcggd0NG6qvexva7uVAnt0FL2nYaEP/YYGDMf92E1XvXGiJcrbwm7Frvu2tvpA+LxLDCdj4DuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7UiM6m",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
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
  "id": -576460752303423406,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAVT65Z2VNMhaOoEcggd0NG6qvexva7uVAnt0FL2nYaEP/YYGDMf92E1XvXGiJcrbwm7Frvu2tvpA+LxLDCdj4DuEDBYfi6u+sr3CYb6BXAbMxrK1GVnopdkMTPKgqOlTZ2pGn2SC46zHSpJhrpmGS7wtoz+P2CN6AirKc72ZUFnbUAuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7+KM8k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423406,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEAVT65Z2VNMhaOoEcggd0NG6qvexva7uVAnt0FL2nYaEP/YYGDMf92E1XvXGiJcrbwm7Frvu2tvpA+LxLDCdj4DuEDBYfi6u+sr3CYb6BXAbMxrK1GVnopdkMTPKgqOlTZ2pGn2SC46zHSpJhrpmGS7wtoz+P2CN6AirKc72ZUFnbUAuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7+KM8k"
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEAVT65Z2VNMhaOoEcggd0NG6qvexva7uVAnt0FL2nYaEP/YYGDMf92E1XvXGiJcrbwm7Frvu2tvpA+LxLDCdj4DuEDBYfi6u+sr3CYb6BXAbMxrK1GVnopdkMTPKgqOlTZ2pGn2SC46zHSpJhrpmGS7wtoz+P2CN6AirKc72ZUFnbUAuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7+KM8k"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423405,
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
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423405,
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

#### initiator ---> node
```javascript
{
  "id": -576460752303423404,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423404,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAVT65Z2VNMhaOoEcggd0NG6qvexva7uVAnt0FL2nYaEP/YYGDMf92E1XvXGiJcrbwm7Frvu2tvpA+LxLDCdj4DuEDBYfi6u+sr3CYb6BXAbMxrK1GVnopdkMTPKgqOlTZ2pGn2SC46zHSpJhrpmGS7wtoz+P2CN6AirKc72ZUFnbUAuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7+KM8k",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423403,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423403,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
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
    "amount": "1",
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "meta": 17,
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "meta": 17,
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnRyany4amgt+ICVyh9FILT6L9ttgLdaxgwzN907IpStBqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tnFxRsY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
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
  "id": -576460752303423402,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBYaRDEP3gAnx0cdB78DjZXYddkmGYBJRQT8dHRamC/IfhZXlnNBGbB+RbZJj6ouTP9d3qyjyDkSqzHaiHhukUMuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Y8nZmU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423402,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBYaRDEP3gAnx0cdB78DjZXYddkmGYBJRQT8dHRamC/IfhZXlnNBGbB+RbZJj6ouTP9d3qyjyDkSqzHaiHhukUMuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Y8nZmU",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
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
  "id": -576460752303423401,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBYaRDEP3gAnx0cdB78DjZXYddkmGYBJRQT8dHRamC/IfhZXlnNBGbB+RbZJj6ouTP9d3qyjyDkSqzHaiHhukUMuEDCJZthvuk7kPUK4u38m03pP47OiqU0MfRxA8wp9MKZI9Hal6evLOccMV3M0x50goJvl81TIDBaNMiz0scoJP8GuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7a3ABow"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423401,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEBYaRDEP3gAnx0cdB78DjZXYddkmGYBJRQT8dHRamC/IfhZXlnNBGbB+RbZJj6ouTP9d3qyjyDkSqzHaiHhukUMuEDCJZthvuk7kPUK4u38m03pP47OiqU0MfRxA8wp9MKZI9Hal6evLOccMV3M0x50goJvl81TIDBaNMiz0scoJP8GuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7a3ABow"
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "state": "tx_+NILAfiEuEBYaRDEP3gAnx0cdB78DjZXYddkmGYBJRQT8dHRamC/IfhZXlnNBGbB+RbZJj6ouTP9d3qyjyDkSqzHaiHhukUMuEDCJZthvuk7kPUK4u38m03pP47OiqU0MfRxA8wp9MKZI9Hal6evLOccMV3M0x50goJvl81TIDBaNMiz0scoJP8GuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7a3ABow"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423400,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423400,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000000
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBYaRDEP3gAnx0cdB78DjZXYddkmGYBJRQT8dHRamC/IfhZXlnNBGbB+RbZJj6ouTP9d3qyjyDkSqzHaiHhukUMuEDCJZthvuk7kPUK4u38m03pP47OiqU0MfRxA8wp9MKZI9Hal6evLOccMV3M0x50goJvl81TIDBaNMiz0scoJP8GuEj4RjkCoQZ0cmp8uGpoLfiAlcofRSC0+i/bbYC3WsYMMzfdOyKUrQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7a3ABow",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423398,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
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
  "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
  "id": -576460752303423398,
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
    "channel_id": "ch_tHUtAYbE9fqVNv3Lqg9yRduubiKaYhfQCoPgWiAxfWzzCrgwD",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator ---> node
```javascript
{
  "id": -576460752303423397,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator closes WebSocket connection
