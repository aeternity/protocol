
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
      "fsm_id": "ba_1pr6WQyVVzO0Z4B4RNzNU8vt5gRcbR/m/CLvYAtCHDWomGEt"
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
      "fsm_id": "ba_x2ySvQcV37ujncudRUaUBYlXWLcLzYEdWLRacWQg2rJdJVax"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYG7onxPA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423391,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAg09zOFAfjVXD2+/d1R7nn3VDyDoJ+fHdDiicrLRIeNxnLu8gXE3+SwgcRkPWtKdE0mCafHyKoOqM2cnsX9bsCuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2BmVBu4E="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423391,
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
      "signed_tx": "tx_+MsLAfhCuEAg09zOFAfjVXD2+/d1R7nn3VDyDoJ+fHdDiicrLRIeNxnLu8gXE3+SwgcRkPWtKdE0mCafHyKoOqM2cnsX9bsCuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2BmVBu4E=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423390,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAINPczhQH41Vw9vv3dUe5591Q8g6Cfnx3Q4onKy0SHjcZy7vIFxN/ksIHEZD1rSnRNJgmnx8iqDqjNnJ7F/W7ArhA30mBpIWCAEaga8WQQLJBdF+BtaAWxTN3U2NRiu/aeWmGGfz4FS8n8MBp8rFpz0ssURuB88cd7/FgD5wIL3EGC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgbpZ2uz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423390,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAINPczhQH41Vw9vv3dUe5591Q8g6Cfnx3Q4onKy0SHjcZy7vIFxN/ksIHEZD1rSnRNJgmnx8iqDqjNnJ7F/W7ArhA30mBpIWCAEaga8WQQLJBdF+BtaAWxTN3U2NRiu/aeWmGGfz4FS8n8MBp8rFpz0ssURuB88cd7/FgD5wIL3EGC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgbpZ2uz",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAINPczhQH41Vw9vv3dUe5591Q8g6Cfnx3Q4onKy0SHjcZy7vIFxN/ksIHEZD1rSnRNJgmnx8iqDqjNnJ7F/W7ArhA30mBpIWCAEaga8WQQLJBdF+BtaAWxTN3U2NRiu/aeWmGGfz4FS8n8MBp8rFpz0ssURuB88cd7/FgD5wIL3EGC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgbpZ2uz",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAINPczhQH41Vw9vv3dUe5591Q8g6Cfnx3Q4onKy0SHjcZy7vIFxN/ksIHEZD1rSnRNJgmnx8iqDqjNnJ7F/W7ArhA30mBpIWCAEaga8WQQLJBdF+BtaAWxTN3U2NRiu/aeWmGGfz4FS8n8MBp8rFpz0ssURuB88cd7/FgD5wIL3EGC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgbpZ2uz",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAINPczhQH41Vw9vv3dUe5591Q8g6Cfnx3Q4onKy0SHjcZy7vIFxN/ksIHEZD1rSnRNJgmnx8iqDqjNnJ7F/W7ArhA30mBpIWCAEaga8WQQLJBdF+BtaAWxTN3U2NRiu/aeWmGGfz4FS8n8MBp8rFpz0ssURuB88cd7/FgD5wIL3EGC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgbpZ2uz",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "message": {
        "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "message": {
        "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
  "id": -576460752303423389,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423389,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+QENCwH4hLhAINPczhQH41Vw9vv3dUe5591Q8g6Cfnx3Q4onKy0SHjcZy7vIFxN/ksIHEZD1rSnRNJgmnx8iqDqjNnJ7F/W7ArhA30mBpIWCAEaga8WQQLJBdF+BtaAWxTN3U2NRiu/aeWmGGfz4FS8n8MBp8rFpz0ssURuB88cd7/FgD5wIL3EGC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgbpZ2uz"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+QENCwH4hLhAINPczhQH41Vw9vv3dUe5591Q8g6Cfnx3Q4onKy0SHjcZy7vIFxN/ksIHEZD1rSnRNJgmnx8iqDqjNnJ7F/W7ArhA30mBpIWCAEaga8WQQLJBdF+BtaAWxTN3U2NRiu/aeWmGGfz4FS8n8MBp8rFpz0ssURuB88cd7/FgD5wIL3EGC7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgbpZ2uz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423388,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "error": {
    "code": 2,
    "data": [
      {
        "code": 1012,
        "message": "Offchain tx expected"
      }
    ],
    "message": "Action not allowed",
    "request": {
      "id": -576460752303423388,
      "jsonrpc": "2.0",
      "method": "channels.snapshot_solo",
      "params": {}
    }
  },
  "id": -576460752303423388,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423387,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423387,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2AqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrtxV+sp8=",
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
  "id": -576460752303423386,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECRQ18ECiCwdzfl2VznVqBS+65Js1ZRfFv+/hFt5GQihN/ei0p6HAwDICiFrv0bWMyOl7BQeHLJ7hm39ttJZ+4AuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7deh0n5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423386,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuECRQ18ECiCwdzfl2VznVqBS+65Js1ZRfFv+/hFt5GQihN/ei0p6HAwDICiFrv0bWMyOl7BQeHLJ7hm39ttJZ+4AuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7deh0n5",
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
  "id": -576460752303423385,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECRQ18ECiCwdzfl2VznVqBS+65Js1ZRfFv+/hFt5GQihN/ei0p6HAwDICiFrv0bWMyOl7BQeHLJ7hm39ttJZ+4AuEDKuMPtwWDQ/+KFegMy1F7canePXrQvXC7tI4J76oeitdyx38MbNKR3Hu5PW/bKhI7JAyay9cQ9XORM/qcYiD0AuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dUjSir"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423385,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuECRQ18ECiCwdzfl2VznVqBS+65Js1ZRfFv+/hFt5GQihN/ei0p6HAwDICiFrv0bWMyOl7BQeHLJ7hm39ttJZ+4AuEDKuMPtwWDQ/+KFegMy1F7canePXrQvXC7tI4J76oeitdyx38MbNKR3Hu5PW/bKhI7JAyay9cQ9XORM/qcYiD0AuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dUjSir"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuECRQ18ECiCwdzfl2VznVqBS+65Js1ZRfFv+/hFt5GQihN/ei0p6HAwDICiFrv0bWMyOl7BQeHLJ7hm39ttJZ+4AuEDKuMPtwWDQ/+KFegMy1F7canePXrQvXC7tI4J76oeitdyx38MbNKR3Hu5PW/bKhI7JAyay9cQ9XORM/qcYiD0AuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dUjSir"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423384,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423384,
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
  "id": -576460752303423383,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423383,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECRQ18ECiCwdzfl2VznVqBS+65Js1ZRfFv+/hFt5GQihN/ei0p6HAwDICiFrv0bWMyOl7BQeHLJ7hm39ttJZ+4AuEDKuMPtwWDQ/+KFegMy1F7canePXrQvXC7tI4J76oeitdyx38MbNKR3Hu5PW/bKhI7JAyay9cQ9XORM/qcYiD0AuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dUjSir",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423382,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423382,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2A6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiilEQg=",
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
  "id": -576460752303423381,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEADSW4p0u6ebBNYluhJyg8/XsJfAx0Tc8ZFZoyPqtA5gweBucAhxrr7g52t03ezsRGv+x8HE8ocufdTUMn5b+kCuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY0MekN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423381,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEADSW4p0u6ebBNYluhJyg8/XsJfAx0Tc8ZFZoyPqtA5gweBucAhxrr7g52t03ezsRGv+x8HE8ocufdTUMn5b+kCuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY0MekN",
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
  "id": -576460752303423380,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEADSW4p0u6ebBNYluhJyg8/XsJfAx0Tc8ZFZoyPqtA5gweBucAhxrr7g52t03ezsRGv+x8HE8ocufdTUMn5b+kCuECg4Zb+sX5wj9+6kqTjb7qdVOS0DIeitYydZEkd2w93I+JBbnE4JryFqXPqQSzaQ/lznBqDaGvnWEkA4eKSebcMuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbCgeQw"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423380,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEADSW4p0u6ebBNYluhJyg8/XsJfAx0Tc8ZFZoyPqtA5gweBucAhxrr7g52t03ezsRGv+x8HE8ocufdTUMn5b+kCuECg4Zb+sX5wj9+6kqTjb7qdVOS0DIeitYydZEkd2w93I+JBbnE4JryFqXPqQSzaQ/lznBqDaGvnWEkA4eKSebcMuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbCgeQw"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEADSW4p0u6ebBNYluhJyg8/XsJfAx0Tc8ZFZoyPqtA5gweBucAhxrr7g52t03ezsRGv+x8HE8ocufdTUMn5b+kCuECg4Zb+sX5wj9+6kqTjb7qdVOS0DIeitYydZEkd2w93I+JBbnE4JryFqXPqQSzaQ/lznBqDaGvnWEkA4eKSebcMuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbCgeQw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423379,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423379,
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
  "id": -576460752303423378,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423378,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEADSW4p0u6ebBNYluhJyg8/XsJfAx0Tc8ZFZoyPqtA5gweBucAhxrr7g52t03ezsRGv+x8HE8ocufdTUMn5b+kCuECg4Zb+sX5wj9+6kqTjb7qdVOS0DIeitYydZEkd2w93I+JBbnE4JryFqXPqQSzaQ/lznBqDaGvnWEkA4eKSebcMuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbCgeQw",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423377,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423377,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2oQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FbjU+NILAfiEuEADSW4p0u6ebBNYluhJyg8/XsJfAx0Tc8ZFZoyPqtA5gweBucAhxrr7g52t03ezsRGv+x8HE8ocufdTUMn5b+kCuECg4Zb+sX5wj9+6kqTjb7qdVOS0DIeitYydZEkd2w93I+JBbnE4JryFqXPqQSzaQ/lznBqDaGvnWEkA4eKSebcMuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYAhhMG0SswAAfunm3m",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhA2E5SVsAjCJyc2Q1jpNJ4Sy9q8Lvq8/TauyzXKTfgyfRIU8Tvi3ZWgaKuQI+l3f/n7+iJO0lM0j9i4kha3NhtCrkBKPkBJTsBoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9qEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAA0luKdLunmwTWJboScoPP17CXwMdE3PGRWaMj6rQOYMHgbnAIca6+4OdrdN3s7ERr/sfBxPKHLn3U1DJ+W/pArhAoOGW/rF+cI/fupKk42+6nVTktAyHorWMnWRJHdsPdyPiQW5xOCa8halz6kEs2kP5c5wag2hr51hJAOHiknm3DLhI+EY5AqEGb4Kuo2YLwfOQcb1Ijbc+UzDniA54xOk70Di/4HEVRPYDoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIYTBtErMAAHaLkBqQ=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423376,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423376,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2BKBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt93kdAk=",
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
  "id": -576460752303423375,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAQyEm1ZrQ+yHTK8PG3o1RNbtnYqtatQl11diYJEhD6V/0shgoszp8DP1mPm6J9Ql+VEo/udTML6+YyPUf+0TcOuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7evq8PT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423375,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAQyEm1ZrQ+yHTK8PG3o1RNbtnYqtatQl11diYJEhD6V/0shgoszp8DP1mPm6J9Ql+VEo/udTML6+YyPUf+0TcOuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7evq8PT",
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
  "id": -576460752303423374,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAQyEm1ZrQ+yHTK8PG3o1RNbtnYqtatQl11diYJEhD6V/0shgoszp8DP1mPm6J9Ql+VEo/udTML6+YyPUf+0TcOuECeQmwMm/+83ngi6Fn3MAeykujti3pg+nzWuUx43kUgBL0VgapXa6DOqhDydZO9VuvmSNsrBUbtelV0b/bOzMgGuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fIzv7M"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423374,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEAQyEm1ZrQ+yHTK8PG3o1RNbtnYqtatQl11diYJEhD6V/0shgoszp8DP1mPm6J9Ql+VEo/udTML6+YyPUf+0TcOuECeQmwMm/+83ngi6Fn3MAeykujti3pg+nzWuUx43kUgBL0VgapXa6DOqhDydZO9VuvmSNsrBUbtelV0b/bOzMgGuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fIzv7M"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEAQyEm1ZrQ+yHTK8PG3o1RNbtnYqtatQl11diYJEhD6V/0shgoszp8DP1mPm6J9Ql+VEo/udTML6+YyPUf+0TcOuECeQmwMm/+83ngi6Fn3MAeykujti3pg+nzWuUx43kUgBL0VgapXa6DOqhDydZO9VuvmSNsrBUbtelV0b/bOzMgGuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fIzv7M"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423373,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423373,
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
  "id": -576460752303423372,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423372,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAQyEm1ZrQ+yHTK8PG3o1RNbtnYqtatQl11diYJEhD6V/0shgoszp8DP1mPm6J9Ql+VEo/udTML6+YyPUf+0TcOuECeQmwMm/+83ngi6Fn3MAeykujti3pg+nzWuUx43kUgBL0VgapXa6DOqhDydZO9VuvmSNsrBUbtelV0b/bOzMgGuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fIzv7M",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423371,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423371,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2BaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjXEJwk=",
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
  "id": -576460752303423370,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAXlH/LQUp0Ia7LsHIs13EOOtc7nG0YY6Fh0l4myP0D93nKESFXqj0JsQdsAaUGo9JLpVuALvbH2ERPdjj2Kf4CuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbcwMJ5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423370,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAXlH/LQUp0Ia7LsHIs13EOOtc7nG0YY6Fh0l4myP0D93nKESFXqj0JsQdsAaUGo9JLpVuALvbH2ERPdjj2Kf4CuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbcwMJ5",
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
  "id": -576460752303423369,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAXlH/LQUp0Ia7LsHIs13EOOtc7nG0YY6Fh0l4myP0D93nKESFXqj0JsQdsAaUGo9JLpVuALvbH2ERPdjj2Kf4CuEBfYa+bszk/aZbA1swjAn0KhDyR4xJDnEYv7stovELcZu8+afXaaIYaBgr/Z05QkHr49ntRYffBsCZpJS9tVaEJuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna6MUQJ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423369,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEAXlH/LQUp0Ia7LsHIs13EOOtc7nG0YY6Fh0l4myP0D93nKESFXqj0JsQdsAaUGo9JLpVuALvbH2ERPdjj2Kf4CuEBfYa+bszk/aZbA1swjAn0KhDyR4xJDnEYv7stovELcZu8+afXaaIYaBgr/Z05QkHr49ntRYffBsCZpJS9tVaEJuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna6MUQJ"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEAXlH/LQUp0Ia7LsHIs13EOOtc7nG0YY6Fh0l4myP0D93nKESFXqj0JsQdsAaUGo9JLpVuALvbH2ERPdjj2Kf4CuEBfYa+bszk/aZbA1swjAn0KhDyR4xJDnEYv7stovELcZu8+afXaaIYaBgr/Z05QkHr49ntRYffBsCZpJS9tVaEJuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna6MUQJ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423368,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423368,
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
  "id": -576460752303423367,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423367,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAXlH/LQUp0Ia7LsHIs13EOOtc7nG0YY6Fh0l4myP0D93nKESFXqj0JsQdsAaUGo9JLpVuALvbH2ERPdjj2Kf4CuEBfYa+bszk/aZbA1swjAn0KhDyR4xJDnEYv7stovELcZu8+afXaaIYaBgr/Z05QkHr49ntRYffBsCZpJS9tVaEJuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna6MUQJ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA2E5SVsAjCJyc2Q1jpNJ4Sy9q8Lvq8/TauyzXKTfgyfRIU8Tvi3ZWgaKuQI+l3f/n7+iJO0lM0j9i4kha3NhtCrkBKPkBJTsBoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9qEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAA0luKdLunmwTWJboScoPP17CXwMdE3PGRWaMj6rQOYMHgbnAIca6+4OdrdN3s7ERr/sfBxPKHLn3U1DJ+W/pArhAoOGW/rF+cI/fupKk42+6nVTktAyHorWMnWRJHdsPdyPiQW5xOCa8halz6kEs2kP5c5wag2hr51hJAOHiknm3DLhI+EY5AqEGb4Kuo2YLwfOQcb1Ijbc+UzDniA54xOk70Di/4HEVRPYDoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIYTBtErMAAHaLkBqQ==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA2E5SVsAjCJyc2Q1jpNJ4Sy9q8Lvq8/TauyzXKTfgyfRIU8Tvi3ZWgaKuQI+l3f/n7+iJO0lM0j9i4kha3NhtCrkBKPkBJTsBoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9qEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAA0luKdLunmwTWJboScoPP17CXwMdE3PGRWaMj6rQOYMHgbnAIca6+4OdrdN3s7ERr/sfBxPKHLn3U1DJ+W/pArhAoOGW/rF+cI/fupKk42+6nVTktAyHorWMnWRJHdsPdyPiQW5xOCa8halz6kEs2kP5c5wag2hr51hJAOHiknm3DLhI+EY5AqEGb4Kuo2YLwfOQcb1Ijbc+UzDniA54xOk70Di/4HEVRPYDoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIYTBtErMAAHaLkBqQ==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "co��B\\��=��JMX�:�\tc��øZɝ\u0007\u000b��",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423366,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423366,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2oQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv7jU+NILAfiEuEAXlH/LQUp0Ia7LsHIs13EOOtc7nG0YY6Fh0l4myP0D93nKESFXqj0JsQdsAaUGo9JLpVuALvbH2ERPdjj2Kf4CuEBfYa+bszk/aZbA1swjAn0KhDyR4xJDnEYv7stovELcZu8+afXaaIYaBgr/Z05QkHr49ntRYffBsCZpJS9tVaEJuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYAhhMG0SswAAFoXXcG",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAu5QEcQMdM/h5IS/q1GrxxTp8oIjTFSP74I8wSXW60b6xMSmd6+vwguBysUomlFcuJe8Y9WVmarH/i9rcSQqgD7kBKPkBJTsBoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9qEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhAF5R/y0FKdCGuy7ByLNdxDjrXO5xtGGOhYdJeJsj9A/d5yhEhV6o9CbEHbAGlBqPSS6VbgC72x9hET3Y49in+ArhAX2Gvm7M5P2mWwNbMIwJ9CoQ8keMSQ5xGL+7LaLxC3GbvPmn12miGGgYK/2dOUJB6+PZ7UWH3wbAmaSUvbVWhCbhI+EY5AqEGb4Kuo2YLwfOQcb1Ijbc+UzDniA54xOk70Di/4HEVRPYFoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIYTBtErMAABuCkktw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAu5QEcQMdM/h5IS/q1GrxxTp8oIjTFSP74I8wSXW60b6xMSmd6+vwguBysUomlFcuJe8Y9WVmarH/i9rcSQqgD7kBKPkBJTsBoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9qEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhAF5R/y0FKdCGuy7ByLNdxDjrXO5xtGGOhYdJeJsj9A/d5yhEhV6o9CbEHbAGlBqPSS6VbgC72x9hET3Y49in+ArhAX2Gvm7M5P2mWwNbMIwJ9CoQ8keMSQ5xGL+7LaLxC3GbvPmn12miGGgYK/2dOUJB6+PZ7UWH3wbAmaSUvbVWhCbhI+EY5AqEGb4Kuo2YLwfOQcb1Ijbc+UzDniA54xOk70Di/4HEVRPYFoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIYTBtErMAABuCkktw==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAu5QEcQMdM/h5IS/q1GrxxTp8oIjTFSP74I8wSXW60b6xMSmd6+vwguBysUomlFcuJe8Y9WVmarH/i9rcSQqgD7kBKPkBJTsBoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9qEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhAF5R/y0FKdCGuy7ByLNdxDjrXO5xtGGOhYdJeJsj9A/d5yhEhV6o9CbEHbAGlBqPSS6VbgC72x9hET3Y49in+ArhAX2Gvm7M5P2mWwNbMIwJ9CoQ8keMSQ5xGL+7LaLxC3GbvPmn12miGGgYK/2dOUJB6+PZ7UWH3wbAmaSUvbVWhCbhI+EY5AqEGb4Kuo2YLwfOQcb1Ijbc+UzDniA54xOk70Di/4HEVRPYFoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIYTBtErMAABuCkktw==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "Vӌ���\u000bz��\"\\$�3\u0011@\u0013�r,tY�2��-�U�",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1013,
        "message": "Tx already on-chain"
      }
    ],
    "message": "Rejected",
    "request": {
      "id": -576460752303423365,
      "jsonrpc": "2.0",
      "method": "channels.snapshot_solo",
      "params": {}
    }
  },
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423364,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423364,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2BqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrtwPSuCw=",
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
  "id": -576460752303423363,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAjLgnMnP2Pus5Auf24Xtngt7ROZvLlFnn8R0ehNjyYg/mSzlCBcPan7CdYYN7IK1YsfwnxNBsQC5IEL2QXPWIDuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dYURpa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423363,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAjLgnMnP2Pus5Auf24Xtngt7ROZvLlFnn8R0ehNjyYg/mSzlCBcPan7CdYYN7IK1YsfwnxNBsQC5IEL2QXPWIDuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dYURpa",
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
  "id": -576460752303423362,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAClOkLWeKb8hEumMCHUhCjO7L3nL1uGbBZXnaM08cLyHse035sZ6ChN6waEk74epPzVLIH78/gU4632sZ27dILuEAjLgnMnP2Pus5Auf24Xtngt7ROZvLlFnn8R0ehNjyYg/mSzlCBcPan7CdYYN7IK1YsfwnxNBsQC5IEL2QXPWIDuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dIax/U"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423362,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEAClOkLWeKb8hEumMCHUhCjO7L3nL1uGbBZXnaM08cLyHse035sZ6ChN6waEk74epPzVLIH78/gU4632sZ27dILuEAjLgnMnP2Pus5Auf24Xtngt7ROZvLlFnn8R0ehNjyYg/mSzlCBcPan7CdYYN7IK1YsfwnxNBsQC5IEL2QXPWIDuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dIax/U"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEAClOkLWeKb8hEumMCHUhCjO7L3nL1uGbBZXnaM08cLyHse035sZ6ChN6waEk74epPzVLIH78/gU4632sZ27dILuEAjLgnMnP2Pus5Auf24Xtngt7ROZvLlFnn8R0ehNjyYg/mSzlCBcPan7CdYYN7IK1YsfwnxNBsQC5IEL2QXPWIDuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dIax/U"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423361,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423361,
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
  "id": -576460752303423360,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423360,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAClOkLWeKb8hEumMCHUhCjO7L3nL1uGbBZXnaM08cLyHse035sZ6ChN6waEk74epPzVLIH78/gU4632sZ27dILuEAjLgnMnP2Pus5Auf24Xtngt7ROZvLlFnn8R0ehNjyYg/mSzlCBcPan7CdYYN7IK1YsfwnxNBsQC5IEL2QXPWIDuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dIax/U",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423359,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423359,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2B6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdlt2Y3U=",
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
  "id": -576460752303423358,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECnjmYGZ944zOH7TX8I0ICq4zN7o8SBBhzBoiEuSgcCEOTLnHPhdtlF/5kUtpAGlP9RlPFzCmfzzzTx14wAypcLuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaG2oSQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423358,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuECnjmYGZ944zOH7TX8I0ICq4zN7o8SBBhzBoiEuSgcCEOTLnHPhdtlF/5kUtpAGlP9RlPFzCmfzzzTx14wAypcLuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaG2oSQ",
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
  "id": -576460752303423357,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECYlrm651bXLTZWEIknQmnViniHC9h4GVaY7SkaA+8K8YQ4LaLwHkVSXRIKVZyB/Er4a0hxIM7yNu64Njh/ISAKuECnjmYGZ944zOH7TX8I0ICq4zN7o8SBBhzBoiEuSgcCEOTLnHPhdtlF/5kUtpAGlP9RlPFzCmfzzzTx14wAypcLuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZhoibj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423357,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuECYlrm651bXLTZWEIknQmnViniHC9h4GVaY7SkaA+8K8YQ4LaLwHkVSXRIKVZyB/Er4a0hxIM7yNu64Njh/ISAKuECnjmYGZ944zOH7TX8I0ICq4zN7o8SBBhzBoiEuSgcCEOTLnHPhdtlF/5kUtpAGlP9RlPFzCmfzzzTx14wAypcLuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZhoibj"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuECYlrm651bXLTZWEIknQmnViniHC9h4GVaY7SkaA+8K8YQ4LaLwHkVSXRIKVZyB/Er4a0hxIM7yNu64Njh/ISAKuECnjmYGZ944zOH7TX8I0ICq4zN7o8SBBhzBoiEuSgcCEOTLnHPhdtlF/5kUtpAGlP9RlPFzCmfzzzTx14wAypcLuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZhoibj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423356,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423356,
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
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECYlrm651bXLTZWEIknQmnViniHC9h4GVaY7SkaA+8K8YQ4LaLwHkVSXRIKVZyB/Er4a0hxIM7yNu64Njh/ISAKuECnjmYGZ944zOH7TX8I0ICq4zN7o8SBBhzBoiEuSgcCEOTLnHPhdtlF/5kUtpAGlP9RlPFzCmfzzzTx14wAypcLuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZhoibj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423354,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423354,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2oQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv7jU+NILAfiEuECYlrm651bXLTZWEIknQmnViniHC9h4GVaY7SkaA+8K8YQ4LaLwHkVSXRIKVZyB/Er4a0hxIM7yNu64Njh/ISAKuECnjmYGZ944zOH7TX8I0ICq4zN7o8SBBhzBoiEuSgcCEOTLnHPhdtlF/5kUtpAGlP9RlPFzCmfzzzTx14wAypcLuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYAhhMG0SswAAKWaP6A",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhA1ydItoEMx6ddNAUT77uw6W0ext2y9vwpY+U4vZSrmu4qXoAuD3itUH4Sz5hNmreEwLppmbl9QH1g05n7CuYiBbkBKPkBJTsBoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9qEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhAmJa5uudW1y02VhCJJ0Jp1Yp4hwvYeBlWmO0pGgPvCvGEOC2i8B5FUl0SClWcgfxK+GtIcSDO8jbuuDY4fyEgCrhAp45mBmfeOMzh+01/CNCAquMze6PEgQYcwaIhLkoHAhDky5xz4XbZRf+ZFLaQBpT/UZTxcwpn88808deMAMqXC7hI+EY5AqEGb4Kuo2YLwfOQcb1Ijbc+UzDniA54xOk70Di/4HEVRPYHoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIYTBtErMAAC1Wjfvg=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423353,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423353,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2CKBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt3Tpswc=",
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
  "id": -576460752303423352,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECFf6I33bUgu7BprGTCGNTyWsfnNhUQba+Wny+vog9hpvk5XrcnBvI6XGcxYTi5Ld+SCfSC8lJHTMUnDgcSTdILuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gigc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fXMYzM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423352,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuECFf6I33bUgu7BprGTCGNTyWsfnNhUQba+Wny+vog9hpvk5XrcnBvI6XGcxYTi5Ld+SCfSC8lJHTMUnDgcSTdILuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gigc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fXMYzM",
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
  "id": -576460752303423351,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECFf6I33bUgu7BprGTCGNTyWsfnNhUQba+Wny+vog9hpvk5XrcnBvI6XGcxYTi5Ld+SCfSC8lJHTMUnDgcSTdILuECxdvrdUbBupEbpnIFVPkHE+0WG07n8h4NelIQfevPj+81/ceEx0nWsUssCcUYwNWNeJfymaWDGwiSJwzvLYAYFuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gigc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cDLnMN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423351,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuECFf6I33bUgu7BprGTCGNTyWsfnNhUQba+Wny+vog9hpvk5XrcnBvI6XGcxYTi5Ld+SCfSC8lJHTMUnDgcSTdILuECxdvrdUbBupEbpnIFVPkHE+0WG07n8h4NelIQfevPj+81/ceEx0nWsUssCcUYwNWNeJfymaWDGwiSJwzvLYAYFuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gigc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cDLnMN"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuECFf6I33bUgu7BprGTCGNTyWsfnNhUQba+Wny+vog9hpvk5XrcnBvI6XGcxYTi5Ld+SCfSC8lJHTMUnDgcSTdILuECxdvrdUbBupEbpnIFVPkHE+0WG07n8h4NelIQfevPj+81/ceEx0nWsUssCcUYwNWNeJfymaWDGwiSJwzvLYAYFuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gigc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cDLnMN"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423350,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423350,
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
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECFf6I33bUgu7BprGTCGNTyWsfnNhUQba+Wny+vog9hpvk5XrcnBvI6XGcxYTi5Ld+SCfSC8lJHTMUnDgcSTdILuECxdvrdUbBupEbpnIFVPkHE+0WG07n8h4NelIQfevPj+81/ceEx0nWsUssCcUYwNWNeJfymaWDGwiSJwzvLYAYFuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gigc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cDLnMN",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423348,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423348,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm+CrqNmC8HzkHG9SI23PlMw54gOeMTpO9A4v+BxFUT2CaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdvkTu4g=",
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
  "id": -576460752303423347,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBJOIz1s8N/xnBosA6VzqsMUAo/I198pqd6LxO1Par0two1yb8SNaavv4xJ7tDnGlSlG7COchAgOGPupc8AwIAEuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gmgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbmFnbg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423347,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBJOIz1s8N/xnBosA6VzqsMUAo/I198pqd6LxO1Par0two1yb8SNaavv4xJ7tDnGlSlG7COchAgOGPupc8AwIAEuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gmgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbmFnbg",
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
  "id": -576460752303423346,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBJOIz1s8N/xnBosA6VzqsMUAo/I198pqd6LxO1Par0two1yb8SNaavv4xJ7tDnGlSlG7COchAgOGPupc8AwIAEuEDSLLf2/nQhjs9wcHS2Z29Qkg490tMOyxWStUAxcd4yArBVR2upuMZMevPOHns9nTQvhc+AyIaIkYBNxYwdW3wFuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gmgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnadIRgV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423346,
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEBJOIz1s8N/xnBosA6VzqsMUAo/I198pqd6LxO1Par0two1yb8SNaavv4xJ7tDnGlSlG7COchAgOGPupc8AwIAEuEDSLLf2/nQhjs9wcHS2Z29Qkg490tMOyxWStUAxcd4yArBVR2upuMZMevPOHns9nTQvhc+AyIaIkYBNxYwdW3wFuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gmgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnadIRgV"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "state": "tx_+NILAfiEuEBJOIz1s8N/xnBosA6VzqsMUAo/I198pqd6LxO1Par0two1yb8SNaavv4xJ7tDnGlSlG7COchAgOGPupc8AwIAEuEDSLLf2/nQhjs9wcHS2Z29Qkg490tMOyxWStUAxcd4yArBVR2upuMZMevPOHns9nTQvhc+AyIaIkYBNxYwdW3wFuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gmgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnadIRgV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423345,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423345,
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
  "id": -576460752303423344,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423344,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBJOIz1s8N/xnBosA6VzqsMUAo/I198pqd6LxO1Par0two1yb8SNaavv4xJ7tDnGlSlG7COchAgOGPupc8AwIAEuEDSLLf2/nQhjs9wcHS2Z29Qkg490tMOyxWStUAxcd4yArBVR2upuMZMevPOHns9nTQvhc+AyIaIkYBNxYwdW3wFuEj4RjkCoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9gmgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnadIRgV",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA1ydItoEMx6ddNAUT77uw6W0ext2y9vwpY+U4vZSrmu4qXoAuD3itUH4Sz5hNmreEwLppmbl9QH1g05n7CuYiBbkBKPkBJTsBoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9qEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhAmJa5uudW1y02VhCJJ0Jp1Yp4hwvYeBlWmO0pGgPvCvGEOC2i8B5FUl0SClWcgfxK+GtIcSDO8jbuuDY4fyEgCrhAp45mBmfeOMzh+01/CNCAquMze6PEgQYcwaIhLkoHAhDky5xz4XbZRf+ZFLaQBpT/UZTxcwpn88808deMAMqXC7hI+EY5AqEGb4Kuo2YLwfOQcb1Ijbc+UzDniA54xOk70Di/4HEVRPYHoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIYTBtErMAAC1Wjfvg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA1ydItoEMx6ddNAUT77uw6W0ext2y9vwpY+U4vZSrmu4qXoAuD3itUH4Sz5hNmreEwLppmbl9QH1g05n7CuYiBbkBKPkBJTsBoQZvgq6jZgvB85BxvUiNtz5TMOeIDnjE6TvQOL/gcRVE9qEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhAmJa5uudW1y02VhCJJ0Jp1Yp4hwvYeBlWmO0pGgPvCvGEOC2i8B5FUl0SClWcgfxK+GtIcSDO8jbuuDY4fyEgCrhAp45mBmfeOMzh+01/CNCAquMze6PEgQYcwaIhLkoHAhDky5xz4XbZRf+ZFLaQBpT/UZTxcwpn88808deMAMqXC7hI+EY5AqEGb4Kuo2YLwfOQcb1Ijbc+UzDniA54xOk70Di/4HEVRPYHoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIYTBtErMAAC1Wjfvg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "��@\u0003_�MI\u0005�c�#��h�J\u0000ՔH��\b�\u001b�\u0003�8",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423343,
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423343,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423342,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
    "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
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
  "channel_id": "ch_r7PMkZrPimBy1YWsqXjuXwGTRQY48xVDUxQvr3aZXgbKxgBeQ",
  "id": -576460752303423342,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
