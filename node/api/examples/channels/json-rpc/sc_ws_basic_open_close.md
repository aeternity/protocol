
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
      "fsm_id": "ba_aJo4IelXkci+vLd3WIyoV65J7upKPZFk5fDP4RvRABejm9jj"
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
      "fsm_id": "ba_NULzOZN778SYZIJl5IM8jh2gx0NhYH8QbN/Y2aVx2rzTd1zj"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYDf8Lzdg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423456,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECraWLYsxtdfHpwWaJ+vggDOj4Tnt3a3cdrsN2uL9d6mDBXPeQKqsJv8u7cQPiSstTE0G+N6+PE0mlFDulyVS8HuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2A84wr9c="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423456,
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
      "signed_tx": "tx_+MsLAfhCuECraWLYsxtdfHpwWaJ+vggDOj4Tnt3a3cdrsN2uL9d6mDBXPeQKqsJv8u7cQPiSstTE0G+N6+PE0mlFDulyVS8HuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2A84wr9c=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423455,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAq2li2LMbXXx6cFmifr4IAzo+E57d2t3Ha7Ddri/XepgwVz3kCqrCb/Lu3ED4krLUxNBvjevjxNJpRQ7pclUvB7hAvTOjGRiolHTN7i3JSuEq9F8epb2sMP/pbUqThgkygDCovz17dOJphqA8wZYnAe47L1sCcJfR4k6Q6/JpcUg2C7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgNXAy5V"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423455,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAq2li2LMbXXx6cFmifr4IAzo+E57d2t3Ha7Ddri/XepgwVz3kCqrCb/Lu3ED4krLUxNBvjevjxNJpRQ7pclUvB7hAvTOjGRiolHTN7i3JSuEq9F8epb2sMP/pbUqThgkygDCovz17dOJphqA8wZYnAe47L1sCcJfR4k6Q6/JpcUg2C7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgNXAy5V",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAq2li2LMbXXx6cFmifr4IAzo+E57d2t3Ha7Ddri/XepgwVz3kCqrCb/Lu3ED4krLUxNBvjevjxNJpRQ7pclUvB7hAvTOjGRiolHTN7i3JSuEq9F8epb2sMP/pbUqThgkygDCovz17dOJphqA8wZYnAe47L1sCcJfR4k6Q6/JpcUg2C7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgNXAy5V",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAq2li2LMbXXx6cFmifr4IAzo+E57d2t3Ha7Ddri/XepgwVz3kCqrCb/Lu3ED4krLUxNBvjevjxNJpRQ7pclUvB7hAvTOjGRiolHTN7i3JSuEq9F8epb2sMP/pbUqThgkygDCovz17dOJphqA8wZYnAe47L1sCcJfR4k6Q6/JpcUg2C7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgNXAy5V",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAq2li2LMbXXx6cFmifr4IAzo+E57d2t3Ha7Ddri/XepgwVz3kCqrCb/Lu3ED4krLUxNBvjevjxNJpRQ7pclUvB7hAvTOjGRiolHTN7i3JSuEq9F8epb2sMP/pbUqThgkygDCovz17dOJphqA8wZYnAe47L1sCcJfR4k6Q6/JpcUg2C7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgNXAy5V",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "message": {
        "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "message": {
        "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "id": -576460752303423454,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423454,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+QENCwH4hLhAq2li2LMbXXx6cFmifr4IAzo+E57d2t3Ha7Ddri/XepgwVz3kCqrCb/Lu3ED4krLUxNBvjevjxNJpRQ7pclUvB7hAvTOjGRiolHTN7i3JSuEq9F8epb2sMP/pbUqThgkygDCovz17dOJphqA8wZYnAe47L1sCcJfR4k6Q6/JpcUg2C7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgNXAy5V"
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+QENCwH4hLhAq2li2LMbXXx6cFmifr4IAzo+E57d2t3Ha7Ddri/XepgwVz3kCqrCb/Lu3ED4krLUxNBvjevjxNJpRQ7pclUvB7hAvTOjGRiolHTN7i3JSuEq9F8epb2sMP/pbUqThgkygDCovz17dOJphqA8wZYnAe47L1sCcJfR4k6Q6/JpcUg2C7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgNXAy5V"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423453,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423453,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnWOVcyKhIckECKjvq26AZXb1q/PE1Z4jeXNruoUV9HsAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt7fHi4U=",
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
  "id": -576460752303423452,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDn77IMFx01XNmTSIM233ZBGdU6CrjBq/2v3oqJqG/8n0oxhnhIk9pKlBL8HVBVrUgcNo5w0Yn/v5TNEyuMcrYAuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eUBPhJ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423452,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDn77IMFx01XNmTSIM233ZBGdU6CrjBq/2v3oqJqG/8n0oxhnhIk9pKlBL8HVBVrUgcNo5w0Yn/v5TNEyuMcrYAuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eUBPhJ",
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
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDn77IMFx01XNmTSIM233ZBGdU6CrjBq/2v3oqJqG/8n0oxhnhIk9pKlBL8HVBVrUgcNo5w0Yn/v5TNEyuMcrYAuED76OhqV5AqRWEj4imA38sugHrGE34CWghSYVNl8ivi6bJ/rp+abxsDVyXU8TAip/wZaowv0ZegLHrwX1RrX3gKuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fvBG9M"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423451,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuEDn77IMFx01XNmTSIM233ZBGdU6CrjBq/2v3oqJqG/8n0oxhnhIk9pKlBL8HVBVrUgcNo5w0Yn/v5TNEyuMcrYAuED76OhqV5AqRWEj4imA38sugHrGE34CWghSYVNl8ivi6bJ/rp+abxsDVyXU8TAip/wZaowv0ZegLHrwX1RrX3gKuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fvBG9M"
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuEDn77IMFx01XNmTSIM233ZBGdU6CrjBq/2v3oqJqG/8n0oxhnhIk9pKlBL8HVBVrUgcNo5w0Yn/v5TNEyuMcrYAuED76OhqV5AqRWEj4imA38sugHrGE34CWghSYVNl8ivi6bJ/rp+abxsDVyXU8TAip/wZaowv0ZegLHrwX1RrX3gKuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fvBG9M"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423450,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423450,
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
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDn77IMFx01XNmTSIM233ZBGdU6CrjBq/2v3oqJqG/8n0oxhnhIk9pKlBL8HVBVrUgcNo5w0Yn/v5TNEyuMcrYAuED76OhqV5AqRWEj4imA38sugHrGE34CWghSYVNl8ivi6bJ/rp+abxsDVyXU8TAip/wZaowv0ZegLHrwX1RrX3gKuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fvBG9M",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423448,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423448,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnWOVcyKhIckECKjvq26AZXb1q/PE1Z4jeXNruoUV9HsA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdvgBey8=",
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
  "id": -576460752303423447,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBzecbKyS7Kr0OEiJvZlLKEnVuYgwJA47tk2MGwP+J1tf17i7wQlRMRhk7wVBbBCqSNVC9ZF8r9vpoZJC7M5oEJuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYsw1My"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423447,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBzecbKyS7Kr0OEiJvZlLKEnVuYgwJA47tk2MGwP+J1tf17i7wQlRMRhk7wVBbBCqSNVC9ZF8r9vpoZJC7M5oEJuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYsw1My",
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
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBzecbKyS7Kr0OEiJvZlLKEnVuYgwJA47tk2MGwP+J1tf17i7wQlRMRhk7wVBbBCqSNVC9ZF8r9vpoZJC7M5oEJuECidBAMCfx0rmHaIZON1KxHlyXRjmWHU3ut1SJs+cfbRPeZnQSMKzSHPJ6zWNaiNt4cBVryYzRlzGRuevbgqPwDuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb6cJi/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423446,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuEBzecbKyS7Kr0OEiJvZlLKEnVuYgwJA47tk2MGwP+J1tf17i7wQlRMRhk7wVBbBCqSNVC9ZF8r9vpoZJC7M5oEJuECidBAMCfx0rmHaIZON1KxHlyXRjmWHU3ut1SJs+cfbRPeZnQSMKzSHPJ6zWNaiNt4cBVryYzRlzGRuevbgqPwDuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb6cJi/"
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuEBzecbKyS7Kr0OEiJvZlLKEnVuYgwJA47tk2MGwP+J1tf17i7wQlRMRhk7wVBbBCqSNVC9ZF8r9vpoZJC7M5oEJuECidBAMCfx0rmHaIZON1KxHlyXRjmWHU3ut1SJs+cfbRPeZnQSMKzSHPJ6zWNaiNt4cBVryYzRlzGRuevbgqPwDuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb6cJi/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423445,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423445,
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
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBzecbKyS7Kr0OEiJvZlLKEnVuYgwJA47tk2MGwP+J1tf17i7wQlRMRhk7wVBbBCqSNVC9ZF8r9vpoZJC7M5oEJuECidBAMCfx0rmHaIZON1KxHlyXRjmWHU3ut1SJs+cfbRPeZnQSMKzSHPJ6zWNaiNt4cBVryYzRlzGRuevbgqPwDuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb6cJi/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423443,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423443,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnWOVcyKhIckECKjvq26AZXb1q/PE1Z4jeXNruoUV9HsBKBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAk1zIn8=",
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
  "id": -576460752303423442,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECk6pET8vig9rKSNAaIse8eiaexvULXGfJkNNydikTt42YGV6t/X4gdtXmVU3DBGWV8WK/Ydo3K1WwbazpWmJcFuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7ASgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALi8BHX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423442,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+JALAfhCuECk6pET8vig9rKSNAaIse8eiaexvULXGfJkNNydikTt42YGV6t/X4gdtXmVU3DBGWV8WK/Ydo3K1WwbazpWmJcFuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7ASgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALi8BHX",
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
  "id": -576460752303423441,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBh7EXJRy9nH54wknHuKjFo6VlxFQEi22lFiuH/ofCK9gPsFU9G5DbYWbxZus9LXO/LVXFyVXQE5DGssuEtissNuECk6pET8vig9rKSNAaIse8eiaexvULXGfJkNNydikTt42YGV6t/X4gdtXmVU3DBGWV8WK/Ydo3K1WwbazpWmJcFuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7ASgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI7AghS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423441,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuEBh7EXJRy9nH54wknHuKjFo6VlxFQEi22lFiuH/ofCK9gPsFU9G5DbYWbxZus9LXO/LVXFyVXQE5DGssuEtissNuECk6pET8vig9rKSNAaIse8eiaexvULXGfJkNNydikTt42YGV6t/X4gdtXmVU3DBGWV8WK/Ydo3K1WwbazpWmJcFuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7ASgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI7AghS"
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuEBh7EXJRy9nH54wknHuKjFo6VlxFQEi22lFiuH/ofCK9gPsFU9G5DbYWbxZus9LXO/LVXFyVXQE5DGssuEtissNuECk6pET8vig9rKSNAaIse8eiaexvULXGfJkNNydikTt42YGV6t/X4gdtXmVU3DBGWV8WK/Ydo3K1WwbazpWmJcFuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7ASgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI7AghS"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423440,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423440,
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
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBh7EXJRy9nH54wknHuKjFo6VlxFQEi22lFiuH/ofCK9gPsFU9G5DbYWbxZus9LXO/LVXFyVXQE5DGssuEtissNuECk6pET8vig9rKSNAaIse8eiaexvULXGfJkNNydikTt42YGV6t/X4gdtXmVU3DBGWV8WK/Ydo3K1WwbazpWmJcFuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7ASgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAI7AghS",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423438,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423438,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnWOVcyKhIckECKjvq26AZXb1q/PE1Z4jeXNruoUV9HsBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkCtzco=",
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
  "id": -576460752303423437,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECJLdm+sBMBU6qOscQeKFewDDqm75d/mQ4sV4LSrLN6zBFWsLE+JIVluJ4yYY+O0E9cJzuAHJ0uF4ZLxzNfC1MCuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZ/9m7O"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423437,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+JALAfhCuECJLdm+sBMBU6qOscQeKFewDDqm75d/mQ4sV4LSrLN6zBFWsLE+JIVluJ4yYY+O0E9cJzuAHJ0uF4ZLxzNfC1MCuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZ/9m7O",
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
  "id": -576460752303423436,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECJLdm+sBMBU6qOscQeKFewDDqm75d/mQ4sV4LSrLN6zBFWsLE+JIVluJ4yYY+O0E9cJzuAHJ0uF4ZLxzNfC1MCuEDev3oOa5jLTW+ocp9FbabzzH4Y5TFOe/Y+xAWk/+qmx3zrA4sf2RJ7eTCAr3AAQzRgWxgJO4M3eLll8xNGHf0NuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb+G2LA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423436,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuECJLdm+sBMBU6qOscQeKFewDDqm75d/mQ4sV4LSrLN6zBFWsLE+JIVluJ4yYY+O0E9cJzuAHJ0uF4ZLxzNfC1MCuEDev3oOa5jLTW+ocp9FbabzzH4Y5TFOe/Y+xAWk/+qmx3zrA4sf2RJ7eTCAr3AAQzRgWxgJO4M3eLll8xNGHf0NuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb+G2LA"
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuECJLdm+sBMBU6qOscQeKFewDDqm75d/mQ4sV4LSrLN6zBFWsLE+JIVluJ4yYY+O0E9cJzuAHJ0uF4ZLxzNfC1MCuEDev3oOa5jLTW+ocp9FbabzzH4Y5TFOe/Y+xAWk/+qmx3zrA4sf2RJ7eTCAr3AAQzRgWxgJO4M3eLll8xNGHf0NuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb+G2LA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423435,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423435,
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
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECJLdm+sBMBU6qOscQeKFewDDqm75d/mQ4sV4LSrLN6zBFWsLE+JIVluJ4yYY+O0E9cJzuAHJ0uF4ZLxzNfC1MCuEDev3oOa5jLTW+ocp9FbabzzH4Y5TFOe/Y+xAWk/+qmx3zrA4sf2RJ7eTCAr3AAQzRgWxgJO4M3eLll8xNGHf0NuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnb+G2LA",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423433,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423433,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnWOVcyKhIckECKjvq26AZXb1q/PE1Z4jeXNruoUV9HsBqBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUApgL61c=",
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
  "id": -576460752303423432,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB7+P88cD29PM3LTkng0YLR5u9/Zwh4liNJXERCr8h/TYU6ObSpijxUCS8S8cskT36N4+UHYft0ctWEkoI7F9wGuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIZUl5P"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423432,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB7+P88cD29PM3LTkng0YLR5u9/Zwh4liNJXERCr8h/TYU6ObSpijxUCS8S8cskT36N4+UHYft0ctWEkoI7F9wGuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIZUl5P",
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
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA/M3n7D2CQDKWfYZkhyGRo/HylAKTXNPKXv5YPi3e2giT6wj3YAVR9xc6uIeP1RqUMzMWxjQp/gkstnTq16toHuEB7+P88cD29PM3LTkng0YLR5u9/Zwh4liNJXERCr8h/TYU6ObSpijxUCS8S8cskT36N4+UHYft0ctWEkoI7F9wGuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIJdVWg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423431,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuEA/M3n7D2CQDKWfYZkhyGRo/HylAKTXNPKXv5YPi3e2giT6wj3YAVR9xc6uIeP1RqUMzMWxjQp/gkstnTq16toHuEB7+P88cD29PM3LTkng0YLR5u9/Zwh4liNJXERCr8h/TYU6ObSpijxUCS8S8cskT36N4+UHYft0ctWEkoI7F9wGuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIJdVWg"
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
    "data": {
      "state": "tx_+NILAfiEuEA/M3n7D2CQDKWfYZkhyGRo/HylAKTXNPKXv5YPi3e2giT6wj3YAVR9xc6uIeP1RqUMzMWxjQp/gkstnTq16toHuEB7+P88cD29PM3LTkng0YLR5u9/Zwh4liNJXERCr8h/TYU6ObSpijxUCS8S8cskT36N4+UHYft0ctWEkoI7F9wGuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIJdVWg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423430,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423430,
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
  "id": -576460752303423429,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423429,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA/M3n7D2CQDKWfYZkhyGRo/HylAKTXNPKXv5YPi3e2giT6wj3YAVR9xc6uIeP1RqUMzMWxjQp/gkstnTq16toHuEB7+P88cD29PM3LTkng0YLR5u9/Zwh4liNJXERCr8h/TYU6ObSpijxUCS8S8cskT36N4+UHYft0ctWEkoI7F9wGuEj4RjkCoQZ1jlXMioSHJBAio76tugGV29avzxNWeI3lza7qFFfR7AagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIJdVWg",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423428,
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423428,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423427,
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
    "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
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
  "channel_id": "ch_tmozNfJQAFW5cp51xz6FJuCyJZ8x2P3tsA4Y4gCDXPmvUmeBb",
  "id": -576460752303423427,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
