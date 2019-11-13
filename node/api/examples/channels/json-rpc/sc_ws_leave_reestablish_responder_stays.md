
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_responder_stays%2F3295
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
      "fsm_id": "ba_2k6Xpzw96jNidmEwuHb7qLV5aYncKGGJxgqTa+iwbykG7ZI8"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=true&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_responder_stays%2F3295
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
      "fsm_id": "ba_ynYrdv/krAqysuOvKj8Yz51RZDVMLZDDUkmuDUt7x1wLx12H"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYXbmMChA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423217,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECXHVM5CGYDDK5KUMXtYkq1ESQaJe+l3KglI+BRbzb6UrRnYIv1gawoH1LESU47vy5tz9DG9JCtTUddnm4E9yYIuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Fzv/qSY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423217,
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
      "signed_tx": "tx_+MsLAfhCuECXHVM5CGYDDK5KUMXtYkq1ESQaJe+l3KglI+BRbzb6UrRnYIv1gawoH1LESU47vy5tz9DG9JCtTUddnm4E9yYIuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Fzv/qSY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423216,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423216,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "message": {
        "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "message": {
        "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "id": -576460752303423215,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423215,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "event": "peer_disconnected"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs&existing_fsm_id=ba_2k6Xpzw96jNidmEwuHb7qLV5aYncKGGJxgqTa%2BiwbykG7ZI8&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82%2BlK0Z2CL9YGsKB9SxElOO78ubc%2FQxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB%2B8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2%2BsXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhdK0mSu&port=13179&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_Khi/qjDKo7hGex+l0gfg4xa907rzOdKR9cuO9Av1dLuXJ6HT"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+QENCwH4hLhAlx1TOQhmAwyuSlDF7WJKtREkGiXvpdyoJSPgUW82+lK0Z2CL9YGsKB9SxElOO78ubc/QxvSQrU1HXZ5uBPcmCLhAvawGuN8YQBsYG9IMgFCB+8fsCNb5i8ToSKp8AVdWXILFhxH6Yth2+sXXZE5HHdRzw8nxJvcpIZiw7GNnLFjNCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhdK0mSu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423214,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423214,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiPEzIX5zd9AjMDzTaKvDQvz685molZcAnYp8TuNItprAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrtz1LoAc=",
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
  "id": -576460752303423213,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECgw/guITOk6II3I6LvBl0K5qXBOI7gatzjkRJWFjfJW7F3M7Yt7ycszIv7Vyhu2JZUcHyaeWCB5n2K/gcPbFwLuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dbXfVN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423213,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+JALAfhCuECgw/guITOk6II3I6LvBl0K5qXBOI7gatzjkRJWFjfJW7F3M7Yt7ycszIv7Vyhu2JZUcHyaeWCB5n2K/gcPbFwLuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dbXfVN",
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
  "id": -576460752303423212,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECUgNagFlkKVsKRiFbVzzWwye/ehmYxXB7hhCwCU9KDQ6TkR+1kO0M+9oxF7YTXKcmztYX0AqGKRbO8d7n8iisJuECgw/guITOk6II3I6LvBl0K5qXBOI7gatzjkRJWFjfJW7F3M7Yt7ycszIv7Vyhu2JZUcHyaeWCB5n2K/gcPbFwLuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eYpZrP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423212,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuECUgNagFlkKVsKRiFbVzzWwye/ehmYxXB7hhCwCU9KDQ6TkR+1kO0M+9oxF7YTXKcmztYX0AqGKRbO8d7n8iisJuECgw/guITOk6II3I6LvBl0K5qXBOI7gatzjkRJWFjfJW7F3M7Yt7ycszIv7Vyhu2JZUcHyaeWCB5n2K/gcPbFwLuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eYpZrP"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuECUgNagFlkKVsKRiFbVzzWwye/ehmYxXB7hhCwCU9KDQ6TkR+1kO0M+9oxF7YTXKcmztYX0AqGKRbO8d7n8iisJuECgw/guITOk6II3I6LvBl0K5qXBOI7gatzjkRJWFjfJW7F3M7Yt7ycszIv7Vyhu2JZUcHyaeWCB5n2K/gcPbFwLuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eYpZrP"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423211,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423211,
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
  "id": -576460752303423210,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423210,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECUgNagFlkKVsKRiFbVzzWwye/ehmYxXB7hhCwCU9KDQ6TkR+1kO0M+9oxF7YTXKcmztYX0AqGKRbO8d7n8iisJuECgw/guITOk6II3I6LvBl0K5qXBOI7gatzjkRJWFjfJW7F3M7Yt7ycszIv7Vyhu2JZUcHyaeWCB5n2K/gcPbFwLuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eYpZrP",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423209,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423209,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiPEzIX5zd9AjMDzTaKvDQvz685molZcAnYp8TuNItprA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdvHJ788=",
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
  "id": -576460752303423208,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECQi5x+vnuDxIkP6ROOTO/ZY8UgihKYgN4WSXJnxdBaguo3fnoXNoo2Sr5TJgRGLm/yLhlDsTVqi66AEjZb1DMEuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYWi7IU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423208,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+JALAfhCuECQi5x+vnuDxIkP6ROOTO/ZY8UgihKYgN4WSXJnxdBaguo3fnoXNoo2Sr5TJgRGLm/yLhlDsTVqi66AEjZb1DMEuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYWi7IU",
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
  "id": -576460752303423207,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAaD/4uRxWPXtQ4/O20A3OpnPbKRSaUL9u2F0mNE9HNcvUsdtxn3//ZnmCL0HcPqhZoOeV9Vvr1T8m74gkAOP0OuECQi5x+vnuDxIkP6ROOTO/ZY8UgihKYgN4WSXJnxdBaguo3fnoXNoo2Sr5TJgRGLm/yLhlDsTVqi66AEjZb1DMEuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYCPuWT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423207,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuEAaD/4uRxWPXtQ4/O20A3OpnPbKRSaUL9u2F0mNE9HNcvUsdtxn3//ZnmCL0HcPqhZoOeV9Vvr1T8m74gkAOP0OuECQi5x+vnuDxIkP6ROOTO/ZY8UgihKYgN4WSXJnxdBaguo3fnoXNoo2Sr5TJgRGLm/yLhlDsTVqi66AEjZb1DMEuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYCPuWT"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuEAaD/4uRxWPXtQ4/O20A3OpnPbKRSaUL9u2F0mNE9HNcvUsdtxn3//ZnmCL0HcPqhZoOeV9Vvr1T8m74gkAOP0OuECQi5x+vnuDxIkP6ROOTO/ZY8UgihKYgN4WSXJnxdBaguo3fnoXNoo2Sr5TJgRGLm/yLhlDsTVqi66AEjZb1DMEuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYCPuWT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423206,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423206,
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
  "id": -576460752303423205,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423205,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAaD/4uRxWPXtQ4/O20A3OpnPbKRSaUL9u2F0mNE9HNcvUsdtxn3//ZnmCL0HcPqhZoOeV9Vvr1T8m74gkAOP0OuECQi5x+vnuDxIkP6ROOTO/ZY8UgihKYgN4WSXJnxdBaguo3fnoXNoo2Sr5TJgRGLm/yLhlDsTVqi66AEjZb1DMEuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYCPuWT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423204,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423204,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiPEzIX5zd9AjMDzTaKvDQvz685molZcAnYp8TuNItprBKBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAj1r/ag=",
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
  "id": -576460752303423203,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC1WJc+vKv3zrJY7xyBSsUnYw+I9Ak+k47eVyGNd53prVlLyVS15tbwby4U5rddr+XqPdZxNleppf8ea48lDGoOuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI7mWku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423203,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC1WJc+vKv3zrJY7xyBSsUnYw+I9Ak+k47eVyGNd53prVlLyVS15tbwby4U5rddr+XqPdZxNleppf8ea48lDGoOuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI7mWku",
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
  "id": -576460752303423202,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECev3c+0veoIiyoxRD09RfP3GK0p5ZPXSDjtiAQ6QEm83xx2Opu1mB4G9HXtXmXTMICbX/vVOHQh23M9snmwqsBuEC1WJc+vKv3zrJY7xyBSsUnYw+I9Ak+k47eVyGNd53prVlLyVS15tbwby4U5rddr+XqPdZxNleppf8ea48lDGoOuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALJjRo0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423202,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuECev3c+0veoIiyoxRD09RfP3GK0p5ZPXSDjtiAQ6QEm83xx2Opu1mB4G9HXtXmXTMICbX/vVOHQh23M9snmwqsBuEC1WJc+vKv3zrJY7xyBSsUnYw+I9Ak+k47eVyGNd53prVlLyVS15tbwby4U5rddr+XqPdZxNleppf8ea48lDGoOuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALJjRo0"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuECev3c+0veoIiyoxRD09RfP3GK0p5ZPXSDjtiAQ6QEm83xx2Opu1mB4G9HXtXmXTMICbX/vVOHQh23M9snmwqsBuEC1WJc+vKv3zrJY7xyBSsUnYw+I9Ak+k47eVyGNd53prVlLyVS15tbwby4U5rddr+XqPdZxNleppf8ea48lDGoOuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALJjRo0"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423201,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423201,
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
  "id": -576460752303423200,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423200,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECev3c+0veoIiyoxRD09RfP3GK0p5ZPXSDjtiAQ6QEm83xx2Opu1mB4G9HXtXmXTMICbX/vVOHQh23M9snmwqsBuEC1WJc+vKv3zrJY7xyBSsUnYw+I9Ak+k47eVyGNd53prVlLyVS15tbwby4U5rddr+XqPdZxNleppf8ea48lDGoOuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALJjRo0",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423199,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423199,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiPEzIX5zd9AjMDzTaKvDQvz685molZcAnYp8TuNItprBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdmJvIY8=",
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
  "id": -576460752303423198,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECSHJjkS3kCG6+6B9PaveatREhx9VSeI24FYtAy5vmcJ7oOxhDeXPOr0erbW6bk/BO2xPYFPqK26WDF6hktnxMJuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZPrUyW"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423198,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+JALAfhCuECSHJjkS3kCG6+6B9PaveatREhx9VSeI24FYtAy5vmcJ7oOxhDeXPOr0erbW6bk/BO2xPYFPqK26WDF6hktnxMJuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZPrUyW",
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
  "id": -576460752303423197,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBHvX5CV9B9Si8WrjMtz3WEorko/V811til+e3M0aU97YMCFBP6at8W1oZZT0PSjO5uUqrFBLRn6/2brkoGeogOuECSHJjkS3kCG6+6B9PaveatREhx9VSeI24FYtAy5vmcJ7oOxhDeXPOr0erbW6bk/BO2xPYFPqK26WDF6hktnxMJuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYvLYg1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423197,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuEBHvX5CV9B9Si8WrjMtz3WEorko/V811til+e3M0aU97YMCFBP6at8W1oZZT0PSjO5uUqrFBLRn6/2brkoGeogOuECSHJjkS3kCG6+6B9PaveatREhx9VSeI24FYtAy5vmcJ7oOxhDeXPOr0erbW6bk/BO2xPYFPqK26WDF6hktnxMJuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYvLYg1"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuEBHvX5CV9B9Si8WrjMtz3WEorko/V811til+e3M0aU97YMCFBP6at8W1oZZT0PSjO5uUqrFBLRn6/2brkoGeogOuECSHJjkS3kCG6+6B9PaveatREhx9VSeI24FYtAy5vmcJ7oOxhDeXPOr0erbW6bk/BO2xPYFPqK26WDF6hktnxMJuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYvLYg1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423196,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423196,
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
  "id": -576460752303423195,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423195,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBHvX5CV9B9Si8WrjMtz3WEorko/V811til+e3M0aU97YMCFBP6at8W1oZZT0PSjO5uUqrFBLRn6/2brkoGeogOuECSHJjkS3kCG6+6B9PaveatREhx9VSeI24FYtAy5vmcJ7oOxhDeXPOr0erbW6bk/BO2xPYFPqK26WDF6hktnxMJuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYvLYg1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423194,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423194,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiPEzIX5zd9AjMDzTaKvDQvz685molZcAnYp8TuNItprBqBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAho4zA8=",
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
  "id": -576460752303423193,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED2QnBVy6UzkqQQopVNHZQXPPfjgSoN+rTF/T6WYL4F0S8UXX9QrnYWXGZnS+pqf7hD11BBm3ffxUN/oSyM6O0CuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJB26/Y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423193,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "signed_tx": "tx_+JALAfhCuED2QnBVy6UzkqQQopVNHZQXPPfjgSoN+rTF/T6WYL4F0S8UXX9QrnYWXGZnS+pqf7hD11BBm3ffxUN/oSyM6O0CuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJB26/Y",
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
  "id": -576460752303423192,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECObw52Ppp24+SSR1C17TDxqH9/sFmKqIpzKBNq0ZAvW1zEqIsQTmAM9He/qzwm+EBP9UFlYlVQiUfD6dvfw80MuED2QnBVy6UzkqQQopVNHZQXPPfjgSoN+rTF/T6WYL4F0S8UXX9QrnYWXGZnS+pqf7hD11BBm3ffxUN/oSyM6O0CuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKqCdh7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423192,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuECObw52Ppp24+SSR1C17TDxqH9/sFmKqIpzKBNq0ZAvW1zEqIsQTmAM9He/qzwm+EBP9UFlYlVQiUfD6dvfw80MuED2QnBVy6UzkqQQopVNHZQXPPfjgSoN+rTF/T6WYL4F0S8UXX9QrnYWXGZnS+pqf7hD11BBm3ffxUN/oSyM6O0CuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKqCdh7"
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
    "data": {
      "state": "tx_+NILAfiEuECObw52Ppp24+SSR1C17TDxqH9/sFmKqIpzKBNq0ZAvW1zEqIsQTmAM9He/qzwm+EBP9UFlYlVQiUfD6dvfw80MuED2QnBVy6UzkqQQopVNHZQXPPfjgSoN+rTF/T6WYL4F0S8UXX9QrnYWXGZnS+pqf7hD11BBm3ffxUN/oSyM6O0CuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKqCdh7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423191,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423191,
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
  "id": -576460752303423190,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423190,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECObw52Ppp24+SSR1C17TDxqH9/sFmKqIpzKBNq0ZAvW1zEqIsQTmAM9He/qzwm+EBP9UFlYlVQiUfD6dvfw80MuED2QnBVy6UzkqQQopVNHZQXPPfjgSoN+rTF/T6WYL4F0S8UXX9QrnYWXGZnS+pqf7hD11BBm3ffxUN/oSyM6O0CuEj4RjkCoQYjxMyF+c3fQIzA802irw0L8+vOZqJWXAJ2KfE7jSLaawagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKqCdh7",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423189,
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423189,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423188,
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
    "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
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
  "channel_id": "ch_GkfYjFXo13ZDwYgKq3yQatvZZjZeeQZPfVFGB6hfmqHneGnQs",
  "id": -576460752303423188,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
