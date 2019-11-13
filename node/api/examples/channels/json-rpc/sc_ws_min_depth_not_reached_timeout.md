
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&minimum_depth=1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_min_depth_not_reached_timeout_%2F2638&timeout_funding_lock=3000
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
      "fsm_id": "ba_LfpfsEbZu7ZarU3VoyqZtNh9hDEat9F0YdMn6md6lnxI+3+8"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&minimum_depth=1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_min_depth_not_reached_timeout_%2F2638&timeout_funding_lock=3000
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
      "fsm_id": "ba_GIU4ISrez6A7Ro7/ZLYogONHgEZ0iccR4raKsbZFsfwXqhwr"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYBXsEXQA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423488,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA/Z8Pyko2aK8afwXzl1OeULladEDTS6uBp5SFD8ch115+tsoL/A5Hlwkb/NDgsCzC0h+P5anGLciiP8AESoh8GuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AdgmgN0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423488,
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
      "signed_tx": "tx_+MsLAfhCuEA/Z8Pyko2aK8afwXzl1OeULladEDTS6uBp5SFD8ch115+tsoL/A5Hlwkb/NDgsCzC0h+P5anGLciiP8AESoh8GuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AdgmgN0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423487,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAP2fD8pKNmivGn8F85dTnlC5WnRA00urgaeUhQ/HIddefrbKC/wOR5cJG/zQ4LAswtIfj+Wpxi3Ioj/ABEqIfBrhAepj/7BgFYTiMDZsTL1h1+jvD/+LncbmWGBen4RmrJ3rOpmy+N1jwnaqTfR6zfdf/qgEwLFBU8kR5uMIPrXwdB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgHF/3+g"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423487,
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
    "channel_id": "ch_2oDaXHCm451T3ZCamVvupyyaayZhAqqA2cuXEkY7xGwX3YmHpi",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAP2fD8pKNmivGn8F85dTnlC5WnRA00urgaeUhQ/HIddefrbKC/wOR5cJG/zQ4LAswtIfj+Wpxi3Ioj/ABEqIfBrhAepj/7BgFYTiMDZsTL1h1+jvD/+LncbmWGBen4RmrJ3rOpmy+N1jwnaqTfR6zfdf/qgEwLFBU8kR5uMIPrXwdB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgHF/3+g",
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
    "channel_id": "ch_2oDaXHCm451T3ZCamVvupyyaayZhAqqA2cuXEkY7xGwX3YmHpi",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAP2fD8pKNmivGn8F85dTnlC5WnRA00urgaeUhQ/HIddefrbKC/wOR5cJG/zQ4LAswtIfj+Wpxi3Ioj/ABEqIfBrhAepj/7BgFYTiMDZsTL1h1+jvD/+LncbmWGBen4RmrJ3rOpmy+N1jwnaqTfR6zfdf/qgEwLFBU8kR5uMIPrXwdB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgHF/3+g",
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
    "channel_id": "ch_2oDaXHCm451T3ZCamVvupyyaayZhAqqA2cuXEkY7xGwX3YmHpi",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAP2fD8pKNmivGn8F85dTnlC5WnRA00urgaeUhQ/HIddefrbKC/wOR5cJG/zQ4LAswtIfj+Wpxi3Ioj/ABEqIfBrhAepj/7BgFYTiMDZsTL1h1+jvD/+LncbmWGBen4RmrJ3rOpmy+N1jwnaqTfR6zfdf/qgEwLFBU8kR5uMIPrXwdB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgHF/3+g",
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
    "channel_id": "ch_2oDaXHCm451T3ZCamVvupyyaayZhAqqA2cuXEkY7xGwX3YmHpi",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAP2fD8pKNmivGn8F85dTnlC5WnRA00urgaeUhQ/HIddefrbKC/wOR5cJG/zQ4LAswtIfj+Wpxi3Ioj/ABEqIfBrhAepj/7BgFYTiMDZsTL1h1+jvD/+LncbmWGBen4RmrJ3rOpmy+N1jwnaqTfR6zfdf/qgEwLFBU8kR5uMIPrXwdB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgHF/3+g",
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
    "channel_id": "ch_2oDaXHCm451T3ZCamVvupyyaayZhAqqA2cuXEkY7xGwX3YmHpi",
    "data": {
      "event": "timeout"
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
    "channel_id": "ch_2oDaXHCm451T3ZCamVvupyyaayZhAqqA2cuXEkY7xGwX3YmHpi",
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
    "channel_id": "ch_2oDaXHCm451T3ZCamVvupyyaayZhAqqA2cuXEkY7xGwX3YmHpi",
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
