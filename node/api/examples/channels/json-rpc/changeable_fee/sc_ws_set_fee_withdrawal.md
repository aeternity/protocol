
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
      "fsm_id": "ba_hgxPQ+MwVBLvRbGDgyciACUHPrrYV1AyWBqh6iQCK3Sjr1le"
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
      "fsm_id": "ba_ywrsWLew/UFysJLTiICPedLHFezuRWSM41jzCRdzDt2BUV/m"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYkK6hFyw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422978,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDGkQENTktYLjUuG+tXS2K5X3PG/5fDQBoq2xs5btY7p/WpxkFltmm6rXetjAnmM848eo1Z1ZqFzv3b7L6MoYYJuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2JEoXCJo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422978,
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
      "signed_tx": "tx_+MsLAfhCuEDGkQENTktYLjUuG+tXS2K5X3PG/5fDQBoq2xs5btY7p/WpxkFltmm6rXetjAnmM848eo1Z1ZqFzv3b7L6MoYYJuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2JEoXCJo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422977,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAxpEBDU5LWC41LhvrV0tiuV9zxv+Xw0AaKtsbOW7WO6f1qcZBZbZpuq13rYwJ5jPOPHqNWdWahc792+y+jKGGCbhA8Hh3RxnOY5S1mg3gPOMKvn63AMXy0tVpPItSmeRPnKhD82cvtPKBwbnlLSkGuTTrQngWDLBmUDR8o0fekpjmALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiTlrPVn"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422977,
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAxpEBDU5LWC41LhvrV0tiuV9zxv+Xw0AaKtsbOW7WO6f1qcZBZbZpuq13rYwJ5jPOPHqNWdWahc792+y+jKGGCbhA8Hh3RxnOY5S1mg3gPOMKvn63AMXy0tVpPItSmeRPnKhD82cvtPKBwbnlLSkGuTTrQngWDLBmUDR8o0fekpjmALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiTlrPVn",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAxpEBDU5LWC41LhvrV0tiuV9zxv+Xw0AaKtsbOW7WO6f1qcZBZbZpuq13rYwJ5jPOPHqNWdWahc792+y+jKGGCbhA8Hh3RxnOY5S1mg3gPOMKvn63AMXy0tVpPItSmeRPnKhD82cvtPKBwbnlLSkGuTTrQngWDLBmUDR8o0fekpjmALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiTlrPVn",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAxpEBDU5LWC41LhvrV0tiuV9zxv+Xw0AaKtsbOW7WO6f1qcZBZbZpuq13rYwJ5jPOPHqNWdWahc792+y+jKGGCbhA8Hh3RxnOY5S1mg3gPOMKvn63AMXy0tVpPItSmeRPnKhD82cvtPKBwbnlLSkGuTTrQngWDLBmUDR8o0fekpjmALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiTlrPVn",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAxpEBDU5LWC41LhvrV0tiuV9zxv+Xw0AaKtsbOW7WO6f1qcZBZbZpuq13rYwJ5jPOPHqNWdWahc792+y+jKGGCbhA8Hh3RxnOY5S1mg3gPOMKvn63AMXy0tVpPItSmeRPnKhD82cvtPKBwbnlLSkGuTTrQngWDLBmUDR8o0fekpjmALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiTlrPVn",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
  "id": -576460752303422976,
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
  "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
  "id": -576460752303422976,
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "state": "tx_+QENCwH4hLhAxpEBDU5LWC41LhvrV0tiuV9zxv+Xw0AaKtsbOW7WO6f1qcZBZbZpuq13rYwJ5jPOPHqNWdWahc792+y+jKGGCbhA8Hh3RxnOY5S1mg3gPOMKvn63AMXy0tVpPItSmeRPnKhD82cvtPKBwbnlLSkGuTTrQngWDLBmUDR8o0fekpjmALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiTlrPVn"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "state": "tx_+QENCwH4hLhAxpEBDU5LWC41LhvrV0tiuV9zxv+Xw0AaKtsbOW7WO6f1qcZBZbZpuq13rYwJ5jPOPHqNWdWahc792+y+jKGGCbhA8Hh3RxnOY5S1mg3gPOMKvn63AMXy0tVpPItSmeRPnKhD82cvtPKBwbnlLSkGuTTrQngWDLBmUDR8o0fekpjmALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiTlrPVn"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBnYTfXlEs+mFtcIFlgSMkrXsfPh24fYbmUnLcZBUTRzgoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhnBIhhsPP6BgzS0CqtQKtAo1G6fKHkdbhC2dBK+zYEZlRDToWhimlwIl4oVfkQ==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422975,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAQADiRKCskm3ujQSP6cUHA5pDYfP8ip5j/Q8Dw9o4/zdbFOqhjOHLO3DGOE3pEfgRq7Y2ergZPCZ6FI9A8E9UPuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCJUgIqRU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
  "id": -576460752303422975,
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAQADiRKCskm3ujQSP6cUHA5pDYfP8ip5j/Q8Dw9o4/zdbFOqhjOHLO3DGOE3pEfgRq7Y2ergZPCZ6FI9A8E9UPuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCJUgIqRU=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422974,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAQADiRKCskm3ujQSP6cUHA5pDYfP8ip5j/Q8Dw9o4/zdbFOqhjOHLO3DGOE3pEfgRq7Y2ergZPCZ6FI9A8E9UPuEAcn3OtVlv76tBRvMEKHHonrJtnTp5GQofEcCsQyaUEMwKf5Qv7kXPlPAOtFsw4UgVefo/Ct/6pozaiEaENIfAHuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCJe90Zhg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
  "id": -576460752303422974,
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAQADiRKCskm3ujQSP6cUHA5pDYfP8ip5j/Q8Dw9o4/zdbFOqhjOHLO3DGOE3pEfgRq7Y2ergZPCZ6FI9A8E9UPuEAcn3OtVlv76tBRvMEKHHonrJtnTp5GQofEcCsQyaUEMwKf5Qv7kXPlPAOtFsw4UgVefo/Ct/6pozaiEaENIfAHuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCJe90Zhg=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAQADiRKCskm3ujQSP6cUHA5pDYfP8ip5j/Q8Dw9o4/zdbFOqhjOHLO3DGOE3pEfgRq7Y2ergZPCZ6FI9A8E9UPuEAcn3OtVlv76tBRvMEKHHonrJtnTp5GQofEcCsQyaUEMwKf5Qv7kXPlPAOtFsw4UgVefo/Ct/6pozaiEaENIfAHuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCJe90Zhg=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello back",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAQADiRKCskm3ujQSP6cUHA5pDYfP8ip5j/Q8Dw9o4/zdbFOqhjOHLO3DGOE3pEfgRq7Y2ergZPCZ6FI9A8E9UPuEAcn3OtVlv76tBRvMEKHHonrJtnTp5GQofEcCsQyaUEMwKf5Qv7kXPlPAOtFsw4UgVefo/Ct/6pozaiEaENIfAHuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCJe90Zhg=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAQADiRKCskm3ujQSP6cUHA5pDYfP8ip5j/Q8Dw9o4/zdbFOqhjOHLO3DGOE3pEfgRq7Y2ergZPCZ6FI9A8E9UPuEAcn3OtVlv76tBRvMEKHHonrJtnTp5GQofEcCsQyaUEMwKf5Qv7kXPlPAOtFsw4UgVefo/Ct/6pozaiEaENIfAHuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCJe90Zhg=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "state": "tx_+P4LAfiEuEAQADiRKCskm3ujQSP6cUHA5pDYfP8ip5j/Q8Dw9o4/zdbFOqhjOHLO3DGOE3pEfgRq7Y2ergZPCZ6FI9A8E9UPuEAcn3OtVlv76tBRvMEKHHonrJtnTp5GQofEcCsQyaUEMwKf5Qv7kXPlPAOtFsw4UgVefo/Ct/6pozaiEaENIfAHuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCJe90Zhg="
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "state": "tx_+P4LAfiEuEAQADiRKCskm3ujQSP6cUHA5pDYfP8ip5j/Q8Dw9o4/zdbFOqhjOHLO3DGOE3pEfgRq7Y2ergZPCZ6FI9A8E9UPuEAcn3OtVlv76tBRvMEKHHonrJtnTp5GQofEcCsQyaUEMwKf5Qv7kXPlPAOtFsw4UgVefo/Ct/6pozaiEaENIfAHuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCJe90Zhg="
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
    "info": "Hello",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello back",
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
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
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
  "method": "channels.message",
  "params": {
    "info": "Hello",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello back",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBnYTfXlEs+mFtcIFlgSMkrXsfPh24fYbmUnLcZBUTRzgoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWvwIAhnBIhhsPP6CX2TeUqz6zdLD4rv7B8yXdbk6T+ffdhvHoEl5GooaacAMO7XhenA==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422973,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDz5Gt9tROb3v2t1BOuZBkE9wIGobZZLRXLC6EDUUGo0uWdMjwFfWxu4UL5HfhOrGEDISqAJc04BffRvvWfgA4PuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gl9k3lKs+s3Sw+K7+wfMl3W5Ok/n33Ybx6BJeRqKGmnADDncfO2w="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
  "id": -576460752303422973,
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDz5Gt9tROb3v2t1BOuZBkE9wIGobZZLRXLC6EDUUGo0uWdMjwFfWxu4UL5HfhOrGEDISqAJc04BffRvvWfgA4PuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gl9k3lKs+s3Sw+K7+wfMl3W5Ok/n33Ybx6BJeRqKGmnADDncfO2w=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422972,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECIOqRzQnTPTzeHBxTzlZ2fyOJwYsJnaWLnKNO6fuR3Vr5sWFNo5O0k6sIvOjUixwatUgJkj0FQVf97GR3zqpwHuEDz5Gt9tROb3v2t1BOuZBkE9wIGobZZLRXLC6EDUUGo0uWdMjwFfWxu4UL5HfhOrGEDISqAJc04BffRvvWfgA4PuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gl9k3lKs+s3Sw+K7+wfMl3W5Ok/n33Ybx6BJeRqKGmnADDp4HiCE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
  "id": -576460752303422972,
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECIOqRzQnTPTzeHBxTzlZ2fyOJwYsJnaWLnKNO6fuR3Vr5sWFNo5O0k6sIvOjUixwatUgJkj0FQVf97GR3zqpwHuEDz5Gt9tROb3v2t1BOuZBkE9wIGobZZLRXLC6EDUUGo0uWdMjwFfWxu4UL5HfhOrGEDISqAJc04BffRvvWfgA4PuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gl9k3lKs+s3Sw+K7+wfMl3W5Ok/n33Ybx6BJeRqKGmnADDp4HiCE=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECIOqRzQnTPTzeHBxTzlZ2fyOJwYsJnaWLnKNO6fuR3Vr5sWFNo5O0k6sIvOjUixwatUgJkj0FQVf97GR3zqpwHuEDz5Gt9tROb3v2t1BOuZBkE9wIGobZZLRXLC6EDUUGo0uWdMjwFfWxu4UL5HfhOrGEDISqAJc04BffRvvWfgA4PuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gl9k3lKs+s3Sw+K7+wfMl3W5Ok/n33Ybx6BJeRqKGmnADDp4HiCE=",
      "type": "channel_withdraw_tx"
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
    "info": "Hello",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "message": {
        "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello back",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
      }
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECIOqRzQnTPTzeHBxTzlZ2fyOJwYsJnaWLnKNO6fuR3Vr5sWFNo5O0k6sIvOjUixwatUgJkj0FQVf97GR3zqpwHuEDz5Gt9tROb3v2t1BOuZBkE9wIGobZZLRXLC6EDUUGo0uWdMjwFfWxu4UL5HfhOrGEDISqAJc04BffRvvWfgA4PuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gl9k3lKs+s3Sw+K7+wfMl3W5Ok/n33Ybx6BJeRqKGmnADDp4HiCE=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECIOqRzQnTPTzeHBxTzlZ2fyOJwYsJnaWLnKNO6fuR3Vr5sWFNo5O0k6sIvOjUixwatUgJkj0FQVf97GR3zqpwHuEDz5Gt9tROb3v2t1BOuZBkE9wIGobZZLRXLC6EDUUGo0uWdMjwFfWxu4UL5HfhOrGEDISqAJc04BffRvvWfgA4PuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gl9k3lKs+s3Sw+K7+wfMl3W5Ok/n33Ybx6BJeRqKGmnADDp4HiCE=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "state": "tx_+P4LAfiEuECIOqRzQnTPTzeHBxTzlZ2fyOJwYsJnaWLnKNO6fuR3Vr5sWFNo5O0k6sIvOjUixwatUgJkj0FQVf97GR3zqpwHuEDz5Gt9tROb3v2t1BOuZBkE9wIGobZZLRXLC6EDUUGo0uWdMjwFfWxu4UL5HfhOrGEDISqAJc04BffRvvWfgA4PuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gl9k3lKs+s3Sw+K7+wfMl3W5Ok/n33Ybx6BJeRqKGmnADDp4HiCE="
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "state": "tx_+P4LAfiEuECIOqRzQnTPTzeHBxTzlZ2fyOJwYsJnaWLnKNO6fuR3Vr5sWFNo5O0k6sIvOjUixwatUgJkj0FQVf97GR3zqpwHuEDz5Gt9tROb3v2t1BOuZBkE9wIGobZZLRXLC6EDUUGo0uWdMjwFfWxu4UL5HfhOrGEDISqAJc04BffRvvWfgA4PuHT4cjQBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gl9k3lKs+s3Sw+K7+wfMl3W5Ok/n33Ybx6BJeRqKGmnADDp4HiCE="
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBnYTfXlEs+mFtcIFlgSMkrXsfPh24fYbmUnLcZBUTRzgoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY2kdavv/2GG0jrV9//AIYSMJzlQAAmRzdeJg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422971,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECep+yNTJhb0MhJ5tRu+k2ieYM2QfkcCKbX3CYQSjxehA1eAZdJc3OSq2U5QpvLtPoe1HVnMnoROpUs4980YgIKuF/4XTUBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/9hhtI61ff/wCGEjCc5UAAJnoKBR8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
  "id": -576460752303422971,
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECep+yNTJhb0MhJ5tRu+k2ieYM2QfkcCKbX3CYQSjxehA1eAZdJc3OSq2U5QpvLtPoe1HVnMnoROpUs4980YgIKuF/4XTUBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/9hhtI61ff/wCGEjCc5UAAJnoKBR8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422970,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuECep+yNTJhb0MhJ5tRu+k2ieYM2QfkcCKbX3CYQSjxehA1eAZdJc3OSq2U5QpvLtPoe1HVnMnoROpUs4980YgIKuEC30DEmr1Wz1lDJlZLm9WAfuQevuE1Y0RsZuSZf3H15K9ztfF7hDetIQP7KaH71TT9Kb1/PB+mVs/N9JGFIYtUGuF/4XTUBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/9hhtI61ff/wCGEjCc5UAAJgigJzA="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
  "id": -576460752303422970,
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECep+yNTJhb0MhJ5tRu+k2ieYM2QfkcCKbX3CYQSjxehA1eAZdJc3OSq2U5QpvLtPoe1HVnMnoROpUs4980YgIKuEC30DEmr1Wz1lDJlZLm9WAfuQevuE1Y0RsZuSZf3H15K9ztfF7hDetIQP7KaH71TT9Kb1/PB+mVs/N9JGFIYtUGuF/4XTUBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/9hhtI61ff/wCGEjCc5UAAJgigJzA=",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECep+yNTJhb0MhJ5tRu+k2ieYM2QfkcCKbX3CYQSjxehA1eAZdJc3OSq2U5QpvLtPoe1HVnMnoROpUs4980YgIKuEC30DEmr1Wz1lDJlZLm9WAfuQevuE1Y0RsZuSZf3H15K9ztfF7hDetIQP7KaH71TT9Kb1/PB+mVs/N9JGFIYtUGuF/4XTUBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/9hhtI61ff/wCGEjCc5UAAJgigJzA=",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECep+yNTJhb0MhJ5tRu+k2ieYM2QfkcCKbX3CYQSjxehA1eAZdJc3OSq2U5QpvLtPoe1HVnMnoROpUs4980YgIKuEC30DEmr1Wz1lDJlZLm9WAfuQevuE1Y0RsZuSZf3H15K9ztfF7hDetIQP7KaH71TT9Kb1/PB+mVs/N9JGFIYtUGuF/4XTUBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/9hhtI61ff/wCGEjCc5UAAJgigJzA=",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECep+yNTJhb0MhJ5tRu+k2ieYM2QfkcCKbX3CYQSjxehA1eAZdJc3OSq2U5QpvLtPoe1HVnMnoROpUs4980YgIKuEC30DEmr1Wz1lDJlZLm9WAfuQevuE1Y0RsZuSZf3H15K9ztfF7hDetIQP7KaH71TT9Kb1/PB+mVs/N9JGFIYtUGuF/4XTUBoQZ2E315RLPphbXCBZYEjJK17Hz4duH2G5lJy3GQVE0c4KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/9hhtI61ff/wCGEjCc5UAAJgigJzA=",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
    "channel_id": "ch_u16b8DaxcEUJi8iFVuQvLM4Z5R7hknQWxz475GN2RyDGAFSHd",
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
