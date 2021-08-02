
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
      "fsm_id": "ba_UFw93TBTxdBRausZRN3zwtD4Dx05xf6aukjL8WSdbOEabnW4"
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
      "fsm_id": "ba_gnUC0zzYfQy5VC04R3PGDVY7Mf1KUyNZpwlvzih1Rtw7QH/J"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4hzQ+1CQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422987,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAdMK0RZ9sliv2WKo9nBoAK8pLFhYu4mJJ8TDCDoDBoT2LBwAPR/g6/ememu6K8Osm9uqJorVd38N60cFl/NVQKuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uIb/PQCU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422987,
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
      "signed_tx": "tx_+MsLAfhCuEAdMK0RZ9sliv2WKo9nBoAK8pLFhYu4mJJ8TDCDoDBoT2LBwAPR/g6/ememu6K8Osm9uqJorVd38N60cFl/NVQKuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uIb/PQCU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422986,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAHTCtEWfbJYr9liqPZwaACvKSxYWLuJiSfEwwg6AwaE9iwcAD0f4Ov3pnpruivDrJvbqiaK1Xd/DetHBZfzVUCrhAyTVr2iKFqnAM6R6Cpqp3fDHKfcjdsBJ2JuXpumF8dxmhWgm0NVrP1ukFGKUR/5Y4kGxmPBgs9F3hPIy0imsLCLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iGGpd1R"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422986,
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAHTCtEWfbJYr9liqPZwaACvKSxYWLuJiSfEwwg6AwaE9iwcAD0f4Ov3pnpruivDrJvbqiaK1Xd/DetHBZfzVUCrhAyTVr2iKFqnAM6R6Cpqp3fDHKfcjdsBJ2JuXpumF8dxmhWgm0NVrP1ukFGKUR/5Y4kGxmPBgs9F3hPIy0imsLCLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iGGpd1R",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAHTCtEWfbJYr9liqPZwaACvKSxYWLuJiSfEwwg6AwaE9iwcAD0f4Ov3pnpruivDrJvbqiaK1Xd/DetHBZfzVUCrhAyTVr2iKFqnAM6R6Cpqp3fDHKfcjdsBJ2JuXpumF8dxmhWgm0NVrP1ukFGKUR/5Y4kGxmPBgs9F3hPIy0imsLCLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iGGpd1R",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHTCtEWfbJYr9liqPZwaACvKSxYWLuJiSfEwwg6AwaE9iwcAD0f4Ov3pnpruivDrJvbqiaK1Xd/DetHBZfzVUCrhAyTVr2iKFqnAM6R6Cpqp3fDHKfcjdsBJ2JuXpumF8dxmhWgm0NVrP1ukFGKUR/5Y4kGxmPBgs9F3hPIy0imsLCLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iGGpd1R",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHTCtEWfbJYr9liqPZwaACvKSxYWLuJiSfEwwg6AwaE9iwcAD0f4Ov3pnpruivDrJvbqiaK1Xd/DetHBZfzVUCrhAyTVr2iKFqnAM6R6Cpqp3fDHKfcjdsBJ2JuXpumF8dxmhWgm0NVrP1ukFGKUR/5Y4kGxmPBgs9F3hPIy0imsLCLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iGGpd1R",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
  "id": -576460752303422985,
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
  "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
  "id": -576460752303422985,
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "state": "tx_+QENCwH4hLhAHTCtEWfbJYr9liqPZwaACvKSxYWLuJiSfEwwg6AwaE9iwcAD0f4Ov3pnpruivDrJvbqiaK1Xd/DetHBZfzVUCrhAyTVr2iKFqnAM6R6Cpqp3fDHKfcjdsBJ2JuXpumF8dxmhWgm0NVrP1ukFGKUR/5Y4kGxmPBgs9F3hPIy0imsLCLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iGGpd1R"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "state": "tx_+QENCwH4hLhAHTCtEWfbJYr9liqPZwaACvKSxYWLuJiSfEwwg6AwaE9iwcAD0f4Ov3pnpruivDrJvbqiaK1Xd/DetHBZfzVUCrhAyTVr2iKFqnAM6R6Cpqp3fDHKfcjdsBJ2JuXpumF8dxmhWgm0NVrP1ukFGKUR/5Y4kGxmPBgs9F3hPIy0imsLCLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iGGpd1R"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
      "method": "channels.deposit",
      "params": {
        "amount": "2"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBoDqe+nn1zsDGliSmag2hKfb4HLC5rXTbB7ifAVkiH7IoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhnBIhhsPP6ChXLDyVpEyqFjhIeWBI1DOO4boF2NOsTcvscbEzeU31gIinxq7xA==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainDeposit"
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
  "id": -576460752303422984,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECYI4DO8PkgOLIAg2uHFd6M6XLSfimokqbYVoXiZEObRKkp5LUVdJOE++MmB9n79gtpQU6Oxm6PAO5ymO1el3ANuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+goVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCIrP81DI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
  "id": -576460752303422984,
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECYI4DO8PkgOLIAg2uHFd6M6XLSfimokqbYVoXiZEObRKkp5LUVdJOE++MmB9n79gtpQU6Oxm6PAO5ymO1el3ANuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+goVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCIrP81DI=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainDeposit"
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
  "id": -576460752303422983,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECYI4DO8PkgOLIAg2uHFd6M6XLSfimokqbYVoXiZEObRKkp5LUVdJOE++MmB9n79gtpQU6Oxm6PAO5ymO1el3ANuEC7FRN7l+Rf8dUJbjPUh45PxJnuAk3t1XOAvjr8hlHsjBXdrTcHBnBAxCy2Um7/akqtzQLHrAQa6n7aa7BFivsEuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+goVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCIiwOr2w="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
  "id": -576460752303422983,
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuECYI4DO8PkgOLIAg2uHFd6M6XLSfimokqbYVoXiZEObRKkp5LUVdJOE++MmB9n79gtpQU6Oxm6PAO5ymO1el3ANuEC7FRN7l+Rf8dUJbjPUh45PxJnuAk3t1XOAvjr8hlHsjBXdrTcHBnBAxCy2Um7/akqtzQLHrAQa6n7aa7BFivsEuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+goVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCIiwOr2w=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuECYI4DO8PkgOLIAg2uHFd6M6XLSfimokqbYVoXiZEObRKkp5LUVdJOE++MmB9n79gtpQU6Oxm6PAO5ymO1el3ANuEC7FRN7l+Rf8dUJbjPUh45PxJnuAk3t1XOAvjr8hlHsjBXdrTcHBnBAxCy2Um7/akqtzQLHrAQa6n7aa7BFivsEuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+goVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCIiwOr2w=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECYI4DO8PkgOLIAg2uHFd6M6XLSfimokqbYVoXiZEObRKkp5LUVdJOE++MmB9n79gtpQU6Oxm6PAO5ymO1el3ANuEC7FRN7l+Rf8dUJbjPUh45PxJnuAk3t1XOAvjr8hlHsjBXdrTcHBnBAxCy2Um7/akqtzQLHrAQa6n7aa7BFivsEuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+goVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCIiwOr2w=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECYI4DO8PkgOLIAg2uHFd6M6XLSfimokqbYVoXiZEObRKkp5LUVdJOE++MmB9n79gtpQU6Oxm6PAO5ymO1el3ANuEC7FRN7l+Rf8dUJbjPUh45PxJnuAk3t1XOAvjr8hlHsjBXdrTcHBnBAxCy2Um7/akqtzQLHrAQa6n7aa7BFivsEuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+goVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCIiwOr2w=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "state": "tx_+P4LAfiEuECYI4DO8PkgOLIAg2uHFd6M6XLSfimokqbYVoXiZEObRKkp5LUVdJOE++MmB9n79gtpQU6Oxm6PAO5ymO1el3ANuEC7FRN7l+Rf8dUJbjPUh45PxJnuAk3t1XOAvjr8hlHsjBXdrTcHBnBAxCy2Um7/akqtzQLHrAQa6n7aa7BFivsEuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+goVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCIiwOr2w="
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "state": "tx_+P4LAfiEuECYI4DO8PkgOLIAg2uHFd6M6XLSfimokqbYVoXiZEObRKkp5LUVdJOE++MmB9n79gtpQU6Oxm6PAO5ymO1el3ANuEC7FRN7l+Rf8dUJbjPUh45PxJnuAk3t1XOAvjr8hlHsjBXdrTcHBnBAxCy2Um7/akqtzQLHrAQa6n7aa7BFivsEuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+goVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCIiwOr2w="
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
    "info": "Hello",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
      "method": "channels.deposit",
      "params": {
        "amount": "2"
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
  "method": "channels.message",
  "params": {
    "info": "Hello",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBoDqe+nn1zsDGliSmag2hKfb4HLC5rXTbB7ifAVkiH7IoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEAIAhnBIhhsPP6B9/+NB55OhzzLOezHqwJrKqcohlQB0t7MzKXQVTQm6nwMN1P0WHw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainDeposit"
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
  "id": -576460752303422982,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBWm2Uiq0uM6RJLAvkJYlc26icisOminIGy8NtR+GVy2GlzJchT8aPXocP1tSZDkXjUFjnvmrGFaABThrWCewICuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DDXwz8vE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
  "id": -576460752303422982,
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBWm2Uiq0uM6RJLAvkJYlc26icisOminIGy8NtR+GVy2GlzJchT8aPXocP1tSZDkXjUFjnvmrGFaABThrWCewICuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DDXwz8vE=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainDeposit"
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
  "id": -576460752303422981,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAFfl0enQvcAPYzgS5V03ZZEgtrd0oPhXZ51whsYp+7f04WoijjE/Y5BoHJwTH+3dq+SsPtPXqn5IEyhhZaeH4CuEBWm2Uiq0uM6RJLAvkJYlc26icisOminIGy8NtR+GVy2GlzJchT8aPXocP1tSZDkXjUFjnvmrGFaABThrWCewICuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DDevqvn8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
  "id": -576460752303422981,
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEAFfl0enQvcAPYzgS5V03ZZEgtrd0oPhXZ51whsYp+7f04WoijjE/Y5BoHJwTH+3dq+SsPtPXqn5IEyhhZaeH4CuEBWm2Uiq0uM6RJLAvkJYlc26icisOminIGy8NtR+GVy2GlzJchT8aPXocP1tSZDkXjUFjnvmrGFaABThrWCewICuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DDevqvn8=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEAFfl0enQvcAPYzgS5V03ZZEgtrd0oPhXZ51whsYp+7f04WoijjE/Y5BoHJwTH+3dq+SsPtPXqn5IEyhhZaeH4CuEBWm2Uiq0uM6RJLAvkJYlc26icisOminIGy8NtR+GVy2GlzJchT8aPXocP1tSZDkXjUFjnvmrGFaABThrWCewICuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DDevqvn8=",
      "type": "channel_deposit_tx"
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
    "info": "Hello",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "message": {
        "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAFfl0enQvcAPYzgS5V03ZZEgtrd0oPhXZ51whsYp+7f04WoijjE/Y5BoHJwTH+3dq+SsPtPXqn5IEyhhZaeH4CuEBWm2Uiq0uM6RJLAvkJYlc26icisOminIGy8NtR+GVy2GlzJchT8aPXocP1tSZDkXjUFjnvmrGFaABThrWCewICuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DDevqvn8=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAFfl0enQvcAPYzgS5V03ZZEgtrd0oPhXZ51whsYp+7f04WoijjE/Y5BoHJwTH+3dq+SsPtPXqn5IEyhhZaeH4CuEBWm2Uiq0uM6RJLAvkJYlc26icisOminIGy8NtR+GVy2GlzJchT8aPXocP1tSZDkXjUFjnvmrGFaABThrWCewICuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DDevqvn8=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "state": "tx_+P4LAfiEuEAFfl0enQvcAPYzgS5V03ZZEgtrd0oPhXZ51whsYp+7f04WoijjE/Y5BoHJwTH+3dq+SsPtPXqn5IEyhhZaeH4CuEBWm2Uiq0uM6RJLAvkJYlc26icisOminIGy8NtR+GVy2GlzJchT8aPXocP1tSZDkXjUFjnvmrGFaABThrWCewICuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DDevqvn8="
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "state": "tx_+P4LAfiEuEAFfl0enQvcAPYzgS5V03ZZEgtrd0oPhXZ51whsYp+7f04WoijjE/Y5BoHJwTH+3dq+SsPtPXqn5IEyhhZaeH4CuEBWm2Uiq0uM6RJLAvkJYlc26icisOminIGy8NtR+GVy2GlzJchT8aPXocP1tSZDkXjUFjnvmrGFaABThrWCewICuHT4cjMBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DDevqvn8="
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBoDqe+nn1zsDGliSmag2hKfb4HLC5rXTbB7ifAVkiH7IoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY2kdavwAGGG0jrV+ADAIYSMJzlQAAjzr6i3A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422980,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECvb7tBT0jOpysZoTHr4FJsoAYf9ps2DUy6ZCBQ8GexYv2GQb/4EbF+ioR/TJOBMBm9q+GxMWxJNv2AVE+FCZQOuF/4XTUBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr8ABhhtI61fgAwCGEjCc5UAAI3pxFm8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
  "id": -576460752303422980,
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECvb7tBT0jOpysZoTHr4FJsoAYf9ps2DUy6ZCBQ8GexYv2GQb/4EbF+ioR/TJOBMBm9q+GxMWxJNv2AVE+FCZQOuF/4XTUBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr8ABhhtI61fgAwCGEjCc5UAAI3pxFm8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422979,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuECbXpOMIY5i9nzFammqdTW3QqtL2VAtBqZpzESY3zIQOTS1VfKJpRZ+ueWUmw6efpmg8qbZbcRo56y7vEK+FKMFuECvb7tBT0jOpysZoTHr4FJsoAYf9ps2DUy6ZCBQ8GexYv2GQb/4EbF+ioR/TJOBMBm9q+GxMWxJNv2AVE+FCZQOuF/4XTUBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr8ABhhtI61fgAwCGEjCc5UAAI18ZjEY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
  "id": -576460752303422979,
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECbXpOMIY5i9nzFammqdTW3QqtL2VAtBqZpzESY3zIQOTS1VfKJpRZ+ueWUmw6efpmg8qbZbcRo56y7vEK+FKMFuECvb7tBT0jOpysZoTHr4FJsoAYf9ps2DUy6ZCBQ8GexYv2GQb/4EbF+ioR/TJOBMBm9q+GxMWxJNv2AVE+FCZQOuF/4XTUBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr8ABhhtI61fgAwCGEjCc5UAAI18ZjEY=",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECbXpOMIY5i9nzFammqdTW3QqtL2VAtBqZpzESY3zIQOTS1VfKJpRZ+ueWUmw6efpmg8qbZbcRo56y7vEK+FKMFuECvb7tBT0jOpysZoTHr4FJsoAYf9ps2DUy6ZCBQ8GexYv2GQb/4EbF+ioR/TJOBMBm9q+GxMWxJNv2AVE+FCZQOuF/4XTUBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr8ABhhtI61fgAwCGEjCc5UAAI18ZjEY=",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECbXpOMIY5i9nzFammqdTW3QqtL2VAtBqZpzESY3zIQOTS1VfKJpRZ+ueWUmw6efpmg8qbZbcRo56y7vEK+FKMFuECvb7tBT0jOpysZoTHr4FJsoAYf9ps2DUy6ZCBQ8GexYv2GQb/4EbF+ioR/TJOBMBm9q+GxMWxJNv2AVE+FCZQOuF/4XTUBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr8ABhhtI61fgAwCGEjCc5UAAI18ZjEY=",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECbXpOMIY5i9nzFammqdTW3QqtL2VAtBqZpzESY3zIQOTS1VfKJpRZ+ueWUmw6efpmg8qbZbcRo56y7vEK+FKMFuECvb7tBT0jOpysZoTHr4FJsoAYf9ps2DUy6ZCBQ8GexYv2GQb/4EbF+ioR/TJOBMBm9q+GxMWxJNv2AVE+FCZQOuF/4XTUBoQaA6nvp59c7AxpYkpmoNoSn2+Bywua102we4nwFZIh+yKEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr8ABhhtI61fgAwCGEjCc5UAAI18ZjEY=",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
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
    "channel_id": "ch_ymz8YsnZsEvyeiYqkT1VHX66wQs9NUhiUS6bVGA2UPQbjSivm",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
