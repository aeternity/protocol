
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
      "fsm_id": "ba_9U4zmKoFq5z++6y7hwbCFQemFGTTJUzuokF5OVYSZyZ5ODWA"
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
      "fsm_id": "ba_POd3QKCDDYREyk6rUY7d/8kmad7ej1VLKDrOfgHYfSVQmArk"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4DLALqqw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423456,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAGe+jv4gduhU6G7rfxuEFVDnpC29PDphcLR710fmSdgfYH8Mk9H3hnhU+94ldq7Tk1uhhSkYzBqNUTAwino9kIuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uA9OEYi0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423456,
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
      "signed_tx": "tx_+MsLAfhCuEAGe+jv4gduhU6G7rfxuEFVDnpC29PDphcLR710fmSdgfYH8Mk9H3hnhU+94ldq7Tk1uhhSkYzBqNUTAwino9kIuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uA9OEYi0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423455,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhABnvo7+IHboVOhu638bhBVQ56QtvTw6YXC0e9dH5knYH2B/DJPR94Z4VPveJXau05NboYUpGMwajVEwMIp6PZCLhAG9veUM7O2ER8JrzqLiBtLEei+JugbdYdJc2/0J88xBRerV+gViFxb57Mxh63FnhMWfmsgVMJ8R6W8WBUbkxUALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gO+ESRP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423455,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhABnvo7+IHboVOhu638bhBVQ56QtvTw6YXC0e9dH5knYH2B/DJPR94Z4VPveJXau05NboYUpGMwajVEwMIp6PZCLhAG9veUM7O2ER8JrzqLiBtLEei+JugbdYdJc2/0J88xBRerV+gViFxb57Mxh63FnhMWfmsgVMJ8R6W8WBUbkxUALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gO+ESRP",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhABnvo7+IHboVOhu638bhBVQ56QtvTw6YXC0e9dH5knYH2B/DJPR94Z4VPveJXau05NboYUpGMwajVEwMIp6PZCLhAG9veUM7O2ER8JrzqLiBtLEei+JugbdYdJc2/0J88xBRerV+gViFxb57Mxh63FnhMWfmsgVMJ8R6W8WBUbkxUALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gO+ESRP",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABnvo7+IHboVOhu638bhBVQ56QtvTw6YXC0e9dH5knYH2B/DJPR94Z4VPveJXau05NboYUpGMwajVEwMIp6PZCLhAG9veUM7O2ER8JrzqLiBtLEei+JugbdYdJc2/0J88xBRerV+gViFxb57Mxh63FnhMWfmsgVMJ8R6W8WBUbkxUALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gO+ESRP",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABnvo7+IHboVOhu638bhBVQ56QtvTw6YXC0e9dH5knYH2B/DJPR94Z4VPveJXau05NboYUpGMwajVEwMIp6PZCLhAG9veUM7O2ER8JrzqLiBtLEei+JugbdYdJc2/0J88xBRerV+gViFxb57Mxh63FnhMWfmsgVMJ8R6W8WBUbkxUALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gO+ESRP",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "message": {
        "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "message": {
        "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "id": -576460752303423454,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423454,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+QENCwH4hLhABnvo7+IHboVOhu638bhBVQ56QtvTw6YXC0e9dH5knYH2B/DJPR94Z4VPveJXau05NboYUpGMwajVEwMIp6PZCLhAG9veUM7O2ER8JrzqLiBtLEei+JugbdYdJc2/0J88xBRerV+gViFxb57Mxh63FnhMWfmsgVMJ8R6W8WBUbkxUALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gO+ESRP"
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+QENCwH4hLhABnvo7+IHboVOhu638bhBVQ56QtvTw6YXC0e9dH5knYH2B/DJPR94Z4VPveJXau05NboYUpGMwajVEwMIp6PZCLhAG9veUM7O2ER8JrzqLiBtLEei+JugbdYdJc2/0J88xBRerV+gViFxb57Mxh63FnhMWfmsgVMJ8R6W8WBUbkxUALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gO+ESRP"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423453,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423453,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsYOib0i9naoJOsiaf1U8ztgcJV2UMJ5j7VQNKXLqqEsAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B91qeXI=",
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
  "id": -576460752303423452,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAyfkjypz6QLs0hL51LFFJGP4givXk+tz/P63LtV0CQCL1QsOj10WMMUgtFDdL2M7MV1FedGjMtUmQcUkHrWbEHuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAetcNt9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423452,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAyfkjypz6QLs0hL51LFFJGP4givXk+tz/P63LtV0CQCL1QsOj10WMMUgtFDdL2M7MV1FedGjMtUmQcUkHrWbEHuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAetcNt9",
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
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAyfkjypz6QLs0hL51LFFJGP4givXk+tz/P63LtV0CQCL1QsOj10WMMUgtFDdL2M7MV1FedGjMtUmQcUkHrWbEHuEA7qOdRDroVaEHJYQq/msUEVX1H20HyE54C8/4JpCqEV1mGqtf5Jm1XsYVXUc9B0tt+XcGPdoIUEEdgyVgJj/AMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeqxmeX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423451,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEAyfkjypz6QLs0hL51LFFJGP4givXk+tz/P63LtV0CQCL1QsOj10WMMUgtFDdL2M7MV1FedGjMtUmQcUkHrWbEHuEA7qOdRDroVaEHJYQq/msUEVX1H20HyE54C8/4JpCqEV1mGqtf5Jm1XsYVXUc9B0tt+XcGPdoIUEEdgyVgJj/AMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeqxmeX"
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEAyfkjypz6QLs0hL51LFFJGP4givXk+tz/P63LtV0CQCL1QsOj10WMMUgtFDdL2M7MV1FedGjMtUmQcUkHrWbEHuEA7qOdRDroVaEHJYQq/msUEVX1H20HyE54C8/4JpCqEV1mGqtf5Jm1XsYVXUc9B0tt+XcGPdoIUEEdgyVgJj/AMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeqxmeX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423450,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423450,
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
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAyfkjypz6QLs0hL51LFFJGP4givXk+tz/P63LtV0CQCL1QsOj10WMMUgtFDdL2M7MV1FedGjMtUmQcUkHrWbEHuEA7qOdRDroVaEHJYQq/msUEVX1H20HyE54C8/4JpCqEV1mGqtf5Jm1XsYVXUc9B0tt+XcGPdoIUEEdgyVgJj/AMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeqxmeX",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423448,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423448,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsYOib0i9naoJOsiaf1U8ztgcJV2UMJ5j7VQNKXLqqEsA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7krmaXQ=",
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
  "id": -576460752303423447,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED6Vpi8R1QojNLTl5bwx4gB/994RB+BbULwFIDv9CgnglP41kPYymOj+1pT3SwblA2g4GP9VhTe3B8mhbtOTqcMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5urh74"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423447,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+JALAfhCuED6Vpi8R1QojNLTl5bwx4gB/994RB+BbULwFIDv9CgnglP41kPYymOj+1pT3SwblA2g4GP9VhTe3B8mhbtOTqcMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5urh74",
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
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBDUo0lpFMNtWTj0lTqOgC2VfvEFnwHBY239brSjPINj1gchEMZT7GlfuznnXOEyiFmzyU6Y8r7+A2TtHcWhY4GuED6Vpi8R1QojNLTl5bwx4gB/994RB+BbULwFIDv9CgnglP41kPYymOj+1pT3SwblA2g4GP9VhTe3B8mhbtOTqcMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7Rzk98"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423446,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEBDUo0lpFMNtWTj0lTqOgC2VfvEFnwHBY239brSjPINj1gchEMZT7GlfuznnXOEyiFmzyU6Y8r7+A2TtHcWhY4GuED6Vpi8R1QojNLTl5bwx4gB/994RB+BbULwFIDv9CgnglP41kPYymOj+1pT3SwblA2g4GP9VhTe3B8mhbtOTqcMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7Rzk98"
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEBDUo0lpFMNtWTj0lTqOgC2VfvEFnwHBY239brSjPINj1gchEMZT7GlfuznnXOEyiFmzyU6Y8r7+A2TtHcWhY4GuED6Vpi8R1QojNLTl5bwx4gB/994RB+BbULwFIDv9CgnglP41kPYymOj+1pT3SwblA2g4GP9VhTe3B8mhbtOTqcMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7Rzk98"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423445,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423445,
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
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBDUo0lpFMNtWTj0lTqOgC2VfvEFnwHBY239brSjPINj1gchEMZT7GlfuznnXOEyiFmzyU6Y8r7+A2TtHcWhY4GuED6Vpi8R1QojNLTl5bwx4gB/994RB+BbULwFIDv9CgnglP41kPYymOj+1pT3SwblA2g4GP9VhTe3B8mhbtOTqcMuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7Rzk98",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423443,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423443,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsYOib0i9naoJOsiaf1U8ztgcJV2UMJ5j7VQNKXLqqEsBKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tsCNb00=",
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
  "id": -576460752303423442,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBj577Bb8YvHJ2iGeoT4FYKBddXXQD0DL3GL1+0+XE/ObMBq77R6JK/zf5+Q7SQA2XfSk4PouwFqMgWihC6b4oPuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7a596s0"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423442,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBj577Bb8YvHJ2iGeoT4FYKBddXXQD0DL3GL1+0+XE/ObMBq77R6JK/zf5+Q7SQA2XfSk4PouwFqMgWihC6b4oPuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7a596s0",
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
  "id": -576460752303423441,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBj577Bb8YvHJ2iGeoT4FYKBddXXQD0DL3GL1+0+XE/ObMBq77R6JK/zf5+Q7SQA2XfSk4PouwFqMgWihC6b4oPuEDCK/AJa74JjeMKRE09JRLXbGay+oQE7Q4o4pBpMvwcpFGMjxVO6UZfrH7aPJ/jparUwzEJIU2HTCkJJ3FJJCgEuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bO8wiU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423441,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEBj577Bb8YvHJ2iGeoT4FYKBddXXQD0DL3GL1+0+XE/ObMBq77R6JK/zf5+Q7SQA2XfSk4PouwFqMgWihC6b4oPuEDCK/AJa74JjeMKRE09JRLXbGay+oQE7Q4o4pBpMvwcpFGMjxVO6UZfrH7aPJ/jparUwzEJIU2HTCkJJ3FJJCgEuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bO8wiU"
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEBj577Bb8YvHJ2iGeoT4FYKBddXXQD0DL3GL1+0+XE/ObMBq77R6JK/zf5+Q7SQA2XfSk4PouwFqMgWihC6b4oPuEDCK/AJa74JjeMKRE09JRLXbGay+oQE7Q4o4pBpMvwcpFGMjxVO6UZfrH7aPJ/jparUwzEJIU2HTCkJJ3FJJCgEuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bO8wiU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423440,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423440,
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
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBj577Bb8YvHJ2iGeoT4FYKBddXXQD0DL3GL1+0+XE/ObMBq77R6JK/zf5+Q7SQA2XfSk4PouwFqMgWihC6b4oPuEDCK/AJa74JjeMKRE09JRLXbGay+oQE7Q4o4pBpMvwcpFGMjxVO6UZfrH7aPJ/jparUwzEJIU2HTCkJJ3FJJCgEuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bO8wiU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423438,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423438,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsYOib0i9naoJOsiaf1U8ztgcJV2UMJ5j7VQNKXLqqEsBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7g45JOs=",
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
  "id": -576460752303423437,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBP1il7u/EB3cStLtG6Ti/8Gd74hr2k5dGzI8oZZ+2l8z8akPVZlQ4hVkRAMtUeB5UsXlzIQe0VMu+Bqol/oHQHuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4tCBe/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423437,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBP1il7u/EB3cStLtG6Ti/8Gd74hr2k5dGzI8oZZ+2l8z8akPVZlQ4hVkRAMtUeB5UsXlzIQe0VMu+Bqol/oHQHuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4tCBe/",
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
  "id": -576460752303423436,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBP1il7u/EB3cStLtG6Ti/8Gd74hr2k5dGzI8oZZ+2l8z8akPVZlQ4hVkRAMtUeB5UsXlzIQe0VMu+Bqol/oHQHuEDr7tKRqDhvbO425ujhkydeG73/Q5oKJQVM9GMCHl724imfQ//L9H66Fg/A9Q7BmSdCmJgxjQBqsAe0kbIOqfQPuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+56AxcK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423436,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEBP1il7u/EB3cStLtG6Ti/8Gd74hr2k5dGzI8oZZ+2l8z8akPVZlQ4hVkRAMtUeB5UsXlzIQe0VMu+Bqol/oHQHuEDr7tKRqDhvbO425ujhkydeG73/Q5oKJQVM9GMCHl724imfQ//L9H66Fg/A9Q7BmSdCmJgxjQBqsAe0kbIOqfQPuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+56AxcK"
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEBP1il7u/EB3cStLtG6Ti/8Gd74hr2k5dGzI8oZZ+2l8z8akPVZlQ4hVkRAMtUeB5UsXlzIQe0VMu+Bqol/oHQHuEDr7tKRqDhvbO425ujhkydeG73/Q5oKJQVM9GMCHl724imfQ//L9H66Fg/A9Q7BmSdCmJgxjQBqsAe0kbIOqfQPuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+56AxcK"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423435,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423435,
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
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBP1il7u/EB3cStLtG6Ti/8Gd74hr2k5dGzI8oZZ+2l8z8akPVZlQ4hVkRAMtUeB5UsXlzIQe0VMu+Bqol/oHQHuEDr7tKRqDhvbO425ujhkydeG73/Q5oKJQVM9GMCHl724imfQ//L9H66Fg/A9Q7BmSdCmJgxjQBqsAe0kbIOqfQPuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+56AxcK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423433,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423433,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsYOib0i9naoJOsiaf1U8ztgcJV2UMJ5j7VQNKXLqqEsBqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tldbqew=",
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
  "id": -576460752303423432,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECVjTaZtSMdT8Jqwj0BKCYCxJ2LAK3xpRb/lxmmCLI+3nl9NvJ9kLSKh4efZUTDnta+BRY7n24zL2ucOjEP/AQIuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Z6nqd1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423432,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "signed_tx": "tx_+JALAfhCuECVjTaZtSMdT8Jqwj0BKCYCxJ2LAK3xpRb/lxmmCLI+3nl9NvJ9kLSKh4efZUTDnta+BRY7n24zL2ucOjEP/AQIuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Z6nqd1",
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
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAfu3nu5A3io08yQQjkwQ6P5eHwpH4nMBWO05nEBaBgEA59+pWcFQ1prQyMaCl9lj8bfiZtW9lQ0V9tsmQ8yCcOuECVjTaZtSMdT8Jqwj0BKCYCxJ2LAK3xpRb/lxmmCLI+3nl9NvJ9kLSKh4efZUTDnta+BRY7n24zL2ucOjEP/AQIuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YSn20l"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423431,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEAfu3nu5A3io08yQQjkwQ6P5eHwpH4nMBWO05nEBaBgEA59+pWcFQ1prQyMaCl9lj8bfiZtW9lQ0V9tsmQ8yCcOuECVjTaZtSMdT8Jqwj0BKCYCxJ2LAK3xpRb/lxmmCLI+3nl9NvJ9kLSKh4efZUTDnta+BRY7n24zL2ucOjEP/AQIuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YSn20l"
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
    "data": {
      "state": "tx_+NILAfiEuEAfu3nu5A3io08yQQjkwQ6P5eHwpH4nMBWO05nEBaBgEA59+pWcFQ1prQyMaCl9lj8bfiZtW9lQ0V9tsmQ8yCcOuECVjTaZtSMdT8Jqwj0BKCYCxJ2LAK3xpRb/lxmmCLI+3nl9NvJ9kLSKh4efZUTDnta+BRY7n24zL2ucOjEP/AQIuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YSn20l"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423430,
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423430,
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
  "id": -576460752303423429,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423429,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAfu3nu5A3io08yQQjkwQ6P5eHwpH4nMBWO05nEBaBgEA59+pWcFQ1prQyMaCl9lj8bfiZtW9lQ0V9tsmQ8yCcOuECVjTaZtSMdT8Jqwj0BKCYCxJ2LAK3xpRb/lxmmCLI+3nl9NvJ9kLSKh4efZUTDnta+BRY7n24zL2ucOjEP/AQIuEj4RjkCoQbGDom9IvZ2qCTrImn9VPM7YHCVdlDCeY+1UDSly6qhLAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YSn20l",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423428,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
  "id": -576460752303423428,
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
    "channel_id": "ch_2WE6W7RNfSgvey2vBocBjQE916eEAEbZaBG4h7st4cyaowYrWj",
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
  "id": -576460752303423427,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection
