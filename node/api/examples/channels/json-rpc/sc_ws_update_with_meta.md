
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
      "fsm_id": "ba_ahqwlm0dPMNZGSvTQ7of8h9lH6dPL0L0yKMWhSEYZBnha/4P"
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
      "fsm_id": "ba_nmi0hfiOUfMsC0TPndiZyh2iJIkf5Wrg/YdEVu2BjaKCm+lM"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4I3XR9Nw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423341,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAXzyozY37hi5C52u6o+of908m0EBKgAwGz5hE8Y6LS8zdm3akzttSLD600jye4HgXOI3Xan0s+e9MAqLA4YAYLuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uCMcfff4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423341,
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
      "signed_tx": "tx_+MsLAfhCuEAXzyozY37hi5C52u6o+of908m0EBKgAwGz5hE8Y6LS8zdm3akzttSLD600jye4HgXOI3Xan0s+e9MAqLA4YAYLuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uCMcfff4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423340,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAF88qM2N+4YuQudruqPqH/dPJtBASoAMBs+YRPGOi0vM3Zt2pM7bUiw+tNI8nuB4FziN12p9LPnvTAKiwOGAGC7hA5EOhD0C3FiM7xlMiXOwiXNcHMZdJMod9tKYnE1M3N3N6Yn8iMlyVozDPzDAnV3kj0U7fFT9TbPvfA250mIDuAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7giXWGMm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423340,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAF88qM2N+4YuQudruqPqH/dPJtBASoAMBs+YRPGOi0vM3Zt2pM7bUiw+tNI8nuB4FziN12p9LPnvTAKiwOGAGC7hA5EOhD0C3FiM7xlMiXOwiXNcHMZdJMod9tKYnE1M3N3N6Yn8iMlyVozDPzDAnV3kj0U7fFT9TbPvfA250mIDuAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7giXWGMm",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAF88qM2N+4YuQudruqPqH/dPJtBASoAMBs+YRPGOi0vM3Zt2pM7bUiw+tNI8nuB4FziN12p9LPnvTAKiwOGAGC7hA5EOhD0C3FiM7xlMiXOwiXNcHMZdJMod9tKYnE1M3N3N6Yn8iMlyVozDPzDAnV3kj0U7fFT9TbPvfA250mIDuAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7giXWGMm",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAF88qM2N+4YuQudruqPqH/dPJtBASoAMBs+YRPGOi0vM3Zt2pM7bUiw+tNI8nuB4FziN12p9LPnvTAKiwOGAGC7hA5EOhD0C3FiM7xlMiXOwiXNcHMZdJMod9tKYnE1M3N3N6Yn8iMlyVozDPzDAnV3kj0U7fFT9TbPvfA250mIDuAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7giXWGMm",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAF88qM2N+4YuQudruqPqH/dPJtBASoAMBs+YRPGOi0vM3Zt2pM7bUiw+tNI8nuB4FziN12p9LPnvTAKiwOGAGC7hA5EOhD0C3FiM7xlMiXOwiXNcHMZdJMod9tKYnE1M3N3N6Yn8iMlyVozDPzDAnV3kj0U7fFT9TbPvfA250mIDuAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7giXWGMm",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "message": {
        "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "message": {
        "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "id": -576460752303423339,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423339,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+QENCwH4hLhAF88qM2N+4YuQudruqPqH/dPJtBASoAMBs+YRPGOi0vM3Zt2pM7bUiw+tNI8nuB4FziN12p9LPnvTAKiwOGAGC7hA5EOhD0C3FiM7xlMiXOwiXNcHMZdJMod9tKYnE1M3N3N6Yn8iMlyVozDPzDAnV3kj0U7fFT9TbPvfA250mIDuAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7giXWGMm"
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+QENCwH4hLhAF88qM2N+4YuQudruqPqH/dPJtBASoAMBs+YRPGOi0vM3Zt2pM7bUiw+tNI8nuB4FziN12p9LPnvTAKiwOGAGC7hA5EOhD0C3FiM7xlMiXOwiXNcHMZdJMod9tKYnE1M3N3N6Yn8iMlyVozDPzDAnV3kj0U7fFT9TbPvfA250mIDuAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7giXWGMm"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423338,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423338,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsWnpB2M7XjTKAEtQBdOULcKQIdkq/dnOl3TIQ2/V7Y6AqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B2gQ31s=",
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
  "id": -576460752303423337,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED6VxgQ5Z4/4zTiVoGbtjpuS68svoDPYIr9MyEmBISBFlYJ+TNWHUo/Manwnah3BRO5QkHrFRslZ+A+2RxDIP4LuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAf2hWlt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423337,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+JALAfhCuED6VxgQ5Z4/4zTiVoGbtjpuS68svoDPYIr9MyEmBISBFlYJ+TNWHUo/Manwnah3BRO5QkHrFRslZ+A+2RxDIP4LuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAf2hWlt",
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
  "id": -576460752303423336,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECvjtv/DmBAveQJciRNxWtNajE90VDjwz2cjOu+2sAISOMuBYIblj+gBaHycHG+lQ7FaYgz2Sf5M2ATFzgSDf0MuED6VxgQ5Z4/4zTiVoGbtjpuS68svoDPYIr9MyEmBISBFlYJ+TNWHUo/Manwnah3BRO5QkHrFRslZ+A+2RxDIP4LuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdoBf0Y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423336,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuECvjtv/DmBAveQJciRNxWtNajE90VDjwz2cjOu+2sAISOMuBYIblj+gBaHycHG+lQ7FaYgz2Sf5M2ATFzgSDf0MuED6VxgQ5Z4/4zTiVoGbtjpuS68svoDPYIr9MyEmBISBFlYJ+TNWHUo/Manwnah3BRO5QkHrFRslZ+A+2RxDIP4LuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdoBf0Y"
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuECvjtv/DmBAveQJciRNxWtNajE90VDjwz2cjOu+2sAISOMuBYIblj+gBaHycHG+lQ7FaYgz2Sf5M2ATFzgSDf0MuED6VxgQ5Z4/4zTiVoGbtjpuS68svoDPYIr9MyEmBISBFlYJ+TNWHUo/Manwnah3BRO5QkHrFRslZ+A+2RxDIP4LuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdoBf0Y"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423335,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423335,
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
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECvjtv/DmBAveQJciRNxWtNajE90VDjwz2cjOu+2sAISOMuBYIblj+gBaHycHG+lQ7FaYgz2Sf5M2ATFzgSDf0MuED6VxgQ5Z4/4zTiVoGbtjpuS68svoDPYIr9MyEmBISBFlYJ+TNWHUo/Manwnah3BRO5QkHrFRslZ+A+2RxDIP4LuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdoBf0Y",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423333,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423333,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsWnpB2M7XjTKAEtQBdOULcKQIdkq/dnOl3TIQ2/V7Y6A6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7oXZwD0=",
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
  "id": -576460752303423332,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBIA+EijopdH8o4qB0Pftw49h1fkXhkfZeh4pXeyYCxy9kZ9P8WKFljmynRCGPBg0To9qezmTMBFp8L59S2boALuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7yzfNj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423332,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBIA+EijopdH8o4qB0Pftw49h1fkXhkfZeh4pXeyYCxy9kZ9P8WKFljmynRCGPBg0To9qezmTMBFp8L59S2boALuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7yzfNj",
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
  "id": -576460752303423331,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBIA+EijopdH8o4qB0Pftw49h1fkXhkfZeh4pXeyYCxy9kZ9P8WKFljmynRCGPBg0To9qezmTMBFp8L59S2boALuECMaAwkhval/plLE4YAulBr5XZr/vWC1jB99d/8e+fjyD8ZHTuIE4fiNA2tezxfY4X3093RGVIl0yn4EpJgSU4FuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5jbFRn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423331,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuEBIA+EijopdH8o4qB0Pftw49h1fkXhkfZeh4pXeyYCxy9kZ9P8WKFljmynRCGPBg0To9qezmTMBFp8L59S2boALuECMaAwkhval/plLE4YAulBr5XZr/vWC1jB99d/8e+fjyD8ZHTuIE4fiNA2tezxfY4X3093RGVIl0yn4EpJgSU4FuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5jbFRn"
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuEBIA+EijopdH8o4qB0Pftw49h1fkXhkfZeh4pXeyYCxy9kZ9P8WKFljmynRCGPBg0To9qezmTMBFp8L59S2boALuECMaAwkhval/plLE4YAulBr5XZr/vWC1jB99d/8e+fjyD8ZHTuIE4fiNA2tezxfY4X3093RGVIl0yn4EpJgSU4FuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5jbFRn"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423330,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423330,
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
  "id": -576460752303423329,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423329,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBIA+EijopdH8o4qB0Pftw49h1fkXhkfZeh4pXeyYCxy9kZ9P8WKFljmynRCGPBg0To9qezmTMBFp8L59S2boALuECMaAwkhval/plLE4YAulBr5XZr/vWC1jB99d/8e+fjyD8ZHTuIE4fiNA2tezxfY4X3093RGVIl0yn4EpJgSU4FuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5jbFRn",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423328,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423328,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsWnpB2M7XjTKAEtQBdOULcKQIdkq/dnOl3TIQ2/V7Y6BKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3ttAL7s0=",
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
  "id": -576460752303423327,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBZmkFEkxEQ6ch1SVmi1SylqHysRaM1W8xFxLbdUdBkmLmhvwlgMr4rvw3uk8c7vW32QrqDgs64XyUlEZnv+SMLuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7aPjuiN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423327,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBZmkFEkxEQ6ch1SVmi1SylqHysRaM1W8xFxLbdUdBkmLmhvwlgMr4rvw3uk8c7vW32QrqDgs64XyUlEZnv+SMLuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7aPjuiN",
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
  "id": -576460752303423326,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBZmkFEkxEQ6ch1SVmi1SylqHysRaM1W8xFxLbdUdBkmLmhvwlgMr4rvw3uk8c7vW32QrqDgs64XyUlEZnv+SMLuEBhdRvlamaWFOiqZoiD5c2UYOZMW3jYlg7MK9/WwNPfYivv3wBDi0rWjR2EP0vGTma4z4IX+6lodaaAgjUUqasIuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7b/96t2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423326,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuEBZmkFEkxEQ6ch1SVmi1SylqHysRaM1W8xFxLbdUdBkmLmhvwlgMr4rvw3uk8c7vW32QrqDgs64XyUlEZnv+SMLuEBhdRvlamaWFOiqZoiD5c2UYOZMW3jYlg7MK9/WwNPfYivv3wBDi0rWjR2EP0vGTma4z4IX+6lodaaAgjUUqasIuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7b/96t2"
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuEBZmkFEkxEQ6ch1SVmi1SylqHysRaM1W8xFxLbdUdBkmLmhvwlgMr4rvw3uk8c7vW32QrqDgs64XyUlEZnv+SMLuEBhdRvlamaWFOiqZoiD5c2UYOZMW3jYlg7MK9/WwNPfYivv3wBDi0rWjR2EP0vGTma4z4IX+6lodaaAgjUUqasIuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7b/96t2"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423325,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423325,
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
  "id": -576460752303423324,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423324,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBZmkFEkxEQ6ch1SVmi1SylqHysRaM1W8xFxLbdUdBkmLmhvwlgMr4rvw3uk8c7vW32QrqDgs64XyUlEZnv+SMLuEBhdRvlamaWFOiqZoiD5c2UYOZMW3jYlg7MK9/WwNPfYivv3wBDi0rWjR2EP0vGTma4z4IX+6lodaaAgjUUqasIuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgSgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7b/96t2",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423323,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423323,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsWnpB2M7XjTKAEtQBdOULcKQIdkq/dnOl3TIQ2/V7Y6BaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7lUIjKA=",
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
  "id": -576460752303423322,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBC+RqlOXPtN/9xfjWZdnJJs17z2RHR//WxLT7NkLM0aqnKxKbqIc1bb/XrBK98MgQcDdFY0H7VI4EoDGPGS0oMuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7mMC6f"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423322,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBC+RqlOXPtN/9xfjWZdnJJs17z2RHR//WxLT7NkLM0aqnKxKbqIc1bb/XrBK98MgQcDdFY0H7VI4EoDGPGS0oMuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7mMC6f",
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
  "id": -576460752303423321,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEArz5wXibIaHTAX3zN5qTfffZ7OqFZudXyfZAiylBPMZ/5aSLZq4+rmCELHZVyr1/MX0Nqnw2LcijGnWA0nbpIJuEBC+RqlOXPtN/9xfjWZdnJJs17z2RHR//WxLT7NkLM0aqnKxKbqIc1bb/XrBK98MgQcDdFY0H7VI4EoDGPGS0oMuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5QhzFe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423321,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuEArz5wXibIaHTAX3zN5qTfffZ7OqFZudXyfZAiylBPMZ/5aSLZq4+rmCELHZVyr1/MX0Nqnw2LcijGnWA0nbpIJuEBC+RqlOXPtN/9xfjWZdnJJs17z2RHR//WxLT7NkLM0aqnKxKbqIc1bb/XrBK98MgQcDdFY0H7VI4EoDGPGS0oMuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5QhzFe"
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuEArz5wXibIaHTAX3zN5qTfffZ7OqFZudXyfZAiylBPMZ/5aSLZq4+rmCELHZVyr1/MX0Nqnw2LcijGnWA0nbpIJuEBC+RqlOXPtN/9xfjWZdnJJs17z2RHR//WxLT7NkLM0aqnKxKbqIc1bb/XrBK98MgQcDdFY0H7VI4EoDGPGS0oMuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5QhzFe"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423320,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423320,
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
  "id": -576460752303423319,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423319,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEArz5wXibIaHTAX3zN5qTfffZ7OqFZudXyfZAiylBPMZ/5aSLZq4+rmCELHZVyr1/MX0Nqnw2LcijGnWA0nbpIJuEBC+RqlOXPtN/9xfjWZdnJJs17z2RHR//WxLT7NkLM0aqnKxKbqIc1bb/XrBK98MgQcDdFY0H7VI4EoDGPGS0oMuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5QhzFe",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423318,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423318,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsWnpB2M7XjTKAEtQBdOULcKQIdkq/dnOl3TIQ2/V7Y6BqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tmQ659E=",
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
  "id": -576460752303423317,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA4pObwKJPtDM16+UAXVjk6zWvvqmzRd5mtNWOZgRXEzwnrjBBKgVaSx00m3unTU6P2zq2RlXGERSG0XKm4acYEuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Yelmal"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423317,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA4pObwKJPtDM16+UAXVjk6zWvvqmzRd5mtNWOZgRXEzwnrjBBKgVaSx00m3unTU6P2zq2RlXGERSG0XKm4acYEuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Yelmal",
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
  "id": -576460752303423316,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA4pObwKJPtDM16+UAXVjk6zWvvqmzRd5mtNWOZgRXEzwnrjBBKgVaSx00m3unTU6P2zq2RlXGERSG0XKm4acYEuED6JrPLE5NiJo+H2Ck0IiL2wcPvYxU+QfVzKAhPxduXJ2Iz/3K9EJLvxmaxo4nTDAjw+3HBCrt9NysqNyAiqlUGuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Y4zgPu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423316,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuEA4pObwKJPtDM16+UAXVjk6zWvvqmzRd5mtNWOZgRXEzwnrjBBKgVaSx00m3unTU6P2zq2RlXGERSG0XKm4acYEuED6JrPLE5NiJo+H2Ck0IiL2wcPvYxU+QfVzKAhPxduXJ2Iz/3K9EJLvxmaxo4nTDAjw+3HBCrt9NysqNyAiqlUGuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Y4zgPu"
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "state": "tx_+NILAfiEuEA4pObwKJPtDM16+UAXVjk6zWvvqmzRd5mtNWOZgRXEzwnrjBBKgVaSx00m3unTU6P2zq2RlXGERSG0XKm4acYEuED6JrPLE5NiJo+H2Ck0IiL2wcPvYxU+QfVzKAhPxduXJ2Iz/3K9EJLvxmaxo4nTDAjw+3HBCrt9NysqNyAiqlUGuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Y4zgPu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423315,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423315,
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
  "id": -576460752303423314,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423314,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA4pObwKJPtDM16+UAXVjk6zWvvqmzRd5mtNWOZgRXEzwnrjBBKgVaSx00m3unTU6P2zq2RlXGERSG0XKm4acYEuED6JrPLE5NiJo+H2Ck0IiL2wcPvYxU+QfVzKAhPxduXJ2Iz/3K9EJLvxmaxo4nTDAjw+3HBCrt9NysqNyAiqlUGuEj4RjkCoQbFp6QdjO140ygBLUAXTlC3CkCHZKv3Zzpd0yENv1e2OgagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Y4zgPu",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423313,
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
  "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
  "id": -576460752303423313,
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
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
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
  "id": -576460752303423312,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2W3q1kga8epY6e9PneAgoenuQq4o5xZwk3u6JQjNFhsYfxgf6c",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
