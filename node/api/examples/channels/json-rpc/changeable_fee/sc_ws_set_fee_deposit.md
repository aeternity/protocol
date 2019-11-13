
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
      "fsm_id": "ba_hXn8QdhycNERnobWcN2TEf/sLnaZVUZ4KQwNxiDRDeNZm3+Z"
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
      "fsm_id": "ba_gCC+5t4ZOFK5xsbwU/fyPJnjMOgQp286/qXuQFyAGscy2/4Q"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYhOfqE6g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422987,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAAUDXb/0Hc7PAT7qN+1GBjzaj6Cp3pHlUrYJ2IB/1kTsXVCz6+lyy0OOjf3c7rMbgDBFsrHvjx3p1IjNj2cgoBuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2IU+tgn8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422987,
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
      "signed_tx": "tx_+MsLAfhCuEAAUDXb/0Hc7PAT7qN+1GBjzaj6Cp3pHlUrYJ2IB/1kTsXVCz6+lyy0OOjf3c7rMbgDBFsrHvjx3p1IjNj2cgoBuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2IU+tgn8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422986,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAAFA12/9B3OzwE+6jftRgY82o+gqd6R5VK2CdiAf9ZE7F1Qs+vpcstDjo393O6zG4AwRbKx748d6dSIzY9nIKAbhA57V9hKuQfuRuikJOZZnWygzlmDRPsLBVfg/fhluzUl7ECeTACaB/NnawX9T4/ujUZVrDanDzwBaI8eGRatRaA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiHhlTAP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422986,
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAAFA12/9B3OzwE+6jftRgY82o+gqd6R5VK2CdiAf9ZE7F1Qs+vpcstDjo393O6zG4AwRbKx748d6dSIzY9nIKAbhA57V9hKuQfuRuikJOZZnWygzlmDRPsLBVfg/fhluzUl7ECeTACaB/NnawX9T4/ujUZVrDanDzwBaI8eGRatRaA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiHhlTAP",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAAFA12/9B3OzwE+6jftRgY82o+gqd6R5VK2CdiAf9ZE7F1Qs+vpcstDjo393O6zG4AwRbKx748d6dSIzY9nIKAbhA57V9hKuQfuRuikJOZZnWygzlmDRPsLBVfg/fhluzUl7ECeTACaB/NnawX9T4/ujUZVrDanDzwBaI8eGRatRaA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiHhlTAP",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAAFA12/9B3OzwE+6jftRgY82o+gqd6R5VK2CdiAf9ZE7F1Qs+vpcstDjo393O6zG4AwRbKx748d6dSIzY9nIKAbhA57V9hKuQfuRuikJOZZnWygzlmDRPsLBVfg/fhluzUl7ECeTACaB/NnawX9T4/ujUZVrDanDzwBaI8eGRatRaA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiHhlTAP",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAAFA12/9B3OzwE+6jftRgY82o+gqd6R5VK2CdiAf9ZE7F1Qs+vpcstDjo393O6zG4AwRbKx748d6dSIzY9nIKAbhA57V9hKuQfuRuikJOZZnWygzlmDRPsLBVfg/fhluzUl7ECeTACaB/NnawX9T4/ujUZVrDanDzwBaI8eGRatRaA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiHhlTAP",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
  "id": -576460752303422985,
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
  "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
  "id": -576460752303422985,
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "state": "tx_+QENCwH4hLhAAFA12/9B3OzwE+6jftRgY82o+gqd6R5VK2CdiAf9ZE7F1Qs+vpcstDjo393O6zG4AwRbKx748d6dSIzY9nIKAbhA57V9hKuQfuRuikJOZZnWygzlmDRPsLBVfg/fhluzUl7ECeTACaB/NnawX9T4/ujUZVrDanDzwBaI8eGRatRaA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiHhlTAP"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "state": "tx_+QENCwH4hLhAAFA12/9B3OzwE+6jftRgY82o+gqd6R5VK2CdiAf9ZE7F1Qs+vpcstDjo393O6zG4AwRbKx748d6dSIzY9nIKAbhA57V9hKuQfuRuikJOZZnWygzlmDRPsLBVfg/fhluzUl7ECeTACaB/NnawX9T4/ujUZVrDanDzwBaI8eGRatRaA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiHhlTAP"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
  "method": "channels.deposit",
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBvCAKHleNDKKmMjUW8UimDQlOUxTYLMMvzNZAir/Pjz4oQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhnBIhhsPP6BkHkp+5scV2OHwQbjEIZHR7qRYh9akzYCkDxPO9Ji42QIiKbET8Q==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainDeposit"
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
  "id": -576460752303422984,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDOTJRtQRFhb0DAZhDTuTSdcw6DNC7A9pih46GdNthl9FGmUqLXBEroDUswFUMqSgs0Q050utBWqszrO5BU8DABuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCIufP4to="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
  "id": -576460752303422984,
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDOTJRtQRFhb0DAZhDTuTSdcw6DNC7A9pih46GdNthl9FGmUqLXBEroDUswFUMqSgs0Q050utBWqszrO5BU8DABuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCIufP4to=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainDeposit"
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
  "id": -576460752303422983,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECffYywdDEw0vcrzVJrmF1+Amxh8bAt3LOA/Y3lZ8Q2FQrKjTFpad/eEruMgT+ldvW93AmUJNI3RGQv3Lofz2EFuEDOTJRtQRFhb0DAZhDTuTSdcw6DNC7A9pih46GdNthl9FGmUqLXBEroDUswFUMqSgs0Q050utBWqszrO5BU8DABuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCIk7K0JU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
  "id": -576460752303422983,
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuECffYywdDEw0vcrzVJrmF1+Amxh8bAt3LOA/Y3lZ8Q2FQrKjTFpad/eEruMgT+ldvW93AmUJNI3RGQv3Lofz2EFuEDOTJRtQRFhb0DAZhDTuTSdcw6DNC7A9pih46GdNthl9FGmUqLXBEroDUswFUMqSgs0Q050utBWqszrO5BU8DABuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCIk7K0JU=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuECffYywdDEw0vcrzVJrmF1+Amxh8bAt3LOA/Y3lZ8Q2FQrKjTFpad/eEruMgT+ldvW93AmUJNI3RGQv3Lofz2EFuEDOTJRtQRFhb0DAZhDTuTSdcw6DNC7A9pih46GdNthl9FGmUqLXBEroDUswFUMqSgs0Q050utBWqszrO5BU8DABuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCIk7K0JU=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECffYywdDEw0vcrzVJrmF1+Amxh8bAt3LOA/Y3lZ8Q2FQrKjTFpad/eEruMgT+ldvW93AmUJNI3RGQv3Lofz2EFuEDOTJRtQRFhb0DAZhDTuTSdcw6DNC7A9pih46GdNthl9FGmUqLXBEroDUswFUMqSgs0Q050utBWqszrO5BU8DABuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCIk7K0JU=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECffYywdDEw0vcrzVJrmF1+Amxh8bAt3LOA/Y3lZ8Q2FQrKjTFpad/eEruMgT+ldvW93AmUJNI3RGQv3Lofz2EFuEDOTJRtQRFhb0DAZhDTuTSdcw6DNC7A9pih46GdNthl9FGmUqLXBEroDUswFUMqSgs0Q050utBWqszrO5BU8DABuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCIk7K0JU=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "state": "tx_+P4LAfiEuECffYywdDEw0vcrzVJrmF1+Amxh8bAt3LOA/Y3lZ8Q2FQrKjTFpad/eEruMgT+ldvW93AmUJNI3RGQv3Lofz2EFuEDOTJRtQRFhb0DAZhDTuTSdcw6DNC7A9pih46GdNthl9FGmUqLXBEroDUswFUMqSgs0Q050utBWqszrO5BU8DABuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCIk7K0JU="
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "state": "tx_+P4LAfiEuECffYywdDEw0vcrzVJrmF1+Amxh8bAt3LOA/Y3lZ8Q2FQrKjTFpad/eEruMgT+ldvW93AmUJNI3RGQv3Lofz2EFuEDOTJRtQRFhb0DAZhDTuTSdcw6DNC7A9pih46GdNthl9FGmUqLXBEroDUswFUMqSgs0Q050utBWqszrO5BU8DABuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIZwSIYbDz+gZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCIk7K0JU="
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
  "method": "channels.deposit",
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBvCAKHleNDKKmMjUW8UimDQlOUxTYLMMvzNZAir/Pjz4oQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWvwIAhnBIhhsPP6DNmaSTSTRoRmnF+iQrsKYc2CmTrB5E7GNocruXEohWugMNQGnFqQ==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainDeposit"
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
  "id": -576460752303422982,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBo8/pyJPPbSM0IsIdJ33kdeQRHTY5zN8EvhJo+C7qWuZISt49zyBpgBZ9nv1zU4PD8MS9glMwL/4VuiUbqUwYJuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDDYg03So="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
  "id": -576460752303422982,
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBo8/pyJPPbSM0IsIdJ33kdeQRHTY5zN8EvhJo+C7qWuZISt49zyBpgBZ9nv1zU4PD8MS9glMwL/4VuiUbqUwYJuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDDYg03So=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainDeposit"
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
  "id": -576460752303422981,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBo8/pyJPPbSM0IsIdJ33kdeQRHTY5zN8EvhJo+C7qWuZISt49zyBpgBZ9nv1zU4PD8MS9glMwL/4VuiUbqUwYJuEDkzxJ2gOFIQe7sKHCZjytQ6UhdAh/qjplsimG4GKw22LzMTXDV1sZ3+h7sPQKYI3Mc6Jc96C0eUKz1hZoO61YGuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDDeTvVPw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
  "id": -576460752303422981,
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBo8/pyJPPbSM0IsIdJ33kdeQRHTY5zN8EvhJo+C7qWuZISt49zyBpgBZ9nv1zU4PD8MS9glMwL/4VuiUbqUwYJuEDkzxJ2gOFIQe7sKHCZjytQ6UhdAh/qjplsimG4GKw22LzMTXDV1sZ3+h7sPQKYI3Mc6Jc96C0eUKz1hZoO61YGuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDDeTvVPw=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBo8/pyJPPbSM0IsIdJ33kdeQRHTY5zN8EvhJo+C7qWuZISt49zyBpgBZ9nv1zU4PD8MS9glMwL/4VuiUbqUwYJuEDkzxJ2gOFIQe7sKHCZjytQ6UhdAh/qjplsimG4GKw22LzMTXDV1sZ3+h7sPQKYI3Mc6Jc96C0eUKz1hZoO61YGuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDDeTvVPw=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "message": {
        "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBo8/pyJPPbSM0IsIdJ33kdeQRHTY5zN8EvhJo+C7qWuZISt49zyBpgBZ9nv1zU4PD8MS9glMwL/4VuiUbqUwYJuEDkzxJ2gOFIQe7sKHCZjytQ6UhdAh/qjplsimG4GKw22LzMTXDV1sZ3+h7sPQKYI3Mc6Jc96C0eUKz1hZoO61YGuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDDeTvVPw=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBo8/pyJPPbSM0IsIdJ33kdeQRHTY5zN8EvhJo+C7qWuZISt49zyBpgBZ9nv1zU4PD8MS9glMwL/4VuiUbqUwYJuEDkzxJ2gOFIQe7sKHCZjytQ6UhdAh/qjplsimG4GKw22LzMTXDV1sZ3+h7sPQKYI3Mc6Jc96C0eUKz1hZoO61YGuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDDeTvVPw=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "state": "tx_+P4LAfiEuEBo8/pyJPPbSM0IsIdJ33kdeQRHTY5zN8EvhJo+C7qWuZISt49zyBpgBZ9nv1zU4PD8MS9glMwL/4VuiUbqUwYJuEDkzxJ2gOFIQe7sKHCZjytQ6UhdAh/qjplsimG4GKw22LzMTXDV1sZ3+h7sPQKYI3Mc6Jc96C0eUKz1hZoO61YGuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDDeTvVPw="
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "state": "tx_+P4LAfiEuEBo8/pyJPPbSM0IsIdJ33kdeQRHTY5zN8EvhJo+C7qWuZISt49zyBpgBZ9nv1zU4PD8MS9glMwL/4VuiUbqUwYJuEDkzxJ2gOFIQe7sKHCZjytQ6UhdAh/qjplsimG4GKw22LzMTXDV1sZ3+h7sPQKYI3Mc6Jc96C0eUKz1hZoO61YGuHT4cjMBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIZwSIYbDz+gzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDDeTvVPw="
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBvCAKHleNDKKmMjUW8UimDQlOUxTYLMMvzNZAir/Pjz4oQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY2kdavwAGGG0jrV+ADAIYSMJzlQAAj1iee9A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422980,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBjDkF76B23cPOXGrFwCrVJDOqdXgbUEdnx53LrWxDGUraRU4gEROEhRL/tQpvtdUrJASA4LSYmaiRskG2EiLQOuF/4XTUBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr8ABhhtI61fgAwCGEjCc5UAAIxQpLWQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
  "id": -576460752303422980,
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBjDkF76B23cPOXGrFwCrVJDOqdXgbUEdnx53LrWxDGUraRU4gEROEhRL/tQpvtdUrJASA4LSYmaiRskG2EiLQOuF/4XTUBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr8ABhhtI61fgAwCGEjCc5UAAIxQpLWQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422979,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAgcXLob7m4xv6do+vUf8RnpFCvig9+YSfU50B1lDqzro3D9iuAHk3aiCRD78fTbRps330bTaHtC/GG/cmH4H8FuEBjDkF76B23cPOXGrFwCrVJDOqdXgbUEdnx53LrWxDGUraRU4gEROEhRL/tQpvtdUrJASA4LSYmaiRskG2EiLQOuF/4XTUBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr8ABhhtI61fgAwCGEjCc5UAAIwuh1qs="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
  "id": -576460752303422979,
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAgcXLob7m4xv6do+vUf8RnpFCvig9+YSfU50B1lDqzro3D9iuAHk3aiCRD78fTbRps330bTaHtC/GG/cmH4H8FuEBjDkF76B23cPOXGrFwCrVJDOqdXgbUEdnx53LrWxDGUraRU4gEROEhRL/tQpvtdUrJASA4LSYmaiRskG2EiLQOuF/4XTUBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr8ABhhtI61fgAwCGEjCc5UAAIwuh1qs=",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAgcXLob7m4xv6do+vUf8RnpFCvig9+YSfU50B1lDqzro3D9iuAHk3aiCRD78fTbRps330bTaHtC/GG/cmH4H8FuEBjDkF76B23cPOXGrFwCrVJDOqdXgbUEdnx53LrWxDGUraRU4gEROEhRL/tQpvtdUrJASA4LSYmaiRskG2EiLQOuF/4XTUBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr8ABhhtI61fgAwCGEjCc5UAAIwuh1qs=",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAgcXLob7m4xv6do+vUf8RnpFCvig9+YSfU50B1lDqzro3D9iuAHk3aiCRD78fTbRps330bTaHtC/GG/cmH4H8FuEBjDkF76B23cPOXGrFwCrVJDOqdXgbUEdnx53LrWxDGUraRU4gEROEhRL/tQpvtdUrJASA4LSYmaiRskG2EiLQOuF/4XTUBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr8ABhhtI61fgAwCGEjCc5UAAIwuh1qs=",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAgcXLob7m4xv6do+vUf8RnpFCvig9+YSfU50B1lDqzro3D9iuAHk3aiCRD78fTbRps330bTaHtC/GG/cmH4H8FuEBjDkF76B23cPOXGrFwCrVJDOqdXgbUEdnx53LrWxDGUraRU4gEROEhRL/tQpvtdUrJASA4LSYmaiRskG2EiLQOuF/4XTUBoQbwgCh5XjQyipjI1FvFIpg0JTlMU2CzDL8zWQIq/z48+KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr8ABhhtI61fgAwCGEjCc5UAAIwuh1qs=",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
    "channel_id": "ch_2pvGQ7LSSRFp4HDM6mjZCSAfsE6dsMME7rkmKem6G9zgDUpQRW",
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
