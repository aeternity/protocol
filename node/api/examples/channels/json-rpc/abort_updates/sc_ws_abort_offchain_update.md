
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
      "fsm_id": "ba_Yss4K1YnefEFvR8JrCrD8Cj3NlvPsSt2vtQ74vOm5awCSWFW"
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
      "fsm_id": "ba_62Pg1sxfkC5g0QhHfb0zWMvgpxJjJc44bZjH1Hh8witAWc3F"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+45RStHrw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422895,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECK63ZGJRbgsMcQRQBkBwbE7lNjglBgu1sX58MyqFCcKTdhu2pX2kV16rWNNdLZ7GIvXx5zhovp2tR27K7qYTIPuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uOc4Z9l8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422895,
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
      "signed_tx": "tx_+MsLAfhCuECK63ZGJRbgsMcQRQBkBwbE7lNjglBgu1sX58MyqFCcKTdhu2pX2kV16rWNNdLZ7GIvXx5zhovp2tR27K7qYTIPuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uOc4Z9l8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422894,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAikU+MX8LDuNTjs2D52Irk+e4fEXUYSdCjRIH21X2158r8c2DkbcJ5jJKub40actO7NSgl13uZaVBIyjCk9KlArhAiut2RiUW4LDHEEUAZAcGxO5TY4JQYLtbF+fDMqhQnCk3YbtqV9pFdeq1jTXS2exiL18ec4aL6drUduyu6mEyD7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jk5cLnq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422894,
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAikU+MX8LDuNTjs2D52Irk+e4fEXUYSdCjRIH21X2158r8c2DkbcJ5jJKub40actO7NSgl13uZaVBIyjCk9KlArhAiut2RiUW4LDHEEUAZAcGxO5TY4JQYLtbF+fDMqhQnCk3YbtqV9pFdeq1jTXS2exiL18ec4aL6drUduyu6mEyD7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jk5cLnq",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAikU+MX8LDuNTjs2D52Irk+e4fEXUYSdCjRIH21X2158r8c2DkbcJ5jJKub40actO7NSgl13uZaVBIyjCk9KlArhAiut2RiUW4LDHEEUAZAcGxO5TY4JQYLtbF+fDMqhQnCk3YbtqV9pFdeq1jTXS2exiL18ec4aL6drUduyu6mEyD7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jk5cLnq",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAikU+MX8LDuNTjs2D52Irk+e4fEXUYSdCjRIH21X2158r8c2DkbcJ5jJKub40actO7NSgl13uZaVBIyjCk9KlArhAiut2RiUW4LDHEEUAZAcGxO5TY4JQYLtbF+fDMqhQnCk3YbtqV9pFdeq1jTXS2exiL18ec4aL6drUduyu6mEyD7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jk5cLnq",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAikU+MX8LDuNTjs2D52Irk+e4fEXUYSdCjRIH21X2158r8c2DkbcJ5jJKub40actO7NSgl13uZaVBIyjCk9KlArhAiut2RiUW4LDHEEUAZAcGxO5TY4JQYLtbF+fDMqhQnCk3YbtqV9pFdeq1jTXS2exiL18ec4aL6drUduyu6mEyD7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jk5cLnq",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "message": {
        "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "message": {
        "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
  "id": -576460752303422893,
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
  "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
  "id": -576460752303422893,
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "state": "tx_+QENCwH4hLhAikU+MX8LDuNTjs2D52Irk+e4fEXUYSdCjRIH21X2158r8c2DkbcJ5jJKub40actO7NSgl13uZaVBIyjCk9KlArhAiut2RiUW4LDHEEUAZAcGxO5TY4JQYLtbF+fDMqhQnCk3YbtqV9pFdeq1jTXS2exiL18ec4aL6drUduyu6mEyD7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jk5cLnq"
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "state": "tx_+QENCwH4hLhAikU+MX8LDuNTjs2D52Irk+e4fEXUYSdCjRIH21X2158r8c2DkbcJ5jJKub40actO7NSgl13uZaVBIyjCk9KlArhAiut2RiUW4LDHEEUAZAcGxO5TY4JQYLtbF+fDMqhQnCk3YbtqV9pFdeq1jTXS2exiL18ec4aL6drUduyu6mEyD7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jk5cLnq"
    }
  },
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpc3eaCSvnPbd9LQkfCKpHrlYs8g1uhTm+WSXlVk+3uCAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B6bjRT8=",
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpc3eaCSvnPbd9LQkfCKpHrlYs8g1uhTm+WSXlVk+3uCAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B6bjRT8=",
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpc3eaCSvnPbd9LQkfCKpHrlYs8g1uhTm+WSXlVk+3uCAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B6bjRT8=",
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
  "id": -576460752303422892,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA2ZqUlhhm1KOJ4YDvrLyuRmHH3l3PN5ezNvSKVGet8TkfsRa+Ar4tdSLfCTbfdCdPl3n2X627WzLn+bw0OtkIJuEj4RjkCoQaXN3mgkr5z23fS0JHwiqR65WLPINboU5vlkl5VZPt7ggKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAf0fTcQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
  "id": -576460752303422892,
  "jsonrpc": "2.0",
  "result": "ok",
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
  "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA2ZqUlhhm1KOJ4YDvrLyuRmHH3l3PN5ezNvSKVGet8TkfsRa+Ar4tdSLfCTbfdCdPl3n2X627WzLn+bw0OtkIJuEj4RjkCoQaXN3mgkr5z23fS0JHwiqR65WLPINboU5vlkl5VZPt7ggKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAf0fTcQ",
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
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
  "id": -576460752303422891,
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
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
  "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
  "id": -576460752303422891,
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
    "channel_id": "ch_29bdQNgc9E3XMkFEf3cM2MA4YahPHEZXrDQ23DQdRNtqLvMZ1t",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
