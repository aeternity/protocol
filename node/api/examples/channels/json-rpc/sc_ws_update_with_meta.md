
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
      "fsm_id": "ba_5jdaTiIStFU9wp827Pk6y5fZZEF1bbSb+DUq55ANX1Qk7gCp"
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
      "fsm_id": "ba_jy7aYZTs96j9bcA95qTIZyFHoMyHyU/YE3TNbOgIkGW/WcGJ"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYIPIGbqA==",
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
    "signed_tx": "tx_+MsLAfhCuEAXwiVvpTNqthpKmm02lg27C2+t8w8nzz+U9G2J+O7lXoickc3Ui/GUD2s1h67FhlI9uRIMN6qJiSbe8tAB3eUFuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2CGCX5mU="
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
      "signed_tx": "tx_+MsLAfhCuEAXwiVvpTNqthpKmm02lg27C2+t8w8nzz+U9G2J+O7lXoickc3Ui/GUD2s1h67FhlI9uRIMN6qJiSbe8tAB3eUFuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2CGCX5mU=",
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
    "signed_tx": "tx_+QENCwH4hLhAF8Ilb6UzarYaSpptNpYNuwtvrfMPJ88/lPRtifju5V6InJHN1IvxlA9rNYeuxYZSPbkSDDeqiYkm3vLQAd3lBbhAQm3yrmc5eVvX8HUZIDJ/Q+CvlEsC22vtLVJz3XUPGmq9psICazbqSEjlzbJetohYGKdiCJaBoJp4QaecKrDGDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgg2w3KQ"
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAF8Ilb6UzarYaSpptNpYNuwtvrfMPJ88/lPRtifju5V6InJHN1IvxlA9rNYeuxYZSPbkSDDeqiYkm3vLQAd3lBbhAQm3yrmc5eVvX8HUZIDJ/Q+CvlEsC22vtLVJz3XUPGmq9psICazbqSEjlzbJetohYGKdiCJaBoJp4QaecKrDGDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgg2w3KQ",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAF8Ilb6UzarYaSpptNpYNuwtvrfMPJ88/lPRtifju5V6InJHN1IvxlA9rNYeuxYZSPbkSDDeqiYkm3vLQAd3lBbhAQm3yrmc5eVvX8HUZIDJ/Q+CvlEsC22vtLVJz3XUPGmq9psICazbqSEjlzbJetohYGKdiCJaBoJp4QaecKrDGDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgg2w3KQ",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAF8Ilb6UzarYaSpptNpYNuwtvrfMPJ88/lPRtifju5V6InJHN1IvxlA9rNYeuxYZSPbkSDDeqiYkm3vLQAd3lBbhAQm3yrmc5eVvX8HUZIDJ/Q+CvlEsC22vtLVJz3XUPGmq9psICazbqSEjlzbJetohYGKdiCJaBoJp4QaecKrDGDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgg2w3KQ",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAF8Ilb6UzarYaSpptNpYNuwtvrfMPJ88/lPRtifju5V6InJHN1IvxlA9rNYeuxYZSPbkSDDeqiYkm3vLQAd3lBbhAQm3yrmc5eVvX8HUZIDJ/Q+CvlEsC22vtLVJz3XUPGmq9psICazbqSEjlzbJetohYGKdiCJaBoJp4QaecKrDGDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgg2w3KQ",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "message": {
        "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "message": {
        "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
  "id": -576460752303423339,
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
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423339,
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+QENCwH4hLhAF8Ilb6UzarYaSpptNpYNuwtvrfMPJ88/lPRtifju5V6InJHN1IvxlA9rNYeuxYZSPbkSDDeqiYkm3vLQAd3lBbhAQm3yrmc5eVvX8HUZIDJ/Q+CvlEsC22vtLVJz3XUPGmq9psICazbqSEjlzbJetohYGKdiCJaBoJp4QaecKrDGDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgg2w3KQ"
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+QENCwH4hLhAF8Ilb6UzarYaSpptNpYNuwtvrfMPJ88/lPRtifju5V6InJHN1IvxlA9rNYeuxYZSPbkSDDeqiYkm3vLQAd3lBbhAQm3yrmc5eVvX8HUZIDJ/Q+CvlEsC22vtLVJz3XUPGmq9psICazbqSEjlzbJetohYGKdiCJaBoJp4QaecKrDGDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgg2w3KQ"
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
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423338,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "meta": 17,
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjwxbpXNQ1eosp6c8nJ3O2RoqzrtvUjT+0ReWz1HefJbAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt3eQuwo=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "signed_tx": "tx_+JALAfhCuEAgzK9r/DMMNL5fJAbXJLebC76+AMdG/Eufc8QU3poCs9zL4NZcDZjIU3oLBsL/RI+2WvYuwqX8tVzQppIA3H0NuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cbLREa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAgzK9r/DMMNL5fJAbXJLebC76+AMdG/Eufc8QU3poCs9zL4NZcDZjIU3oLBsL/RI+2WvYuwqX8tVzQppIA3H0NuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cbLREa",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "signed_tx": "tx_+NILAfiEuEAgzK9r/DMMNL5fJAbXJLebC76+AMdG/Eufc8QU3poCs9zL4NZcDZjIU3oLBsL/RI+2WvYuwqX8tVzQppIA3H0NuECIrAiZqzKB5wgN669VtRVhvL02tOi69CYVBGlp9oms41cTLNbmesn7gLA/GBOt9W1LEPEIi8+TuQKCc/hwhJMCuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fxtA4t"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEAgzK9r/DMMNL5fJAbXJLebC76+AMdG/Eufc8QU3poCs9zL4NZcDZjIU3oLBsL/RI+2WvYuwqX8tVzQppIA3H0NuECIrAiZqzKB5wgN669VtRVhvL02tOi69CYVBGlp9oms41cTLNbmesn7gLA/GBOt9W1LEPEIi8+TuQKCc/hwhJMCuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fxtA4t"
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEAgzK9r/DMMNL5fJAbXJLebC76+AMdG/Eufc8QU3poCs9zL4NZcDZjIU3oLBsL/RI+2WvYuwqX8tVzQppIA3H0NuECIrAiZqzKB5wgN669VtRVhvL02tOi69CYVBGlp9oms41cTLNbmesn7gLA/GBOt9W1LEPEIi8+TuQKCc/hwhJMCuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fxtA4t"
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
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423335,
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
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAgzK9r/DMMNL5fJAbXJLebC76+AMdG/Eufc8QU3poCs9zL4NZcDZjIU3oLBsL/RI+2WvYuwqX8tVzQppIA3H0NuECIrAiZqzKB5wgN669VtRVhvL02tOi69CYVBGlp9oms41cTLNbmesn7gLA/GBOt9W1LEPEIi8+TuQKCc/hwhJMCuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fxtA4t",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
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
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423333,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "meta": 17,
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjwxbpXNQ1eosp6c8nJ3O2RoqzrtvUjT+0ReWz1HefJbA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdvI2RyU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "signed_tx": "tx_+JALAfhCuEAU0ROjebJis/XjIWIwTmkVcZFuF5vcSAiuP5/muhQNmD/p1ZDdpVpoc5PSjqJf++rggmxPPmmEriQ5mtDY628OuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYUlMkd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAU0ROjebJis/XjIWIwTmkVcZFuF5vcSAiuP5/muhQNmD/p1ZDdpVpoc5PSjqJf++rggmxPPmmEriQ5mtDY628OuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYUlMkd",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "signed_tx": "tx_+NILAfiEuEAU0ROjebJis/XjIWIwTmkVcZFuF5vcSAiuP5/muhQNmD/p1ZDdpVpoc5PSjqJf++rggmxPPmmEriQ5mtDY628OuECfUhRI4evCQB80kNBbdMbb5urASDgyGXttwr0owFpWj69tVn9zN2BW85FQurKmvIz9/VvQQKbgSswWqgx5BTANuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb/U5sG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEAU0ROjebJis/XjIWIwTmkVcZFuF5vcSAiuP5/muhQNmD/p1ZDdpVpoc5PSjqJf++rggmxPPmmEriQ5mtDY628OuECfUhRI4evCQB80kNBbdMbb5urASDgyGXttwr0owFpWj69tVn9zN2BW85FQurKmvIz9/VvQQKbgSswWqgx5BTANuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb/U5sG"
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEAU0ROjebJis/XjIWIwTmkVcZFuF5vcSAiuP5/muhQNmD/p1ZDdpVpoc5PSjqJf++rggmxPPmmEriQ5mtDY628OuECfUhRI4evCQB80kNBbdMbb5urASDgyGXttwr0owFpWj69tVn9zN2BW85FQurKmvIz9/VvQQKbgSswWqgx5BTANuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb/U5sG"
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
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423330,
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
  "id": -576460752303423329,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423329,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAU0ROjebJis/XjIWIwTmkVcZFuF5vcSAiuP5/muhQNmD/p1ZDdpVpoc5PSjqJf++rggmxPPmmEriQ5mtDY628OuECfUhRI4evCQB80kNBbdMbb5urASDgyGXttwr0owFpWj69tVn9zN2BW85FQurKmvIz9/VvQQKbgSswWqgx5BTANuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb/U5sG",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
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
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423328,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "meta": 17,
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjwxbpXNQ1eosp6c8nJ3O2RoqzrtvUjT+0ReWz1HefJbBKBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAgGU7+s=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "signed_tx": "tx_+JALAfhCuEDBAClOO+cVhJ7uEyOVkicD/tAy56uf1r1WmD0bQcxHbebqRhtnNw2WGAw9undkM5F13BJIjx806Fr3DGiR4xEPuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIwtNv2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDBAClOO+cVhJ7uEyOVkicD/tAy56uf1r1WmD0bQcxHbebqRhtnNw2WGAw9undkM5F13BJIjx806Fr3DGiR4xEPuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIwtNv2",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "signed_tx": "tx_+NILAfiEuEDBAClOO+cVhJ7uEyOVkicD/tAy56uf1r1WmD0bQcxHbebqRhtnNw2WGAw9undkM5F13BJIjx806Fr3DGiR4xEPuEDf3sunE4bydLZUqVFqWKJIvlfN0sI4OWYHL3oUyyssvQ7crEshWYEc3GT2ZDmMuQJYjRbspN93Emrtum3TlOUPuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJP4gnz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEDBAClOO+cVhJ7uEyOVkicD/tAy56uf1r1WmD0bQcxHbebqRhtnNw2WGAw9undkM5F13BJIjx806Fr3DGiR4xEPuEDf3sunE4bydLZUqVFqWKJIvlfN0sI4OWYHL3oUyyssvQ7crEshWYEc3GT2ZDmMuQJYjRbspN93Emrtum3TlOUPuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJP4gnz"
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEDBAClOO+cVhJ7uEyOVkicD/tAy56uf1r1WmD0bQcxHbebqRhtnNw2WGAw9undkM5F13BJIjx806Fr3DGiR4xEPuEDf3sunE4bydLZUqVFqWKJIvlfN0sI4OWYHL3oUyyssvQ7crEshWYEc3GT2ZDmMuQJYjRbspN93Emrtum3TlOUPuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJP4gnz"
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
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423325,
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
  "id": -576460752303423324,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423324,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDBAClOO+cVhJ7uEyOVkicD/tAy56uf1r1WmD0bQcxHbebqRhtnNw2WGAw9undkM5F13BJIjx806Fr3DGiR4xEPuEDf3sunE4bydLZUqVFqWKJIvlfN0sI4OWYHL3oUyyssvQ7crEshWYEc3GT2ZDmMuQJYjRbspN93Emrtum3TlOUPuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJP4gnz",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
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
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423323,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "meta": 17,
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjwxbpXNQ1eosp6c8nJ3O2RoqzrtvUjT+0ReWz1HefJbBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhg2oK4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "signed_tx": "tx_+JALAfhCuEAuZ5hkmM7u/NY3vE+r6KtGQMXTUWhlX0DVovMIBdn0lTFsr09UWn99eCOEGjchpqjd+gdyH7RctMHT+s7y/MsLuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnass34e"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAuZ5hkmM7u/NY3vE+r6KtGQMXTUWhlX0DVovMIBdn0lTFsr09UWn99eCOEGjchpqjd+gdyH7RctMHT+s7y/MsLuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnass34e",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "signed_tx": "tx_+NILAfiEuEAhnpUg7OAbYhnjQCzFglpBpVfnKXgSBJ+syGUPVHzCe3jm3F1juXzbgAacqchsCIlDo6GrK0YLKAjaUKKvzncCuEAuZ5hkmM7u/NY3vE+r6KtGQMXTUWhlX0DVovMIBdn0lTFsr09UWn99eCOEGjchpqjd+gdyH7RctMHT+s7y/MsLuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaIrzFo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEAhnpUg7OAbYhnjQCzFglpBpVfnKXgSBJ+syGUPVHzCe3jm3F1juXzbgAacqchsCIlDo6GrK0YLKAjaUKKvzncCuEAuZ5hkmM7u/NY3vE+r6KtGQMXTUWhlX0DVovMIBdn0lTFsr09UWn99eCOEGjchpqjd+gdyH7RctMHT+s7y/MsLuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaIrzFo"
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEAhnpUg7OAbYhnjQCzFglpBpVfnKXgSBJ+syGUPVHzCe3jm3F1juXzbgAacqchsCIlDo6GrK0YLKAjaUKKvzncCuEAuZ5hkmM7u/NY3vE+r6KtGQMXTUWhlX0DVovMIBdn0lTFsr09UWn99eCOEGjchpqjd+gdyH7RctMHT+s7y/MsLuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaIrzFo"
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
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423320,
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
  "id": -576460752303423319,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423319,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAhnpUg7OAbYhnjQCzFglpBpVfnKXgSBJ+syGUPVHzCe3jm3F1juXzbgAacqchsCIlDo6GrK0YLKAjaUKKvzncCuEAuZ5hkmM7u/NY3vE+r6KtGQMXTUWhlX0DVovMIBdn0lTFsr09UWn99eCOEGjchpqjd+gdyH7RctMHT+s7y/MsLuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaIrzFo",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
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
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423318,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "meta": 17,
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjwxbpXNQ1eosp6c8nJ3O2RoqzrtvUjT+0ReWz1HefJbBqBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAqGWFoI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "signed_tx": "tx_+JALAfhCuEAAZtxDMucBeIkuoOZGLkjiBFlV9X8HTEJZ9wuDwt3AtZLxjmtb2hsHTOUjBufkj3zYIRONFZsQOC1e2gRyovQFuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALY4MaT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAAZtxDMucBeIkuoOZGLkjiBFlV9X8HTEJZ9wuDwt3AtZLxjmtb2hsHTOUjBufkj3zYIRONFZsQOC1e2gRyovQFuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALY4MaT",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "signed_tx": "tx_+NILAfiEuEAAZtxDMucBeIkuoOZGLkjiBFlV9X8HTEJZ9wuDwt3AtZLxjmtb2hsHTOUjBufkj3zYIRONFZsQOC1e2gRyovQFuEBRxhtwMBd3sy93/bhJz65tXrzqvzUpQaiuJWWcjVwtFF9KHslVGsU/IO7vaJ8xgr8pdVJX9mFV29/EhukWZhgDuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKFpzhH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEAAZtxDMucBeIkuoOZGLkjiBFlV9X8HTEJZ9wuDwt3AtZLxjmtb2hsHTOUjBufkj3zYIRONFZsQOC1e2gRyovQFuEBRxhtwMBd3sy93/bhJz65tXrzqvzUpQaiuJWWcjVwtFF9KHslVGsU/IO7vaJ8xgr8pdVJX9mFV29/EhukWZhgDuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKFpzhH"
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
    "data": {
      "state": "tx_+NILAfiEuEAAZtxDMucBeIkuoOZGLkjiBFlV9X8HTEJZ9wuDwt3AtZLxjmtb2hsHTOUjBufkj3zYIRONFZsQOC1e2gRyovQFuEBRxhtwMBd3sy93/bhJz65tXrzqvzUpQaiuJWWcjVwtFF9KHslVGsU/IO7vaJ8xgr8pdVJX9mFV29/EhukWZhgDuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKFpzhH"
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
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423315,
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
  "id": -576460752303423314,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423314,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAAZtxDMucBeIkuoOZGLkjiBFlV9X8HTEJZ9wuDwt3AtZLxjmtb2hsHTOUjBufkj3zYIRONFZsQOC1e2gRyovQFuEBRxhtwMBd3sy93/bhJz65tXrzqvzUpQaiuJWWcjVwtFF9KHslVGsU/IO7vaJ8xgr8pdVJX9mFV29/EhukWZhgDuEj4RjkCoQY8MW6VzUNXqLKenPJydztkaKs67b1I0/tEXls9R3nyWwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKFpzhH",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
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
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423313,
  "jsonrpc": "2.0",
  "result": "ok",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
    "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
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
  "channel_id": "ch_TWZ1DkhfnQTjpbeHZryDCHNuoaffLoEA5QmUcPmJkqHLK3Fda",
  "id": -576460752303423312,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
