
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
      "fsm_id": "ba_nA/FVGUYCoxglu+bswaPN4jkoSgOX1X9RKCp8CF3f2xjqZ41"
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
      "fsm_id": "ba_4O33GBFZ1ID8+bCiJvJoHQqfwwnXenh8OxSnO/A+Iim/VzVJ"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY7rQJwFA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422883,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDmtxY+KzLQaInTtQJF/pX3x5Ir5+MpH2TytuF/512QLT4I3G3XAC9rkWyufvvE7F5ga2X4NdPdOxg9WxV1F/IJuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2O7DX+2s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422883,
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
      "signed_tx": "tx_+MsLAfhCuEDmtxY+KzLQaInTtQJF/pX3x5Ir5+MpH2TytuF/512QLT4I3G3XAC9rkWyufvvE7F5ga2X4NdPdOxg9WxV1F/IJuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2O7DX+2s=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422882,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhA2EKqo3GGvV5muXY7rf0lvxCQQWu8iNA+XibT4JSi84KOnuBpwYT47dAmNokpsbmAUfFvuxzli4fuLCalq3sRCLhA5rcWPisy0GiJ07UCRf6V98eSK+fjKR9k8rbhf+ddkC0+CNxt1wAva5Fsrn77xOxeYGtl+DXT3TsYPVsVdRfyCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjuBa+sk"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422882,
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhA2EKqo3GGvV5muXY7rf0lvxCQQWu8iNA+XibT4JSi84KOnuBpwYT47dAmNokpsbmAUfFvuxzli4fuLCalq3sRCLhA5rcWPisy0GiJ07UCRf6V98eSK+fjKR9k8rbhf+ddkC0+CNxt1wAva5Fsrn77xOxeYGtl+DXT3TsYPVsVdRfyCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjuBa+sk",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhA2EKqo3GGvV5muXY7rf0lvxCQQWu8iNA+XibT4JSi84KOnuBpwYT47dAmNokpsbmAUfFvuxzli4fuLCalq3sRCLhA5rcWPisy0GiJ07UCRf6V98eSK+fjKR9k8rbhf+ddkC0+CNxt1wAva5Fsrn77xOxeYGtl+DXT3TsYPVsVdRfyCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjuBa+sk",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA2EKqo3GGvV5muXY7rf0lvxCQQWu8iNA+XibT4JSi84KOnuBpwYT47dAmNokpsbmAUfFvuxzli4fuLCalq3sRCLhA5rcWPisy0GiJ07UCRf6V98eSK+fjKR9k8rbhf+ddkC0+CNxt1wAva5Fsrn77xOxeYGtl+DXT3TsYPVsVdRfyCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjuBa+sk",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA2EKqo3GGvV5muXY7rf0lvxCQQWu8iNA+XibT4JSi84KOnuBpwYT47dAmNokpsbmAUfFvuxzli4fuLCalq3sRCLhA5rcWPisy0GiJ07UCRf6V98eSK+fjKR9k8rbhf+ddkC0+CNxt1wAva5Fsrn77xOxeYGtl+DXT3TsYPVsVdRfyCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjuBa+sk",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "message": {
        "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "message": {
        "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
  "id": -576460752303422881,
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
  "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
  "id": -576460752303422881,
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "state": "tx_+QENCwH4hLhA2EKqo3GGvV5muXY7rf0lvxCQQWu8iNA+XibT4JSi84KOnuBpwYT47dAmNokpsbmAUfFvuxzli4fuLCalq3sRCLhA5rcWPisy0GiJ07UCRf6V98eSK+fjKR9k8rbhf+ddkC0+CNxt1wAva5Fsrn77xOxeYGtl+DXT3TsYPVsVdRfyCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjuBa+sk"
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "state": "tx_+QENCwH4hLhA2EKqo3GGvV5muXY7rf0lvxCQQWu8iNA+XibT4JSi84KOnuBpwYT47dAmNokpsbmAUfFvuxzli4fuLCalq3sRCLhA5rcWPisy0GiJ07UCRf6V98eSK+fjKR9k8rbhf+ddkC0+CNxt1wAva5Fsrn77xOxeYGtl+DXT3TsYPVsVdRfyCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjuBa+sk"
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
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBrXgGj7tu+FU697Nja+Ri3MGdjYUYQworyy1cRrs5JjwoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhg/AoHKQAKBgzS0CqtQKtAo1G6fKHkdbhC2dBK+zYEZlRDToWhimlwI8Jlsenw==",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBrXgGj7tu+FU697Nja+Ri3MGdjYUYQworyy1cRrs5JjwoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWvwIAhg/AoHKQAKBPOCB5BWN+vvRjkbB9heHfLcWKwwj0q//CGyZQWiojggIX9cobBw==",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBrXgGj7tu+FU697Nja+Ri3MGdjYUYQworyy1cRrs5JjwoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhg/AoHKQAKBgzS0CqtQKtAo1G6fKHkdbhC2dBK+zYEZlRDToWhimlwI8Jlsenw==",
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
  "id": -576460752303422880,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBn4MjQk64RaLyhSZD91gJo7JYQjMGHXoGbUvX7EfOOZMJ+G4z79MAnWYumoPF7KSA7rA4b+vN08fOEd79v5XMOuHT4cjQBoQa14Bo+7bvhVOvezY2vkYtzBnY2FGEMKK8stXEa7OSY8KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCPDXsOxY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
  "id": -576460752303422880,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
      "method": "channels.withdraw_tx",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBn4MjQk64RaLyhSZD91gJo7JYQjMGHXoGbUvX7EfOOZMJ+G4z79MAnWYumoPF7KSA7rA4b+vN08fOEd79v5XMOuHT4cjQBoQa14Bo+7bvhVOvezY2vkYtzBnY2FGEMKK8stXEa7OSY8KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgYM0tAqrUCrQKNRunyh5HW4QtnQSvs2BGZUQ06FoYppcCPDXsOxY=",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
    "data": {
      "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
  "id": -576460752303422879,
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
  "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
  "id": -576460752303422879,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422878,
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
    "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
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
  "channel_id": "ch_2P6mFjyL1dQaDNJLTw7zPZ7HfsNoUmruHPJvnmbp7GcmTjz2fj",
  "id": -576460752303422878,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
