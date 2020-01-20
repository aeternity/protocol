
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator
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
      "fsm_id": "ba_Ga9JB+zE2Ejp5Iep7wR2Uzp7zsEneDrooT8G2gNOx/Lj9JBr"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder
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
      "fsm_id": "ba_n0KyMvxX37F53aBEEMY/mECrPyJY52eTS0cFNgU4bGZAOxYT"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4CukUNaA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423486,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBh0BPu7okaaRZV6cYTAtaA1MIV4YAQxySgE5TuBZwed1fEGA0187T7lZIIJmZ8YaR4eaf8Ywa3q8cWZ4R+N4YPuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAgPhEWE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423486,
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
      "signed_tx": "tx_+MsLAfhCuEBh0BPu7okaaRZV6cYTAtaA1MIV4YAQxySgE5TuBZwed1fEGA0187T7lZIIJmZ8YaR4eaf8Ywa3q8cWZ4R+N4YPuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAgPhEWE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAYdAT7u6JGmkWVenGEwLWgNTCFeGAEMckoBOU7gWcHndXxBgNNfO0+5WSCCZmfGGkeHmn/GMGt6vHFmeEfjeGD7hAj1Y8ZimpXMt34i2YADLg6X2m42vnUkSudeQbHyxBG5vNFq3E/lp83MjuqkfjyClEiGeqSSg8OazKyk+HkUFyBLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gIBO3OV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423485,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAYdAT7u6JGmkWVenGEwLWgNTCFeGAEMckoBOU7gWcHndXxBgNNfO0+5WSCCZmfGGkeHmn/GMGt6vHFmeEfjeGD7hAj1Y8ZimpXMt34i2YADLg6X2m42vnUkSudeQbHyxBG5vNFq3E/lp83MjuqkfjyClEiGeqSSg8OazKyk+HkUFyBLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gIBO3OV",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAYdAT7u6JGmkWVenGEwLWgNTCFeGAEMckoBOU7gWcHndXxBgNNfO0+5WSCCZmfGGkeHmn/GMGt6vHFmeEfjeGD7hAj1Y8ZimpXMt34i2YADLg6X2m42vnUkSudeQbHyxBG5vNFq3E/lp83MjuqkfjyClEiGeqSSg8OazKyk+HkUFyBLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gIBO3OV",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAYdAT7u6JGmkWVenGEwLWgNTCFeGAEMckoBOU7gWcHndXxBgNNfO0+5WSCCZmfGGkeHmn/GMGt6vHFmeEfjeGD7hAj1Y8ZimpXMt34i2YADLg6X2m42vnUkSudeQbHyxBG5vNFq3E/lp83MjuqkfjyClEiGeqSSg8OazKyk+HkUFyBLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gIBO3OV",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAYdAT7u6JGmkWVenGEwLWgNTCFeGAEMckoBOU7gWcHndXxBgNNfO0+5WSCCZmfGGkeHmn/GMGt6vHFmeEfjeGD7hAj1Y8ZimpXMt34i2YADLg6X2m42vnUkSudeQbHyxBG5vNFq3E/lp83MjuqkfjyClEiGeqSSg8OazKyk+HkUFyBLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gIBO3OV",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+QENCwH4hLhAYdAT7u6JGmkWVenGEwLWgNTCFeGAEMckoBOU7gWcHndXxBgNNfO0+5WSCCZmfGGkeHmn/GMGt6vHFmeEfjeGD7hAj1Y8ZimpXMt34i2YADLg6X2m42vnUkSudeQbHyxBG5vNFq3E/lp83MjuqkfjyClEiGeqSSg8OazKyk+HkUFyBLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gIBO3OV"
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+QENCwH4hLhAYdAT7u6JGmkWVenGEwLWgNTCFeGAEMckoBOU7gWcHndXxBgNNfO0+5WSCCZmfGGkeHmn/GMGt6vHFmeEfjeGD7hAj1Y8ZimpXMt34i2YADLg6X2m42vnUkSudeQbHyxBG5vNFq3E/lp83MjuqkfjyClEiGeqSSg8OazKyk+HkUFyBLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gIBO3OV"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "message": {
        "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "message": {
        "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "id": -576460752303423484,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423484,
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
  "id": -576460752303423483,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423483,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmpXp5DqEqIW3YZM1XHy5jcFe+9utk7unuRS5whrx0ltAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B+QWTSg=",
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
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECR8uom3Tudx4tFp5YxmiGcweN8JqeKmP8pkO8aA7HUkuXL2k3GWBLAF618f3dPdVUEeRjROHp8moqxtSBY0uICuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe0hA+n"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423482,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+JALAfhCuECR8uom3Tudx4tFp5YxmiGcweN8JqeKmP8pkO8aA7HUkuXL2k3GWBLAF618f3dPdVUEeRjROHp8moqxtSBY0uICuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe0hA+n",
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
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECR8uom3Tudx4tFp5YxmiGcweN8JqeKmP8pkO8aA7HUkuXL2k3GWBLAF618f3dPdVUEeRjROHp8moqxtSBY0uICuEDUMLxcgXyR0aKRdhOAhRSrBvUEmlDyMlfAGBIx67rWsIJ7KCi4Gld2mCRPdLKSgmnDGS/wEPgudXrklKP1xDYAuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAd3hgSK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423481,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuECR8uom3Tudx4tFp5YxmiGcweN8JqeKmP8pkO8aA7HUkuXL2k3GWBLAF618f3dPdVUEeRjROHp8moqxtSBY0uICuEDUMLxcgXyR0aKRdhOAhRSrBvUEmlDyMlfAGBIx67rWsIJ7KCi4Gld2mCRPdLKSgmnDGS/wEPgudXrklKP1xDYAuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAd3hgSK"
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuECR8uom3Tudx4tFp5YxmiGcweN8JqeKmP8pkO8aA7HUkuXL2k3GWBLAF618f3dPdVUEeRjROHp8moqxtSBY0uICuEDUMLxcgXyR0aKRdhOAhRSrBvUEmlDyMlfAGBIx67rWsIJ7KCi4Gld2mCRPdLKSgmnDGS/wEPgudXrklKP1xDYAuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAd3hgSK"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423480,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423480,
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
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECR8uom3Tudx4tFp5YxmiGcweN8JqeKmP8pkO8aA7HUkuXL2k3GWBLAF618f3dPdVUEeRjROHp8moqxtSBY0uICuEDUMLxcgXyR0aKRdhOAhRSrBvUEmlDyMlfAGBIx67rWsIJ7KCi4Gld2mCRPdLKSgmnDGS/wEPgudXrklKP1xDYAuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAd3hgSK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423478,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423478,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmpXp5DqEqIW3YZM1XHy5jcFe+9utk7unuRS5whrx0ltA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hq3bzo=",
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
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDuSSuq+wVD8iJxswbXj50xHLQrctrtSMqOGy5SuUlL1XE7q9x2P9X+wmRjfef2EZix9x/lOZeZzU7J0J/BpiQCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7aUmWE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423477,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDuSSuq+wVD8iJxswbXj50xHLQrctrtSMqOGy5SuUlL1XE7q9x2P9X+wmRjfef2EZix9x/lOZeZzU7J0J/BpiQCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7aUmWE",
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
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDddnSJlYiVinX1Cwg63jOnFjhZu+dh2CTSufF/cWJWCUfOrmyHD0IOovycw/P47HR5NpCgFVmGHvX4+7AIz8sOuEDuSSuq+wVD8iJxswbXj50xHLQrctrtSMqOGy5SuUlL1XE7q9x2P9X+wmRjfef2EZix9x/lOZeZzU7J0J/BpiQCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7uuonp"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423476,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuEDddnSJlYiVinX1Cwg63jOnFjhZu+dh2CTSufF/cWJWCUfOrmyHD0IOovycw/P47HR5NpCgFVmGHvX4+7AIz8sOuEDuSSuq+wVD8iJxswbXj50xHLQrctrtSMqOGy5SuUlL1XE7q9x2P9X+wmRjfef2EZix9x/lOZeZzU7J0J/BpiQCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7uuonp"
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuEDddnSJlYiVinX1Cwg63jOnFjhZu+dh2CTSufF/cWJWCUfOrmyHD0IOovycw/P47HR5NpCgFVmGHvX4+7AIz8sOuEDuSSuq+wVD8iJxswbXj50xHLQrctrtSMqOGy5SuUlL1XE7q9x2P9X+wmRjfef2EZix9x/lOZeZzU7J0J/BpiQCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7uuonp"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423475,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423475,
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
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDddnSJlYiVinX1Cwg63jOnFjhZu+dh2CTSufF/cWJWCUfOrmyHD0IOovycw/P47HR5NpCgFVmGHvX4+7AIz8sOuEDuSSuq+wVD8iJxswbXj50xHLQrctrtSMqOGy5SuUlL1XE7q9x2P9X+wmRjfef2EZix9x/lOZeZzU7J0J/BpiQCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7uuonp",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423473,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423473,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmpXp5DqEqIW3YZM1XHy5jcFe+9utk7unuRS5whrx0ltBKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tnm3wvA=",
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
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDUxp5XpSS5F6EscKtPg+UBpz4IpoDo1SospgXSBH8mT7GdZK9WyGHd2ckKTzIRF8/G5dpYKS3H9MJL+oxIDbgHuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZkUqId"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423472,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDUxp5XpSS5F6EscKtPg+UBpz4IpoDo1SospgXSBH8mT7GdZK9WyGHd2ckKTzIRF8/G5dpYKS3H9MJL+oxIDbgHuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZkUqId",
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
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAXPoKMMq+kw29Yl8FCaSWJ6g+cD120lcV9+3cUoGSuI3jEkkkWOh6GN+ROVGwZ4LItVgFd+e5VlMvPm+a/A5ENuEDUxp5XpSS5F6EscKtPg+UBpz4IpoDo1SospgXSBH8mT7GdZK9WyGHd2ckKTzIRF8/G5dpYKS3H9MJL+oxIDbgHuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7aXudqM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423471,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuEAXPoKMMq+kw29Yl8FCaSWJ6g+cD120lcV9+3cUoGSuI3jEkkkWOh6GN+ROVGwZ4LItVgFd+e5VlMvPm+a/A5ENuEDUxp5XpSS5F6EscKtPg+UBpz4IpoDo1SospgXSBH8mT7GdZK9WyGHd2ckKTzIRF8/G5dpYKS3H9MJL+oxIDbgHuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7aXudqM"
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuEAXPoKMMq+kw29Yl8FCaSWJ6g+cD120lcV9+3cUoGSuI3jEkkkWOh6GN+ROVGwZ4LItVgFd+e5VlMvPm+a/A5ENuEDUxp5XpSS5F6EscKtPg+UBpz4IpoDo1SospgXSBH8mT7GdZK9WyGHd2ckKTzIRF8/G5dpYKS3H9MJL+oxIDbgHuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7aXudqM"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423470,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423470,
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
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAXPoKMMq+kw29Yl8FCaSWJ6g+cD120lcV9+3cUoGSuI3jEkkkWOh6GN+ROVGwZ4LItVgFd+e5VlMvPm+a/A5ENuEDUxp5XpSS5F6EscKtPg+UBpz4IpoDo1SospgXSBH8mT7GdZK9WyGHd2ckKTzIRF8/G5dpYKS3H9MJL+oxIDbgHuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7aXudqM",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423468,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423468,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmpXp5DqEqIW3YZM1XHy5jcFe+9utk7unuRS5whrx0ltBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hjolr4=",
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
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEChgCUeMlRyyS4eg2Hc+ityi2R+PGIw2G2dUxLSmPGUSFgO0kBIF6f9oB/k/RQAqsmhugdNKv/4qLyOTFnhBskKuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4MasnD"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423467,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+JALAfhCuEChgCUeMlRyyS4eg2Hc+ityi2R+PGIw2G2dUxLSmPGUSFgO0kBIF6f9oB/k/RQAqsmhugdNKv/4qLyOTFnhBskKuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4MasnD",
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
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA6VSea0yQJBJuXmfOV+SJ936HEV2itwx+NKIDPwm7go9TQihoReXvZyW8JIe+eG2LA4kVAF5+anx7qTsk/V34CuEChgCUeMlRyyS4eg2Hc+ityi2R+PGIw2G2dUxLSmPGUSFgO0kBIF6f9oB/k/RQAqsmhugdNKv/4qLyOTFnhBskKuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+61Ukod"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423466,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuEA6VSea0yQJBJuXmfOV+SJ936HEV2itwx+NKIDPwm7go9TQihoReXvZyW8JIe+eG2LA4kVAF5+anx7qTsk/V34CuEChgCUeMlRyyS4eg2Hc+ityi2R+PGIw2G2dUxLSmPGUSFgO0kBIF6f9oB/k/RQAqsmhugdNKv/4qLyOTFnhBskKuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+61Ukod"
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuEA6VSea0yQJBJuXmfOV+SJ936HEV2itwx+NKIDPwm7go9TQihoReXvZyW8JIe+eG2LA4kVAF5+anx7qTsk/V34CuEChgCUeMlRyyS4eg2Hc+ityi2R+PGIw2G2dUxLSmPGUSFgO0kBIF6f9oB/k/RQAqsmhugdNKv/4qLyOTFnhBskKuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+61Ukod"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423465,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423465,
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
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA6VSea0yQJBJuXmfOV+SJ936HEV2itwx+NKIDPwm7go9TQihoReXvZyW8JIe+eG2LA4kVAF5+anx7qTsk/V34CuEChgCUeMlRyyS4eg2Hc+ityi2R+PGIw2G2dUxLSmPGUSFgO0kBIF6f9oB/k/RQAqsmhugdNKv/4qLyOTFnhBskKuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+61Ukod",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423463,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423463,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmpXp5DqEqIW3YZM1XHy5jcFe+9utk7unuRS5whrx0ltBqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tnjEPZw=",
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
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAMfoM5scxYdj/5RWjQVRYUa+wdgpYUpSQ+8JWi3ifjSelmFdcHqhSdULIlubYsCysZ7p1MILB6Q86lGJiwAM0CuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7aWC8Ec"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423462,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAMfoM5scxYdj/5RWjQVRYUa+wdgpYUpSQ+8JWi3ifjSelmFdcHqhSdULIlubYsCysZ7p1MILB6Q86lGJiwAM0CuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7aWC8Ec",
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
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAMfoM5scxYdj/5RWjQVRYUa+wdgpYUpSQ+8JWi3ifjSelmFdcHqhSdULIlubYsCysZ7p1MILB6Q86lGJiwAM0CuED985js7sz+zdzFK3e7D7Bk7TkgAEM2M35k6DxrSQft3vgx8PtYLarx1LuWUNSMYDHuwOvIChmv7yD/k9KCfJcCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Yj2WnQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423461,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuEAMfoM5scxYdj/5RWjQVRYUa+wdgpYUpSQ+8JWi3ifjSelmFdcHqhSdULIlubYsCysZ7p1MILB6Q86lGJiwAM0CuED985js7sz+zdzFK3e7D7Bk7TkgAEM2M35k6DxrSQft3vgx8PtYLarx1LuWUNSMYDHuwOvIChmv7yD/k9KCfJcCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Yj2WnQ"
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
    "data": {
      "state": "tx_+NILAfiEuEAMfoM5scxYdj/5RWjQVRYUa+wdgpYUpSQ+8JWi3ifjSelmFdcHqhSdULIlubYsCysZ7p1MILB6Q86lGJiwAM0CuED985js7sz+zdzFK3e7D7Bk7TkgAEM2M35k6DxrSQft3vgx8PtYLarx1LuWUNSMYDHuwOvIChmv7yD/k9KCfJcCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Yj2WnQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423460,
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423460,
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
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAMfoM5scxYdj/5RWjQVRYUa+wdgpYUpSQ+8JWi3ifjSelmFdcHqhSdULIlubYsCysZ7p1MILB6Q86lGJiwAM0CuED985js7sz+zdzFK3e7D7Bk7TkgAEM2M35k6DxrSQft3vgx8PtYLarx1LuWUNSMYDHuwOvIChmv7yD/k9KCfJcCuEj4RjkCoQZqV6eQ6hKiFt2GTNVx8uY3BXvvbrZO7p7kUucIa8dJbQagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Yj2WnQ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423458,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
  "id": -576460752303423458,
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
    "channel_id": "ch_oqNgnmPr1QmmNbA3AeDW8Bu9XwBPZUXr47hh2xSaTrtBc2iXK",
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
  "id": -576460752303423457,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator closes WebSocket connection
