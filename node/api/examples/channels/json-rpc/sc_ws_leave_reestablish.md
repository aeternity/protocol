
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish%2F3279
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
      "fsm_id": "ba_Mwnd0t5nU7NYUWqLBYohEmEazuK91R4phhYckrutLPM5BaLi"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish%2F3279
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
      "fsm_id": "ba_bu8MUltLSzpGSbjKPp+gOJJyRoH6C9Bnw49g6X2w+ZaSxiH9"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYVfB3f9g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423277,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDYOCUxCZ/sCFPjW5cGcEIlg7fMOUxyhlnWRkhh8uMrfwVTClKU29SgSA/0SAqI0Us/TO9z3CHcJskt7vl0ozIJuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2FcNtlAQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423277,
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
      "signed_tx": "tx_+MsLAfhCuEDYOCUxCZ/sCFPjW5cGcEIlg7fMOUxyhlnWRkhh8uMrfwVTClKU29SgSA/0SAqI0Us/TO9z3CHcJskt7vl0ozIJuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2FcNtlAQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423276,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423276,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "message": {
        "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "message": {
        "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "id": -576460752303423275,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423275,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w&existing_fsm_id=ba_bu8MUltLSzpGSbjKPp%2BgOJJyRoH6C9Bnw49g6X2w%2BZaSxiH9&offchain_tx=tx_%2BQENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5%2BSa8HeItD%2FBVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhWkUKxn&port=13180&protocol=json-rpc&role=responder
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
      "fsm_id": "ba_q0uPHp5yh0IH3v8ez2XLgBGC2uTVJcq4JgYykjx5yxQSpvLC"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w&existing_fsm_id=ba_Mwnd0t5nU7NYUWqLBYohEmEazuK91R4phhYckrutLPM5BaLi&host=localhost&offchain_tx=tx_%2BQENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5%2BSa8HeItD%2FBVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD%2BIEyAaEBv%2FPUIGzYM0BS8xcMEvgU5vVHR1p%2FpL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl%2F1Vz6PZNXjTCdhWkUKxn&port=13180&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_MxC7JNUSp+P93xzhtc+utlVifydiUxHNBlczZpj3aAW1lzGJ"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+QENCwH4hLhA2DglMQmf7AhT41uXBnBCJYO3zDlMcoZZ1kZIYfLjK38FUwpSlNvUoEgP9EgKiNFLP0zvc9wh3CbJLe75dKMyCbhA4VNFxVnm5+Sa8HeItD/BVyKURVK2BS0zgCerhJ3dCxaZ42AE1OBwDQlljd8pC1Md0APIX0JcL4hOir9N0aYLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhWkUKxn"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423274,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423274,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkxsmeBKv0M36aCpsCc9VfmQs40oYE2hK2eB3vFKIdh/AqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt0lEBg8=",
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
  "id": -576460752303423273,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAXKKmgWK6thKw9HG5/25CmsEjfLwhbco+tUQ6th4lqo/rGAMC8Ym3z70c7m4PGjlazdQkEbM/LpWKrSZMf7pYMuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dwFoM9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423273,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAXKKmgWK6thKw9HG5/25CmsEjfLwhbco+tUQ6th4lqo/rGAMC8Ym3z70c7m4PGjlazdQkEbM/LpWKrSZMf7pYMuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dwFoM9",
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
  "id": -576460752303423272,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAXKKmgWK6thKw9HG5/25CmsEjfLwhbco+tUQ6th4lqo/rGAMC8Ym3z70c7m4PGjlazdQkEbM/LpWKrSZMf7pYMuEArsy3t9S9tYDEYET+WtATsxHocNm2ExG0lLP7Lg75MTHZ5ZG9raTvInrS6FGnHb8JRK8y8iBXy68C0Q/87SmAAuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dDKDZe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423272,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuEAXKKmgWK6thKw9HG5/25CmsEjfLwhbco+tUQ6th4lqo/rGAMC8Ym3z70c7m4PGjlazdQkEbM/LpWKrSZMf7pYMuEArsy3t9S9tYDEYET+WtATsxHocNm2ExG0lLP7Lg75MTHZ5ZG9raTvInrS6FGnHb8JRK8y8iBXy68C0Q/87SmAAuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dDKDZe"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuEAXKKmgWK6thKw9HG5/25CmsEjfLwhbco+tUQ6th4lqo/rGAMC8Ym3z70c7m4PGjlazdQkEbM/LpWKrSZMf7pYMuEArsy3t9S9tYDEYET+WtATsxHocNm2ExG0lLP7Lg75MTHZ5ZG9raTvInrS6FGnHb8JRK8y8iBXy68C0Q/87SmAAuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dDKDZe"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423271,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423271,
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
  "id": -576460752303423270,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423270,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAXKKmgWK6thKw9HG5/25CmsEjfLwhbco+tUQ6th4lqo/rGAMC8Ym3z70c7m4PGjlazdQkEbM/LpWKrSZMf7pYMuEArsy3t9S9tYDEYET+WtATsxHocNm2ExG0lLP7Lg75MTHZ5ZG9raTvInrS6FGnHb8JRK8y8iBXy68C0Q/87SmAAuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dDKDZe",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423269,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423269,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkxsmeBKv0M36aCpsCc9VfmQs40oYE2hK2eB3vFKIdh/A6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCds7ZzG0=",
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
  "id": -576460752303423268,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDHiB+4v6amU8AlUpjYiu7yiz+QAhShIaiqb8oZO7NKPgUYkVGrvBlquizUnm27WpsS4Yi4LxR1s9xuvwzXQEkCuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZX4HpI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423268,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDHiB+4v6amU8AlUpjYiu7yiz+QAhShIaiqb8oZO7NKPgUYkVGrvBlquizUnm27WpsS4Yi4LxR1s9xuvwzXQEkCuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZX4HpI",
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
  "id": -576460752303423267,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC/LMCNacy5fiNAbrUPFjQcqEQgFiQJSO6Ql2NkkI6yL+/H7/ewazR5/2/Lgqe9FvDWW8t3TG7TKlsVnWt9CR4MuEDHiB+4v6amU8AlUpjYiu7yiz+QAhShIaiqb8oZO7NKPgUYkVGrvBlquizUnm27WpsS4Yi4LxR1s9xuvwzXQEkCuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZO1cP9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423267,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuEC/LMCNacy5fiNAbrUPFjQcqEQgFiQJSO6Ql2NkkI6yL+/H7/ewazR5/2/Lgqe9FvDWW8t3TG7TKlsVnWt9CR4MuEDHiB+4v6amU8AlUpjYiu7yiz+QAhShIaiqb8oZO7NKPgUYkVGrvBlquizUnm27WpsS4Yi4LxR1s9xuvwzXQEkCuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZO1cP9"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuEC/LMCNacy5fiNAbrUPFjQcqEQgFiQJSO6Ql2NkkI6yL+/H7/ewazR5/2/Lgqe9FvDWW8t3TG7TKlsVnWt9CR4MuEDHiB+4v6amU8AlUpjYiu7yiz+QAhShIaiqb8oZO7NKPgUYkVGrvBlquizUnm27WpsS4Yi4LxR1s9xuvwzXQEkCuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZO1cP9"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423266,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423266,
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
  "id": -576460752303423265,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423265,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC/LMCNacy5fiNAbrUPFjQcqEQgFiQJSO6Ql2NkkI6yL+/H7/ewazR5/2/Lgqe9FvDWW8t3TG7TKlsVnWt9CR4MuEDHiB+4v6amU8AlUpjYiu7yiz+QAhShIaiqb8oZO7NKPgUYkVGrvBlquizUnm27WpsS4Yi4LxR1s9xuvwzXQEkCuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZO1cP9",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423264,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423264,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkxsmeBKv0M36aCpsCc9VfmQs40oYE2hK2eB3vFKIdh/BKBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAgUtubk=",
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
  "id": -576460752303423263,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECrklce8ZsrWXMOn2dHo/U8aVg/xyYWhVpu5xnDd0uN/Ek1sTan0FKDd/04D1DX0nVhpzZmKj4skzHYgvl9XboGuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJHLCKZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423263,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+JALAfhCuECrklce8ZsrWXMOn2dHo/U8aVg/xyYWhVpu5xnDd0uN/Ek1sTan0FKDd/04D1DX0nVhpzZmKj4skzHYgvl9XboGuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJHLCKZ",
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
  "id": -576460752303423262,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECF0NyjAewlg2LmKMC/RfxNQMClBolRWcFlOidwwxDsbIr/gqyjfG4SlzemxjGLWP1sTZzoL7BFQBgOBUwmS0QCuECrklce8ZsrWXMOn2dHo/U8aVg/xyYWhVpu5xnDd0uN/Ek1sTan0FKDd/04D1DX0nVhpzZmKj4skzHYgvl9XboGuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI6gOCZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423262,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuECF0NyjAewlg2LmKMC/RfxNQMClBolRWcFlOidwwxDsbIr/gqyjfG4SlzemxjGLWP1sTZzoL7BFQBgOBUwmS0QCuECrklce8ZsrWXMOn2dHo/U8aVg/xyYWhVpu5xnDd0uN/Ek1sTan0FKDd/04D1DX0nVhpzZmKj4skzHYgvl9XboGuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI6gOCZ"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuECF0NyjAewlg2LmKMC/RfxNQMClBolRWcFlOidwwxDsbIr/gqyjfG4SlzemxjGLWP1sTZzoL7BFQBgOBUwmS0QCuECrklce8ZsrWXMOn2dHo/U8aVg/xyYWhVpu5xnDd0uN/Ek1sTan0FKDd/04D1DX0nVhpzZmKj4skzHYgvl9XboGuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI6gOCZ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423261,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423261,
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
  "id": -576460752303423260,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423260,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECF0NyjAewlg2LmKMC/RfxNQMClBolRWcFlOidwwxDsbIr/gqyjfG4SlzemxjGLWP1sTZzoL7BFQBgOBUwmS0QCuECrklce8ZsrWXMOn2dHo/U8aVg/xyYWhVpu5xnDd0uN/Ek1sTan0FKDd/04D1DX0nVhpzZmKj4skzHYgvl9XboGuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI6gOCZ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423259,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423259,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkxsmeBKv0M36aCpsCc9VfmQs40oYE2hK2eB3vFKIdh/BaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdtkVVy8=",
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
  "id": -576460752303423258,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB967cgGX0ei2ZJ09hS/tvawGKS6aISJ8J/URaFcCX3TI42iii4Yt6R2P8SatBIbtSrGpQDd94pyoWtoSbZVUsPuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbBe2pv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423258,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB967cgGX0ei2ZJ09hS/tvawGKS6aISJ8J/URaFcCX3TI42iii4Yt6R2P8SatBIbtSrGpQDd94pyoWtoSbZVUsPuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbBe2pv",
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
  "id": -576460752303423257,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBfgJ1rwzCbzdV2JyKs9Rn2YzwETsHR1ni2l2opJtmpLgXow46Drj+rHyJtbtPc9gIqMYFurfANJV6qLpB35fwAuEB967cgGX0ei2ZJ09hS/tvawGKS6aISJ8J/URaFcCX3TI42iii4Yt6R2P8SatBIbtSrGpQDd94pyoWtoSbZVUsPuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaL3mfi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423257,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuEBfgJ1rwzCbzdV2JyKs9Rn2YzwETsHR1ni2l2opJtmpLgXow46Drj+rHyJtbtPc9gIqMYFurfANJV6qLpB35fwAuEB967cgGX0ei2ZJ09hS/tvawGKS6aISJ8J/URaFcCX3TI42iii4Yt6R2P8SatBIbtSrGpQDd94pyoWtoSbZVUsPuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaL3mfi"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuEBfgJ1rwzCbzdV2JyKs9Rn2YzwETsHR1ni2l2opJtmpLgXow46Drj+rHyJtbtPc9gIqMYFurfANJV6qLpB35fwAuEB967cgGX0ei2ZJ09hS/tvawGKS6aISJ8J/URaFcCX3TI42iii4Yt6R2P8SatBIbtSrGpQDd94pyoWtoSbZVUsPuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaL3mfi"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423256,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423256,
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
  "id": -576460752303423255,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423255,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBfgJ1rwzCbzdV2JyKs9Rn2YzwETsHR1ni2l2opJtmpLgXow46Drj+rHyJtbtPc9gIqMYFurfANJV6qLpB35fwAuEB967cgGX0ei2ZJ09hS/tvawGKS6aISJ8J/URaFcCX3TI42iii4Yt6R2P8SatBIbtSrGpQDd94pyoWtoSbZVUsPuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaL3mfi",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423254,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423254,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkxsmeBKv0M36aCpsCc9VfmQs40oYE2hK2eB3vFKIdh/BqBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAmhjOT0=",
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
  "id": -576460752303423253,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECC8cdqLsLtu1Sd3U831D6eI5+9rjth2zwaZDqEi3iagNeDrAm9FGNv6bnCmTc+R+EO7gq8SoH7urawK29NKTANuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJpit3m"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423253,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "signed_tx": "tx_+JALAfhCuECC8cdqLsLtu1Sd3U831D6eI5+9rjth2zwaZDqEi3iagNeDrAm9FGNv6bnCmTc+R+EO7gq8SoH7urawK29NKTANuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJpit3m",
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
  "id": -576460752303423252,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAIa9gZgeHPqhRhMSSPkiXsn41GmQN2v3uDtDmJo8sBtx9bQ8OKfFhRe6h4aTSR/n0+SOpco5Yx9g8NPXefKVYPuECC8cdqLsLtu1Sd3U831D6eI5+9rjth2zwaZDqEi3iagNeDrAm9FGNv6bnCmTc+R+EO7gq8SoH7urawK29NKTANuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI1oyI8"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423252,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuEAIa9gZgeHPqhRhMSSPkiXsn41GmQN2v3uDtDmJo8sBtx9bQ8OKfFhRe6h4aTSR/n0+SOpco5Yx9g8NPXefKVYPuECC8cdqLsLtu1Sd3U831D6eI5+9rjth2zwaZDqEi3iagNeDrAm9FGNv6bnCmTc+R+EO7gq8SoH7urawK29NKTANuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI1oyI8"
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
    "data": {
      "state": "tx_+NILAfiEuEAIa9gZgeHPqhRhMSSPkiXsn41GmQN2v3uDtDmJo8sBtx9bQ8OKfFhRe6h4aTSR/n0+SOpco5Yx9g8NPXefKVYPuECC8cdqLsLtu1Sd3U831D6eI5+9rjth2zwaZDqEi3iagNeDrAm9FGNv6bnCmTc+R+EO7gq8SoH7urawK29NKTANuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI1oyI8"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423251,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423251,
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
  "id": -576460752303423250,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423250,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAIa9gZgeHPqhRhMSSPkiXsn41GmQN2v3uDtDmJo8sBtx9bQ8OKfFhRe6h4aTSR/n0+SOpco5Yx9g8NPXefKVYPuECC8cdqLsLtu1Sd3U831D6eI5+9rjth2zwaZDqEi3iagNeDrAm9FGNv6bnCmTc+R+EO7gq8SoH7urawK29NKTANuEj4RjkCoQZMbJngSr9DN+mgqbAnPVX5kLONKGBNoStngd7xSiHYfwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI1oyI8",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423249,
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423249,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423248,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
  "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
  "id": -576460752303423248,
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
    "channel_id": "ch_af9wjwiDqHc83GrZ3GATNoqw9gCdtuLxQu27YMJtLSJ2Yzh7w",
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
