
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3123%5Binitiator44initiator%5D
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
      "fsm_id": "ba_7Nyh/HRazToaBLvby2A/UyGmORXGOSXleMnvT+Mg6p92GwIE"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3123%5Binitiator44initiator%5D
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
      "fsm_id": "ba_s43fBAt5m6dVl7QX0MFjPcgF9jCMZ6g3EpbLj9B7dkiM7PWH"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYQzN3Xzg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423295,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAhRNstiupJjZatPet7Yz9xAiNMbbImNpe3X91mru7XOxLX9GCK4LBZ7EkseTPAS+10gldlI3GJhTdgeeHVjOgCuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2ED+55Yc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423295,
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
      "signed_tx": "tx_+MsLAfhCuEAhRNstiupJjZatPet7Yz9xAiNMbbImNpe3X91mru7XOxLX9GCK4LBZ7EkseTPAS+10gldlI3GJhTdgeeHVjOgCuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2ED+55Yc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423294,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAIUTbLYrqSY2WrT3re2M/cQIjTG2yJjaXt1/dZq7u1zsS1/RgiuCwWexJLHkzwEvtdIJXZSNxiYU3YHnh1YzoArhASCv/o88u7p8duAGYvCN+PlnPjFbjt50rJkhNK0p6VbYfJKi689JAj4TSBkobSntzuQMSab4La8auaZS+4WPMC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhBo2nBL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423294,
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAIUTbLYrqSY2WrT3re2M/cQIjTG2yJjaXt1/dZq7u1zsS1/RgiuCwWexJLHkzwEvtdIJXZSNxiYU3YHnh1YzoArhASCv/o88u7p8duAGYvCN+PlnPjFbjt50rJkhNK0p6VbYfJKi689JAj4TSBkobSntzuQMSab4La8auaZS+4WPMC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhBo2nBL",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAIUTbLYrqSY2WrT3re2M/cQIjTG2yJjaXt1/dZq7u1zsS1/RgiuCwWexJLHkzwEvtdIJXZSNxiYU3YHnh1YzoArhASCv/o88u7p8duAGYvCN+PlnPjFbjt50rJkhNK0p6VbYfJKi689JAj4TSBkobSntzuQMSab4La8auaZS+4WPMC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhBo2nBL",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIUTbLYrqSY2WrT3re2M/cQIjTG2yJjaXt1/dZq7u1zsS1/RgiuCwWexJLHkzwEvtdIJXZSNxiYU3YHnh1YzoArhASCv/o88u7p8duAGYvCN+PlnPjFbjt50rJkhNK0p6VbYfJKi689JAj4TSBkobSntzuQMSab4La8auaZS+4WPMC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhBo2nBL",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIUTbLYrqSY2WrT3re2M/cQIjTG2yJjaXt1/dZq7u1zsS1/RgiuCwWexJLHkzwEvtdIJXZSNxiYU3YHnh1YzoArhASCv/o88u7p8duAGYvCN+PlnPjFbjt50rJkhNK0p6VbYfJKi689JAj4TSBkobSntzuQMSab4La8auaZS+4WPMC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhBo2nBL",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "message": {
        "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "message": {
        "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
  "id": -576460752303423293,
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
  "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
  "id": -576460752303423293,
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "state": "tx_+QENCwH4hLhAIUTbLYrqSY2WrT3re2M/cQIjTG2yJjaXt1/dZq7u1zsS1/RgiuCwWexJLHkzwEvtdIJXZSNxiYU3YHnh1YzoArhASCv/o88u7p8duAGYvCN+PlnPjFbjt50rJkhNK0p6VbYfJKi689JAj4TSBkobSntzuQMSab4La8auaZS+4WPMC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhBo2nBL"
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "state": "tx_+QENCwH4hLhAIUTbLYrqSY2WrT3re2M/cQIjTG2yJjaXt1/dZq7u1zsS1/RgiuCwWexJLHkzwEvtdIJXZSNxiYU3YHnh1YzoArhASCv/o88u7p8duAGYvCN+PlnPjFbjt50rJkhNK0p6VbYfJKi689JAj4TSBkobSntzuQMSab4La8auaZS+4WPMC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhBo2nBL"
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
  "id": -576460752303423292,
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
  "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
  "id": -576460752303423292,
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkMzGIuzTopyENfknqCw6RdjQcNEoy03rNEty4NFCYjvAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt74K+Vw=",
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
  "id": -576460752303423291,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDEdZe2cKf2bkR6VDRsglZYXeDm2SNxKgxCKSGvPpzzfNTiQU9SFlgkjt5Txtl7YDHKWvN5o1oNuijP+JE1JIcHuEj4RjkCoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI7wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eCDkCJ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
  "id": -576460752303423291,
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDEdZe2cKf2bkR6VDRsglZYXeDm2SNxKgxCKSGvPpzzfNTiQU9SFlgkjt5Txtl7YDHKWvN5o1oNuijP+JE1JIcHuEj4RjkCoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI7wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eCDkCJ",
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
  "id": -576460752303423290,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA7hUAjEE95u06ENGJg7eZhFkqq5XizQO+C42mP0L7ZvmDnnZ4gy/7HBIO/gkPwCmti+bqDdataOzr49mXdCHcLuEDEdZe2cKf2bkR6VDRsglZYXeDm2SNxKgxCKSGvPpzzfNTiQU9SFlgkjt5Txtl7YDHKWvN5o1oNuijP+JE1JIcHuEj4RjkCoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI7wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDGVpw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
  "id": -576460752303423290,
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "state": "tx_+NILAfiEuEA7hUAjEE95u06ENGJg7eZhFkqq5XizQO+C42mP0L7ZvmDnnZ4gy/7HBIO/gkPwCmti+bqDdataOzr49mXdCHcLuEDEdZe2cKf2bkR6VDRsglZYXeDm2SNxKgxCKSGvPpzzfNTiQU9SFlgkjt5Txtl7YDHKWvN5o1oNuijP+JE1JIcHuEj4RjkCoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI7wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDGVpw"
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "state": "tx_+NILAfiEuEA7hUAjEE95u06ENGJg7eZhFkqq5XizQO+C42mP0L7ZvmDnnZ4gy/7HBIO/gkPwCmti+bqDdataOzr49mXdCHcLuEDEdZe2cKf2bkR6VDRsglZYXeDm2SNxKgxCKSGvPpzzfNTiQU9SFlgkjt5Txtl7YDHKWvN5o1oNuijP+JE1JIcHuEj4RjkCoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI7wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDGVpw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423289,
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
  "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
  "id": -576460752303423289,
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
  "id": -576460752303423288,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
  "id": -576460752303423288,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA7hUAjEE95u06ENGJg7eZhFkqq5XizQO+C42mP0L7ZvmDnnZ4gy/7HBIO/gkPwCmti+bqDdataOzr49mXdCHcLuEDEdZe2cKf2bkR6VDRsglZYXeDm2SNxKgxCKSGvPpzzfNTiQU9SFlgkjt5Txtl7YDHKWvN5o1oNuijP+JE1JIcHuEj4RjkCoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI7wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDGVpw",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEA7hUAjEE95u06ENGJg7eZhFkqq5XizQO+C42mP0L7ZvmDnnZ4gy/7HBIO/gkPwCmti+bqDdataOzr49mXdCHcLuEDEdZe2cKf2bkR6VDRsglZYXeDm2SNxKgxCKSGvPpzzfNTiQU9SFlgkjt5Txtl7YDHKWvN5o1oNuijP+JE1JIcHuEj4RjkCoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI7wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDGVpw",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEA7hUAjEE95u06ENGJg7eZhFkqq5XizQO+C42mP0L7ZvmDnnZ4gy/7HBIO/gkPwCmti+bqDdataOzr49mXdCHcLuEDEdZe2cKf2bkR6VDRsglZYXeDm2SNxKgxCKSGvPpzzfNTiQU9SFlgkjt5Txtl7YDHKWvN5o1oNuijP+JE1JIcHuEj4RjkCoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI7wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDGVpw",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
  "id": -576460752303423287,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
  "id": -576460752303423287,
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBkMzGIuzTopyENfknqCw6RdjQcNEoy03rNEty4NFCYjvoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FbjU+NILAfiEuEA7hUAjEE95u06ENGJg7eZhFkqq5XizQO+C42mP0L7ZvmDnnZ4gy/7HBIO/gkPwCmti+bqDdataOzr49mXdCHcLuEDEdZe2cKf2bkR6VDRsglZYXeDm2SNxKgxCKSGvPpzzfNTiQU9SFlgkjt5Txtl7YDHKWvN5o1oNuijP+JE1JIcHuEj4RjkCoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI7wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e5AUz5AUk8AfkBP/kBPKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/kBGPhPoIwQMvdl1B3ZAUDZzuNxddRyHf3p+pDSqNveQcWslAcQ7aA/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/vh0oJrWju+oAdodnhBQlwqDl3iMAspFMq+nLp0wmgzI3QOX+FGAgICAgICgm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfeAgICAoIwQMvdl1B3ZAUDZzuNxddRyHf3p+pDSqNveQcWslAcQgICAgID4T6CbwMWhhIwhv2ZTcDDDCus1HYUa1lQPr69R59bcdfhh9+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgALAwMDAwACGGR7ISegAEn2WRL4=",
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
    "signed_tx": "tx_+QLACwH4QrhAQ+aitf3Hn4yuN0G3jOo35uwt2b9XjY8HYXQUFjKqCZM2Lg81ibGz8y6BIlBR+w7pLWgzBfK6+78QGNo47Q2RALkCd/kCdDcBoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI76EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAO4VAIxBPebtOhDRiYO3mYRZKquV4s0DvguNpj9C+2b5g552eIMv+xwSDv4JD8AprYvm6g3WrWjs6+PZl3Qh3C7hAxHWXtnCn9m5EelQ0bIJWWF3g5tkjcSoMQikhrz6c83zU4kFPUhZYJI7eU8bZe2AxylrzeaNaDbooz/iRNSSHB7hI+EY5AqEGQzMYi7NOinIQ1+SeoLDpF2NBw0SjLTes0S3Lg0UJiO8CoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoABJ3x+IU"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAQ+aitf3Hn4yuN0G3jOo35uwt2b9XjY8HYXQUFjKqCZM2Lg81ibGz8y6BIlBR+w7pLWgzBfK6+78QGNo47Q2RALkCd/kCdDcBoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI76EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAO4VAIxBPebtOhDRiYO3mYRZKquV4s0DvguNpj9C+2b5g552eIMv+xwSDv4JD8AprYvm6g3WrWjs6+PZl3Qh3C7hAxHWXtnCn9m5EelQ0bIJWWF3g5tkjcSoMQikhrz6c83zU4kFPUhZYJI7eU8bZe2AxylrzeaNaDbooz/iRNSSHB7hI+EY5AqEGQzMYi7NOinIQ1+SeoLDpF2NBw0SjLTes0S3Lg0UJiO8CoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoABJ3x+IU",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAQ+aitf3Hn4yuN0G3jOo35uwt2b9XjY8HYXQUFjKqCZM2Lg81ibGz8y6BIlBR+w7pLWgzBfK6+78QGNo47Q2RALkCd/kCdDcBoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI76EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAO4VAIxBPebtOhDRiYO3mYRZKquV4s0DvguNpj9C+2b5g552eIMv+xwSDv4JD8AprYvm6g3WrWjs6+PZl3Qh3C7hAxHWXtnCn9m5EelQ0bIJWWF3g5tkjcSoMQikhrz6c83zU4kFPUhZYJI7eU8bZe2AxylrzeaNaDbooz/iRNSSHB7hI+EY5AqEGQzMYi7NOinIQ1+SeoLDpF2NBw0SjLTes0S3Lg0UJiO8CoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoABJ3x+IU",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBkMzGIuzTopyENfknqCw6RdjQcNEoy03rNEty4NFCYjvoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y/qiUiX/6GJGE5yoACAIYPXtZ/KAAGAFSLlA==",
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
    "signed_tx": "tx_+KcLAfhCuEBwMQPSYdczH1PCrscgGt1NLkzP26bhEIRYJZLnaWivPY7I9HgZmM8EAE2aVbg6qT1VJnttyXWx9Ey2EceUIssAuF/4XTgBoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI76EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygABvbbxmw="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBwMQPSYdczH1PCrscgGt1NLkzP26bhEIRYJZLnaWivPY7I9HgZmM8EAE2aVbg6qT1VJnttyXWx9Ey2EceUIssAuF/4XTgBoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI76EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygABvbbxmw=",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBwMQPSYdczH1PCrscgGt1NLkzP26bhEIRYJZLnaWivPY7I9HgZmM8EAE2aVbg6qT1VJnttyXWx9Ey2EceUIssAuF/4XTgBoQZDMxiLs06KchDX5J6gsOkXY0HDRKMtN6zRLcuDRQmI76EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygABvbbxmw=",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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
    "channel_id": "ch_WbXMnMdGxhft74mT1qFk7bv4kTo4UQprpMoaVwwZXDbZEsGCr",
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

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3123%5Binitiator44responder%5D
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
      "fsm_id": "ba_2NoJENvIFSYEW/jsWeqvyle/NjMGUFHwCoUgqHLQgcmph5T8"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3123%5Binitiator44responder%5D
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
      "fsm_id": "ba_fyM8wCC6/3OVzvJuuuel/BcfeB6d2Fvw2vvS/ZZ/8Wr3P2ec"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYTf/wBbQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423286,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDiWVZQtr9FqamsQIhO61Lw1SgYX7EjiiYr33ZCikqWxJaqcmg1NeKd7NBvbxv7vqe3uLJ5TNMlEW7ew6ncJTAJuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2E1ZLqSk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423286,
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
      "signed_tx": "tx_+MsLAfhCuEDiWVZQtr9FqamsQIhO61Lw1SgYX7EjiiYr33ZCikqWxJaqcmg1NeKd7NBvbxv7vqe3uLJ5TNMlEW7ew6ncJTAJuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2E1ZLqSk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423285,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAv0qsx8j93yQDPJiWhIcpVoY0JQYfbeDILeND8IWtQ01nCjDF1YQluFm/BUL6RhoiwcuDqUT9Fa+h2gH8cpt7CbhA4llWULa/RamprECITutS8NUoGF+xI4omK992QopKlsSWqnJoNTXinezQb28b+76nt7iyeUzTJRFu3sOp3CUwCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhNhN5iW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423285,
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAv0qsx8j93yQDPJiWhIcpVoY0JQYfbeDILeND8IWtQ01nCjDF1YQluFm/BUL6RhoiwcuDqUT9Fa+h2gH8cpt7CbhA4llWULa/RamprECITutS8NUoGF+xI4omK992QopKlsSWqnJoNTXinezQb28b+76nt7iyeUzTJRFu3sOp3CUwCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhNhN5iW",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAv0qsx8j93yQDPJiWhIcpVoY0JQYfbeDILeND8IWtQ01nCjDF1YQluFm/BUL6RhoiwcuDqUT9Fa+h2gH8cpt7CbhA4llWULa/RamprECITutS8NUoGF+xI4omK992QopKlsSWqnJoNTXinezQb28b+76nt7iyeUzTJRFu3sOp3CUwCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhNhN5iW",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAv0qsx8j93yQDPJiWhIcpVoY0JQYfbeDILeND8IWtQ01nCjDF1YQluFm/BUL6RhoiwcuDqUT9Fa+h2gH8cpt7CbhA4llWULa/RamprECITutS8NUoGF+xI4omK992QopKlsSWqnJoNTXinezQb28b+76nt7iyeUzTJRFu3sOp3CUwCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhNhN5iW",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAv0qsx8j93yQDPJiWhIcpVoY0JQYfbeDILeND8IWtQ01nCjDF1YQluFm/BUL6RhoiwcuDqUT9Fa+h2gH8cpt7CbhA4llWULa/RamprECITutS8NUoGF+xI4omK992QopKlsSWqnJoNTXinezQb28b+76nt7iyeUzTJRFu3sOp3CUwCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhNhN5iW",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "message": {
        "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "message": {
        "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
  "id": -576460752303423284,
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
  "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
  "id": -576460752303423284,
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "event": "open"
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "state": "tx_+QENCwH4hLhAv0qsx8j93yQDPJiWhIcpVoY0JQYfbeDILeND8IWtQ01nCjDF1YQluFm/BUL6RhoiwcuDqUT9Fa+h2gH8cpt7CbhA4llWULa/RamprECITutS8NUoGF+xI4omK992QopKlsSWqnJoNTXinezQb28b+76nt7iyeUzTJRFu3sOp3CUwCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhNhN5iW"
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "state": "tx_+QENCwH4hLhAv0qsx8j93yQDPJiWhIcpVoY0JQYfbeDILeND8IWtQ01nCjDF1YQluFm/BUL6RhoiwcuDqUT9Fa+h2gH8cpt7CbhA4llWULa/RamprECITutS8NUoGF+xI4omK992QopKlsSWqnJoNTXinezQb28b+76nt7iyeUzTJRFu3sOp3CUwCbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhNhN5iW"
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
  "id": -576460752303423283,
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
  "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
  "id": -576460752303423283,
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhRXOf/X+7dGwAaE4zp3Ku+5YnO/pGhEKycrMhzp+iTjAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt5nls2w=",
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
  "id": -576460752303423282,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECkBrTr3UhZe+mxZGZ6qxo+5D3IYipNSCDCR2eUeARtBKrfi7F6iMOz3ecFNtGmNv8chsv9IxsnBAWTYgaQfQ4AuEj4RjkCoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok4wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e36mM5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
  "id": -576460752303423282,
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "signed_tx": "tx_+JALAfhCuECkBrTr3UhZe+mxZGZ6qxo+5D3IYipNSCDCR2eUeARtBKrfi7F6iMOz3ecFNtGmNv8chsv9IxsnBAWTYgaQfQ4AuEj4RjkCoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok4wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e36mM5",
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
  "id": -576460752303423281,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECkBrTr3UhZe+mxZGZ6qxo+5D3IYipNSCDCR2eUeARtBKrfi7F6iMOz3ecFNtGmNv8chsv9IxsnBAWTYgaQfQ4AuED4ukUve6tfLTV5ea0f5EuuvqmknjQZZ07UWpopBvxPez6r7/DRH4ZvaThuvkVTwMWoiF4lfx4+twtOtrVgfEEBuEj4RjkCoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok4wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cnYqR4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
  "id": -576460752303423281,
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "state": "tx_+NILAfiEuECkBrTr3UhZe+mxZGZ6qxo+5D3IYipNSCDCR2eUeARtBKrfi7F6iMOz3ecFNtGmNv8chsv9IxsnBAWTYgaQfQ4AuED4ukUve6tfLTV5ea0f5EuuvqmknjQZZ07UWpopBvxPez6r7/DRH4ZvaThuvkVTwMWoiF4lfx4+twtOtrVgfEEBuEj4RjkCoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok4wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cnYqR4"
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "state": "tx_+NILAfiEuECkBrTr3UhZe+mxZGZ6qxo+5D3IYipNSCDCR2eUeARtBKrfi7F6iMOz3ecFNtGmNv8chsv9IxsnBAWTYgaQfQ4AuED4ukUve6tfLTV5ea0f5EuuvqmknjQZZ07UWpopBvxPez6r7/DRH4ZvaThuvkVTwMWoiF4lfx4+twtOtrVgfEEBuEj4RjkCoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok4wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cnYqR4"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423280,
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
  "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
  "id": -576460752303423280,
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
  "id": -576460752303423279,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
  "id": -576460752303423279,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECkBrTr3UhZe+mxZGZ6qxo+5D3IYipNSCDCR2eUeARtBKrfi7F6iMOz3ecFNtGmNv8chsv9IxsnBAWTYgaQfQ4AuED4ukUve6tfLTV5ea0f5EuuvqmknjQZZ07UWpopBvxPez6r7/DRH4ZvaThuvkVTwMWoiF4lfx4+twtOtrVgfEEBuEj4RjkCoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok4wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cnYqR4",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECkBrTr3UhZe+mxZGZ6qxo+5D3IYipNSCDCR2eUeARtBKrfi7F6iMOz3ecFNtGmNv8chsv9IxsnBAWTYgaQfQ4AuED4ukUve6tfLTV5ea0f5EuuvqmknjQZZ07UWpopBvxPez6r7/DRH4ZvaThuvkVTwMWoiF4lfx4+twtOtrVgfEEBuEj4RjkCoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok4wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cnYqR4",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECkBrTr3UhZe+mxZGZ6qxo+5D3IYipNSCDCR2eUeARtBKrfi7F6iMOz3ecFNtGmNv8chsv9IxsnBAWTYgaQfQ4AuED4ukUve6tfLTV5ea0f5EuuvqmknjQZZ07UWpopBvxPez6r7/DRH4ZvaThuvkVTwMWoiF4lfx4+twtOtrVgfEEBuEj4RjkCoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok4wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cnYqR4",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
  "id": -576460752303423278,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
  "id": -576460752303423278,
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBhRXOf/X+7dGwAaE4zp3Ku+5YnO/pGhEKycrMhzp+iTjoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv7jU+NILAfiEuECkBrTr3UhZe+mxZGZ6qxo+5D3IYipNSCDCR2eUeARtBKrfi7F6iMOz3ecFNtGmNv8chsv9IxsnBAWTYgaQfQ4AuED4ukUve6tfLTV5ea0f5EuuvqmknjQZZ07UWpopBvxPez6r7/DRH4ZvaThuvkVTwMWoiF4lfx4+twtOtrVgfEEBuEj4RjkCoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok4wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e5AUz5AUk8AfkBP/kBPKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/kBGPhPoIwQMvdl1B3ZAUDZzuNxddRyHf3p+pDSqNveQcWslAcQ7aA/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/vh0oJrWju+oAdodnhBQlwqDl3iMAspFMq+nLp0wmgzI3QOX+FGAgICAgICgm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfeAgICAoIwQMvdl1B3ZAUDZzuNxddRyHf3p+pDSqNveQcWslAcQgICAgID4T6CbwMWhhIwhv2ZTcDDDCus1HYUa1lQPr69R59bcdfhh9+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgALAwMDAwACGGR7ISegABwoVPHw=",
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
    "signed_tx": "tx_+QLACwH4QrhAA0ni414mCfj5eAmnMdvcLgThUeRRzlPgEfiJ56VDN82mcmyrtz7cddh34dPvMm5D9NvLjdZSlPHUT6DmxAb3ALkCd/kCdDcBoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok46EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhApAa0691IWXvpsWRmeqsaPuQ9yGIqTUggwkdnlHgEbQSq34uxeojDs93nBTbRpjb/HIbL/SMbJwQFk2IGkH0OALhA+LpFL3urXy01eXmtH+RLrr6ppJ40GWdO1FqaKQb8T3s+q+/w0R+Gb2k4br5FU8DFqIheJX8ePrcLTra1YHxBAbhI+EY5AqEGFFc5/9f7t0bABoTjOncq77lic7+kaEQrJysyHOn6JOMCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoAAd9caBm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAA0ni414mCfj5eAmnMdvcLgThUeRRzlPgEfiJ56VDN82mcmyrtz7cddh34dPvMm5D9NvLjdZSlPHUT6DmxAb3ALkCd/kCdDcBoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok46EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhApAa0691IWXvpsWRmeqsaPuQ9yGIqTUggwkdnlHgEbQSq34uxeojDs93nBTbRpjb/HIbL/SMbJwQFk2IGkH0OALhA+LpFL3urXy01eXmtH+RLrr6ppJ40GWdO1FqaKQb8T3s+q+/w0R+Gb2k4br5FU8DFqIheJX8ePrcLTra1YHxBAbhI+EY5AqEGFFc5/9f7t0bABoTjOncq77lic7+kaEQrJysyHOn6JOMCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoAAd9caBm",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAA0ni414mCfj5eAmnMdvcLgThUeRRzlPgEfiJ56VDN82mcmyrtz7cddh34dPvMm5D9NvLjdZSlPHUT6DmxAb3ALkCd/kCdDcBoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok46EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhApAa0691IWXvpsWRmeqsaPuQ9yGIqTUggwkdnlHgEbQSq34uxeojDs93nBTbRpjb/HIbL/SMbJwQFk2IGkH0OALhA+LpFL3urXy01eXmtH+RLrr6ppJ40GWdO1FqaKQb8T3s+q+/w0R+Gb2k4br5FU8DFqIheJX8ePrcLTra1YHxBAbhI+EY5AqEGFFc5/9f7t0bABoTjOncq77lic7+kaEQrJysyHOn6JOMCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3uQFM+QFJPAH5AT/5ATygmtaO76gB2h2eEFCXCoOXeIwCykUyr6cunTCaDMjdA5f5ARj4T6CMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX/74dKCa1o7vqAHaHZ4QUJcKg5d4jALKRTKvpy6dMJoMyN0Dl/hRgICAgICAoJvAxaGEjCG/ZlNwMMMK6zUdhRrWVA+vr1Hn1tx1+GH3gICAgKCMEDL3ZdQd2QFA2c7jcXXUch396fqQ0qjb3kHFrJQHEICAgICA+E+gm8DFoYSMIb9mU3AwwwrrNR2FGtZUD6+vUefW3HX4YfftoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoACwMDAwMAAhhkeyEnoAAd9caBm",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBhRXOf/X+7dGwAaE4zp3Ku+5YnO/pGhEKycrMhzp+iTjoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y/qiUiX/6GJGE5yoACAIYPXtZ/KAAI3JdJ2w==",
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
    "signed_tx": "tx_+KcLAfhCuEBUnyMf+TJCbSwFkJRlHoxte6GInqthxGD01puI9Z/ob3Xxa8QL55ZyaciuMVY/M8m5nVuCqFOKPMWh0eKRZFIEuF/4XTgBoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok46EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygACCDK7gY="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBUnyMf+TJCbSwFkJRlHoxte6GInqthxGD01puI9Z/ob3Xxa8QL55ZyaciuMVY/M8m5nVuCqFOKPMWh0eKRZFIEuF/4XTgBoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok46EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygACCDK7gY=",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBUnyMf+TJCbSwFkJRlHoxte6GInqthxGD01puI9Z/ob3Xxa8QL55ZyaciuMVY/M8m5nVuCqFOKPMWh0eKRZFIEuF/4XTgBoQYUVzn/1/u3RsAGhOM6dyrvuWJzv6RoRCsnKzIc6fok46EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl/+hiRhOcqAAgCGD17WfygACCDK7gY=",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
    "channel_id": "ch_9xaSjfDvKWqiA4cyv9KCsQVjRy1wjPYSQ2jiMKLgJ5XhHDC4e",
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
