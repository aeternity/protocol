
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
      "fsm_id": "ba_wJK8hPZ5lS5HktUWf5yYMdEMQwzozJD4IK/tsscxPd2NC5Mg"
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
      "fsm_id": "ba_XrG6fKH0NzLrCfuQyEdFn2iFe/707BOXsxISOH9Z8uApAQ+L"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYvg5aJCw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422919,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDMbvv8MIIip696KgdMHUbcaFNxsU7VJJCCAXig2Tv9bXZ9emIU+fF+JOkNIiuP8OZkDnk3FV6ItIDiJAl6wWoGuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2L4TGEn0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422919,
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
      "signed_tx": "tx_+MsLAfhCuEDMbvv8MIIip696KgdMHUbcaFNxsU7VJJCCAXig2Tv9bXZ9emIU+fF+JOkNIiuP8OZkDnk3FV6ItIDiJAl6wWoGuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2L4TGEn0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422918,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAyFUo3JnfBHycISaFbeohGma3AzLUZyTD47mHyl8jlm8rwF2ICb5s2dIolFflihmQnr3xuUF54CwfAfINGw/tArhAzG77/DCCIqeveioHTB1G3GhTcbFO1SSQggF4oNk7/W12fXpiFPnxfiTpDSIrj/DmZA55NxVeiLSA4iQJesFqBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi8Q00+S"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422918,
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAyFUo3JnfBHycISaFbeohGma3AzLUZyTD47mHyl8jlm8rwF2ICb5s2dIolFflihmQnr3xuUF54CwfAfINGw/tArhAzG77/DCCIqeveioHTB1G3GhTcbFO1SSQggF4oNk7/W12fXpiFPnxfiTpDSIrj/DmZA55NxVeiLSA4iQJesFqBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi8Q00+S",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAyFUo3JnfBHycISaFbeohGma3AzLUZyTD47mHyl8jlm8rwF2ICb5s2dIolFflihmQnr3xuUF54CwfAfINGw/tArhAzG77/DCCIqeveioHTB1G3GhTcbFO1SSQggF4oNk7/W12fXpiFPnxfiTpDSIrj/DmZA55NxVeiLSA4iQJesFqBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi8Q00+S",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAyFUo3JnfBHycISaFbeohGma3AzLUZyTD47mHyl8jlm8rwF2ICb5s2dIolFflihmQnr3xuUF54CwfAfINGw/tArhAzG77/DCCIqeveioHTB1G3GhTcbFO1SSQggF4oNk7/W12fXpiFPnxfiTpDSIrj/DmZA55NxVeiLSA4iQJesFqBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi8Q00+S",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAyFUo3JnfBHycISaFbeohGma3AzLUZyTD47mHyl8jlm8rwF2ICb5s2dIolFflihmQnr3xuUF54CwfAfINGw/tArhAzG77/DCCIqeveioHTB1G3GhTcbFO1SSQggF4oNk7/W12fXpiFPnxfiTpDSIrj/DmZA55NxVeiLSA4iQJesFqBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi8Q00+S",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "message": {
        "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "message": {
        "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
  "id": -576460752303422917,
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
  "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
  "id": -576460752303422917,
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "state": "tx_+QENCwH4hLhAyFUo3JnfBHycISaFbeohGma3AzLUZyTD47mHyl8jlm8rwF2ICb5s2dIolFflihmQnr3xuUF54CwfAfINGw/tArhAzG77/DCCIqeveioHTB1G3GhTcbFO1SSQggF4oNk7/W12fXpiFPnxfiTpDSIrj/DmZA55NxVeiLSA4iQJesFqBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi8Q00+S"
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "state": "tx_+QENCwH4hLhAyFUo3JnfBHycISaFbeohGma3AzLUZyTD47mHyl8jlm8rwF2ICb5s2dIolFflihmQnr3xuUF54CwfAfINGw/tArhAzG77/DCCIqeveioHTB1G3GhTcbFO1SSQggF4oNk7/W12fXpiFPnxfiTpDSIrj/DmZA55NxVeiLSA4iQJesFqBriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi8Q00+S"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAwUGNQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422916,
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
  "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
  "id": -576460752303422916,
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqP4twOilG71Ml+e1cyeszVNJFpXfI4+Q22YSXfqzLMXAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt3LRCbw=",
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
  "id": -576460752303422915,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECOYu2QvDEwsO92BF5/qeEcWx1w2VSBBD6mX3yP6M8BFbfsGibfU9DSmPuZPwdNI+rXUjxQcMpR7nkrHPChcbkFuEj4RjkCoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzFwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dKQDbw"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
  "id": -576460752303422915,
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECOYu2QvDEwsO92BF5/qeEcWx1w2VSBBD6mX3yP6M8BFbfsGibfU9DSmPuZPwdNI+rXUjxQcMpR7nkrHPChcbkFuEj4RjkCoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzFwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dKQDbw",
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
  "id": -576460752303422914,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBczd4g3RKkwQ8PVfn2q4foHwr7Be90SsRaGlkYMPIVkCSze4my6HEIuxH3OzcxHc5wgqRuv7TEftTigpEURioAuECOYu2QvDEwsO92BF5/qeEcWx1w2VSBBD6mX3yP6M8BFbfsGibfU9DSmPuZPwdNI+rXUjxQcMpR7nkrHPChcbkFuEj4RjkCoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzFwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dJ38et"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
  "id": -576460752303422914,
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "state": "tx_+NILAfiEuEBczd4g3RKkwQ8PVfn2q4foHwr7Be90SsRaGlkYMPIVkCSze4my6HEIuxH3OzcxHc5wgqRuv7TEftTigpEURioAuECOYu2QvDEwsO92BF5/qeEcWx1w2VSBBD6mX3yP6M8BFbfsGibfU9DSmPuZPwdNI+rXUjxQcMpR7nkrHPChcbkFuEj4RjkCoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzFwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dJ38et"
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "state": "tx_+NILAfiEuEBczd4g3RKkwQ8PVfn2q4foHwr7Be90SsRaGlkYMPIVkCSze4my6HEIuxH3OzcxHc5wgqRuv7TEftTigpEURioAuECOYu2QvDEwsO92BF5/qeEcWx1w2VSBBD6mX3yP6M8BFbfsGibfU9DSmPuZPwdNI+rXUjxQcMpR7nkrHPChcbkFuEj4RjkCoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzFwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dJ38et"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422913,
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
  "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
  "id": -576460752303422913,
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
  "id": -576460752303422912,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
  "id": -576460752303422912,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBczd4g3RKkwQ8PVfn2q4foHwr7Be90SsRaGlkYMPIVkCSze4my6HEIuxH3OzcxHc5wgqRuv7TEftTigpEURioAuECOYu2QvDEwsO92BF5/qeEcWx1w2VSBBD6mX3yP6M8BFbfsGibfU9DSmPuZPwdNI+rXUjxQcMpR7nkrHPChcbkFuEj4RjkCoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzFwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dJ38et",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBczd4g3RKkwQ8PVfn2q4foHwr7Be90SsRaGlkYMPIVkCSze4my6HEIuxH3OzcxHc5wgqRuv7TEftTigpEURioAuECOYu2QvDEwsO92BF5/qeEcWx1w2VSBBD6mX3yP6M8BFbfsGibfU9DSmPuZPwdNI+rXUjxQcMpR7nkrHPChcbkFuEj4RjkCoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzFwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dJ38et",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBczd4g3RKkwQ8PVfn2q4foHwr7Be90SsRaGlkYMPIVkCSze4my6HEIuxH3OzcxHc5wgqRuv7TEftTigpEURioAuECOYu2QvDEwsO92BF5/qeEcWx1w2VSBBD6mX3yP6M8BFbfsGibfU9DSmPuZPwdNI+rXUjxQcMpR7nkrHPChcbkFuEj4RjkCoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzFwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dJ38et",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
  "id": -576460752303422911,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
  "id": -576460752303422911,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBqP4twOilG71Ml+e1cyeszVNJFpXfI4+Q22YSXfqzLMXoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FbjU+NILAfiEuEBczd4g3RKkwQ8PVfn2q4foHwr7Be90SsRaGlkYMPIVkCSze4my6HEIuxH3OzcxHc5wgqRuv7TEftTigpEURioAuECOYu2QvDEwsO92BF5/qeEcWx1w2VSBBD6mX3yP6M8BFbfsGibfU9DSmPuZPwdNI+rXUjxQcMpR7nkrHPChcbkFuEj4RjkCoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzFwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e5AUz5AUk8AfkBP/kBPKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/kBGPhPoIwQMvdl1B3ZAUDZzuNxddRyHf3p+pDSqNveQcWslAcQ7aA/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/vh0oJrWju+oAdodnhBQlwqDl3iMAspFMq+nLp0wmgzI3QOX+FGAgICAgICgm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfeAgICAoIwQMvdl1B3ZAUDZzuNxddRyHf3p+pDSqNveQcWslAcQgICAgID4T6CbwMWhhIwhv2ZTcDDDCus1HYUa1lQPr69R59bcdfhh9+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgALAwMDAwACGcEiGGw8/MdOJWG0=",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhARqoxx7Yy7oyfq8oybAG8/2z14TU+I9bL/Tv2iMeRfOMtJw3hKW2T6fEjDalA1SXhq76U5/a9uePmcoRGvbTlD7kCd/kCdDcBoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzF6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAXM3eIN0SpMEPD1X59quH6B8K+wXvdErEWhpZGDDyFZAks3uJsuhxCLsR9zs3MR3OcIKkbr+0xH7U4oKRFEYqALhAjmLtkLwxMLDvdgRef6nhHFsdcNlUgQQ+pl98j+jPARW37Bom31PQ0pj7mT8HTSPq11I8UHDKUe55KxzwoXG5BbhI+EY5AqEGo/i3A6KUbvUyX57VzJ6zNU0kWld8jj5DbZhJd+rMsxcCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPPzF7uQbt"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhARqoxx7Yy7oyfq8oybAG8/2z14TU+I9bL/Tv2iMeRfOMtJw3hKW2T6fEjDalA1SXhq76U5/a9uePmcoRGvbTlD7kCd/kCdDcBoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzF6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAXM3eIN0SpMEPD1X59quH6B8K+wXvdErEWhpZGDDyFZAks3uJsuhxCLsR9zs3MR3OcIKkbr+0xH7U4oKRFEYqALhAjmLtkLwxMLDvdgRef6nhHFsdcNlUgQQ+pl98j+jPARW37Bom31PQ0pj7mT8HTSPq11I8UHDKUe55KxzwoXG5BbhI+EY5AqEGo/i3A6KUbvUyX57VzJ6zNU0kWld8jj5DbZhJd+rMsxcCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPPzF7uQbt",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhARqoxx7Yy7oyfq8oybAG8/2z14TU+I9bL/Tv2iMeRfOMtJw3hKW2T6fEjDalA1SXhq76U5/a9uePmcoRGvbTlD7kCd/kCdDcBoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzF6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAXM3eIN0SpMEPD1X59quH6B8K+wXvdErEWhpZGDDyFZAks3uJsuhxCLsR9zs3MR3OcIKkbr+0xH7U4oKRFEYqALhAjmLtkLwxMLDvdgRef6nhHFsdcNlUgQQ+pl98j+jPARW37Bom31PQ0pj7mT8HTSPq11I8UHDKUe55KxzwoXG5BbhI+EY5AqEGo/i3A6KUbvUyX57VzJ6zNU0kWld8jj5DbZhJd+rMsxcCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPPzF7uQbt",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBqP4twOilG71Ml+e1cyeszVNJFpXfI4+Q22YSXfqzLMXoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y/qiUiX/6GJGE5yoACAIYPXtZ/KAAT/YKWdg==",
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
    "signed_tx": "tx_+KcLAfhCuEBVrI4OonHn7jjdilStonDgni3TuUwOdH0KU/ySRe6P/OBOpS3T5i6ueduHPjdBpVla0iftL+TaShBwVdzIy7AJuF/4XTgBoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzF6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygAE/JdCqM="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBVrI4OonHn7jjdilStonDgni3TuUwOdH0KU/ySRe6P/OBOpS3T5i6ueduHPjdBpVla0iftL+TaShBwVdzIy7AJuF/4XTgBoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzF6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygAE/JdCqM=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBVrI4OonHn7jjdilStonDgni3TuUwOdH0KU/ySRe6P/OBOpS3T5i6ueduHPjdBpVla0iftL+TaShBwVdzIy7AJuF/4XTgBoQaj+LcDopRu9TJfntXMnrM1TSRaV3yOPkNtmEl36syzF6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygAE/JdCqM=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
    "channel_id": "ch_2FDS7Yz1EN6xZktVSCnKaKR2docygkfHh24rdWKfyhMexrPuLo",
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
      "fsm_id": "ba_GcWqgIUqnqq2yIO6yiO8722YhQi9bJkSMwmuU4GfFj50/FGY"
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
      "fsm_id": "ba_dYcsWf/5w9YVs8AvxsH7ZUB0DBpzCbtOyJvLwKcko2xJplt/"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYyiJGxNA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422910,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBf5qDNxiFwbjx6m9npSYkNalDKbzvR4VpkrOZVRLbj0fetx6U02qeg8gDs07mza6xXiAMtGnC4Pd6+ODZAVOgIuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2MspAP4k="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422910,
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
      "signed_tx": "tx_+MsLAfhCuEBf5qDNxiFwbjx6m9npSYkNalDKbzvR4VpkrOZVRLbj0fetx6U02qeg8gDs07mza6xXiAMtGnC4Pd6+ODZAVOgIuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2MspAP4k=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422909,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAX+agzcYhcG48epvZ6UmJDWpQym870eFaZKzmVUS249H3rcelNNqnoPIA7NO5s2usV4gDLRpwuD3evjg2QFToCLhA/eF6gvBKtaEZvNRl3sDNcCECIAa0/yAyQXitQ2zVR+KBFzOXB/nnzFnLvezHtEwD0fKWrvTinFnwHLSRBdueAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjJ9qc7K"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422909,
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAX+agzcYhcG48epvZ6UmJDWpQym870eFaZKzmVUS249H3rcelNNqnoPIA7NO5s2usV4gDLRpwuD3evjg2QFToCLhA/eF6gvBKtaEZvNRl3sDNcCECIAa0/yAyQXitQ2zVR+KBFzOXB/nnzFnLvezHtEwD0fKWrvTinFnwHLSRBdueAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjJ9qc7K",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAX+agzcYhcG48epvZ6UmJDWpQym870eFaZKzmVUS249H3rcelNNqnoPIA7NO5s2usV4gDLRpwuD3evjg2QFToCLhA/eF6gvBKtaEZvNRl3sDNcCECIAa0/yAyQXitQ2zVR+KBFzOXB/nnzFnLvezHtEwD0fKWrvTinFnwHLSRBdueAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjJ9qc7K",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAX+agzcYhcG48epvZ6UmJDWpQym870eFaZKzmVUS249H3rcelNNqnoPIA7NO5s2usV4gDLRpwuD3evjg2QFToCLhA/eF6gvBKtaEZvNRl3sDNcCECIAa0/yAyQXitQ2zVR+KBFzOXB/nnzFnLvezHtEwD0fKWrvTinFnwHLSRBdueAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjJ9qc7K",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAX+agzcYhcG48epvZ6UmJDWpQym870eFaZKzmVUS249H3rcelNNqnoPIA7NO5s2usV4gDLRpwuD3evjg2QFToCLhA/eF6gvBKtaEZvNRl3sDNcCECIAa0/yAyQXitQ2zVR+KBFzOXB/nnzFnLvezHtEwD0fKWrvTinFnwHLSRBdueAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjJ9qc7K",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "message": {
        "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "message": {
        "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
  "id": -576460752303422908,
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
  "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
  "id": -576460752303422908,
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "state": "tx_+QENCwH4hLhAX+agzcYhcG48epvZ6UmJDWpQym870eFaZKzmVUS249H3rcelNNqnoPIA7NO5s2usV4gDLRpwuD3evjg2QFToCLhA/eF6gvBKtaEZvNRl3sDNcCECIAa0/yAyQXitQ2zVR+KBFzOXB/nnzFnLvezHtEwD0fKWrvTinFnwHLSRBdueAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjJ9qc7K"
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "state": "tx_+QENCwH4hLhAX+agzcYhcG48epvZ6UmJDWpQym870eFaZKzmVUS249H3rcelNNqnoPIA7NO5s2usV4gDLRpwuD3evjg2QFToCLhA/eF6gvBKtaEZvNRl3sDNcCECIAa0/yAyQXitQ2zVR+KBFzOXB/nnzFnLvezHtEwD0fKWrvTinFnwHLSRBdueAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjJ9qc7K"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAwUGNQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422907,
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
  "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
  "id": -576460752303422907,
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBosc9yaBzFbwspydQWdx7B+4tB/CTZUQcEMrGGaFaV43AqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt+kRRHQ=",
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
  "id": -576460752303422906,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED50bHZmMO+WEJumKUgTSi/f0eWO7xXzojA8YsESXdIeOjtALAcpoJVNhv9Jl/Xv0KW+4CA1ZYOi+7OUJbYuboEuEj4RjkCoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleNwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cAF1T1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
  "id": -576460752303422906,
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "signed_tx": "tx_+JALAfhCuED50bHZmMO+WEJumKUgTSi/f0eWO7xXzojA8YsESXdIeOjtALAcpoJVNhv9Jl/Xv0KW+4CA1ZYOi+7OUJbYuboEuEj4RjkCoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleNwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cAF1T1",
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
  "id": -576460752303422905,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAnVa210viT6pl/DY1toFF1c7/+Y1tI/uUJmLYdMxUA6svM+8Plocn/IYIklA7R9irtHv2qXv7O/M46E6D0JIwPuED50bHZmMO+WEJumKUgTSi/f0eWO7xXzojA8YsESXdIeOjtALAcpoJVNhv9Jl/Xv0KW+4CA1ZYOi+7OUJbYuboEuEj4RjkCoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleNwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cfwEQY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
  "id": -576460752303422905,
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "state": "tx_+NILAfiEuEAnVa210viT6pl/DY1toFF1c7/+Y1tI/uUJmLYdMxUA6svM+8Plocn/IYIklA7R9irtHv2qXv7O/M46E6D0JIwPuED50bHZmMO+WEJumKUgTSi/f0eWO7xXzojA8YsESXdIeOjtALAcpoJVNhv9Jl/Xv0KW+4CA1ZYOi+7OUJbYuboEuEj4RjkCoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleNwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cfwEQY"
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "state": "tx_+NILAfiEuEAnVa210viT6pl/DY1toFF1c7/+Y1tI/uUJmLYdMxUA6svM+8Plocn/IYIklA7R9irtHv2qXv7O/M46E6D0JIwPuED50bHZmMO+WEJumKUgTSi/f0eWO7xXzojA8YsESXdIeOjtALAcpoJVNhv9Jl/Xv0KW+4CA1ZYOi+7OUJbYuboEuEj4RjkCoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleNwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cfwEQY"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422904,
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
  "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
  "id": -576460752303422904,
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
  "id": -576460752303422903,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
  "id": -576460752303422903,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAnVa210viT6pl/DY1toFF1c7/+Y1tI/uUJmLYdMxUA6svM+8Plocn/IYIklA7R9irtHv2qXv7O/M46E6D0JIwPuED50bHZmMO+WEJumKUgTSi/f0eWO7xXzojA8YsESXdIeOjtALAcpoJVNhv9Jl/Xv0KW+4CA1ZYOi+7OUJbYuboEuEj4RjkCoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleNwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cfwEQY",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAnVa210viT6pl/DY1toFF1c7/+Y1tI/uUJmLYdMxUA6svM+8Plocn/IYIklA7R9irtHv2qXv7O/M46E6D0JIwPuED50bHZmMO+WEJumKUgTSi/f0eWO7xXzojA8YsESXdIeOjtALAcpoJVNhv9Jl/Xv0KW+4CA1ZYOi+7OUJbYuboEuEj4RjkCoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleNwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cfwEQY",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAnVa210viT6pl/DY1toFF1c7/+Y1tI/uUJmLYdMxUA6svM+8Plocn/IYIklA7R9irtHv2qXv7O/M46E6D0JIwPuED50bHZmMO+WEJumKUgTSi/f0eWO7xXzojA8YsESXdIeOjtALAcpoJVNhv9Jl/Xv0KW+4CA1ZYOi+7OUJbYuboEuEj4RjkCoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleNwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cfwEQY",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422902,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
  "id": -576460752303422902,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBosc9yaBzFbwspydQWdx7B+4tB/CTZUQcEMrGGaFaV43oQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv7jU+NILAfiEuEAnVa210viT6pl/DY1toFF1c7/+Y1tI/uUJmLYdMxUA6svM+8Plocn/IYIklA7R9irtHv2qXv7O/M46E6D0JIwPuED50bHZmMO+WEJumKUgTSi/f0eWO7xXzojA8YsESXdIeOjtALAcpoJVNhv9Jl/Xv0KW+4CA1ZYOi+7OUJbYuboEuEj4RjkCoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleNwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e5AUz5AUk8AfkBP/kBPKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/kBGPhPoIwQMvdl1B3ZAUDZzuNxddRyHf3p+pDSqNveQcWslAcQ7aA/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/vh0oJrWju+oAdodnhBQlwqDl3iMAspFMq+nLp0wmgzI3QOX+FGAgICAgICgm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfeAgICAoIwQMvdl1B3ZAUDZzuNxddRyHf3p+pDSqNveQcWslAcQgICAgID4T6CbwMWhhIwhv2ZTcDDDCus1HYUa1lQPr69R59bcdfhh9+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgALAwMDAwACGcEiGGw8/FHUxxvA=",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAiueHHfM7nfe6DbzpW2NL2pDRwYbmNK32YDeZbirHBgAT6y9zRqR3MnS6H/Y+Tz9hLe/+4hC3Hke9nBfcONGNAbkCd/kCdDcBoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleN6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhAJ1WttdL4k+qZfw2NbaBRdXO//mNbSP7lCZi2HTMVAOrLzPvD5aHJ/yGCJJQO0fYq7R79ql7+zvzOOhOg9CSMD7hA+dGx2ZjDvlhCbpilIE0ov39Hlju8V86IwPGLBEl3SHjo7QCwHKaCVTYb/SZf179ClvuAgNWWDovuzlCW2Lm6BLhI+EY5AqEGixz3JoHMVvCynJ1BZ3HsH7i0H8JNlRBwQysYZoVpXjcCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPPxSOuFqr"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAiueHHfM7nfe6DbzpW2NL2pDRwYbmNK32YDeZbirHBgAT6y9zRqR3MnS6H/Y+Tz9hLe/+4hC3Hke9nBfcONGNAbkCd/kCdDcBoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleN6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhAJ1WttdL4k+qZfw2NbaBRdXO//mNbSP7lCZi2HTMVAOrLzPvD5aHJ/yGCJJQO0fYq7R79ql7+zvzOOhOg9CSMD7hA+dGx2ZjDvlhCbpilIE0ov39Hlju8V86IwPGLBEl3SHjo7QCwHKaCVTYb/SZf179ClvuAgNWWDovuzlCW2Lm6BLhI+EY5AqEGixz3JoHMVvCynJ1BZ3HsH7i0H8JNlRBwQysYZoVpXjcCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPPxSOuFqr",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAiueHHfM7nfe6DbzpW2NL2pDRwYbmNK32YDeZbirHBgAT6y9zRqR3MnS6H/Y+Tz9hLe/+4hC3Hke9nBfcONGNAbkCd/kCdDcBoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleN6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhAJ1WttdL4k+qZfw2NbaBRdXO//mNbSP7lCZi2HTMVAOrLzPvD5aHJ/yGCJJQO0fYq7R79ql7+zvzOOhOg9CSMD7hA+dGx2ZjDvlhCbpilIE0ov39Hlju8V86IwPGLBEl3SHjo7QCwHKaCVTYb/SZf179ClvuAgNWWDovuzlCW2Lm6BLhI+EY5AqEGixz3JoHMVvCynJ1BZ3HsH7i0H8JNlRBwQysYZoVpXjcCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPPxSOuFqr",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBosc9yaBzFbwspydQWdx7B+4tB/CTZUQcEMrGGaFaV43oQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y/qiUiX/6GJGE5yoACAIYPXtZ/KAAVNp4kFA==",
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
    "signed_tx": "tx_+KcLAfhCuECfnXfvKztdLvythFP1yAoCGgKCwuwwUGzSSB9AwbhThdHCDXYHyEml0q3jxuJjHnA/kn7J2KPS+FoMap848/UIuF/4XTgBoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleN6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygAFS/yodg="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECfnXfvKztdLvythFP1yAoCGgKCwuwwUGzSSB9AwbhThdHCDXYHyEml0q3jxuJjHnA/kn7J2KPS+FoMap848/UIuF/4XTgBoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleN6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygAFS/yodg=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECfnXfvKztdLvythFP1yAoCGgKCwuwwUGzSSB9AwbhThdHCDXYHyEml0q3jxuJjHnA/kn7J2KPS+FoMap848/UIuF/4XTgBoQaLHPcmgcxW8LKcnUFncewfuLQfwk2VEHBDKxhmhWleN6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygAFS/yodg=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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
    "channel_id": "ch_24GTbmQu3rNPNkUptehtC6Abu3eUtWK9CuY8eDswXz1cQNUmTs",
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

#### responder closes WebSocket connection
```

```
