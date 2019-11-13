
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_wrong_fsm_id%2F3286
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
      "fsm_id": "ba_4iIVT345ETGLVBdO0Jb6XCFqzw9lZgEaGyg3WSPAJrzAbK/8"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_wrong_fsm_id%2F3286
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
      "fsm_id": "ba_WKE6kSA65KocyoXdxHeObyviNRzaBCzm6I/RTk+vXPJu6vDE"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYW0v4FDA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423247,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEClyslNVete5CV8AYvt8wYIE7z7YG1Co2eBXEPcwymYgdWscvUpITVP+siLKWPtIwkwGVy22TzSf7Bw2y9UkLIBuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2FlCvgSY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423247,
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
      "signed_tx": "tx_+MsLAfhCuEClyslNVete5CV8AYvt8wYIE7z7YG1Co2eBXEPcwymYgdWscvUpITVP+siLKWPtIwkwGVy22TzSf7Bw2y9UkLIBuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2FlCvgSY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423246,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423246,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "message": {
        "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "message": {
        "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "id": -576460752303423245,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423245,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&host=localhost&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&host=localhost&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&existing_fsm_id=ba_pj1ffo9q0j5JXAZl&host=localhost&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&existing_fsm_id=ba_pj1ffo9q0j5JXAZl&host=localhost&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&existing_fsm_id=ba_7F%2FbL2HeGEYQhQq1hzYv19gp8SRimMUadK%2BHtox3WgEOkwDc&host=localhost&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&existing_fsm_id=ba_7F%2FbL2HeGEYQhQq1hzYv19gp8SRimMUadK%2BHtox3WgEOkwDc&host=localhost&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&existing_fsm_id=ba_WKE6kSA65KocyoXdxHeObyviNRzaBCzm6I%2FRTk%2BvXPJu6vDE&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=responder
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
      "fsm_id": "ba_5gHAsN7PTEDAdpcKoqIdw/w3q7qiWGXj/ArTAnM+1Pp3gXAh"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz&existing_fsm_id=ba_4iIVT345ETGLVBdO0Jb6XCFqzw9lZgEaGyg3WSPAJrzAbK%2F8&host=localhost&offchain_tx=tx_%2BQENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8%2B2BtQqNngVxD3MMpmIHVrHL1KSE1T%2FrIiylj7SMJMBlcttk80n%2BwcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec%2BQ32zDcyuEjmvIr6VThGWH8Q%2BIFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhYIC7tB&port=13180&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_2z25b7/QzaTeWz/otGSHIFAfSCsRjwW9b+MHA+earEEM0bAs"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+QENCwH4hLhApcrJTVXrXuQlfAGL7fMGCBO8+2BtQqNngVxD3MMpmIHVrHL1KSE1T/rIiylj7SMJMBlcttk80n+wcNsvVJCyAbhAp2ve63uMoHW2yWqkW43XBe0Ec+Q32zDcyuEjmvIr6VThGWH8Q+IFap47KhkQxyxotW6IqXAaobXmkVyKeIx4DLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhYIC7tB"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423244,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423244,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlV84875oHTC+RwetGp3+AXIcKa0jrvZvTSnm1k/DwGtAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt/Y+/LU=",
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
  "id": -576460752303423243,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECfNG7EJooiQLWG7ElpooN5jDRYFLT55mB1SPmgDie/EYDf3y8lc4ZV33iwqPjTy8Geafr2/UrFdbzvrDx9EvsJuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7c3kAhx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423243,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+JALAfhCuECfNG7EJooiQLWG7ElpooN5jDRYFLT55mB1SPmgDie/EYDf3y8lc4ZV33iwqPjTy8Geafr2/UrFdbzvrDx9EvsJuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7c3kAhx",
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
  "id": -576460752303423242,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBr6ivP8y3+XeENvbJvMBb6XW7y520ZAgLKS8nNeUni1tjpu4hA7T7tpEbM1YSa7V50hLVQeAC78eva9dRF2v8OuECfNG7EJooiQLWG7ElpooN5jDRYFLT55mB1SPmgDie/EYDf3y8lc4ZV33iwqPjTy8Geafr2/UrFdbzvrDx9EvsJuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cHSaDg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423242,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuEBr6ivP8y3+XeENvbJvMBb6XW7y520ZAgLKS8nNeUni1tjpu4hA7T7tpEbM1YSa7V50hLVQeAC78eva9dRF2v8OuECfNG7EJooiQLWG7ElpooN5jDRYFLT55mB1SPmgDie/EYDf3y8lc4ZV33iwqPjTy8Geafr2/UrFdbzvrDx9EvsJuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cHSaDg"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuEBr6ivP8y3+XeENvbJvMBb6XW7y520ZAgLKS8nNeUni1tjpu4hA7T7tpEbM1YSa7V50hLVQeAC78eva9dRF2v8OuECfNG7EJooiQLWG7ElpooN5jDRYFLT55mB1SPmgDie/EYDf3y8lc4ZV33iwqPjTy8Geafr2/UrFdbzvrDx9EvsJuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cHSaDg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423241,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423241,
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
  "id": -576460752303423240,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423240,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBr6ivP8y3+XeENvbJvMBb6XW7y520ZAgLKS8nNeUni1tjpu4hA7T7tpEbM1YSa7V50hLVQeAC78eva9dRF2v8OuECfNG7EJooiQLWG7ElpooN5jDRYFLT55mB1SPmgDie/EYDf3y8lc4ZV33iwqPjTy8Geafr2/UrFdbzvrDx9EvsJuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cHSaDg",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423239,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423239,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlV84875oHTC+RwetGp3+AXIcKa0jrvZvTSnm1k/DwGtA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjwl59M=",
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
  "id": -576460752303423238,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECkgq4Rz7W+V+vhAhPwG7yQM3dIvPV3dppquS8lPWIwX4neXqCLKXJeKz7EIZU9ZqFeAgT3d+LvZef260fsidsEuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna3TWU+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423238,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+JALAfhCuECkgq4Rz7W+V+vhAhPwG7yQM3dIvPV3dppquS8lPWIwX4neXqCLKXJeKz7EIZU9ZqFeAgT3d+LvZef260fsidsEuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna3TWU+",
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
  "id": -576460752303423237,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA7CthmhvgicACdTGfMgRT7xbWO2m38L5xLrPpLiNzYQCNt0BbvCvXdqwY7w9dKDcSPVigKHjmUFnpm9eglqxAFuECkgq4Rz7W+V+vhAhPwG7yQM3dIvPV3dppquS8lPWIwX4neXqCLKXJeKz7EIZU9ZqFeAgT3d+LvZef260fsidsEuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaN+F7B"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423237,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuEA7CthmhvgicACdTGfMgRT7xbWO2m38L5xLrPpLiNzYQCNt0BbvCvXdqwY7w9dKDcSPVigKHjmUFnpm9eglqxAFuECkgq4Rz7W+V+vhAhPwG7yQM3dIvPV3dppquS8lPWIwX4neXqCLKXJeKz7EIZU9ZqFeAgT3d+LvZef260fsidsEuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaN+F7B"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuEA7CthmhvgicACdTGfMgRT7xbWO2m38L5xLrPpLiNzYQCNt0BbvCvXdqwY7w9dKDcSPVigKHjmUFnpm9eglqxAFuECkgq4Rz7W+V+vhAhPwG7yQM3dIvPV3dppquS8lPWIwX4neXqCLKXJeKz7EIZU9ZqFeAgT3d+LvZef260fsidsEuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaN+F7B"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423236,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423236,
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
  "id": -576460752303423235,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423235,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA7CthmhvgicACdTGfMgRT7xbWO2m38L5xLrPpLiNzYQCNt0BbvCvXdqwY7w9dKDcSPVigKHjmUFnpm9eglqxAFuECkgq4Rz7W+V+vhAhPwG7yQM3dIvPV3dppquS8lPWIwX4neXqCLKXJeKz7EIZU9ZqFeAgT3d+LvZef260fsidsEuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaN+F7B",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423234,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423234,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlV84875oHTC+RwetGp3+AXIcKa0jrvZvTSnm1k/DwGtBKBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAuPtFAs=",
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
  "id": -576460752303423233,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECyxfUwm5+FbltNR+1Uy/lDY0Gv2JI0DePYNsUSYJFOd19SanxvmKD7pf8+edwa3aANwZ0VHZ+6DHiggzgA0iMNuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJLTVVB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423233,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+JALAfhCuECyxfUwm5+FbltNR+1Uy/lDY0Gv2JI0DePYNsUSYJFOd19SanxvmKD7pf8+edwa3aANwZ0VHZ+6DHiggzgA0iMNuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJLTVVB",
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
  "id": -576460752303423232,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECyxfUwm5+FbltNR+1Uy/lDY0Gv2JI0DePYNsUSYJFOd19SanxvmKD7pf8+edwa3aANwZ0VHZ+6DHiggzgA0iMNuEC4eBjoPyr4Z5yuz0jhjlnK8Y+D9ikzCDEB8jYNIPhM4VJSlpMWtHKroKyPrFiDkRt6zpQ3S+K/XkxIM7q4TK0EuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKKXAcf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423232,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuECyxfUwm5+FbltNR+1Uy/lDY0Gv2JI0DePYNsUSYJFOd19SanxvmKD7pf8+edwa3aANwZ0VHZ+6DHiggzgA0iMNuEC4eBjoPyr4Z5yuz0jhjlnK8Y+D9ikzCDEB8jYNIPhM4VJSlpMWtHKroKyPrFiDkRt6zpQ3S+K/XkxIM7q4TK0EuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKKXAcf"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuECyxfUwm5+FbltNR+1Uy/lDY0Gv2JI0DePYNsUSYJFOd19SanxvmKD7pf8+edwa3aANwZ0VHZ+6DHiggzgA0iMNuEC4eBjoPyr4Z5yuz0jhjlnK8Y+D9ikzCDEB8jYNIPhM4VJSlpMWtHKroKyPrFiDkRt6zpQ3S+K/XkxIM7q4TK0EuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKKXAcf"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423231,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423231,
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
  "id": -576460752303423230,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423230,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECyxfUwm5+FbltNR+1Uy/lDY0Gv2JI0DePYNsUSYJFOd19SanxvmKD7pf8+edwa3aANwZ0VHZ+6DHiggzgA0iMNuEC4eBjoPyr4Z5yuz0jhjlnK8Y+D9ikzCDEB8jYNIPhM4VJSlpMWtHKroKyPrFiDkRt6zpQ3S+K/XkxIM7q4TK0EuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKKXAcf",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423229,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423229,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlV84875oHTC+RwetGp3+AXIcKa0jrvZvTSnm1k/DwGtBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdvPiaSw=",
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
  "id": -576460752303423228,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAjOZGQxG5Q4XMeB+VvNcRf5WBJyaDgCDJvciwcoGmvNGErCWWjKl3el9WyxhQWbdMzVZZe2VlqTIvJJWO3xZwBuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbpkWKI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423228,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAjOZGQxG5Q4XMeB+VvNcRf5WBJyaDgCDJvciwcoGmvNGErCWWjKl3el9WyxhQWbdMzVZZe2VlqTIvJJWO3xZwBuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbpkWKI",
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
  "id": -576460752303423227,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAjOZGQxG5Q4XMeB+VvNcRf5WBJyaDgCDJvciwcoGmvNGErCWWjKl3el9WyxhQWbdMzVZZe2VlqTIvJJWO3xZwBuEDqJSnaExKS3DDfHH1ontiB2RaBAvueEBI/dPwDPoE6QNpHrXo7KjqZV6gOmaEfN6cUQ7f4FZ2LjPWD6pYlCR0IuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYS2uq7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423227,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuEAjOZGQxG5Q4XMeB+VvNcRf5WBJyaDgCDJvciwcoGmvNGErCWWjKl3el9WyxhQWbdMzVZZe2VlqTIvJJWO3xZwBuEDqJSnaExKS3DDfHH1ontiB2RaBAvueEBI/dPwDPoE6QNpHrXo7KjqZV6gOmaEfN6cUQ7f4FZ2LjPWD6pYlCR0IuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYS2uq7"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuEAjOZGQxG5Q4XMeB+VvNcRf5WBJyaDgCDJvciwcoGmvNGErCWWjKl3el9WyxhQWbdMzVZZe2VlqTIvJJWO3xZwBuEDqJSnaExKS3DDfHH1ontiB2RaBAvueEBI/dPwDPoE6QNpHrXo7KjqZV6gOmaEfN6cUQ7f4FZ2LjPWD6pYlCR0IuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYS2uq7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423226,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423226,
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
  "id": -576460752303423225,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423225,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAjOZGQxG5Q4XMeB+VvNcRf5WBJyaDgCDJvciwcoGmvNGErCWWjKl3el9WyxhQWbdMzVZZe2VlqTIvJJWO3xZwBuEDqJSnaExKS3DDfHH1ontiB2RaBAvueEBI/dPwDPoE6QNpHrXo7KjqZV6gOmaEfN6cUQ7f4FZ2LjPWD6pYlCR0IuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYS2uq7",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423224,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423224,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlV84875oHTC+RwetGp3+AXIcKa0jrvZvTSnm1k/DwGtBqBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAgOMT44=",
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
  "id": -576460752303423223,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB6Zdd8fGfU6VWaSYV6JGsJ8uTtGhPZi/S/vnV3gLTpaPQYE4qh+xt7PceJbeVM6B463xXMgMHWQQ2LoikGA/MEuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKLiTYO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423223,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB6Zdd8fGfU6VWaSYV6JGsJ8uTtGhPZi/S/vnV3gLTpaPQYE4qh+xt7PceJbeVM6B463xXMgMHWQQ2LoikGA/MEuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKLiTYO",
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
  "id": -576460752303423222,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB6Zdd8fGfU6VWaSYV6JGsJ8uTtGhPZi/S/vnV3gLTpaPQYE4qh+xt7PceJbeVM6B463xXMgMHWQQ2LoikGA/MEuECFgSHKRYSW0OZAPeKuvR3jLddNOLgu0wBYs9/stVz60oYlDmT4K9dsCB27DgmEUx9m8XTRAPfTzD+xUunomoIPuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAK+hyRl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423222,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuEB6Zdd8fGfU6VWaSYV6JGsJ8uTtGhPZi/S/vnV3gLTpaPQYE4qh+xt7PceJbeVM6B463xXMgMHWQQ2LoikGA/MEuECFgSHKRYSW0OZAPeKuvR3jLddNOLgu0wBYs9/stVz60oYlDmT4K9dsCB27DgmEUx9m8XTRAPfTzD+xUunomoIPuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAK+hyRl"
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
    "data": {
      "state": "tx_+NILAfiEuEB6Zdd8fGfU6VWaSYV6JGsJ8uTtGhPZi/S/vnV3gLTpaPQYE4qh+xt7PceJbeVM6B463xXMgMHWQQ2LoikGA/MEuECFgSHKRYSW0OZAPeKuvR3jLddNOLgu0wBYs9/stVz60oYlDmT4K9dsCB27DgmEUx9m8XTRAPfTzD+xUunomoIPuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAK+hyRl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423221,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423221,
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
  "id": -576460752303423220,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423220,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB6Zdd8fGfU6VWaSYV6JGsJ8uTtGhPZi/S/vnV3gLTpaPQYE4qh+xt7PceJbeVM6B463xXMgMHWQQ2LoikGA/MEuECFgSHKRYSW0OZAPeKuvR3jLddNOLgu0wBYs9/stVz60oYlDmT4K9dsCB27DgmEUx9m8XTRAPfTzD+xUunomoIPuEj4RjkCoQZVfOPO+aB0wvkcHrRqd/gFyHCmtI672b00p5tZPw8BrQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAK+hyRl",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423219,
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423219,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423218,
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
    "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
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
  "channel_id": "ch_eeg122XXnuzovSLy7HrhWHoNx7x6AzCzhVrD9X735HMUTn2bz",
  "id": -576460752303423218,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
