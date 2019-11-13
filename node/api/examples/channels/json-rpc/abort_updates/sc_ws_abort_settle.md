
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
      "fsm_id": "ba_0p+rilrWUqIrGO9AIbVNjMXVXSazXewajZZGOUFp33T/bgMm"
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
      "fsm_id": "ba_vkLZGVm8mecNmDAudAKXrHz0q0CPgDljwoub9PNHa0HzfKnf"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZEg1MKuw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422752,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBz9RCBYkiuQxb07+G2ILtlON7U0mA5IMs4dH+LnOB+U1ZP3I4F9120laaDNv6/6cMwPDlm44f7Ed3OlSbA62wBuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2RDBc4Dg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422752,
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
      "signed_tx": "tx_+MsLAfhCuEBz9RCBYkiuQxb07+G2ILtlON7U0mA5IMs4dH+LnOB+U1ZP3I4F9120laaDNv6/6cMwPDlm44f7Ed3OlSbA62wBuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2RDBc4Dg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422751,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAc/UQgWJIrkMW9O/htiC7ZTje1NJgOSDLOHR/i5zgflNWT9yOBfddtJWmgzb+v+nDMDw5ZuOH+xHdzpUmwOtsAbhAyBMiyVMpbyGMAcj35rRalQyaPg6XMF+uUEZ1I9h6p8Nkp1O8uxmIDpC2x3f9BpG3n9WVxMYdOwpPg/knUbm4D7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkRW9gYp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422751,
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAc/UQgWJIrkMW9O/htiC7ZTje1NJgOSDLOHR/i5zgflNWT9yOBfddtJWmgzb+v+nDMDw5ZuOH+xHdzpUmwOtsAbhAyBMiyVMpbyGMAcj35rRalQyaPg6XMF+uUEZ1I9h6p8Nkp1O8uxmIDpC2x3f9BpG3n9WVxMYdOwpPg/knUbm4D7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkRW9gYp",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAc/UQgWJIrkMW9O/htiC7ZTje1NJgOSDLOHR/i5zgflNWT9yOBfddtJWmgzb+v+nDMDw5ZuOH+xHdzpUmwOtsAbhAyBMiyVMpbyGMAcj35rRalQyaPg6XMF+uUEZ1I9h6p8Nkp1O8uxmIDpC2x3f9BpG3n9WVxMYdOwpPg/knUbm4D7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkRW9gYp",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAc/UQgWJIrkMW9O/htiC7ZTje1NJgOSDLOHR/i5zgflNWT9yOBfddtJWmgzb+v+nDMDw5ZuOH+xHdzpUmwOtsAbhAyBMiyVMpbyGMAcj35rRalQyaPg6XMF+uUEZ1I9h6p8Nkp1O8uxmIDpC2x3f9BpG3n9WVxMYdOwpPg/knUbm4D7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkRW9gYp",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAc/UQgWJIrkMW9O/htiC7ZTje1NJgOSDLOHR/i5zgflNWT9yOBfddtJWmgzb+v+nDMDw5ZuOH+xHdzpUmwOtsAbhAyBMiyVMpbyGMAcj35rRalQyaPg6XMF+uUEZ1I9h6p8Nkp1O8uxmIDpC2x3f9BpG3n9WVxMYdOwpPg/knUbm4D7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkRW9gYp",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "message": {
        "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "message": {
        "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
  "id": -576460752303422750,
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
  "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
  "id": -576460752303422750,
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "state": "tx_+QENCwH4hLhAc/UQgWJIrkMW9O/htiC7ZTje1NJgOSDLOHR/i5zgflNWT9yOBfddtJWmgzb+v+nDMDw5ZuOH+xHdzpUmwOtsAbhAyBMiyVMpbyGMAcj35rRalQyaPg6XMF+uUEZ1I9h6p8Nkp1O8uxmIDpC2x3f9BpG3n9WVxMYdOwpPg/knUbm4D7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkRW9gYp"
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "state": "tx_+QENCwH4hLhAc/UQgWJIrkMW9O/htiC7ZTje1NJgOSDLOHR/i5zgflNWT9yOBfddtJWmgzb+v+nDMDw5ZuOH+xHdzpUmwOtsAbhAyBMiyVMpbyGMAcj35rRalQyaPg6XMF+uUEZ1I9h6p8Nkp1O8uxmIDpC2x3f9BpG3n9WVxMYdOwpPg/knUbm4D7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkRW9gYp"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBhNbiMOqhL1WUMPo5+8UX4CA5hTP7KxIIgJvXWBfNJ/WoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYC5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGFT7sgIAARcT8caU=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhA38sq/jykv9Xxd7AQjeH6SwZJKDnzANjxo/I9xpUG9LPq49b+Ukw/V3kj/GqF/aTsMmEYXsKOWRhcz/1ztsRJDrkBovkBnzYBoQYTW4jDqoS9VlDD6OfvFF+AgOYUz+ysSCICb11gXzSf1qEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAEVEdaGa"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA38sq/jykv9Xxd7AQjeH6SwZJKDnzANjxo/I9xpUG9LPq49b+Ukw/V3kj/GqF/aTsMmEYXsKOWRhcz/1ztsRJDrkBovkBnzYBoQYTW4jDqoS9VlDD6OfvFF+AgOYUz+ysSCICb11gXzSf1qEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAEVEdaGa",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA38sq/jykv9Xxd7AQjeH6SwZJKDnzANjxo/I9xpUG9LPq49b+Ukw/V3kj/GqF/aTsMmEYXsKOWRhcz/1ztsRJDrkBovkBnzYBoQYTW4jDqoS9VlDD6OfvFF+AgOYUz+ysSCICb11gXzSf1qEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAEVEdaGa",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBhNbiMOqhL1WUMPo5+8UX4CA5hTP7KxIIgJvXWBfNJ/WoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiX/+GJGE5yoABAIYPXtZ/KABG0T+biA==",
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
  "method": "channels.settle_sign",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBhNbiMOqhL1WUMPo5+8UX4CA5hTP7KxIIgJvXWBfNJ/WoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y/qiUiX/+GJGE5yoABAIYPXtZ/KAAZclXCOw==",
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
  "method": "channels.settle_sign",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
  "id": -576460752303422749,
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
  "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
  "id": -576460752303422749,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422748,
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
    "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
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
  "channel_id": "ch_9XTqnRneUCziUeGFtZu1Gs87vq1YHvmVBgFC3zxh5To8kMVZP",
  "id": -576460752303422748,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
