
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
      "fsm_id": "ba_b1zIMxdUcZviJ5QEkdSdUtrNqnVcyqzRmo4IR72XE/mbq9Ce"
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
      "fsm_id": "ba_FRg1k+vPdAAABzZVBseN8uB9WTjXGBrS1BarSH6bKGAzm0qI"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+48ESq6Ng==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422877,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAptDKw/my+9lq33GKyPKqi0Y0KBLNDpnDpnJU8KE4yTrMh4qCNMY1idHZ3FD2DWJ7v6C9kOc5ciWNRomghVwsGuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uPNl5Xks="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422877,
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
      "signed_tx": "tx_+MsLAfhCuEAptDKw/my+9lq33GKyPKqi0Y0KBLNDpnDpnJU8KE4yTrMh4qCNMY1idHZ3FD2DWJ7v6C9kOc5ciWNRomghVwsGuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uPNl5Xks=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422876,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAKbQysP5svvZat9xisjyqotGNCgSzQ6Zw6ZyVPChOMk6zIeKgjTGNYnR2dxQ9g1ie7+gvZDnOXIljUaJoIVcLBrhAo+dw/RviL+6McxMj4K7h+dFFEk57vq5kgSek9qHwHPKZ9GnlAfasN1aV9Bvr2w5nBsBccye9OJ5BwdBrgWiGDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jy7LMX7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422876,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAKbQysP5svvZat9xisjyqotGNCgSzQ6Zw6ZyVPChOMk6zIeKgjTGNYnR2dxQ9g1ie7+gvZDnOXIljUaJoIVcLBrhAo+dw/RviL+6McxMj4K7h+dFFEk57vq5kgSek9qHwHPKZ9GnlAfasN1aV9Bvr2w5nBsBccye9OJ5BwdBrgWiGDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jy7LMX7",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAKbQysP5svvZat9xisjyqotGNCgSzQ6Zw6ZyVPChOMk6zIeKgjTGNYnR2dxQ9g1ie7+gvZDnOXIljUaJoIVcLBrhAo+dw/RviL+6McxMj4K7h+dFFEk57vq5kgSek9qHwHPKZ9GnlAfasN1aV9Bvr2w5nBsBccye9OJ5BwdBrgWiGDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jy7LMX7",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKbQysP5svvZat9xisjyqotGNCgSzQ6Zw6ZyVPChOMk6zIeKgjTGNYnR2dxQ9g1ie7+gvZDnOXIljUaJoIVcLBrhAo+dw/RviL+6McxMj4K7h+dFFEk57vq5kgSek9qHwHPKZ9GnlAfasN1aV9Bvr2w5nBsBccye9OJ5BwdBrgWiGDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jy7LMX7",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKbQysP5svvZat9xisjyqotGNCgSzQ6Zw6ZyVPChOMk6zIeKgjTGNYnR2dxQ9g1ie7+gvZDnOXIljUaJoIVcLBrhAo+dw/RviL+6McxMj4K7h+dFFEk57vq5kgSek9qHwHPKZ9GnlAfasN1aV9Bvr2w5nBsBccye9OJ5BwdBrgWiGDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jy7LMX7",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "message": {
        "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "message": {
        "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
  "id": -576460752303422875,
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
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422875,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "state": "tx_+QENCwH4hLhAKbQysP5svvZat9xisjyqotGNCgSzQ6Zw6ZyVPChOMk6zIeKgjTGNYnR2dxQ9g1ie7+gvZDnOXIljUaJoIVcLBrhAo+dw/RviL+6McxMj4K7h+dFFEk57vq5kgSek9qHwHPKZ9GnlAfasN1aV9Bvr2w5nBsBccye9OJ5BwdBrgWiGDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jy7LMX7"
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "state": "tx_+QENCwH4hLhAKbQysP5svvZat9xisjyqotGNCgSzQ6Zw6ZyVPChOMk6zIeKgjTGNYnR2dxQ9g1ie7+gvZDnOXIljUaJoIVcLBrhAo+dw/RviL+6McxMj4K7h+dFFEk57vq5kgSek9qHwHPKZ9GnlAfasN1aV9Bvr2w5nBsBccye9OJ5BwdBrgWiGDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jy7LMX7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422874,
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
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422874,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrJzNcrMuxjqUQpTpfl4R46ejztgl5ZXxZbpfcyqCPmSAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B8HAwzY=",
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
  "id": -576460752303422873,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECgRZ7LvQo3xY9+QK8xFCsOMMbgJZR8Ax2bgLLDQwrPKguZk4TSP2ZVBfPXA/PG1Qw4f68F9w5LCv8dgR8UilAGuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcHTwLE"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422873,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "signed_tx": "tx_+JALAfhCuECgRZ7LvQo3xY9+QK8xFCsOMMbgJZR8Ax2bgLLDQwrPKguZk4TSP2ZVBfPXA/PG1Qw4f68F9w5LCv8dgR8UilAGuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcHTwLE",
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
  "id": -576460752303422872,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECH9DWnYW2LK5yj5K4VUd0xpkqzavAjCJZopA6wEGDTXpIE9YruqVG+cZ8MfPEyrkOkg3QPMRTZRrKbE6JDYD0AuECgRZ7LvQo3xY9+QK8xFCsOMMbgJZR8Ax2bgLLDQwrPKguZk4TSP2ZVBfPXA/PG1Qw4f68F9w5LCv8dgR8UilAGuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfGNYuz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422872,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "state": "tx_+NILAfiEuECH9DWnYW2LK5yj5K4VUd0xpkqzavAjCJZopA6wEGDTXpIE9YruqVG+cZ8MfPEyrkOkg3QPMRTZRrKbE6JDYD0AuECgRZ7LvQo3xY9+QK8xFCsOMMbgJZR8Ax2bgLLDQwrPKguZk4TSP2ZVBfPXA/PG1Qw4f68F9w5LCv8dgR8UilAGuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfGNYuz"
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "state": "tx_+NILAfiEuECH9DWnYW2LK5yj5K4VUd0xpkqzavAjCJZopA6wEGDTXpIE9YruqVG+cZ8MfPEyrkOkg3QPMRTZRrKbE6JDYD0AuECgRZ7LvQo3xY9+QK8xFCsOMMbgJZR8Ax2bgLLDQwrPKguZk4TSP2ZVBfPXA/PG1Qw4f68F9w5LCv8dgR8UilAGuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfGNYuz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422871,
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
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422871,
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
  "id": -576460752303422870,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422870,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECH9DWnYW2LK5yj5K4VUd0xpkqzavAjCJZopA6wEGDTXpIE9YruqVG+cZ8MfPEyrkOkg3QPMRTZRrKbE6JDYD0AuECgRZ7LvQo3xY9+QK8xFCsOMMbgJZR8Ax2bgLLDQwrPKguZk4TSP2ZVBfPXA/PG1Qw4f68F9w5LCv8dgR8UilAGuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfGNYuz",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422869,
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
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422869,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBrJzNcrMuxjqUQpTpfl4R46ejztgl5ZXxZbpfcyqCPmSA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7vqsoAg=",
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
  "id": -576460752303422868,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAQJ5/PhK0Q8ZNiYe7Zb3plwFaU9+zOoBE2MXC82w0QBh28AEXo3Y3CtnKuKWFD5hpR0tnX1bvC0gB1W/kyShABuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6YwtE1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422868,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAQJ5/PhK0Q8ZNiYe7Zb3plwFaU9+zOoBE2MXC82w0QBh28AEXo3Y3CtnKuKWFD5hpR0tnX1bvC0gB1W/kyShABuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6YwtE1",
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
  "id": -576460752303422867,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAQJ5/PhK0Q8ZNiYe7Zb3plwFaU9+zOoBE2MXC82w0QBh28AEXo3Y3CtnKuKWFD5hpR0tnX1bvC0gB1W/kyShABuEDdkUnwwtEIeb+Pw6fG/olZCBu1BojZBoTVbO5beCbpBluzrpUWvQT1f8bKyoZyvITVeaVx+ixaLkEFPVJGjQYAuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6OhbX8"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422867,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "state": "tx_+NILAfiEuEAQJ5/PhK0Q8ZNiYe7Zb3plwFaU9+zOoBE2MXC82w0QBh28AEXo3Y3CtnKuKWFD5hpR0tnX1bvC0gB1W/kyShABuEDdkUnwwtEIeb+Pw6fG/olZCBu1BojZBoTVbO5beCbpBluzrpUWvQT1f8bKyoZyvITVeaVx+ixaLkEFPVJGjQYAuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6OhbX8"
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "state": "tx_+NILAfiEuEAQJ5/PhK0Q8ZNiYe7Zb3plwFaU9+zOoBE2MXC82w0QBh28AEXo3Y3CtnKuKWFD5hpR0tnX1bvC0gB1W/kyShABuEDdkUnwwtEIeb+Pw6fG/olZCBu1BojZBoTVbO5beCbpBluzrpUWvQT1f8bKyoZyvITVeaVx+ixaLkEFPVJGjQYAuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6OhbX8"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422866,
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
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422866,
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
  "id": -576460752303422865,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422865,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAQJ5/PhK0Q8ZNiYe7Zb3plwFaU9+zOoBE2MXC82w0QBh28AEXo3Y3CtnKuKWFD5hpR0tnX1bvC0gB1W/kyShABuEDdkUnwwtEIeb+Pw6fG/olZCBu1BojZBoTVbO5beCbpBluzrpUWvQT1f8bKyoZyvITVeaVx+ixaLkEFPVJGjQYAuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6OhbX8",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBrJzNcrMuxjqUQpTpfl4R46ejztgl5ZXxZbpfcyqCPmSoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79LjU+NILAfiEuEAQJ5/PhK0Q8ZNiYe7Zb3plwFaU9+zOoBE2MXC82w0QBh28AEXo3Y3CtnKuKWFD5hpR0tnX1bvC0gB1W/kyShABuEDdkUnwwtEIeb+Pw6fG/olZCBu1BojZBoTVbO5beCbpBluzrpUWvQT1f8bKyoZyvITVeaVx+ixaLkEFPVJGjQYAuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4AhhMG0SswAD0K7ctX",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBrJzNcrMuxjqUQpTpfl4R46ejztgl5ZXxZbpfcyqCPmSoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROELjU+NILAfiEuEAQJ5/PhK0Q8ZNiYe7Zb3plwFaU9+zOoBE2MXC82w0QBh28AEXo3Y3CtnKuKWFD5hpR0tnX1bvC0gB1W/kyShABuEDdkUnwwtEIeb+Pw6fG/olZCBu1BojZBoTVbO5beCbpBluzrpUWvQT1f8bKyoZyvITVeaVx+ixaLkEFPVJGjQYAuEj4RjkCoQayczXKzLsY6lEKU6X5eEeOno87YJeWV8WW6X3Mqgj5kgOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4AhhMG0SswABdgNNVT",
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
  "id": -576460752303422864,
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
  "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
  "id": -576460752303422864,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
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
  "id": -576460752303422863,
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
    "channel_id": "ch_2MbGUN8AxZBgj8QMcy5W3y3Dn2DBTGxAYaa9x3wfP46pqkz5JZ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
