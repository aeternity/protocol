
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
      "fsm_id": "ba_lVecLom9tWc1qQCKWHPJxwW1/z+Co+yd/9oaNiQPtQILnNy6"
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
      "fsm_id": "ba_D7uRiTEPD7o+z7pgjpZVX0PpOWDgjaB+PS0Yqov5CmGs3yS1"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4c9jxO0A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423141,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDB4vKCfQdbtvmpXcLKCUPCn1MwzJWsdz27WCDWcAfUwhJkVBYhzJsmIj+1ygaVepFE5F7o7a3fhe+S1Xw9FdgMuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uHBkH1zY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423141,
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
      "signed_tx": "tx_+MsLAfhCuEDB4vKCfQdbtvmpXcLKCUPCn1MwzJWsdz27WCDWcAfUwhJkVBYhzJsmIj+1ygaVepFE5F7o7a3fhe+S1Xw9FdgMuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uHBkH1zY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423140,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAc8Zu76QkA3KTPPj14JazTizMT+JImu8OVU/ovR8YHWZgLdtJpDxIdZnAfsoswkUB3lb9B19XtevnODBHq+vzArhAweLygn0HW7b5qV3CyglDwp9TMMyVrHc9u1gg1nAH1MISZFQWIcybJiI/tcoGlXqRRORe6O2t34XvktV8PRXYDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hz33kAw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423140,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAc8Zu76QkA3KTPPj14JazTizMT+JImu8OVU/ovR8YHWZgLdtJpDxIdZnAfsoswkUB3lb9B19XtevnODBHq+vzArhAweLygn0HW7b5qV3CyglDwp9TMMyVrHc9u1gg1nAH1MISZFQWIcybJiI/tcoGlXqRRORe6O2t34XvktV8PRXYDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hz33kAw",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAc8Zu76QkA3KTPPj14JazTizMT+JImu8OVU/ovR8YHWZgLdtJpDxIdZnAfsoswkUB3lb9B19XtevnODBHq+vzArhAweLygn0HW7b5qV3CyglDwp9TMMyVrHc9u1gg1nAH1MISZFQWIcybJiI/tcoGlXqRRORe6O2t34XvktV8PRXYDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hz33kAw",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAc8Zu76QkA3KTPPj14JazTizMT+JImu8OVU/ovR8YHWZgLdtJpDxIdZnAfsoswkUB3lb9B19XtevnODBHq+vzArhAweLygn0HW7b5qV3CyglDwp9TMMyVrHc9u1gg1nAH1MISZFQWIcybJiI/tcoGlXqRRORe6O2t34XvktV8PRXYDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hz33kAw",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAc8Zu76QkA3KTPPj14JazTizMT+JImu8OVU/ovR8YHWZgLdtJpDxIdZnAfsoswkUB3lb9B19XtevnODBHq+vzArhAweLygn0HW7b5qV3CyglDwp9TMMyVrHc9u1gg1nAH1MISZFQWIcybJiI/tcoGlXqRRORe6O2t34XvktV8PRXYDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hz33kAw",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
  "id": -576460752303423139,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423139,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+QENCwH4hLhAc8Zu76QkA3KTPPj14JazTizMT+JImu8OVU/ovR8YHWZgLdtJpDxIdZnAfsoswkUB3lb9B19XtevnODBHq+vzArhAweLygn0HW7b5qV3CyglDwp9TMMyVrHc9u1gg1nAH1MISZFQWIcybJiI/tcoGlXqRRORe6O2t34XvktV8PRXYDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hz33kAw"
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+QENCwH4hLhAc8Zu76QkA3KTPPj14JazTizMT+JImu8OVU/ovR8YHWZgLdtJpDxIdZnAfsoswkUB3lb9B19XtevnODBHq+vzArhAweLygn0HW7b5qV3CyglDwp9TMMyVrHc9u1gg1nAH1MISZFQWIcybJiI/tcoGlXqRRORe6O2t34XvktV8PRXYDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hz33kAw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423138,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423138,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmV3F8qHwm7xU8x22yKQLWC+6gL8XPoMYX+53e5gtWpBAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B0MjwL0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423137,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBMdNsizPQEKgukZ9HQFH61JLpOQ+Hrh5FLBlF/GU8NSu0sJwoaR8aSqurGS9r85+ScnZ5ySdxLx4frav9+i2QAuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcvi2mO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423137,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBMdNsizPQEKgukZ9HQFH61JLpOQ+Hrh5FLBlF/GU8NSu0sJwoaR8aSqurGS9r85+ScnZ5ySdxLx4frav9+i2QAuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcvi2mO",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423136,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBMdNsizPQEKgukZ9HQFH61JLpOQ+Hrh5FLBlF/GU8NSu0sJwoaR8aSqurGS9r85+ScnZ5ySdxLx4frav9+i2QAuEDPxHRL8BFUACLuDnOY8+76wANJmr/15LX9pCGQb9G8CZiQz2fncMHRb0F06KgQD1zd+GkQ2rFzLZDUJtYMtSkBuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdSPJNO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423136,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEBMdNsizPQEKgukZ9HQFH61JLpOQ+Hrh5FLBlF/GU8NSu0sJwoaR8aSqurGS9r85+ScnZ5ySdxLx4frav9+i2QAuEDPxHRL8BFUACLuDnOY8+76wANJmr/15LX9pCGQb9G8CZiQz2fncMHRb0F06KgQD1zd+GkQ2rFzLZDUJtYMtSkBuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdSPJNO"
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEBMdNsizPQEKgukZ9HQFH61JLpOQ+Hrh5FLBlF/GU8NSu0sJwoaR8aSqurGS9r85+ScnZ5ySdxLx4frav9+i2QAuEDPxHRL8BFUACLuDnOY8+76wANJmr/15LX9pCGQb9G8CZiQz2fncMHRb0F06KgQD1zd+GkQ2rFzLZDUJtYMtSkBuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdSPJNO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423135,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423135,
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
  "id": -576460752303423134,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423134,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBMdNsizPQEKgukZ9HQFH61JLpOQ+Hrh5FLBlF/GU8NSu0sJwoaR8aSqurGS9r85+ScnZ5ySdxLx4frav9+i2QAuEDPxHRL8BFUACLuDnOY8+76wANJmr/15LX9pCGQb9G8CZiQz2fncMHRb0F06KgQD1zd+GkQ2rFzLZDUJtYMtSkBuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdSPJNO",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423133,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423133,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmV3F8qHwm7xU8x22yKQLWC+6gL8XPoMYX+53e5gtWpBA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7nLJumg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423132,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAGUZi/JHHC6hwk2CWmb0Ed8G0JUm/BQjFpeSk9y3iDwuFDbwhd0QTLqpGe8Of191ahWfgz2KLhuRbJrvY7lh8MuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7IChIZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423132,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAGUZi/JHHC6hwk2CWmb0Ed8G0JUm/BQjFpeSk9y3iDwuFDbwhd0QTLqpGe8Of191ahWfgz2KLhuRbJrvY7lh8MuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7IChIZ",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423131,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAGUZi/JHHC6hwk2CWmb0Ed8G0JUm/BQjFpeSk9y3iDwuFDbwhd0QTLqpGe8Of191ahWfgz2KLhuRbJrvY7lh8MuEAtTWRrR178ZzMsQKBf7gRuwWx44cqOcssbDlE/IQnDosNdUjKXXQBzZpuznjvXpXenxO7RE5hBblx0IXYVdmgLuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5jkcwG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423131,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEAGUZi/JHHC6hwk2CWmb0Ed8G0JUm/BQjFpeSk9y3iDwuFDbwhd0QTLqpGe8Of191ahWfgz2KLhuRbJrvY7lh8MuEAtTWRrR178ZzMsQKBf7gRuwWx44cqOcssbDlE/IQnDosNdUjKXXQBzZpuznjvXpXenxO7RE5hBblx0IXYVdmgLuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5jkcwG"
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEAGUZi/JHHC6hwk2CWmb0Ed8G0JUm/BQjFpeSk9y3iDwuFDbwhd0QTLqpGe8Of191ahWfgz2KLhuRbJrvY7lh8MuEAtTWRrR178ZzMsQKBf7gRuwWx44cqOcssbDlE/IQnDosNdUjKXXQBzZpuznjvXpXenxO7RE5hBblx0IXYVdmgLuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5jkcwG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423130,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423130,
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
  "id": -576460752303423129,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423129,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAGUZi/JHHC6hwk2CWmb0Ed8G0JUm/BQjFpeSk9y3iDwuFDbwhd0QTLqpGe8Of191ahWfgz2KLhuRbJrvY7lh8MuEAtTWRrR178ZzMsQKBf7gRuwWx44cqOcssbDlE/IQnDosNdUjKXXQBzZpuznjvXpXenxO7RE5hBblx0IXYVdmgLuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5jkcwG",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423128,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423128,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmV3F8qHwm7xU8x22yKQLWC+6gL8XPoMYX+53e5gtWpBBKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3toCVY2c=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423127,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAsnvwxixCY8nSs02jQfaiyQ41j8z4b5rj9Abz2fnwDIpkKOW8ZeE1OU5cGqqqLbKvOjxmXYAIdjvlgwu3rJO0KuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZDRjSf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423127,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAsnvwxixCY8nSs02jQfaiyQ41j8z4b5rj9Abz2fnwDIpkKOW8ZeE1OU5cGqqqLbKvOjxmXYAIdjvlgwu3rJO0KuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZDRjSf",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423126,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAsnvwxixCY8nSs02jQfaiyQ41j8z4b5rj9Abz2fnwDIpkKOW8ZeE1OU5cGqqqLbKvOjxmXYAIdjvlgwu3rJO0KuEDDo6Cfl+oJ36xTlgRoevTDLEIeXPBaauGOA6irOLEAVKACU67smPp8yuKidRkAfZg5itqckAv5WlmaM5bMxV0KuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Zk5HFO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423126,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEAsnvwxixCY8nSs02jQfaiyQ41j8z4b5rj9Abz2fnwDIpkKOW8ZeE1OU5cGqqqLbKvOjxmXYAIdjvlgwu3rJO0KuEDDo6Cfl+oJ36xTlgRoevTDLEIeXPBaauGOA6irOLEAVKACU67smPp8yuKidRkAfZg5itqckAv5WlmaM5bMxV0KuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Zk5HFO"
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEAsnvwxixCY8nSs02jQfaiyQ41j8z4b5rj9Abz2fnwDIpkKOW8ZeE1OU5cGqqqLbKvOjxmXYAIdjvlgwu3rJO0KuEDDo6Cfl+oJ36xTlgRoevTDLEIeXPBaauGOA6irOLEAVKACU67smPp8yuKidRkAfZg5itqckAv5WlmaM5bMxV0KuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Zk5HFO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423125,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423125,
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
  "id": -576460752303423124,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423124,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAsnvwxixCY8nSs02jQfaiyQ41j8z4b5rj9Abz2fnwDIpkKOW8ZeE1OU5cGqqqLbKvOjxmXYAIdjvlgwu3rJO0KuEDDo6Cfl+oJ36xTlgRoevTDLEIeXPBaauGOA6irOLEAVKACU67smPp8yuKidRkAfZg5itqckAv5WlmaM5bMxV0KuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Zk5HFO",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423123,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423123,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmV3F8qHwm7xU8x22yKQLWC+6gL8XPoMYX+53e5gtWpBBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ozERCs=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423122,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAZ1Hm0bVP/JohUERGupez3qRHSruOgHyxL3Osz4DbhQTEMvxvcbmLdA6v/Bl+ewZt4S1aLF4oRpj3QQtbA/CYBuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7bicE9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423122,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAZ1Hm0bVP/JohUERGupez3qRHSruOgHyxL3Osz4DbhQTEMvxvcbmLdA6v/Bl+ewZt4S1aLF4oRpj3QQtbA/CYBuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7bicE9",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423121,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAZ1Hm0bVP/JohUERGupez3qRHSruOgHyxL3Osz4DbhQTEMvxvcbmLdA6v/Bl+ewZt4S1aLF4oRpj3QQtbA/CYBuEDOHaXvlln5tM+/hkwbUVVVmpyjIm4f/7UgXksv7GZWm1g0NMU+ek3AOuxqo50YuUpdTOLTaxu18owwPP8mC1wJuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+79foqm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423121,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEAZ1Hm0bVP/JohUERGupez3qRHSruOgHyxL3Osz4DbhQTEMvxvcbmLdA6v/Bl+ewZt4S1aLF4oRpj3QQtbA/CYBuEDOHaXvlln5tM+/hkwbUVVVmpyjIm4f/7UgXksv7GZWm1g0NMU+ek3AOuxqo50YuUpdTOLTaxu18owwPP8mC1wJuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+79foqm"
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEAZ1Hm0bVP/JohUERGupez3qRHSruOgHyxL3Osz4DbhQTEMvxvcbmLdA6v/Bl+ewZt4S1aLF4oRpj3QQtbA/CYBuEDOHaXvlln5tM+/hkwbUVVVmpyjIm4f/7UgXksv7GZWm1g0NMU+ek3AOuxqo50YuUpdTOLTaxu18owwPP8mC1wJuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+79foqm"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423120,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423120,
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
  "id": -576460752303423119,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423119,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAZ1Hm0bVP/JohUERGupez3qRHSruOgHyxL3Osz4DbhQTEMvxvcbmLdA6v/Bl+ewZt4S1aLF4oRpj3QQtbA/CYBuEDOHaXvlln5tM+/hkwbUVVVmpyjIm4f/7UgXksv7GZWm1g0NMU+ek3AOuxqo50YuUpdTOLTaxu18owwPP8mC1wJuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+79foqm",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423118,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423118,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmV3F8qHwm7xU8x22yKQLWC+6gL8XPoMYX+53e5gtWpBBqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tnMvq18=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423117,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBRqHjGPmJ+p9SdOH/7U9JlFeiWxCbVq5zstk6UZbkoM8EsJ8jjDn05GkciwUTrm2DGNK/JkDvebsJRx9l+utULuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Y+ycVe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423117,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBRqHjGPmJ+p9SdOH/7U9JlFeiWxCbVq5zstk6UZbkoM8EsJ8jjDn05GkciwUTrm2DGNK/JkDvebsJRx9l+utULuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Y+ycVe",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423116,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBRqHjGPmJ+p9SdOH/7U9JlFeiWxCbVq5zstk6UZbkoM8EsJ8jjDn05GkciwUTrm2DGNK/JkDvebsJRx9l+utULuEBa7wJMBW8DtQqVTtfVNqheurjePra/DPahlPEehXYUcpJz0fLRW9cJfZm/4lKu6BwayO+9TbDIR8CKZiw1GYAFuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YDlCP4"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423116,
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEBRqHjGPmJ+p9SdOH/7U9JlFeiWxCbVq5zstk6UZbkoM8EsJ8jjDn05GkciwUTrm2DGNK/JkDvebsJRx9l+utULuEBa7wJMBW8DtQqVTtfVNqheurjePra/DPahlPEehXYUcpJz0fLRW9cJfZm/4lKu6BwayO+9TbDIR8CKZiw1GYAFuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YDlCP4"
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+NILAfiEuEBRqHjGPmJ+p9SdOH/7U9JlFeiWxCbVq5zstk6UZbkoM8EsJ8jjDn05GkciwUTrm2DGNK/JkDvebsJRx9l+utULuEBa7wJMBW8DtQqVTtfVNqheurjePra/DPahlPEehXYUcpJz0fLRW9cJfZm/4lKu6BwayO+9TbDIR8CKZiw1GYAFuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YDlCP4"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423115,
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
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423115,
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
  "id": -576460752303423114,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423114,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBRqHjGPmJ+p9SdOH/7U9JlFeiWxCbVq5zstk6UZbkoM8EsJ8jjDn05GkciwUTrm2DGNK/JkDvebsJRx9l+utULuEBa7wJMBW8DtQqVTtfVNqheurjePra/DPahlPEehXYUcpJz0fLRW9cJfZm/4lKu6BwayO+9TbDIR8CKZiw1GYAFuEj4RjkCoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YDlCP4",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```
