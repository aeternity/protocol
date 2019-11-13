
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reconnect%2F3304
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
      "fsm_id": "ba_i6R2Ittsg7Vora7gu1O4oZGFs8x7oePH8s0jZwxjz90nrOui"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=true&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reconnect%2F3304
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
      "fsm_id": "ba_kH4aruclwMpbcLd8XUuBk5lR003ru4W6N1zS1Z+X/hUmhbTp"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYYvF2Byg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423187,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA7YalnOCEsnNhZ0dStxTZ7OhBXSxkirmQXreKPHTXOFYspL0egCWLsnQSxw1aoisKaC6InLJr2zhsUQNb3YvoHuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2GBXSkJU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423187,
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
      "signed_tx": "tx_+MsLAfhCuEA7YalnOCEsnNhZ0dStxTZ7OhBXSxkirmQXreKPHTXOFYspL0egCWLsnQSxw1aoisKaC6InLJr2zhsUQNb3YvoHuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2GBXSkJU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423186,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423186,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "message": {
        "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "message": {
        "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
  "id": -576460752303423185,
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
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423185,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T"
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T"
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T"
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "event": "peer_disconnected"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s%2FPLChJsuTNM2ELC8AbiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhjJLd9T&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s%2FPLChJsuTNM2ELC8AbiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhjJLd9T&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5&existing_fsm_id=ba_pKqs74LBR6aAvFax&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s%2FPLChJsuTNM2ELC8AbiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhjJLd9T&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5&existing_fsm_id=ba_OgGIO2VfcBjPm6d2lege4L6%2B9YO7D9UY57zwPM8N1D%2BlueEj&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s%2FPLChJsuTNM2ELC8AbiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhjJLd9T&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5&existing_fsm_id=ba_i6R2Ittsg7Vora7gu1O4oZGFs8x7oePH8s0jZwxjz90nrOui&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s%2FPLChJsuTNM2ELC8AbiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhjJLd9T&port=13179&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_qxut1McurPZHPDbkkLRN4iTaWfth3ZBZGMKckelEQGvUr18U"
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+QENCwH4hLhAO2GpZzghLJzYWdHUrcU2ezoQV0sZIq5kF63ijx01zhWLKS9HoAli7J0EscNWqIrCmguiJyya9s4bFEDW92L6B7hAWyH4nUpPnCiEqyNcqf6Fi22SoXbiobJp4iaoYOGFSgrxAMt9unIxg8m0w2sU7NFg8m7s/PLChJsuTNM2ELC8AbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhjJLd9T"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423184,
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
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423184,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "meta": 17,
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "meta": 17,
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhsR2L7LkmbGZ+61nECis/zWHxVAINcPtaSoH7SgpjMnAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt4K/t+E=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303423183,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA6CvacJCWOO/6GYlE5FKS6iUTr26OQqawXJixA9nXPJkWP3aS1B60dpb8iYqoO73t1ZWaUSrnIJcFfe1Ttk9gGuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eqvotM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423183,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA6CvacJCWOO/6GYlE5FKS6iUTr26OQqawXJixA9nXPJkWP3aS1B60dpb8iYqoO73t1ZWaUSrnIJcFfe1Ttk9gGuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eqvotM",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303423182,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAKcLF90B/gURAfYG265j1iOa+D1u7e51P6vIY15QjI7XVSrgX9Wbs4TmMCKhH+PrQi1wxGoFmzAHzUhvfDVTcHuEA6CvacJCWOO/6GYlE5FKS6iUTr26OQqawXJixA9nXPJkWP3aS1B60dpb8iYqoO73t1ZWaUSrnIJcFfe1Ttk9gGuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fKoYwd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423182,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEAKcLF90B/gURAfYG265j1iOa+D1u7e51P6vIY15QjI7XVSrgX9Wbs4TmMCKhH+PrQi1wxGoFmzAHzUhvfDVTcHuEA6CvacJCWOO/6GYlE5FKS6iUTr26OQqawXJixA9nXPJkWP3aS1B60dpb8iYqoO73t1ZWaUSrnIJcFfe1Ttk9gGuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fKoYwd"
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEAKcLF90B/gURAfYG265j1iOa+D1u7e51P6vIY15QjI7XVSrgX9Wbs4TmMCKhH+PrQi1wxGoFmzAHzUhvfDVTcHuEA6CvacJCWOO/6GYlE5FKS6iUTr26OQqawXJixA9nXPJkWP3aS1B60dpb8iYqoO73t1ZWaUSrnIJcFfe1Ttk9gGuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fKoYwd"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423181,
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
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423181,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999998
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423180,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423180,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAKcLF90B/gURAfYG265j1iOa+D1u7e51P6vIY15QjI7XVSrgX9Wbs4TmMCKhH+PrQi1wxGoFmzAHzUhvfDVTcHuEA6CvacJCWOO/6GYlE5FKS6iUTr26OQqawXJixA9nXPJkWP3aS1B60dpb8iYqoO73t1ZWaUSrnIJcFfe1Ttk9gGuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fKoYwd",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423179,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423179,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000002
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "meta": 17,
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "meta": 17,
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhsR2L7LkmbGZ+61nECis/zWHxVAINcPtaSoH7SgpjMnA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgXcAVg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303423178,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDIFo2oxKFUqaRsQr/XmeWIGIQ4EGDLruOuHjLe/9UPocl1zk8c1EM4/m0VsyBfPmtminfZi3OHvla9Upb0M0sCuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnboFmNg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423178,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDIFo2oxKFUqaRsQr/XmeWIGIQ4EGDLruOuHjLe/9UPocl1zk8c1EM4/m0VsyBfPmtminfZi3OHvla9Upb0M0sCuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnboFmNg",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303423177,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDIFo2oxKFUqaRsQr/XmeWIGIQ4EGDLruOuHjLe/9UPocl1zk8c1EM4/m0VsyBfPmtminfZi3OHvla9Upb0M0sCuEDryVFqnBOT1yrwQ8brGGeLNu3BlVGyYJlqnCMm1t1A+XRum4flyqhMXF+NXr0q1nZrwt+3sF5Wh1heRN1UMKMIuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnazvJvO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423177,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEDIFo2oxKFUqaRsQr/XmeWIGIQ4EGDLruOuHjLe/9UPocl1zk8c1EM4/m0VsyBfPmtminfZi3OHvla9Upb0M0sCuEDryVFqnBOT1yrwQ8brGGeLNu3BlVGyYJlqnCMm1t1A+XRum4flyqhMXF+NXr0q1nZrwt+3sF5Wh1heRN1UMKMIuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnazvJvO"
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEDIFo2oxKFUqaRsQr/XmeWIGIQ4EGDLruOuHjLe/9UPocl1zk8c1EM4/m0VsyBfPmtminfZi3OHvla9Upb0M0sCuEDryVFqnBOT1yrwQ8brGGeLNu3BlVGyYJlqnCMm1t1A+XRum4flyqhMXF+NXr0q1nZrwt+3sF5Wh1heRN1UMKMIuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnazvJvO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423176,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423176,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000001
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423175,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423175,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDIFo2oxKFUqaRsQr/XmeWIGIQ4EGDLruOuHjLe/9UPocl1zk8c1EM4/m0VsyBfPmtminfZi3OHvla9Upb0M0sCuEDryVFqnBOT1yrwQ8brGGeLNu3BlVGyYJlqnCMm1t1A+XRum4flyqhMXF+NXr0q1nZrwt+3sF5Wh1heRN1UMKMIuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnazvJvO",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423174,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423174,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000001
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "meta": 17,
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "meta": 17,
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhsR2L7LkmbGZ+61nECis/zWHxVAINcPtaSoH7SgpjMnBKBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUArjy1xc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303423173,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAIYbUzZi3WtZz0xvwrWQBgGTnrftkz44HWRujnphqYWD3abjj18dRQowAg7yBqi3s2RX8UkGqEe2zXws40AxkDuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIuoWMc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423173,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAIYbUzZi3WtZz0xvwrWQBgGTnrftkz44HWRujnphqYWD3abjj18dRQowAg7yBqi3s2RX8UkGqEe2zXws40AxkDuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIuoWMc",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303423172,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAIYbUzZi3WtZz0xvwrWQBgGTnrftkz44HWRujnphqYWD3abjj18dRQowAg7yBqi3s2RX8UkGqEe2zXws40AxkDuECgzgynTdC8KDfis1hjDOhT2mjlSoQZXjhCe3Sskmo2XZ3tG1MQDMjnVwX1gIzg8G/u5rVk7r6y40MPQO6tWQIHuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI+hvlK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423172,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEAIYbUzZi3WtZz0xvwrWQBgGTnrftkz44HWRujnphqYWD3abjj18dRQowAg7yBqi3s2RX8UkGqEe2zXws40AxkDuECgzgynTdC8KDfis1hjDOhT2mjlSoQZXjhCe3Sskmo2XZ3tG1MQDMjnVwX1gIzg8G/u5rVk7r6y40MPQO6tWQIHuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI+hvlK"
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEAIYbUzZi3WtZz0xvwrWQBgGTnrftkz44HWRujnphqYWD3abjj18dRQowAg7yBqi3s2RX8UkGqEe2zXws40AxkDuECgzgynTdC8KDfis1hjDOhT2mjlSoQZXjhCe3Sskmo2XZ3tG1MQDMjnVwX1gIzg8G/u5rVk7r6y40MPQO6tWQIHuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI+hvlK"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423171,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423171,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000000
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423170,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423170,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAIYbUzZi3WtZz0xvwrWQBgGTnrftkz44HWRujnphqYWD3abjj18dRQowAg7yBqi3s2RX8UkGqEe2zXws40AxkDuECgzgynTdC8KDfis1hjDOhT2mjlSoQZXjhCe3Sskmo2XZ3tG1MQDMjnVwX1gIzg8G/u5rVk7r6y40MPQO6tWQIHuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI+hvlK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423169,
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
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423169,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 70000000000000
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "meta": 17,
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "meta": 17,
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhsR2L7LkmbGZ+61nECis/zWHxVAINcPtaSoH7SgpjMnBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdr52obA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303423168,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC3Tg7wddhmixYyWc5Cc84eB8SDj+CQ7wpKFQHEFT4FHatuEIg/aCE7G2WY5LKmk52MqX7fL11O7ezEivkJX9oNuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaACRbk"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423168,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC3Tg7wddhmixYyWc5Cc84eB8SDj+CQ7wpKFQHEFT4FHatuEIg/aCE7G2WY5LKmk52MqX7fL11O7ezEivkJX9oNuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaACRbk",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303423167,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBYa3N1nlUZ4WI9LjsP8Szd5JlkFhkkr8JZaCNVWIcR+6xW2gzj1qaCuTIt45t2nKkInbq+9qAR5/Zyo6LxTZ8JuEC3Tg7wddhmixYyWc5Cc84eB8SDj+CQ7wpKFQHEFT4FHatuEIg/aCE7G2WY5LKmk52MqX7fL11O7ezEivkJX9oNuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYVS2JX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423167,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEBYa3N1nlUZ4WI9LjsP8Szd5JlkFhkkr8JZaCNVWIcR+6xW2gzj1qaCuTIt45t2nKkInbq+9qAR5/Zyo6LxTZ8JuEC3Tg7wddhmixYyWc5Cc84eB8SDj+CQ7wpKFQHEFT4FHatuEIg/aCE7G2WY5LKmk52MqX7fL11O7ezEivkJX9oNuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYVS2JX"
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEBYa3N1nlUZ4WI9LjsP8Szd5JlkFhkkr8JZaCNVWIcR+6xW2gzj1qaCuTIt45t2nKkInbq+9qAR5/Zyo6LxTZ8JuEC3Tg7wddhmixYyWc5Cc84eB8SDj+CQ7wpKFQHEFT4FHatuEIg/aCE7G2WY5LKmk52MqX7fL11O7ezEivkJX9oNuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYVS2JX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423166,
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
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423166,
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

#### initiator ---> node
```javascript
{
  "id": -576460752303423165,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423165,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBYa3N1nlUZ4WI9LjsP8Szd5JlkFhkkr8JZaCNVWIcR+6xW2gzj1qaCuTIt45t2nKkInbq+9qAR5/Zyo6LxTZ8JuEC3Tg7wddhmixYyWc5Cc84eB8SDj+CQ7wpKFQHEFT4FHatuEIg/aCE7G2WY5LKmk52MqX7fL11O7ezEivkJX9oNuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYVS2JX",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423164,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423164,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000001
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "meta": 17,
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "meta": 17,
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhsR2L7LkmbGZ+61nECis/zWHxVAINcPtaSoH7SgpjMnBqBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAuDEg2o=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303423163,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBcwAfSOaBdiDIjPzAWOBSgxYwf9wHzUkG9kUOs1Bxzr77BGYjleDRQAewjKQ9QHc/RS/EVkDZE4lI4da+oS2EFuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJ13bgi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423163,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBcwAfSOaBdiDIjPzAWOBSgxYwf9wHzUkG9kUOs1Bxzr77BGYjleDRQAewjKQ9QHc/RS/EVkDZE4lI4da+oS2EFuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJ13bgi",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303423162,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBcwAfSOaBdiDIjPzAWOBSgxYwf9wHzUkG9kUOs1Bxzr77BGYjleDRQAewjKQ9QHc/RS/EVkDZE4lI4da+oS2EFuEBd33yirxEOBs+S7lYnZit0SuLnrjtQLm1/aKLBHFziGqpcRUS7dMHlaRBGUD03aSdnTpRaXNKUxfMEPC7d3PUMuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKILCvv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423162,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEBcwAfSOaBdiDIjPzAWOBSgxYwf9wHzUkG9kUOs1Bxzr77BGYjleDRQAewjKQ9QHc/RS/EVkDZE4lI4da+oS2EFuEBd33yirxEOBs+S7lYnZit0SuLnrjtQLm1/aKLBHFziGqpcRUS7dMHlaRBGUD03aSdnTpRaXNKUxfMEPC7d3PUMuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKILCvv"
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
    "data": {
      "state": "tx_+NILAfiEuEBcwAfSOaBdiDIjPzAWOBSgxYwf9wHzUkG9kUOs1Bxzr77BGYjleDRQAewjKQ9QHc/RS/EVkDZE4lI4da+oS2EFuEBd33yirxEOBs+S7lYnZit0SuLnrjtQLm1/aKLBHFziGqpcRUS7dMHlaRBGUD03aSdnTpRaXNKUxfMEPC7d3PUMuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKILCvv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423161,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423161,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000000
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423160,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423160,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBcwAfSOaBdiDIjPzAWOBSgxYwf9wHzUkG9kUOs1Bxzr77BGYjleDRQAewjKQ9QHc/RS/EVkDZE4lI4da+oS2EFuEBd33yirxEOBs+S7lYnZit0SuLnrjtQLm1/aKLBHFziGqpcRUS7dMHlaRBGUD03aSdnTpRaXNKUxfMEPC7d3PUMuEj4RjkCoQYbEdi+y5JmxmfutZxAorP81h8VQCDXD7WkqB+0oKYzJwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKILCvv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423159,
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
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423159,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423158,
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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
    "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
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

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CvTem4ScTwkb5hLZPL11Z8rhYZMcXRjfXKyLgst56DxTztmt5",
  "id": -576460752303423158,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
