
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator
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
      "fsm_id": "ba_v0pypyJUBPw4kOMKB338TrN9byCRA+5CYok23XqcX8bLtFtf"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder
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
      "fsm_id": "ba_fie2q24c4gevFDtSzyzhwN/uobi5aMiS+uw4hLKfOCr7v0Xv"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYJesJbuA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423311,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEC2UtZNMze90VGUlpAT4LvhPeZmXfN7Se+nVWrnJT1LBvxEytyl561J7+U+5xv2jr582CNlXvFV6ZakMF8POTIGuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2CTczv6s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423311,
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
      "signed_tx": "tx_+MsLAfhCuEC2UtZNMze90VGUlpAT4LvhPeZmXfN7Se+nVWrnJT1LBvxEytyl561J7+U+5xv2jr582CNlXvFV6ZakMF8POTIGuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2CTczv6s=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423310,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAeqz1gw9J95x9at7mQ2JDauqwtBSI6iIf8WdcVcMU/OICzgRJzW4hk2Pf3mYLMY+ImCnUiY7Va7Fm70NxulZnBrhAtlLWTTM3vdFRlJaQE+C74T3mZl3ze0nvp1Vq5yU9Swb8RMrcpeetSe/lPucb9o6+fNgjZV7xVemWpDBfDzkyBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgn8pP9P"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423310,
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAeqz1gw9J95x9at7mQ2JDauqwtBSI6iIf8WdcVcMU/OICzgRJzW4hk2Pf3mYLMY+ImCnUiY7Va7Fm70NxulZnBrhAtlLWTTM3vdFRlJaQE+C74T3mZl3ze0nvp1Vq5yU9Swb8RMrcpeetSe/lPucb9o6+fNgjZV7xVemWpDBfDzkyBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgn8pP9P",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAeqz1gw9J95x9at7mQ2JDauqwtBSI6iIf8WdcVcMU/OICzgRJzW4hk2Pf3mYLMY+ImCnUiY7Va7Fm70NxulZnBrhAtlLWTTM3vdFRlJaQE+C74T3mZl3ze0nvp1Vq5yU9Swb8RMrcpeetSe/lPucb9o6+fNgjZV7xVemWpDBfDzkyBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgn8pP9P",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAeqz1gw9J95x9at7mQ2JDauqwtBSI6iIf8WdcVcMU/OICzgRJzW4hk2Pf3mYLMY+ImCnUiY7Va7Fm70NxulZnBrhAtlLWTTM3vdFRlJaQE+C74T3mZl3ze0nvp1Vq5yU9Swb8RMrcpeetSe/lPucb9o6+fNgjZV7xVemWpDBfDzkyBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgn8pP9P",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAeqz1gw9J95x9at7mQ2JDauqwtBSI6iIf8WdcVcMU/OICzgRJzW4hk2Pf3mYLMY+ImCnUiY7Va7Fm70NxulZnBrhAtlLWTTM3vdFRlJaQE+C74T3mZl3ze0nvp1Vq5yU9Swb8RMrcpeetSe/lPucb9o6+fNgjZV7xVemWpDBfDzkyBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgn8pP9P",
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
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "message": {
        "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "message": {
        "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello back",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423309,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
  "id": -576460752303423309,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "state": "tx_+QENCwH4hLhAeqz1gw9J95x9at7mQ2JDauqwtBSI6iIf8WdcVcMU/OICzgRJzW4hk2Pf3mYLMY+ImCnUiY7Va7Fm70NxulZnBrhAtlLWTTM3vdFRlJaQE+C74T3mZl3ze0nvp1Vq5yU9Swb8RMrcpeetSe/lPucb9o6+fNgjZV7xVemWpDBfDzkyBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgn8pP9P"
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "state": "tx_+QENCwH4hLhAeqz1gw9J95x9at7mQ2JDauqwtBSI6iIf8WdcVcMU/OICzgRJzW4hk2Pf3mYLMY+ImCnUiY7Va7Fm70NxulZnBrhAtlLWTTM3vdFRlJaQE+C74T3mZl3ze0nvp1Vq5yU9Swb8RMrcpeetSe/lPucb9o6+fNgjZV7xVemWpDBfDzkyBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgn8pP9P"
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBrdcLAgf7h+/2NTN/WSpSb11NqHgWebLvu5Y2CXcdcFXoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY2kdavv/+GG0jrV+ABAIYSMJzlQAAKbvOJ9g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423308,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAaulCQmxNkWG2tvCz4BGSNVMhDeqPai74zbbE6RYFVMrhAwv/IxypAkhlS3DVUfi8XczMqvESALtT7dCSK7TkNuF/4XTUBoQa3XCwIH+4fv9jUzf1kqUm9dTah4Fnmy77uWNgl3HXBV6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAACh/4iKU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
  "id": -576460752303423308,
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAaulCQmxNkWG2tvCz4BGSNVMhDeqPai74zbbE6RYFVMrhAwv/IxypAkhlS3DVUfi8XczMqvESALtT7dCSK7TkNuF/4XTUBoQa3XCwIH+4fv9jUzf1kqUm9dTah4Fnmy77uWNgl3HXBV6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAACh/4iKU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423307,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAaulCQmxNkWG2tvCz4BGSNVMhDeqPai74zbbE6RYFVMrhAwv/IxypAkhlS3DVUfi8XczMqvESALtT7dCSK7TkNuECV//seT3iMtgqNdWuko4NN9qpzk3zHhtHgqOi56OR8xcgB98vhytMBQhIZpSrgq++kcU8eyel2bVzmw65oevMLuF/4XTUBoQa3XCwIH+4fv9jUzf1kqUm9dTah4Fnmy77uWNgl3HXBV6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAACkdWhnw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
  "id": -576460752303423307,
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAaulCQmxNkWG2tvCz4BGSNVMhDeqPai74zbbE6RYFVMrhAwv/IxypAkhlS3DVUfi8XczMqvESALtT7dCSK7TkNuECV//seT3iMtgqNdWuko4NN9qpzk3zHhtHgqOi56OR8xcgB98vhytMBQhIZpSrgq++kcU8eyel2bVzmw65oevMLuF/4XTUBoQa3XCwIH+4fv9jUzf1kqUm9dTah4Fnmy77uWNgl3HXBV6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAACkdWhnw=",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAaulCQmxNkWG2tvCz4BGSNVMhDeqPai74zbbE6RYFVMrhAwv/IxypAkhlS3DVUfi8XczMqvESALtT7dCSK7TkNuECV//seT3iMtgqNdWuko4NN9qpzk3zHhtHgqOi56OR8xcgB98vhytMBQhIZpSrgq++kcU8eyel2bVzmw65oevMLuF/4XTUBoQa3XCwIH+4fv9jUzf1kqUm9dTah4Fnmy77uWNgl3HXBV6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAACkdWhnw=",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAaulCQmxNkWG2tvCz4BGSNVMhDeqPai74zbbE6RYFVMrhAwv/IxypAkhlS3DVUfi8XczMqvESALtT7dCSK7TkNuECV//seT3iMtgqNdWuko4NN9qpzk3zHhtHgqOi56OR8xcgB98vhytMBQhIZpSrgq++kcU8eyel2bVzmw65oevMLuF/4XTUBoQa3XCwIH+4fv9jUzf1kqUm9dTah4Fnmy77uWNgl3HXBV6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAACkdWhnw=",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAaulCQmxNkWG2tvCz4BGSNVMhDeqPai74zbbE6RYFVMrhAwv/IxypAkhlS3DVUfi8XczMqvESALtT7dCSK7TkNuECV//seT3iMtgqNdWuko4NN9qpzk3zHhtHgqOi56OR8xcgB98vhytMBQhIZpSrgq++kcU8eyel2bVzmw65oevMLuF/4XTUBoQa3XCwIH+4fv9jUzf1kqUm9dTah4Fnmy77uWNgl3HXBV6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAACkdWhnw=",
      "type": "channel_close_mutual_tx"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator
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
      "fsm_id": "ba_NiXGnksQOklx4PPOnhmWd7FgtMy5VyoI2m100JJeSJ3zdq6Z"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder
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
      "fsm_id": "ba_pCqpWyb2WX0yxIvpE6R53g4qmgPzNih9aN6vbVvaCwC9MGAY"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYL+UH4dQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423306,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBkBFXeML8hl+MNdrJPeAXPONGPms9YOAofA6mzxFWP2oluGk01KFppC28FhTKm/dcIvTaNsgPZlLsULzWU4EkOuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2C9jwrCY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423306,
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
      "signed_tx": "tx_+MsLAfhCuEBkBFXeML8hl+MNdrJPeAXPONGPms9YOAofA6mzxFWP2oluGk01KFppC28FhTKm/dcIvTaNsgPZlLsULzWU4EkOuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2C9jwrCY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423305,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAZARV3jC/IZfjDXayT3gFzzjRj5rPWDgKHwOps8RVj9qJbhpNNShaaQtvBYUypv3XCL02jbID2ZS7FC81lOBJDrhAuceZ51JCijzchwTkYRXHUB05wLIj9F4bCF5a9Mdf4ZmELmSRYkK00pFx++gWsmJuN3o9Io0Z7nsCAwoeLRmMBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdguqDJTh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423305,
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAZARV3jC/IZfjDXayT3gFzzjRj5rPWDgKHwOps8RVj9qJbhpNNShaaQtvBYUypv3XCL02jbID2ZS7FC81lOBJDrhAuceZ51JCijzchwTkYRXHUB05wLIj9F4bCF5a9Mdf4ZmELmSRYkK00pFx++gWsmJuN3o9Io0Z7nsCAwoeLRmMBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdguqDJTh",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAZARV3jC/IZfjDXayT3gFzzjRj5rPWDgKHwOps8RVj9qJbhpNNShaaQtvBYUypv3XCL02jbID2ZS7FC81lOBJDrhAuceZ51JCijzchwTkYRXHUB05wLIj9F4bCF5a9Mdf4ZmELmSRYkK00pFx++gWsmJuN3o9Io0Z7nsCAwoeLRmMBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdguqDJTh",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAZARV3jC/IZfjDXayT3gFzzjRj5rPWDgKHwOps8RVj9qJbhpNNShaaQtvBYUypv3XCL02jbID2ZS7FC81lOBJDrhAuceZ51JCijzchwTkYRXHUB05wLIj9F4bCF5a9Mdf4ZmELmSRYkK00pFx++gWsmJuN3o9Io0Z7nsCAwoeLRmMBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdguqDJTh",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAZARV3jC/IZfjDXayT3gFzzjRj5rPWDgKHwOps8RVj9qJbhpNNShaaQtvBYUypv3XCL02jbID2ZS7FC81lOBJDrhAuceZ51JCijzchwTkYRXHUB05wLIj9F4bCF5a9Mdf4ZmELmSRYkK00pFx++gWsmJuN3o9Io0Z7nsCAwoeLRmMBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdguqDJTh",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
    "channel_id": "ch_2Pkgoin4o7yjU4G3gm7vAb5gBjvF5jSW8tMphy2auWX9kjBi2N",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator closes WebSocket connection
```

```

#### responder closes WebSocket connection
```

```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "message": {
        "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "message": {
        "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello back",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423304,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
  "id": -576460752303423304,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "state": "tx_+QENCwH4hLhAZARV3jC/IZfjDXayT3gFzzjRj5rPWDgKHwOps8RVj9qJbhpNNShaaQtvBYUypv3XCL02jbID2ZS7FC81lOBJDrhAuceZ51JCijzchwTkYRXHUB05wLIj9F4bCF5a9Mdf4ZmELmSRYkK00pFx++gWsmJuN3o9Io0Z7nsCAwoeLRmMBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdguqDJTh"
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "state": "tx_+QENCwH4hLhAZARV3jC/IZfjDXayT3gFzzjRj5rPWDgKHwOps8RVj9qJbhpNNShaaQtvBYUypv3XCL02jbID2ZS7FC81lOBJDrhAuceZ51JCijzchwTkYRXHUB05wLIj9F4bCF5a9Mdf4ZmELmSRYkK00pFx++gWsmJuN3o9Io0Z7nsCAwoeLRmMBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdguqDJTh"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBh0/EhZR0OdFP6sc6avKlzEJds1S0yx+tPulGbDUgHW6oQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y2kdavv/+GG0jrV+ABAIYSMJzlQAADHr6PMA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423303,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDku6FjeJ5vzMbF/tQDcUurpaRCXPQtQBW3rI8X/TfRiG1F7KChel6U9dCfXl2FRZDprZgYNFps9cHoTBdmIuAEuF/4XTUBoQYdPxIWUdDnRT+rHOmrypcxCXbNUtMsfrT7pRmw1IB1uqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GNpHWr7//hhtI61fgAQCGEjCc5UAAA2uYE20="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
  "id": -576460752303423303,
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDku6FjeJ5vzMbF/tQDcUurpaRCXPQtQBW3rI8X/TfRiG1F7KChel6U9dCfXl2FRZDprZgYNFps9cHoTBdmIuAEuF/4XTUBoQYdPxIWUdDnRT+rHOmrypcxCXbNUtMsfrT7pRmw1IB1uqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GNpHWr7//hhtI61fgAQCGEjCc5UAAA2uYE20=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423302,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEDku6FjeJ5vzMbF/tQDcUurpaRCXPQtQBW3rI8X/TfRiG1F7KChel6U9dCfXl2FRZDprZgYNFps9cHoTBdmIuAEuED38O+FOKD+9B5YHhjjxibZNLO7rN5e43bJ0sLkwagaKNA35hMBwA03/vmGcpn0EONIi9BFp5yc+qFeL1frzCQDuF/4XTUBoQYdPxIWUdDnRT+rHOmrypcxCXbNUtMsfrT7pRmw1IB1uqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GNpHWr7//hhtI61fgAQCGEjCc5UAAA/gAKIM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
  "id": -576460752303423302,
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEDku6FjeJ5vzMbF/tQDcUurpaRCXPQtQBW3rI8X/TfRiG1F7KChel6U9dCfXl2FRZDprZgYNFps9cHoTBdmIuAEuED38O+FOKD+9B5YHhjjxibZNLO7rN5e43bJ0sLkwagaKNA35hMBwA03/vmGcpn0EONIi9BFp5yc+qFeL1frzCQDuF/4XTUBoQYdPxIWUdDnRT+rHOmrypcxCXbNUtMsfrT7pRmw1IB1uqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GNpHWr7//hhtI61fgAQCGEjCc5UAAA/gAKIM=",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEDku6FjeJ5vzMbF/tQDcUurpaRCXPQtQBW3rI8X/TfRiG1F7KChel6U9dCfXl2FRZDprZgYNFps9cHoTBdmIuAEuED38O+FOKD+9B5YHhjjxibZNLO7rN5e43bJ0sLkwagaKNA35hMBwA03/vmGcpn0EONIi9BFp5yc+qFeL1frzCQDuF/4XTUBoQYdPxIWUdDnRT+rHOmrypcxCXbNUtMsfrT7pRmw1IB1uqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GNpHWr7//hhtI61fgAQCGEjCc5UAAA/gAKIM=",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEDku6FjeJ5vzMbF/tQDcUurpaRCXPQtQBW3rI8X/TfRiG1F7KChel6U9dCfXl2FRZDprZgYNFps9cHoTBdmIuAEuED38O+FOKD+9B5YHhjjxibZNLO7rN5e43bJ0sLkwagaKNA35hMBwA03/vmGcpn0EONIi9BFp5yc+qFeL1frzCQDuF/4XTUBoQYdPxIWUdDnRT+rHOmrypcxCXbNUtMsfrT7pRmw1IB1uqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GNpHWr7//hhtI61fgAQCGEjCc5UAAA/gAKIM=",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEDku6FjeJ5vzMbF/tQDcUurpaRCXPQtQBW3rI8X/TfRiG1F7KChel6U9dCfXl2FRZDprZgYNFps9cHoTBdmIuAEuED38O+FOKD+9B5YHhjjxibZNLO7rN5e43bJ0sLkwagaKNA35hMBwA03/vmGcpn0EONIi9BFp5yc+qFeL1frzCQDuF/4XTUBoQYdPxIWUdDnRT+rHOmrypcxCXbNUtMsfrT7pRmw1IB1uqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GNpHWr7//hhtI61fgAQCGEjCc5UAAA/gAKIM=",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
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
    "channel_id": "ch_Dt4SMmMaNmE6pouQNXhWLRWnJsA3GUxvWpgCzBXysQSNmWYzi",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator closes WebSocket connection
```

```
