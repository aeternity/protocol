
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
      "fsm_id": "ba_LjdXsIcR8sqVgRLawNV+iBmbq7KGFZdj9UVBYfsrz6py269S"
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
      "fsm_id": "ba_tED8KqO55erXmKZbOQJKBxHy36JAZ48Xs+LE3jaas/cmaDLI"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4GLp+DmQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423391,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDJ3EEn/rhCVwmuAxzvWmzl1KmTLS6Muy+RsEwC38QqfgPOEXOhhnSl4THw+DanTXsPTXHF2BtUp9YOLqBxn9cLuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uBvIiYcU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423391,
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
      "signed_tx": "tx_+MsLAfhCuEDJ3EEn/rhCVwmuAxzvWmzl1KmTLS6Muy+RsEwC38QqfgPOEXOhhnSl4THw+DanTXsPTXHF2BtUp9YOLqBxn9cLuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uBvIiYcU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423390,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAydxBJ/64QlcJrgMc71ps5dSpky0ujLsvkbBMAt/EKn4DzhFzoYZ0peEx8Pg2p017D01xxdgbVKfWDi6gcZ/XC7hA7OcDxLIvgWDCx/Wkx53CZqqOHKeEBJVeOP4p6pm5hDFHgEJNM/hIhxRLYnYM1C7HXqwV+R5i3YgbWPeOAcg2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gaM04aZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423390,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAydxBJ/64QlcJrgMc71ps5dSpky0ujLsvkbBMAt/EKn4DzhFzoYZ0peEx8Pg2p017D01xxdgbVKfWDi6gcZ/XC7hA7OcDxLIvgWDCx/Wkx53CZqqOHKeEBJVeOP4p6pm5hDFHgEJNM/hIhxRLYnYM1C7HXqwV+R5i3YgbWPeOAcg2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gaM04aZ",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAydxBJ/64QlcJrgMc71ps5dSpky0ujLsvkbBMAt/EKn4DzhFzoYZ0peEx8Pg2p017D01xxdgbVKfWDi6gcZ/XC7hA7OcDxLIvgWDCx/Wkx53CZqqOHKeEBJVeOP4p6pm5hDFHgEJNM/hIhxRLYnYM1C7HXqwV+R5i3YgbWPeOAcg2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gaM04aZ",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAydxBJ/64QlcJrgMc71ps5dSpky0ujLsvkbBMAt/EKn4DzhFzoYZ0peEx8Pg2p017D01xxdgbVKfWDi6gcZ/XC7hA7OcDxLIvgWDCx/Wkx53CZqqOHKeEBJVeOP4p6pm5hDFHgEJNM/hIhxRLYnYM1C7HXqwV+R5i3YgbWPeOAcg2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gaM04aZ",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAydxBJ/64QlcJrgMc71ps5dSpky0ujLsvkbBMAt/EKn4DzhFzoYZ0peEx8Pg2p017D01xxdgbVKfWDi6gcZ/XC7hA7OcDxLIvgWDCx/Wkx53CZqqOHKeEBJVeOP4p6pm5hDFHgEJNM/hIhxRLYnYM1C7HXqwV+R5i3YgbWPeOAcg2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gaM04aZ",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "message": {
        "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "message": {
        "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
  "id": -576460752303423389,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423389,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "event": "own_funding_locked"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+QENCwH4hLhAydxBJ/64QlcJrgMc71ps5dSpky0ujLsvkbBMAt/EKn4DzhFzoYZ0peEx8Pg2p017D01xxdgbVKfWDi6gcZ/XC7hA7OcDxLIvgWDCx/Wkx53CZqqOHKeEBJVeOP4p6pm5hDFHgEJNM/hIhxRLYnYM1C7HXqwV+R5i3YgbWPeOAcg2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gaM04aZ"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+QENCwH4hLhAydxBJ/64QlcJrgMc71ps5dSpky0ujLsvkbBMAt/EKn4DzhFzoYZ0peEx8Pg2p017D01xxdgbVKfWDi6gcZ/XC7hA7OcDxLIvgWDCx/Wkx53CZqqOHKeEBJVeOP4p6pm5hDFHgEJNM/hIhxRLYnYM1C7HXqwV+R5i3YgbWPeOAcg2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gaM04aZ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423388,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "error": {
    "code": 2,
    "data": [
      {
        "code": 1012,
        "message": "Offchain tx expected"
      }
    ],
    "message": "Action not allowed",
    "request": {
      "id": -576460752303423388,
      "jsonrpc": "2.0",
      "method": "channels.snapshot_solo",
      "params": {}
    }
  },
  "id": -576460752303423388,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423387,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423387,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B9OepDc=",
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
  "id": -576460752303423386,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAw/1JJSRgIRwxckL0EUwRNIes3OVV3wCSfluPhyxT5qRP5sQqLxxfyp0Gc2agoaTXi9kJDdbT+CXvdL4RAARkCuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeELWry"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423386,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAw/1JJSRgIRwxckL0EUwRNIes3OVV3wCSfluPhyxT5qRP5sQqLxxfyp0Gc2agoaTXi9kJDdbT+CXvdL4RAARkCuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeELWry",
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
  "id": -576460752303423385,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAw/1JJSRgIRwxckL0EUwRNIes3OVV3wCSfluPhyxT5qRP5sQqLxxfyp0Gc2agoaTXi9kJDdbT+CXvdL4RAARkCuEDRky1WJYlIW58E08/QcD4yzfxyKLoEfQQvPNMF+catJdq6H7w6wL6GF+QmcsvADnal76dPpodrpWQ0W6fI1v8FuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdgP9pr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423385,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEAw/1JJSRgIRwxckL0EUwRNIes3OVV3wCSfluPhyxT5qRP5sQqLxxfyp0Gc2agoaTXi9kJDdbT+CXvdL4RAARkCuEDRky1WJYlIW58E08/QcD4yzfxyKLoEfQQvPNMF+catJdq6H7w6wL6GF+QmcsvADnal76dPpodrpWQ0W6fI1v8FuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdgP9pr"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEAw/1JJSRgIRwxckL0EUwRNIes3OVV3wCSfluPhyxT5qRP5sQqLxxfyp0Gc2agoaTXi9kJDdbT+CXvdL4RAARkCuEDRky1WJYlIW58E08/QcD4yzfxyKLoEfQQvPNMF+catJdq6H7w6wL6GF+QmcsvADnal76dPpodrpWQ0W6fI1v8FuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdgP9pr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423384,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423384,
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
  "id": -576460752303423383,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423383,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAw/1JJSRgIRwxckL0EUwRNIes3OVV3wCSfluPhyxT5qRP5sQqLxxfyp0Gc2agoaTXi9kJDdbT+CXvdL4RAARkCuEDRky1WJYlIW58E08/QcD4yzfxyKLoEfQQvPNMF+catJdq6H7w6wL6GF+QmcsvADnal76dPpodrpWQ0W6fI1v8FuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdgP9pr",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423382,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423382,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7nQ8Dso=",
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
  "id": -576460752303423381,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC3yUYNw94XH5OIJ5Gr8jhLiXhO7Dn9pyaKsNBq/N+/ZmGnK+hufjfzcby+fzwO1u49oc0ufVttwYJBe8YuSf8BuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7PiDmG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423381,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC3yUYNw94XH5OIJ5Gr8jhLiXhO7Dn9pyaKsNBq/N+/ZmGnK+hufjfzcby+fzwO1u49oc0ufVttwYJBe8YuSf8BuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7PiDmG",
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
  "id": -576460752303423380,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC3yUYNw94XH5OIJ5Gr8jhLiXhO7Dn9pyaKsNBq/N+/ZmGnK+hufjfzcby+fzwO1u49oc0ufVttwYJBe8YuSf8BuEDAFAPiML+6xSLewH7n1btB6qLLIm12fPacQLYA2iMN/EYuBO1ovQWKOz3rTbXiJUg+APNId00FFc1Vvzf41lQPuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6v8bCa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423380,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEC3yUYNw94XH5OIJ5Gr8jhLiXhO7Dn9pyaKsNBq/N+/ZmGnK+hufjfzcby+fzwO1u49oc0ufVttwYJBe8YuSf8BuEDAFAPiML+6xSLewH7n1btB6qLLIm12fPacQLYA2iMN/EYuBO1ovQWKOz3rTbXiJUg+APNId00FFc1Vvzf41lQPuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6v8bCa"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEC3yUYNw94XH5OIJ5Gr8jhLiXhO7Dn9pyaKsNBq/N+/ZmGnK+hufjfzcby+fzwO1u49oc0ufVttwYJBe8YuSf8BuEDAFAPiML+6xSLewH7n1btB6qLLIm12fPacQLYA2iMN/EYuBO1ovQWKOz3rTbXiJUg+APNId00FFc1Vvzf41lQPuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6v8bCa"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423379,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423379,
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
  "id": -576460752303423378,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423378,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC3yUYNw94XH5OIJ5Gr8jhLiXhO7Dn9pyaKsNBq/N+/ZmGnK+hufjfzcby+fzwO1u49oc0ufVttwYJBe8YuSf8BuEDAFAPiML+6xSLewH7n1btB6qLLIm12fPacQLYA2iMN/EYuBO1ovQWKOz3rTbXiJUg+APNId00FFc1Vvzf41lQPuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6v8bCa",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423377,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423377,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79LjU+NILAfiEuEC3yUYNw94XH5OIJ5Gr8jhLiXhO7Dn9pyaKsNBq/N+/ZmGnK+hufjfzcby+fzwO1u49oc0ufVttwYJBe8YuSf8BuEDAFAPiML+6xSLewH7n1btB6qLLIm12fPacQLYA2iMN/EYuBO1ovQWKOz3rTbXiJUg+APNId00FFc1Vvzf41lQPuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4AhhMG0SswAAdbwYLB",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAMO7VNkPJ4DxH672QtrPfNcR/6vFgbkyeIiUCVIlH1cdBYeUyzWreb0BDcCox5Lac094omQswylnFZj/czFmpArkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAt8lGDcPeFx+TiCeRq/I4S4l4Tuw5/acmirDQavzfv2Zhpyvobn4383G8vn88DtbuPaHNLn1bbcGCQXvGLkn/AbhAwBQD4jC/usUi3sB+59W7QeqiyyJtdnz2nEC2ANojDfxGLgTtaL0Fijs960214iVIPgDzSHdNBRXNVb83+NZUD7hI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4DoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAAHzBQSIg=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423376,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423376,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOBKAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8Byq+6H0=",
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
  "id": -576460752303423375,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECJt4wn61DRsnOl+B4wvLCV3S374o6z6j+LFNIhBwU1BKpVITUU8SKaO5bWc3pUuR2tWQfM4pkotTNBnMVXwVcHuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdVIHSB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423375,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+JALAfhCuECJt4wn61DRsnOl+B4wvLCV3S374o6z6j+LFNIhBwU1BKpVITUU8SKaO5bWc3pUuR2tWQfM4pkotTNBnMVXwVcHuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdVIHSB",
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
  "id": -576460752303423374,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECJt4wn61DRsnOl+B4wvLCV3S374o6z6j+LFNIhBwU1BKpVITUU8SKaO5bWc3pUuR2tWQfM4pkotTNBnMVXwVcHuEDT1f0v+wfeawGQhcgkm+8xOoIPW3zfTRNHqQymmUvk3ifq8U8iRVZ7s3SGS+k2ianSxESvrQnQFWdz5RgrbawCuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcnuovV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423374,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuECJt4wn61DRsnOl+B4wvLCV3S374o6z6j+LFNIhBwU1BKpVITUU8SKaO5bWc3pUuR2tWQfM4pkotTNBnMVXwVcHuEDT1f0v+wfeawGQhcgkm+8xOoIPW3zfTRNHqQymmUvk3ifq8U8iRVZ7s3SGS+k2ianSxESvrQnQFWdz5RgrbawCuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcnuovV"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuECJt4wn61DRsnOl+B4wvLCV3S374o6z6j+LFNIhBwU1BKpVITUU8SKaO5bWc3pUuR2tWQfM4pkotTNBnMVXwVcHuEDT1f0v+wfeawGQhcgkm+8xOoIPW3zfTRNHqQymmUvk3ifq8U8iRVZ7s3SGS+k2ianSxESvrQnQFWdz5RgrbawCuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcnuovV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423373,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423373,
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
  "id": -576460752303423372,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423372,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECJt4wn61DRsnOl+B4wvLCV3S374o6z6j+LFNIhBwU1BKpVITUU8SKaO5bWc3pUuR2tWQfM4pkotTNBnMVXwVcHuEDT1f0v+wfeawGQhcgkm+8xOoIPW3zfTRNHqQymmUvk3ifq8U8iRVZ7s3SGS+k2ianSxESvrQnQFWdz5RgrbawCuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcnuovV",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423371,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423371,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7tbaU/Q=",
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
  "id": -576460752303423370,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDr+hWc0jwrJfeW9ZIojnua4h/tuWLQsr4j2Le5i3spTHVXjba1IClTiqeIZS/3NpnReUsDv1/POzEj1oBZRaEFuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7NvkJx"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423370,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDr+hWc0jwrJfeW9ZIojnua4h/tuWLQsr4j2Le5i3spTHVXjba1IClTiqeIZS/3NpnReUsDv1/POzEj1oBZRaEFuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7NvkJx",
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
  "id": -576460752303423369,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAgCeNiiWzLM/cnnqBUv7vRXbaq1oaWD8Ef51YSkRYbPItrwgWidg6w7Q8Ood5kz83sYM26CgwKz4I/AuHusZgKuEDr+hWc0jwrJfeW9ZIojnua4h/tuWLQsr4j2Le5i3spTHVXjba1IClTiqeIZS/3NpnReUsDv1/POzEj1oBZRaEFuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6Sk48a"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423369,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEAgCeNiiWzLM/cnnqBUv7vRXbaq1oaWD8Ef51YSkRYbPItrwgWidg6w7Q8Ood5kz83sYM26CgwKz4I/AuHusZgKuEDr+hWc0jwrJfeW9ZIojnua4h/tuWLQsr4j2Le5i3spTHVXjba1IClTiqeIZS/3NpnReUsDv1/POzEj1oBZRaEFuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6Sk48a"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEAgCeNiiWzLM/cnnqBUv7vRXbaq1oaWD8Ef51YSkRYbPItrwgWidg6w7Q8Ood5kz83sYM26CgwKz4I/AuHusZgKuEDr+hWc0jwrJfeW9ZIojnua4h/tuWLQsr4j2Le5i3spTHVXjba1IClTiqeIZS/3NpnReUsDv1/POzEj1oBZRaEFuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6Sk48a"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423368,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423368,
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
  "id": -576460752303423367,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423367,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAgCeNiiWzLM/cnnqBUv7vRXbaq1oaWD8Ef51YSkRYbPItrwgWidg6w7Q8Ood5kz83sYM26CgwKz4I/AuHusZgKuEDr+hWc0jwrJfeW9ZIojnua4h/tuWLQsr4j2Le5i3spTHVXjba1IClTiqeIZS/3NpnReUsDv1/POzEj1oBZRaEFuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6Sk48a",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAMO7VNkPJ4DxH672QtrPfNcR/6vFgbkyeIiUCVIlH1cdBYeUyzWreb0BDcCox5Lac094omQswylnFZj/czFmpArkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAt8lGDcPeFx+TiCeRq/I4S4l4Tuw5/acmirDQavzfv2Zhpyvobn4383G8vn88DtbuPaHNLn1bbcGCQXvGLkn/AbhAwBQD4jC/usUi3sB+59W7QeqiyyJtdnz2nEC2ANojDfxGLgTtaL0Fijs960214iVIPgDzSHdNBRXNVb83+NZUD7hI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4DoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAAHzBQSIg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAMO7VNkPJ4DxH672QtrPfNcR/6vFgbkyeIiUCVIlH1cdBYeUyzWreb0BDcCox5Lac094omQswylnFZj/czFmpArkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAt8lGDcPeFx+TiCeRq/I4S4l4Tuw5/acmirDQavzfv2Zhpyvobn4383G8vn88DtbuPaHNLn1bbcGCQXvGLkn/AbhAwBQD4jC/usUi3sB+59W7QeqiyyJtdnz2nEC2ANojDfxGLgTtaL0Fijs960214iVIPgDzSHdNBRXNVb83+NZUD7hI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4DoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAAHzBQSIg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "�\f�b���ͩk�=/3+\u0016��w��G�\u001d�[��Q\\\u0011",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423366,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423366,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROELjU+NILAfiEuEAgCeNiiWzLM/cnnqBUv7vRXbaq1oaWD8Ef51YSkRYbPItrwgWidg6w7Q8Ood5kz83sYM26CgwKz4I/AuHusZgKuEDr+hWc0jwrJfeW9ZIojnua4h/tuWLQsr4j2Le5i3spTHVXjba1IClTiqeIZS/3NpnReUsDv1/POzEj1oBZRaEFuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4AhhMG0SswAAH0oWnV",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAV/hWnb8Sh/IknFVUSLYJSQu8v9+SIqilR/Hd/jqKGxCq2OOostDw/DtGNBeqkqeftz2OT4g9EjTR1fyWINwEDLkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAIAnjYolsyzP3J56gVL+70V22qtaGlg/BH+dWEpEWGzyLa8IFonYOsO0PDqHeZM/N7GDNugoMCs+CPwLh7rGYCrhA6/oVnNI8KyX3lvWSKI57muIf7bli0LK+I9i3uYt7KUx1V422tSApU4qniGUv9zaZ0XlLA79fzzsxI9aAWUWhBbhI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4FoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAABqvLutg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAV/hWnb8Sh/IknFVUSLYJSQu8v9+SIqilR/Hd/jqKGxCq2OOostDw/DtGNBeqkqeftz2OT4g9EjTR1fyWINwEDLkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAIAnjYolsyzP3J56gVL+70V22qtaGlg/BH+dWEpEWGzyLa8IFonYOsO0PDqHeZM/N7GDNugoMCs+CPwLh7rGYCrhA6/oVnNI8KyX3lvWSKI57muIf7bli0LK+I9i3uYt7KUx1V422tSApU4qniGUv9zaZ0XlLA79fzzsxI9aAWUWhBbhI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4FoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAABqvLutg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAV/hWnb8Sh/IknFVUSLYJSQu8v9+SIqilR/Hd/jqKGxCq2OOostDw/DtGNBeqkqeftz2OT4g9EjTR1fyWINwEDLkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAIAnjYolsyzP3J56gVL+70V22qtaGlg/BH+dWEpEWGzyLa8IFonYOsO0PDqHeZM/N7GDNugoMCs+CPwLh7rGYCrhA6/oVnNI8KyX3lvWSKI57muIf7bli0LK+I9i3uYt7KUx1V422tSApU4qniGUv9zaZ0XlLA79fzzsxI9aAWUWhBbhI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4FoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAABqvLutg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "�=�?\"<�\u001b�\u0001�$��^�z����\u0014\u0018[[���Y�",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1013,
        "message": "Tx already on-chain"
      }
    ],
    "message": "Rejected",
    "request": {
      "id": -576460752303423365,
      "jsonrpc": "2.0",
      "method": "channels.snapshot_solo",
      "params": {}
    }
  },
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423364,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423364,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOBqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B8x1rEY=",
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
  "id": -576460752303423363,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBwYOUU32pIxd4dfnjk5TRduBe8Pge87zkJNDJo/k2MjK7xkBBUIvibVWb1C0DEFu1kNuOGVDZH+pPQXpOAo2oOuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAegGdpP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423363,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBwYOUU32pIxd4dfnjk5TRduBe8Pge87zkJNDJo/k2MjK7xkBBUIvibVWb1C0DEFu1kNuOGVDZH+pPQXpOAo2oOuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAegGdpP",
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
  "id": -576460752303423362,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBwYOUU32pIxd4dfnjk5TRduBe8Pge87zkJNDJo/k2MjK7xkBBUIvibVWb1C0DEFu1kNuOGVDZH+pPQXpOAo2oOuEDHtseROGeclzJoBhPorSlYUV0ftD/V2Ptb+tQkDq1UKbexHm46FmUsFSMSCjOhm6n9sF3lLngE7V3Iy7MVCZ8KuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAck05Ja"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423362,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEBwYOUU32pIxd4dfnjk5TRduBe8Pge87zkJNDJo/k2MjK7xkBBUIvibVWb1C0DEFu1kNuOGVDZH+pPQXpOAo2oOuEDHtseROGeclzJoBhPorSlYUV0ftD/V2Ptb+tQkDq1UKbexHm46FmUsFSMSCjOhm6n9sF3lLngE7V3Iy7MVCZ8KuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAck05Ja"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEBwYOUU32pIxd4dfnjk5TRduBe8Pge87zkJNDJo/k2MjK7xkBBUIvibVWb1C0DEFu1kNuOGVDZH+pPQXpOAo2oOuEDHtseROGeclzJoBhPorSlYUV0ftD/V2Ptb+tQkDq1UKbexHm46FmUsFSMSCjOhm6n9sF3lLngE7V3Iy7MVCZ8KuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAck05Ja"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423361,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423361,
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
  "id": -576460752303423360,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423360,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBwYOUU32pIxd4dfnjk5TRduBe8Pge87zkJNDJo/k2MjK7xkBBUIvibVWb1C0DEFu1kNuOGVDZH+pPQXpOAo2oOuEDHtseROGeclzJoBhPorSlYUV0ftD/V2Ptb+tQkDq1UKbexHm46FmUsFSMSCjOhm6n9sF3lLngE7V3Iy7MVCZ8KuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAck05Ja",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423359,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423359,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOB6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jbRhE0=",
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
  "id": -576460752303423358,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDZNKFSuJS1bL1XGqco+j6VN8S0eKX+YcJox1jwL8zOBV0FfcqiuZUw+QyMbuaf+YXS7Fd5EapDQUqBQ35qIxwKuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5BPahR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423358,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDZNKFSuJS1bL1XGqco+j6VN8S0eKX+YcJox1jwL8zOBV0FfcqiuZUw+QyMbuaf+YXS7Fd5EapDQUqBQ35qIxwKuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5BPahR",
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
  "id": -576460752303423357,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBIytJ3WVVOaDHIUg84Os6MMsvTVoK2+Sx2o+fcUrDuQaBcaTW5SpzjJksvm9bq0o60mr0XLADLFGYOuMkiJ1YOuEDZNKFSuJS1bL1XGqco+j6VN8S0eKX+YcJox1jwL8zOBV0FfcqiuZUw+QyMbuaf+YXS7Fd5EapDQUqBQ35qIxwKuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6njnq/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423357,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEBIytJ3WVVOaDHIUg84Os6MMsvTVoK2+Sx2o+fcUrDuQaBcaTW5SpzjJksvm9bq0o60mr0XLADLFGYOuMkiJ1YOuEDZNKFSuJS1bL1XGqco+j6VN8S0eKX+YcJox1jwL8zOBV0FfcqiuZUw+QyMbuaf+YXS7Fd5EapDQUqBQ35qIxwKuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6njnq/"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEBIytJ3WVVOaDHIUg84Os6MMsvTVoK2+Sx2o+fcUrDuQaBcaTW5SpzjJksvm9bq0o60mr0XLADLFGYOuMkiJ1YOuEDZNKFSuJS1bL1XGqco+j6VN8S0eKX+YcJox1jwL8zOBV0FfcqiuZUw+QyMbuaf+YXS7Fd5EapDQUqBQ35qIxwKuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6njnq/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423356,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423356,
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
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBIytJ3WVVOaDHIUg84Os6MMsvTVoK2+Sx2o+fcUrDuQaBcaTW5SpzjJksvm9bq0o60mr0XLADLFGYOuMkiJ1YOuEDZNKFSuJS1bL1XGqco+j6VN8S0eKX+YcJox1jwL8zOBV0FfcqiuZUw+QyMbuaf+YXS7Fd5EapDQUqBQ35qIxwKuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6njnq/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423354,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423354,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROELjU+NILAfiEuEBIytJ3WVVOaDHIUg84Os6MMsvTVoK2+Sx2o+fcUrDuQaBcaTW5SpzjJksvm9bq0o60mr0XLADLFGYOuMkiJ1YOuEDZNKFSuJS1bL1XGqco+j6VN8S0eKX+YcJox1jwL8zOBV0FfcqiuZUw+QyMbuaf+YXS7Fd5EapDQUqBQ35qIxwKuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4AhhMG0SswAAIGnLQr",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAn1UD9b64XPS1x3SA4WfrqdkactUjE369X3UeZbdoC0ofg+qxu7Z9YUPZHNFACHwnZfOqjBn/nocW8anfTRGsBbkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhASMrSd1lVTmgxyFIPODrOjDLL01aCtvksdqPn3FKw7kGgXGk1uUqc4yZLL5vW6tKOtJq9FywAyxRmDrjJIidWDrhA2TShUriUtWy9VxqnKPo+lTfEtHil/mHCaMdY8C/MzgVdBX3KormVMPkMjG7mn/mF0uxXeRGqQ0FKgUN+aiMcCrhI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4HoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAAChdh6ig=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423353,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423353,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOCKAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B2aoxps=",
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
  "id": -576460752303423352,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAd6lTwTW17BDH1xM/diTPtkkExdVkYKxUGwapdKf2j3RhaD8a+91R/PUHLg6WVePUZO/sFcabLEkPKjH/ESnEPuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgigKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfw2vq8"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423352,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAd6lTwTW17BDH1xM/diTPtkkExdVkYKxUGwapdKf2j3RhaD8a+91R/PUHLg6WVePUZO/sFcabLEkPKjH/ESnEPuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgigKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfw2vq8",
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
  "id": -576460752303423351,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAd6lTwTW17BDH1xM/diTPtkkExdVkYKxUGwapdKf2j3RhaD8a+91R/PUHLg6WVePUZO/sFcabLEkPKjH/ESnEPuEDy3Qo+2YIylAW8HQGFjVsgRfRVP7yOfvive6cUHLGpmLu/+JYetzKtheMphsy2Ak2RqejWVwF8NCOQMHeHr84GuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgigKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfhm6kE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423351,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEAd6lTwTW17BDH1xM/diTPtkkExdVkYKxUGwapdKf2j3RhaD8a+91R/PUHLg6WVePUZO/sFcabLEkPKjH/ESnEPuEDy3Qo+2YIylAW8HQGFjVsgRfRVP7yOfvive6cUHLGpmLu/+JYetzKtheMphsy2Ak2RqejWVwF8NCOQMHeHr84GuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgigKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfhm6kE"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEAd6lTwTW17BDH1xM/diTPtkkExdVkYKxUGwapdKf2j3RhaD8a+91R/PUHLg6WVePUZO/sFcabLEkPKjH/ESnEPuEDy3Qo+2YIylAW8HQGFjVsgRfRVP7yOfvive6cUHLGpmLu/+JYetzKtheMphsy2Ak2RqejWVwF8NCOQMHeHr84GuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgigKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfhm6kE"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423350,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423350,
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
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAd6lTwTW17BDH1xM/diTPtkkExdVkYKxUGwapdKf2j3RhaD8a+91R/PUHLg6WVePUZO/sFcabLEkPKjH/ESnEPuEDy3Qo+2YIylAW8HQGFjVsgRfRVP7yOfvive6cUHLGpmLu/+JYetzKtheMphsy2Ak2RqejWVwF8NCOQMHeHr84GuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgigKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfhm6kE",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423348,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423348,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtlTLk1APdmHaziEHEcIBoE7hPShdgfNfwXzK6QenjIOCaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7vTCCwo=",
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
  "id": -576460752303423347,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDrCxo8tAYcWVZpq0CBfYstMqt3ZjkhZd6l2vRcP6bHWNF3pyNUYs7a7XYqTL6aOe0skRBCI/trJq8BmMI5/PcMuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgmgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+76Djrw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423347,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDrCxo8tAYcWVZpq0CBfYstMqt3ZjkhZd6l2vRcP6bHWNF3pyNUYs7a7XYqTL6aOe0skRBCI/trJq8BmMI5/PcMuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgmgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+76Djrw",
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
  "id": -576460752303423346,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC5tYXcetO2wVk6bcdK+XMDQyEsCyWf1cOTv9j8EWgNxIMK13jZ1hdhzhR184xBJElIkICv/Vi38YDS1YBt0KYAuEDrCxo8tAYcWVZpq0CBfYstMqt3ZjkhZd6l2vRcP6bHWNF3pyNUYs7a7XYqTL6aOe0skRBCI/trJq8BmMI5/PcMuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgmgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7DM9tV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423346,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEC5tYXcetO2wVk6bcdK+XMDQyEsCyWf1cOTv9j8EWgNxIMK13jZ1hdhzhR184xBJElIkICv/Vi38YDS1YBt0KYAuEDrCxo8tAYcWVZpq0CBfYstMqt3ZjkhZd6l2vRcP6bHWNF3pyNUYs7a7XYqTL6aOe0skRBCI/trJq8BmMI5/PcMuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgmgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7DM9tV"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "state": "tx_+NILAfiEuEC5tYXcetO2wVk6bcdK+XMDQyEsCyWf1cOTv9j8EWgNxIMK13jZ1hdhzhR184xBJElIkICv/Vi38YDS1YBt0KYAuEDrCxo8tAYcWVZpq0CBfYstMqt3ZjkhZd6l2vRcP6bHWNF3pyNUYs7a7XYqTL6aOe0skRBCI/trJq8BmMI5/PcMuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgmgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7DM9tV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423345,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423345,
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
  "id": -576460752303423344,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423344,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC5tYXcetO2wVk6bcdK+XMDQyEsCyWf1cOTv9j8EWgNxIMK13jZ1hdhzhR184xBJElIkICv/Vi38YDS1YBt0KYAuEDrCxo8tAYcWVZpq0CBfYstMqt3ZjkhZd6l2vRcP6bHWNF3pyNUYs7a7XYqTL6aOe0skRBCI/trJq8BmMI5/PcMuEj4RjkCoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDgmgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7DM9tV",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAn1UD9b64XPS1x3SA4WfrqdkactUjE369X3UeZbdoC0ofg+qxu7Z9YUPZHNFACHwnZfOqjBn/nocW8anfTRGsBbkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhASMrSd1lVTmgxyFIPODrOjDLL01aCtvksdqPn3FKw7kGgXGk1uUqc4yZLL5vW6tKOtJq9FywAyxRmDrjJIidWDrhA2TShUriUtWy9VxqnKPo+lTfEtHil/mHCaMdY8C/MzgVdBX3KormVMPkMjG7mn/mF0uxXeRGqQ0FKgUN+aiMcCrhI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4HoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAAChdh6ig==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAn1UD9b64XPS1x3SA4WfrqdkactUjE369X3UeZbdoC0ofg+qxu7Z9YUPZHNFACHwnZfOqjBn/nocW8anfTRGsBbkBKPkBJTsBoQbZUy5NQD3Zh2s4hBxHCAaBO4T0oXYHzX8F8yukHp4yDqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhASMrSd1lVTmgxyFIPODrOjDLL01aCtvksdqPn3FKw7kGgXGk1uUqc4yZLL5vW6tKOtJq9FywAyxRmDrjJIidWDrhA2TShUriUtWy9VxqnKPo+lTfEtHil/mHCaMdY8C/MzgVdBX3KormVMPkMjG7mn/mF0uxXeRGqQ0FKgUN+aiMcCrhI+EY5AqEG2VMuTUA92YdrOIQcRwgGgTuE9KF2B81/BfMrpB6eMg4HoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIYTBtErMAAChdh6ig==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "�EM�V�J>\f�DP\u0003\u0016 �s!i�i�`�\u0017ũ c?",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423343,
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423343,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423342,
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
    "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
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
  "channel_id": "ch_2eiGsAvtieLe2LUwRZLRVdYce9GyPESxJ9UMTBNyZ1gMvoJnnh",
  "id": -576460752303423342,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
