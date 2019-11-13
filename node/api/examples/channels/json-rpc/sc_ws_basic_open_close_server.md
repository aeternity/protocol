
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
      "fsm_id": "ba_nzXbJHYVhJ3Hrxzs4KAiTJAeX1X3oRFq6v4cXx/GEOGTJPEM"
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
      "fsm_id": "ba_WU95FWusLqN5tXAGwEzwFaLLeylPegq+JQAxXtOJKSyUb8kM"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYE8Gi0JQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423426,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBLo74fODrqViKCgjqjGJchyguNALdLxCGrnypQkUevWuFWo4JdskEqw8YC4iJkhiG/ajXHIVfw/QWqiurk4p8NuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2BFAUHhE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423426,
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
      "signed_tx": "tx_+MsLAfhCuEBLo74fODrqViKCgjqjGJchyguNALdLxCGrnypQkUevWuFWo4JdskEqw8YC4iJkhiG/ajXHIVfw/QWqiurk4p8NuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2BFAUHhE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423425,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAS6O+Hzg66lYigoI6oxiXIcoLjQC3S8Qhq58qUJFHr1rhVqOCXbJBKsPGAuIiZIYhv2o1xyFX8P0Fqorq5OKfDbhApYGpu4tByCz6OS8PU2DDIvytIz3y5zFCCsPwwQLgZcYHELirPhuR3lgkveO7xYtxw4LbQ3toBhcNYsjlz3bxCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgSl841G"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423425,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAS6O+Hzg66lYigoI6oxiXIcoLjQC3S8Qhq58qUJFHr1rhVqOCXbJBKsPGAuIiZIYhv2o1xyFX8P0Fqorq5OKfDbhApYGpu4tByCz6OS8PU2DDIvytIz3y5zFCCsPwwQLgZcYHELirPhuR3lgkveO7xYtxw4LbQ3toBhcNYsjlz3bxCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgSl841G",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAS6O+Hzg66lYigoI6oxiXIcoLjQC3S8Qhq58qUJFHr1rhVqOCXbJBKsPGAuIiZIYhv2o1xyFX8P0Fqorq5OKfDbhApYGpu4tByCz6OS8PU2DDIvytIz3y5zFCCsPwwQLgZcYHELirPhuR3lgkveO7xYtxw4LbQ3toBhcNYsjlz3bxCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgSl841G",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAS6O+Hzg66lYigoI6oxiXIcoLjQC3S8Qhq58qUJFHr1rhVqOCXbJBKsPGAuIiZIYhv2o1xyFX8P0Fqorq5OKfDbhApYGpu4tByCz6OS8PU2DDIvytIz3y5zFCCsPwwQLgZcYHELirPhuR3lgkveO7xYtxw4LbQ3toBhcNYsjlz3bxCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgSl841G",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAS6O+Hzg66lYigoI6oxiXIcoLjQC3S8Qhq58qUJFHr1rhVqOCXbJBKsPGAuIiZIYhv2o1xyFX8P0Fqorq5OKfDbhApYGpu4tByCz6OS8PU2DDIvytIz3y5zFCCsPwwQLgZcYHELirPhuR3lgkveO7xYtxw4LbQ3toBhcNYsjlz3bxCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgSl841G",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "message": {
        "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "message": {
        "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "id": -576460752303423424,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423424,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+QENCwH4hLhAS6O+Hzg66lYigoI6oxiXIcoLjQC3S8Qhq58qUJFHr1rhVqOCXbJBKsPGAuIiZIYhv2o1xyFX8P0Fqorq5OKfDbhApYGpu4tByCz6OS8PU2DDIvytIz3y5zFCCsPwwQLgZcYHELirPhuR3lgkveO7xYtxw4LbQ3toBhcNYsjlz3bxCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgSl841G"
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+QENCwH4hLhAS6O+Hzg66lYigoI6oxiXIcoLjQC3S8Qhq58qUJFHr1rhVqOCXbJBKsPGAuIiZIYhv2o1xyFX8P0Fqorq5OKfDbhApYGpu4tByCz6OS8PU2DDIvytIz3y5zFCCsPwwQLgZcYHELirPhuR3lgkveO7xYtxw4LbQ3toBhcNYsjlz3bxCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgSl841G"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423423,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423423,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkHVq7RM7EF4MjWvHthq1+fb9Hr8dnxNjdewh8sSMobpAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt3S8cV8=",
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
  "id": -576460752303423422,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA8vkvpZTQgmyQZoxSws+xfkdHQMgPZghwj6Vxt96o+EGcTBWLCbEu0zxiGukGnVpjcC1R6tV+SmeW1fO7gykQMuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dSr6Jd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423422,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA8vkvpZTQgmyQZoxSws+xfkdHQMgPZghwj6Vxt96o+EGcTBWLCbEu0zxiGukGnVpjcC1R6tV+SmeW1fO7gykQMuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dSr6Jd",
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
  "id": -576460752303423421,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA8vkvpZTQgmyQZoxSws+xfkdHQMgPZghwj6Vxt96o+EGcTBWLCbEu0zxiGukGnVpjcC1R6tV+SmeW1fO7gykQMuEDBxdf85c/sSBS0PvLFY9m1n5g3xR0fE9esjGzfCLkHDQsm2CKEPZUUZQ+w76NAwpy5fjv2hJLf41utWszDq7oIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7f+Lekc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423421,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEA8vkvpZTQgmyQZoxSws+xfkdHQMgPZghwj6Vxt96o+EGcTBWLCbEu0zxiGukGnVpjcC1R6tV+SmeW1fO7gykQMuEDBxdf85c/sSBS0PvLFY9m1n5g3xR0fE9esjGzfCLkHDQsm2CKEPZUUZQ+w76NAwpy5fjv2hJLf41utWszDq7oIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7f+Lekc"
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEA8vkvpZTQgmyQZoxSws+xfkdHQMgPZghwj6Vxt96o+EGcTBWLCbEu0zxiGukGnVpjcC1R6tV+SmeW1fO7gykQMuEDBxdf85c/sSBS0PvLFY9m1n5g3xR0fE9esjGzfCLkHDQsm2CKEPZUUZQ+w76NAwpy5fjv2hJLf41utWszDq7oIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7f+Lekc"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423420,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423420,
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
  "id": -576460752303423419,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423419,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA8vkvpZTQgmyQZoxSws+xfkdHQMgPZghwj6Vxt96o+EGcTBWLCbEu0zxiGukGnVpjcC1R6tV+SmeW1fO7gykQMuEDBxdf85c/sSBS0PvLFY9m1n5g3xR0fE9esjGzfCLkHDQsm2CKEPZUUZQ+w76NAwpy5fjv2hJLf41utWszDq7oIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7f+Lekc",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423418,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423418,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkHVq7RM7EF4MjWvHthq1+fb9Hr8dnxNjdewh8sSMobpA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgsRG+E=",
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
  "id": -576460752303423417,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBRLcqWbubWER2bEmo8Ez6AMQlSuTLx7GZ1piNjRtR0X9brt0W3Kx//YP044xmSeM8yIx+cPpr+fdu2e0sAymMOuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbMHyqR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423417,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBRLcqWbubWER2bEmo8Ez6AMQlSuTLx7GZ1piNjRtR0X9brt0W3Kx//YP044xmSeM8yIx+cPpr+fdu2e0sAymMOuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbMHyqR",
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
  "id": -576460752303423416,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEADJ++LQsbycYUYjUVwzHKUdu3a5Xx57Y20eQJ2xJYHZP4WV47L0vEzPa+2Z52oTEwAJYBww44IcdEuPse4pYsBuEBRLcqWbubWER2bEmo8Ez6AMQlSuTLx7GZ1piNjRtR0X9brt0W3Kx//YP044xmSeM8yIx+cPpr+fdu2e0sAymMOuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZ6husb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423416,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEADJ++LQsbycYUYjUVwzHKUdu3a5Xx57Y20eQJ2xJYHZP4WV47L0vEzPa+2Z52oTEwAJYBww44IcdEuPse4pYsBuEBRLcqWbubWER2bEmo8Ez6AMQlSuTLx7GZ1piNjRtR0X9brt0W3Kx//YP044xmSeM8yIx+cPpr+fdu2e0sAymMOuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZ6husb"
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEADJ++LQsbycYUYjUVwzHKUdu3a5Xx57Y20eQJ2xJYHZP4WV47L0vEzPa+2Z52oTEwAJYBww44IcdEuPse4pYsBuEBRLcqWbubWER2bEmo8Ez6AMQlSuTLx7GZ1piNjRtR0X9brt0W3Kx//YP044xmSeM8yIx+cPpr+fdu2e0sAymMOuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZ6husb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423415,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423415,
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
  "id": -576460752303423414,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423414,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEADJ++LQsbycYUYjUVwzHKUdu3a5Xx57Y20eQJ2xJYHZP4WV47L0vEzPa+2Z52oTEwAJYBww44IcdEuPse4pYsBuEBRLcqWbubWER2bEmo8Ez6AMQlSuTLx7GZ1piNjRtR0X9brt0W3Kx//YP044xmSeM8yIx+cPpr+fdu2e0sAymMOuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZ6husb",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423413,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423413,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkHVq7RM7EF4MjWvHthq1+fb9Hr8dnxNjdewh8sSMobpBKBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAsoPLcE=",
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
  "id": -576460752303423412,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA12V5O13TcqvRvQppL6srff6QvypwbWZMph9bZEZPuBFlxJZ2n0ht7E1zkJxa5knEiRW9q1BcaCSkP3y1l3H0MuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKtpBEo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423412,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA12V5O13TcqvRvQppL6srff6QvypwbWZMph9bZEZPuBFlxJZ2n0ht7E1zkJxa5knEiRW9q1BcaCSkP3y1l3H0MuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKtpBEo",
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
  "id": -576460752303423411,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA12V5O13TcqvRvQppL6srff6QvypwbWZMph9bZEZPuBFlxJZ2n0ht7E1zkJxa5knEiRW9q1BcaCSkP3y1l3H0MuEDkphvRZvb+ULPLkv6y8x7LXqazT2kDzucIZgDG4uMCZWBgJmMaRF3Q5me/YwHWgaPFjAwI8YhfXJyBIssSW6MNuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALBL0o9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423411,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEA12V5O13TcqvRvQppL6srff6QvypwbWZMph9bZEZPuBFlxJZ2n0ht7E1zkJxa5knEiRW9q1BcaCSkP3y1l3H0MuEDkphvRZvb+ULPLkv6y8x7LXqazT2kDzucIZgDG4uMCZWBgJmMaRF3Q5me/YwHWgaPFjAwI8YhfXJyBIssSW6MNuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALBL0o9"
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEA12V5O13TcqvRvQppL6srff6QvypwbWZMph9bZEZPuBFlxJZ2n0ht7E1zkJxa5knEiRW9q1BcaCSkP3y1l3H0MuEDkphvRZvb+ULPLkv6y8x7LXqazT2kDzucIZgDG4uMCZWBgJmMaRF3Q5me/YwHWgaPFjAwI8YhfXJyBIssSW6MNuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALBL0o9"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423410,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423410,
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
  "id": -576460752303423409,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423409,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA12V5O13TcqvRvQppL6srff6QvypwbWZMph9bZEZPuBFlxJZ2n0ht7E1zkJxa5knEiRW9q1BcaCSkP3y1l3H0MuEDkphvRZvb+ULPLkv6y8x7LXqazT2kDzucIZgDG4uMCZWBgJmMaRF3Q5me/YwHWgaPFjAwI8YhfXJyBIssSW6MNuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALBL0o9",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423408,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423408,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkHVq7RM7EF4MjWvHthq1+fb9Hr8dnxNjdewh8sSMobpBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdq4rniM=",
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
  "id": -576460752303423407,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB0rlZZrvWs0iN6YwXnevR47lL9PdXUtHDFEGnjNSRzRTWN5pFY6H8uPXMWpvPla1UlHr1BBG5kHDoyzO8MDrkIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZxuTqm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423407,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB0rlZZrvWs0iN6YwXnevR47lL9PdXUtHDFEGnjNSRzRTWN5pFY6H8uPXMWpvPla1UlHr1BBG5kHDoyzO8MDrkIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZxuTqm",
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
  "id": -576460752303423406,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB0rlZZrvWs0iN6YwXnevR47lL9PdXUtHDFEGnjNSRzRTWN5pFY6H8uPXMWpvPla1UlHr1BBG5kHDoyzO8MDrkIuEDcJguhPNjddMQzpARQn+bOG0xsXjVlOjef1mTOKZ0WhUYJ5fmMQwW+2fB9V1tRXybyqeFhcHiWYU0PlQ2kgWgIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnattPIh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423406,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEB0rlZZrvWs0iN6YwXnevR47lL9PdXUtHDFEGnjNSRzRTWN5pFY6H8uPXMWpvPla1UlHr1BBG5kHDoyzO8MDrkIuEDcJguhPNjddMQzpARQn+bOG0xsXjVlOjef1mTOKZ0WhUYJ5fmMQwW+2fB9V1tRXybyqeFhcHiWYU0PlQ2kgWgIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnattPIh"
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEB0rlZZrvWs0iN6YwXnevR47lL9PdXUtHDFEGnjNSRzRTWN5pFY6H8uPXMWpvPla1UlHr1BBG5kHDoyzO8MDrkIuEDcJguhPNjddMQzpARQn+bOG0xsXjVlOjef1mTOKZ0WhUYJ5fmMQwW+2fB9V1tRXybyqeFhcHiWYU0PlQ2kgWgIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnattPIh"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423405,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423405,
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
  "id": -576460752303423404,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423404,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB0rlZZrvWs0iN6YwXnevR47lL9PdXUtHDFEGnjNSRzRTWN5pFY6H8uPXMWpvPla1UlHr1BBG5kHDoyzO8MDrkIuEDcJguhPNjddMQzpARQn+bOG0xsXjVlOjef1mTOKZ0WhUYJ5fmMQwW+2fB9V1tRXybyqeFhcHiWYU0PlQ2kgWgIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnattPIh",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423403,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423403,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkHVq7RM7EF4MjWvHthq1+fb9Hr8dnxNjdewh8sSMobpBqBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUApsJrtk=",
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
  "id": -576460752303423402,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDQnaVO6lo+tByzlwxjEEwqFyX9obya6Jwzdq1Aq7QtoU/nunl2JQeiYbTk73JFFsQFhCFFwoz+JInrGMtUxrAIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALup1TB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423402,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDQnaVO6lo+tByzlwxjEEwqFyX9obya6Jwzdq1Aq7QtoU/nunl2JQeiYbTk73JFFsQFhCFFwoz+JInrGMtUxrAIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALup1TB",
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
  "id": -576460752303423401,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEByaZ2f0l1NPCDDXaSbn5WZjujrwO3jE+ZKFIMOlljE2vdvPHQ5Xr4s7QyNAzgO8jCyrYJ7GAjNTgvvhiZp7ygEuEDQnaVO6lo+tByzlwxjEEwqFyX9obya6Jwzdq1Aq7QtoU/nunl2JQeiYbTk73JFFsQFhCFFwoz+JInrGMtUxrAIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKn4CtF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423401,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEByaZ2f0l1NPCDDXaSbn5WZjujrwO3jE+ZKFIMOlljE2vdvPHQ5Xr4s7QyNAzgO8jCyrYJ7GAjNTgvvhiZp7ygEuEDQnaVO6lo+tByzlwxjEEwqFyX9obya6Jwzdq1Aq7QtoU/nunl2JQeiYbTk73JFFsQFhCFFwoz+JInrGMtUxrAIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKn4CtF"
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
    "data": {
      "state": "tx_+NILAfiEuEByaZ2f0l1NPCDDXaSbn5WZjujrwO3jE+ZKFIMOlljE2vdvPHQ5Xr4s7QyNAzgO8jCyrYJ7GAjNTgvvhiZp7ygEuEDQnaVO6lo+tByzlwxjEEwqFyX9obya6Jwzdq1Aq7QtoU/nunl2JQeiYbTk73JFFsQFhCFFwoz+JInrGMtUxrAIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKn4CtF"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423400,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423400,
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
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEByaZ2f0l1NPCDDXaSbn5WZjujrwO3jE+ZKFIMOlljE2vdvPHQ5Xr4s7QyNAzgO8jCyrYJ7GAjNTgvvhiZp7ygEuEDQnaVO6lo+tByzlwxjEEwqFyX9obya6Jwzdq1Aq7QtoU/nunl2JQeiYbTk73JFFsQFhCFFwoz+JInrGMtUxrAIuEj4RjkCoQZB1au0TOxBeDI1rx7Yatfn2/R6/HZ8TY3XsIfLEjKG6QagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKn4CtF",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423398,
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423398,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423397,
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
    "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
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
  "channel_id": "ch_Vzf9rzBTxzxRmqFYE5GoqDKvnq1ftSro57J9Madic2cHqZ7Wt",
  "id": -576460752303423397,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
