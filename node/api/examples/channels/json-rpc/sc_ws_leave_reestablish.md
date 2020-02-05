
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish%2F3285
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
      "fsm_id": "ba_ev75kEfKaBwYTeF4w2wXHQKkYKXkWgJ3+qOldrKlCLE0jo5a"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish%2F3285
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
      "fsm_id": "ba_AQZruhGNzVKRyfT7AcNWN/Sf0MGJxB3DkmOIUzM/c/3kv3LL"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4VHQeUww==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423277,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECrN4gykTeUq0+kXSYjmMoWiaFbe6AD3SukNBs/avgYo0C3KGgEIKizrScndPOCohXO3LRw2i8yV9C6DIh3djwLuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uFV/HuKE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423277,
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
      "signed_tx": "tx_+MsLAfhCuECrN4gykTeUq0+kXSYjmMoWiaFbe6AD3SukNBs/avgYo0C3KGgEIKizrScndPOCohXO3LRw2i8yV9C6DIh3djwLuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uFV/HuKE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423276,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423276,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "message": {
        "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "message": {
        "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "id": -576460752303423275,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423275,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64&existing_fsm_id=ba_AQZruhGNzVKRyfT7AcNWN%2FSf0MGJxB3DkmOIUzM%2Fc%2F3kv3LL&offchain_tx=tx_%2BQENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan%2BiEBTUi6KoijGuioCKyHOb%2B2P8rYO8Lkqn%2FdNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hXxa0Kg&port=13180&protocol=json-rpc&role=responder
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
      "fsm_id": "ba_g8B7bB1muga6l6HV0Es86CF4xpKzc5OcmgHV3doFuxRurn2+"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64&existing_fsm_id=ba_ev75kEfKaBwYTeF4w2wXHQKkYKXkWgJ3%2BqOldrKlCLE0jo5a&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan%2BiEBTUi6KoijGuioCKyHOb%2B2P8rYO8Lkqn%2FdNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hXxa0Kg&port=13180&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_kIKgexWm53Hfk/gYN7mM6CVw8brYHe8ujY+keCJmUEKau07s"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+QENCwH4hLhAHkfNsGP7rYONDus9m3HUbTGIoqX2ApFAZan+iEBTUi6KoijGuioCKyHOb+2P8rYO8Lkqn/dNty2MEImqTR4DALhAqzeIMpE3lKtPpF0mI5jKFomhW3ugA90rpDQbP2r4GKNAtyhoBCCos60nJ3TzgqIVzty0cNovMlfQugyId3Y8C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hXxa0Kg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423274,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423274,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuBROHsmTP98le1n5XxdLm4KroeAr/7d/haeaLN9Ii5nAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B36DN44=",
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
  "id": -576460752303423273,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECghnh9w8CCDu21XWL8FzFqYT4p8yWcXXyI8qEiVoXLz9gUwN4CKSnbomOLR3QxyGdnIPk2YuS8Ktoe7lJuBXIHuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAchSqcj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423273,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+JALAfhCuECghnh9w8CCDu21XWL8FzFqYT4p8yWcXXyI8qEiVoXLz9gUwN4CKSnbomOLR3QxyGdnIPk2YuS8Ktoe7lJuBXIHuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAchSqcj",
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
  "id": -576460752303423272,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBH7SZvPU90UEhZ8d2jeM++fXP9IMCNCXR3lpRov3K16zbnA/KaJvTHBFW2mROef8sv6WpNbx59UulBeUAq85QLuECghnh9w8CCDu21XWL8FzFqYT4p8yWcXXyI8qEiVoXLz9gUwN4CKSnbomOLR3QxyGdnIPk2YuS8Ktoe7lJuBXIHuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe8Gne3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423272,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEBH7SZvPU90UEhZ8d2jeM++fXP9IMCNCXR3lpRov3K16zbnA/KaJvTHBFW2mROef8sv6WpNbx59UulBeUAq85QLuECghnh9w8CCDu21XWL8FzFqYT4p8yWcXXyI8qEiVoXLz9gUwN4CKSnbomOLR3QxyGdnIPk2YuS8Ktoe7lJuBXIHuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe8Gne3"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEBH7SZvPU90UEhZ8d2jeM++fXP9IMCNCXR3lpRov3K16zbnA/KaJvTHBFW2mROef8sv6WpNbx59UulBeUAq85QLuECghnh9w8CCDu21XWL8FzFqYT4p8yWcXXyI8qEiVoXLz9gUwN4CKSnbomOLR3QxyGdnIPk2YuS8Ktoe7lJuBXIHuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe8Gne3"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423271,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423271,
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
  "id": -576460752303423270,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423270,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBH7SZvPU90UEhZ8d2jeM++fXP9IMCNCXR3lpRov3K16zbnA/KaJvTHBFW2mROef8sv6WpNbx59UulBeUAq85QLuECghnh9w8CCDu21XWL8FzFqYT4p8yWcXXyI8qEiVoXLz9gUwN4CKSnbomOLR3QxyGdnIPk2YuS8Ktoe7lJuBXIHuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe8Gne3",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423269,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423269,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuBROHsmTP98le1n5XxdLm4KroeAr/7d/haeaLN9Ii5nA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7nW6mvU=",
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
  "id": -576460752303423268,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDeOSDlVQTV9quYsmijQkEur6VxOt9/oaj+xghLDmjPP6tg//f/QNvJhtI3xbsKsrcrKHef+H4v1BR2kOAlwhcCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5j4/9D"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423268,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDeOSDlVQTV9quYsmijQkEur6VxOt9/oaj+xghLDmjPP6tg//f/QNvJhtI3xbsKsrcrKHef+H4v1BR2kOAlwhcCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5j4/9D",
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
  "id": -576460752303423267,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAfuM0arWlVHmS9keMq40XSJHjY09JdCUngoo/Yqua9zzYZHfKTrL2VhBP6frqPTFiKkjgoqQYXw6Cjv+/4WygAuEDeOSDlVQTV9quYsmijQkEur6VxOt9/oaj+xghLDmjPP6tg//f/QNvJhtI3xbsKsrcrKHef+H4v1BR2kOAlwhcCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5rbZlG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423267,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEAfuM0arWlVHmS9keMq40XSJHjY09JdCUngoo/Yqua9zzYZHfKTrL2VhBP6frqPTFiKkjgoqQYXw6Cjv+/4WygAuEDeOSDlVQTV9quYsmijQkEur6VxOt9/oaj+xghLDmjPP6tg//f/QNvJhtI3xbsKsrcrKHef+H4v1BR2kOAlwhcCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5rbZlG"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEAfuM0arWlVHmS9keMq40XSJHjY09JdCUngoo/Yqua9zzYZHfKTrL2VhBP6frqPTFiKkjgoqQYXw6Cjv+/4WygAuEDeOSDlVQTV9quYsmijQkEur6VxOt9/oaj+xghLDmjPP6tg//f/QNvJhtI3xbsKsrcrKHef+H4v1BR2kOAlwhcCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5rbZlG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423266,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423266,
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
  "id": -576460752303423265,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423265,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAfuM0arWlVHmS9keMq40XSJHjY09JdCUngoo/Yqua9zzYZHfKTrL2VhBP6frqPTFiKkjgoqQYXw6Cjv+/4WygAuEDeOSDlVQTV9quYsmijQkEur6VxOt9/oaj+xghLDmjPP6tg//f/QNvJhtI3xbsKsrcrKHef+H4v1BR2kOAlwhcCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5rbZlG",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423264,
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

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423264,
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

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuBROHsmTP98le1n5XxdLm4KroeAr/7d/haeaLN9Ii5nBKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3toLLKvU=",
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
  "id": -576460752303423263,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBxjpJSPWTW5PhnPQKJ3oZLo6xpursAcI3xbWZGaSk+06LhYYbJlU/RdCxXeRbF2cAWgxhGw4x78u1sxC7wl7AJuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7avWqrj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423263,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBxjpJSPWTW5PhnPQKJ3oZLo6xpursAcI3xbWZGaSk+06LhYYbJlU/RdCxXeRbF2cAWgxhGw4x78u1sxC7wl7AJuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7avWqrj",
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
  "id": -576460752303423262,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBxjpJSPWTW5PhnPQKJ3oZLo6xpursAcI3xbWZGaSk+06LhYYbJlU/RdCxXeRbF2cAWgxhGw4x78u1sxC7wl7AJuEChJCmlKbcuF1KCrzRRh9SFmxYsTEMNDs624hhOrbsNoQNgq3yBhMUlHm5V7yBTDhBUXtEvDEtnZ/XHu1VZIhQCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Ym5jv5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423262,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEBxjpJSPWTW5PhnPQKJ3oZLo6xpursAcI3xbWZGaSk+06LhYYbJlU/RdCxXeRbF2cAWgxhGw4x78u1sxC7wl7AJuEChJCmlKbcuF1KCrzRRh9SFmxYsTEMNDs624hhOrbsNoQNgq3yBhMUlHm5V7yBTDhBUXtEvDEtnZ/XHu1VZIhQCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Ym5jv5"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEBxjpJSPWTW5PhnPQKJ3oZLo6xpursAcI3xbWZGaSk+06LhYYbJlU/RdCxXeRbF2cAWgxhGw4x78u1sxC7wl7AJuEChJCmlKbcuF1KCrzRRh9SFmxYsTEMNDs624hhOrbsNoQNgq3yBhMUlHm5V7yBTDhBUXtEvDEtnZ/XHu1VZIhQCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Ym5jv5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423261,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423261,
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
  "id": -576460752303423260,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423260,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBxjpJSPWTW5PhnPQKJ3oZLo6xpursAcI3xbWZGaSk+06LhYYbJlU/RdCxXeRbF2cAWgxhGw4x78u1sxC7wl7AJuEChJCmlKbcuF1KCrzRRh9SFmxYsTEMNDs624hhOrbsNoQNgq3yBhMUlHm5V7yBTDhBUXtEvDEtnZ/XHu1VZIhQCuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Ym5jv5",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423259,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423259,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuBROHsmTP98le1n5XxdLm4KroeAr/7d/haeaLN9Ii5nBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ir/URY=",
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
  "id": -576460752303423258,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAqX8HN8NrAnKYaS97k26+TNma6Bt9khWDkhk3PgfIh2vwHYFAOERr/ILEiq/ycWaz76hNwZeShnN/dcnXQ49kAuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6g/HGK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423258,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAqX8HN8NrAnKYaS97k26+TNma6Bt9khWDkhk3PgfIh2vwHYFAOERr/ILEiq/ycWaz76hNwZeShnN/dcnXQ49kAuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6g/HGK",
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
  "id": -576460752303423257,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAqX8HN8NrAnKYaS97k26+TNma6Bt9khWDkhk3PgfIh2vwHYFAOERr/ILEiq/ycWaz76hNwZeShnN/dcnXQ49kAuECV69FbuxsZUxhDlBcQ2rQc3H33jBH9GelwgWta2iyWby2LM8KosSNHP3WWgN6rQgEh6MNKzvfCdBrYNcJJF64CuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7Mu8wt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423257,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEAqX8HN8NrAnKYaS97k26+TNma6Bt9khWDkhk3PgfIh2vwHYFAOERr/ILEiq/ycWaz76hNwZeShnN/dcnXQ49kAuECV69FbuxsZUxhDlBcQ2rQc3H33jBH9GelwgWta2iyWby2LM8KosSNHP3WWgN6rQgEh6MNKzvfCdBrYNcJJF64CuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7Mu8wt"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEAqX8HN8NrAnKYaS97k26+TNma6Bt9khWDkhk3PgfIh2vwHYFAOERr/ILEiq/ycWaz76hNwZeShnN/dcnXQ49kAuECV69FbuxsZUxhDlBcQ2rQc3H33jBH9GelwgWta2iyWby2LM8KosSNHP3WWgN6rQgEh6MNKzvfCdBrYNcJJF64CuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7Mu8wt"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423256,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423256,
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
  "id": -576460752303423255,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423255,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAqX8HN8NrAnKYaS97k26+TNma6Bt9khWDkhk3PgfIh2vwHYFAOERr/ILEiq/ycWaz76hNwZeShnN/dcnXQ49kAuECV69FbuxsZUxhDlBcQ2rQc3H33jBH9GelwgWta2iyWby2LM8KosSNHP3WWgN6rQgEh6MNKzvfCdBrYNcJJF64CuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7Mu8wt",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423254,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423254,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuBROHsmTP98le1n5XxdLm4KroeAr/7d/haeaLN9Ii5nBqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tg5I2OY=",
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
  "id": -576460752303423253,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDxoq82h9Xe4ZDpCUeDWQ1uWjL+He4C6EbKst6m5Rzn+RdZRi+AmcS3Oc0BBSbB1VmEDhDMHEUvZojvkAbz/M0GuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bJT+o5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423253,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDxoq82h9Xe4ZDpCUeDWQ1uWjL+He4C6EbKst6m5Rzn+RdZRi+AmcS3Oc0BBSbB1VmEDhDMHEUvZojvkAbz/M0GuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bJT+o5",
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
  "id": -576460752303423252,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBefzgPfOs8K7bgHBevHjULVVFEdXggBF2tJ42JX/yWKu8wQuganN4hRU1/KWkzyQShvWV6av1V1k8vWqcU5i8FuEDxoq82h9Xe4ZDpCUeDWQ1uWjL+He4C6EbKst6m5Rzn+RdZRi+AmcS3Oc0BBSbB1VmEDhDMHEUvZojvkAbz/M0GuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZsgiUd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423252,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEBefzgPfOs8K7bgHBevHjULVVFEdXggBF2tJ42JX/yWKu8wQuganN4hRU1/KWkzyQShvWV6av1V1k8vWqcU5i8FuEDxoq82h9Xe4ZDpCUeDWQ1uWjL+He4C6EbKst6m5Rzn+RdZRi+AmcS3Oc0BBSbB1VmEDhDMHEUvZojvkAbz/M0GuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZsgiUd"
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "state": "tx_+NILAfiEuEBefzgPfOs8K7bgHBevHjULVVFEdXggBF2tJ42JX/yWKu8wQuganN4hRU1/KWkzyQShvWV6av1V1k8vWqcU5i8FuEDxoq82h9Xe4ZDpCUeDWQ1uWjL+He4C6EbKst6m5Rzn+RdZRi+AmcS3Oc0BBSbB1VmEDhDMHEUvZojvkAbz/M0GuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZsgiUd"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423251,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423251,
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
  "id": -576460752303423250,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423250,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBefzgPfOs8K7bgHBevHjULVVFEdXggBF2tJ42JX/yWKu8wQuganN4hRU1/KWkzyQShvWV6av1V1k8vWqcU5i8FuEDxoq82h9Xe4ZDpCUeDWQ1uWjL+He4C6EbKst6m5Rzn+RdZRi+AmcS3Oc0BBSbB1VmEDhDMHEUvZojvkAbz/M0GuEj4RjkCoQbgUTh7Jkz/fJXtZ+V8XS5uCq6HgK/+3f4WnmizfSIuZwagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZsgiUd",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423249,
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
  "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
  "id": -576460752303423249,
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
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
    "channel_id": "ch_2hntFFjL2z2RsSiq7m7CqwKULSfzK8Y8DX93CsvrsSHmvBWo64",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423248,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection
